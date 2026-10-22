Reading additional input from stdin...
2026-10-22T17:31:40.278364Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a164ab-2800-7013-90c4-e43894e9d6c3
--------
user
Review only model/ (beast_system/, tests/, examples/). Do not explore outside model/. Output the findings list and the VERDICT line only.

Definitions the code must implement (Largo 2026 source objects plus the Part VII spec):
- Pillars M = {F, P, J, I, C, W}, M = 6, 15 pairs. Multiplex network with weights a^m_ij in [0,1]; many-to-many role map.
- Shares s^m_i >= 0 summing to 1; H_m = sum_i s^2 (monopoly 1, uniform 1/n); Q_m in [0,1]; U = sum_m w_m H_m (1 - Q_m), w >= 0, sum w = 1, with weight-sensitivity analysis; C_mn in [0,1] symmetric; I = 2/(M(M-1)) sum_{m<n} C_mn. Degree decomposition I = (sum_m deg_m)/30, deg_m = sum_{n!=m} C_mn. Hub bound: if C_mn = 0 whenever both m,n lie outside a set of k pillars, I <= (k(6-k) + k(k-1)/2)/15. Coalition overlap C_mn = max_S min(kappa_m(S), kappa_n(S)), additive kappa as special case.
- Capture link needs all of: privileged access; weakens accountability; material evidence. Proposition B: U >= u* AND I >= i* AND >= 1 capture link. a_does_not_imply_b(): two systems that both satisfy A, only one satisfies B.
- Dependencies: AND/OR hypergraph GENERATED from axioms. Hyperarc (T, h), provider(s) -> dependent, h needs AT LEAST ONE member of T. Incidence Inc(k, m) ("the problem of Ax_k arises about pillar m's inputs or rules") generates arc pillar(Ax_k) -> m. Core set D*: from Ax6, W->F, W->P, W->J, W->I, W->C; from Part III Prop 3.6, OR-hyperarc ({I,C} -> J); from Ax4 + Part I Def 2.2(b), I->F; incidence axioms X1 (Ax1 at W's inputs) F->W, X2 (Ax2 at F's rules) P->F, X3 (Ax3 at F's rules) J->F, X5 (Ax5 at F's rules) C->F. Further arcs reported, not needed: I->P, P->J, P->I (X2 + Ax4), J->P (precedent), ({F,I} -> C). Removing an axiom must remove every arc it generates. Underlying digraph replaces (T,h) by t->h. Cascade closure cl(S): least superset of S with T subset cl(S) => h in cl(S). Required results: D* underlying strongly connected and cascade-complete; D* without X5 strongly connected but cl({C}) = {C}; without X1 not strongly connected (F->W is the only arc into W); without X2 P has no out-arc, not strongly connected; replacing X3 by J->P keeps strong connectivity; splitting the OR-hyperarc wrongly adds J to cl({C}) in the no-X5 case.
- Proposition A: A.holds = all six pillars realized (from coded practices) AND D0 (W->m arcs and the OR-hyperarc) generated in the system. Interdependence (strongly connected + cascade-complete) is a separate predicate, claimed for every persistent system whose axioms include Ax1..Ax6 and X1, X2, X3, X5; a system coding an incidence as absent is the falsifier route. A persistent Ax1..Ax6 system failing A is a counterexample. Axiom-independence fixtures: for each k, Ax_k dropped and pillar k missing (antecedent false, not a counterexample), plus a consistent baseline.
- Clique bound: if one coalition S has kappa_m(S) >= c in each pillar of a k-set, I >= c k(k-1)/30; pure star around hub h gives I <= (1/3) max C. Corner polities: (U,I) = (0,0) plural Q=1; (1,1) fused one coalition Q=0; (0,1) grand coalition with equal shares in every pillar, Q=1; (1,0) a different monopolist per pillar, Q=0; all satisfy A, only (1,1) has a capture link.
- Linear dynamics x_{t+1} = B x_t + D z_t + eps; rho(B) >= 1 means some deviation does not decay; positive links do not guarantee persistence (negative-feedback example).
- Coalition conversion: y, delta in [0,1]^6; K >= 0, zero diagonal, row sums <= 1, K[n,m] = eta[n,m](1 - Q_n); T(y) = (1-delta)y + (1-y)(K y); A = diag(1-delta) + K. Claims: T maps [0,1]^6 into itself; T(y) <= A y; rho(A) < 1 => y_t -> 0; Q_n = 1, delta_n > 0 => y_n,t <= (1-delta_n)^t y_n,0 and coalition integration share asymptotically <= 10/15; rho(A) nonincreasing in each Q_n; K irreducible, max delta < 1, rho(A) > 1 => v.y_t >= min(v.y_0, (1 - max delta)(rho-1)/(2c)), v left Perron vector, c = v_max kappa / v_min^2, kappa = max column sum of K.
- Regime profiles are illustrative assumptions, not measurements; none may imply a religion is inherently captured.

Review for: correctness against these definitions, validation gaps, test coverage of each claim, whether necessity / A-not-implies-B / cascade / foothold code demonstrates what it claims, numerical issues, idiomatic style. This is round 4 (final). Round 3 raised: (P1) coalition overlap limited to additive partitions; (P2) near-symmetric C not symmetrized; (P2) hub_bound accepted non-integer k; (P2) foothold test only symmetric K and uniform delta. Verify each is fixed. List issues with file:line. End with VERDICT: PASS or VERDICT: NEEDS_FIX.
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T17:31:41.969570Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T17:31:42.737273Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
2026-10-22T17:31:47.621928Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
I’m using the code-review skill to structure this final-round audit. I’ll restrict repository inspection and all review commands to `model/`, then report only actionable findings and the verdict.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '1,240p' /Users/mlong/.codex/plugins/cache/claude-cowork/engineering/1.1.0/skills/code-review/SKILL.md" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
---
name: code-review
description: Review code for bugs, security vulnerabilities, performance issues, and maintainability. Trigger with "review this code", "check this PR", "look at this diff", "is this code safe?", or when the user shares code and asks for feedback.
---

# Code Review

Structured code review covering security, performance, correctness, and maintainability. Works on diffs, PRs, files, or pasted code snippets.

## Review Dimensions

### Security
- SQL injection, XSS, CSRF
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure deserialization
- Path traversal
- SSRF

### Performance
- N+1 queries
- Unnecessary memory allocations
- Algorithmic complexity (O(n²) in hot paths)
- Missing database indexes
- Unbounded queries or loops
- Resource leaks

### Correctness
- Edge cases (empty input, null, overflow)
- Race conditions and concurrency issues
- Error handling and propagation
- Off-by-one errors
- Type safety

### Maintainability
- Naming clarity
- Single responsibility
- Duplication
- Test coverage
- Documentation for non-obvious logic

## Output Format

Rate each dimension and provide specific, actionable findings with file and line references. Prioritize critical issues first. Always include positive observations alongside issues.

2026-10-22T17:31:53.172479Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'rg --files model | sort' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
model/beast_system/__init__.py
model/beast_system/capture.py
model/beast_system/dynamics.py
model/beast_system/indices.py
model/beast_system/necessity.py
model/beast_system/network.py
model/beast_system/pillars.py
model/beast_system/regimes.py
model/examples/run_all.py
model/pyproject.toml
model/tests/test_capture.py
model/tests/test_conversion.py
model/tests/test_dynamics_regimes.py
model/tests/test_indices.py
model/tests/test_necessity.py
model/tests/test_pillars_network.py

