"""Concentration, contestability and integration indices (source Section 5; notation.md).

Definitions implemented here:
  s^m_i >= 0, sum_i s^m_i = 1                              control shares
  H_m = sum_i (s^m_i)^2                                     Herfindahl-Hirschman concentration
  Q_m in [0, 1]                                             contestability
  U = sum_m w_m H_m (1 - Q_m), w_m >= 0, sum_m w_m = 1      unaccountable concentration
  C_mn in [0, 1]                                            cross-pillar integration
  I = 2 / (M (M - 1)) sum_{m<n} C_mn, M = 6 (15 pairs)      integration statistic (math cal I)

The source calls U 'an illustrative index, not a validated measurement instrument' and
requires preregistered weights plus sensitivity analysis; see ``weight_sensitivity``.
"""

from __future__ import annotations

import math
from collections.abc import Mapping, Sequence
from dataclasses import dataclass

import numpy as np

from .pillars import M, PAIRS, PILLARS, Pillar

SHARE_ATOL = 1e-9
WEIGHT_ATOL = 1e-9

ShareLike = Mapping[str, float] | Sequence[float] | np.ndarray


def validate_unit_interval(value: float, name: str) -> float:
    """Return ``value`` as float after checking it is finite and in [0, 1]."""
    if isinstance(value, bool) or not isinstance(value, (int, float, np.integer, np.floating)):
        raise TypeError(f"{name} must be a real number, got {type(value).__name__}")
    v = float(value)
    if not math.isfinite(v) or v < 0.0 or v > 1.0:
        raise ValueError(f"{name} must lie in [0, 1], got {value!r}")
    return v


def _share_array(shares: ShareLike) -> np.ndarray:
    values = list(shares.values()) if isinstance(shares, Mapping) else shares
    arr = np.asarray(values, dtype=float).ravel()
    if arr.size == 0:
        raise ValueError("shares must be non-empty")
    if not np.all(np.isfinite(arr)):
        raise ValueError("shares must be finite")
    if arr.min() < 0.0:
        raise ValueError("shares must be non-negative")
    return arr


def control_shares(raw: Mapping[str, float]) -> dict[str, float]:
    """Normalize non-negative control weights to shares s^m_i summing to 1 (notation.md)."""
    arr = _share_array(raw)
    scale = float(arr.max())
    if scale <= 0.0:
        raise ValueError("at least one control weight must be positive")
    scaled = arr / scale  # in [0, 1], so the sum cannot overflow
    total = float(scaled.sum())
    return {k: float(v) / total for k, v in zip(raw, scaled)}


def validate_shares(shares: ShareLike, atol: float = SHARE_ATOL) -> np.ndarray:
    """Check s^m_i >= 0 and sum_i s^m_i = 1 (notation.md 'Control share').

    Returns the shares renormalized to sum exactly 1, so rounding within ``atol`` cannot push
    H outside [1/n, 1].
    """
    arr = _share_array(shares)
    total = float(arr.sum())
    if abs(total - 1.0) > atol:
        raise ValueError(f"shares must sum to 1, got {total:.12g}")
    return arr / total


def hhi(shares: ShareLike) -> float:
    """H_m = sum_i (s^m_i)^2 (source Eq. for H_{m,t}). Lies in [1/n, 1]."""
    arr = validate_shares(shares)
    return float(np.dot(arr, arr))


def normalized_hhi(shares: ShareLike) -> float:
    """H* = (H - 1/n) / (1 - 1/n), for comparing polities with different n (KB VII.3 (v)).

    Not in the source. Defined as 1 for n = 1 (a monopoly by construction).
    """
    arr = validate_shares(shares)
    n = arr.size
    if n == 1:
        return 1.0
    return float((np.dot(arr, arr) - 1.0 / n) / (1.0 - 1.0 / n))


def validate_weights(weights: Mapping[Pillar, float] | None) -> dict[Pillar, float]:
    """Check the U weights: one per pillar, w_m >= 0, sum_m w_m = 1 (source Eq. U_t).

    ``None`` gives equal weights 1/M.
    """
    if weights is None:
        return {m: 1.0 / M for m in PILLARS}
    if set(weights) != set(PILLARS):
        raise ValueError("weights must give exactly one value per pillar")
    w = {m: float(weights[m]) for m in PILLARS}
    if any(not math.isfinite(v) or v < 0.0 for v in w.values()):
        raise ValueError("weights must be finite and non-negative")
    total = sum(w.values())
    if abs(total - 1.0) > WEIGHT_ATOL:
        raise ValueError(f"weights must sum to 1, got {total:.12g}")
    return {m: v / total for m, v in w.items()}


def _per_pillar(values: Mapping[Pillar, float], name: str) -> dict[Pillar, float]:
    if set(values) != set(PILLARS):
        raise ValueError(f"{name} must give exactly one value per pillar")
    return {m: validate_unit_interval(values[m], f"{name}[{m.name}]") for m in PILLARS}


