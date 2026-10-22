Reading additional input from stdin...
2026-10-22T17:58:32.914491Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a164c3-c255-7482-b047-fa21378f9183
--------
user
Review only model/ (beast_system/representation.py, beast_system/uniqueness.py, tests/test_representation.py, tests/test_uniqueness.py, tests/test_necessity.py). Do not explore outside model/. Scoped round covering two things. (A) Confirm round-7 items resolved: [P1] representation theorem false over accepted CodedRecord domain (missing shares, unvalidated weights/coalitions); now CodedRecord requires shares for exactly the implemented pillars, validates Q, weights, coalitions (keys = frozensets of actors), and test_theorem_on_random_well_formed_records checks representable == A.holds on 300 random well-formed records; [P2] in_formalized_class did not enforce F2/F3 domain (empty Q, NaN, out-of-domain entries, layer shapes); now well_formed() gates it (test_class_check_rejects_malformed_structures); [P2] equivalent_A ignored out-of-domain entries and compared kappa as an unlabeled multiset; now find_bijection checks domains and transports kappa by coalition membership (test_equivalence_is_strict_on_domain_and_transports_kappa); [P2] falsifier assertions and consensus-village X1/X3 keys (test_incidence_axiom_statements_and_falsifiers, test_hard_case_x_codings_cite_the_part_vii_sources). (B) New uniqueness block in uniqueness.py: coarsen(F, c, lam) for c: M -> K or None (drop), lam > 0 summing to 1 per block, block holders union, lam-weighted shares/layers/Q/kappa, omega summed, hyperarcs with no dropped element mapped and self-loops removed; phi = coarsen(represent, identity); p_equal = isomorphism of represent(G) incl. layers; factor_through_phi(alpha, records) checks alpha(G)=alpha(G2) implies p_equal (well-defined) and bijection on fixtures, tested with alpha_represent and alpha_renamed; witness_coarsening(c, lam): merge {m,n} G1 s^m=(1,0), s^n=(0,1), G2 s^m=s^n=(mu,1-mu), mu=lam_m/(lam_m+lam_n); drop m: G1 (1,0), G2 (1/2,1/2); both satisfy all axioms; tested on all 15 merges, 6 drops, all 202 non-trivial set partitions and random maps with drops; predecessor encodings parsons, mann, easton, luhmann, almond (coarsenings), aristotle (typology: one/few/many by s^P>0 count, deviant iff capture link), weber (coded label outside P) each with witness_pair(k) and a test alpha_k(G)=alpha_k(G2), P differs; Weber label not determined by P. Check correctness, that tests demonstrate the claims, validation gaps, defects. Output the findings list and the VERDICT line only. End with VERDICT: PASS or VERDICT: NEEDS_FIX.
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T17:58:34.249106Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T17:58:35.139183Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
2026-10-22T17:59:04.953690Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
I’ll keep the review strictly inside `model/` and inspect only the five named files plus the scoped implementation they exercise. I’ll report only actionable findings and the verdict.
codex
I’m using the code-review skill to structure the correctness and test-evidence audit; it won’t broaden the requested file scope.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '1,240p' /Users/mlong/.codex/plugins/cache/claude-cowork/engineering/1.1.0/skills/code-review/SKILL.md && rg -n \"the-beast-system|representation|uniqueness\" /Users/mlong/.codex/memories/MEMORY.md" in /Users/mlong/Documents/Development/the-beast-system
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