2026-10-22T17:31:56.163349Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'nl -ba model/pyproject.toml; nl -ba model/examples/run_all.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	[build-system]
     2	requires = ["setuptools>=61"]
     3	build-backend = "setuptools.build_meta"
     4	
     5	[project]
     6	name = "beast-system"
     7	version = "0.1.0"
     8	description = "Reference implementation of the six-pillar model (Part VII, The Formalized State)"
     9	requires-python = ">=3.10"
    10	dependencies = ["numpy>=1.23"]
    11	
    12	[project.optional-dependencies]
    13	test = ["pytest>=7"]
    14	
    15	[tool.setuptools]
    16	packages = ["beast_system"]
    17	
    18	[tool.pytest.ini_options]
    19	pythonpath = ["."]
    20	testpaths = ["tests"]
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
    17	    AXIOM_INDEPENDENCE,
    18	    BRIEF_ARCS,
    19	    D0_KEYS,
    20	    D_STAR_KEYS,
    21	    FURTHER_RULES,
    22	    HARD_CASES,
    23	    arc_key,
    24	    cascade_closure,
    25	    check_proposition_a,
    26	    critical_edges,
    27	    generate_dependencies,
    28	    is_cascade_complete,
    29	    is_strongly_connected,
    30	    sinks_and_sources,
    31	    underlying_digraph,
    32	    without_axiom,
    33	)
    34	from beast_system.pillars import PILLARS, IncidenceAxiom, Pillar  # noqa: E402
    35	from beast_system.regimes import regime_profiles  # noqa: E402
    36	
    37	
    38	def _yn(flag: bool) -> str:
    39	    return "yes" if flag else "no"
    40	
    41	
    42	def _row(label: str, a: Assessment) -> str:
    43	    hs = " ".join(f"{a.H[m]:.2f}" for m in PILLARS)
    44	    b = a.prop_b
    45	    return (f"{label:<58} {hs}  {a.U:.3f}  {a.I:.3f}  {_yn(a.prop_a.holds):<3}  "
    46	            f"{_yn(b.thresholds_met):<6}  {a.u_high_fraction:.2f}  {b.n_links}  {_yn(b.holds)}")
    47	
    48	
    49	def main() -> None:
    50	    th = CaptureThresholds()
    51	    head_h = " ".join(f"H_{m.name:<3}" for m in PILLARS)
    52	    header = (f"{'profile':<58} {head_h} U      I      A    U,I>=*  P(U>=u*)  L  B")
    53	    print(f"Thresholds u* = {th.u_star}, i* = {th.i_star}. "
    54	          "Regime values: ILLUSTRATIVE ASSUMPTIONS, not measurements.")
    55	    print(header)
    56	    print("-" * len(header))
    57	    for prof in regime_profiles():
    58	        print(_row(prof.label, assess(prof.polity, th)))
    59	    print("-" * len(header))
    60	    cm = a_does_not_imply_b(th)
    61	    print(_row("[counter-model] " + cm.plural.name, cm.plural))
    62	    print(_row("[counter-model] " + cm.fused.name, cm.fused))
    63	    print(f"A does not imply B (constructive counter-model): {cm.demonstrates_non_implication}")
    64	    print("P(U>=u*) = share of 2000 uniform weight draws with U >= u* (weight sensitivity).")
    65	    print("L = evidenced capture links; regime profiles carry none, so B never holds for them.")
    66	
    67	    print("\nHard cases (Theorem A check):")
    68	    for sys_ in HARD_CASES:
    69	        r = check_proposition_a(sys_)
    70	        forms = ", ".join(f"{d.pillar.name}:{d.form}" for d in r.derivations.values())
    71	        print(f"  {sys_.name:<36} A={_yn(r.holds)} counterexample={_yn(r.counterexample)} "
    72	              f"interdependent={_yn(r.interdependent)}  {forms}")
    73	
    74	    print("\nAxiom independence models (Ax_k dropped, pillar k absent):")
    75	    for ax, sys_ in AXIOM_INDEPENDENCE.items():
    76	        r = check_proposition_a(sys_)
    77	        print(f"  without {ax.name}: missing={sorted(m.name for m in r.missing)} "
    78	              f"antecedent={_yn(r.antecedent)} counterexample={_yn(r.counterexample)}")
    79	
    80	    print("\nGenerated dependency hypergraph (provider -> dependent; OR-hyperarc {I,C}->J):")
    81	    precedent = next(r for r in FURTHER_RULES if r.premise == "precedent (Hart)")
    82	    cases = [("D0", D0_KEYS), ("D* (Ax1..Ax6 + X1,X2,X3,X5)", D_STAR_KEYS)]
    83	    cases += [(f"D* without {x.name}", generate_dependencies(without_axiom(x)))
    84	              for x in IncidenceAxiom]
    85	    cases.append(("D* with X3 replaced by J->P",
    86	                  (D_STAR_KEYS - {arc_key(Pillar.J, Pillar.F)}) | {precedent.key}))
    87	    for label, arcs in cases:
    88	        print(f"  {label:<30} strongly connected = "
    89	              f"{is_strongly_connected(underlying_digraph(arcs))!s:<5}; cascade-complete = "
    90	              f"{is_cascade_complete(arcs)!s:<5}; cl({{C}}) = "
    91	              f"{''.join(sorted(m.name for m in cascade_closure(arcs, {Pillar.C})))}")
    92	    print("  critical arcs of D*: "
    93	          + ", ".join(f"{u.name}->{v.name}" for u, v in critical_edges(underlying_digraph(D_STAR_KEYS))))
    94	    brief = underlying_digraph(BRIEF_ARCS)
    95	    sinks, _ = sinks_and_sources(brief)
    96	    print(f"  six brief relations alone: strongly connected = {is_strongly_connected(brief)}; "
    97	          f"sinks = {sorted(m.name for m in sinks)}")
    98	
    99	    fb = negative_feedback_example()
   100	    print("\nDynamics: same positive links, rho(B+) = "
   101	          f"{fb.rho_positive:.3f} (some deviation persists), rho(B+ with negative feedback) = "
   102	          f"{fb.rho_feedback:.3f} (decays); same positive links = {fb.same_positive_links}")
   103	
   104	
   105	if __name__ == "__main__":
   106	    main()

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/capture.py; nl -ba model/beast_system/necessity.py' in /Users/mlong/Documents/Development/the-beast-system
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
    17	    WeightSensitivity,
    18	    coalition_integration,
    19	    control_shares,
    20	    hhi,
    21	    integration_statistic,
    22	    unaccountable_concentration,
    23	    validate_integration_matrix,
    24	    validate_unit_interval,
    25	    validate_weights,
    26	    weight_sensitivity,
    27	)
    28	from .necessity import (
    29	    GovernanceSystem,
    30	    PropositionAResult,
    31	    check_proposition_a,
    32	    formal_system,
    33	    role_map,
    34	)
    35	from .network import MultiplexNetwork
    36	from .pillars import PILLARS, Pillar
    37	
    38	
    39	@dataclass(frozen=True)
    40	class CaptureLink:
    41	    """Capture link (i -> j, m) (source Section 5; notation.md 'Capture link').
    42	
    43	    All three conditions are required: (i) privileged access or discretion; (ii) the privilege
    44	    weakens otherwise applicable accountability or contestability; (iii) material evidence
    45	    links the asymmetry to an institutional output. A disclosure-compliant donor meeting is
    46	    not automatically capture. Claiming (iii) requires citing the evidence.
    47	    """
    48	
    49	    source: str
    50	    target: str
    51	    pillar: Pillar
    52	    privileged_access: bool
    53	    weakens_accountability: bool
    54	    material_evidence: bool
    55	    evidence: str = ""
    56	
    57	    def __post_init__(self) -> None:
    58	        for end in (self.source, self.target):
    59	            if not isinstance(end, str) or not end:
    60	                raise ValueError("capture link endpoints must be named")
    61	        if not isinstance(self.pillar, Pillar):
    62	            raise TypeError("capture link pillar must be a Pillar")
    63	        for flag in ("privileged_access", "weakens_accountability", "material_evidence"):
    64	            if not isinstance(getattr(self, flag), bool):
    65	                raise TypeError(f"{flag} must be a bool")
    66	        if not isinstance(self.evidence, str):
    67	            raise TypeError("evidence must be a string")
    68	        if self.material_evidence and not self.evidence.strip():
    69	            raise ValueError("condition (iii) requires a citation of the material evidence")
    70	
    71	    @property
    72	    def holds(self) -> bool:
    73	        return self.privileged_access and self.weakens_accountability and self.material_evidence
    74	
    75	
    76	def is_capture_link(link: CaptureLink) -> bool:
    77	    """Conjunction of the source's three conditions."""
    78	    return link.holds
    79	
    80	
    81	@dataclass(frozen=True)
    82	class CaptureThresholds:
    83	    """Thresholds u*, i* for Proposition B. Illustrative defaults; preregister in applications."""
    84	
    85	    u_star: float = 0.4
    86	    i_star: float = 0.5
    87	
    88	    def __post_init__(self) -> None:
    89	        object.__setattr__(self, "u_star", validate_unit_interval(self.u_star, "u_star"))
    90	        object.__setattr__(self, "i_star", validate_unit_interval(self.i_star, "i_star"))
    91	
    92	
    93	@dataclass(frozen=True)
    94	class PropositionBResult:
    95	    u_high: bool
    96	    i_high: bool
    97	    n_links: int
    98	
    99	    @property
   100	    def thresholds_met(self) -> bool:
   101	        return self.u_high and self.i_high
   102	
   103	    @property
   104	    def holds(self) -> bool:
   105	        return self.thresholds_met and self.n_links > 0
   106	
   107	
   108	def proposition_b(
   109	    U: float,
   110	    I: float,  # noqa: E741  (integration statistic, math cal I)
   111	    links: tuple[CaptureLink, ...] | list[CaptureLink],
   112	    thresholds: CaptureThresholds = CaptureThresholds(),
   113	) -> PropositionBResult:
   114	    """Proposition B: U >= u* AND I >= i* AND some capture link holds."""
   115	    U = validate_unit_interval(U, "U")
   116	    I = validate_unit_interval(I, "I")  # noqa: E741
   117	    return PropositionBResult(
   118	        u_high=U >= thresholds.u_star,
   119	        i_high=I >= thresholds.i_star,
   120	        n_links=sum(1 for link in links if is_capture_link(link)),
   121	    )
   122	
   123	
   124	@dataclass(frozen=True)
   125	class Polity:
   126	    """A coded polity: governance system (for A) plus index inputs (for B).
   127	
   128	    ``shares[m]`` holds raw non-negative control weights per actor, normalized to s^m.
   129	    ``weights`` are the preregistered U weights (None means the equal-weight preregistration
   130	    1/M); ``assess`` always adds a weight-sensitivity analysis. Capture-link endpoints must be
   131	    actors of the polity (share holders or holders of coded practices).
   132	    """
   133	
   134	    name: str
   135	    system: GovernanceSystem
   136	    shares: Mapping[Pillar, Mapping[str, float]]
   137	    contestability: Mapping[Pillar, float]
   138	    integration: np.ndarray
   139	    capture_links: tuple[CaptureLink, ...] = ()
   140	    weights: Mapping[Pillar, float] | None = None
   141	    normalized_shares: Mapping[Pillar, Mapping[str, float]] = field(init=False, repr=False)
   142	
   143	    def __post_init__(self) -> None:
   144	        if set(self.shares) != set(PILLARS):
   145	            raise ValueError("shares must cover every pillar")
   146	        norm = {m: control_shares(self.shares[m]) for m in PILLARS}
   147	        object.__setattr__(self, "normalized_shares", norm)
   148	        object.__setattr__(self, "integration", validate_integration_matrix(self.integration))
   149	        object.__setattr__(self, "weights", validate_weights(self.weights))
   150	        links = tuple(self.capture_links)
   151	        if any(not isinstance(link, CaptureLink) for link in links):
   152	            raise TypeError("capture_links must be CaptureLink instances")
   153	        actors = self.actors
   154	        for link in links:
   155	            for end in (link.source, link.target):
   156	                if end not in actors:
   157	                    raise ValueError(f"capture link endpoint {end!r} is not an actor of {self.name}")
   158	        object.__setattr__(self, "capture_links", links)
   159	        # Fail early on bad Q.
   160	        unaccountable_concentration(self.H, self.contestability, self.weights)
   161	
   162	    @property
   163	    def actors(self) -> frozenset[str]:
   164	        """V: every share holder plus every holder of a coded practice."""
   165	        held = {a for m in PILLARS for a in self.shares[m]}
   166	        return frozenset(held | set(role_map(self.system)))
   167	
   168	    @property
   169	    def H(self) -> dict[Pillar, float]:  # noqa: N802
   170	        return {m: hhi(self.normalized_shares[m]) for m in PILLARS}
   171	
   172	    @property
   173	    def U(self) -> float:  # noqa: N802
   174	        return unaccountable_concentration(self.H, self.contestability, self.weights)
   175	
   176	    @property
   177	    def I(self) -> float:  # noqa: E743, N802
   178	        return integration_statistic(self.integration)
   179	
   180	
   181	@dataclass(frozen=True)
   182	class Assessment:
   183	    name: str
   184	    H: dict[Pillar, float]
   185	    U: float
   186	    I: float  # noqa: E741
   187	    prop_a: PropositionAResult
   188	    prop_b: PropositionBResult
   189	    sensitivity: WeightSensitivity
   190	    u_star: float
   191	
   192	    @property
   193	    def u_high_fraction(self) -> float:
   194	        """Share of weight draws with U >= u*: robustness of the U side of Proposition B."""
   195	        return self.sensitivity.fraction_at_least(self.u_star)
   196	
   197	
   198	def assess(
   199	    polity: Polity,
   200	    thresholds: CaptureThresholds = CaptureThresholds(),
   201	    n_draws: int = 2000,
   202	    seed: int = 0,
   203	) -> Assessment:
   204	    """Evaluate Proposition A, Proposition B and the weight sensitivity of U on one polity."""
   205	    return Assessment(
   206	        name=polity.name,
   207	        H=polity.H,
   208	        U=polity.U,
   209	        I=polity.I,
   210	        prop_a=check_proposition_a(polity.system),
   211	        prop_b=proposition_b(polity.U, polity.I, polity.capture_links, thresholds),
   212	        sensitivity=weight_sensitivity(polity.H, polity.contestability, polity.weights,
   213	                                       n_draws=n_draws, seed=seed),
   214	        u_star=thresholds.u_star,
   215	    )
   216	
   217	
   218	# Counter-model: A does not imply B --------------------------------------------------------
   219	
   220	
   221	def _layer_from(holders: list[str], actors: list[str], weight: float) -> np.ndarray:
   222	    idx = {a: k for k, a in enumerate(actors)}
   223	    arr = np.zeros((len(actors), len(actors)))
   224	    for h in holders:
   225	        for a in actors:
   226	            if a != h:
   227	                arr[idx[h], idx[a]] = weight
   228	    return arr
   229	
   230	
   231	def plural_polity(n_per_pillar: int = 5, q: float = 0.9) -> Polity:
   232	    """G1, accountable pluralism: each pillar held by n independent organizations.
   233	
   234	    Holders are disjoint across pillars, so every coalition overlap is 0 and C_mn = 0.
   235	    """
   236	    if n_per_pillar < 1:
   237	        raise ValueError("n_per_pillar must be positive")
   238	    q = validate_unit_interval(q, "q")
   239	    holders = {m: [f"{m.label}-org-{k}" for k in range(n_per_pillar)] for m in PILLARS}
   240	    actors = [a for m in PILLARS for a in holders[m]]
   241	    net = MultiplexNetwork(
   242	        actors=tuple(actors),
   243	        layers={m: _layer_from(holders[m], actors, 0.5) for m in PILLARS},
   244	        roles={a: {m} for m in PILLARS for a in holders[m]},
   245	    )
   246	    shares = {m: net.out_strength_shares(m) for m in PILLARS}
   247	    return Polity(
   248	        name="G1 accountable pluralism",
   249	        system=formal_system("G1 accountable pluralism", holders),
   250	        shares=shares,
   251	        contestability={m: q for m in PILLARS},
   252	        integration=coalition_integration(shares),
   253	    )
   254	
   255	
   256	def fused_polity(n_subordinate: int = 5, q: float = 0.0) -> Polity:
   257	    """G2, fused capture: one coalition holds all six pillars with Q = q, one evidenced link.
   258	
   259	    H_m = 1 and C_mn = 1, so U = 1 - q and I = 1; with the default q = 0 both indices reach
   260	    their maximum and meet every admissible threshold pair (u*, i*) in [0, 1]^2.
   261	    """
   262	    if n_subordinate < 1:
   263	        raise ValueError("n_subordinate must be positive")
   264	    q = validate_unit_interval(q, "q")
   265	    core = "ruling coalition"
   266	    actors = [core] + [f"subordinate-{k}" for k in range(n_subordinate)]
   267	    net = MultiplexNetwork(
   268	        actors=tuple(actors),
   269	        layers={m: _layer_from([core], actors, 1.0) for m in PILLARS},
   270	        roles={core: set(PILLARS)},
   271	    )
   272	    shares = {m: net.out_strength_shares(m) for m in PILLARS}
   273	    link = CaptureLink(
   274	        source=core, target="subordinate-0", pillar=Pillar.J,
   275	        privileged_access=True, weakens_accountability=True, material_evidence=True,
   276	        evidence="synthetic: appointment record ties removal of reviewing judges to ruling",
   277	    )
   278	    return Polity(
   279	        name="G2 fused capture",
   280	        system=formal_system("G2 fused capture", {m: [core] for m in PILLARS}),
   281	        shares=shares,
   282	        contestability={m: q for m in PILLARS},
   283	        integration=coalition_integration(shares),
   284	        capture_links=(link,),
   285	    )
   286	
   287	
   288	@dataclass(frozen=True)
   289	class CounterModel:
   290	    plural: Assessment
   291	    fused: Assessment
   292	
   293	    @property
   294	    def demonstrates_non_implication(self) -> bool:
   295	        """Both satisfy A; only G2 satisfies B. Hence A does not imply B."""
   296	        return (
   297	            self.plural.prop_a.holds
   298	            and self.fused.prop_a.holds
   299	            and not self.plural.prop_b.holds
   300	            and self.fused.prop_b.holds
   301	        )
   302	
   303	
   304	def a_does_not_imply_b(thresholds: CaptureThresholds = CaptureThresholds()) -> CounterModel:
   305	    """Constructive counter-model for Part VII Theorem 2 (KB Section 4.3 item 4).
   306	
   307	    G1 has U = (1/5)(1 - 0.9) = 0.02, I = 0 and no capture link; G2 has U = 1, I = 1 and one
   308	    evidenced link. Both pass the Theorem A check (six pillars realized, D0 generated) and
   309	    both are interdependent, so interdependence does not imply capture either. G1 fails B for every thresholds pair because it has no link (and its indices lie
   310	    below any u* > 0.02, i* > 0); G2 meets B for every thresholds pair in [0, 1]^2.
   311	    """
   312	    return CounterModel(
   313	        plural=assess(plural_polity(), thresholds),
   314	        fused=assess(fused_polity(), thresholds),
   315	    )
   316	
   317	
   318	# Corner attainability (Part VII addendum item 9) --------------------------------------------
   319	
   320	
   321	def grand_coalition_polity(n_members: int = 5) -> Polity:
   322	    """(U, I) = (0, 1): one consensus coalition holds every pillar in equal shares, Q = 1."""
   323	    if n_members < 1:
   324	        raise ValueError("n_members must be positive")
   325	    members = [f"member-{k}" for k in range(n_members)]
   326	    shares = {m: {a: 1.0 / n_members for a in members} for m in PILLARS}
   327	    return Polity(
   328	        name="consensus grand coalition",
   329	        system=formal_system("consensus grand coalition", {m: members for m in PILLARS}),
   330	        shares=shares,
   331	        contestability={m: 1.0 for m in PILLARS},
   332	        integration=coalition_integration(shares, {a: "grand coalition" for a in members}),
   333	    )
   334	
   335	
   336	def separate_monopolies_polity() -> Polity:
   337	    """(U, I) = (1, 0): a different monopolist per pillar, Q = 0, no shared coalition."""
   338	    holders = {m: [f"{m.label} monopolist"] for m in PILLARS}
   339	    shares = {m: {holders[m][0]: 1.0} for m in PILLARS}
   340	    return Polity(
   341	        name="separate monopolies",
   342	        system=formal_system("separate monopolies", holders),
   343	        shares=shares,
   344	        contestability={m: 0.0 for m in PILLARS},
   345	        integration=coalition_integration(shares),
   346	    )
   347	
   348	
   349	def corner_polities() -> dict[tuple[int, int], Polity]:
   350	    """Four polities satisfying A that attain the corners of the (U, I) square.
   351	
   352	    Only the (1, 1) corner carries a capture link, so U and I alone never decide B.
   353	    """
   354	    return {
   355	        (0, 0): plural_polity(q=1.0),
   356	        (1, 1): fused_polity(q=0.0),
   357	        (0, 1): grand_coalition_polity(),
   358	        (1, 0): separate_monopolies_polity(),
   359	    }
     1	"""Structural necessity: Proposition A and the pillar dependency hypergraph (Part VII Theorem A).
     2	
     3	Theorem A (notation.md CENTRAL THESIS; KB Section 4): if a governance system G persists and
     4	satisfies Ax1..Ax6, then every pillar in M is implemented in G, and the dependency relations
     5	D0 are present. Implementation is role-level, not institution-level
     6	(Hempel 1959): a function may be held by a formal institution, fused with other functions
     7	inside one institution, or exercised informally (gossip and shunning as C, mediators as J).
     8	
     9	What this module does and does not do. It cannot prove Theorem A. It encodes the lemma schema
    10	'Ax_k + persistence => some practice solves problem_k' and checks it against coded cases. The
    11	role map is DERIVED from independently coded practices, never declared, so a persistent case
    12	that satisfies all six axioms yet has no practice for some problem, or lacks a D0 relation, is
    13	reported as a counterexample (the falsifier required by KB Section 4.4).
    14	
    15	Dependencies form an AND/OR hypergraph GENERATED from the axioms (Part VII revised dependency
    16	spec). A hyperarc (T, h) is written provider(s) -> dependent and means: h needs an output of
    17	AT LEAST ONE member of T. Incidence Inc(k, m), 'the problem of Ax_k arises about the inputs or
    18	rules of pillar m', generates the arc pillar(k) -> m. The core set D* comes from Ax6 (W -> m),
    19	Part III Prop 3.6 ({I, C} -> J), Ax4 with Part I Def 2.2(b) (I -> F), and the incidence axioms
    20	X1 (F -> W), X2 (P -> F), X3 (J -> F), X5 (C -> F). Removing an axiom removes every arc it
    21	generates. Two connectivity notions are computed:
    22	  (a) the underlying digraph (each (T, h) replaced by arcs t -> h) is strongly connected;
    23	  (b) cascade completeness: cl({n}) = M for every n, where cl(S) is the least superset of S
    24	      such that T subset of cl(S) implies h in cl(S) for every hyperarc (T, h).
    25	Interdependence = (a) and (b). It is a separate predicate from Theorem A's Struct(G) and is
    26	claimed for every system satisfying the extended axiom set; a system coding an incidence as
    27	absent while its premises hold is reported as an interdependence counterexample.
    28	"""
    29	
    30	from __future__ import annotations
    31	
    32	from collections.abc import Iterable, Mapping
    33	from dataclasses import dataclass, field
    34	from typing import Literal
    35	
    36	from .pillars import AXIOM_TO_PILLAR, PILLAR_TO_AXIOM, PILLARS, Axiom, IncidenceAxiom, Pillar
    37	
    38	RealizedForm = Literal["formal institution", "fused", "informal/minimal"]
    39	FORMAL: RealizedForm = "formal institution"
    40	FUSED: RealizedForm = "fused"
    41	INFORMAL: RealizedForm = "informal/minimal"
    42	
    43	# Dependency hypergraph primitives ----------------------------------------------------------
    44	
    45	#: A hyperarc key (T, h): tail set T, head h.
    46	ArcKey = tuple[frozenset[Pillar], Pillar]
    47	Graph = Mapping[Pillar, Iterable[Pillar]]
    48	AnyAxiom = Axiom | IncidenceAxiom
    49	
    50	#: Ax1..Ax6 plus the incidence axioms X1, X2, X3, X5 (Part VII extended axiom set).
    51	EXTENDED_AXIOMS: frozenset[AnyAxiom] = frozenset(Axiom) | frozenset(IncidenceAxiom)
    52	
    53	
    54	def arc_key(tail: Pillar | Iterable[Pillar], head: Pillar) -> ArcKey:
    55	    """Normalize (T, h) to an ArcKey, validating T non-empty, h a Pillar and h not in T."""
    56	    t = frozenset((tail,) if isinstance(tail, Pillar) else tail)
    57	    if not t or not all(isinstance(m, Pillar) for m in t) or not isinstance(head, Pillar):
    58	        raise TypeError("a hyperarc needs a non-empty tail of Pillars and a Pillar head")
    59	    if head in t:
    60	        raise ValueError(f"head {head.name} may not belong to its own tail")
    61	    return t, head
    62	
    63	
    64	def _keys(arcs: Iterable[DependencyRule | ArcKey]) -> frozenset[ArcKey]:
    65	    return frozenset(a.key if isinstance(a, DependencyRule) else arc_key(*a) for a in arcs)
    66	
    67	
    68	def underlying_digraph(arcs: Iterable[DependencyRule | ArcKey]) -> dict[Pillar, frozenset[Pillar]]:
    69	    """Replace each hyperarc (T, h) by the arcs t -> h; adjacency over all six pillars."""
    70	    adj: dict[Pillar, set[Pillar]] = {m: set() for m in PILLARS}
    71	    for tail, head in _keys(arcs):
    72	        for t in tail:
    73	            adj[t].add(head)
    74	    return {m: frozenset(v) for m, v in adj.items()}
    75	
    76	
    77	def cascade_closure(
    78	    arcs: Iterable[DependencyRule | ArcKey], start: Iterable[Pillar]
    79	) -> frozenset[Pillar]:
    80	    """cl(S): least superset of S with T subset of cl(S) => h in cl(S) for every (T, h).
    81	
    82	    Read as a failure cascade: h fails once every provider in its tail has failed.
    83	    """
    84	    keys = _keys(arcs)
    85	    closed = set(start)
    86	    changed = True
    87	    while changed:
    88	        changed = False
    89	        for tail, head in keys:
    90	            if head not in closed and tail <= closed:
    91	                closed.add(head)
    92	                changed = True
    93	    return frozenset(closed)
    94	
    95	
    96	def is_cascade_complete(
    97	    arcs: Iterable[DependencyRule | ArcKey], nodes: Iterable[Pillar] = PILLARS
    98	) -> bool:
    99	    """True iff cl({n}) contains every node, for every node n (restricted to ``nodes``)."""
   100	    keep = frozenset(nodes)
   101	    if not keep:
   102	        return False
   103	    inside = [(t, h) for t, h in _keys(arcs) if h in keep and t <= keep]
   104	    return all(cascade_closure(inside, {n}) >= keep for n in keep)
   105	
   106	
   107	def _nodes(graph: Graph) -> set[Pillar]:
   108	    nodes = set(graph)
   109	    for targets in graph.values():
   110	        nodes.update(targets)
   111	    return nodes
   112	
   113	
   114	def _reach(graph: Mapping[Pillar, frozenset[Pillar]], start: Pillar) -> set[Pillar]:
   115	    seen = {start}
   116	    stack = [start]
   117	    while stack:
   118	        for nxt in graph.get(stack.pop(), frozenset()):
   119	            if nxt not in seen:
   120	                seen.add(nxt)
   121	                stack.append(nxt)
   122	    return seen
   123	
   124	
   125	def is_strongly_connected(graph: Graph, nodes: Iterable[Pillar] | None = None) -> bool:
   126	    """True iff every node of the graph is reachable from every other node.
   127	
   128	    ``nodes`` restricts the graph to an induced subgraph (default: all nodes that appear).
   129	    The empty graph is not strongly connected; a single node is.
   130	    """
   131	    keep = set(nodes) if nodes is not None else _nodes(graph)
   132	    if not keep:
   133	        return False
   134	    fwd: dict[Pillar, frozenset[Pillar]] = {
   135	        u: frozenset(v for v in graph.get(u, ()) if v in keep) for u in keep
   136	    }
   137	    rev: dict[Pillar, set[Pillar]] = {u: set() for u in keep}
   138	    for u, vs in fwd.items():
   139	        for v in vs:
   140	            rev[v].add(u)
   141	    start = next(iter(keep))
   142	    rev_f = {u: frozenset(v) for u, v in rev.items()}
   143	    return _reach(fwd, start) == keep and _reach(rev_f, start) == keep
   144	
   145	
   146	def critical_edges(graph: Graph) -> list[tuple[Pillar, Pillar]]:
   147	    """Edges whose single removal breaks strong connectivity (empty if not connected)."""
   148	    nodes = _nodes(graph)
   149	    base = {u: frozenset(graph.get(u, ())) for u in nodes}
   150	    if not is_strongly_connected(base):
   151	        return []
   152	    out = []
   153	    for u in PILLARS:
   154	        for v in sorted(base.get(u, ()), key=lambda p: p.position):
   155	            pruned = dict(base)
   156	            pruned[u] = base[u] - {v}
   157	            if not is_strongly_connected(pruned, nodes):
   158	                out.append((u, v))
   159	    return out
   160	
   161	
   162	def sinks_and_sources(graph: Graph) -> tuple[frozenset[Pillar], frozenset[Pillar]]:
   163	    """Pillars with no outgoing edge (sinks) and with no incoming edge (sources)."""
   164	    nodes = _nodes(graph)
   165	    has_out = {u for u in nodes if any(True for _ in graph.get(u, ()))}
   166	    has_in = {v for u in nodes for v in graph.get(u, ())}
   167	    return frozenset(nodes - has_out), frozenset(nodes - has_in)
   168	
   169	
   170	# Axiom-generated dependency rules (Part VII revised dependency spec) ----------------------
   171	
   172	
   173	@dataclass(frozen=True)
   174	class DependencyRule:
   175	    """A hyperarc (T, h) generated when every premise in ``requires`` holds.
   176	
   177	    h needs an output of AT LEAST ONE member of T (provider(s) -> dependent). ``incidence`` is
   178	    the incidence Inc(k, m) the rule instantiates (the problem of Ax_k arises about pillar m's
   179	    inputs or rules, giving arc pillar(k) -> m), or None for a rule that is not an incidence.
   180	    ``core`` marks membership of D*; non-core rules are reported, not needed.
   181	    """
   182	
   183	    tail: frozenset[Pillar]
   184	    head: Pillar
   185	    premise: str
   186	    requires: frozenset[AnyAxiom]
   187	    source: str
   188	    core: bool
   189	    incidence: tuple[Axiom, Pillar] | None = None
   190	
   191	    def __post_init__(self) -> None:
   192	        tail, _ = arc_key(self.tail, self.head)
   193	        requires = frozenset(self.requires)
   194	        if not requires or any(not isinstance(a, (Axiom, IncidenceAxiom)) for a in requires):
   195	            raise ValueError("a dependency rule needs at least one axiom premise")
   196	        if self.incidence is not None:
   197	            axiom, target = self.incidence
   198	            if tail != frozenset({axiom.pillar}) or target is not self.head:
   199	                raise ValueError("an incidence Inc(k, m) generates exactly pillar(k) -> m")
   200	            if axiom not in requires:
   201	                raise ValueError("an incidence rule must require its own axiom")
   202	        object.__setattr__(self, "tail", tail)
   203	        object.__setattr__(self, "requires", requires)
   204	
   205	    @property
   206	    def key(self) -> ArcKey:
   207	        return self.tail, self.head
   208	
   209	
   210	def _inc(axiom: Axiom, target: Pillar, premise: str, requires: Iterable[AnyAxiom],
   211	         source: str, core: bool = True) -> DependencyRule:
   212	    return DependencyRule(frozenset({axiom.pillar}), target, premise,
   213	                          frozenset(requires) | {axiom}, source, core, (axiom, target))
   214	
   215	
   216	_P, _A, _X = Pillar, Axiom, IncidenceAxiom
   217	
   218	#: D*: the core rules. Under Ax1..Ax6 plus X1, X2, X3, X5 they generate a strongly connected,
   219	#: cascade-complete hypergraph (Part VII revised dependency spec).
   220	CORE_RULES: tuple[DependencyRule, ...] = (
   221	    *(_inc(_A.Ax6, m, "Ax6", (), "practitioners consume produced resources (Part VI)")
   222	      for m in (_P.F, _P.P, _P.J, _P.I, _P.C)),
   223	    DependencyRule(frozenset({_P.I, _P.C}), _P.J, "Part III Prop 3.6",
   224	                   frozenset({_A.Ax3, _A.Ax4, _A.Ax5}),
   225	                   "rulings settle disputes if recognized or if enforced", core=True),
   226	    _inc(_A.Ax4, _P.F, "Ax4 + Part I Def 2.2(b)", (),
   227	         "members must anticipate the settlement procedure"),
   228	    _inc(_A.Ax1, _P.W, "X1", (_X.X1,), "contested productive inputs (Part I)"),
   229	    _inc(_A.Ax2, _P.F, "X2", (_X.X2,), "changing environment hits allocation rules (Part II Ass 3.2)"),
   230	    _inc(_A.Ax3, _P.F, "X3", (_X.X3,), "open-textured allocation rules (Part III Thm 3.3)"),
   231	    _inc(_A.Ax5, _P.F, "X5", (_X.X5,), "tempting allocation rules (Part V Thm 3.4)"),
   232	)
   233	
   234	#: Further rules: reported, not needed for interdependence. Each rests on a premise beyond
   235	#: the extended axiom set (stated in ``premise``), so none is generated for a system.
   236	FURTHER_RULES: tuple[DependencyRule, ...] = (
   237	    _inc(_A.Ax4, _P.P, "X2 + Ax4", (_A.Ax2, _X.X2), "recognition of rule change", core=False),
   238	    _inc(_A.Ax2, _P.J, "X2 + Ax4", (_A.Ax4, _X.X2), "new rules to interpret", core=False),
   239	    _inc(_A.Ax2, _P.I, "X2 + Ax4", (_A.Ax4, _X.X2), "new rules to be made common knowledge",
   240	         core=False),
   241	    _inc(_A.Ax3, _P.P, "precedent (Hart)", (), "interpretation feeds rule change", core=False),
   242	    DependencyRule(frozenset({_P.F, _P.I}), _P.C, "Part V Cor 3.7 conditions",
   243	                   frozenset({_A.Ax1, _A.Ax4, _A.Ax5}),
   244	                   "costly public-good sanctions at large n, no higher-order sanctions",
   245	                   core=False),
   246	)
   247	
   248	D_STAR_KEYS: frozenset[ArcKey] = frozenset(r.key for r in CORE_RULES)
   249	#: D0: the relations Theorem A requires (W -> m for m != W, and the OR-hyperarc {I, C} -> J).
   250	D0_KEYS: frozenset[ArcKey] = frozenset(
   251	    r.key for r in CORE_RULES if r.premise in {"Ax6", "Part III Prop 3.6"}
   252	)
   253	
   254	#: The six single arcs named in the original model brief (kept for comparison only).
   255	BRIEF_ARCS: frozenset[ArcKey] = frozenset(
   256	    arc_key(t, h) for t, h in [(_P.W, _P.C), (_P.P, _P.J), (_P.I, _P.P), (_P.J, _P.F),
   257	                               (_P.F, _P.W), (_P.W, _P.I)]
   258	)
   259	
   260	
   261	def rules_holding(
   262	    axioms: Iterable[AnyAxiom], rules: Iterable[DependencyRule] = CORE_RULES
   263	) -> tuple[DependencyRule, ...]:
   264	    """The rules whose premises all hold under ``axioms``."""
   265	    held = frozenset(axioms)
   266	    return tuple(r for r in rules if r.requires <= held)
   267	
   268	
   269	def dependency_graph(axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS) -> dict[Pillar, frozenset[Pillar]]:
   270	    """Underlying digraph of the core rules generated under ``axioms`` (default: all)."""
   271	    return underlying_digraph(rules_holding(axioms))
   272	
   273	
   274	# Governance systems ------------------------------------------------------------------------
   275	
   276	
   277	@dataclass(frozen=True)
   278	class Practice:
   279	    """A regular activity that discharges the problem generated by axiom ``solves``.
   280	
   281	    ``formal`` is True when the activity is attached to a designated office or organization.
   282	    ``source`` holds the citation key(s) supporting the coding.
   283	    """
   284	
   285	    description: str
   286	    solves: Axiom
   287	    holders: frozenset[str]
   288	    formal: bool = False
   289	    source: str = ""
   290	
   291	    def __post_init__(self) -> None:
   292	        if not isinstance(self.solves, Axiom):
   293	            raise TypeError("Practice.solves must be an Axiom")
   294	        holders = frozenset(self.holders)
   295	        if not holders or any(not isinstance(h, str) or not h for h in holders):
   296	            raise ValueError("a practice needs at least one named holder")
   297	        if not self.description.strip():
   298	            raise ValueError("a practice needs a description")
   299	        object.__setattr__(self, "holders", holders)
   300	
   301	    @property
   302	    def pillar(self) -> Pillar:
   303	        return AXIOM_TO_PILLAR[self.solves]
   304	
   305	
   306	@dataclass(frozen=True)
   307	class GovernanceSystem:
   308	    """A collective that makes and enforces collective decisions (KB Section 4.1).
   309	
   310	    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
   311	    over the period studied; it may include the incidence axioms X1, X2, X3, X5. Both are
   312	    coded independently of ``practices``. Dependencies are generated from ``axioms``;
   313	    ``absent_incidences`` records incidences Inc(k, m) OBSERVED not to arise in this system,
   314	    which suppress the arcs they would generate (the route by which a case can falsify D0 or
   315	    interdependence).
   316	    """
   317	
   318	    name: str
   319	    persistent: bool
   320	    axioms: frozenset[AnyAxiom]
   321	    practices: tuple[Practice, ...] = ()
   322	    absent_incidences: frozenset[tuple[Axiom, Pillar]] = frozenset()
   323	    note: str = ""
   324	
   325	    def __post_init__(self) -> None:
   326	        if not isinstance(self.persistent, bool):
   327	            raise TypeError("persistent must be a bool")
   328	        axioms = frozenset(self.axioms)
   329	        if any(not isinstance(a, (Axiom, IncidenceAxiom)) for a in axioms):
   330	            raise TypeError("axioms must be Axiom or IncidenceAxiom members")
   331	        practices = tuple(self.practices)
   332	        if any(not isinstance(p, Practice) for p in practices):
   333	            raise TypeError("practices must be Practice instances")
   334	        object.__setattr__(self, "axioms", axioms)
   335	        object.__setattr__(self, "practices", practices)
   336	        absent = frozenset(tuple(i) for i in self.absent_incidences)
   337	        if any(len(i) != 2 or not isinstance(i[0], Axiom) or not isinstance(i[1], Pillar)
   338	               for i in absent):
   339	            raise TypeError("absent_incidences must be (Axiom, Pillar) pairs")
   340	        object.__setattr__(self, "absent_incidences", absent)
   341	
   342	    def holds(self, axiom: AnyAxiom) -> bool:
   343	        """Predicate for one axiom (Ax1..Ax6 or an incidence axiom X_k)."""
   344	        return axiom in self.axioms
   345	
   346	    @property
   347	    def all_axioms_hold(self) -> bool:
   348	        """Ax1..Ax6 all hold (the antecedent of Theorem A)."""
   349	        return all(self.holds(a) for a in Axiom)
   350	
   351	    @property
   352	    def extended_axioms_hold(self) -> bool:
   353	        """Ax1..Ax6 and X1, X2, X3, X5 all hold (the antecedent of interdependence)."""
   354	        return EXTENDED_AXIOMS <= self.axioms
   355	
   356	
   357	def generate_dependencies(
   358	    system: GovernanceSystem, rules: Iterable[DependencyRule] = CORE_RULES
   359	) -> frozenset[ArcKey]:
   360	    """Hyperarcs generated in ``system``: rules whose premises hold, minus absent incidences."""
   361	    return frozenset(
   362	        r.key for r in rules_holding(system.axioms, rules)
   363	        if r.incidence is None or r.incidence not in system.absent_incidences
   364	    )
   365	
   366	
   367	def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
   368	    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
   369	    roles: dict[str, set[Pillar]] = {}
   370	    for p in system.practices:
   371	        for h in p.holders:
   372	            roles.setdefault(h, set()).add(p.pillar)
   373	    return {h: frozenset(ps) for h, ps in roles.items()}
   374	
   375	
   376	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   377	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   378	
   379	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   380	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   381	    """
   382	    practices = [p for p in system.practices if p.pillar is pillar]
   383	    if not practices:
   384	        return None
   385	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   386	    if not formal_holders:
   387	        return INFORMAL
   388	    formal_roles: dict[str, set[Pillar]] = {}
   389	    for p in system.practices:
   390	        if p.formal:
   391	            for h in p.holders:
   392	                formal_roles.setdefault(h, set()).add(p.pillar)
   393	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   394	        return FUSED
   395	    return FORMAL
   396	
   397	
   398	@dataclass(frozen=True)
   399	class Derivation:
   400	    """Result of the lemma for one axiom: required pillar and its realized form."""
   401	
   402	    axiom: Axiom
   403	    pillar: Pillar
   404	    form: RealizedForm | None
   405	    practices: tuple[Practice, ...]
   406	
   407	    @property
   408	    def realized(self) -> bool:
   409	        return self.form is not None
   410	
   411	
   412	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   413	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   414	
   415	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   416	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   417	    """
   418	    out: dict[Axiom, Derivation] = {}
   419	    for axiom in Axiom:
   420	        if not system.holds(axiom):
   421	            continue
   422	        pillar = AXIOM_TO_PILLAR[axiom]
   423	        out[axiom] = Derivation(
   424	            axiom=axiom,
   425	            pillar=pillar,
   426	            form=realized_form(system, pillar),
   427	            practices=tuple(p for p in system.practices if p.solves is axiom),
   428	        )
   429	    return out
   430	
   431	
   432	# Proposition A and interdependence --------------------------------------------------------
   433	
   434	
   435	@dataclass(frozen=True)
   436	class PropositionAResult:
   437	    """Outcome of checking Theorem A and interdependence on one coded system.
   438	
   439	    ``holds`` is Struct(G): all six pillars realized AND every D0 relation generated.
   440	    ``counterexample`` is True when Theorem A's antecedent holds (persistent, Ax1..Ax6) but
   441	    Struct(G) fails.
   442	
   443	    ``interdependent`` is the separate structural predicate: all six pillars realized and the
   444	    generated hypergraph both strongly connected (underlying digraph) and cascade-complete.
   445	    ``interdependence_counterexample`` is True when the system is persistent, satisfies the
   446	    extended axiom set, yet is not interdependent.
   447	    """
   448	
   449	    system: str
   450	    antecedent: bool
   451	    realized: frozenset[Pillar]
   452	    missing: frozenset[Pillar]
   453	    dependencies: frozenset[ArcKey]
   454	    missing_dependencies: frozenset[ArcKey]
   455	    strongly_connected: bool
   456	    cascade_complete: bool
   457	    holds: bool
   458	    interdependence_antecedent: bool
   459	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   460	
   461	    @property
   462	    def counterexample(self) -> bool:
   463	        return self.antecedent and not self.holds
   464	
   465	    @property
   466	    def interdependent(self) -> bool:
   467	        return not self.missing and self.strongly_connected and self.cascade_complete
   468	
   469	    @property
   470	    def interdependence_counterexample(self) -> bool:
   471	        return self.interdependence_antecedent and not self.interdependent
   472	
   473	
   474	def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
   475	    """Check Theorem A and interdependence on ``system`` (Part VII; KB Section 4.3).
   476	
   477	    A D0 relation is demanded when its head and every tail member are realized.
   478	    """
   479	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   480	    deps = generate_dependencies(system)
   481	    needed = frozenset((t, h) for t, h in D0_KEYS if h in realized and t <= realized)
   482	    missing_deps = needed - deps
   483	    return PropositionAResult(
   484	        system=system.name,
   485	        antecedent=system.persistent and system.all_axioms_hold,
   486	        realized=realized,
   487	        missing=frozenset(PILLARS) - realized,
   488	        dependencies=deps,
   489	        missing_dependencies=missing_deps,
   490	        strongly_connected=is_strongly_connected(underlying_digraph(deps), realized),
   491	        cascade_complete=is_cascade_complete(deps, realized),
   492	        holds=realized == frozenset(PILLARS) and not missing_deps,
   493	        interdependence_antecedent=system.persistent and system.extended_axioms_hold,
   494	        derivations=derive_functions(system),
   495	    )
   496	
   497	
   498	def formal_system(
   499	    name: str,
   500	    holders: Mapping[Pillar, Iterable[str]],
   501	    persistent: bool = True,
   502	    source: str = "",
   503	    axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS,
   504	) -> GovernanceSystem:
   505	    """A persistent system whose pillars are held by formal organizations.
   506	
   507	    An actor listed under several pillars is fused. By default the extended axiom set is
   508	    coded as holding: an assumption of the stylized model, not an observation. Used for regime
   509	    profiles and counter-models.
   510	    """
   511	    practices = tuple(
   512	        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
   513	                 frozenset(hs), formal=True, source=source)
   514	        for m, hs in holders.items()
   515	        if hs
   516	    )
   517	    return GovernanceSystem(name, persistent, frozenset(axioms), practices)
   518	
   519	
   520	# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
   521	# Each codes the extended axiom set as holding. For X1, X2, X3, X5 this is a coding
   522	# assumption with the falsifier stated on IncidenceAxiom; e.g. Nuer grazing and herds and
   523	# Ju/'hoansi n!ore territories are contested inputs (X1).
   524	
   525	
   526	def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
   527	    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)
   528	
   529	
   530	NUER = GovernanceSystem(
   531	    name="Nuer ('ordered anarchy')",
   532	    persistent=True,
   533	    axioms=EXTENDED_AXIOMS,
   534	    practices=(
   535	        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
   536	                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
   537	        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
   538	                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
   539	        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
   540	                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
   541	        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
   542	                  {"prophets", "lineages"}, "evanspritchard1940"),
   543	        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
   544	                  {"agnatic kin"}, "evanspritchard1940"),
   545	        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
   546	                  "evanspritchard1940"),
   547	    ),
   548	    note="no office holds coercive authority; functions exist without separation",
   549	)
   550	
   551	JU_HOANSI = GovernanceSystem(
   552	    name="Ju/'hoansi (!Kung)",
   553	    persistent=True,
   554	    axioms=EXTENDED_AXIOMS,
   555	    practices=(
   556	        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
   557	                  {"hunters", "camp members"}, "lee2013; marshall1976"),
   558	        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
   559	                  {"camp members"}, "lee2013"),
   560	        _informal("disputes talked out with kin mediators", Axiom.Ax3,
   561	                  {"kin mediators"}, "lee1979; wiessner2005"),
   562	        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
   563	                  {"healers", "camp members"}, "marshall1976"),
   564	        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
   565	                  {"camp members"}, "wiessner2005; lee2013"),
   566	        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
   567	    ),
   568	    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
   569	)
   570	
   571	OSTROM_COMMONS = GovernanceSystem(
   572	    name="Ostrom commons (design principles)",
   573	    persistent=True,
   574	    axioms=EXTENDED_AXIOMS,
   575	    practices=(
   576	        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
   577	                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
   578	        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
   579	                  {"appropriators"}, "ostrom1990"),
   580	        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
   581	                  {"appropriators"}, "ostrom1990; cox2010"),
   582	        _informal("shared norms; minimal recognition of rights to organize (DP7)",
   583	                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),
   584	        _informal("monitoring and graduated sanctions by appropriators (DP4, DP5)",
   585	                  Axiom.Ax5, {"appropriators"}, "ostrom1990; cox2010"),
   586	        _informal("appropriation and maintenance labor", Axiom.Ax6, {"appropriators"},
   587	                  "ostrom1990"),
   588	    ),
   589	    note="checks in minimal form; monitors are appropriators or accountable to them",
   590	)
   591	
   592	CONSENSUS_VILLAGE = GovernanceSystem(
   593	    name="Consensus village (stylized)",
   594	    persistent=True,
   595	    axioms=EXTENDED_AXIOMS,
   596	    practices=(
   597	        _informal("household plots; reciprocal labor exchange; sharing norms", Axiom.Ax1,
   598	                  {"households"}, "sahlins1972"),
   599	        _informal("consensus meeting of adults", Axiom.Ax2, {"village meeting"},
   600	                  "clastres1987; boehm1999"),
   601	        _informal("elders mediate disputes", Axiom.Ax3, {"elders"}, "boehm1999"),
   602	        _informal("ritual and myth; moral talk", Axiom.Ax4, {"village meeting", "elders"},
   603	                  "boehm1999"),
   604	        _informal("gossip, shunning, ostracism of would-be dominants", Axiom.Ax5,
   605	                  {"village meeting"}, "boehm1999; woodburn1982"),
   606	        _informal("gardening and household labor", Axiom.Ax6, {"households"},
   607	                  "sahlins1972"),
   608	    ),
   609	    note="stylized composite; reverse dominance hierarchy",
   610	)
   611	
   612	HARD_CASES: tuple[GovernanceSystem, ...] = (NUER, JU_HOANSI, OSTROM_COMMONS, CONSENSUS_VILLAGE)
   613	
   614	
   615	# Axiom independence fixtures (Part VII spec, item 7). ---------------------------------------
   616	
   617	#: Consistency model: the extended axiom set holds and all six pillars are realized (the
   618	#: consensus village coding).
   619	BASELINE_MODEL: GovernanceSystem = CONSENSUS_VILLAGE
   620	
   621	
   622	def without_axiom(axiom: AnyAxiom, base: GovernanceSystem = BASELINE_MODEL) -> GovernanceSystem:
   623	    """``base`` with one axiom removed; for Ax_k the practices solving Ax_k are removed too."""
   624	    practices = base.practices
   625	    if isinstance(axiom, Axiom):
   626	        practices = tuple(p for p in practices if p.solves is not axiom)
   627	    return GovernanceSystem(
   628	        name=f"{base.name} without {axiom.name} ({axiom.label})",
   629	        persistent=base.persistent,
   630	        axioms=base.axioms - {axiom},
   631	        practices=practices,
   632	        absent_incidences=base.absent_incidences,
   633	        note="hypothetical: one axiom removed",
   634	    )
   635	
   636	
   637	#: For each k: persistent, Ax_k removed, pillar k missing. Theorem A's antecedent is false,
   638	#: so none is a counterexample; each shows pillar k is not forced by the other five axioms.
   639	AXIOM_INDEPENDENCE: dict[Axiom, GovernanceSystem] = {a: without_axiom(a) for a in Axiom}

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/pillars.py; nl -ba model/beast_system/network.py; nl -ba model/beast_system/indices.py' in /Users/mlong/Documents/Development/the-beast-system
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
   106	
   107	
   108	class IncidenceAxiom(Enum):
   109	    """Incidence axioms X_k (Part VII revised dependency spec).
   110	
   111	    X_k states that the problem of Ax_k arises about the inputs or rules of a named pillar,
   112	    which generates the arc pillar(Ax_k) -> that pillar. Each is an empirical premise with a
   113	    stated falsifier, not a logical truth.
   114	    """
   115	
   116	    X1 = "contested inputs"
   117	    X2 = "changing environment"
   118	    X3 = "open-textured allocation rules"
   119	    X5 = "tempting allocation rules"
   120	
   121	    @property
   122	    def label(self) -> str:
   123	        return self.value
   124	
   125	    @property
   126	    def base(self) -> Axiom:
   127	        """The axiom whose problem the incidence locates."""
   128	        return _INCIDENCE[self][0]
   129	
   130	    @property
   131	    def target(self) -> Pillar:
   132	        """The pillar whose inputs or rules the problem arises about."""
   133	        return _INCIDENCE[self][1]
   134	
   135	    @property
   136	    def statement(self) -> str:
   137	        return _INCIDENCE[self][2]
   138	
   139	    @property
   140	    def falsifier(self) -> str:
   141	        return _INCIDENCE[self][3]
   142	
   143	
   144	_INCIDENCE: dict[IncidenceAxiom, tuple[Axiom, Pillar, str, str]] = {
   145	    IncidenceAxiom.X1: (
   146	        Axiom.Ax1, Pillar.W,
   147	        "productive inputs (land, territory, herds, tools) are objects of conflicting claims",
   148	        "a persistent collective whose productive inputs never meet conflicting claims",
   149	    ),
   150	    IncidenceAxiom.X2: (
   151	        Axiom.Ax2, Pillar.F,
   152	        "the environment changes, so allocation rules must sometimes be revised collectively",
   153	        "a persistent collective whose allocation rules never change",
   154	    ),
   155	    IncidenceAxiom.X3: (
   156	        Axiom.Ax3, Pillar.F,
   157	        "allocation rules have open texture and leave residual disputes",
   158	        "allocation rules that settle every case without dispute",
   159	    ),
   160	    IncidenceAxiom.X5: (
   161	        Axiom.Ax5, Pillar.F,
   162	        "some allocation rule is tempting to break (p > theta)",
   163	        "no member is ever tempted to take more than the allocation rule grants",
   164	    ),
   165	}
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
    33	    if isinstance(value, bool) or not isinstance(value, (int, float, np.integer, np.floating)):
    34	        raise TypeError(f"{name} must be a real number, got {type(value).__name__}")
    35	    v = float(value)
    36	    if not math.isfinite(v) or v < 0.0 or v > 1.0:
    37	        raise ValueError(f"{name} must lie in [0, 1], got {value!r}")
    38	    return v
    39	
    40	
    41	def _share_array(shares: ShareLike) -> np.ndarray:
    42	    values = list(shares.values()) if isinstance(shares, Mapping) else shares
    43	    arr = np.asarray(values, dtype=float).ravel()
    44	    if arr.size == 0:
    45	        raise ValueError("shares must be non-empty")
    46	    if not np.all(np.isfinite(arr)):
    47	        raise ValueError("shares must be finite")
    48	    if arr.min() < 0.0:
    49	        raise ValueError("shares must be non-negative")
    50	    return arr
    51	
    52	
    53	def control_shares(raw: Mapping[str, float]) -> dict[str, float]:
    54	    """Normalize non-negative control weights to shares s^m_i summing to 1 (notation.md)."""
    55	    arr = _share_array(raw)
    56	    scale = float(arr.max())
    57	    if scale <= 0.0:
    58	        raise ValueError("at least one control weight must be positive")
    59	    scaled = arr / scale  # in [0, 1], so the sum cannot overflow
    60	    total = float(scaled.sum())
    61	    return {k: float(v) / total for k, v in zip(raw, scaled)}
    62	
    63	
    64	def validate_shares(shares: ShareLike, atol: float = SHARE_ATOL) -> np.ndarray:
    65	    """Check s^m_i >= 0 and sum_i s^m_i = 1 (notation.md 'Control share').
    66	
    67	    Returns the shares renormalized to sum exactly 1, so rounding within ``atol`` cannot push
    68	    H outside [1/n, 1].
    69	    """
    70	    arr = _share_array(shares)
    71	    total = float(arr.sum())
    72	    if abs(total - 1.0) > atol:
    73	        raise ValueError(f"shares must sum to 1, got {total:.12g}")
    74	    return arr / total
    75	
    76	
    77	def hhi(shares: ShareLike) -> float:
    78	    """H_m = sum_i (s^m_i)^2 (source Eq. for H_{m,t}). Lies in [1/n, 1]."""
    79	    arr = validate_shares(shares)
    80	    return float(np.dot(arr, arr))
    81	
    82	
    83	def normalized_hhi(shares: ShareLike) -> float:
    84	    """H* = (H - 1/n) / (1 - 1/n), for comparing polities with different n (KB VII.3 (v)).
    85	
    86	    Not in the source. Defined as 1 for n = 1 (a monopoly by construction).
    87	    """
    88	    arr = validate_shares(shares)
    89	    n = arr.size
    90	    if n == 1:
    91	        return 1.0
    92	    return float((np.dot(arr, arr) - 1.0 / n) / (1.0 - 1.0 / n))
    93	
    94	
    95	def validate_weights(weights: Mapping[Pillar, float] | None) -> dict[Pillar, float]:
    96	    """Check the U weights: one per pillar, w_m >= 0, sum_m w_m = 1 (source Eq. U_t).
    97	
    98	    ``None`` gives equal weights 1/M.
    99	    """
   100	    if weights is None:
   101	        return {m: 1.0 / M for m in PILLARS}
   102	    if set(weights) != set(PILLARS):
   103	        raise ValueError("weights must give exactly one value per pillar")
   104	    w = {m: float(weights[m]) for m in PILLARS}
   105	    if any(not math.isfinite(v) or v < 0.0 for v in w.values()):
   106	        raise ValueError("weights must be finite and non-negative")
   107	    total = sum(w.values())
   108	    if abs(total - 1.0) > WEIGHT_ATOL:
   109	        raise ValueError(f"weights must sum to 1, got {total:.12g}")
   110	    return {m: v / total for m, v in w.items()}
   111	
   112	
   113	def _per_pillar(values: Mapping[Pillar, float], name: str) -> dict[Pillar, float]:
   114	    if set(values) != set(PILLARS):
   115	        raise ValueError(f"{name} must give exactly one value per pillar")
   116	    return {m: validate_unit_interval(values[m], f"{name}[{m.name}]") for m in PILLARS}
   117	
   118	
   119	def unaccountable_concentration(
   120	    H: Mapping[Pillar, float],
   121	    Q: Mapping[Pillar, float],
   122	    weights: Mapping[Pillar, float] | None = None,
   123	) -> float:
   124	    """U = sum_m w_m H_m (1 - Q_m) (source Eq. U_t). Lies in [0, 1].
   125	
   126	    U = 0 iff Q_m = 1 for every m with w_m > 0, because H_m >= 1/n > 0 (KB VII.3 (ii)).
   127	    """
   128	    h = _per_pillar(H, "H")
   129	    if any(v == 0.0 for v in h.values()):
   130	        raise ValueError("H_m >= 1/n > 0 for any valid share vector; got H_m = 0")
   131	    q = _per_pillar(Q, "Q")
   132	    w = validate_weights(weights)
   133	    u = sum(w[m] * h[m] * (1.0 - q[m]) for m in PILLARS)
   134	    return float(min(max(u, 0.0), 1.0))  # guard against last-ulp rounding
   135	
   136	
   137	def validate_integration_matrix(C: np.ndarray, atol: float = 1e-12) -> np.ndarray:
   138	    """Check C is 6x6, finite, symmetric, with off-diagonal C_mn in [0, 1].
   139	
   140	    The diagonal is unused by the integration statistic; by convention it is set to 1.
   141	    """
   142	    arr = np.array(C, dtype=float)
   143	    if arr.shape != (M, M):
   144	        raise ValueError(f"integration matrix must be {M}x{M}, got {arr.shape}")
   145	    if not np.all(np.isfinite(arr)):
   146	        raise ValueError("integration matrix must be finite")
   147	    if not np.allclose(arr, arr.T, atol=atol, rtol=0.0):
   148	        raise ValueError("integration matrix must be symmetric (C_mn = C_nm)")
   149	    off = arr[~np.eye(M, dtype=bool)]
   150	    if off.min() < 0.0 or off.max() > 1.0:
   151	        raise ValueError("off-diagonal C_mn must lie in [0, 1]")
   152	    arr = (arr + arr.T) / 2.0  # exact symmetry, so both triangles agree
   153	    np.fill_diagonal(arr, 1.0)
   154	    return arr
   155	
   156	
   157	def integration_matrix(
   158	    pairs: Mapping[tuple[Pillar, Pillar], float], default: float = 0.0
   159	) -> np.ndarray:
   160	    """Build a symmetric C from {(m, n): C_mn}; unspecified pairs take ``default``."""
   161	    validate_unit_interval(default, "default")
   162	    arr = np.full((M, M), float(default))
   163	    seen: set[frozenset[Pillar]] = set()
   164	    for (m, n), value in pairs.items():
   165	        if m == n:
   166	            raise ValueError(f"pair ({m.name}, {n.name}) is not a cross-pillar pair")
   167	        key = frozenset((m, n))
   168	        if key in seen:
   169	            raise ValueError(f"pair {m.name}{n.name} given twice")
   170	        seen.add(key)
   171	        v = validate_unit_interval(value, f"C[{m.name}{n.name}]")
   172	        arr[m.position, n.position] = arr[n.position, m.position] = v
   173	    np.fill_diagonal(arr, 1.0)
   174	    return arr
   175	
   176	
   177	def integration_statistic(C: np.ndarray) -> float:
   178	    """I = 2 / (M (M - 1)) sum_{m<n} C_mn with M = 6, i.e. the mean over 15 pairs (source Eq. I_t)."""
   179	    arr = validate_integration_matrix(C)
   180	    total = sum(arr[m.position, n.position] for m, n in PAIRS)
   181	    return float(2.0 / (M * (M - 1)) * total)
   182	
   183	
   184	def integration_degrees(C: np.ndarray) -> dict[Pillar, float]:
   185	    """deg_m = sum_{n != m} C_mn, so that I = (sum_m deg_m) / 30 (Part VII spec, item 5)."""
   186	    arr = validate_integration_matrix(C)
   187	    return {m: float(arr[m.position].sum() - arr[m.position, m.position]) for m in PILLARS}
   188	
   189	
   190	def hub_bound(k: int) -> float:
   191	    """Upper bound on I when every C_mn with both m, n outside a hub set of k pillars is 0.
   192	
   193	    Only pairs touching the hub can be non-zero: k(6 - k) + k(k - 1)/2 of the 15 pairs.
   194	    k = 1 gives 1/3, k = 2 gives 0.6, k = 3 gives 0.8.
   195	    """
   196	    if isinstance(k, bool) or not isinstance(k, (int, np.integer)):
   197	        raise TypeError("k must be an integer")
   198	    if not 0 <= k <= M:
   199	        raise ValueError(f"k must lie in 0..{M}")
   200	    return (k * (M - k) + k * (k - 1) / 2) / 15.0
   201	
   202	
   203	def coalition_overlap(kappa: Mapping[str, Mapping[Pillar, float]]) -> np.ndarray:
   204	    """C_mn = max over candidate coalitions S of min(kappa_m(S), kappa_n(S)) (Part II eq. overlap).
   205	
   206	    ``kappa[S][m]`` in [0, 1] is coalition S's control of pillar m; pillars missing for S
   207	    count as 0. Candidate coalitions may overlap and kappa need not be additive. The result
   208	    lies in [0, 1] and is weakly increasing in every kappa_m(S).
   209	    """
   210	    arr = np.eye(M)
   211	    if not kappa:
   212	        return arr
   213	    table: list[dict[Pillar, float]] = []
   214	    for name, row in kappa.items():
   215	        if any(not isinstance(m, Pillar) for m in row):
   216	            raise TypeError(f"kappa[{name!r}] keys must be Pillars")
   217	        table.append({m: validate_unit_interval(row.get(m, 0.0), f"kappa[{name!r}][{m.name}]")
   218	                      for m in PILLARS})
   219	    for m, n in PAIRS:
   220	        v = max(min(row[m], row[n]) for row in table)
   221	        arr[m.position, n.position] = arr[n.position, m.position] = v
   222	    return arr
   223	
   224	
   225	def coalition_integration(
   226	    shares: Mapping[Pillar, Mapping[str, float]],
   227	    coalition_of: Mapping[str, str] | None = None,
   228	) -> np.ndarray:
   229	    """Additive special case of ``coalition_overlap`` for a partition of actors into coalitions.
   230	
   231	    kappa_m(S) = s^m(S), the summed (normalized) share of S's members in pillar m. The source
   232	    describes C_mn only verbally ('the same coalition commands appointments, budgets,
   233	    sanctions or agenda in both m and n'); KB VII.3 (iv) asks Part VII to define it. Actors
   234	    absent from ``coalition_of`` form singleton coalitions.
   235	    """
   236	    coalition_of = dict(coalition_of or {})
   237	    kappa: dict[str, dict[Pillar, float]] = {}
   238	    for m in PILLARS:
   239	        if m not in shares:
   240	            raise ValueError(f"shares missing pillar {m.name}")
   241	        actors = list(shares[m])
   242	        normalized = validate_shares(shares[m])
   243	        for actor, v in zip(actors, normalized):
   244	            row = kappa.setdefault(coalition_of.get(actor, actor), {})
   245	            row[m] = min(row.get(m, 0.0) + float(v), 1.0)
   246	    return coalition_overlap(kappa)
   247	
   248	
   249	def clique_lower_bound(c: float, k: int) -> float:
   250	    """If one coalition has kappa_m(S) >= c in each of k pillars, then I >= c k (k - 1) / 30.
   251	
   252	    Those k pillars form k(k - 1)/2 pairs with C_mn >= c (Part VII addendum item 8).
   253	    """
   254	    c = validate_unit_interval(c, "c")
   255	    if isinstance(k, bool) or not isinstance(k, (int, np.integer)) or not 0 <= k <= M:
   256	        raise ValueError(f"k must be an integer in 0..{M}")
   257	    return c * k * (k - 1) / 30.0
   258	
   259	
   260	def star_upper_bound(C: np.ndarray, hub: Pillar) -> float:
   261	    """Bound (1/3) max C_mn for a pure star: every positive C_mn involves ``hub``.
   262	
   263	    Raises if the matrix is not a star around ``hub``.
   264	    """
   265	    arr = validate_integration_matrix(C)
   266	    for m, n in PAIRS:
   267	        if hub not in (m, n) and arr[m.position, n.position] > 0.0:
   268	            raise ValueError(f"C_{m.name}{n.name} > 0 does not involve hub {hub.name}")
   269	    off = arr[~np.eye(M, dtype=bool)]
   270	    return float(off.max()) / 3.0
   271	
   272	
   273	@dataclass(frozen=True)
   274	class WeightSensitivity:
   275	    """Result of ``weight_sensitivity``. ``draws`` holds U for each sampled weight vector."""
   276	
   277	    baseline: float
   278	    vertex_min: float
   279	    vertex_max: float
   280	    draws: np.ndarray
   281	
   282	    @property
   283	    def quantiles(self) -> tuple[float, float]:
   284	        """5th and 95th percentile of U across draws."""
   285	        lo, hi = np.quantile(self.draws, [0.05, 0.95])
   286	        return float(lo), float(hi)
   287	
   288	    def fraction_at_least(self, u_star: float) -> float:
   289	        """Share of weight draws with U >= u_star (robustness of a threshold call)."""
   290	        validate_unit_interval(u_star, "u_star")
   291	        return float(np.mean(self.draws >= u_star))
   292	
   293	
   294	def weight_sensitivity(
   295	    H: Mapping[Pillar, float],
   296	    Q: Mapping[Pillar, float],
   297	    weights: Mapping[Pillar, float] | None = None,
   298	    n_draws: int = 2000,
   299	    seed: int = 0,
   300	) -> WeightSensitivity:
   301	    """Sensitivity of U to the weights w (source: 'weights preregistered; sensitivity analysis').
   302	
   303	    U is linear in w, so over the whole weight simplex its exact range is
   304	    [min_m H_m (1 - Q_m), max_m H_m (1 - Q_m)] (attained at the vertices). ``draws`` samples
   305	    w uniformly on the simplex (Dirichlet(1, ..., 1)) to show the typical spread.
   306	    """
   307	    if n_draws < 1:
   308	        raise ValueError("n_draws must be positive")
   309	    baseline = unaccountable_concentration(H, Q, weights)
   310	    h = _per_pillar(H, "H")
   311	    q = _per_pillar(Q, "Q")
   312	    terms = np.array([h[m] * (1.0 - q[m]) for m in PILLARS])
   313	    rng = np.random.default_rng(seed)
   314	    w = rng.dirichlet(np.ones(M), size=n_draws)
   315	    return WeightSensitivity(
   316	        baseline=baseline,
   317	        vertex_min=float(terms.min()),
   318	        vertex_max=float(terms.max()),
   319	        draws=(w * terms).sum(axis=1),
   320	    )

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/dynamics.py; nl -ba model/beast_system/regimes.py; nl -ba model/beast_system/__init__.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Linear pillar-capacity dynamics x_{t+1} = B x_t + D z_t + eps_t (source Section 5.3).
     2	
     3	x_t = (F_t, P_t, J_t, I^cap_t, C_t, W_t) in pillar order. The source warns that stability
     4	cannot be inferred from positive links alone (negative feedback, substitution, saturation,
     5	legitimacy loss) and uses dominant eigenvalues of a local linearization as the language of
     6	persistence. Every deviation of x from its steady state decays iff the spectral radius
     7	rho(B) < 1; if rho(B) >= 1 SOME deviation (e.g. along a dominant eigenvector) does not decay,
     8	although a deviation inside a stable subspace still may.
     9	
    10	The second half implements coalition conversion dynamics (Part VII spec, item 4): a
    11	coalition's control shares y in [0,1]^6 evolve by T(y) = (1 - delta) y + (1 - y) (K y).
    12	"""
    13	
    14	from __future__ import annotations
    15	
    16	from collections.abc import Mapping
    17	from dataclasses import dataclass
    18	
    19	import numpy as np
    20	
    21	from .necessity import Graph, dependency_graph
    22	from .pillars import M, Pillar
    23	
    24	
    25	def _square(B: np.ndarray) -> np.ndarray:
    26	    arr = np.asarray(B, dtype=float)
    27	    if arr.shape != (M, M):
    28	        raise ValueError(f"B must be {M}x{M}, got {arr.shape}")
    29	    if not np.all(np.isfinite(arr)):
    30	        raise ValueError("B must be finite")
    31	    return arr
    32	
    33	
    34	def spectral_radius(B: np.ndarray) -> float:
    35	    """rho(B) = max |lambda| over eigenvalues of B."""
    36	    return float(np.max(np.abs(np.linalg.eigvals(_square(B)))))
    37	
    38	
    39	def some_deviation_persists(B: np.ndarray) -> bool:
    40	    """True iff rho(B) >= 1: x = 0 is not globally asymptotically stable for x -> B x.
    41	
    42	    Then some deviation does not decay; it does not follow that EVERY deviation persists.
    43	    """
    44	    return spectral_radius(B) >= 1.0
    45	
    46	
    47	def dependency_matrix(graph: Graph, weight: float, self_weight: float = 0.0) -> np.ndarray:
    48	    """B with B[dependent, provider] = weight for each edge, and self_weight on the diagonal.
    49	
    50	    Row = pillar at t+1, column = pillar at t, matching x_{t+1} = B x_t.
    51	    """
    52	    B = np.eye(M) * float(self_weight)
    53	    for provider, dependents in graph.items():
    54	        for dep in dependents:
    55	            B[dep.position, provider.position] = float(weight)
    56	    return B
    57	
    58	
    59	def simulate(
    60	    B: np.ndarray,
    61	    x0: np.ndarray,
    62	    steps: int,
    63	    D: np.ndarray | None = None,
    64	    z: np.ndarray | None = None,
    65	    noise_sd: float = 0.0,
    66	    seed: int | None = None,
    67	) -> np.ndarray:
    68	    """Iterate x_{t+1} = B x_t + D z_t + eps_t; returns an array of shape (steps + 1, 6).
    69	
    70	    ``z`` has shape (steps, k) and ``D`` shape (6, k); eps_t ~ N(0, noise_sd^2 I).
    71	    """
    72	    B = _square(B)
    73	    x = np.asarray(x0, dtype=float)
    74	    if x.shape != (M,):
    75	        raise ValueError(f"x0 must have shape ({M},)")
    76	    if steps < 0:
    77	        raise ValueError("steps must be non-negative")
    78	    if (D is None) != (z is None):
    79	        raise ValueError("pass both D and z, or neither")
    80	    if D is not None and z is not None:
    81	        D = np.asarray(D, dtype=float)
    82	        z = np.asarray(z, dtype=float)
    83	        if D.ndim != 2 or D.shape[0] != M or z.shape != (steps, D.shape[1]):
    84	            raise ValueError("D must be (6, k) and z must be (steps, k)")
    85	    if not np.all(np.isfinite(x)):
    86	        raise ValueError("x0 must be finite")
    87	    if D is not None and z is not None and not (np.all(np.isfinite(D)) and np.all(np.isfinite(z))):
    88	        raise ValueError("D and z must be finite")
    89	    noise_sd = float(noise_sd)
    90	    if not np.isfinite(noise_sd) or noise_sd < 0.0:
    91	        raise ValueError("noise_sd must be finite and non-negative")
    92	    rng = np.random.default_rng(seed)
    93	    path = np.empty((steps + 1, M))
    94	    path[0] = x
    95	    for t in range(steps):
    96	        x = B @ x
    97	        if D is not None and z is not None:
    98	            x = x + D @ z[t]
    99	        if noise_sd > 0.0:
   100	            x = x + rng.normal(0.0, noise_sd, size=M)
   101	        path[t + 1] = x
   102	    return path
   103	
   104	
   105	@dataclass(frozen=True)
   106	class FeedbackExample:
   107	    """Two matrices with the same positive links; only the feedback one has negative entries."""
   108	
   109	    B_positive: np.ndarray
   110	    B_feedback: np.ndarray
   111	    rho_positive: float
   112	    rho_feedback: float
   113	
   114	    @property
   115	    def same_positive_links(self) -> bool:
   116	        return bool(np.array_equal(self.B_positive > 0, self.B_feedback > 0))
   117	
   118	
   119	#: Negative feedback entries (provider, dependent) -> weight: coercion erodes legitimacy and
   120	#: depresses productive effort (source Section 5.3, 'legitimacy loss'). Illustrative values.
   121	NEGATIVE_FEEDBACK: Mapping[tuple[Pillar, Pillar], float] = {
   122	    (Pillar.C, Pillar.I): -0.5,
   123	    (Pillar.C, Pillar.W): -0.4,
   124	}
   125	
   126	
   127	def negative_feedback_example(
   128	    weight: float = 0.25,
   129	    self_weight: float = 0.6,
   130	    feedback: Mapping[tuple[Pillar, Pillar], float] = NEGATIVE_FEEDBACK,
   131	) -> FeedbackExample:
   132	    """Positive dependency links do not guarantee persistence (source Section 5.3).
   133	
   134	    With every arc of the underlying digraph of D* at ``weight`` and ``self_weight`` on the
   135	    diagonal, rho > 1. Adding negative feedback on entries that carry no positive link leaves every
   136	    positive link unchanged yet pushes rho below 1, so deviations decay.
   137	    """
   138	    B_pos = dependency_matrix(dependency_graph(), weight, self_weight)
   139	    B_fb = B_pos.copy()
   140	    for (provider, dependent), w in feedback.items():
   141	        if w >= 0.0:
   142	            raise ValueError("feedback entries must be negative")
   143	        if B_pos[dependent.position, provider.position] != 0.0:
   144	            raise ValueError("feedback must not overwrite a positive link")
   145	        B_fb[dependent.position, provider.position] = w
   146	    return FeedbackExample(B_pos, B_fb, spectral_radius(B_pos), spectral_radius(B_fb))
   147	
   148	
   149	# Coalition conversion dynamics (Part VII spec, item 4) -------------------------------------
   150	
   151	
   152	def _unit_vector(v: np.ndarray, name: str) -> np.ndarray:
   153	    arr = np.asarray(v, dtype=float)
   154	    if arr.shape != (M,):
   155	        raise ValueError(f"{name} must have shape ({M},)")
   156	    if not np.all(np.isfinite(arr)) or arr.min() < 0.0 or arr.max() > 1.0:
   157	        raise ValueError(f"{name} entries must lie in [0, 1]")
   158	    return arr
   159	
   160	
   161	def validate_conversion_matrix(K: np.ndarray, atol: float = 1e-12) -> np.ndarray:
   162	    """Check K >= 0, zero diagonal, row sums <= 1 (so T maps [0,1]^6 into itself)."""
   163	    arr = _square(K)
   164	    if arr.min() < 0.0:
   165	        raise ValueError("K must be non-negative")
   166	    if np.any(np.diag(arr) != 0.0):
   167	        raise ValueError("K must have a zero diagonal")
   168	    if arr.sum(axis=1).max() > 1.0 + atol:
   169	        raise ValueError("K row sums must be <= 1")
   170	    return arr
   171	
   172	
   173	def conversion_matrix(eta: np.ndarray, Q: np.ndarray) -> np.ndarray:
   174	    """K[n, m] = eta[n, m] (1 - Q_n): conversion of control in m into control in n.
   175	
   176	    Contestability of the receiving pillar n damps conversion into it.
   177	    """
   178	    e = _square(eta)
   179	    q = _unit_vector(Q, "Q")
   180	    if e.min() < 0.0 or np.any(np.diag(e) != 0.0):
   181	        raise ValueError("eta must be non-negative with zero diagonal")
   182	    return validate_conversion_matrix(e * (1.0 - q)[:, None])
   183	
   184	
   185	def conversion_step(y: np.ndarray, delta: np.ndarray, K: np.ndarray) -> np.ndarray:
   186	    """T(y) = (1 - delta) y + (1 - y) (K y). Maps [0,1]^6 into [0,1]^6."""
   187	    y = _unit_vector(y, "y")
   188	    d = _unit_vector(delta, "delta")
   189	    K = validate_conversion_matrix(K)
   190	    out = (1.0 - d) * y + (1.0 - y) * (K @ y)
   191	    return np.clip(out, 0.0, 1.0)  # guard against last-ulp rounding only
   192	
   193	
   194	def comparison_matrix(delta: np.ndarray, K: np.ndarray) -> np.ndarray:
   195	    """A = diag(1 - delta) + K, with 0 <= T(y) <= A y componentwise."""
   196	    return np.diag(1.0 - _unit_vector(delta, "delta")) + validate_conversion_matrix(K)
   197	
   198	
   199	def simulate_conversion(
   200	    y0: np.ndarray, delta: np.ndarray, K: np.ndarray, steps: int
   201	) -> np.ndarray:
   202	    """Iterate y_{t+1} = T(y_t); returns shape (steps + 1, 6)."""
   203	    if steps < 0:
   204	        raise ValueError("steps must be non-negative")
   205	    path = np.empty((steps + 1, M))
   206	    path[0] = _unit_vector(y0, "y0")
   207	    for t in range(steps):
   208	        path[t + 1] = conversion_step(path[t], delta, K)
   209	    return path
   210	
   211	
   212	def coalition_integration_share(y: np.ndarray) -> float:
   213	    """(1/15) sum_{m<n} min(y_m, y_n): the coalition's contribution to the integration statistic."""
   214	    y = _unit_vector(y, "y")
   215	    return float(sum(min(y[i], y[j]) for i in range(M) for j in range(i + 1, M)) / 15.0)
   216	
   217	
   218	def _is_irreducible(K: np.ndarray) -> bool:
   219	    reach = (np.eye(M) + (K > 0)).astype(float)
   220	    return bool(np.all(np.linalg.matrix_power(reach, M - 1) > 0))
   221	
   222	
   223	@dataclass(frozen=True)
   224	class Foothold:
   225	    """Foothold bound: v . y_t >= min(v . y_0, (1 - max delta)(rho - 1) / (2c)) for all t.
   226	
   227	    v is the left Perron vector of A (normalized to sum 1), c = v_max kappa / v_min^2 and
   228	    kappa the largest column sum of K. Proof sketch: v . T(y) = rho v . y - sum_n v_n y_n (K y)_n
   229	    >= rho s - c s^2 with s = v . y, and v . T(y) >= (1 - max delta) s.
   230	    """
   231	
   232	    rho: float
   233	    v: np.ndarray
   234	    c: float
   235	    bound: float
   236	
   237	
   238	def foothold_bound(y0: np.ndarray, delta: np.ndarray, K: np.ndarray) -> Foothold:
   239	    """Lower bound on v . y_t when K is irreducible, max delta < 1 and rho(A) > 1."""
   240	    y0 = _unit_vector(y0, "y0")
   241	    d = _unit_vector(delta, "delta")
   242	    K = validate_conversion_matrix(K)
   243	    if not _is_irreducible(K):
   244	        raise ValueError("the foothold bound needs an irreducible K")
   245	    if d.max() >= 1.0:
   246	        raise ValueError("the foothold bound needs max delta < 1")
   247	    A = comparison_matrix(d, K)
   248	    vals, vecs = np.linalg.eig(A.T)
   249	    k = int(np.argmax(vals.real))
   250	    rho = float(vals[k].real)
   251	    if rho <= 1.0:
   252	        raise ValueError("the foothold bound needs rho(A) > 1")
   253	    v = np.abs(vecs[:, k].real)
   254	    v = v / v.sum()
   255	    kappa = float(K.sum(axis=0).max())
   256	    c = float(v.max() * kappa / v.min() ** 2)
   257	    bound = min(float(v @ y0), (1.0 - float(d.max())) * (rho - 1.0) / (2.0 * c))
   258	    return Foothold(rho=rho, v=v, c=c, bound=bound)
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
    27	    CORE_RULES,
    28	    D0_KEYS,
    29	    D_STAR_KEYS,
    30	    HARD_CASES,
    31	    GovernanceSystem,
    32	    Practice,
    33	    cascade_closure,
    34	    check_proposition_a,
    35	    dependency_graph,
    36	    derive_functions,
    37	    generate_dependencies,
    38	    is_cascade_complete,
    39	    is_strongly_connected,
    40	)
    41	from .network import MultiplexNetwork
    42	from .pillars import AXIOM_TO_PILLAR, M, PAIRS, PILLARS, Axiom, IncidenceAxiom, Pillar
    43	from .regimes import regime_profiles
    44	
    45	__all__ = [
    46	    "AXIOM_TO_PILLAR", "Axiom", "CaptureLink", "CaptureThresholds", "CORE_RULES", "D0_KEYS",
    47	    "D_STAR_KEYS",
    48	    "GovernanceSystem", "HARD_CASES", "IncidenceAxiom", "M", "MultiplexNetwork", "PAIRS", "PILLARS", "Pillar",
    49	    "Polity", "Practice", "a_does_not_imply_b", "assess", "cascade_closure", "check_proposition_a",
    50	    "coalition_integration", "control_shares", "dependency_graph", "derive_functions", "hhi",
    51	    "generate_dependencies", "integration_matrix", "integration_statistic", "is_capture_link",
    52	    "is_cascade_complete", "is_strongly_connected",
    53	    "negative_feedback_example", "proposition_b", "regime_profiles", "simulate",
    54	    "spectral_radius", "unaccountable_concentration", "weight_sensitivity",
    55	]

