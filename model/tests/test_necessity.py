import pytest

from beast_system.necessity import (
    AXIOM_INDEPENDENCE,
    BASELINE_MODEL,
    BRIEF_ARCS,
    CORE_RULES,
    D0_KEYS,
    D_STAR_KEYS,
    EXTENDED_AXIOMS,
    FORMAL,
    FURTHER_RULES,
    FUSED,
    HARD_CASES,
    INFORMAL,
    JU_HOANSI,
    NUER,
    DependencyRule,
    GovernanceSystem,
    Practice,
    arc_key,
    cascade_closure,
    check_proposition_a,
    critical_edges,
    derive_functions,
    formal_system,
    generate_dependencies,
    is_cascade_complete,
    is_strongly_connected,
    role_map,
    rules_holding,
    sinks_and_sources,
    underlying_digraph,
    without_axiom,
)
from beast_system.pillars import PILLARS, Axiom, IncidenceAxiom, Pillar

F, P, J, I, C, W = PILLARS
X1, X2, X3, X5 = IncidenceAxiom


# Theorem A ---------------------------------------------------------------------------------


@pytest.mark.parametrize("system", HARD_CASES, ids=lambda s: s.name)
def test_theorem_a_on_hard_cases(system):
    result = check_proposition_a(system)
    assert result.antecedent
    assert result.holds and not result.counterexample
    assert result.realized == frozenset(PILLARS)
    derivs = derive_functions(system)
    assert {d.pillar for d in derivs.values()} == set(PILLARS)
    assert all(d.form == INFORMAL for d in derivs.values())


def test_role_map_is_derived_from_practices():
    roles = role_map(JU_HOANSI)
    assert Pillar.C in roles["camp members"] and Pillar.P in roles["camp members"]


def test_missing_axiom_drops_pillar_and_is_not_a_counterexample():
    # A perfectly cooperative collective: Ax5 fails and there is no sanction practice.
    practices = tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5)
    system = GovernanceSystem("no defection", True, EXTENDED_AXIOMS - {Axiom.Ax5}, practices)
    derivs = derive_functions(system)
    assert Axiom.Ax5 not in derivs and len(derivs) == 5
    result = check_proposition_a(system)
    assert not result.antecedent
    assert result.missing == {C}
    assert not result.holds and not result.counterexample


def test_falsifier_is_reported():
    # All axioms coded as holding, persistent, but no sanction practice: a counterexample.
    practices = tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5)
    system = GovernanceSystem("hypothetical", True, EXTENDED_AXIOMS, practices)
    result = check_proposition_a(system)
    assert result.counterexample and result.struct_counterexample
    assert derive_functions(system)[Axiom.Ax5].form is None


def test_non_persistent_system_does_not_trigger_theorem():
    system = GovernanceSystem("short-lived", False, EXTENDED_AXIOMS, ())
    assert not check_proposition_a(system).antecedent
    assert not check_proposition_a(system).counterexample
    assert not check_proposition_a(system).struct_counterexample


def test_fused_and_formal_forms():
    system = formal_system("toy", {F: ["Treasury"], P: ["Crown"], J: ["Crown"], I: ["Church"],
                                   C: ["Crown"], W: ["Peasants"]})
    derivs = derive_functions(system)
    assert derivs[Axiom.Ax2].form == FUSED
    assert derivs[Axiom.Ax5].form == FUSED
    assert derivs[Axiom.Ax1].form == FORMAL
    assert check_proposition_a(system).holds


def test_practice_and_system_validation():
    with pytest.raises(ValueError):
        Practice("x", Axiom.Ax1, frozenset())
    with pytest.raises(TypeError):
        Practice("x", Pillar.F, frozenset({"a"}))  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        GovernanceSystem("bad", True, frozenset({"Ax1"}))  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        GovernanceSystem("bad", True, EXTENDED_AXIOMS, (), frozenset({(F, W)}))


def test_missing_d0_relation_is_a_counterexample():
    system = GovernanceSystem("no Inc(Ax6, C)", True, EXTENDED_AXIOMS, JU_HOANSI.practices,
                              frozenset({(Axiom.Ax6, C)}))
    result = check_proposition_a(system)
    assert result.realized == frozenset(PILLARS)
    assert result.missing_dependencies == {arc_key(W, C)}
    assert not result.struct and result.struct_counterexample and result.counterexample


# Generated dependency hypergraph -------------------------------------------------------------


