"""Structural necessity: Proposition A and the pillar dependency hypergraph (Part VII Theorem A).

Theorem A (notation.md CENTRAL THESIS; KB Section 4): if a governance system G persists and
satisfies Ax1..Ax6, then every pillar in M is implemented in G, and the dependency relations
D0 are present. Implementation is role-level, not institution-level
(Hempel 1959): a function may be held by a formal institution, fused with other functions
inside one institution, or exercised informally (gossip and shunning as C, mediators as J).

What this module does and does not do. It cannot prove Theorem A. It encodes the lemma schema
'Ax_k + persistence => some practice solves problem_k' and checks it against coded cases. The
role map is DERIVED from independently coded practices, never declared, so a persistent case
that satisfies all six axioms yet has no practice for some problem, or lacks a D0 relation, is
reported as a counterexample (the falsifier required by KB Section 4.4).

Dependencies form an AND/OR hypergraph GENERATED from the axioms (Part VII revised dependency
spec). A hyperarc (T, h) is written provider(s) -> dependent and means: h needs an output of
AT LEAST ONE member of T. Incidence Inc(k, m), 'the problem of Ax_k arises about the inputs or
rules of pillar m', generates the arc pillar(k) -> m. The core set D* comes from Ax6 (W -> m),
Part III Prop 3.6 ({I, C} -> J), Ax4 with Part I Def 2.2(b) (I -> F), and the incidence axioms
X1 (F -> W), X2 (P -> F), X3 (J -> F), X5 (C -> F). Removing an axiom removes every arc it
generates. Two connectivity notions are computed:
  (a) the underlying digraph (each (T, h) replaced by arcs t -> h) is strongly connected;
  (b) cascade completeness: cl({n}) = M for every n, where cl(S) is the least superset of S
      such that T subset of cl(S) implies h in cl(S) for every hyperarc (T, h).
Interdependence = (a) and (b). Proposition A in full is Struct(G) (six pillars plus D0, from
Ax1..Ax6) AND interdependence (from Ax1..Ax6 plus X1, X2, X3, X5); both are exposed
separately. A system coding an incidence as absent while its premises hold is the falsifier
route for either part.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Literal

from .pillars import AXIOM_TO_PILLAR, PILLAR_TO_AXIOM, PILLARS, Axiom, IncidenceAxiom, Pillar

RealizedForm = Literal["formal institution", "fused", "informal/minimal"]
FORMAL: RealizedForm = "formal institution"
FUSED: RealizedForm = "fused"
INFORMAL: RealizedForm = "informal/minimal"

# Dependency hypergraph primitives ----------------------------------------------------------

#: A hyperarc key (T, h): tail set T, head h.
ArcKey = tuple[frozenset[Pillar], Pillar]
Graph = Mapping[Pillar, Iterable[Pillar]]
AnyAxiom = Axiom | IncidenceAxiom

#: Ax1..Ax6 plus the incidence axioms X1, X2, X3, X5 (Part VII extended axiom set).
EXTENDED_AXIOMS: frozenset[AnyAxiom] = frozenset(Axiom) | frozenset(IncidenceAxiom)


def arc_key(tail: Pillar | Iterable[Pillar], head: Pillar) -> ArcKey:
    """Normalize (T, h) to an ArcKey, validating T non-empty, h a Pillar and h not in T."""
    t = frozenset((tail,) if isinstance(tail, Pillar) else tail)
    if not t or not all(isinstance(m, Pillar) for m in t) or not isinstance(head, Pillar):
        raise TypeError("a hyperarc needs a non-empty tail of Pillars and a Pillar head")
    if head in t:
        raise ValueError(f"head {head.name} may not belong to its own tail")
    return t, head


def _keys(arcs: Iterable[DependencyRule | ArcKey]) -> frozenset[ArcKey]:
    return frozenset(a.key if isinstance(a, DependencyRule) else arc_key(*a) for a in arcs)


def underlying_digraph(arcs: Iterable[DependencyRule | ArcKey]) -> dict[Pillar, frozenset[Pillar]]:
    """Replace each hyperarc (T, h) by the arcs t -> h; adjacency over all six pillars."""
    adj: dict[Pillar, set[Pillar]] = {m: set() for m in PILLARS}
    for tail, head in _keys(arcs):
        for t in tail:
            adj[t].add(head)
    return {m: frozenset(v) for m, v in adj.items()}


def cascade_closure(
    arcs: Iterable[DependencyRule | ArcKey], start: Iterable[Pillar]
) -> frozenset[Pillar]:
    """cl(S): least superset of S with T subset of cl(S) => h in cl(S) for every (T, h).

    Read as a failure cascade: h fails once every provider in its tail has failed.
    """
    keys = _keys(arcs)
    closed = set(start)
    changed = True
    while changed:
        changed = False
        for tail, head in keys:
            if head not in closed and tail <= closed:
                closed.add(head)
                changed = True
    return frozenset(closed)


def is_cascade_complete(
    arcs: Iterable[DependencyRule | ArcKey], nodes: Iterable[Pillar] = PILLARS
) -> bool:
    """True iff cl({n}) contains every node, for every node n (restricted to ``nodes``)."""
    keep = frozenset(nodes)
    if not keep:
        return False
    inside = [(t, h) for t, h in _keys(arcs) if h in keep and t <= keep]
    return all(cascade_closure(inside, {n}) >= keep for n in keep)


def _nodes(graph: Graph) -> set[Pillar]:
    nodes = set(graph)
    for targets in graph.values():
        nodes.update(targets)
    return nodes


def _reach(graph: Mapping[Pillar, frozenset[Pillar]], start: Pillar) -> set[Pillar]:
    seen = {start}
    stack = [start]
    while stack:
        for nxt in graph.get(stack.pop(), frozenset()):
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return seen


def is_strongly_connected(graph: Graph, nodes: Iterable[Pillar] | None = None) -> bool:
    """True iff every node of the graph is reachable from every other node.

    ``nodes`` restricts the graph to an induced subgraph (default: all nodes that appear).
    The empty graph is not strongly connected; a single node is.
    """
    keep = set(nodes) if nodes is not None else _nodes(graph)
    if not keep:
        return False
    fwd: dict[Pillar, frozenset[Pillar]] = {
        u: frozenset(v for v in graph.get(u, ()) if v in keep) for u in keep
    }
    rev: dict[Pillar, set[Pillar]] = {u: set() for u in keep}
    for u, vs in fwd.items():
        for v in vs:
            rev[v].add(u)
    start = next(iter(keep))
    rev_f = {u: frozenset(v) for u, v in rev.items()}
    return _reach(fwd, start) == keep and _reach(rev_f, start) == keep


def critical_edges(graph: Graph) -> list[tuple[Pillar, Pillar]]:
    """Edges whose single removal breaks strong connectivity (empty if not connected)."""
    nodes = _nodes(graph)
    base = {u: frozenset(graph.get(u, ())) for u in nodes}
    if not is_strongly_connected(base):
        return []
    out = []
    for u in PILLARS:
        for v in sorted(base.get(u, ()), key=lambda p: p.position):
            pruned = dict(base)
            pruned[u] = base[u] - {v}
            if not is_strongly_connected(pruned, nodes):
                out.append((u, v))
    return out


def sinks_and_sources(graph: Graph) -> tuple[frozenset[Pillar], frozenset[Pillar]]:
    """Pillars with no outgoing edge (sinks) and with no incoming edge (sources)."""
    nodes = _nodes(graph)
    has_out = {u for u in nodes if any(True for _ in graph.get(u, ()))}
    has_in = {v for u in nodes for v in graph.get(u, ())}
    return frozenset(nodes - has_out), frozenset(nodes - has_in)


# Axiom-generated dependency rules (Part VII revised dependency spec) ----------------------


@dataclass(frozen=True)
class DependencyRule:
    """A hyperarc (T, h) generated when every premise in ``requires`` holds.

    h needs an output of AT LEAST ONE member of T (provider(s) -> dependent). ``incidence`` is
    the incidence Inc(k, m) the rule instantiates (the problem of Ax_k arises about pillar m's
    inputs or rules, giving arc pillar(k) -> m), or None for a rule that is not an incidence.
    ``core`` marks membership of D*; non-core rules are reported, not needed.
    """

    tail: frozenset[Pillar]
    head: Pillar
    premise: str
    requires: frozenset[AnyAxiom]
    source: str
    core: bool
    incidence: tuple[Axiom, Pillar] | None = None

    def __post_init__(self) -> None:
        tail, _ = arc_key(self.tail, self.head)
        requires = frozenset(self.requires)
        if not requires or any(not isinstance(a, (Axiom, IncidenceAxiom)) for a in requires):
            raise ValueError("a dependency rule needs at least one axiom premise")
        if self.incidence is not None:
            axiom, target = self.incidence
            if tail != frozenset({axiom.pillar}) or target is not self.head:
                raise ValueError("an incidence Inc(k, m) generates exactly pillar(k) -> m")
            if axiom not in requires:
                raise ValueError("an incidence rule must require its own axiom")
        object.__setattr__(self, "tail", tail)
        object.__setattr__(self, "requires", requires)

    @property
    def key(self) -> ArcKey:
        return self.tail, self.head


def _inc(axiom: Axiom, target: Pillar, premise: str, requires: Iterable[AnyAxiom],
         source: str, core: bool = True) -> DependencyRule:
    return DependencyRule(frozenset({axiom.pillar}), target, premise,
                          frozenset(requires) | {axiom}, source, core, (axiom, target))


_P, _A, _X = Pillar, Axiom, IncidenceAxiom

#: D*: the core rules. Under Ax1..Ax6 plus X1, X2, X3, X5 they generate a strongly connected,
#: cascade-complete hypergraph (Part VII revised dependency spec).
CORE_RULES: tuple[DependencyRule, ...] = (
    *(_inc(_A.Ax6, m, "Ax6", (), "practitioners consume produced resources (Part VI Lem 3.3, 3.4)")
      for m in (_P.F, _P.P, _P.J, _P.I, _P.C)),
    DependencyRule(frozenset({_P.I, _P.C}), _P.J, "Part III Prop 3.6",
                   frozenset({_A.Ax3, _A.Ax4, _A.Ax5}),
                   "loser complies iff ell + sigma >= g, g > 0: recognition or enforcement",
                   core=True),
    _inc(_A.Ax4, _P.F, "Ax4 + Ax1", (_A.Ax1,),
         "settlements must be anticipable (Part I Def 2.2(b)); entrants learn the procedure "
         "only through legitimation (Part IV Lem 3.4, Thm 3.5)"),
    _inc(_A.Ax1, _P.W, "X1", (_X.X1,), "contested productive inputs (Part I)"),
    _inc(_A.Ax2, _P.F, "X2", (_X.X2,), "changing environment hits allocation rules (Part II Ass 3.2)"),
    _inc(_A.Ax3, _P.F, "X3", (_X.X3,), "open-textured allocation rules (Part III Thm 3.3)"),
    _inc(_A.Ax5, _P.F, "X5", (_X.X5,), "tempting allocation rules (Part V Thm 3.4)"),
)

#: Further rules (Part VII Remark 5.12): reported, not needed for interdependence. Each rests on a premise beyond
#: the extended axiom set (stated in ``premise``); ``rules_holding`` skips non-core rules, so
#: none is ever generated for a system.
FURTHER_RULES: tuple[DependencyRule, ...] = (
    _inc(_A.Ax4, _P.P, "X2 + Ax4", (_A.Ax2, _X.X2), "recognition of rule change", core=False),
    _inc(_A.Ax2, _P.J, "X2 + Ax4", (_A.Ax4, _X.X2), "new rules to interpret", core=False),
    _inc(_A.Ax2, _P.I, "X2 + Ax4", (_A.Ax4, _X.X2), "new rules to be made common knowledge",
         core=False),
    _inc(_A.Ax3, _P.P, "precedent (Hart)", (), "interpretation feeds rule change", core=False),
    _inc(_A.Ax4, _P.C, "Ax4 at C's rules", (),
         "an entrant is deterred only once informed of the sanction rule", core=False),
    DependencyRule(frozenset({_P.F, _P.I}), _P.C, "Part V Cor 3.7 conditions",
                   frozenset({_A.Ax1, _A.Ax4, _A.Ax5}),
                   "costly public-good sanctions at large n, no higher-order sanctions",
                   core=False),
)

D_STAR_KEYS: frozenset[ArcKey] = frozenset(r.key for r in CORE_RULES)
#: D0: the core relations generated by Ax1..Ax6 alone (W -> m for m != W, the OR-hyperarc
#: {I, C} -> J, and I -> F); Part VII Thm 4.3.
D0_KEYS: frozenset[ArcKey] = frozenset(
    r.key for r in CORE_RULES if not any(isinstance(a, IncidenceAxiom) for a in r.requires)
)

#: The six single arcs named in the original model brief (kept for comparison only).
BRIEF_ARCS: frozenset[ArcKey] = frozenset(
    arc_key(t, h) for t, h in [(_P.W, _P.C), (_P.P, _P.J), (_P.I, _P.P), (_P.J, _P.F),
                               (_P.F, _P.W), (_P.W, _P.I)]
)


def rules_holding(
    axioms: Iterable[AnyAxiom], rules: Iterable[DependencyRule] = CORE_RULES
) -> tuple[DependencyRule, ...]:
    """The CORE rules whose premises all hold under ``axioms``.

    Non-core (further) rules are never generated, whatever ``axioms`` contains.
    """
    held = frozenset(axioms)
    return tuple(r for r in rules if r.core and r.requires <= held)


def dependency_graph(axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS) -> dict[Pillar, frozenset[Pillar]]:
    """Underlying digraph of the core rules generated under ``axioms`` (default: all)."""
    return underlying_digraph(rules_holding(axioms))


# Governance systems ------------------------------------------------------------------------


@dataclass(frozen=True)
class Practice:
    """A regular activity that discharges the problem generated by axiom ``solves``.

    ``formal`` is True when the activity is attached to a designated office or organization.
    ``source`` holds the citation key(s) supporting the coding.
    """

    description: str
    solves: Axiom
    holders: frozenset[str]
    formal: bool = False
    source: str = ""

    def __post_init__(self) -> None:
        if not isinstance(self.solves, Axiom):
            raise TypeError("Practice.solves must be an Axiom")
        holders = frozenset(self.holders)
        if not holders or any(not isinstance(h, str) or not h for h in holders):
            raise ValueError("a practice needs at least one named holder")
        if not self.description.strip():
            raise ValueError("a practice needs a description")
        object.__setattr__(self, "holders", holders)

    @property
    def pillar(self) -> Pillar:
        return AXIOM_TO_PILLAR[self.solves]


@dataclass(frozen=True)
class GovernanceSystem:
    """A collective that makes and enforces collective decisions (KB Section 4.1).

    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
    over the period studied; it may include the incidence axioms X1, X2, X3, X5. Both are
    coded independently of ``practices``. Dependencies are generated from ``axioms``;
    ``absent_incidences`` records incidences Inc(k, m) OBSERVED not to arise in this system,
    which suppress the arcs they would generate (the route by which a case can falsify D0 or
    interdependence).
    """

    name: str
    persistent: bool
    axioms: frozenset[AnyAxiom]
    practices: tuple[Practice, ...] = ()
    absent_incidences: frozenset[tuple[Axiom, Pillar]] = frozenset()
    note: str = ""

    def __post_init__(self) -> None:
        if not isinstance(self.persistent, bool):
            raise TypeError("persistent must be a bool")
        axioms = frozenset(self.axioms)
        if any(not isinstance(a, (Axiom, IncidenceAxiom)) for a in axioms):
            raise TypeError("axioms must be Axiom or IncidenceAxiom members")
        practices = tuple(self.practices)
        if any(not isinstance(p, Practice) for p in practices):
            raise TypeError("practices must be Practice instances")
        object.__setattr__(self, "axioms", axioms)
        object.__setattr__(self, "practices", practices)
        absent = frozenset(tuple(i) for i in self.absent_incidences)
        if any(len(i) != 2 or not isinstance(i[0], Axiom) or not isinstance(i[1], Pillar)
               for i in absent):
            raise TypeError("absent_incidences must be (Axiom, Pillar) pairs")
        object.__setattr__(self, "absent_incidences", absent)

    def holds(self, axiom: AnyAxiom) -> bool:
        """Predicate for one axiom (Ax1..Ax6 or an incidence axiom X_k)."""
        return axiom in self.axioms

    @property
    def all_axioms_hold(self) -> bool:
        """Ax1..Ax6 all hold (the antecedent of Theorem A)."""
        return all(self.holds(a) for a in Axiom)

    @property
    def extended_axioms_hold(self) -> bool:
        """Ax1..Ax6 and X1, X2, X3, X5 all hold (the antecedent of interdependence)."""
        return EXTENDED_AXIOMS <= self.axioms


def generate_dependencies(
    system: GovernanceSystem, rules: Iterable[DependencyRule] = CORE_RULES
) -> frozenset[ArcKey]:
    """Hyperarcs generated in ``system``: rules whose premises hold, minus absent incidences."""
    return frozenset(
        r.key for r in rules_holding(system.axioms, rules)
        if r.incidence is None or r.incidence not in system.absent_incidences
    )


def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
    roles: dict[str, set[Pillar]] = {}
    for p in system.practices:
        for h in p.holders:
            roles.setdefault(h, set()).add(p.pillar)
    return {h: frozenset(ps) for h, ps in roles.items()}


def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.

    'fused' if some formal holder of the pillar also holds another pillar; 'formal
    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
    """
    practices = [p for p in system.practices if p.pillar is pillar]
    if not practices:
        return None
    formal_holders = {h for p in practices if p.formal for h in p.holders}
    if not formal_holders:
        return INFORMAL
    formal_roles: dict[str, set[Pillar]] = {}
    for p in system.practices:
        if p.formal:
            for h in p.holders:
                formal_roles.setdefault(h, set()).add(p.pillar)
    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
        return FUSED
    return FORMAL


