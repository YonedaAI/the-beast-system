"""Representation theorem and minimality (Part VII Thm 7.4, Prop 7.5).

A FormalizedStructure F = (V, rho, A^m, s^m, Q, omega, kappa, L, D) is the formal object; the
profile map ``represent`` sends a coded record of a governance system G to F_G. The theorem
tested here: F_G lies in the formalized class iff Proposition A holds for G (six pillars
realized, D0 present, interdependent). No uniqueness claim is made.

Minimality: ``drop`` deletes a pillar and ``merge`` fuses two; fixtures in the tests show
pairs of systems that become indistinguishable after coarsening although a preserved
property (A.holds, U, C_mn, I) differs.

Pillar labels are strings (``Pillar.name``) so that coarsened structures, whose label set is
no longer M, use the same type.
"""

from __future__ import annotations

import itertools
import math
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field

import numpy as np

from .capture import CaptureLink, CaptureThresholds, Polity
from .indices import hhi, validate_unit_interval, validate_weights
from .necessity import (
    D0_KEYS,
    D_STAR_KEYS,
    GovernanceSystem,
    generate_dependencies,
    is_strongly_connected,
    realized_form,
    role_map,
)
from .pillars import PILLARS, Pillar

Label = str
LabelArc = tuple[frozenset[Label], Label]
M_LABELS: tuple[Label, ...] = tuple(m.name for m in PILLARS)
D0_LABELS: frozenset[LabelArc] = frozenset(
    (frozenset(t.name for t in tail), head.name) for tail, head in D0_KEYS
)
_ATOL = 1e-9
_ROUND = 12


@dataclass(frozen=True)
class FormalizedStructure:
    """F = (V, rho, A^m, s^m, Q, omega, kappa, L, D) over pillar labels ``pillars``.

    ``kappa`` is keyed by coalition membership (a frozenset of actors), so it transports under
    an actor bijection. ``links`` holds (source, target, pillar label) for capture links
    meeting all three conditions; ``arcs`` holds hyperarcs (tail labels, head label).
    """

    actors: tuple[str, ...]
    pillars: tuple[Label, ...]
    roles: Mapping[str, frozenset[Label]]
    layers: Mapping[Label, np.ndarray] = field(repr=False)
    shares: Mapping[Label, Mapping[str, float]]
    contestability: Mapping[Label, float]
    weights: Mapping[Label, float]
    kappa: Mapping[frozenset[str], Mapping[Label, float]]
    links: frozenset[tuple[str, str, Label]]
    arcs: frozenset[LabelArc]

    def holders(self, m: Label) -> frozenset[str]:
        return frozenset(v for v, ps in self.roles.items() if m in ps)


# Coded records and the profile map ---------------------------------------------------------


@dataclass(frozen=True)
class CodedRecord:
    """The coded record of a governance system: practices plus index inputs (Part VII F6,
    well-formed record; Thm 7.4 assumes it).

    Well-formedness (enforced): ``shares`` has a probability vector for EVERY implemented
    pillar and none for an unimplemented one, each supported on the performers of that
    pillar's practices; Q has one value in [0, 1] per pillar; ``weights`` (None = 1/M each)
    are non-negative and sum to 1; ``coalitions`` maps a non-empty coalition (frozenset of
    actors) to kappa_m(S) in [0, 1] (None = singleton coalitions, kappa_m({v}) = s^m_v).
    On this domain F2 and F3 hold for every image, so the theorem's content rests on F1, F4.
    """

    system: GovernanceSystem
    shares: Mapping[Pillar, Mapping[str, float]]
    contestability: Mapping[Pillar, float]
    weights: Mapping[Pillar, float] | None = None
    coalitions: Mapping[frozenset[str], Mapping[Pillar, float]] | None = None
    links: tuple[CaptureLink, ...] = ()

    def __post_init__(self) -> None:
        roles = role_map(self.system)
        implemented = {m for m in PILLARS if realized_form(self.system, m) is not None}
        if any(not isinstance(m, Pillar) for m in self.shares):
            raise TypeError("share keys must be Pillars")
        if set(self.shares) != implemented:
            raise ValueError("shares must cover exactly the implemented pillars")
        for m, s in self.shares.items():
            vals = [float(v) for v in s.values()]
            if not vals or any(not math.isfinite(v) or v < 0 for v in vals):
                raise ValueError(f"shares[{m.name}] must be finite and non-negative")
            if abs(sum(vals) - 1.0) > _ATOL:
                raise ValueError(f"shares[{m.name}] must sum to 1")
            for actor, v in s.items():
                if float(v) > 0 and m not in roles.get(actor, frozenset()):
                    raise ValueError(f"{actor!r} has share in {m.name} but performs no practice")
        if set(self.contestability) != set(PILLARS):
            raise ValueError("contestability must give one value per pillar")
        for m in PILLARS:
            validate_unit_interval(self.contestability[m], f"Q[{m.name}]")
        object.__setattr__(self, "weights", validate_weights(self.weights))
        if self.coalitions is not None:
            known = set(roles) | {a for s in self.shares.values() for a in s}
            known |= {e for lk in self.links for e in (lk.source, lk.target)}
            for members, row in self.coalitions.items():
                if not isinstance(members, frozenset) or not members:
                    raise TypeError("coalition keys must be non-empty frozensets of actors")
                if any(not isinstance(v, str) for v in members):
                    raise TypeError("coalition members must be actor names (str)")
                if not members <= known:
                    raise ValueError(f"coalition {sorted(members)} names unknown actors")
                if any(not isinstance(m, Pillar) for m in row):
                    raise TypeError("kappa keys must be Pillars")
                for m, x in row.items():
                    validate_unit_interval(x, f"kappa[{sorted(members)}][{m.name}]")


