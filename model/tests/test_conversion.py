import numpy as np
import pytest

from beast_system.dynamics import (
    coalition_integration_share,
    comparison_matrix,
    conversion_matrix,
    conversion_step,
    foothold_bound,
    simulate_conversion,
    spectral_radius,
    validate_conversion_matrix,
)

RNG = np.random.default_rng(11)


def _eta(scale=0.18):
    eta = np.full((6, 6), scale)
    np.fill_diagonal(eta, 0.0)
    return eta


def test_conversion_matrix_definition_and_validation():
    Q = np.linspace(0, 1, 6)
    K = conversion_matrix(_eta(), Q)
    assert K == pytest.approx(_eta() * (1 - Q)[:, None])
    with pytest.raises(ValueError):
        validate_conversion_matrix(np.eye(6) * 0.1)  # non-zero diagonal
    with pytest.raises(ValueError):
        conversion_matrix(_eta(0.3), np.zeros(6))  # row sums 1.5 > 1
    with pytest.raises(ValueError):
        conversion_matrix(-_eta(), np.zeros(6))


def test_t_maps_cube_into_itself_and_is_dominated_by_a():
    K = conversion_matrix(_eta(0.2), np.zeros(6))
    for _ in range(300):
        y = RNG.uniform(0, 1, 6)
        delta = RNG.uniform(0, 1, 6)
        ty = conversion_step(y, delta, K)
        assert ty.min() >= 0.0 and ty.max() <= 1.0
        assert np.all(ty <= comparison_matrix(delta, K) @ y + 1e-12)
    corner = conversion_step(np.ones(6), np.zeros(6), K)
    assert corner == pytest.approx(np.ones(6))


def test_rho_below_one_means_reversible():
    K = conversion_matrix(_eta(0.1), np.full(6, 0.5))
    delta = np.full(6, 0.3)
    assert spectral_radius(comparison_matrix(delta, K)) < 1.0
    path = simulate_conversion(np.ones(6), delta, K, 300)
    assert path[-1].max() < 1e-6


def test_full_contestability_drains_pillar_and_caps_integration():
    Q = np.zeros(6)
    Q[2] = 1.0  # pillar J fully contestable
    delta = np.full(6, 0.05)
    delta[2] = 0.2
    K = conversion_matrix(_eta(0.19), Q)
    path = simulate_conversion(np.full(6, 0.9), delta, K, 400)
    for t in range(0, 401, 50):
        assert path[t, 2] <= (1 - 0.2) ** t * 0.9 + 1e-15
    assert coalition_integration_share(path[-1]) <= 10 / 15 + 1e-6


def test_rho_nonincreasing_in_each_q():
    delta = np.full(6, 0.1)
    for n in range(6):
        prev = np.inf
        for q in np.linspace(0, 1, 11):
            Q = np.full(6, 0.2)
            Q[n] = q
            rho = spectral_radius(comparison_matrix(delta, conversion_matrix(_eta(), Q)))
            assert rho <= prev + 1e-12
            prev = rho


def test_foothold_never_vanishes():
    K = conversion_matrix(_eta(0.19), np.zeros(6))
    delta = np.full(6, 0.2)
    y0 = np.array([0.01, 0, 0, 0, 0, 0])
    fh = foothold_bound(y0, delta, K)
    assert fh.rho > 1.0 and fh.bound > 0.0
    path = simulate_conversion(y0, delta, K, 500)
    assert np.all((path * fh.v).sum(axis=1) >= fh.bound - 1e-12)


def test_foothold_preconditions():
    with pytest.raises(ValueError):
        foothold_bound(np.full(6, 0.1), np.full(6, 0.9), conversion_matrix(_eta(0.01), np.zeros(6)))
    reducible = np.zeros((6, 6))
    reducible[1, 0] = 0.5
    with pytest.raises(ValueError):
        foothold_bound(np.full(6, 0.1), np.zeros(6), reducible)


@pytest.mark.parametrize("seed", range(5))
def test_foothold_with_asymmetric_k_and_heterogeneous_delta(seed):
    rng = np.random.default_rng(100 + seed)
    eta = rng.uniform(0.0, 1.0, (6, 6))
    np.fill_diagonal(eta, 0.0)
    eta *= 0.95 / eta.sum(axis=1, keepdims=True)  # row sums 0.95, irreducible, asymmetric
    Q = rng.uniform(0.0, 0.3, 6)
    K = conversion_matrix(eta, Q)
    delta = rng.uniform(0.05, 0.4, 6)
    assert not np.allclose(K, K.T)
    A = comparison_matrix(delta, K)
    if spectral_radius(A) <= 1.0:
        pytest.skip("draw has rho(A) <= 1")
    y0 = np.zeros(6)
    y0[seed % 6] = 0.02
    fh = foothold_bound(y0, delta, K)
    assert fh.v @ A == pytest.approx(fh.rho * fh.v)  # left eigenvector orientation
    path = simulate_conversion(y0, delta, K, 400)
    assert np.all((path * fh.v).sum(axis=1) >= fh.bound - 1e-12)


def test_foothold_bound_is_overflow_safe_for_near_reducible_k():
    # Codex round 4 fixture: a 5-node core with weights 0.22 and 1e-155 links to node 6.
    K = np.zeros((6, 6))
    K[:5, :5] = 0.22
    np.fill_diagonal(K, 0.0)
    K[0, 5] = 1e-155
    K[5, 1] = 1e-155  # asymmetric attachment
    delta = np.full(6, 0.1)
    y0 = np.full(6, 0.05)
    fh = foothold_bound(y0, delta, K)
    assert np.isfinite(fh.bound) and fh.bound > 0.0
    assert fh.rho == pytest.approx(0.9 + 0.88)
    A = comparison_matrix(delta, K)
    assert (A * fh.v[:, None]).sum(axis=0) == pytest.approx(fh.rho * fh.v, rel=1e-9, abs=0)
    path = simulate_conversion(y0, delta, K, 300)
    assert np.all((path * fh.v).sum(axis=1) >= fh.bound)