2026-10-22T17:32:01.082857Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/necessity.py' in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/capture.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Structural necessity: Proposition A and the pillar dependency hypergraph (Part VII Theorem A).
     2	
     3	Theorem A (notation.md CENTRAL THESIS; KB Section 4): if a governance system G persists and
     4	satisfies Ax1..Ax6, then every pillar in M is implemented in G, and the dependency relations
     5	D0 are present. Implementation is role-level, not institution-level
     6	(Hempel 1959): a function may be held by a formal institution, fused with other functions
     7	inside one institution, or exercised informally (gossip and shunning as C, mediators as J).
     8	
     9	What this module does and does not do. It cannot prove Theorem A. It encodes the lemma schema
    10	'Ax_k + persistence => some practice solves problem_k' and checks it against coded cases. The
    11	role map is DERIVED from independently coded practices, never declared, so a persistent case
    12	that satisfies all six axioms yet has no practice for some problem, or lacks a D0 relation, is
    13	reported as a counterexample (the falsifier required by KB Section 4.4).
    14	
    15	Dependencies form an AND/OR hypergraph GENERATED from the axioms (Part VII revised dependency
    16	spec). A hyperarc (T, h) is written provider(s) -> dependent and means: h needs an output of
    17	AT LEAST ONE member of T. Incidence Inc(k, m), 'the problem of Ax_k arises about the inputs or
    18	rules of pillar m', generates the arc pillar(k) -> m. The core set D* comes from Ax6 (W -> m),
    19	Part III Prop 3.6 ({I, C} -> J), Ax4 with Part I Def 2.2(b) (I -> F), and the incidence axioms
    20	X1 (F -> W), X2 (P -> F), X3 (J -> F), X5 (C -> F). Removing an axiom removes every arc it
    21	generates. Two connectivity notions are computed:
    22	  (a) the underlying digraph (each (T, h) replaced by arcs t -> h) is strongly connected;
    23	  (b) cascade completeness: cl({n}) = M for every n, where cl(S) is the least superset of S
    24	      such that T subset of cl(S) implies h in cl(S) for every hyperarc (T, h).
    25	Interdependence = (a) and (b). It is a separate predicate from Theorem A's Struct(G) and is
    26	claimed for every system satisfying the extended axiom set; a system coding an incidence as
    27	absent while its premises hold is reported as an interdependence counterexample.
    28	"""
    29	
    30	from __future__ import annotations
    31	
    32	from collections.abc import Iterable, Mapping
    33	from dataclasses import dataclass, field
    34	from typing import Literal
    35	
    36	from .pillars import AXIOM_TO_PILLAR, PILLAR_TO_AXIOM, PILLARS, Axiom, IncidenceAxiom, Pillar
    37	
    38	RealizedForm = Literal["formal institution", "fused", "informal/minimal"]
    39	FORMAL: RealizedForm = "formal institution"
    40	FUSED: RealizedForm = "fused"
    41	INFORMAL: RealizedForm = "informal/minimal"
    42	
    43	# Dependency hypergraph primitives ----------------------------------------------------------
    44	
    45	#: A hyperarc key (T, h): tail set T, head h.
    46	ArcKey = tuple[frozenset[Pillar], Pillar]
    47	Graph = Mapping[Pillar, Iterable[Pillar]]
    48	AnyAxiom = Axiom | IncidenceAxiom
    49	
    50	#: Ax1..Ax6 plus the incidence axioms X1, X2, X3, X5 (Part VII extended axiom set).
    51	EXTENDED_AXIOMS: frozenset[AnyAxiom] = frozenset(Axiom) | frozenset(IncidenceAxiom)
    52	
    53	
    54	def arc_key(tail: Pillar | Iterable[Pillar], head: Pillar) -> ArcKey:
    55	    """Normalize (T, h) to an ArcKey, validating T non-empty, h a Pillar and h not in T."""
    56	    t = frozenset((tail,) if isinstance(tail, Pillar) else tail)
    57	    if not t or not all(isinstance(m, Pillar) for m in t) or not isinstance(head, Pillar):
    58	        raise TypeError("a hyperarc needs a non-empty tail of Pillars and a Pillar head")
    59	    if head in t:
    60	        raise ValueError(f"head {head.name} may not belong to its own tail")
    61	    return t, head
    62	
    63	
    64	def _keys(arcs: Iterable[DependencyRule | ArcKey]) -> frozenset[ArcKey]:
    65	    return frozenset(a.key if isinstance(a, DependencyRule) else arc_key(*a) for a in arcs)
    66	
    67	
    68	def underlying_digraph(arcs: Iterable[DependencyRule | ArcKey]) -> dict[Pillar, frozenset[Pillar]]:
    69	    """Replace each hyperarc (T, h) by the arcs t -> h; adjacency over all six pillars."""
    70	    adj: dict[Pillar, set[Pillar]] = {m: set() for m in PILLARS}
    71	    for tail, head in _keys(arcs):
    72	        for t in tail:
    73	            adj[t].add(head)
    74	    return {m: frozenset(v) for m, v in adj.items()}
    75	
    76	
    77	def cascade_closure(
    78	    arcs: Iterable[DependencyRule | ArcKey], start: Iterable[Pillar]
    79	) -> frozenset[Pillar]:
    80	    """cl(S): least superset of S with T subset of cl(S) => h in cl(S) for every (T, h).
    81	
    82	    Read as a failure cascade: h fails once every provider in its tail has failed.
    83	    """
    84	    keys = _keys(arcs)
    85	    closed = set(start)
    86	    changed = True
    87	    while changed:
    88	        changed = False
    89	        for tail, head in keys:
    90	            if head not in closed and tail <= closed:
    91	                closed.add(head)
    92	                changed = True
    93	    return frozenset(closed)
    94	
    95	
    96	def is_cascade_complete(
    97	    arcs: Iterable[DependencyRule | ArcKey], nodes: Iterable[Pillar] = PILLARS
    98	) -> bool:
    99	    """True iff cl({n}) contains every node, for every node n (restricted to ``nodes``)."""
   100	    keep = frozenset(nodes)
   101	    if not keep:
   102	        return False
   103	    inside = [(t, h) for t, h in _keys(arcs) if h in keep and t <= keep]
   104	    return all(cascade_closure(inside, {n}) >= keep for n in keep)
   105	
   106	
   107	def _nodes(graph: Graph) -> set[Pillar]:
   108	    nodes = set(graph)
   109	    for targets in graph.values():
   110	        nodes.update(targets)
   111	    return nodes
   112	
   113	
   114	def _reach(graph: Mapping[Pillar, frozenset[Pillar]], start: Pillar) -> set[Pillar]:
   115	    seen = {start}
   116	    stack = [start]
   117	    while stack:
   118	        for nxt in graph.get(stack.pop(), frozenset()):
   119	            if nxt not in seen:
   120	                seen.add(nxt)
   121	                stack.append(nxt)
   122	    return seen
   123	
   124	
   125	def is_strongly_connected(graph: Graph, nodes: Iterable[Pillar] | None = None) -> bool:
   126	    """True iff every node of the graph is reachable from every other node.
   127	
   128	    ``nodes`` restricts the graph to an induced subgraph (default: all nodes that appear).
   129	    The empty graph is not strongly connected; a single node is.
   130	    """
   131	    keep = set(nodes) if nodes is not None else _nodes(graph)
   132	    if not keep:
   133	        return False
   134	    fwd: dict[Pillar, frozenset[Pillar]] = {
   135	        u: frozenset(v for v in graph.get(u, ()) if v in keep) for u in keep
   136	    }
   137	    rev: dict[Pillar, set[Pillar]] = {u: set() for u in keep}
   138	    for u, vs in fwd.items():
   139	        for v in vs:
   140	            rev[v].add(u)
   141	    start = next(iter(keep))
   142	    rev_f = {u: frozenset(v) for u, v in rev.items()}
   143	    return _reach(fwd, start) == keep and _reach(rev_f, start) == keep
   144	
   145	
   146	def critical_edges(graph: Graph) -> list[tuple[Pillar, Pillar]]:
   147	    """Edges whose single removal breaks strong connectivity (empty if not connected)."""
   148	    nodes = _nodes(graph)
   149	    base = {u: frozenset(graph.get(u, ())) for u in nodes}
   150	    if not is_strongly_connected(base):
   151	        return []
   152	    out = []
   153	    for u in PILLARS:
   154	        for v in sorted(base.get(u, ()), key=lambda p: p.position):
   155	            pruned = dict(base)
   156	            pruned[u] = base[u] - {v}
   157	            if not is_strongly_connected(pruned, nodes):
   158	                out.append((u, v))
   159	    return out
   160	
   161	
   162	def sinks_and_sources(graph: Graph) -> tuple[frozenset[Pillar], frozenset[Pillar]]:
   163	    """Pillars with no outgoing edge (sinks) and with no incoming edge (sources)."""
   164	    nodes = _nodes(graph)
   165	    has_out = {u for u in nodes if any(True for _ in graph.get(u, ()))}
   166	    has_in = {v for u in nodes for v in graph.get(u, ())}
   167	    return frozenset(nodes - has_out), frozenset(nodes - has_in)
   168	
   169	
   170	# Axiom-generated dependency rules (Part VII revised dependency spec) ----------------------
   171	
   172	
   173	@dataclass(frozen=True)
   174	class DependencyRule:
   175	    """A hyperarc (T, h) generated when every premise in ``requires`` holds.
   176	
   177	    h needs an output of AT LEAST ONE member of T (provider(s) -> dependent). ``incidence`` is
   178	    the incidence Inc(k, m) the rule instantiates (the problem of Ax_k arises about pillar m's
   179	    inputs or rules, giving arc pillar(k) -> m), or None for a rule that is not an incidence.
   180	    ``core`` marks membership of D*; non-core rules are reported, not needed.
   181	    """
   182	
   183	    tail: frozenset[Pillar]
   184	    head: Pillar
   185	    premise: str
   186	    requires: frozenset[AnyAxiom]
   187	    source: str
   188	    core: bool
   189	    incidence: tuple[Axiom, Pillar] | None = None
   190	
   191	    def __post_init__(self) -> None:
   192	        tail, _ = arc_key(self.tail, self.head)
   193	        requires = frozenset(self.requires)
   194	        if not requires or any(not isinstance(a, (Axiom, IncidenceAxiom)) for a in requires):
   195	            raise ValueError("a dependency rule needs at least one axiom premise")
   196	        if self.incidence is not None:
   197	            axiom, target = self.incidence
   198	            if tail != frozenset({axiom.pillar}) or target is not self.head:
   199	                raise ValueError("an incidence Inc(k, m) generates exactly pillar(k) -> m")
   200	            if axiom not in requires:
   201	                raise ValueError("an incidence rule must require its own axiom")
   202	        object.__setattr__(self, "tail", tail)
   203	        object.__setattr__(self, "requires", requires)
   204	
   205	    @property
   206	    def key(self) -> ArcKey:
   207	        return self.tail, self.head
   208	
   209	
   210	def _inc(axiom: Axiom, target: Pillar, premise: str, requires: Iterable[AnyAxiom],
   211	         source: str, core: bool = True) -> DependencyRule:
   212	    return DependencyRule(frozenset({axiom.pillar}), target, premise,
   213	                          frozenset(requires) | {axiom}, source, core, (axiom, target))
   214	
   215	
   216	_P, _A, _X = Pillar, Axiom, IncidenceAxiom
   217	
   218	#: D*: the core rules. Under Ax1..Ax6 plus X1, X2, X3, X5 they generate a strongly connected,
   219	#: cascade-complete hypergraph (Part VII revised dependency spec).
   220	CORE_RULES: tuple[DependencyRule, ...] = (
   221	    *(_inc(_A.Ax6, m, "Ax6", (), "practitioners consume produced resources (Part VI)")
   222	      for m in (_P.F, _P.P, _P.J, _P.I, _P.C)),
   223	    DependencyRule(frozenset({_P.I, _P.C}), _P.J, "Part III Prop 3.6",
   224	                   frozenset({_A.Ax3, _A.Ax4, _A.Ax5}),
   225	                   "rulings settle disputes if recognized or if enforced", core=True),
   226	    _inc(_A.Ax4, _P.F, "Ax4 + Part I Def 2.2(b)", (),
   227	         "members must anticipate the settlement procedure"),
   228	    _inc(_A.Ax1, _P.W, "X1", (_X.X1,), "contested productive inputs (Part I)"),
   229	    _inc(_A.Ax2, _P.F, "X2", (_X.X2,), "changing environment hits allocation rules (Part II Ass 3.2)"),
   230	    _inc(_A.Ax3, _P.F, "X3", (_X.X3,), "open-textured allocation rules (Part III Thm 3.3)"),
   231	    _inc(_A.Ax5, _P.F, "X5", (_X.X5,), "tempting allocation rules (Part V Thm 3.4)"),
   232	)
   233	
   234	#: Further rules: reported, not needed for interdependence. Each rests on a premise beyond
   235	#: the extended axiom set (stated in ``premise``), so none is generated for a system.
   236	FURTHER_RULES: tuple[DependencyRule, ...] = (
   237	    _inc(_A.Ax4, _P.P, "X2 + Ax4", (_A.Ax2, _X.X2), "recognition of rule change", core=False),
   238	    _inc(_A.Ax2, _P.J, "X2 + Ax4", (_A.Ax4, _X.X2), "new rules to interpret", core=False),
   239	    _inc(_A.Ax2, _P.I, "X2 + Ax4", (_A.Ax4, _X.X2), "new rules to be made common knowledge",
   240	         core=False),
   241	    _inc(_A.Ax3, _P.P, "precedent (Hart)", (), "interpretation feeds rule change", core=False),
   242	    DependencyRule(frozenset({_P.F, _P.I}), _P.C, "Part V Cor 3.7 conditions",
   243	                   frozenset({_A.Ax1, _A.Ax4, _A.Ax5}),
   244	                   "costly public-good sanctions at large n, no higher-order sanctions",
   245	                   core=False),
   246	)
   247	
   248	D_STAR_KEYS: frozenset[ArcKey] = frozenset(r.key for r in CORE_RULES)
   249	#: D0: the relations Theorem A requires (W -> m for m != W, and the OR-hyperarc {I, C} -> J).
   250	D0_KEYS: frozenset[ArcKey] = frozenset(
   251	    r.key for r in CORE_RULES if r.premise in {"Ax6", "Part III Prop 3.6"}
   252	)
   253	
   254	#: The six single arcs named in the original model brief (kept for comparison only).
   255	BRIEF_ARCS: frozenset[ArcKey] = frozenset(
   256	    arc_key(t, h) for t, h in [(_P.W, _P.C), (_P.P, _P.J), (_P.I, _P.P), (_P.J, _P.F),
   257	                               (_P.F, _P.W), (_P.W, _P.I)]
   258	)
   259	
   260	
   261	def rules_holding(
   262	    axioms: Iterable[AnyAxiom], rules: Iterable[DependencyRule] = CORE_RULES
   263	) -> tuple[DependencyRule, ...]:
   264	    """The rules whose premises all hold under ``axioms``."""
   265	    held = frozenset(axioms)
   266	    return tuple(r for r in rules if r.requires <= held)
   267	
   268	
   269	def dependency_graph(axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS) -> dict[Pillar, frozenset[Pillar]]:
   270	    """Underlying digraph of the core rules generated under ``axioms`` (default: all)."""
   271	    return underlying_digraph(rules_holding(axioms))
   272	
   273	
   274	# Governance systems ------------------------------------------------------------------------
   275	
   276	
   277	@dataclass(frozen=True)
   278	class Practice:
   279	    """A regular activity that discharges the problem generated by axiom ``solves``.
   280	
   281	    ``formal`` is True when the activity is attached to a designated office or organization.
   282	    ``source`` holds the citation key(s) supporting the coding.
   283	    """
   284	
   285	    description: str
   286	    solves: Axiom
   287	    holders: frozenset[str]
   288	    formal: bool = False
   289	    source: str = ""
   290	
   291	    def __post_init__(self) -> None:
   292	        if not isinstance(self.solves, Axiom):
   293	            raise TypeError("Practice.solves must be an Axiom")
   294	        holders = frozenset(self.holders)
   295	        if not holders or any(not isinstance(h, str) or not h for h in holders):
   296	            raise ValueError("a practice needs at least one named holder")
   297	        if not self.description.strip():
   298	            raise ValueError("a practice needs a description")
   299	        object.__setattr__(self, "holders", holders)
   300	
   301	    @property
   302	    def pillar(self) -> Pillar:
   303	        return AXIOM_TO_PILLAR[self.solves]
   304	
   305	
   306	@dataclass(frozen=True)
   307	class GovernanceSystem:
   308	    """A collective that makes and enforces collective decisions (KB Section 4.1).
   309	
   310	    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
   311	    over the period studied; it may include the incidence axioms X1, X2, X3, X5. Both are
   312	    coded independently of ``practices``. Dependencies are generated from ``axioms``;
   313	    ``absent_incidences`` records incidences Inc(k, m) OBSERVED not to arise in this system,
   314	    which suppress the arcs they would generate (the route by which a case can falsify D0 or
   315	    interdependence).
   316	    """
   317	
   318	    name: str
   319	    persistent: bool
   320	    axioms: frozenset[AnyAxiom]
   321	    practices: tuple[Practice, ...] = ()
   322	    absent_incidences: frozenset[tuple[Axiom, Pillar]] = frozenset()
   323	    note: str = ""
   324	
   325	    def __post_init__(self) -> None:
   326	        if not isinstance(self.persistent, bool):
   327	            raise TypeError("persistent must be a bool")
   328	        axioms = frozenset(self.axioms)
   329	        if any(not isinstance(a, (Axiom, IncidenceAxiom)) for a in axioms):
   330	            raise TypeError("axioms must be Axiom or IncidenceAxiom members")
   331	        practices = tuple(self.practices)
   332	        if any(not isinstance(p, Practice) for p in practices):
   333	            raise TypeError("practices must be Practice instances")
   334	        object.__setattr__(self, "axioms", axioms)
   335	        object.__setattr__(self, "practices", practices)
   336	        absent = frozenset(tuple(i) for i in self.absent_incidences)
   337	        if any(len(i) != 2 or not isinstance(i[0], Axiom) or not isinstance(i[1], Pillar)
   338	               for i in absent):
   339	            raise TypeError("absent_incidences must be (Axiom, Pillar) pairs")
   340	        object.__setattr__(self, "absent_incidences", absent)
   341	
   342	    def holds(self, axiom: AnyAxiom) -> bool:
   343	        """Predicate for one axiom (Ax1..Ax6 or an incidence axiom X_k)."""
   344	        return axiom in self.axioms
   345	
   346	    @property
   347	    def all_axioms_hold(self) -> bool:
   348	        """Ax1..Ax6 all hold (the antecedent of Theorem A)."""
   349	        return all(self.holds(a) for a in Axiom)
   350	
   351	    @property
   352	    def extended_axioms_hold(self) -> bool:
   353	        """Ax1..Ax6 and X1, X2, X3, X5 all hold (the antecedent of interdependence)."""
   354	        return EXTENDED_AXIOMS <= self.axioms
   355	
   356	
   357	def generate_dependencies(
   358	    system: GovernanceSystem, rules: Iterable[DependencyRule] = CORE_RULES
   359	) -> frozenset[ArcKey]:
   360	    """Hyperarcs generated in ``system``: rules whose premises hold, minus absent incidences."""
   361	    return frozenset(
   362	        r.key for r in rules_holding(system.axioms, rules)
   363	        if r.incidence is None or r.incidence not in system.absent_incidences
   364	    )
   365	
   366	
   367	def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
   368	    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
   369	    roles: dict[str, set[Pillar]] = {}
   370	    for p in system.practices:
   371	        for h in p.holders:
   372	            roles.setdefault(h, set()).add(p.pillar)
   373	    return {h: frozenset(ps) for h, ps in roles.items()}
   374	
   375	
   376	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   377	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   378	
   379	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   380	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   381	    """
   382	    practices = [p for p in system.practices if p.pillar is pillar]
   383	    if not practices:
   384	        return None
   385	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   386	    if not formal_holders:
   387	        return INFORMAL
   388	    formal_roles: dict[str, set[Pillar]] = {}
   389	    for p in system.practices:
   390	        if p.formal:
   391	            for h in p.holders:
   392	                formal_roles.setdefault(h, set()).add(p.pillar)
   393	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   394	        return FUSED
   395	    return FORMAL
   396	
   397	
   398	@dataclass(frozen=True)
   399	class Derivation:
   400	    """Result of the lemma for one axiom: required pillar and its realized form."""
   401	
   402	    axiom: Axiom
   403	    pillar: Pillar
   404	    form: RealizedForm | None
   405	    practices: tuple[Practice, ...]
   406	
   407	    @property
   408	    def realized(self) -> bool:
   409	        return self.form is not None
   410	
   411	
   412	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   413	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   414	
   415	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   416	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   417	    """
   418	    out: dict[Axiom, Derivation] = {}
   419	    for axiom in Axiom:
   420	        if not system.holds(axiom):
   421	            continue
   422	        pillar = AXIOM_TO_PILLAR[axiom]
   423	        out[axiom] = Derivation(
   424	            axiom=axiom,
   425	            pillar=pillar,
   426	            form=realized_form(system, pillar),
   427	            practices=tuple(p for p in system.practices if p.solves is axiom),
   428	        )
   429	    return out
   430	
   431	
   432	# Proposition A and interdependence --------------------------------------------------------
   433	
   434	
   435	@dataclass(frozen=True)
   436	class PropositionAResult:
   437	    """Outcome of checking Theorem A and interdependence on one coded system.
   438	
   439	    ``holds`` is Struct(G): all six pillars realized AND every D0 relation generated.
   440	    ``counterexample`` is True when Theorem A's antecedent holds (persistent, Ax1..Ax6) but
   441	    Struct(G) fails.
   442	
   443	    ``interdependent`` is the separate structural predicate: all six pillars realized and the
   444	    generated hypergraph both strongly connected (underlying digraph) and cascade-complete.
   445	    ``interdependence_counterexample`` is True when the system is persistent, satisfies the
   446	    extended axiom set, yet is not interdependent.
   447	    """
   448	
   449	    system: str
   450	    antecedent: bool
   451	    realized: frozenset[Pillar]
   452	    missing: frozenset[Pillar]
   453	    dependencies: frozenset[ArcKey]
   454	    missing_dependencies: frozenset[ArcKey]
   455	    strongly_connected: bool
   456	    cascade_complete: bool
   457	    holds: bool
   458	    interdependence_antecedent: bool
   459	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   460	
   461	    @property
   462	    def counterexample(self) -> bool:
   463	        return self.antecedent and not self.holds
   464	
   465	    @property
   466	    def interdependent(self) -> bool:
   467	        return not self.missing and self.strongly_connected and self.cascade_complete
   468	
   469	    @property
   470	    def interdependence_counterexample(self) -> bool:
   471	        return self.interdependence_antecedent and not self.interdependent
   472	
   473	
   474	def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
   475	    """Check Theorem A and interdependence on ``system`` (Part VII; KB Section 4.3).
   476	
   477	    A D0 relation is demanded when its head and every tail member are realized.
   478	    """
   479	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   480	    deps = generate_dependencies(system)
   481	    needed = frozenset((t, h) for t, h in D0_KEYS if h in realized and t <= realized)
   482	    missing_deps = needed - deps
   483	    return PropositionAResult(
   484	        system=system.name,
   485	        antecedent=system.persistent and system.all_axioms_hold,
   486	        realized=realized,
   487	        missing=frozenset(PILLARS) - realized,
   488	        dependencies=deps,
   489	        missing_dependencies=missing_deps,
   490	        strongly_connected=is_strongly_connected(underlying_digraph(deps), realized),
   491	        cascade_complete=is_cascade_complete(deps, realized),
   492	        holds=realized == frozenset(PILLARS) and not missing_deps,
   493	        interdependence_antecedent=system.persistent and system.extended_axioms_hold,
   494	        derivations=derive_functions(system),
   495	    )
   496	
   497	
   498	def formal_system(
   499	    name: str,
   500	    holders: Mapping[Pillar, Iterable[str]],
   501	    persistent: bool = True,
   502	    source: str = "",
   503	    axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS,
   504	) -> GovernanceSystem:
   505	    """A persistent system whose pillars are held by formal organizations.
   506	
   507	    An actor listed under several pillars is fused. By default the extended axiom set is
   508	    coded as holding: an assumption of the stylized model, not an observation. Used for regime
   509	    profiles and counter-models.
   510	    """
   511	    practices = tuple(
   512	        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
   513	                 frozenset(hs), formal=True, source=source)
   514	        for m, hs in holders.items()
   515	        if hs
   516	    )
   517	    return GovernanceSystem(name, persistent, frozenset(axioms), practices)
   518	
   519	
   520	# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
   521	# Each codes the extended axiom set as holding. For X1, X2, X3, X5 this is a coding
   522	# assumption with the falsifier stated on IncidenceAxiom; e.g. Nuer grazing and herds and
   523	# Ju/'hoansi n!ore territories are contested inputs (X1).
   524	
   525	
   526	def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
   527	    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)
   528	
   529	
   530	NUER = GovernanceSystem(
   531	    name="Nuer ('ordered anarchy')",
   532	    persistent=True,
   533	    axioms=EXTENDED_AXIOMS,
   534	    practices=(
   535	        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
   536	                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
   537	        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
   538	                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
   539	        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
   540	                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
   541	        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
   542	                  {"prophets", "lineages"}, "evanspritchard1940"),
   543	        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
   544	                  {"agnatic kin"}, "evanspritchard1940"),
   545	        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
   546	                  "evanspritchard1940"),
   547	    ),
   548	    note="no office holds coercive authority; functions exist without separation",
   549	)
   550	
   551	JU_HOANSI = GovernanceSystem(
   552	    name="Ju/'hoansi (!Kung)",
   553	    persistent=True,
   554	    axioms=EXTENDED_AXIOMS,
   555	    practices=(
   556	        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
   557	                  {"hunters", "camp members"}, "lee2013; marshall1976"),
   558	        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
   559	                  {"camp members"}, "lee2013"),
   560	        _informal("disputes talked out with kin mediators", Axiom.Ax3,
   561	                  {"kin mediators"}, "lee1979; wiessner2005"),
   562	        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
   563	                  {"healers", "camp members"}, "marshall1976"),
   564	        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
   565	                  {"camp members"}, "wiessner2005; lee2013"),
   566	        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
   567	    ),
   568	    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
   569	)
   570	
   571	OSTROM_COMMONS = GovernanceSystem(
   572	    name="Ostrom commons (design principles)",
   573	    persistent=True,
   574	    axioms=EXTENDED_AXIOMS,
   575	    practices=(
   576	        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
   577	                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
   578	        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
   579	                  {"appropriators"}, "ostrom1990"),
   580	        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
   581	                  {"appropriators"}, "ostrom1990; cox2010"),
   582	        _informal("shared norms; minimal recognition of rights to organize (DP7)",
   583	                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),
   584	        _informal("monitoring and graduated sanctions by appropriators (DP4, DP5)",
   585	                  Axiom.Ax5, {"appropriators"}, "ostrom1990; cox2010"),
   586	        _informal("appropriation and maintenance labor", Axiom.Ax6, {"appropriators"},
   587	                  "ostrom1990"),
   588	    ),
   589	    note="checks in minimal form; monitors are appropriators or accountable to them",
   590	)
   591	
   592	CONSENSUS_VILLAGE = GovernanceSystem(
   593	    name="Consensus village (stylized)",
   594	    persistent=True,
   595	    axioms=EXTENDED_AXIOMS,
   596	    practices=(
   597	        _informal("household plots; reciprocal labor exchange; sharing norms", Axiom.Ax1,
   598	                  {"households"}, "sahlins1972"),
   599	        _informal("consensus meeting of adults", Axiom.Ax2, {"village meeting"},
   600	                  "clastres1987; boehm1999"),
   601	        _informal("elders mediate disputes", Axiom.Ax3, {"elders"}, "boehm1999"),
   602	        _informal("ritual and myth; moral talk", Axiom.Ax4, {"village meeting", "elders"},
   603	                  "boehm1999"),
   604	        _informal("gossip, shunning, ostracism of would-be dominants", Axiom.Ax5,
   605	                  {"village meeting"}, "boehm1999; woodburn1982"),
   606	        _informal("gardening and household labor", Axiom.Ax6, {"households"},
   607	                  "sahlins1972"),
   608	    ),
   609	    note="stylized composite; reverse dominance hierarchy",
   610	)
   611	
   612	HARD_CASES: tuple[GovernanceSystem, ...] = (NUER, JU_HOANSI, OSTROM_COMMONS, CONSENSUS_VILLAGE)
   613	
   614	
   615	# Axiom independence fixtures (Part VII spec, item 7). ---------------------------------------
   616	
   617	#: Consistency model: the extended axiom set holds and all six pillars are realized (the
   618	#: consensus village coding).
   619	BASELINE_MODEL: GovernanceSystem = CONSENSUS_VILLAGE
   620	
   621	
   622	def without_axiom(axiom: AnyAxiom, base: GovernanceSystem = BASELINE_MODEL) -> GovernanceSystem:
   623	    """``base`` with one axiom removed; for Ax_k the practices solving Ax_k are removed too."""
   624	    practices = base.practices
   625	    if isinstance(axiom, Axiom):
   626	        practices = tuple(p for p in practices if p.solves is not axiom)
   627	    return GovernanceSystem(
   628	        name=f"{base.name} without {axiom.name} ({axiom.label})",
   629	        persistent=base.persistent,
   630	        axioms=base.axioms - {axiom},
   631	        practices=practices,
   632	        absent_incidences=base.absent_incidences,
   633	        note="hypothetical: one axiom removed",
   634	    )
   635	
   636	
   637	#: For each k: persistent, Ax_k removed, pillar k missing. Theorem A's antecedent is false,
   638	#: so none is a counterexample; each shows pillar k is not forced by the other five axioms.
   639	AXIOM_INDEPENDENCE: dict[Axiom, GovernanceSystem] = {a: without_axiom(a) for a in Axiom}

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
    17	    WeightSensitivity,
    18	    coalition_integration,
    19	    control_shares,
    20	    hhi,
    21	    integration_statistic,
    22	    unaccountable_concentration,
    23	    validate_integration_matrix,
    24	    validate_unit_interval,
    25	    validate_weights,
    26	    weight_sensitivity,
    27	)
    28	from .necessity import (
    29	    GovernanceSystem,
    30	    PropositionAResult,
    31	    check_proposition_a,
    32	    formal_system,
    33	    role_map,
    34	)
    35	from .network import MultiplexNetwork
    36	from .pillars import PILLARS, Pillar
    37	
    38	
    39	@dataclass(frozen=True)
    40	class CaptureLink:
    41	    """Capture link (i -> j, m) (source Section 5; notation.md 'Capture link').
    42	
    43	    All three conditions are required: (i) privileged access or discretion; (ii) the privilege
    44	    weakens otherwise applicable accountability or contestability; (iii) material evidence
    45	    links the asymmetry to an institutional output. A disclosure-compliant donor meeting is
    46	    not automatically capture. Claiming (iii) requires citing the evidence.
    47	    """
    48	
    49	    source: str
    50	    target: str
    51	    pillar: Pillar
    52	    privileged_access: bool
    53	    weakens_accountability: bool
    54	    material_evidence: bool
    55	    evidence: str = ""
    56	
    57	    def __post_init__(self) -> None:
    58	        for end in (self.source, self.target):
    59	            if not isinstance(end, str) or not end:
    60	                raise ValueError("capture link endpoints must be named")
    61	        if not isinstance(self.pillar, Pillar):
    62	            raise TypeError("capture link pillar must be a Pillar")
    63	        for flag in ("privileged_access", "weakens_accountability", "material_evidence"):
    64	            if not isinstance(getattr(self, flag), bool):
    65	                raise TypeError(f"{flag} must be a bool")
    66	        if not isinstance(self.evidence, str):
    67	            raise TypeError("evidence must be a string")
    68	        if self.material_evidence and not self.evidence.strip():
    69	            raise ValueError("condition (iii) requires a citation of the material evidence")
    70	
    71	    @property
    72	    def holds(self) -> bool:
    73	        return self.privileged_access and self.weakens_accountability and self.material_evidence
    74	
    75	
    76	def is_capture_link(link: CaptureLink) -> bool:
    77	    """Conjunction of the source's three conditions."""
    78	    return link.holds
    79	
    80	
    81	@dataclass(frozen=True)
    82	class CaptureThresholds:
    83	    """Thresholds u*, i* for Proposition B. Illustrative defaults; preregister in applications."""
    84	
    85	    u_star: float = 0.4
    86	    i_star: float = 0.5
    87	
    88	    def __post_init__(self) -> None:
    89	        object.__setattr__(self, "u_star", validate_unit_interval(self.u_star, "u_star"))
    90	        object.__setattr__(self, "i_star", validate_unit_interval(self.i_star, "i_star"))
    91	
    92	
    93	@dataclass(frozen=True)
    94	class PropositionBResult:
    95	    u_high: bool
    96	    i_high: bool
    97	    n_links: int
    98	
    99	    @property
   100	    def thresholds_met(self) -> bool:
   101	        return self.u_high and self.i_high
   102	
   103	    @property
   104	    def holds(self) -> bool:
   105	        return self.thresholds_met and self.n_links > 0
   106	
   107	
   108	def proposition_b(
   109	    U: float,
   110	    I: float,  # noqa: E741  (integration statistic, math cal I)
   111	    links: tuple[CaptureLink, ...] | list[CaptureLink],
   112	    thresholds: CaptureThresholds = CaptureThresholds(),
   113	) -> PropositionBResult:
   114	    """Proposition B: U >= u* AND I >= i* AND some capture link holds."""
   115	    U = validate_unit_interval(U, "U")
   116	    I = validate_unit_interval(I, "I")  # noqa: E741
   117	    return PropositionBResult(
   118	        u_high=U >= thresholds.u_star,
   119	        i_high=I >= thresholds.i_star,
   120	        n_links=sum(1 for link in links if is_capture_link(link)),
   121	    )
   122	
   123	
   124	@dataclass(frozen=True)
   125	class Polity:
   126	    """A coded polity: governance system (for A) plus index inputs (for B).
   127	
   128	    ``shares[m]`` holds raw non-negative control weights per actor, normalized to s^m.
   129	    ``weights`` are the preregistered U weights (None means the equal-weight preregistration
   130	    1/M); ``assess`` always adds a weight-sensitivity analysis. Capture-link endpoints must be
   131	    actors of the polity (share holders or holders of coded practices).
   132	    """
   133	
   134	    name: str
   135	    system: GovernanceSystem
   136	    shares: Mapping[Pillar, Mapping[str, float]]
   137	    contestability: Mapping[Pillar, float]
   138	    integration: np.ndarray
   139	    capture_links: tuple[CaptureLink, ...] = ()
   140	    weights: Mapping[Pillar, float] | None = None
   141	    normalized_shares: Mapping[Pillar, Mapping[str, float]] = field(init=False, repr=False)
   142	
   143	    def __post_init__(self) -> None:
   144	        if set(self.shares) != set(PILLARS):
   145	            raise ValueError("shares must cover every pillar")
   146	        norm = {m: control_shares(self.shares[m]) for m in PILLARS}
   147	        object.__setattr__(self, "normalized_shares", norm)
   148	        object.__setattr__(self, "integration", validate_integration_matrix(self.integration))
   149	        object.__setattr__(self, "weights", validate_weights(self.weights))
   150	        links = tuple(self.capture_links)
   151	        if any(not isinstance(link, CaptureLink) for link in links):
   152	            raise TypeError("capture_links must be CaptureLink instances")
   153	        actors = self.actors
   154	        for link in links:
   155	            for end in (link.source, link.target):
   156	                if end not in actors:
   157	                    raise ValueError(f"capture link endpoint {end!r} is not an actor of {self.name}")
   158	        object.__setattr__(self, "capture_links", links)
   159	        # Fail early on bad Q.
   160	        unaccountable_concentration(self.H, self.contestability, self.weights)
   161	
   162	    @property
   163	    def actors(self) -> frozenset[str]:
   164	        """V: every share holder plus every holder of a coded practice."""
   165	        held = {a for m in PILLARS for a in self.shares[m]}
   166	        return frozenset(held | set(role_map(self.system)))
   167	
   168	    @property
   169	    def H(self) -> dict[Pillar, float]:  # noqa: N802
   170	        return {m: hhi(self.normalized_shares[m]) for m in PILLARS}
   171	
   172	    @property
   173	    def U(self) -> float:  # noqa: N802
   174	        return unaccountable_concentration(self.H, self.contestability, self.weights)
   175	
   176	    @property
   177	    def I(self) -> float:  # noqa: E743, N802
   178	        return integration_statistic(self.integration)
   179	
   180	
   181	@dataclass(frozen=True)
   182	class Assessment:
   183	    name: str
   184	    H: dict[Pillar, float]
   185	    U: float
   186	    I: float  # noqa: E741
   187	    prop_a: PropositionAResult
   188	    prop_b: PropositionBResult
   189	    sensitivity: WeightSensitivity
   190	    u_star: float
   191	
   192	    @property
   193	    def u_high_fraction(self) -> float:
   194	        """Share of weight draws with U >= u*: robustness of the U side of Proposition B."""
   195	        return self.sensitivity.fraction_at_least(self.u_star)
   196	
   197	
   198	def assess(
   199	    polity: Polity,
   200	    thresholds: CaptureThresholds = CaptureThresholds(),
   201	    n_draws: int = 2000,
   202	    seed: int = 0,
   203	) -> Assessment:
   204	    """Evaluate Proposition A, Proposition B and the weight sensitivity of U on one polity."""
   205	    return Assessment(
   206	        name=polity.name,
   207	        H=polity.H,
   208	        U=polity.U,
   209	        I=polity.I,
   210	        prop_a=check_proposition_a(polity.system),
   211	        prop_b=proposition_b(polity.U, polity.I, polity.capture_links, thresholds),
   212	        sensitivity=weight_sensitivity(polity.H, polity.contestability, polity.weights,
   213	                                       n_draws=n_draws, seed=seed),
   214	        u_star=thresholds.u_star,
   215	    )
   216	
   217	
   218	# Counter-model: A does not imply B --------------------------------------------------------
   219	
   220	
   221	def _layer_from(holders: list[str], actors: list[str], weight: float) -> np.ndarray:
   222	    idx = {a: k for k, a in enumerate(actors)}
   223	    arr = np.zeros((len(actors), len(actors)))
   224	    for h in holders:
   225	        for a in actors:
   226	            if a != h:
   227	                arr[idx[h], idx[a]] = weight
   228	    return arr
   229	
   230	
   231	def plural_polity(n_per_pillar: int = 5, q: float = 0.9) -> Polity:
   232	    """G1, accountable pluralism: each pillar held by n independent organizations.
   233	
   234	    Holders are disjoint across pillars, so every coalition overlap is 0 and C_mn = 0.
   235	    """
   236	    if n_per_pillar < 1:
   237	        raise ValueError("n_per_pillar must be positive")
   238	    q = validate_unit_interval(q, "q")
   239	    holders = {m: [f"{m.label}-org-{k}" for k in range(n_per_pillar)] for m in PILLARS}
   240	    actors = [a for m in PILLARS for a in holders[m]]
   241	    net = MultiplexNetwork(
   242	        actors=tuple(actors),
   243	        layers={m: _layer_from(holders[m], actors, 0.5) for m in PILLARS},
   244	        roles={a: {m} for m in PILLARS for a in holders[m]},
   245	    )
   246	    shares = {m: net.out_strength_shares(m) for m in PILLARS}
   247	    return Polity(
   248	        name="G1 accountable pluralism",
   249	        system=formal_system("G1 accountable pluralism", holders),
   250	        shares=shares,
   251	        contestability={m: q for m in PILLARS},
   252	        integration=coalition_integration(shares),
   253	    )
   254	
   255	
   256	def fused_polity(n_subordinate: int = 5, q: float = 0.0) -> Polity:
   257	    """G2, fused capture: one coalition holds all six pillars with Q = q, one evidenced link.
   258	
   259	    H_m = 1 and C_mn = 1, so U = 1 - q and I = 1; with the default q = 0 both indices reach
   260	    their maximum and meet every admissible threshold pair (u*, i*) in [0, 1]^2.
   261	    """
   262	    if n_subordinate < 1:
   263	        raise ValueError("n_subordinate must be positive")
   264	    q = validate_unit_interval(q, "q")
   265	    core = "ruling coalition"
   266	    actors = [core] + [f"subordinate-{k}" for k in range(n_subordinate)]
   267	    net = MultiplexNetwork(
   268	        actors=tuple(actors),
   269	        layers={m: _layer_from([core], actors, 1.0) for m in PILLARS},
   270	        roles={core: set(PILLARS)},
   271	    )
   272	    shares = {m: net.out_strength_shares(m) for m in PILLARS}
   273	    link = CaptureLink(
   274	        source=core, target="subordinate-0", pillar=Pillar.J,
   275	        privileged_access=True, weakens_accountability=True, material_evidence=True,
   276	        evidence="synthetic: appointment record ties removal of reviewing judges to ruling",
   277	    )
   278	    return Polity(
   279	        name="G2 fused capture",
   280	        system=formal_system("G2 fused capture", {m: [core] for m in PILLARS}),
   281	        shares=shares,
   282	        contestability={m: q for m in PILLARS},
   283	        integration=coalition_integration(shares),
   284	        capture_links=(link,),
   285	    )
   286	
   287	
   288	@dataclass(frozen=True)
   289	class CounterModel:
   290	    plural: Assessment
   291	    fused: Assessment
   292	
   293	    @property
   294	    def demonstrates_non_implication(self) -> bool:
   295	        """Both satisfy A; only G2 satisfies B. Hence A does not imply B."""
   296	        return (
   297	            self.plural.prop_a.holds
   298	            and self.fused.prop_a.holds
   299	            and not self.plural.prop_b.holds
   300	            and self.fused.prop_b.holds
   301	        )
   302	
   303	
   304	def a_does_not_imply_b(thresholds: CaptureThresholds = CaptureThresholds()) -> CounterModel:
   305	    """Constructive counter-model for Part VII Theorem 2 (KB Section 4.3 item 4).
   306	
   307	    G1 has U = (1/5)(1 - 0.9) = 0.02, I = 0 and no capture link; G2 has U = 1, I = 1 and one
   308	    evidenced link. Both pass the Theorem A check (six pillars realized, D0 generated) and
   309	    both are interdependent, so interdependence does not imply capture either. G1 fails B for every thresholds pair because it has no link (and its indices lie
   310	    below any u* > 0.02, i* > 0); G2 meets B for every thresholds pair in [0, 1]^2.
   311	    """
   312	    return CounterModel(
   313	        plural=assess(plural_polity(), thresholds),
   314	        fused=assess(fused_polity(), thresholds),
   315	    )
   316	
   317	
   318	# Corner attainability (Part VII addendum item 9) --------------------------------------------
   319	
   320	
   321	def grand_coalition_polity(n_members: int = 5) -> Polity:
   322	    """(U, I) = (0, 1): one consensus coalition holds every pillar in equal shares, Q = 1."""
   323	    if n_members < 1:
   324	        raise ValueError("n_members must be positive")
   325	    members = [f"member-{k}" for k in range(n_members)]
   326	    shares = {m: {a: 1.0 / n_members for a in members} for m in PILLARS}
   327	    return Polity(
   328	        name="consensus grand coalition",
   329	        system=formal_system("consensus grand coalition", {m: members for m in PILLARS}),
   330	        shares=shares,
   331	        contestability={m: 1.0 for m in PILLARS},
   332	        integration=coalition_integration(shares, {a: "grand coalition" for a in members}),
   333	    )
   334	
   335	
   336	def separate_monopolies_polity() -> Polity:
   337	    """(U, I) = (1, 0): a different monopolist per pillar, Q = 0, no shared coalition."""
   338	    holders = {m: [f"{m.label} monopolist"] for m in PILLARS}
   339	    shares = {m: {holders[m][0]: 1.0} for m in PILLARS}
   340	    return Polity(
   341	        name="separate monopolies",
   342	        system=formal_system("separate monopolies", holders),
   343	        shares=shares,
   344	        contestability={m: 0.0 for m in PILLARS},
   345	        integration=coalition_integration(shares),
   346	    )
   347	
   348	
   349	def corner_polities() -> dict[tuple[int, int], Polity]:
   350	    """Four polities satisfying A that attain the corners of the (U, I) square.
   351	
   352	    Only the (1, 1) corner carries a capture link, so U and I alone never decide B.
   353	    """
   354	    return {
   355	        (0, 0): plural_polity(q=1.0),
   356	        (1, 1): fused_polity(q=0.0),
   357	        (0, 1): grand_coalition_polity(),
   358	        (1, 0): separate_monopolies_polity(),
   359	    }

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
    33	    if isinstance(value, bool) or not isinstance(value, (int, float, np.integer, np.floating)):
    34	        raise TypeError(f"{name} must be a real number, got {type(value).__name__}")
    35	    v = float(value)
    36	    if not math.isfinite(v) or v < 0.0 or v > 1.0:
    37	        raise ValueError(f"{name} must lie in [0, 1], got {value!r}")
    38	    return v
    39	
    40	
    41	def _share_array(shares: ShareLike) -> np.ndarray:
    42	    values = list(shares.values()) if isinstance(shares, Mapping) else shares
    43	    arr = np.asarray(values, dtype=float).ravel()
    44	    if arr.size == 0:
    45	        raise ValueError("shares must be non-empty")
    46	    if not np.all(np.isfinite(arr)):
    47	        raise ValueError("shares must be finite")
    48	    if arr.min() < 0.0:
    49	        raise ValueError("shares must be non-negative")
    50	    return arr
    51	
    52	
    53	def control_shares(raw: Mapping[str, float]) -> dict[str, float]:
    54	    """Normalize non-negative control weights to shares s^m_i summing to 1 (notation.md)."""
    55	    arr = _share_array(raw)
    56	    scale = float(arr.max())
    57	    if scale <= 0.0:
    58	        raise ValueError("at least one control weight must be positive")
    59	    scaled = arr / scale  # in [0, 1], so the sum cannot overflow
    60	    total = float(scaled.sum())
    61	    return {k: float(v) / total for k, v in zip(raw, scaled)}
    62	
    63	
    64	def validate_shares(shares: ShareLike, atol: float = SHARE_ATOL) -> np.ndarray:
    65	    """Check s^m_i >= 0 and sum_i s^m_i = 1 (notation.md 'Control share').
    66	
    67	    Returns the shares renormalized to sum exactly 1, so rounding within ``atol`` cannot push
    68	    H outside [1/n, 1].
    69	    """
    70	    arr = _share_array(shares)
    71	    total = float(arr.sum())
    72	    if abs(total - 1.0) > atol:
    73	        raise ValueError(f"shares must sum to 1, got {total:.12g}")
    74	    return arr / total
    75	
    76	
    77	def hhi(shares: ShareLike) -> float:
    78	    """H_m = sum_i (s^m_i)^2 (source Eq. for H_{m,t}). Lies in [1/n, 1]."""
    79	    arr = validate_shares(shares)
    80	    return float(np.dot(arr, arr))
    81	
    82	
    83	def normalized_hhi(shares: ShareLike) -> float:
    84	    """H* = (H - 1/n) / (1 - 1/n), for comparing polities with different n (KB VII.3 (v)).
    85	
    86	    Not in the source. Defined as 1 for n = 1 (a monopoly by construction).
    87	    """
    88	    arr = validate_shares(shares)
    89	    n = arr.size
    90	    if n == 1:
    91	        return 1.0
    92	    return float((np.dot(arr, arr) - 1.0 / n) / (1.0 - 1.0 / n))
    93	
    94	
    95	def validate_weights(weights: Mapping[Pillar, float] | None) -> dict[Pillar, float]:
    96	    """Check the U weights: one per pillar, w_m >= 0, sum_m w_m = 1 (source Eq. U_t).
    97	
    98	    ``None`` gives equal weights 1/M.
    99	    """
   100	    if weights is None:
   101	        return {m: 1.0 / M for m in PILLARS}
   102	    if set(weights) != set(PILLARS):
   103	        raise ValueError("weights must give exactly one value per pillar")
   104	    w = {m: float(weights[m]) for m in PILLARS}
   105	    if any(not math.isfinite(v) or v < 0.0 for v in w.values()):
   106	        raise ValueError("weights must be finite and non-negative")
   107	    total = sum(w.values())
   108	    if abs(total - 1.0) > WEIGHT_ATOL:
   109	        raise ValueError(f"weights must sum to 1, got {total:.12g}")
   110	    return {m: v / total for m, v in w.items()}
   111	
   112	
   113	def _per_pillar(values: Mapping[Pillar, float], name: str) -> dict[Pillar, float]:
   114	    if set(values) != set(PILLARS):
   115	        raise ValueError(f"{name} must give exactly one value per pillar")
   116	    return {m: validate_unit_interval(values[m], f"{name}[{m.name}]") for m in PILLARS}
   117	
   118	
   119	def unaccountable_concentration(
   120	    H: Mapping[Pillar, float],
   121	    Q: Mapping[Pillar, float],
   122	    weights: Mapping[Pillar, float] | None = None,
   123	) -> float:
   124	    """U = sum_m w_m H_m (1 - Q_m) (source Eq. U_t). Lies in [0, 1].
   125	
   126	    U = 0 iff Q_m = 1 for every m with w_m > 0, because H_m >= 1/n > 0 (KB VII.3 (ii)).
   127	    """
   128	    h = _per_pillar(H, "H")
   129	    if any(v == 0.0 for v in h.values()):
   130	        raise ValueError("H_m >= 1/n > 0 for any valid share vector; got H_m = 0")
   131	    q = _per_pillar(Q, "Q")
   132	    w = validate_weights(weights)
   133	    u = sum(w[m] * h[m] * (1.0 - q[m]) for m in PILLARS)
   134	    return float(min(max(u, 0.0), 1.0))  # guard against last-ulp rounding
   135	
   136	
   137	def validate_integration_matrix(C: np.ndarray, atol: float = 1e-12) -> np.ndarray:
   138	    """Check C is 6x6, finite, symmetric, with off-diagonal C_mn in [0, 1].
   139	
   140	    The diagonal is unused by the integration statistic; by convention it is set to 1.
   141	    """
   142	    arr = np.array(C, dtype=float)
   143	    if arr.shape != (M, M):
   144	        raise ValueError(f"integration matrix must be {M}x{M}, got {arr.shape}")
   145	    if not np.all(np.isfinite(arr)):
   146	        raise ValueError("integration matrix must be finite")
   147	    if not np.allclose(arr, arr.T, atol=atol, rtol=0.0):
   148	        raise ValueError("integration matrix must be symmetric (C_mn = C_nm)")
   149	    off = arr[~np.eye(M, dtype=bool)]
   150	    if off.min() < 0.0 or off.max() > 1.0:
   151	        raise ValueError("off-diagonal C_mn must lie in [0, 1]")
   152	    arr = (arr + arr.T) / 2.0  # exact symmetry, so both triangles agree
   153	    np.fill_diagonal(arr, 1.0)
   154	    return arr
   155	
   156	
   157	def integration_matrix(
   158	    pairs: Mapping[tuple[Pillar, Pillar], float], default: float = 0.0
   159	) -> np.ndarray:
   160	    """Build a symmetric C from {(m, n): C_mn}; unspecified pairs take ``default``."""
   161	    validate_unit_interval(default, "default")
   162	    arr = np.full((M, M), float(default))
   163	    seen: set[frozenset[Pillar]] = set()
   164	    for (m, n), value in pairs.items():
   165	        if m == n:
   166	            raise ValueError(f"pair ({m.name}, {n.name}) is not a cross-pillar pair")
   167	        key = frozenset((m, n))
   168	        if key in seen:
   169	            raise ValueError(f"pair {m.name}{n.name} given twice")
   170	        seen.add(key)
   171	        v = validate_unit_interval(value, f"C[{m.name}{n.name}]")
   172	        arr[m.position, n.position] = arr[n.position, m.position] = v
   173	    np.fill_diagonal(arr, 1.0)
   174	    return arr
   175	
   176	
   177	def integration_statistic(C: np.ndarray) -> float:
   178	    """I = 2 / (M (M - 1)) sum_{m<n} C_mn with M = 6, i.e. the mean over 15 pairs (source Eq. I_t)."""
   179	    arr = validate_integration_matrix(C)
   180	    total = sum(arr[m.position, n.position] for m, n in PAIRS)
   181	    return float(2.0 / (M * (M - 1)) * total)
   182	
   183	
   184	def integration_degrees(C: np.ndarray) -> dict[Pillar, float]:
   185	    """deg_m = sum_{n != m} C_mn, so that I = (sum_m deg_m) / 30 (Part VII spec, item 5)."""
   186	    arr = validate_integration_matrix(C)
   187	    return {m: float(arr[m.position].sum() - arr[m.position, m.position]) for m in PILLARS}
   188	
   189	
   190	def hub_bound(k: int) -> float:
   191	    """Upper bound on I when every C_mn with both m, n outside a hub set of k pillars is 0.
   192	
   193	    Only pairs touching the hub can be non-zero: k(6 - k) + k(k - 1)/2 of the 15 pairs.
   194	    k = 1 gives 1/3, k = 2 gives 0.6, k = 3 gives 0.8.
   195	    """
   196	    if isinstance(k, bool) or not isinstance(k, (int, np.integer)):
   197	        raise TypeError("k must be an integer")
   198	    if not 0 <= k <= M:
   199	        raise ValueError(f"k must lie in 0..{M}")
   200	    return (k * (M - k) + k * (k - 1) / 2) / 15.0
   201	
   202	
   203	def coalition_overlap(kappa: Mapping[str, Mapping[Pillar, float]]) -> np.ndarray:
   204	    """C_mn = max over candidate coalitions S of min(kappa_m(S), kappa_n(S)) (Part II eq. overlap).
   205	
   206	    ``kappa[S][m]`` in [0, 1] is coalition S's control of pillar m; pillars missing for S
   207	    count as 0. Candidate coalitions may overlap and kappa need not be additive. The result
   208	    lies in [0, 1] and is weakly increasing in every kappa_m(S).
   209	    """
   210	    arr = np.eye(M)
   211	    if not kappa:
   212	        return arr
   213	    table: list[dict[Pillar, float]] = []
   214	    for name, row in kappa.items():
   215	        if any(not isinstance(m, Pillar) for m in row):
   216	            raise TypeError(f"kappa[{name!r}] keys must be Pillars")
   217	        table.append({m: validate_unit_interval(row.get(m, 0.0), f"kappa[{name!r}][{m.name}]")
   218	                      for m in PILLARS})
   219	    for m, n in PAIRS:
   220	        v = max(min(row[m], row[n]) for row in table)
   221	        arr[m.position, n.position] = arr[n.position, m.position] = v
   222	    return arr
   223	
   224	
   225	def coalition_integration(
   226	    shares: Mapping[Pillar, Mapping[str, float]],
   227	    coalition_of: Mapping[str, str] | None = None,
   228	) -> np.ndarray:
   229	    """Additive special case of ``coalition_overlap`` for a partition of actors into coalitions.
   230	
   231	    kappa_m(S) = s^m(S), the summed (normalized) share of S's members in pillar m. The source
   232	    describes C_mn only verbally ('the same coalition commands appointments, budgets,
   233	    sanctions or agenda in both m and n'); KB VII.3 (iv) asks Part VII to define it. Actors
   234	    absent from ``coalition_of`` form singleton coalitions.
   235	    """
   236	    coalition_of = dict(coalition_of or {})
   237	    kappa: dict[str, dict[Pillar, float]] = {}
   238	    for m in PILLARS:
   239	        if m not in shares:
   240	            raise ValueError(f"shares missing pillar {m.name}")
   241	        actors = list(shares[m])
   242	        normalized = validate_shares(shares[m])
   243	        for actor, v in zip(actors, normalized):
   244	            row = kappa.setdefault(coalition_of.get(actor, actor), {})
   245	            row[m] = min(row.get(m, 0.0) + float(v), 1.0)
   246	    return coalition_overlap(kappa)
   247	
   248	
   249	def clique_lower_bound(c: float, k: int) -> float:
   250	    """If one coalition has kappa_m(S) >= c in each of k pillars, then I >= c k (k - 1) / 30.
   251	
   252	    Those k pillars form k(k - 1)/2 pairs with C_mn >= c (Part VII addendum item 8).
   253	    """
   254	    c = validate_unit_interval(c, "c")
   255	    if isinstance(k, bool) or not isinstance(k, (int, np.integer)) or not 0 <= k <= M:
   256	        raise ValueError(f"k must be an integer in 0..{M}")
   257	    return c * k * (k - 1) / 30.0
   258	
   259	
   260	def star_upper_bound(C: np.ndarray, hub: Pillar) -> float:
   261	    """Bound (1/3) max C_mn for a pure star: every positive C_mn involves ``hub``.
   262	
   263	    Raises if the matrix is not a star around ``hub``.
   264	    """
   265	    arr = validate_integration_matrix(C)
   266	    for m, n in PAIRS:
   267	        if hub not in (m, n) and arr[m.position, n.position] > 0.0:
   268	            raise ValueError(f"C_{m.name}{n.name} > 0 does not involve hub {hub.name}")
   269	    off = arr[~np.eye(M, dtype=bool)]
   270	    return float(off.max()) / 3.0
   271	
   272	
   273	@dataclass(frozen=True)
   274	class WeightSensitivity:
   275	    """Result of ``weight_sensitivity``. ``draws`` holds U for each sampled weight vector."""
   276	
   277	    baseline: float
   278	    vertex_min: float
   279	    vertex_max: float
   280	    draws: np.ndarray
   281	
   282	    @property
   283	    def quantiles(self) -> tuple[float, float]:
   284	        """5th and 95th percentile of U across draws."""
   285	        lo, hi = np.quantile(self.draws, [0.05, 0.95])
   286	        return float(lo), float(hi)
   287	
   288	    def fraction_at_least(self, u_star: float) -> float:
   289	        """Share of weight draws with U >= u_star (robustness of a threshold call)."""
   290	        validate_unit_interval(u_star, "u_star")
   291	        return float(np.mean(self.draws >= u_star))
   292	
   293	
   294	def weight_sensitivity(
   295	    H: Mapping[Pillar, float],
   296	    Q: Mapping[Pillar, float],
   297	    weights: Mapping[Pillar, float] | None = None,
   298	    n_draws: int = 2000,
   299	    seed: int = 0,
   300	) -> WeightSensitivity:
   301	    """Sensitivity of U to the weights w (source: 'weights preregistered; sensitivity analysis').
   302	
   303	    U is linear in w, so over the whole weight simplex its exact range is
   304	    [min_m H_m (1 - Q_m), max_m H_m (1 - Q_m)] (attained at the vertices). ``draws`` samples
   305	    w uniformly on the simplex (Dirichlet(1, ..., 1)) to show the typical spread.
   306	    """
   307	    if n_draws < 1:
   308	        raise ValueError("n_draws must be positive")
   309	    baseline = unaccountable_concentration(H, Q, weights)
   310	    h = _per_pillar(H, "H")
   311	    q = _per_pillar(Q, "Q")
   312	    terms = np.array([h[m] * (1.0 - q[m]) for m in PILLARS])
   313	    rng = np.random.default_rng(seed)
   314	    w = rng.dirichlet(np.ones(M), size=n_draws)
   315	    return WeightSensitivity(
   316	        baseline=baseline,
   317	        vertex_min=float(terms.min()),
   318	        vertex_max=float(terms.max()),
   319	        draws=(w * terms).sum(axis=1),
   320	    )

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/dynamics.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Linear pillar-capacity dynamics x_{t+1} = B x_t + D z_t + eps_t (source Section 5.3).
     2	
     3	x_t = (F_t, P_t, J_t, I^cap_t, C_t, W_t) in pillar order. The source warns that stability
     4	cannot be inferred from positive links alone (negative feedback, substitution, saturation,
     5	legitimacy loss) and uses dominant eigenvalues of a local linearization as the language of
     6	persistence. Every deviation of x from its steady state decays iff the spectral radius
     7	rho(B) < 1; if rho(B) >= 1 SOME deviation (e.g. along a dominant eigenvector) does not decay,
     8	although a deviation inside a stable subspace still may.
     9	
    10	The second half implements coalition conversion dynamics (Part VII spec, item 4): a
    11	coalition's control shares y in [0,1]^6 evolve by T(y) = (1 - delta) y + (1 - y) (K y).
    12	"""
    13	
    14	from __future__ import annotations
    15	
    16	from collections.abc import Mapping
    17	from dataclasses import dataclass
    18	
    19	import numpy as np
    20	
    21	from .necessity import Graph, dependency_graph
    22	from .pillars import M, Pillar
    23	
    24	
    25	def _square(B: np.ndarray) -> np.ndarray:
    26	    arr = np.asarray(B, dtype=float)
    27	    if arr.shape != (M, M):
    28	        raise ValueError(f"B must be {M}x{M}, got {arr.shape}")
    29	    if not np.all(np.isfinite(arr)):
    30	        raise ValueError("B must be finite")
    31	    return arr
    32	
    33	
    34	def spectral_radius(B: np.ndarray) -> float:
    35	    """rho(B) = max |lambda| over eigenvalues of B."""
    36	    return float(np.max(np.abs(np.linalg.eigvals(_square(B)))))
    37	
    38	
    39	def some_deviation_persists(B: np.ndarray) -> bool:
    40	    """True iff rho(B) >= 1: x = 0 is not globally asymptotically stable for x -> B x.
    41	
    42	    Then some deviation does not decay; it does not follow that EVERY deviation persists.
    43	    """
    44	    return spectral_radius(B) >= 1.0
    45	
    46	
    47	def dependency_matrix(graph: Graph, weight: float, self_weight: float = 0.0) -> np.ndarray:
    48	    """B with B[dependent, provider] = weight for each edge, and self_weight on the diagonal.
    49	
    50	    Row = pillar at t+1, column = pillar at t, matching x_{t+1} = B x_t.
    51	    """
    52	    B = np.eye(M) * float(self_weight)
    53	    for provider, dependents in graph.items():
    54	        for dep in dependents:
    55	            B[dep.position, provider.position] = float(weight)
    56	    return B
    57	
    58	
    59	def simulate(
    60	    B: np.ndarray,
    61	    x0: np.ndarray,
    62	    steps: int,
    63	    D: np.ndarray | None = None,
    64	    z: np.ndarray | None = None,
    65	    noise_sd: float = 0.0,
    66	    seed: int | None = None,
    67	) -> np.ndarray:
    68	    """Iterate x_{t+1} = B x_t + D z_t + eps_t; returns an array of shape (steps + 1, 6).
    69	
    70	    ``z`` has shape (steps, k) and ``D`` shape (6, k); eps_t ~ N(0, noise_sd^2 I).
    71	    """
    72	    B = _square(B)
    73	    x = np.asarray(x0, dtype=float)
    74	    if x.shape != (M,):
    75	        raise ValueError(f"x0 must have shape ({M},)")
    76	    if steps < 0:
    77	        raise ValueError("steps must be non-negative")
    78	    if (D is None) != (z is None):
    79	        raise ValueError("pass both D and z, or neither")
    80	    if D is not None and z is not None:
    81	        D = np.asarray(D, dtype=float)
    82	        z = np.asarray(z, dtype=float)
    83	        if D.ndim != 2 or D.shape[0] != M or z.shape != (steps, D.shape[1]):
    84	            raise ValueError("D must be (6, k) and z must be (steps, k)")
    85	    if not np.all(np.isfinite(x)):
    86	        raise ValueError("x0 must be finite")
    87	    if D is not None and z is not None and not (np.all(np.isfinite(D)) and np.all(np.isfinite(z))):
    88	        raise ValueError("D and z must be finite")
    89	    noise_sd = float(noise_sd)
    90	    if not np.isfinite(noise_sd) or noise_sd < 0.0:
    91	        raise ValueError("noise_sd must be finite and non-negative")
    92	    rng = np.random.default_rng(seed)
    93	    path = np.empty((steps + 1, M))
    94	    path[0] = x
    95	    for t in range(steps):
    96	        x = B @ x
    97	        if D is not None and z is not None:
    98	            x = x + D @ z[t]
    99	        if noise_sd > 0.0:
   100	            x = x + rng.normal(0.0, noise_sd, size=M)
   101	        path[t + 1] = x
   102	    return path
   103	
   104	
   105	@dataclass(frozen=True)
   106	class FeedbackExample:
   107	    """Two matrices with the same positive links; only the feedback one has negative entries."""
   108	
   109	    B_positive: np.ndarray
   110	    B_feedback: np.ndarray
   111	    rho_positive: float
   112	    rho_feedback: float
   113	
   114	    @property
   115	    def same_positive_links(self) -> bool:
   116	        return bool(np.array_equal(self.B_positive > 0, self.B_feedback > 0))
   117	
   118	
   119	#: Negative feedback entries (provider, dependent) -> weight: coercion erodes legitimacy and
   120	#: depresses productive effort (source Section 5.3, 'legitimacy loss'). Illustrative values.
   121	NEGATIVE_FEEDBACK: Mapping[tuple[Pillar, Pillar], float] = {
   122	    (Pillar.C, Pillar.I): -0.5,
   123	    (Pillar.C, Pillar.W): -0.4,
   124	}
   125	
   126	
   127	def negative_feedback_example(
   128	    weight: float = 0.25,
   129	    self_weight: float = 0.6,
   130	    feedback: Mapping[tuple[Pillar, Pillar], float] = NEGATIVE_FEEDBACK,
   131	) -> FeedbackExample:
   132	    """Positive dependency links do not guarantee persistence (source Section 5.3).
   133	
   134	    With every arc of the underlying digraph of D* at ``weight`` and ``self_weight`` on the
   135	    diagonal, rho > 1. Adding negative feedback on entries that carry no positive link leaves every
   136	    positive link unchanged yet pushes rho below 1, so deviations decay.
   137	    """
   138	    B_pos = dependency_matrix(dependency_graph(), weight, self_weight)
   139	    B_fb = B_pos.copy()
   140	    for (provider, dependent), w in feedback.items():
   141	        if w >= 0.0:
   142	            raise ValueError("feedback entries must be negative")
   143	        if B_pos[dependent.position, provider.position] != 0.0:
   144	            raise ValueError("feedback must not overwrite a positive link")
   145	        B_fb[dependent.position, provider.position] = w
   146	    return FeedbackExample(B_pos, B_fb, spectral_radius(B_pos), spectral_radius(B_fb))
   147	
   148	
   149	# Coalition conversion dynamics (Part VII spec, item 4) -------------------------------------
   150	
   151	
   152	def _unit_vector(v: np.ndarray, name: str) -> np.ndarray:
   153	    arr = np.asarray(v, dtype=float)
   154	    if arr.shape != (M,):
   155	        raise ValueError(f"{name} must have shape ({M},)")
   156	    if not np.all(np.isfinite(arr)) or arr.min() < 0.0 or arr.max() > 1.0:
   157	        raise ValueError(f"{name} entries must lie in [0, 1]")
   158	    return arr
   159	
   160	
   161	def validate_conversion_matrix(K: np.ndarray, atol: float = 1e-12) -> np.ndarray:
   162	    """Check K >= 0, zero diagonal, row sums <= 1 (so T maps [0,1]^6 into itself)."""
   163	    arr = _square(K)
   164	    if arr.min() < 0.0:
   165	        raise ValueError("K must be non-negative")
   166	    if np.any(np.diag(arr) != 0.0):
   167	        raise ValueError("K must have a zero diagonal")
   168	    if arr.sum(axis=1).max() > 1.0 + atol:
   169	        raise ValueError("K row sums must be <= 1")
   170	    return arr
   171	
   172	
   173	def conversion_matrix(eta: np.ndarray, Q: np.ndarray) -> np.ndarray:
   174	    """K[n, m] = eta[n, m] (1 - Q_n): conversion of control in m into control in n.
   175	
   176	    Contestability of the receiving pillar n damps conversion into it.
   177	    """
   178	    e = _square(eta)
   179	    q = _unit_vector(Q, "Q")
   180	    if e.min() < 0.0 or np.any(np.diag(e) != 0.0):
   181	        raise ValueError("eta must be non-negative with zero diagonal")
   182	    return validate_conversion_matrix(e * (1.0 - q)[:, None])
   183	
   184	
   185	def conversion_step(y: np.ndarray, delta: np.ndarray, K: np.ndarray) -> np.ndarray:
   186	    """T(y) = (1 - delta) y + (1 - y) (K y). Maps [0,1]^6 into [0,1]^6."""
   187	    y = _unit_vector(y, "y")
   188	    d = _unit_vector(delta, "delta")
   189	    K = validate_conversion_matrix(K)
   190	    out = (1.0 - d) * y + (1.0 - y) * (K @ y)
   191	    return np.clip(out, 0.0, 1.0)  # guard against last-ulp rounding only
   192	
   193	
   194	def comparison_matrix(delta: np.ndarray, K: np.ndarray) -> np.ndarray:
   195	    """A = diag(1 - delta) + K, with 0 <= T(y) <= A y componentwise."""
   196	    return np.diag(1.0 - _unit_vector(delta, "delta")) + validate_conversion_matrix(K)
   197	
   198	
   199	def simulate_conversion(
   200	    y0: np.ndarray, delta: np.ndarray, K: np.ndarray, steps: int
   201	) -> np.ndarray:
   202	    """Iterate y_{t+1} = T(y_t); returns shape (steps + 1, 6)."""
   203	    if steps < 0:
   204	        raise ValueError("steps must be non-negative")
   205	    path = np.empty((steps + 1, M))
   206	    path[0] = _unit_vector(y0, "y0")
   207	    for t in range(steps):
   208	        path[t + 1] = conversion_step(path[t], delta, K)
   209	    return path
   210	
   211	
   212	def coalition_integration_share(y: np.ndarray) -> float:
   213	    """(1/15) sum_{m<n} min(y_m, y_n): the coalition's contribution to the integration statistic."""
   214	    y = _unit_vector(y, "y")
   215	    return float(sum(min(y[i], y[j]) for i in range(M) for j in range(i + 1, M)) / 15.0)
   216	
   217	
   218	def _is_irreducible(K: np.ndarray) -> bool:
   219	    reach = (np.eye(M) + (K > 0)).astype(float)
   220	    return bool(np.all(np.linalg.matrix_power(reach, M - 1) > 0))
   221	
   222	
   223	@dataclass(frozen=True)
   224	class Foothold:
   225	    """Foothold bound: v . y_t >= min(v . y_0, (1 - max delta)(rho - 1) / (2c)) for all t.
   226	
   227	    v is the left Perron vector of A (normalized to sum 1), c = v_max kappa / v_min^2 and
   228	    kappa the largest column sum of K. Proof sketch: v . T(y) = rho v . y - sum_n v_n y_n (K y)_n
   229	    >= rho s - c s^2 with s = v . y, and v . T(y) >= (1 - max delta) s.
   230	    """
   231	
   232	    rho: float
   233	    v: np.ndarray
   234	    c: float
   235	    bound: float
   236	
   237	
   238	def foothold_bound(y0: np.ndarray, delta: np.ndarray, K: np.ndarray) -> Foothold:
   239	    """Lower bound on v . y_t when K is irreducible, max delta < 1 and rho(A) > 1."""
   240	    y0 = _unit_vector(y0, "y0")
   241	    d = _unit_vector(delta, "delta")
   242	    K = validate_conversion_matrix(K)
   243	    if not _is_irreducible(K):
   244	        raise ValueError("the foothold bound needs an irreducible K")
   245	    if d.max() >= 1.0:
   246	        raise ValueError("the foothold bound needs max delta < 1")
   247	    A = comparison_matrix(d, K)
   248	    vals, vecs = np.linalg.eig(A.T)
   249	    k = int(np.argmax(vals.real))
   250	    rho = float(vals[k].real)
   251	    if rho <= 1.0:
   252	        raise ValueError("the foothold bound needs rho(A) > 1")
   253	    v = np.abs(vecs[:, k].real)
   254	    v = v / v.sum()
   255	    kappa = float(K.sum(axis=0).max())
   256	    c = float(v.max() * kappa / v.min() ** 2)
   257	    bound = min(float(v @ y0), (1.0 - float(d.max())) * (rho - 1.0) / (2.0 * c))
   258	    return Foothold(rho=rho, v=v, c=c, bound=bound)