def minimal_record(system: GovernanceSystem, q: float = 0.5) -> CodedRecord:
    """Record with PLACEHOLDER index inputs: uniform shares over performers, Q = q everywhere.

    For systems such as the hard cases, which are coded only by practices. Representability
    does not depend on these values; preserved quantities computed from them are not data.
    """
    roles = role_map(system)
    shares = {}
    for m in PILLARS:
        hs = sorted(a for a, ps in roles.items() if m in ps)
        if hs:
            shares[m] = {a: 1.0 / len(hs) for a in hs}
    return CodedRecord(system, shares, {m: q for m in PILLARS})


def record_from_polity(
    polity: Polity, coalitions: Mapping[frozenset[str], Mapping[Pillar, float]] | None = None
) -> CodedRecord:
    """The coded record of a Polity (shares normalized, zero-share pillars of unimplemented
    functions omitted, weights validated)."""
    implemented = {m for m in PILLARS if realized_form(polity.system, m) is not None}
    return CodedRecord(
        system=polity.system,
        shares={m: s for m, s in polity.normalized_shares.items() if m in implemented},
        contestability=polity.contestability,
        weights=polity.weights,
        coalitions=coalitions,
        links=polity.capture_links,
    )


def represent(record: CodedRecord) -> FormalizedStructure:
    """The profile map pi: G -> F_G.

    V = practice performers plus actors named in shares or links (roles come only from
    practices). m in rho(v) iff v performs a practice of pillar m and m is implemented.
    Shares, Q, weights, coalitions and links are copied; D = arcs generated from G's axioms.
    Layers: a^m_ij = s^m_i for i != j, so out-strength shares reproduce s^m.
    """
    system = record.system
    implemented = {m for m in PILLARS if realized_form(system, m) is not None}
    performers = role_map(system)
    named = {a for s in record.shares.values() for a in s}
    named |= {e for link in record.links for e in (link.source, link.target)}
    actors = tuple(sorted(set(performers) | named))
    roles = {
        v: frozenset(m.name for m in performers.get(v, frozenset()) if m in implemented)
        for v in actors
    }
    shares = {
        m.name: {v: float(record.shares.get(m, {}).get(v, 0.0)) for v in actors}
        for m in PILLARS
    }
    idx = {v: k for k, v in enumerate(actors)}
    layers = {}
    for m in M_LABELS:
        arr = np.zeros((len(actors), len(actors)))
        for v, s in shares[m].items():
            arr[idx[v], :] = s
        np.fill_diagonal(arr, 0.0)
        layers[m] = arr
    weights = record.weights
    if record.coalitions is None:
        kappa = {frozenset({v}): {m: shares[m][v] for m in M_LABELS} for v in actors}
    else:
        kappa = {members: {m.name: float(row.get(m, 0.0)) for m in PILLARS}
                 for members, row in record.coalitions.items()}
    links = frozenset((lk.source, lk.target, lk.pillar.name) for lk in record.links if lk.holds)
    arcs = frozenset(
        (frozenset(t.name for t in tail), head.name)
        for tail, head in generate_dependencies(system)
    )
    return FormalizedStructure(
        actors=actors, pillars=M_LABELS, roles=roles, layers=layers, shares=shares,
        contestability={m.name: float(record.contestability[m]) for m in PILLARS},
        weights={m.name: float(weights[m]) for m in PILLARS},
        kappa=kappa, links=links, arcs=arcs,
    )


