"""Reference implementation of the six-pillar model (Part VII, The Formalized State).

Source objects follow team/notation.md and Largo (2026) [largo2026hbs]; Proposition A
(structural necessity) and Proposition B (contingent capture) follow the CENTRAL THESIS.
"""

from .capture import (
    CaptureLink,
    CaptureThresholds,
    Polity,
    a_does_not_imply_b,
    assess,
    is_capture_link,
    proposition_b,
)
from .dynamics import negative_feedback_example, simulate, spectral_radius
from .indices import (
    coalition_integration,
    control_shares,
    hhi,
    integration_matrix,
    integration_statistic,
    unaccountable_concentration,
    weight_sensitivity,
)
from .necessity import (
    CORE_RULES,
    D0_KEYS,
    D_STAR_KEYS,
    HARD_CASES,
    GovernanceSystem,
    Practice,
    cascade_closure,
    check_proposition_a,
    dependency_graph,
    derive_functions,
    generate_dependencies,
    is_cascade_complete,
    is_strongly_connected,
)
from .network import MultiplexNetwork
from .pillars import AXIOM_TO_PILLAR, M, PAIRS, PILLARS, Axiom, IncidenceAxiom, Pillar
from .regimes import regime_profiles
from .representation import (
    FormalizedStructure,
    drop,
    equivalent_A,
    in_formalized_class,
    merge,
    represent,
    representable,
)

__all__ = [
    "FormalizedStructure", "drop", "equivalent_A", "in_formalized_class", "merge",
    "represent", "representable",
    "AXIOM_TO_PILLAR", "Axiom", "CaptureLink", "CaptureThresholds", "CORE_RULES", "D0_KEYS",
    "D_STAR_KEYS",
    "GovernanceSystem", "HARD_CASES", "IncidenceAxiom", "M", "MultiplexNetwork", "PAIRS", "PILLARS", "Pillar",
    "Polity", "Practice", "a_does_not_imply_b", "assess", "cascade_closure", "check_proposition_a",
    "coalition_integration", "control_shares", "dependency_graph", "derive_functions", "hhi",
    "generate_dependencies", "integration_matrix", "integration_statistic", "is_capture_link",
    "is_cascade_complete", "is_strongly_connected",
    "negative_feedback_example", "proposition_b", "regime_profiles", "simulate",
    "spectral_radius", "unaccountable_concentration", "weight_sensitivity",
]
