import itertools

import numpy as np
import pytest

from beast_system.capture import corner_polities, fused_polity, plural_polity
from beast_system.necessity import HARD_CASES, check_proposition_a
from beast_system.regimes import regime_profiles
from beast_system.representation import (
    M_LABELS,
    FormalizedStructure,
    drop,
    merge,
    minimal_record,
    record_from_polity,
    represent,
    representable,
    structurally_equal,
)
from beast_system.uniqueness import (
    ALMOND,
    EASTON,
    ENCODINGS,
    IDENTITY,
    LUHMANN,
    MANN,
    PARSONS,
    alpha_canonical,
    alpha_canonical_phi,
    alpha_represent,
    coarsen,
    coarsenings_equal,
    encode_aristotle,
    encode_weber,
    factor_through_phi,
    p_equal,
    phi,
    rename_record,
    witness_record,
    witness_coarsening,
    witness_pair,
)


def _fixtures():
    recs = [minimal_record(s) for s in HARD_CASES]
    recs += [record_from_polity(p.polity) for p in regime_profiles()]
    recs += [record_from_polity(p) for p in corner_polities().values()]
    recs += [record_from_polity(plural_polity()), record_from_polity(fused_polity(q=0.2))]
    return recs


def _all_set_partitions(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for part in _all_set_partitions(rest):
        for k in range(len(part)):
            yield part[:k] + [[first] + part[k]] + part[k + 1:]
        yield [[first]] + part


# Coarsening ---------------------------------------------------------------------------------


def test_phi_equals_represent_up_to_relabeling():
    for rec in _fixtures():
        assert p_equal(phi(rec), represent(rec))


def test_coarsen_generalizes_merge_and_drop():
    F_ = represent(minimal_record(HARD_CASES[0]))
    for m, n in itertools.combinations(M_LABELS, 2):
        c = {p: (f"{m}+{n}" if p in (m, n) else p) for p in M_LABELS}
        lam = {p: 1.0 for p in M_LABELS} | {m: 0.3, n: 0.7}
        assert structurally_equal(coarsen(F_, c, lam), merge(F_, m, n, 0.3))
    for m in M_LABELS:
        c = {p: (None if p == m else p) for p in M_LABELS}
        G_, D_ = coarsen(F_, c), drop(F_, m)
        total = sum(G_.weights.values())
        renorm = FormalizedStructure(**{**G_.__dict__,
                                        "weights": {p: w / total for p, w in G_.weights.items()}})
        assert structurally_equal(renorm, D_)  # drop() renormalizes omega, coarsen() does not


def test_coarsen_validation():
    F_ = represent(minimal_record(HARD_CASES[0]))
    with pytest.raises(ValueError):
        coarsen(F_, {"F": "F"})
    with pytest.raises(ValueError):
        coarsen(F_, MANN, {p: 0.5 for p in M_LABELS})  # singleton blocks need lam = 1
    with pytest.raises(ValueError):
        coarsen(F_, MANN, {**{p: 1.0 for p in M_LABELS}, "P": 0.0, "J": 1.0})
    with pytest.raises(ValueError):
        witness_coarsening(IDENTITY)


# P-equality and factorization ---------------------------------------------------------------


def test_p_equal_detects_renaming_and_differences():
    rec = record_from_polity(fused_polity())
    F_ = represent(rec)
    ren = {v: f"z-{v}" for v in F_.actors}
    G_ = FormalizedStructure(
        actors=tuple(ren[v] for v in F_.actors), pillars=F_.pillars,
        roles={ren[v]: ps for v, ps in F_.roles.items()}, layers=F_.layers,
        shares={m: {ren[v]: x for v, x in s.items()} for m, s in F_.shares.items()},
        contestability=F_.contestability, weights=F_.weights,
        kappa={frozenset(ren[v] for v in S): r for S, r in F_.kappa.items()},
        links=frozenset((ren[a], ren[b], m) for a, b, m in F_.links), arcs=F_.arcs)
    assert p_equal(F_, G_)
    layers = {m: a.copy() for m, a in F_.layers.items()}
    layers["J"][0, 1] = 0.5
    assert not p_equal(F_, FormalizedStructure(**{**F_.__dict__, "layers": layers}))


def _renamed(rec, tag):
    return rename_record(rec, {v: f"{tag}-{k}" for k, v in
                               enumerate(reversed(represent(rec).actors))})


def _fixtures_with_duplicates():
    base = _fixtures()
    dups = [_renamed(base[0], "r"), _renamed(record_from_polity(fused_polity()), "r"),
            _renamed(record_from_polity(regime_profiles()[1].polity), "r")]
    return base + [record_from_polity(fused_polity())] + dups


@pytest.mark.parametrize("alpha", [alpha_canonical, alpha_canonical_phi])
def test_p_preserving_abstractions_factor_through_phi(alpha):
    recs = _fixtures_with_duplicates()
    phis = [phi(r) for r in recs]
    same_p_pairs = sum(p_equal(phis[i], phis[j])
                       for i, j in itertools.combinations(range(len(recs)), 2))
    assert same_p_pairs >= 3  # the same_p => same_alpha branch is exercised
    result = factor_through_phi(alpha, recs)
    assert result.well_defined and result.bijective


def test_name_dependent_abstraction_is_not_bijective():
    result = factor_through_phi(alpha_represent, _fixtures_with_duplicates())
    assert result.well_defined and not result.bijective


def test_canonical_form_is_a_complete_invariant():
    recs = _fixtures_with_duplicates()
    forms = [alpha_canonical(r) for r in recs]
    phis = [phi(r) for r in recs]
    for i, j in itertools.combinations(range(len(recs)), 2):
        assert (forms[i] == forms[j]) == p_equal(phis[i], phis[j]), (i, j)
    rng = np.random.default_rng(5)
    for rec in _fixtures()[:6]:
        actors = list(represent(rec).actors)
        perm = rng.permutation(len(actors))
        renamed = rename_record(rec, {v: f"p{perm[k]}" for k, v in enumerate(actors)})
        assert alpha_canonical(renamed) == alpha_canonical(rec)


def test_rename_record_must_be_injective():
    rec = record_from_polity(fused_polity())
    with pytest.raises(ValueError):
        rename_record(rec, {v: "same" for v in represent(rec).actors})


def test_fixtures_have_distinct_p_classes():
    phis = [phi(r) for r in _fixtures()]
    for i, j in itertools.combinations(range(len(phis)), 2):
        assert not p_equal(phis[i], phis[j]), (i, j)


def test_non_p_preserving_abstraction_fails_to_factor():
    # Mann's encoding identifies the witness pair, so h would not be a function.
    recs = list(witness_pair("mann"))
    alpha = lambda r: tuple(sorted((k, round(v, 9)) for k, v in  # noqa: E731
                                   coarsen(represent(r), MANN).shares["Political"].items()))
    assert not factor_through_phi(alpha, recs).well_defined


# Witnesses: every non-injective coarsening collapses a pair ---------------------------------


def _check_witness(c, lam=None):
    g1, g2 = witness_coarsening(c, lam)
    r1, r2 = represent(g1), represent(g2)
    assert r1.actors == r2.actors and r1.roles == r2.roles  # same V and role map
    assert check_proposition_a(g1.system).holds and check_proposition_a(g2.system).holds
    assert representable(g1) and representable(g2)
    F1, F2 = phi(g1), phi(g2)
    assert not p_equal(F1, F2)
    assert coarsenings_equal(coarsen(F1, c, lam), coarsen(F2, c, lam))


@pytest.mark.parametrize("m,n", list(itertools.combinations(M_LABELS, 2)))
@pytest.mark.parametrize("lam_m", [0.2, 0.5, 0.9])
def test_every_merge_collapses_a_witness(m, n, lam_m):
    c = {p: (f"{m}+{n}" if p in (m, n) else p) for p in M_LABELS}
    lam = {p: 1.0 for p in M_LABELS} | {m: lam_m, n: 1 - lam_m}
    _check_witness(c, lam)


@pytest.mark.parametrize("m", M_LABELS)
def test_every_drop_collapses_a_witness(m):
    _check_witness({p: (None if p == m else p) for p in M_LABELS})


def test_pigeonhole_every_partition_with_fewer_than_six_blocks():
    rng = np.random.default_rng(0)
    count = 0
    for part in _all_set_partitions(list(M_LABELS)):
        if len(part) == 6:
            continue
        c = {p: "|".join(block) for block in part for p in block}
        lam = {}
        for block in part:
            w = rng.dirichlet(np.ones(len(block)))
            lam.update(dict(zip(block, w / w.sum())))
        _check_witness(c, lam)
        count += 1
    assert count == 202  # Bell(6) - 1


def test_pigeonhole_random_maps_with_drops():
    rng = np.random.default_rng(1)
    targets = ["k0", "k1", "k2", "k3", "k4", "k5", None]
    for _ in range(150):
        c = {p: targets[rng.integers(len(targets))] for p in M_LABELS}
        if None not in c.values() and len(set(c.values())) == 6:
            continue
        _check_witness(c)


# Predecessor encodings ----------------------------------------------------------------------


@pytest.mark.parametrize("k", list(ENCODINGS))
def test_predecessor_encoding_collapses_its_witness(k):
    g1, g2 = witness_pair(k)
    assert check_proposition_a(g1.system).holds and check_proposition_a(g2.system).holds
    F1, F2 = represent(g1), represent(g2)
    assert F1.actors == F2.actors and F1.roles == F2.roles  # same V and role map
    a1, a2 = ENCODINGS[k](F1), ENCODINGS[k](F2)
    if isinstance(a1, FormalizedStructure):
        assert coarsenings_equal(a1, a2)
    else:
        assert a1 == a2
    assert not p_equal(F1, F2)


@pytest.mark.parametrize("cmap,blocks", [(PARSONS, 4), (MANN, 4), (EASTON, 2), (LUHMANN, 4),
                                         (ALMOND, 4)])
def test_coarsening_encodings_have_fewer_than_six_dimensions(cmap, blocks):
    assert len({v for v in cmap.values() if v is not None}) == blocks < 6
    assert set(cmap) == set(M_LABELS)


def test_aristotle_typology():
    F_ = represent(witness_record({"P": (1.0, 0.0)}))
    assert encode_aristotle(F_) == ("one", "correct")
    assert encode_aristotle(represent(record_from_polity(fused_polity()))) == ("one", "deviant")
    assert encode_aristotle(represent(record_from_polity(plural_polity())))[0] == "few"


def test_weber_label_is_not_determined_by_p():
    rec = witness_record({"I": (0.5, 0.5)})
    F_ = represent(rec)
    assert p_equal(F_, represent(rec))
    assert encode_weber(F_, "traditional", False) != encode_weber(F_, "legal-rational", True)
    with pytest.raises(ValueError):
        encode_weber(F_, "theocratic", True)


def test_drop_witness_keeps_b_as_actor_via_retained_pillar():
    g1, g2 = witness_pair("almond")
    r1, r2 = represent(g1), represent(g2)
    assert r1.actors == r2.actors == ("a", "b", "c")
    assert r1.shares["F"]["b"] == 0.0 and "F" in r1.roles["b"]
    assert r1.shares["P"] == r2.shares["P"] == {"a": 0.5, "b": 0.5, "c": 0.0}


def test_merge_witness_actors_hold_only_the_merged_pillars():
    g1, _ = witness_pair("mann")
    r1 = represent(g1)
    assert r1.roles["a"] == r1.roles["b"] == frozenset({"P", "J"})
    assert r1.roles["c"] == frozenset({"F", "I", "C", "W"})


def test_bijective_coarsenings_are_p_preserving():
    # Thm 7.8 (coarsenings): Phi_c is P-preserving iff c is a bijection onto |K| = 6.
    rng = np.random.default_rng(3)
    F_ = represent(record_from_polity(regime_profiles()[0].polity))
    for _ in range(10):
        perm = rng.permutation(6)
        c = {m: f"k{perm[i]}" for i, m in enumerate(M_LABELS)}
        back = {f"k{perm[i]}": m for i, m in enumerate(M_LABELS)}
        G_ = coarsen(F_, c)
        assert len(G_.pillars) == 6
        restored = coarsen(G_, back)
        reordered = FormalizedStructure(**{**restored.__dict__, "pillars": M_LABELS})
        assert structurally_equal(reordered, F_)
        with pytest.raises(ValueError):
            witness_coarsening(c)


def _cycle(n: int, x: float = 0.4) -> FormalizedStructure:
    from beast_system.representation import make_structure

    base = make_structure({p: {f"v{k}": 1.0 / n for k in range(n)} for p in M_LABELS},
                          {p: 0.5 for p in M_LABELS})
    layers = {}
    for p in M_LABELS:
        arr = np.zeros((n, n))
        for k in range(n):
            arr[k, (k + 1) % n] = x
        layers[p] = arr
    return FormalizedStructure(**{**base.__dict__, "layers": layers})


def test_canonical_form_is_total_on_symmetric_structures():
    from beast_system.uniqueness import canonical_form

    nine = _cycle(9)
    form = canonical_form(nine)  # previously exceeded the 9! branch guard
    ren = {v: f"w{(k * 4) % 9}" for k, v in enumerate(nine.actors)}
    relabeled = FormalizedStructure(
        actors=tuple(sorted(ren.values())), pillars=nine.pillars,
        roles={ren[v]: r for v, r in nine.roles.items()},
        layers={p: a[np.ix_([nine.actors.index(v) for v in sorted(nine.actors, key=lambda v: ren[v])],
                            [nine.actors.index(v) for v in sorted(nine.actors, key=lambda v: ren[v])])]
                for p, a in nine.layers.items()},
        shares={p: {ren[v]: x for v, x in sh.items()} for p, sh in nine.shares.items()},
        contestability=nine.contestability, weights=nine.weights,
        kappa={frozenset(ren[v] for v in S): r for S, r in nine.kappa.items()},
        links=nine.links, arcs=nine.arcs)
    assert p_equal(nine, relabeled) and canonical_form(relabeled) == form
    # Two cycles of 4 and 5 are not isomorphic to one 9-cycle.
    split = _cycle(9)
    layers = {p: a.copy() for p, a in split.layers.items()}
    for p in layers:
        layers[p][3, 4] = 0.0
        layers[p][3, 0] = 0.4
        layers[p][8, 0] = 0.0
        layers[p][8, 4] = 0.4
    split = FormalizedStructure(**{**split.__dict__, "layers": layers})
    assert not p_equal(nine, split) and canonical_form(split) != form


def test_p_equal_and_canonical_form_use_one_normalization():
    from beast_system.uniqueness import canonical_form

    F_ = represent(record_from_polity(fused_polity()))
    for eps in (5e-10, 1e-14):
        G_ = FormalizedStructure(**{**F_.__dict__, "contestability":
                                    {**F_.contestability, "J": F_.contestability["J"] + eps}})
        assert p_equal(F_, G_) == (canonical_form(F_) == canonical_form(G_))


def test_missing_kappa_column_differs_from_explicit_zero():
    from beast_system.uniqueness import canonical_form

    F_ = represent(record_from_polity(fused_polity()))
    missing = {S: {m: x for m, x in row.items() if m != "P"} for S, row in F_.kappa.items()}
    zero = {S: {**row, "P": 0.0} for S, row in missing.items()}
    G1 = FormalizedStructure(**{**F_.__dict__, "kappa": missing})
    G2 = FormalizedStructure(**{**F_.__dict__, "kappa": zero})
    assert not p_equal(G1, G2)
    assert canonical_form(G1) != canonical_form(G2)


def test_all_dropped_coarsening_has_a_witness():
    c = {m: None for m in M_LABELS}
    g1, g2 = witness_coarsening(c)
    F1, F2 = phi(g1), phi(g2)
    assert not p_equal(F1, F2)
    i1, i2 = coarsen(F1, c), coarsen(F2, c)
    assert i1.pillars == () and i1.actors == i2.actors == ("a", "b", "c")
    assert coarsenings_equal(i1, i2)