def unaccountable_concentration(
    H: Mapping[Pillar, float],
    Q: Mapping[Pillar, float],
    weights: Mapping[Pillar, float] | None = None,
) -> float:
    """U = sum_m w_m H_m (1 - Q_m) (source Eq. U_t). Lies in [0, 1].

    U = 0 iff Q_m = 1 for every m with w_m > 0, because H_m >= 1/n > 0 (KB VII.3 (ii)).
    """
    h = _per_pillar(H, "H")
    if any(v == 0.0 for v in h.values()):
        raise ValueError("H_m >= 1/n > 0 for any valid share vector; got H_m = 0")
    q = _per_pillar(Q, "Q")
    w = validate_weights(weights)
    u = sum(w[m] * h[m] * (1.0 - q[m]) for m in PILLARS)
    return float(min(max(u, 0.0), 1.0))  # guard against last-ulp rounding


def validate_integration_matrix(C: np.ndarray, atol: float = 1e-12) -> np.ndarray:
    """Check C is 6x6, finite, symmetric, with off-diagonal C_mn in [0, 1].

    The diagonal is unused by the integration statistic; by convention it is set to 1.
    """
    arr = np.array(C, dtype=float)
    if arr.shape != (M, M):
        raise ValueError(f"integration matrix must be {M}x{M}, got {arr.shape}")
    if not np.all(np.isfinite(arr)):
        raise ValueError("integration matrix must be finite")
    if not np.allclose(arr, arr.T, atol=atol, rtol=0.0):
        raise ValueError("integration matrix must be symmetric (C_mn = C_nm)")
    off = arr[~np.eye(M, dtype=bool)]
    if off.min() < 0.0 or off.max() > 1.0:
        raise ValueError("off-diagonal C_mn must lie in [0, 1]")
    arr = (arr + arr.T) / 2.0  # exact symmetry, so both triangles agree
    np.fill_diagonal(arr, 1.0)
    return arr


def integration_matrix(
    pairs: Mapping[tuple[Pillar, Pillar], float], default: float = 0.0
) -> np.ndarray:
    """Build a symmetric C from {(m, n): C_mn}; unspecified pairs take ``default``."""
    validate_unit_interval(default, "default")
    arr = np.full((M, M), float(default))
    seen: set[frozenset[Pillar]] = set()
    for (m, n), value in pairs.items():
        if m == n:
            raise ValueError(f"pair ({m.name}, {n.name}) is not a cross-pillar pair")
        key = frozenset((m, n))
        if key in seen:
            raise ValueError(f"pair {m.name}{n.name} given twice")
        seen.add(key)
        v = validate_unit_interval(value, f"C[{m.name}{n.name}]")
        arr[m.position, n.position] = arr[n.position, m.position] = v
    np.fill_diagonal(arr, 1.0)
    return arr


def integration_statistic(C: np.ndarray) -> float:
    """I = 2 / (M (M - 1)) sum_{m<n} C_mn with M = 6, i.e. the mean over 15 pairs (source Eq. I_t)."""
    arr = validate_integration_matrix(C)
    total = sum(arr[m.position, n.position] for m, n in PAIRS)
    return float(2.0 / (M * (M - 1)) * total)


def integration_degrees(C: np.ndarray) -> dict[Pillar, float]:
    """deg_m = sum_{n != m} C_mn, so that I = (sum_m deg_m) / 30 (Part VII spec, item 5)."""
    arr = validate_integration_matrix(C)
    return {m: float(arr[m.position].sum() - arr[m.position, m.position]) for m in PILLARS}


def hub_bound(k: int) -> float:
    """Upper bound on I when every C_mn with both m, n outside a hub set of k pillars is 0.

    Only pairs touching the hub can be non-zero: k(6 - k) + k(k - 1)/2 of the 15 pairs.
    k = 1 gives 1/3, k = 2 gives 0.6, k = 3 gives 0.8.
    """
    if isinstance(k, bool) or not isinstance(k, (int, np.integer)):
        raise TypeError("k must be an integer")
    if not 0 <= k <= M:
        raise ValueError(f"k must lie in 0..{M}")
    return (k * (M - k) + k * (k - 1) / 2) / 15.0


