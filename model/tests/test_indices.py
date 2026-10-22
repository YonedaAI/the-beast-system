import numpy as np
import pytest

from beast_system.indices import (
    coalition_integration,
    control_shares,
    hhi,
    integration_matrix,
    integration_statistic,
    normalized_hhi,
    unaccountable_concentration,
    validate_integration_matrix,
    validate_shares,
    validate_weights,
    weight_sensitivity,
)
from beast_system.pillars import PAIRS, PILLARS

F, P, J, I, C, W = PILLARS


def test_control_shares_normalize():
    assert control_shares({"x": 3, "y": 1}) == pytest.approx({"x": 0.75, "y": 0.25})


@pytest.mark.parametrize("raw", [{"x": -1, "y": 2}, {"x": 0, "y": 0}, {}, {"x": float("inf")}])
def test_control_shares_reject_bad_input(raw):
    with pytest.raises(ValueError):
        control_shares(raw)


def test_validate_shares_requires_sum_one():
    with pytest.raises(ValueError):
        validate_shares([0.5, 0.4])
    validate_shares([0.5, 0.5])


def test_hhi_monopoly_is_one():
    assert hhi([1.0]) == 1.0
    assert hhi([1.0, 0.0, 0.0]) == 1.0


@pytest.mark.parametrize("n", [1, 2, 5, 37])
def test_hhi_uniform_is_one_over_n(n):
    assert hhi(np.full(n, 1.0 / n)) == pytest.approx(1.0 / n)


def test_normalized_hhi_endpoints():
    assert normalized_hhi([0.25] * 4) == pytest.approx(0.0)
    assert normalized_hhi([1.0, 0.0]) == pytest.approx(1.0)
    assert normalized_hhi([1.0]) == 1.0


def test_u_bounds_random():
    rng = np.random.default_rng(1)
    for _ in range(200):
        H = {m: float(rng.uniform(0.01, 1.0)) for m in PILLARS}
        Q = {m: float(rng.uniform(0.0, 1.0)) for m in PILLARS}
        w = rng.dirichlet(np.ones(6))
        u = unaccountable_concentration(H, Q, dict(zip(PILLARS, w)))
        assert 0.0 <= u <= 1.0


def test_u_extremes():
    ones = {m: 1.0 for m in PILLARS}
    zeros = {m: 0.0 for m in PILLARS}
    assert unaccountable_concentration(ones, zeros) == pytest.approx(1.0)
    assert unaccountable_concentration(ones, ones) == 0.0
    # U = 0 only needs Q_m = 1 where w_m > 0.
    Q = {**zeros, F: 1.0}
    assert unaccountable_concentration(ones, Q, {m: float(m is F) for m in PILLARS}) == 0.0


@pytest.mark.parametrize("weights", [
    {m: 1 / 6 for m in PILLARS if m is not W},
    {m: 0.25 for m in PILLARS},
    {**{m: 0.2 for m in PILLARS}, F: -0.2, P: 0.4},
])
def test_u_rejects_invalid_weights(weights):
    with pytest.raises(ValueError):
        validate_weights(weights)


def test_u_rejects_bad_h_and_q():
    ok = {m: 0.5 for m in PILLARS}
    with pytest.raises(ValueError):
        unaccountable_concentration({**ok, F: 1.5}, ok)
    with pytest.raises(ValueError):
        unaccountable_concentration(ok, {**ok, C: -0.1})
    with pytest.raises(ValueError):
        unaccountable_concentration({**ok, F: 0.0}, ok)
    with pytest.raises(ValueError):
        unaccountable_concentration({F: 0.5}, ok)


def test_integration_statistic_averages_fifteen_pairs():
    assert integration_statistic(np.ones((6, 6))) == pytest.approx(1.0)
    assert integration_statistic(integration_matrix({})) == 0.0
    assert integration_statistic(integration_matrix({(F, P): 0.9})) == pytest.approx(0.9 / 15)
    vals = np.linspace(0, 1, 15)
    C_ = integration_matrix(dict(zip(PAIRS, vals)))
    assert integration_statistic(C_) == pytest.approx(vals.mean())


def test_integration_matrix_validation():
    bad = np.eye(6)
    bad[0, 1] = 0.5
    with pytest.raises(ValueError):
        validate_integration_matrix(bad)  # asymmetric
    with pytest.raises(ValueError):
        integration_matrix({(F, P): 1.2})
    with pytest.raises(ValueError):
        integration_matrix({(F, F): 0.5})
    with pytest.raises(ValueError):
        integration_matrix({(F, P): 0.5, (P, F): 0.4})
    with pytest.raises(ValueError):
        validate_integration_matrix(np.eye(5))


def test_coalition_integration_fused_and_disjoint():
    fused = {m: {"core": 1.0} for m in PILLARS}
    assert integration_statistic(coalition_integration(fused)) == 1.0
    disjoint = {m: {f"{m.name}{k}": 0.5 for k in range(2)} for m in PILLARS}
    assert integration_statistic(coalition_integration(disjoint)) == 0.0
    # Merging two actors into one coalition raises C_FP to min(s^F(S), s^P(S)).
    shares = dict(disjoint)
    shares[F] = {"a": 0.6, "b": 0.4}
    shares[P] = {"c": 0.3, "d": 0.7}
    Cm = coalition_integration(shares, {"a": "S", "c": "S"})
    assert Cm[F.position, P.position] == pytest.approx(0.3)