def test_rules_are_documented_and_traced_to_axioms():
    for r in CORE_RULES + FURTHER_RULES:
        assert r.head not in r.tail and r.premise and r.source and r.requires
    assert len({r.key for r in CORE_RULES}) == len(CORE_RULES)
    # Every incidence axiom generates exactly one core arc, pillar(base) -> target.
    for x in IncidenceAxiom:
        rules = [r for r in CORE_RULES if x in r.requires]
        assert len(rules) == 1
        assert rules[0].key == arc_key(x.base.pillar, x.target)
        assert rules[0].incidence == (x.base, x.target)


def test_d_star_and_d0_contents():
    w_arcs = {arc_key(W, m) for m in (F, P, J, I, C)}
    assert D0_KEYS == w_arcs | {arc_key({I, C}, J), arc_key(I, F)}
    assert D_STAR_KEYS == D0_KEYS | {arc_key(F, W), arc_key(P, F), arc_key(J, F),
                                     arc_key(C, F)}
    assert arc_key(C, J) not in D_STAR_KEYS and arc_key(I, J) not in D_STAR_KEYS
    assert frozenset(r.key for r in rules_holding(EXTENDED_AXIOMS)) == D_STAR_KEYS


def test_d0_alone_is_not_strongly_connected():
    assert not is_strongly_connected(underlying_digraph(D0_KEYS))
    assert not is_cascade_complete(D0_KEYS)


def test_d_star_is_strongly_connected_and_cascade_complete():
    assert is_strongly_connected(underlying_digraph(D_STAR_KEYS))
    assert is_cascade_complete(D_STAR_KEYS)
    for n in PILLARS:
        assert cascade_closure(D_STAR_KEYS, {n}) == frozenset(PILLARS), n


def test_without_x5_strongly_connected_but_c_isolated():
    arcs = generate_dependencies(without_axiom(X5))
    assert arc_key(C, F) not in arcs
    assert is_strongly_connected(underlying_digraph(arcs))
    assert cascade_closure(arcs, {C}) == {C}
    assert not is_cascade_complete(arcs)
    # Splitting the OR-hyperarc would wrongly put J in cl({C}).
    split = (arcs - {arc_key({I, C}, J)}) | {arc_key(C, J), arc_key(I, J)}
    assert J in cascade_closure(split, {C})


def test_without_x1_no_arc_into_w():
    arcs = generate_dependencies(without_axiom(X1))
    graph = underlying_digraph(arcs)
    assert not is_strongly_connected(graph)
    assert W in sinks_and_sources(graph)[1]
    # F -> W is the only arc into W anywhere in the catalogue.
    into_w = {r.key for r in CORE_RULES + FURTHER_RULES if r.head is W}
    assert into_w == {arc_key(F, W)}


def test_without_x2_p_has_no_out_arc():
    graph = underlying_digraph(generate_dependencies(without_axiom(X2)))
    assert not graph[P]
    assert not is_strongly_connected(graph)


def test_replacing_x3_by_precedent_keeps_strong_connectivity():
    precedent = next(r for r in FURTHER_RULES if r.premise == "precedent (Hart)")
    arcs = (D_STAR_KEYS - {arc_key(J, F)}) | {precedent.key}
    assert precedent.key == arc_key(J, P)
    assert is_strongly_connected(underlying_digraph(arcs))


@pytest.mark.parametrize("rule", CORE_RULES, ids=lambda r: f"{'+'.join(sorted(t.name for t in r.tail))}->{r.head.name}")
def test_removing_a_premise_removes_its_arc(rule):
    for premise in rule.requires:
        assert rule.key not in generate_dependencies(without_axiom(premise))
    assert rule.key in generate_dependencies(BASELINE_MODEL)


@pytest.mark.parametrize("system", HARD_CASES, ids=lambda s: s.name)
def test_interdependence_holds_for_every_axiom_built_fixture(system):
    result = check_proposition_a(system)
    assert result.interdependence_antecedent
    assert result.strongly_connected and result.cascade_complete and result.interdependent
    assert result.dependencies == D_STAR_KEYS


def test_absent_incidence_is_an_interdependence_counterexample():
    system = GovernanceSystem("no Inc(Ax5, F)", True, EXTENDED_AXIOMS, JU_HOANSI.practices,
                              frozenset({(Axiom.Ax5, F)}))
    result = check_proposition_a(system)
    assert result.struct and not result.struct_counterexample  # struct only needs D0
    assert not result.interdependent and not result.holds and result.counterexample