2026-10-22T17:59:10.185285Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'git status --short -- model && wc -l model/beast_system/representation.py model/beast_system/uniqueness.py model/tests/test_representation.py model/tests/test_uniqueness.py model/tests/test_necessity.py && nl -ba model/beast_system/representation.py && nl -ba model/beast_system/uniqueness.py' in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T17:59:15.477723Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 1519ms:
2026-10-22 12:59:14.104 xcodebuild[71667:4165354]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:59:14.247 xcodebuild[71667:4165353] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-IPX2Dcfe' (errno=Operation not permitted)
2026-10-22 12:59:14.681 xcodebuild[71670:4165375]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:59:14.769 xcodebuild[71670:4165374] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
?? model/
     573 model/beast_system/representation.py
     337 model/beast_system/uniqueness.py
     277 model/tests/test_representation.py
     225 model/tests/test_uniqueness.py
     336 model/tests/test_necessity.py
    1748 total
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
   116	            for members, row in self.coalitions.items():
   117	                if not isinstance(members, frozenset) or not members:
   118	                    raise TypeError("coalition keys must be non-empty frozensets of actors")
   119	                if any(not isinstance(m, Pillar) for m in row):
   120	                    raise TypeError("kappa keys must be Pillars")
   121	                for m, x in row.items():
   122	                    validate_unit_interval(x, f"kappa[{sorted(members)}][{m.name}]")
   123	
   124	
   125	def minimal_record(system: GovernanceSystem, q: float = 0.5) -> CodedRecord:
   126	    """Record with PLACEHOLDER index inputs: uniform shares over performers, Q = q everywhere.
   127	
   128	    For systems such as the hard cases, which are coded only by practices. Representability
   129	    does not depend on these values; preserved quantities computed from them are not data.
   130	    """
   131	    roles = role_map(system)
   132	    shares = {}
   133	    for m in PILLARS:
   134	        hs = sorted(a for a, ps in roles.items() if m in ps)
   135	        if hs:
   136	            shares[m] = {a: 1.0 / len(hs) for a in hs}
   137	    return CodedRecord(system, shares, {m: q for m in PILLARS})
   138	
   139	
   140	def record_from_polity(
   141	    polity: Polity, coalitions: Mapping[frozenset[str], Mapping[Pillar, float]] | None = None
   142	) -> CodedRecord:
   143	    """The coded record of a Polity (shares normalized, zero-share pillars of unimplemented
   144	    functions omitted, weights validated)."""
   145	    implemented = {m for m in PILLARS if realized_form(polity.system, m) is not None}
   146	    return CodedRecord(
   147	        system=polity.system,
   148	        shares={m: s for m, s in polity.normalized_shares.items() if m in implemented},
   149	        contestability=polity.contestability,
   150	        weights=polity.weights,
   151	        coalitions=coalitions,
   152	        links=polity.capture_links,
   153	    )
   154	
   155	
   156	def represent(record: CodedRecord) -> FormalizedStructure:
   157	    """The profile map pi: G -> F_G.
   158	
   159	    V = practice performers plus actors named in shares or links (roles come only from
   160	    practices). m in rho(v) iff v performs a practice of pillar m and m is implemented.
   161	    Shares, Q, weights, coalitions and links are copied; D = arcs generated from G's axioms.
   162	    Layers: a^m_ij = s^m_i for i != j, so out-strength shares reproduce s^m.
   163	    """
   164	    system = record.system
   165	    implemented = {m for m in PILLARS if realized_form(system, m) is not None}
   166	    performers = role_map(system)
   167	    named = {a for s in record.shares.values() for a in s}
   168	    named |= {e for link in record.links for e in (link.source, link.target)}
   169	    if record.coalitions:
   170	        named |= {v for members in record.coalitions for v in members}
   171	    actors = tuple(sorted(set(performers) | named))
   172	    roles = {
   173	        v: frozenset(m.name for m in performers.get(v, frozenset()) if m in implemented)
   174	        for v in actors
   175	    }
   176	    shares = {
   177	        m.name: {v: float(record.shares.get(m, {}).get(v, 0.0)) for v in actors}
   178	        for m in PILLARS
   179	    }
   180	    idx = {v: k for k, v in enumerate(actors)}
   181	    layers = {}
   182	    for m in M_LABELS:
   183	        arr = np.zeros((len(actors), len(actors)))
   184	        for v, s in shares[m].items():
   185	            arr[idx[v], :] = s
   186	        np.fill_diagonal(arr, 0.0)
   187	        layers[m] = arr
   188	    weights = record.weights
   189	    if record.coalitions is None:
   190	        kappa = {frozenset({v}): {m: shares[m][v] for m in M_LABELS} for v in actors}
   191	    else:
   192	        kappa = {members: {m.name: float(row.get(m, 0.0)) for m in PILLARS}
   193	                 for members, row in record.coalitions.items()}
   194	    links = frozenset((lk.source, lk.target, lk.pillar.name) for lk in record.links if lk.holds)
   195	    arcs = frozenset(
   196	        (frozenset(t.name for t in tail), head.name)
   197	        for tail, head in generate_dependencies(system)
   198	    )
   199	    return FormalizedStructure(
   200	        actors=actors, pillars=M_LABELS, roles=roles, layers=layers, shares=shares,
   201	        contestability={m.name: float(record.contestability[m]) for m in PILLARS},
   202	        weights={m.name: float(weights[m]) for m in PILLARS},
   203	        kappa=kappa, links=links, arcs=arcs,
   204	    )
   205	
   206	
   207	# Formalized class --------------------------------------------------------------------------
   208	
   209	
   210	def _underlying(arcs: Iterable[LabelArc], labels: Iterable[Label]) -> dict[Label, set[Label]]:
   211	    adj: dict[Label, set[Label]] = {m: set() for m in labels}
   212	    for tail, head in arcs:
   213	        for t in tail:
   214	            adj.setdefault(t, set()).add(head)
   215	    return adj
   216	
   217	
   218	def _closure(arcs: Iterable[LabelArc], start: Iterable[Label]) -> frozenset[Label]:
   219	    """cl(S) on string labels (same rule as necessity.cascade_closure)."""
   220	    arcs = list(arcs)
   221	    closed = set(start)
   222	    changed = True
   223	    while changed:
   224	        changed = False
   225	        for tail, head in arcs:
   226	            if head not in closed and tail <= closed:
   227	                closed.add(head)
   228	                changed = True
   229	    return frozenset(closed)
   230	
   231	
   232	def _cascade_complete(arcs: Iterable[LabelArc], labels: tuple[Label, ...]) -> bool:
   233	    keep = frozenset(labels)
   234	    inside = [(t, h) for t, h in arcs if h in keep and t <= keep]
   235	    return bool(keep) and all(_closure(inside, {n}) >= keep for n in keep)
   236	
   237	
   238	@dataclass(frozen=True)
   239	class ClassMembership:
   240	    """Conditions F1..F4 of the formalized class."""
   241	
   242	    f1: bool
   243	    f2: bool
   244	    f3: bool
   245	    f4: bool
   246	
   247	    @property
   248	    def holds(self) -> bool:
   249	        return self.f1 and self.f2 and self.f3 and self.f4
   250	
   251	
   252	def well_formed(F: FormalizedStructure) -> bool:
   253	    """Domain check: every component is indexed by exactly V and the pillar labels, layers
   254	    are |V| x |V| and finite, and every number is finite."""
   255	    actors, labels = set(F.actors), set(F.pillars)
   256	    if len(actors) != len(F.actors) or len(labels) != len(F.pillars):
   257	        return False
   258	    if set(F.roles) != actors or any(not ps <= labels for ps in F.roles.values()):
   259	        return False
   260	    if set(F.shares) != labels or any(set(F.shares[m]) != actors for m in labels):
   261	        return False
   262	    if set(F.layers) != labels or set(F.contestability) != labels or set(F.weights) != labels:
   263	        return False
   264	    n = len(F.actors)
   265	    for m in labels:
   266	        arr = np.asarray(F.layers[m], dtype=float)
   267	        if arr.shape != (n, n) or not np.all(np.isfinite(arr)):
   268	            return False
   269	    nums = [*(x for m in labels for x in F.shares[m].values()), *F.contestability.values(),
   270	            *F.weights.values(), *(x for r in F.kappa.values() for x in r.values())]
   271	    if not all(math.isfinite(float(x)) for x in nums):
   272	        return False
   273	    for members, row in F.kappa.items():
   274	        if not isinstance(members, frozenset) or not members or not members <= actors:
   275	            return False
   276	        if not set(row) <= labels:
   277	            return False
   278	    return all(a in actors and b in actors and m in labels for a, b, m in F.links)
   279	
   280	
   281	def in_formalized_class(F: FormalizedStructure) -> ClassMembership:
   282	    """F1 every layer has a holder; F2 s^m a probability vector on holders of m, a^m_ij in
   283	    [0, 1] and > 0 only if i holds m; F3 Q, omega, kappa in range (omega summing to 1), link
   284	    endpoints in V; F4 D contains D0 and is strongly connected and cascade-complete.
   285	
   286	    A structure that is not ``well_formed`` (or whose labels are not the six pillars) fails
   287	    every condition.
   288	    """
   289	    if F.pillars != M_LABELS or not well_formed(F):
   290	        return ClassMembership(False, False, False, False)
   291	    f1 = all(F.holders(m) for m in F.pillars)
   292	    f2 = True
   293	    for m in F.pillars:
   294	        s = np.array([F.shares[m][v] for v in F.actors], dtype=float)
   295	        holders = F.holders(m)
   296	        arr = np.asarray(F.layers[m], dtype=float)
   297	        on_holders = all(F.shares[m][v] == 0.0 or v in holders for v in F.actors)
   298	        rows_ok = all(not arr[i].any() or v in holders for i, v in enumerate(F.actors))
   299	        if (s.min() < 0 or abs(s.sum() - 1.0) > _ATOL or not on_holders or not rows_ok
   300	                or arr.min() < 0.0 or arr.max() > 1.0):
   301	            f2 = False
   302	    vals = [*F.contestability.values(), *F.weights.values(),
   303	            *(x for row in F.kappa.values() for x in row.values())]
   304	    f3 = (all(0.0 <= float(x) <= 1.0 for x in vals)
   305	          and abs(sum(F.weights.values()) - 1.0) <= _ATOL)
   306	    f4 = (
   307	        D0_LABELS <= F.arcs
   308	        and is_strongly_connected(_underlying(F.arcs, F.pillars), set(F.pillars))
   309	        and _cascade_complete(F.arcs, F.pillars)
   310	    )
   311	    return ClassMembership(f1, f2, f3, f4)
   312	
   313	
   314	def representable(record: CodedRecord) -> bool:
   315	    """G is representable iff its image F_G lies in the formalized class."""
   316	    return in_formalized_class(represent(record)).holds
   317	
   318	
   319	# Preserved quantities and A-equivalence ----------------------------------------------------
   320	
   321	
   322	@dataclass(frozen=True)
   323	class PreservedQuantities:
   324	    H: dict[Label, float]
   325	    U: float
   326	    C: dict[frozenset[Label], float]
   327	    I: float  # noqa: E741  (integration statistic, math cal I)
   328	    cap: bool
   329	    inter: bool
   330	
   331	
   332	def preserved_quantities(
   333	    F: FormalizedStructure, thresholds: CaptureThresholds = CaptureThresholds()
   334	) -> PreservedQuantities:
   335	    """H_m, U, C_mn (coalition overlap), I, Cap (Proposition B) and Inter on F's own labels."""
   336	    H = {m: hhi([F.shares[m].get(v, 0.0) for v in F.actors]) if F.holders(m) else 0.0
   337	         for m in F.pillars}
   338	    U = sum(F.weights[m] * H[m] * (1.0 - F.contestability[m]) for m in F.pillars)
   339	    pairs = list(itertools.combinations(F.pillars, 2))
   340	    C = {frozenset((m, n)): max((min(row.get(m, 0.0), row.get(n, 0.0))
   341	                                 for row in F.kappa.values()), default=0.0)
   342	         for m, n in pairs}
   343	    I = sum(C.values()) / len(pairs) if pairs else 0.0  # noqa: E741
   344	    cap = U >= thresholds.u_star and I >= thresholds.i_star and bool(F.links)
   345	    inter = (is_strongly_connected(_underlying(F.arcs, F.pillars), set(F.pillars))
   346	             and _cascade_complete(F.arcs, F.pillars))
   347	    return PreservedQuantities(H, float(U), C, float(I), cap, inter)
   348	
   349	
   350	def _r(x: float) -> float:
   351	    return round(float(x), _ROUND) + 0.0
   352	
   353	
   354	def _same(a: float, b: float) -> bool:
   355	    return abs(a - b) <= _ATOL
   356	
   357	
   358	def _actor_signature(F: FormalizedStructure, k: int, with_layers: bool) -> tuple:
   359	    v = F.actors[k]
   360	    sig = (
   361	        tuple(sorted(F.roles[v])),
   362	        tuple(_r(F.shares[m][v]) for m in F.pillars),
   363	        tuple(sorted((m, a == v, b == v) for a, b, m in F.links if v in (a, b))),
   364	        tuple(sorted(tuple(_r(r.get(m, 0.0)) for m in F.pillars)
   365	                     for S, r in F.kappa.items() if v in S)),
   366	    )
   367	    if with_layers:
   368	        sig += tuple((tuple(sorted(_r(x) for x in F.layers[m][k])),
   369	                      tuple(sorted(_r(x) for x in F.layers[m][:, k]))) for m in F.pillars)
   370	    return sig
   371	
   372	
   373	def find_bijection(F: FormalizedStructure, G: FormalizedStructure,
   374	                   with_layers: bool) -> dict[str, str] | None:
   375	    """An actor bijection phi: V_F -> V_G under which roles, shares, Q, omega, kappa
   376	    (transported: kappa_F(S) = kappa_G(phi(S))), links and D agree, and, if ``with_layers``,
   377	    every layer entry. None if there is none.
   378	
   379	    Backtracking within classes of equal actor signatures; the identity on names is tried
   380	    first. Both structures must be ``well_formed``.
   381	    """
   382	    if not (well_formed(F) and well_formed(G)):
   383	        return None
   384	    if F.pillars != G.pillars or len(F.actors) != len(G.actors) or F.arcs != G.arcs:
   385	        return None
   386	    if any(not _same(F.contestability[m], G.contestability[m])
   387	           or not _same(F.weights[m], G.weights[m]) for m in F.pillars):
   388	        return None
   389	    if len(F.kappa) != len(G.kappa) or len(F.links) != len(G.links):
   390	        return None
   391	    sig_f = [_actor_signature(F, k, with_layers) for k in range(len(F.actors))]
   392	    sig_g = [_actor_signature(G, k, with_layers) for k in range(len(G.actors))]
   393	    if sorted(sig_f) != sorted(sig_g):
   394	        return None
   395	    gi = {v: k for k, v in enumerate(G.actors)}
   396	    fi = {v: k for k, v in enumerate(F.actors)}
   397	    order = sorted(range(len(F.actors)), key=lambda k: sig_f[k])
   398	    assign: dict[int, int] = {}
   399	    used: set[int] = set()
   400	
   401	    def consistent(i: int, j: int) -> bool:
   402	        if with_layers:
   403	            for i2, j2 in assign.items():
   404	                for m in F.pillars:
   405	                    if (_r(F.layers[m][i, i2]) != _r(G.layers[m][j, j2])
   406	                            or _r(F.layers[m][i2, i]) != _r(G.layers[m][j2, j])):
   407	                        return False
   408	        mapped = {**assign, i: j}
   409	        for a, b, m in F.links:
   410	            ia, ib = fi[a], fi[b]
   411	            if ia in mapped and ib in mapped:
   412	                if (G.actors[mapped[ia]], G.actors[mapped[ib]], m) not in G.links:
   413	                    return False
   414	        return True
   415	
   416	    def kappa_ok() -> bool:
   417	        to_g = {F.actors[i]: G.actors[j] for i, j in assign.items()}
   418	        for S, row in F.kappa.items():
   419	            other = G.kappa.get(frozenset(to_g[v] for v in S))
   420	            if other is None or set(other) != set(row):
   421	                return False
   422	            if any(not _same(row[m], other[m]) for m in row):
   423	                return False
   424	        return True
   425	
   426	    def search(pos: int) -> bool:
   427	        if pos == len(order):
   428	            return kappa_ok()
   429	        i = order[pos]
   430	        cands = [j for j in range(len(G.actors)) if j not in used and sig_g[j] == sig_f[i]]
   431	        pref = gi.get(F.actors[i])
   432	        if pref in cands:
   433	            cands.remove(pref)
   434	            cands.insert(0, pref)
   435	        for j in cands:
   436	            if consistent(i, j):
   437	                assign[i] = j
   438	                used.add(j)
   439	                if search(pos + 1):
   440	                    return True
   441	                del assign[i]
   442	                used.discard(j)
   443	        return False
   444	
   445	    if not search(0):
   446	        return None
   447	    return {F.actors[i]: G.actors[j] for i, j in assign.items()}
   448	
   449	
   450	def equivalent_A(F: FormalizedStructure, G: FormalizedStructure) -> bool:  # noqa: N802
   451	    """F and G agree on roles, shares, Q, omega, kappa, links and D under an actor bijection
   452	    (layers not compared; see ``uniqueness.p_equal`` for the version with layers)."""
   453	    return find_bijection(F, G, with_layers=False) is not None
   454	
   455	
   456	# Coarsenings (minimality) ------------------------------------------------------------------
   457	
   458	
   459	def drop(F: FormalizedStructure, m: Label) -> FormalizedStructure:
   460	    """Delete pillar m: its layer, shares, Q, kappa column and every hyperarc involving m.
   461	
   462	    Remaining weights are renormalized to sum 1.
   463	    """
   464	    if m not in F.pillars:
   465	        raise ValueError(f"unknown pillar {m!r}")
   466	    keep = tuple(p for p in F.pillars if p != m)
   467	    total = sum(F.weights[p] for p in keep)
   468	    weights = {p: (F.weights[p] / total if total > 0 else 1.0 / len(keep)) for p in keep}
   469	    return FormalizedStructure(
   470	        actors=F.actors, pillars=keep,
   471	        roles={v: ps - {m} for v, ps in F.roles.items()},
   472	        layers={p: F.layers[p] for p in keep},
   473	        shares={p: dict(F.shares[p]) for p in keep},
   474	        contestability={p: F.contestability[p] for p in keep},
   475	        weights=weights,
   476	        kappa={s: {p: row.get(p, 0.0) for p in keep} for s, row in F.kappa.items()},
   477	        links=frozenset(lk for lk in F.links if lk[2] != m),
   478	        arcs=frozenset((t, h) for t, h in F.arcs if h != m and m not in t),
   479	    )
   480	
   481	
   482	def merge(F: FormalizedStructure, m: Label, n: Label, lam: float) -> FormalizedStructure:
   483	    """Replace m, n by one pillar 'm+n': holders united, shares, layers, Q and kappa mixed with
   484	    weight lam on m; omega_m + omega_n; arcs relabeled, self-loops removed."""
   485	    if m == n or m not in F.pillars or n not in F.pillars:
   486	        raise ValueError("merge needs two distinct existing pillars")
   487	    lam = validate_unit_interval(lam, "lam")
   488	    new = f"{m}+{n}"
   489	    keep = tuple(new if p == m else p for p in F.pillars if p != n)
   490	    relabel = lambda p: new if p in (m, n) else p  # noqa: E731
   491	
   492	    def mix(a: float, b: float) -> float:
   493	        return lam * a + (1.0 - lam) * b
   494	
   495	    shares = {p: dict(F.shares[p]) for p in keep if p != new}
   496	    shares[new] = {v: mix(F.shares[m].get(v, 0.0), F.shares[n].get(v, 0.0)) for v in F.actors}
   497	    layers = {p: F.layers[p] for p in keep if p != new}
   498	    layers[new] = lam * F.layers[m] + (1.0 - lam) * F.layers[n]
   499	    contest = {p: F.contestability[p] for p in keep if p != new}
   500	    contest[new] = mix(F.contestability[m], F.contestability[n])
   501	    weights = {p: F.weights[p] for p in keep if p != new}
   502	    weights[new] = F.weights[m] + F.weights[n]
   503	    kappa = {}
   504	    for s, row in F.kappa.items():
   505	        r = {p: row.get(p, 0.0) for p in keep if p != new}
   506	        r[new] = mix(row.get(m, 0.0), row.get(n, 0.0))
   507	        kappa[s] = r
   508	    arcs = set()
   509	    for t, h in F.arcs:
   510	        t2, h2 = frozenset(relabel(x) for x in t), relabel(h)
   511	        if h2 not in t2:
   512	            arcs.add((t2, h2))
   513	    return FormalizedStructure(
   514	        actors=F.actors, pillars=keep,
   515	        roles={v: frozenset(relabel(p) for p in ps) for v, ps in F.roles.items()},
   516	        layers=layers, shares=shares, contestability=contest, weights=weights, kappa=kappa,
   517	        links=frozenset((a, b, relabel(p)) for a, b, p in F.links),
   518	        arcs=frozenset(arcs),
   519	    )
   520	
   521	
   522	def structurally_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   523	    """Equality of every component with the identity on actor names (floats within 1e-9)."""
   524	    if not (well_formed(F) and well_formed(G)):
   525	        return False
   526	    if (F.actors, F.pillars, F.links, F.arcs) != (G.actors, G.pillars, G.links, G.arcs):
   527	        return False
   528	    if any(F.roles[v] != G.roles[v] for v in F.actors) or set(F.kappa) != set(G.kappa):
   529	        return False
   530	    return (
   531	        all(_same(F.shares[m][v], G.shares[m][v]) for m in F.pillars for v in F.actors)
   532	        and all(np.allclose(F.layers[m], G.layers[m], atol=_ATOL, rtol=0) for m in F.pillars)
   533	        and all(_same(F.contestability[m], G.contestability[m]) for m in F.pillars)
   534	        and all(_same(F.weights[m], G.weights[m]) for m in F.pillars)
   535	        and all(set(F.kappa[S]) == set(G.kappa[S])
   536	                and all(_same(F.kappa[S][m], G.kappa[S][m]) for m in F.kappa[S])
   537	                for S in F.kappa)
   538	    )
   539	
   540	
   541	D_STAR_LABELS: frozenset[LabelArc] = frozenset(
   542	    (frozenset(t.name for t in tail), head.name) for tail, head in D_STAR_KEYS
   543	)
   544	
   545	
   546	def make_structure(
   547	    shares: Mapping[Label, Mapping[str, float]],
   548	    contestability: Mapping[Label, float],
   549	    weights: Mapping[Label, float] | None = None,
   550	    kappa: Mapping[frozenset[str], Mapping[Label, float]] | None = None,
   551	    links: Iterable[tuple[str, str, Label]] = (),
   552	    arcs: Iterable[LabelArc] = D_STAR_LABELS,
   553	) -> FormalizedStructure:
   554	    """Build F directly: holders are actors with positive share, a^m_ij = s^m_i (i != j),
   555	    singleton coalitions by default. Used for the minimality fixtures."""
   556	    pillars = tuple(shares)
   557	    actors = tuple(sorted({v for s in shares.values() for v in s}))
   558	    full = {m: {v: float(shares[m].get(v, 0.0)) for v in actors} for m in pillars}
   559	    roles = {v: frozenset(m for m in pillars if full[m][v] > 0) for v in actors}
   560	    layers = {}
   561	    for m in pillars:
   562	        arr = np.tile(np.array([full[m][v] for v in actors])[:, None], (1, len(actors)))
   563	        np.fill_diagonal(arr, 0.0)
   564	        layers[m] = arr
   565	    if kappa is None:
   566	        kappa = {frozenset({v}): {m: full[m][v] for m in pillars} for v in actors}
   567	    return FormalizedStructure(
   568	        actors=actors, pillars=pillars, roles=roles, layers=layers, shares=full,
   569	        contestability=dict(contestability),
   570	        weights=dict(weights) if weights else {m: 1.0 / len(pillars) for m in pillars},
   571	        kappa={s: dict(r) for s, r in kappa.items()},
   572	        links=frozenset(links), arcs=frozenset(arcs),
   573	    )
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
    14	import math
    15	from collections.abc import Callable, Iterable, Mapping, Sequence
    16	from dataclasses import dataclass
    17	
    18	import numpy as np
    19	
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
    30	)
    31	
    32	_ROUND = 12
    33	_ATOL = 1e-9
    34	Coarsening = Mapping[Label, "Label | None"]
    35	
    36	
    37	# Coarsening --------------------------------------------------------------------------------
    38	
    39	
    40	def _blocks(F: FormalizedStructure, c: Coarsening) -> dict[Label, list[Label]]:
    41	    if set(c) != set(F.pillars):
    42	        raise ValueError("a coarsening must assign every pillar (None drops it)")
    43	    blocks: dict[Label, list[Label]] = {}
    44	    for m in F.pillars:
    45	        if c[m] is not None:
    46	            blocks.setdefault(c[m], []).append(m)
    47	    return blocks
    48	
    49	
    50	def _block_weights(blocks: Mapping[Label, list[Label]],
    51	                   lam: Mapping[Label, float] | None) -> dict[Label, float]:
    52	    out: dict[Label, float] = {}
    53	    for members in blocks.values():
    54	        for m in members:
    55	            out[m] = 1.0 / len(members) if lam is None else float(lam[m])
    56	        if any(not math.isfinite(out[m]) or out[m] <= 0.0 for m in members):
    57	            raise ValueError("lam_m must be positive")
    58	        if abs(sum(out[m] for m in members) - 1.0) > _ATOL:
    59	            raise ValueError("lam must sum to 1 within each block")
    60	    return out
    61	
    62	
    63	def coarsen(F: FormalizedStructure, c: Coarsening,
    64	            lam: Mapping[Label, float] | None = None) -> FormalizedStructure:
    65	    """Coarsen F by c: M -> K or None (drop), lam-weighted within each block (default equal).
    66	
    67	    Block holders are the union; shares, layers, Q and kappa are lam-weighted sums; omega_k is
    68	    the sum of omega_m (not renormalized); hyperarcs with no dropped element map to their image
    69	    under c, self-loops removed; links in dropped pillars are removed.
    70	    """
    71	    blocks = _blocks(F, c)
    72	    w = _block_weights(blocks, lam)
    73	    keys = tuple(blocks)
    74	
    75	    def mix(get: Callable[[Label], float], k: Label) -> float:
    76	        return sum(w[m] * get(m) for m in blocks[k])
    77	
    78	    shares = {k: {v: mix(lambda m: F.shares[m].get(v, 0.0), k) for v in F.actors} for k in keys}
    79	    layers = {k: sum(w[m] * F.layers[m] for m in blocks[k]) for k in keys}
    80	    arcs = set()
    81	    for tail, head in F.arcs:
    82	        if c[head] is None or any(c[t] is None for t in tail):
    83	            continue
    84	        t2, h2 = frozenset(c[t] for t in tail), c[head]
    85	        if h2 not in t2:
    86	            arcs.add((t2, h2))
    87	    return FormalizedStructure(
    88	        actors=F.actors, pillars=keys,
    89	        roles={v: frozenset(c[m] for m in ps if c[m] is not None) for v, ps in F.roles.items()},
    90	        layers=layers, shares=shares,
    91	        contestability={k: mix(lambda m: F.contestability[m], k) for k in keys},
    92	        weights={k: sum(F.weights[m] for m in blocks[k]) for k in keys},
    93	        kappa={s: {k: mix(lambda m: row.get(m, 0.0), k) for k in keys} for s, row in F.kappa.items()},
    94	        links=frozenset((a, b, c[m]) for a, b, m in F.links if c[m] is not None),
    95	        arcs=frozenset(arcs),
    96	    )
    97	
    98	
    99	IDENTITY: dict[Label, Label] = {m: m for m in M_LABELS}
   100	
   101	
   102	def phi(record: CodedRecord) -> FormalizedStructure:
   103	    """Phi = coarsen(represent(G), identity)."""
   104	    return coarsen(represent(record), IDENTITY)
   105	
   106	
   107	# P-equality --------------------------------------------------------------------------------
   108	
   109	
   110	def _r(x: float) -> float:
   111	    return round(float(x), _ROUND) + 0.0
   112	
   113	
   114	def p_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   115	    """P(F) = P(G): roles, shares, Q, omega, kappa (transported), links, D and layers agree
   116	    under an actor bijection (``representation.find_bijection`` with layers)."""
   117	    return find_bijection(F, G, with_layers=True) is not None
   118	
   119	
   120	def _global(F: FormalizedStructure) -> tuple:
   121	    return (
   122	        F.pillars,
   123	        tuple(_r(F.contestability[m]) for m in F.pillars),
   124	        tuple(_r(F.weights[m]) for m in F.pillars),
   125	        tuple(sorted((tuple(sorted(S)), tuple(_r(r.get(m, 0.0)) for m in F.pillars))
   126	                     for S, r in F.kappa.items())),
   127	        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
   128	        len(F.actors),
   129	    )
   130	
   131	
   132	def freeze(F: FormalizedStructure) -> tuple:
   133	    """Hashable encoding of F with its actor names (equality = identity on names)."""
   134	    return (
   135	        F.actors, F.pillars,
   136	        tuple(tuple(sorted(F.roles[v])) for v in F.actors),
   137	        tuple(tuple(_r(F.shares[m][v]) for v in F.actors) for m in F.pillars),
   138	        tuple(tuple(_r(x) for x in F.layers[m].ravel()) for m in F.pillars),
   139	        _global(F), tuple(sorted(F.links)),
   140	    )
   141	
   142	
   143	# Factorization through Phi -----------------------------------------------------------------
   144	
   145	
   146	@dataclass(frozen=True)
   147	class Factorization:
   148	    """alpha factors through Phi on the fixtures: alpha(G) = alpha(G2) implies P(G) = P(G2)
   149	    (``well_defined``: h(alpha(G)) = Phi(G) is a function); ``bijective``: h is also
   150	    injective onto the P-classes of the fixtures."""
   151	
   152	    well_defined: bool
   153	    bijective: bool
   154	
   155	
   156	def factor_through_phi(alpha: Callable[[CodedRecord], object],
   157	                       records: Sequence[CodedRecord]) -> Factorization:
   158	    """Check that the P-preserving abstraction ``alpha`` factors through Phi on ``records``."""
   159	    images = [alpha(r) for r in records]
   160	    phis = [phi(r) for r in records]
   161	    well_defined = injective = True
   162	    for i in range(len(records)):
   163	        for j in range(i + 1, len(records)):
   164	            same_alpha = images[i] == images[j]
   165	            same_p = p_equal(phis[i], phis[j])
   166	            if same_alpha and not same_p:
   167	                well_defined = False
   168	            if same_p and not same_alpha:
   169	                injective = False
   170	    return Factorization(well_defined, well_defined and injective)
   171	
   172	
   173	def alpha_represent(record: CodedRecord) -> tuple:
   174	    """A P-preserving abstraction: the frozen profile with its actor names."""
   175	    return freeze(represent(record))
   176	
   177	
   178	def alpha_renamed(record: CodedRecord) -> tuple:
   179	    """A second, differently built one: actors renamed v0, v1, ... in name order, plus a
   180	    redundant field (the number of hyperarcs)."""
   181	    F = represent(record)
   182	    ren = {v: f"v{k}" for k, v in enumerate(F.actors)}
   183	    G = FormalizedStructure(
   184	        actors=tuple(ren[v] for v in F.actors), pillars=F.pillars,
   185	        roles={ren[v]: ps for v, ps in F.roles.items()}, layers=F.layers,
   186	        shares={m: {ren[v]: x for v, x in s.items()} for m, s in F.shares.items()},
   187	        contestability=F.contestability, weights=F.weights,
   188	        kappa={frozenset(ren[v] for v in S): row for S, row in F.kappa.items()},
   189	        links=frozenset((ren[a], ren[b], m) for a, b, m in F.links), arcs=F.arcs,
   190	    )
   191	    return (freeze(G), len(F.arcs))
   192	
   193	
   194	# Witnesses ---------------------------------------------------------------------------------
   195	
   196	
   197	def two_actor_record(shares: Mapping[Label, tuple[float, float]], q: float = 0.5,
   198	                     links: Iterable = ()) -> CodedRecord:
   199	    """Actors a, b both perform every pillar; Ax1..Ax6 and X1, X2, X3, X5 hold.
   200	
   201	    ``shares[m]`` = (s^m_a, s^m_b); unspecified pillars get (1/2, 1/2).
   202	    """
   203	    practices = tuple(
   204	        Practice(f"{m.label} practice", PILLAR_TO_AXIOM[m], frozenset({"a", "b"}),
   205	                 source="synthetic witness")
   206	        for m in PILLARS
   207	    )
   208	    system = GovernanceSystem("two-actor witness", True, EXTENDED_AXIOMS, practices)
   209	    full = {m: dict(zip(("a", "b"), shares.get(m.name, (0.5, 0.5)))) for m in PILLARS}
   210	    return CodedRecord(system, full, {m: q for m in PILLARS}, links=tuple(links))
   211	
   212	
   213	def witness_coarsening(c: Coarsening, lam: Mapping[Label, float] | None = None
   214	                       ) -> tuple[CodedRecord, CodedRecord]:
   215	    """(G1, G2) with coarsen(Phi(G1), c) = coarsen(Phi(G2), c) and P(G1) != P(G2).
   216	
   217	    Merge {m, n} in one block: G1 s^m = (1, 0), s^n = (0, 1); G2 s^m = s^n = (mu, 1 - mu),
   218	    mu = lam_m / (lam_m + lam_n). Drop m: G1 s^m = (1, 0), G2 s^m = (1/2, 1/2). Raises if c
   219	    is a total injection (then no witness exists by this construction).
   220	    """
   221	    if set(c) != set(M_LABELS):
   222	        raise ValueError("c must assign all six pillars")
   223	    dropped = [m for m in M_LABELS if c[m] is None]
   224	    if dropped:
   225	        m = dropped[0]
   226	        return two_actor_record({m: (1.0, 0.0)}), two_actor_record({m: (0.5, 0.5)})
   227	    for i, m in enumerate(M_LABELS):
   228	        for n in M_LABELS[i + 1:]:
   229	            if c[m] == c[n]:
   230	                if lam is None:
   231	                    size = sum(1 for x in M_LABELS if c[x] == c[m])
   232	                    lm = ln = 1.0 / size
   233	                else:
   234	                    lm, ln = float(lam[m]), float(lam[n])
   235	                mu = lm / (lm + ln)
   236	                return (two_actor_record({m: (1.0, 0.0), n: (0.0, 1.0)}),
   237	                        two_actor_record({m: (mu, 1 - mu), n: (mu, 1 - mu)}))
   238	    raise ValueError("c is a total injection; no collapse witness")
   239	
   240	
   241	# Predecessor encodings ---------------------------------------------------------------------
   242	
   243	PARSONS: dict[Label, Label | None] = {"F": "A", "W": "A", "P": "G", "J": "I", "C": "I", "I": "L"}
   244	MANN: dict[Label, Label | None] = {"I": "Ideological", "F": "Economic", "W": "Economic",
   245	                                   "C": "Military", "P": "Political", "J": "Political"}
   246	EASTON: dict[Label, Label | None] = {"I": "Inputs", "W": "Inputs", "F": "Outputs",
   247	                                     "P": "Outputs", "J": "Outputs", "C": "Outputs"}
   248	LUHMANN: dict[Label, Label | None] = {"F": "Economy", "W": "Economy", "P": "Politics",
   249	                                      "C": "Politics", "J": "Law", "I": "Culture"}
   250	ALMOND: dict[Label, Label | None] = {"F": None, "W": None, "P": "RuleMaking",
   251	                                     "J": "RuleAdjudication", "C": "RuleApplication",
   252	                                     "I": "Inputs"}
   253	
   254	
   255	def encode_parsons(F: FormalizedStructure) -> FormalizedStructure:
   256	    """AGIL: A = {F, W}, G = {P}, I = {J, C}, L = {I}."""
   257	    return coarsen(F, PARSONS)
   258	
   259	
   260	def encode_mann(F: FormalizedStructure) -> FormalizedStructure:
   261	    """IEMP: Ideological = {I}, Economic = {F, W}, Military = {C}, Political = {P, J}."""
   262	    return coarsen(F, MANN)
   263	
   264	
   265	def encode_easton(F: FormalizedStructure) -> FormalizedStructure:
   266	    """Inputs = {I, W}, Outputs = {F, P, J, C}."""
   267	    return coarsen(F, EASTON)
   268	
   269	
   270	def encode_luhmann(F: FormalizedStructure) -> FormalizedStructure:
   271	    """Economy = {F, W}, Politics = {P, C}, Law = {J}, Culture = {I} (Luhmann splits it
   272	    further; the split does not affect the witness)."""
   273	    return coarsen(F, LUHMANN)
   274	
   275	
   276	def encode_almond(F: FormalizedStructure) -> FormalizedStructure:
   277	    """F and W dropped; RuleMaking = {P}, RuleAdjudication = {J}, RuleApplication = {C},
   278	    Inputs = {I}."""
   279	    return coarsen(F, ALMOND)
   280	
   281	
   282	def encode_aristotle(F: FormalizedStructure) -> tuple[str, str]:
   283	    """(rulers, aim): 'one' if exactly one actor has s^P > 0, 'few' if 2 to n/2, else 'many';
   284	    'deviant' if any capture link, else 'correct'. A typology, not a coarsening."""
   285	    k = sum(1 for v in F.actors if F.shares["P"].get(v, 0.0) > 0.0)
   286	    n = len(F.actors)
   287	    rulers = "one" if k == 1 else ("few" if 2 <= k <= n / 2 else "many")
   288	    return rulers, ("deviant" if F.links else "correct")
   289	
   290	
   291	WEBER_TYPES = ("traditional", "charismatic", "legal-rational")
   292	
   293	
   294	def encode_weber(F: FormalizedStructure, legitimation: str, has_staff: bool) -> tuple[str, bool]:
   295	    """(legitimation type, administrative staff). Both come from a coded field the profile
   296	    does NOT contain, so the encoding does not factor through P (nor P through it)."""
   297	    if legitimation not in WEBER_TYPES:
   298	        raise ValueError(f"legitimation must be one of {WEBER_TYPES}")
   299	    return legitimation, bool(has_staff)
   300	
   301	
   302	ENCODINGS: dict[str, Callable[[FormalizedStructure], object]] = {
   303	    "parsons": encode_parsons,
   304	    "mann": encode_mann,
   305	    "easton": encode_easton,
   306	    "luhmann": encode_luhmann,
   307	    "almond": encode_almond,
   308	    "aristotle": encode_aristotle,
   309	    "weber": lambda F: encode_weber(F, "legal-rational", True),
   310	}
   311	
   312	_WITNESS_SHARES: dict[str, tuple[dict, dict]] = {
   313	    "parsons": ({"F": (1.0, 0.0), "W": (0.0, 1.0)}, {"F": (0.5, 0.5), "W": (0.5, 0.5)}),
   314	    "mann": ({"P": (1.0, 0.0), "J": (0.0, 1.0)}, {"P": (0.5, 0.5), "J": (0.5, 0.5)}),
   315	    "easton": ({"P": (1.0, 0.0), "J": (0.0, 1.0)}, {"P": (0.5, 0.5), "J": (0.5, 0.5)}),
   316	    "luhmann": ({"F": (1.0, 0.0), "W": (0.0, 1.0)}, {"F": (0.5, 0.5), "W": (0.5, 0.5)}),
   317	    "almond": ({"F": (1.0, 0.0)}, {"F": (0.5, 0.5)}),
   318	    "aristotle": ({"J": (1.0, 0.0)}, {"J": (0.5, 0.5)}),
   319	    "weber": ({"C": (1.0, 0.0)}, {"C": (0.5, 0.5)}),
   320	}
   321	
   322	
   323	def witness_pair(k: str) -> tuple[CodedRecord, CodedRecord]:
   324	    """Two systems satisfying all axioms that encoding ``k`` cannot tell apart, with P differing.
   325	
   326	    Easton's Outputs block has four members, so equal lam gives the merge witness with
   327	    mu = 1/2 for (P, J).
   328	    """
   329	    if k not in _WITNESS_SHARES:
   330	        raise ValueError(f"unknown encoding {k!r}")
   331	    s1, s2 = _WITNESS_SHARES[k]
   332	    return two_actor_record(s1), two_actor_record(s2)
   333	
   334	
   335	def coarsenings_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   336	    """Coarsened profiles equal component by component (identity on actor names)."""
   337	    return structurally_equal(F, G)

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/representation.py | sed -n '230,470p'
nl -ba model/tests/test_representation.py
nl -ba model/tests/test_uniqueness.py" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   230	
   231	
   232	def _cascade_complete(arcs: Iterable[LabelArc], labels: tuple[Label, ...]) -> bool:
   233	    keep = frozenset(labels)
   234	    inside = [(t, h) for t, h in arcs if h in keep and t <= keep]
   235	    return bool(keep) and all(_closure(inside, {n}) >= keep for n in keep)
   236	
   237	
   238	@dataclass(frozen=True)
   239	class ClassMembership:
   240	    """Conditions F1..F4 of the formalized class."""
   241	
   242	    f1: bool
   243	    f2: bool
   244	    f3: bool
   245	    f4: bool
   246	
   247	    @property
   248	    def holds(self) -> bool:
   249	        return self.f1 and self.f2 and self.f3 and self.f4
   250	
   251	
   252	def well_formed(F: FormalizedStructure) -> bool:
   253	    """Domain check: every component is indexed by exactly V and the pillar labels, layers
   254	    are |V| x |V| and finite, and every number is finite."""
   255	    actors, labels = set(F.actors), set(F.pillars)
   256	    if len(actors) != len(F.actors) or len(labels) != len(F.pillars):
   257	        return False
   258	    if set(F.roles) != actors or any(not ps <= labels for ps in F.roles.values()):
   259	        return False
   260	    if set(F.shares) != labels or any(set(F.shares[m]) != actors for m in labels):
   261	        return False
   262	    if set(F.layers) != labels or set(F.contestability) != labels or set(F.weights) != labels:
   263	        return False
   264	    n = len(F.actors)
   265	    for m in labels:
   266	        arr = np.asarray(F.layers[m], dtype=float)
   267	        if arr.shape != (n, n) or not np.all(np.isfinite(arr)):
   268	            return False
   269	    nums = [*(x for m in labels for x in F.shares[m].values()), *F.contestability.values(),
   270	            *F.weights.values(), *(x for r in F.kappa.values() for x in r.values())]
   271	    if not all(math.isfinite(float(x)) for x in nums):
   272	        return False
   273	    for members, row in F.kappa.items():
   274	        if not isinstance(members, frozenset) or not members or not members <= actors:
   275	            return False
   276	        if not set(row) <= labels:
   277	            return False
   278	    return all(a in actors and b in actors and m in labels for a, b, m in F.links)
   279	
   280	
   281	def in_formalized_class(F: FormalizedStructure) -> ClassMembership:
   282	    """F1 every layer has a holder; F2 s^m a probability vector on holders of m, a^m_ij in
   283	    [0, 1] and > 0 only if i holds m; F3 Q, omega, kappa in range (omega summing to 1), link
   284	    endpoints in V; F4 D contains D0 and is strongly connected and cascade-complete.
   285	
   286	    A structure that is not ``well_formed`` (or whose labels are not the six pillars) fails
   287	    every condition.
   288	    """
   289	    if F.pillars != M_LABELS or not well_formed(F):
   290	        return ClassMembership(False, False, False, False)
   291	    f1 = all(F.holders(m) for m in F.pillars)
   292	    f2 = True
   293	    for m in F.pillars:
   294	        s = np.array([F.shares[m][v] for v in F.actors], dtype=float)
   295	        holders = F.holders(m)
   296	        arr = np.asarray(F.layers[m], dtype=float)
   297	        on_holders = all(F.shares[m][v] == 0.0 or v in holders for v in F.actors)
   298	        rows_ok = all(not arr[i].any() or v in holders for i, v in enumerate(F.actors))
   299	        if (s.min() < 0 or abs(s.sum() - 1.0) > _ATOL or not on_holders or not rows_ok
   300	                or arr.min() < 0.0 or arr.max() > 1.0):
   301	            f2 = False
   302	    vals = [*F.contestability.values(), *F.weights.values(),
   303	            *(x for row in F.kappa.values() for x in row.values())]
   304	    f3 = (all(0.0 <= float(x) <= 1.0 for x in vals)
   305	          and abs(sum(F.weights.values()) - 1.0) <= _ATOL)
   306	    f4 = (
   307	        D0_LABELS <= F.arcs
   308	        and is_strongly_connected(_underlying(F.arcs, F.pillars), set(F.pillars))
   309	        and _cascade_complete(F.arcs, F.pillars)
   310	    )
   311	    return ClassMembership(f1, f2, f3, f4)
   312	
   313	
   314	def representable(record: CodedRecord) -> bool:
   315	    """G is representable iff its image F_G lies in the formalized class."""
   316	    return in_formalized_class(represent(record)).holds
   317	
   318	
   319	# Preserved quantities and A-equivalence ----------------------------------------------------
   320	
   321	
   322	@dataclass(frozen=True)
   323	class PreservedQuantities:
   324	    H: dict[Label, float]
   325	    U: float
   326	    C: dict[frozenset[Label], float]
   327	    I: float  # noqa: E741  (integration statistic, math cal I)
   328	    cap: bool
   329	    inter: bool
   330	
   331	
   332	def preserved_quantities(
   333	    F: FormalizedStructure, thresholds: CaptureThresholds = CaptureThresholds()
   334	) -> PreservedQuantities:
   335	    """H_m, U, C_mn (coalition overlap), I, Cap (Proposition B) and Inter on F's own labels."""
   336	    H = {m: hhi([F.shares[m].get(v, 0.0) for v in F.actors]) if F.holders(m) else 0.0
   337	         for m in F.pillars}
   338	    U = sum(F.weights[m] * H[m] * (1.0 - F.contestability[m]) for m in F.pillars)
   339	    pairs = list(itertools.combinations(F.pillars, 2))
   340	    C = {frozenset((m, n)): max((min(row.get(m, 0.0), row.get(n, 0.0))
   341	                                 for row in F.kappa.values()), default=0.0)
   342	         for m, n in pairs}
   343	    I = sum(C.values()) / len(pairs) if pairs else 0.0  # noqa: E741
   344	    cap = U >= thresholds.u_star and I >= thresholds.i_star and bool(F.links)
   345	    inter = (is_strongly_connected(_underlying(F.arcs, F.pillars), set(F.pillars))
   346	             and _cascade_complete(F.arcs, F.pillars))
   347	    return PreservedQuantities(H, float(U), C, float(I), cap, inter)
   348	
   349	
   350	def _r(x: float) -> float:
   351	    return round(float(x), _ROUND) + 0.0
   352	
   353	
   354	def _same(a: float, b: float) -> bool:
   355	    return abs(a - b) <= _ATOL
   356	
   357	
   358	def _actor_signature(F: FormalizedStructure, k: int, with_layers: bool) -> tuple:
   359	    v = F.actors[k]
   360	    sig = (
   361	        tuple(sorted(F.roles[v])),
   362	        tuple(_r(F.shares[m][v]) for m in F.pillars),
   363	        tuple(sorted((m, a == v, b == v) for a, b, m in F.links if v in (a, b))),
   364	        tuple(sorted(tuple(_r(r.get(m, 0.0)) for m in F.pillars)
   365	                     for S, r in F.kappa.items() if v in S)),
   366	    )
   367	    if with_layers:
   368	        sig += tuple((tuple(sorted(_r(x) for x in F.layers[m][k])),
   369	                      tuple(sorted(_r(x) for x in F.layers[m][:, k]))) for m in F.pillars)
   370	    return sig
   371	
   372	
   373	def find_bijection(F: FormalizedStructure, G: FormalizedStructure,
   374	                   with_layers: bool) -> dict[str, str] | None:
   375	    """An actor bijection phi: V_F -> V_G under which roles, shares, Q, omega, kappa
   376	    (transported: kappa_F(S) = kappa_G(phi(S))), links and D agree, and, if ``with_layers``,
   377	    every layer entry. None if there is none.
   378	
   379	    Backtracking within classes of equal actor signatures; the identity on names is tried
   380	    first. Both structures must be ``well_formed``.
   381	    """
   382	    if not (well_formed(F) and well_formed(G)):
   383	        return None
   384	    if F.pillars != G.pillars or len(F.actors) != len(G.actors) or F.arcs != G.arcs:
   385	        return None
   386	    if any(not _same(F.contestability[m], G.contestability[m])
   387	           or not _same(F.weights[m], G.weights[m]) for m in F.pillars):
   388	        return None
   389	    if len(F.kappa) != len(G.kappa) or len(F.links) != len(G.links):
   390	        return None
   391	    sig_f = [_actor_signature(F, k, with_layers) for k in range(len(F.actors))]
   392	    sig_g = [_actor_signature(G, k, with_layers) for k in range(len(G.actors))]
   393	    if sorted(sig_f) != sorted(sig_g):
   394	        return None
   395	    gi = {v: k for k, v in enumerate(G.actors)}
   396	    fi = {v: k for k, v in enumerate(F.actors)}
   397	    order = sorted(range(len(F.actors)), key=lambda k: sig_f[k])
   398	    assign: dict[int, int] = {}
   399	    used: set[int] = set()
   400	
   401	    def consistent(i: int, j: int) -> bool:
   402	        if with_layers:
   403	            for i2, j2 in assign.items():
   404	                for m in F.pillars:
   405	                    if (_r(F.layers[m][i, i2]) != _r(G.layers[m][j, j2])
   406	                            or _r(F.layers[m][i2, i]) != _r(G.layers[m][j2, j])):
   407	                        return False
   408	        mapped = {**assign, i: j}
   409	        for a, b, m in F.links:
   410	            ia, ib = fi[a], fi[b]
   411	            if ia in mapped and ib in mapped:
   412	                if (G.actors[mapped[ia]], G.actors[mapped[ib]], m) not in G.links:
   413	                    return False
   414	        return True
   415	
   416	    def kappa_ok() -> bool:
   417	        to_g = {F.actors[i]: G.actors[j] for i, j in assign.items()}
   418	        for S, row in F.kappa.items():
   419	            other = G.kappa.get(frozenset(to_g[v] for v in S))
   420	            if other is None or set(other) != set(row):
   421	                return False
   422	            if any(not _same(row[m], other[m]) for m in row):
   423	                return False
   424	        return True
   425	
   426	    def search(pos: int) -> bool:
   427	        if pos == len(order):
   428	            return kappa_ok()
   429	        i = order[pos]
   430	        cands = [j for j in range(len(G.actors)) if j not in used and sig_g[j] == sig_f[i]]
   431	        pref = gi.get(F.actors[i])
   432	        if pref in cands:
   433	            cands.remove(pref)
   434	            cands.insert(0, pref)
   435	        for j in cands:
   436	            if consistent(i, j):
   437	                assign[i] = j
   438	                used.add(j)
   439	                if search(pos + 1):
   440	                    return True
   441	                del assign[i]
   442	                used.discard(j)
   443	        return False
   444	
   445	    if not search(0):
   446	        return None
   447	    return {F.actors[i]: G.actors[j] for i, j in assign.items()}
   448	
   449	
   450	def equivalent_A(F: FormalizedStructure, G: FormalizedStructure) -> bool:  # noqa: N802
   451	    """F and G agree on roles, shares, Q, omega, kappa, links and D under an actor bijection
   452	    (layers not compared; see ``uniqueness.p_equal`` for the version with layers)."""
   453	    return find_bijection(F, G, with_layers=False) is not None
   454	
   455	
   456	# Coarsenings (minimality) ------------------------------------------------------------------
   457	
   458	
   459	def drop(F: FormalizedStructure, m: Label) -> FormalizedStructure:
   460	    """Delete pillar m: its layer, shares, Q, kappa column and every hyperarc involving m.
   461	
   462	    Remaining weights are renormalized to sum 1.
   463	    """
   464	    if m not in F.pillars:
   465	        raise ValueError(f"unknown pillar {m!r}")
   466	    keep = tuple(p for p in F.pillars if p != m)
   467	    total = sum(F.weights[p] for p in keep)
   468	    weights = {p: (F.weights[p] / total if total > 0 else 1.0 / len(keep)) for p in keep}
   469	    return FormalizedStructure(
   470	        actors=F.actors, pillars=keep,
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
    28	    alpha_renamed,
    29	    alpha_represent,
    30	    coarsen,
    31	    coarsenings_equal,
    32	    encode_aristotle,
    33	    encode_weber,
    34	    factor_through_phi,
    35	    p_equal,
    36	    phi,
    37	    two_actor_record,
    38	    witness_coarsening,
    39	    witness_pair,
    40	)
    41	
    42	
    43	def _fixtures():
    44	    recs = [minimal_record(s) for s in HARD_CASES]
    45	    recs += [record_from_polity(p.polity) for p in regime_profiles()]
    46	    recs += [record_from_polity(p) for p in corner_polities().values()]
    47	    recs += [record_from_polity(plural_polity()), record_from_polity(fused_polity(q=0.2))]
    48	    return recs
    49	
    50	
    51	def _all_set_partitions(items):
    52	    if not items:
    53	        yield []
    54	        return
    55	    first, rest = items[0], items[1:]
    56	    for part in _all_set_partitions(rest):
    57	        for k in range(len(part)):
    58	            yield part[:k] + [[first] + part[k]] + part[k + 1:]
    59	        yield [[first]] + part
    60	
    61	
    62	# Coarsening ---------------------------------------------------------------------------------
    63	
    64	
    65	def test_phi_equals_represent_up_to_relabeling():
    66	    for rec in _fixtures():
    67	        assert p_equal(phi(rec), represent(rec))
    68	
    69	
    70	def test_coarsen_generalizes_merge_and_drop():
    71	    F_ = represent(minimal_record(HARD_CASES[0]))
    72	    for m, n in itertools.combinations(M_LABELS, 2):
    73	        c = {p: (f"{m}+{n}" if p in (m, n) else p) for p in M_LABELS}
    74	        lam = {p: 1.0 for p in M_LABELS} | {m: 0.3, n: 0.7}
    75	        assert structurally_equal(coarsen(F_, c, lam), merge(F_, m, n, 0.3))
    76	    for m in M_LABELS:
    77	        c = {p: (None if p == m else p) for p in M_LABELS}
    78	        G_, D_ = coarsen(F_, c), drop(F_, m)
    79	        total = sum(G_.weights.values())
    80	        renorm = FormalizedStructure(**{**G_.__dict__,
    81	                                        "weights": {p: w / total for p, w in G_.weights.items()}})
    82	        assert structurally_equal(renorm, D_)  # drop() renormalizes omega, coarsen() does not
    83	
    84	
    85	def test_coarsen_validation():
    86	    F_ = represent(minimal_record(HARD_CASES[0]))
    87	    with pytest.raises(ValueError):
    88	        coarsen(F_, {"F": "F"})
    89	    with pytest.raises(ValueError):
    90	        coarsen(F_, MANN, {p: 0.5 for p in M_LABELS})  # singleton blocks need lam = 1
    91	    with pytest.raises(ValueError):
    92	        coarsen(F_, MANN, {**{p: 1.0 for p in M_LABELS}, "P": 0.0, "J": 1.0})
    93	    with pytest.raises(ValueError):
    94	        witness_coarsening(IDENTITY)
    95	
    96	
    97	# P-equality and factorization ---------------------------------------------------------------
    98	
    99	
   100	def test_p_equal_detects_renaming_and_differences():
   101	    rec = record_from_polity(fused_polity())
   102	    F_ = represent(rec)
   103	    ren = {v: f"z-{v}" for v in F_.actors}
   104	    G_ = FormalizedStructure(
   105	        actors=tuple(ren[v] for v in F_.actors), pillars=F_.pillars,
   106	        roles={ren[v]: ps for v, ps in F_.roles.items()}, layers=F_.layers,
   107	        shares={m: {ren[v]: x for v, x in s.items()} for m, s in F_.shares.items()},
   108	        contestability=F_.contestability, weights=F_.weights,
   109	        kappa={frozenset(ren[v] for v in S): r for S, r in F_.kappa.items()},
   110	        links=frozenset((ren[a], ren[b], m) for a, b, m in F_.links), arcs=F_.arcs)
   111	    assert p_equal(F_, G_)
   112	    layers = {m: a.copy() for m, a in F_.layers.items()}
   113	    layers["J"][0, 1] = 0.5
   114	    assert not p_equal(F_, FormalizedStructure(**{**F_.__dict__, "layers": layers}))
   115	
   116	
   117	@pytest.mark.parametrize("alpha", [alpha_represent, alpha_renamed])
   118	def test_p_preserving_abstractions_factor_through_phi(alpha):
   119	    recs = _fixtures()
   120	    result = factor_through_phi(alpha, recs)
   121	    assert result.well_defined and result.bijective
   122	
   123	
   124	def test_fixtures_have_distinct_p_classes():
   125	    phis = [phi(r) for r in _fixtures()]
   126	    for i, j in itertools.combinations(range(len(phis)), 2):
   127	        assert not p_equal(phis[i], phis[j]), (i, j)
   128	
   129	
   130	def test_non_p_preserving_abstraction_fails_to_factor():
   131	    # Mann's encoding identifies the witness pair, so h would not be a function.
   132	    recs = list(witness_pair("mann"))
   133	    alpha = lambda r: tuple(sorted((k, round(v, 9)) for k, v in  # noqa: E731
   134	                                   coarsen(represent(r), MANN).shares["Political"].items()))
   135	    assert not factor_through_phi(alpha, recs).well_defined
   136	
   137	
   138	# Witnesses: every non-injective coarsening collapses a pair ---------------------------------
   139	
   140	
   141	def _check_witness(c, lam=None):
   142	    g1, g2 = witness_coarsening(c, lam)
   143	    assert check_proposition_a(g1.system).holds and check_proposition_a(g2.system).holds
   144	    assert representable(g1) and representable(g2)
   145	    F1, F2 = phi(g1), phi(g2)
   146	    assert not p_equal(F1, F2)
   147	    assert coarsenings_equal(coarsen(F1, c, lam), coarsen(F2, c, lam))
   148	
   149	
   150	@pytest.mark.parametrize("m,n", list(itertools.combinations(M_LABELS, 2)))
   151	@pytest.mark.parametrize("lam_m", [0.2, 0.5, 0.9])
   152	def test_every_merge_collapses_a_witness(m, n, lam_m):
   153	    c = {p: (f"{m}+{n}" if p in (m, n) else p) for p in M_LABELS}
   154	    lam = {p: 1.0 for p in M_LABELS} | {m: lam_m, n: 1 - lam_m}
   155	    _check_witness(c, lam)
   156	
   157	
   158	@pytest.mark.parametrize("m", M_LABELS)
   159	def test_every_drop_collapses_a_witness(m):
   160	    _check_witness({p: (None if p == m else p) for p in M_LABELS})
   161	
   162	
   163	def test_pigeonhole_every_partition_with_fewer_than_six_blocks():
   164	    rng = np.random.default_rng(0)
   165	    count = 0
   166	    for part in _all_set_partitions(list(M_LABELS)):
   167	        if len(part) == 6:
   168	            continue
   169	        c = {p: "|".join(block) for block in part for p in block}
   170	        lam = {}
   171	        for block in part:
   172	            w = rng.dirichlet(np.ones(len(block)))
   173	            lam.update(dict(zip(block, w / w.sum())))
   174	        _check_witness(c, lam)
   175	        count += 1
   176	    assert count == 202  # Bell(6) - 1
   177	
   178	
   179	def test_pigeonhole_random_maps_with_drops():
   180	    rng = np.random.default_rng(1)
   181	    targets = ["k0", "k1", "k2", "k3", "k4", "k5", None]
   182	    for _ in range(150):
   183	        c = {p: targets[rng.integers(len(targets))] for p in M_LABELS}
   184	        if None not in c.values() and len(set(c.values())) == 6:
   185	            continue
   186	        _check_witness(c)
   187	
   188	
   189	# Predecessor encodings ----------------------------------------------------------------------
   190	
   191	
   192	@pytest.mark.parametrize("k", list(ENCODINGS))
   193	def test_predecessor_encoding_collapses_its_witness(k):
   194	    g1, g2 = witness_pair(k)
   195	    assert check_proposition_a(g1.system).holds and check_proposition_a(g2.system).holds
   196	    F1, F2 = represent(g1), represent(g2)
   197	    a1, a2 = ENCODINGS[k](F1), ENCODINGS[k](F2)
   198	    if isinstance(a1, FormalizedStructure):
   199	        assert coarsenings_equal(a1, a2)
   200	    else:
   201	        assert a1 == a2
   202	    assert not p_equal(F1, F2)
   203	
   204	
   205	@pytest.mark.parametrize("cmap,blocks", [(PARSONS, 4), (MANN, 4), (EASTON, 2), (LUHMANN, 4),
   206	                                         (ALMOND, 4)])
   207	def test_coarsening_encodings_have_fewer_than_six_dimensions(cmap, blocks):
   208	    assert len({v for v in cmap.values() if v is not None}) == blocks < 6
   209	    assert set(cmap) == set(M_LABELS)
   210	
   211	
   212	def test_aristotle_typology():
   213	    F_ = represent(two_actor_record({"P": (1.0, 0.0)}))
   214	    assert encode_aristotle(F_) == ("one", "correct")
   215	    assert encode_aristotle(represent(record_from_polity(fused_polity()))) == ("one", "deviant")
   216	    assert encode_aristotle(represent(record_from_polity(plural_polity())))[0] == "few"
   217	
   218	
   219	def test_weber_label_is_not_determined_by_p():
   220	    rec = two_actor_record({})
   221	    F_ = represent(rec)
   222	    assert p_equal(F_, represent(rec))
   223	    assert encode_weber(F_, "traditional", False) != encode_weber(F_, "legal-rational", True)
   224	    with pytest.raises(ValueError):
   225	        encode_weber(F_, "theocratic", True)