def test_weight_sensitivity_within_vertex_bounds():
    H = {m: 0.2 + 0.1 * m.position for m in PILLARS}
    Q = {m: 0.5 for m in PILLARS}
    res = weight_sensitivity(H, Q, n_draws=500)
    terms = [H[m] * 0.5 for m in PILLARS]
    assert res.vertex_min == pytest.approx(min(terms))
    assert res.vertex_max == pytest.approx(max(terms))
    assert res.draws.min() >= res.vertex_min - 1e-12
    assert res.draws.max() <= res.vertex_max + 1e-12
    assert res.vertex_min <= res.baseline <= res.vertex_max
    lo, hi = res.quantiles
    assert lo <= hi
    assert res.fraction_at_least(0.0) == 1.0
    assert res.fraction_at_least(1.0) == 0.0


def test_tolerated_rounding_cannot_break_bounds():
    w = {m: 1 / 6 for m in PILLARS}
    w[F] += 5e-10
    ones, zeros = {m: 1.0 for m in PILLARS}, {m: 0.0 for m in PILLARS}
    assert unaccountable_concentration(ones, zeros, w) <= 1.0
    assert hhi([1.0 + 5e-10]) == 1.0
    with pytest.raises(TypeError):
        unaccountable_concentration(ones, {**zeros, F: True})


def test_control_shares_survive_huge_weights():
    shares = control_shares({"a": 1e308, "b": 1e308})
    assert shares == pytest.approx({"a": 0.5, "b": 0.5})


def test_degree_decomposition_of_integration():
    from beast_system.indices import integration_degrees

    rng = np.random.default_rng(7)
    C_ = integration_matrix(dict(zip(PAIRS, rng.uniform(0, 1, 15))))
    deg = integration_degrees(C_)
    assert sum(deg.values()) / 30 == pytest.approx(integration_statistic(C_))


@pytest.mark.parametrize("k,expected", [(0, 0.0), (1, 1 / 3), (2, 0.6), (3, 0.8), (6, 1.0)])
def test_hub_bound_values_and_validity(k, expected):
    from beast_system.indices import hub_bound

    assert hub_bound(k) == pytest.approx(expected)
    hub = set(PILLARS[:k])
    full = integration_matrix({(m, n): 1.0 for m, n in PAIRS if m in hub or n in hub})
    assert integration_statistic(full) == pytest.approx(hub_bound(k))  # bound is attained


def test_coalition_overlap_general_kappa():
    from beast_system.indices import coalition_overlap

    # Overlapping, non-additive candidate coalitions.
    kappa = {"S1": {F: 0.7, P: 0.4}, "S2": {F: 0.5, P: 0.6, J: 0.9}, "S1+S2": {F: 0.8, P: 0.8}}
    Cm = coalition_overlap(kappa)
    assert Cm[F.position, P.position] == pytest.approx(0.8)
    assert Cm[P.position, J.position] == pytest.approx(0.6)
    assert Cm[F.position, W.position] == 0.0
    assert integration_statistic(coalition_overlap({})) == 0.0
    with pytest.raises(ValueError):
        coalition_overlap({"S": {F: 1.2}})


def test_near_symmetric_matrix_is_symmetrized():
    from beast_system.indices import integration_degrees

    Cm = integration_matrix({(F, P): 0.5})
    Cm[F.position, P.position] += 1e-13
    v = validate_integration_matrix(Cm)
    assert np.array_equal(v, v.T)
    assert sum(integration_degrees(Cm).values()) / 30 == pytest.approx(integration_statistic(Cm))


@pytest.mark.parametrize("k", [1.5, True, -1, 7])
def test_hub_bound_rejects_bad_k(k):
    from beast_system.indices import hub_bound

    with pytest.raises((TypeError, ValueError)):
        hub_bound(k)


@pytest.mark.parametrize("k", range(7))
def test_clique_lower_bound(k):
    from beast_system.indices import clique_lower_bound, coalition_overlap

    c = 0.4
    clique = set(PILLARS[:k])
    rng = np.random.default_rng(k)
    kappa = {"S": {m: c + 0.6 * rng.uniform() if m in clique else 0.0 for m in PILLARS},
             "T": {m: float(rng.uniform(0, 0.3)) for m in PILLARS}}
    assert integration_statistic(coalition_overlap(kappa)) >= clique_lower_bound(c, k) - 1e-12
    assert clique_lower_bound(c, 6) == pytest.approx(c)


def test_star_upper_bound():
    from beast_system.indices import star_upper_bound

    rng = np.random.default_rng(3)
    for hub in PILLARS:
        Cm = integration_matrix({(m, n): float(rng.uniform()) for m, n in PAIRS if hub in (m, n)})
        assert integration_statistic(Cm) <= star_upper_bound(Cm, hub) + 1e-12
    with pytest.raises(ValueError):
        star_upper_bound(integration_matrix({(P, J): 0.5}), F)