def test_brief_relations_alone_are_not_strongly_connected():
    brief = underlying_digraph(BRIEF_ARCS)
    assert not is_strongly_connected(brief)
    sinks, sources = sinks_and_sources(brief)
    assert sinks == {C} and not sources


def test_critical_edges_of_d_star():
    # Sole arc into W, P, I, C, and sole out-arc of P and of J.
    expected = {(F, W), (W, P), (W, I), (W, C), (P, F), (J, F)}
    assert set(critical_edges(underlying_digraph(D_STAR_KEYS))) == expected


def test_or_hyperarc_needs_whole_tail_to_fail():
    arcs = [arc_key({I, C}, J)]
    assert cascade_closure(arcs, {I}) == {I}
    assert cascade_closure(arcs, {I, C}) == {I, C, J}


def test_rule_and_arc_validation():
    with pytest.raises(ValueError):
        arc_key({J, C}, J)
    with pytest.raises(TypeError):
        arc_key(set(), J)
    with pytest.raises(ValueError):
        DependencyRule(frozenset({F}), W, "x", frozenset(), "s", True)
    with pytest.raises(ValueError):
        DependencyRule(frozenset({F}), W, "x", frozenset({Axiom.Ax2}), "s", True,
                       (Axiom.Ax2, W))  # incidence of Ax2 must start at P


# Axiom independence --------------------------------------------------------------------------


@pytest.mark.parametrize("axiom", list(Axiom), ids=lambda a: a.name)
def test_axiom_independence_fixtures(axiom):
    system = AXIOM_INDEPENDENCE[axiom]
    assert system.persistent and not system.holds(axiom)
    result = check_proposition_a(system)
    assert result.missing == {axiom.pillar}
    assert not result.antecedent and not result.counterexample
    assert not result.counterexample and not result.holds


def test_baseline_model_is_consistent():
    result = check_proposition_a(BASELINE_MODEL)
    assert BASELINE_MODEL.extended_axioms_hold and result.antecedent
    assert result.holds and result.interdependent


def test_strong_connectivity_small_cases():
    assert not is_strongly_connected({})
    assert is_strongly_connected({F: set()})
    assert is_strongly_connected({F: {P}, P: {F}})
    assert not is_strongly_connected({F: {P}, P: set()})
    assert is_strongly_connected({F: {P}, P: {F, J}}, nodes={F, P})


def test_d0_axioms_without_x_give_struct_but_not_interdependence():
    # Part VII Prop 5.11(a): Ax1..Ax6 without the incidence axioms.
    system = GovernanceSystem("baseline without X", True, frozenset(Axiom),
                              BASELINE_MODEL.practices)
    result = check_proposition_a(system)
    assert result.dependencies == D0_KEYS
    assert result.struct and not result.struct_counterexample
    assert not result.interdependent and not result.holds
    assert not result.counterexample  # extended antecedent fails, so not a counterexample
    graph = underlying_digraph(result.dependencies)
    assert not any(W in targets for targets in graph.values())  # no arc into W


def test_hard_case_x_codings_are_sourced():
    from beast_system.necessity import X_CODING_SOURCES

    assert set(X_CODING_SOURCES) == {s.name for s in HARD_CASES}
    for codings in X_CODING_SOURCES.values():
        assert set(codings) == set(IncidenceAxiom)
        assert all("(" in src and src.endswith(")") for src in codings.values())


def test_further_rules_are_never_generated():
    assert rules_holding(EXTENDED_AXIOMS, FURTHER_RULES) == ()
    assert generate_dependencies(BASELINE_MODEL, CORE_RULES + FURTHER_RULES) == D_STAR_KEYS
    further = {r.key: r.premise for r in FURTHER_RULES}
    assert further == {
        arc_key(I, P): "X2 + Ax4",
        arc_key(P, J): "X2 + Ax4",
        arc_key(P, I): "X2 + Ax4",
        arc_key(J, P): "precedent (Hart)",
        arc_key(I, C): "Ax4 at C's rules",
        arc_key({F, I}, C): "Part V Cor 3.7 conditions",
    }
    assert all(not r.core for r in FURTHER_RULES)