# Formalized class --------------------------------------------------------------------------


def _underlying(arcs: Iterable[LabelArc], labels: Iterable[Label]) -> dict[Label, set[Label]]:
    adj: dict[Label, set[Label]] = {m: set() for m in labels}
    for tail, head in arcs:
        for t in tail:
            adj.setdefault(t, set()).add(head)
    return adj


def _closure(arcs: Iterable[LabelArc], start: Iterable[Label]) -> frozenset[Label]:
    """cl(S) on string labels (same rule as necessity.cascade_closure)."""
    arcs = list(arcs)
    closed = set(start)
    changed = True
    while changed:
        changed = False
        for tail, head in arcs:
            if head not in closed and tail <= closed:
                closed.add(head)
                changed = True
    return frozenset(closed)


def _cascade_complete(arcs: Iterable[LabelArc], labels: tuple[Label, ...]) -> bool:
    keep = frozenset(labels)
    inside = [(t, h) for t, h in arcs if h in keep and t <= keep]
    return bool(keep) and all(_closure(inside, {n}) >= keep for n in keep)


@dataclass(frozen=True)
class ClassMembership:
    """Conditions F1..F4 of the formalized class."""

    f1: bool
    f2: bool
    f3: bool
    f4: bool

    @property
    def holds(self) -> bool:
        return self.f1 and self.f2 and self.f3 and self.f4


def well_formed(F: FormalizedStructure) -> bool:
    """Domain check: every component is indexed by exactly V and the pillar labels, layers
    are |V| x |V| and finite, every number is finite, and every hyperarc (T, h) has a
    non-empty tail of labels and a label head outside T."""
    actors, labels = set(F.actors), set(F.pillars)
    if len(actors) != len(F.actors) or len(labels) != len(F.pillars):
        return False
    if set(F.roles) != actors or any(not ps <= labels for ps in F.roles.values()):
        return False
    if set(F.shares) != labels or any(set(F.shares[m]) != actors for m in labels):
        return False
    if set(F.layers) != labels or set(F.contestability) != labels or set(F.weights) != labels:
        return False
    n = len(F.actors)
    for m in labels:
        arr = np.asarray(F.layers[m], dtype=float)
        if arr.shape != (n, n) or not np.all(np.isfinite(arr)):
            return False
    nums = [*(x for m in labels for x in F.shares[m].values()), *F.contestability.values(),
            *F.weights.values(), *(x for r in F.kappa.values() for x in r.values())]
    if not all(math.isfinite(float(x)) for x in nums):
        return False
    for members, row in F.kappa.items():
        if not isinstance(members, frozenset) or not members or not members <= actors:
            return False
        if not set(row) <= labels:
            return False
    for tail, head in F.arcs:
        if not isinstance(tail, frozenset) or not tail or not tail <= labels:
            return False
        if head not in labels or head in tail:
            return False
    return all(a in actors and b in actors and m in labels for a, b, m in F.links)


def in_formalized_class(F: FormalizedStructure) -> ClassMembership:
    """F1 every layer has a holder; F2 s^m a probability vector on holders of m, a^m_ij in
    [0, 1] and > 0 only if i holds m; F3 Q, omega, kappa in range (omega summing to 1), link
    endpoints in V; F4 D contains D0 and is strongly connected and cascade-complete.

    A structure that is not ``well_formed`` (or whose labels are not the six pillars) fails
    every condition.
    """
    if F.pillars != M_LABELS or not F.actors or not well_formed(F):
        return ClassMembership(False, False, False, False)
    f1 = all(F.holders(m) for m in F.pillars)
    f2 = True
    for m in F.pillars:
        s = np.array([F.shares[m][v] for v in F.actors], dtype=float)
        holders = F.holders(m)
        arr = np.asarray(F.layers[m], dtype=float)
        on_holders = all(F.shares[m][v] == 0.0 or v in holders for v in F.actors)
        rows_ok = all(not arr[i].any() or v in holders for i, v in enumerate(F.actors))
        if (s.min() < 0 or abs(s.sum() - 1.0) > _ATOL or not on_holders or not rows_ok
                or arr.min() < 0.0 or arr.max() > 1.0):
            f2 = False
    vals = [*F.contestability.values(), *F.weights.values(),
            *(x for row in F.kappa.values() for x in row.values())]
    f3 = (all(0.0 <= float(x) <= 1.0 for x in vals)
          and abs(sum(F.weights.values()) - 1.0) <= _ATOL)
    f4 = (
        D0_LABELS <= F.arcs
        and is_strongly_connected(_underlying(F.arcs, F.pillars), set(F.pillars))
        and _cascade_complete(F.arcs, F.pillars)
    )
    return ClassMembership(f1, f2, f3, f4)