@dataclass(frozen=True)
class Derivation:
    """Result of the lemma for one axiom: required pillar and its realized form."""

    axiom: Axiom
    pillar: Pillar
    form: RealizedForm | None
    practices: tuple[Practice, ...]

    @property
    def realized(self) -> bool:
        return self.form is not None


def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
    """For each axiom that holds, the pillar it requires and how that pillar is realized.

    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
    """
    out: dict[Axiom, Derivation] = {}
    for axiom in Axiom:
        if not system.holds(axiom):
            continue
        pillar = AXIOM_TO_PILLAR[axiom]
        out[axiom] = Derivation(
            axiom=axiom,
            pillar=pillar,
            form=realized_form(system, pillar),
            practices=tuple(p for p in system.practices if p.solves is axiom),
        )
    return out


# Proposition A and interdependence --------------------------------------------------------


@dataclass(frozen=True)
class PropositionAResult:
    """Outcome of checking Proposition A on one coded system (Part VII Cor 5.5, Thm 5.10).

    ``struct``: all six pillars realized (Thm 4.3) AND every D0 relation generated (Cor 5.5,
    from Ax1..Ax6). ``interdependent``: all six realized and the generated hypergraph strongly
    connected (underlying digraph) AND cascade-complete (Thm 5.10, from Ax1..Ax6 plus
    Assumptions 5.6 to 5.9, i.e. X1, X2, X3, X5; the role of each premise is Prop 5.11).
    ``holds`` is Proposition A in full: struct AND interdependent.

    ``counterexample``: persistent, the extended axiom set holds, yet ``holds`` is False.
    ``struct_counterexample``: persistent, Ax1..Ax6 hold, yet ``struct`` is False.
    """

    system: str
    antecedent: bool
    realized: frozenset[Pillar]
    missing: frozenset[Pillar]
    dependencies: frozenset[ArcKey]
    missing_dependencies: frozenset[ArcKey]
    strongly_connected: bool
    cascade_complete: bool
    struct: bool
    interdependence_antecedent: bool
    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)

    @property
    def interdependent(self) -> bool:
        return not self.missing and self.strongly_connected and self.cascade_complete

    @property
    def holds(self) -> bool:
        return self.struct and self.interdependent

    @property
    def struct_counterexample(self) -> bool:
        return self.antecedent and not self.struct

    @property
    def counterexample(self) -> bool:
        return self.interdependence_antecedent and not self.holds