2026-10-22T17:32:05.280077Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '1,220p'" in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/capture.py | sed -n '221,430p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Structural necessity: Proposition A and the pillar dependency hypergraph (Part VII Theorem A).
     2	
     3	Theorem A (notation.md CENTRAL THESIS; KB Section 4): if a governance system G persists and
     4	satisfies Ax1..Ax6, then every pillar in M is implemented in G, and the dependency relations
     5	D0 are present. Implementation is role-level, not institution-level
     6	(Hempel 1959): a function may be held by a formal institution, fused with other functions
     7	inside one institution, or exercised informally (gossip and shunning as C, mediators as J).
     8	
     9	What this module does and does not do. It cannot prove Theorem A. It encodes the lemma schema
    10	'Ax_k + persistence => some practice solves problem_k' and checks it against coded cases. The
    11	role map is DERIVED from independently coded practices, never declared, so a persistent case
    12	that satisfies all six axioms yet has no practice for some problem, or lacks a D0 relation, is
    13	reported as a counterexample (the falsifier required by KB Section 4.4).
    14	
    15	Dependencies form an AND/OR hypergraph GENERATED from the axioms (Part VII revised dependency
    16	spec). A hyperarc (T, h) is written provider(s) -> dependent and means: h needs an output of
    17	AT LEAST ONE member of T. Incidence Inc(k, m), 'the problem of Ax_k arises about the inputs or
    18	rules of pillar m', generates the arc pillar(k) -> m. The core set D* comes from Ax6 (W -> m),
    19	Part III Prop 3.6 ({I, C} -> J), Ax4 with Part I Def 2.2(b) (I -> F), and the incidence axioms
    20	X1 (F -> W), X2 (P -> F), X3 (J -> F), X5 (C -> F). Removing an axiom removes every arc it
    21	generates. Two connectivity notions are computed:
    22	  (a) the underlying digraph (each (T, h) replaced by arcs t -> h) is strongly connected;
    23	  (b) cascade completeness: cl({n}) = M for every n, where cl(S) is the least superset of S
    24	      such that T subset of cl(S) implies h in cl(S) for every hyperarc (T, h).
    25	Interdependence = (a) and (b). It is a separate predicate from Theorem A's Struct(G) and is
    26	claimed for every system satisfying the extended axiom set; a system coding an incidence as
    27	absent while its premises hold is reported as an interdependence counterexample.
    28	"""
    29	
    30	from __future__ import annotations
    31	
    32	from collections.abc import Iterable, Mapping
    33	from dataclasses import dataclass, field
    34	from typing import Literal
    35	
    36	from .pillars import AXIOM_TO_PILLAR, PILLAR_TO_AXIOM, PILLARS, Axiom, IncidenceAxiom, Pillar
    37	
    38	RealizedForm = Literal["formal institution", "fused", "informal/minimal"]
    39	FORMAL: RealizedForm = "formal institution"
    40	FUSED: RealizedForm = "fused"
    41	INFORMAL: RealizedForm = "informal/minimal"
    42	
    43	# Dependency hypergraph primitives ----------------------------------------------------------
    44	
    45	#: A hyperarc key (T, h): tail set T, head h.
    46	ArcKey = tuple[frozenset[Pillar], Pillar]
    47	Graph = Mapping[Pillar, Iterable[Pillar]]
    48	AnyAxiom = Axiom | IncidenceAxiom
    49	
    50	#: Ax1..Ax6 plus the incidence axioms X1, X2, X3, X5 (Part VII extended axiom set).
    51	EXTENDED_AXIOMS: frozenset[AnyAxiom] = frozenset(Axiom) | frozenset(IncidenceAxiom)
    52	
    53	
    54	def arc_key(tail: Pillar | Iterable[Pillar], head: Pillar) -> ArcKey:
    55	    """Normalize (T, h) to an ArcKey, validating T non-empty, h a Pillar and h not in T."""
    56	    t = frozenset((tail,) if isinstance(tail, Pillar) else tail)
    57	    if not t or not all(isinstance(m, Pillar) for m in t) or not isinstance(head, Pillar):
    58	        raise TypeError("a hyperarc needs a non-empty tail of Pillars and a Pillar head")
    59	    if head in t:
    60	        raise ValueError(f"head {head.name} may not belong to its own tail")
    61	    return t, head
    62	
    63	
    64	def _keys(arcs: Iterable[DependencyRule | ArcKey]) -> frozenset[ArcKey]:
    65	    return frozenset(a.key if isinstance(a, DependencyRule) else arc_key(*a) for a in arcs)
    66	
    67	
    68	def underlying_digraph(arcs: Iterable[DependencyRule | ArcKey]) -> dict[Pillar, frozenset[Pillar]]:
    69	    """Replace each hyperarc (T, h) by the arcs t -> h; adjacency over all six pillars."""
    70	    adj: dict[Pillar, set[Pillar]] = {m: set() for m in PILLARS}
    71	    for tail, head in _keys(arcs):
    72	        for t in tail:
    73	            adj[t].add(head)
    74	    return {m: frozenset(v) for m, v in adj.items()}
    75	
    76	
    77	def cascade_closure(
    78	    arcs: Iterable[DependencyRule | ArcKey], start: Iterable[Pillar]
    79	) -> frozenset[Pillar]:
    80	    """cl(S): least superset of S with T subset of cl(S) => h in cl(S) for every (T, h).
    81	
    82	    Read as a failure cascade: h fails once every provider in its tail has failed.
    83	    """
    84	    keys = _keys(arcs)
    85	    closed = set(start)
    86	    changed = True
    87	    while changed:
    88	        changed = False
    89	        for tail, head in keys:
    90	            if head not in closed and tail <= closed:
    91	                closed.add(head)
    92	                changed = True
    93	    return frozenset(closed)
    94	
    95	
    96	def is_cascade_complete(
    97	    arcs: Iterable[DependencyRule | ArcKey], nodes: Iterable[Pillar] = PILLARS
    98	) -> bool:
    99	    """True iff cl({n}) contains every node, for every node n (restricted to ``nodes``)."""
   100	    keep = frozenset(nodes)
   101	    if not keep:
   102	        return False
   103	    inside = [(t, h) for t, h in _keys(arcs) if h in keep and t <= keep]
   104	    return all(cascade_closure(inside, {n}) >= keep for n in keep)
   105	
   106	
   107	def _nodes(graph: Graph) -> set[Pillar]:
   108	    nodes = set(graph)
   109	    for targets in graph.values():
   110	        nodes.update(targets)
   111	    return nodes
   112	
   113	
   114	def _reach(graph: Mapping[Pillar, frozenset[Pillar]], start: Pillar) -> set[Pillar]:
   115	    seen = {start}
   116	    stack = [start]
   117	    while stack:
   118	        for nxt in graph.get(stack.pop(), frozenset()):
   119	            if nxt not in seen:
   120	                seen.add(nxt)
   121	                stack.append(nxt)
   122	    return seen
   123	
   124	
   125	def is_strongly_connected(graph: Graph, nodes: Iterable[Pillar] | None = None) -> bool:
   126	    """True iff every node of the graph is reachable from every other node.
   127	
   128	    ``nodes`` restricts the graph to an induced subgraph (default: all nodes that appear).
   129	    The empty graph is not strongly connected; a single node is.
   130	    """
   131	    keep = set(nodes) if nodes is not None else _nodes(graph)
   132	    if not keep:
   133	        return False
   134	    fwd: dict[Pillar, frozenset[Pillar]] = {
   135	        u: frozenset(v for v in graph.get(u, ()) if v in keep) for u in keep
   136	    }
   137	    rev: dict[Pillar, set[Pillar]] = {u: set() for u in keep}
   138	    for u, vs in fwd.items():
   139	        for v in vs:
   140	            rev[v].add(u)
   141	    start = next(iter(keep))
   142	    rev_f = {u: frozenset(v) for u, v in rev.items()}
   143	    return _reach(fwd, start) == keep and _reach(rev_f, start) == keep
   144	
   145	
   146	def critical_edges(graph: Graph) -> list[tuple[Pillar, Pillar]]:
   147	    """Edges whose single removal breaks strong connectivity (empty if not connected)."""
   148	    nodes = _nodes(graph)
   149	    base = {u: frozenset(graph.get(u, ())) for u in nodes}
   150	    if not is_strongly_connected(base):
   151	        return []
   152	    out = []
   153	    for u in PILLARS:
   154	        for v in sorted(base.get(u, ()), key=lambda p: p.position):
   155	            pruned = dict(base)
   156	            pruned[u] = base[u] - {v}
   157	            if not is_strongly_connected(pruned, nodes):
   158	                out.append((u, v))
   159	    return out
   160	
   161	
   162	def sinks_and_sources(graph: Graph) -> tuple[frozenset[Pillar], frozenset[Pillar]]:
   163	    """Pillars with no outgoing edge (sinks) and with no incoming edge (sources)."""
   164	    nodes = _nodes(graph)
   165	    has_out = {u for u in nodes if any(True for _ in graph.get(u, ()))}
   166	    has_in = {v for u in nodes for v in graph.get(u, ())}
   167	    return frozenset(nodes - has_out), frozenset(nodes - has_in)
   168	
   169	
   170	# Axiom-generated dependency rules (Part VII revised dependency spec) ----------------------
   171	
   172	
   173	@dataclass(frozen=True)
   174	class DependencyRule:
   175	    """A hyperarc (T, h) generated when every premise in ``requires`` holds.
   176	
   177	    h needs an output of AT LEAST ONE member of T (provider(s) -> dependent). ``incidence`` is
   178	    the incidence Inc(k, m) the rule instantiates (the problem of Ax_k arises about pillar m's
   179	    inputs or rules, giving arc pillar(k) -> m), or None for a rule that is not an incidence.
   180	    ``core`` marks membership of D*; non-core rules are reported, not needed.
   181	    """
   182	
   183	    tail: frozenset[Pillar]
   184	    head: Pillar
   185	    premise: str
   186	    requires: frozenset[AnyAxiom]
   187	    source: str
   188	    core: bool
   189	    incidence: tuple[Axiom, Pillar] | None = None
   190	
   191	    def __post_init__(self) -> None:
   192	        tail, _ = arc_key(self.tail, self.head)
   193	        requires = frozenset(self.requires)
   194	        if not requires or any(not isinstance(a, (Axiom, IncidenceAxiom)) for a in requires):
   195	            raise ValueError("a dependency rule needs at least one axiom premise")
   196	        if self.incidence is not None:
   197	            axiom, target = self.incidence
   198	            if tail != frozenset({axiom.pillar}) or target is not self.head:
   199	                raise ValueError("an incidence Inc(k, m) generates exactly pillar(k) -> m")
   200	            if axiom not in requires:
   201	                raise ValueError("an incidence rule must require its own axiom")
   202	        object.__setattr__(self, "tail", tail)
   203	        object.__setattr__(self, "requires", requires)
   204	
   205	    @property
   206	    def key(self) -> ArcKey:
   207	        return self.tail, self.head
   208	
   209	
   210	def _inc(axiom: Axiom, target: Pillar, premise: str, requires: Iterable[AnyAxiom],
   211	         source: str, core: bool = True) -> DependencyRule:
   212	    return DependencyRule(frozenset({axiom.pillar}), target, premise,
   213	                          frozenset(requires) | {axiom}, source, core, (axiom, target))
   214	
   215	
   216	_P, _A, _X = Pillar, Axiom, IncidenceAxiom
   217	
   218	#: D*: the core rules. Under Ax1..Ax6 plus X1, X2, X3, X5 they generate a strongly connected,
   219	#: cascade-complete hypergraph (Part VII revised dependency spec).
   220	CORE_RULES: tuple[DependencyRule, ...] = (

 succeeded in 0ms:
   221	def _layer_from(holders: list[str], actors: list[str], weight: float) -> np.ndarray:
   222	    idx = {a: k for k, a in enumerate(actors)}
   223	    arr = np.zeros((len(actors), len(actors)))
   224	    for h in holders:
   225	        for a in actors:
   226	            if a != h:
   227	                arr[idx[h], idx[a]] = weight
   228	    return arr
   229	
   230	
   231	def plural_polity(n_per_pillar: int = 5, q: float = 0.9) -> Polity:
   232	    """G1, accountable pluralism: each pillar held by n independent organizations.
   233	
   234	    Holders are disjoint across pillars, so every coalition overlap is 0 and C_mn = 0.
   235	    """
   236	    if n_per_pillar < 1:
   237	        raise ValueError("n_per_pillar must be positive")
   238	    q = validate_unit_interval(q, "q")
   239	    holders = {m: [f"{m.label}-org-{k}" for k in range(n_per_pillar)] for m in PILLARS}
   240	    actors = [a for m in PILLARS for a in holders[m]]
   241	    net = MultiplexNetwork(
   242	        actors=tuple(actors),
   243	        layers={m: _layer_from(holders[m], actors, 0.5) for m in PILLARS},
   244	        roles={a: {m} for m in PILLARS for a in holders[m]},
   245	    )
   246	    shares = {m: net.out_strength_shares(m) for m in PILLARS}
   247	    return Polity(
   248	        name="G1 accountable pluralism",
   249	        system=formal_system("G1 accountable pluralism", holders),
   250	        shares=shares,
   251	        contestability={m: q for m in PILLARS},
   252	        integration=coalition_integration(shares),
   253	    )
   254	
   255	
   256	def fused_polity(n_subordinate: int = 5, q: float = 0.0) -> Polity:
   257	    """G2, fused capture: one coalition holds all six pillars with Q = q, one evidenced link.
   258	
   259	    H_m = 1 and C_mn = 1, so U = 1 - q and I = 1; with the default q = 0 both indices reach
   260	    their maximum and meet every admissible threshold pair (u*, i*) in [0, 1]^2.
   261	    """
   262	    if n_subordinate < 1:
   263	        raise ValueError("n_subordinate must be positive")
   264	    q = validate_unit_interval(q, "q")
   265	    core = "ruling coalition"
   266	    actors = [core] + [f"subordinate-{k}" for k in range(n_subordinate)]
   267	    net = MultiplexNetwork(
   268	        actors=tuple(actors),
   269	        layers={m: _layer_from([core], actors, 1.0) for m in PILLARS},
   270	        roles={core: set(PILLARS)},
   271	    )
   272	    shares = {m: net.out_strength_shares(m) for m in PILLARS}
   273	    link = CaptureLink(
   274	        source=core, target="subordinate-0", pillar=Pillar.J,
   275	        privileged_access=True, weakens_accountability=True, material_evidence=True,
   276	        evidence="synthetic: appointment record ties removal of reviewing judges to ruling",
   277	    )
   278	    return Polity(
   279	        name="G2 fused capture",
   280	        system=formal_system("G2 fused capture", {m: [core] for m in PILLARS}),
   281	        shares=shares,
   282	        contestability={m: q for m in PILLARS},
   283	        integration=coalition_integration(shares),
   284	        capture_links=(link,),
   285	    )
   286	
   287	
   288	@dataclass(frozen=True)
   289	class CounterModel:
   290	    plural: Assessment
   291	    fused: Assessment
   292	
   293	    @property
   294	    def demonstrates_non_implication(self) -> bool:
   295	        """Both satisfy A; only G2 satisfies B. Hence A does not imply B."""
   296	        return (
   297	            self.plural.prop_a.holds
   298	            and self.fused.prop_a.holds
   299	            and not self.plural.prop_b.holds
   300	            and self.fused.prop_b.holds
   301	        )
   302	
   303	
   304	def a_does_not_imply_b(thresholds: CaptureThresholds = CaptureThresholds()) -> CounterModel:
   305	    """Constructive counter-model for Part VII Theorem 2 (KB Section 4.3 item 4).
   306	
   307	    G1 has U = (1/5)(1 - 0.9) = 0.02, I = 0 and no capture link; G2 has U = 1, I = 1 and one
   308	    evidenced link. Both pass the Theorem A check (six pillars realized, D0 generated) and
   309	    both are interdependent, so interdependence does not imply capture either. G1 fails B for every thresholds pair because it has no link (and its indices lie
   310	    below any u* > 0.02, i* > 0); G2 meets B for every thresholds pair in [0, 1]^2.
   311	    """
   312	    return CounterModel(
   313	        plural=assess(plural_polity(), thresholds),
   314	        fused=assess(fused_polity(), thresholds),
   315	    )
   316	
   317	
   318	# Corner attainability (Part VII addendum item 9) --------------------------------------------
   319	
   320	
   321	def grand_coalition_polity(n_members: int = 5) -> Polity:
   322	    """(U, I) = (0, 1): one consensus coalition holds every pillar in equal shares, Q = 1."""
   323	    if n_members < 1:
   324	        raise ValueError("n_members must be positive")
   325	    members = [f"member-{k}" for k in range(n_members)]
   326	    shares = {m: {a: 1.0 / n_members for a in members} for m in PILLARS}
   327	    return Polity(
   328	        name="consensus grand coalition",
   329	        system=formal_system("consensus grand coalition", {m: members for m in PILLARS}),
   330	        shares=shares,
   331	        contestability={m: 1.0 for m in PILLARS},
   332	        integration=coalition_integration(shares, {a: "grand coalition" for a in members}),
   333	    )
   334	
   335	
   336	def separate_monopolies_polity() -> Polity:
   337	    """(U, I) = (1, 0): a different monopolist per pillar, Q = 0, no shared coalition."""
   338	    holders = {m: [f"{m.label} monopolist"] for m in PILLARS}
   339	    shares = {m: {holders[m][0]: 1.0} for m in PILLARS}
   340	    return Polity(
   341	        name="separate monopolies",
   342	        system=formal_system("separate monopolies", holders),
   343	        shares=shares,
   344	        contestability={m: 0.0 for m in PILLARS},
   345	        integration=coalition_integration(shares),
   346	    )
   347	
   348	
   349	def corner_polities() -> dict[tuple[int, int], Polity]:
   350	    """Four polities satisfying A that attain the corners of the (U, I) square.
   351	
   352	    Only the (1, 1) corner carries a capture link, so U and I alone never decide B.
   353	    """
   354	    return {
   355	        (0, 0): plural_polity(q=1.0),
   356	        (1, 1): fused_polity(q=0.0),
   357	        (0, 1): grand_coalition_polity(),
   358	        (1, 0): separate_monopolies_polity(),
   359	    }

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '221,500p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   221	    *(_inc(_A.Ax6, m, "Ax6", (), "practitioners consume produced resources (Part VI)")
   222	      for m in (_P.F, _P.P, _P.J, _P.I, _P.C)),
   223	    DependencyRule(frozenset({_P.I, _P.C}), _P.J, "Part III Prop 3.6",
   224	                   frozenset({_A.Ax3, _A.Ax4, _A.Ax5}),
   225	                   "rulings settle disputes if recognized or if enforced", core=True),
   226	    _inc(_A.Ax4, _P.F, "Ax4 + Part I Def 2.2(b)", (),
   227	         "members must anticipate the settlement procedure"),
   228	    _inc(_A.Ax1, _P.W, "X1", (_X.X1,), "contested productive inputs (Part I)"),
   229	    _inc(_A.Ax2, _P.F, "X2", (_X.X2,), "changing environment hits allocation rules (Part II Ass 3.2)"),
   230	    _inc(_A.Ax3, _P.F, "X3", (_X.X3,), "open-textured allocation rules (Part III Thm 3.3)"),
   231	    _inc(_A.Ax5, _P.F, "X5", (_X.X5,), "tempting allocation rules (Part V Thm 3.4)"),
   232	)
   233	
   234	#: Further rules: reported, not needed for interdependence. Each rests on a premise beyond
   235	#: the extended axiom set (stated in ``premise``), so none is generated for a system.
   236	FURTHER_RULES: tuple[DependencyRule, ...] = (
   237	    _inc(_A.Ax4, _P.P, "X2 + Ax4", (_A.Ax2, _X.X2), "recognition of rule change", core=False),
   238	    _inc(_A.Ax2, _P.J, "X2 + Ax4", (_A.Ax4, _X.X2), "new rules to interpret", core=False),
   239	    _inc(_A.Ax2, _P.I, "X2 + Ax4", (_A.Ax4, _X.X2), "new rules to be made common knowledge",
   240	         core=False),
   241	    _inc(_A.Ax3, _P.P, "precedent (Hart)", (), "interpretation feeds rule change", core=False),
   242	    DependencyRule(frozenset({_P.F, _P.I}), _P.C, "Part V Cor 3.7 conditions",
   243	                   frozenset({_A.Ax1, _A.Ax4, _A.Ax5}),
   244	                   "costly public-good sanctions at large n, no higher-order sanctions",
   245	                   core=False),
   246	)
   247	
   248	D_STAR_KEYS: frozenset[ArcKey] = frozenset(r.key for r in CORE_RULES)
   249	#: D0: the relations Theorem A requires (W -> m for m != W, and the OR-hyperarc {I, C} -> J).
   250	D0_KEYS: frozenset[ArcKey] = frozenset(
   251	    r.key for r in CORE_RULES if r.premise in {"Ax6", "Part III Prop 3.6"}
   252	)
   253	
   254	#: The six single arcs named in the original model brief (kept for comparison only).
   255	BRIEF_ARCS: frozenset[ArcKey] = frozenset(
   256	    arc_key(t, h) for t, h in [(_P.W, _P.C), (_P.P, _P.J), (_P.I, _P.P), (_P.J, _P.F),
   257	                               (_P.F, _P.W), (_P.W, _P.I)]
   258	)
   259	
   260	
   261	def rules_holding(
   262	    axioms: Iterable[AnyAxiom], rules: Iterable[DependencyRule] = CORE_RULES
   263	) -> tuple[DependencyRule, ...]:
   264	    """The rules whose premises all hold under ``axioms``."""
   265	    held = frozenset(axioms)
   266	    return tuple(r for r in rules if r.requires <= held)
   267	
   268	
   269	def dependency_graph(axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS) -> dict[Pillar, frozenset[Pillar]]:
   270	    """Underlying digraph of the core rules generated under ``axioms`` (default: all)."""
   271	    return underlying_digraph(rules_holding(axioms))
   272	
   273	
   274	# Governance systems ------------------------------------------------------------------------
   275	
   276	
   277	@dataclass(frozen=True)
   278	class Practice:
   279	    """A regular activity that discharges the problem generated by axiom ``solves``.
   280	
   281	    ``formal`` is True when the activity is attached to a designated office or organization.
   282	    ``source`` holds the citation key(s) supporting the coding.
   283	    """
   284	
   285	    description: str
   286	    solves: Axiom
   287	    holders: frozenset[str]
   288	    formal: bool = False
   289	    source: str = ""
   290	
   291	    def __post_init__(self) -> None:
   292	        if not isinstance(self.solves, Axiom):
   293	            raise TypeError("Practice.solves must be an Axiom")
   294	        holders = frozenset(self.holders)
   295	        if not holders or any(not isinstance(h, str) or not h for h in holders):
   296	            raise ValueError("a practice needs at least one named holder")
   297	        if not self.description.strip():
   298	            raise ValueError("a practice needs a description")
   299	        object.__setattr__(self, "holders", holders)
   300	
   301	    @property
   302	    def pillar(self) -> Pillar:
   303	        return AXIOM_TO_PILLAR[self.solves]
   304	
   305	
   306	@dataclass(frozen=True)
   307	class GovernanceSystem:
   308	    """A collective that makes and enforces collective decisions (KB Section 4.1).
   309	
   310	    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
   311	    over the period studied; it may include the incidence axioms X1, X2, X3, X5. Both are
   312	    coded independently of ``practices``. Dependencies are generated from ``axioms``;
   313	    ``absent_incidences`` records incidences Inc(k, m) OBSERVED not to arise in this system,
   314	    which suppress the arcs they would generate (the route by which a case can falsify D0 or
   315	    interdependence).
   316	    """
   317	
   318	    name: str
   319	    persistent: bool
   320	    axioms: frozenset[AnyAxiom]
   321	    practices: tuple[Practice, ...] = ()
   322	    absent_incidences: frozenset[tuple[Axiom, Pillar]] = frozenset()
   323	    note: str = ""
   324	
   325	    def __post_init__(self) -> None:
   326	        if not isinstance(self.persistent, bool):
   327	            raise TypeError("persistent must be a bool")
   328	        axioms = frozenset(self.axioms)
   329	        if any(not isinstance(a, (Axiom, IncidenceAxiom)) for a in axioms):
   330	            raise TypeError("axioms must be Axiom or IncidenceAxiom members")
   331	        practices = tuple(self.practices)
   332	        if any(not isinstance(p, Practice) for p in practices):
   333	            raise TypeError("practices must be Practice instances")
   334	        object.__setattr__(self, "axioms", axioms)
   335	        object.__setattr__(self, "practices", practices)
   336	        absent = frozenset(tuple(i) for i in self.absent_incidences)
   337	        if any(len(i) != 2 or not isinstance(i[0], Axiom) or not isinstance(i[1], Pillar)
   338	               for i in absent):
   339	            raise TypeError("absent_incidences must be (Axiom, Pillar) pairs")
   340	        object.__setattr__(self, "absent_incidences", absent)
   341	
   342	    def holds(self, axiom: AnyAxiom) -> bool:
   343	        """Predicate for one axiom (Ax1..Ax6 or an incidence axiom X_k)."""
   344	        return axiom in self.axioms
   345	
   346	    @property
   347	    def all_axioms_hold(self) -> bool:
   348	        """Ax1..Ax6 all hold (the antecedent of Theorem A)."""
   349	        return all(self.holds(a) for a in Axiom)
   350	
   351	    @property
   352	    def extended_axioms_hold(self) -> bool:
   353	        """Ax1..Ax6 and X1, X2, X3, X5 all hold (the antecedent of interdependence)."""
   354	        return EXTENDED_AXIOMS <= self.axioms
   355	
   356	
   357	def generate_dependencies(
   358	    system: GovernanceSystem, rules: Iterable[DependencyRule] = CORE_RULES
   359	) -> frozenset[ArcKey]:
   360	    """Hyperarcs generated in ``system``: rules whose premises hold, minus absent incidences."""
   361	    return frozenset(
   362	        r.key for r in rules_holding(system.axioms, rules)
   363	        if r.incidence is None or r.incidence not in system.absent_incidences
   364	    )
   365	
   366	
   367	def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
   368	    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
   369	    roles: dict[str, set[Pillar]] = {}
   370	    for p in system.practices:
   371	        for h in p.holders:
   372	            roles.setdefault(h, set()).add(p.pillar)
   373	    return {h: frozenset(ps) for h, ps in roles.items()}
   374	
   375	
   376	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   377	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   378	
   379	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   380	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   381	    """
   382	    practices = [p for p in system.practices if p.pillar is pillar]
   383	    if not practices:
   384	        return None
   385	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   386	    if not formal_holders:
   387	        return INFORMAL
   388	    formal_roles: dict[str, set[Pillar]] = {}
   389	    for p in system.practices:
   390	        if p.formal:
   391	            for h in p.holders:
   392	                formal_roles.setdefault(h, set()).add(p.pillar)
   393	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   394	        return FUSED
   395	    return FORMAL
   396	
   397	
   398	@dataclass(frozen=True)
   399	class Derivation:
   400	    """Result of the lemma for one axiom: required pillar and its realized form."""
   401	
   402	    axiom: Axiom
   403	    pillar: Pillar
   404	    form: RealizedForm | None
   405	    practices: tuple[Practice, ...]
   406	
   407	    @property
   408	    def realized(self) -> bool:
   409	        return self.form is not None
   410	
   411	
   412	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   413	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   414	
   415	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   416	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   417	    """
   418	    out: dict[Axiom, Derivation] = {}
   419	    for axiom in Axiom:
   420	        if not system.holds(axiom):
   421	            continue
   422	        pillar = AXIOM_TO_PILLAR[axiom]
   423	        out[axiom] = Derivation(
   424	            axiom=axiom,
   425	            pillar=pillar,
   426	            form=realized_form(system, pillar),
   427	            practices=tuple(p for p in system.practices if p.solves is axiom),
   428	        )
   429	    return out
   430	
   431	
   432	# Proposition A and interdependence --------------------------------------------------------
   433	
   434	
   435	@dataclass(frozen=True)
   436	class PropositionAResult:
   437	    """Outcome of checking Theorem A and interdependence on one coded system.
   438	
   439	    ``holds`` is Struct(G): all six pillars realized AND every D0 relation generated.
   440	    ``counterexample`` is True when Theorem A's antecedent holds (persistent, Ax1..Ax6) but
   441	    Struct(G) fails.
   442	
   443	    ``interdependent`` is the separate structural predicate: all six pillars realized and the
   444	    generated hypergraph both strongly connected (underlying digraph) and cascade-complete.
   445	    ``interdependence_counterexample`` is True when the system is persistent, satisfies the
   446	    extended axiom set, yet is not interdependent.
   447	    """
   448	
   449	    system: str
   450	    antecedent: bool
   451	    realized: frozenset[Pillar]
   452	    missing: frozenset[Pillar]
   453	    dependencies: frozenset[ArcKey]
   454	    missing_dependencies: frozenset[ArcKey]
   455	    strongly_connected: bool
   456	    cascade_complete: bool
   457	    holds: bool
   458	    interdependence_antecedent: bool
   459	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   460	
   461	    @property
   462	    def counterexample(self) -> bool:
   463	        return self.antecedent and not self.holds
   464	
   465	    @property
   466	    def interdependent(self) -> bool:
   467	        return not self.missing and self.strongly_connected and self.cascade_complete
   468	
   469	    @property
   470	    def interdependence_counterexample(self) -> bool:
   471	        return self.interdependence_antecedent and not self.interdependent
   472	
   473	
   474	def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
   475	    """Check Theorem A and interdependence on ``system`` (Part VII; KB Section 4.3).
   476	
   477	    A D0 relation is demanded when its head and every tail member are realized.
   478	    """
   479	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   480	    deps = generate_dependencies(system)
   481	    needed = frozenset((t, h) for t, h in D0_KEYS if h in realized and t <= realized)
   482	    missing_deps = needed - deps
   483	    return PropositionAResult(
   484	        system=system.name,
   485	        antecedent=system.persistent and system.all_axioms_hold,
   486	        realized=realized,
   487	        missing=frozenset(PILLARS) - realized,
   488	        dependencies=deps,
   489	        missing_dependencies=missing_deps,
   490	        strongly_connected=is_strongly_connected(underlying_digraph(deps), realized),
   491	        cascade_complete=is_cascade_complete(deps, realized),
   492	        holds=realized == frozenset(PILLARS) and not missing_deps,
   493	        interdependence_antecedent=system.persistent and system.extended_axioms_hold,
   494	        derivations=derive_functions(system),
   495	    )
   496	
   497	
   498	def formal_system(
   499	    name: str,
   500	    holders: Mapping[Pillar, Iterable[str]],

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/capture.py | sed -n '1,220p'" in /Users/mlong/Documents/Development/the-beast-system
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
    17	    WeightSensitivity,
    18	    coalition_integration,
    19	    control_shares,
    20	    hhi,
    21	    integration_statistic,
    22	    unaccountable_concentration,
    23	    validate_integration_matrix,
    24	    validate_unit_interval,
    25	    validate_weights,
    26	    weight_sensitivity,
    27	)
    28	from .necessity import (
    29	    GovernanceSystem,
    30	    PropositionAResult,
    31	    check_proposition_a,
    32	    formal_system,
    33	    role_map,
    34	)
    35	from .network import MultiplexNetwork
    36	from .pillars import PILLARS, Pillar
    37	
    38	
    39	@dataclass(frozen=True)
    40	class CaptureLink:
    41	    """Capture link (i -> j, m) (source Section 5; notation.md 'Capture link').
    42	
    43	    All three conditions are required: (i) privileged access or discretion; (ii) the privilege
    44	    weakens otherwise applicable accountability or contestability; (iii) material evidence
    45	    links the asymmetry to an institutional output. A disclosure-compliant donor meeting is
    46	    not automatically capture. Claiming (iii) requires citing the evidence.
    47	    """
    48	
    49	    source: str
    50	    target: str
    51	    pillar: Pillar
    52	    privileged_access: bool
    53	    weakens_accountability: bool
    54	    material_evidence: bool
    55	    evidence: str = ""
    56	
    57	    def __post_init__(self) -> None:
    58	        for end in (self.source, self.target):
    59	            if not isinstance(end, str) or not end:
    60	                raise ValueError("capture link endpoints must be named")
    61	        if not isinstance(self.pillar, Pillar):
    62	            raise TypeError("capture link pillar must be a Pillar")
    63	        for flag in ("privileged_access", "weakens_accountability", "material_evidence"):
    64	            if not isinstance(getattr(self, flag), bool):
    65	                raise TypeError(f"{flag} must be a bool")
    66	        if not isinstance(self.evidence, str):
    67	            raise TypeError("evidence must be a string")
    68	        if self.material_evidence and not self.evidence.strip():
    69	            raise ValueError("condition (iii) requires a citation of the material evidence")
    70	
    71	    @property
    72	    def holds(self) -> bool:
    73	        return self.privileged_access and self.weakens_accountability and self.material_evidence
    74	
    75	
    76	def is_capture_link(link: CaptureLink) -> bool:
    77	    """Conjunction of the source's three conditions."""
    78	    return link.holds
    79	
    80	
    81	@dataclass(frozen=True)
    82	class CaptureThresholds:
    83	    """Thresholds u*, i* for Proposition B. Illustrative defaults; preregister in applications."""
    84	
    85	    u_star: float = 0.4
    86	    i_star: float = 0.5
    87	
    88	    def __post_init__(self) -> None:
    89	        object.__setattr__(self, "u_star", validate_unit_interval(self.u_star, "u_star"))
    90	        object.__setattr__(self, "i_star", validate_unit_interval(self.i_star, "i_star"))
    91	
    92	
    93	@dataclass(frozen=True)
    94	class PropositionBResult:
    95	    u_high: bool
    96	    i_high: bool
    97	    n_links: int
    98	
    99	    @property
   100	    def thresholds_met(self) -> bool:
   101	        return self.u_high and self.i_high
   102	
   103	    @property
   104	    def holds(self) -> bool:
   105	        return self.thresholds_met and self.n_links > 0
   106	
   107	
   108	def proposition_b(
   109	    U: float,
   110	    I: float,  # noqa: E741  (integration statistic, math cal I)
   111	    links: tuple[CaptureLink, ...] | list[CaptureLink],
   112	    thresholds: CaptureThresholds = CaptureThresholds(),
   113	) -> PropositionBResult:
   114	    """Proposition B: U >= u* AND I >= i* AND some capture link holds."""
   115	    U = validate_unit_interval(U, "U")
   116	    I = validate_unit_interval(I, "I")  # noqa: E741
   117	    return PropositionBResult(
   118	        u_high=U >= thresholds.u_star,
   119	        i_high=I >= thresholds.i_star,
   120	        n_links=sum(1 for link in links if is_capture_link(link)),
   121	    )
   122	
   123	
   124	@dataclass(frozen=True)
   125	class Polity:
   126	    """A coded polity: governance system (for A) plus index inputs (for B).
   127	
   128	    ``shares[m]`` holds raw non-negative control weights per actor, normalized to s^m.
   129	    ``weights`` are the preregistered U weights (None means the equal-weight preregistration
   130	    1/M); ``assess`` always adds a weight-sensitivity analysis. Capture-link endpoints must be
   131	    actors of the polity (share holders or holders of coded practices).
   132	    """
   133	
   134	    name: str
   135	    system: GovernanceSystem
   136	    shares: Mapping[Pillar, Mapping[str, float]]
   137	    contestability: Mapping[Pillar, float]
   138	    integration: np.ndarray
   139	    capture_links: tuple[CaptureLink, ...] = ()
   140	    weights: Mapping[Pillar, float] | None = None
   141	    normalized_shares: Mapping[Pillar, Mapping[str, float]] = field(init=False, repr=False)
   142	
   143	    def __post_init__(self) -> None:
   144	        if set(self.shares) != set(PILLARS):
   145	            raise ValueError("shares must cover every pillar")
   146	        norm = {m: control_shares(self.shares[m]) for m in PILLARS}
   147	        object.__setattr__(self, "normalized_shares", norm)
   148	        object.__setattr__(self, "integration", validate_integration_matrix(self.integration))
   149	        object.__setattr__(self, "weights", validate_weights(self.weights))
   150	        links = tuple(self.capture_links)
   151	        if any(not isinstance(link, CaptureLink) for link in links):
   152	            raise TypeError("capture_links must be CaptureLink instances")
   153	        actors = self.actors
   154	        for link in links:
   155	            for end in (link.source, link.target):
   156	                if end not in actors:
   157	                    raise ValueError(f"capture link endpoint {end!r} is not an actor of {self.name}")
   158	        object.__setattr__(self, "capture_links", links)
   159	        # Fail early on bad Q.
   160	        unaccountable_concentration(self.H, self.contestability, self.weights)
   161	
   162	    @property
   163	    def actors(self) -> frozenset[str]:
   164	        """V: every share holder plus every holder of a coded practice."""
   165	        held = {a for m in PILLARS for a in self.shares[m]}
   166	        return frozenset(held | set(role_map(self.system)))
   167	
   168	    @property
   169	    def H(self) -> dict[Pillar, float]:  # noqa: N802
   170	        return {m: hhi(self.normalized_shares[m]) for m in PILLARS}
   171	
   172	    @property
   173	    def U(self) -> float:  # noqa: N802
   174	        return unaccountable_concentration(self.H, self.contestability, self.weights)
   175	
   176	    @property
   177	    def I(self) -> float:  # noqa: E743, N802
   178	        return integration_statistic(self.integration)
   179	
   180	
   181	@dataclass(frozen=True)
   182	class Assessment:
   183	    name: str
   184	    H: dict[Pillar, float]
   185	    U: float
   186	    I: float  # noqa: E741
   187	    prop_a: PropositionAResult
   188	    prop_b: PropositionBResult
   189	    sensitivity: WeightSensitivity
   190	    u_star: float
   191	
   192	    @property
   193	    def u_high_fraction(self) -> float:
   194	        """Share of weight draws with U >= u*: robustness of the U side of Proposition B."""
   195	        return self.sensitivity.fraction_at_least(self.u_star)
   196	
   197	
   198	def assess(
   199	    polity: Polity,
   200	    thresholds: CaptureThresholds = CaptureThresholds(),
   201	    n_draws: int = 2000,
   202	    seed: int = 0,
   203	) -> Assessment:
   204	    """Evaluate Proposition A, Proposition B and the weight sensitivity of U on one polity."""
   205	    return Assessment(
   206	        name=polity.name,
   207	        H=polity.H,
   208	        U=polity.U,
   209	        I=polity.I,
   210	        prop_a=check_proposition_a(polity.system),
   211	        prop_b=proposition_b(polity.U, polity.I, polity.capture_links, thresholds),
   212	        sensitivity=weight_sensitivity(polity.H, polity.contestability, polity.weights,
   213	                                       n_draws=n_draws, seed=seed),
   214	        u_star=thresholds.u_star,
   215	    )
   216	
   217	
   218	# Counter-model: A does not imply B --------------------------------------------------------
   219	
   220	

