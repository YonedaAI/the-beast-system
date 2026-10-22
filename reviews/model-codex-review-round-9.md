Reading additional input from stdin...
2026-10-22T18:16:01.744705Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a164d3-c490-7f01-9a3d-7c7c527737cc
--------
user
Review only model/beast_system/representation.py, model/beast_system/uniqueness.py, model/tests/test_representation.py, model/tests/test_uniqueness.py. Do not explore elsewhere. Scoped confirmation round on the fixes for round 8 only. Round 8 items: [P1] representable() not total: zero-actor image raised ValueError (now in_formalized_class returns all-False for empty V; test_representable_is_total_on_empty_and_bad_coalitions). [P1] factorization examples not P-preserving: alpha_represent kept names, alpha_renamed depended on name order, fixtures pairwise P-distinct made same_p => same_alpha vacuous (now canonical_form(F), a colour-refinement plus lexicographic-minimum complete invariant; alpha_canonical and alpha_canonical_phi; fixtures include actor-renamed duplicates via rename_record; tests test_p_preserving_abstractions_factor_through_phi asserts >= 3 same-P pairs and bijectivity, test_name_dependent_abstraction_is_not_bijective is a negative control, test_canonical_form_is_a_complete_invariant). [P1] coalition keys not validated as actor names (now str members that are performers, share holders or link endpoints required; tested). [P2] well_formed ignored hyperarc domain (now tails non-empty subsets of labels, head a label outside the tail; test_well_formed_checks_hyperarc_domain). Also: witness pairs now asserted to share V and the role map. Confirm each item is resolved and flag any defect introduced by these fixes (especially canonical_form correctness: is it a complete invariant, is the transposition-automorphism shortcut sound). Output the findings list and the VERDICT line only. End with VERDICT: PASS or VERDICT: NEEDS_FIX.
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T18:16:03.172296Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T18:16:04.301337Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
2026-10-22T18:16:08.667462Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
I’ll inspect exactly those four files, compare each Round 8 claim to implementation and tests, and run only the two scoped test modules if the environment permits.
codex
I’m using the code-review skill to keep this confirmation round evidence-focused and severity-ranked; it will not broaden the four-file review scope.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '1,240p' /Users/mlong/.codex/plugins/cache/claude-cowork/engineering/1.1.0/skills/code-review/SKILL.md && rg -n \"the-beast-system|GrokRxiv|canonical_form|round 8\" /Users/mlong/.codex/memories/MEMORY.md" in /Users/mlong/Documents/Development/the-beast-system
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
75:# Task Group: the-beast-system comparative research-paper setup
77:applies_to: cwd=/Users/mlong/the-beast-system; reuse_rule=project contents and research conclusions must be inspected from the current files; observed planning activity is not a validated paper or published claim.
83:- extensions/skysight/resources/2026-10-22T13-40-00-mOWP-10min-memory-summary.md (cwd=/Users/mlong/the-beast-system, rollout_path=extensions/skysight/resources/2026-10-22T13-40-00-mOWP-10min-memory-summary.md, updated_at=2026-10-22T13:40:00+00:00, thread_id=None, research framing continued; no response or artifact outcome captured) [skysight memory]
84:- extensions/skysight/resources/2026-10-22T13-20-00-YYQx-10min-memory-summary.md (cwd=/Users/mlong/the-beast-system, rollout_path=extensions/skysight/resources/2026-10-22T13-20-00-YYQx-10min-memory-summary.md, updated_at=2026-10-22T13:20:00+00:00, thread_id=None, project and `context` directory created; draft revised) [skysight memory]
88:- `the-beast-system`, `context`, `six-pillars-beast-system-papers`, comparative research, Apple Notes, paper scoping, Parallels error 521
92:- The user created `the-beast-system` and a `context` subdirectory, organized source material, revised a related Apple Notes draft, and began an initial paper-scoping session. Subsequent conceptual questions and “more context” in `six-pillars-beast-system-papers` did not yield a captured research response, source inspection, plan, or artifact. [Task 1] [skysight memory]
1083:- `Matthew_Long_AI_Agent_Systems.txt`, ContextFS, GrokRxiv, JAPL, forecasting, HR analytics, FinOps, regulatory AI, network observability
1350:- AgentHero is a Rust/Tokio DAGOps platform: `crates/` holds platform mechanics, `agenthero/apps/` installed product apps, and `agenthero/plugins/` process plugins; GrokRxiv is an installed app, not the root product. [Task 1]
1771:- Use one persistent disposable environment to batch fixes, rebuild/restart changed native processes, rerun, and validate CLI/dashboard/SigNoz. A fresh isolated environment is only for final clean acceptance. Task 11 must exercise real native `agh`, GrokRxiv and Principia, artifacts, pause/resume, retry/replay, approvals, cancellation, monitoring, and dashboard behavior. [Task 1]
1772:- The observed GrokRxiv run reached moderation with 111 artifacts, then failed citation validation on unresolved `#/definitions/graph_warning`; the provider schema-composition repair was source-ready and still required native rebuild/rerun. Principia's intended deliverable is EPUB, with chapter/word budgets rather than fixed PDF pages. [Task 1]
1832:# Task Group: GrokRxiv local Docker native-platform migration and volume-safe service recovery
1833:scope: Local Docker/Compose platform detection and recovery for AgentHero, SigNoz, NATS, and GrokRxiv Supabase after a foreign-architecture override; use before recreating local containers, never as proof that a current stack is healthy.