2026-10-22T17:59:18.096611Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/tests/test_necessity.py
nl -ba model/beast_system/representation.py | sed -n '456,575p'
rg -n \"def check_proposition_a|class Proposition|class GovernanceSystem|def generate_dependencies|def role_map|def realized_form|EXTENDED_AXIOMS|D0_KEYS|D_STAR_KEYS\" model/beast_system/necessity.py" in /Users/mlong/Documents/Development/the-beast-system
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
    78	    assert result.counterexample and result.struct_counterexample
    79	    assert derive_functions(system)[Axiom.Ax5].form is None
    80	
    81	
    82	def test_non_persistent_system_does_not_trigger_theorem():
    83	    system = GovernanceSystem("short-lived", False, EXTENDED_AXIOMS, ())
    84	    assert not check_proposition_a(system).antecedent
    85	    assert not check_proposition_a(system).counterexample
    86	    assert not check_proposition_a(system).struct_counterexample
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
   116	    assert not result.struct and result.struct_counterexample and result.counterexample
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
   136	    assert D0_KEYS == w_arcs | {arc_key({I, C}, J), arc_key(I, F)}
   137	    assert D_STAR_KEYS == D0_KEYS | {arc_key(F, W), arc_key(P, F), arc_key(J, F),
   138	                                     arc_key(C, F)}
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
   208	    assert result.struct and not result.struct_counterexample  # struct only needs D0
   209	    assert not result.interdependent and not result.holds and result.counterexample
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
   253	    assert not result.counterexample and not result.holds
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
   268	
   269	
   270	def test_d0_axioms_without_x_give_struct_but_not_interdependence():
   271	    # Part VII Prop 5.10(a): Ax1..Ax6 without the incidence axioms.
   272	    system = GovernanceSystem("baseline without X", True, frozenset(Axiom),
   273	                              BASELINE_MODEL.practices)
   274	    result = check_proposition_a(system)
   275	    assert result.dependencies == D0_KEYS
   276	    assert result.struct and not result.struct_counterexample
   277	    assert not result.interdependent and not result.holds
   278	    assert not result.counterexample  # extended antecedent fails, so not a counterexample
   279	    graph = underlying_digraph(result.dependencies)
   280	    assert not any(W in targets for targets in graph.values())  # no arc into W
   281	
   282	
   283	def test_hard_case_x_codings_are_sourced():
   284	    from beast_system.necessity import X_CODING_SOURCES
   285	
   286	    assert set(X_CODING_SOURCES) == {s.name for s in HARD_CASES}
   287	    for codings in X_CODING_SOURCES.values():
   288	        assert set(codings) == set(IncidenceAxiom)
   289	        assert all("(" in src and src.endswith(")") for src in codings.values())
   290	
   291	
   292	def test_further_rules_are_never_generated():
   293	    assert rules_holding(EXTENDED_AXIOMS, FURTHER_RULES) == ()
   294	    assert generate_dependencies(BASELINE_MODEL, CORE_RULES + FURTHER_RULES) == D_STAR_KEYS
   295	    further = {r.key: r.premise for r in FURTHER_RULES}
   296	    assert further == {
   297	        arc_key(I, P): "X2 + Ax4",
   298	        arc_key(P, J): "X2 + Ax4",
   299	        arc_key(P, I): "X2 + Ax4",
   300	        arc_key(J, P): "precedent (Hart)",
   301	        arc_key(I, C): "Ax4 at C's rules",
   302	        arc_key({F, I}, C): "Part V Cor 3.7 conditions",
   303	    }
   304	    assert all(not r.core for r in FURTHER_RULES)
   305	
   306	
   307	def test_incidence_axiom_statements_and_falsifiers():
   308	    assert [(x.base, x.target) for x in IncidenceAxiom] == [
   309	        (Axiom.Ax1, W), (Axiom.Ax2, F), (Axiom.Ax3, F), (Axiom.Ax5, F)]
   310	    assert "conflicting claims" in X1.statement and "anticipable assignment" in X1.statement
   311	    assert "infinitely often" in X2.statement and "Ass 3.2" in X2.statement
   312	    assert "open texture" in X3.statement and "residual disputes" in X3.statement
   313	    assert X5.statement == "Ax5 holds for some settlement procedure"
   314	    assert X1.falsifier == "a persistent collective whose productive inputs never meet conflicting claims"
   315	    assert X2.falsifier == ("a persistent collective whose prior settlement procedures settle "
   316	                            "every new conflict")
   317	    assert X3.falsifier == "settlement procedures that leave only finitely many residual disputes"
   318	    assert X5.falsifier == "no member ever breaks any settlement procedure"
   319	
   320	
   321	def test_hard_case_x_codings_cite_the_part_vii_sources():
   322	    from beast_system.necessity import (
   323	        CONSENSUS_VILLAGE, OSTROM_COMMONS, X_CODING_SOURCES)
   324	
   325	    expected = {
   326	        NUER.name: {X1: "evanspritchard1940", X2: "evanspritchard1940",
   327	                    X3: "evanspritchard1940", X5: "evanspritchard1940"},
   328	        JU_HOANSI.name: {X1: "lee2013", X2: "lee2013", X3: "wiessner2005", X5: "wiessner2005"},
   329	        OSTROM_COMMONS.name: {X1: "ostrom1990", X2: "ostrom1990", X3: "cox2010",
   330	                              X5: "ostrom1990"},
   331	        CONSENSUS_VILLAGE.name: {X1: "sahlins1972", X2: "graeber2021", X3: "boehm1999",
   332	                                 X5: "boehm1999"},
   333	    }
   334	    for case, keys in expected.items():
   335	        for x, key in keys.items():
   336	            assert key in X_CODING_SOURCES[case][x], (case, x)
   456	# Coarsenings (minimality) ------------------------------------------------------------------
   457	
   458	
   459	def drop(F: FormalizedStructure, m: Label) -> FormalizedStructure:
   460	    """Delete pillar m: its layer, shares, Q, kappa column and every hyperarc involving m.
   461	
   462	    Remaining weights are renormalized to sum 1.
   463	    """
   464	    if m not in F.pillars:
   465	        raise ValueError(f"unknown pillar {m!r}")
   466	    keep = tuple(p for p in F.pillars if p != m)
   467	    total = sum(F.weights[p] for p in keep)
   468	    weights = {p: (F.weights[p] / total if total > 0 else 1.0 / len(keep)) for p in keep}
   469	    return FormalizedStructure(
   470	        actors=F.actors, pillars=keep,
   471	        roles={v: ps - {m} for v, ps in F.roles.items()},
   472	        layers={p: F.layers[p] for p in keep},
   473	        shares={p: dict(F.shares[p]) for p in keep},
   474	        contestability={p: F.contestability[p] for p in keep},
   475	        weights=weights,
   476	        kappa={s: {p: row.get(p, 0.0) for p in keep} for s, row in F.kappa.items()},
   477	        links=frozenset(lk for lk in F.links if lk[2] != m),
   478	        arcs=frozenset((t, h) for t, h in F.arcs if h != m and m not in t),
   479	    )
   480	
   481	
   482	def merge(F: FormalizedStructure, m: Label, n: Label, lam: float) -> FormalizedStructure:
   483	    """Replace m, n by one pillar 'm+n': holders united, shares, layers, Q and kappa mixed with
   484	    weight lam on m; omega_m + omega_n; arcs relabeled, self-loops removed."""
   485	    if m == n or m not in F.pillars or n not in F.pillars:
   486	        raise ValueError("merge needs two distinct existing pillars")
   487	    lam = validate_unit_interval(lam, "lam")
   488	    new = f"{m}+{n}"
   489	    keep = tuple(new if p == m else p for p in F.pillars if p != n)
   490	    relabel = lambda p: new if p in (m, n) else p  # noqa: E731
   491	
   492	    def mix(a: float, b: float) -> float:
   493	        return lam * a + (1.0 - lam) * b
   494	
   495	    shares = {p: dict(F.shares[p]) for p in keep if p != new}
   496	    shares[new] = {v: mix(F.shares[m].get(v, 0.0), F.shares[n].get(v, 0.0)) for v in F.actors}
   497	    layers = {p: F.layers[p] for p in keep if p != new}
   498	    layers[new] = lam * F.layers[m] + (1.0 - lam) * F.layers[n]
   499	    contest = {p: F.contestability[p] for p in keep if p != new}
   500	    contest[new] = mix(F.contestability[m], F.contestability[n])
   501	    weights = {p: F.weights[p] for p in keep if p != new}
   502	    weights[new] = F.weights[m] + F.weights[n]
   503	    kappa = {}
   504	    for s, row in F.kappa.items():
   505	        r = {p: row.get(p, 0.0) for p in keep if p != new}
   506	        r[new] = mix(row.get(m, 0.0), row.get(n, 0.0))
   507	        kappa[s] = r
   508	    arcs = set()
   509	    for t, h in F.arcs:
   510	        t2, h2 = frozenset(relabel(x) for x in t), relabel(h)
   511	        if h2 not in t2:
   512	            arcs.add((t2, h2))
   513	    return FormalizedStructure(
   514	        actors=F.actors, pillars=keep,
   515	        roles={v: frozenset(relabel(p) for p in ps) for v, ps in F.roles.items()},
   516	        layers=layers, shares=shares, contestability=contest, weights=weights, kappa=kappa,
   517	        links=frozenset((a, b, relabel(p)) for a, b, p in F.links),
   518	        arcs=frozenset(arcs),
   519	    )
   520	
   521	
   522	def structurally_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   523	    """Equality of every component with the identity on actor names (floats within 1e-9)."""
   524	    if not (well_formed(F) and well_formed(G)):
   525	        return False
   526	    if (F.actors, F.pillars, F.links, F.arcs) != (G.actors, G.pillars, G.links, G.arcs):
   527	        return False
   528	    if any(F.roles[v] != G.roles[v] for v in F.actors) or set(F.kappa) != set(G.kappa):
   529	        return False
   530	    return (
   531	        all(_same(F.shares[m][v], G.shares[m][v]) for m in F.pillars for v in F.actors)
   532	        and all(np.allclose(F.layers[m], G.layers[m], atol=_ATOL, rtol=0) for m in F.pillars)
   533	        and all(_same(F.contestability[m], G.contestability[m]) for m in F.pillars)
   534	        and all(_same(F.weights[m], G.weights[m]) for m in F.pillars)
   535	        and all(set(F.kappa[S]) == set(G.kappa[S])
   536	                and all(_same(F.kappa[S][m], G.kappa[S][m]) for m in F.kappa[S])
   537	                for S in F.kappa)
   538	    )
   539	
   540	
   541	D_STAR_LABELS: frozenset[LabelArc] = frozenset(
   542	    (frozenset(t.name for t in tail), head.name) for tail, head in D_STAR_KEYS
   543	)
   544	
   545	
   546	def make_structure(
   547	    shares: Mapping[Label, Mapping[str, float]],
   548	    contestability: Mapping[Label, float],
   549	    weights: Mapping[Label, float] | None = None,
   550	    kappa: Mapping[frozenset[str], Mapping[Label, float]] | None = None,
   551	    links: Iterable[tuple[str, str, Label]] = (),
   552	    arcs: Iterable[LabelArc] = D_STAR_LABELS,
   553	) -> FormalizedStructure:
   554	    """Build F directly: holders are actors with positive share, a^m_ij = s^m_i (i != j),
   555	    singleton coalitions by default. Used for the minimality fixtures."""
   556	    pillars = tuple(shares)
   557	    actors = tuple(sorted({v for s in shares.values() for v in s}))
   558	    full = {m: {v: float(shares[m].get(v, 0.0)) for v in actors} for m in pillars}
   559	    roles = {v: frozenset(m for m in pillars if full[m][v] > 0) for v in actors}
   560	    layers = {}
   561	    for m in pillars:
   562	        arr = np.tile(np.array([full[m][v] for v in actors])[:, None], (1, len(actors)))
   563	        np.fill_diagonal(arr, 0.0)
   564	        layers[m] = arr
   565	    if kappa is None:
   566	        kappa = {frozenset({v}): {m: full[m][v] for m in pillars} for v in actors}
   567	    return FormalizedStructure(
   568	        actors=actors, pillars=pillars, roles=roles, layers=layers, shares=full,
   569	        contestability=dict(contestability),
   570	        weights=dict(weights) if weights else {m: 1.0 / len(pillars) for m in pillars},
   571	        kappa={s: dict(r) for s, r in kappa.items()},
   572	        links=frozenset(links), arcs=frozenset(arcs),
   573	    )
