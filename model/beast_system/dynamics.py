"""Linear pillar-capacity dynamics x_{t+1} = B x_t + D z_t + eps_t (source Section 5.3).

x_t = (F_t, P_t, J_t, I^cap_t, C_t, W_t) in pillar order. The source warns that stability
cannot be inferred from positive links alone (negative feedback, substitution, saturation,
legitimacy loss) and uses dominant eigenvalues of a local linearization as the language of
persistence. Every deviation of x from its steady state decays iff the spectral radius
rho(B) < 1; if rho(B) >= 1 SOME deviation (e.g. along a dominant eigenvector) does not decay,
although a deviation inside a stable subspace still may.

The second half implements coalition conversion dynamics (Part VII spec, item 4): a
coalition's control shares y in [0,1]^6 evolve by T(y) = (1 - delta) y + (1 - y) (K y).
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

import numpy as np

from .necessity import Graph, dependency_graph
from .pillars import M, Pillar


def _square(B: np.ndarray) -> np.ndarray:
    arr = np.asarray(B, dtype=float)
    if arr.shape != (M, M):
        raise ValueError(f"B must be {M}x{M}, got {arr.shape}")
    if not np.all(np.isfinite(arr)):
        raise ValueError("B must be finite")
    return arr


def spectral_radius(B: np.ndarray) -> float:
    """rho(B) = max |lambda| over eigenvalues of B."""
    return float(np.max(np.abs(np.linalg.eigvals(_square(B)))))


def some_deviation_persists(B: np.ndarray) -> bool:
    """True iff rho(B) >= 1: x = 0 is not globally asymptotically stable for x -> B x.

    Then some deviation does not decay; it does not follow that EVERY deviation persists.
    """
    return spectral_radius(B) >= 1.0


def dependency_matrix(graph: Graph, weight: float, self_weight: float = 0.0) -> np.ndarray:
    """B with B[dependent, provider] = weight for each edge, and self_weight on the diagonal.

    Row = pillar at t+1, column = pillar at t, matching x_{t+1} = B x_t.
    """
    B = np.eye(M) * float(self_weight)
    for provider, dependents in graph.items():
        for dep in dependents:
            B[dep.position, provider.position] = float(weight)
    return B


def simulate(
    B: np.ndarray,
    x0: np.ndarray,
    steps: int,
    D: np.ndarray | None = None,
    z: np.ndarray | None = None,
    noise_sd: float = 0.0,
    seed: int | None = None,
) -> np.ndarray:
    """Iterate x_{t+1} = B x_t + D z_t + eps_t; returns an array of shape (steps + 1, 6).

    ``z`` has shape (steps, k) and ``D`` shape (6, k); eps_t ~ N(0, noise_sd^2 I).
    """
    B = _square(B)
    x = np.asarray(x0, dtype=float)
    if x.shape != (M,):
        raise ValueError(f"x0 must have shape ({M},)")
    if steps < 0:
        raise ValueError("steps must be non-negative")
    if (D is None) != (z is None):
        raise ValueError("pass both D and z, or neither")
    if D is not None and z is not None:
        D = np.asarray(D, dtype=float)
        z = np.asarray(z, dtype=float)
        if D.ndim != 2 or D.shape[0] != M or z.shape != (steps, D.shape[1]):
            raise ValueError("D must be (6, k) and z must be (steps, k)")
    if not np.all(np.isfinite(x)):
        raise ValueError("x0 must be finite")
    if D is not None and z is not None and not (np.all(np.isfinite(D)) and np.all(np.isfinite(z))):
        raise ValueError("D and z must be finite")
    noise_sd = float(noise_sd)
    if not np.isfinite(noise_sd) or noise_sd < 0.0:
        raise ValueError("noise_sd must be finite and non-negative")
    rng = np.random.default_rng(seed)
    path = np.empty((steps + 1, M))
    path[0] = x
    for t in range(steps):
        x = B @ x
        if D is not None and z is not None:
            x = x + D @ z[t]
        if noise_sd > 0.0:
            x = x + rng.normal(0.0, noise_sd, size=M)
        path[t + 1] = x
    return path


@dataclass(frozen=True)
class FeedbackExample:
    """Two matrices with the same positive links; only the feedback one has negative entries."""

    B_positive: np.ndarray
    B_feedback: np.ndarray
    rho_positive: float
    rho_feedback: float

    @property
    def same_positive_links(self) -> bool:
        return bool(np.array_equal(self.B_positive > 0, self.B_feedback > 0))


#: Negative feedback entries (provider, dependent) -> weight: coercion erodes legitimacy and
#: depresses productive effort (source Section 5.3, 'legitimacy loss'). Illustrative values.
NEGATIVE_FEEDBACK: Mapping[tuple[Pillar, Pillar], float] = {
    (Pillar.C, Pillar.I): -0.5,
    (Pillar.C, Pillar.W): -0.4,
}


def negative_feedback_example(
    weight: float = 0.25,
    self_weight: float = 0.6,
    feedback: Mapping[tuple[Pillar, Pillar], float] = NEGATIVE_FEEDBACK,
) -> FeedbackExample:
    """Positive dependency links do not guarantee persistence (source Section 5.3).

    With every arc of the underlying digraph of D* at ``weight`` and ``self_weight`` on the
    diagonal, rho > 1. Adding negative feedback on entries that carry no positive link leaves every
    positive link unchanged yet pushes rho below 1, so deviations decay.
    """
    B_pos = dependency_matrix(dependency_graph(), weight, self_weight)
    B_fb = B_pos.copy()
    for (provider, dependent), w in feedback.items():
        if w >= 0.0:
            raise ValueError("feedback entries must be negative")
        if B_pos[dependent.position, provider.position] != 0.0:
            raise ValueError("feedback must not overwrite a positive link")
        B_fb[dependent.position, provider.position] = w
    return FeedbackExample(B_pos, B_fb, spectral_radius(B_pos), spectral_radius(B_fb))


# Coalition conversion dynamics (Part VII spec, item 4) -------------------------------------


def _unit_vector(v: np.ndarray, name: str) -> np.ndarray:
    arr = np.asarray(v, dtype=float)
    if arr.shape != (M,):
        raise ValueError(f"{name} must have shape ({M},)")
    if not np.all(np.isfinite(arr)) or arr.min() < 0.0 or arr.max() > 1.0:
        raise ValueError(f"{name} entries must lie in [0, 1]")
    return arr


def validate_conversion_matrix(K: np.ndarray, atol: float = 1e-12) -> np.ndarray:
    """Check K >= 0, zero diagonal, row sums <= 1 (so T maps [0,1]^6 into itself)."""
    arr = _square(K)
    if arr.min() < 0.0:
        raise ValueError("K must be non-negative")
    if np.any(np.diag(arr) != 0.0):
        raise ValueError("K must have a zero diagonal")
    if arr.sum(axis=1).max() > 1.0 + atol:
        raise ValueError("K row sums must be <= 1")
    return arr


def conversion_matrix(eta: np.ndarray, Q: np.ndarray) -> np.ndarray:
    """K[n, m] = eta[n, m] (1 - Q_n): conversion of control in m into control in n.

    Contestability of the receiving pillar n damps conversion into it.
    """
    e = _square(eta)
    q = _unit_vector(Q, "Q")
    if e.min() < 0.0 or np.any(np.diag(e) != 0.0):
        raise ValueError("eta must be non-negative with zero diagonal")
    return validate_conversion_matrix(e * (1.0 - q)[:, None])


def conversion_step(y: np.ndarray, delta: np.ndarray, K: np.ndarray) -> np.ndarray:
    """T(y) = (1 - delta) y + (1 - y) (K y). Maps [0,1]^6 into [0,1]^6."""
    y = _unit_vector(y, "y")
    d = _unit_vector(delta, "delta")
    K = validate_conversion_matrix(K)
    out = (1.0 - d) * y + (1.0 - y) * (K @ y)
    return np.clip(out, 0.0, 1.0)  # guard against last-ulp rounding only


def comparison_matrix(delta: np.ndarray, K: np.ndarray) -> np.ndarray:
    """A = diag(1 - delta) + K, with 0 <= T(y) <= A y componentwise."""
    return np.diag(1.0 - _unit_vector(delta, "delta")) + validate_conversion_matrix(K)


def simulate_conversion(
    y0: np.ndarray, delta: np.ndarray, K: np.ndarray, steps: int
) -> np.ndarray:
    """Iterate y_{t+1} = T(y_t); returns shape (steps + 1, 6)."""
    if steps < 0:
        raise ValueError("steps must be non-negative")
    path = np.empty((steps + 1, M))
    path[0] = _unit_vector(y0, "y0")
    for t in range(steps):
        path[t + 1] = conversion_step(path[t], delta, K)
    return path


def coalition_integration_share(y: np.ndarray) -> float:
    """(1/15) sum_{m<n} min(y_m, y_n): the coalition's contribution to the integration statistic."""
    y = _unit_vector(y, "y")
    return float(sum(min(y[i], y[j]) for i in range(M) for j in range(i + 1, M)) / 15.0)