def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
    """Check Proposition A (struct and interdependence) on ``system`` (Part VII; KB 4.3).

    A D0 relation is demanded when its head and every tail member are realized.
    """
    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
    deps = generate_dependencies(system)
    needed = frozenset((t, h) for t, h in D0_KEYS if h in realized and t <= realized)
    missing_deps = needed - deps
    return PropositionAResult(
        system=system.name,
        antecedent=system.persistent and system.all_axioms_hold,
        realized=realized,
        missing=frozenset(PILLARS) - realized,
        dependencies=deps,
        missing_dependencies=missing_deps,
        strongly_connected=is_strongly_connected(underlying_digraph(deps), realized),
        cascade_complete=is_cascade_complete(deps, realized),
        struct=realized == frozenset(PILLARS) and not missing_deps,
        interdependence_antecedent=system.persistent and system.extended_axioms_hold,
        derivations=derive_functions(system),
    )


def formal_system(
    name: str,
    holders: Mapping[Pillar, Iterable[str]],
    persistent: bool = True,
    source: str = "",
    axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS,
) -> GovernanceSystem:
    """A persistent system whose pillars are held by formal organizations.

    An actor listed under several pillars is fused. By default the extended axiom set is
    coded as holding: an assumption of the stylized model, not an observation. Used for regime
    profiles and counter-models.
    """
    practices = tuple(
        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
                 frozenset(hs), formal=True, source=source)
        for m, hs in holders.items()
        if hs
    )
    return GovernanceSystem(name, persistent, frozenset(axioms), practices)


# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
# Each codes the extended axiom set as holding. The X1, X2, X3, X5 codings are QUALITATIVE
# readings of the ethnography (sources in X_CODING_SOURCES), each open to the falsifier
# stated on IncidenceAxiom.


def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)


NUER = GovernanceSystem(
    name="Nuer ('ordered anarchy')",
    persistent=True,
    axioms=EXTENDED_AXIOMS,
    practices=(
        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
                  {"prophets", "lineages"}, "evanspritchard1940"),
        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
                  {"agnatic kin"}, "evanspritchard1940"),
        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
                  "evanspritchard1940"),
    ),
    note="no office holds coercive authority; functions exist without separation",
)

JU_HOANSI = GovernanceSystem(
    name="Ju/'hoansi (!Kung)",
    persistent=True,
    axioms=EXTENDED_AXIOMS,
    practices=(
        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
                  {"hunters", "camp members"}, "lee2013; marshall1976"),
        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
                  {"camp members"}, "lee2013"),
        _informal("disputes talked out with kin mediators", Axiom.Ax3,
                  {"kin mediators"}, "lee1979; wiessner2005"),
        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
                  {"healers", "camp members"}, "marshall1976"),
        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
                  {"camp members"}, "wiessner2005; lee2013"),
        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
    ),
    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
)

