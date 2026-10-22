"""Capture links, Proposition B, and the non-implication A -/-> B (Part VII Theorem 2).

Proposition B (notation.md CENTRAL THESIS): the functions become concentrated or coordinated
so that independent accountability fails: U >= u* AND I >= i* AND at least one evidenced
capture link. Proposition A is a statement about the support of the role map; Proposition B
is a threshold on real-valued functionals of (H, Q, C) plus evidence (KB Section 4.3 item 4).
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field

import numpy as np

from .indices import (
    WeightSensitivity,
    coalition_integration,
    control_shares,
    hhi,
    integration_statistic,
    unaccountable_concentration,
    validate_integration_matrix,
    validate_unit_interval,
    validate_weights,
    weight_sensitivity,
)
from .necessity import (
    GovernanceSystem,
    PropositionAResult,
    check_proposition_a,
    formal_system,
    role_map,
)
from .network import MultiplexNetwork
from .pillars import PILLARS, Pillar


@dataclass(frozen=True)
class CaptureLink:
    """Capture link (i -> j, m) (source Section 5; notation.md 'Capture link').

    All three conditions are required: (i) privileged access or discretion; (ii) the privilege
    weakens otherwise applicable accountability or contestability; (iii) material evidence
    links the asymmetry to an institutional output. A disclosure-compliant donor meeting is
    not automatically capture. Claiming (iii) requires citing the evidence.
    """

    source: str
    target: str
    pillar: Pillar
    privileged_access: bool
    weakens_accountability: bool
    material_evidence: bool
    evidence: str = ""

    def __post_init__(self) -> None:
        for end in (self.source, self.target):
            if not isinstance(end, str) or not end:
                raise ValueError("capture link endpoints must be named")
        if not isinstance(self.pillar, Pillar):
            raise TypeError("capture link pillar must be a Pillar")
        for flag in ("privileged_access", "weakens_accountability", "material_evidence"):
            if not isinstance(getattr(self, flag), bool):
                raise TypeError(f"{flag} must be a bool")
        if not isinstance(self.evidence, str):
            raise TypeError("evidence must be a string")
        if self.material_evidence and not self.evidence.strip():
            raise ValueError("condition (iii) requires a citation of the material evidence")

    @property
    def holds(self) -> bool:
        return self.privileged_access and self.weakens_accountability and self.material_evidence


def is_capture_link(link: CaptureLink) -> bool:
    """Conjunction of the source's three conditions."""
    return link.holds


@dataclass(frozen=True)
class CaptureThresholds:
    """Thresholds u*, i* for Proposition B. Illustrative defaults; preregister in applications."""

    u_star: float = 0.4
    i_star: float = 0.5

    def __post_init__(self) -> None:
        object.__setattr__(self, "u_star", validate_unit_interval(self.u_star, "u_star"))
        object.__setattr__(self, "i_star", validate_unit_interval(self.i_star, "i_star"))


@dataclass(frozen=True)
class PropositionBResult:
    u_high: bool
    i_high: bool
    n_links: int

    @property
    def thresholds_met(self) -> bool:
        return self.u_high and self.i_high

    @property
    def holds(self) -> bool:
        return self.thresholds_met and self.n_links > 0


def proposition_b(
    U: float,
    I: float,  # noqa: E741  (integration statistic, math cal I)
    links: tuple[CaptureLink, ...] | list[CaptureLink],
    thresholds: CaptureThresholds = CaptureThresholds(),
) -> PropositionBResult:
    """Proposition B: U >= u* AND I >= i* AND some capture link holds."""
    U = validate_unit_interval(U, "U")
    I = validate_unit_interval(I, "I")  # noqa: E741
    return PropositionBResult(
        u_high=U >= thresholds.u_star,
        i_high=I >= thresholds.i_star,
        n_links=sum(1 for link in links if is_capture_link(link)),
    )