2026-10-22T18:16:13.814945Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'wc -l model/beast_system/representation.py model/beast_system/uniqueness.py model/tests/test_representation.py model/tests/test_uniqueness.py
git diff -- model/beast_system/representation.py model/beast_system/uniqueness.py model/tests/test_representation.py model/tests/test_uniqueness.py
nl -ba model/beast_system/representation.py
nl -ba model/beast_system/uniqueness.py
nl -ba model/tests/test_representation.py
nl -ba model/tests/test_uniqueness.py' in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T18:16:22.459077Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 1811ms:
2026-10-22 13:16:21.019 xcodebuild[83371:4247254]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:16:21.199 xcodebuild[83371:4247253] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-V5m5pMkI' (errno=Operation not permitted)
2026-10-22 13:16:21.649 xcodebuild[83381:4247296]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:16:21.737 xcodebuild[83381:4247294] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
     1	"""Representation theorem and minimality (Part VII, Section 6).
     2	
     3	A FormalizedStructure F = (V, rho, A^m, s^m, Q, omega, kappa, L, D) is the formal object; the
     4	profile map ``represent`` sends a coded record of a governance system G to F_G. The theorem
     5	tested here: F_G lies in the formalized class iff Proposition A holds for G (six pillars
     6	realized, D0 present, interdependent). No uniqueness claim is made.
     7	
     8	Minimality: ``drop`` deletes a pillar and ``merge`` fuses two; fixtures in the tests show
     9	pairs of systems that become indistinguishable after coarsening although a preserved
    10	property (A.holds, U, C_mn, I) differs.
    11	
    12	Pillar labels are strings (``Pillar.name``) so that coarsened structures, whose label set is
    13	no longer M, use the same type.
    14	"""
    15	
    16	from __future__ import annotations
    17	
    18	import itertools
    19	import math
    20	from collections.abc import Iterable, Mapping
    21	from dataclasses import dataclass, field
    22	
    23	import numpy as np
    24	
    25	from .capture import CaptureLink, CaptureThresholds, Polity
    26	from .indices import hhi, validate_unit_interval, validate_weights
    27	from .necessity import (
    28	    D0_KEYS,
    29	    D_STAR_KEYS,
    30	    GovernanceSystem,
    31	    generate_dependencies,
    32	    is_strongly_connected,
    33	    realized_form,
    34	    role_map,
    35	)
    36	from .pillars import PILLARS, Pillar
    37	
    38	Label = str
    39	LabelArc = tuple[frozenset[Label], Label]
    40	M_LABELS: tuple[Label, ...] = tuple(m.name for m in PILLARS)
    41	D0_LABELS: frozenset[LabelArc] = frozenset(
    42	    (frozenset(t.name for t in tail), head.name) for tail, head in D0_KEYS
    43	)
    44	_ATOL = 1e-9
    45	_ROUND = 12
    46	
    47	
    48	@dataclass(frozen=True)
    49	class FormalizedStructure:
    50	    """F = (V, rho, A^m, s^m, Q, omega, kappa, L, D) over pillar labels ``pillars``.
    51	
    52	    ``kappa`` is keyed by coalition membership (a frozenset of actors), so it transports under
    53	    an actor bijection. ``links`` holds (source, target, pillar label) for capture links
    54	    meeting all three conditions; ``arcs`` holds hyperarcs (tail labels, head label).
    55	    """
    56	
    57	    actors: tuple[str, ...]
    58	    pillars: tuple[Label, ...]
    59	    roles: Mapping[str, frozenset[Label]]
    60	    layers: Mapping[Label, np.ndarray] = field(repr=False)
    61	    shares: Mapping[Label, Mapping[str, float]]
    62	    contestability: Mapping[Label, float]
    63	    weights: Mapping[Label, float]
    64	    kappa: Mapping[frozenset[str], Mapping[Label, float]]
    65	    links: frozenset[tuple[str, str, Label]]
    66	    arcs: frozenset[LabelArc]
    67	
    68	    def holders(self, m: Label) -> frozenset[str]:
    69	        return frozenset(v for v, ps in self.roles.items() if m in ps)
    70	
    71	
    72	# Coded records and the profile map ---------------------------------------------------------
    73	
    74	
    75	@dataclass(frozen=True)
    76	class CodedRecord:
    77	    """The coded record of a governance system: practices plus index inputs.
    78	
    79	    Well-formedness (enforced): ``shares`` has a probability vector for EVERY implemented
    80	    pillar and none for an unimplemented one, each supported on the performers of that
    81	    pillar's practices; Q has one value in [0, 1] per pillar; ``weights`` (None = 1/M each)
    82	    are non-negative and sum to 1; ``coalitions`` maps a non-empty coalition (frozenset of
    83	    actors) to kappa_m(S) in [0, 1] (None = singleton coalitions, kappa_m({v}) = s^m_v).
    84	    On this domain F2 and F3 hold for every image, so the theorem's content rests on F1, F4.
    85	    """
    86	
    87	    system: GovernanceSystem
    88	    shares: Mapping[Pillar, Mapping[str, float]]
    89	    contestability: Mapping[Pillar, float]
    90	    weights: Mapping[Pillar, float] | None = None
    91	    coalitions: Mapping[frozenset[str], Mapping[Pillar, float]] | None = None
    92	    links: tuple[CaptureLink, ...] = ()
    93	
    94	    def __post_init__(self) -> None:
    95	        roles = role_map(self.system)
    96	        implemented = {m for m in PILLARS if realized_form(self.system, m) is not None}
    97	        if any(not isinstance(m, Pillar) for m in self.shares):
    98	            raise TypeError("share keys must be Pillars")
    99	        if set(self.shares) != implemented:
   100	            raise ValueError("shares must cover exactly the implemented pillars")
   101	        for m, s in self.shares.items():
   102	            vals = [float(v) for v in s.values()]
   103	            if not vals or any(not math.isfinite(v) or v < 0 for v in vals):
   104	                raise ValueError(f"shares[{m.name}] must be finite and non-negative")
   105	            if abs(sum(vals) - 1.0) > _ATOL:
   106	                raise ValueError(f"shares[{m.name}] must sum to 1")
   107	            for actor, v in s.items():
   108	                if float(v) > 0 and m not in roles.get(actor, frozenset()):
   109	                    raise ValueError(f"{actor!r} has share in {m.name} but performs no practice")
   110	        if set(self.contestability) != set(PILLARS):
   111	            raise ValueError("contestability must give one value per pillar")
   112	        for m in PILLARS:
   113	            validate_unit_interval(self.contestability[m], f"Q[{m.name}]")
   114	        object.__setattr__(self, "weights", validate_weights(self.weights))
   115	        if self.coalitions is not None:
   116	            known = set(roles) | {a for s in self.shares.values() for a in s}
   117	            known |= {e for lk in self.links for e in (lk.source, lk.target)}
   118	            for members, row in self.coalitions.items():
   119	                if not isinstance(members, frozenset) or not members:
   120	                    raise TypeError("coalition keys must be non-empty frozensets of actors")
   121	                if any(not isinstance(v, str) for v in members):
   122	                    raise TypeError("coalition members must be actor names (str)")
   123	                if not members <= known:
   124	                    raise ValueError(f"coalition {sorted(members)} names unknown actors")
   125	                if any(not isinstance(m, Pillar) for m in row):
   126	                    raise TypeError("kappa keys must be Pillars")
   127	                for m, x in row.items():
   128	                    validate_unit_interval(x, f"kappa[{sorted(members)}][{m.name}]")
   129	
   130	
   131	def minimal_record(system: GovernanceSystem, q: float = 0.5) -> CodedRecord:
   132	    """Record with PLACEHOLDER index inputs: uniform shares over performers, Q = q everywhere.
   133	
   134	    For systems such as the hard cases, which are coded only by practices. Representability
   135	    does not depend on these values; preserved quantities computed from them are not data.
   136	    """
   137	    roles = role_map(system)
   138	    shares = {}
   139	    for m in PILLARS:
   140	        hs = sorted(a for a, ps in roles.items() if m in ps)
   141	        if hs:
   142	            shares[m] = {a: 1.0 / len(hs) for a in hs}
   143	    return CodedRecord(system, shares, {m: q for m in PILLARS})
   144	
   145	
   146	def record_from_polity(
   147	    polity: Polity, coalitions: Mapping[frozenset[str], Mapping[Pillar, float]] | None = None
   148	) -> CodedRecord:
   149	    """The coded record of a Polity (shares normalized, zero-share pillars of unimplemented
   150	    functions omitted, weights validated)."""
   151	    implemented = {m for m in PILLARS if realized_form(polity.system, m) is not None}
   152	    return CodedRecord(
   153	        system=polity.system,
   154	        shares={m: s for m, s in polity.normalized_shares.items() if m in implemented},
   155	        contestability=polity.contestability,
   156	        weights=polity.weights,
   157	        coalitions=coalitions,
   158	        links=polity.capture_links,
   159	    )
   160	
   161	
   162	def represent(record: CodedRecord) -> FormalizedStructure:
   163	    """The profile map pi: G -> F_G.
   164	
   165	    V = practice performers plus actors named in shares or links (roles come only from
   166	    practices). m in rho(v) iff v performs a practice of pillar m and m is implemented.
   167	    Shares, Q, weights, coalitions and links are copied; D = arcs generated from G's axioms.
   168	    Layers: a^m_ij = s^m_i for i != j, so out-strength shares reproduce s^m.
   169	    """
   170	    system = record.system
   171	    implemented = {m for m in PILLARS if realized_form(system, m) is not None}
   172	    performers = role_map(system)
   173	    named = {a for s in record.shares.values() for a in s}
   174	    named |= {e for link in record.links for e in (link.source, link.target)}
   175	    actors = tuple(sorted(set(performers) | named))
   176	    roles = {
   177	        v: frozenset(m.name for m in performers.get(v, frozenset()) if m in implemented)
   178	        for v in actors
   179	    }
   180	    shares = {
   181	        m.name: {v: float(record.shares.get(m, {}).get(v, 0.0)) for v in actors}
   182	        for m in PILLARS
   183	    }
   184	    idx = {v: k for k, v in enumerate(actors)}
   185	    layers = {}
   186	    for m in M_LABELS:
   187	        arr = np.zeros((len(actors), len(actors)))
   188	        for v, s in shares[m].items():
   189	            arr[idx[v], :] = s
   190	        np.fill_diagonal(arr, 0.0)
   191	        layers[m] = arr
   192	    weights = record.weights
   193	    if record.coalitions is None:
   194	        kappa = {frozenset({v}): {m: shares[m][v] for m in M_LABELS} for v in actors}
   195	    else:
   196	        kappa = {members: {m.name: float(row.get(m, 0.0)) for m in PILLARS}
   197	                 for members, row in record.coalitions.items()}
   198	    links = frozenset((lk.source, lk.target, lk.pillar.name) for lk in record.links if lk.holds)
   199	    arcs = frozenset(
   200	        (frozenset(t.name for t in tail), head.name)
   201	        for tail, head in generate_dependencies(system)
   202	    )
   203	    return FormalizedStructure(
   204	        actors=actors, pillars=M_LABELS, roles=roles, layers=layers, shares=shares,
   205	        contestability={m.name: float(record.contestability[m]) for m in PILLARS},
   206	        weights={m.name: float(weights[m]) for m in PILLARS},
   207	        kappa=kappa, links=links, arcs=arcs,
   208	    )
   209	
   210	
   211	# Formalized class --------------------------------------------------------------------------
   212	
   213	
   214	def _underlying(arcs: Iterable[LabelArc], labels: Iterable[Label]) -> dict[Label, set[Label]]:
   215	    adj: dict[Label, set[Label]] = {m: set() for m in labels}
   216	    for tail, head in arcs:
   217	        for t in tail:
   218	            adj.setdefault(t, set()).add(head)
   219	    return adj
   220	
   221	
   222	def _closure(arcs: Iterable[LabelArc], start: Iterable[Label]) -> frozenset[Label]:
   223	    """cl(S) on string labels (same rule as necessity.cascade_closure)."""
   224	    arcs = list(arcs)
   225	    closed = set(start)
   226	    changed = True
   227	    while changed:
   228	        changed = False
   229	        for tail, head in arcs:
   230	            if head not in closed and tail <= closed:
   231	                closed.add(head)
   232	                changed = True
   233	    return frozenset(closed)
   234	
   235	
   236	def _cascade_complete(arcs: Iterable[LabelArc], labels: tuple[Label, ...]) -> bool:
   237	    keep = frozenset(labels)
   238	    inside = [(t, h) for t, h in arcs if h in keep and t <= keep]
   239	    return bool(keep) and all(_closure(inside, {n}) >= keep for n in keep)
   240	
   241	
   242	@dataclass(frozen=True)
   243	class ClassMembership:
   244	    """Conditions F1..F4 of the formalized class."""
   245	
   246	    f1: bool
   247	    f2: bool
   248	    f3: bool
   249	    f4: bool
   250	
   251	    @property
   252	    def holds(self) -> bool:
   253	        return self.f1 and self.f2 and self.f3 and self.f4
   254	
   255	
   256	def well_formed(F: FormalizedStructure) -> bool:
   257	    """Domain check: every component is indexed by exactly V and the pillar labels, layers
   258	    are |V| x |V| and finite, every number is finite, and every hyperarc (T, h) has a
   259	    non-empty tail of labels and a label head outside T."""
   260	    actors, labels = set(F.actors), set(F.pillars)
   261	    if len(actors) != len(F.actors) or len(labels) != len(F.pillars):
   262	        return False
   263	    if set(F.roles) != actors or any(not ps <= labels for ps in F.roles.values()):
   264	        return False
   265	    if set(F.shares) != labels or any(set(F.shares[m]) != actors for m in labels):
   266	        return False
   267	    if set(F.layers) != labels or set(F.contestability) != labels or set(F.weights) != labels:
   268	        return False
   269	    n = len(F.actors)
   270	    for m in labels:
   271	        arr = np.asarray(F.layers[m], dtype=float)
   272	        if arr.shape != (n, n) or not np.all(np.isfinite(arr)):
   273	            return False
   274	    nums = [*(x for m in labels for x in F.shares[m].values()), *F.contestability.values(),
   275	            *F.weights.values(), *(x for r in F.kappa.values() for x in r.values())]
   276	    if not all(math.isfinite(float(x)) for x in nums):
   277	        return False
   278	    for members, row in F.kappa.items():
   279	        if not isinstance(members, frozenset) or not members or not members <= actors:
   280	            return False
   281	        if not set(row) <= labels:
   282	            return False
   283	    for tail, head in F.arcs:
   284	        if not isinstance(tail, frozenset) or not tail or not tail <= labels:
   285	            return False
   286	        if head not in labels or head in tail:
   287	            return False
   288	    return all(a in actors and b in actors and m in labels for a, b, m in F.links)
   289	
   290	
   291	def in_formalized_class(F: FormalizedStructure) -> ClassMembership:
   292	    """F1 every layer has a holder; F2 s^m a probability vector on holders of m, a^m_ij in
   293	    [0, 1] and > 0 only if i holds m; F3 Q, omega, kappa in range (omega summing to 1), link
   294	    endpoints in V; F4 D contains D0 and is strongly connected and cascade-complete.
   295	
   296	    A structure that is not ``well_formed`` (or whose labels are not the six pillars) fails
   297	    every condition.
   298	    """
   299	    if F.pillars != M_LABELS or not F.actors or not well_formed(F):
   300	        return ClassMembership(False, False, False, False)
   301	    f1 = all(F.holders(m) for m in F.pillars)
   302	    f2 = True
   303	    for m in F.pillars:
   304	        s = np.array([F.shares[m][v] for v in F.actors], dtype=float)
   305	        holders = F.holders(m)
   306	        arr = np.asarray(F.layers[m], dtype=float)
   307	        on_holders = all(F.shares[m][v] == 0.0 or v in holders for v in F.actors)
   308	        rows_ok = all(not arr[i].any() or v in holders for i, v in enumerate(F.actors))
   309	        if (s.min() < 0 or abs(s.sum() - 1.0) > _ATOL or not on_holders or not rows_ok
   310	                or arr.min() < 0.0 or arr.max() > 1.0):
   311	            f2 = False
   312	    vals = [*F.contestability.values(), *F.weights.values(),
   313	            *(x for row in F.kappa.values() for x in row.values())]
   314	    f3 = (all(0.0 <= float(x) <= 1.0 for x in vals)
   315	          and abs(sum(F.weights.values()) - 1.0) <= _ATOL)
   316	    f4 = (
   317	        D0_LABELS <= F.arcs
   318	        and is_strongly_connected(_underlying(F.arcs, F.pillars), set(F.pillars))
   319	        and _cascade_complete(F.arcs, F.pillars)
   320	    )
   321	    return ClassMembership(f1, f2, f3, f4)
   322	
   323	
   324	def representable(record: CodedRecord) -> bool:
   325	    """G is representable iff its image F_G lies in the formalized class."""
   326	    return in_formalized_class(represent(record)).holds
   327	
   328	
   329	# Preserved quantities and A-equivalence ----------------------------------------------------
   330	
   331	
   332	@dataclass(frozen=True)
   333	class PreservedQuantities:
   334	    H: dict[Label, float]
   335	    U: float
   336	    C: dict[frozenset[Label], float]
   337	    I: float  # noqa: E741  (integration statistic, math cal I)
   338	    cap: bool
   339	    inter: bool
   340	
   341	
   342	def preserved_quantities(
   343	    F: FormalizedStructure, thresholds: CaptureThresholds = CaptureThresholds()
   344	) -> PreservedQuantities:
   345	    """H_m, U, C_mn (coalition overlap), I, Cap (Proposition B) and Inter on F's own labels."""
   346	    H = {m: hhi([F.shares[m].get(v, 0.0) for v in F.actors]) if F.holders(m) else 0.0
   347	         for m in F.pillars}
   348	    U = sum(F.weights[m] * H[m] * (1.0 - F.contestability[m]) for m in F.pillars)
   349	    pairs = list(itertools.combinations(F.pillars, 2))
   350	    C = {frozenset((m, n)): max((min(row.get(m, 0.0), row.get(n, 0.0))
   351	                                 for row in F.kappa.values()), default=0.0)
   352	         for m, n in pairs}
   353	    I = sum(C.values()) / len(pairs) if pairs else 0.0  # noqa: E741
   354	    cap = U >= thresholds.u_star and I >= thresholds.i_star and bool(F.links)
   355	    inter = (is_strongly_connected(_underlying(F.arcs, F.pillars), set(F.pillars))
   356	             and _cascade_complete(F.arcs, F.pillars))
   357	    return PreservedQuantities(H, float(U), C, float(I), cap, inter)
   358	
   359	
   360	def _r(x: float) -> float:
   361	    return round(float(x), _ROUND) + 0.0
   362	
   363	
   364	def _same(a: float, b: float) -> bool:
   365	    return abs(a - b) <= _ATOL
   366	
   367	
   368	def _actor_signature(F: FormalizedStructure, k: int, with_layers: bool) -> tuple:
   369	    v = F.actors[k]
   370	    sig = (
   371	        tuple(sorted(F.roles[v])),
   372	        tuple(_r(F.shares[m][v]) for m in F.pillars),
   373	        tuple(sorted((m, a == v, b == v) for a, b, m in F.links if v in (a, b))),
   374	        tuple(sorted(tuple(_r(r.get(m, 0.0)) for m in F.pillars)
   375	                     for S, r in F.kappa.items() if v in S)),
   376	    )
   377	    if with_layers:
   378	        sig += tuple((tuple(sorted(_r(x) for x in F.layers[m][k])),
   379	                      tuple(sorted(_r(x) for x in F.layers[m][:, k]))) for m in F.pillars)
   380	    return sig
   381	
   382	
   383	def find_bijection(F: FormalizedStructure, G: FormalizedStructure,
   384	                   with_layers: bool) -> dict[str, str] | None:
   385	    """An actor bijection phi: V_F -> V_G under which roles, shares, Q, omega, kappa
   386	    (transported: kappa_F(S) = kappa_G(phi(S))), links and D agree, and, if ``with_layers``,
   387	    every layer entry. None if there is none.
   388	
   389	    Backtracking within classes of equal actor signatures; the identity on names is tried
   390	    first. Both structures must be ``well_formed``.
   391	    """
   392	    if not (well_formed(F) and well_formed(G)):
   393	        return None
   394	    if F.pillars != G.pillars or len(F.actors) != len(G.actors) or F.arcs != G.arcs:
   395	        return None
   396	    if any(not _same(F.contestability[m], G.contestability[m])
   397	           or not _same(F.weights[m], G.weights[m]) for m in F.pillars):
   398	        return None
   399	    if len(F.kappa) != len(G.kappa) or len(F.links) != len(G.links):
   400	        return None
   401	    sig_f = [_actor_signature(F, k, with_layers) for k in range(len(F.actors))]
   402	    sig_g = [_actor_signature(G, k, with_layers) for k in range(len(G.actors))]
   403	    if sorted(sig_f) != sorted(sig_g):
   404	        return None
   405	    gi = {v: k for k, v in enumerate(G.actors)}
   406	    fi = {v: k for k, v in enumerate(F.actors)}
   407	    order = sorted(range(len(F.actors)), key=lambda k: sig_f[k])
   408	    assign: dict[int, int] = {}
   409	    used: set[int] = set()
   410	
   411	    def consistent(i: int, j: int) -> bool:
   412	        if with_layers:
   413	            for i2, j2 in assign.items():
   414	                for m in F.pillars:
   415	                    if (_r(F.layers[m][i, i2]) != _r(G.layers[m][j, j2])
   416	                            or _r(F.layers[m][i2, i]) != _r(G.layers[m][j2, j])):
   417	                        return False
   418	        mapped = {**assign, i: j}
   419	        for a, b, m in F.links:
   420	            ia, ib = fi[a], fi[b]
   421	            if ia in mapped and ib in mapped:
   422	                if (G.actors[mapped[ia]], G.actors[mapped[ib]], m) not in G.links:
   423	                    return False
   424	        return True
   425	
   426	    def kappa_ok() -> bool:
   427	        to_g = {F.actors[i]: G.actors[j] for i, j in assign.items()}
   428	        for S, row in F.kappa.items():
   429	            other = G.kappa.get(frozenset(to_g[v] for v in S))
   430	            if other is None or set(other) != set(row):
   431	                return False
   432	            if any(not _same(row[m], other[m]) for m in row):
   433	                return False
   434	        return True
   435	
   436	    def search(pos: int) -> bool:
   437	        if pos == len(order):
   438	            return kappa_ok()
   439	        i = order[pos]
   440	        cands = [j for j in range(len(G.actors)) if j not in used and sig_g[j] == sig_f[i]]
   441	        pref = gi.get(F.actors[i])
   442	        if pref in cands:
   443	            cands.remove(pref)
   444	            cands.insert(0, pref)
   445	        for j in cands:
   446	            if consistent(i, j):
   447	                assign[i] = j
   448	                used.add(j)
   449	                if search(pos + 1):
   450	                    return True
   451	                del assign[i]
   452	                used.discard(j)
   453	        return False
   454	
   455	    if not search(0):
   456	        return None
   457	    return {F.actors[i]: G.actors[j] for i, j in assign.items()}
   458	
   459	
   460	def equivalent_A(F: FormalizedStructure, G: FormalizedStructure) -> bool:  # noqa: N802
   461	    """F and G agree on roles, shares, Q, omega, kappa, links and D under an actor bijection
   462	    (layers not compared; see ``uniqueness.p_equal`` for the version with layers)."""
   463	    return find_bijection(F, G, with_layers=False) is not None
   464	
   465	
   466	# Coarsenings (minimality) ------------------------------------------------------------------
   467	
   468	
   469	def drop(F: FormalizedStructure, m: Label) -> FormalizedStructure:
   470	    """Delete pillar m: its layer, shares, Q, kappa column and every hyperarc involving m.
   471	
   472	    Remaining weights are renormalized to sum 1.
   473	    """
   474	    if m not in F.pillars:
   475	        raise ValueError(f"unknown pillar {m!r}")
   476	    keep = tuple(p for p in F.pillars if p != m)
   477	    total = sum(F.weights[p] for p in keep)
   478	    weights = {p: (F.weights[p] / total if total > 0 else 1.0 / len(keep)) for p in keep}
   479	    return FormalizedStructure(
   480	        actors=F.actors, pillars=keep,
   481	        roles={v: ps - {m} for v, ps in F.roles.items()},
   482	        layers={p: F.layers[p] for p in keep},
   483	        shares={p: dict(F.shares[p]) for p in keep},
   484	        contestability={p: F.contestability[p] for p in keep},
   485	        weights=weights,
   486	        kappa={s: {p: row.get(p, 0.0) for p in keep} for s, row in F.kappa.items()},
   487	        links=frozenset(lk for lk in F.links if lk[2] != m),
   488	        arcs=frozenset((t, h) for t, h in F.arcs if h != m and m not in t),
   489	    )
   490	
   491	
   492	def merge(F: FormalizedStructure, m: Label, n: Label, lam: float) -> FormalizedStructure:
   493	    """Replace m, n by one pillar 'm+n': holders united, shares, layers, Q and kappa mixed with
   494	    weight lam on m; omega_m + omega_n; arcs relabeled, self-loops removed."""
   495	    if m == n or m not in F.pillars or n not in F.pillars:
   496	        raise ValueError("merge needs two distinct existing pillars")
   497	    lam = validate_unit_interval(lam, "lam")
   498	    new = f"{m}+{n}"
   499	    keep = tuple(new if p == m else p for p in F.pillars if p != n)
   500	    relabel = lambda p: new if p in (m, n) else p  # noqa: E731
   501	
   502	    def mix(a: float, b: float) -> float:
   503	        return lam * a + (1.0 - lam) * b
   504	
   505	    shares = {p: dict(F.shares[p]) for p in keep if p != new}
   506	    shares[new] = {v: mix(F.shares[m].get(v, 0.0), F.shares[n].get(v, 0.0)) for v in F.actors}
   507	    layers = {p: F.layers[p] for p in keep if p != new}
   508	    layers[new] = lam * F.layers[m] + (1.0 - lam) * F.layers[n]
   509	    contest = {p: F.contestability[p] for p in keep if p != new}
   510	    contest[new] = mix(F.contestability[m], F.contestability[n])
   511	    weights = {p: F.weights[p] for p in keep if p != new}
   512	    weights[new] = F.weights[m] + F.weights[n]
   513	    kappa = {}
   514	    for s, row in F.kappa.items():
   515	        r = {p: row.get(p, 0.0) for p in keep if p != new}
   516	        r[new] = mix(row.get(m, 0.0), row.get(n, 0.0))
   517	        kappa[s] = r
   518	    arcs = set()
   519	    for t, h in F.arcs:
   520	        t2, h2 = frozenset(relabel(x) for x in t), relabel(h)
   521	        if h2 not in t2:
   522	            arcs.add((t2, h2))
   523	    return FormalizedStructure(
   524	        actors=F.actors, pillars=keep,
   525	        roles={v: frozenset(relabel(p) for p in ps) for v, ps in F.roles.items()},
   526	        layers=layers, shares=shares, contestability=contest, weights=weights, kappa=kappa,
   527	        links=frozenset((a, b, relabel(p)) for a, b, p in F.links),
   528	        arcs=frozenset(arcs),
   529	    )
   530	
   531	
   532	def structurally_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   533	    """Equality of every component with the identity on actor names (floats within 1e-9)."""
   534	    if not (well_formed(F) and well_formed(G)):
   535	        return False
   536	    if (F.actors, F.pillars, F.links, F.arcs) != (G.actors, G.pillars, G.links, G.arcs):
   537	        return False
   538	    if any(F.roles[v] != G.roles[v] for v in F.actors) or set(F.kappa) != set(G.kappa):
   539	        return False
   540	    return (
   541	        all(_same(F.shares[m][v], G.shares[m][v]) for m in F.pillars for v in F.actors)
   542	        and all(np.allclose(F.layers[m], G.layers[m], atol=_ATOL, rtol=0) for m in F.pillars)
   543	        and all(_same(F.contestability[m], G.contestability[m]) for m in F.pillars)
   544	        and all(_same(F.weights[m], G.weights[m]) for m in F.pillars)
   545	        and all(set(F.kappa[S]) == set(G.kappa[S])
   546	                and all(_same(F.kappa[S][m], G.kappa[S][m]) for m in F.kappa[S])
   547	                for S in F.kappa)
   548	    )
   549	
   550	
   551	D_STAR_LABELS: frozenset[LabelArc] = frozenset(
   552	    (frozenset(t.name for t in tail), head.name) for tail, head in D_STAR_KEYS
   553	)
   554	
   555	
   556	def make_structure(
   557	    shares: Mapping[Label, Mapping[str, float]],
   558	    contestability: Mapping[Label, float],
   559	    weights: Mapping[Label, float] | None = None,
   560	    kappa: Mapping[frozenset[str], Mapping[Label, float]] | None = None,
   561	    links: Iterable[tuple[str, str, Label]] = (),
   562	    arcs: Iterable[LabelArc] = D_STAR_LABELS,
   563	) -> FormalizedStructure:
   564	    """Build F directly: holders are actors with positive share, a^m_ij = s^m_i (i != j),
   565	    singleton coalitions by default. Used for the minimality fixtures."""
   566	    pillars = tuple(shares)
   567	    actors = tuple(sorted({v for s in shares.values() for v in s}))
   568	    full = {m: {v: float(shares[m].get(v, 0.0)) for v in actors} for m in pillars}
   569	    roles = {v: frozenset(m for m in pillars if full[m][v] > 0) for v in actors}
   570	    layers = {}
   571	    for m in pillars:
   572	        arr = np.tile(np.array([full[m][v] for v in actors])[:, None], (1, len(actors)))
   573	        np.fill_diagonal(arr, 0.0)
   574	        layers[m] = arr
   575	    if kappa is None:
   576	        kappa = {frozenset({v}): {m: full[m][v] for m in pillars} for v in actors}
   577	    return FormalizedStructure(
   578	        actors=actors, pillars=pillars, roles=roles, layers=layers, shares=full,
   579	        contestability=dict(contestability),
   580	        weights=dict(weights) if weights else {m: 1.0 / len(pillars) for m in pillars},
   581	        kappa={s: dict(r) for s, r in kappa.items()},
   582	        links=frozenset(links), arcs=frozenset(arcs),
   583	    )
     1	"""Uniqueness and novelty: coarsenings, factorization through Phi, predecessor encodings.
     2	
     3	Part VII (uniqueness and novelty by proof). P(G) is the isomorphism class of represent(G):
     4	roles, shares, Q, omega, kappa, links, D and layers up to an actor bijection (``p_equal``).
     5	A coarsening c: M -> K or None merges pillars into blocks (lam-weighted) or drops them. Every
     6	c that is not a total injection collapses a witness pair (``witness_coarsening``): two
     7	systems satisfying all axioms with equal coarsened profiles but different P. Classical
     8	schemes (Parsons, Mann, Easton, Luhmann, Almond) are coarsenings; Aristotle and Weber are
     9	typologies; each has a witness pair. No uniqueness claim is made beyond these statements.
    10	"""
    11	
    12	from __future__ import annotations
    13	
    14	import itertools
    15	import math
    16	from collections.abc import Callable, Iterable, Mapping, Sequence
    17	from dataclasses import dataclass
    18	
    19	from .capture import CaptureLink
    20	from .necessity import EXTENDED_AXIOMS, GovernanceSystem, Practice
    21	from .pillars import PILLAR_TO_AXIOM, PILLARS
    22	from .representation import (
    23	    CodedRecord,
    24	    FormalizedStructure,
    25	    Label,
    26	    M_LABELS,
    27	    find_bijection,
    28	    represent,
    29	    structurally_equal,
    30	    well_formed,
    31	)
    32	
    33	_ROUND = 12
    34	_ATOL = 1e-9
    35	Coarsening = Mapping[Label, "Label | None"]
    36	
    37	
    38	# Coarsening --------------------------------------------------------------------------------
    39	
    40	
    41	def _blocks(F: FormalizedStructure, c: Coarsening) -> dict[Label, list[Label]]:
    42	    if set(c) != set(F.pillars):
    43	        raise ValueError("a coarsening must assign every pillar (None drops it)")
    44	    blocks: dict[Label, list[Label]] = {}
    45	    for m in F.pillars:
    46	        if c[m] is not None:
    47	            blocks.setdefault(c[m], []).append(m)
    48	    return blocks
    49	
    50	
    51	def _block_weights(blocks: Mapping[Label, list[Label]],
    52	                   lam: Mapping[Label, float] | None) -> dict[Label, float]:
    53	    out: dict[Label, float] = {}
    54	    for members in blocks.values():
    55	        for m in members:
    56	            out[m] = 1.0 / len(members) if lam is None else float(lam[m])
    57	        if any(not math.isfinite(out[m]) or out[m] <= 0.0 for m in members):
    58	            raise ValueError("lam_m must be positive")
    59	        if abs(sum(out[m] for m in members) - 1.0) > _ATOL:
    60	            raise ValueError("lam must sum to 1 within each block")
    61	    return out
    62	
    63	
    64	def coarsen(F: FormalizedStructure, c: Coarsening,
    65	            lam: Mapping[Label, float] | None = None) -> FormalizedStructure:
    66	    """Coarsen F by c: M -> K or None (drop), lam-weighted within each block (default equal).
    67	
    68	    Block holders are the union; shares, layers, Q and kappa are lam-weighted sums; omega_k is
    69	    the sum of omega_m (not renormalized); hyperarcs with no dropped element map to their image
    70	    under c, self-loops removed; links in dropped pillars are removed.
    71	    """
    72	    blocks = _blocks(F, c)
    73	    w = _block_weights(blocks, lam)
    74	    keys = tuple(blocks)
    75	
    76	    def mix(get: Callable[[Label], float], k: Label) -> float:
    77	        return sum(w[m] * get(m) for m in blocks[k])
    78	
    79	    shares = {k: {v: mix(lambda m: F.shares[m].get(v, 0.0), k) for v in F.actors} for k in keys}
    80	    layers = {k: sum(w[m] * F.layers[m] for m in blocks[k]) for k in keys}
    81	    arcs = set()
    82	    for tail, head in F.arcs:
    83	        if c[head] is None or any(c[t] is None for t in tail):
    84	            continue
    85	        t2, h2 = frozenset(c[t] for t in tail), c[head]
    86	        if h2 not in t2:
    87	            arcs.add((t2, h2))
    88	    return FormalizedStructure(
    89	        actors=F.actors, pillars=keys,
    90	        roles={v: frozenset(c[m] for m in ps if c[m] is not None) for v, ps in F.roles.items()},
    91	        layers=layers, shares=shares,
    92	        contestability={k: mix(lambda m: F.contestability[m], k) for k in keys},
    93	        weights={k: sum(F.weights[m] for m in blocks[k]) for k in keys},
    94	        kappa={s: {k: mix(lambda m: row.get(m, 0.0), k) for k in keys} for s, row in F.kappa.items()},
    95	        links=frozenset((a, b, c[m]) for a, b, m in F.links if c[m] is not None),
    96	        arcs=frozenset(arcs),
    97	    )
    98	
    99	
   100	IDENTITY: dict[Label, Label] = {m: m for m in M_LABELS}
   101	
   102	
   103	def phi(record: CodedRecord) -> FormalizedStructure:
   104	    """Phi = coarsen(represent(G), identity)."""
   105	    return coarsen(represent(record), IDENTITY)
   106	
   107	
   108	# P-equality --------------------------------------------------------------------------------
   109	
   110	
   111	def _r(x: float) -> float:
   112	    return round(float(x), _ROUND) + 0.0
   113	
   114	
   115	def p_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   116	    """P(F) = P(G): roles, shares, Q, omega, kappa (transported), links, D and layers agree
   117	    under an actor bijection (``representation.find_bijection`` with layers)."""
   118	    return find_bijection(F, G, with_layers=True) is not None
   119	
   120	
   121	def _global(F: FormalizedStructure) -> tuple:
   122	    return (
   123	        F.pillars,
   124	        tuple(_r(F.contestability[m]) for m in F.pillars),
   125	        tuple(_r(F.weights[m]) for m in F.pillars),
   126	        tuple(sorted((tuple(sorted(S)), tuple(_r(r.get(m, 0.0)) for m in F.pillars))
   127	                     for S, r in F.kappa.items())),
   128	        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
   129	        len(F.actors),
   130	    )
   131	
   132	
   133	def freeze(F: FormalizedStructure) -> tuple:
   134	    """Hashable encoding of F with its actor names (equality = identity on names)."""
   135	    return (
   136	        F.actors, F.pillars,
   137	        tuple(tuple(sorted(F.roles[v])) for v in F.actors),
   138	        tuple(tuple(_r(F.shares[m][v]) for v in F.actors) for m in F.pillars),
   139	        tuple(tuple(_r(x) for x in F.layers[m].ravel()) for m in F.pillars),
   140	        _global(F), tuple(sorted(F.links)),
   141	    )
   142	
   143	
   144	# Factorization through Phi -----------------------------------------------------------------
   145	
   146	
   147	@dataclass(frozen=True)
   148	class Factorization:
   149	    """alpha factors through Phi on the fixtures: alpha(G) = alpha(G2) implies P(G) = P(G2)
   150	    (``well_defined``: h(alpha(G)) = Phi(G) is a function); ``bijective``: h is also
   151	    injective onto the P-classes of the fixtures."""
   152	
   153	    well_defined: bool
   154	    bijective: bool
   155	
   156	
   157	def factor_through_phi(alpha: Callable[[CodedRecord], object],
   158	                       records: Sequence[CodedRecord]) -> Factorization:
   159	    """Check that the P-preserving abstraction ``alpha`` factors through Phi on ``records``."""
   160	    images = [alpha(r) for r in records]
   161	    phis = [phi(r) for r in records]
   162	    well_defined = injective = True
   163	    for i in range(len(records)):
   164	        for j in range(i + 1, len(records)):
   165	            same_alpha = images[i] == images[j]
   166	            same_p = p_equal(phis[i], phis[j])
   167	            if same_alpha and not same_p:
   168	                well_defined = False
   169	            if same_p and not same_alpha:
   170	                injective = False
   171	    return Factorization(well_defined, well_defined and injective)
   172	
   173	
   174	def alpha_represent(record: CodedRecord) -> tuple:
   175	    """NOT P-preserving (negative control): the frozen profile keeps actor names, so two
   176	    actor-renamed copies of one system get different values."""
   177	    return freeze(represent(record))
   178	
   179	
   180	# Canonical form (a complete invariant of P) ------------------------------------------------
   181	
   182	
   183	def _encode(F: FormalizedStructure, order: Sequence[int]) -> tuple:
   184	    """Name-free encoding of F with actors listed in ``order``."""
   185	    pos = {F.actors[k]: i for i, k in enumerate(order)}
   186	    return (
   187	        F.pillars,
   188	        tuple(tuple(sorted(F.roles[F.actors[k]])) for k in order),
   189	        tuple(tuple(_r(F.shares[m][F.actors[k]]) for k in order) for m in F.pillars),
   190	        tuple(tuple(_r(F.layers[m][i, j]) for i in order for j in order) for m in F.pillars),
   191	        tuple(_r(F.contestability[m]) for m in F.pillars),
   192	        tuple(_r(F.weights[m]) for m in F.pillars),
   193	        tuple(sorted((tuple(sorted(pos[v] for v in S)),
   194	                      tuple(_r(r.get(m, 0.0)) for m in F.pillars)) for S, r in F.kappa.items())),
   195	        tuple(sorted((pos[a], pos[b], m) for a, b, m in F.links)),
   196	        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
   197	    )
   198	
   199	
   200	def _refined_colors(F: FormalizedStructure) -> list[int]:
   201	    """Colour refinement: actor colours invariant under actor bijections, iterated until the
   202	    number of colour classes is stable."""
   203	    n = len(F.actors)
   204	    idx = {v: k for k, v in enumerate(F.actors)}
   205	
   206	    def sig0(k: int) -> tuple:
   207	        v = F.actors[k]
   208	        return (tuple(sorted(F.roles[v])), tuple(_r(F.shares[m][v]) for m in F.pillars))
   209	
   210	    def relabel(sigs: list) -> list[int]:
   211	        table = {sg: c for c, sg in enumerate(sorted(set(sigs)))}
   212	        return [table[sg] for sg in sigs]
   213	
   214	    colors = relabel([sig0(k) for k in range(n)])
   215	    while True:
   216	        sigs = []
   217	        for k in range(n):
   218	            v = F.actors[k]
   219	            sigs.append((
   220	                colors[k],
   221	                tuple(sorted((colors[j],
   222	                              tuple(_r(F.layers[m][k, j]) for m in F.pillars),
   223	                              tuple(_r(F.layers[m][j, k]) for m in F.pillars))
   224	                             for j in range(n) if j != k)),
   225	                tuple(sorted((colors[idx[b]], m, "out") for a, b, m in F.links if a == v)
   226	                      + sorted((colors[idx[a]], m, "in") for a, b, m in F.links if b == v)),
   227	                tuple(sorted((tuple(sorted(colors[idx[u]] for u in S)),
   228	                              tuple(_r(r.get(m, 0.0)) for m in F.pillars))
   229	                             for S, r in F.kappa.items() if v in S)),
   230	            ))
   231	        new = relabel(sigs)
   232	        if len(set(new)) == len(set(colors)):
   233	            return new
   234	        colors = new
   235	
   236	
   237	def canonical_form(F: FormalizedStructure, max_branch: int = 40320) -> tuple:
   238	    """A complete invariant of P: canonical_form(F) == canonical_form(G) iff p_equal(F, G).
   239	
   240	    Lexicographic minimum of ``_encode`` over actor orders consistent with the refined
   241	    colours. A colour class all of whose transpositions are automorphisms contributes no
   242	    branching (every order within it encodes identically); other classes are enumerated,
   243	    and a ValueError is raised if that would exceed ``max_branch`` orders.
   244	    """
   245	    if not well_formed(F):
   246	        raise ValueError("canonical_form needs a well-formed structure")
   247	    colors = _refined_colors(F)
   248	    classes = [sorted(k for k in range(len(F.actors)) if colors[k] == c)
   249	               for c in sorted(set(colors))]
   250	    base = [k for cl in classes for k in cl]
   251	    ref = _encode(F, base)
   252	    branching = []
   253	    for ci, cl in enumerate(classes):
   254	        start = sum(len(c) for c in classes[:ci])
   255	        swaps_ok = True
   256	        for t in range(1, len(cl)):
   257	            order = list(base)
   258	            order[start], order[start + t] = order[start + t], order[start]
   259	            if _encode(F, order) != ref:
   260	                swaps_ok = False
   261	                break
   262	        if not swaps_ok:
   263	            branching.append(ci)
   264	    total = math.prod(math.factorial(len(classes[ci])) for ci in branching)
   265	    if total > max_branch:
   266	        raise ValueError(f"canonical form would need {total} orders (> {max_branch})")
   267	    best = None
   268	    for perms in itertools.product(*(itertools.permutations(classes[ci]) for ci in branching)):
   269	        chosen = dict(zip(branching, perms))
   270	        order = [k for ci, cl in enumerate(classes) for k in chosen.get(ci, cl)]
   271	        enc = _encode(F, order)
   272	        if best is None or enc < best:
   273	            best = enc
   274	    return best
   275	
   276	
   277	def alpha_canonical(record: CodedRecord) -> tuple:
   278	    """A P-preserving abstraction: the canonical form of represent(G)."""
   279	    return canonical_form(represent(record))
   280	
   281	
   282	def alpha_canonical_phi(record: CodedRecord) -> tuple:
   283	    """A second, differently built one: the canonical form of Phi(G) (coarsen by identity)
   284	    plus a redundant field (the number of hyperarcs)."""
   285	    F = phi(record)
   286	    return (canonical_form(F), len(F.arcs))
   287	
   288	
   289	def rename_record(record: CodedRecord, mapping: Mapping[str, str]) -> CodedRecord:
   290	    """The same coded system with actors renamed by ``mapping`` (missing names kept)."""
   291	    ren = lambda v: mapping.get(v, v)  # noqa: E731
   292	    sys_ = record.system
   293	    names = set(represent(record).actors)
   294	    if len({ren(v) for v in names}) != len(names):
   295	        raise ValueError("renaming must be injective on the record's actors")
   296	    practices = tuple(
   297	        Practice(p.description, p.solves, frozenset(ren(h) for h in p.holders), p.formal,
   298	                 p.source)
   299	        for p in sys_.practices
   300	    )
   301	    system = GovernanceSystem(sys_.name, sys_.persistent, sys_.axioms, practices,
   302	                              sys_.absent_incidences, sys_.note)
   303	    links = tuple(CaptureLink(ren(lk.source), ren(lk.target), lk.pillar, lk.privileged_access,
   304	                              lk.weakens_accountability, lk.material_evidence, lk.evidence)
   305	                  for lk in record.links)
   306	    coalitions = None if record.coalitions is None else {
   307	        frozenset(ren(v) for v in S): row for S, row in record.coalitions.items()}
   308	    return CodedRecord(system, {m: {ren(v): x for v, x in sh.items()}
   309	                                for m, sh in record.shares.items()},
   310	                       record.contestability, record.weights, coalitions, links)
   311	
   312	
   313	# Witnesses ---------------------------------------------------------------------------------
   314	
   315	
   316	def two_actor_record(shares: Mapping[Label, tuple[float, float]], q: float = 0.5,
   317	                     links: Iterable = ()) -> CodedRecord:
   318	    """Actors a, b both perform every pillar; Ax1..Ax6 and X1, X2, X3, X5 hold.
   319	
   320	    ``shares[m]`` = (s^m_a, s^m_b); unspecified pillars get (1/2, 1/2).
   321	    """
   322	    practices = tuple(
   323	        Practice(f"{m.label} practice", PILLAR_TO_AXIOM[m], frozenset({"a", "b"}),
   324	                 source="synthetic witness")
   325	        for m in PILLARS
   326	    )
   327	    system = GovernanceSystem("two-actor witness", True, EXTENDED_AXIOMS, practices)
   328	    full = {m: dict(zip(("a", "b"), shares.get(m.name, (0.5, 0.5)))) for m in PILLARS}
   329	    return CodedRecord(system, full, {m: q for m in PILLARS}, links=tuple(links))
   330	
   331	
   332	def witness_coarsening(c: Coarsening, lam: Mapping[Label, float] | None = None
   333	                       ) -> tuple[CodedRecord, CodedRecord]:
   334	    """(G1, G2) with coarsen(Phi(G1), c) = coarsen(Phi(G2), c) and P(G1) != P(G2).
   335	
   336	    Merge {m, n} in one block: G1 s^m = (1, 0), s^n = (0, 1); G2 s^m = s^n = (mu, 1 - mu),
   337	    mu = lam_m / (lam_m + lam_n). Drop m: G1 s^m = (1, 0), G2 s^m = (1/2, 1/2). Raises if c
   338	    is a total injection (then no witness exists by this construction).
   339	    """
   340	    if set(c) != set(M_LABELS):
   341	        raise ValueError("c must assign all six pillars")
   342	    dropped = [m for m in M_LABELS if c[m] is None]
   343	    if dropped:
   344	        m = dropped[0]
   345	        return two_actor_record({m: (1.0, 0.0)}), two_actor_record({m: (0.5, 0.5)})
   346	    for i, m in enumerate(M_LABELS):
   347	        for n in M_LABELS[i + 1:]:
   348	            if c[m] == c[n]:
   349	                if lam is None:
   350	                    size = sum(1 for x in M_LABELS if c[x] == c[m])
   351	                    lm = ln = 1.0 / size
   352	                else:
   353	                    lm, ln = float(lam[m]), float(lam[n])
   354	                mu = lm / (lm + ln)
   355	                return (two_actor_record({m: (1.0, 0.0), n: (0.0, 1.0)}),
   356	                        two_actor_record({m: (mu, 1 - mu), n: (mu, 1 - mu)}))
   357	    raise ValueError("c is a total injection; no collapse witness")
   358	
   359	
   360	# Predecessor encodings ---------------------------------------------------------------------
   361	
   362	PARSONS: dict[Label, Label | None] = {"F": "A", "W": "A", "P": "G", "J": "I", "C": "I", "I": "L"}
   363	MANN: dict[Label, Label | None] = {"I": "Ideological", "F": "Economic", "W": "Economic",
   364	                                   "C": "Military", "P": "Political", "J": "Political"}
   365	EASTON: dict[Label, Label | None] = {"I": "Inputs", "W": "Inputs", "F": "Outputs",
   366	                                     "P": "Outputs", "J": "Outputs", "C": "Outputs"}
   367	LUHMANN: dict[Label, Label | None] = {"F": "Economy", "W": "Economy", "P": "Politics",
   368	                                      "C": "Politics", "J": "Law", "I": "Culture"}
   369	ALMOND: dict[Label, Label | None] = {"F": None, "W": None, "P": "RuleMaking",
   370	                                     "J": "RuleAdjudication", "C": "RuleApplication",
   371	                                     "I": "Inputs"}
   372	
   373	
   374	def encode_parsons(F: FormalizedStructure) -> FormalizedStructure:
   375	    """AGIL: A = {F, W}, G = {P}, I = {J, C}, L = {I}."""
   376	    return coarsen(F, PARSONS)
   377	
   378	
   379	def encode_mann(F: FormalizedStructure) -> FormalizedStructure:
   380	    """IEMP: Ideological = {I}, Economic = {F, W}, Military = {C}, Political = {P, J}."""
   381	    return coarsen(F, MANN)
   382	
   383	
   384	def encode_easton(F: FormalizedStructure) -> FormalizedStructure:
   385	    """Inputs = {I, W}, Outputs = {F, P, J, C}."""
   386	    return coarsen(F, EASTON)
   387	
   388	
   389	def encode_luhmann(F: FormalizedStructure) -> FormalizedStructure:
   390	    """Economy = {F, W}, Politics = {P, C}, Law = {J}, Culture = {I} (Luhmann splits it
   391	    further; the split does not affect the witness)."""
   392	    return coarsen(F, LUHMANN)
   393	
   394	
   395	def encode_almond(F: FormalizedStructure) -> FormalizedStructure:
   396	    """F and W dropped; RuleMaking = {P}, RuleAdjudication = {J}, RuleApplication = {C},
   397	    Inputs = {I}."""
   398	    return coarsen(F, ALMOND)
   399	
   400	
   401	def encode_aristotle(F: FormalizedStructure) -> tuple[str, str]:
   402	    """(rulers, aim): 'one' if exactly one actor has s^P > 0, 'few' if 2 to n/2, else 'many';
   403	    'deviant' if any capture link, else 'correct'. A typology, not a coarsening."""
   404	    k = sum(1 for v in F.actors if F.shares["P"].get(v, 0.0) > 0.0)
   405	    n = len(F.actors)
   406	    rulers = "one" if k == 1 else ("few" if 2 <= k <= n / 2 else "many")
   407	    return rulers, ("deviant" if F.links else "correct")
   408	
   409	
   410	WEBER_TYPES = ("traditional", "charismatic", "legal-rational")
   411	
   412	
   413	def encode_weber(F: FormalizedStructure, legitimation: str, has_staff: bool) -> tuple[str, bool]:
   414	    """(legitimation type, administrative staff). Both come from a coded field the profile
   415	    does NOT contain, so the encoding does not factor through P (nor P through it)."""
   416	    if legitimation not in WEBER_TYPES:
   417	        raise ValueError(f"legitimation must be one of {WEBER_TYPES}")
   418	    return legitimation, bool(has_staff)
   419	
   420	
   421	ENCODINGS: dict[str, Callable[[FormalizedStructure], object]] = {
   422	    "parsons": encode_parsons,
   423	    "mann": encode_mann,
   424	    "easton": encode_easton,
   425	    "luhmann": encode_luhmann,
   426	    "almond": encode_almond,
   427	    "aristotle": encode_aristotle,
   428	    "weber": lambda F: encode_weber(F, "legal-rational", True),
   429	}
   430	
   431	_WITNESS_SHARES: dict[str, tuple[dict, dict]] = {
   432	    "parsons": ({"F": (1.0, 0.0), "W": (0.0, 1.0)}, {"F": (0.5, 0.5), "W": (0.5, 0.5)}),
   433	    "mann": ({"P": (1.0, 0.0), "J": (0.0, 1.0)}, {"P": (0.5, 0.5), "J": (0.5, 0.5)}),
   434	    "easton": ({"P": (1.0, 0.0), "J": (0.0, 1.0)}, {"P": (0.5, 0.5), "J": (0.5, 0.5)}),
   435	    "luhmann": ({"F": (1.0, 0.0), "W": (0.0, 1.0)}, {"F": (0.5, 0.5), "W": (0.5, 0.5)}),
   436	    "almond": ({"F": (1.0, 0.0)}, {"F": (0.5, 0.5)}),
   437	    "aristotle": ({"J": (1.0, 0.0)}, {"J": (0.5, 0.5)}),
   438	    "weber": ({"C": (1.0, 0.0)}, {"C": (0.5, 0.5)}),
   439	}
   440	
   441	
   442	def witness_pair(k: str) -> tuple[CodedRecord, CodedRecord]:
   443	    """Two systems satisfying all axioms that encoding ``k`` cannot tell apart, with P differing.
   444	
   445	    Easton's Outputs block has four members, so equal lam gives the merge witness with
   446	    mu = 1/2 for (P, J).
   447	    """
   448	    if k not in _WITNESS_SHARES:
   449	        raise ValueError(f"unknown encoding {k!r}")
   450	    s1, s2 = _WITNESS_SHARES[k]
   451	    return two_actor_record(s1), two_actor_record(s2)
   452	
   453	
   454	def coarsenings_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   455	    """Coarsened profiles equal component by component (identity on actor names)."""
   456	    return structurally_equal(F, G)
     1	import itertools
     2	
     3	import pytest
     4	
     5	from beast_system.capture import (
     6	    a_does_not_imply_b,
     7	    assess,
     8	    corner_polities,
     9	    fused_polity,
    10	    plural_polity,
    11	)
    12	from beast_system.indices import coalition_integration, integration_statistic
    13	from beast_system.necessity import (
    14	    AXIOM_INDEPENDENCE,
    15	    BASELINE_MODEL,
    16	    EXTENDED_AXIOMS,
    17	    HARD_CASES,
    18	    JU_HOANSI,
    19	    GovernanceSystem,
    20	    check_proposition_a,
    21	)
    22	from beast_system.pillars import PILLARS, Axiom
    23	from beast_system.regimes import regime_profiles
    24	from beast_system.representation import (
    25	    M_LABELS,
    26	    FormalizedStructure,
    27	    drop,
    28	    equivalent_A,
    29	    in_formalized_class,
    30	    make_structure,
    31	    merge,
    32	    minimal_record,
    33	    preserved_quantities,
    34	    record_from_polity,
    35	    represent,
    36	    representable,
    37	    structurally_equal,
    38	)
    39	
    40	F, P, J, I, C, W = PILLARS
    41	
    42	
    43	def _all_records():
    44	    records = [(s.name, minimal_record(s)) for s in HARD_CASES]
    45	    records += [(p.label, record_from_polity(p.polity)) for p in regime_profiles()]
    46	    records += [(f"corner {k}", record_from_polity(p)) for k, p in corner_polities().items()]
    47	    records += [(f"independence {a.name}", minimal_record(s)) for a, s in AXIOM_INDEPENDENCE.items()]
    48	    no_x = GovernanceSystem("baseline without X", True, frozenset(Axiom), BASELINE_MODEL.practices)
    49	    absent = GovernanceSystem("absent Inc(Ax5, F)", True, EXTENDED_AXIOMS, JU_HOANSI.practices,
    50	                              frozenset({(Axiom.Ax5, F)}))
    51	    no_c = GovernanceSystem("no sanction practice", True, EXTENDED_AXIOMS,
    52	                            tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5))
    53	    records += [(s.name, minimal_record(s)) for s in (no_x, absent, no_c)]
    54	    return records
    55	
    56	
    57	@pytest.mark.parametrize("name,record", _all_records(), ids=[n for n, _ in _all_records()])
    58	def test_representable_iff_proposition_a(name, record):
    59	    assert representable(record) == check_proposition_a(record.system).holds
    60	
    61	
    62	def test_hard_cases_and_regimes_are_representable():
    63	    for s in HARD_CASES:
    64	        assert representable(minimal_record(s)), s.name
    65	    for p in regime_profiles():
    66	        assert representable(record_from_polity(p.polity)), p.label
    67	
    68	
    69	@pytest.mark.parametrize("axiom", list(Axiom), ids=lambda a: a.name)
    70	def test_independence_models_are_not_representable_empty_layer(axiom):
    71	    F_ = represent(minimal_record(AXIOM_INDEPENDENCE[axiom]))
    72	    assert not F_.holders(axiom.pillar.name)
    73	    assert not in_formalized_class(F_).f1
    74	
    75	
    76	def test_baseline_without_x_fails_only_f4():
    77	    no_x = GovernanceSystem("baseline without X", True, frozenset(Axiom), BASELINE_MODEL.practices)
    78	    m = in_formalized_class(represent(minimal_record(no_x)))
    79	    assert m.f1 and m.f2 and m.f3 and not m.f4
    80	
    81	
    82	@pytest.mark.parametrize("polity", [plural_polity(), fused_polity()]
    83	                         + list(corner_polities().values()), ids=lambda p: p.name)
    84	def test_represent_preserves_quantities(polity):
    85	    coalitions = None
    86	    if polity.name == "consensus grand coalition":
    87	        members = frozenset(a for a in polity.normalized_shares[F] if a.startswith("member"))
    88	        coalitions = {members: {m: 1.0 for m in PILLARS}}
    89	    F_ = represent(record_from_polity(polity, coalitions))
    90	    q = preserved_quantities(F_)
    91	    a = assess(polity)
    92	    assert q.H == pytest.approx({m.name: a.H[m] for m in PILLARS})
    93	    assert q.U == pytest.approx(a.U)
    94	    assert q.I == pytest.approx(a.I)  # these polities derive C from coalitions
    95	    assert q.cap == a.prop_b.holds
    96	    assert q.inter == a.prop_a.interdependent
    97	
    98	
    99	def test_represent_regime_quantities_h_u_inter():
   100	    for p in regime_profiles():
   101	        F_ = represent(record_from_polity(p.polity))
   102	        q = preserved_quantities(F_)
   103	        a = assess(p.polity)
   104	        assert q.U == pytest.approx(a.U) and q.inter == a.prop_a.interdependent
   105	        singleton_I = integration_statistic(coalition_integration(p.polity.normalized_shares))
   106	        assert q.I == pytest.approx(singleton_I)
   107	
   108	
   109	def _relabel(F_: FormalizedStructure, phi: dict[str, str]) -> FormalizedStructure:
   110	    return FormalizedStructure(
   111	        actors=tuple(sorted(phi[v] for v in F_.actors)), pillars=F_.pillars,
   112	        roles={phi[v]: ps for v, ps in F_.roles.items()},
   113	        layers=F_.layers,
   114	        shares={m: {phi[v]: x for v, x in s.items()} for m, s in F_.shares.items()},
   115	        contestability=F_.contestability, weights=F_.weights,
   116	        kappa={frozenset(phi[v] for v in S): row for S, row in F_.kappa.items()},
   117	        links=frozenset((phi[a], phi[b], m) for a, b, m in F_.links), arcs=F_.arcs,
   118	    )
   119	
   120	
   121	def test_equivalent_a_under_actor_bijection_preserves_quantities():
   122	    for polity in (fused_polity(), plural_polity(), regime_profiles()[1].polity):
   123	        F_ = represent(record_from_polity(polity))
   124	        phi = {v: f"x{k:03d}" for k, v in enumerate(reversed(F_.actors))}
   125	        G_ = _relabel(F_, phi)
   126	        assert equivalent_A(F_, G_)
   127	        q1, q2 = preserved_quantities(F_), preserved_quantities(G_)
   128	        assert q1.H == pytest.approx(q2.H) and q1.U == pytest.approx(q2.U)
   129	        assert q1.C == pytest.approx(q2.C) and q1.I == pytest.approx(q2.I)
   130	        assert (q1.cap, q1.inter) == (q2.cap, q2.inter)
   131	    F_ = represent(record_from_polity(fused_polity()))
   132	    changed = FormalizedStructure(**{**F_.__dict__, "contestability":
   133	                                     {**F_.contestability, "J": 0.5}})
   134	    assert not equivalent_A(F_, changed)
   135	    no_link = FormalizedStructure(**{**F_.__dict__, "links": frozenset()})
   136	    assert not equivalent_A(F_, no_link)
   137	
   138	
   139	@pytest.mark.parametrize("axiom", list(Axiom), ids=lambda a: a.name)
   140	def test_drop_makes_baseline_and_independence_model_indistinguishable(axiom):
   141	    k = axiom.pillar.name
   142	    base = represent(minimal_record(BASELINE_MODEL))
   143	    indep = represent(minimal_record(AXIOM_INDEPENDENCE[axiom]))
   144	    assert structurally_equal(drop(base, k), drop(indep, k))
   145	    assert check_proposition_a(BASELINE_MODEL).holds
   146	    assert not check_proposition_a(AXIOM_INDEPENDENCE[axiom]).holds
   147	
   148	
   149	def _merge_pair(m: str, n: str, lam: float):
   150	    others = {p: {"a": 0.5, "b": 0.5} for p in M_LABELS if p not in (m, n)}
   151	    q = {p: 0.3 for p in M_LABELS}
   152	    g1 = make_structure({**others, m: {"a": 1.0, "b": 0.0}, n: {"a": 0.0, "b": 1.0}}, q)
   153	    g2 = make_structure({**others, m: {"a": lam, "b": 1 - lam}, n: {"a": lam, "b": 1 - lam}}, q)
   154	    return g1, g2
   155	
   156	
   157	@pytest.mark.parametrize("lam", [0.2, 0.5, 0.7])
   158	@pytest.mark.parametrize("m,n", list(itertools.combinations(M_LABELS, 2)))
   159	def test_merge_makes_distinct_systems_indistinguishable(m, n, lam):
   160	    g1, g2 = _merge_pair(m, n, lam)
   161	    assert structurally_equal(merge(g1, m, n, lam), merge(g2, m, n, lam))
   162	    q1, q2 = preserved_quantities(g1), preserved_quantities(g2)
   163	    assert q1.H[m] == 1.0 and q2.H[m] == pytest.approx(lam**2 + (1 - lam) ** 2)
   164	    assert q1.U != pytest.approx(q2.U)
   165	    assert q1.C[frozenset((m, n))] == 0.0
   166	    assert q2.C[frozenset((m, n))] == pytest.approx(max(lam, 1 - lam))
   167	    assert q1.I != pytest.approx(q2.I)
   168	
   169	
   170	def test_coarsening_validation():
   171	    F_ = represent(minimal_record(BASELINE_MODEL))
   172	    with pytest.raises(ValueError):
   173	        drop(F_, "Z")
   174	    with pytest.raises(ValueError):
   175	        merge(F_, "F", "F", 0.5)
   176	    with pytest.raises(ValueError):
   177	        merge(F_, "F", "P", 1.5)
   178	    merged = merge(F_, "F", "P", 0.5)
   179	    assert merged.pillars == ("F+P", "J", "I", "C", "W")
   180	    assert sum(merged.weights.values()) == pytest.approx(1.0)
   181	    assert not in_formalized_class(merged).holds  # coarsened label set leaves the class
   182	
   183	
   184	def test_counter_model_images_both_in_class():
   185	    cm = a_does_not_imply_b()
   186	    assert cm.demonstrates_non_implication
   187	    assert representable(record_from_polity(plural_polity()))
   188	    assert representable(record_from_polity(fused_polity()))
   189	
   190	
   191	def test_coded_record_domain_is_enforced():
   192	    from beast_system.representation import CodedRecord
   193	
   194	    good = minimal_record(BASELINE_MODEL)
   195	    q = good.contestability
   196	    with pytest.raises(ValueError):
   197	        CodedRecord(BASELINE_MODEL, {}, q)  # implemented pillars without shares
   198	    with pytest.raises(ValueError):
   199	        CodedRecord(BASELINE_MODEL, {**good.shares, F: {"households": 0.5}}, q)
   200	    with pytest.raises(ValueError):
   201	        CodedRecord(BASELINE_MODEL, good.shares, q, weights={m: 0.0 for m in PILLARS})
   202	    with pytest.raises(ValueError):
   203	        CodedRecord(BASELINE_MODEL, good.shares, {F: 0.5})
   204	    with pytest.raises(TypeError):
   205	        CodedRecord(BASELINE_MODEL, good.shares, q, coalitions={"S": {F: 0.5}})
   206	    with pytest.raises(ValueError):
   207	        CodedRecord(BASELINE_MODEL, good.shares, q,
   208	                    coalitions={frozenset({"elders"}): {F: 1.5}})
   209	    indep = AXIOM_INDEPENDENCE[Axiom.Ax1]
   210	    with pytest.raises(ValueError):  # share for the unimplemented pillar F
   211	        CodedRecord(indep, {**minimal_record(indep).shares, F: {"households": 1.0}}, q)
   212	
   213	
   214	def test_theorem_on_random_well_formed_records():
   215	    import numpy as np
   216	
   217	    from beast_system.necessity import role_map
   218	    from beast_system.pillars import IncidenceAxiom
   219	    from beast_system.representation import CodedRecord
   220	
   221	    rng = np.random.default_rng(42)
   222	    axioms_all = list(EXTENDED_AXIOMS)
   223	    hits = {True: 0, False: 0}
   224	    for trial in range(300):
   225	        keep = frozenset(a for a in axioms_all if rng.uniform() < 0.9)
   226	        practices = tuple(p for p in JU_HOANSI.practices
   227	                          if p.solves in keep and rng.uniform() < 0.95)
   228	        absent = frozenset({(Axiom.Ax6, C)}) if rng.uniform() < 0.1 else frozenset()
   229	        system = GovernanceSystem(f"random {trial}", True, keep, practices, absent)
   230	        roles = role_map(system)
   231	        shares = {}
   232	        for m in PILLARS:
   233	            hs = sorted(a for a, ps in roles.items() if m in ps)
   234	            if hs:
   235	                w = rng.dirichlet(np.ones(len(hs)))
   236	                shares[m] = dict(zip(hs, w / w.sum()))
   237	        weights = dict(zip(PILLARS, rng.dirichlet(np.ones(6))))
   238	        actors = sorted(roles)
   239	        coalitions = {frozenset(rng.choice(actors, size=min(2, len(actors)), replace=False)):
   240	                      {m: float(rng.uniform()) for m in PILLARS}} if actors else None
   241	        rec = CodedRecord(system, shares, {m: float(rng.uniform()) for m in PILLARS},
   242	                          weights=weights, coalitions=coalitions)
   243	        holds = check_proposition_a(system).holds
   244	        assert representable(rec) == holds, trial
   245	        hits[holds] += 1
   246	    assert hits[True] > 10 and hits[False] > 10
   247	    assert IncidenceAxiom.X1 in EXTENDED_AXIOMS
   248	
   249	
   250	def test_class_check_rejects_malformed_structures():
   251	    F_ = represent(minimal_record(BASELINE_MODEL))
   252	    assert in_formalized_class(F_).holds
   253	    bad = [
   254	        {"contestability": {}},
   255	        {"shares": {**F_.shares, "F": {**F_.shares["F"], "ghost": 0.0}}},
   256	        {"shares": {**F_.shares, "F": {v: float("nan") for v in F_.actors}}},
   257	        {"layers": {**F_.layers, "F": F_.layers["F"][:-1]}},
   258	        {"roles": {**F_.roles, "ghost": frozenset()}},
   259	    ]
   260	    for change in bad:
   261	        m = in_formalized_class(FormalizedStructure(**{**F_.__dict__, **change}))
   262	        assert not (m.f1 or m.f2 or m.f3 or m.f4), change
   263	
   264	
   265	def test_equivalence_is_strict_on_domain_and_transports_kappa():
   266	    g = make_structure({p: {"a": 0.5, "b": 0.5} for p in M_LABELS}, {p: 0.3 for p in M_LABELS},
   267	                       kappa={frozenset({"a"}): {"F": 0.9}, frozenset({"b"}): {"F": 0.1}})
   268	    swapped = FormalizedStructure(**{**g.__dict__, "kappa": {frozenset({"a"}): {"F": 0.1},
   269	                                                             frozenset({"b"}): {"F": 0.9}}})
   270	    assert equivalent_A(g, swapped)  # a <-> b is a valid bijection here
   271	    pinned = make_structure({**{p: {"a": 0.5, "b": 0.5} for p in M_LABELS},
   272	                             "P": {"a": 0.7, "b": 0.3}}, {p: 0.3 for p in M_LABELS},
   273	                            kappa={frozenset({"a"}): {"F": 0.9}, frozenset({"b"}): {"F": 0.1}})
   274	    pinned_swapped = FormalizedStructure(**{**pinned.__dict__, "kappa": swapped.kappa})
   275	    assert not equivalent_A(pinned, pinned_swapped)  # same kappa rows, wrong members
   276	    extra = FormalizedStructure(**{**g.__dict__, "weights": {**g.weights, "Z": 0.0}})
   277	    assert not equivalent_A(g, extra)
   278	
   279	
   280	def test_representable_is_total_on_empty_and_bad_coalitions():
   281	    from beast_system.representation import CodedRecord
   282	
   283	    empty = GovernanceSystem("empty", True, EXTENDED_AXIOMS, ())
   284	    rec = CodedRecord(empty, {}, {m: 0.5 for m in PILLARS})
   285	    assert not representable(rec) and not check_proposition_a(empty).holds
   286	    good = minimal_record(BASELINE_MODEL)
   287	    with pytest.raises(TypeError):
   288	        CodedRecord(BASELINE_MODEL, good.shares, good.contestability,
   289	                    coalitions={frozenset({42}): {F: 0.5}})
   290	    with pytest.raises(ValueError):
   291	        CodedRecord(BASELINE_MODEL, good.shares, good.contestability,
   292	                    coalitions={frozenset({"stranger"}): {F: 0.5}})
   293	
   294	
   295	def test_well_formed_checks_hyperarc_domain():
   296	    from beast_system.representation import well_formed
   297	
   298	    F_ = represent(minimal_record(BASELINE_MODEL))
   299	    assert well_formed(F_)
   300	    for arc in [(frozenset({"Z"}), "F"), (frozenset({"F"}), "Z"), (frozenset({"F"}), "F"),
   301	                (frozenset(), "F")]:
   302	        G_ = FormalizedStructure(**{**F_.__dict__, "arcs": F_.arcs | {arc}})
   303	        assert not well_formed(G_) and not in_formalized_class(G_).holds, arc
     1	import itertools
     2	
     3	import numpy as np
     4	import pytest
     5	
     6	from beast_system.capture import corner_polities, fused_polity, plural_polity
     7	from beast_system.necessity import HARD_CASES, check_proposition_a
     8	from beast_system.regimes import regime_profiles
     9	from beast_system.representation import (
    10	    M_LABELS,
    11	    FormalizedStructure,
    12	    drop,
    13	    merge,
    14	    minimal_record,
    15	    record_from_polity,
    16	    represent,
    17	    representable,
    18	    structurally_equal,
    19	)
    20	from beast_system.uniqueness import (
    21	    ALMOND,
    22	    EASTON,
    23	    ENCODINGS,
    24	    IDENTITY,
    25	    LUHMANN,
    26	    MANN,
    27	    PARSONS,
    28	    alpha_canonical,
    29	    alpha_canonical_phi,
    30	    alpha_represent,
    31	    coarsen,
    32	    coarsenings_equal,
    33	    encode_aristotle,
    34	    encode_weber,
    35	    factor_through_phi,
    36	    p_equal,
    37	    phi,
    38	    rename_record,
    39	    two_actor_record,
    40	    witness_coarsening,
    41	    witness_pair,
    42	)
    43	
    44	
    45	def _fixtures():
    46	    recs = [minimal_record(s) for s in HARD_CASES]
    47	    recs += [record_from_polity(p.polity) for p in regime_profiles()]
    48	    recs += [record_from_polity(p) for p in corner_polities().values()]
    49	    recs += [record_from_polity(plural_polity()), record_from_polity(fused_polity(q=0.2))]
    50	    return recs
    51	
    52	
    53	def _all_set_partitions(items):
    54	    if not items:
    55	        yield []
    56	        return
    57	    first, rest = items[0], items[1:]
    58	    for part in _all_set_partitions(rest):
    59	        for k in range(len(part)):
    60	            yield part[:k] + [[first] + part[k]] + part[k + 1:]
    61	        yield [[first]] + part
    62	
    63	
    64	# Coarsening ---------------------------------------------------------------------------------
    65	
    66	
    67	def test_phi_equals_represent_up_to_relabeling():
    68	    for rec in _fixtures():
    69	        assert p_equal(phi(rec), represent(rec))
    70	
    71	
    72	def test_coarsen_generalizes_merge_and_drop():
    73	    F_ = represent(minimal_record(HARD_CASES[0]))
    74	    for m, n in itertools.combinations(M_LABELS, 2):
    75	        c = {p: (f"{m}+{n}" if p in (m, n) else p) for p in M_LABELS}
    76	        lam = {p: 1.0 for p in M_LABELS} | {m: 0.3, n: 0.7}
    77	        assert structurally_equal(coarsen(F_, c, lam), merge(F_, m, n, 0.3))
    78	    for m in M_LABELS:
    79	        c = {p: (None if p == m else p) for p in M_LABELS}
    80	        G_, D_ = coarsen(F_, c), drop(F_, m)
    81	        total = sum(G_.weights.values())
    82	        renorm = FormalizedStructure(**{**G_.__dict__,
    83	                                        "weights": {p: w / total for p, w in G_.weights.items()}})
    84	        assert structurally_equal(renorm, D_)  # drop() renormalizes omega, coarsen() does not
    85	
    86	
    87	def test_coarsen_validation():
    88	    F_ = represent(minimal_record(HARD_CASES[0]))
    89	    with pytest.raises(ValueError):
    90	        coarsen(F_, {"F": "F"})
    91	    with pytest.raises(ValueError):
    92	        coarsen(F_, MANN, {p: 0.5 for p in M_LABELS})  # singleton blocks need lam = 1
    93	    with pytest.raises(ValueError):
    94	        coarsen(F_, MANN, {**{p: 1.0 for p in M_LABELS}, "P": 0.0, "J": 1.0})
    95	    with pytest.raises(ValueError):
    96	        witness_coarsening(IDENTITY)
    97	
    98	
    99	# P-equality and factorization ---------------------------------------------------------------
   100	
   101	
   102	def test_p_equal_detects_renaming_and_differences():
   103	    rec = record_from_polity(fused_polity())
   104	    F_ = represent(rec)
   105	    ren = {v: f"z-{v}" for v in F_.actors}
   106	    G_ = FormalizedStructure(
   107	        actors=tuple(ren[v] for v in F_.actors), pillars=F_.pillars,
   108	        roles={ren[v]: ps for v, ps in F_.roles.items()}, layers=F_.layers,
   109	        shares={m: {ren[v]: x for v, x in s.items()} for m, s in F_.shares.items()},
   110	        contestability=F_.contestability, weights=F_.weights,
   111	        kappa={frozenset(ren[v] for v in S): r for S, r in F_.kappa.items()},
   112	        links=frozenset((ren[a], ren[b], m) for a, b, m in F_.links), arcs=F_.arcs)
   113	    assert p_equal(F_, G_)
   114	    layers = {m: a.copy() for m, a in F_.layers.items()}
   115	    layers["J"][0, 1] = 0.5
   116	    assert not p_equal(F_, FormalizedStructure(**{**F_.__dict__, "layers": layers}))
   117	
   118	
   119	def _renamed(rec, tag):
   120	    return rename_record(rec, {v: f"{tag}-{k}" for k, v in
   121	                               enumerate(reversed(represent(rec).actors))})
   122	
   123	
   124	def _fixtures_with_duplicates():
   125	    base = _fixtures()
   126	    dups = [_renamed(base[0], "r"), _renamed(record_from_polity(fused_polity()), "r"),
   127	            _renamed(record_from_polity(regime_profiles()[1].polity), "r")]
   128	    return base + [record_from_polity(fused_polity())] + dups
   129	
   130	
   131	@pytest.mark.parametrize("alpha", [alpha_canonical, alpha_canonical_phi])
   132	def test_p_preserving_abstractions_factor_through_phi(alpha):
   133	    recs = _fixtures_with_duplicates()
   134	    phis = [phi(r) for r in recs]
   135	    same_p_pairs = sum(p_equal(phis[i], phis[j])
   136	                       for i, j in itertools.combinations(range(len(recs)), 2))
   137	    assert same_p_pairs >= 3  # the same_p => same_alpha branch is exercised
   138	    result = factor_through_phi(alpha, recs)
   139	    assert result.well_defined and result.bijective
   140	
   141	
   142	def test_name_dependent_abstraction_is_not_bijective():
   143	    result = factor_through_phi(alpha_represent, _fixtures_with_duplicates())
   144	    assert result.well_defined and not result.bijective
   145	
   146	
   147	def test_canonical_form_is_a_complete_invariant():
   148	    recs = _fixtures_with_duplicates()
   149	    forms = [alpha_canonical(r) for r in recs]
   150	    phis = [phi(r) for r in recs]
   151	    for i, j in itertools.combinations(range(len(recs)), 2):
   152	        assert (forms[i] == forms[j]) == p_equal(phis[i], phis[j]), (i, j)
   153	    rng = np.random.default_rng(5)
   154	    for rec in _fixtures()[:6]:
   155	        actors = list(represent(rec).actors)
   156	        perm = rng.permutation(len(actors))
   157	        renamed = rename_record(rec, {v: f"p{perm[k]}" for k, v in enumerate(actors)})
   158	        assert alpha_canonical(renamed) == alpha_canonical(rec)
   159	
   160	
   161	def test_rename_record_must_be_injective():
   162	    rec = record_from_polity(fused_polity())
   163	    with pytest.raises(ValueError):
   164	        rename_record(rec, {v: "same" for v in represent(rec).actors})
   165	
   166	
   167	def test_fixtures_have_distinct_p_classes():
   168	    phis = [phi(r) for r in _fixtures()]
   169	    for i, j in itertools.combinations(range(len(phis)), 2):
   170	        assert not p_equal(phis[i], phis[j]), (i, j)
   171	
   172	
   173	def test_non_p_preserving_abstraction_fails_to_factor():
   174	    # Mann's encoding identifies the witness pair, so h would not be a function.
   175	    recs = list(witness_pair("mann"))
   176	    alpha = lambda r: tuple(sorted((k, round(v, 9)) for k, v in  # noqa: E731
   177	                                   coarsen(represent(r), MANN).shares["Political"].items()))
   178	    assert not factor_through_phi(alpha, recs).well_defined
   179	
   180	
   181	# Witnesses: every non-injective coarsening collapses a pair ---------------------------------
   182	
   183	
   184	def _check_witness(c, lam=None):
   185	    g1, g2 = witness_coarsening(c, lam)
   186	    r1, r2 = represent(g1), represent(g2)
   187	    assert r1.actors == r2.actors and r1.roles == r2.roles  # same V and role map
   188	    assert check_proposition_a(g1.system).holds and check_proposition_a(g2.system).holds
   189	    assert representable(g1) and representable(g2)
   190	    F1, F2 = phi(g1), phi(g2)
   191	    assert not p_equal(F1, F2)
   192	    assert coarsenings_equal(coarsen(F1, c, lam), coarsen(F2, c, lam))
   193	
   194	
   195	@pytest.mark.parametrize("m,n", list(itertools.combinations(M_LABELS, 2)))
   196	@pytest.mark.parametrize("lam_m", [0.2, 0.5, 0.9])
   197	def test_every_merge_collapses_a_witness(m, n, lam_m):
   198	    c = {p: (f"{m}+{n}" if p in (m, n) else p) for p in M_LABELS}
   199	    lam = {p: 1.0 for p in M_LABELS} | {m: lam_m, n: 1 - lam_m}
   200	    _check_witness(c, lam)
   201	
   202	
   203	@pytest.mark.parametrize("m", M_LABELS)
   204	def test_every_drop_collapses_a_witness(m):
   205	    _check_witness({p: (None if p == m else p) for p in M_LABELS})
   206	
   207	
   208	def test_pigeonhole_every_partition_with_fewer_than_six_blocks():
   209	    rng = np.random.default_rng(0)
   210	    count = 0
   211	    for part in _all_set_partitions(list(M_LABELS)):
   212	        if len(part) == 6:
   213	            continue
   214	        c = {p: "|".join(block) for block in part for p in block}
   215	        lam = {}
   216	        for block in part:
   217	            w = rng.dirichlet(np.ones(len(block)))
   218	            lam.update(dict(zip(block, w / w.sum())))
   219	        _check_witness(c, lam)
   220	        count += 1
   221	    assert count == 202  # Bell(6) - 1
   222	
   223	
   224	def test_pigeonhole_random_maps_with_drops():
   225	    rng = np.random.default_rng(1)
   226	    targets = ["k0", "k1", "k2", "k3", "k4", "k5", None]
   227	    for _ in range(150):
   228	        c = {p: targets[rng.integers(len(targets))] for p in M_LABELS}
   229	        if None not in c.values() and len(set(c.values())) == 6:
   230	            continue
   231	        _check_witness(c)
   232	
   233	
   234	# Predecessor encodings ----------------------------------------------------------------------
   235	
   236	
   237	@pytest.mark.parametrize("k", list(ENCODINGS))
   238	def test_predecessor_encoding_collapses_its_witness(k):
   239	    g1, g2 = witness_pair(k)
   240	    assert check_proposition_a(g1.system).holds and check_proposition_a(g2.system).holds
   241	    F1, F2 = represent(g1), represent(g2)
   242	    assert F1.actors == F2.actors and F1.roles == F2.roles  # same V and role map
   243	    a1, a2 = ENCODINGS[k](F1), ENCODINGS[k](F2)
   244	    if isinstance(a1, FormalizedStructure):
   245	        assert coarsenings_equal(a1, a2)
   246	    else:
   247	        assert a1 == a2
   248	    assert not p_equal(F1, F2)
   249	
   250	
   251	@pytest.mark.parametrize("cmap,blocks", [(PARSONS, 4), (MANN, 4), (EASTON, 2), (LUHMANN, 4),
   252	                                         (ALMOND, 4)])
   253	def test_coarsening_encodings_have_fewer_than_six_dimensions(cmap, blocks):
   254	    assert len({v for v in cmap.values() if v is not None}) == blocks < 6
   255	    assert set(cmap) == set(M_LABELS)
   256	
   257	
   258	def test_aristotle_typology():
   259	    F_ = represent(two_actor_record({"P": (1.0, 0.0)}))
   260	    assert encode_aristotle(F_) == ("one", "correct")
   261	    assert encode_aristotle(represent(record_from_polity(fused_polity()))) == ("one", "deviant")
   262	    assert encode_aristotle(represent(record_from_polity(plural_polity())))[0] == "few"
   263	
   264	
   265	def test_weber_label_is_not_determined_by_p():
   266	    rec = two_actor_record({})
   267	    F_ = represent(rec)
   268	    assert p_equal(F_, represent(rec))
   269	    assert encode_weber(F_, "traditional", False) != encode_weber(F_, "legal-rational", True)
   270	    with pytest.raises(ValueError):
   271	        encode_weber(F_, "theocratic", True)

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/representation.py | sed -n '350,583p'
nl -ba model/beast_system/uniqueness.py | sed -n '1,240p'
nl -ba model/beast_system/uniqueness.py | sed -n '241,456p'
nl -ba model/tests/test_representation.py | sed -n '1,180p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   350	    C = {frozenset((m, n)): max((min(row.get(m, 0.0), row.get(n, 0.0))
   351	                                 for row in F.kappa.values()), default=0.0)
   352	         for m, n in pairs}
   353	    I = sum(C.values()) / len(pairs) if pairs else 0.0  # noqa: E741
   354	    cap = U >= thresholds.u_star and I >= thresholds.i_star and bool(F.links)
   355	    inter = (is_strongly_connected(_underlying(F.arcs, F.pillars), set(F.pillars))
   356	             and _cascade_complete(F.arcs, F.pillars))
   357	    return PreservedQuantities(H, float(U), C, float(I), cap, inter)
   358	
   359	
   360	def _r(x: float) -> float:
   361	    return round(float(x), _ROUND) + 0.0
   362	
   363	
   364	def _same(a: float, b: float) -> bool:
   365	    return abs(a - b) <= _ATOL
   366	
   367	
   368	def _actor_signature(F: FormalizedStructure, k: int, with_layers: bool) -> tuple:
   369	    v = F.actors[k]
   370	    sig = (
   371	        tuple(sorted(F.roles[v])),
   372	        tuple(_r(F.shares[m][v]) for m in F.pillars),
   373	        tuple(sorted((m, a == v, b == v) for a, b, m in F.links if v in (a, b))),
   374	        tuple(sorted(tuple(_r(r.get(m, 0.0)) for m in F.pillars)
   375	                     for S, r in F.kappa.items() if v in S)),
   376	    )
   377	    if with_layers:
   378	        sig += tuple((tuple(sorted(_r(x) for x in F.layers[m][k])),
   379	                      tuple(sorted(_r(x) for x in F.layers[m][:, k]))) for m in F.pillars)
   380	    return sig
   381	
   382	
   383	def find_bijection(F: FormalizedStructure, G: FormalizedStructure,
   384	                   with_layers: bool) -> dict[str, str] | None:
   385	    """An actor bijection phi: V_F -> V_G under which roles, shares, Q, omega, kappa
   386	    (transported: kappa_F(S) = kappa_G(phi(S))), links and D agree, and, if ``with_layers``,
   387	    every layer entry. None if there is none.
   388	
   389	    Backtracking within classes of equal actor signatures; the identity on names is tried
   390	    first. Both structures must be ``well_formed``.
   391	    """
   392	    if not (well_formed(F) and well_formed(G)):
   393	        return None
   394	    if F.pillars != G.pillars or len(F.actors) != len(G.actors) or F.arcs != G.arcs:
   395	        return None
   396	    if any(not _same(F.contestability[m], G.contestability[m])
   397	           or not _same(F.weights[m], G.weights[m]) for m in F.pillars):
   398	        return None
   399	    if len(F.kappa) != len(G.kappa) or len(F.links) != len(G.links):
   400	        return None
   401	    sig_f = [_actor_signature(F, k, with_layers) for k in range(len(F.actors))]
   402	    sig_g = [_actor_signature(G, k, with_layers) for k in range(len(G.actors))]
   403	    if sorted(sig_f) != sorted(sig_g):
   404	        return None
   405	    gi = {v: k for k, v in enumerate(G.actors)}
   406	    fi = {v: k for k, v in enumerate(F.actors)}
   407	    order = sorted(range(len(F.actors)), key=lambda k: sig_f[k])
   408	    assign: dict[int, int] = {}
   409	    used: set[int] = set()
   410	
   411	    def consistent(i: int, j: int) -> bool:
   412	        if with_layers:
   413	            for i2, j2 in assign.items():
   414	                for m in F.pillars:
   415	                    if (_r(F.layers[m][i, i2]) != _r(G.layers[m][j, j2])
   416	                            or _r(F.layers[m][i2, i]) != _r(G.layers[m][j2, j])):
   417	                        return False
   418	        mapped = {**assign, i: j}
   419	        for a, b, m in F.links:
   420	            ia, ib = fi[a], fi[b]
   421	            if ia in mapped and ib in mapped:
   422	                if (G.actors[mapped[ia]], G.actors[mapped[ib]], m) not in G.links:
   423	                    return False
   424	        return True
   425	
   426	    def kappa_ok() -> bool:
   427	        to_g = {F.actors[i]: G.actors[j] for i, j in assign.items()}
   428	        for S, row in F.kappa.items():
   429	            other = G.kappa.get(frozenset(to_g[v] for v in S))
   430	            if other is None or set(other) != set(row):
   431	                return False
   432	            if any(not _same(row[m], other[m]) for m in row):
   433	                return False
   434	        return True
   435	
   436	    def search(pos: int) -> bool:
   437	        if pos == len(order):
   438	            return kappa_ok()
   439	        i = order[pos]
   440	        cands = [j for j in range(len(G.actors)) if j not in used and sig_g[j] == sig_f[i]]
   441	        pref = gi.get(F.actors[i])
   442	        if pref in cands:
   443	            cands.remove(pref)
   444	            cands.insert(0, pref)
   445	        for j in cands:
   446	            if consistent(i, j):
   447	                assign[i] = j
   448	                used.add(j)
   449	                if search(pos + 1):
   450	                    return True
   451	                del assign[i]
   452	                used.discard(j)
   453	        return False
   454	
   455	    if not search(0):
   456	        return None
   457	    return {F.actors[i]: G.actors[j] for i, j in assign.items()}
   458	
   459	
   460	def equivalent_A(F: FormalizedStructure, G: FormalizedStructure) -> bool:  # noqa: N802
   461	    """F and G agree on roles, shares, Q, omega, kappa, links and D under an actor bijection
   462	    (layers not compared; see ``uniqueness.p_equal`` for the version with layers)."""
   463	    return find_bijection(F, G, with_layers=False) is not None
   464	
   465	
   466	# Coarsenings (minimality) ------------------------------------------------------------------
   467	
   468	
   469	def drop(F: FormalizedStructure, m: Label) -> FormalizedStructure:
   470	    """Delete pillar m: its layer, shares, Q, kappa column and every hyperarc involving m.
   471	
   472	    Remaining weights are renormalized to sum 1.
   473	    """
   474	    if m not in F.pillars:
   475	        raise ValueError(f"unknown pillar {m!r}")
   476	    keep = tuple(p for p in F.pillars if p != m)
   477	    total = sum(F.weights[p] for p in keep)
   478	    weights = {p: (F.weights[p] / total if total > 0 else 1.0 / len(keep)) for p in keep}
   479	    return FormalizedStructure(
   480	        actors=F.actors, pillars=keep,
   481	        roles={v: ps - {m} for v, ps in F.roles.items()},
   482	        layers={p: F.layers[p] for p in keep},
   483	        shares={p: dict(F.shares[p]) for p in keep},
   484	        contestability={p: F.contestability[p] for p in keep},
   485	        weights=weights,
   486	        kappa={s: {p: row.get(p, 0.0) for p in keep} for s, row in F.kappa.items()},
   487	        links=frozenset(lk for lk in F.links if lk[2] != m),
   488	        arcs=frozenset((t, h) for t, h in F.arcs if h != m and m not in t),
   489	    )
   490	
   491	
   492	def merge(F: FormalizedStructure, m: Label, n: Label, lam: float) -> FormalizedStructure:
   493	    """Replace m, n by one pillar 'm+n': holders united, shares, layers, Q and kappa mixed with
   494	    weight lam on m; omega_m + omega_n; arcs relabeled, self-loops removed."""
   495	    if m == n or m not in F.pillars or n not in F.pillars:
   496	        raise ValueError("merge needs two distinct existing pillars")
   497	    lam = validate_unit_interval(lam, "lam")
   498	    new = f"{m}+{n}"
   499	    keep = tuple(new if p == m else p for p in F.pillars if p != n)
   500	    relabel = lambda p: new if p in (m, n) else p  # noqa: E731
   501	
   502	    def mix(a: float, b: float) -> float:
   503	        return lam * a + (1.0 - lam) * b
   504	
   505	    shares = {p: dict(F.shares[p]) for p in keep if p != new}
   506	    shares[new] = {v: mix(F.shares[m].get(v, 0.0), F.shares[n].get(v, 0.0)) for v in F.actors}
   507	    layers = {p: F.layers[p] for p in keep if p != new}
   508	    layers[new] = lam * F.layers[m] + (1.0 - lam) * F.layers[n]
   509	    contest = {p: F.contestability[p] for p in keep if p != new}
   510	    contest[new] = mix(F.contestability[m], F.contestability[n])
   511	    weights = {p: F.weights[p] for p in keep if p != new}
   512	    weights[new] = F.weights[m] + F.weights[n]
   513	    kappa = {}
   514	    for s, row in F.kappa.items():
   515	        r = {p: row.get(p, 0.0) for p in keep if p != new}
   516	        r[new] = mix(row.get(m, 0.0), row.get(n, 0.0))
   517	        kappa[s] = r
   518	    arcs = set()
   519	    for t, h in F.arcs:
   520	        t2, h2 = frozenset(relabel(x) for x in t), relabel(h)
   521	        if h2 not in t2:
   522	            arcs.add((t2, h2))
   523	    return FormalizedStructure(
   524	        actors=F.actors, pillars=keep,
   525	        roles={v: frozenset(relabel(p) for p in ps) for v, ps in F.roles.items()},
   526	        layers=layers, shares=shares, contestability=contest, weights=weights, kappa=kappa,
   527	        links=frozenset((a, b, relabel(p)) for a, b, p in F.links),
   528	        arcs=frozenset(arcs),
   529	    )
   530	
   531	
   532	def structurally_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   533	    """Equality of every component with the identity on actor names (floats within 1e-9)."""
   534	    if not (well_formed(F) and well_formed(G)):
   535	        return False
   536	    if (F.actors, F.pillars, F.links, F.arcs) != (G.actors, G.pillars, G.links, G.arcs):
   537	        return False
   538	    if any(F.roles[v] != G.roles[v] for v in F.actors) or set(F.kappa) != set(G.kappa):
   539	        return False
   540	    return (
   541	        all(_same(F.shares[m][v], G.shares[m][v]) for m in F.pillars for v in F.actors)
   542	        and all(np.allclose(F.layers[m], G.layers[m], atol=_ATOL, rtol=0) for m in F.pillars)
   543	        and all(_same(F.contestability[m], G.contestability[m]) for m in F.pillars)
   544	        and all(_same(F.weights[m], G.weights[m]) for m in F.pillars)
   545	        and all(set(F.kappa[S]) == set(G.kappa[S])
   546	                and all(_same(F.kappa[S][m], G.kappa[S][m]) for m in F.kappa[S])
   547	                for S in F.kappa)
   548	    )
   549	
   550	
   551	D_STAR_LABELS: frozenset[LabelArc] = frozenset(
   552	    (frozenset(t.name for t in tail), head.name) for tail, head in D_STAR_KEYS
   553	)
   554	
   555	
   556	def make_structure(
   557	    shares: Mapping[Label, Mapping[str, float]],
   558	    contestability: Mapping[Label, float],
   559	    weights: Mapping[Label, float] | None = None,
   560	    kappa: Mapping[frozenset[str], Mapping[Label, float]] | None = None,
   561	    links: Iterable[tuple[str, str, Label]] = (),
   562	    arcs: Iterable[LabelArc] = D_STAR_LABELS,
   563	) -> FormalizedStructure:
   564	    """Build F directly: holders are actors with positive share, a^m_ij = s^m_i (i != j),
   565	    singleton coalitions by default. Used for the minimality fixtures."""
   566	    pillars = tuple(shares)
   567	    actors = tuple(sorted({v for s in shares.values() for v in s}))
   568	    full = {m: {v: float(shares[m].get(v, 0.0)) for v in actors} for m in pillars}
   569	    roles = {v: frozenset(m for m in pillars if full[m][v] > 0) for v in actors}
   570	    layers = {}
   571	    for m in pillars:
   572	        arr = np.tile(np.array([full[m][v] for v in actors])[:, None], (1, len(actors)))
   573	        np.fill_diagonal(arr, 0.0)
   574	        layers[m] = arr
   575	    if kappa is None:
   576	        kappa = {frozenset({v}): {m: full[m][v] for m in pillars} for v in actors}
   577	    return FormalizedStructure(
   578	        actors=actors, pillars=pillars, roles=roles, layers=layers, shares=full,
   579	        contestability=dict(contestability),
   580	        weights=dict(weights) if weights else {m: 1.0 / len(pillars) for m in pillars},
   581	        kappa={s: dict(r) for s, r in kappa.items()},
   582	        links=frozenset(links), arcs=frozenset(arcs),
   583	    )
     1	"""Uniqueness and novelty: coarsenings, factorization through Phi, predecessor encodings.
     2	
     3	Part VII (uniqueness and novelty by proof). P(G) is the isomorphism class of represent(G):
     4	roles, shares, Q, omega, kappa, links, D and layers up to an actor bijection (``p_equal``).
     5	A coarsening c: M -> K or None merges pillars into blocks (lam-weighted) or drops them. Every
     6	c that is not a total injection collapses a witness pair (``witness_coarsening``): two
     7	systems satisfying all axioms with equal coarsened profiles but different P. Classical
     8	schemes (Parsons, Mann, Easton, Luhmann, Almond) are coarsenings; Aristotle and Weber are
     9	typologies; each has a witness pair. No uniqueness claim is made beyond these statements.
    10	"""
    11	
    12	from __future__ import annotations
    13	
    14	import itertools
    15	import math
    16	from collections.abc import Callable, Iterable, Mapping, Sequence
    17	from dataclasses import dataclass
    18	
    19	from .capture import CaptureLink
    20	from .necessity import EXTENDED_AXIOMS, GovernanceSystem, Practice
    21	from .pillars import PILLAR_TO_AXIOM, PILLARS
    22	from .representation import (
    23	    CodedRecord,
    24	    FormalizedStructure,
    25	    Label,
    26	    M_LABELS,
    27	    find_bijection,
    28	    represent,
    29	    structurally_equal,
    30	    well_formed,
    31	)
    32	
    33	_ROUND = 12
    34	_ATOL = 1e-9
    35	Coarsening = Mapping[Label, "Label | None"]
    36	
    37	
    38	# Coarsening --------------------------------------------------------------------------------
    39	
    40	
    41	def _blocks(F: FormalizedStructure, c: Coarsening) -> dict[Label, list[Label]]:
    42	    if set(c) != set(F.pillars):
    43	        raise ValueError("a coarsening must assign every pillar (None drops it)")
    44	    blocks: dict[Label, list[Label]] = {}
    45	    for m in F.pillars:
    46	        if c[m] is not None:
    47	            blocks.setdefault(c[m], []).append(m)
    48	    return blocks
    49	
    50	
    51	def _block_weights(blocks: Mapping[Label, list[Label]],
    52	                   lam: Mapping[Label, float] | None) -> dict[Label, float]:
    53	    out: dict[Label, float] = {}
    54	    for members in blocks.values():
    55	        for m in members:
    56	            out[m] = 1.0 / len(members) if lam is None else float(lam[m])
    57	        if any(not math.isfinite(out[m]) or out[m] <= 0.0 for m in members):
    58	            raise ValueError("lam_m must be positive")
    59	        if abs(sum(out[m] for m in members) - 1.0) > _ATOL:
    60	            raise ValueError("lam must sum to 1 within each block")
    61	    return out
    62	
    63	
    64	def coarsen(F: FormalizedStructure, c: Coarsening,
    65	            lam: Mapping[Label, float] | None = None) -> FormalizedStructure:
    66	    """Coarsen F by c: M -> K or None (drop), lam-weighted within each block (default equal).
    67	
    68	    Block holders are the union; shares, layers, Q and kappa are lam-weighted sums; omega_k is
    69	    the sum of omega_m (not renormalized); hyperarcs with no dropped element map to their image
    70	    under c, self-loops removed; links in dropped pillars are removed.
    71	    """
    72	    blocks = _blocks(F, c)
    73	    w = _block_weights(blocks, lam)
    74	    keys = tuple(blocks)
    75	
    76	    def mix(get: Callable[[Label], float], k: Label) -> float:
    77	        return sum(w[m] * get(m) for m in blocks[k])
    78	
    79	    shares = {k: {v: mix(lambda m: F.shares[m].get(v, 0.0), k) for v in F.actors} for k in keys}
    80	    layers = {k: sum(w[m] * F.layers[m] for m in blocks[k]) for k in keys}
    81	    arcs = set()
    82	    for tail, head in F.arcs:
    83	        if c[head] is None or any(c[t] is None for t in tail):
    84	            continue
    85	        t2, h2 = frozenset(c[t] for t in tail), c[head]
    86	        if h2 not in t2:
    87	            arcs.add((t2, h2))
    88	    return FormalizedStructure(
    89	        actors=F.actors, pillars=keys,
    90	        roles={v: frozenset(c[m] for m in ps if c[m] is not None) for v, ps in F.roles.items()},
    91	        layers=layers, shares=shares,
    92	        contestability={k: mix(lambda m: F.contestability[m], k) for k in keys},
    93	        weights={k: sum(F.weights[m] for m in blocks[k]) for k in keys},
    94	        kappa={s: {k: mix(lambda m: row.get(m, 0.0), k) for k in keys} for s, row in F.kappa.items()},
    95	        links=frozenset((a, b, c[m]) for a, b, m in F.links if c[m] is not None),
    96	        arcs=frozenset(arcs),
    97	    )
    98	
    99	
   100	IDENTITY: dict[Label, Label] = {m: m for m in M_LABELS}
   101	
   102	
   103	def phi(record: CodedRecord) -> FormalizedStructure:
   104	    """Phi = coarsen(represent(G), identity)."""
   105	    return coarsen(represent(record), IDENTITY)
   106	
   107	
   108	# P-equality --------------------------------------------------------------------------------
   109	
   110	
   111	def _r(x: float) -> float:
   112	    return round(float(x), _ROUND) + 0.0
   113	
   114	
   115	def p_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   116	    """P(F) = P(G): roles, shares, Q, omega, kappa (transported), links, D and layers agree
   117	    under an actor bijection (``representation.find_bijection`` with layers)."""
   118	    return find_bijection(F, G, with_layers=True) is not None
   119	
   120	
   121	def _global(F: FormalizedStructure) -> tuple:
   122	    return (
   123	        F.pillars,
   124	        tuple(_r(F.contestability[m]) for m in F.pillars),
   125	        tuple(_r(F.weights[m]) for m in F.pillars),
   126	        tuple(sorted((tuple(sorted(S)), tuple(_r(r.get(m, 0.0)) for m in F.pillars))
   127	                     for S, r in F.kappa.items())),
   128	        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
   129	        len(F.actors),
   130	    )
   131	
   132	
   133	def freeze(F: FormalizedStructure) -> tuple:
   134	    """Hashable encoding of F with its actor names (equality = identity on names)."""
   135	    return (
   136	        F.actors, F.pillars,
   137	        tuple(tuple(sorted(F.roles[v])) for v in F.actors),
   138	        tuple(tuple(_r(F.shares[m][v]) for v in F.actors) for m in F.pillars),
   139	        tuple(tuple(_r(x) for x in F.layers[m].ravel()) for m in F.pillars),
   140	        _global(F), tuple(sorted(F.links)),
   141	    )
   142	
   143	
   144	# Factorization through Phi -----------------------------------------------------------------
   145	
   146	
   147	@dataclass(frozen=True)
   148	class Factorization:
   149	    """alpha factors through Phi on the fixtures: alpha(G) = alpha(G2) implies P(G) = P(G2)
   150	    (``well_defined``: h(alpha(G)) = Phi(G) is a function); ``bijective``: h is also
   151	    injective onto the P-classes of the fixtures."""
   152	
   153	    well_defined: bool
   154	    bijective: bool
   155	
   156	
   157	def factor_through_phi(alpha: Callable[[CodedRecord], object],
   158	                       records: Sequence[CodedRecord]) -> Factorization:
   159	    """Check that the P-preserving abstraction ``alpha`` factors through Phi on ``records``."""
   160	    images = [alpha(r) for r in records]
   161	    phis = [phi(r) for r in records]
   162	    well_defined = injective = True
   163	    for i in range(len(records)):
   164	        for j in range(i + 1, len(records)):
   165	            same_alpha = images[i] == images[j]
   166	            same_p = p_equal(phis[i], phis[j])
   167	            if same_alpha and not same_p:
   168	                well_defined = False
   169	            if same_p and not same_alpha:
   170	                injective = False
   171	    return Factorization(well_defined, well_defined and injective)
   172	
   173	
   174	def alpha_represent(record: CodedRecord) -> tuple:
   175	    """NOT P-preserving (negative control): the frozen profile keeps actor names, so two
   176	    actor-renamed copies of one system get different values."""
   177	    return freeze(represent(record))
   178	
   179	
   180	# Canonical form (a complete invariant of P) ------------------------------------------------
   181	
   182	
   183	def _encode(F: FormalizedStructure, order: Sequence[int]) -> tuple:
   184	    """Name-free encoding of F with actors listed in ``order``."""
   185	    pos = {F.actors[k]: i for i, k in enumerate(order)}
   186	    return (
   187	        F.pillars,
   188	        tuple(tuple(sorted(F.roles[F.actors[k]])) for k in order),
   189	        tuple(tuple(_r(F.shares[m][F.actors[k]]) for k in order) for m in F.pillars),
   190	        tuple(tuple(_r(F.layers[m][i, j]) for i in order for j in order) for m in F.pillars),
   191	        tuple(_r(F.contestability[m]) for m in F.pillars),
   192	        tuple(_r(F.weights[m]) for m in F.pillars),
   193	        tuple(sorted((tuple(sorted(pos[v] for v in S)),
   194	                      tuple(_r(r.get(m, 0.0)) for m in F.pillars)) for S, r in F.kappa.items())),
   195	        tuple(sorted((pos[a], pos[b], m) for a, b, m in F.links)),
   196	        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
   197	    )
   198	
   199	
   200	def _refined_colors(F: FormalizedStructure) -> list[int]:
   201	    """Colour refinement: actor colours invariant under actor bijections, iterated until the
   202	    number of colour classes is stable."""
   203	    n = len(F.actors)
   204	    idx = {v: k for k, v in enumerate(F.actors)}
   205	
   206	    def sig0(k: int) -> tuple:
   207	        v = F.actors[k]
   208	        return (tuple(sorted(F.roles[v])), tuple(_r(F.shares[m][v]) for m in F.pillars))
   209	
   210	    def relabel(sigs: list) -> list[int]:
   211	        table = {sg: c for c, sg in enumerate(sorted(set(sigs)))}
   212	        return [table[sg] for sg in sigs]
   213	
   214	    colors = relabel([sig0(k) for k in range(n)])
   215	    while True:
   216	        sigs = []
   217	        for k in range(n):
   218	            v = F.actors[k]
   219	            sigs.append((
   220	                colors[k],
   221	                tuple(sorted((colors[j],
   222	                              tuple(_r(F.layers[m][k, j]) for m in F.pillars),
   223	                              tuple(_r(F.layers[m][j, k]) for m in F.pillars))
   224	                             for j in range(n) if j != k)),
   225	                tuple(sorted((colors[idx[b]], m, "out") for a, b, m in F.links if a == v)
   226	                      + sorted((colors[idx[a]], m, "in") for a, b, m in F.links if b == v)),
   227	                tuple(sorted((tuple(sorted(colors[idx[u]] for u in S)),
   228	                              tuple(_r(r.get(m, 0.0)) for m in F.pillars))
   229	                             for S, r in F.kappa.items() if v in S)),
   230	            ))
   231	        new = relabel(sigs)
   232	        if len(set(new)) == len(set(colors)):
   233	            return new
   234	        colors = new
   235	
   236	
   237	def canonical_form(F: FormalizedStructure, max_branch: int = 40320) -> tuple:
   238	    """A complete invariant of P: canonical_form(F) == canonical_form(G) iff p_equal(F, G).
   239	
   240	    Lexicographic minimum of ``_encode`` over actor orders consistent with the refined
   241	    colours. A colour class all of whose transpositions are automorphisms contributes no
   242	    branching (every order within it encodes identically); other classes are enumerated,
   243	    and a ValueError is raised if that would exceed ``max_branch`` orders.
   244	    """
   245	    if not well_formed(F):
   246	        raise ValueError("canonical_form needs a well-formed structure")
   247	    colors = _refined_colors(F)
   248	    classes = [sorted(k for k in range(len(F.actors)) if colors[k] == c)
   249	               for c in sorted(set(colors))]
   250	    base = [k for cl in classes for k in cl]
   251	    ref = _encode(F, base)
   252	    branching = []
   253	    for ci, cl in enumerate(classes):
   254	        start = sum(len(c) for c in classes[:ci])
   255	        swaps_ok = True
   256	        for t in range(1, len(cl)):
   257	            order = list(base)
   258	            order[start], order[start + t] = order[start + t], order[start]
   259	            if _encode(F, order) != ref:
   260	                swaps_ok = False
   261	                break
   262	        if not swaps_ok:
   263	            branching.append(ci)
   264	    total = math.prod(math.factorial(len(classes[ci])) for ci in branching)
   265	    if total > max_branch:
   266	        raise ValueError(f"canonical form would need {total} orders (> {max_branch})")
   267	    best = None
   268	    for perms in itertools.product(*(itertools.permutations(classes[ci]) for ci in branching)):
   269	        chosen = dict(zip(branching, perms))
   270	        order = [k for ci, cl in enumerate(classes) for k in chosen.get(ci, cl)]
   271	        enc = _encode(F, order)
   272	        if best is None or enc < best:
   273	            best = enc
   274	    return best
   275	
   276	
   277	def alpha_canonical(record: CodedRecord) -> tuple:
   278	    """A P-preserving abstraction: the canonical form of represent(G)."""
   279	    return canonical_form(represent(record))
   280	
   281	
   282	def alpha_canonical_phi(record: CodedRecord) -> tuple:
   283	    """A second, differently built one: the canonical form of Phi(G) (coarsen by identity)
   284	    plus a redundant field (the number of hyperarcs)."""
   285	    F = phi(record)
   286	    return (canonical_form(F), len(F.arcs))
   287	
   288	
   289	def rename_record(record: CodedRecord, mapping: Mapping[str, str]) -> CodedRecord:
   290	    """The same coded system with actors renamed by ``mapping`` (missing names kept)."""
   291	    ren = lambda v: mapping.get(v, v)  # noqa: E731
   292	    sys_ = record.system
   293	    names = set(represent(record).actors)
   294	    if len({ren(v) for v in names}) != len(names):
   295	        raise ValueError("renaming must be injective on the record's actors")
   296	    practices = tuple(
   297	        Practice(p.description, p.solves, frozenset(ren(h) for h in p.holders), p.formal,
   298	                 p.source)
   299	        for p in sys_.practices
   300	    )
   301	    system = GovernanceSystem(sys_.name, sys_.persistent, sys_.axioms, practices,
   302	                              sys_.absent_incidences, sys_.note)
   303	    links = tuple(CaptureLink(ren(lk.source), ren(lk.target), lk.pillar, lk.privileged_access,
   304	                              lk.weakens_accountability, lk.material_evidence, lk.evidence)
   305	                  for lk in record.links)
   306	    coalitions = None if record.coalitions is None else {
   307	        frozenset(ren(v) for v in S): row for S, row in record.coalitions.items()}
   308	    return CodedRecord(system, {m: {ren(v): x for v, x in sh.items()}
   309	                                for m, sh in record.shares.items()},
   310	                       record.contestability, record.weights, coalitions, links)
   311	
   312	
   313	# Witnesses ---------------------------------------------------------------------------------
   314	
   315	
   316	def two_actor_record(shares: Mapping[Label, tuple[float, float]], q: float = 0.5,
   317	                     links: Iterable = ()) -> CodedRecord:
   318	    """Actors a, b both perform every pillar; Ax1..Ax6 and X1, X2, X3, X5 hold.
   319	
   320	    ``shares[m]`` = (s^m_a, s^m_b); unspecified pillars get (1/2, 1/2).
   321	    """
   322	    practices = tuple(
   323	        Practice(f"{m.label} practice", PILLAR_TO_AXIOM[m], frozenset({"a", "b"}),
   324	                 source="synthetic witness")
   325	        for m in PILLARS
   326	    )
   327	    system = GovernanceSystem("two-actor witness", True, EXTENDED_AXIOMS, practices)
   328	    full = {m: dict(zip(("a", "b"), shares.get(m.name, (0.5, 0.5)))) for m in PILLARS}
   329	    return CodedRecord(system, full, {m: q for m in PILLARS}, links=tuple(links))
   330	
   331	
   332	def witness_coarsening(c: Coarsening, lam: Mapping[Label, float] | None = None
   333	                       ) -> tuple[CodedRecord, CodedRecord]:
   334	    """(G1, G2) with coarsen(Phi(G1), c) = coarsen(Phi(G2), c) and P(G1) != P(G2).
   335	
   336	    Merge {m, n} in one block: G1 s^m = (1, 0), s^n = (0, 1); G2 s^m = s^n = (mu, 1 - mu),
   337	    mu = lam_m / (lam_m + lam_n). Drop m: G1 s^m = (1, 0), G2 s^m = (1/2, 1/2). Raises if c
   338	    is a total injection (then no witness exists by this construction).
   339	    """
   340	    if set(c) != set(M_LABELS):
   341	        raise ValueError("c must assign all six pillars")
   342	    dropped = [m for m in M_LABELS if c[m] is None]
   343	    if dropped:
   344	        m = dropped[0]
   345	        return two_actor_record({m: (1.0, 0.0)}), two_actor_record({m: (0.5, 0.5)})
   346	    for i, m in enumerate(M_LABELS):
   347	        for n in M_LABELS[i + 1:]:
   348	            if c[m] == c[n]:
   349	                if lam is None:
   350	                    size = sum(1 for x in M_LABELS if c[x] == c[m])
   351	                    lm = ln = 1.0 / size
   352	                else:
   353	                    lm, ln = float(lam[m]), float(lam[n])
   354	                mu = lm / (lm + ln)
   355	                return (two_actor_record({m: (1.0, 0.0), n: (0.0, 1.0)}),
   356	                        two_actor_record({m: (mu, 1 - mu), n: (mu, 1 - mu)}))
   357	    raise ValueError("c is a total injection; no collapse witness")
   358	
   359	
   360	# Predecessor encodings ---------------------------------------------------------------------
   361	
   362	PARSONS: dict[Label, Label | None] = {"F": "A", "W": "A", "P": "G", "J": "I", "C": "I", "I": "L"}
   363	MANN: dict[Label, Label | None] = {"I": "Ideological", "F": "Economic", "W": "Economic",
   364	                                   "C": "Military", "P": "Political", "J": "Political"}
   365	EASTON: dict[Label, Label | None] = {"I": "Inputs", "W": "Inputs", "F": "Outputs",
   366	                                     "P": "Outputs", "J": "Outputs", "C": "Outputs"}
   367	LUHMANN: dict[Label, Label | None] = {"F": "Economy", "W": "Economy", "P": "Politics",
   368	                                      "C": "Politics", "J": "Law", "I": "Culture"}
   369	ALMOND: dict[Label, Label | None] = {"F": None, "W": None, "P": "RuleMaking",
   370	                                     "J": "RuleAdjudication", "C": "RuleApplication",
   371	                                     "I": "Inputs"}
   372	
   373	
   374	def encode_parsons(F: FormalizedStructure) -> FormalizedStructure:
   375	    """AGIL: A = {F, W}, G = {P}, I = {J, C}, L = {I}."""
   376	    return coarsen(F, PARSONS)
   377	
   378	
   379	def encode_mann(F: FormalizedStructure) -> FormalizedStructure:
   380	    """IEMP: Ideological = {I}, Economic = {F, W}, Military = {C}, Political = {P, J}."""
   381	    return coarsen(F, MANN)
   382	
   383	
   384	def encode_easton(F: FormalizedStructure) -> FormalizedStructure:
   385	    """Inputs = {I, W}, Outputs = {F, P, J, C}."""
   386	    return coarsen(F, EASTON)
   387	
   388	
   389	def encode_luhmann(F: FormalizedStructure) -> FormalizedStructure:
   390	    """Economy = {F, W}, Politics = {P, C}, Law = {J}, Culture = {I} (Luhmann splits it
   391	    further; the split does not affect the witness)."""
   392	    return coarsen(F, LUHMANN)
   393	
   394	
   395	def encode_almond(F: FormalizedStructure) -> FormalizedStructure:
   396	    """F and W dropped; RuleMaking = {P}, RuleAdjudication = {J}, RuleApplication = {C},
   397	    Inputs = {I}."""
   398	    return coarsen(F, ALMOND)
   399	
   400	
   401	def encode_aristotle(F: FormalizedStructure) -> tuple[str, str]:
   402	    """(rulers, aim): 'one' if exactly one actor has s^P > 0, 'few' if 2 to n/2, else 'many';
   403	    'deviant' if any capture link, else 'correct'. A typology, not a coarsening."""
   404	    k = sum(1 for v in F.actors if F.shares["P"].get(v, 0.0) > 0.0)
   405	    n = len(F.actors)
   406	    rulers = "one" if k == 1 else ("few" if 2 <= k <= n / 2 else "many")
   407	    return rulers, ("deviant" if F.links else "correct")
   408	
   409	
   410	WEBER_TYPES = ("traditional", "charismatic", "legal-rational")
   411	
   412	
   413	def encode_weber(F: FormalizedStructure, legitimation: str, has_staff: bool) -> tuple[str, bool]:
   414	    """(legitimation type, administrative staff). Both come from a coded field the profile
   415	    does NOT contain, so the encoding does not factor through P (nor P through it)."""
   416	    if legitimation not in WEBER_TYPES:
   417	        raise ValueError(f"legitimation must be one of {WEBER_TYPES}")
   418	    return legitimation, bool(has_staff)
   419	
   420	
   421	ENCODINGS: dict[str, Callable[[FormalizedStructure], object]] = {
   422	    "parsons": encode_parsons,
   423	    "mann": encode_mann,
   424	    "easton": encode_easton,
   425	    "luhmann": encode_luhmann,
   426	    "almond": encode_almond,
   427	    "aristotle": encode_aristotle,
   428	    "weber": lambda F: encode_weber(F, "legal-rational", True),
   429	}
   430	
   431	_WITNESS_SHARES: dict[str, tuple[dict, dict]] = {
   432	    "parsons": ({"F": (1.0, 0.0), "W": (0.0, 1.0)}, {"F": (0.5, 0.5), "W": (0.5, 0.5)}),
   433	    "mann": ({"P": (1.0, 0.0), "J": (0.0, 1.0)}, {"P": (0.5, 0.5), "J": (0.5, 0.5)}),
   434	    "easton": ({"P": (1.0, 0.0), "J": (0.0, 1.0)}, {"P": (0.5, 0.5), "J": (0.5, 0.5)}),
   435	    "luhmann": ({"F": (1.0, 0.0), "W": (0.0, 1.0)}, {"F": (0.5, 0.5), "W": (0.5, 0.5)}),
   436	    "almond": ({"F": (1.0, 0.0)}, {"F": (0.5, 0.5)}),
   437	    "aristotle": ({"J": (1.0, 0.0)}, {"J": (0.5, 0.5)}),
   438	    "weber": ({"C": (1.0, 0.0)}, {"C": (0.5, 0.5)}),
   439	}
   440	
   441	
   442	def witness_pair(k: str) -> tuple[CodedRecord, CodedRecord]:
   443	    """Two systems satisfying all axioms that encoding ``k`` cannot tell apart, with P differing.
   444	
   445	    Easton's Outputs block has four members, so equal lam gives the merge witness with
   446	    mu = 1/2 for (P, J).
   447	    """
   448	    if k not in _WITNESS_SHARES:
   449	        raise ValueError(f"unknown encoding {k!r}")
   450	    s1, s2 = _WITNESS_SHARES[k]
   451	    return two_actor_record(s1), two_actor_record(s2)
   452	
   453	
   454	def coarsenings_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   455	    """Coarsened profiles equal component by component (identity on actor names)."""
   456	    return structurally_equal(F, G)
     1	import itertools
     2	
     3	import pytest
     4	
     5	from beast_system.capture import (
     6	    a_does_not_imply_b,
     7	    assess,
     8	    corner_polities,
     9	    fused_polity,
    10	    plural_polity,
    11	)
    12	from beast_system.indices import coalition_integration, integration_statistic
    13	from beast_system.necessity import (
    14	    AXIOM_INDEPENDENCE,
    15	    BASELINE_MODEL,
    16	    EXTENDED_AXIOMS,
    17	    HARD_CASES,
    18	    JU_HOANSI,
    19	    GovernanceSystem,
    20	    check_proposition_a,
    21	)
    22	from beast_system.pillars import PILLARS, Axiom
    23	from beast_system.regimes import regime_profiles
    24	from beast_system.representation import (
    25	    M_LABELS,
    26	    FormalizedStructure,
    27	    drop,
    28	    equivalent_A,
    29	    in_formalized_class,
    30	    make_structure,
    31	    merge,
    32	    minimal_record,
    33	    preserved_quantities,
    34	    record_from_polity,
    35	    represent,
    36	    representable,
    37	    structurally_equal,
    38	)
    39	
    40	F, P, J, I, C, W = PILLARS
    41	
    42	
    43	def _all_records():
    44	    records = [(s.name, minimal_record(s)) for s in HARD_CASES]
    45	    records += [(p.label, record_from_polity(p.polity)) for p in regime_profiles()]
    46	    records += [(f"corner {k}", record_from_polity(p)) for k, p in corner_polities().items()]
    47	    records += [(f"independence {a.name}", minimal_record(s)) for a, s in AXIOM_INDEPENDENCE.items()]
    48	    no_x = GovernanceSystem("baseline without X", True, frozenset(Axiom), BASELINE_MODEL.practices)
    49	    absent = GovernanceSystem("absent Inc(Ax5, F)", True, EXTENDED_AXIOMS, JU_HOANSI.practices,
    50	                              frozenset({(Axiom.Ax5, F)}))
    51	    no_c = GovernanceSystem("no sanction practice", True, EXTENDED_AXIOMS,
    52	                            tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5))
    53	    records += [(s.name, minimal_record(s)) for s in (no_x, absent, no_c)]
    54	    return records
    55	
    56	
    57	@pytest.mark.parametrize("name,record", _all_records(), ids=[n for n, _ in _all_records()])
    58	def test_representable_iff_proposition_a(name, record):
    59	    assert representable(record) == check_proposition_a(record.system).holds
    60	
    61	
    62	def test_hard_cases_and_regimes_are_representable():
    63	    for s in HARD_CASES:
    64	        assert representable(minimal_record(s)), s.name
    65	    for p in regime_profiles():
    66	        assert representable(record_from_polity(p.polity)), p.label
    67	
    68	
    69	@pytest.mark.parametrize("axiom", list(Axiom), ids=lambda a: a.name)
    70	def test_independence_models_are_not_representable_empty_layer(axiom):
    71	    F_ = represent(minimal_record(AXIOM_INDEPENDENCE[axiom]))
    72	    assert not F_.holders(axiom.pillar.name)
    73	    assert not in_formalized_class(F_).f1
    74	
    75	
    76	def test_baseline_without_x_fails_only_f4():
    77	    no_x = GovernanceSystem("baseline without X", True, frozenset(Axiom), BASELINE_MODEL.practices)
    78	    m = in_formalized_class(represent(minimal_record(no_x)))
    79	    assert m.f1 and m.f2 and m.f3 and not m.f4
    80	
    81	
    82	@pytest.mark.parametrize("polity", [plural_polity(), fused_polity()]
    83	                         + list(corner_polities().values()), ids=lambda p: p.name)
    84	def test_represent_preserves_quantities(polity):
    85	    coalitions = None
    86	    if polity.name == "consensus grand coalition":
    87	        members = frozenset(a for a in polity.normalized_shares[F] if a.startswith("member"))
    88	        coalitions = {members: {m: 1.0 for m in PILLARS}}
    89	    F_ = represent(record_from_polity(polity, coalitions))
    90	    q = preserved_quantities(F_)
    91	    a = assess(polity)
    92	    assert q.H == pytest.approx({m.name: a.H[m] for m in PILLARS})
    93	    assert q.U == pytest.approx(a.U)
    94	    assert q.I == pytest.approx(a.I)  # these polities derive C from coalitions
    95	    assert q.cap == a.prop_b.holds
    96	    assert q.inter == a.prop_a.interdependent
    97	
    98	
    99	def test_represent_regime_quantities_h_u_inter():
   100	    for p in regime_profiles():
   101	        F_ = represent(record_from_polity(p.polity))
   102	        q = preserved_quantities(F_)
   103	        a = assess(p.polity)
   104	        assert q.U == pytest.approx(a.U) and q.inter == a.prop_a.interdependent
   105	        singleton_I = integration_statistic(coalition_integration(p.polity.normalized_shares))
   106	        assert q.I == pytest.approx(singleton_I)
   107	
   108	
   109	def _relabel(F_: FormalizedStructure, phi: dict[str, str]) -> FormalizedStructure:
   110	    return FormalizedStructure(
   111	        actors=tuple(sorted(phi[v] for v in F_.actors)), pillars=F_.pillars,
   112	        roles={phi[v]: ps for v, ps in F_.roles.items()},
   113	        layers=F_.layers,
   114	        shares={m: {phi[v]: x for v, x in s.items()} for m, s in F_.shares.items()},
   115	        contestability=F_.contestability, weights=F_.weights,
   116	        kappa={frozenset(phi[v] for v in S): row for S, row in F_.kappa.items()},
   117	        links=frozenset((phi[a], phi[b], m) for a, b, m in F_.links), arcs=F_.arcs,
   118	    )
   119	
   120	
   121	def test_equivalent_a_under_actor_bijection_preserves_quantities():
   122	    for polity in (fused_polity(), plural_polity(), regime_profiles()[1].polity):
   123	        F_ = represent(record_from_polity(polity))
   124	        phi = {v: f"x{k:03d}" for k, v in enumerate(reversed(F_.actors))}
   125	        G_ = _relabel(F_, phi)
   126	        assert equivalent_A(F_, G_)
   127	        q1, q2 = preserved_quantities(F_), preserved_quantities(G_)
   128	        assert q1.H == pytest.approx(q2.H) and q1.U == pytest.approx(q2.U)
   129	        assert q1.C == pytest.approx(q2.C) and q1.I == pytest.approx(q2.I)
   130	        assert (q1.cap, q1.inter) == (q2.cap, q2.inter)
   131	    F_ = represent(record_from_polity(fused_polity()))
   132	    changed = FormalizedStructure(**{**F_.__dict__, "contestability":
   133	                                     {**F_.contestability, "J": 0.5}})
   134	    assert not equivalent_A(F_, changed)
   135	    no_link = FormalizedStructure(**{**F_.__dict__, "links": frozenset()})
   136	    assert not equivalent_A(F_, no_link)
   137	
   138	
   139	@pytest.mark.parametrize("axiom", list(Axiom), ids=lambda a: a.name)
   140	def test_drop_makes_baseline_and_independence_model_indistinguishable(axiom):
   141	    k = axiom.pillar.name
   142	    base = represent(minimal_record(BASELINE_MODEL))
   143	    indep = represent(minimal_record(AXIOM_INDEPENDENCE[axiom]))
   144	    assert structurally_equal(drop(base, k), drop(indep, k))
   145	    assert check_proposition_a(BASELINE_MODEL).holds
   146	    assert not check_proposition_a(AXIOM_INDEPENDENCE[axiom]).holds
   147	
   148	
   149	def _merge_pair(m: str, n: str, lam: float):
   150	    others = {p: {"a": 0.5, "b": 0.5} for p in M_LABELS if p not in (m, n)}
   151	    q = {p: 0.3 for p in M_LABELS}
   152	    g1 = make_structure({**others, m: {"a": 1.0, "b": 0.0}, n: {"a": 0.0, "b": 1.0}}, q)
   153	    g2 = make_structure({**others, m: {"a": lam, "b": 1 - lam}, n: {"a": lam, "b": 1 - lam}}, q)
   154	    return g1, g2
   155	
   156	
   157	@pytest.mark.parametrize("lam", [0.2, 0.5, 0.7])
   158	@pytest.mark.parametrize("m,n", list(itertools.combinations(M_LABELS, 2)))
   159	def test_merge_makes_distinct_systems_indistinguishable(m, n, lam):
   160	    g1, g2 = _merge_pair(m, n, lam)
   161	    assert structurally_equal(merge(g1, m, n, lam), merge(g2, m, n, lam))
   162	    q1, q2 = preserved_quantities(g1), preserved_quantities(g2)
   163	    assert q1.H[m] == 1.0 and q2.H[m] == pytest.approx(lam**2 + (1 - lam) ** 2)
   164	    assert q1.U != pytest.approx(q2.U)
   165	    assert q1.C[frozenset((m, n))] == 0.0
   166	    assert q2.C[frozenset((m, n))] == pytest.approx(max(lam, 1 - lam))
   167	    assert q1.I != pytest.approx(q2.I)
   168	
   169	
   170	def test_coarsening_validation():
   171	    F_ = represent(minimal_record(BASELINE_MODEL))
   172	    with pytest.raises(ValueError):
   173	        drop(F_, "Z")
   174	    with pytest.raises(ValueError):
   175	        merge(F_, "F", "F", 0.5)
   176	    with pytest.raises(ValueError):
   177	        merge(F_, "F", "P", 1.5)
   178	    merged = merge(F_, "F", "P", 0.5)
   179	    assert merged.pillars == ("F+P", "J", "I", "C", "W")
   180	    assert sum(merged.weights.values()) == pytest.approx(1.0)