def representable(record: CodedRecord) -> bool:
    """G is representable iff its image F_G lies in the formalized class."""
    return in_formalized_class(represent(record)).holds


# Preserved quantities and A-equivalence ----------------------------------------------------


@dataclass(frozen=True)
class PreservedQuantities:
    H: dict[Label, float]
    U: float
    C: dict[frozenset[Label], float]
    I: float  # noqa: E741  (integration statistic, math cal I)
    cap: bool
    inter: bool


def preserved_quantities(
    F: FormalizedStructure, thresholds: CaptureThresholds = CaptureThresholds()
) -> PreservedQuantities:
    """H_m, U, C_mn (coalition overlap), I, Cap (Proposition B) and Inter on F's own labels."""
    H = {m: hhi([F.shares[m].get(v, 0.0) for v in F.actors]) if F.holders(m) else 0.0
         for m in F.pillars}
    U = sum(F.weights[m] * H[m] * (1.0 - F.contestability[m]) for m in F.pillars)
    pairs = list(itertools.combinations(F.pillars, 2))
    C = {frozenset((m, n)): max((min(row.get(m, 0.0), row.get(n, 0.0))
                                 for row in F.kappa.values()), default=0.0)
         for m, n in pairs}
    I = sum(C.values()) / len(pairs) if pairs else 0.0  # noqa: E741
    cap = U >= thresholds.u_star and I >= thresholds.i_star and bool(F.links)
    inter = (is_strongly_connected(_underlying(F.arcs, F.pillars), set(F.pillars))
             and _cascade_complete(F.arcs, F.pillars))
    return PreservedQuantities(H, float(U), C, float(I), cap, inter)


def _r(x: float) -> float:
    return round(float(x), _ROUND) + 0.0


def _kv(row: Mapping[Label, float], m: Label) -> tuple[int, float]:
    """kappa entry with an explicit presence flag: a missing column is (0, 0.0), a present
    one (1, value), so missing and explicit zero stay distinct (as in ``find_bijection``)."""
    return (1, _r(row[m])) if m in row else (0, 0.0)


def _same(a: float, b: float) -> bool:
    return abs(a - b) <= _ATOL


def _actor_signature(F: FormalizedStructure, k: int, with_layers: bool) -> tuple:
    v = F.actors[k]
    sig = (
        tuple(sorted(F.roles[v])),
        tuple(_r(F.shares[m][v]) for m in F.pillars),
        tuple(sorted((m, a == v, b == v) for a, b, m in F.links if v in (a, b))),
        tuple(sorted(tuple(_kv(r, m) for m in F.pillars)
                     for S, r in F.kappa.items() if v in S)),
    )
    if with_layers:
        sig += tuple((tuple(sorted(_r(x) for x in F.layers[m][k])),
                      tuple(sorted(_r(x) for x in F.layers[m][:, k]))) for m in F.pillars)
    return sig