@dataclass(frozen=True)
class Polity:
    """A coded polity: governance system (for A) plus index inputs (for B).

    ``shares[m]`` holds raw non-negative control weights per actor, normalized to s^m.
    ``weights`` are the preregistered U weights (None means the equal-weight preregistration
    1/M); ``assess`` always adds a weight-sensitivity analysis. Capture-link endpoints must be
    actors of the polity (share holders or holders of coded practices).
    """

    name: str
    system: GovernanceSystem
    shares: Mapping[Pillar, Mapping[str, float]]
    contestability: Mapping[Pillar, float]
    integration: np.ndarray
    capture_links: tuple[CaptureLink, ...] = ()
    weights: Mapping[Pillar, float] | None = None
    normalized_shares: Mapping[Pillar, Mapping[str, float]] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        if set(self.shares) != set(PILLARS):
            raise ValueError("shares must cover every pillar")
        norm = {m: control_shares(self.shares[m]) for m in PILLARS}
        object.__setattr__(self, "normalized_shares", norm)
        object.__setattr__(self, "integration", validate_integration_matrix(self.integration))
        object.__setattr__(self, "weights", validate_weights(self.weights))
        links = tuple(self.capture_links)
        if any(not isinstance(link, CaptureLink) for link in links):
            raise TypeError("capture_links must be CaptureLink instances")
        actors = self.actors
        for link in links:
            for end in (link.source, link.target):
                if end not in actors:
                    raise ValueError(f"capture link endpoint {end!r} is not an actor of {self.name}")
        object.__setattr__(self, "capture_links", links)
        # Fail early on bad Q.
        unaccountable_concentration(self.H, self.contestability, self.weights)

    @property
    def actors(self) -> frozenset[str]:
        """V: every share holder plus every holder of a coded practice."""
        held = {a for m in PILLARS for a in self.shares[m]}
        return frozenset(held | set(role_map(self.system)))

    @property
    def H(self) -> dict[Pillar, float]:  # noqa: N802
        return {m: hhi(self.normalized_shares[m]) for m in PILLARS}

    @property
    def U(self) -> float:  # noqa: N802
        return unaccountable_concentration(self.H, self.contestability, self.weights)

    @property
    def I(self) -> float:  # noqa: E743, N802
        return integration_statistic(self.integration)


@dataclass(frozen=True)
class Assessment:
    name: str
    H: dict[Pillar, float]
    U: float
    I: float  # noqa: E741
    prop_a: PropositionAResult
    prop_b: PropositionBResult
    sensitivity: WeightSensitivity
    u_star: float

    @property
    def u_high_fraction(self) -> float:
        """Share of weight draws with U >= u*: robustness of the U side of Proposition B."""
        return self.sensitivity.fraction_at_least(self.u_star)


def assess(
    polity: Polity,
    thresholds: CaptureThresholds = CaptureThresholds(),
    n_draws: int = 2000,
    seed: int = 0,
) -> Assessment:
    """Evaluate Proposition A, Proposition B and the weight sensitivity of U on one polity."""
    return Assessment(
        name=polity.name,
        H=polity.H,
        U=polity.U,
        I=polity.I,
        prop_a=check_proposition_a(polity.system),
        prop_b=proposition_b(polity.U, polity.I, polity.capture_links, thresholds),
        sensitivity=weight_sensitivity(polity.H, polity.contestability, polity.weights,
                                       n_draws=n_draws, seed=seed),
        u_star=thresholds.u_star,
    )


# Counter-model: A does not imply B --------------------------------------------------------


def _layer_from(holders: list[str], actors: list[str], weight: float) -> np.ndarray:
    idx = {a: k for k, a in enumerate(actors)}
    arr = np.zeros((len(actors), len(actors)))
    for h in holders:
        for a in actors:
            if a != h:
                arr[idx[h], idx[a]] = weight
    return arr


def plural_polity(n_per_pillar: int = 5, q: float = 0.9) -> Polity:
    """G1, accountable pluralism: each pillar held by n independent organizations.

    Holders are disjoint across pillars, so every coalition overlap is 0 and C_mn = 0.
    """
    if n_per_pillar < 1:
        raise ValueError("n_per_pillar must be positive")
    q = validate_unit_interval(q, "q")
    holders = {m: [f"{m.label}-org-{k}" for k in range(n_per_pillar)] for m in PILLARS}
    actors = [a for m in PILLARS for a in holders[m]]
    net = MultiplexNetwork(
        actors=tuple(actors),
        layers={m: _layer_from(holders[m], actors, 0.5) for m in PILLARS},
        roles={a: {m} for m in PILLARS for a in holders[m]},
    )
    shares = {m: net.out_strength_shares(m) for m in PILLARS}
    return Polity(
        name="G1 accountable pluralism",
        system=formal_system("G1 accountable pluralism", holders),
        shares=shares,
        contestability={m: q for m in PILLARS},
        integration=coalition_integration(shares),
    )