2026-10-22T18:16:25.692278Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/uniqueness.py | sed -n '144,312p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   144	# Factorization through Phi -----------------------------------------------------------------
   145	
   146	
   147	@dataclass(frozen=True)
   148	class Factorization:
   149	    """alpha factors through Phi on the fixtures: alpha(G) = alpha(G2) implies P(G) = P(G2)
   150	    (``well_defined``: h(alpha(G)) = Phi(G) is a function); ``bijective``: h is also
   151	    injective onto the P-classes of the fixtures."""
   152	
   153	    well_defined: bool
   154	    bijective: bool
   155	
   156	
   157	def factor_through_phi(alpha: Callable[[CodedRecord], object],
   158	                       records: Sequence[CodedRecord]) -> Factorization:
   159	    """Check that the P-preserving abstraction ``alpha`` factors through Phi on ``records``."""
   160	    images = [alpha(r) for r in records]
   161	    phis = [phi(r) for r in records]
   162	    well_defined = injective = True
   163	    for i in range(len(records)):
   164	        for j in range(i + 1, len(records)):
   165	            same_alpha = images[i] == images[j]
   166	            same_p = p_equal(phis[i], phis[j])
   167	            if same_alpha and not same_p:
   168	                well_defined = False
   169	            if same_p and not same_alpha:
   170	                injective = False
   171	    return Factorization(well_defined, well_defined and injective)
   172	
   173	
   174	def alpha_represent(record: CodedRecord) -> tuple:
   175	    """NOT P-preserving (negative control): the frozen profile keeps actor names, so two
   176	    actor-renamed copies of one system get different values."""
   177	    return freeze(represent(record))
   178	
   179	
   180	# Canonical form (a complete invariant of P) ------------------------------------------------
   181	
   182	
   183	def _encode(F: FormalizedStructure, order: Sequence[int]) -> tuple:
   184	    """Name-free encoding of F with actors listed in ``order``."""
   185	    pos = {F.actors[k]: i for i, k in enumerate(order)}
   186	    return (
   187	        F.pillars,
   188	        tuple(tuple(sorted(F.roles[F.actors[k]])) for k in order),
   189	        tuple(tuple(_r(F.shares[m][F.actors[k]]) for k in order) for m in F.pillars),
   190	        tuple(tuple(_r(F.layers[m][i, j]) for i in order for j in order) for m in F.pillars),
   191	        tuple(_r(F.contestability[m]) for m in F.pillars),
   192	        tuple(_r(F.weights[m]) for m in F.pillars),
   193	        tuple(sorted((tuple(sorted(pos[v] for v in S)),
   194	                      tuple(_r(r.get(m, 0.0)) for m in F.pillars)) for S, r in F.kappa.items())),
   195	        tuple(sorted((pos[a], pos[b], m) for a, b, m in F.links)),
   196	        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
   197	    )
   198	
   199	
   200	def _refined_colors(F: FormalizedStructure) -> list[int]:
   201	    """Colour refinement: actor colours invariant under actor bijections, iterated until the
   202	    number of colour classes is stable."""
   203	    n = len(F.actors)
   204	    idx = {v: k for k, v in enumerate(F.actors)}
   205	
   206	    def sig0(k: int) -> tuple:
   207	        v = F.actors[k]
   208	        return (tuple(sorted(F.roles[v])), tuple(_r(F.shares[m][v]) for m in F.pillars))
   209	
   210	    def relabel(sigs: list) -> list[int]:
   211	        table = {sg: c for c, sg in enumerate(sorted(set(sigs)))}
   212	        return [table[sg] for sg in sigs]
   213	
   214	    colors = relabel([sig0(k) for k in range(n)])
   215	    while True:
   216	        sigs = []
   217	        for k in range(n):
   218	            v = F.actors[k]
   219	            sigs.append((
   220	                colors[k],
   221	                tuple(sorted((colors[j],
   222	                              tuple(_r(F.layers[m][k, j]) for m in F.pillars),
   223	                              tuple(_r(F.layers[m][j, k]) for m in F.pillars))
   224	                             for j in range(n) if j != k)),
   225	                tuple(sorted((colors[idx[b]], m, "out") for a, b, m in F.links if a == v)
   226	                      + sorted((colors[idx[a]], m, "in") for a, b, m in F.links if b == v)),
   227	                tuple(sorted((tuple(sorted(colors[idx[u]] for u in S)),
   228	                              tuple(_r(r.get(m, 0.0)) for m in F.pillars))
   229	                             for S, r in F.kappa.items() if v in S)),
   230	            ))
   231	        new = relabel(sigs)
   232	        if len(set(new)) == len(set(colors)):
   233	            return new
   234	        colors = new
   235	
   236	
   237	def canonical_form(F: FormalizedStructure, max_branch: int = 40320) -> tuple:
   238	    """A complete invariant of P: canonical_form(F) == canonical_form(G) iff p_equal(F, G).
   239	
   240	    Lexicographic minimum of ``_encode`` over actor orders consistent with the refined
   241	    colours. A colour class all of whose transpositions are automorphisms contributes no
   242	    branching (every order within it encodes identically); other classes are enumerated,
   243	    and a ValueError is raised if that would exceed ``max_branch`` orders.
   244	    """
   245	    if not well_formed(F):
   246	        raise ValueError("canonical_form needs a well-formed structure")
   247	    colors = _refined_colors(F)
   248	    classes = [sorted(k for k in range(len(F.actors)) if colors[k] == c)
   249	               for c in sorted(set(colors))]
   250	    base = [k for cl in classes for k in cl]
   251	    ref = _encode(F, base)
   252	    branching = []
   253	    for ci, cl in enumerate(classes):
   254	        start = sum(len(c) for c in classes[:ci])
   255	        swaps_ok = True
   256	        for t in range(1, len(cl)):
   257	            order = list(base)
   258	            order[start], order[start + t] = order[start + t], order[start]
   259	            if _encode(F, order) != ref:
   260	                swaps_ok = False
   261	                break
   262	        if not swaps_ok:
   263	            branching.append(ci)
   264	    total = math.prod(math.factorial(len(classes[ci])) for ci in branching)
   265	    if total > max_branch:
   266	        raise ValueError(f"canonical form would need {total} orders (> {max_branch})")
   267	    best = None
   268	    for perms in itertools.product(*(itertools.permutations(classes[ci]) for ci in branching)):
   269	        chosen = dict(zip(branching, perms))
   270	        order = [k for ci, cl in enumerate(classes) for k in chosen.get(ci, cl)]
   271	        enc = _encode(F, order)
   272	        if best is None or enc < best:
   273	            best = enc
   274	    return best
   275	
   276	
   277	def alpha_canonical(record: CodedRecord) -> tuple:
   278	    """A P-preserving abstraction: the canonical form of represent(G)."""
   279	    return canonical_form(represent(record))
   280	
   281	
   282	def alpha_canonical_phi(record: CodedRecord) -> tuple:
   283	    """A second, differently built one: the canonical form of Phi(G) (coarsen by identity)
   284	    plus a redundant field (the number of hyperarcs)."""
   285	    F = phi(record)
   286	    return (canonical_form(F), len(F.arcs))
   287	
   288	
   289	def rename_record(record: CodedRecord, mapping: Mapping[str, str]) -> CodedRecord:
   290	    """The same coded system with actors renamed by ``mapping`` (missing names kept)."""
   291	    ren = lambda v: mapping.get(v, v)  # noqa: E731
   292	    sys_ = record.system
   293	    names = set(represent(record).actors)
   294	    if len({ren(v) for v in names}) != len(names):
   295	        raise ValueError("renaming must be injective on the record's actors")
   296	    practices = tuple(
   297	        Practice(p.description, p.solves, frozenset(ren(h) for h in p.holders), p.formal,
   298	                 p.source)
   299	        for p in sys_.practices
   300	    )
   301	    system = GovernanceSystem(sys_.name, sys_.persistent, sys_.axioms, practices,
   302	                              sys_.absent_incidences, sys_.note)
   303	    links = tuple(CaptureLink(ren(lk.source), ren(lk.target), lk.pillar, lk.privileged_access,
   304	                              lk.weakens_accountability, lk.material_evidence, lk.evidence)
   305	                  for lk in record.links)
   306	    coalitions = None if record.coalitions is None else {
   307	        frozenset(ren(v) for v in S): row for S, row in record.coalitions.items()}
   308	    return CodedRecord(system, {m: {ren(v): x for v, x in sh.items()}
   309	                                for m, sh in record.shares.items()},
   310	                       record.contestability, record.weights, coalitions, links)
   311	
   312	

