"""Uniqueness and novelty: coarsenings, factorization through Phi, predecessor encodings.

Part VII Def 7.6 (Abs_P), Thm 7.7 (uniqueness), Thm 7.8 (six dimensions, stated for
coarsenings Phi_c: Phi_c is P-preserving iff c is a bijection onto K with |K| = 6),
Prop 10.1 (witnesses), Thm 10.2 (novelty).

Part VII (uniqueness and novelty by proof). P(G) is the isomorphism class of represent(G):
roles, shares, Q, omega, kappa, links, D and layers up to an actor bijection (``p_equal``).
A coarsening c: M -> K or None merges pillars into blocks (lam-weighted) or drops them. Every
c that is not a total injection collapses a witness pair (``witness_coarsening``): two
systems satisfying all axioms with equal coarsened profiles but different P. Classical
schemes (Parsons, Mann, Easton, Luhmann, Almond) are coarsenings; Aristotle and Weber are
typologies; each has a witness pair. No uniqueness claim is made beyond these statements.
"""

from __future__ import annotations

import itertools
import math
from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass

from .capture import CaptureLink
from .necessity import EXTENDED_AXIOMS, GovernanceSystem, Practice
from .pillars import PILLAR_TO_AXIOM, PILLARS
from .representation import (
    CodedRecord,
    FormalizedStructure,
    Label,
    M_LABELS,
    _kv,
    find_bijection,
    represent,
    structurally_equal,
    well_formed,
)

_ROUND = 12
_ATOL = 1e-9
Coarsening = Mapping[Label, "Label | None"]


# Coarsening --------------------------------------------------------------------------------


def _blocks(F: FormalizedStructure, c: Coarsening) -> dict[Label, list[Label]]:
    if set(c) != set(F.pillars):
        raise ValueError("a coarsening must assign every pillar (None drops it)")
    blocks: dict[Label, list[Label]] = {}
    for m in F.pillars:
        if c[m] is not None:
            blocks.setdefault(c[m], []).append(m)
    return blocks


def _block_weights(blocks: Mapping[Label, list[Label]],
                   lam: Mapping[Label, float] | None) -> dict[Label, float]:
    out: dict[Label, float] = {}
    for members in blocks.values():
        for m in members:
            out[m] = 1.0 / len(members) if lam is None else float(lam[m])
        if any(not math.isfinite(out[m]) or out[m] <= 0.0 for m in members):
            raise ValueError("lam_m must be positive")
        if abs(sum(out[m] for m in members) - 1.0) > _ATOL:
            raise ValueError("lam must sum to 1 within each block")
    return out


def coarsen(F: FormalizedStructure, c: Coarsening,
            lam: Mapping[Label, float] | None = None) -> FormalizedStructure:
    """Coarsen F by c: M -> K or None (drop), lam-weighted within each block (default equal).

    Block holders are the union; shares, layers, Q and kappa are lam-weighted sums; omega_k is
    the sum of omega_m (not renormalized); hyperarcs with no dropped element map to their image
    under c, self-loops removed; links in dropped pillars are removed.
    """
    blocks = _blocks(F, c)
    w = _block_weights(blocks, lam)
    keys = tuple(blocks)

    def mix(get: Callable[[Label], float], k: Label) -> float:
        return sum(w[m] * get(m) for m in blocks[k])

    shares = {k: {v: mix(lambda m: F.shares[m].get(v, 0.0), k) for v in F.actors} for k in keys}
    layers = {k: sum(w[m] * F.layers[m] for m in blocks[k]) for k in keys}
    arcs = set()
    for tail, head in F.arcs:
        if c[head] is None or any(c[t] is None for t in tail):
            continue
        t2, h2 = frozenset(c[t] for t in tail), c[head]
        if h2 not in t2:
            arcs.add((t2, h2))
    return FormalizedStructure(
        actors=F.actors, pillars=keys,
        roles={v: frozenset(c[m] for m in ps if c[m] is not None) for v, ps in F.roles.items()},
        layers=layers, shares=shares,
        contestability={k: mix(lambda m: F.contestability[m], k) for k in keys},
        weights={k: sum(F.weights[m] for m in blocks[k]) for k in keys},
        kappa={s: {k: mix(lambda m: row.get(m, 0.0), k) for k in keys} for s, row in F.kappa.items()},
        links=frozenset((a, b, c[m]) for a, b, m in F.links if c[m] is not None),
        arcs=frozenset(arcs),
    )


IDENTITY: dict[Label, Label] = {m: m for m in M_LABELS}


