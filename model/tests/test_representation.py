import itertools

import pytest

from beast_system.capture import (
    a_does_not_imply_b,
    assess,
    corner_polities,
    fused_polity,
    plural_polity,
)
from beast_system.indices import coalition_integration, integration_statistic
from beast_system.necessity import (
    AXIOM_INDEPENDENCE,
    BASELINE_MODEL,
    EXTENDED_AXIOMS,
    HARD_CASES,
    JU_HOANSI,
    GovernanceSystem,
    check_proposition_a,
)
from beast_system.pillars import PILLARS, Axiom
from beast_system.regimes import regime_profiles
from beast_system.representation import (
    M_LABELS,
    FormalizedStructure,
    drop,
    equivalent_A,
    in_formalized_class,
    make_structure,
    merge,
    minimal_record,
    preserved_quantities,
    record_from_polity,
    represent,
    representable,
    structurally_equal,
)

F, P, J, I, C, W = PILLARS


def _all_records():
    records = [(s.name, minimal_record(s)) for s in HARD_CASES]
    records += [(p.label, record_from_polity(p.polity)) for p in regime_profiles()]
    records += [(f"corner {k}", record_from_polity(p)) for k, p in corner_polities().items()]
    records += [(f"independence {a.name}", minimal_record(s)) for a, s in AXIOM_INDEPENDENCE.items()]
    no_x = GovernanceSystem("baseline without X", True, frozenset(Axiom), BASELINE_MODEL.practices)
    absent = GovernanceSystem("absent Inc(Ax5, F)", True, EXTENDED_AXIOMS, JU_HOANSI.practices,
                              frozenset({(Axiom.Ax5, F)}))
    no_c = GovernanceSystem("no sanction practice", True, EXTENDED_AXIOMS,
                            tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5))
    records += [(s.name, minimal_record(s)) for s in (no_x, absent, no_c)]
    return records


@pytest.mark.parametrize("name,record", _all_records(), ids=[n for n, _ in _all_records()])
def test_representable_iff_proposition_a(name, record):
    assert representable(record) == check_proposition_a(record.system).holds


def test_hard_cases_and_regimes_are_representable():
    for s in HARD_CASES:
        assert representable(minimal_record(s)), s.name
    for p in regime_profiles():
        assert representable(record_from_polity(p.polity)), p.label


@pytest.mark.parametrize("axiom", list(Axiom), ids=lambda a: a.name)
def test_independence_models_are_not_representable_empty_layer(axiom):
    F_ = represent(minimal_record(AXIOM_INDEPENDENCE[axiom]))
    assert not F_.holders(axiom.pillar.name)
    assert not in_formalized_class(F_).f1


def test_baseline_without_x_fails_only_f4():
    no_x = GovernanceSystem("baseline without X", True, frozenset(Axiom), BASELINE_MODEL.practices)
    m = in_formalized_class(represent(minimal_record(no_x)))
    assert m.f1 and m.f2 and m.f3 and not m.f4


@pytest.mark.parametrize("polity", [plural_polity(), fused_polity()]
                         + list(corner_polities().values()), ids=lambda p: p.name)
def test_represent_preserves_quantities(polity):
    coalitions = None
    if polity.name == "consensus grand coalition":
        members = frozenset(a for a in polity.normalized_shares[F] if a.startswith("member"))
        coalitions = {members: {m: 1.0 for m in PILLARS}}
    F_ = represent(record_from_polity(polity, coalitions))
    q = preserved_quantities(F_)
    a = assess(polity)
    assert q.H == pytest.approx({m.name: a.H[m] for m in PILLARS})
    assert q.U == pytest.approx(a.U)
    assert q.I == pytest.approx(a.I)  # these polities derive C from coalitions
    assert q.cap == a.prop_b.holds
    assert q.inter == a.prop_a.interdependent


def test_represent_regime_quantities_h_u_inter():
    for p in regime_profiles():
        F_ = represent(record_from_polity(p.polity))
        q = preserved_quantities(F_)
        a = assess(p.polity)
        assert q.U == pytest.approx(a.U) and q.inter == a.prop_a.interdependent
        singleton_I = integration_statistic(coalition_integration(p.polity.normalized_shares))
        assert q.I == pytest.approx(singleton_I)


def _relabel(F_: FormalizedStructure, phi: dict[str, str]) -> FormalizedStructure:
    return FormalizedStructure(
        actors=tuple(sorted(phi[v] for v in F_.actors)), pillars=F_.pillars,
        roles={phi[v]: ps for v, ps in F_.roles.items()},
        layers=F_.layers,
        shares={m: {phi[v]: x for v, x in s.items()} for m, s in F_.shares.items()},
        contestability=F_.contestability, weights=F_.weights,
        kappa={frozenset(phi[v] for v in S): row for S, row in F_.kappa.items()},
        links=frozenset((phi[a], phi[b], m) for a, b, m in F_.links), arcs=F_.arcs,
    )