def find_bijection(F: FormalizedStructure, G: FormalizedStructure,
                   with_layers: bool) -> dict[str, str] | None:
    """An actor bijection phi: V_F -> V_G under which roles, shares, Q, omega, kappa
    (transported: kappa_F(S) = kappa_G(phi(S))), links and D agree, and, if ``with_layers``,
    every layer entry. None if there is none.

    Numbers are compared EXACTLY after quantization to 12 decimals (``_r``), the same
    normalization the canonical form uses, so equality is an equivalence relation.

    Backtracking within classes of equal actor signatures; the identity on names is tried
    first. Both structures must be ``well_formed``.
    """
    if not (well_formed(F) and well_formed(G)):
        return None
    if F.pillars != G.pillars or len(F.actors) != len(G.actors) or F.arcs != G.arcs:
        return None
    if any(_r(F.contestability[m]) != _r(G.contestability[m])
           or _r(F.weights[m]) != _r(G.weights[m]) for m in F.pillars):
        return None
    if len(F.kappa) != len(G.kappa) or len(F.links) != len(G.links):
        return None
    sig_f = [_actor_signature(F, k, with_layers) for k in range(len(F.actors))]
    sig_g = [_actor_signature(G, k, with_layers) for k in range(len(G.actors))]
    if sorted(sig_f) != sorted(sig_g):
        return None
    gi = {v: k for k, v in enumerate(G.actors)}
    fi = {v: k for k, v in enumerate(F.actors)}
    order = sorted(range(len(F.actors)), key=lambda k: sig_f[k])
    assign: dict[int, int] = {}
    used: set[int] = set()

    def consistent(i: int, j: int) -> bool:
        if with_layers:
            for i2, j2 in assign.items():
                for m in F.pillars:
                    if (_r(F.layers[m][i, i2]) != _r(G.layers[m][j, j2])
                            or _r(F.layers[m][i2, i]) != _r(G.layers[m][j2, j])):
                        return False
        mapped = {**assign, i: j}
        for a, b, m in F.links:
            ia, ib = fi[a], fi[b]
            if ia in mapped and ib in mapped:
                if (G.actors[mapped[ia]], G.actors[mapped[ib]], m) not in G.links:
                    return False
        return True

    def kappa_ok() -> bool:
        to_g = {F.actors[i]: G.actors[j] for i, j in assign.items()}
        for S, row in F.kappa.items():
            other = G.kappa.get(frozenset(to_g[v] for v in S))
            if other is None or set(other) != set(row):
                return False
            if any(_r(row[m]) != _r(other[m]) for m in row):
                return False
        return True

    def search(pos: int) -> bool:
        if pos == len(order):
            return kappa_ok()
        i = order[pos]
        cands = [j for j in range(len(G.actors)) if j not in used and sig_g[j] == sig_f[i]]
        pref = gi.get(F.actors[i])
        if pref in cands:
            cands.remove(pref)
            cands.insert(0, pref)
        for j in cands:
            if consistent(i, j):
                assign[i] = j
                used.add(j)
                if search(pos + 1):
                    return True
                del assign[i]
                used.discard(j)
        return False

    if not search(0):
        return None
    return {F.actors[i]: G.actors[j] for i, j in assign.items()}


def equivalent_A(F: FormalizedStructure, G: FormalizedStructure) -> bool:  # noqa: N802
    """F and G agree on roles, shares, Q, omega, kappa, links and D under an actor bijection
    (layers not compared; see ``uniqueness.p_equal`` for the version with layers)."""
    return find_bijection(F, G, with_layers=False) is not None


# Coarsenings (minimality) ------------------------------------------------------------------


def drop(F: FormalizedStructure, m: Label) -> FormalizedStructure:
    """Delete pillar m: its layer, shares, Q, kappa column and every hyperarc involving m.

    Remaining weights are renormalized to sum 1.
    """
    if m not in F.pillars:
        raise ValueError(f"unknown pillar {m!r}")
    keep = tuple(p for p in F.pillars if p != m)
    total = sum(F.weights[p] for p in keep)
    weights = {p: (F.weights[p] / total if total > 0 else 1.0 / len(keep)) for p in keep}
    return FormalizedStructure(
        actors=F.actors, pillars=keep,
        roles={v: ps - {m} for v, ps in F.roles.items()},
        layers={p: F.layers[p] for p in keep},
        shares={p: dict(F.shares[p]) for p in keep},
        contestability={p: F.contestability[p] for p in keep},
        weights=weights,
        kappa={s: {p: row.get(p, 0.0) for p in keep} for s, row in F.kappa.items()},
        links=frozenset(lk for lk in F.links if lk[2] != m),
        arcs=frozenset((t, h) for t, h in F.arcs if h != m and m not in t),
    )