def phi(record: CodedRecord) -> FormalizedStructure:
    """Phi = coarsen(represent(G), identity)."""
    return coarsen(represent(record), IDENTITY)


# P-equality --------------------------------------------------------------------------------


def _r(x: float) -> float:
    return round(float(x), _ROUND) + 0.0


def p_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
    """P(F) = P(G): roles, shares, Q, omega, kappa (transported), links, D and layers agree
    under an actor bijection (``representation.find_bijection`` with layers)."""
    return find_bijection(F, G, with_layers=True) is not None


def _global(F: FormalizedStructure) -> tuple:
    return (
        F.pillars,
        tuple(_r(F.contestability[m]) for m in F.pillars),
        tuple(_r(F.weights[m]) for m in F.pillars),
        tuple(sorted((tuple(sorted(S)), tuple(_kv(r, m) for m in F.pillars))
                     for S, r in F.kappa.items())),
        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
        len(F.actors),
    )


def freeze(F: FormalizedStructure) -> tuple:
    """Hashable encoding of F with its actor names (equality = identity on names)."""
    return (
        F.actors, F.pillars,
        tuple(tuple(sorted(F.roles[v])) for v in F.actors),
        tuple(tuple(_r(F.shares[m][v]) for v in F.actors) for m in F.pillars),
        tuple(tuple(_r(x) for x in F.layers[m].ravel()) for m in F.pillars),
        _global(F), tuple(sorted(F.links)),
    )


# Factorization through Phi -----------------------------------------------------------------


@dataclass(frozen=True)
class Factorization:
    """alpha factors through Phi on the fixtures: alpha(G) = alpha(G2) implies P(G) = P(G2)
    (``well_defined``: h(alpha(G)) = Phi(G) is a function); ``bijective``: h is also
    injective onto the P-classes of the fixtures."""

    well_defined: bool
    bijective: bool


def factor_through_phi(alpha: Callable[[CodedRecord], object],
                       records: Sequence[CodedRecord]) -> Factorization:
    """Check that the P-preserving abstraction ``alpha`` factors through Phi on ``records``."""
    images = [alpha(r) for r in records]
    phis = [phi(r) for r in records]
    well_defined = injective = True
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            same_alpha = images[i] == images[j]
            same_p = p_equal(phis[i], phis[j])
            if same_alpha and not same_p:
                well_defined = False
            if same_p and not same_alpha:
                injective = False
    return Factorization(well_defined, well_defined and injective)


def alpha_represent(record: CodedRecord) -> tuple:
    """NOT P-preserving (negative control): the frozen profile keeps actor names, so two
    actor-renamed copies of one system get different values."""
    return freeze(represent(record))


# Canonical form (a complete invariant of P) ------------------------------------------------


def _encode(F: FormalizedStructure, order: Sequence[int]) -> tuple:
    """Name-free encoding of F with actors listed in ``order``."""
    pos = {F.actors[k]: i for i, k in enumerate(order)}
    return (
        F.pillars,
        tuple(tuple(sorted(F.roles[F.actors[k]])) for k in order),
        tuple(tuple(_r(F.shares[m][F.actors[k]]) for k in order) for m in F.pillars),
        tuple(tuple(_r(F.layers[m][i, j]) for i in order for j in order) for m in F.pillars),
        tuple(_r(F.contestability[m]) for m in F.pillars),
        tuple(_r(F.weights[m]) for m in F.pillars),
        tuple(sorted((tuple(sorted(pos[v] for v in S)),
                      tuple(_kv(r, m) for m in F.pillars)) for S, r in F.kappa.items())),
        tuple(sorted((pos[a], pos[b], m) for a, b, m in F.links)),
        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
    )


def _relabel(sigs: Sequence) -> list[int]:
    table = {sg: c for c, sg in enumerate(sorted(set(sigs)))}
    return [table[sg] for sg in sigs]


def _initial_colors(F: FormalizedStructure) -> list[int]:
    return _relabel([(tuple(sorted(F.roles[v])), tuple(_r(F.shares[m][v]) for m in F.pillars))
                     for v in F.actors])