def test_equivalent_a_under_actor_bijection_preserves_quantities():
    for polity in (fused_polity(), plural_polity(), regime_profiles()[1].polity):
        F_ = represent(record_from_polity(polity))
        phi = {v: f"x{k:03d}" for k, v in enumerate(reversed(F_.actors))}
        G_ = _relabel(F_, phi)
        assert equivalent_A(F_, G_)
        q1, q2 = preserved_quantities(F_), preserved_quantities(G_)
        assert q1.H == pytest.approx(q2.H) and q1.U == pytest.approx(q2.U)
        assert q1.C == pytest.approx(q2.C) and q1.I == pytest.approx(q2.I)
        assert (q1.cap, q1.inter) == (q2.cap, q2.inter)
    F_ = represent(record_from_polity(fused_polity()))
    changed = FormalizedStructure(**{**F_.__dict__, "contestability":
                                     {**F_.contestability, "J": 0.5}})
    assert not equivalent_A(F_, changed)
    no_link = FormalizedStructure(**{**F_.__dict__, "links": frozenset()})
    assert not equivalent_A(F_, no_link)


@pytest.mark.parametrize("axiom", list(Axiom), ids=lambda a: a.name)
def test_drop_makes_baseline_and_independence_model_indistinguishable(axiom):
    k = axiom.pillar.name
    base = represent(minimal_record(BASELINE_MODEL))
    indep = represent(minimal_record(AXIOM_INDEPENDENCE[axiom]))
    assert structurally_equal(drop(base, k), drop(indep, k))
    assert check_proposition_a(BASELINE_MODEL).holds
    assert not check_proposition_a(AXIOM_INDEPENDENCE[axiom]).holds


def _merge_pair(m: str, n: str, lam: float):
    others = {p: {"a": 0.5, "b": 0.5} for p in M_LABELS if p not in (m, n)}
    q = {p: 0.3 for p in M_LABELS}
    g1 = make_structure({**others, m: {"a": 1.0, "b": 0.0}, n: {"a": 0.0, "b": 1.0}}, q)
    g2 = make_structure({**others, m: {"a": lam, "b": 1 - lam}, n: {"a": lam, "b": 1 - lam}}, q)
    return g1, g2


@pytest.mark.parametrize("lam", [0.2, 0.5, 0.7])
@pytest.mark.parametrize("m,n", list(itertools.combinations(M_LABELS, 2)))
def test_merge_makes_distinct_systems_indistinguishable(m, n, lam):
    g1, g2 = _merge_pair(m, n, lam)
    assert structurally_equal(merge(g1, m, n, lam), merge(g2, m, n, lam))
    q1, q2 = preserved_quantities(g1), preserved_quantities(g2)
    assert q1.H[m] == 1.0 and q2.H[m] == pytest.approx(lam**2 + (1 - lam) ** 2)
    assert q1.U != pytest.approx(q2.U)
    assert q1.C[frozenset((m, n))] == 0.0
    assert q2.C[frozenset((m, n))] == pytest.approx(max(lam, 1 - lam))
    assert q1.I != pytest.approx(q2.I)


def test_coarsening_validation():
    F_ = represent(minimal_record(BASELINE_MODEL))
    with pytest.raises(ValueError):
        drop(F_, "Z")
    with pytest.raises(ValueError):
        merge(F_, "F", "F", 0.5)
    with pytest.raises(ValueError):
        merge(F_, "F", "P", 1.5)
    merged = merge(F_, "F", "P", 0.5)
    assert merged.pillars == ("F+P", "J", "I", "C", "W")
    assert sum(merged.weights.values()) == pytest.approx(1.0)
    assert not in_formalized_class(merged).holds  # coarsened label set leaves the class


def test_counter_model_images_both_in_class():
    cm = a_does_not_imply_b()
    assert cm.demonstrates_non_implication
    assert representable(record_from_polity(plural_polity()))
    assert representable(record_from_polity(fused_polity()))


def test_coded_record_domain_is_enforced():
    from beast_system.representation import CodedRecord

    good = minimal_record(BASELINE_MODEL)
    q = good.contestability
    with pytest.raises(ValueError):
        CodedRecord(BASELINE_MODEL, {}, q)  # implemented pillars without shares
    with pytest.raises(ValueError):
        CodedRecord(BASELINE_MODEL, {**good.shares, F: {"households": 0.5}}, q)
    with pytest.raises(ValueError):
        CodedRecord(BASELINE_MODEL, good.shares, q, weights={m: 0.0 for m in PILLARS})
    with pytest.raises(ValueError):
        CodedRecord(BASELINE_MODEL, good.shares, {F: 0.5})
    with pytest.raises(TypeError):
        CodedRecord(BASELINE_MODEL, good.shares, q, coalitions={"S": {F: 0.5}})
    with pytest.raises(ValueError):
        CodedRecord(BASELINE_MODEL, good.shares, q,
                    coalitions={frozenset({"elders"}): {F: 1.5}})
    indep = AXIOM_INDEPENDENCE[Axiom.Ax1]
    with pytest.raises(ValueError):  # share for the unimplemented pillar F
        CodedRecord(indep, {**minimal_record(indep).shares, F: {"households": 1.0}}, q)