def coalition_overlap(kappa: Mapping[str, Mapping[Pillar, float]]) -> np.ndarray:
    """C_mn = max over candidate coalitions S of min(kappa_m(S), kappa_n(S)) (Part II eq. overlap).

    ``kappa[S][m]`` in [0, 1] is coalition S's control of pillar m; pillars missing for S
    count as 0. Candidate coalitions may overlap and kappa need not be additive. The result
    lies in [0, 1] and is weakly increasing in every kappa_m(S).
    """
    arr = np.eye(M)
    if not kappa:
        return arr
    table: list[dict[Pillar, float]] = []
    for name, row in kappa.items():
        if any(not isinstance(m, Pillar) for m in row):
            raise TypeError(f"kappa[{name!r}] keys must be Pillars")
        table.append({m: validate_unit_interval(row.get(m, 0.0), f"kappa[{name!r}][{m.name}]")
                      for m in PILLARS})
    for m, n in PAIRS:
        v = max(min(row[m], row[n]) for row in table)
        arr[m.position, n.position] = arr[n.position, m.position] = v
    return arr


def coalition_integration(
    shares: Mapping[Pillar, Mapping[str, float]],
    coalition_of: Mapping[str, str] | None = None,
) -> np.ndarray:
    """Additive special case of ``coalition_overlap`` for a partition of actors into coalitions.

    kappa_m(S) = s^m(S), the summed (normalized) share of S's members in pillar m. The source
    describes C_mn only verbally ('the same coalition commands appointments, budgets,
    sanctions or agenda in both m and n'); KB VII.3 (iv) asks Part VII to define it. Actors
    absent from ``coalition_of`` form singleton coalitions.
    """
    coalition_of = dict(coalition_of or {})
    kappa: dict[str, dict[Pillar, float]] = {}
    for m in PILLARS:
        if m not in shares:
            raise ValueError(f"shares missing pillar {m.name}")
        actors = list(shares[m])
        normalized = validate_shares(shares[m])
        for actor, v in zip(actors, normalized):
            row = kappa.setdefault(coalition_of.get(actor, actor), {})
            row[m] = min(row.get(m, 0.0) + float(v), 1.0)
    return coalition_overlap(kappa)


def clique_lower_bound(c: float, k: int) -> float:
    """If one coalition has kappa_m(S) >= c in each of k pillars, then I >= c k (k - 1) / 30.

    Those k pillars form k(k - 1)/2 pairs with C_mn >= c (Part VII addendum item 8).
    """
    c = validate_unit_interval(c, "c")
    if isinstance(k, bool) or not isinstance(k, (int, np.integer)) or not 0 <= k <= M:
        raise ValueError(f"k must be an integer in 0..{M}")
    return c * k * (k - 1) / 30.0


def star_upper_bound(C: np.ndarray, hub: Pillar) -> float:
    """Bound (1/3) max C_mn for a pure star: every positive C_mn involves ``hub``.

    Raises if the matrix is not a star around ``hub``.
    """
    arr = validate_integration_matrix(C)
    for m, n in PAIRS:
        if hub not in (m, n) and arr[m.position, n.position] > 0.0:
            raise ValueError(f"C_{m.name}{n.name} > 0 does not involve hub {hub.name}")
    off = arr[~np.eye(M, dtype=bool)]
    return float(off.max()) / 3.0


@dataclass(frozen=True)
class WeightSensitivity:
    """Result of ``weight_sensitivity``. ``draws`` holds U for each sampled weight vector."""

    baseline: float
    vertex_min: float
    vertex_max: float
    draws: np.ndarray

    @property
    def quantiles(self) -> tuple[float, float]:
        """5th and 95th percentile of U across draws."""
        lo, hi = np.quantile(self.draws, [0.05, 0.95])
        return float(lo), float(hi)

    def fraction_at_least(self, u_star: float) -> float:
        """Share of weight draws with U >= u_star (robustness of a threshold call)."""
        validate_unit_interval(u_star, "u_star")
        return float(np.mean(self.draws >= u_star))


def weight_sensitivity(
    H: Mapping[Pillar, float],
    Q: Mapping[Pillar, float],
    weights: Mapping[Pillar, float] | None = None,
    n_draws: int = 2000,
    seed: int = 0,
) -> WeightSensitivity:
    """Sensitivity of U to the weights w (source: 'weights preregistered; sensitivity analysis').

    U is linear in w, so over the whole weight simplex its exact range is
    [min_m H_m (1 - Q_m), max_m H_m (1 - Q_m)] (attained at the vertices). ``draws`` samples
    w uniformly on the simplex (Dirichlet(1, ..., 1)) to show the typical spread.
    """
    if n_draws < 1:
        raise ValueError("n_draws must be positive")
    baseline = unaccountable_concentration(H, Q, weights)
    h = _per_pillar(H, "H")
    q = _per_pillar(Q, "Q")
    terms = np.array([h[m] * (1.0 - q[m]) for m in PILLARS])
    rng = np.random.default_rng(seed)
    w = rng.dirichlet(np.ones(M), size=n_draws)
    return WeightSensitivity(
        baseline=baseline,
        vertex_min=float(terms.min()),
        vertex_max=float(terms.max()),
        draws=(w * terms).sum(axis=1),
    )