def _refine(F: FormalizedStructure, colors: list[int]) -> list[int]:
    """Colour refinement from ``colors``, iterated until the partition is stable. The result
    depends only on the structure and the input colouring, never on actor names."""
    n = len(F.actors)
    idx = {v: k for k, v in enumerate(F.actors)}
    while True:
        sigs = []
        for k in range(n):
            v = F.actors[k]
            sigs.append((
                colors[k],
                tuple(sorted((colors[j],
                              tuple(_r(F.layers[m][k, j]) for m in F.pillars),
                              tuple(_r(F.layers[m][j, k]) for m in F.pillars))
                             for j in range(n) if j != k)),
                tuple(sorted((colors[idx[b]], m, "out") for a, b, m in F.links if a == v)
                      + sorted((colors[idx[a]], m, "in") for a, b, m in F.links if b == v)),
                tuple(sorted((tuple(sorted(colors[idx[u]] for u in S)),
                              tuple(_kv(r, m) for m in F.pillars))
                             for S, r in F.kappa.items() if v in S)),
            ))
        new = _relabel(sigs)
        if len(set(new)) == len(set(colors)):
            return new
        colors = new


def _interchangeable(F: FormalizedStructure, colors: list[int], cls: list[int]) -> bool:
    """True if every transposition (cls[0] cls[t]) is an automorphism of F that preserves
    ``colors``; these transpositions generate all permutations of the class."""
    order = sorted(range(len(F.actors)), key=lambda k: (colors[k], k))
    ref = _encode(F, order)
    pos = {k: i for i, k in enumerate(order)}
    for other in cls[1:]:
        swapped = list(order)
        a, b = pos[cls[0]], pos[other]
        swapped[a], swapped[b] = swapped[b], swapped[a]
        if _encode(F, swapped) != ref:
            return False
    return True


def canonical_form(F: FormalizedStructure) -> tuple:
    """A complete invariant of P: canonical_form(F) == canonical_form(G) iff p_equal(F, G).

    Individualization-refinement: refine colours; if every class is a singleton, encode in
    colour order; otherwise branch on each member of the first smallest non-singleton class
    (individualize it, refine, recurse) and return the lexicographic minimum. When all
    transpositions within that class are automorphisms, the branches give identical results
    and only one is explored. Total on well-formed structures (worst-case exponential time).
    Numbers enter quantized to 12 decimals, as in ``p_equal``.
    """
    if not well_formed(F):
        raise ValueError("canonical_form needs a well-formed structure")
    n = len(F.actors)
    if n == 0:
        return _encode(F, [])

    def search(colors: list[int]) -> tuple:
        colors = _refine(F, colors)
        classes: dict[int, list[int]] = {}
        for k, c in enumerate(colors):
            classes.setdefault(c, []).append(k)
        open_ = [cl for c, cl in sorted(classes.items()) if len(cl) > 1]
        if not open_:
            return _encode(F, sorted(range(n), key=lambda k: colors[k]))
        cls = min(open_, key=len)
        branches = cls[:1] if _interchangeable(F, colors, cls) else cls
        best = None
        for v in branches:
            individualized = _relabel([(colors[k], 0 if k == v else 1) for k in range(n)])
            enc = search(individualized)
            if best is None or enc < best:
                best = enc
        return best

    return search(_initial_colors(F))


def alpha_canonical(record: CodedRecord) -> tuple:
    """A P-preserving abstraction: the canonical form of represent(G)."""
    return canonical_form(represent(record))


def alpha_canonical_phi(record: CodedRecord) -> tuple:
    """A second, differently built one: the canonical form of Phi(G) (coarsen by identity)
    plus a redundant field (the number of hyperarcs)."""
    F = phi(record)
    return (canonical_form(F), len(F.arcs))


def rename_record(record: CodedRecord, mapping: Mapping[str, str]) -> CodedRecord:
    """The same coded system with actors renamed by ``mapping`` (missing names kept)."""
    ren = lambda v: mapping.get(v, v)  # noqa: E731
    sys_ = record.system
    names = set(represent(record).actors)
    if len({ren(v) for v in names}) != len(names):
        raise ValueError("renaming must be injective on the record's actors")
    practices = tuple(
        Practice(p.description, p.solves, frozenset(ren(h) for h in p.holders), p.formal,
                 p.source)
        for p in sys_.practices
    )
    system = GovernanceSystem(sys_.name, sys_.persistent, sys_.axioms, practices,
                              sys_.absent_incidences, sys_.note)
    links = tuple(CaptureLink(ren(lk.source), ren(lk.target), lk.pillar, lk.privileged_access,
                              lk.weakens_accountability, lk.material_evidence, lk.evidence)
                  for lk in record.links)
    coalitions = None if record.coalitions is None else {
        frozenset(ren(v) for v in S): row for S, row in record.coalitions.items()}
    return CodedRecord(system, {m: {ren(v): x for v, x in sh.items()}
                                for m, sh in record.shares.items()},
                       record.contestability, record.weights, coalitions, links)