2026-10-22T18:16:28.156259Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
The four fixes are present in code and tests. I’m now stress-checking the canonical invariant against the exact equivalence relation, including the shortcut’s group-theoretic assumption and numeric tolerance boundary.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 python -m pytest -p no:cacheprovider model/tests/test_representation.py model/tests/test_uniqueness.py' in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T18:16:49.941061Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 exited 1 in 245ms:
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
FileNotFoundError: [Errno 2] No usable temporary directory found in ['/var/folders/6z/np99jwkj4ys5z6l5y0xpwdx80000gn/T/', '/tmp', '/var/tmp', '/usr/tmp', '/Users/mlong/Documents/Development/the-beast-system']

codex
The scoped suite could not start because this read-only environment has no writable temporary directory; I’m retrying with capture and third-party plugin loading disabled, without changing files.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -s -p no:cacheprovider model/tests/test_representation.py model/tests/test_uniqueness.py' in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T18:16:55.349877Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 1149ms:
============================= test session starts ==============================
platform darwin -- Python 3.12.9, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/mlong/Documents/Development/the-beast-system/model
configfile: pyproject.toml
collected 178 items

model/tests/test_representation.py ....................................................................................................
model/tests/test_uniqueness.py ..............................................................................

============================= 178 passed in 0.98s ==============================

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=model python -c 'from beast_system.representation import M_LABELS, FormalizedStructure, make_structure; from beast_system.uniqueness import p_equal, canonical_form; F=make_structure({m:{\"a\":0.5,\"b\":0.5} for m in M_LABELS},{m:0.3 for m in M_LABELS}); G=FormalizedStructure(**{**F.__dict__,\"contestability\":{**F.contestability,\"F\":0.3000000005}}); print(\"p_equal\",p_equal(F,G)); print(\"canonical_equal\",canonical_form(F)==canonical_form(G))'" in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T18:17:02.279084Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 159ms:
p_equal True
canonical_equal False

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=model python -c 'from beast_system.representation import M_LABELS, make_structure; from beast_system.uniqueness import canonical_form; actors=[f\"a{i}\" for i in range(9)]; shares={m:{v:1/9 for v in actors} for m in M_LABELS}; F=make_structure(shares,{m:0.3 for m in M_LABELS},links={(actors[i],actors[(i+1)%9],\"F\") for i in range(9)}); print(\"actors\",len(F.actors));
try: canonical_form(F)
except Exception as e: print(type(e).__name__,str(e))'" in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T18:17:32.468834Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 151ms:
actors 9
ValueError canonical form would need 362880 orders (> 40320)