OSTROM_COMMONS = GovernanceSystem(
    name="Ostrom commons (design principles)",
    persistent=True,
    axioms=EXTENDED_AXIOMS,
    practices=(
        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
                  {"appropriators"}, "ostrom1990"),
        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
                  {"appropriators"}, "ostrom1990; cox2010"),
        _informal("shared norms; minimal recognition of rights to organize (DP7)",
                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),
        _informal("monitoring and graduated sanctions by appropriators (DP4, DP5)",
                  Axiom.Ax5, {"appropriators"}, "ostrom1990; cox2010"),
        _informal("appropriation and maintenance labor", Axiom.Ax6, {"appropriators"},
                  "ostrom1990"),
    ),
    note="checks in minimal form; monitors are appropriators or accountable to them",
)

CONSENSUS_VILLAGE = GovernanceSystem(
    name="Consensus village (stylized)",
    persistent=True,
    axioms=EXTENDED_AXIOMS,
    practices=(
        _informal("household plots; reciprocal labor exchange; sharing norms", Axiom.Ax1,
                  {"households"}, "sahlins1972"),
        _informal("consensus meeting of adults", Axiom.Ax2, {"village meeting"},
                  "clastres1987; boehm1999"),
        _informal("elders mediate disputes", Axiom.Ax3, {"elders"}, "boehm1999"),
        _informal("ritual and myth; moral talk", Axiom.Ax4, {"village meeting", "elders"},
                  "boehm1999"),
        _informal("gossip, shunning, ostracism of would-be dominants", Axiom.Ax5,
                  {"village meeting"}, "boehm1999; woodburn1982"),
        _informal("gardening and household labor", Axiom.Ax6, {"households"},
                  "sahlins1972"),
    ),
    note="stylized composite; reverse dominance hierarchy",
)

