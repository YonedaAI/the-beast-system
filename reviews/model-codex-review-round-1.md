Reading additional input from stdin...
2026-10-22T14:28:17.075706Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a16403-4320-7153-b172-e4a0492e490f
--------
user
Review only the Python files under model/ (model/beast_system/*.py, model/tests/*.py, model/examples/run_all.py). Do not explore other directories.

Definitions the code must implement (source: Largo 2026, series notation):
- Pillars M = {F, P, J, I, C, W}, M = 6, 15 unordered pairs m<n.
- Multiplex network G_t: actors V, one adjacency A^m per pillar, weights a^m_ij in [0,1]; role map V -> 2^M many-to-many.
- Control shares s^m_i >= 0, sum_i s^m_i = 1. Concentration H_m = sum_i (s^m_i)^2 (HHI; monopoly 1, uniform 1/n).
- Contestability Q_m in [0,1].
- Unaccountable concentration U = sum_m w_m H_m (1 - Q_m), w_m >= 0, sum_m w_m = 1 (weights preregistered; sensitivity analysis required). U in [0,1].
- Cross-pillar integration C_mn in [0,1]; integration statistic I = 2/(M(M-1)) sum_{m<n} C_mn with M = 6 (mean over 15 pairs).
- Capture link (i -> j, m): requires ALL of (i) privileged access or discretion, (ii) the privilege weakens otherwise applicable accountability or contestability, (iii) material evidence links the asymmetry to an institutional output.
- Proposition A (structural necessity theorem): a persistent governance system satisfying axioms Ax1 scarcity -> F, Ax2 plurality -> P, Ax3 generality -> J, Ax4 coordination -> I, Ax5 defection -> C, Ax6 maintenance -> W implements all six pillars (formal, fused, or informal/minimal forms) plus dependency relations among them. The code cannot prove it; it must encode the lemma schema and detect counterexamples rather than make A true by definition. Strong connectivity of the dependency graph is an open problem; code must test and report honestly.
- Proposition B (capture): U >= u* AND I >= i* AND at least one capture link. A does not imply B: a_does_not_imply_b() must construct two systems that both satisfy A, one with low U and I and no links, one satisfying B.
- Dynamics x_{t+1} = B x_t + D z_t + eps; spectral radius as persistence language; positive links do not guarantee persistence (negative feedback example).
- Regime profiles are illustrative assumptions, not measurements; none may imply a religion is inherently captured.

Review for: correctness of the indices against these definitions, validation gaps, test coverage of each theorem, whether the necessity and A-not-implies-B code actually demonstrates what it claims, numerical issues, idiomatic style. List issues with file:line. End with VERDICT: PASS or VERDICT: NEEDS_FIX.
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T14:28:18.832535Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T14:28:19.900603Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
warning: Exceeded skills context budget of 2%. All skill descriptions were removed and 108 additional skills were not included in the model-visible skills list.
hook: SessionStart
hook: SessionStart
hook: SessionStart
hook: SessionStart
hook: SessionStart
hook: SessionStart
hook: SessionStart
hook: SessionStart Completed
hook: SessionStart Completed
hook: SessionStart Completed
hook: SessionStart Completed
hook: SessionStart Completed
hook: SessionStart Completed
hook: SessionStart Completed
hook: UserPromptSubmit
hook: UserPromptSubmit Completed
codex
I’ll inspect only the specified Python files under `model/`, then trace each stated definition and theorem claim into implementation and tests. I’ll keep the output to actionable findings with exact file:line references.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg --files model/beast_system model/tests model/examples | rg '"'^(model/beast_system/[''^/]+'"\\.py|model/tests/["'^/]+'"\\.py|model/examples/run_all\\.py)"'$'"'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
model/beast_system/dynamics.py
model/tests/test_necessity.py
model/examples/run_all.py
model/beast_system/pillars.py
model/beast_system/indices.py
model/beast_system/network.py
model/beast_system/capture.py
model/beast_system/necessity.py
model/beast_system/__init__.py
model/beast_system/regimes.py
model/tests/test_pillars_network.py
model/tests/test_indices.py
model/tests/test_dynamics_regimes.py
model/tests/test_capture.py

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/__init__.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Reference implementation of the six-pillar model (Part VII, The Formalized State).
     2	
     3	Source objects follow team/notation.md and Largo (2026) [largo2026hbs]; Proposition A
     4	(structural necessity) and Proposition B (contingent capture) follow the CENTRAL THESIS.
     5	"""
     6	
     7	from .capture import (
     8	    CaptureLink,
     9	    CaptureThresholds,
    10	    Polity,
    11	    a_does_not_imply_b,
    12	    assess,
    13	    is_capture_link,
    14	    proposition_b,
    15	)
    16	from .dynamics import negative_feedback_example, simulate, spectral_radius
    17	from .indices import (
    18	    coalition_integration,
    19	    control_shares,
    20	    hhi,
    21	    integration_matrix,
    22	    integration_statistic,
    23	    unaccountable_concentration,
    24	    weight_sensitivity,
    25	)
    26	from .necessity import (
    27	    DEPENDENCIES,
    28	    HARD_CASES,
    29	    GovernanceSystem,
    30	    Practice,
    31	    check_proposition_a,
    32	    dependency_graph,
    33	    derive_functions,
    34	    is_strongly_connected,
    35	)
    36	from .network import MultiplexNetwork
    37	from .pillars import AXIOM_TO_PILLAR, M, PAIRS, PILLARS, Axiom, Pillar
    38	from .regimes import regime_profiles
    39	
    40	__all__ = [
    41	    "AXIOM_TO_PILLAR", "Axiom", "CaptureLink", "CaptureThresholds", "DEPENDENCIES",
    42	    "GovernanceSystem", "HARD_CASES", "M", "MultiplexNetwork", "PAIRS", "PILLARS", "Pillar",
    43	    "Polity", "Practice", "a_does_not_imply_b", "assess", "check_proposition_a",
    44	    "coalition_integration", "control_shares", "dependency_graph", "derive_functions", "hhi",
    45	    "integration_matrix", "integration_statistic", "is_capture_link", "is_strongly_connected",
    46	    "negative_feedback_example", "proposition_b", "regime_profiles", "simulate",
    47	    "spectral_radius", "unaccountable_concentration", "weight_sensitivity",
    48	]

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/dynamics.py' in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/regimes.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Linear pillar-capacity dynamics x_{t+1} = B x_t + D z_t + eps_t (source Section 5.3).
     2	
     3	x_t = (F_t, P_t, J_t, I^cap_t, C_t, W_t) in pillar order. The source warns that stability
     4	cannot be inferred from positive links alone (negative feedback, substitution, saturation,
     5	legitimacy loss) and uses dominant eigenvalues of a local linearization as the language of
     6	persistence. Here a deviation of x from its steady state persists iff the spectral radius
     7	rho(B) >= 1; for rho(B) < 1 it decays geometrically.
     8	"""
     9	
    10	from __future__ import annotations
    11	
    12	from collections.abc import Mapping
    13	from dataclasses import dataclass
    14	
    15	import numpy as np
    16	
    17	from .necessity import Graph, dependency_graph
    18	from .pillars import M, Pillar
    19	
    20	
    21	def _square(B: np.ndarray) -> np.ndarray:
    22	    arr = np.asarray(B, dtype=float)
    23	    if arr.shape != (M, M):
    24	        raise ValueError(f"B must be {M}x{M}, got {arr.shape}")
    25	    if not np.all(np.isfinite(arr)):
    26	        raise ValueError("B must be finite")
    27	    return arr
    28	
    29	
    30	def spectral_radius(B: np.ndarray) -> float:
    31	    """rho(B) = max |lambda| over eigenvalues of B."""
    32	    return float(np.max(np.abs(np.linalg.eigvals(_square(B)))))
    33	
    34	
    35	def deviation_persists(B: np.ndarray) -> bool:
    36	    """True iff rho(B) >= 1, i.e. a deviation from steady state does not die out."""
    37	    return spectral_radius(B) >= 1.0
    38	
    39	
    40	def dependency_matrix(graph: Graph, weight: float, self_weight: float = 0.0) -> np.ndarray:
    41	    """B with B[dependent, provider] = weight for each edge, and self_weight on the diagonal.
    42	
    43	    Row = pillar at t+1, column = pillar at t, matching x_{t+1} = B x_t.
    44	    """
    45	    B = np.eye(M) * float(self_weight)
    46	    for provider, dependents in graph.items():
    47	        for dep in dependents:
    48	            B[dep.position, provider.position] = float(weight)
    49	    return B
    50	
    51	
    52	def simulate(
    53	    B: np.ndarray,
    54	    x0: np.ndarray,
    55	    steps: int,
    56	    D: np.ndarray | None = None,
    57	    z: np.ndarray | None = None,
    58	    noise_sd: float = 0.0,
    59	    seed: int | None = None,
    60	) -> np.ndarray:
    61	    """Iterate x_{t+1} = B x_t + D z_t + eps_t; returns an array of shape (steps + 1, 6).
    62	
    63	    ``z`` has shape (steps, k) and ``D`` shape (6, k); eps_t ~ N(0, noise_sd^2 I).
    64	    """
    65	    B = _square(B)
    66	    x = np.asarray(x0, dtype=float)
    67	    if x.shape != (M,):
    68	        raise ValueError(f"x0 must have shape ({M},)")
    69	    if steps < 0:
    70	        raise ValueError("steps must be non-negative")
    71	    if (D is None) != (z is None):
    72	        raise ValueError("pass both D and z, or neither")
    73	    if D is not None and z is not None:
    74	        D = np.asarray(D, dtype=float)
    75	        z = np.asarray(z, dtype=float)
    76	        if D.ndim != 2 or D.shape[0] != M or z.shape != (steps, D.shape[1]):
    77	            raise ValueError("D must be (6, k) and z must be (steps, k)")
    78	    if noise_sd < 0.0:
    79	        raise ValueError("noise_sd must be non-negative")
    80	    rng = np.random.default_rng(seed)
    81	    path = np.empty((steps + 1, M))
    82	    path[0] = x
    83	    for t in range(steps):
    84	        x = B @ x
    85	        if D is not None and z is not None:
    86	            x = x + D @ z[t]
    87	        if noise_sd > 0.0:
    88	            x = x + rng.normal(0.0, noise_sd, size=M)
    89	        path[t + 1] = x
    90	    return path
    91	
    92	
    93	@dataclass(frozen=True)
    94	class FeedbackExample:
    95	    """Two matrices with the same positive links; only the feedback one has negative entries."""
    96	
    97	    B_positive: np.ndarray
    98	    B_feedback: np.ndarray
    99	    rho_positive: float
   100	    rho_feedback: float
   101	
   102	    @property
   103	    def same_positive_links(self) -> bool:
   104	        return bool(np.array_equal(self.B_positive > 0, self.B_feedback > 0))
   105	
   106	
   107	#: Negative feedback entries (provider, dependent) -> weight: coercion erodes legitimacy and
   108	#: depresses productive effort (source Section 5.3, 'legitimacy loss'). Illustrative values.
   109	NEGATIVE_FEEDBACK: Mapping[tuple[Pillar, Pillar], float] = {
   110	    (Pillar.C, Pillar.I): -0.4,
   111	    (Pillar.C, Pillar.W): -0.3,
   112	}
   113	
   114	
   115	def negative_feedback_example(
   116	    weight: float = 0.25,
   117	    self_weight: float = 0.6,
   118	    feedback: Mapping[tuple[Pillar, Pillar], float] = NEGATIVE_FEEDBACK,
   119	) -> FeedbackExample:
   120	    """Positive dependency links do not guarantee persistence (source Section 5.3).
   121	
   122	    With the derived dependency edges at ``weight`` and ``self_weight`` on the diagonal,
   123	    rho > 1. Adding negative feedback on entries that carry no positive link leaves every
   124	    positive link unchanged yet pushes rho below 1, so deviations decay.
   125	    """
   126	    B_pos = dependency_matrix(dependency_graph(include_conditional=False), weight, self_weight)
   127	    B_fb = B_pos.copy()
   128	    for (provider, dependent), w in feedback.items():
   129	        if w >= 0.0:
   130	            raise ValueError("feedback entries must be negative")
   131	        if B_pos[dependent.position, provider.position] != 0.0:
   132	            raise ValueError("feedback must not overwrite a positive link")
   133	        B_fb[dependent.position, provider.position] = w
   134	    return FeedbackExample(B_pos, B_fb, spectral_radius(B_pos), spectral_radius(B_fb))

 succeeded in 0ms:
     1	"""Stylized regime profiles for the six regime types (notation.md 'The six regime types').
     2	
     3	ILLUSTRATIVE ASSUMPTIONS, NOT MEASUREMENTS. Every share, contestability value Q_m and
     4	integration value C_mn below is a stylized assumption chosen to show how the universal
     5	six-pillar structure (Proposition A) can be DISTRIBUTED differently. None is an estimate for
     6	any country or period, and none should be cited as data.
     7	
     8	Every profile satisfies Proposition A by construction of its coded practices. No profile
     9	carries a capture link, because a capture link requires cited material evidence (source
    10	Section 5); hence no profile satisfies Proposition B, whatever its U and I. Variants within
    11	the Islamic and Catholic types differ in their checks, so no value attaches capture to a
    12	religion as such (guardrail 1).
    13	"""
    14	
    15	from __future__ import annotations
    16	
    17	from collections.abc import Mapping
    18	from dataclasses import dataclass
    19	
    20	from .capture import Polity
    21	from .indices import integration_matrix
    22	from .necessity import formal_system
    23	from .pillars import PAIRS, Pillar
    24	
    25	ILLUSTRATIVE = True
    26	DISCLAIMER = "Illustrative assumption, not a measurement."
    27	
    28	F, P, J, I, C, W = Pillar.F, Pillar.P, Pillar.J, Pillar.I, Pillar.C, Pillar.W  # noqa: E741
    29	
    30	
    31	@dataclass(frozen=True)
    32	class RegimeProfile:
    33	    """One stylized profile. ``polity`` holds the illustrative inputs; ``rationale`` the story."""
    34	
    35	    regime_type: str
    36	    variant: str
    37	    polity: Polity
    38	    rationale: str
    39	    illustrative: bool = ILLUSTRATIVE
    40	
    41	    @property
    42	    def label(self) -> str:
    43	        return f"{self.regime_type} ({self.variant})" if self.variant else self.regime_type
    44	
    45	
    46	def _profile(
    47	    regime_type: str,
    48	    variant: str,
    49	    shares: Mapping[Pillar, Mapping[str, float]],
    50	    q: tuple[float, float, float, float, float, float],
    51	    c_pairs: Mapping[tuple[Pillar, Pillar], float],
    52	    c_default: float,
    53	    rationale: str,
    54	) -> RegimeProfile:
    55	    name = f"{regime_type} ({variant})" if variant else regime_type
    56	    holders = {m: [a for a, v in s.items() if v > 0] for m, s in shares.items()}
    57	    polity = Polity(
    58	        name=name,
    59	        system=formal_system(name, holders, source=DISCLAIMER),
    60	        shares=shares,
    61	        contestability=dict(zip((F, P, J, I, C, W), q)),
    62	        integration=integration_matrix(c_pairs, default=c_default),
    63	    )
    64	    return RegimeProfile(regime_type, variant, polity, f"{rationale} {DISCLAIMER}")
    65	
    66	
    67	def _pairs_among(pillars: tuple[Pillar, ...], value: float) -> dict[tuple[Pillar, Pillar], float]:
    68	    return {(m, n): value for m, n in PAIRS if m in pillars and n in pillars}
    69	
    70	
    71	def regime_profiles() -> tuple[RegimeProfile, ...]:
    72	    """The stylized profiles, two variants each for the Islamic and Catholic types."""
    73	    return (
    74	        _profile(
    75	            "Market capitalism", "",
    76	            {F: {"Financial firms": 4, "Non-financial firms": 3, "State budget": 2, "Households": 1},
    77	             P: {"Legislature": 4, "Executive": 4, "Organized interests": 2},
    78	             J: {"Courts": 7, "Private arbitration": 2, "Regulators": 1},
    79	             I: {"Media firms": 3, "Platforms": 3, "Universities": 2, "Religious bodies": 2},
    80	             C: {"Police": 5, "Military": 3, "Private security": 2},
    81	             W: {"Wage workers": 5, "Non-financial firms": 3, "Households": 2}},
    82	            (0.45, 0.60, 0.70, 0.55, 0.55, 0.40),
    83	            {(F, P): 0.50, (F, I): 0.45, (F, J): 0.35, (F, W): 0.50, (P, J): 0.30,
    84	             (P, I): 0.30, (P, C): 0.30, (P, W): 0.30},
    85	            0.20,
    86	            "Wealth-to-rules pathway (source Prop 3): C_FP, C_FI, C_FW elevated.",
    87	        ),
    88	        _profile(
    89	            "Communist party-state", "",
    90	            {F: {"Party": 6, "SOE management": 3, "Households": 1},
    91	             P: {"Party": 9, "People's congress": 1},
    92	             J: {"Party": 6, "Courts": 4},
    93	             I: {"Party": 7, "Universities": 2, "Religious bodies": 1},
    94	             C: {"Party": 6, "Security services": 4},
    95	             W: {"Workers": 6, "SOE management": 3, "Households": 1}},
    96	            (0.20, 0.10, 0.15, 0.15, 0.10, 0.25),
    97	            _pairs_among((F, P, J, I, C), 0.80),
    98	            0.45,
    99	            "Appointments-to-resources pathway (nomenklatura): party-centred pairs high.",
   100	        ),
   101	        _profile(
   102	            "Democratic socialism", "",
   103	            {F: {"State budget": 3, "Firms": 3, "Public pension funds": 2, "Cooperatives": 1,
   104	                 "Households": 1},
   105	             P: {"Parliament": 5, "Government": 3, "Social partners": 2},
   106	             J: {"Courts": 8, "Ombudsman": 2},
   107	             I: {"Public broadcaster": 3, "Private media": 3, "Universities": 2,
   108	                 "Churches and civil society": 2},
   109	             C: {"Police": 6, "Military": 4},
   110	             W: {"Unions": 4, "Firms": 3, "Workers": 3}},
   111	            (0.65, 0.75, 0.80, 0.70, 0.70, 0.70),
   112	            {(P, W): 0.45, (F, W): 0.40, (F, P): 0.35},
   113	            0.15,
   114	            "Corporatist bargaining couples P, F and W; high Q offsets concentration.",
   115	        ),
   116	        _profile(
   117	            "Islamic state", "plural juristic authority",
   118	            {F: {"Ruler's treasury": 4, "Waqf endowments": 3, "Merchants": 3},
   119	             P: {"Ruler": 5, "Jurists (plural schools)": 3, "Notables council": 2},
   120	             J: {"Qadi courts": 5, "Jurists (plural schools)": 3, "Ruler's grievance court": 2},
   121	             I: {"Jurists (plural schools)": 5, "Sufi orders": 3, "Ruler": 2},
   122	             C: {"Ruler's army": 6, "Local militias": 2, "Market inspectors": 2},
   123	             W: {"Peasants": 5, "Artisan guilds": 3, "Merchants": 2}},
   124	            (0.45, 0.35, 0.55, 0.50, 0.30, 0.40),
   125	            {(P, C): 0.55, (F, P): 0.45, (J, I): 0.45, (F, C): 0.40, (P, I): 0.35,
   126	             (P, J): 0.35},
   127	            0.20,
   128	            "Juristic class trained and endowed apart from the ruler checks P via J and I.",
   129	        ),
   130	        _profile(
   131	            "Islamic state", "centralized clerical-political authority",
   132	            {F: {"Clerical-political center": 5, "State budget": 3, "Merchants": 2},
   133	             P: {"Clerical-political center": 5, "Vetting council": 3, "Elected assembly": 2},
   134	             J: {"Clerical-political center": 5, "State courts": 5},
   135	             I: {"Clerical-political center": 6, "Seminaries": 3, "Media": 1},
   136	             C: {"Clerical-political center": 6, "Regular army": 4},
   137	             W: {"Workers": 5, "Center-linked enterprises": 3, "Merchants": 2}},
   138	            (0.25, 0.25, 0.20, 0.20, 0.15, 0.30),
   139	            _pairs_among((F, P, J, I, C), 0.70),
   140	            0.40,
   141	            "One center commands appointments across P, J, I, C; elected assembly is checked.",
   142	        ),
   143	        _profile(
   144	            "Catholic monarchy", "estates and Church-crown rivalry",
   145	            {F: {"Crown treasury": 4, "Church benefices": 3, "Bankers": 2, "Nobility": 1},
   146	             P: {"Crown": 5, "Estates assembly": 3, "Nobility": 2},
   147	             J: {"Royal courts": 4, "Parlements": 3, "Church courts": 3},
   148	             I: {"Church": 6, "Universities": 2, "Crown": 2},
   149	             C: {"Crown army": 5, "Nobility": 3, "Town militias": 2},
   150	             W: {"Peasants": 6, "Guilds": 3, "Merchants": 1}},
   151	            (0.40, 0.40, 0.45, 0.35, 0.30, 0.30),
   152	            {(F, P): 0.45, (P, I): 0.40, (P, J): 0.40, (F, C): 0.40},
   153	            0.20,
   154	            "Estates, parlements and an autonomous Church contest the crown.",
   155	        ),
   156	        _profile(
   157	            "Catholic monarchy", "absolutist with venal offices",
   158	            {F: {"Crown": 6, "Tax farmers": 3, "Church benefices": 1},
   159	             P: {"Crown": 9, "Royal council": 1},
   160	             J: {"Crown": 5, "Venal office holders": 4, "Church courts": 1},
   161	             I: {"Church hierarchy": 6, "Crown": 3, "Universities": 1},
   162	             C: {"Crown": 8, "Nobility": 2},
   163	             W: {"Peasants": 6, "Guilds": 3, "Tax farmers": 1}},
   164	            (0.20, 0.10, 0.25, 0.20, 0.15, 0.20),
   165	            {**_pairs_among((F, P, J, C), 0.75), (P, I): 0.70},
   166	            0.40,
   167	            "Crown fuses F, P, J, C; venality couples F and J; Church aligned with crown.",
   168	        ),
   169	        _profile(
   170	            "Secular democracy", "",
   171	            {F: {"Central bank": 2, "Firms": 3, "State budget": 3, "Households": 2},
   172	             P: {"Legislature": 4, "Executive": 3, "Subnational governments": 3},
   173	             J: {"Constitutional court": 3, "Ordinary courts": 6, "Administrative tribunals": 1},
   174	             I: {"Public media": 2, "Private media": 3, "Universities": 2, "Religious bodies": 1,
   175	                 "Civil society": 2},
   176	             C: {"Police": 5, "Military": 3, "Oversight bodies": 2},
   177	             W: {"Workers": 5, "Firms": 3, "Unions": 2}},
   178	            (0.60, 0.75, 0.80, 0.70, 0.65, 0.55),
   179	            {(F, P): 0.30},
   180	            0.15,
   181	            "Authority distributed among elected officials, courts and private bodies.",
   182	        ),
   183	    )

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/indices.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Concentration, contestability and integration indices (source Section 5; notation.md).
     2	
     3	Definitions implemented here:
     4	  s^m_i >= 0, sum_i s^m_i = 1                              control shares
     5	  H_m = sum_i (s^m_i)^2                                     Herfindahl-Hirschman concentration
     6	  Q_m in [0, 1]                                             contestability
     7	  U = sum_m w_m H_m (1 - Q_m), w_m >= 0, sum_m w_m = 1      unaccountable concentration
     8	  C_mn in [0, 1]                                            cross-pillar integration
     9	  I = 2 / (M (M - 1)) sum_{m<n} C_mn, M = 6 (15 pairs)      integration statistic (math cal I)
    10	
    11	The source calls U 'an illustrative index, not a validated measurement instrument' and
    12	requires preregistered weights plus sensitivity analysis; see ``weight_sensitivity``.
    13	"""
    14	
    15	from __future__ import annotations
    16	
    17	import math
    18	from collections.abc import Mapping, Sequence
    19	from dataclasses import dataclass
    20	
    21	import numpy as np
    22	
    23	from .pillars import M, PAIRS, PILLARS, Pillar
    24	
    25	SHARE_ATOL = 1e-9
    26	WEIGHT_ATOL = 1e-9
    27	
    28	ShareLike = Mapping[str, float] | Sequence[float] | np.ndarray
    29	
    30	
    31	def validate_unit_interval(value: float, name: str) -> float:
    32	    """Return ``value`` as float after checking it is finite and in [0, 1]."""
    33	    v = float(value)
    34	    if not math.isfinite(v) or v < 0.0 or v > 1.0:
    35	        raise ValueError(f"{name} must lie in [0, 1], got {value!r}")
    36	    return v
    37	
    38	
    39	def _share_array(shares: ShareLike) -> np.ndarray:
    40	    values = list(shares.values()) if isinstance(shares, Mapping) else shares
    41	    arr = np.asarray(values, dtype=float).ravel()
    42	    if arr.size == 0:
    43	        raise ValueError("shares must be non-empty")
    44	    if not np.all(np.isfinite(arr)):
    45	        raise ValueError("shares must be finite")
    46	    if arr.min() < 0.0:
    47	        raise ValueError("shares must be non-negative")
    48	    return arr
    49	
    50	
    51	def control_shares(raw: Mapping[str, float]) -> dict[str, float]:
    52	    """Normalize non-negative control weights to shares s^m_i summing to 1 (notation.md)."""
    53	    arr = _share_array(raw)
    54	    total = float(arr.sum())
    55	    if total <= 0.0:
    56	        raise ValueError("at least one control weight must be positive")
    57	    return {k: float(v) / total for k, v in raw.items()}
    58	
    59	
    60	def validate_shares(shares: ShareLike, atol: float = SHARE_ATOL) -> np.ndarray:
    61	    """Check s^m_i >= 0 and sum_i s^m_i = 1 (notation.md 'Control share')."""
    62	    arr = _share_array(shares)
    63	    if abs(float(arr.sum()) - 1.0) > atol:
    64	        raise ValueError(f"shares must sum to 1, got {arr.sum():.12g}")
    65	    return arr
    66	
    67	
    68	def hhi(shares: ShareLike) -> float:
    69	    """H_m = sum_i (s^m_i)^2 (source Eq. for H_{m,t}). Lies in [1/n, 1]."""
    70	    arr = validate_shares(shares)
    71	    return float(np.dot(arr, arr))
    72	
    73	
    74	def normalized_hhi(shares: ShareLike) -> float:
    75	    """H* = (H - 1/n) / (1 - 1/n), for comparing polities with different n (KB VII.3 (v)).
    76	
    77	    Not in the source. Defined as 1 for n = 1 (a monopoly by construction).
    78	    """
    79	    arr = validate_shares(shares)
    80	    n = arr.size
    81	    if n == 1:
    82	        return 1.0
    83	    return float((np.dot(arr, arr) - 1.0 / n) / (1.0 - 1.0 / n))
    84	
    85	
    86	def validate_weights(weights: Mapping[Pillar, float] | None) -> dict[Pillar, float]:
    87	    """Check the U weights: one per pillar, w_m >= 0, sum_m w_m = 1 (source Eq. U_t).
    88	
    89	    ``None`` gives equal weights 1/M.
    90	    """
    91	    if weights is None:
    92	        return {m: 1.0 / M for m in PILLARS}
    93	    if set(weights) != set(PILLARS):
    94	        raise ValueError("weights must give exactly one value per pillar")
    95	    w = {m: float(weights[m]) for m in PILLARS}
    96	    if any(not math.isfinite(v) or v < 0.0 for v in w.values()):
    97	        raise ValueError("weights must be finite and non-negative")
    98	    if abs(sum(w.values()) - 1.0) > WEIGHT_ATOL:
    99	        raise ValueError(f"weights must sum to 1, got {sum(w.values()):.12g}")
   100	    return w
   101	
   102	
   103	def _per_pillar(values: Mapping[Pillar, float], name: str) -> dict[Pillar, float]:
   104	    if set(values) != set(PILLARS):
   105	        raise ValueError(f"{name} must give exactly one value per pillar")
   106	    return {m: validate_unit_interval(values[m], f"{name}[{m.name}]") for m in PILLARS}
   107	
   108	
   109	def unaccountable_concentration(
   110	    H: Mapping[Pillar, float],
   111	    Q: Mapping[Pillar, float],
   112	    weights: Mapping[Pillar, float] | None = None,
   113	) -> float:
   114	    """U = sum_m w_m H_m (1 - Q_m) (source Eq. U_t). Lies in [0, 1].
   115	
   116	    U = 0 iff Q_m = 1 for every m with w_m > 0, because H_m >= 1/n > 0 (KB VII.3 (ii)).
   117	    """
   118	    h = _per_pillar(H, "H")
   119	    if any(v == 0.0 for v in h.values()):
   120	        raise ValueError("H_m >= 1/n > 0 for any valid share vector; got H_m = 0")
   121	    q = _per_pillar(Q, "Q")
   122	    w = validate_weights(weights)
   123	    return float(sum(w[m] * h[m] * (1.0 - q[m]) for m in PILLARS))
   124	
   125	
   126	def validate_integration_matrix(C: np.ndarray, atol: float = 1e-12) -> np.ndarray:
   127	    """Check C is 6x6, finite, symmetric, with off-diagonal C_mn in [0, 1].
   128	
   129	    The diagonal is unused by the integration statistic; by convention it is set to 1.
   130	    """
   131	    arr = np.array(C, dtype=float)
   132	    if arr.shape != (M, M):
   133	        raise ValueError(f"integration matrix must be {M}x{M}, got {arr.shape}")
   134	    if not np.all(np.isfinite(arr)):
   135	        raise ValueError("integration matrix must be finite")
   136	    if not np.allclose(arr, arr.T, atol=atol, rtol=0.0):
   137	        raise ValueError("integration matrix must be symmetric (C_mn = C_nm)")
   138	    off = arr[~np.eye(M, dtype=bool)]
   139	    if off.min() < 0.0 or off.max() > 1.0:
   140	        raise ValueError("off-diagonal C_mn must lie in [0, 1]")
   141	    np.fill_diagonal(arr, 1.0)
   142	    return arr
   143	
   144	
   145	def integration_matrix(
   146	    pairs: Mapping[tuple[Pillar, Pillar], float], default: float = 0.0
   147	) -> np.ndarray:
   148	    """Build a symmetric C from {(m, n): C_mn}; unspecified pairs take ``default``."""
   149	    validate_unit_interval(default, "default")
   150	    arr = np.full((M, M), float(default))
   151	    seen: set[frozenset[Pillar]] = set()
   152	    for (m, n), value in pairs.items():
   153	        if m == n:
   154	            raise ValueError(f"pair ({m.name}, {n.name}) is not a cross-pillar pair")
   155	        key = frozenset((m, n))
   156	        if key in seen:
   157	            raise ValueError(f"pair {m.name}{n.name} given twice")
   158	        seen.add(key)
   159	        v = validate_unit_interval(value, f"C[{m.name}{n.name}]")
   160	        arr[m.position, n.position] = arr[n.position, m.position] = v
   161	    np.fill_diagonal(arr, 1.0)
   162	    return arr
   163	
   164	
   165	def integration_statistic(C: np.ndarray) -> float:
   166	    """I = 2 / (M (M - 1)) sum_{m<n} C_mn with M = 6, i.e. the mean over 15 pairs (source Eq. I_t)."""
   167	    arr = validate_integration_matrix(C)
   168	    total = sum(arr[m.position, n.position] for m, n in PAIRS)
   169	    return float(2.0 / (M * (M - 1)) * total)
   170	
   171	
   172	def coalition_integration(
   173	    shares: Mapping[Pillar, Mapping[str, float]],
   174	    coalition_of: Mapping[str, str] | None = None,
   175	) -> np.ndarray:
   176	    """A formal variant of C_mn: max over coalitions S of min(s^m(S), s^n(S)).
   177	
   178	    The source describes C_mn only verbally ('the same coalition commands appointments,
   179	    budgets, sanctions or agenda in both m and n'); KB VII.3 (iv) asks Part VII to propose a
   180	    definition. Here s^m(S) is the summed share of coalition S in pillar m. Actors absent from
   181	    ``coalition_of`` form singleton coalitions. The result lies in [0, 1] and is weakly
   182	    increasing when a coalition gains share in either pillar.
   183	    """
   184	    coalition_of = dict(coalition_of or {})
   185	    by_pillar: dict[Pillar, dict[str, float]] = {}
   186	    for m in PILLARS:
   187	        if m not in shares:
   188	            raise ValueError(f"shares missing pillar {m.name}")
   189	        s = shares[m]
   190	        validate_shares(s)
   191	        agg: dict[str, float] = {}
   192	        for actor, v in s.items():
   193	            key = coalition_of.get(actor, actor)
   194	            agg[key] = agg.get(key, 0.0) + float(v)
   195	        by_pillar[m] = agg
   196	    arr = np.eye(M)
   197	    for m, n in PAIRS:
   198	        common = by_pillar[m].keys() & by_pillar[n].keys()
   199	        v = max((min(by_pillar[m][k], by_pillar[n][k]) for k in common), default=0.0)
   200	        v = min(max(v, 0.0), 1.0)
   201	        arr[m.position, n.position] = arr[n.position, m.position] = v
   202	    return arr
   203	
   204	
   205	@dataclass(frozen=True)
   206	class WeightSensitivity:
   207	    """Result of ``weight_sensitivity``. ``draws`` holds U for each sampled weight vector."""
   208	
   209	    baseline: float
   210	    vertex_min: float
   211	    vertex_max: float
   212	    draws: np.ndarray
   213	
   214	    @property
   215	    def quantiles(self) -> tuple[float, float]:
   216	        """5th and 95th percentile of U across draws."""
   217	        lo, hi = np.quantile(self.draws, [0.05, 0.95])
   218	        return float(lo), float(hi)
   219	
   220	    def fraction_at_least(self, u_star: float) -> float:
   221	        """Share of weight draws with U >= u_star (robustness of a threshold call)."""
   222	        validate_unit_interval(u_star, "u_star")
   223	        return float(np.mean(self.draws >= u_star))
   224	
   225	
   226	def weight_sensitivity(
   227	    H: Mapping[Pillar, float],
   228	    Q: Mapping[Pillar, float],
   229	    weights: Mapping[Pillar, float] | None = None,
   230	    n_draws: int = 2000,
   231	    seed: int = 0,
   232	) -> WeightSensitivity:
   233	    """Sensitivity of U to the weights w (source: 'weights preregistered; sensitivity analysis').
   234	
   235	    U is linear in w, so over the whole weight simplex its exact range is
   236	    [min_m H_m (1 - Q_m), max_m H_m (1 - Q_m)] (attained at the vertices). ``draws`` samples
   237	    w uniformly on the simplex (Dirichlet(1, ..., 1)) to show the typical spread.
   238	    """
   239	    if n_draws < 1:
   240	        raise ValueError("n_draws must be positive")
   241	    baseline = unaccountable_concentration(H, Q, weights)
   242	    h = _per_pillar(H, "H")
   243	    q = _per_pillar(Q, "Q")
   244	    terms = np.array([h[m] * (1.0 - q[m]) for m in PILLARS])
   245	    rng = np.random.default_rng(seed)
   246	    w = rng.dirichlet(np.ones(M), size=n_draws)
   247	    return WeightSensitivity(
   248	        baseline=baseline,
   249	        vertex_min=float(terms.min()),
   250	        vertex_max=float(terms.max()),
   251	        draws=(w * terms).sum(axis=1),
   252	    )

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/network.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Directed multiplex polity network G_t = (V_t, E_t) (source Section 5; notation.md).
     2	
     3	One weighted adjacency A^m per pillar, with a^m_ij in [0,1] the documented capacity of actor
     4	i to constrain a feasible action of actor j through mechanism m, and a many-to-many role
     5	map V -> 2^M.
     6	"""
     7	
     8	from __future__ import annotations
     9	
    10	from collections.abc import Iterable, Mapping
    11	from dataclasses import dataclass, field
    12	
    13	import numpy as np
    14	
    15	from .pillars import PILLARS, Pillar
    16	
    17	
    18	@dataclass(frozen=True)
    19	class MultiplexNetwork:
    20	    """Polity multiplex G_t with layers A^m_t and role map (notation.md 'Core objects').
    21	
    22	    Layers missing from ``layers`` are taken as all-zero. Arrays are copied and frozen.
    23	    """
    24	
    25	    actors: tuple[str, ...]
    26	    layers: Mapping[Pillar, np.ndarray]
    27	    roles: Mapping[str, Iterable[Pillar]] = field(default_factory=dict)
    28	
    29	    def __post_init__(self) -> None:
    30	        actors = tuple(self.actors)
    31	        if not actors:
    32	            raise ValueError("a polity network needs at least one actor")
    33	        if any(not isinstance(a, str) or not a for a in actors):
    34	            raise ValueError("actors must be non-empty strings")
    35	        if len(set(actors)) != len(actors):
    36	            raise ValueError("actor names must be unique")
    37	        n = len(actors)
    38	
    39	        layers: dict[Pillar, np.ndarray] = {}
    40	        for key, raw in self.layers.items():
    41	            if not isinstance(key, Pillar):
    42	                raise TypeError(f"layer key {key!r} is not a Pillar")
    43	            arr = np.array(raw, dtype=float)
    44	            if arr.shape != (n, n):
    45	                raise ValueError(f"layer {key.name} has shape {arr.shape}, expected {(n, n)}")
    46	            if not np.all(np.isfinite(arr)):
    47	                raise ValueError(f"layer {key.name} has non-finite weights")
    48	            if arr.min() < 0.0 or arr.max() > 1.0:
    49	                raise ValueError(f"layer {key.name} weights must lie in [0, 1]")
    50	            arr.setflags(write=False)
    51	            layers[key] = arr
    52	        for m in PILLARS:
    53	            if m not in layers:
    54	                zero = np.zeros((n, n))
    55	                zero.setflags(write=False)
    56	                layers[m] = zero
    57	
    58	        known = set(actors)
    59	        roles: dict[str, frozenset[Pillar]] = {a: frozenset() for a in actors}
    60	        for actor, pillars in self.roles.items():
    61	            if actor not in known:
    62	                raise ValueError(f"role map names unknown actor {actor!r}")
    63	            ps = frozenset(pillars)
    64	            if any(not isinstance(p, Pillar) for p in ps):
    65	                raise TypeError(f"role map for {actor!r} contains a non-Pillar")
    66	            roles[actor] = ps
    67	
    68	        object.__setattr__(self, "actors", actors)
    69	        object.__setattr__(self, "layers", layers)
    70	        object.__setattr__(self, "roles", roles)
    71	
    72	    @property
    73	    def n(self) -> int:
    74	        return len(self.actors)
    75	
    76	    def layer(self, m: Pillar) -> np.ndarray:
    77	        """Adjacency A^m (read-only)."""
    78	        return self.layers[m]
    79	
    80	    def holders(self, m: Pillar) -> frozenset[str]:
    81	        """Actors whose role set contains m."""
    82	        return frozenset(a for a, ps in self.roles.items() if m in ps)
    83	
    84	    def has_full_support(self) -> bool:
    85	        """Role-map surjectivity: every pillar has at least one holder (KB Section 4.3, item 1)."""
    86	        return all(self.holders(m) for m in PILLARS)
    87	
    88	    def fused_actors(self) -> frozenset[str]:
    89	        """Actors assigned to two or more pillars by the role map."""
    90	        return frozenset(a for a, ps in self.roles.items() if len(ps) >= 2)
    91	
    92	    def out_strength_shares(self, m: Pillar) -> dict[str, float]:
    93	        """Control shares s^m_i proportional to out-strength sum_j a^m_ij.
    94	
    95	        One preregistrable operationalization of s^m (not fixed by the source). Raises if
    96	        layer m has no edges, since shares would then be undefined.
    97	        """
    98	        strength = self.layers[m].sum(axis=1)
    99	        total = float(strength.sum())
   100	        if total <= 0.0:
   101	            raise ValueError(f"layer {m.name} has no edges; control shares are undefined")
   102	        return {a: float(s / total) for a, s in zip(self.actors, strength)}

exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_dynamics_regimes.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	import numpy as np
     2	import pytest
     3	
     4	from beast_system.capture import CaptureThresholds, assess
     5	from beast_system.dynamics import (
     6	    dependency_matrix,
     7	    deviation_persists,
     8	    negative_feedback_example,
     9	    simulate,
    10	    spectral_radius,
    11	)
    12	from beast_system.pillars import PILLARS, Pillar
    13	from beast_system.regimes import regime_profiles
    14	
    15	
    16	def test_spectral_radius_diagonal_and_rotation():
    17	    assert spectral_radius(np.diag([0.5, -1.2, 0.1, 0, 0, 0])) == pytest.approx(1.2)
    18	    R = np.zeros((6, 6))
    19	    R[0, 1], R[1, 0] = -1.0, 1.0  # rotation block, eigenvalues +-i
    20	    assert spectral_radius(R) == pytest.approx(1.0)
    21	    assert deviation_persists(R)
    22	    with pytest.raises(ValueError):
    23	        spectral_radius(np.eye(3))
    24	
    25	
    26	def test_dependency_matrix_orientation():
    27	    B = dependency_matrix({Pillar.W: {Pillar.C}}, weight=0.3)
    28	    assert B[Pillar.C.position, Pillar.W.position] == 0.3
    29	    assert B[Pillar.W.position, Pillar.C.position] == 0.0
    30	
    31	
    32	def test_positive_links_do_not_guarantee_persistence():
    33	    ex = negative_feedback_example()
    34	    assert ex.same_positive_links
    35	    assert ex.rho_positive > 1.0 and deviation_persists(ex.B_positive)
    36	    assert ex.rho_feedback < 1.0 and not deviation_persists(ex.B_feedback)
    37	    assert (ex.B_feedback < 0).sum() == 2
    38	
    39	
    40	def test_simulation_decays_or_grows_with_spectral_radius():
    41	    ex = negative_feedback_example()
    42	    x0 = np.ones(6)
    43	    decay = simulate(ex.B_feedback, x0, 200)
    44	    grow = simulate(ex.B_positive, x0, 200)
    45	    assert decay.shape == (201, 6)
    46	    assert np.linalg.norm(decay[-1]) < 1e-6
    47	    assert np.linalg.norm(grow[-1]) > 1e3
    48	
    49	
    50	def test_simulation_with_shocks_and_noise():
    51	    B = 0.5 * np.eye(6)
    52	    D = np.ones((6, 1))
    53	    z = np.ones((50, 1))
    54	    path = simulate(B, np.zeros(6), 50, D=D, z=z)
    55	    assert path[-1] == pytest.approx(np.full(6, 2.0))  # steady state (I - B)^-1 D z
    56	    a = simulate(B, np.zeros(6), 5, noise_sd=0.1, seed=3)
    57	    b = simulate(B, np.zeros(6), 5, noise_sd=0.1, seed=3)
    58	    assert np.array_equal(a, b)
    59	    with pytest.raises(ValueError):
    60	        simulate(B, np.zeros(6), 5, D=D)
    61	
    62	
    63	def test_all_regimes_satisfy_proposition_a():
    64	    for prof in regime_profiles():
    65	        a = assess(prof.polity)
    66	        assert a.prop_a.holds, prof.label
    67	        assert 0.0 <= a.U <= 1.0 and 0.0 <= a.I <= 1.0
    68	        assert prof.illustrative and "not a measurement" in prof.rationale
    69	
    70	
    71	def test_six_regime_types_with_variants():
    72	    types = {p.regime_type for p in regime_profiles()}
    73	    assert len(types) == 6
    74	    labels = [p.label for p in regime_profiles()]
    75	    assert len(labels) == len(set(labels))
    76	
    77	
    78	def test_no_regime_satisfies_b_without_evidenced_links():
    79	    for prof in regime_profiles():
    80	        assert not assess(prof.polity).prop_b.holds
    81	
    82	
    83	@pytest.mark.parametrize("rtype", ["Islamic state", "Catholic monarchy"])
    84	def test_religious_types_vary_and_have_a_variant_below_thresholds(rtype):
    85	    th = CaptureThresholds()
    86	    variants = [assess(p.polity, th) for p in regime_profiles() if p.regime_type == rtype]
    87	    assert len(variants) == 2
    88	    assert any(not v.prop_b.thresholds_met for v in variants)
    89	    assert abs(variants[0].U - variants[1].U) > 0.05
    90	    assert abs(variants[0].I - variants[1].I) > 0.05
    91	
    92	
    93	def test_regimes_differ_in_h_q_c():
    94	    profs = regime_profiles()
    95	    hs = {tuple(round(v, 6) for v in p.polity.H.values()) for p in profs}
    96	    qs = {tuple(p.polity.contestability.values()) for p in profs}
    97	    cs = {p.polity.integration.round(6).tobytes() for p in profs}
    98	    assert len(hs) == len(qs) == len(cs) == len(profs)
    99	    assert all(set(p.polity.H) == set(PILLARS) for p in profs)

exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_pillars_network.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	import numpy as np
     2	import pytest
     3	
     4	from beast_system.network import MultiplexNetwork
     5	from beast_system.pillars import AXIOM_TO_PILLAR, M, PAIRS, PILLARS, Axiom, Pillar
     6	
     7	
     8	def test_six_pillars_with_labels_and_questions():
     9	    assert M == 6
    10	    assert [p.label for p in PILLARS] == [
    11	        "financial", "political", "judicial", "ideological", "coercive", "productive"]
    12	    assert Pillar.J.question == "Who interprets the laws?"
    13	    assert [p.position for p in PILLARS] == list(range(6))
    14	
    15	
    16	def test_axiom_map_is_bijection_in_kb_order():
    17	    assert [a.label for a in Axiom] == [
    18	        "scarcity", "plurality", "generality", "coordination", "defection", "maintenance"]
    19	    assert set(AXIOM_TO_PILLAR.values()) == set(PILLARS)
    20	    assert Axiom.Ax5.pillar is Pillar.C and Axiom.Ax6.pillar is Pillar.W
    21	
    22	
    23	def test_fifteen_pairs():
    24	    assert len(PAIRS) == 15 == M * (M - 1) // 2
    25	
    26	
    27	def _net(**overrides):
    28	    kw = dict(actors=("a", "b"), layers={Pillar.F: [[0, 0.5], [0.2, 0]]},
    29	              roles={"a": {Pillar.F}})
    30	    kw.update(overrides)
    31	    return MultiplexNetwork(**kw)
    32	
    33	
    34	def test_network_fills_missing_layers_and_freezes():
    35	    net = _net()
    36	    assert net.layer(Pillar.W).shape == (2, 2) and not net.layer(Pillar.W).any()
    37	    with pytest.raises(ValueError):
    38	        net.layer(Pillar.F)[0, 1] = 0.9
    39	
    40	
    41	@pytest.mark.parametrize("bad", [[[0, 1.2], [0, 0]], [[0, -0.1], [0, 0]], [[0, np.nan], [0, 0]]])
    42	def test_network_rejects_weights_outside_unit_interval(bad):
    43	    with pytest.raises(ValueError):
    44	        _net(layers={Pillar.F: bad})
    45	
    46	
    47	def test_network_rejects_wrong_shape_and_unknown_role_actor():
    48	    with pytest.raises(ValueError):
    49	        _net(layers={Pillar.F: np.zeros((3, 3))})
    50	    with pytest.raises(ValueError):
    51	        _net(roles={"zed": {Pillar.F}})
    52	    with pytest.raises(ValueError):
    53	        _net(actors=("a", "a"))
    54	
    55	
    56	def test_role_map_support_and_fusion():
    57	    net = _net(roles={"a": {Pillar.F, Pillar.P}, "b": set(PILLARS) - {Pillar.F, Pillar.P}})
    58	    assert net.has_full_support()
    59	    assert net.fused_actors() == {"a", "b"}
    60	    assert not _net().has_full_support()
    61	
    62	
    63	def test_out_strength_shares():
    64	    shares = _net().out_strength_shares(Pillar.F)
    65	    assert shares == pytest.approx({"a": 0.5 / 0.7, "b": 0.2 / 0.7})
    66	    with pytest.raises(ValueError):
    67	        _net().out_strength_shares(Pillar.C)

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/pillars.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Pillar and axiom vocabulary.
     2	
     3	Pillars follow team/notation.md (index set M = {F, P, J, I, C, W}, M = 6); axioms follow
     4	the working set Ax1..Ax6 of the knowledge base, Section 4.2 (Part VII owns and refines them).
     5	"""
     6	
     7	from __future__ import annotations
     8	
     9	from enum import Enum
    10	from itertools import combinations
    11	
    12	
    13	class Pillar(Enum):
    14	    """The six pillars. The source's rule function L is split into P and J (notation.md)."""
    15	
    16	    F = "F"
    17	    P = "P"
    18	    J = "J"
    19	    I = "I"  # noqa: E741  (pillar label, not the integration statistic)
    20	    C = "C"
    21	    W = "W"
    22	
    23	    @property
    24	    def label(self) -> str:
    25	        """Long name, e.g. 'financial'."""
    26	        return _LABELS[self]
    27	
    28	    @property
    29	    def question(self) -> str:
    30	        """Guiding question of the Part that owns the pillar (notation.md table)."""
    31	        return _QUESTIONS[self]
    32	
    33	    @property
    34	    def position(self) -> int:
    35	        """Row/column of the pillar in 6x6 arrays (order F, P, J, I, C, W)."""
    36	        return PILLARS.index(self)
    37	
    38	
    39	_LABELS = {
    40	    Pillar.F: "financial",
    41	    Pillar.P: "political",
    42	    Pillar.J: "judicial",
    43	    Pillar.I: "ideological",
    44	    Pillar.C: "coercive",
    45	    Pillar.W: "productive",
    46	}
    47	
    48	_QUESTIONS = {
    49	    Pillar.F: "Who controls the resources?",
    50	    Pillar.P: "Who makes the laws?",
    51	    Pillar.J: "Who interprets the laws?",
    52	    Pillar.I: "Who shapes the beliefs?",
    53	    Pillar.C: "Who enforces the rules?",
    54	    Pillar.W: "Who produces the wealth that sustains everything?",
    55	}
    56	
    57	PILLARS: tuple[Pillar, ...] = tuple(Pillar)
    58	M: int = len(PILLARS)
    59	#: The M(M-1)/2 = 15 unordered pillar pairs (m < n) summed in the integration statistic.
    60	PAIRS: tuple[tuple[Pillar, Pillar], ...] = tuple(combinations(PILLARS, 2))
    61	
    62	
    63	class Axiom(Enum):
    64	    """Working axioms about collective life (KB Section 4.2; notation.md CENTRAL THESIS)."""
    65	
    66	    Ax1 = "scarcity"
    67	    Ax2 = "plurality"
    68	    Ax3 = "generality"
    69	    Ax4 = "coordination"
    70	    Ax5 = "defection"
    71	    Ax6 = "maintenance"
    72	
    73	    @property
    74	    def label(self) -> str:
    75	        return self.value
    76	
    77	    @property
    78	    def statement(self) -> str:
    79	        return _STATEMENTS[self]
    80	
    81	    @property
    82	    def pillar(self) -> Pillar:
    83	        """The pillar whose function solves the problem this axiom generates."""
    84	        return AXIOM_TO_PILLAR[self]
    85	
    86	
    87	_STATEMENTS = {
    88	    Axiom.Ax1: "resources are finite and claims on them conflict",
    89	    Axiom.Ax2: "members' preferences diverge and some collective choices must be made",
    90	    Axiom.Ax3: "rules are general, cases are particular, and disputes arise",
    91	    Axiom.Ax4: "compliance and cooperation need shared beliefs or common knowledge",
    92	    Axiom.Ax5: "some members sometimes break rules",
    93	    Axiom.Ax6: "the group and its institutions consume resources that someone produces",
    94	}
    95	
    96	#: Axiom -> pillar map (KB Section 4.2 table, 'Yields' column). It is a bijection.
    97	AXIOM_TO_PILLAR: dict[Axiom, Pillar] = {
    98	    Axiom.Ax1: Pillar.F,
    99	    Axiom.Ax2: Pillar.P,
   100	    Axiom.Ax3: Pillar.J,
   101	    Axiom.Ax4: Pillar.I,
   102	    Axiom.Ax5: Pillar.C,
   103	    Axiom.Ax6: Pillar.W,
   104	}
   105	PILLAR_TO_AXIOM: dict[Pillar, Axiom] = {p: a for a, p in AXIOM_TO_PILLAR.items()}

exec
/usr/local/bin/zsh -lc 'nl -ba model/examples/run_all.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Print the Part VII summary table: regime profiles, counter-model, dependency graph.
     2	
     3	Run from model/:  python3 examples/run_all.py
     4	Regime values are ILLUSTRATIVE ASSUMPTIONS, not measurements (see beast_system.regimes).
     5	"""
     6	
     7	from __future__ import annotations
     8	
     9	import sys
    10	from pathlib import Path
    11	
    12	sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    13	
    14	from beast_system.capture import Assessment, CaptureThresholds, a_does_not_imply_b, assess  # noqa: E402
    15	from beast_system.dynamics import negative_feedback_example  # noqa: E402
    16	from beast_system.necessity import (  # noqa: E402
    17	    BRIEF_DEPENDENCIES,
    18	    HARD_CASES,
    19	    check_proposition_a,
    20	    critical_edges,
    21	    dependency_graph,
    22	    is_strongly_connected,
    23	    sinks_and_sources,
    24	)
    25	from beast_system.pillars import PILLARS  # noqa: E402
    26	from beast_system.regimes import regime_profiles  # noqa: E402
    27	
    28	
    29	def _yn(flag: bool) -> str:
    30	    return "yes" if flag else "no"
    31	
    32	
    33	def _row(label: str, a: Assessment) -> str:
    34	    hs = " ".join(f"{a.H[m]:.2f}" for m in PILLARS)
    35	    b = a.prop_b
    36	    return (f"{label:<58} {hs}  {a.U:.3f}  {a.I:.3f}  {_yn(a.prop_a.holds):<3}  "
    37	            f"{_yn(b.thresholds_met):<6}  {b.n_links}  {_yn(b.holds)}")
    38	
    39	
    40	def main() -> None:
    41	    th = CaptureThresholds()
    42	    head_h = " ".join(f"H_{m.name:<3}" for m in PILLARS)
    43	    header = (f"{'profile':<58} {head_h} U      I      A    U,I>=*  L  B")
    44	    print(f"Thresholds u* = {th.u_star}, i* = {th.i_star}. "
    45	          "Regime values: ILLUSTRATIVE ASSUMPTIONS, not measurements.")
    46	    print(header)
    47	    print("-" * len(header))
    48	    for prof in regime_profiles():
    49	        print(_row(prof.label, assess(prof.polity, th)))
    50	    print("-" * len(header))
    51	    cm = a_does_not_imply_b(th)
    52	    print(_row("[counter-model] " + cm.plural.name, cm.plural))
    53	    print(_row("[counter-model] " + cm.fused.name, cm.fused))
    54	    print(f"A does not imply B (constructive counter-model): {cm.demonstrates_non_implication}")
    55	    print("L = evidenced capture links; regime profiles carry none, so B never holds for them.")
    56	
    57	    print("\nHard cases (Theorem A check):")
    58	    for sys_ in HARD_CASES:
    59	        r = check_proposition_a(sys_)
    60	        forms = ", ".join(f"{d.pillar.name}:{d.form}" for d in r.derivations.values())
    61	        print(f"  {sys_.name:<36} A={_yn(r.holds)} counterexample={_yn(r.counterexample)}  {forms}")
    62	
    63	    derived = dependency_graph(include_conditional=False)
    64	    full = dependency_graph(include_conditional=True)
    65	    brief = dependency_graph(dependencies=BRIEF_DEPENDENCIES)
    66	    print("\nDependency graph (provider -> dependent):")
    67	    print(f"  derived edges only: strongly connected = {is_strongly_connected(derived)}; "
    68	          "critical edges = "
    69	          + ", ".join(f"{u.name}->{v.name}" for u, v in critical_edges(derived)))
    70	    print(f"  derived + conditional: strongly connected = {is_strongly_connected(full)}")
    71	    sinks, _ = sinks_and_sources(brief)
    72	    print(f"  six brief relations alone: strongly connected = {is_strongly_connected(brief)}; "
    73	          f"sinks = {sorted(m.name for m in sinks)}")
    74	
    75	    fb = negative_feedback_example()
    76	    print("\nDynamics: same positive links, rho(B+) = "
    77	          f"{fb.rho_positive:.3f} (persists), rho(B+ with negative feedback) = "
    78	          f"{fb.rho_feedback:.3f} (decays); same positive links = {fb.same_positive_links}")
    79	
    80	
    81	if __name__ == "__main__":
    82	    main()

exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_necessity.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	import pytest
     2	
     3	from beast_system.necessity import (
     4	    BRIEF_DEPENDENCIES,
     5	    DEPENDENCIES,
     6	    FORMAL,
     7	    FUSED,
     8	    HARD_CASES,
     9	    INFORMAL,
    10	    JU_HOANSI,
    11	    GovernanceSystem,
    12	    Practice,
    13	    check_proposition_a,
    14	    critical_edges,
    15	    dependency_graph,
    16	    derive_functions,
    17	    formal_system,
    18	    is_strongly_connected,
    19	    role_map,
    20	    sinks_and_sources,
    21	)
    22	from beast_system.pillars import PILLARS, Axiom, Pillar
    23	
    24	F, P, J, I, C, W = PILLARS
    25	
    26	
    27	@pytest.mark.parametrize("system", HARD_CASES, ids=lambda s: s.name)
    28	def test_theorem_a_on_hard_cases(system):
    29	    result = check_proposition_a(system)
    30	    assert result.antecedent
    31	    assert result.holds and not result.counterexample
    32	    assert result.realized == frozenset(PILLARS)
    33	    derivs = derive_functions(system)
    34	    assert {d.pillar for d in derivs.values()} == set(PILLARS)
    35	    assert all(d.form == INFORMAL for d in derivs.values())
    36	
    37	
    38	def test_role_map_is_derived_from_practices():
    39	    roles = role_map(JU_HOANSI)
    40	    assert Pillar.C in roles["camp members"] and Pillar.P in roles["camp members"]
    41	
    42	
    43	def test_missing_axiom_drops_pillar_and_is_not_a_counterexample():
    44	    # A perfectly cooperative collective: Ax5 fails and there is no sanction practice.
    45	    practices = tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5)
    46	    system = GovernanceSystem("no defection", True, frozenset(Axiom) - {Axiom.Ax5}, practices)
    47	    derivs = derive_functions(system)
    48	    assert Axiom.Ax5 not in derivs and len(derivs) == 5
    49	    result = check_proposition_a(system)
    50	    assert not result.antecedent
    51	    assert result.missing == {C}
    52	    assert not result.holds and not result.counterexample
    53	
    54	
    55	def test_falsifier_is_reported():
    56	    # All axioms coded as holding, persistent, but no sanction practice: a counterexample.
    57	    practices = tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5)
    58	    system = GovernanceSystem("hypothetical", True, frozenset(Axiom), practices)
    59	    result = check_proposition_a(system)
    60	    assert result.counterexample
    61	    assert derive_functions(system)[Axiom.Ax5].form is None
    62	
    63	
    64	def test_non_persistent_system_does_not_trigger_theorem():
    65	    system = GovernanceSystem("short-lived", False, frozenset(Axiom), ())
    66	    assert not check_proposition_a(system).antecedent
    67	    assert not check_proposition_a(system).counterexample
    68	
    69	
    70	def test_fused_and_formal_forms():
    71	    system = formal_system("toy", {F: ["Treasury"], P: ["Crown"], J: ["Crown"], I: ["Church"],
    72	                                   C: ["Crown"], W: ["Peasants"]})
    73	    derivs = derive_functions(system)
    74	    assert derivs[Axiom.Ax2].form == FUSED
    75	    assert derivs[Axiom.Ax5].form == FUSED
    76	    assert derivs[Axiom.Ax1].form == FORMAL
    77	    assert check_proposition_a(system).holds
    78	
    79	
    80	def test_practice_validation():
    81	    with pytest.raises(ValueError):
    82	        Practice("x", Axiom.Ax1, frozenset())
    83	    with pytest.raises(TypeError):
    84	        Practice("x", Pillar.F, frozenset({"a"}))  # type: ignore[arg-type]
    85	
    86	
    87	def test_dependency_edges_are_documented():
    88	    for d in DEPENDENCIES:
    89	        assert d.provider is not d.dependent
    90	        assert d.rationale and len(d.basis) == 2
    91	        assert d.status in {"derived", "conditional"}
    92	    pairs = [(d.provider, d.dependent) for d in DEPENDENCIES]
    93	    assert len(pairs) == len(set(pairs))
    94	    brief = {(d.provider, d.dependent) for d in BRIEF_DEPENDENCIES}
    95	    assert brief == {(W, C), (P, J), (I, P), (J, F), (F, W), (W, I)}
    96	
    97	
    98	def test_encoded_dependency_graph_strong_connectivity():
    99	    assert is_strongly_connected(dependency_graph(include_conditional=False))
   100	    assert is_strongly_connected(dependency_graph(include_conditional=True))
   101	
   102	
   103	def test_brief_relations_alone_are_not_strongly_connected():
   104	    brief = dependency_graph(dependencies=BRIEF_DEPENDENCIES)
   105	    assert not is_strongly_connected(brief)
   106	    sinks, sources = sinks_and_sources(brief)
   107	    assert sinks == {C} and not sources
   108	
   109	
   110	def test_critical_edges_of_derived_graph():
   111	    crit = critical_edges(dependency_graph(include_conditional=False))
   112	    assert set(crit) == {(F, W), (P, J), (J, F), (I, P), (W, I)}
   113	    assert critical_edges(dependency_graph(include_conditional=True)) == []
   114	
   115	
   116	def test_strong_connectivity_small_cases():
   117	    assert not is_strongly_connected({})
   118	    assert is_strongly_connected({F: set()})
   119	    assert is_strongly_connected({F: {P}, P: {F}})
   120	    assert not is_strongly_connected({F: {P}, P: set()})
   121	    assert is_strongly_connected({F: {P}, P: {F, J}}, nodes={F, P})

exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_capture.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	import pytest
     2	
     3	from beast_system.capture import (
     4	    CaptureLink,
     5	    CaptureThresholds,
     6	    a_does_not_imply_b,
     7	    fused_polity,
     8	    is_capture_link,
     9	    plural_polity,
    10	    proposition_b,
    11	)
    12	from beast_system.pillars import Pillar
    13	
    14	
    15	def _link(access=True, weakens=True, evidence=True):
    16	    return CaptureLink("donor", "agency", Pillar.P, access, weakens, evidence,
    17	                       evidence="procurement record" if evidence else "")
    18	
    19	
    20	def test_capture_link_needs_all_three_conditions():
    21	    assert is_capture_link(_link())
    22	
    23	
    24	@pytest.mark.parametrize("missing", ["access", "weakens", "evidence"])
    25	def test_each_capture_condition_is_necessary(missing):
    26	    assert not is_capture_link(_link(**{missing: False}))
    27	
    28	
    29	def test_disclosure_compliant_meeting_is_not_capture():
    30	    # Privileged access alone, with no weakening of accountability and no evidence.
    31	    assert not is_capture_link(_link(weakens=False, evidence=False))
    32	
    33	
    34	def test_material_evidence_must_be_cited():
    35	    with pytest.raises(ValueError):
    36	        CaptureLink("a", "b", Pillar.J, True, True, True, evidence="  ")
    37	    with pytest.raises(ValueError):
    38	        CaptureLink("", "b", Pillar.J, True, True, False)
    39	
    40	
    41	def test_prop_b_needs_u_i_and_link():
    42	    th = CaptureThresholds(u_star=0.4, i_star=0.5)
    43	    assert proposition_b(0.6, 0.7, [_link()], th).holds
    44	    assert not proposition_b(0.6, 0.7, [], th).holds
    45	    assert not proposition_b(0.6, 0.7, [_link(evidence=False)], th).holds
    46	    assert not proposition_b(0.3, 0.7, [_link()], th).holds
    47	    assert not proposition_b(0.6, 0.4, [_link()], th).holds
    48	    assert proposition_b(0.4, 0.5, [_link()], th).holds  # thresholds are inclusive
    49	
    50	
    51	def test_thresholds_validated():
    52	    with pytest.raises(ValueError):
    53	        CaptureThresholds(u_star=1.5)
    54	    with pytest.raises(ValueError):
    55	        proposition_b(1.2, 0.5, [])
    56	
    57	
    58	def test_counter_model_a_does_not_imply_b():
    59	    cm = a_does_not_imply_b()
    60	    assert cm.plural.prop_a.holds and cm.fused.prop_a.holds
    61	    assert not cm.plural.prop_b.holds and cm.fused.prop_b.holds
    62	    assert cm.demonstrates_non_implication
    63	
    64	
    65	def test_counter_model_index_values():
    66	    g1, g2 = plural_polity(), fused_polity()
    67	    assert g1.U == pytest.approx(0.2 * 0.1)
    68	    assert g1.I == 0.0
    69	    assert g2.U == pytest.approx(0.95)
    70	    assert g2.I == 1.0
    71	    assert all(h == pytest.approx(1.0) for h in g2.H.values())
    72	
    73	
    74	def test_counter_model_robust_to_thresholds():
    75	    for u_star, i_star in [(0.1, 0.1), (0.5, 0.5), (0.9, 0.9)]:
    76	        assert a_does_not_imply_b(CaptureThresholds(u_star, i_star)).demonstrates_non_implication

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/necessity.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Structural necessity: Proposition A and the pillar dependency graph (Part VII Theorem A).
     2	
     3	Theorem A (notation.md CENTRAL THESIS; KB Section 4): if a governance system G persists and
     4	satisfies Ax1..Ax6, then every pillar in M is implemented in G, and the pillars stand in the
     5	dependency relations D. Implementation is role-level, not institution-level (Hempel 1959): a
     6	function may be held by a formal institution, fused with other functions inside one
     7	institution, or exercised informally (gossip and shunning as C, mediators as J).
     8	
     9	What this module does and does not do. It cannot prove Theorem A. It encodes the lemma schema
    10	'Ax_k + persistence => some practice solves problem_k' and checks it against coded cases. The
    11	role map is DERIVED from independently coded practices, never declared, so a persistent case
    12	that satisfies all six axioms yet has no practice for some problem is reported as a
    13	counterexample (the falsifier required by KB Section 4.4), not silently accepted.
    14	
    15	Dependency edges are written provider -> dependent ('dependent needs provider'). Each edge
    16	carries its axiom basis and a status: 'derived' (argued from the axioms for every persistent
    17	G) or 'conditional' (holds only under an extra assumption, e.g. specialized office holders).
    18	Strong connectivity of D is flagged in KB Section 4.3 as an OPEN problem; it is tested here on
    19	the encoded graph, which is a property of the encoding, not a proof that it is forced.
    20	"""
    21	
    22	from __future__ import annotations
    23	
    24	from collections.abc import Iterable, Mapping
    25	from dataclasses import dataclass, field
    26	from typing import Literal
    27	
    28	from .pillars import AXIOM_TO_PILLAR, PILLAR_TO_AXIOM, PILLARS, Axiom, Pillar
    29	
    30	RealizedForm = Literal["formal institution", "fused", "informal/minimal"]
    31	FORMAL: RealizedForm = "formal institution"
    32	FUSED: RealizedForm = "fused"
    33	INFORMAL: RealizedForm = "informal/minimal"
    34	
    35	
    36	@dataclass(frozen=True)
    37	class Practice:
    38	    """A regular activity that discharges the problem generated by axiom ``solves``.
    39	
    40	    ``formal`` is True when the activity is attached to a designated office or organization.
    41	    ``source`` holds the citation key(s) supporting the coding.
    42	    """
    43	
    44	    description: str
    45	    solves: Axiom
    46	    holders: frozenset[str]
    47	    formal: bool = False
    48	    source: str = ""
    49	
    50	    def __post_init__(self) -> None:
    51	        if not isinstance(self.solves, Axiom):
    52	            raise TypeError("Practice.solves must be an Axiom")
    53	        holders = frozenset(self.holders)
    54	        if not holders or any(not isinstance(h, str) or not h for h in holders):
    55	            raise ValueError("a practice needs at least one named holder")
    56	        if not self.description.strip():
    57	            raise ValueError("a practice needs a description")
    58	        object.__setattr__(self, "holders", holders)
    59	
    60	    @property
    61	    def pillar(self) -> Pillar:
    62	        return AXIOM_TO_PILLAR[self.solves]
    63	
    64	
    65	@dataclass(frozen=True)
    66	class GovernanceSystem:
    67	    """A collective that makes and enforces collective decisions (KB Section 4.1).
    68	
    69	    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
    70	    over the period studied. Both are coded independently of ``practices``.
    71	    """
    72	
    73	    name: str
    74	    persistent: bool
    75	    axioms: frozenset[Axiom]
    76	    practices: tuple[Practice, ...] = ()
    77	    note: str = ""
    78	
    79	    def __post_init__(self) -> None:
    80	        axioms = frozenset(self.axioms)
    81	        if any(not isinstance(a, Axiom) for a in axioms):
    82	            raise TypeError("axioms must be Axiom members")
    83	        practices = tuple(self.practices)
    84	        if any(not isinstance(p, Practice) for p in practices):
    85	            raise TypeError("practices must be Practice instances")
    86	        object.__setattr__(self, "axioms", axioms)
    87	        object.__setattr__(self, "practices", practices)
    88	
    89	    def holds(self, axiom: Axiom) -> bool:
    90	        """Predicate for one axiom (Ax1 scarcity, ..., Ax6 maintenance)."""
    91	        return axiom in self.axioms
    92	
    93	    @property
    94	    def all_axioms_hold(self) -> bool:
    95	        return all(self.holds(a) for a in Axiom)
    96	
    97	
    98	def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
    99	    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
   100	    roles: dict[str, set[Pillar]] = {}
   101	    for p in system.practices:
   102	        for h in p.holders:
   103	            roles.setdefault(h, set()).add(p.pillar)
   104	    return {h: frozenset(ps) for h, ps in roles.items()}
   105	
   106	
   107	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   108	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   109	
   110	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   111	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   112	    """
   113	    practices = [p for p in system.practices if p.pillar is pillar]
   114	    if not practices:
   115	        return None
   116	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   117	    if not formal_holders:
   118	        return INFORMAL
   119	    formal_roles: dict[str, set[Pillar]] = {}
   120	    for p in system.practices:
   121	        if p.formal:
   122	            for h in p.holders:
   123	                formal_roles.setdefault(h, set()).add(p.pillar)
   124	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   125	        return FUSED
   126	    return FORMAL
   127	
   128	
   129	@dataclass(frozen=True)
   130	class Derivation:
   131	    """Result of the lemma for one axiom: required pillar and its realized form."""
   132	
   133	    axiom: Axiom
   134	    pillar: Pillar
   135	    form: RealizedForm | None
   136	    practices: tuple[Practice, ...]
   137	
   138	    @property
   139	    def realized(self) -> bool:
   140	        return self.form is not None
   141	
   142	
   143	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   144	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   145	
   146	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   147	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   148	    """
   149	    out: dict[Axiom, Derivation] = {}
   150	    for axiom in Axiom:
   151	        if not system.holds(axiom):
   152	            continue
   153	        pillar = AXIOM_TO_PILLAR[axiom]
   154	        out[axiom] = Derivation(
   155	            axiom=axiom,
   156	            pillar=pillar,
   157	            form=realized_form(system, pillar),
   158	            practices=tuple(p for p in system.practices if p.solves is axiom),
   159	        )
   160	    return out
   161	
   162	
   163	# Dependency graph -------------------------------------------------------------------------
   164	
   165	DependencyStatus = Literal["derived", "conditional"]
   166	Graph = Mapping[Pillar, Iterable[Pillar]]
   167	
   168	
   169	@dataclass(frozen=True)
   170	class Dependency:
   171	    """Edge provider -> dependent: the dependent pillar needs an output of the provider."""
   172	
   173	    provider: Pillar
   174	    dependent: Pillar
   175	    basis: tuple[Axiom, ...]
   176	    status: DependencyStatus
   177	    rationale: str
   178	
   179	
   180	_A = Axiom
   181	_P = Pillar
   182	
   183	#: Encoded dependency relations D (KB Sections 4.3 item 3 and VII.2). The first six entries are
   184	#: the relations listed in the Part VII brief; the remainder come from the KB list.
   185	DEPENDENCIES: tuple[Dependency, ...] = (
   186	    Dependency(_P.W, _P.C, (_A.Ax6, _A.Ax5), "derived",
   187	               "C needs W's resources: sanctioning consumes time and goods someone produces"),
   188	    Dependency(_P.P, _P.J, (_A.Ax2, _A.Ax3), "derived",
   189	               "J needs P's rules: interpretation presupposes rules to interpret"),
   190	    Dependency(_P.I, _P.P, (_A.Ax4, _A.Ax2), "derived",
   191	               "P needs I's legitimacy: rule-making needs a recognized rule of recognition (Hart)"),
   192	    Dependency(_P.J, _P.F, (_A.Ax3, _A.Ax1), "derived",
   193	               "F needs J's enforcement of claims: contested claims on resources need case rulings"),
   194	    Dependency(_P.F, _P.W, (_A.Ax1, _A.Ax6), "derived",
   195	               "W needs F's allocation: producers need allocated inputs and shares"),
   196	    Dependency(_P.W, _P.I, (_A.Ax6, _A.Ax4), "derived",
   197	               "I needs W's surplus: belief maintenance consumes produced resources"),
   198	    Dependency(_P.W, _P.F, (_A.Ax6, _A.Ax1), "derived",
   199	               "production creates the stock that allocation divides"),
   200	    Dependency(_P.C, _P.F, (_A.Ax5, _A.Ax1), "derived",
   201	               "allocation rules are sometimes defected from; sanctions back them"),
   202	    Dependency(_P.C, _P.J, (_A.Ax5, _A.Ax3), "derived",
   203	               "adjudication without enforcement is advice"),
   204	    Dependency(_P.I, _P.J, (_A.Ax4, _A.Ax3), "derived",
   205	               "rulings settle disputes only if recognized as authoritative"),
   206	    Dependency(_P.I, _P.C, (_A.Ax4, _A.Ax5), "derived",
   207	               "a sanction must be recognized as sanction rather than aggression"),
   208	    Dependency(_P.I, _P.W, (_A.Ax4, _A.Ax6), "derived",
   209	               "norms of work and quasi-voluntary compliance (Levi)"),
   210	    Dependency(_P.F, _P.C, (_A.Ax1, _A.Ax5), "conditional",
   211	               "specialized sanction capacity needs provisioning (Tilly, Levi); gossip does not"),
   212	    Dependency(_P.J, _P.P, (_A.Ax3, _A.Ax2), "conditional",
   213	               "precedent feeds rule change; only where rules change through interpretation"),
   214	    Dependency(_P.J, _P.I, (_A.Ax3, _A.Ax4), "conditional",
   215	               "reasoned judgments act as public symbols; needs public adjudication"),
   216	    Dependency(_P.F, _P.I, (_A.Ax1, _A.Ax4), "conditional",
   217	               "funding of ideology producers; needs specialist belief producers"),
   218	    Dependency(_P.P, _P.I, (_A.Ax2, _A.Ax4), "conditional",
   219	               "legislation as a public symbolic act; needs declared rules"),
   220	)
   221	
   222	#: The six relations named in the Part VII brief, on their own.
   223	BRIEF_DEPENDENCIES: tuple[Dependency, ...] = DEPENDENCIES[:6]
   224	
   225	
   226	def dependency_graph(
   227	    include_conditional: bool = True,
   228	    dependencies: Iterable[Dependency] = DEPENDENCIES,
   229	) -> dict[Pillar, frozenset[Pillar]]:
   230	    """Adjacency provider -> set of dependents over all six pillars."""
   231	    adj: dict[Pillar, set[Pillar]] = {m: set() for m in PILLARS}
   232	    for d in dependencies:
   233	        if include_conditional or d.status == "derived":
   234	            adj[d.provider].add(d.dependent)
   235	    return {m: frozenset(v) for m, v in adj.items()}
   236	
   237	
   238	def _nodes(graph: Graph) -> set[Pillar]:
   239	    nodes = set(graph)
   240	    for targets in graph.values():
   241	        nodes.update(targets)
   242	    return nodes
   243	
   244	
   245	def _reach(graph: Mapping[Pillar, frozenset[Pillar]], start: Pillar) -> set[Pillar]:
   246	    seen = {start}
   247	    stack = [start]
   248	    while stack:
   249	        for nxt in graph.get(stack.pop(), frozenset()):
   250	            if nxt not in seen:
   251	                seen.add(nxt)
   252	                stack.append(nxt)
   253	    return seen
   254	
   255	
   256	def is_strongly_connected(graph: Graph, nodes: Iterable[Pillar] | None = None) -> bool:
   257	    """True iff every node of the graph is reachable from every other node.
   258	
   259	    ``nodes`` restricts the graph to an induced subgraph (default: all nodes that appear).
   260	    The empty graph is not strongly connected; a single node is.
   261	    """
   262	    keep = set(nodes) if nodes is not None else _nodes(graph)
   263	    if not keep:
   264	        return False
   265	    fwd: dict[Pillar, frozenset[Pillar]] = {
   266	        u: frozenset(v for v in graph.get(u, ()) if v in keep) for u in keep
   267	    }
   268	    rev: dict[Pillar, set[Pillar]] = {u: set() for u in keep}
   269	    for u, vs in fwd.items():
   270	        for v in vs:
   271	            rev[v].add(u)
   272	    start = next(iter(keep))
   273	    rev_f = {u: frozenset(v) for u, v in rev.items()}
   274	    return _reach(fwd, start) == keep and _reach(rev_f, start) == keep
   275	
   276	
   277	def critical_edges(graph: Graph) -> list[tuple[Pillar, Pillar]]:
   278	    """Edges whose single removal breaks strong connectivity (empty if not connected)."""
   279	    nodes = _nodes(graph)
   280	    base = {u: frozenset(graph.get(u, ())) for u in nodes}
   281	    if not is_strongly_connected(base):
   282	        return []
   283	    out = []
   284	    for u in PILLARS:
   285	        for v in sorted(base.get(u, ()), key=lambda p: p.position):
   286	            pruned = dict(base)
   287	            pruned[u] = base[u] - {v}
   288	            if not is_strongly_connected(pruned, nodes):
   289	                out.append((u, v))
   290	    return out
   291	
   292	
   293	def sinks_and_sources(graph: Graph) -> tuple[frozenset[Pillar], frozenset[Pillar]]:
   294	    """Pillars with no outgoing edge (sinks) and with no incoming edge (sources)."""
   295	    nodes = _nodes(graph)
   296	    has_out = {u for u in nodes if any(True for _ in graph.get(u, ()))}
   297	    has_in = {v for u in nodes for v in graph.get(u, ())}
   298	    return frozenset(nodes - has_out), frozenset(nodes - has_in)
   299	
   300	
   301	# Proposition A ----------------------------------------------------------------------------
   302	
   303	
   304	@dataclass(frozen=True)
   305	class PropositionAResult:
   306	    """Outcome of checking Theorem A on one coded system.
   307	
   308	    ``holds`` is the structural predicate Struct(G): all six pillars realized and the derived
   309	    dependency graph strongly connected on them. ``counterexample`` is True when the theorem's
   310	    antecedent holds (persistent, Ax1..Ax6) but Struct(G) fails: a falsifier of Theorem A.
   311	    """
   312	
   313	    system: str
   314	    antecedent: bool
   315	    realized: frozenset[Pillar]
   316	    missing: frozenset[Pillar]
   317	    dependencies_connected: bool
   318	    holds: bool
   319	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   320	
   321	    @property
   322	    def counterexample(self) -> bool:
   323	        return self.antecedent and not self.holds
   324	
   325	
   326	def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
   327	    """Check Theorem A on ``system`` (Part VII Theorem A; KB Section 4.3)."""
   328	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   329	    connected = is_strongly_connected(dependency_graph(include_conditional=False), realized)
   330	    return PropositionAResult(
   331	        system=system.name,
   332	        antecedent=system.persistent and system.all_axioms_hold,
   333	        realized=realized,
   334	        missing=frozenset(PILLARS) - realized,
   335	        dependencies_connected=connected,
   336	        holds=realized == frozenset(PILLARS) and connected,
   337	        derivations=derive_functions(system),
   338	    )
   339	
   340	
   341	def formal_system(
   342	    name: str,
   343	    holders: Mapping[Pillar, Iterable[str]],
   344	    persistent: bool = True,
   345	    source: str = "",
   346	) -> GovernanceSystem:
   347	    """A persistent system satisfying Ax1..Ax6 whose pillars are held by formal organizations.
   348	
   349	    An actor listed under several pillars is fused. Used for regime profiles and counter-models.
   350	    """
   351	    practices = tuple(
   352	        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
   353	                 frozenset(hs), formal=True, source=source)
   354	        for m, hs in holders.items()
   355	        if hs
   356	    )
   357	    return GovernanceSystem(name, persistent, frozenset(Axiom), practices)
   358	
   359	
   360	# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
   361	
   362	
   363	def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
   364	    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)
   365	
   366	
   367	NUER = GovernanceSystem(
   368	    name="Nuer ('ordered anarchy')",
   369	    persistent=True,
   370	    axioms=frozenset(Axiom),
   371	    practices=(
   372	        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
   373	                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
   374	        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
   375	                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
   376	        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
   377	                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
   378	        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
   379	                  {"prophets", "lineages"}, "evanspritchard1940"),
   380	        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
   381	                  {"agnatic kin"}, "evanspritchard1940"),
   382	        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
   383	                  "evanspritchard1940"),
   384	    ),
   385	    note="no office holds coercive authority; functions exist without separation",
   386	)
   387	
   388	JU_HOANSI = GovernanceSystem(
   389	    name="Ju/'hoansi (!Kung)",
   390	    persistent=True,
   391	    axioms=frozenset(Axiom),
   392	    practices=(
   393	        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
   394	                  {"hunters", "camp members"}, "lee2013; marshall1976"),
   395	        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
   396	                  {"camp members"}, "lee2013"),
   397	        _informal("disputes talked out with kin mediators", Axiom.Ax3,
   398	                  {"kin mediators"}, "lee1979; wiessner2005"),
   399	        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
   400	                  {"healers", "camp members"}, "marshall1976"),
   401	        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
   402	                  {"camp members"}, "wiessner2005; lee2013"),
   403	        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
   404	    ),
   405	    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
   406	)
   407	
   408	OSTROM_COMMONS = GovernanceSystem(
   409	    name="Ostrom commons (design principles)",
   410	    persistent=True,
   411	    axioms=frozenset(Axiom),
   412	    practices=(
   413	        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
   414	                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
   415	        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
   416	                  {"appropriators"}, "ostrom1990"),
   417	        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
   418	                  {"appropriators"}, "ostrom1990; cox2010"),
   419	        _informal("shared norms; minimal recognition of rights to organize (DP7)",
   420	                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),
   421	        _informal("monitoring and graduated sanctions by appropriators (DP4, DP5)",
   422	                  Axiom.Ax5, {"appropriators"}, "ostrom1990; cox2010"),
   423	        _informal("appropriation and maintenance labor", Axiom.Ax6, {"appropriators"},
   424	                  "ostrom1990"),
   425	    ),
   426	    note="checks in minimal form; monitors are appropriators or accountable to them",
   427	)
   428	
   429	CONSENSUS_VILLAGE = GovernanceSystem(
   430	    name="Consensus village (stylized)",
   431	    persistent=True,
   432	    axioms=frozenset(Axiom),
   433	    practices=(
   434	        _informal("household plots; reciprocal labor exchange; sharing norms", Axiom.Ax1,
   435	                  {"households"}, "sahlins1972"),
   436	        _informal("consensus meeting of adults", Axiom.Ax2, {"village meeting"},
   437	                  "clastres1987; boehm1999"),
   438	        _informal("elders mediate disputes", Axiom.Ax3, {"elders"}, "boehm1999"),
   439	        _informal("ritual and myth; moral talk", Axiom.Ax4, {"village meeting", "elders"},
   440	                  "boehm1999"),
   441	        _informal("gossip, shunning, ostracism of would-be dominants", Axiom.Ax5,
   442	                  {"village meeting"}, "boehm1999; woodburn1982"),
   443	        _informal("gardening and household labor", Axiom.Ax6, {"households"},
   444	                  "sahlins1972"),
   445	    ),
   446	    note="stylized composite; reverse dominance hierarchy",
   447	)
   448	
   449	HARD_CASES: tuple[GovernanceSystem, ...] = (NUER, JU_HOANSI, OSTROM_COMMONS, CONSENSUS_VILLAGE)

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/capture.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Capture links, Proposition B, and the non-implication A -/-> B (Part VII Theorem 2).
     2	
     3	Proposition B (notation.md CENTRAL THESIS): the functions become concentrated or coordinated
     4	so that independent accountability fails: U >= u* AND I >= i* AND at least one evidenced
     5	capture link. Proposition A is a statement about the support of the role map; Proposition B
     6	is a threshold on real-valued functionals of (H, Q, C) plus evidence (KB Section 4.3 item 4).
     7	"""
     8	
     9	from __future__ import annotations
    10	
    11	from collections.abc import Mapping
    12	from dataclasses import dataclass, field
    13	
    14	import numpy as np
    15	
    16	from .indices import (
    17	    coalition_integration,
    18	    control_shares,
    19	    hhi,
    20	    integration_statistic,
    21	    unaccountable_concentration,
    22	    validate_integration_matrix,
    23	    validate_unit_interval,
    24	)
    25	from .necessity import GovernanceSystem, PropositionAResult, check_proposition_a, formal_system
    26	from .network import MultiplexNetwork
    27	from .pillars import PILLARS, Pillar
    28	
    29	
    30	@dataclass(frozen=True)
    31	class CaptureLink:
    32	    """Capture link (i -> j, m) (source Section 5; notation.md 'Capture link').
    33	
    34	    All three conditions are required: (i) privileged access or discretion; (ii) the privilege
    35	    weakens otherwise applicable accountability or contestability; (iii) material evidence
    36	    links the asymmetry to an institutional output. A disclosure-compliant donor meeting is
    37	    not automatically capture. Claiming (iii) requires citing the evidence.
    38	    """
    39	
    40	    source: str
    41	    target: str
    42	    pillar: Pillar
    43	    privileged_access: bool
    44	    weakens_accountability: bool
    45	    material_evidence: bool
    46	    evidence: str = ""
    47	
    48	    def __post_init__(self) -> None:
    49	        if not self.source or not self.target:
    50	            raise ValueError("capture link endpoints must be named")
    51	        if not isinstance(self.pillar, Pillar):
    52	            raise TypeError("capture link pillar must be a Pillar")
    53	        if self.material_evidence and not self.evidence.strip():
    54	            raise ValueError("condition (iii) requires a citation of the material evidence")
    55	
    56	    @property
    57	    def holds(self) -> bool:
    58	        return self.privileged_access and self.weakens_accountability and self.material_evidence
    59	
    60	
    61	def is_capture_link(link: CaptureLink) -> bool:
    62	    """Conjunction of the source's three conditions."""
    63	    return link.holds
    64	
    65	
    66	@dataclass(frozen=True)
    67	class CaptureThresholds:
    68	    """Thresholds u*, i* for Proposition B. Illustrative defaults; preregister in applications."""
    69	
    70	    u_star: float = 0.4
    71	    i_star: float = 0.5
    72	
    73	    def __post_init__(self) -> None:
    74	        validate_unit_interval(self.u_star, "u_star")
    75	        validate_unit_interval(self.i_star, "i_star")
    76	
    77	
    78	@dataclass(frozen=True)
    79	class PropositionBResult:
    80	    u_high: bool
    81	    i_high: bool
    82	    n_links: int
    83	
    84	    @property
    85	    def thresholds_met(self) -> bool:
    86	        return self.u_high and self.i_high
    87	
    88	    @property
    89	    def holds(self) -> bool:
    90	        return self.thresholds_met and self.n_links > 0
    91	
    92	
    93	def proposition_b(
    94	    U: float,
    95	    I: float,  # noqa: E741  (integration statistic, math cal I)
    96	    links: tuple[CaptureLink, ...] | list[CaptureLink],
    97	    thresholds: CaptureThresholds = CaptureThresholds(),
    98	) -> PropositionBResult:
    99	    """Proposition B: U >= u* AND I >= i* AND some capture link holds."""
   100	    U = validate_unit_interval(U, "U")
   101	    I = validate_unit_interval(I, "I")  # noqa: E741
   102	    return PropositionBResult(
   103	        u_high=U >= thresholds.u_star,
   104	        i_high=I >= thresholds.i_star,
   105	        n_links=sum(1 for link in links if is_capture_link(link)),
   106	    )
   107	
   108	
   109	@dataclass(frozen=True)
   110	class Polity:
   111	    """A coded polity: governance system (for A) plus index inputs (for B).
   112	
   113	    ``shares[m]`` holds raw non-negative control weights per actor, normalized to s^m.
   114	    """
   115	
   116	    name: str
   117	    system: GovernanceSystem
   118	    shares: Mapping[Pillar, Mapping[str, float]]
   119	    contestability: Mapping[Pillar, float]
   120	    integration: np.ndarray
   121	    capture_links: tuple[CaptureLink, ...] = ()
   122	    weights: Mapping[Pillar, float] | None = None
   123	    normalized_shares: Mapping[Pillar, Mapping[str, float]] = field(init=False, repr=False)
   124	
   125	    def __post_init__(self) -> None:
   126	        if set(self.shares) != set(PILLARS):
   127	            raise ValueError("shares must cover every pillar")
   128	        norm = {m: control_shares(self.shares[m]) for m in PILLARS}
   129	        object.__setattr__(self, "normalized_shares", norm)
   130	        object.__setattr__(self, "integration", validate_integration_matrix(self.integration))
   131	        object.__setattr__(self, "capture_links", tuple(self.capture_links))
   132	        # Fail early on bad Q or weights.
   133	        unaccountable_concentration(self.H, self.contestability, self.weights)
   134	
   135	    @property
   136	    def H(self) -> dict[Pillar, float]:  # noqa: N802
   137	        return {m: hhi(self.normalized_shares[m]) for m in PILLARS}
   138	
   139	    @property
   140	    def U(self) -> float:  # noqa: N802
   141	        return unaccountable_concentration(self.H, self.contestability, self.weights)
   142	
   143	    @property
   144	    def I(self) -> float:  # noqa: E743, N802
   145	        return integration_statistic(self.integration)
   146	
   147	
   148	@dataclass(frozen=True)
   149	class Assessment:
   150	    name: str
   151	    H: dict[Pillar, float]
   152	    U: float
   153	    I: float  # noqa: E741
   154	    prop_a: PropositionAResult
   155	    prop_b: PropositionBResult
   156	
   157	
   158	def assess(polity: Polity, thresholds: CaptureThresholds = CaptureThresholds()) -> Assessment:
   159	    """Evaluate Proposition A and Proposition B on one polity."""
   160	    return Assessment(
   161	        name=polity.name,
   162	        H=polity.H,
   163	        U=polity.U,
   164	        I=polity.I,
   165	        prop_a=check_proposition_a(polity.system),
   166	        prop_b=proposition_b(polity.U, polity.I, polity.capture_links, thresholds),
   167	    )
   168	
   169	
   170	# Counter-model: A does not imply B --------------------------------------------------------
   171	
   172	
   173	def _layer_from(holders: list[str], actors: list[str], weight: float) -> np.ndarray:
   174	    idx = {a: k for k, a in enumerate(actors)}
   175	    arr = np.zeros((len(actors), len(actors)))
   176	    for h in holders:
   177	        for a in actors:
   178	            if a != h:
   179	                arr[idx[h], idx[a]] = weight
   180	    return arr
   181	
   182	
   183	def plural_polity(n_per_pillar: int = 5, q: float = 0.9) -> Polity:
   184	    """G1, accountable pluralism: each pillar held by n independent organizations.
   185	
   186	    Holders are disjoint across pillars, so every coalition overlap is 0 and C_mn = 0.
   187	    """
   188	    if n_per_pillar < 1:
   189	        raise ValueError("n_per_pillar must be positive")
   190	    holders = {m: [f"{m.label}-org-{k}" for k in range(n_per_pillar)] for m in PILLARS}
   191	    actors = [a for m in PILLARS for a in holders[m]]
   192	    net = MultiplexNetwork(
   193	        actors=tuple(actors),
   194	        layers={m: _layer_from(holders[m], actors, 0.5) for m in PILLARS},
   195	        roles={a: {m} for m in PILLARS for a in holders[m]},
   196	    )
   197	    shares = {m: net.out_strength_shares(m) for m in PILLARS}
   198	    return Polity(
   199	        name="G1 accountable pluralism",
   200	        system=formal_system("G1 accountable pluralism", holders),
   201	        shares=shares,
   202	        contestability={m: q for m in PILLARS},
   203	        integration=coalition_integration(shares),
   204	    )
   205	
   206	
   207	def fused_polity(n_subordinate: int = 5, q: float = 0.05) -> Polity:
   208	    """G2, fused capture: one coalition holds all six pillars, Q near 0, one evidenced link."""
   209	    if n_subordinate < 1:
   210	        raise ValueError("n_subordinate must be positive")
   211	    core = "ruling coalition"
   212	    actors = [core] + [f"subordinate-{k}" for k in range(n_subordinate)]
   213	    net = MultiplexNetwork(
   214	        actors=tuple(actors),
   215	        layers={m: _layer_from([core], actors, 1.0) for m in PILLARS},
   216	        roles={core: set(PILLARS)},
   217	    )
   218	    shares = {m: net.out_strength_shares(m) for m in PILLARS}
   219	    link = CaptureLink(
   220	        source=core, target="subordinate-0", pillar=Pillar.J,
   221	        privileged_access=True, weakens_accountability=True, material_evidence=True,
   222	        evidence="synthetic: appointment record ties removal of reviewing judges to ruling",
   223	    )
   224	    return Polity(
   225	        name="G2 fused capture",
   226	        system=formal_system("G2 fused capture", {m: [core] for m in PILLARS}),
   227	        shares=shares,
   228	        contestability={m: q for m in PILLARS},
   229	        integration=coalition_integration(shares),
   230	        capture_links=(link,),
   231	    )
   232	
   233	
   234	@dataclass(frozen=True)
   235	class CounterModel:
   236	    plural: Assessment
   237	    fused: Assessment
   238	
   239	    @property
   240	    def demonstrates_non_implication(self) -> bool:
   241	        """Both satisfy A; only G2 satisfies B. Hence A does not imply B."""
   242	        return (
   243	            self.plural.prop_a.holds
   244	            and self.fused.prop_a.holds
   245	            and not self.plural.prop_b.holds
   246	            and self.fused.prop_b.holds
   247	        )
   248	
   249	
   250	def a_does_not_imply_b(thresholds: CaptureThresholds = CaptureThresholds()) -> CounterModel:
   251	    """Constructive counter-model for Part VII Theorem 2 (KB Section 4.3 item 4).
   252	
   253	    G1 has U = (1/5)(1 - 0.9) = 0.02 and I = 0; G2 has U = 0.95 and I = 1. Both pass the
   254	    Theorem A check with all six pillars realized; only G2 meets Proposition B.
   255	    """
   256	    return CounterModel(
   257	        plural=assess(plural_polity(), thresholds),
   258	        fused=assess(fused_polity(), thresholds),
   259	    )

exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_indices.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	import numpy as np
     2	import pytest
     3	
     4	from beast_system.indices import (
     5	    coalition_integration,
     6	    control_shares,
     7	    hhi,
     8	    integration_matrix,
     9	    integration_statistic,
    10	    normalized_hhi,
    11	    unaccountable_concentration,
    12	    validate_integration_matrix,
    13	    validate_shares,
    14	    validate_weights,
    15	    weight_sensitivity,
    16	)
    17	from beast_system.pillars import PAIRS, PILLARS, Pillar
    18	
    19	F, P, J, I, C, W = PILLARS
    20	
    21	
    22	def test_control_shares_normalize():
    23	    assert control_shares({"x": 3, "y": 1}) == pytest.approx({"x": 0.75, "y": 0.25})
    24	
    25	
    26	@pytest.mark.parametrize("raw", [{"x": -1, "y": 2}, {"x": 0, "y": 0}, {}, {"x": float("inf")}])
    27	def test_control_shares_reject_bad_input(raw):
    28	    with pytest.raises(ValueError):
    29	        control_shares(raw)
    30	
    31	
    32	def test_validate_shares_requires_sum_one():
    33	    with pytest.raises(ValueError):
    34	        validate_shares([0.5, 0.4])
    35	    validate_shares([0.5, 0.5])
    36	
    37	
    38	def test_hhi_monopoly_is_one():
    39	    assert hhi([1.0]) == 1.0
    40	    assert hhi([1.0, 0.0, 0.0]) == 1.0
    41	
    42	
    43	@pytest.mark.parametrize("n", [1, 2, 5, 37])
    44	def test_hhi_uniform_is_one_over_n(n):
    45	    assert hhi(np.full(n, 1.0 / n)) == pytest.approx(1.0 / n)
    46	
    47	
    48	def test_normalized_hhi_endpoints():
    49	    assert normalized_hhi([0.25] * 4) == pytest.approx(0.0)
    50	    assert normalized_hhi([1.0, 0.0]) == pytest.approx(1.0)
    51	    assert normalized_hhi([1.0]) == 1.0
    52	
    53	
    54	def test_u_bounds_random():
    55	    rng = np.random.default_rng(1)
    56	    for _ in range(200):
    57	        H = {m: float(rng.uniform(0.01, 1.0)) for m in PILLARS}
    58	        Q = {m: float(rng.uniform(0.0, 1.0)) for m in PILLARS}
    59	        w = rng.dirichlet(np.ones(6))
    60	        u = unaccountable_concentration(H, Q, dict(zip(PILLARS, w)))
    61	        assert 0.0 <= u <= 1.0
    62	
    63	
    64	def test_u_extremes():
    65	    ones = {m: 1.0 for m in PILLARS}
    66	    zeros = {m: 0.0 for m in PILLARS}
    67	    assert unaccountable_concentration(ones, zeros) == pytest.approx(1.0)
    68	    assert unaccountable_concentration(ones, ones) == 0.0
    69	    # U = 0 only needs Q_m = 1 where w_m > 0.
    70	    Q = {**zeros, F: 1.0}
    71	    assert unaccountable_concentration(ones, Q, {m: float(m is F) for m in PILLARS}) == 0.0
    72	
    73	
    74	@pytest.mark.parametrize("weights", [
    75	    {m: 1 / 6 for m in PILLARS if m is not W},
    76	    {m: 0.25 for m in PILLARS},
    77	    {**{m: 0.2 for m in PILLARS}, F: -0.2, P: 0.4},
    78	])
    79	def test_u_rejects_invalid_weights(weights):
    80	    with pytest.raises(ValueError):
    81	        validate_weights(weights)
    82	
    83	
    84	def test_u_rejects_bad_h_and_q():
    85	    ok = {m: 0.5 for m in PILLARS}
    86	    with pytest.raises(ValueError):
    87	        unaccountable_concentration({**ok, F: 1.5}, ok)
    88	    with pytest.raises(ValueError):
    89	        unaccountable_concentration(ok, {**ok, C: -0.1})
    90	    with pytest.raises(ValueError):
    91	        unaccountable_concentration({**ok, F: 0.0}, ok)
    92	    with pytest.raises(ValueError):
    93	        unaccountable_concentration({F: 0.5}, ok)
    94	
    95	
    96	def test_integration_statistic_averages_fifteen_pairs():
    97	    assert integration_statistic(np.ones((6, 6))) == pytest.approx(1.0)
    98	    assert integration_statistic(integration_matrix({})) == 0.0
    99	    assert integration_statistic(integration_matrix({(F, P): 0.9})) == pytest.approx(0.9 / 15)
   100	    vals = np.linspace(0, 1, 15)
   101	    C_ = integration_matrix(dict(zip(PAIRS, vals)))
   102	    assert integration_statistic(C_) == pytest.approx(vals.mean())
   103	
   104	
   105	def test_integration_matrix_validation():
   106	    bad = np.eye(6)
   107	    bad[0, 1] = 0.5
   108	    with pytest.raises(ValueError):
   109	        validate_integration_matrix(bad)  # asymmetric
   110	    with pytest.raises(ValueError):
   111	        integration_matrix({(F, P): 1.2})
   112	    with pytest.raises(ValueError):
   113	        integration_matrix({(F, F): 0.5})
   114	    with pytest.raises(ValueError):
   115	        integration_matrix({(F, P): 0.5, (P, F): 0.4})
   116	    with pytest.raises(ValueError):
   117	        validate_integration_matrix(np.eye(5))
   118	
   119	
   120	def test_coalition_integration_fused_and_disjoint():
   121	    fused = {m: {"core": 1.0} for m in PILLARS}
   122	    assert integration_statistic(coalition_integration(fused)) == 1.0
   123	    disjoint = {m: {f"{m.name}{k}": 0.5 for k in range(2)} for m in PILLARS}
   124	    assert integration_statistic(coalition_integration(disjoint)) == 0.0
   125	    # Merging two actors into one coalition raises C_FP to min(s^F(S), s^P(S)).
   126	    shares = dict(disjoint)
   127	    shares[F] = {"a": 0.6, "b": 0.4}
   128	    shares[P] = {"c": 0.3, "d": 0.7}
   129	    Cm = coalition_integration(shares, {"a": "S", "c": "S"})
   130	    assert Cm[F.position, P.position] == pytest.approx(0.3)
   131	
   132	
   133	def test_weight_sensitivity_within_vertex_bounds():
   134	    H = {m: 0.2 + 0.1 * m.position for m in PILLARS}
   135	    Q = {m: 0.5 for m in PILLARS}
   136	    res = weight_sensitivity(H, Q, n_draws=500)
   137	    terms = [H[m] * 0.5 for m in PILLARS]
   138	    assert res.vertex_min == pytest.approx(min(terms))
   139	    assert res.vertex_max == pytest.approx(max(terms))
   140	    assert res.draws.min() >= res.vertex_min - 1e-12
   141	    assert res.draws.max() <= res.vertex_max + 1e-12
   142	    assert res.vertex_min <= res.baseline <= res.vertex_max
   143	    lo, hi = res.quantiles
   144	    assert lo <= hi
   145	    assert res.fraction_at_least(0.0) == 1.0
   146	    assert res.fraction_at_least(1.0) == 0.0

codex
The first pass confirms the project has dedicated representations for all six pillars, the 15-pair integration statistic, capture predicates, proposition checks, dynamics, and illustrative regimes. I’m now checking whether those representations preserve the logical distinctions in your definitions rather than merely producing expected example outputs.
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/indices.py | sed -n '220,360p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   220	    def fraction_at_least(self, u_star: float) -> float:
   221	        """Share of weight draws with U >= u_star (robustness of a threshold call)."""
   222	        validate_unit_interval(u_star, "u_star")
   223	        return float(np.mean(self.draws >= u_star))
   224	
   225	
   226	def weight_sensitivity(
   227	    H: Mapping[Pillar, float],
   228	    Q: Mapping[Pillar, float],
   229	    weights: Mapping[Pillar, float] | None = None,
   230	    n_draws: int = 2000,
   231	    seed: int = 0,
   232	) -> WeightSensitivity:
   233	    """Sensitivity of U to the weights w (source: 'weights preregistered; sensitivity analysis').
   234	
   235	    U is linear in w, so over the whole weight simplex its exact range is
   236	    [min_m H_m (1 - Q_m), max_m H_m (1 - Q_m)] (attained at the vertices). ``draws`` samples
   237	    w uniformly on the simplex (Dirichlet(1, ..., 1)) to show the typical spread.
   238	    """
   239	    if n_draws < 1:
   240	        raise ValueError("n_draws must be positive")
   241	    baseline = unaccountable_concentration(H, Q, weights)
   242	    h = _per_pillar(H, "H")
   243	    q = _per_pillar(Q, "Q")
   244	    terms = np.array([h[m] * (1.0 - q[m]) for m in PILLARS])
   245	    rng = np.random.default_rng(seed)
   246	    w = rng.dirichlet(np.ones(M), size=n_draws)
   247	    return WeightSensitivity(
   248	        baseline=baseline,
   249	        vertex_min=float(terms.min()),
   250	        vertex_max=float(terms.max()),
   251	        draws=(w * terms).sum(axis=1),
   252	    )

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/capture.py | sed -n '1,360p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Capture links, Proposition B, and the non-implication A -/-> B (Part VII Theorem 2).
     2	
     3	Proposition B (notation.md CENTRAL THESIS): the functions become concentrated or coordinated
     4	so that independent accountability fails: U >= u* AND I >= i* AND at least one evidenced
     5	capture link. Proposition A is a statement about the support of the role map; Proposition B
     6	is a threshold on real-valued functionals of (H, Q, C) plus evidence (KB Section 4.3 item 4).
     7	"""
     8	
     9	from __future__ import annotations
    10	
    11	from collections.abc import Mapping
    12	from dataclasses import dataclass, field
    13	
    14	import numpy as np
    15	
    16	from .indices import (
    17	    coalition_integration,
    18	    control_shares,
    19	    hhi,
    20	    integration_statistic,
    21	    unaccountable_concentration,
    22	    validate_integration_matrix,
    23	    validate_unit_interval,
    24	)
    25	from .necessity import GovernanceSystem, PropositionAResult, check_proposition_a, formal_system
    26	from .network import MultiplexNetwork
    27	from .pillars import PILLARS, Pillar
    28	
    29	
    30	@dataclass(frozen=True)
    31	class CaptureLink:
    32	    """Capture link (i -> j, m) (source Section 5; notation.md 'Capture link').
    33	
    34	    All three conditions are required: (i) privileged access or discretion; (ii) the privilege
    35	    weakens otherwise applicable accountability or contestability; (iii) material evidence
    36	    links the asymmetry to an institutional output. A disclosure-compliant donor meeting is
    37	    not automatically capture. Claiming (iii) requires citing the evidence.
    38	    """
    39	
    40	    source: str
    41	    target: str
    42	    pillar: Pillar
    43	    privileged_access: bool
    44	    weakens_accountability: bool
    45	    material_evidence: bool
    46	    evidence: str = ""
    47	
    48	    def __post_init__(self) -> None:
    49	        if not self.source or not self.target:
    50	            raise ValueError("capture link endpoints must be named")
    51	        if not isinstance(self.pillar, Pillar):
    52	            raise TypeError("capture link pillar must be a Pillar")
    53	        if self.material_evidence and not self.evidence.strip():
    54	            raise ValueError("condition (iii) requires a citation of the material evidence")
    55	
    56	    @property
    57	    def holds(self) -> bool:
    58	        return self.privileged_access and self.weakens_accountability and self.material_evidence
    59	
    60	
    61	def is_capture_link(link: CaptureLink) -> bool:
    62	    """Conjunction of the source's three conditions."""
    63	    return link.holds
    64	
    65	
    66	@dataclass(frozen=True)
    67	class CaptureThresholds:
    68	    """Thresholds u*, i* for Proposition B. Illustrative defaults; preregister in applications."""
    69	
    70	    u_star: float = 0.4
    71	    i_star: float = 0.5
    72	
    73	    def __post_init__(self) -> None:
    74	        validate_unit_interval(self.u_star, "u_star")
    75	        validate_unit_interval(self.i_star, "i_star")
    76	
    77	
    78	@dataclass(frozen=True)
    79	class PropositionBResult:
    80	    u_high: bool
    81	    i_high: bool
    82	    n_links: int
    83	
    84	    @property
    85	    def thresholds_met(self) -> bool:
    86	        return self.u_high and self.i_high
    87	
    88	    @property
    89	    def holds(self) -> bool:
    90	        return self.thresholds_met and self.n_links > 0
    91	
    92	
    93	def proposition_b(
    94	    U: float,
    95	    I: float,  # noqa: E741  (integration statistic, math cal I)
    96	    links: tuple[CaptureLink, ...] | list[CaptureLink],
    97	    thresholds: CaptureThresholds = CaptureThresholds(),
    98	) -> PropositionBResult:
    99	    """Proposition B: U >= u* AND I >= i* AND some capture link holds."""
   100	    U = validate_unit_interval(U, "U")
   101	    I = validate_unit_interval(I, "I")  # noqa: E741
   102	    return PropositionBResult(
   103	        u_high=U >= thresholds.u_star,
   104	        i_high=I >= thresholds.i_star,
   105	        n_links=sum(1 for link in links if is_capture_link(link)),
   106	    )
   107	
   108	
   109	@dataclass(frozen=True)
   110	class Polity:
   111	    """A coded polity: governance system (for A) plus index inputs (for B).
   112	
   113	    ``shares[m]`` holds raw non-negative control weights per actor, normalized to s^m.
   114	    """
   115	
   116	    name: str
   117	    system: GovernanceSystem
   118	    shares: Mapping[Pillar, Mapping[str, float]]
   119	    contestability: Mapping[Pillar, float]
   120	    integration: np.ndarray
   121	    capture_links: tuple[CaptureLink, ...] = ()
   122	    weights: Mapping[Pillar, float] | None = None
   123	    normalized_shares: Mapping[Pillar, Mapping[str, float]] = field(init=False, repr=False)
   124	
   125	    def __post_init__(self) -> None:
   126	        if set(self.shares) != set(PILLARS):
   127	            raise ValueError("shares must cover every pillar")
   128	        norm = {m: control_shares(self.shares[m]) for m in PILLARS}
   129	        object.__setattr__(self, "normalized_shares", norm)
   130	        object.__setattr__(self, "integration", validate_integration_matrix(self.integration))
   131	        object.__setattr__(self, "capture_links", tuple(self.capture_links))
   132	        # Fail early on bad Q or weights.
   133	        unaccountable_concentration(self.H, self.contestability, self.weights)
   134	
   135	    @property
   136	    def H(self) -> dict[Pillar, float]:  # noqa: N802
   137	        return {m: hhi(self.normalized_shares[m]) for m in PILLARS}
   138	
   139	    @property
   140	    def U(self) -> float:  # noqa: N802
   141	        return unaccountable_concentration(self.H, self.contestability, self.weights)
   142	
   143	    @property
   144	    def I(self) -> float:  # noqa: E743, N802
   145	        return integration_statistic(self.integration)
   146	
   147	
   148	@dataclass(frozen=True)
   149	class Assessment:
   150	    name: str
   151	    H: dict[Pillar, float]
   152	    U: float
   153	    I: float  # noqa: E741
   154	    prop_a: PropositionAResult
   155	    prop_b: PropositionBResult
   156	
   157	
   158	def assess(polity: Polity, thresholds: CaptureThresholds = CaptureThresholds()) -> Assessment:
   159	    """Evaluate Proposition A and Proposition B on one polity."""
   160	    return Assessment(
   161	        name=polity.name,
   162	        H=polity.H,
   163	        U=polity.U,
   164	        I=polity.I,
   165	        prop_a=check_proposition_a(polity.system),
   166	        prop_b=proposition_b(polity.U, polity.I, polity.capture_links, thresholds),
   167	    )
   168	
   169	
   170	# Counter-model: A does not imply B --------------------------------------------------------
   171	
   172	
   173	def _layer_from(holders: list[str], actors: list[str], weight: float) -> np.ndarray:
   174	    idx = {a: k for k, a in enumerate(actors)}
   175	    arr = np.zeros((len(actors), len(actors)))
   176	    for h in holders:
   177	        for a in actors:
   178	            if a != h:
   179	                arr[idx[h], idx[a]] = weight
   180	    return arr
   181	
   182	
   183	def plural_polity(n_per_pillar: int = 5, q: float = 0.9) -> Polity:
   184	    """G1, accountable pluralism: each pillar held by n independent organizations.
   185	
   186	    Holders are disjoint across pillars, so every coalition overlap is 0 and C_mn = 0.
   187	    """
   188	    if n_per_pillar < 1:
   189	        raise ValueError("n_per_pillar must be positive")
   190	    holders = {m: [f"{m.label}-org-{k}" for k in range(n_per_pillar)] for m in PILLARS}
   191	    actors = [a for m in PILLARS for a in holders[m]]
   192	    net = MultiplexNetwork(
   193	        actors=tuple(actors),
   194	        layers={m: _layer_from(holders[m], actors, 0.5) for m in PILLARS},
   195	        roles={a: {m} for m in PILLARS for a in holders[m]},
   196	    )
   197	    shares = {m: net.out_strength_shares(m) for m in PILLARS}
   198	    return Polity(
   199	        name="G1 accountable pluralism",
   200	        system=formal_system("G1 accountable pluralism", holders),
   201	        shares=shares,
   202	        contestability={m: q for m in PILLARS},
   203	        integration=coalition_integration(shares),
   204	    )
   205	
   206	
   207	def fused_polity(n_subordinate: int = 5, q: float = 0.05) -> Polity:
   208	    """G2, fused capture: one coalition holds all six pillars, Q near 0, one evidenced link."""
   209	    if n_subordinate < 1:
   210	        raise ValueError("n_subordinate must be positive")
   211	    core = "ruling coalition"
   212	    actors = [core] + [f"subordinate-{k}" for k in range(n_subordinate)]
   213	    net = MultiplexNetwork(
   214	        actors=tuple(actors),
   215	        layers={m: _layer_from([core], actors, 1.0) for m in PILLARS},
   216	        roles={core: set(PILLARS)},
   217	    )
   218	    shares = {m: net.out_strength_shares(m) for m in PILLARS}
   219	    link = CaptureLink(
   220	        source=core, target="subordinate-0", pillar=Pillar.J,
   221	        privileged_access=True, weakens_accountability=True, material_evidence=True,
   222	        evidence="synthetic: appointment record ties removal of reviewing judges to ruling",
   223	    )
   224	    return Polity(
   225	        name="G2 fused capture",
   226	        system=formal_system("G2 fused capture", {m: [core] for m in PILLARS}),
   227	        shares=shares,
   228	        contestability={m: q for m in PILLARS},
   229	        integration=coalition_integration(shares),
   230	        capture_links=(link,),
   231	    )
   232	
   233	
   234	@dataclass(frozen=True)
   235	class CounterModel:
   236	    plural: Assessment
   237	    fused: Assessment
   238	
   239	    @property
   240	    def demonstrates_non_implication(self) -> bool:
   241	        """Both satisfy A; only G2 satisfies B. Hence A does not imply B."""
   242	        return (
   243	            self.plural.prop_a.holds
   244	            and self.fused.prop_a.holds
   245	            and not self.plural.prop_b.holds
   246	            and self.fused.prop_b.holds
   247	        )
   248	
   249	
   250	def a_does_not_imply_b(thresholds: CaptureThresholds = CaptureThresholds()) -> CounterModel:
   251	    """Constructive counter-model for Part VII Theorem 2 (KB Section 4.3 item 4).
   252	
   253	    G1 has U = (1/5)(1 - 0.9) = 0.02 and I = 0; G2 has U = 0.95 and I = 1. Both pass the
   254	    Theorem A check with all six pillars realized; only G2 meets Proposition B.
   255	    """
   256	    return CounterModel(
   257	        plural=assess(plural_polity(), thresholds),
   258	        fused=assess(fused_polity(), thresholds),
   259	    )

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '1,420p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Structural necessity: Proposition A and the pillar dependency graph (Part VII Theorem A).
     2	
     3	Theorem A (notation.md CENTRAL THESIS; KB Section 4): if a governance system G persists and
     4	satisfies Ax1..Ax6, then every pillar in M is implemented in G, and the pillars stand in the
     5	dependency relations D. Implementation is role-level, not institution-level (Hempel 1959): a
     6	function may be held by a formal institution, fused with other functions inside one
     7	institution, or exercised informally (gossip and shunning as C, mediators as J).
     8	
     9	What this module does and does not do. It cannot prove Theorem A. It encodes the lemma schema
    10	'Ax_k + persistence => some practice solves problem_k' and checks it against coded cases. The
    11	role map is DERIVED from independently coded practices, never declared, so a persistent case
    12	that satisfies all six axioms yet has no practice for some problem is reported as a
    13	counterexample (the falsifier required by KB Section 4.4), not silently accepted.
    14	
    15	Dependency edges are written provider -> dependent ('dependent needs provider'). Each edge
    16	carries its axiom basis and a status: 'derived' (argued from the axioms for every persistent
    17	G) or 'conditional' (holds only under an extra assumption, e.g. specialized office holders).
    18	Strong connectivity of D is flagged in KB Section 4.3 as an OPEN problem; it is tested here on
    19	the encoded graph, which is a property of the encoding, not a proof that it is forced.
    20	"""
    21	
    22	from __future__ import annotations
    23	
    24	from collections.abc import Iterable, Mapping
    25	from dataclasses import dataclass, field
    26	from typing import Literal
    27	
    28	from .pillars import AXIOM_TO_PILLAR, PILLAR_TO_AXIOM, PILLARS, Axiom, Pillar
    29	
    30	RealizedForm = Literal["formal institution", "fused", "informal/minimal"]
    31	FORMAL: RealizedForm = "formal institution"
    32	FUSED: RealizedForm = "fused"
    33	INFORMAL: RealizedForm = "informal/minimal"
    34	
    35	
    36	@dataclass(frozen=True)
    37	class Practice:
    38	    """A regular activity that discharges the problem generated by axiom ``solves``.
    39	
    40	    ``formal`` is True when the activity is attached to a designated office or organization.
    41	    ``source`` holds the citation key(s) supporting the coding.
    42	    """
    43	
    44	    description: str
    45	    solves: Axiom
    46	    holders: frozenset[str]
    47	    formal: bool = False
    48	    source: str = ""
    49	
    50	    def __post_init__(self) -> None:
    51	        if not isinstance(self.solves, Axiom):
    52	            raise TypeError("Practice.solves must be an Axiom")
    53	        holders = frozenset(self.holders)
    54	        if not holders or any(not isinstance(h, str) or not h for h in holders):
    55	            raise ValueError("a practice needs at least one named holder")
    56	        if not self.description.strip():
    57	            raise ValueError("a practice needs a description")
    58	        object.__setattr__(self, "holders", holders)
    59	
    60	    @property
    61	    def pillar(self) -> Pillar:
    62	        return AXIOM_TO_PILLAR[self.solves]
    63	
    64	
    65	@dataclass(frozen=True)
    66	class GovernanceSystem:
    67	    """A collective that makes and enforces collective decisions (KB Section 4.1).
    68	
    69	    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
    70	    over the period studied. Both are coded independently of ``practices``.
    71	    """
    72	
    73	    name: str
    74	    persistent: bool
    75	    axioms: frozenset[Axiom]
    76	    practices: tuple[Practice, ...] = ()
    77	    note: str = ""
    78	
    79	    def __post_init__(self) -> None:
    80	        axioms = frozenset(self.axioms)
    81	        if any(not isinstance(a, Axiom) for a in axioms):
    82	            raise TypeError("axioms must be Axiom members")
    83	        practices = tuple(self.practices)
    84	        if any(not isinstance(p, Practice) for p in practices):
    85	            raise TypeError("practices must be Practice instances")
    86	        object.__setattr__(self, "axioms", axioms)
    87	        object.__setattr__(self, "practices", practices)
    88	
    89	    def holds(self, axiom: Axiom) -> bool:
    90	        """Predicate for one axiom (Ax1 scarcity, ..., Ax6 maintenance)."""
    91	        return axiom in self.axioms
    92	
    93	    @property
    94	    def all_axioms_hold(self) -> bool:
    95	        return all(self.holds(a) for a in Axiom)
    96	
    97	
    98	def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
    99	    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
   100	    roles: dict[str, set[Pillar]] = {}
   101	    for p in system.practices:
   102	        for h in p.holders:
   103	            roles.setdefault(h, set()).add(p.pillar)
   104	    return {h: frozenset(ps) for h, ps in roles.items()}
   105	
   106	
   107	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   108	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   109	
   110	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   111	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   112	    """
   113	    practices = [p for p in system.practices if p.pillar is pillar]
   114	    if not practices:
   115	        return None
   116	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   117	    if not formal_holders:
   118	        return INFORMAL
   119	    formal_roles: dict[str, set[Pillar]] = {}
   120	    for p in system.practices:
   121	        if p.formal:
   122	            for h in p.holders:
   123	                formal_roles.setdefault(h, set()).add(p.pillar)
   124	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   125	        return FUSED
   126	    return FORMAL
   127	
   128	
   129	@dataclass(frozen=True)
   130	class Derivation:
   131	    """Result of the lemma for one axiom: required pillar and its realized form."""
   132	
   133	    axiom: Axiom
   134	    pillar: Pillar
   135	    form: RealizedForm | None
   136	    practices: tuple[Practice, ...]
   137	
   138	    @property
   139	    def realized(self) -> bool:
   140	        return self.form is not None
   141	
   142	
   143	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   144	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   145	
   146	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   147	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   148	    """
   149	    out: dict[Axiom, Derivation] = {}
   150	    for axiom in Axiom:
   151	        if not system.holds(axiom):
   152	            continue
   153	        pillar = AXIOM_TO_PILLAR[axiom]
   154	        out[axiom] = Derivation(
   155	            axiom=axiom,
   156	            pillar=pillar,
   157	            form=realized_form(system, pillar),
   158	            practices=tuple(p for p in system.practices if p.solves is axiom),
   159	        )
   160	    return out
   161	
   162	
   163	# Dependency graph -------------------------------------------------------------------------
   164	
   165	DependencyStatus = Literal["derived", "conditional"]
   166	Graph = Mapping[Pillar, Iterable[Pillar]]
   167	
   168	
   169	@dataclass(frozen=True)
   170	class Dependency:
   171	    """Edge provider -> dependent: the dependent pillar needs an output of the provider."""
   172	
   173	    provider: Pillar
   174	    dependent: Pillar
   175	    basis: tuple[Axiom, ...]
   176	    status: DependencyStatus
   177	    rationale: str
   178	
   179	
   180	_A = Axiom
   181	_P = Pillar
   182	
   183	#: Encoded dependency relations D (KB Sections 4.3 item 3 and VII.2). The first six entries are
   184	#: the relations listed in the Part VII brief; the remainder come from the KB list.
   185	DEPENDENCIES: tuple[Dependency, ...] = (
   186	    Dependency(_P.W, _P.C, (_A.Ax6, _A.Ax5), "derived",
   187	               "C needs W's resources: sanctioning consumes time and goods someone produces"),
   188	    Dependency(_P.P, _P.J, (_A.Ax2, _A.Ax3), "derived",
   189	               "J needs P's rules: interpretation presupposes rules to interpret"),
   190	    Dependency(_P.I, _P.P, (_A.Ax4, _A.Ax2), "derived",
   191	               "P needs I's legitimacy: rule-making needs a recognized rule of recognition (Hart)"),
   192	    Dependency(_P.J, _P.F, (_A.Ax3, _A.Ax1), "derived",
   193	               "F needs J's enforcement of claims: contested claims on resources need case rulings"),
   194	    Dependency(_P.F, _P.W, (_A.Ax1, _A.Ax6), "derived",
   195	               "W needs F's allocation: producers need allocated inputs and shares"),
   196	    Dependency(_P.W, _P.I, (_A.Ax6, _A.Ax4), "derived",
   197	               "I needs W's surplus: belief maintenance consumes produced resources"),
   198	    Dependency(_P.W, _P.F, (_A.Ax6, _A.Ax1), "derived",
   199	               "production creates the stock that allocation divides"),
   200	    Dependency(_P.C, _P.F, (_A.Ax5, _A.Ax1), "derived",
   201	               "allocation rules are sometimes defected from; sanctions back them"),
   202	    Dependency(_P.C, _P.J, (_A.Ax5, _A.Ax3), "derived",
   203	               "adjudication without enforcement is advice"),
   204	    Dependency(_P.I, _P.J, (_A.Ax4, _A.Ax3), "derived",
   205	               "rulings settle disputes only if recognized as authoritative"),
   206	    Dependency(_P.I, _P.C, (_A.Ax4, _A.Ax5), "derived",
   207	               "a sanction must be recognized as sanction rather than aggression"),
   208	    Dependency(_P.I, _P.W, (_A.Ax4, _A.Ax6), "derived",
   209	               "norms of work and quasi-voluntary compliance (Levi)"),
   210	    Dependency(_P.F, _P.C, (_A.Ax1, _A.Ax5), "conditional",
   211	               "specialized sanction capacity needs provisioning (Tilly, Levi); gossip does not"),
   212	    Dependency(_P.J, _P.P, (_A.Ax3, _A.Ax2), "conditional",
   213	               "precedent feeds rule change; only where rules change through interpretation"),
   214	    Dependency(_P.J, _P.I, (_A.Ax3, _A.Ax4), "conditional",
   215	               "reasoned judgments act as public symbols; needs public adjudication"),
   216	    Dependency(_P.F, _P.I, (_A.Ax1, _A.Ax4), "conditional",
   217	               "funding of ideology producers; needs specialist belief producers"),
   218	    Dependency(_P.P, _P.I, (_A.Ax2, _A.Ax4), "conditional",
   219	               "legislation as a public symbolic act; needs declared rules"),
   220	)
   221	
   222	#: The six relations named in the Part VII brief, on their own.
   223	BRIEF_DEPENDENCIES: tuple[Dependency, ...] = DEPENDENCIES[:6]
   224	
   225	
   226	def dependency_graph(
   227	    include_conditional: bool = True,
   228	    dependencies: Iterable[Dependency] = DEPENDENCIES,
   229	) -> dict[Pillar, frozenset[Pillar]]:
   230	    """Adjacency provider -> set of dependents over all six pillars."""
   231	    adj: dict[Pillar, set[Pillar]] = {m: set() for m in PILLARS}
   232	    for d in dependencies:
   233	        if include_conditional or d.status == "derived":
   234	            adj[d.provider].add(d.dependent)
   235	    return {m: frozenset(v) for m, v in adj.items()}
   236	
   237	
   238	def _nodes(graph: Graph) -> set[Pillar]:
   239	    nodes = set(graph)
   240	    for targets in graph.values():
   241	        nodes.update(targets)
   242	    return nodes
   243	
   244	
   245	def _reach(graph: Mapping[Pillar, frozenset[Pillar]], start: Pillar) -> set[Pillar]:
   246	    seen = {start}
   247	    stack = [start]
   248	    while stack:
   249	        for nxt in graph.get(stack.pop(), frozenset()):
   250	            if nxt not in seen:
   251	                seen.add(nxt)
   252	                stack.append(nxt)
   253	    return seen
   254	
   255	
   256	def is_strongly_connected(graph: Graph, nodes: Iterable[Pillar] | None = None) -> bool:
   257	    """True iff every node of the graph is reachable from every other node.
   258	
   259	    ``nodes`` restricts the graph to an induced subgraph (default: all nodes that appear).
   260	    The empty graph is not strongly connected; a single node is.
   261	    """
   262	    keep = set(nodes) if nodes is not None else _nodes(graph)
   263	    if not keep:
   264	        return False
   265	    fwd: dict[Pillar, frozenset[Pillar]] = {
   266	        u: frozenset(v for v in graph.get(u, ()) if v in keep) for u in keep
   267	    }
   268	    rev: dict[Pillar, set[Pillar]] = {u: set() for u in keep}
   269	    for u, vs in fwd.items():
   270	        for v in vs:
   271	            rev[v].add(u)
   272	    start = next(iter(keep))
   273	    rev_f = {u: frozenset(v) for u, v in rev.items()}
   274	    return _reach(fwd, start) == keep and _reach(rev_f, start) == keep
   275	
   276	
   277	def critical_edges(graph: Graph) -> list[tuple[Pillar, Pillar]]:
   278	    """Edges whose single removal breaks strong connectivity (empty if not connected)."""
   279	    nodes = _nodes(graph)
   280	    base = {u: frozenset(graph.get(u, ())) for u in nodes}
   281	    if not is_strongly_connected(base):
   282	        return []
   283	    out = []
   284	    for u in PILLARS:
   285	        for v in sorted(base.get(u, ()), key=lambda p: p.position):
   286	            pruned = dict(base)
   287	            pruned[u] = base[u] - {v}
   288	            if not is_strongly_connected(pruned, nodes):
   289	                out.append((u, v))
   290	    return out
   291	
   292	
   293	def sinks_and_sources(graph: Graph) -> tuple[frozenset[Pillar], frozenset[Pillar]]:
   294	    """Pillars with no outgoing edge (sinks) and with no incoming edge (sources)."""
   295	    nodes = _nodes(graph)
   296	    has_out = {u for u in nodes if any(True for _ in graph.get(u, ()))}
   297	    has_in = {v for u in nodes for v in graph.get(u, ())}
   298	    return frozenset(nodes - has_out), frozenset(nodes - has_in)
   299	
   300	
   301	# Proposition A ----------------------------------------------------------------------------
   302	
   303	
   304	@dataclass(frozen=True)
   305	class PropositionAResult:
   306	    """Outcome of checking Theorem A on one coded system.
   307	
   308	    ``holds`` is the structural predicate Struct(G): all six pillars realized and the derived
   309	    dependency graph strongly connected on them. ``counterexample`` is True when the theorem's
   310	    antecedent holds (persistent, Ax1..Ax6) but Struct(G) fails: a falsifier of Theorem A.
   311	    """
   312	
   313	    system: str
   314	    antecedent: bool
   315	    realized: frozenset[Pillar]
   316	    missing: frozenset[Pillar]
   317	    dependencies_connected: bool
   318	    holds: bool
   319	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   320	
   321	    @property
   322	    def counterexample(self) -> bool:
   323	        return self.antecedent and not self.holds
   324	
   325	
   326	def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
   327	    """Check Theorem A on ``system`` (Part VII Theorem A; KB Section 4.3)."""
   328	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   329	    connected = is_strongly_connected(dependency_graph(include_conditional=False), realized)
   330	    return PropositionAResult(
   331	        system=system.name,
   332	        antecedent=system.persistent and system.all_axioms_hold,
   333	        realized=realized,
   334	        missing=frozenset(PILLARS) - realized,
   335	        dependencies_connected=connected,
   336	        holds=realized == frozenset(PILLARS) and connected,
   337	        derivations=derive_functions(system),
   338	    )
   339	
   340	
   341	def formal_system(
   342	    name: str,
   343	    holders: Mapping[Pillar, Iterable[str]],
   344	    persistent: bool = True,
   345	    source: str = "",
   346	) -> GovernanceSystem:
   347	    """A persistent system satisfying Ax1..Ax6 whose pillars are held by formal organizations.
   348	
   349	    An actor listed under several pillars is fused. Used for regime profiles and counter-models.
   350	    """
   351	    practices = tuple(
   352	        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
   353	                 frozenset(hs), formal=True, source=source)
   354	        for m, hs in holders.items()
   355	        if hs
   356	    )
   357	    return GovernanceSystem(name, persistent, frozenset(Axiom), practices)
   358	
   359	
   360	# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
   361	
   362	
   363	def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
   364	    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)
   365	
   366	
   367	NUER = GovernanceSystem(
   368	    name="Nuer ('ordered anarchy')",
   369	    persistent=True,
   370	    axioms=frozenset(Axiom),
   371	    practices=(
   372	        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
   373	                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
   374	        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
   375	                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
   376	        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
   377	                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
   378	        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
   379	                  {"prophets", "lineages"}, "evanspritchard1940"),
   380	        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
   381	                  {"agnatic kin"}, "evanspritchard1940"),
   382	        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
   383	                  "evanspritchard1940"),
   384	    ),
   385	    note="no office holds coercive authority; functions exist without separation",
   386	)
   387	
   388	JU_HOANSI = GovernanceSystem(
   389	    name="Ju/'hoansi (!Kung)",
   390	    persistent=True,
   391	    axioms=frozenset(Axiom),
   392	    practices=(
   393	        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
   394	                  {"hunters", "camp members"}, "lee2013; marshall1976"),
   395	        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
   396	                  {"camp members"}, "lee2013"),
   397	        _informal("disputes talked out with kin mediators", Axiom.Ax3,
   398	                  {"kin mediators"}, "lee1979; wiessner2005"),
   399	        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
   400	                  {"healers", "camp members"}, "marshall1976"),
   401	        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
   402	                  {"camp members"}, "wiessner2005; lee2013"),
   403	        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
   404	    ),
   405	    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
   406	)
   407	
   408	OSTROM_COMMONS = GovernanceSystem(
   409	    name="Ostrom commons (design principles)",
   410	    persistent=True,
   411	    axioms=frozenset(Axiom),
   412	    practices=(
   413	        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
   414	                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
   415	        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
   416	                  {"appropriators"}, "ostrom1990"),
   417	        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
   418	                  {"appropriators"}, "ostrom1990; cox2010"),
   419	        _informal("shared norms; minimal recognition of rights to organize (DP7)",
   420	                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/regimes.py | sed -n '1,420p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Stylized regime profiles for the six regime types (notation.md 'The six regime types').
     2	
     3	ILLUSTRATIVE ASSUMPTIONS, NOT MEASUREMENTS. Every share, contestability value Q_m and
     4	integration value C_mn below is a stylized assumption chosen to show how the universal
     5	six-pillar structure (Proposition A) can be DISTRIBUTED differently. None is an estimate for
     6	any country or period, and none should be cited as data.
     7	
     8	Every profile satisfies Proposition A by construction of its coded practices. No profile
     9	carries a capture link, because a capture link requires cited material evidence (source
    10	Section 5); hence no profile satisfies Proposition B, whatever its U and I. Variants within
    11	the Islamic and Catholic types differ in their checks, so no value attaches capture to a
    12	religion as such (guardrail 1).
    13	"""
    14	
    15	from __future__ import annotations
    16	
    17	from collections.abc import Mapping
    18	from dataclasses import dataclass
    19	
    20	from .capture import Polity
    21	from .indices import integration_matrix
    22	from .necessity import formal_system
    23	from .pillars import PAIRS, Pillar
    24	
    25	ILLUSTRATIVE = True
    26	DISCLAIMER = "Illustrative assumption, not a measurement."
    27	
    28	F, P, J, I, C, W = Pillar.F, Pillar.P, Pillar.J, Pillar.I, Pillar.C, Pillar.W  # noqa: E741
    29	
    30	
    31	@dataclass(frozen=True)
    32	class RegimeProfile:
    33	    """One stylized profile. ``polity`` holds the illustrative inputs; ``rationale`` the story."""
    34	
    35	    regime_type: str
    36	    variant: str
    37	    polity: Polity
    38	    rationale: str
    39	    illustrative: bool = ILLUSTRATIVE
    40	
    41	    @property
    42	    def label(self) -> str:
    43	        return f"{self.regime_type} ({self.variant})" if self.variant else self.regime_type
    44	
    45	
    46	def _profile(
    47	    regime_type: str,
    48	    variant: str,
    49	    shares: Mapping[Pillar, Mapping[str, float]],
    50	    q: tuple[float, float, float, float, float, float],
    51	    c_pairs: Mapping[tuple[Pillar, Pillar], float],
    52	    c_default: float,
    53	    rationale: str,
    54	) -> RegimeProfile:
    55	    name = f"{regime_type} ({variant})" if variant else regime_type
    56	    holders = {m: [a for a, v in s.items() if v > 0] for m, s in shares.items()}
    57	    polity = Polity(
    58	        name=name,
    59	        system=formal_system(name, holders, source=DISCLAIMER),
    60	        shares=shares,
    61	        contestability=dict(zip((F, P, J, I, C, W), q)),
    62	        integration=integration_matrix(c_pairs, default=c_default),
    63	    )
    64	    return RegimeProfile(regime_type, variant, polity, f"{rationale} {DISCLAIMER}")
    65	
    66	
    67	def _pairs_among(pillars: tuple[Pillar, ...], value: float) -> dict[tuple[Pillar, Pillar], float]:
    68	    return {(m, n): value for m, n in PAIRS if m in pillars and n in pillars}
    69	
    70	
    71	def regime_profiles() -> tuple[RegimeProfile, ...]:
    72	    """The stylized profiles, two variants each for the Islamic and Catholic types."""
    73	    return (
    74	        _profile(
    75	            "Market capitalism", "",
    76	            {F: {"Financial firms": 4, "Non-financial firms": 3, "State budget": 2, "Households": 1},
    77	             P: {"Legislature": 4, "Executive": 4, "Organized interests": 2},
    78	             J: {"Courts": 7, "Private arbitration": 2, "Regulators": 1},
    79	             I: {"Media firms": 3, "Platforms": 3, "Universities": 2, "Religious bodies": 2},
    80	             C: {"Police": 5, "Military": 3, "Private security": 2},
    81	             W: {"Wage workers": 5, "Non-financial firms": 3, "Households": 2}},
    82	            (0.45, 0.60, 0.70, 0.55, 0.55, 0.40),
    83	            {(F, P): 0.50, (F, I): 0.45, (F, J): 0.35, (F, W): 0.50, (P, J): 0.30,
    84	             (P, I): 0.30, (P, C): 0.30, (P, W): 0.30},
    85	            0.20,
    86	            "Wealth-to-rules pathway (source Prop 3): C_FP, C_FI, C_FW elevated.",
    87	        ),
    88	        _profile(
    89	            "Communist party-state", "",
    90	            {F: {"Party": 6, "SOE management": 3, "Households": 1},
    91	             P: {"Party": 9, "People's congress": 1},
    92	             J: {"Party": 6, "Courts": 4},
    93	             I: {"Party": 7, "Universities": 2, "Religious bodies": 1},
    94	             C: {"Party": 6, "Security services": 4},
    95	             W: {"Workers": 6, "SOE management": 3, "Households": 1}},
    96	            (0.20, 0.10, 0.15, 0.15, 0.10, 0.25),
    97	            _pairs_among((F, P, J, I, C), 0.80),
    98	            0.45,
    99	            "Appointments-to-resources pathway (nomenklatura): party-centred pairs high.",
   100	        ),
   101	        _profile(
   102	            "Democratic socialism", "",
   103	            {F: {"State budget": 3, "Firms": 3, "Public pension funds": 2, "Cooperatives": 1,
   104	                 "Households": 1},
   105	             P: {"Parliament": 5, "Government": 3, "Social partners": 2},
   106	             J: {"Courts": 8, "Ombudsman": 2},
   107	             I: {"Public broadcaster": 3, "Private media": 3, "Universities": 2,
   108	                 "Churches and civil society": 2},
   109	             C: {"Police": 6, "Military": 4},
   110	             W: {"Unions": 4, "Firms": 3, "Workers": 3}},
   111	            (0.65, 0.75, 0.80, 0.70, 0.70, 0.70),
   112	            {(P, W): 0.45, (F, W): 0.40, (F, P): 0.35},
   113	            0.15,
   114	            "Corporatist bargaining couples P, F and W; high Q offsets concentration.",
   115	        ),
   116	        _profile(
   117	            "Islamic state", "plural juristic authority",
   118	            {F: {"Ruler's treasury": 4, "Waqf endowments": 3, "Merchants": 3},
   119	             P: {"Ruler": 5, "Jurists (plural schools)": 3, "Notables council": 2},
   120	             J: {"Qadi courts": 5, "Jurists (plural schools)": 3, "Ruler's grievance court": 2},
   121	             I: {"Jurists (plural schools)": 5, "Sufi orders": 3, "Ruler": 2},
   122	             C: {"Ruler's army": 6, "Local militias": 2, "Market inspectors": 2},
   123	             W: {"Peasants": 5, "Artisan guilds": 3, "Merchants": 2}},
   124	            (0.45, 0.35, 0.55, 0.50, 0.30, 0.40),
   125	            {(P, C): 0.55, (F, P): 0.45, (J, I): 0.45, (F, C): 0.40, (P, I): 0.35,
   126	             (P, J): 0.35},
   127	            0.20,
   128	            "Juristic class trained and endowed apart from the ruler checks P via J and I.",
   129	        ),
   130	        _profile(
   131	            "Islamic state", "centralized clerical-political authority",
   132	            {F: {"Clerical-political center": 5, "State budget": 3, "Merchants": 2},
   133	             P: {"Clerical-political center": 5, "Vetting council": 3, "Elected assembly": 2},
   134	             J: {"Clerical-political center": 5, "State courts": 5},
   135	             I: {"Clerical-political center": 6, "Seminaries": 3, "Media": 1},
   136	             C: {"Clerical-political center": 6, "Regular army": 4},
   137	             W: {"Workers": 5, "Center-linked enterprises": 3, "Merchants": 2}},
   138	            (0.25, 0.25, 0.20, 0.20, 0.15, 0.30),
   139	            _pairs_among((F, P, J, I, C), 0.70),
   140	            0.40,
   141	            "One center commands appointments across P, J, I, C; elected assembly is checked.",
   142	        ),
   143	        _profile(
   144	            "Catholic monarchy", "estates and Church-crown rivalry",
   145	            {F: {"Crown treasury": 4, "Church benefices": 3, "Bankers": 2, "Nobility": 1},
   146	             P: {"Crown": 5, "Estates assembly": 3, "Nobility": 2},
   147	             J: {"Royal courts": 4, "Parlements": 3, "Church courts": 3},
   148	             I: {"Church": 6, "Universities": 2, "Crown": 2},
   149	             C: {"Crown army": 5, "Nobility": 3, "Town militias": 2},
   150	             W: {"Peasants": 6, "Guilds": 3, "Merchants": 1}},
   151	            (0.40, 0.40, 0.45, 0.35, 0.30, 0.30),
   152	            {(F, P): 0.45, (P, I): 0.40, (P, J): 0.40, (F, C): 0.40},
   153	            0.20,
   154	            "Estates, parlements and an autonomous Church contest the crown.",
   155	        ),
   156	        _profile(
   157	            "Catholic monarchy", "absolutist with venal offices",
   158	            {F: {"Crown": 6, "Tax farmers": 3, "Church benefices": 1},
   159	             P: {"Crown": 9, "Royal council": 1},
   160	             J: {"Crown": 5, "Venal office holders": 4, "Church courts": 1},
   161	             I: {"Church hierarchy": 6, "Crown": 3, "Universities": 1},
   162	             C: {"Crown": 8, "Nobility": 2},
   163	             W: {"Peasants": 6, "Guilds": 3, "Tax farmers": 1}},
   164	            (0.20, 0.10, 0.25, 0.20, 0.15, 0.20),
   165	            {**_pairs_among((F, P, J, C), 0.75), (P, I): 0.70},
   166	            0.40,
   167	            "Crown fuses F, P, J, C; venality couples F and J; Church aligned with crown.",
   168	        ),
   169	        _profile(
   170	            "Secular democracy", "",
   171	            {F: {"Central bank": 2, "Firms": 3, "State budget": 3, "Households": 2},
   172	             P: {"Legislature": 4, "Executive": 3, "Subnational governments": 3},
   173	             J: {"Constitutional court": 3, "Ordinary courts": 6, "Administrative tribunals": 1},
   174	             I: {"Public media": 2, "Private media": 3, "Universities": 2, "Religious bodies": 1,
   175	                 "Civil society": 2},
   176	             C: {"Police": 5, "Military": 3, "Oversight bodies": 2},
   177	             W: {"Workers": 5, "Firms": 3, "Unions": 2}},
   178	            (0.60, 0.75, 0.80, 0.70, 0.65, 0.55),
   179	            {(F, P): 0.30},
   180	            0.15,
   181	            "Authority distributed among elected officials, courts and private bodies.",
   182	        ),
   183	    )

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/__init__.py | sed -n '1,300p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Reference implementation of the six-pillar model (Part VII, The Formalized State).
     2	
     3	Source objects follow team/notation.md and Largo (2026) [largo2026hbs]; Proposition A
     4	(structural necessity) and Proposition B (contingent capture) follow the CENTRAL THESIS.
     5	"""
     6	
     7	from .capture import (
     8	    CaptureLink,
     9	    CaptureThresholds,
    10	    Polity,
    11	    a_does_not_imply_b,
    12	    assess,
    13	    is_capture_link,
    14	    proposition_b,
    15	)
    16	from .dynamics import negative_feedback_example, simulate, spectral_radius
    17	from .indices import (
    18	    coalition_integration,
    19	    control_shares,
    20	    hhi,
    21	    integration_matrix,
    22	    integration_statistic,
    23	    unaccountable_concentration,
    24	    weight_sensitivity,
    25	)
    26	from .necessity import (
    27	    DEPENDENCIES,
    28	    HARD_CASES,
    29	    GovernanceSystem,
    30	    Practice,
    31	    check_proposition_a,
    32	    dependency_graph,
    33	    derive_functions,
    34	    is_strongly_connected,
    35	)
    36	from .network import MultiplexNetwork
    37	from .pillars import AXIOM_TO_PILLAR, M, PAIRS, PILLARS, Axiom, Pillar
    38	from .regimes import regime_profiles
    39	
    40	__all__ = [
    41	    "AXIOM_TO_PILLAR", "Axiom", "CaptureLink", "CaptureThresholds", "DEPENDENCIES",
    42	    "GovernanceSystem", "HARD_CASES", "M", "MultiplexNetwork", "PAIRS", "PILLARS", "Pillar",
    43	    "Polity", "Practice", "a_does_not_imply_b", "assess", "check_proposition_a",
    44	    "coalition_integration", "control_shares", "dependency_graph", "derive_functions", "hhi",
    45	    "integration_matrix", "integration_statistic", "is_capture_link", "is_strongly_connected",
    46	    "negative_feedback_example", "proposition_b", "regime_profiles", "simulate",
    47	    "spectral_radius", "unaccountable_concentration", "weight_sensitivity",
    48	]

exec
/usr/local/bin/zsh -lc "nl -ba model/tests/test_pillars_network.py | sed -n '1,260p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	import numpy as np
     2	import pytest
     3	
     4	from beast_system.network import MultiplexNetwork
     5	from beast_system.pillars import AXIOM_TO_PILLAR, M, PAIRS, PILLARS, Axiom, Pillar
     6	
     7	
     8	def test_six_pillars_with_labels_and_questions():
     9	    assert M == 6
    10	    assert [p.label for p in PILLARS] == [
    11	        "financial", "political", "judicial", "ideological", "coercive", "productive"]
    12	    assert Pillar.J.question == "Who interprets the laws?"
    13	    assert [p.position for p in PILLARS] == list(range(6))
    14	
    15	
    16	def test_axiom_map_is_bijection_in_kb_order():
    17	    assert [a.label for a in Axiom] == [
    18	        "scarcity", "plurality", "generality", "coordination", "defection", "maintenance"]
    19	    assert set(AXIOM_TO_PILLAR.values()) == set(PILLARS)
    20	    assert Axiom.Ax5.pillar is Pillar.C and Axiom.Ax6.pillar is Pillar.W
    21	
    22	
    23	def test_fifteen_pairs():
    24	    assert len(PAIRS) == 15 == M * (M - 1) // 2
    25	
    26	
    27	def _net(**overrides):
    28	    kw = dict(actors=("a", "b"), layers={Pillar.F: [[0, 0.5], [0.2, 0]]},
    29	              roles={"a": {Pillar.F}})
    30	    kw.update(overrides)
    31	    return MultiplexNetwork(**kw)
    32	
    33	
    34	def test_network_fills_missing_layers_and_freezes():
    35	    net = _net()
    36	    assert net.layer(Pillar.W).shape == (2, 2) and not net.layer(Pillar.W).any()
    37	    with pytest.raises(ValueError):
    38	        net.layer(Pillar.F)[0, 1] = 0.9
    39	
    40	
    41	@pytest.mark.parametrize("bad", [[[0, 1.2], [0, 0]], [[0, -0.1], [0, 0]], [[0, np.nan], [0, 0]]])
    42	def test_network_rejects_weights_outside_unit_interval(bad):
    43	    with pytest.raises(ValueError):
    44	        _net(layers={Pillar.F: bad})
    45	
    46	
    47	def test_network_rejects_wrong_shape_and_unknown_role_actor():
    48	    with pytest.raises(ValueError):
    49	        _net(layers={Pillar.F: np.zeros((3, 3))})
    50	    with pytest.raises(ValueError):
    51	        _net(roles={"zed": {Pillar.F}})
    52	    with pytest.raises(ValueError):
    53	        _net(actors=("a", "a"))
    54	
    55	
    56	def test_role_map_support_and_fusion():
    57	    net = _net(roles={"a": {Pillar.F, Pillar.P}, "b": set(PILLARS) - {Pillar.F, Pillar.P}})
    58	    assert net.has_full_support()
    59	    assert net.fused_actors() == {"a", "b"}
    60	    assert not _net().has_full_support()
    61	
    62	
    63	def test_out_strength_shares():
    64	    shares = _net().out_strength_shares(Pillar.F)
    65	    assert shares == pytest.approx({"a": 0.5 / 0.7, "b": 0.2 / 0.7})
    66	    with pytest.raises(ValueError):
    67	        _net().out_strength_shares(Pillar.C)

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/dynamics.py | sed -n '1,320p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Linear pillar-capacity dynamics x_{t+1} = B x_t + D z_t + eps_t (source Section 5.3).
     2	
     3	x_t = (F_t, P_t, J_t, I^cap_t, C_t, W_t) in pillar order. The source warns that stability
     4	cannot be inferred from positive links alone (negative feedback, substitution, saturation,
     5	legitimacy loss) and uses dominant eigenvalues of a local linearization as the language of
     6	persistence. Here a deviation of x from its steady state persists iff the spectral radius
     7	rho(B) >= 1; for rho(B) < 1 it decays geometrically.
     8	"""
     9	
    10	from __future__ import annotations
    11	
    12	from collections.abc import Mapping
    13	from dataclasses import dataclass
    14	
    15	import numpy as np
    16	
    17	from .necessity import Graph, dependency_graph
    18	from .pillars import M, Pillar
    19	
    20	
    21	def _square(B: np.ndarray) -> np.ndarray:
    22	    arr = np.asarray(B, dtype=float)
    23	    if arr.shape != (M, M):
    24	        raise ValueError(f"B must be {M}x{M}, got {arr.shape}")
    25	    if not np.all(np.isfinite(arr)):
    26	        raise ValueError("B must be finite")
    27	    return arr
    28	
    29	
    30	def spectral_radius(B: np.ndarray) -> float:
    31	    """rho(B) = max |lambda| over eigenvalues of B."""
    32	    return float(np.max(np.abs(np.linalg.eigvals(_square(B)))))
    33	
    34	
    35	def deviation_persists(B: np.ndarray) -> bool:
    36	    """True iff rho(B) >= 1, i.e. a deviation from steady state does not die out."""
    37	    return spectral_radius(B) >= 1.0
    38	
    39	
    40	def dependency_matrix(graph: Graph, weight: float, self_weight: float = 0.0) -> np.ndarray:
    41	    """B with B[dependent, provider] = weight for each edge, and self_weight on the diagonal.
    42	
    43	    Row = pillar at t+1, column = pillar at t, matching x_{t+1} = B x_t.
    44	    """
    45	    B = np.eye(M) * float(self_weight)
    46	    for provider, dependents in graph.items():
    47	        for dep in dependents:
    48	            B[dep.position, provider.position] = float(weight)
    49	    return B
    50	
    51	
    52	def simulate(
    53	    B: np.ndarray,
    54	    x0: np.ndarray,
    55	    steps: int,
    56	    D: np.ndarray | None = None,
    57	    z: np.ndarray | None = None,
    58	    noise_sd: float = 0.0,
    59	    seed: int | None = None,
    60	) -> np.ndarray:
    61	    """Iterate x_{t+1} = B x_t + D z_t + eps_t; returns an array of shape (steps + 1, 6).
    62	
    63	    ``z`` has shape (steps, k) and ``D`` shape (6, k); eps_t ~ N(0, noise_sd^2 I).
    64	    """
    65	    B = _square(B)
    66	    x = np.asarray(x0, dtype=float)
    67	    if x.shape != (M,):
    68	        raise ValueError(f"x0 must have shape ({M},)")
    69	    if steps < 0:
    70	        raise ValueError("steps must be non-negative")
    71	    if (D is None) != (z is None):
    72	        raise ValueError("pass both D and z, or neither")
    73	    if D is not None and z is not None:
    74	        D = np.asarray(D, dtype=float)
    75	        z = np.asarray(z, dtype=float)
    76	        if D.ndim != 2 or D.shape[0] != M or z.shape != (steps, D.shape[1]):
    77	            raise ValueError("D must be (6, k) and z must be (steps, k)")
    78	    if noise_sd < 0.0:
    79	        raise ValueError("noise_sd must be non-negative")
    80	    rng = np.random.default_rng(seed)
    81	    path = np.empty((steps + 1, M))
    82	    path[0] = x
    83	    for t in range(steps):
    84	        x = B @ x
    85	        if D is not None and z is not None:
    86	            x = x + D @ z[t]
    87	        if noise_sd > 0.0:
    88	            x = x + rng.normal(0.0, noise_sd, size=M)
    89	        path[t + 1] = x
    90	    return path
    91	
    92	
    93	@dataclass(frozen=True)
    94	class FeedbackExample:
    95	    """Two matrices with the same positive links; only the feedback one has negative entries."""
    96	
    97	    B_positive: np.ndarray
    98	    B_feedback: np.ndarray
    99	    rho_positive: float
   100	    rho_feedback: float
   101	
   102	    @property
   103	    def same_positive_links(self) -> bool:
   104	        return bool(np.array_equal(self.B_positive > 0, self.B_feedback > 0))
   105	
   106	
   107	#: Negative feedback entries (provider, dependent) -> weight: coercion erodes legitimacy and
   108	#: depresses productive effort (source Section 5.3, 'legitimacy loss'). Illustrative values.
   109	NEGATIVE_FEEDBACK: Mapping[tuple[Pillar, Pillar], float] = {
   110	    (Pillar.C, Pillar.I): -0.4,
   111	    (Pillar.C, Pillar.W): -0.3,
   112	}
   113	
   114	
   115	def negative_feedback_example(
   116	    weight: float = 0.25,
   117	    self_weight: float = 0.6,
   118	    feedback: Mapping[tuple[Pillar, Pillar], float] = NEGATIVE_FEEDBACK,
   119	) -> FeedbackExample:
   120	    """Positive dependency links do not guarantee persistence (source Section 5.3).
   121	
   122	    With the derived dependency edges at ``weight`` and ``self_weight`` on the diagonal,
   123	    rho > 1. Adding negative feedback on entries that carry no positive link leaves every
   124	    positive link unchanged yet pushes rho below 1, so deviations decay.
   125	    """
   126	    B_pos = dependency_matrix(dependency_graph(include_conditional=False), weight, self_weight)
   127	    B_fb = B_pos.copy()
   128	    for (provider, dependent), w in feedback.items():
   129	        if w >= 0.0:
   130	            raise ValueError("feedback entries must be negative")
   131	        if B_pos[dependent.position, provider.position] != 0.0:
   132	            raise ValueError("feedback must not overwrite a positive link")
   133	        B_fb[dependent.position, provider.position] = w
   134	    return FeedbackExample(B_pos, B_fb, spectral_radius(B_pos), spectral_radius(B_fb))

exec
/usr/local/bin/zsh -lc "nl -ba model/tests/test_indices.py | sed -n '1,220p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	import numpy as np
     2	import pytest
     3	
     4	from beast_system.indices import (
     5	    coalition_integration,
     6	    control_shares,
     7	    hhi,
     8	    integration_matrix,
     9	    integration_statistic,
    10	    normalized_hhi,
    11	    unaccountable_concentration,
    12	    validate_integration_matrix,
    13	    validate_shares,
    14	    validate_weights,
    15	    weight_sensitivity,
    16	)
    17	from beast_system.pillars import PAIRS, PILLARS, Pillar
    18	
    19	F, P, J, I, C, W = PILLARS
    20	
    21	
    22	def test_control_shares_normalize():
    23	    assert control_shares({"x": 3, "y": 1}) == pytest.approx({"x": 0.75, "y": 0.25})
    24	
    25	
    26	@pytest.mark.parametrize("raw", [{"x": -1, "y": 2}, {"x": 0, "y": 0}, {}, {"x": float("inf")}])
    27	def test_control_shares_reject_bad_input(raw):
    28	    with pytest.raises(ValueError):
    29	        control_shares(raw)
    30	
    31	
    32	def test_validate_shares_requires_sum_one():
    33	    with pytest.raises(ValueError):
    34	        validate_shares([0.5, 0.4])
    35	    validate_shares([0.5, 0.5])
    36	
    37	
    38	def test_hhi_monopoly_is_one():
    39	    assert hhi([1.0]) == 1.0
    40	    assert hhi([1.0, 0.0, 0.0]) == 1.0
    41	
    42	
    43	@pytest.mark.parametrize("n", [1, 2, 5, 37])
    44	def test_hhi_uniform_is_one_over_n(n):
    45	    assert hhi(np.full(n, 1.0 / n)) == pytest.approx(1.0 / n)
    46	
    47	
    48	def test_normalized_hhi_endpoints():
    49	    assert normalized_hhi([0.25] * 4) == pytest.approx(0.0)
    50	    assert normalized_hhi([1.0, 0.0]) == pytest.approx(1.0)
    51	    assert normalized_hhi([1.0]) == 1.0
    52	
    53	
    54	def test_u_bounds_random():
    55	    rng = np.random.default_rng(1)
    56	    for _ in range(200):
    57	        H = {m: float(rng.uniform(0.01, 1.0)) for m in PILLARS}
    58	        Q = {m: float(rng.uniform(0.0, 1.0)) for m in PILLARS}
    59	        w = rng.dirichlet(np.ones(6))
    60	        u = unaccountable_concentration(H, Q, dict(zip(PILLARS, w)))
    61	        assert 0.0 <= u <= 1.0
    62	
    63	
    64	def test_u_extremes():
    65	    ones = {m: 1.0 for m in PILLARS}
    66	    zeros = {m: 0.0 for m in PILLARS}
    67	    assert unaccountable_concentration(ones, zeros) == pytest.approx(1.0)
    68	    assert unaccountable_concentration(ones, ones) == 0.0
    69	    # U = 0 only needs Q_m = 1 where w_m > 0.
    70	    Q = {**zeros, F: 1.0}
    71	    assert unaccountable_concentration(ones, Q, {m: float(m is F) for m in PILLARS}) == 0.0
    72	
    73	
    74	@pytest.mark.parametrize("weights", [
    75	    {m: 1 / 6 for m in PILLARS if m is not W},
    76	    {m: 0.25 for m in PILLARS},
    77	    {**{m: 0.2 for m in PILLARS}, F: -0.2, P: 0.4},
    78	])
    79	def test_u_rejects_invalid_weights(weights):
    80	    with pytest.raises(ValueError):
    81	        validate_weights(weights)
    82	
    83	
    84	def test_u_rejects_bad_h_and_q():
    85	    ok = {m: 0.5 for m in PILLARS}
    86	    with pytest.raises(ValueError):
    87	        unaccountable_concentration({**ok, F: 1.5}, ok)
    88	    with pytest.raises(ValueError):
    89	        unaccountable_concentration(ok, {**ok, C: -0.1})
    90	    with pytest.raises(ValueError):
    91	        unaccountable_concentration({**ok, F: 0.0}, ok)
    92	    with pytest.raises(ValueError):
    93	        unaccountable_concentration({F: 0.5}, ok)
    94	
    95	
    96	def test_integration_statistic_averages_fifteen_pairs():
    97	    assert integration_statistic(np.ones((6, 6))) == pytest.approx(1.0)
    98	    assert integration_statistic(integration_matrix({})) == 0.0
    99	    assert integration_statistic(integration_matrix({(F, P): 0.9})) == pytest.approx(0.9 / 15)
   100	    vals = np.linspace(0, 1, 15)
   101	    C_ = integration_matrix(dict(zip(PAIRS, vals)))
   102	    assert integration_statistic(C_) == pytest.approx(vals.mean())
   103	
   104	
   105	def test_integration_matrix_validation():
   106	    bad = np.eye(6)
   107	    bad[0, 1] = 0.5
   108	    with pytest.raises(ValueError):
   109	        validate_integration_matrix(bad)  # asymmetric
   110	    with pytest.raises(ValueError):
   111	        integration_matrix({(F, P): 1.2})
   112	    with pytest.raises(ValueError):
   113	        integration_matrix({(F, F): 0.5})
   114	    with pytest.raises(ValueError):
   115	        integration_matrix({(F, P): 0.5, (P, F): 0.4})
   116	    with pytest.raises(ValueError):
   117	        validate_integration_matrix(np.eye(5))
   118	
   119	
   120	def test_coalition_integration_fused_and_disjoint():
   121	    fused = {m: {"core": 1.0} for m in PILLARS}
   122	    assert integration_statistic(coalition_integration(fused)) == 1.0
   123	    disjoint = {m: {f"{m.name}{k}": 0.5 for k in range(2)} for m in PILLARS}
   124	    assert integration_statistic(coalition_integration(disjoint)) == 0.0
   125	    # Merging two actors into one coalition raises C_FP to min(s^F(S), s^P(S)).
   126	    shares = dict(disjoint)
   127	    shares[F] = {"a": 0.6, "b": 0.4}
   128	    shares[P] = {"c": 0.3, "d": 0.7}
   129	    Cm = coalition_integration(shares, {"a": "S", "c": "S"})
   130	    assert Cm[F.position, P.position] == pytest.approx(0.3)
   131	
   132	
   133	def test_weight_sensitivity_within_vertex_bounds():
   134	    H = {m: 0.2 + 0.1 * m.position for m in PILLARS}
   135	    Q = {m: 0.5 for m in PILLARS}
   136	    res = weight_sensitivity(H, Q, n_draws=500)
   137	    terms = [H[m] * 0.5 for m in PILLARS]
   138	    assert res.vertex_min == pytest.approx(min(terms))
   139	    assert res.vertex_max == pytest.approx(max(terms))
   140	    assert res.draws.min() >= res.vertex_min - 1e-12
   141	    assert res.draws.max() <= res.vertex_max + 1e-12
   142	    assert res.vertex_min <= res.baseline <= res.vertex_max
   143	    lo, hi = res.quantiles
   144	    assert lo <= hi
   145	    assert res.fraction_at_least(0.0) == 1.0
   146	    assert res.fraction_at_least(1.0) == 0.0

2026-10-22T14:28:39.881814Z ERROR codex_core::tools::router: error=collab spawn failed: no thread with id: 01a16403-79d5-7590-bd98-8c27d52fd577
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/necessity.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Structural necessity: Proposition A and the pillar dependency graph (Part VII Theorem A).
     2	
     3	Theorem A (notation.md CENTRAL THESIS; KB Section 4): if a governance system G persists and
     4	satisfies Ax1..Ax6, then every pillar in M is implemented in G, and the pillars stand in the
     5	dependency relations D. Implementation is role-level, not institution-level (Hempel 1959): a
     6	function may be held by a formal institution, fused with other functions inside one
     7	institution, or exercised informally (gossip and shunning as C, mediators as J).
     8	
     9	What this module does and does not do. It cannot prove Theorem A. It encodes the lemma schema
    10	'Ax_k + persistence => some practice solves problem_k' and checks it against coded cases. The
    11	role map is DERIVED from independently coded practices, never declared, so a persistent case
    12	that satisfies all six axioms yet has no practice for some problem is reported as a
    13	counterexample (the falsifier required by KB Section 4.4), not silently accepted.
    14	
    15	Dependency edges are written provider -> dependent ('dependent needs provider'). Each edge
    16	carries its axiom basis and a status: 'derived' (argued from the axioms for every persistent
    17	G) or 'conditional' (holds only under an extra assumption, e.g. specialized office holders).
    18	Strong connectivity of D is flagged in KB Section 4.3 as an OPEN problem; it is tested here on
    19	the encoded graph, which is a property of the encoding, not a proof that it is forced.
    20	"""
    21	
    22	from __future__ import annotations
    23	
    24	from collections.abc import Iterable, Mapping
    25	from dataclasses import dataclass, field
    26	from typing import Literal
    27	
    28	from .pillars import AXIOM_TO_PILLAR, PILLAR_TO_AXIOM, PILLARS, Axiom, Pillar
    29	
    30	RealizedForm = Literal["formal institution", "fused", "informal/minimal"]
    31	FORMAL: RealizedForm = "formal institution"
    32	FUSED: RealizedForm = "fused"
    33	INFORMAL: RealizedForm = "informal/minimal"
    34	
    35	
    36	@dataclass(frozen=True)
    37	class Practice:
    38	    """A regular activity that discharges the problem generated by axiom ``solves``.
    39	
    40	    ``formal`` is True when the activity is attached to a designated office or organization.
    41	    ``source`` holds the citation key(s) supporting the coding.
    42	    """
    43	
    44	    description: str
    45	    solves: Axiom
    46	    holders: frozenset[str]
    47	    formal: bool = False
    48	    source: str = ""
    49	
    50	    def __post_init__(self) -> None:
    51	        if not isinstance(self.solves, Axiom):
    52	            raise TypeError("Practice.solves must be an Axiom")
    53	        holders = frozenset(self.holders)
    54	        if not holders or any(not isinstance(h, str) or not h for h in holders):
    55	            raise ValueError("a practice needs at least one named holder")
    56	        if not self.description.strip():
    57	            raise ValueError("a practice needs a description")
    58	        object.__setattr__(self, "holders", holders)
    59	
    60	    @property
    61	    def pillar(self) -> Pillar:
    62	        return AXIOM_TO_PILLAR[self.solves]
    63	
    64	
    65	@dataclass(frozen=True)
    66	class GovernanceSystem:
    67	    """A collective that makes and enforces collective decisions (KB Section 4.1).
    68	
    69	    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
    70	    over the period studied. Both are coded independently of ``practices``.
    71	    """
    72	
    73	    name: str
    74	    persistent: bool
    75	    axioms: frozenset[Axiom]
    76	    practices: tuple[Practice, ...] = ()
    77	    note: str = ""
    78	
    79	    def __post_init__(self) -> None:
    80	        axioms = frozenset(self.axioms)
    81	        if any(not isinstance(a, Axiom) for a in axioms):
    82	            raise TypeError("axioms must be Axiom members")
    83	        practices = tuple(self.practices)
    84	        if any(not isinstance(p, Practice) for p in practices):
    85	            raise TypeError("practices must be Practice instances")
    86	        object.__setattr__(self, "axioms", axioms)
    87	        object.__setattr__(self, "practices", practices)
    88	
    89	    def holds(self, axiom: Axiom) -> bool:
    90	        """Predicate for one axiom (Ax1 scarcity, ..., Ax6 maintenance)."""
    91	        return axiom in self.axioms
    92	
    93	    @property
    94	    def all_axioms_hold(self) -> bool:
    95	        return all(self.holds(a) for a in Axiom)
    96	
    97	
    98	def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
    99	    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
   100	    roles: dict[str, set[Pillar]] = {}
   101	    for p in system.practices:
   102	        for h in p.holders:
   103	            roles.setdefault(h, set()).add(p.pillar)
   104	    return {h: frozenset(ps) for h, ps in roles.items()}
   105	
   106	
   107	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   108	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   109	
   110	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   111	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   112	    """
   113	    practices = [p for p in system.practices if p.pillar is pillar]
   114	    if not practices:
   115	        return None
   116	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   117	    if not formal_holders:
   118	        return INFORMAL
   119	    formal_roles: dict[str, set[Pillar]] = {}
   120	    for p in system.practices:
   121	        if p.formal:
   122	            for h in p.holders:
   123	                formal_roles.setdefault(h, set()).add(p.pillar)
   124	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   125	        return FUSED
   126	    return FORMAL
   127	
   128	
   129	@dataclass(frozen=True)
   130	class Derivation:
   131	    """Result of the lemma for one axiom: required pillar and its realized form."""
   132	
   133	    axiom: Axiom
   134	    pillar: Pillar
   135	    form: RealizedForm | None
   136	    practices: tuple[Practice, ...]
   137	
   138	    @property
   139	    def realized(self) -> bool:
   140	        return self.form is not None
   141	
   142	
   143	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   144	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   145	
   146	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   147	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   148	    """
   149	    out: dict[Axiom, Derivation] = {}
   150	    for axiom in Axiom:
   151	        if not system.holds(axiom):
   152	            continue
   153	        pillar = AXIOM_TO_PILLAR[axiom]
   154	        out[axiom] = Derivation(
   155	            axiom=axiom,
   156	            pillar=pillar,
   157	            form=realized_form(system, pillar),
   158	            practices=tuple(p for p in system.practices if p.solves is axiom),
   159	        )
   160	    return out
   161	
   162	
   163	# Dependency graph -------------------------------------------------------------------------
   164	
   165	DependencyStatus = Literal["derived", "conditional"]
   166	Graph = Mapping[Pillar, Iterable[Pillar]]
   167	
   168	
   169	@dataclass(frozen=True)
   170	class Dependency:
   171	    """Edge provider -> dependent: the dependent pillar needs an output of the provider."""
   172	
   173	    provider: Pillar
   174	    dependent: Pillar
   175	    basis: tuple[Axiom, ...]
   176	    status: DependencyStatus
   177	    rationale: str
   178	
   179	
   180	_A = Axiom
   181	_P = Pillar
   182	
   183	#: Encoded dependency relations D (KB Sections 4.3 item 3 and VII.2). The first six entries are
   184	#: the relations listed in the Part VII brief; the remainder come from the KB list.
   185	DEPENDENCIES: tuple[Dependency, ...] = (
   186	    Dependency(_P.W, _P.C, (_A.Ax6, _A.Ax5), "derived",
   187	               "C needs W's resources: sanctioning consumes time and goods someone produces"),
   188	    Dependency(_P.P, _P.J, (_A.Ax2, _A.Ax3), "derived",
   189	               "J needs P's rules: interpretation presupposes rules to interpret"),
   190	    Dependency(_P.I, _P.P, (_A.Ax4, _A.Ax2), "derived",
   191	               "P needs I's legitimacy: rule-making needs a recognized rule of recognition (Hart)"),
   192	    Dependency(_P.J, _P.F, (_A.Ax3, _A.Ax1), "derived",
   193	               "F needs J's enforcement of claims: contested claims on resources need case rulings"),
   194	    Dependency(_P.F, _P.W, (_A.Ax1, _A.Ax6), "derived",
   195	               "W needs F's allocation: producers need allocated inputs and shares"),
   196	    Dependency(_P.W, _P.I, (_A.Ax6, _A.Ax4), "derived",
   197	               "I needs W's surplus: belief maintenance consumes produced resources"),
   198	    Dependency(_P.W, _P.F, (_A.Ax6, _A.Ax1), "derived",
   199	               "production creates the stock that allocation divides"),
   200	    Dependency(_P.C, _P.F, (_A.Ax5, _A.Ax1), "derived",
   201	               "allocation rules are sometimes defected from; sanctions back them"),
   202	    Dependency(_P.C, _P.J, (_A.Ax5, _A.Ax3), "derived",
   203	               "adjudication without enforcement is advice"),
   204	    Dependency(_P.I, _P.J, (_A.Ax4, _A.Ax3), "derived",
   205	               "rulings settle disputes only if recognized as authoritative"),
   206	    Dependency(_P.I, _P.C, (_A.Ax4, _A.Ax5), "derived",
   207	               "a sanction must be recognized as sanction rather than aggression"),
   208	    Dependency(_P.I, _P.W, (_A.Ax4, _A.Ax6), "derived",
   209	               "norms of work and quasi-voluntary compliance (Levi)"),
   210	    Dependency(_P.F, _P.C, (_A.Ax1, _A.Ax5), "conditional",
   211	               "specialized sanction capacity needs provisioning (Tilly, Levi); gossip does not"),
   212	    Dependency(_P.J, _P.P, (_A.Ax3, _A.Ax2), "conditional",
   213	               "precedent feeds rule change; only where rules change through interpretation"),
   214	    Dependency(_P.J, _P.I, (_A.Ax3, _A.Ax4), "conditional",
   215	               "reasoned judgments act as public symbols; needs public adjudication"),
   216	    Dependency(_P.F, _P.I, (_A.Ax1, _A.Ax4), "conditional",
   217	               "funding of ideology producers; needs specialist belief producers"),
   218	    Dependency(_P.P, _P.I, (_A.Ax2, _A.Ax4), "conditional",
   219	               "legislation as a public symbolic act; needs declared rules"),
   220	)
   221	
   222	#: The six relations named in the Part VII brief, on their own.
   223	BRIEF_DEPENDENCIES: tuple[Dependency, ...] = DEPENDENCIES[:6]
   224	
   225	
   226	def dependency_graph(
   227	    include_conditional: bool = True,
   228	    dependencies: Iterable[Dependency] = DEPENDENCIES,
   229	) -> dict[Pillar, frozenset[Pillar]]:
   230	    """Adjacency provider -> set of dependents over all six pillars."""
   231	    adj: dict[Pillar, set[Pillar]] = {m: set() for m in PILLARS}
   232	    for d in dependencies:
   233	        if include_conditional or d.status == "derived":
   234	            adj[d.provider].add(d.dependent)
   235	    return {m: frozenset(v) for m, v in adj.items()}
   236	
   237	
   238	def _nodes(graph: Graph) -> set[Pillar]:
   239	    nodes = set(graph)
   240	    for targets in graph.values():
   241	        nodes.update(targets)
   242	    return nodes
   243	
   244	
   245	def _reach(graph: Mapping[Pillar, frozenset[Pillar]], start: Pillar) -> set[Pillar]:
   246	    seen = {start}
   247	    stack = [start]
   248	    while stack:
   249	        for nxt in graph.get(stack.pop(), frozenset()):
   250	            if nxt not in seen:
   251	                seen.add(nxt)
   252	                stack.append(nxt)
   253	    return seen
   254	
   255	
   256	def is_strongly_connected(graph: Graph, nodes: Iterable[Pillar] | None = None) -> bool:
   257	    """True iff every node of the graph is reachable from every other node.
   258	
   259	    ``nodes`` restricts the graph to an induced subgraph (default: all nodes that appear).
   260	    The empty graph is not strongly connected; a single node is.
   261	    """
   262	    keep = set(nodes) if nodes is not None else _nodes(graph)
   263	    if not keep:
   264	        return False
   265	    fwd: dict[Pillar, frozenset[Pillar]] = {
   266	        u: frozenset(v for v in graph.get(u, ()) if v in keep) for u in keep
   267	    }
   268	    rev: dict[Pillar, set[Pillar]] = {u: set() for u in keep}
   269	    for u, vs in fwd.items():
   270	        for v in vs:
   271	            rev[v].add(u)
   272	    start = next(iter(keep))
   273	    rev_f = {u: frozenset(v) for u, v in rev.items()}
   274	    return _reach(fwd, start) == keep and _reach(rev_f, start) == keep
   275	
   276	
   277	def critical_edges(graph: Graph) -> list[tuple[Pillar, Pillar]]:
   278	    """Edges whose single removal breaks strong connectivity (empty if not connected)."""
   279	    nodes = _nodes(graph)
   280	    base = {u: frozenset(graph.get(u, ())) for u in nodes}
   281	    if not is_strongly_connected(base):
   282	        return []
   283	    out = []
   284	    for u in PILLARS:
   285	        for v in sorted(base.get(u, ()), key=lambda p: p.position):
   286	            pruned = dict(base)
   287	            pruned[u] = base[u] - {v}
   288	            if not is_strongly_connected(pruned, nodes):
   289	                out.append((u, v))
   290	    return out
   291	
   292	
   293	def sinks_and_sources(graph: Graph) -> tuple[frozenset[Pillar], frozenset[Pillar]]:
   294	    """Pillars with no outgoing edge (sinks) and with no incoming edge (sources)."""
   295	    nodes = _nodes(graph)
   296	    has_out = {u for u in nodes if any(True for _ in graph.get(u, ()))}
   297	    has_in = {v for u in nodes for v in graph.get(u, ())}
   298	    return frozenset(nodes - has_out), frozenset(nodes - has_in)
   299	
   300	
   301	# Proposition A ----------------------------------------------------------------------------
   302	
   303	
   304	@dataclass(frozen=True)
   305	class PropositionAResult:
   306	    """Outcome of checking Theorem A on one coded system.
   307	
   308	    ``holds`` is the structural predicate Struct(G): all six pillars realized and the derived
   309	    dependency graph strongly connected on them. ``counterexample`` is True when the theorem's
   310	    antecedent holds (persistent, Ax1..Ax6) but Struct(G) fails: a falsifier of Theorem A.
   311	    """
   312	
   313	    system: str
   314	    antecedent: bool
   315	    realized: frozenset[Pillar]
   316	    missing: frozenset[Pillar]
   317	    dependencies_connected: bool
   318	    holds: bool
   319	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   320	
   321	    @property
   322	    def counterexample(self) -> bool:
   323	        return self.antecedent and not self.holds
   324	
   325	
   326	def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
   327	    """Check Theorem A on ``system`` (Part VII Theorem A; KB Section 4.3)."""
   328	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   329	    connected = is_strongly_connected(dependency_graph(include_conditional=False), realized)
   330	    return PropositionAResult(
   331	        system=system.name,
   332	        antecedent=system.persistent and system.all_axioms_hold,
   333	        realized=realized,
   334	        missing=frozenset(PILLARS) - realized,
   335	        dependencies_connected=connected,
   336	        holds=realized == frozenset(PILLARS) and connected,
   337	        derivations=derive_functions(system),
   338	    )
   339	
   340	
   341	def formal_system(
   342	    name: str,
   343	    holders: Mapping[Pillar, Iterable[str]],
   344	    persistent: bool = True,
   345	    source: str = "",
   346	) -> GovernanceSystem:
   347	    """A persistent system satisfying Ax1..Ax6 whose pillars are held by formal organizations.
   348	
   349	    An actor listed under several pillars is fused. Used for regime profiles and counter-models.
   350	    """
   351	    practices = tuple(
   352	        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
   353	                 frozenset(hs), formal=True, source=source)
   354	        for m, hs in holders.items()
   355	        if hs
   356	    )
   357	    return GovernanceSystem(name, persistent, frozenset(Axiom), practices)
   358	
   359	
   360	# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
   361	
   362	
   363	def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
   364	    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)
   365	
   366	
   367	NUER = GovernanceSystem(
   368	    name="Nuer ('ordered anarchy')",
   369	    persistent=True,
   370	    axioms=frozenset(Axiom),
   371	    practices=(
   372	        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
   373	                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
   374	        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
   375	                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
   376	        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
   377	                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
   378	        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
   379	                  {"prophets", "lineages"}, "evanspritchard1940"),
   380	        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
   381	                  {"agnatic kin"}, "evanspritchard1940"),
   382	        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
   383	                  "evanspritchard1940"),
   384	    ),
   385	    note="no office holds coercive authority; functions exist without separation",
   386	)
   387	
   388	JU_HOANSI = GovernanceSystem(
   389	    name="Ju/'hoansi (!Kung)",
   390	    persistent=True,
   391	    axioms=frozenset(Axiom),
   392	    practices=(
   393	        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
   394	                  {"hunters", "camp members"}, "lee2013; marshall1976"),
   395	        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
   396	                  {"camp members"}, "lee2013"),
   397	        _informal("disputes talked out with kin mediators", Axiom.Ax3,
   398	                  {"kin mediators"}, "lee1979; wiessner2005"),
   399	        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
   400	                  {"healers", "camp members"}, "marshall1976"),
   401	        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
   402	                  {"camp members"}, "wiessner2005; lee2013"),
   403	        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
   404	    ),
   405	    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
   406	)
   407	
   408	OSTROM_COMMONS = GovernanceSystem(
   409	    name="Ostrom commons (design principles)",
   410	    persistent=True,
   411	    axioms=frozenset(Axiom),
   412	    practices=(
   413	        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
   414	                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
   415	        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
   416	                  {"appropriators"}, "ostrom1990"),
   417	        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
   418	                  {"appropriators"}, "ostrom1990; cox2010"),
   419	        _informal("shared norms; minimal recognition of rights to organize (DP7)",
   420	                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),
   421	        _informal("monitoring and graduated sanctions by appropriators (DP4, DP5)",
   422	                  Axiom.Ax5, {"appropriators"}, "ostrom1990; cox2010"),
   423	        _informal("appropriation and maintenance labor", Axiom.Ax6, {"appropriators"},
   424	                  "ostrom1990"),
   425	    ),
   426	    note="checks in minimal form; monitors are appropriators or accountable to them",
   427	)
   428	
   429	CONSENSUS_VILLAGE = GovernanceSystem(
   430	    name="Consensus village (stylized)",
   431	    persistent=True,
   432	    axioms=frozenset(Axiom),
   433	    practices=(
   434	        _informal("household plots; reciprocal labor exchange; sharing norms", Axiom.Ax1,
   435	                  {"households"}, "sahlins1972"),
   436	        _informal("consensus meeting of adults", Axiom.Ax2, {"village meeting"},
   437	                  "clastres1987; boehm1999"),
   438	        _informal("elders mediate disputes", Axiom.Ax3, {"elders"}, "boehm1999"),
   439	        _informal("ritual and myth; moral talk", Axiom.Ax4, {"village meeting", "elders"},
   440	                  "boehm1999"),
   441	        _informal("gossip, shunning, ostracism of would-be dominants", Axiom.Ax5,
   442	                  {"village meeting"}, "boehm1999; woodburn1982"),
   443	        _informal("gardening and household labor", Axiom.Ax6, {"households"},
   444	                  "sahlins1972"),
   445	    ),
   446	    note="stylized composite; reverse dominance hierarchy",
   447	)
   448	
   449	HARD_CASES: tuple[GovernanceSystem, ...] = (NUER, JU_HOANSI, OSTROM_COMMONS, CONSENSUS_VILLAGE)

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/dynamics.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Linear pillar-capacity dynamics x_{t+1} = B x_t + D z_t + eps_t (source Section 5.3).
     2	
     3	x_t = (F_t, P_t, J_t, I^cap_t, C_t, W_t) in pillar order. The source warns that stability
     4	cannot be inferred from positive links alone (negative feedback, substitution, saturation,
     5	legitimacy loss) and uses dominant eigenvalues of a local linearization as the language of
     6	persistence. Here a deviation of x from its steady state persists iff the spectral radius
     7	rho(B) >= 1; for rho(B) < 1 it decays geometrically.
     8	"""
     9	
    10	from __future__ import annotations
    11	
    12	from collections.abc import Mapping
    13	from dataclasses import dataclass
    14	
    15	import numpy as np
    16	
    17	from .necessity import Graph, dependency_graph
    18	from .pillars import M, Pillar
    19	
    20	
    21	def _square(B: np.ndarray) -> np.ndarray:
    22	    arr = np.asarray(B, dtype=float)
    23	    if arr.shape != (M, M):
    24	        raise ValueError(f"B must be {M}x{M}, got {arr.shape}")
    25	    if not np.all(np.isfinite(arr)):
    26	        raise ValueError("B must be finite")
    27	    return arr
    28	
    29	
    30	def spectral_radius(B: np.ndarray) -> float:
    31	    """rho(B) = max |lambda| over eigenvalues of B."""
    32	    return float(np.max(np.abs(np.linalg.eigvals(_square(B)))))
    33	
    34	
    35	def deviation_persists(B: np.ndarray) -> bool:
    36	    """True iff rho(B) >= 1, i.e. a deviation from steady state does not die out."""
    37	    return spectral_radius(B) >= 1.0
    38	
    39	
    40	def dependency_matrix(graph: Graph, weight: float, self_weight: float = 0.0) -> np.ndarray:
    41	    """B with B[dependent, provider] = weight for each edge, and self_weight on the diagonal.
    42	
    43	    Row = pillar at t+1, column = pillar at t, matching x_{t+1} = B x_t.
    44	    """
    45	    B = np.eye(M) * float(self_weight)
    46	    for provider, dependents in graph.items():
    47	        for dep in dependents:
    48	            B[dep.position, provider.position] = float(weight)
    49	    return B
    50	
    51	
    52	def simulate(
    53	    B: np.ndarray,
    54	    x0: np.ndarray,
    55	    steps: int,
    56	    D: np.ndarray | None = None,
    57	    z: np.ndarray | None = None,
    58	    noise_sd: float = 0.0,
    59	    seed: int | None = None,
    60	) -> np.ndarray:
    61	    """Iterate x_{t+1} = B x_t + D z_t + eps_t; returns an array of shape (steps + 1, 6).
    62	
    63	    ``z`` has shape (steps, k) and ``D`` shape (6, k); eps_t ~ N(0, noise_sd^2 I).
    64	    """
    65	    B = _square(B)
    66	    x = np.asarray(x0, dtype=float)
    67	    if x.shape != (M,):
    68	        raise ValueError(f"x0 must have shape ({M},)")
    69	    if steps < 0:
    70	        raise ValueError("steps must be non-negative")
    71	    if (D is None) != (z is None):
    72	        raise ValueError("pass both D and z, or neither")
    73	    if D is not None and z is not None:
    74	        D = np.asarray(D, dtype=float)
    75	        z = np.asarray(z, dtype=float)
    76	        if D.ndim != 2 or D.shape[0] != M or z.shape != (steps, D.shape[1]):
    77	            raise ValueError("D must be (6, k) and z must be (steps, k)")
    78	    if noise_sd < 0.0:
    79	        raise ValueError("noise_sd must be non-negative")
    80	    rng = np.random.default_rng(seed)
    81	    path = np.empty((steps + 1, M))
    82	    path[0] = x
    83	    for t in range(steps):
    84	        x = B @ x
    85	        if D is not None and z is not None:
    86	            x = x + D @ z[t]
    87	        if noise_sd > 0.0:
    88	            x = x + rng.normal(0.0, noise_sd, size=M)
    89	        path[t + 1] = x
    90	    return path
    91	
    92	
    93	@dataclass(frozen=True)
    94	class FeedbackExample:
    95	    """Two matrices with the same positive links; only the feedback one has negative entries."""
    96	
    97	    B_positive: np.ndarray
    98	    B_feedback: np.ndarray
    99	    rho_positive: float
   100	    rho_feedback: float
   101	
   102	    @property
   103	    def same_positive_links(self) -> bool:
   104	        return bool(np.array_equal(self.B_positive > 0, self.B_feedback > 0))
   105	
   106	
   107	#: Negative feedback entries (provider, dependent) -> weight: coercion erodes legitimacy and
   108	#: depresses productive effort (source Section 5.3, 'legitimacy loss'). Illustrative values.
   109	NEGATIVE_FEEDBACK: Mapping[tuple[Pillar, Pillar], float] = {
   110	    (Pillar.C, Pillar.I): -0.4,
   111	    (Pillar.C, Pillar.W): -0.3,
   112	}
   113	
   114	
   115	def negative_feedback_example(
   116	    weight: float = 0.25,
   117	    self_weight: float = 0.6,
   118	    feedback: Mapping[tuple[Pillar, Pillar], float] = NEGATIVE_FEEDBACK,
   119	) -> FeedbackExample:
   120	    """Positive dependency links do not guarantee persistence (source Section 5.3).
   121	
   122	    With the derived dependency edges at ``weight`` and ``self_weight`` on the diagonal,
   123	    rho > 1. Adding negative feedback on entries that carry no positive link leaves every
   124	    positive link unchanged yet pushes rho below 1, so deviations decay.
   125	    """
   126	    B_pos = dependency_matrix(dependency_graph(include_conditional=False), weight, self_weight)
   127	    B_fb = B_pos.copy()
   128	    for (provider, dependent), w in feedback.items():
   129	        if w >= 0.0:
   130	            raise ValueError("feedback entries must be negative")
   131	        if B_pos[dependent.position, provider.position] != 0.0:
   132	            raise ValueError("feedback must not overwrite a positive link")
   133	        B_fb[dependent.position, provider.position] = w
   134	    return FeedbackExample(B_pos, B_fb, spectral_radius(B_pos), spectral_radius(B_fb))

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONPATH=model pytest -q -c /dev/null model/tests' in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T14:29:34.951801Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 exited 1 in 263ms:
Traceback (most recent call last):
  File "/Users/mlong/.pyenv/versions/3.12.9/bin/pytest", line 8, in <module>
    sys.exit(console_main())
             ^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/_pytest/config/__init__.py", line 223, in console_main
    code = main()
           ^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/_pytest/config/__init__.py", line 193, in main
    config = _prepareconfig(new_args, plugins)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/_pytest/config/__init__.py", line 361, in _prepareconfig
    config: Config = pluginmanager.hook.pytest_cmdline_parse(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/pluggy/_callers.py", line 167, in _multicall
    raise exception
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/pluggy/_callers.py", line 139, in _multicall
    teardown.throw(exception)
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/_pytest/helpconfig.py", line 124, in pytest_cmdline_parse
    config = yield
             ^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/_pytest/config/__init__.py", line 1186, in pytest_cmdline_parse
    self.parse(args)
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/_pytest/config/__init__.py", line 1556, in parse
    self.hook.pytest_load_initial_conftests(
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/pluggy/_callers.py", line 167, in _multicall
    raise exception
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/pluggy/_callers.py", line 139, in _multicall
    teardown.throw(exception)
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/_pytest/warnings.py", line 128, in pytest_load_initial_conftests
    return (yield)
            ^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/pluggy/_callers.py", line 116, in _multicall
    next(function_gen)  # first yield
    ^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/_pytest/capture.py", line 170, in pytest_load_initial_conftests
    capman.start_global_capturing()
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/_pytest/capture.py", line 773, in start_global_capturing
    self._global_capturing = _get_multicapture(self._method)
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/_pytest/capture.py", line 714, in _get_multicapture
    return MultiCapture(in_=FDCapture(0), out=FDCapture(1), err=FDCapture(2))
                                              ^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/_pytest/capture.py", line 493, in __init__
    TemporaryFile(buffering=0),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/tempfile.py", line 631, in TemporaryFile
    prefix, suffix, dir, output_type = _sanitize_params(prefix, suffix, dir)
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/tempfile.py", line 126, in _sanitize_params
    dir = gettempdir()
          ^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/tempfile.py", line 315, in gettempdir
    return _os.fsdecode(_gettempdir())
                        ^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/tempfile.py", line 308, in _gettempdir
    tempdir = _get_default_tempdir()
              ^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/tempfile.py", line 223, in _get_default_tempdir
    raise FileNotFoundError(_errno.ENOENT,
FileNotFoundError: [Errno 2] No usable temporary directory found in ['/var/folders/6z/np99jwkj4ys5z6l5y0xpwdx80000gn/T/', '/tmp', '/var/tmp', '/usr/tmp', '/Users/mlong/Documents/Development/the-beast-system']

2026-10-22T14:29:35.724405Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
2026-10-22T14:29:37.956394Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
The current tests could not start under the read-only environment because pytest tried to create a temporary capture file. I’m rerunning with capture and cache disabled; this does not change or inspect anything outside the requested Python scope.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=model pytest -q -s -p no:cacheprovider -c /dev/null model/tests' in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T14:29:39.969780Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 388ms:
.....................................................................
69 passed in 0.15s

hook: PreToolUse
hook: PreToolUse Completed
2026-10-22T14:29:46.179994Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=model python -c 'from beast_system.capture import CaptureLink,CaptureThresholds,a_does_not_imply_b,proposition_b; from beast_system.indices import unaccountable_concentration; from beast_system.pillars import PILLARS,Pillar; print(\"threshold_one\",a_does_not_imply_b(CaptureThresholds(1.0,1.0)).demonstrates_non_implication); link=CaptureLink(\"a\",\"b\",Pillar.F,\"yes\",\"yes\",\"yes\",evidence=\"citation\"); print(\"non_bool\",repr(link.holds),type(link.holds).__name__); H={m:1.0 for m in PILLARS}; Q={m:0.0 for m in PILLARS}; w={m:0.0 for m in PILLARS}; w[PILLARS[0]]=1.0+5e-10; print(\"u_above_one\",repr(unaccountable_concentration(H,Q,w))); th=CaptureThresholds(\"0.4\",\"0.5\"); print(\"threshold_types\",type(th.u_star).__name__,type(th.i_star).__name__); proposition_b(.5,.5,[],th)'" in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T14:29:51.355085Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 exited 1 in 239ms:
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/Users/mlong/Documents/Development/the-beast-system/model/beast_system/capture.py", line 103, in proposition_b
    u_high=U >= thresholds.u_star,
           ^^^^^^^^^^^^^^^^^^^^^^
TypeError: '>=' not supported between instances of 'float' and 'str'
threshold_one False
non_bool 'yes' str
u_above_one 1.0000000005
threshold_types str str

2026-10-22T14:29:53.981438Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
2026-10-22T14:30:01.702043Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
2026-10-22T14:30:06.534444Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
2026-10-22T14:30:11.172845Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
2026-10-22T14:30:13.784590Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
2026-10-22T14:30:19.007119Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
All 69 existing tests pass. The important gaps are semantic rather than regressions: in particular, the Proposition A result currently folds the open strong-connectivity question into `holds`, and dependency relations are checked from one global constant graph rather than from each coded system. I’m checking the example output and boundary cases before finalizing severity and coverage notes.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=model python model/examples/run_all.py' in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T14:30:20.116748Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 172ms:
Thresholds u* = 0.4, i* = 0.5. Regime values: ILLUSTRATIVE ASSUMPTIONS, not measurements.
profile                                                    H_F   H_P   H_J   H_I   H_C   H_W   U      I      A    U,I>=*  L  B
------------------------------------------------------------------------------------------------------------------------------
Market capitalism                                          0.30 0.36 0.54 0.26 0.38 0.38  0.165  0.293  yes  no      0  no
Communist party-state                                      0.46 0.82 0.52 0.54 0.52 0.46  0.470  0.683  yes  yes     0  no
Democratic socialism                                       0.24 0.38 0.68 0.26 0.52 0.34  0.108  0.200  yes  no      0  no
Islamic state (plural juristic authority)                  0.34 0.38 0.38 0.38 0.44 0.38  0.222  0.290  yes  no      0  no
Islamic state (centralized clerical-political authority)   0.38 0.38 0.50 0.46 0.52 0.38  0.341  0.600  yes  no      0  no
Catholic monarchy (estates and Church-crown rivalry)       0.30 0.38 0.34 0.44 0.38 0.46  0.245  0.257  yes  no      0  no
Catholic monarchy (absolutist with venal offices)          0.46 0.82 0.42 0.46 0.68 0.46  0.456  0.560  yes  yes     0  no
Secular democracy                                          0.26 0.34 0.46 0.22 0.38 0.38  0.108  0.160  yes  no      0  no
------------------------------------------------------------------------------------------------------------------------------
[counter-model] G1 accountable pluralism                   0.20 0.20 0.20 0.20 0.20 0.20  0.020  0.000  yes  no      0  no
[counter-model] G2 fused capture                           1.00 1.00 1.00 1.00 1.00 1.00  0.950  1.000  yes  yes     1  yes
A does not imply B (constructive counter-model): True
L = evidenced capture links; regime profiles carry none, so B never holds for them.

Hard cases (Theorem A check):
  Nuer ('ordered anarchy')             A=yes counterexample=no  F:informal/minimal, P:informal/minimal, J:informal/minimal, I:informal/minimal, C:informal/minimal, W:informal/minimal
  Ju/'hoansi (!Kung)                   A=yes counterexample=no  F:informal/minimal, P:informal/minimal, J:informal/minimal, I:informal/minimal, C:informal/minimal, W:informal/minimal
  Ostrom commons (design principles)   A=yes counterexample=no  F:informal/minimal, P:informal/minimal, J:informal/minimal, I:informal/minimal, C:informal/minimal, W:informal/minimal
  Consensus village (stylized)         A=yes counterexample=no  F:informal/minimal, P:informal/minimal, J:informal/minimal, I:informal/minimal, C:informal/minimal, W:informal/minimal

Dependency graph (provider -> dependent):
  derived edges only: strongly connected = True; critical edges = F->W, P->J, J->F, I->P, W->I
  derived + conditional: strongly connected = True
  six brief relations alone: strongly connected = False; sinks = ['C']

Dynamics: same positive links, rho(B+) = 1.077 (persists), rho(B+ with negative feedback) = 0.838 (decays); same positive links = True

2026-10-22T14:30:21.721872Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
2026-10-22T14:30:27.382152Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
1. **High — Proposition A incorrectly requires strong connectivity.** [`model/beast_system/necessity.py:304`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/necessity.py:304) defines `holds` as all pillars realized *and* the dependency graph strongly connected, and line 336 enforces it. Strong connectivity is explicitly an open problem, not part of Proposition A. [`model/tests/test_necessity.py:98`](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_necessity.py:98) then locks the conjectured result in as expected behavior. Connectivity should be reported separately, without affecting `holds`.

2. **High — dependency relations are not checked per governance system.** [`model/beast_system/necessity.py:326`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/necessity.py:326) always checks the global `DEPENDENCIES` constant; `GovernanceSystem` has no observed or coded dependency relations. Consequently, any system with six practices receives the same dependency result, even if none of those relations exists in that system. The falsifier test at [`model/tests/test_necessity.py:55`](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_necessity.py:55) only detects a missing pillar, not missing dependency relations.

3. **Medium — required weight sensitivity is optional and disconnected from assessment.** Although `weight_sensitivity()` exists, [`model/beast_system/capture.py:122`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/capture.py:122) permits implicit equal weights, and [`assess()` at line 158](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/capture.py:158) produces U and Proposition B without preregistered weights or a sensitivity result. The test at [`model/tests/test_indices.py:133`](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_indices.py:133) verifies the helper only in isolation.

4. **Medium — capture evidence is not tied to the polity’s actor set.** [`CaptureLink.__post_init__()`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/capture.py:48) checks only that endpoint strings are nonempty. `Polity` never verifies that `source` and `target` belong to \(V\), so an evidenced link between invented actors can make Proposition B hold. The boolean conditions are also not type-checked: truthy strings are accepted, and `holds` can return a string instead of `bool`.

5. **Medium — the threshold-parameterized non-implication constructor fails for valid boundary thresholds.** [`fused_polity()`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/capture.py:207) fixes \(U=0.95\), so `a_does_not_imply_b(CaptureThresholds(1.0, 1.0))` returns a counter-model whose `demonstrates_non_implication` is false. [`model/tests/test_capture.py:74`](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_capture.py:74) calls this “robust to thresholds” but omits the legal endpoints. The no-argument/default construction does correctly demonstrate the requested A-not-implies-B result.

6. **Low — accepted floating-point inputs can violate documented index bounds.** [`validate_weights()`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/indices.py:86) accepts sums within `1e-9` without normalization. For example, an otherwise valid vector summing to `1.0000000005` produces \(U=1.0000000005\), contradicting the promised \([0,1]\) bound. `validate_shares()` has the analogous issue. Normalize accepted vectors or bound results after tolerance-aware validation.

7. **Low — numeric validation is inconsistent.** [`CaptureThresholds.__post_init__()`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/capture.py:73) validates through `float(value)` but does not store the converted value; numeric strings therefore pass construction and later cause a `TypeError` in `proposition_b`. [`simulate()`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/dynamics.py:65) similarly omits finiteness checks for `x0`, `D`, `z`, and `noise_sd`, allowing silent NaN propagation.

The core HHI, U, 15-pair integration, Proposition B conjunction, default A-not-implies-B example, and negative-feedback spectral-radius example are otherwise indexed correctly. All 69 existing tests pass, but they do not cover the semantic and boundary failures above.

VERDICT: NEEDS_FIX
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
67,647
1. **High — Proposition A incorrectly requires strong connectivity.** [`model/beast_system/necessity.py:304`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/necessity.py:304) defines `holds` as all pillars realized *and* the dependency graph strongly connected, and line 336 enforces it. Strong connectivity is explicitly an open problem, not part of Proposition A. [`model/tests/test_necessity.py:98`](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_necessity.py:98) then locks the conjectured result in as expected behavior. Connectivity should be reported separately, without affecting `holds`.

2. **High — dependency relations are not checked per governance system.** [`model/beast_system/necessity.py:326`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/necessity.py:326) always checks the global `DEPENDENCIES` constant; `GovernanceSystem` has no observed or coded dependency relations. Consequently, any system with six practices receives the same dependency result, even if none of those relations exists in that system. The falsifier test at [`model/tests/test_necessity.py:55`](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_necessity.py:55) only detects a missing pillar, not missing dependency relations.

3. **Medium — required weight sensitivity is optional and disconnected from assessment.** Although `weight_sensitivity()` exists, [`model/beast_system/capture.py:122`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/capture.py:122) permits implicit equal weights, and [`assess()` at line 158](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/capture.py:158) produces U and Proposition B without preregistered weights or a sensitivity result. The test at [`model/tests/test_indices.py:133`](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_indices.py:133) verifies the helper only in isolation.

4. **Medium — capture evidence is not tied to the polity’s actor set.** [`CaptureLink.__post_init__()`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/capture.py:48) checks only that endpoint strings are nonempty. `Polity` never verifies that `source` and `target` belong to \(V\), so an evidenced link between invented actors can make Proposition B hold. The boolean conditions are also not type-checked: truthy strings are accepted, and `holds` can return a string instead of `bool`.

5. **Medium — the threshold-parameterized non-implication constructor fails for valid boundary thresholds.** [`fused_polity()`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/capture.py:207) fixes \(U=0.95\), so `a_does_not_imply_b(CaptureThresholds(1.0, 1.0))` returns a counter-model whose `demonstrates_non_implication` is false. [`model/tests/test_capture.py:74`](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_capture.py:74) calls this “robust to thresholds” but omits the legal endpoints. The no-argument/default construction does correctly demonstrate the requested A-not-implies-B result.

6. **Low — accepted floating-point inputs can violate documented index bounds.** [`validate_weights()`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/indices.py:86) accepts sums within `1e-9` without normalization. For example, an otherwise valid vector summing to `1.0000000005` produces \(U=1.0000000005\), contradicting the promised \([0,1]\) bound. `validate_shares()` has the analogous issue. Normalize accepted vectors or bound results after tolerance-aware validation.

7. **Low — numeric validation is inconsistent.** [`CaptureThresholds.__post_init__()`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/capture.py:73) validates through `float(value)` but does not store the converted value; numeric strings therefore pass construction and later cause a `TypeError` in `proposition_b`. [`simulate()`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/dynamics.py:65) similarly omits finiteness checks for `x0`, `D`, `z`, and `noise_sd`, allowing silent NaN propagation.

The core HHI, U, 15-pair integration, Proposition B conjunction, default A-not-implies-B example, and negative-feedback spectral-radius example are otherwise indexed correctly. All 69 existing tests pass, but they do not cover the semantic and boundary failures above.

VERDICT: NEEDS_FIX