def merge(F: FormalizedStructure, m: Label, n: Label, lam: float) -> FormalizedStructure:
    """Replace m, n by one pillar 'm+n': holders united, shares, layers, Q and kappa mixed with
    weight lam on m; omega_m + omega_n; arcs relabeled, self-loops removed."""
    if m == n or m not in F.pillars or n not in F.pillars:
        raise ValueError("merge needs two distinct existing pillars")
    lam = validate_unit_interval(lam, "lam")
    new = f"{m}+{n}"
    keep = tuple(new if p == m else p for p in F.pillars if p != n)
    relabel = lambda p: new if p in (m, n) else p  # noqa: E731

    def mix(a: float, b: float) -> float:
        return lam * a + (1.0 - lam) * b

    shares = {p: dict(F.shares[p]) for p in keep if p != new}
    shares[new] = {v: mix(F.shares[m].get(v, 0.0), F.shares[n].get(v, 0.0)) for v in F.actors}
    layers = {p: F.layers[p] for p in keep if p != new}
    layers[new] = lam * F.layers[m] + (1.0 - lam) * F.layers[n]
    contest = {p: F.contestability[p] for p in keep if p != new}
    contest[new] = mix(F.contestability[m], F.contestability[n])
    weights = {p: F.weights[p] for p in keep if p != new}
    weights[new] = F.weights[m] + F.weights[n]
    kappa = {}
    for s, row in F.kappa.items():
        r = {p: row.get(p, 0.0) for p in keep if p != new}
        r[new] = mix(row.get(m, 0.0), row.get(n, 0.0))
        kappa[s] = r
    arcs = set()
    for t, h in F.arcs:
        t2, h2 = frozenset(relabel(x) for x in t), relabel(h)
        if h2 not in t2:
            arcs.add((t2, h2))
    return FormalizedStructure(
        actors=F.actors, pillars=keep,
        roles={v: frozenset(relabel(p) for p in ps) for v, ps in F.roles.items()},
        layers=layers, shares=shares, contestability=contest, weights=weights, kappa=kappa,
        links=frozenset((a, b, relabel(p)) for a, b, p in F.links),
        arcs=frozenset(arcs),
    )


def structurally_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
    """Equality of every component with the identity on actor names (floats within 1e-9)."""
    if not (well_formed(F) and well_formed(G)):
        return False
    if (F.actors, F.pillars, F.links, F.arcs) != (G.actors, G.pillars, G.links, G.arcs):
        return False
    if any(F.roles[v] != G.roles[v] for v in F.actors) or set(F.kappa) != set(G.kappa):
        return False
    return (
        all(_same(F.shares[m][v], G.shares[m][v]) for m in F.pillars for v in F.actors)
        and all(np.allclose(F.layers[m], G.layers[m], atol=_ATOL, rtol=0) for m in F.pillars)
        and all(_same(F.contestability[m], G.contestability[m]) for m in F.pillars)
        and all(_same(F.weights[m], G.weights[m]) for m in F.pillars)
        and all(set(F.kappa[S]) == set(G.kappa[S])
                and all(_same(F.kappa[S][m], G.kappa[S][m]) for m in F.kappa[S])
                for S in F.kappa)
    )


D_STAR_LABELS: frozenset[LabelArc] = frozenset(
    (frozenset(t.name for t in tail), head.name) for tail, head in D_STAR_KEYS
)


def make_structure(
    shares: Mapping[Label, Mapping[str, float]],
    contestability: Mapping[Label, float],
    weights: Mapping[Label, float] | None = None,
    kappa: Mapping[frozenset[str], Mapping[Label, float]] | None = None,
    links: Iterable[tuple[str, str, Label]] = (),
    arcs: Iterable[LabelArc] = D_STAR_LABELS,
) -> FormalizedStructure:
    """Build F directly: holders are actors with positive share, a^m_ij = s^m_i (i != j),
    singleton coalitions by default. Used for the minimality fixtures."""
    pillars = tuple(shares)
    actors = tuple(sorted({v for s in shares.values() for v in s}))
    full = {m: {v: float(shares[m].get(v, 0.0)) for v in actors} for m in pillars}
    roles = {v: frozenset(m for m in pillars if full[m][v] > 0) for v in actors}
    layers = {}
    for m in pillars:
        arr = np.tile(np.array([full[m][v] for v in actors])[:, None], (1, len(actors)))
        np.fill_diagonal(arr, 0.0)
        layers[m] = arr
    if kappa is None:
        kappa = {frozenset({v}): {m: full[m][v] for m in pillars} for v in actors}
    return FormalizedStructure(
        actors=actors, pillars=pillars, roles=roles, layers=layers, shares=full,
        contestability=dict(contestability),
        weights=dict(weights) if weights else {m: 1.0 / len(pillars) for m in pillars},
        kappa={s: dict(r) for s, r in kappa.items()},
        links=frozenset(links), arcs=frozenset(arcs),
    )