HARD_CASES: tuple[GovernanceSystem, ...] = (NUER, JU_HOANSI, OSTROM_COMMONS, CONSENSUS_VILLAGE)

_X1, _X2, _X3, _X5 = IncidenceAxiom
#: Qualitative codings of the incidence axioms for the hard cases (Part VII), with sources.
X_CODING_SOURCES: dict[str, dict[IncidenceAxiom, str]] = {
    NUER.name: {
        _X1: "cattle and grazing rights (evanspritchard1940)",
        _X2: "norms adjusted by negotiation among lineages (evanspritchard1940)",
        _X3: "cattle compensation fixed through the leopard-skin chief (evanspritchard1940)",
        _X5: "feud over cattle (evanspritchard1940)",
    },
    JU_HOANSI.name: {
        _X1: "kin-based n!ore rights to territory and water (lee2013)",
        _X2: "camp talk and fission (lee2013)",
        _X3: "disputes over sharing talked out (lee2013; wiessner2005)",
        _X5: "criticism of failures to share (wiessner2005)",
    },
    OSTROM_COMMONS.name: {
        _X1: "boundary and appropriation rules (ostrom1990)",
        _X2: "users modify their rules (ostrom1990)",
        _X3: "conflict-resolution arenas (ostrom1990; cox2010)",
        _X5: "monitoring and graduated sanctions (ostrom1990)",
    },
    CONSENSUS_VILLAGE.name: {
        _X1: "household plots under sharing norms (sahlins1972)",
        _X2: "seasonal re-arrangement (graeber2021)",
        _X3: "elders mediate residual disputes (boehm1999)",
        _X5: "sharing enforced against hoarders (boehm1999)",
    },
}