# Witnesses ---------------------------------------------------------------------------------


def witness_record(ab_shares: Mapping[Label, tuple[float, float]], q: float = 0.5,
                   links: Iterable = ()) -> CodedRecord:
    """Witness system (Part VII Prop 7.5, Prop 10.1): actors a and b perform exactly the
    pillars in ``ab_shares`` with shares (s^m_a, s^m_b); actor c alone performs every other
    pillar (share 1). Ax1..Ax6 and X1, X2, X3, X5 hold, so Proposition A holds. Both members
    of a witness pair use the same keys, hence the same actor set and role map.
    """
    if not ab_shares or not set(ab_shares) <= set(M_LABELS):
        raise ValueError("ab_shares must name at least one pillar label")
    practices = tuple(
        Practice(f"{m.label} practice", PILLAR_TO_AXIOM[m],
                 frozenset({"a", "b"}) if m.name in ab_shares else frozenset({"c"}),
                 source="synthetic witness")
        for m in PILLARS
    )
    system = GovernanceSystem("witness", True, EXTENDED_AXIOMS, practices)
    shares = {m: (dict(zip(("a", "b"), ab_shares[m.name])) if m.name in ab_shares
                  else {"c": 1.0}) for m in PILLARS}
    return CodedRecord(system, shares, {m: q for m in PILLARS}, links=tuple(links))


def _drop_witness(m: Label, l0: Label) -> tuple[CodedRecord, CodedRecord]:
    """Drop m: G1 s^m = (1, 0), G2 s^m = (1/2, 1/2); a and b also hold (1/2, 1/2) in the
    retained pillar l0 in both, so b is an actor of G1 too."""
    return (witness_record({m: (1.0, 0.0), l0: (0.5, 0.5)}),
            witness_record({m: (0.5, 0.5), l0: (0.5, 0.5)}))


def _merge_witness(m: Label, n: Label, mu: float) -> tuple[CodedRecord, CodedRecord]:
    """Merge {m, n}: G1 s^m = (1, 0), s^n = (0, 1); G2 s^m = s^n = (mu, 1 - mu)."""
    return (witness_record({m: (1.0, 0.0), n: (0.0, 1.0)}),
            witness_record({m: (mu, 1.0 - mu), n: (mu, 1.0 - mu)}))


def witness_coarsening(c: Coarsening, lam: Mapping[Label, float] | None = None
                       ) -> tuple[CodedRecord, CodedRecord]:
    """(G1, G2) with coarsen(Phi(G1), c) = coarsen(Phi(G2), c) and P(G1) != P(G2)
    (Part VII Prop 7.5).

    If c drops a pillar m, the drop witness with l0 the first retained pillar (if c drops
    every pillar, a and b hold only m and both images are the actor set); otherwise, for
    the first pair {m, n} in one block, the merge witness with mu = lam_m / (lam_m + lam_n).
    Raises if c is a total injection (then Phi_c is P-preserving, Thm 7.8).
    """
    if set(c) != set(M_LABELS):
        raise ValueError("c must assign all six pillars")
    dropped = [m for m in M_LABELS if c[m] is None]
    kept = [m for m in M_LABELS if c[m] is not None]
    if dropped:
        if not kept:
            # K is empty: both images reduce to the shared actor set {a, b, c} (Prop 7.5(a)).
            m = dropped[0]
            return witness_record({m: (1.0, 0.0)}), witness_record({m: (0.5, 0.5)})
        return _drop_witness(dropped[0], kept[0])
    for i, m in enumerate(M_LABELS):
        for n in M_LABELS[i + 1:]:
            if c[m] == c[n]:
                if lam is None:
                    size = sum(1 for x in M_LABELS if c[x] == c[m])
                    lm = ln = 1.0 / size
                else:
                    lm, ln = float(lam[m]), float(lam[n])
                return _merge_witness(m, n, lm / (lm + ln))
    raise ValueError("c is a total injection; no collapse witness")


# Predecessor encodings ---------------------------------------------------------------------

PARSONS: dict[Label, Label | None] = {"F": "A", "W": "A", "P": "G", "J": "I", "C": "I", "I": "L"}
MANN: dict[Label, Label | None] = {"I": "Ideological", "F": "Economic", "W": "Economic",
                                   "C": "Military", "P": "Political", "J": "Political"}
EASTON: dict[Label, Label | None] = {"I": "Inputs", "W": "Inputs", "F": "Outputs",
                                     "P": "Outputs", "J": "Outputs", "C": "Outputs"}
