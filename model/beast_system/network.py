"""Directed multiplex polity network G_t = (V_t, E_t) (source Section 5; notation.md).

One weighted adjacency A^m per pillar, with a^m_ij in [0,1] the documented capacity of actor
i to constrain a feasible action of actor j through mechanism m, and a many-to-many role
map V -> 2^M.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field

import numpy as np

from .pillars import PILLARS, Pillar


@dataclass(frozen=True)
class MultiplexNetwork:
    """Polity multiplex G_t with layers A^m_t and role map (notation.md 'Core objects').

    Layers missing from ``layers`` are taken as all-zero. Arrays are copied and frozen.
    """

    actors: tuple[str, ...]
    layers: Mapping[Pillar, np.ndarray]
    roles: Mapping[str, Iterable[Pillar]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        actors = tuple(self.actors)
        if not actors:
            raise ValueError("a polity network needs at least one actor")
        if any(not isinstance(a, str) or not a for a in actors):
            raise ValueError("actors must be non-empty strings")
        if len(set(actors)) != len(actors):
            raise ValueError("actor names must be unique")
        n = len(actors)

        layers: dict[Pillar, np.ndarray] = {}
        for key, raw in self.layers.items():
            if not isinstance(key, Pillar):
                raise TypeError(f"layer key {key!r} is not a Pillar")
            arr = np.array(raw, dtype=float)
            if arr.shape != (n, n):
                raise ValueError(f"layer {key.name} has shape {arr.shape}, expected {(n, n)}")
            if not np.all(np.isfinite(arr)):
                raise ValueError(f"layer {key.name} has non-finite weights")
            if arr.min() < 0.0 or arr.max() > 1.0:
                raise ValueError(f"layer {key.name} weights must lie in [0, 1]")
            arr.setflags(write=False)
            layers[key] = arr
        for m in PILLARS:
            if m not in layers:
                zero = np.zeros((n, n))
                zero.setflags(write=False)
                layers[m] = zero

        known = set(actors)
        roles: dict[str, frozenset[Pillar]] = {a: frozenset() for a in actors}
        for actor, pillars in self.roles.items():
            if actor not in known:
                raise ValueError(f"role map names unknown actor {actor!r}")
            ps = frozenset(pillars)
            if any(not isinstance(p, Pillar) for p in ps):
                raise TypeError(f"role map for {actor!r} contains a non-Pillar")
            roles[actor] = ps

        object.__setattr__(self, "actors", actors)
        object.__setattr__(self, "layers", layers)
        object.__setattr__(self, "roles", roles)

    @property
    def n(self) -> int:
        return len(self.actors)

    def layer(self, m: Pillar) -> np.ndarray:
        """Adjacency A^m (read-only)."""
        return self.layers[m]

    def holders(self, m: Pillar) -> frozenset[str]:
        """Actors whose role set contains m."""
        return frozenset(a for a, ps in self.roles.items() if m in ps)

    def has_full_support(self) -> bool:
        """Role-map surjectivity: every pillar has at least one holder (KB Section 4.3, item 1)."""
        return all(self.holders(m) for m in PILLARS)

    def fused_actors(self) -> frozenset[str]:
        """Actors assigned to two or more pillars by the role map."""
        return frozenset(a for a, ps in self.roles.items() if len(ps) >= 2)

    def out_strength_shares(self, m: Pillar) -> dict[str, float]:
        """Control shares s^m_i proportional to out-strength sum_j a^m_ij.

        One preregistrable operationalization of s^m (not fixed by the source). Raises if
        layer m has no edges, since shares would then be undefined.
        """
        strength = self.layers[m].sum(axis=1)
        total = float(strength.sum())
        if total <= 0.0:
            raise ValueError(f"layer {m.name} has no edges; control shares are undefined")
        return {a: float(s / total) for a, s in zip(self.actors, strength)}
