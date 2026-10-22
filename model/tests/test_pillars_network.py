import numpy as np
import pytest

from beast_system.network import MultiplexNetwork
from beast_system.pillars import AXIOM_TO_PILLAR, M, PAIRS, PILLARS, Axiom, Pillar


def test_six_pillars_with_labels_and_questions():
    assert M == 6
    assert [p.label for p in PILLARS] == [
        "financial", "political", "judicial", "ideological", "coercive", "productive"]
    assert Pillar.J.question == "Who interprets the laws?"
    assert [p.position for p in PILLARS] == list(range(6))


def test_axiom_map_is_bijection_in_kb_order():
    assert [a.label for a in Axiom] == [
        "scarcity", "plurality", "generality", "coordination", "defection", "maintenance"]
    assert set(AXIOM_TO_PILLAR.values()) == set(PILLARS)
    assert Axiom.Ax5.pillar is Pillar.C and Axiom.Ax6.pillar is Pillar.W


def test_fifteen_pairs():
    assert len(PAIRS) == 15 == M * (M - 1) // 2


def _net(**overrides):
    kw = dict(actors=("a", "b"), layers={Pillar.F: [[0, 0.5], [0.2, 0]]},
              roles={"a": {Pillar.F}})
    kw.update(overrides)
    return MultiplexNetwork(**kw)


def test_network_fills_missing_layers_and_freezes():
    net = _net()
    assert net.layer(Pillar.W).shape == (2, 2) and not net.layer(Pillar.W).any()
    with pytest.raises(ValueError):
        net.layer(Pillar.F)[0, 1] = 0.9


@pytest.mark.parametrize("bad", [[[0, 1.2], [0, 0]], [[0, -0.1], [0, 0]], [[0, np.nan], [0, 0]]])
def test_network_rejects_weights_outside_unit_interval(bad):
    with pytest.raises(ValueError):
        _net(layers={Pillar.F: bad})


def test_network_rejects_wrong_shape_and_unknown_role_actor():
    with pytest.raises(ValueError):
        _net(layers={Pillar.F: np.zeros((3, 3))})
    with pytest.raises(ValueError):
        _net(roles={"zed": {Pillar.F}})
    with pytest.raises(ValueError):
        _net(actors=("a", "a"))


def test_role_map_support_and_fusion():
    net = _net(roles={"a": {Pillar.F, Pillar.P}, "b": set(PILLARS) - {Pillar.F, Pillar.P}})
    assert net.has_full_support()
    assert net.fused_actors() == {"a", "b"}
    assert not _net().has_full_support()


def test_out_strength_shares():
    shares = _net().out_strength_shares(Pillar.F)
    assert shares == pytest.approx({"a": 0.5 / 0.7, "b": 0.2 / 0.7})
    with pytest.raises(ValueError):
        _net().out_strength_shares(Pillar.C)