# Axiom independence fixtures (Part VII spec, item 7). ---------------------------------------

#: Consistency model: the extended axiom set holds and all six pillars are realized (the
#: consensus village coding).
BASELINE_MODEL: GovernanceSystem = CONSENSUS_VILLAGE


def without_axiom(axiom: AnyAxiom, base: GovernanceSystem = BASELINE_MODEL) -> GovernanceSystem:
    """``base`` with one axiom removed; for Ax_k the practices solving Ax_k are removed too."""
    practices = base.practices
    if isinstance(axiom, Axiom):
        practices = tuple(p for p in practices if p.solves is not axiom)
    return GovernanceSystem(
        name=f"{base.name} without {axiom.name} ({axiom.label})",
        persistent=base.persistent,
        axioms=base.axioms - {axiom},
        practices=practices,
        absent_incidences=base.absent_incidences,
        note="hypothetical: one axiom removed",
    )


#: Part VII R1, the k = 4 independence model: innate rules, no initiation, a fine d >= g on
#: defiance of a determination (so rulings bind through C alone), ell = 0, Pr(Pi) = 1;
#: Impl_I fails.
R1_AX4_MODEL = GovernanceSystem(
    name="R1: independence model for Ax4",
    persistent=True,
    axioms=BASELINE_MODEL.axioms - {Axiom.Ax4},
    practices=tuple(p for p in BASELINE_MODEL.practices if p.solves is not Axiom.Ax4) + (
        Practice("fine d >= g on defiance of a determination", Axiom.Ax5,
                 frozenset({"village meeting"}), source="Part VII R1"),
    ),
    note="innate rules, no initiation, ell = 0, Pr(Pi) = 1; Impl_I fails",
)