def test_theorem_on_random_well_formed_records():
    import numpy as np

    from beast_system.necessity import role_map
    from beast_system.pillars import IncidenceAxiom
    from beast_system.representation import CodedRecord

    rng = np.random.default_rng(42)
    axioms_all = list(EXTENDED_AXIOMS)
    hits = {True: 0, False: 0}
    for trial in range(300):
        keep = frozenset(a for a in axioms_all if rng.uniform() < 0.9)
        practices = tuple(p for p in JU_HOANSI.practices
                          if p.solves in keep and rng.uniform() < 0.95)
        absent = frozenset({(Axiom.Ax6, C)}) if rng.uniform() < 0.1 else frozenset()
        system = GovernanceSystem(f"random {trial}", True, keep, practices, absent)
        roles = role_map(system)
        shares = {}
        for m in PILLARS:
            hs = sorted(a for a, ps in roles.items() if m in ps)
            if hs:
                w = rng.dirichlet(np.ones(len(hs)))
                shares[m] = dict(zip(hs, w / w.sum()))
        weights = dict(zip(PILLARS, rng.dirichlet(np.ones(6))))
        actors = sorted(roles)
        coalitions = {frozenset(rng.choice(actors, size=min(2, len(actors)), replace=False)):
                      {m: float(rng.uniform()) for m in PILLARS}} if actors else None
        rec = CodedRecord(system, shares, {m: float(rng.uniform()) for m in PILLARS},
                          weights=weights, coalitions=coalitions)
        holds = check_proposition_a(system).holds
        assert representable(rec) == holds, trial
        hits[holds] += 1
    assert hits[True] > 10 and hits[False] > 10
    assert IncidenceAxiom.X1 in EXTENDED_AXIOMS


def test_class_check_rejects_malformed_structures():
    F_ = represent(minimal_record(BASELINE_MODEL))
    assert in_formalized_class(F_).holds
    bad = [
        {"contestability": {}},
        {"shares": {**F_.shares, "F": {**F_.shares["F"], "ghost": 0.0}}},
        {"shares": {**F_.shares, "F": {v: float("nan") for v in F_.actors}}},
        {"layers": {**F_.layers, "F": F_.layers["F"][:-1]}},
        {"roles": {**F_.roles, "ghost": frozenset()}},
    ]
    for change in bad:
        m = in_formalized_class(FormalizedStructure(**{**F_.__dict__, **change}))
        assert not (m.f1 or m.f2 or m.f3 or m.f4), change


def test_equivalence_is_strict_on_domain_and_transports_kappa():
    g = make_structure({p: {"a": 0.5, "b": 0.5} for p in M_LABELS}, {p: 0.3 for p in M_LABELS},
                       kappa={frozenset({"a"}): {"F": 0.9}, frozenset({"b"}): {"F": 0.1}})
    swapped = FormalizedStructure(**{**g.__dict__, "kappa": {frozenset({"a"}): {"F": 0.1},
                                                             frozenset({"b"}): {"F": 0.9}}})
    assert equivalent_A(g, swapped)  # a <-> b is a valid bijection here
    pinned = make_structure({**{p: {"a": 0.5, "b": 0.5} for p in M_LABELS},
                             "P": {"a": 0.7, "b": 0.3}}, {p: 0.3 for p in M_LABELS},
                            kappa={frozenset({"a"}): {"F": 0.9}, frozenset({"b"}): {"F": 0.1}})
    pinned_swapped = FormalizedStructure(**{**pinned.__dict__, "kappa": swapped.kappa})
    assert not equivalent_A(pinned, pinned_swapped)  # same kappa rows, wrong members
    extra = FormalizedStructure(**{**g.__dict__, "weights": {**g.weights, "Z": 0.0}})
    assert not equivalent_A(g, extra)


def test_representable_is_total_on_empty_and_bad_coalitions():
    from beast_system.representation import CodedRecord

    empty = GovernanceSystem("empty", True, EXTENDED_AXIOMS, ())
    rec = CodedRecord(empty, {}, {m: 0.5 for m in PILLARS})
    assert not representable(rec) and not check_proposition_a(empty).holds
    good = minimal_record(BASELINE_MODEL)
    with pytest.raises(TypeError):
        CodedRecord(BASELINE_MODEL, good.shares, good.contestability,
                    coalitions={frozenset({42}): {F: 0.5}})
    with pytest.raises(ValueError):
        CodedRecord(BASELINE_MODEL, good.shares, good.contestability,
                    coalitions={frozenset({"stranger"}): {F: 0.5}})


def test_well_formed_checks_hyperarc_domain():
    from beast_system.representation import well_formed

    F_ = represent(minimal_record(BASELINE_MODEL))
    assert well_formed(F_)
    for arc in [(frozenset({"Z"}), "F"), (frozenset({"F"}), "Z"), (frozenset({"F"}), "F"),
                (frozenset(), "F")]:
        G_ = FormalizedStructure(**{**F_.__dict__, "arcs": F_.arcs | {arc}})
        assert not well_formed(G_) and not in_formalized_class(G_).holds, arc
