Reading additional input from stdin...
2026-10-22T17:45:26.052843Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a164b7-c1bc-7ab0-8a34-f2e25bfc208a
--------
user
Review only model/beast_system/necessity.py, model/beast_system/pillars.py (IncidenceAxiom statements) and model/tests/test_necessity.py. Do not explore elsewhere. This is a scoped round covering only these changes made after the previous review:
(1) D0 now = W->F, W->P, W->J, W->I, W->C (Ax6), OR-hyperarc ({I,C} -> J) (Ax3+Ax4+Ax5, Part III Prop 3.6), and I->F (Ax4+Ax1). D0_KEYS is computed as the core rules with no incidence-axiom premise. D* = D0 plus X1 F->W, X2 P->F, X3 J->F, X5 C->F.
(2) PropositionAResult: struct = six pillars realized AND D0 generated; interdependent = six realized AND generated hypergraph's underlying digraph strongly connected AND cascade-complete; holds = struct AND interdependent; counterexample = persistent and extended axioms (Ax1..Ax6, X1, X2, X3, X5) hold but holds False; struct_counterexample = persistent, Ax1..Ax6 hold, struct False.
(3) Further (reported, not generated) arcs now include I->C (Ax4 at C's rules).
(4) IncidenceAxiom statements and falsifiers revised; X_CODING_SOURCES maps each hard case to qualitative X codings with sources.
(5) Tests updated accordingly, plus test_d0_axioms_without_x_give_struct_but_not_interdependence (Ax1..Ax6 without X: struct True, interdependent False, no arc into W) and test_hard_case_x_codings_are_sourced.
Check correctness of these semantics, that removing any premise removes its arcs, that tests assert the claims, and any defect introduced. Output the findings list and the VERDICT line only. End with VERDICT: PASS or VERDICT: NEEDS_FIX.
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T17:45:27.455527Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T17:45:28.323724Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
I’ll inspect exactly the three named files and compare the rule generation, falsifiers, and tests against the five stated changes.
codex
I’m using the code-review skill to keep the review evidence-focused and severity-ranked; I’ll preserve the requested findings-only final format.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'cat /Users/mlong/.codex/plugins/cache/claude-cowork/engineering/1.1.0/skills/code-review/SKILL.md && rg -n -i "the-beast-system|necessity.py|IncidenceAxiom|D0_KEYS|PropositionAResult" /Users/mlong/.codex/memories/MEMORY.md' in /Users/mlong/Documents/Development/the-beast-system
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

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'git status --short -- model/beast_system/necessity.py model/beast_system/pillars.py model/tests/test_necessity.py && git diff -- model/beast_system/necessity.py model/beast_system/pillars.py model/tests/test_necessity.py && wc -l model/beast_system/necessity.py model/beast_system/pillars.py model/tests/test_necessity.py && nl -ba model/beast_system/necessity.py && nl -ba model/beast_system/pillars.py && nl -ba model/tests/test_necessity.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 2892ms:
2026-10-22 12:45:44.523 xcodebuild[59443:4097166]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:45:44.656 xcodebuild[59443:4097165] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-nBIdPyMG' (errno=Operation not permitted)
2026-10-22 12:45:45.080 xcodebuild[59445:4097182]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:45:45.170 xcodebuild[59445:4097180] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
?? model/beast_system/necessity.py
?? model/beast_system/pillars.py
?? model/tests/test_necessity.py
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-qzz7gq40' (errno=Operation not permitted)
2026-10-22 12:45:46.011 xcodebuild[59540:4097324]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:45:46.099 xcodebuild[59540:4097322] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-BdCA3Vhf' (errno=Operation not permitted)
2026-10-22 12:45:46.480 xcodebuild[59542:4097335]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:45:46.570 xcodebuild[59542:4097333] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
     677 model/beast_system/necessity.py
     168 model/beast_system/pillars.py
     289 model/tests/test_necessity.py
    1134 total
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
    25	Interdependence = (a) and (b). Proposition A in full is Struct(G) (six pillars plus D0, from
    26	Ax1..Ax6) AND interdependence (from Ax1..Ax6 plus X1, X2, X3, X5); both are exposed
    27	separately. A system coding an incidence as absent while its premises hold is the falsifier
    28	route for either part.
    29	"""
    30	
    31	from __future__ import annotations
    32	
    33	from collections.abc import Iterable, Mapping
    34	from dataclasses import dataclass, field
    35	from typing import Literal
    36	
    37	from .pillars import AXIOM_TO_PILLAR, PILLAR_TO_AXIOM, PILLARS, Axiom, IncidenceAxiom, Pillar
    38	
    39	RealizedForm = Literal["formal institution", "fused", "informal/minimal"]
    40	FORMAL: RealizedForm = "formal institution"
    41	FUSED: RealizedForm = "fused"
    42	INFORMAL: RealizedForm = "informal/minimal"
    43	
    44	# Dependency hypergraph primitives ----------------------------------------------------------
    45	
    46	#: A hyperarc key (T, h): tail set T, head h.
    47	ArcKey = tuple[frozenset[Pillar], Pillar]
    48	Graph = Mapping[Pillar, Iterable[Pillar]]
    49	AnyAxiom = Axiom | IncidenceAxiom
    50	
    51	#: Ax1..Ax6 plus the incidence axioms X1, X2, X3, X5 (Part VII extended axiom set).
    52	EXTENDED_AXIOMS: frozenset[AnyAxiom] = frozenset(Axiom) | frozenset(IncidenceAxiom)
    53	
    54	
    55	def arc_key(tail: Pillar | Iterable[Pillar], head: Pillar) -> ArcKey:
    56	    """Normalize (T, h) to an ArcKey, validating T non-empty, h a Pillar and h not in T."""
    57	    t = frozenset((tail,) if isinstance(tail, Pillar) else tail)
    58	    if not t or not all(isinstance(m, Pillar) for m in t) or not isinstance(head, Pillar):
    59	        raise TypeError("a hyperarc needs a non-empty tail of Pillars and a Pillar head")
    60	    if head in t:
    61	        raise ValueError(f"head {head.name} may not belong to its own tail")
    62	    return t, head
    63	
    64	
    65	def _keys(arcs: Iterable[DependencyRule | ArcKey]) -> frozenset[ArcKey]:
    66	    return frozenset(a.key if isinstance(a, DependencyRule) else arc_key(*a) for a in arcs)
    67	
    68	
    69	def underlying_digraph(arcs: Iterable[DependencyRule | ArcKey]) -> dict[Pillar, frozenset[Pillar]]:
    70	    """Replace each hyperarc (T, h) by the arcs t -> h; adjacency over all six pillars."""
    71	    adj: dict[Pillar, set[Pillar]] = {m: set() for m in PILLARS}
    72	    for tail, head in _keys(arcs):
    73	        for t in tail:
    74	            adj[t].add(head)
    75	    return {m: frozenset(v) for m, v in adj.items()}
    76	
    77	
    78	def cascade_closure(
    79	    arcs: Iterable[DependencyRule | ArcKey], start: Iterable[Pillar]
    80	) -> frozenset[Pillar]:
    81	    """cl(S): least superset of S with T subset of cl(S) => h in cl(S) for every (T, h).
    82	
    83	    Read as a failure cascade: h fails once every provider in its tail has failed.
    84	    """
    85	    keys = _keys(arcs)
    86	    closed = set(start)
    87	    changed = True
    88	    while changed:
    89	        changed = False
    90	        for tail, head in keys:
    91	            if head not in closed and tail <= closed:
    92	                closed.add(head)
    93	                changed = True
    94	    return frozenset(closed)
    95	
    96	
    97	def is_cascade_complete(
    98	    arcs: Iterable[DependencyRule | ArcKey], nodes: Iterable[Pillar] = PILLARS
    99	) -> bool:
   100	    """True iff cl({n}) contains every node, for every node n (restricted to ``nodes``)."""
   101	    keep = frozenset(nodes)
   102	    if not keep:
   103	        return False
   104	    inside = [(t, h) for t, h in _keys(arcs) if h in keep and t <= keep]
   105	    return all(cascade_closure(inside, {n}) >= keep for n in keep)
   106	
   107	
   108	def _nodes(graph: Graph) -> set[Pillar]:
   109	    nodes = set(graph)
   110	    for targets in graph.values():
   111	        nodes.update(targets)
   112	    return nodes
   113	
   114	
   115	def _reach(graph: Mapping[Pillar, frozenset[Pillar]], start: Pillar) -> set[Pillar]:
   116	    seen = {start}
   117	    stack = [start]
   118	    while stack:
   119	        for nxt in graph.get(stack.pop(), frozenset()):
   120	            if nxt not in seen:
   121	                seen.add(nxt)
   122	                stack.append(nxt)
   123	    return seen
   124	
   125	
   126	def is_strongly_connected(graph: Graph, nodes: Iterable[Pillar] | None = None) -> bool:
   127	    """True iff every node of the graph is reachable from every other node.
   128	
   129	    ``nodes`` restricts the graph to an induced subgraph (default: all nodes that appear).
   130	    The empty graph is not strongly connected; a single node is.
   131	    """
   132	    keep = set(nodes) if nodes is not None else _nodes(graph)
   133	    if not keep:
   134	        return False
   135	    fwd: dict[Pillar, frozenset[Pillar]] = {
   136	        u: frozenset(v for v in graph.get(u, ()) if v in keep) for u in keep
   137	    }
   138	    rev: dict[Pillar, set[Pillar]] = {u: set() for u in keep}
   139	    for u, vs in fwd.items():
   140	        for v in vs:
   141	            rev[v].add(u)
   142	    start = next(iter(keep))
   143	    rev_f = {u: frozenset(v) for u, v in rev.items()}
   144	    return _reach(fwd, start) == keep and _reach(rev_f, start) == keep
   145	
   146	
   147	def critical_edges(graph: Graph) -> list[tuple[Pillar, Pillar]]:
   148	    """Edges whose single removal breaks strong connectivity (empty if not connected)."""
   149	    nodes = _nodes(graph)
   150	    base = {u: frozenset(graph.get(u, ())) for u in nodes}
   151	    if not is_strongly_connected(base):
   152	        return []
   153	    out = []
   154	    for u in PILLARS:
   155	        for v in sorted(base.get(u, ()), key=lambda p: p.position):
   156	            pruned = dict(base)
   157	            pruned[u] = base[u] - {v}
   158	            if not is_strongly_connected(pruned, nodes):
   159	                out.append((u, v))
   160	    return out
   161	
   162	
   163	def sinks_and_sources(graph: Graph) -> tuple[frozenset[Pillar], frozenset[Pillar]]:
   164	    """Pillars with no outgoing edge (sinks) and with no incoming edge (sources)."""
   165	    nodes = _nodes(graph)
   166	    has_out = {u for u in nodes if any(True for _ in graph.get(u, ()))}
   167	    has_in = {v for u in nodes for v in graph.get(u, ())}
   168	    return frozenset(nodes - has_out), frozenset(nodes - has_in)
   169	
   170	
   171	# Axiom-generated dependency rules (Part VII revised dependency spec) ----------------------
   172	
   173	
   174	@dataclass(frozen=True)
   175	class DependencyRule:
   176	    """A hyperarc (T, h) generated when every premise in ``requires`` holds.
   177	
   178	    h needs an output of AT LEAST ONE member of T (provider(s) -> dependent). ``incidence`` is
   179	    the incidence Inc(k, m) the rule instantiates (the problem of Ax_k arises about pillar m's
   180	    inputs or rules, giving arc pillar(k) -> m), or None for a rule that is not an incidence.
   181	    ``core`` marks membership of D*; non-core rules are reported, not needed.
   182	    """
   183	
   184	    tail: frozenset[Pillar]
   185	    head: Pillar
   186	    premise: str
   187	    requires: frozenset[AnyAxiom]
   188	    source: str
   189	    core: bool
   190	    incidence: tuple[Axiom, Pillar] | None = None
   191	
   192	    def __post_init__(self) -> None:
   193	        tail, _ = arc_key(self.tail, self.head)
   194	        requires = frozenset(self.requires)
   195	        if not requires or any(not isinstance(a, (Axiom, IncidenceAxiom)) for a in requires):
   196	            raise ValueError("a dependency rule needs at least one axiom premise")
   197	        if self.incidence is not None:
   198	            axiom, target = self.incidence
   199	            if tail != frozenset({axiom.pillar}) or target is not self.head:
   200	                raise ValueError("an incidence Inc(k, m) generates exactly pillar(k) -> m")
   201	            if axiom not in requires:
   202	                raise ValueError("an incidence rule must require its own axiom")
   203	        object.__setattr__(self, "tail", tail)
   204	        object.__setattr__(self, "requires", requires)
   205	
   206	    @property
   207	    def key(self) -> ArcKey:
   208	        return self.tail, self.head
   209	
   210	
   211	def _inc(axiom: Axiom, target: Pillar, premise: str, requires: Iterable[AnyAxiom],
   212	         source: str, core: bool = True) -> DependencyRule:
   213	    return DependencyRule(frozenset({axiom.pillar}), target, premise,
   214	                          frozenset(requires) | {axiom}, source, core, (axiom, target))
   215	
   216	
   217	_P, _A, _X = Pillar, Axiom, IncidenceAxiom
   218	
   219	#: D*: the core rules. Under Ax1..Ax6 plus X1, X2, X3, X5 they generate a strongly connected,
   220	#: cascade-complete hypergraph (Part VII revised dependency spec).
   221	CORE_RULES: tuple[DependencyRule, ...] = (
   222	    *(_inc(_A.Ax6, m, "Ax6", (), "practitioners consume produced resources (Part VI Lem 3.3, 3.4)")
   223	      for m in (_P.F, _P.P, _P.J, _P.I, _P.C)),
   224	    DependencyRule(frozenset({_P.I, _P.C}), _P.J, "Part III Prop 3.6",
   225	                   frozenset({_A.Ax3, _A.Ax4, _A.Ax5}),
   226	                   "loser complies iff ell + sigma >= g, g > 0: recognition or enforcement",
   227	                   core=True),
   228	    _inc(_A.Ax4, _P.F, "Ax4 + Ax1", (_A.Ax1,),
   229	         "settlements must be anticipable (Part I Def 2.2(b)); entrants learn the procedure "
   230	         "only through legitimation (Part IV Lem 3.4, Thm 3.5)"),
   231	    _inc(_A.Ax1, _P.W, "X1", (_X.X1,), "contested productive inputs (Part I)"),
   232	    _inc(_A.Ax2, _P.F, "X2", (_X.X2,), "changing environment hits allocation rules (Part II Ass 3.2)"),
   233	    _inc(_A.Ax3, _P.F, "X3", (_X.X3,), "open-textured allocation rules (Part III Thm 3.3)"),
   234	    _inc(_A.Ax5, _P.F, "X5", (_X.X5,), "tempting allocation rules (Part V Thm 3.4)"),
   235	)
   236	
   237	#: Further rules: reported, not needed for interdependence. Each rests on a premise beyond
   238	#: the extended axiom set (stated in ``premise``), so none is generated for a system.
   239	FURTHER_RULES: tuple[DependencyRule, ...] = (
   240	    _inc(_A.Ax4, _P.P, "X2 + Ax4", (_A.Ax2, _X.X2), "recognition of rule change", core=False),
   241	    _inc(_A.Ax2, _P.J, "X2 + Ax4", (_A.Ax4, _X.X2), "new rules to interpret", core=False),
   242	    _inc(_A.Ax2, _P.I, "X2 + Ax4", (_A.Ax4, _X.X2), "new rules to be made common knowledge",
   243	         core=False),
   244	    _inc(_A.Ax3, _P.P, "precedent (Hart)", (), "interpretation feeds rule change", core=False),
   245	    _inc(_A.Ax4, _P.C, "Ax4 at C's rules", (),
   246	         "an entrant is deterred only once informed of the sanction rule", core=False),
   247	    DependencyRule(frozenset({_P.F, _P.I}), _P.C, "Part V Cor 3.7 conditions",
   248	                   frozenset({_A.Ax1, _A.Ax4, _A.Ax5}),
   249	                   "costly public-good sanctions at large n, no higher-order sanctions",
   250	                   core=False),
   251	)
   252	
   253	D_STAR_KEYS: frozenset[ArcKey] = frozenset(r.key for r in CORE_RULES)
   254	#: D0: the core relations generated by Ax1..Ax6 alone (W -> m for m != W, the OR-hyperarc
   255	#: {I, C} -> J, and I -> F); Part VII Thm 4.3.
   256	D0_KEYS: frozenset[ArcKey] = frozenset(
   257	    r.key for r in CORE_RULES if not any(isinstance(a, IncidenceAxiom) for a in r.requires)
   258	)
   259	
   260	#: The six single arcs named in the original model brief (kept for comparison only).
   261	BRIEF_ARCS: frozenset[ArcKey] = frozenset(
   262	    arc_key(t, h) for t, h in [(_P.W, _P.C), (_P.P, _P.J), (_P.I, _P.P), (_P.J, _P.F),
   263	                               (_P.F, _P.W), (_P.W, _P.I)]
   264	)
   265	
   266	
   267	def rules_holding(
   268	    axioms: Iterable[AnyAxiom], rules: Iterable[DependencyRule] = CORE_RULES
   269	) -> tuple[DependencyRule, ...]:
   270	    """The rules whose premises all hold under ``axioms``."""
   271	    held = frozenset(axioms)
   272	    return tuple(r for r in rules if r.requires <= held)
   273	
   274	
   275	def dependency_graph(axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS) -> dict[Pillar, frozenset[Pillar]]:
   276	    """Underlying digraph of the core rules generated under ``axioms`` (default: all)."""
   277	    return underlying_digraph(rules_holding(axioms))
   278	
   279	
   280	# Governance systems ------------------------------------------------------------------------
   281	
   282	
   283	@dataclass(frozen=True)
   284	class Practice:
   285	    """A regular activity that discharges the problem generated by axiom ``solves``.
   286	
   287	    ``formal`` is True when the activity is attached to a designated office or organization.
   288	    ``source`` holds the citation key(s) supporting the coding.
   289	    """
   290	
   291	    description: str
   292	    solves: Axiom
   293	    holders: frozenset[str]
   294	    formal: bool = False
   295	    source: str = ""
   296	
   297	    def __post_init__(self) -> None:
   298	        if not isinstance(self.solves, Axiom):
   299	            raise TypeError("Practice.solves must be an Axiom")
   300	        holders = frozenset(self.holders)
   301	        if not holders or any(not isinstance(h, str) or not h for h in holders):
   302	            raise ValueError("a practice needs at least one named holder")
   303	        if not self.description.strip():
   304	            raise ValueError("a practice needs a description")
   305	        object.__setattr__(self, "holders", holders)
   306	
   307	    @property
   308	    def pillar(self) -> Pillar:
   309	        return AXIOM_TO_PILLAR[self.solves]
   310	
   311	
   312	@dataclass(frozen=True)
   313	class GovernanceSystem:
   314	    """A collective that makes and enforces collective decisions (KB Section 4.1).
   315	
   316	    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
   317	    over the period studied; it may include the incidence axioms X1, X2, X3, X5. Both are
   318	    coded independently of ``practices``. Dependencies are generated from ``axioms``;
   319	    ``absent_incidences`` records incidences Inc(k, m) OBSERVED not to arise in this system,
   320	    which suppress the arcs they would generate (the route by which a case can falsify D0 or
   321	    interdependence).
   322	    """
   323	
   324	    name: str
   325	    persistent: bool
   326	    axioms: frozenset[AnyAxiom]
   327	    practices: tuple[Practice, ...] = ()
   328	    absent_incidences: frozenset[tuple[Axiom, Pillar]] = frozenset()
   329	    note: str = ""
   330	
   331	    def __post_init__(self) -> None:
   332	        if not isinstance(self.persistent, bool):
   333	            raise TypeError("persistent must be a bool")
   334	        axioms = frozenset(self.axioms)
   335	        if any(not isinstance(a, (Axiom, IncidenceAxiom)) for a in axioms):
   336	            raise TypeError("axioms must be Axiom or IncidenceAxiom members")
   337	        practices = tuple(self.practices)
   338	        if any(not isinstance(p, Practice) for p in practices):
   339	            raise TypeError("practices must be Practice instances")
   340	        object.__setattr__(self, "axioms", axioms)
   341	        object.__setattr__(self, "practices", practices)
   342	        absent = frozenset(tuple(i) for i in self.absent_incidences)
   343	        if any(len(i) != 2 or not isinstance(i[0], Axiom) or not isinstance(i[1], Pillar)
   344	               for i in absent):
   345	            raise TypeError("absent_incidences must be (Axiom, Pillar) pairs")
   346	        object.__setattr__(self, "absent_incidences", absent)
   347	
   348	    def holds(self, axiom: AnyAxiom) -> bool:
   349	        """Predicate for one axiom (Ax1..Ax6 or an incidence axiom X_k)."""
   350	        return axiom in self.axioms
   351	
   352	    @property
   353	    def all_axioms_hold(self) -> bool:
   354	        """Ax1..Ax6 all hold (the antecedent of Theorem A)."""
   355	        return all(self.holds(a) for a in Axiom)
   356	
   357	    @property
   358	    def extended_axioms_hold(self) -> bool:
   359	        """Ax1..Ax6 and X1, X2, X3, X5 all hold (the antecedent of interdependence)."""
   360	        return EXTENDED_AXIOMS <= self.axioms
   361	
   362	
   363	def generate_dependencies(
   364	    system: GovernanceSystem, rules: Iterable[DependencyRule] = CORE_RULES
   365	) -> frozenset[ArcKey]:
   366	    """Hyperarcs generated in ``system``: rules whose premises hold, minus absent incidences."""
   367	    return frozenset(
   368	        r.key for r in rules_holding(system.axioms, rules)
   369	        if r.incidence is None or r.incidence not in system.absent_incidences
   370	    )
   371	
   372	
   373	def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
   374	    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
   375	    roles: dict[str, set[Pillar]] = {}
   376	    for p in system.practices:
   377	        for h in p.holders:
   378	            roles.setdefault(h, set()).add(p.pillar)
   379	    return {h: frozenset(ps) for h, ps in roles.items()}
   380	
   381	
   382	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   383	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   384	
   385	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   386	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   387	    """
   388	    practices = [p for p in system.practices if p.pillar is pillar]
   389	    if not practices:
   390	        return None
   391	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   392	    if not formal_holders:
   393	        return INFORMAL
   394	    formal_roles: dict[str, set[Pillar]] = {}
   395	    for p in system.practices:
   396	        if p.formal:
   397	            for h in p.holders:
   398	                formal_roles.setdefault(h, set()).add(p.pillar)
   399	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   400	        return FUSED
   401	    return FORMAL
   402	
   403	
   404	@dataclass(frozen=True)
   405	class Derivation:
   406	    """Result of the lemma for one axiom: required pillar and its realized form."""
   407	
   408	    axiom: Axiom
   409	    pillar: Pillar
   410	    form: RealizedForm | None
   411	    practices: tuple[Practice, ...]
   412	
   413	    @property
   414	    def realized(self) -> bool:
   415	        return self.form is not None
   416	
   417	
   418	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   419	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   420	
   421	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   422	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   423	    """
   424	    out: dict[Axiom, Derivation] = {}
   425	    for axiom in Axiom:
   426	        if not system.holds(axiom):
   427	            continue
   428	        pillar = AXIOM_TO_PILLAR[axiom]
   429	        out[axiom] = Derivation(
   430	            axiom=axiom,
   431	            pillar=pillar,
   432	            form=realized_form(system, pillar),
   433	            practices=tuple(p for p in system.practices if p.solves is axiom),
   434	        )
   435	    return out
   436	
   437	
   438	# Proposition A and interdependence --------------------------------------------------------
   439	
   440	
   441	@dataclass(frozen=True)
   442	class PropositionAResult:
   443	    """Outcome of checking Proposition A on one coded system (Part VII Thms 4.3 and 5.9).
   444	
   445	    ``struct``: all six pillars realized AND every D0 relation generated (Thm 4.3, from
   446	    Ax1..Ax6). ``interdependent``: all six realized and the generated hypergraph strongly
   447	    connected (underlying digraph) AND cascade-complete (Thm 5.9, from Ax1..Ax6 plus X1, X2,
   448	    X3, X5). ``holds`` is Proposition A in full: struct AND interdependent.
   449	
   450	    ``counterexample``: persistent, the extended axiom set holds, yet ``holds`` is False.
   451	    ``struct_counterexample``: persistent, Ax1..Ax6 hold, yet ``struct`` is False.
   452	    """
   453	
   454	    system: str
   455	    antecedent: bool
   456	    realized: frozenset[Pillar]
   457	    missing: frozenset[Pillar]
   458	    dependencies: frozenset[ArcKey]
   459	    missing_dependencies: frozenset[ArcKey]
   460	    strongly_connected: bool
   461	    cascade_complete: bool
   462	    struct: bool
   463	    interdependence_antecedent: bool
   464	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   465	
   466	    @property
   467	    def interdependent(self) -> bool:
   468	        return not self.missing and self.strongly_connected and self.cascade_complete
   469	
   470	    @property
   471	    def holds(self) -> bool:
   472	        return self.struct and self.interdependent
   473	
   474	    @property
   475	    def struct_counterexample(self) -> bool:
   476	        return self.antecedent and not self.struct
   477	
   478	    @property
   479	    def counterexample(self) -> bool:
   480	        return self.interdependence_antecedent and not self.holds
   481	
   482	
   483	def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
   484	    """Check Proposition A (struct and interdependence) on ``system`` (Part VII; KB 4.3).
   485	
   486	    A D0 relation is demanded when its head and every tail member are realized.
   487	    """
   488	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   489	    deps = generate_dependencies(system)
   490	    needed = frozenset((t, h) for t, h in D0_KEYS if h in realized and t <= realized)
   491	    missing_deps = needed - deps
   492	    return PropositionAResult(
   493	        system=system.name,
   494	        antecedent=system.persistent and system.all_axioms_hold,
   495	        realized=realized,
   496	        missing=frozenset(PILLARS) - realized,
   497	        dependencies=deps,
   498	        missing_dependencies=missing_deps,
   499	        strongly_connected=is_strongly_connected(underlying_digraph(deps), realized),
   500	        cascade_complete=is_cascade_complete(deps, realized),
   501	        struct=realized == frozenset(PILLARS) and not missing_deps,
   502	        interdependence_antecedent=system.persistent and system.extended_axioms_hold,
   503	        derivations=derive_functions(system),
   504	    )
   505	
   506	
   507	def formal_system(
   508	    name: str,
   509	    holders: Mapping[Pillar, Iterable[str]],
   510	    persistent: bool = True,
   511	    source: str = "",
   512	    axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS,
   513	) -> GovernanceSystem:
   514	    """A persistent system whose pillars are held by formal organizations.
   515	
   516	    An actor listed under several pillars is fused. By default the extended axiom set is
   517	    coded as holding: an assumption of the stylized model, not an observation. Used for regime
   518	    profiles and counter-models.
   519	    """
   520	    practices = tuple(
   521	        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
   522	                 frozenset(hs), formal=True, source=source)
   523	        for m, hs in holders.items()
   524	        if hs
   525	    )
   526	    return GovernanceSystem(name, persistent, frozenset(axioms), practices)
   527	
   528	
   529	# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
   530	# Each codes the extended axiom set as holding. The X1, X2, X3, X5 codings are QUALITATIVE
   531	# readings of the ethnography (sources in X_CODING_SOURCES), each open to the falsifier
   532	# stated on IncidenceAxiom.
   533	
   534	
   535	def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
   536	    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)
   537	
   538	
   539	NUER = GovernanceSystem(
   540	    name="Nuer ('ordered anarchy')",
   541	    persistent=True,
   542	    axioms=EXTENDED_AXIOMS,
   543	    practices=(
   544	        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
   545	                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
   546	        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
   547	                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
   548	        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
   549	                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
   550	        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
   551	                  {"prophets", "lineages"}, "evanspritchard1940"),
   552	        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
   553	                  {"agnatic kin"}, "evanspritchard1940"),
   554	        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
   555	                  "evanspritchard1940"),
   556	    ),
   557	    note="no office holds coercive authority; functions exist without separation",
   558	)
   559	
   560	JU_HOANSI = GovernanceSystem(
   561	    name="Ju/'hoansi (!Kung)",
   562	    persistent=True,
   563	    axioms=EXTENDED_AXIOMS,
   564	    practices=(
   565	        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
   566	                  {"hunters", "camp members"}, "lee2013; marshall1976"),
   567	        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
   568	                  {"camp members"}, "lee2013"),
   569	        _informal("disputes talked out with kin mediators", Axiom.Ax3,
   570	                  {"kin mediators"}, "lee1979; wiessner2005"),
   571	        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
   572	                  {"healers", "camp members"}, "marshall1976"),
   573	        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
   574	                  {"camp members"}, "wiessner2005; lee2013"),
   575	        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
   576	    ),
   577	    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
   578	)
   579	
   580	OSTROM_COMMONS = GovernanceSystem(
   581	    name="Ostrom commons (design principles)",
   582	    persistent=True,
   583	    axioms=EXTENDED_AXIOMS,
   584	    practices=(
   585	        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
   586	                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
   587	        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
   588	                  {"appropriators"}, "ostrom1990"),
   589	        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
   590	                  {"appropriators"}, "ostrom1990; cox2010"),
   591	        _informal("shared norms; minimal recognition of rights to organize (DP7)",
   592	                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),
   593	        _informal("monitoring and graduated sanctions by appropriators (DP4, DP5)",
   594	                  Axiom.Ax5, {"appropriators"}, "ostrom1990; cox2010"),
   595	        _informal("appropriation and maintenance labor", Axiom.Ax6, {"appropriators"},
   596	                  "ostrom1990"),
   597	    ),
   598	    note="checks in minimal form; monitors are appropriators or accountable to them",
   599	)
   600	
   601	CONSENSUS_VILLAGE = GovernanceSystem(
   602	    name="Consensus village (stylized)",
   603	    persistent=True,
   604	    axioms=EXTENDED_AXIOMS,
   605	    practices=(
   606	        _informal("household plots; reciprocal labor exchange; sharing norms", Axiom.Ax1,
   607	                  {"households"}, "sahlins1972"),
   608	        _informal("consensus meeting of adults", Axiom.Ax2, {"village meeting"},
   609	                  "clastres1987; boehm1999"),
   610	        _informal("elders mediate disputes", Axiom.Ax3, {"elders"}, "boehm1999"),
   611	        _informal("ritual and myth; moral talk", Axiom.Ax4, {"village meeting", "elders"},
   612	                  "boehm1999"),
   613	        _informal("gossip, shunning, ostracism of would-be dominants", Axiom.Ax5,
   614	                  {"village meeting"}, "boehm1999; woodburn1982"),
   615	        _informal("gardening and household labor", Axiom.Ax6, {"households"},
   616	                  "sahlins1972"),
   617	    ),
   618	    note="stylized composite; reverse dominance hierarchy",
   619	)
   620	
   621	HARD_CASES: tuple[GovernanceSystem, ...] = (NUER, JU_HOANSI, OSTROM_COMMONS, CONSENSUS_VILLAGE)
   622	
   623	_X1, _X2, _X3, _X5 = IncidenceAxiom
   624	#: Qualitative codings of the incidence axioms for the hard cases (Part VII), with sources.
   625	X_CODING_SOURCES: dict[str, dict[IncidenceAxiom, str]] = {
   626	    NUER.name: {
   627	        _X1: "cattle and grazing rights (evanspritchard1940)",
   628	        _X2: "norms adjusted by negotiation among lineages (evanspritchard1940)",
   629	        _X3: "cattle compensation fixed through the leopard-skin chief (evanspritchard1940)",
   630	        _X5: "feud over cattle (evanspritchard1940)",
   631	    },
   632	    JU_HOANSI.name: {
   633	        _X1: "kin-based n!ore rights to territory and water (lee2013)",
   634	        _X2: "camp talk and fission (lee2013)",
   635	        _X3: "disputes over sharing talked out (lee2013; wiessner2005)",
   636	        _X5: "criticism of failures to share (wiessner2005)",
   637	    },
   638	    OSTROM_COMMONS.name: {
   639	        _X1: "boundary and appropriation rules (ostrom1990)",
   640	        _X2: "users modify their rules (ostrom1990)",
   641	        _X3: "conflict-resolution arenas (ostrom1990; cox2010)",
   642	        _X5: "monitoring and graduated sanctions (ostrom1990)",
   643	    },
   644	    CONSENSUS_VILLAGE.name: {
   645	        _X1: "household plots under sharing norms (sahlins1972)",
   646	        _X2: "seasonal re-arrangement (graeber2021)",
   647	        _X3: "elders mediate residual disputes (boehm1999)",
   648	        _X5: "sharing enforced against hoarders (boehm1999)",
   649	    },
   650	}
   651	
   652	
   653	# Axiom independence fixtures (Part VII spec, item 7). ---------------------------------------
   654	
   655	#: Consistency model: the extended axiom set holds and all six pillars are realized (the
   656	#: consensus village coding).
   657	BASELINE_MODEL: GovernanceSystem = CONSENSUS_VILLAGE
   658	
   659	
   660	def without_axiom(axiom: AnyAxiom, base: GovernanceSystem = BASELINE_MODEL) -> GovernanceSystem:
   661	    """``base`` with one axiom removed; for Ax_k the practices solving Ax_k are removed too."""
   662	    practices = base.practices
   663	    if isinstance(axiom, Axiom):
   664	        practices = tuple(p for p in practices if p.solves is not axiom)
   665	    return GovernanceSystem(
   666	        name=f"{base.name} without {axiom.name} ({axiom.label})",
   667	        persistent=base.persistent,
   668	        axioms=base.axioms - {axiom},
   669	        practices=practices,
   670	        absent_incidences=base.absent_incidences,
   671	        note="hypothetical: one axiom removed",
   672	    )
   673	
   674	
   675	#: For each k: persistent, Ax_k removed, pillar k missing. Theorem A's antecedent is false,
   676	#: so none is a counterexample; each shows pillar k is not forced by the other five axioms.
   677	AXIOM_INDEPENDENCE: dict[Axiom, GovernanceSystem] = {a: without_axiom(a) for a in Axiom}
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
   147	        "productive activity uses inputs under conflicting claims, used only under an "
   148	        "anticipable assignment",
   149	        "a persistent collective whose productive inputs never meet conflicting claims",
   150	    ),
   151	    IncidenceAxiom.X2: (
   152	        Axiom.Ax2, Pillar.F,
   153	        "the environment changes infinitely often (Part II Ass 3.2) and each change creates "
   154	        "conflicts no prior settlement procedure can settle",
   155	        "a persistent collective whose prior settlement procedures settle every new conflict",
   156	    ),
   157	    IncidenceAxiom.X3: (
   158	        Axiom.Ax3, Pillar.F,
   159	        "some settlement procedure has open texture and generates infinitely many residual "
   160	        "disputes",
   161	        "settlement procedures that leave only finitely many residual disputes",
   162	    ),
   163	    IncidenceAxiom.X5: (
   164	        Axiom.Ax5, Pillar.F,
   165	        "Ax5 holds for some settlement procedure",
   166	        "no member ever breaks any settlement procedure",
   167	    ),
   168	}
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

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '313,677p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   313	class GovernanceSystem:
   314	    """A collective that makes and enforces collective decisions (KB Section 4.1).
   315	
   316	    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
   317	    over the period studied; it may include the incidence axioms X1, X2, X3, X5. Both are
   318	    coded independently of ``practices``. Dependencies are generated from ``axioms``;
   319	    ``absent_incidences`` records incidences Inc(k, m) OBSERVED not to arise in this system,
   320	    which suppress the arcs they would generate (the route by which a case can falsify D0 or
   321	    interdependence).
   322	    """
   323	
   324	    name: str
   325	    persistent: bool
   326	    axioms: frozenset[AnyAxiom]
   327	    practices: tuple[Practice, ...] = ()
   328	    absent_incidences: frozenset[tuple[Axiom, Pillar]] = frozenset()
   329	    note: str = ""
   330	
   331	    def __post_init__(self) -> None:
   332	        if not isinstance(self.persistent, bool):
   333	            raise TypeError("persistent must be a bool")
   334	        axioms = frozenset(self.axioms)
   335	        if any(not isinstance(a, (Axiom, IncidenceAxiom)) for a in axioms):
   336	            raise TypeError("axioms must be Axiom or IncidenceAxiom members")
   337	        practices = tuple(self.practices)
   338	        if any(not isinstance(p, Practice) for p in practices):
   339	            raise TypeError("practices must be Practice instances")
   340	        object.__setattr__(self, "axioms", axioms)
   341	        object.__setattr__(self, "practices", practices)
   342	        absent = frozenset(tuple(i) for i in self.absent_incidences)
   343	        if any(len(i) != 2 or not isinstance(i[0], Axiom) or not isinstance(i[1], Pillar)
   344	               for i in absent):
   345	            raise TypeError("absent_incidences must be (Axiom, Pillar) pairs")
   346	        object.__setattr__(self, "absent_incidences", absent)
   347	
   348	    def holds(self, axiom: AnyAxiom) -> bool:
   349	        """Predicate for one axiom (Ax1..Ax6 or an incidence axiom X_k)."""
   350	        return axiom in self.axioms
   351	
   352	    @property
   353	    def all_axioms_hold(self) -> bool:
   354	        """Ax1..Ax6 all hold (the antecedent of Theorem A)."""
   355	        return all(self.holds(a) for a in Axiom)
   356	
   357	    @property
   358	    def extended_axioms_hold(self) -> bool:
   359	        """Ax1..Ax6 and X1, X2, X3, X5 all hold (the antecedent of interdependence)."""
   360	        return EXTENDED_AXIOMS <= self.axioms
   361	
   362	
   363	def generate_dependencies(
   364	    system: GovernanceSystem, rules: Iterable[DependencyRule] = CORE_RULES
   365	) -> frozenset[ArcKey]:
   366	    """Hyperarcs generated in ``system``: rules whose premises hold, minus absent incidences."""
   367	    return frozenset(
   368	        r.key for r in rules_holding(system.axioms, rules)
   369	        if r.incidence is None or r.incidence not in system.absent_incidences
   370	    )
   371	
   372	
   373	def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
   374	    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
   375	    roles: dict[str, set[Pillar]] = {}
   376	    for p in system.practices:
   377	        for h in p.holders:
   378	            roles.setdefault(h, set()).add(p.pillar)
   379	    return {h: frozenset(ps) for h, ps in roles.items()}
   380	
   381	
   382	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   383	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   384	
   385	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   386	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   387	    """
   388	    practices = [p for p in system.practices if p.pillar is pillar]
   389	    if not practices:
   390	        return None
   391	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   392	    if not formal_holders:
   393	        return INFORMAL
   394	    formal_roles: dict[str, set[Pillar]] = {}
   395	    for p in system.practices:
   396	        if p.formal:
   397	            for h in p.holders:
   398	                formal_roles.setdefault(h, set()).add(p.pillar)
   399	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   400	        return FUSED
   401	    return FORMAL
   402	
   403	
   404	@dataclass(frozen=True)
   405	class Derivation:
   406	    """Result of the lemma for one axiom: required pillar and its realized form."""
   407	
   408	    axiom: Axiom
   409	    pillar: Pillar
   410	    form: RealizedForm | None
   411	    practices: tuple[Practice, ...]
   412	
   413	    @property
   414	    def realized(self) -> bool:
   415	        return self.form is not None
   416	
   417	
   418	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   419	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   420	
   421	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   422	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   423	    """
   424	    out: dict[Axiom, Derivation] = {}
   425	    for axiom in Axiom:
   426	        if not system.holds(axiom):
   427	            continue
   428	        pillar = AXIOM_TO_PILLAR[axiom]
   429	        out[axiom] = Derivation(
   430	            axiom=axiom,
   431	            pillar=pillar,
   432	            form=realized_form(system, pillar),
   433	            practices=tuple(p for p in system.practices if p.solves is axiom),
   434	        )
   435	    return out
   436	
   437	
   438	# Proposition A and interdependence --------------------------------------------------------
   439	
   440	
   441	@dataclass(frozen=True)
   442	class PropositionAResult:
   443	    """Outcome of checking Proposition A on one coded system (Part VII Thms 4.3 and 5.9).
   444	
   445	    ``struct``: all six pillars realized AND every D0 relation generated (Thm 4.3, from
   446	    Ax1..Ax6). ``interdependent``: all six realized and the generated hypergraph strongly
   447	    connected (underlying digraph) AND cascade-complete (Thm 5.9, from Ax1..Ax6 plus X1, X2,
   448	    X3, X5). ``holds`` is Proposition A in full: struct AND interdependent.
   449	
   450	    ``counterexample``: persistent, the extended axiom set holds, yet ``holds`` is False.
   451	    ``struct_counterexample``: persistent, Ax1..Ax6 hold, yet ``struct`` is False.
   452	    """
   453	
   454	    system: str
   455	    antecedent: bool
   456	    realized: frozenset[Pillar]
   457	    missing: frozenset[Pillar]
   458	    dependencies: frozenset[ArcKey]
   459	    missing_dependencies: frozenset[ArcKey]
   460	    strongly_connected: bool
   461	    cascade_complete: bool
   462	    struct: bool
   463	    interdependence_antecedent: bool
   464	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   465	
   466	    @property
   467	    def interdependent(self) -> bool:
   468	        return not self.missing and self.strongly_connected and self.cascade_complete
   469	
   470	    @property
   471	    def holds(self) -> bool:
   472	        return self.struct and self.interdependent
   473	
   474	    @property
   475	    def struct_counterexample(self) -> bool:
   476	        return self.antecedent and not self.struct
   477	
   478	    @property
   479	    def counterexample(self) -> bool:
   480	        return self.interdependence_antecedent and not self.holds
   481	
   482	
   483	def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
   484	    """Check Proposition A (struct and interdependence) on ``system`` (Part VII; KB 4.3).
   485	
   486	    A D0 relation is demanded when its head and every tail member are realized.
   487	    """
   488	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   489	    deps = generate_dependencies(system)
   490	    needed = frozenset((t, h) for t, h in D0_KEYS if h in realized and t <= realized)
   491	    missing_deps = needed - deps
   492	    return PropositionAResult(
   493	        system=system.name,
   494	        antecedent=system.persistent and system.all_axioms_hold,
   495	        realized=realized,
   496	        missing=frozenset(PILLARS) - realized,
   497	        dependencies=deps,
   498	        missing_dependencies=missing_deps,
   499	        strongly_connected=is_strongly_connected(underlying_digraph(deps), realized),
   500	        cascade_complete=is_cascade_complete(deps, realized),
   501	        struct=realized == frozenset(PILLARS) and not missing_deps,
   502	        interdependence_antecedent=system.persistent and system.extended_axioms_hold,
   503	        derivations=derive_functions(system),
   504	    )
   505	
   506	
   507	def formal_system(
   508	    name: str,
   509	    holders: Mapping[Pillar, Iterable[str]],
   510	    persistent: bool = True,
   511	    source: str = "",
   512	    axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS,
   513	) -> GovernanceSystem:
   514	    """A persistent system whose pillars are held by formal organizations.
   515	
   516	    An actor listed under several pillars is fused. By default the extended axiom set is
   517	    coded as holding: an assumption of the stylized model, not an observation. Used for regime
   518	    profiles and counter-models.
   519	    """
   520	    practices = tuple(
   521	        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
   522	                 frozenset(hs), formal=True, source=source)
   523	        for m, hs in holders.items()
   524	        if hs
   525	    )
   526	    return GovernanceSystem(name, persistent, frozenset(axioms), practices)
   527	
   528	
   529	# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
   530	# Each codes the extended axiom set as holding. The X1, X2, X3, X5 codings are QUALITATIVE
   531	# readings of the ethnography (sources in X_CODING_SOURCES), each open to the falsifier
   532	# stated on IncidenceAxiom.
   533	
   534	
   535	def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
   536	    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)
   537	
   538	
   539	NUER = GovernanceSystem(
   540	    name="Nuer ('ordered anarchy')",
   541	    persistent=True,
   542	    axioms=EXTENDED_AXIOMS,
   543	    practices=(
   544	        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
   545	                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
   546	        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
   547	                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
   548	        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
   549	                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
   550	        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
   551	                  {"prophets", "lineages"}, "evanspritchard1940"),
   552	        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
   553	                  {"agnatic kin"}, "evanspritchard1940"),
   554	        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
   555	                  "evanspritchard1940"),
   556	    ),
   557	    note="no office holds coercive authority; functions exist without separation",
   558	)
   559	
   560	JU_HOANSI = GovernanceSystem(
   561	    name="Ju/'hoansi (!Kung)",
   562	    persistent=True,
   563	    axioms=EXTENDED_AXIOMS,
   564	    practices=(
   565	        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
   566	                  {"hunters", "camp members"}, "lee2013; marshall1976"),
   567	        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
   568	                  {"camp members"}, "lee2013"),
   569	        _informal("disputes talked out with kin mediators", Axiom.Ax3,
   570	                  {"kin mediators"}, "lee1979; wiessner2005"),
   571	        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
   572	                  {"healers", "camp members"}, "marshall1976"),
   573	        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
   574	                  {"camp members"}, "wiessner2005; lee2013"),
   575	        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
   576	    ),
   577	    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
   578	)
   579	
   580	OSTROM_COMMONS = GovernanceSystem(
   581	    name="Ostrom commons (design principles)",
   582	    persistent=True,
   583	    axioms=EXTENDED_AXIOMS,
   584	    practices=(
   585	        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
   586	                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
   587	        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
   588	                  {"appropriators"}, "ostrom1990"),
   589	        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
   590	                  {"appropriators"}, "ostrom1990; cox2010"),
   591	        _informal("shared norms; minimal recognition of rights to organize (DP7)",
   592	                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),
   593	        _informal("monitoring and graduated sanctions by appropriators (DP4, DP5)",
   594	                  Axiom.Ax5, {"appropriators"}, "ostrom1990; cox2010"),
   595	        _informal("appropriation and maintenance labor", Axiom.Ax6, {"appropriators"},
   596	                  "ostrom1990"),
   597	    ),
   598	    note="checks in minimal form; monitors are appropriators or accountable to them",
   599	)
   600	
   601	CONSENSUS_VILLAGE = GovernanceSystem(
   602	    name="Consensus village (stylized)",
   603	    persistent=True,
   604	    axioms=EXTENDED_AXIOMS,
   605	    practices=(
   606	        _informal("household plots; reciprocal labor exchange; sharing norms", Axiom.Ax1,
   607	                  {"households"}, "sahlins1972"),
   608	        _informal("consensus meeting of adults", Axiom.Ax2, {"village meeting"},
   609	                  "clastres1987; boehm1999"),
   610	        _informal("elders mediate disputes", Axiom.Ax3, {"elders"}, "boehm1999"),
   611	        _informal("ritual and myth; moral talk", Axiom.Ax4, {"village meeting", "elders"},
   612	                  "boehm1999"),
   613	        _informal("gossip, shunning, ostracism of would-be dominants", Axiom.Ax5,
   614	                  {"village meeting"}, "boehm1999; woodburn1982"),
   615	        _informal("gardening and household labor", Axiom.Ax6, {"households"},
   616	                  "sahlins1972"),
   617	    ),
   618	    note="stylized composite; reverse dominance hierarchy",
   619	)
   620	
   621	HARD_CASES: tuple[GovernanceSystem, ...] = (NUER, JU_HOANSI, OSTROM_COMMONS, CONSENSUS_VILLAGE)
   622	
   623	_X1, _X2, _X3, _X5 = IncidenceAxiom
   624	#: Qualitative codings of the incidence axioms for the hard cases (Part VII), with sources.
   625	X_CODING_SOURCES: dict[str, dict[IncidenceAxiom, str]] = {
   626	    NUER.name: {
   627	        _X1: "cattle and grazing rights (evanspritchard1940)",
   628	        _X2: "norms adjusted by negotiation among lineages (evanspritchard1940)",
   629	        _X3: "cattle compensation fixed through the leopard-skin chief (evanspritchard1940)",
   630	        _X5: "feud over cattle (evanspritchard1940)",
   631	    },
   632	    JU_HOANSI.name: {
   633	        _X1: "kin-based n!ore rights to territory and water (lee2013)",
   634	        _X2: "camp talk and fission (lee2013)",
   635	        _X3: "disputes over sharing talked out (lee2013; wiessner2005)",
   636	        _X5: "criticism of failures to share (wiessner2005)",
   637	    },
   638	    OSTROM_COMMONS.name: {
   639	        _X1: "boundary and appropriation rules (ostrom1990)",
   640	        _X2: "users modify their rules (ostrom1990)",
   641	        _X3: "conflict-resolution arenas (ostrom1990; cox2010)",
   642	        _X5: "monitoring and graduated sanctions (ostrom1990)",
   643	    },
   644	    CONSENSUS_VILLAGE.name: {
   645	        _X1: "household plots under sharing norms (sahlins1972)",
   646	        _X2: "seasonal re-arrangement (graeber2021)",
   647	        _X3: "elders mediate residual disputes (boehm1999)",
   648	        _X5: "sharing enforced against hoarders (boehm1999)",
   649	    },
   650	}
   651	
   652	
   653	# Axiom independence fixtures (Part VII spec, item 7). ---------------------------------------
   654	
   655	#: Consistency model: the extended axiom set holds and all six pillars are realized (the
   656	#: consensus village coding).
   657	BASELINE_MODEL: GovernanceSystem = CONSENSUS_VILLAGE
   658	
   659	
   660	def without_axiom(axiom: AnyAxiom, base: GovernanceSystem = BASELINE_MODEL) -> GovernanceSystem:
   661	    """``base`` with one axiom removed; for Ax_k the practices solving Ax_k are removed too."""
   662	    practices = base.practices
   663	    if isinstance(axiom, Axiom):
   664	        practices = tuple(p for p in practices if p.solves is not axiom)
   665	    return GovernanceSystem(
   666	        name=f"{base.name} without {axiom.name} ({axiom.label})",
   667	        persistent=base.persistent,
   668	        axioms=base.axioms - {axiom},
   669	        practices=practices,
   670	        absent_incidences=base.absent_incidences,
   671	        note="hypothetical: one axiom removed",
   672	    )
   673	
   674	
   675	#: For each k: persistent, Ax_k removed, pillar k missing. Theorem A's antecedent is false,
   676	#: so none is a counterexample; each shows pillar k is not forced by the other five axioms.
   677	AXIOM_INDEPENDENCE: dict[Axiom, GovernanceSystem] = {a: without_axiom(a) for a in Axiom}

codex
The implementation matches the requested D0/D* sets on inspection. I’m now checking the behavioral edge cases, especially whether “all six realized” accidentally makes empty/partial systems look interconnected and whether every premise-removal claim is genuinely exercised.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider model/tests/test_necessity.py' in /Users/mlong/Documents/Development/the-beast-system
 exited 1 in 195ms:
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

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 pytest -q -s -p no:cacheprovider model/tests/test_necessity.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 245ms:
.................................................
49 passed in 0.04s

hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONPATH=model PYTHONDONTWRITEBYTECODE=1 python -B -c 'from beast_system.necessity import BASELINE_MODEL,EXTENDED_AXIOMS,FURTHER_RULES,generate_dependencies,rules_holding; held=rules_holding(EXTENDED_AXIOMS,FURTHER_RULES); print(len(FURTHER_RULES),len(held),len(generate_dependencies(BASELINE_MODEL,FURTHER_RULES))); print([(sorted(p.name for p in r.tail),r.head.name,r.premise) for r in held])'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 114ms:
6 6 6
[(['I'], 'P', 'X2 + Ax4'), (['P'], 'J', 'X2 + Ax4'), (['P'], 'I', 'X2 + Ax4'), (['J'], 'P', 'precedent (Hart)'), (['I'], 'C', "Ax4 at C's rules"), (['F', 'I'], 'C', 'Part V Cor 3.7 conditions')]

codex
- [P2] [necessity.py:237](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/necessity.py:237): `FURTHER_RULES` are not actually report-only. All six—including `I -> C`—satisfy `EXTENDED_AXIOMS`, so passing them to `rules_holding` or `generate_dependencies` generates every further arc. This contradicts the documented semantics that their extra premises prevent generation.
- [P2] [test_necessity.py:122](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_necessity.py:122): Tests never assert the new `I -> C` further arc or the revised `IncidenceAxiom.statement`/`.falsifier` values. The source test at line 283 only validates parentheses, so placeholder or semantically wrong codings still pass.

VERDICT: NEEDS_FIX
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
37,597
- [P2] [necessity.py:237](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/necessity.py:237): `FURTHER_RULES` are not actually report-only. All six—including `I -> C`—satisfy `EXTENDED_AXIOMS`, so passing them to `rules_holding` or `generate_dependencies` generates every further arc. This contradicts the documented semantics that their extra premises prevent generation.
- [P2] [test_necessity.py:122](/Users/mlong/Documents/Development/the-beast-system/model/tests/test_necessity.py:122): Tests never assert the new `I -> C` further arc or the revised `IncidenceAxiom.statement`/`.falsifier` values. The source test at line 283 only validates parentheses, so placeholder or semantically wrong codings still pass.

VERDICT: NEEDS_FIX