2026-10-22T17:32:08.941400Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '376,700p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   376	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   377	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   378	
   379	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   380	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   381	    """
   382	    practices = [p for p in system.practices if p.pillar is pillar]
   383	    if not practices:
   384	        return None
   385	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   386	    if not formal_holders:
   387	        return INFORMAL
   388	    formal_roles: dict[str, set[Pillar]] = {}
   389	    for p in system.practices:
   390	        if p.formal:
   391	            for h in p.holders:
   392	                formal_roles.setdefault(h, set()).add(p.pillar)
   393	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   394	        return FUSED
   395	    return FORMAL
   396	
   397	
   398	@dataclass(frozen=True)
   399	class Derivation:
   400	    """Result of the lemma for one axiom: required pillar and its realized form."""
   401	
   402	    axiom: Axiom
   403	    pillar: Pillar
   404	    form: RealizedForm | None
   405	    practices: tuple[Practice, ...]
   406	
   407	    @property
   408	    def realized(self) -> bool:
   409	        return self.form is not None
   410	
   411	
   412	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   413	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   414	
   415	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   416	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   417	    """
   418	    out: dict[Axiom, Derivation] = {}
   419	    for axiom in Axiom:
   420	        if not system.holds(axiom):
   421	            continue
   422	        pillar = AXIOM_TO_PILLAR[axiom]
   423	        out[axiom] = Derivation(
   424	            axiom=axiom,
   425	            pillar=pillar,
   426	            form=realized_form(system, pillar),
   427	            practices=tuple(p for p in system.practices if p.solves is axiom),
   428	        )
   429	    return out
   430	
   431	
   432	# Proposition A and interdependence --------------------------------------------------------
   433	
   434	
   435	@dataclass(frozen=True)
   436	class PropositionAResult:
   437	    """Outcome of checking Theorem A and interdependence on one coded system.
   438	
   439	    ``holds`` is Struct(G): all six pillars realized AND every D0 relation generated.
   440	    ``counterexample`` is True when Theorem A's antecedent holds (persistent, Ax1..Ax6) but
   441	    Struct(G) fails.
   442	
   443	    ``interdependent`` is the separate structural predicate: all six pillars realized and the
   444	    generated hypergraph both strongly connected (underlying digraph) and cascade-complete.
   445	    ``interdependence_counterexample`` is True when the system is persistent, satisfies the
   446	    extended axiom set, yet is not interdependent.
   447	    """
   448	
   449	    system: str
   450	    antecedent: bool
   451	    realized: frozenset[Pillar]
   452	    missing: frozenset[Pillar]
   453	    dependencies: frozenset[ArcKey]
   454	    missing_dependencies: frozenset[ArcKey]
   455	    strongly_connected: bool
   456	    cascade_complete: bool
   457	    holds: bool
   458	    interdependence_antecedent: bool
   459	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   460	
   461	    @property
   462	    def counterexample(self) -> bool:
   463	        return self.antecedent and not self.holds
   464	
   465	    @property
   466	    def interdependent(self) -> bool:
   467	        return not self.missing and self.strongly_connected and self.cascade_complete
   468	
   469	    @property
   470	    def interdependence_counterexample(self) -> bool:
   471	        return self.interdependence_antecedent and not self.interdependent
   472	
   473	
   474	def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
   475	    """Check Theorem A and interdependence on ``system`` (Part VII; KB Section 4.3).
   476	
   477	    A D0 relation is demanded when its head and every tail member are realized.
   478	    """
   479	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   480	    deps = generate_dependencies(system)
   481	    needed = frozenset((t, h) for t, h in D0_KEYS if h in realized and t <= realized)
   482	    missing_deps = needed - deps
   483	    return PropositionAResult(
   484	        system=system.name,
   485	        antecedent=system.persistent and system.all_axioms_hold,
   486	        realized=realized,
   487	        missing=frozenset(PILLARS) - realized,
   488	        dependencies=deps,
   489	        missing_dependencies=missing_deps,
   490	        strongly_connected=is_strongly_connected(underlying_digraph(deps), realized),
   491	        cascade_complete=is_cascade_complete(deps, realized),
   492	        holds=realized == frozenset(PILLARS) and not missing_deps,
   493	        interdependence_antecedent=system.persistent and system.extended_axioms_hold,
   494	        derivations=derive_functions(system),
   495	    )
   496	
   497	
   498	def formal_system(
   499	    name: str,
   500	    holders: Mapping[Pillar, Iterable[str]],
   501	    persistent: bool = True,
   502	    source: str = "",
   503	    axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS,
   504	) -> GovernanceSystem:
   505	    """A persistent system whose pillars are held by formal organizations.
   506	
   507	    An actor listed under several pillars is fused. By default the extended axiom set is
   508	    coded as holding: an assumption of the stylized model, not an observation. Used for regime
   509	    profiles and counter-models.
   510	    """
   511	    practices = tuple(
   512	        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
   513	                 frozenset(hs), formal=True, source=source)
   514	        for m, hs in holders.items()
   515	        if hs
   516	    )
   517	    return GovernanceSystem(name, persistent, frozenset(axioms), practices)
   518	
   519	
   520	# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
   521	# Each codes the extended axiom set as holding. For X1, X2, X3, X5 this is a coding
   522	# assumption with the falsifier stated on IncidenceAxiom; e.g. Nuer grazing and herds and
   523	# Ju/'hoansi n!ore territories are contested inputs (X1).
   524	
   525	
   526	def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
   527	    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)
   528	
   529	
   530	NUER = GovernanceSystem(
   531	    name="Nuer ('ordered anarchy')",
   532	    persistent=True,
   533	    axioms=EXTENDED_AXIOMS,
   534	    practices=(
   535	        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
   536	                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
   537	        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
   538	                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
   539	        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
   540	                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
   541	        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
   542	                  {"prophets", "lineages"}, "evanspritchard1940"),
   543	        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
   544	                  {"agnatic kin"}, "evanspritchard1940"),
   545	        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
   546	                  "evanspritchard1940"),
   547	    ),
   548	    note="no office holds coercive authority; functions exist without separation",
   549	)
   550	
   551	JU_HOANSI = GovernanceSystem(
   552	    name="Ju/'hoansi (!Kung)",
   553	    persistent=True,
   554	    axioms=EXTENDED_AXIOMS,
   555	    practices=(
   556	        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
   557	                  {"hunters", "camp members"}, "lee2013; marshall1976"),
   558	        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
   559	                  {"camp members"}, "lee2013"),
   560	        _informal("disputes talked out with kin mediators", Axiom.Ax3,
   561	                  {"kin mediators"}, "lee1979; wiessner2005"),
   562	        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
   563	                  {"healers", "camp members"}, "marshall1976"),
   564	        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
   565	                  {"camp members"}, "wiessner2005; lee2013"),
   566	        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
   567	    ),
   568	    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
   569	)
   570	
   571	OSTROM_COMMONS = GovernanceSystem(
   572	    name="Ostrom commons (design principles)",
   573	    persistent=True,
   574	    axioms=EXTENDED_AXIOMS,
   575	    practices=(
   576	        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
   577	                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
   578	        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
   579	                  {"appropriators"}, "ostrom1990"),
   580	        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
   581	                  {"appropriators"}, "ostrom1990; cox2010"),
   582	        _informal("shared norms; minimal recognition of rights to organize (DP7)",
   583	                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),
   584	        _informal("monitoring and graduated sanctions by appropriators (DP4, DP5)",
   585	                  Axiom.Ax5, {"appropriators"}, "ostrom1990; cox2010"),
   586	        _informal("appropriation and maintenance labor", Axiom.Ax6, {"appropriators"},
   587	                  "ostrom1990"),
   588	    ),
   589	    note="checks in minimal form; monitors are appropriators or accountable to them",
   590	)
   591	
   592	CONSENSUS_VILLAGE = GovernanceSystem(
   593	    name="Consensus village (stylized)",
   594	    persistent=True,
   595	    axioms=EXTENDED_AXIOMS,
   596	    practices=(
   597	        _informal("household plots; reciprocal labor exchange; sharing norms", Axiom.Ax1,
   598	                  {"households"}, "sahlins1972"),
   599	        _informal("consensus meeting of adults", Axiom.Ax2, {"village meeting"},
   600	                  "clastres1987; boehm1999"),
   601	        _informal("elders mediate disputes", Axiom.Ax3, {"elders"}, "boehm1999"),
   602	        _informal("ritual and myth; moral talk", Axiom.Ax4, {"village meeting", "elders"},
   603	                  "boehm1999"),
   604	        _informal("gossip, shunning, ostracism of would-be dominants", Axiom.Ax5,
   605	                  {"village meeting"}, "boehm1999; woodburn1982"),
   606	        _informal("gardening and household labor", Axiom.Ax6, {"households"},
   607	                  "sahlins1972"),
   608	    ),
   609	    note="stylized composite; reverse dominance hierarchy",
   610	)
   611	
   612	HARD_CASES: tuple[GovernanceSystem, ...] = (NUER, JU_HOANSI, OSTROM_COMMONS, CONSENSUS_VILLAGE)
   613	
   614	
   615	# Axiom independence fixtures (Part VII spec, item 7). ---------------------------------------
   616	
   617	#: Consistency model: the extended axiom set holds and all six pillars are realized (the
   618	#: consensus village coding).
   619	BASELINE_MODEL: GovernanceSystem = CONSENSUS_VILLAGE
   620	
   621	
   622	def without_axiom(axiom: AnyAxiom, base: GovernanceSystem = BASELINE_MODEL) -> GovernanceSystem:
   623	    """``base`` with one axiom removed; for Ax_k the practices solving Ax_k are removed too."""
   624	    practices = base.practices
   625	    if isinstance(axiom, Axiom):
   626	        practices = tuple(p for p in practices if p.solves is not axiom)
   627	    return GovernanceSystem(
   628	        name=f"{base.name} without {axiom.name} ({axiom.label})",
   629	        persistent=base.persistent,
   630	        axioms=base.axioms - {axiom},
   631	        practices=practices,
   632	        absent_incidences=base.absent_incidences,
   633	        note="hypothetical: one axiom removed",
   634	    )
   635	
   636	
   637	#: For each k: persistent, Ax_k removed, pillar k missing. Theorem A's antecedent is false,
   638	#: so none is a counterexample; each shows pillar k is not forced by the other five axioms.
   639	AXIOM_INDEPENDENCE: dict[Axiom, GovernanceSystem] = {a: without_axiom(a) for a in Axiom}

