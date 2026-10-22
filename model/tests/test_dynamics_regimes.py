import numpy as np
import pytest

from beast_system.capture import CaptureThresholds, assess
from beast_system.dynamics import (
    dependency_matrix,
    some_deviation_persists,
    negative_feedback_example,
    simulate,
    spectral_radius,
)
from beast_system.pillars import PILLARS, Pillar
from beast_system.regimes import regime_profiles


def test_spectral_radius_diagonal_and_rotation():
    assert spectral_radius(np.diag([0.5, -1.2, 0.1, 0, 0, 0])) == pytest.approx(1.2)
    R = np.zeros((6, 6))
    R[0, 1], R[1, 0] = -1.0, 1.0  # rotation block, eigenvalues +-i
    assert spectral_radius(R) == pytest.approx(1.0)
    assert some_deviation_persists(R)
    with pytest.raises(ValueError):
        spectral_radius(np.eye(3))


def test_dependency_matrix_orientation():
    B = dependency_matrix({Pillar.W: {Pillar.C}}, weight=0.3)
    assert B[Pillar.C.position, Pillar.W.position] == 0.3
    assert B[Pillar.W.position, Pillar.C.position] == 0.0


def test_positive_links_do_not_guarantee_persistence():
    ex = negative_feedback_example()
    assert ex.same_positive_links
    assert ex.rho_positive > 1.0 and some_deviation_persists(ex.B_positive)
    assert ex.rho_feedback < 1.0 and not some_deviation_persists(ex.B_feedback)
    assert (ex.B_feedback < 0).sum() == 2


def test_simulation_decays_or_grows_with_spectral_radius():
    ex = negative_feedback_example()
    x0 = np.ones(6)
    decay = simulate(ex.B_feedback, x0, 200)
    grow = simulate(ex.B_positive, x0, 200)
    assert decay.shape == (201, 6)
    assert np.linalg.norm(decay[-1]) < 1e-6
    assert np.linalg.norm(grow[-1]) > 1e3


def test_simulation_with_shocks_and_noise():
    B = 0.5 * np.eye(6)
    D = np.ones((6, 1))
    z = np.ones((50, 1))
    path = simulate(B, np.zeros(6), 50, D=D, z=z)
    assert path[-1] == pytest.approx(np.full(6, 2.0))  # steady state (I - B)^-1 D z
    a = simulate(B, np.zeros(6), 5, noise_sd=0.1, seed=3)
    b = simulate(B, np.zeros(6), 5, noise_sd=0.1, seed=3)
    assert np.array_equal(a, b)
    with pytest.raises(ValueError):
        simulate(B, np.zeros(6), 5, D=D)
    with pytest.raises(ValueError):
        simulate(B, np.full(6, np.nan), 5)
    with pytest.raises(ValueError):
        simulate(B, np.zeros(6), 5, noise_sd=float("inf"))


def test_all_regimes_satisfy_proposition_a():
    for prof in regime_profiles():
        a = assess(prof.polity)
        assert a.prop_a.holds, prof.label
        assert 0.0 <= a.U <= 1.0 and 0.0 <= a.I <= 1.0
        assert prof.illustrative and "not a measurement" in prof.rationale


def test_six_regime_types_with_variants():
    types = {p.regime_type for p in regime_profiles()}
    assert len(types) == 6
    labels = [p.label for p in regime_profiles()]
    assert len(labels) == len(set(labels))


def test_no_regime_satisfies_b_without_evidenced_links():
    for prof in regime_profiles():
        assert not assess(prof.polity).prop_b.holds


@pytest.mark.parametrize("rtype", ["Islamic state", "Catholic monarchy"])
def test_religious_types_vary_and_have_a_variant_below_thresholds(rtype):
    th = CaptureThresholds()
    variants = [assess(p.polity, th) for p in regime_profiles() if p.regime_type == rtype]
    assert len(variants) == 2
    assert any(not v.prop_b.thresholds_met for v in variants)
    assert abs(variants[0].U - variants[1].U) > 0.05
    assert abs(variants[0].I - variants[1].I) > 0.05


def test_regimes_differ_in_h_q_c():
    profs = regime_profiles()
    hs = {tuple(round(v, 6) for v in p.polity.H.values()) for p in profs}
    qs = {tuple(p.polity.contestability.values()) for p in profs}
    cs = {p.polity.integration.round(6).tobytes() for p in profs}
    assert len(hs) == len(qs) == len(cs) == len(profs)
    assert all(set(p.polity.H) == set(PILLARS) for p in profs)
