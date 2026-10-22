import pytest

import numpy as np

from beast_system.capture import (
    Polity,
    assess,
    CaptureLink,
    CaptureThresholds,
    a_does_not_imply_b,
    fused_polity,
    is_capture_link,
    plural_polity,
    proposition_b,
)
from beast_system.indices import integration_matrix
from beast_system.necessity import formal_system
from beast_system.pillars import PILLARS, Pillar


def _link(access=True, weakens=True, evidence=True):
    return CaptureLink("donor", "agency", Pillar.P, access, weakens, evidence,
                       evidence="procurement record" if evidence else "")


def test_capture_link_needs_all_three_conditions():
    assert is_capture_link(_link())


@pytest.mark.parametrize("missing", ["access", "weakens", "evidence"])
def test_each_capture_condition_is_necessary(missing):
    assert not is_capture_link(_link(**{missing: False}))


def test_disclosure_compliant_meeting_is_not_capture():
    # Privileged access alone, with no weakening of accountability and no evidence.
    assert not is_capture_link(_link(weakens=False, evidence=False))


def test_material_evidence_must_be_cited():
    with pytest.raises(ValueError):
        CaptureLink("a", "b", Pillar.J, True, True, True, evidence="  ")
    with pytest.raises(ValueError):
        CaptureLink("", "b", Pillar.J, True, True, False)


def test_prop_b_needs_u_i_and_link():
    th = CaptureThresholds(u_star=0.4, i_star=0.5)
    assert proposition_b(0.6, 0.7, [_link()], th).holds
    assert not proposition_b(0.6, 0.7, [], th).holds
    assert not proposition_b(0.6, 0.7, [_link(evidence=False)], th).holds
    assert not proposition_b(0.3, 0.7, [_link()], th).holds
    assert not proposition_b(0.6, 0.4, [_link()], th).holds
    assert proposition_b(0.4, 0.5, [_link()], th).holds  # thresholds are inclusive


def test_thresholds_validated():
    with pytest.raises(ValueError):
        CaptureThresholds(u_star=1.5)
    with pytest.raises(ValueError):
        proposition_b(1.2, 0.5, [])


def test_counter_model_a_does_not_imply_b():
    cm = a_does_not_imply_b()
    assert cm.plural.prop_a.holds and cm.fused.prop_a.holds
    assert cm.plural.prop_a.interdependent and cm.fused.prop_a.interdependent
    assert not cm.plural.prop_b.holds and cm.fused.prop_b.holds
    assert cm.demonstrates_non_implication


def test_counter_model_index_values():
    g1, g2 = plural_polity(), fused_polity()
    assert g1.U == pytest.approx(0.2 * 0.1)
    assert g1.I == 0.0
    assert g2.U == 1.0
    assert g2.I == 1.0
    assert all(h == pytest.approx(1.0) for h in g2.H.values())


def test_counter_model_robust_to_thresholds():
    for u_star, i_star in [(0.0, 0.0), (0.1, 0.1), (0.5, 0.5), (0.9, 0.9), (1.0, 1.0), (0.0, 1.0)]:
        assert a_does_not_imply_b(CaptureThresholds(u_star, i_star)).demonstrates_non_implication


def test_capture_link_flags_must_be_bool():
    with pytest.raises(TypeError):
        CaptureLink("a", "b", Pillar.J, "yes", True, False)  # type: ignore[arg-type]


def _toy_polity(links=()):
    holders = {m: ["state", "society"] for m in PILLARS}
    return Polity(
        name="toy",
        system=formal_system("toy", holders),
        shares={m: {"state": 1, "society": 1} for m in PILLARS},
        contestability={m: 0.5 for m in PILLARS},
        integration=integration_matrix({}, default=0.3),
        capture_links=tuple(links),
    )


def test_capture_link_endpoints_must_be_polity_actors():
    _toy_polity([CaptureLink("state", "society", Pillar.P, True, True, True, "record")])
    with pytest.raises(ValueError):
        _toy_polity([CaptureLink("invented", "society", Pillar.P, True, True, True, "record")])


def test_thresholds_are_stored_as_floats_and_typed():
    th = CaptureThresholds(u_star=np.float32(0.25), i_star=1)
    assert type(th.u_star) is float and th.i_star == 1.0
    with pytest.raises(TypeError):
        CaptureThresholds(u_star="0.4")  # type: ignore[arg-type]


def test_assess_reports_weight_sensitivity():
    a = assess(_toy_polity())
    assert a.sensitivity.vertex_min <= a.U <= a.sensitivity.vertex_max
    assert 0.0 <= a.u_high_fraction <= 1.0
    cm = a_does_not_imply_b()
    assert cm.fused.u_high_fraction == 1.0 and cm.plural.u_high_fraction == 0.0


def test_corner_polities_attain_the_four_corners():
    from beast_system.capture import corner_polities

    corners = corner_polities()
    assert set(corners) == {(0, 0), (1, 1), (0, 1), (1, 0)}
    for (u, i), polity in corners.items():
        a = assess(polity)
        assert a.U == pytest.approx(u) and a.I == pytest.approx(i)
        assert a.prop_a.holds and a.prop_a.interdependent
        assert a.prop_b.holds == ((u, i) == (1, 1))
        assert (a.prop_b.n_links > 0) == ((u, i) == (1, 1))