2026-10-22T17:32:11.406069Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
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
   147	
   148	
   149	def test_tolerated_rounding_cannot_break_bounds():
   150	    w = {m: 1 / 6 for m in PILLARS}
   151	    w[F] += 5e-10
   152	    ones, zeros = {m: 1.0 for m in PILLARS}, {m: 0.0 for m in PILLARS}
   153	    assert unaccountable_concentration(ones, zeros, w) <= 1.0
   154	    assert hhi([1.0 + 5e-10]) == 1.0
   155	    with pytest.raises(TypeError):
   156	        unaccountable_concentration(ones, {**zeros, F: True})
   157	
   158	
   159	def test_control_shares_survive_huge_weights():
   160	    shares = control_shares({"a": 1e308, "b": 1e308})
   161	    assert shares == pytest.approx({"a": 0.5, "b": 0.5})
   162	
   163	
   164	def test_degree_decomposition_of_integration():
   165	    from beast_system.indices import integration_degrees
   166	
   167	    rng = np.random.default_rng(7)
   168	    C_ = integration_matrix(dict(zip(PAIRS, rng.uniform(0, 1, 15))))
   169	    deg = integration_degrees(C_)
   170	    assert sum(deg.values()) / 30 == pytest.approx(integration_statistic(C_))
   171	
   172	
   173	@pytest.mark.parametrize("k,expected", [(0, 0.0), (1, 1 / 3), (2, 0.6), (3, 0.8), (6, 1.0)])
   174	def test_hub_bound_values_and_validity(k, expected):
   175	    from beast_system.indices import hub_bound
   176	
   177	    assert hub_bound(k) == pytest.approx(expected)
   178	    hub = set(PILLARS[:k])
   179	    full = integration_matrix({(m, n): 1.0 for m, n in PAIRS if m in hub or n in hub})
   180	    assert integration_statistic(full) == pytest.approx(hub_bound(k))  # bound is attained
   181	
   182	
   183	def test_coalition_overlap_general_kappa():
   184	    from beast_system.indices import coalition_overlap
   185	
   186	    # Overlapping, non-additive candidate coalitions.
   187	    kappa = {"S1": {F: 0.7, P: 0.4}, "S2": {F: 0.5, P: 0.6, J: 0.9}, "S1+S2": {F: 0.8, P: 0.8}}
   188	    Cm = coalition_overlap(kappa)
   189	    assert Cm[F.position, P.position] == pytest.approx(0.8)
   190	    assert Cm[P.position, J.position] == pytest.approx(0.6)
   191	    assert Cm[F.position, W.position] == 0.0
   192	    assert integration_statistic(coalition_overlap({})) == 0.0
   193	    with pytest.raises(ValueError):
   194	        coalition_overlap({"S": {F: 1.2}})
   195	
   196	
   197	def test_near_symmetric_matrix_is_symmetrized():
   198	    from beast_system.indices import integration_degrees
   199	
   200	    Cm = integration_matrix({(F, P): 0.5})
   201	    Cm[F.position, P.position] += 1e-13
   202	    v = validate_integration_matrix(Cm)
   203	    assert np.array_equal(v, v.T)
   204	    assert sum(integration_degrees(Cm).values()) / 30 == pytest.approx(integration_statistic(Cm))
   205	
   206	
   207	@pytest.mark.parametrize("k", [1.5, True, -1, 7])
   208	def test_hub_bound_rejects_bad_k(k):
   209	    from beast_system.indices import hub_bound
   210	
   211	    with pytest.raises((TypeError, ValueError)):
   212	        hub_bound(k)
   213	
   214	
   215	@pytest.mark.parametrize("k", range(7))
   216	def test_clique_lower_bound(k):
   217	    from beast_system.indices import clique_lower_bound, coalition_overlap
   218	
   219	    c = 0.4
   220	    clique = set(PILLARS[:k])
   221	    rng = np.random.default_rng(k)
   222	    kappa = {"S": {m: c + 0.6 * rng.uniform() if m in clique else 0.0 for m in PILLARS},
   223	             "T": {m: float(rng.uniform(0, 0.3)) for m in PILLARS}}
   224	    assert integration_statistic(coalition_overlap(kappa)) >= clique_lower_bound(c, k) - 1e-12
   225	    assert clique_lower_bound(c, 6) == pytest.approx(c)
   226	
   227	
   228	def test_star_upper_bound():
   229	    from beast_system.indices import star_upper_bound
   230	
   231	    rng = np.random.default_rng(3)
   232	    for hub in PILLARS:
   233	        Cm = integration_matrix({(m, n): float(rng.uniform()) for m, n in PAIRS if hub in (m, n)})
   234	        assert integration_statistic(Cm) <= star_upper_bound(Cm, hub) + 1e-12
   235	    with pytest.raises(ValueError):
   236	        star_upper_bound(integration_matrix({(P, J): 0.5}), F)

exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_conversion.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	import numpy as np
     2	import pytest
     3	
     4	from beast_system.dynamics import (
     5	    coalition_integration_share,
     6	    comparison_matrix,
     7	    conversion_matrix,
     8	    conversion_step,
     9	    foothold_bound,
    10	    simulate_conversion,
    11	    spectral_radius,
    12	    validate_conversion_matrix,
    13	)
    14	
    15	RNG = np.random.default_rng(11)
    16	
    17	
    18	def _eta(scale=0.18):
    19	    eta = np.full((6, 6), scale)
    20	    np.fill_diagonal(eta, 0.0)
    21	    return eta
    22	
    23	
    24	def test_conversion_matrix_definition_and_validation():
    25	    Q = np.linspace(0, 1, 6)
    26	    K = conversion_matrix(_eta(), Q)
    27	    assert K == pytest.approx(_eta() * (1 - Q)[:, None])
    28	    with pytest.raises(ValueError):
    29	        validate_conversion_matrix(np.eye(6) * 0.1)  # non-zero diagonal
    30	    with pytest.raises(ValueError):
    31	        conversion_matrix(_eta(0.3), np.zeros(6))  # row sums 1.5 > 1
    32	    with pytest.raises(ValueError):
    33	        conversion_matrix(-_eta(), np.zeros(6))
    34	
    35	
    36	def test_t_maps_cube_into_itself_and_is_dominated_by_a():
    37	    K = conversion_matrix(_eta(0.2), np.zeros(6))
    38	    for _ in range(300):
    39	        y = RNG.uniform(0, 1, 6)
    40	        delta = RNG.uniform(0, 1, 6)
    41	        ty = conversion_step(y, delta, K)
    42	        assert ty.min() >= 0.0 and ty.max() <= 1.0
    43	        assert np.all(ty <= comparison_matrix(delta, K) @ y + 1e-12)
    44	    corner = conversion_step(np.ones(6), np.zeros(6), K)
    45	    assert corner == pytest.approx(np.ones(6))
    46	
    47	
    48	def test_rho_below_one_means_reversible():
    49	    K = conversion_matrix(_eta(0.1), np.full(6, 0.5))
    50	    delta = np.full(6, 0.3)
    51	    assert spectral_radius(comparison_matrix(delta, K)) < 1.0
    52	    path = simulate_conversion(np.ones(6), delta, K, 300)
    53	    assert path[-1].max() < 1e-6
    54	
    55	
    56	def test_full_contestability_drains_pillar_and_caps_integration():
    57	    Q = np.zeros(6)
    58	    Q[2] = 1.0  # pillar J fully contestable
    59	    delta = np.full(6, 0.05)
    60	    delta[2] = 0.2
    61	    K = conversion_matrix(_eta(0.19), Q)
    62	    path = simulate_conversion(np.full(6, 0.9), delta, K, 400)
    63	    for t in range(0, 401, 50):
    64	        assert path[t, 2] <= (1 - 0.2) ** t * 0.9 + 1e-15
    65	    assert coalition_integration_share(path[-1]) <= 10 / 15 + 1e-6
    66	
    67	
    68	def test_rho_nonincreasing_in_each_q():
    69	    delta = np.full(6, 0.1)
    70	    for n in range(6):
    71	        prev = np.inf
    72	        for q in np.linspace(0, 1, 11):
    73	            Q = np.full(6, 0.2)
    74	            Q[n] = q
    75	            rho = spectral_radius(comparison_matrix(delta, conversion_matrix(_eta(), Q)))
    76	            assert rho <= prev + 1e-12
    77	            prev = rho
    78	
    79	
    80	def test_foothold_never_vanishes():
    81	    K = conversion_matrix(_eta(0.19), np.zeros(6))
    82	    delta = np.full(6, 0.2)
    83	    y0 = np.array([0.01, 0, 0, 0, 0, 0])
    84	    fh = foothold_bound(y0, delta, K)
    85	    assert fh.rho > 1.0 and fh.bound > 0.0
    86	    path = simulate_conversion(y0, delta, K, 500)
    87	    assert np.all((path * fh.v).sum(axis=1) >= fh.bound - 1e-12)
    88	
    89	
    90	def test_foothold_preconditions():
    91	    with pytest.raises(ValueError):
    92	        foothold_bound(np.full(6, 0.1), np.full(6, 0.9), conversion_matrix(_eta(0.01), np.zeros(6)))
    93	    reducible = np.zeros((6, 6))
    94	    reducible[1, 0] = 0.5
    95	    with pytest.raises(ValueError):
    96	        foothold_bound(np.full(6, 0.1), np.zeros(6), reducible)
    97	
    98	
    99	@pytest.mark.parametrize("seed", range(5))
   100	def test_foothold_with_asymmetric_k_and_heterogeneous_delta(seed):
   101	    rng = np.random.default_rng(100 + seed)
   102	    eta = rng.uniform(0.0, 1.0, (6, 6))
   103	    np.fill_diagonal(eta, 0.0)
   104	    eta *= 0.95 / eta.sum(axis=1, keepdims=True)  # row sums 0.95, irreducible, asymmetric
   105	    Q = rng.uniform(0.0, 0.3, 6)
   106	    K = conversion_matrix(eta, Q)
   107	    delta = rng.uniform(0.05, 0.4, 6)
   108	    assert not np.allclose(K, K.T)
   109	    A = comparison_matrix(delta, K)
   110	    if spectral_radius(A) <= 1.0:
   111	        pytest.skip("draw has rho(A) <= 1")
   112	    y0 = np.zeros(6)
   113	    y0[seed % 6] = 0.02
   114	    fh = foothold_bound(y0, delta, K)
   115	    assert fh.v @ A == pytest.approx(fh.rho * fh.v)  # left eigenvector orientation
   116	    path = simulate_conversion(y0, delta, K, 400)
   117	    assert np.all((path * fh.v).sum(axis=1) >= fh.bound - 1e-12)

exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_necessity.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	import pytest
     2	
     3	from beast_system.necessity import (
     4	    AXIOM_INDEPENDENCE,
     5	    BASELINE_MODEL,
     6	    BRIEF_ARCS,
     7	    CORE_RULES,
     8	    D0_KEYS,
     9	    D_STAR_KEYS,
    10	    EXTENDED_AXIOMS,
    11	    FORMAL,
    12	    FURTHER_RULES,
    13	    FUSED,
    14	    HARD_CASES,
    15	    INFORMAL,
    16	    JU_HOANSI,
    17	    NUER,
    18	    DependencyRule,
    19	    GovernanceSystem,
    20	    Practice,
    21	    arc_key,
    22	    cascade_closure,
    23	    check_proposition_a,
    24	    critical_edges,
    25	    derive_functions,
    26	    formal_system,
    27	    generate_dependencies,
    28	    is_cascade_complete,
    29	    is_strongly_connected,
    30	    role_map,
    31	    rules_holding,
    32	    sinks_and_sources,
    33	    underlying_digraph,
    34	    without_axiom,
    35	)
    36	from beast_system.pillars import PILLARS, Axiom, IncidenceAxiom, Pillar
    37	
    38	F, P, J, I, C, W = PILLARS
    39	X1, X2, X3, X5 = IncidenceAxiom
    40	
    41	
    42	# Theorem A ---------------------------------------------------------------------------------
    43	
    44	
    45	@pytest.mark.parametrize("system", HARD_CASES, ids=lambda s: s.name)
    46	def test_theorem_a_on_hard_cases(system):
    47	    result = check_proposition_a(system)
    48	    assert result.antecedent
    49	    assert result.holds and not result.counterexample
    50	    assert result.realized == frozenset(PILLARS)
    51	    derivs = derive_functions(system)
    52	    assert {d.pillar for d in derivs.values()} == set(PILLARS)
    53	    assert all(d.form == INFORMAL for d in derivs.values())
    54	
    55	
    56	def test_role_map_is_derived_from_practices():
    57	    roles = role_map(JU_HOANSI)
    58	    assert Pillar.C in roles["camp members"] and Pillar.P in roles["camp members"]
    59	
    60	
    61	def test_missing_axiom_drops_pillar_and_is_not_a_counterexample():
    62	    # A perfectly cooperative collective: Ax5 fails and there is no sanction practice.
    63	    practices = tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5)
    64	    system = GovernanceSystem("no defection", True, EXTENDED_AXIOMS - {Axiom.Ax5}, practices)
    65	    derivs = derive_functions(system)
    66	    assert Axiom.Ax5 not in derivs and len(derivs) == 5
    67	    result = check_proposition_a(system)
    68	    assert not result.antecedent
    69	    assert result.missing == {C}
    70	    assert not result.holds and not result.counterexample
    71	
    72	
    73	def test_falsifier_is_reported():
    74	    # All axioms coded as holding, persistent, but no sanction practice: a counterexample.
    75	    practices = tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5)
    76	    system = GovernanceSystem("hypothetical", True, EXTENDED_AXIOMS, practices)
    77	    result = check_proposition_a(system)
    78	    assert result.counterexample
    79	    assert derive_functions(system)[Axiom.Ax5].form is None
    80	
    81	
    82	def test_non_persistent_system_does_not_trigger_theorem():
    83	    system = GovernanceSystem("short-lived", False, EXTENDED_AXIOMS, ())
    84	    assert not check_proposition_a(system).antecedent
    85	    assert not check_proposition_a(system).counterexample
    86	    assert not check_proposition_a(system).interdependence_counterexample
    87	
    88	
    89	def test_fused_and_formal_forms():
    90	    system = formal_system("toy", {F: ["Treasury"], P: ["Crown"], J: ["Crown"], I: ["Church"],
    91	                                   C: ["Crown"], W: ["Peasants"]})
    92	    derivs = derive_functions(system)
    93	    assert derivs[Axiom.Ax2].form == FUSED
    94	    assert derivs[Axiom.Ax5].form == FUSED
    95	    assert derivs[Axiom.Ax1].form == FORMAL
    96	    assert check_proposition_a(system).holds
    97	
    98	
    99	def test_practice_and_system_validation():
   100	    with pytest.raises(ValueError):
   101	        Practice("x", Axiom.Ax1, frozenset())
   102	    with pytest.raises(TypeError):
   103	        Practice("x", Pillar.F, frozenset({"a"}))  # type: ignore[arg-type]
   104	    with pytest.raises(TypeError):
   105	        GovernanceSystem("bad", True, frozenset({"Ax1"}))  # type: ignore[arg-type]
   106	    with pytest.raises(TypeError):
   107	        GovernanceSystem("bad", True, EXTENDED_AXIOMS, (), frozenset({(F, W)}))
   108	
   109	
   110	def test_missing_d0_relation_is_a_counterexample():
   111	    system = GovernanceSystem("no Inc(Ax6, C)", True, EXTENDED_AXIOMS, JU_HOANSI.practices,
   112	                              frozenset({(Axiom.Ax6, C)}))
   113	    result = check_proposition_a(system)
   114	    assert result.realized == frozenset(PILLARS)
   115	    assert result.missing_dependencies == {arc_key(W, C)}
   116	    assert result.counterexample
   117	
   118	
   119	# Generated dependency hypergraph -------------------------------------------------------------
   120	
   121	
   122	def test_rules_are_documented_and_traced_to_axioms():
   123	    for r in CORE_RULES + FURTHER_RULES:
   124	        assert r.head not in r.tail and r.premise and r.source and r.requires
   125	    assert len({r.key for r in CORE_RULES}) == len(CORE_RULES)
   126	    # Every incidence axiom generates exactly one core arc, pillar(base) -> target.
   127	    for x in IncidenceAxiom:
   128	        rules = [r for r in CORE_RULES if x in r.requires]
   129	        assert len(rules) == 1
   130	        assert rules[0].key == arc_key(x.base.pillar, x.target)
   131	        assert rules[0].incidence == (x.base, x.target)
   132	
   133	
   134	def test_d_star_and_d0_contents():
   135	    w_arcs = {arc_key(W, m) for m in (F, P, J, I, C)}
   136	    assert D0_KEYS == w_arcs | {arc_key({I, C}, J)}
   137	    assert D_STAR_KEYS == D0_KEYS | {arc_key(I, F), arc_key(F, W), arc_key(P, F),
   138	                                     arc_key(J, F), arc_key(C, F)}
   139	    assert arc_key(C, J) not in D_STAR_KEYS and arc_key(I, J) not in D_STAR_KEYS
   140	    assert frozenset(r.key for r in rules_holding(EXTENDED_AXIOMS)) == D_STAR_KEYS
   141	
   142	
   143	def test_d0_alone_is_not_strongly_connected():
   144	    assert not is_strongly_connected(underlying_digraph(D0_KEYS))
   145	    assert not is_cascade_complete(D0_KEYS)
   146	
   147	
   148	def test_d_star_is_strongly_connected_and_cascade_complete():
   149	    assert is_strongly_connected(underlying_digraph(D_STAR_KEYS))
   150	    assert is_cascade_complete(D_STAR_KEYS)
   151	    for n in PILLARS:
   152	        assert cascade_closure(D_STAR_KEYS, {n}) == frozenset(PILLARS), n
   153	
   154	
   155	def test_without_x5_strongly_connected_but_c_isolated():
   156	    arcs = generate_dependencies(without_axiom(X5))
   157	    assert arc_key(C, F) not in arcs
   158	    assert is_strongly_connected(underlying_digraph(arcs))
   159	    assert cascade_closure(arcs, {C}) == {C}
   160	    assert not is_cascade_complete(arcs)
   161	    # Splitting the OR-hyperarc would wrongly put J in cl({C}).
   162	    split = (arcs - {arc_key({I, C}, J)}) | {arc_key(C, J), arc_key(I, J)}
   163	    assert J in cascade_closure(split, {C})
   164	
   165	
   166	def test_without_x1_no_arc_into_w():
   167	    arcs = generate_dependencies(without_axiom(X1))
   168	    graph = underlying_digraph(arcs)
   169	    assert not is_strongly_connected(graph)
   170	    assert W in sinks_and_sources(graph)[1]
   171	    # F -> W is the only arc into W anywhere in the catalogue.
   172	    into_w = {r.key for r in CORE_RULES + FURTHER_RULES if r.head is W}
   173	    assert into_w == {arc_key(F, W)}
   174	
   175	
   176	def test_without_x2_p_has_no_out_arc():
   177	    graph = underlying_digraph(generate_dependencies(without_axiom(X2)))
   178	    assert not graph[P]
   179	    assert not is_strongly_connected(graph)
   180	
   181	
   182	def test_replacing_x3_by_precedent_keeps_strong_connectivity():
   183	    precedent = next(r for r in FURTHER_RULES if r.premise == "precedent (Hart)")
   184	    arcs = (D_STAR_KEYS - {arc_key(J, F)}) | {precedent.key}
   185	    assert precedent.key == arc_key(J, P)
   186	    assert is_strongly_connected(underlying_digraph(arcs))
   187	
   188	
   189	@pytest.mark.parametrize("rule", CORE_RULES, ids=lambda r: f"{'+'.join(sorted(t.name for t in r.tail))}->{r.head.name}")
   190	def test_removing_a_premise_removes_its_arc(rule):
   191	    for premise in rule.requires:
   192	        assert rule.key not in generate_dependencies(without_axiom(premise))
   193	    assert rule.key in generate_dependencies(BASELINE_MODEL)
   194	
   195	
   196	@pytest.mark.parametrize("system", HARD_CASES, ids=lambda s: s.name)
   197	def test_interdependence_holds_for_every_axiom_built_fixture(system):
   198	    result = check_proposition_a(system)
   199	    assert result.interdependence_antecedent
   200	    assert result.strongly_connected and result.cascade_complete and result.interdependent
   201	    assert result.dependencies == D_STAR_KEYS
   202	
   203	
   204	def test_absent_incidence_is_an_interdependence_counterexample():
   205	    system = GovernanceSystem("no Inc(Ax5, F)", True, EXTENDED_AXIOMS, JU_HOANSI.practices,
   206	                              frozenset({(Axiom.Ax5, F)}))
   207	    result = check_proposition_a(system)
   208	    assert result.holds  # Theorem A only needs D0
   209	    assert not result.interdependent and result.interdependence_counterexample
   210	
   211	
   212	def test_brief_relations_alone_are_not_strongly_connected():
   213	    brief = underlying_digraph(BRIEF_ARCS)
   214	    assert not is_strongly_connected(brief)
   215	    sinks, sources = sinks_and_sources(brief)
   216	    assert sinks == {C} and not sources
   217	
   218	
   219	def test_critical_edges_of_d_star():
   220	    # Sole arc into W, P, I, C, and sole out-arc of P and of J.
   221	    expected = {(F, W), (W, P), (W, I), (W, C), (P, F), (J, F)}
   222	    assert set(critical_edges(underlying_digraph(D_STAR_KEYS))) == expected
   223	
   224	
   225	def test_or_hyperarc_needs_whole_tail_to_fail():
   226	    arcs = [arc_key({I, C}, J)]
   227	    assert cascade_closure(arcs, {I}) == {I}
   228	    assert cascade_closure(arcs, {I, C}) == {I, C, J}
   229	
   230	
   231	def test_rule_and_arc_validation():
   232	    with pytest.raises(ValueError):
   233	        arc_key({J, C}, J)
   234	    with pytest.raises(TypeError):
   235	        arc_key(set(), J)
   236	    with pytest.raises(ValueError):
   237	        DependencyRule(frozenset({F}), W, "x", frozenset(), "s", True)
   238	    with pytest.raises(ValueError):
   239	        DependencyRule(frozenset({F}), W, "x", frozenset({Axiom.Ax2}), "s", True,
   240	                       (Axiom.Ax2, W))  # incidence of Ax2 must start at P
   241	
   242	
   243	# Axiom independence --------------------------------------------------------------------------
   244	
   245	
   246	@pytest.mark.parametrize("axiom", list(Axiom), ids=lambda a: a.name)
   247	def test_axiom_independence_fixtures(axiom):
   248	    system = AXIOM_INDEPENDENCE[axiom]
   249	    assert system.persistent and not system.holds(axiom)
   250	    result = check_proposition_a(system)
   251	    assert result.missing == {axiom.pillar}
   252	    assert not result.antecedent and not result.counterexample
   253	    assert not result.interdependence_counterexample
   254	
   255	
   256	def test_baseline_model_is_consistent():
   257	    result = check_proposition_a(BASELINE_MODEL)
   258	    assert BASELINE_MODEL.extended_axioms_hold and result.antecedent
   259	    assert result.holds and result.interdependent
   260	
   261	
   262	def test_strong_connectivity_small_cases():
   263	    assert not is_strongly_connected({})
   264	    assert is_strongly_connected({F: set()})
   265	    assert is_strongly_connected({F: {P}, P: {F}})
   266	    assert not is_strongly_connected({F: {P}, P: set()})
   267	    assert is_strongly_connected({F: {P}, P: {F, J}}, nodes={F, P})

exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_pillars_network.py; nl -ba model/tests/test_dynamics_regimes.py' in /Users/mlong/Documents/Development/the-beast-system
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
     1	import numpy as np
     2	import pytest
     3	
     4	from beast_system.capture import CaptureThresholds, assess
     5	from beast_system.dynamics import (
     6	    dependency_matrix,
     7	    some_deviation_persists,
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
    21	    assert some_deviation_persists(R)
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
    35	    assert ex.rho_positive > 1.0 and some_deviation_persists(ex.B_positive)
    36	    assert ex.rho_feedback < 1.0 and not some_deviation_persists(ex.B_feedback)
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
    61	    with pytest.raises(ValueError):
    62	        simulate(B, np.full(6, np.nan), 5)
    63	    with pytest.raises(ValueError):
    64	        simulate(B, np.zeros(6), 5, noise_sd=float("inf"))
    65	
    66	
    67	def test_all_regimes_satisfy_proposition_a():
    68	    for prof in regime_profiles():
    69	        a = assess(prof.polity)
    70	        assert a.prop_a.holds, prof.label
    71	        assert 0.0 <= a.U <= 1.0 and 0.0 <= a.I <= 1.0
    72	        assert prof.illustrative and "not a measurement" in prof.rationale
    73	
    74	
    75	def test_six_regime_types_with_variants():
    76	    types = {p.regime_type for p in regime_profiles()}
    77	    assert len(types) == 6
    78	    labels = [p.label for p in regime_profiles()]
    79	    assert len(labels) == len(set(labels))
    80	
    81	
    82	def test_no_regime_satisfies_b_without_evidenced_links():
    83	    for prof in regime_profiles():
    84	        assert not assess(prof.polity).prop_b.holds
    85	
    86	
    87	@pytest.mark.parametrize("rtype", ["Islamic state", "Catholic monarchy"])
    88	def test_religious_types_vary_and_have_a_variant_below_thresholds(rtype):
    89	    th = CaptureThresholds()
    90	    variants = [assess(p.polity, th) for p in regime_profiles() if p.regime_type == rtype]
    91	    assert len(variants) == 2
    92	    assert any(not v.prop_b.thresholds_met for v in variants)
    93	    assert abs(variants[0].U - variants[1].U) > 0.05
    94	    assert abs(variants[0].I - variants[1].I) > 0.05
    95	
    96	
    97	def test_regimes_differ_in_h_q_c():
    98	    profs = regime_profiles()
    99	    hs = {tuple(round(v, 6) for v in p.polity.H.values()) for p in profs}
   100	    qs = {tuple(p.polity.contestability.values()) for p in profs}
   101	    cs = {p.polity.integration.round(6).tobytes() for p in profs}
   102	    assert len(hs) == len(qs) == len(cs) == len(profs)
   103	    assert all(set(p.polity.H) == set(PILLARS) for p in profs)

exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_capture.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	import pytest
     2	
     3	import numpy as np
     4	
     5	from beast_system.capture import (
     6	    Polity,
     7	    assess,
     8	    CaptureLink,
     9	    CaptureThresholds,
    10	    a_does_not_imply_b,
    11	    fused_polity,
    12	    is_capture_link,
    13	    plural_polity,
    14	    proposition_b,
    15	)
    16	from beast_system.indices import integration_matrix
    17	from beast_system.necessity import formal_system
    18	from beast_system.pillars import PILLARS, Pillar
    19	
    20	
    21	def _link(access=True, weakens=True, evidence=True):
    22	    return CaptureLink("donor", "agency", Pillar.P, access, weakens, evidence,
    23	                       evidence="procurement record" if evidence else "")
    24	
    25	
    26	def test_capture_link_needs_all_three_conditions():
    27	    assert is_capture_link(_link())
    28	
    29	
    30	@pytest.mark.parametrize("missing", ["access", "weakens", "evidence"])
    31	def test_each_capture_condition_is_necessary(missing):
    32	    assert not is_capture_link(_link(**{missing: False}))
    33	
    34	
    35	def test_disclosure_compliant_meeting_is_not_capture():
    36	    # Privileged access alone, with no weakening of accountability and no evidence.
    37	    assert not is_capture_link(_link(weakens=False, evidence=False))
    38	
    39	
    40	def test_material_evidence_must_be_cited():
    41	    with pytest.raises(ValueError):
    42	        CaptureLink("a", "b", Pillar.J, True, True, True, evidence="  ")
    43	    with pytest.raises(ValueError):
    44	        CaptureLink("", "b", Pillar.J, True, True, False)
    45	
    46	
    47	def test_prop_b_needs_u_i_and_link():
    48	    th = CaptureThresholds(u_star=0.4, i_star=0.5)
    49	    assert proposition_b(0.6, 0.7, [_link()], th).holds
    50	    assert not proposition_b(0.6, 0.7, [], th).holds
    51	    assert not proposition_b(0.6, 0.7, [_link(evidence=False)], th).holds
    52	    assert not proposition_b(0.3, 0.7, [_link()], th).holds
    53	    assert not proposition_b(0.6, 0.4, [_link()], th).holds
    54	    assert proposition_b(0.4, 0.5, [_link()], th).holds  # thresholds are inclusive
    55	
    56	
    57	def test_thresholds_validated():
    58	    with pytest.raises(ValueError):
    59	        CaptureThresholds(u_star=1.5)
    60	    with pytest.raises(ValueError):
    61	        proposition_b(1.2, 0.5, [])
    62	
    63	
    64	def test_counter_model_a_does_not_imply_b():
    65	    cm = a_does_not_imply_b()
    66	    assert cm.plural.prop_a.holds and cm.fused.prop_a.holds
    67	    assert cm.plural.prop_a.interdependent and cm.fused.prop_a.interdependent
    68	    assert not cm.plural.prop_b.holds and cm.fused.prop_b.holds
    69	    assert cm.demonstrates_non_implication
    70	
    71	
    72	def test_counter_model_index_values():
    73	    g1, g2 = plural_polity(), fused_polity()
    74	    assert g1.U == pytest.approx(0.2 * 0.1)
    75	    assert g1.I == 0.0
    76	    assert g2.U == 1.0
    77	    assert g2.I == 1.0
    78	    assert all(h == pytest.approx(1.0) for h in g2.H.values())
    79	
    80	
    81	def test_counter_model_robust_to_thresholds():
    82	    for u_star, i_star in [(0.0, 0.0), (0.1, 0.1), (0.5, 0.5), (0.9, 0.9), (1.0, 1.0), (0.0, 1.0)]:
    83	        assert a_does_not_imply_b(CaptureThresholds(u_star, i_star)).demonstrates_non_implication
    84	
    85	
    86	def test_capture_link_flags_must_be_bool():
    87	    with pytest.raises(TypeError):
    88	        CaptureLink("a", "b", Pillar.J, "yes", True, False)  # type: ignore[arg-type]
    89	
    90	
    91	def _toy_polity(links=()):
    92	    holders = {m: ["state", "society"] for m in PILLARS}
    93	    return Polity(
    94	        name="toy",
    95	        system=formal_system("toy", holders),
    96	        shares={m: {"state": 1, "society": 1} for m in PILLARS},
    97	        contestability={m: 0.5 for m in PILLARS},
    98	        integration=integration_matrix({}, default=0.3),
    99	        capture_links=tuple(links),
   100	    )
   101	
   102	
   103	def test_capture_link_endpoints_must_be_polity_actors():
   104	    _toy_polity([CaptureLink("state", "society", Pillar.P, True, True, True, "record")])
   105	    with pytest.raises(ValueError):
   106	        _toy_polity([CaptureLink("invented", "society", Pillar.P, True, True, True, "record")])
   107	
   108	
   109	def test_thresholds_are_stored_as_floats_and_typed():
   110	    th = CaptureThresholds(u_star=np.float32(0.25), i_star=1)
   111	    assert type(th.u_star) is float and th.i_star == 1.0
   112	    with pytest.raises(TypeError):
   113	        CaptureThresholds(u_star="0.4")  # type: ignore[arg-type]
   114	
   115	
   116	def test_assess_reports_weight_sensitivity():
   117	    a = assess(_toy_polity())
   118	    assert a.sensitivity.vertex_min <= a.U <= a.sensitivity.vertex_max
   119	    assert 0.0 <= a.u_high_fraction <= 1.0
   120	    cm = a_does_not_imply_b()
   121	    assert cm.fused.u_high_fraction == 1.0 and cm.plural.u_high_fraction == 0.0
   122	
   123	
   124	def test_corner_polities_attain_the_four_corners():
   125	    from beast_system.capture import corner_polities
   126	
   127	    corners = corner_polities()
   128	    assert set(corners) == {(0, 0), (1, 1), (0, 1), (1, 0)}
   129	    for (u, i), polity in corners.items():
   130	        a = assess(polity)
   131	        assert a.U == pytest.approx(u) and a.I == pytest.approx(i)
   132	        assert a.prop_a.holds and a.prop_a.interdependent
   133	        assert a.prop_b.holds == ((u, i) == (1, 1))
   134	        assert (a.prop_b.n_links > 0) == ((u, i) == (1, 1))

2026-10-22T17:32:17.618496Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
The four round-3 items are present in both implementation and tests: general non-additive coalition overlap, exact symmetrization after tolerance validation, integer-only hub size, and asymmetric/heterogeneous foothold coverage. I’m now checking the full suite and probing boundary cases that the current tests do not exercise.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'python3 -m pytest -q' in /Users/mlong/Documents/Development/the-beast-system/model
2026-10-22T17:33:01.310845Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 exited 1 in 1482ms:
2026-10-22 12:32:59.947 xcodebuild[50518:4044269]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:33:00.075 xcodebuild[50518:4044268] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-s1HEn8q0' (errno=Operation not permitted)
2026-10-22 12:33:00.491 xcodebuild[50520:4044281]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:33:00.581 xcodebuild[50520:4044279] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
/Applications/Xcode.app/Contents/Developer/usr/bin/python3: No module named pytest

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'ls -la model; command -v -a python3 pytest || true' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
total 8
drwxr-xr-x   7 mlong  staff  224 Oct 22 09:27 .
drwxr-xr-x@ 15 mlong  staff  480 Oct 22 12:15 ..
drwxr-xr-x   6 mlong  staff  192 Oct 22 09:27 .pytest_cache
drwxr-xr-x  11 mlong  staff  352 Oct 22 12:30 beast_system
drwxr-xr-x   3 mlong  staff   96 Oct 22 12:31 examples
-rw-r--r--   1 mlong  staff  461 Oct 22 09:22 pyproject.toml
drwxr-xr-x   9 mlong  staff  288 Oct 22 12:30 tests
zsh:1: command not found: -v

2026-10-22T17:33:05.296075Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'which -a python python3 pytest uv 2>/dev/null || true' in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 0ms:
/Users/mlong/.pyenv/shims/python
/opt/homebrew/opt/python/libexec/bin/python
/usr/bin/python3
/Users/mlong/.pyenv/shims/python3
/opt/homebrew/bin/python3
/usr/local/bin/pytest
/Users/mlong/.pyenv/shims/pytest
/Users/mlong/.pyenv/shims/uv
/opt/homebrew/bin/uv

2026-10-22T17:33:08.391043Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
2026-10-22T17:33:10.905298Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc '/opt/homebrew/opt/python/libexec/bin/python -m pytest -q' in /Users/mlong/Documents/Development/the-beast-system/model
 exited 1 in 0ms:
/opt/homebrew/opt/python@3.15/bin/python3.15: No module named pytest

2026-10-22T17:33:13.220891Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'pyenv versions --bare 2>/dev/null || true' in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 0ms:
2.7.17
3.5.6
3.6.0
3.6.3
3.6.5
3.7.7
3.7.8
3.7.9
3.9.4
3.9.16
3.9.18
3.11.6
3.11.8
3.11.11
3.12.3
3.12.5
3.12.6
3.12.9

2026-10-22T17:33:18.368062Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc '/Users/mlong/.pyenv/versions/3.12.9/bin/python -m pytest -q' in /Users/mlong/Documents/Development/the-beast-system/model
2026-10-22T17:33:22.653114Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 exited 1 in 130ms:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/Users/mlong/.pyenv/versions/3.12.9/lib/python3.12/site-packages/pytest/__main__.py", line 9, in <module>
    raise SystemExit(pytest.console_main())
                     ^^^^^^^^^^^^^^^^^^^^^
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
FileNotFoundError: [Errno 2] No usable temporary directory found in ['/var/folders/6z/np99jwkj4ys5z6l5y0xpwdx80000gn/T/', '/tmp', '/var/tmp', '/usr/tmp', '/Users/mlong/Documents/Development/the-beast-system/model']

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 /Users/mlong/.pyenv/versions/3.12.9/bin/python -m pytest -q -s -p no:cacheprovider' in /Users/mlong/Documents/Development/the-beast-system/model
2026-10-22T17:33:25.666561Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 281ms:
............................................................................................................................................
140 passed in 0.18s

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 /Users/mlong/.pyenv/versions/3.12.9/bin/python -c 'import numpy as np; from beast_system.dynamics import foothold_bound; K=np.zeros((6,6)); K[:5,:5]=0.22; np.fill_diagonal(K,0); K[0,5]=1e-300; K[5,0]=1e-300; d=np.full(6,0.1); y=np.full(6,0.1); print(K.sum(1)); print(foothold_bound(y,d,K))'" in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 0ms:
/Users/mlong/Documents/Development/the-beast-system/model/beast_system/dynamics.py:256: RuntimeWarning: divide by zero encountered in scalar divide
  c = float(v.max() * kappa / v.min() ** 2)
[8.8e-001 8.8e-001 8.8e-001 8.8e-001 8.8e-001 1.0e-300]
Foothold(rho=1.7799999999999996, v=array([2.00000000e-001, 2.00000000e-001, 2.00000000e-001, 2.00000000e-001,
       2.00000000e-001, 9.09090909e-301]), c=inf, bound=0.0)

2026-10-22T17:33:48.792178Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 /Users/mlong/.pyenv/versions/3.12.9/bin/python -c 'import numpy as np; from beast_system.dynamics import foothold_bound; K=np.zeros((6,6)); K[:5,:5]=0.22; np.fill_diagonal(K,0); K[0,5]=1e-160; K[5,0]=1e-160; d=np.full(6,0.1); y=np.full(6,0.1); f=foothold_bound(y,d,K); print(f); print(\"vmin\",f.v.min(),\"vmin2\",f.v.min()**2)'" in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 0ms:
/Users/mlong/Documents/Development/the-beast-system/model/beast_system/dynamics.py:256: RuntimeWarning: overflow encountered in scalar divide
  c = float(v.max() * kappa / v.min() ** 2)
Foothold(rho=1.7799999999999996, v=array([2.00000000e-001, 2.00000000e-001, 2.00000000e-001, 2.00000000e-001,
       2.00000000e-001, 9.09090909e-161]), c=inf, bound=0.0)
vmin 9.090909090909092e-161 vmin2 8.266e-321

2026-10-22T17:34:27.716114Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'git diff -- model; git status --short -- model' in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T17:34:40.505234Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 2784ms:
2026-10-22 12:34:37.851 xcodebuild[50991:4049383]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:34:37.942 xcodebuild[50991:4049382] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-TnYmSjh4' (errno=Operation not permitted)
2026-10-22 12:34:38.327 xcodebuild[50993:4049402]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:34:38.417 xcodebuild[50993:4049401] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-MTuWwBVX' (errno=Operation not permitted)
2026-10-22 12:34:39.244 xcodebuild[51025:4049706]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:34:39.337 xcodebuild[51025:4049705] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-3pbHm5W1' (errno=Operation not permitted)
2026-10-22 12:34:39.718 xcodebuild[51027:4049743]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:34:39.808 xcodebuild[51027:4049742] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
?? model/

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 /Users/mlong/.pyenv/versions/3.12.9/bin/python examples/run_all.py' in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 0ms:
Thresholds u* = 0.4, i* = 0.5. Regime values: ILLUSTRATIVE ASSUMPTIONS, not measurements.
profile                                                    H_F   H_P   H_J   H_I   H_C   H_W   U      I      A    U,I>=*  P(U>=u*)  L  B
----------------------------------------------------------------------------------------------------------------------------------------
Market capitalism                                          0.30 0.36 0.54 0.26 0.38 0.38  0.165  0.293  yes  no      0.00  0  no
Communist party-state                                      0.46 0.82 0.52 0.54 0.52 0.46  0.470  0.683  yes  yes     0.96  0  no
Democratic socialism                                       0.24 0.38 0.68 0.26 0.52 0.34  0.109  0.200  yes  no      0.00  0  no
Islamic state (plural juristic authority)                  0.34 0.38 0.38 0.38 0.44 0.38  0.222  0.290  yes  no      0.00  0  no
Islamic state (centralized clerical-political authority)   0.38 0.38 0.50 0.46 0.52 0.38  0.341  0.600  yes  no      0.01  0  no
Catholic monarchy (estates and Church-crown rivalry)       0.30 0.38 0.34 0.44 0.38 0.46  0.245  0.257  yes  no      0.00  0  no
Catholic monarchy (absolutist with venal offices)          0.46 0.82 0.42 0.46 0.68 0.46  0.456  0.560  yes  yes     0.81  0  no
Secular democracy                                          0.26 0.34 0.46 0.22 0.38 0.38  0.108  0.160  yes  no      0.00  0  no
----------------------------------------------------------------------------------------------------------------------------------------
[counter-model] G1 accountable pluralism                   0.20 0.20 0.20 0.20 0.20 0.20  0.020  0.000  yes  no      0.00  0  no
[counter-model] G2 fused capture                           1.00 1.00 1.00 1.00 1.00 1.00  1.000  1.000  yes  yes     1.00  1  yes
A does not imply B (constructive counter-model): True
P(U>=u*) = share of 2000 uniform weight draws with U >= u* (weight sensitivity).
L = evidenced capture links; regime profiles carry none, so B never holds for them.

Hard cases (Theorem A check):
  Nuer ('ordered anarchy')             A=yes counterexample=no interdependent=yes  F:informal/minimal, P:informal/minimal, J:informal/minimal, I:informal/minimal, C:informal/minimal, W:informal/minimal
  Ju/'hoansi (!Kung)                   A=yes counterexample=no interdependent=yes  F:informal/minimal, P:informal/minimal, J:informal/minimal, I:informal/minimal, C:informal/minimal, W:informal/minimal
  Ostrom commons (design principles)   A=yes counterexample=no interdependent=yes  F:informal/minimal, P:informal/minimal, J:informal/minimal, I:informal/minimal, C:informal/minimal, W:informal/minimal
  Consensus village (stylized)         A=yes counterexample=no interdependent=yes  F:informal/minimal, P:informal/minimal, J:informal/minimal, I:informal/minimal, C:informal/minimal, W:informal/minimal

Axiom independence models (Ax_k dropped, pillar k absent):
  without Ax1: missing=['F'] antecedent=no counterexample=no
  without Ax2: missing=['P'] antecedent=no counterexample=no
  without Ax3: missing=['J'] antecedent=no counterexample=no
  without Ax4: missing=['I'] antecedent=no counterexample=no
  without Ax5: missing=['C'] antecedent=no counterexample=no
  without Ax6: missing=['W'] antecedent=no counterexample=no

Generated dependency hypergraph (provider -> dependent; OR-hyperarc {I,C}->J):
  D0                             strongly connected = False; cascade-complete = False; cl({C}) = C
  D* (Ax1..Ax6 + X1,X2,X3,X5)    strongly connected = True ; cascade-complete = True ; cl({C}) = CFIJPW
  D* without X1                  strongly connected = False; cascade-complete = False; cl({C}) = CF
  D* without X2                  strongly connected = False; cascade-complete = False; cl({C}) = CFIJPW
  D* without X3                  strongly connected = False; cascade-complete = False; cl({C}) = CFIJPW
  D* without X5                  strongly connected = True ; cascade-complete = False; cl({C}) = C
  D* with X3 replaced by J->P    strongly connected = True ; cascade-complete = True ; cl({C}) = CFIJPW
  critical arcs of D*: F->W, P->F, J->F, W->P, W->I, W->C
  six brief relations alone: strongly connected = False; sinks = ['C']

Dynamics: same positive links, rho(B+) = 1.077 (some deviation persists), rho(B+ with negative feedback) = 0.914 (decays); same positive links = True

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 /Users/mlong/.pyenv/versions/3.12.9/bin/python -c 'import numpy as np; from beast_system.dynamics import foothold_bound; K=np.zeros((6,6)); K[:5,:5]=0.22; np.fill_diagonal(K,0); K[0,5]=K[5,0]=1e-155; f=foothold_bound(np.full(6,.1),np.full(6,.1),K); expected=.9*(f.rho-1)*f.v.min()**2/(2*f.v.max()*K.sum(0).max()); print(f.rho, f.v.min(), f.c, f.bound, expected)'" in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 0ms:
/Users/mlong/Documents/Development/the-beast-system/model/beast_system/dynamics.py:256: RuntimeWarning: overflow encountered in scalar divide
  c = float(v.max() * kappa / v.min() ** 2)
1.7799999999999996 9.090909090909092e-156 inf 0.0 1.6481968444778e-310

codex
- **P2 — `model/beast_system/dynamics.py:253-257`, `model/tests/test_conversion.py:99-117`:** `foothold_bound()` overflows `c` for admissible near-reducible matrices, silently returning a zero bound despite a representable positive bound. With core weights `0.22`, bidirectional links of `1e-155` to the sixth node, and `delta=0.1`, it returns `c=inf, bound=0.0`; the specified bound is approximately `1.65e-310`. Compute the bound in an overflow-safe order and add an ill-conditioned asymmetric fixture.

VERDICT: NEEDS_FIX
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
83,611
- **P2 — `model/beast_system/dynamics.py:253-257`, `model/tests/test_conversion.py:99-117`:** `foothold_bound()` overflows `c` for admissible near-reducible matrices, silently returning a zero bound despite a representable positive bound. With core weights `0.22`, bidirectional links of `1e-155` to the sixth node, and `delta=0.1`, it returns `c=inf, bound=0.0`; the specified bound is approximately `1.65e-310`. Compute the bound in an overflow-safe order and add an ill-conditioned asymmetric fixture.

VERDICT: NEEDS_FIX