def _is_irreducible(K: np.ndarray) -> bool:
    reach = (np.eye(M) + (K > 0)).astype(float)
    return bool(np.all(np.linalg.matrix_power(reach, M - 1) > 0))


_REFINE_STEPS = 200


@dataclass(frozen=True)
class Foothold:
    """Foothold bound: v . y_t >= min(v . y_0, (1 - max delta)(rho - 1) / (2c)) for all t.

    v is the left Perron vector of A (normalized to sum 1), c = v_max kappa / v_min^2 and
    kappa the largest column sum of K. Proof sketch: v . T(y) = rho v . y - sum_n v_n y_n (K y)_n
    >= rho s - c s^2 with s = v . y, and v . T(y) >= (1 - max delta) s.
    """

    rho: float
    v: np.ndarray
    c: float  # may be inf for near-reducible K; ``bound`` is computed without forming c
    bound: float


def foothold_bound(y0: np.ndarray, delta: np.ndarray, K: np.ndarray) -> Foothold:
    """Lower bound on v . y_t when K is irreducible, max delta < 1 and rho(A) > 1."""
    y0 = _unit_vector(y0, "y0")
    d = _unit_vector(delta, "delta")
    K = validate_conversion_matrix(K)
    if not _is_irreducible(K):
        raise ValueError("the foothold bound needs an irreducible K")
    if d.max() >= 1.0:
        raise ValueError("the foothold bound needs max delta < 1")
    A = comparison_matrix(d, K)
    vals, vecs = np.linalg.eig(A.T)
    k = int(np.argmax(vals.real))
    rho = float(vals[k].real)
    if rho <= 1.0:
        raise ValueError("the foothold bound needs rho(A) > 1")
    v = np.abs(vecs[:, k].real)
    v = v / v.max()
    # Refine with v <- v A / rho. Every step sums non-negative terms, so entries many orders
    # of magnitude below max(v) regain relative accuracy lost in the dense eigensolver.
    for _ in range(_REFINE_STEPS):
        v = (A * v[:, None]).sum(axis=0) / rho
        v = v / v.max()
    if v.min() <= 0.0:
        raise ValueError("left Perron vector underflows; the bound is not representable")
    v = v / v.sum()
    kappa = float(K.sum(axis=0).max())
    v_min, v_max = float(v.min()), float(v.max())
    c = v_max * kappa / v_min**2 if v_min > 0.0 else float("inf")
    # (1 - max delta)(rho - 1) / (2c), ordered so no intermediate overflows or underflows early.
    margin = (1.0 - float(d.max())) * (rho - 1.0) / (2.0 * kappa) * (v_min / v_max) * v_min
    bound = min(float((v * y0).sum()), margin)
    return Foothold(rho=rho, v=v, c=float(c), bound=bound)