def fused_polity(n_subordinate: int = 5, q: float = 0.0) -> Polity:
    """G2, fused capture: one coalition holds all six pillars with Q = q, one evidenced link.

    H_m = 1 and C_mn = 1, so U = 1 - q and I = 1; with the default q = 0 both indices reach
    their maximum and meet every admissible threshold pair (u*, i*) in [0, 1]^2.
    """
    if n_subordinate < 1:
        raise ValueError("n_subordinate must be positive")
    q = validate_unit_interval(q, "q")
    core = "ruling coalition"
    actors = [core] + [f"subordinate-{k}" for k in range(n_subordinate)]
    net = MultiplexNetwork(
        actors=tuple(actors),
        layers={m: _layer_from([core], actors, 1.0) for m in PILLARS},
        roles={core: set(PILLARS)},
    )
    shares = {m: net.out_strength_shares(m) for m in PILLARS}
    link = CaptureLink(
        source=core, target="subordinate-0", pillar=Pillar.J,
        privileged_access=True, weakens_accountability=True, material_evidence=True,
        evidence="synthetic: appointment record ties removal of reviewing judges to ruling",
    )
    return Polity(
        name="G2 fused capture",
        system=formal_system("G2 fused capture", {m: [core] for m in PILLARS}),
        shares=shares,
        contestability={m: q for m in PILLARS},
        integration=coalition_integration(shares),
        capture_links=(link,),
    )


@dataclass(frozen=True)
class CounterModel:
    plural: Assessment
    fused: Assessment

    @property
    def demonstrates_non_implication(self) -> bool:
        """Both satisfy A; only G2 satisfies B. Hence A does not imply B."""
        return (
            self.plural.prop_a.holds
            and self.fused.prop_a.holds
            and not self.plural.prop_b.holds
            and self.fused.prop_b.holds
        )


def a_does_not_imply_b(thresholds: CaptureThresholds = CaptureThresholds()) -> CounterModel:
    """Constructive counter-model for Part VII Theorem 2 (KB Section 4.3 item 4).

    G1 has U = (1/5)(1 - 0.9) = 0.02, I = 0 and no capture link; G2 has U = 1, I = 1 and one
    evidenced link. Both pass the Theorem A check (six pillars realized, D0 generated) and
    both are interdependent, so interdependence does not imply capture either. G1 fails B for every thresholds pair because it has no link (and its indices lie
    below any u* > 0.02, i* > 0); G2 meets B for every thresholds pair in [0, 1]^2.
    """
    return CounterModel(
        plural=assess(plural_polity(), thresholds),
        fused=assess(fused_polity(), thresholds),
    )


# Corner attainability (Part VII addendum item 9) --------------------------------------------


def grand_coalition_polity(n_members: int = 5) -> Polity:
    """(U, I) = (0, 1): one consensus coalition holds every pillar in equal shares, Q = 1."""
    if n_members < 1:
        raise ValueError("n_members must be positive")
    members = [f"member-{k}" for k in range(n_members)]
    shares = {m: {a: 1.0 / n_members for a in members} for m in PILLARS}
    return Polity(
        name="consensus grand coalition",
        system=formal_system("consensus grand coalition", {m: members for m in PILLARS}),
        shares=shares,
        contestability={m: 1.0 for m in PILLARS},
        integration=coalition_integration(shares, {a: "grand coalition" for a in members}),
    )


def separate_monopolies_polity() -> Polity:
    """(U, I) = (1, 0): a different monopolist per pillar, Q = 0, no shared coalition."""
    holders = {m: [f"{m.label} monopolist"] for m in PILLARS}
    shares = {m: {holders[m][0]: 1.0} for m in PILLARS}
    return Polity(
        name="separate monopolies",
        system=formal_system("separate monopolies", holders),
        shares=shares,
        contestability={m: 0.0 for m in PILLARS},
        integration=coalition_integration(shares),
    )


def corner_polities() -> dict[tuple[int, int], Polity]:
    """Four polities satisfying A that attain the corners of the (U, I) square.

    Only the (1, 1) corner carries a capture link, so U and I alone never decide B.
    """
    return {
        (0, 0): plural_polity(q=1.0),
        (1, 1): fused_polity(q=0.0),
        (0, 1): grand_coalition_polity(),
        (1, 0): separate_monopolies_polity(),
    }