def test_incidence_axiom_statements_and_falsifiers():
    assert [(x.base, x.target) for x in IncidenceAxiom] == [
        (Axiom.Ax1, W), (Axiom.Ax2, F), (Axiom.Ax3, F), (Axiom.Ax5, F)]
    assert "conflicting claims" in X1.statement and "anticipable assignment" in X1.statement
    assert "infinitely often" in X2.statement and "Ass 3.2" in X2.statement
    assert "open texture" in X3.statement and "residual disputes" in X3.statement
    assert X5.statement == "Ax5 holds for some settlement procedure"
    assert X1.falsifier == "a persistent collective whose productive inputs never meet conflicting claims"
    assert X2.falsifier == ("a persistent collective whose prior settlement procedures settle "
                            "every new conflict")
    assert X3.falsifier == "settlement procedures that leave only finitely many residual disputes"
    assert X5.falsifier == "no member ever breaks any settlement procedure"


def test_hard_case_x_codings_cite_the_part_vii_sources():
    from beast_system.necessity import (
        CONSENSUS_VILLAGE, OSTROM_COMMONS, X_CODING_SOURCES)

    expected = {
        NUER.name: {X1: "evanspritchard1940", X2: "evanspritchard1940",
                    X3: "evanspritchard1940", X5: "evanspritchard1940"},
        JU_HOANSI.name: {X1: "lee2013", X2: "lee2013", X3: "wiessner2005", X5: "wiessner2005"},
        OSTROM_COMMONS.name: {X1: "ostrom1990", X2: "ostrom1990", X3: "cox2010",
                              X5: "ostrom1990"},
        CONSENSUS_VILLAGE.name: {X1: "sahlins1972", X2: "graeber2021", X3: "boehm1999",
                                 X5: "boehm1999"},
    }
    for case, keys in expected.items():
        for x, key in keys.items():
            assert key in X_CODING_SOURCES[case][x], (case, x)


def test_prop_4_4a_model_and_variant():
    from beast_system.necessity import PROP_4_4A_MODEL, PROP_4_4A_VARIANT

    for system in (PROP_4_4A_MODEL, PROP_4_4A_VARIANT):
        r = check_proposition_a(system)
        assert r.struct and not r.interdependent and not r.holds
        assert not r.struct_counterexample and not r.counterexample
        graph = underlying_digraph(r.dependencies)
        assert not any(W in targets for targets in graph.values())  # Prop 5.11(a)
        assert arc_key({I, C}, J) in r.dependencies
        assert arc_key(I, J) not in r.dependencies and arc_key(C, J) not in r.dependencies


def test_r1_independence_model_for_ax4():
    from beast_system.necessity import R1_AX4_MODEL

    assert AXIOM_INDEPENDENCE[Axiom.Ax4] is R1_AX4_MODEL
    r = check_proposition_a(R1_AX4_MODEL)
    assert r.missing == {I} and not r.antecedent and not r.counterexample
    assert any("defiance of a determination" in p.description for p in R1_AX4_MODEL.practices
               if p.solves is Axiom.Ax5)
    assert "ell = 0" in R1_AX4_MODEL.note and "Impl_I fails" in R1_AX4_MODEL.note


def test_starred_axiom_clauses():
    assert "finite time" in Axiom.Ax3.statement and "ell + sigma >= g" in Axiom.Ax3.statement
    assert "common-knowledge rule system" in Axiom.Ax4.statement
    assert "infinitely many periods" in Axiom.Ax4.statement
    assert "best-respond" in Axiom.Ax5.statement
    assert "consumption is counted" in Axiom.Ax6.statement


def test_admissibility():
    from beast_system.necessity import is_admissible, role_map

    from beast_system.capture import corner_polities

    for system in HARD_CASES:
        assert is_admissible(system, role_map(system)), system.name
    for polity in corner_polities().values():  # corner polities, all holders as members
        assert is_admissible(polity.system, role_map(polity.system)), polity.name
    holders = set(role_map(JU_HOANSI))
    assert not is_admissible(JU_HOANSI, holders - {"kin mediators"})  # outsider holder
    assert is_admissible(JU_HOANSI, holders - {"camp members"} | {"m1", "m2"},
                         organizations={"camp members": {"m1", "m2"}})
    assert not is_admissible(JU_HOANSI, holders - {"camp members"},
                             organizations={"camp members": set()})
    mediation = next(p for p in JU_HOANSI.practices if p.solves is Axiom.Ax3)
    assert not is_admissible(JU_HOANSI, holders,
                             dispute_parties={mediation.description: {"kin mediators"}})