codex
- [P1] `canonical_form` is not a complete invariant of `p_equal`. [`find_bijection`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py:396) accepts contestability/weight differences up to `1e-9`, while [`canonical_form`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/uniqueness.py:191) compares 12-decimal encodings exactly. Reproduced: a `5e-10` contestability change gives `p_equal(F, G) == True` but unequal canonical forms. Use one exact normalization consistently; tolerance equality is non-transitive and cannot support a complete invariant.

- [P1] `canonical_form` is not total on well-formed structures. Its [`max_branch=40320` guard](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/uniqueness.py:237) raises for legitimate inputs. Reproduced with nine identically coloured actors connected in a directed cycle: canonicalization requires `9! = 362880` orders and raises `ValueError`. Consequently `alpha_canonical` is not a general abstraction on all records.

- Resolved: empty-actor images return all-false membership before reductions, coalition members are validated as known string actor names, and hyperarcs are checked for nonempty in-domain tails and out-of-tail heads. The corresponding tests cover these cases.

- Resolved on the supplied fixtures: renamed duplicates exercise at least three same-P pairs, both canonical abstractions factor bijectively, the name-dependent negative control fails bijectivity, and witness tests assert equal actor sets and role maps.

- Confirmed sound: the transposition shortcut checks star transpositions while fixing every other actor. Equality of the complete encoding makes each checked transposition an automorphism; those transpositions generate every permutation of the colour class.