#: For each k: persistent, Ax_k removed, pillar k missing (k = 4 is the R1 model). Theorem A's
#: antecedent is false, so none is a counterexample; each shows pillar k is not forced by the
#: other five axioms.
AXIOM_INDEPENDENCE: dict[Axiom, GovernanceSystem] = {
    a: (R1_AX4_MODEL if a is Axiom.Ax4 else without_axiom(a)) for a in Axiom
}


# Part VII Prop 4.4(a) model and its Lemma 5.4 variant (Ax1..Ax6, no incidence axioms). ------

_M = frozenset({"members"})
PROP_4_4A_MODEL = GovernanceSystem(
    name="Prop 4.4(a) model",
    persistent=True,
    axioms=frozenset(Axiom),
    practices=(
        Practice("plot claimed each period by the most recent entrant and one other member; "
                 "assigned by lot", Axiom.Ax1, _M, source="Part VII Prop 4.4(a)"),
        Practice("members make their own rules; the longest-serving member is replaced every "
                 "L periods", Axiom.Ax2, _M, source="Part VII Prop 4.4(a)"),
        Practice("the lot determines each residual dispute", Axiom.Ax3, _M,
                 source="Part VII Prop 4.4(a)"),
        Practice("the lot is presented as rightful at initiation (ell from I); entrants do not "
                 "know the rules at entry; no forgetting", Axiom.Ax4, _M,
                 source="Part VII Prop 4.4(a)"),
        Practice("camp chores rule with fine d; members best-respond", Axiom.Ax5, _M,
                 source="Part VII Prop 4.4(a)"),
        Practice("each member forages alone at any campsite", Axiom.Ax6, _M,
                 source="Part VII Prop 4.4(a)"),
    ),
    note="struct holds, interdependence fails: no arc into W (Prop 5.11(a))",
)

#: Lemma 5.4 variant: the fine d >= g also attaches to defiance of a determination, so J is
#: served by C as well as I; neither I -> J nor C -> J alone is forced (the OR-hyperarc).
PROP_4_4A_VARIANT = GovernanceSystem(
    name="Prop 4.4(a) model, Lemma 5.4 variant",
    persistent=True,
    axioms=frozenset(Axiom),
    practices=PROP_4_4A_MODEL.practices + (
        Practice("fine d >= g on defiance of a determination", Axiom.Ax5, _M,
                 source="Part VII Lemma 5.4"),
    ),
    note="witness that neither I -> J nor C -> J is forced",
)


# Admissible assignments (Part VII F5) ----------------------------------------------------


def is_admissible(
    system: GovernanceSystem,
    members: Iterable[str],
    organizations: Mapping[str, Iterable[str]] | None = None,
    dispute_parties: Mapping[str, Iterable[str]] | None = None,
) -> bool:
    """Admissible Lambda (Part VII F5), on the coded information available.

    (i) every assigned agent is a member or an organization of members (whose consumption
    is counted); (ii) no party to a residual dispute alone controls its determination: a J
    practice with a single holder may not have that holder, or any of its members, among
    ``dispute_parties[practice.description]``; (iii) rule-making (P) practices are the
    members' own, which (i) already requires of their holders.
    """
    mem = frozenset(members)
    orgs = {k: frozenset(v) for k, v in (organizations or {}).items()}
    parties = {k: frozenset(v) for k, v in (dispute_parties or {}).items()}
    for p in system.practices:
        for h in p.holders:
            if h not in mem and not (h in orgs and orgs[h] and orgs[h] <= mem):
                return False
        if p.solves is Axiom.Ax3 and len(p.holders) == 1:
            (h,) = p.holders
            involved = parties.get(p.description, frozenset())
            if h in involved or orgs.get(h, frozenset()) & involved:
                return False
    return True