LUHMANN: dict[Label, Label | None] = {"F": "Economy", "W": "Economy", "P": "Politics",
                                      "C": "Politics", "J": "Law", "I": "Culture"}
ALMOND: dict[Label, Label | None] = {"F": None, "W": None, "P": "RuleMaking",
                                     "J": "RuleAdjudication", "C": "RuleApplication",
                                     "I": "Inputs"}


def encode_parsons(F: FormalizedStructure) -> FormalizedStructure:
    """AGIL: A = {F, W}, G = {P}, I = {J, C}, L = {I}."""
    return coarsen(F, PARSONS)


def encode_mann(F: FormalizedStructure) -> FormalizedStructure:
    """IEMP: Ideological = {I}, Economic = {F, W}, Military = {C}, Political = {P, J}."""
    return coarsen(F, MANN)


def encode_easton(F: FormalizedStructure) -> FormalizedStructure:
    """Inputs = {I, W}, Outputs = {F, P, J, C}."""
    return coarsen(F, EASTON)


def encode_luhmann(F: FormalizedStructure) -> FormalizedStructure:
    """Economy = {F, W}, Politics = {P, C}, Law = {J}, Culture = {I} (Luhmann splits it
    further; the split does not affect the witness)."""
    return coarsen(F, LUHMANN)


def encode_almond(F: FormalizedStructure) -> FormalizedStructure:
    """F and W dropped; RuleMaking = {P}, RuleAdjudication = {J}, RuleApplication = {C},
    Inputs = {I}."""
    return coarsen(F, ALMOND)


def encode_aristotle(F: FormalizedStructure) -> tuple[str, str]:
    """(rulers, aim): 'one' if exactly one actor has s^P > 0, 'few' if 2 to n/2, else 'many';
    'deviant' if any capture link, else 'correct'. A typology, not a coarsening."""
    k = sum(1 for v in F.actors if F.shares["P"].get(v, 0.0) > 0.0)
    n = len(F.actors)
    rulers = "one" if k == 1 else ("few" if 2 <= k <= n / 2 else "many")
    return rulers, ("deviant" if F.links else "correct")


WEBER_TYPES = ("traditional", "charismatic", "legal-rational")


def encode_weber(F: FormalizedStructure, legitimation: str, has_staff: bool) -> tuple[str, bool]:
    """(legitimation type, administrative staff). Both come from a coded field the profile
    does NOT contain, so the encoding does not factor through P (nor P through it)."""
    if legitimation not in WEBER_TYPES:
        raise ValueError(f"legitimation must be one of {WEBER_TYPES}")
    return legitimation, bool(has_staff)


ENCODINGS: dict[str, Callable[[FormalizedStructure], object]] = {
    "parsons": encode_parsons,
    "mann": encode_mann,
    "easton": encode_easton,
    "luhmann": encode_luhmann,
    "almond": encode_almond,
    "aristotle": encode_aristotle,
    "weber": lambda F: encode_weber(F, "legal-rational", True),
}

_WITNESSES: dict[str, Callable[[], tuple[CodedRecord, CodedRecord]]] = {
    "parsons": lambda: _merge_witness("F", "W", 0.5),
    "mann": lambda: _merge_witness("P", "J", 0.5),
    "easton": lambda: _merge_witness("P", "J", 0.5),
    "luhmann": lambda: _merge_witness("F", "W", 0.5),
    "almond": lambda: _drop_witness("F", "P"),
    "aristotle": lambda: (witness_record({"J": (1.0, 0.0), "I": (0.5, 0.5)}),
                          witness_record({"J": (0.5, 0.5), "I": (0.5, 0.5)})),
    "weber": lambda: (witness_record({"C": (1.0, 0.0), "I": (0.5, 0.5)}),
                      witness_record({"C": (0.5, 0.5), "I": (0.5, 0.5)})),
}


def witness_pair(k: str) -> tuple[CodedRecord, CodedRecord]:
    """Two systems satisfying all axioms that encoding ``k`` cannot tell apart, with P
    differing (Part VII Prop 10.1). Merge witnesses use mu = 1/2 (equal lam; Easton's
    four-member Outputs block also gives mu = 1/2 for (P, J)); Almond drops F with l0 = P;
    Aristotle and Weber differ in s^J or s^C with a and b also holding (1/2, 1/2) in I.
    """
    if k not in _WITNESSES:
        raise ValueError(f"unknown encoding {k!r}")
    return _WITNESSES[k]()


def coarsenings_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
    """Coarsened profiles equal component by component (identity on actor names)."""
    return structurally_equal(F, G)