- Verification: both scoped test modules pass, 178 tests total, but they do not cover the two canonicalization counterexamples above.

VERDICT: NEEDS_FIX
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
44,933
- [P1] `canonical_form` is not a complete invariant of `p_equal`. [`find_bijection`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py:396) accepts contestability/weight differences up to `1e-9`, while [`canonical_form`](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/uniqueness.py:191) compares 12-decimal encodings exactly. Reproduced: a `5e-10` contestability change gives `p_equal(F, G) == True` but unequal canonical forms. Use one exact normalization consistently; tolerance equality is non-transitive and cannot support a complete invariant.

- [P1] `canonical_form` is not total on well-formed structures. Its [`max_branch=40320` guard](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/uniqueness.py:237) raises for legitimate inputs. Reproduced with nine identically coloured actors connected in a directed cycle: canonicalization requires `9! = 362880` orders and raises `ValueError`. Consequently `alpha_canonical` is not a general abstraction on all records.

- Resolved: empty-actor images return all-false membership before reductions, coalition members are validated as known string actor names, and hyperarcs are checked for nonempty in-domain tails and out-of-tail heads. The corresponding tests cover these cases.

- Resolved on the supplied fixtures: renamed duplicates exercise at least three same-P pairs, both canonical abstractions factor bijectively, the name-dependent negative control fails bijectivity, and witness tests assert equal actor sets and role maps.

- Confirmed sound: the transposition shortcut checks star transpositions while fixing every other actor. Equality of the complete encoding makes each checked transposition an automorphism; those transpositions generate every permutation of the colour class.

- Verification: both scoped test modules pass, 178 tests total, but they do not cover the two canonicalization counterexamples above.

VERDICT: NEEDS_FIX
exit 0