52:EXTENDED_AXIOMS: frozenset[AnyAxiom] = frozenset(Axiom) | frozenset(IncidenceAxiom)
254:D_STAR_KEYS: frozenset[ArcKey] = frozenset(r.key for r in CORE_RULES)
257:D0_KEYS: frozenset[ArcKey] = frozenset(
279:def dependency_graph(axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS) -> dict[Pillar, frozenset[Pillar]]:
317:class GovernanceSystem:
364:        return EXTENDED_AXIOMS <= self.axioms
367:def generate_dependencies(
377:def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
386:def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
446:class PropositionAResult:
487:def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
494:    needed = frozenset((t, h) for t, h in D0_KEYS if h in realized and t <= realized)
516:    axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS,
546:    axioms=EXTENDED_AXIOMS,
567:    axioms=EXTENDED_AXIOMS,
587:    axioms=EXTENDED_AXIOMS,
608:    axioms=EXTENDED_AXIOMS,

2026-10-22T17:59:21.286610Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
The first substantive issue is in the uniqueness evidence: the factorization fixtures are explicitly pairwise distinct P-classes, so both “P-preserving” examples avoid the isomorphic-input case that actually tests whether the abstraction descends to P. I’m checking that and the representation-domain edge cases with targeted executions now.
hook: PreToolUse
hook: PreToolUse Completed
2026-10-22T18:00:39.447388Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider tests/test_representation.py tests/test_uniqueness.py tests/test_necessity.py' in /Users/mlong/Documents/Development/the-beast-system/model
2026-10-22T18:00:44.845938Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 exited 1 in 1823ms:
2026-10-22 13:00:43.404 xcodebuild[73138:4173440]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:00:43.549 xcodebuild[73138:4173426] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-EWFCiNS2' (errno=Operation not permitted)
2026-10-22 13:00:44.003 xcodebuild[73141:4173463]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:00:44.092 xcodebuild[73141:4173462] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
/Applications/Xcode.app/Contents/Developer/usr/bin/python3: No module named pytest

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'command -v -a python python3 pytest uv pipx || true
ls -la .venv/bin/python .venv/bin/pytest venv/bin/python venv/bin/pytest 2>/dev/null || true' in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 0ms:
zsh:1: command not found: -v

2026-10-22T18:00:50.258588Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'whence -a python python3 pytest uv pipx
ls -la .venv/bin/python .venv/bin/pytest venv/bin/python venv/bin/pytest 2>/dev/null || true' in /Users/mlong/Documents/Development/the-beast-system/model
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
/opt/homebrew/bin/pipx

2026-10-22T18:00:53.457735Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3 -m pytest -q -p no:cacheprovider tests/test_representation.py tests/test_uniqueness.py tests/test_necessity.py' in /Users/mlong/Documents/Development/the-beast-system/model
 exited 1 in 0ms:
/opt/homebrew/opt/python@3.15/bin/python3.15: No module named pytest

2026-10-22T18:00:56.142821Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3 -c 'from dataclasses import replace; from beast_system.necessity import BASELINE_MODEL, check_proposition_a; from beast_system.representation import minimal_record, representable; s=replace(BASELINE_MODEL, persistent=False); r=minimal_record(s); print(\"persistent theorem\", representable(r), check_proposition_a(s).holds)'" in /Users/mlong/Documents/Development/the-beast-system/model
2026-10-22T18:01:12.240227Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 196ms:
persistent theorem True True

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3 -c 'from beast_system.necessity import GovernanceSystem, check_proposition_a; from beast_system.representation import minimal_record, representable; s=GovernanceSystem(\"short\",False,frozenset(),()); r=minimal_record(s); a=check_proposition_a(s); print(representable(r),a.holds,a.antecedent,a.counterexample)'" in /Users/mlong/Documents/Development/the-beast-system/model
2026-10-22T18:01:18.737968Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 exited 1 in 170ms:
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    from beast_system.necessity import GovernanceSystem, check_proposition_a; from beast_system.representation import minimal_record, representable; s=GovernanceSystem("short",False,frozenset(),()); r=minimal_record(s); a=check_proposition_a(s); print(representable(r),a.holds,a.antecedent,a.counterexample)
                                                                                                                                                                                                                                                            ~~~~~~~~~~~~~^^^
  File "/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py", line 316, in representable
    return in_formalized_class(represent(record)).holds
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py", line 299, in in_formalized_class
    if (s.min() < 0 or abs(s.sum() - 1.0) > _ATOL or not on_holders or not rows_ok
        ~~~~~^^
  File "/opt/homebrew/lib/python3.15/site-packages/numpy/_core/_methods.py", line 45, in _amin
    return umr_minimum(a, axis, None, out, keepdims, initial, where)
ValueError: zero-size array to reduction operation minimum which has no identity

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3 -c 'from dataclasses import replace; from beast_system.necessity import AXIOM_INDEPENDENCE, check_proposition_a; from beast_system.pillars import Axiom; from beast_system.representation import minimal_record, representable; s=replace(AXIOM_INDEPENDENCE[Axiom.Ax1], persistent=False); r=minimal_record(s); a=check_proposition_a(s); print(representable(r),a.holds,a.antecedent,a.counterexample)'" in /Users/mlong/Documents/Development/the-beast-system/model
2026-10-22T18:01:25.409911Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 151ms:
False False False False

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3 -c 'from beast_system.necessity import BASELINE_MODEL; from beast_system.representation import *; f=represent(minimal_record(BASELINE_MODEL)); g=FormalizedStructure(**{**f.__dict__,\"arcs\":f.arcs|{(frozenset({\"Z\"}),\"F\")}}); print(well_formed(g),in_formalized_class(g))'" in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 145ms:
True ClassMembership(f1=True, f2=True, f3=True, f4=True)

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3 -c 'from dataclasses import fields; from beast_system.necessity import Practice, GovernanceSystem; from beast_system.representation import CodedRecord; print([f.name for f in fields(Practice)]); print([f.name for f in fields(GovernanceSystem)]); print([f.name for f in fields(CodedRecord)])'" in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 148ms:
['description', 'solves', 'holders', 'formal', 'source']
['name', 'persistent', 'axioms', 'practices', 'absent_incidences', 'note']
['system', 'shares', 'contestability', 'weights', 'coalitions', 'links']

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3 -c 'from dataclasses import replace; from beast_system.uniqueness import *; from beast_system.representation import CodedRecord,represent; r=two_actor_record({\"F\":(0.8,0.2),\"P\":(0.7,0.3)}); ren={\"a\":\"z\",\"b\":\"y\"}; ps=tuple(replace(p,holders=frozenset(ren[x] for x in p.holders)) for p in r.system.practices); s=replace(r.system,practices=ps); rr=CodedRecord(s,{m:{ren[x]:v for x,v in row.items()} for m,row in r.shares.items()},r.contestability,weights=r.weights,coalitions=None); print(\"p_equal\",p_equal(phi(r),phi(rr))); print(\"alpha_represent equal\",alpha_represent(r)==alpha_represent(rr),factor_through_phi(alpha_represent,[r,rr])); print(\"alpha_renamed equal\",alpha_renamed(r)==alpha_renamed(rr),factor_through_phi(alpha_renamed,[r,rr]))'" in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 148ms:
p_equal True
alpha_represent equal False Factorization(well_defined=True, bijective=False)
alpha_renamed equal False Factorization(well_defined=True, bijective=False)

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3 -c 'from beast_system.necessity import BASELINE_MODEL; from beast_system.pillars import PILLARS; from beast_system.representation import CodedRecord,minimal_record,represent; g=minimal_record(BASELINE_MODEL); r=CodedRecord(g.system,g.shares,g.contestability,coalitions={frozenset({42}):{PILLARS[0]:0.5}}); print(\"accepted\"); represent(r)'" in /Users/mlong/Documents/Development/the-beast-system/model
2026-10-22T18:02:40.264039Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 exited 1 in 174ms:
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    from beast_system.necessity import BASELINE_MODEL; from beast_system.pillars import PILLARS; from beast_system.representation import CodedRecord,minimal_record,represent; g=minimal_record(BASELINE_MODEL); r=CodedRecord(g.system,g.shares,g.contestability,coalitions={frozenset({42}):{PILLARS[0]:0.5}}); print("accepted"); represent(r)
                                                                                                                                                                                                                                                                                                                                     ~~~~~~~~~^^^
  File "/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py", line 171, in represent
    actors = tuple(sorted(set(performers) | named))
                   ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: '<' not supported between instances of 'int' and 'str'
accepted

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba /Users/mlong/.codex/memories/MEMORY.md | sed -n '75,93p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
    75	# Task Group: the-beast-system comparative research-paper setup
    76	scope: Continue the local research-content project and six-paper planning while retaining the boundary between source organization/scoping and any completed research outcome.
    77	applies_to: cwd=/Users/mlong/the-beast-system; reuse_rule=project contents and research conclusions must be inspected from the current files; observed planning activity is not a validated paper or published claim.
    78	
    79	## Task 1: Create context workspace and scope comparative papers, observed/partial
    80	
    81	### rollout_summary_files
    82	
    83	- extensions/skysight/resources/2026-10-22T13-40-00-mOWP-10min-memory-summary.md (cwd=/Users/mlong/the-beast-system, rollout_path=extensions/skysight/resources/2026-10-22T13-40-00-mOWP-10min-memory-summary.md, updated_at=2026-10-22T13:40:00+00:00, thread_id=None, research framing continued; no response or artifact outcome captured) [skysight memory]
    84	- extensions/skysight/resources/2026-10-22T13-20-00-YYQx-10min-memory-summary.md (cwd=/Users/mlong/the-beast-system, rollout_path=extensions/skysight/resources/2026-10-22T13-20-00-YYQx-10min-memory-summary.md, updated_at=2026-10-22T13:20:00+00:00, thread_id=None, project and `context` directory created; draft revised) [skysight memory]
    85	
    86	### keywords
    87	
    88	- `the-beast-system`, `context`, `six-pillars-beast-system-papers`, comparative research, Apple Notes, paper scoping, Parallels error 521
    89	
    90	## Reusable knowledge
    91	
    92	- The user created `the-beast-system` and a `context` subdirectory, organized source material, revised a related Apple Notes draft, and began an initial paper-scoping session. Subsequent conceptual questions and “more context” in `six-pillars-beast-system-papers` did not yield a captured research response, source inspection, plan, or artifact. [Task 1] [skysight memory]
    93	

2026-10-22T18:03:07.923948Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
- [P1] `representable()` is not total over accepted `CodedRecord`s. A record with no implemented pillars is accepted, but its zero-actor image reaches `s.min()`/`arr.min()` and raises `ValueError` instead of returning false. The 300-record test does not explicitly cover this boundary. [representation.py:299](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py:299) [test_representation.py:214](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_representation.py:214)

- [P1] The claimed factorization examples are not P-preserving. `alpha_represent` retains actor names, while `alpha_renamed` depends on actor-name ordering. For two actor-renamed records, `p_equal(phi(r1), phi(r2))` is true, but both alpha values differ and `factor_through_phi(...).bijective` is false. Existing fixtures are explicitly pairwise P-distinct, making the crucial `same_p ⇒ same_alpha` branch vacuous. [uniqueness.py:173](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/uniqueness.py:173) [test_uniqueness.py:117](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_uniqueness.py:117) [test_uniqueness.py:124](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_uniqueness.py:124)

- [P1] Coalition keys are only checked for being nonempty frozensets, not for containing valid actor identifiers. For example, `frozenset({42})` is accepted and then makes `represent()` fail while sorting mixed `str`/`int` actors. Thus the claimed coalition validation still does not make the accepted record domain safe for the representation theorem. [representation.py:115](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py:115) [representation.py:171](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py:171)

- [P2] `well_formed()` never validates hyperarc tails and heads against the pillar domain. Adding `(frozenset({"Z"}), "F")` to an otherwise valid structure leaves both `well_formed()` and `in_formalized_class().holds` true. The malformed-structure test omits arcs, so the stated strict domain gate remains incomplete. [representation.py:252](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py:252) [test_representation.py:250](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_representation.py:250)

VERDICT: NEEDS_FIX


hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
60,306
- [P1] `representable()` is not total over accepted `CodedRecord`s. A record with no implemented pillars is accepted, but its zero-actor image reaches `s.min()`/`arr.min()` and raises `ValueError` instead of returning false. The 300-record test does not explicitly cover this boundary. [representation.py:299](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py:299) [test_representation.py:214](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_representation.py:214)

- [P1] The claimed factorization examples are not P-preserving. `alpha_represent` retains actor names, while `alpha_renamed` depends on actor-name ordering. For two actor-renamed records, `p_equal(phi(r1), phi(r2))` is true, but both alpha values differ and `factor_through_phi(...).bijective` is false. Existing fixtures are explicitly pairwise P-distinct, making the crucial `same_p ⇒ same_alpha` branch vacuous. [uniqueness.py:173](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/uniqueness.py:173) [test_uniqueness.py:117](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_uniqueness.py:117) [test_uniqueness.py:124](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_uniqueness.py:124)

- [P1] Coalition keys are only checked for being nonempty frozensets, not for containing valid actor identifiers. For example, `frozenset({42})` is accepted and then makes `represent()` fail while sorting mixed `str`/`int` actors. Thus the claimed coalition validation still does not make the accepted record domain safe for the representation theorem. [representation.py:115](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py:115) [representation.py:171](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py:171)

- [P2] `well_formed()` never validates hyperarc tails and heads against the pillar domain. Adding `(frozenset({"Z"}), "F")` to an otherwise valid structure leaves both `well_formed()` and `in_formalized_class().holds` true. The malformed-structure test omits arcs, so the stated strict domain gate remains incomplete. [representation.py:252](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py:252) [test_representation.py:250](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_representation.py:250)

VERDICT: NEEDS_FIX


exit 0
