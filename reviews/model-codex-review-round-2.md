Reading additional input from stdin...
2026-10-22T17:13:43.990204Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a1649a-bb1b-7dd2-8a2a-6807ed0f9651
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

This is review round 2. Round 1 raised: (1) Prop A holds required strong connectivity; (2) dependencies not checked per system; (3) weight sensitivity disconnected from assess(); (4) capture-link endpoints not tied to polity actors, flags not bool-checked; (5) counter-model failed at thresholds (1,1); (6) tolerance could push U above 1; (7) thresholds stored unconverted, simulate lacked finiteness checks. Verify each is fixed and look for anything new.

Review only model/ (beast_system/, tests/, examples/). Do not explore outside model/. Output the findings list and the VERDICT line only.
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T17:13:45.117720Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T17:13:46.063710Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
I’m using the code-review skill to structure a findings-first review. I’ll restrict repository inspection to the specified Python files under `model/` and verify all seven round-one issues against the current code and tests.
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

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg --files model/beast_system model/tests model/examples/run_all.py -g '*.py' | sort" in /Users/mlong/Documents/Development/the-beast-system
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
model/tests/test_capture.py
model/tests/test_dynamics_regimes.py
model/tests/test_indices.py
model/tests/test_necessity.py
model/tests/test_pillars_network.py

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'wc -l model/beast_system/*.py model/tests/*.py model/examples/run_all.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
      48 model/beast_system/__init__.py
     315 model/beast_system/capture.py
     139 model/beast_system/dynamics.py
     261 model/beast_system/indices.py
     502 model/beast_system/necessity.py
     102 model/beast_system/network.py
     105 model/beast_system/pillars.py
     183 model/beast_system/regimes.py
     120 model/tests/test_capture.py
     103 model/tests/test_dynamics_regimes.py
     156 model/tests/test_indices.py
     149 model/tests/test_necessity.py
      67 model/tests/test_pillars_network.py
      84 model/examples/run_all.py
    2334 total

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
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
    56	    total = float(arr.sum())
    57	    if total <= 0.0:
    58	        raise ValueError("at least one control weight must be positive")
    59	    return {k: float(v) / total for k, v in raw.items()}
    60	
    61	
    62	def validate_shares(shares: ShareLike, atol: float = SHARE_ATOL) -> np.ndarray:
    63	    """Check s^m_i >= 0 and sum_i s^m_i = 1 (notation.md 'Control share').
    64	
    65	    Returns the shares renormalized to sum exactly 1, so rounding within ``atol`` cannot push
    66	    H outside [1/n, 1].
    67	    """
    68	    arr = _share_array(shares)
    69	    total = float(arr.sum())
    70	    if abs(total - 1.0) > atol:
    71	        raise ValueError(f"shares must sum to 1, got {total:.12g}")
    72	    return arr / total
    73	
    74	
    75	def hhi(shares: ShareLike) -> float:
    76	    """H_m = sum_i (s^m_i)^2 (source Eq. for H_{m,t}). Lies in [1/n, 1]."""
    77	    arr = validate_shares(shares)
    78	    return float(np.dot(arr, arr))
    79	
    80	
    81	def normalized_hhi(shares: ShareLike) -> float:
    82	    """H* = (H - 1/n) / (1 - 1/n), for comparing polities with different n (KB VII.3 (v)).
    83	
    84	    Not in the source. Defined as 1 for n = 1 (a monopoly by construction).
    85	    """
    86	    arr = validate_shares(shares)
    87	    n = arr.size
    88	    if n == 1:
    89	        return 1.0
    90	    return float((np.dot(arr, arr) - 1.0 / n) / (1.0 - 1.0 / n))
    91	
    92	
    93	def validate_weights(weights: Mapping[Pillar, float] | None) -> dict[Pillar, float]:
    94	    """Check the U weights: one per pillar, w_m >= 0, sum_m w_m = 1 (source Eq. U_t).
    95	
    96	    ``None`` gives equal weights 1/M.
    97	    """
    98	    if weights is None:
    99	        return {m: 1.0 / M for m in PILLARS}
   100	    if set(weights) != set(PILLARS):
   101	        raise ValueError("weights must give exactly one value per pillar")
   102	    w = {m: float(weights[m]) for m in PILLARS}
   103	    if any(not math.isfinite(v) or v < 0.0 for v in w.values()):
   104	        raise ValueError("weights must be finite and non-negative")
   105	    total = sum(w.values())
   106	    if abs(total - 1.0) > WEIGHT_ATOL:
   107	        raise ValueError(f"weights must sum to 1, got {total:.12g}")
   108	    return {m: v / total for m, v in w.items()}
   109	
   110	
   111	def _per_pillar(values: Mapping[Pillar, float], name: str) -> dict[Pillar, float]:
   112	    if set(values) != set(PILLARS):
   113	        raise ValueError(f"{name} must give exactly one value per pillar")
   114	    return {m: validate_unit_interval(values[m], f"{name}[{m.name}]") for m in PILLARS}
   115	
   116	
   117	def unaccountable_concentration(
   118	    H: Mapping[Pillar, float],
   119	    Q: Mapping[Pillar, float],
   120	    weights: Mapping[Pillar, float] | None = None,
   121	) -> float:
   122	    """U = sum_m w_m H_m (1 - Q_m) (source Eq. U_t). Lies in [0, 1].
   123	
   124	    U = 0 iff Q_m = 1 for every m with w_m > 0, because H_m >= 1/n > 0 (KB VII.3 (ii)).
   125	    """
   126	    h = _per_pillar(H, "H")
   127	    if any(v == 0.0 for v in h.values()):
   128	        raise ValueError("H_m >= 1/n > 0 for any valid share vector; got H_m = 0")
   129	    q = _per_pillar(Q, "Q")
   130	    w = validate_weights(weights)
   131	    u = sum(w[m] * h[m] * (1.0 - q[m]) for m in PILLARS)
   132	    return float(min(max(u, 0.0), 1.0))  # guard against last-ulp rounding
   133	
   134	
   135	def validate_integration_matrix(C: np.ndarray, atol: float = 1e-12) -> np.ndarray:
   136	    """Check C is 6x6, finite, symmetric, with off-diagonal C_mn in [0, 1].
   137	
   138	    The diagonal is unused by the integration statistic; by convention it is set to 1.
   139	    """
   140	    arr = np.array(C, dtype=float)
   141	    if arr.shape != (M, M):
   142	        raise ValueError(f"integration matrix must be {M}x{M}, got {arr.shape}")
   143	    if not np.all(np.isfinite(arr)):
   144	        raise ValueError("integration matrix must be finite")
   145	    if not np.allclose(arr, arr.T, atol=atol, rtol=0.0):
   146	        raise ValueError("integration matrix must be symmetric (C_mn = C_nm)")
   147	    off = arr[~np.eye(M, dtype=bool)]
   148	    if off.min() < 0.0 or off.max() > 1.0:
   149	        raise ValueError("off-diagonal C_mn must lie in [0, 1]")
   150	    np.fill_diagonal(arr, 1.0)
   151	    return arr
   152	
   153	
   154	def integration_matrix(
   155	    pairs: Mapping[tuple[Pillar, Pillar], float], default: float = 0.0
   156	) -> np.ndarray:
   157	    """Build a symmetric C from {(m, n): C_mn}; unspecified pairs take ``default``."""
   158	    validate_unit_interval(default, "default")
   159	    arr = np.full((M, M), float(default))
   160	    seen: set[frozenset[Pillar]] = set()
   161	    for (m, n), value in pairs.items():
   162	        if m == n:
   163	            raise ValueError(f"pair ({m.name}, {n.name}) is not a cross-pillar pair")
   164	        key = frozenset((m, n))
   165	        if key in seen:
   166	            raise ValueError(f"pair {m.name}{n.name} given twice")
   167	        seen.add(key)
   168	        v = validate_unit_interval(value, f"C[{m.name}{n.name}]")
   169	        arr[m.position, n.position] = arr[n.position, m.position] = v
   170	    np.fill_diagonal(arr, 1.0)
   171	    return arr
   172	
   173	
   174	def integration_statistic(C: np.ndarray) -> float:
   175	    """I = 2 / (M (M - 1)) sum_{m<n} C_mn with M = 6, i.e. the mean over 15 pairs (source Eq. I_t)."""
   176	    arr = validate_integration_matrix(C)
   177	    total = sum(arr[m.position, n.position] for m, n in PAIRS)
   178	    return float(2.0 / (M * (M - 1)) * total)
   179	
   180	
   181	def coalition_integration(
   182	    shares: Mapping[Pillar, Mapping[str, float]],
   183	    coalition_of: Mapping[str, str] | None = None,
   184	) -> np.ndarray:
   185	    """A formal variant of C_mn: max over coalitions S of min(s^m(S), s^n(S)).
   186	
   187	    The source describes C_mn only verbally ('the same coalition commands appointments,
   188	    budgets, sanctions or agenda in both m and n'); KB VII.3 (iv) asks Part VII to propose a
   189	    definition. Here s^m(S) is the summed share of coalition S in pillar m. Actors absent from
   190	    ``coalition_of`` form singleton coalitions. The result lies in [0, 1] and is weakly
   191	    increasing when a coalition gains share in either pillar.
   192	    """
   193	    coalition_of = dict(coalition_of or {})
   194	    by_pillar: dict[Pillar, dict[str, float]] = {}
   195	    for m in PILLARS:
   196	        if m not in shares:
   197	            raise ValueError(f"shares missing pillar {m.name}")
   198	        s = shares[m]
   199	        validate_shares(s)
   200	        agg: dict[str, float] = {}
   201	        for actor, v in s.items():
   202	            key = coalition_of.get(actor, actor)
   203	            agg[key] = agg.get(key, 0.0) + float(v)
   204	        by_pillar[m] = agg
   205	    arr = np.eye(M)
   206	    for m, n in PAIRS:
   207	        common = by_pillar[m].keys() & by_pillar[n].keys()
   208	        v = max((min(by_pillar[m][k], by_pillar[n][k]) for k in common), default=0.0)
   209	        v = min(max(v, 0.0), 1.0)
   210	        arr[m.position, n.position] = arr[n.position, m.position] = v
   211	    return arr
   212	
   213	
   214	@dataclass(frozen=True)
   215	class WeightSensitivity:
   216	    """Result of ``weight_sensitivity``. ``draws`` holds U for each sampled weight vector."""
   217	
   218	    baseline: float
   219	    vertex_min: float
   220	    vertex_max: float
   221	    draws: np.ndarray
   222	
   223	    @property
   224	    def quantiles(self) -> tuple[float, float]:
   225	        """5th and 95th percentile of U across draws."""
   226	        lo, hi = np.quantile(self.draws, [0.05, 0.95])
   227	        return float(lo), float(hi)
   228	
   229	    def fraction_at_least(self, u_star: float) -> float:
   230	        """Share of weight draws with U >= u_star (robustness of a threshold call)."""
   231	        validate_unit_interval(u_star, "u_star")
   232	        return float(np.mean(self.draws >= u_star))
   233	
   234	
   235	def weight_sensitivity(
   236	    H: Mapping[Pillar, float],
   237	    Q: Mapping[Pillar, float],
   238	    weights: Mapping[Pillar, float] | None = None,
   239	    n_draws: int = 2000,
   240	    seed: int = 0,
   241	) -> WeightSensitivity:
   242	    """Sensitivity of U to the weights w (source: 'weights preregistered; sensitivity analysis').
   243	
   244	    U is linear in w, so over the whole weight simplex its exact range is
   245	    [min_m H_m (1 - Q_m), max_m H_m (1 - Q_m)] (attained at the vertices). ``draws`` samples
   246	    w uniformly on the simplex (Dirichlet(1, ..., 1)) to show the typical spread.
   247	    """
   248	    if n_draws < 1:
   249	        raise ValueError("n_draws must be positive")
   250	    baseline = unaccountable_concentration(H, Q, weights)
   251	    h = _per_pillar(H, "H")
   252	    q = _per_pillar(Q, "Q")
   253	    terms = np.array([h[m] * (1.0 - q[m]) for m in PILLARS])
   254	    rng = np.random.default_rng(seed)
   255	    w = rng.dirichlet(np.ones(M), size=n_draws)
   256	    return WeightSensitivity(
   257	        baseline=baseline,
   258	        vertex_min=float(terms.min()),
   259	        vertex_max=float(terms.max()),
   260	        draws=(w * terms).sum(axis=1),
   261	    )

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '261,540p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   261	    stack = [start]
   262	    while stack:
   263	        for nxt in graph.get(stack.pop(), frozenset()):
   264	            if nxt not in seen:
   265	                seen.add(nxt)
   266	                stack.append(nxt)
   267	    return seen
   268	
   269	
   270	def is_strongly_connected(graph: Graph, nodes: Iterable[Pillar] | None = None) -> bool:
   271	    """True iff every node of the graph is reachable from every other node.
   272	
   273	    ``nodes`` restricts the graph to an induced subgraph (default: all nodes that appear).
   274	    The empty graph is not strongly connected; a single node is.
   275	    """
   276	    keep = set(nodes) if nodes is not None else _nodes(graph)
   277	    if not keep:
   278	        return False
   279	    fwd: dict[Pillar, frozenset[Pillar]] = {
   280	        u: frozenset(v for v in graph.get(u, ()) if v in keep) for u in keep
   281	    }
   282	    rev: dict[Pillar, set[Pillar]] = {u: set() for u in keep}
   283	    for u, vs in fwd.items():
   284	        for v in vs:
   285	            rev[v].add(u)
   286	    start = next(iter(keep))
   287	    rev_f = {u: frozenset(v) for u, v in rev.items()}
   288	    return _reach(fwd, start) == keep and _reach(rev_f, start) == keep
   289	
   290	
   291	def critical_edges(graph: Graph) -> list[tuple[Pillar, Pillar]]:
   292	    """Edges whose single removal breaks strong connectivity (empty if not connected)."""
   293	    nodes = _nodes(graph)
   294	    base = {u: frozenset(graph.get(u, ())) for u in nodes}
   295	    if not is_strongly_connected(base):
   296	        return []
   297	    out = []
   298	    for u in PILLARS:
   299	        for v in sorted(base.get(u, ()), key=lambda p: p.position):
   300	            pruned = dict(base)
   301	            pruned[u] = base[u] - {v}
   302	            if not is_strongly_connected(pruned, nodes):
   303	                out.append((u, v))
   304	    return out
   305	
   306	
   307	def sinks_and_sources(graph: Graph) -> tuple[frozenset[Pillar], frozenset[Pillar]]:
   308	    """Pillars with no outgoing edge (sinks) and with no incoming edge (sources)."""
   309	    nodes = _nodes(graph)
   310	    has_out = {u for u in nodes if any(True for _ in graph.get(u, ()))}
   311	    has_in = {v for u in nodes for v in graph.get(u, ())}
   312	    return frozenset(nodes - has_out), frozenset(nodes - has_in)
   313	
   314	
   315	# Proposition A ----------------------------------------------------------------------------
   316	
   317	
   318	#: Edges claimed necessary for every persistent G (status 'derived').
   319	DERIVED_EDGES: frozenset[tuple[Pillar, Pillar]] = frozenset(
   320	    (d.provider, d.dependent) for d in DEPENDENCIES if d.status == "derived"
   321	)
   322	
   323	
   324	@dataclass(frozen=True)
   325	class PropositionAResult:
   326	    """Outcome of checking Theorem A on one coded system.
   327	
   328	    ``holds`` is the structural predicate Struct(G): all six pillars realized AND every
   329	    required dependency relation coded as present in this system. ``counterexample`` is True
   330	    when the theorem's antecedent holds (persistent, Ax1..Ax6) but Struct(G) fails: a
   331	    falsifier of Theorem A (a missing pillar or a missing required relation).
   332	
   333	    ``strongly_connected`` reports whether the system's coded dependency graph is strongly
   334	    connected on the realized pillars. It does NOT enter ``holds``: strong connectivity is an
   335	    open problem (KB Section 4.3), reported but not assumed.
   336	    """
   337	
   338	    system: str
   339	    antecedent: bool
   340	    realized: frozenset[Pillar]
   341	    missing: frozenset[Pillar]
   342	    missing_dependencies: frozenset[tuple[Pillar, Pillar]]
   343	    strongly_connected: bool
   344	    holds: bool
   345	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   346	
   347	    @property
   348	    def counterexample(self) -> bool:
   349	        return self.antecedent and not self.holds
   350	
   351	
   352	def check_proposition_a(
   353	    system: GovernanceSystem,
   354	    required: Iterable[Dependency] = DEPENDENCIES,
   355	) -> PropositionAResult:
   356	    """Check Theorem A on ``system`` (Part VII Theorem A; KB Section 4.3).
   357	
   358	    Required relations are the 'derived' entries of ``required`` whose two pillars are both
   359	    realized; 'conditional' relations are never required.
   360	    """
   361	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   362	    needed = frozenset(
   363	        (d.provider, d.dependent)
   364	        for d in required
   365	        if d.status == "derived" and d.provider in realized and d.dependent in realized
   366	    )
   367	    coded: dict[Pillar, set[Pillar]] = {m: set() for m in PILLARS}
   368	    for u, v in system.dependencies:
   369	        coded[u].add(v)
   370	    missing_deps = needed - system.dependencies
   371	    return PropositionAResult(
   372	        system=system.name,
   373	        antecedent=system.persistent and system.all_axioms_hold,
   374	        realized=realized,
   375	        missing=frozenset(PILLARS) - realized,
   376	        missing_dependencies=missing_deps,
   377	        strongly_connected=is_strongly_connected(coded, realized),
   378	        holds=realized == frozenset(PILLARS) and not missing_deps,
   379	        derivations=derive_functions(system),
   380	    )
   381	
   382	
   383	def formal_system(
   384	    name: str,
   385	    holders: Mapping[Pillar, Iterable[str]],
   386	    persistent: bool = True,
   387	    source: str = "",
   388	    dependencies: Iterable[tuple[Pillar, Pillar]] = DERIVED_EDGES,
   389	) -> GovernanceSystem:
   390	    """A persistent system satisfying Ax1..Ax6 whose pillars are held by formal organizations.
   391	
   392	    An actor listed under several pillars is fused. By default the derived dependency relations
   393	    are coded as present: an assumption of the stylized model, not an observation. Used for
   394	    regime profiles and counter-models.
   395	    """
   396	    practices = tuple(
   397	        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
   398	                 frozenset(hs), formal=True, source=source)
   399	        for m, hs in holders.items()
   400	        if hs
   401	    )
   402	    return GovernanceSystem(name, persistent, frozenset(Axiom), practices,
   403	                            frozenset(dependencies))
   404	
   405	
   406	# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
   407	
   408	
   409	def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
   410	    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)
   411	
   412	
   413	NUER = GovernanceSystem(
   414	    name="Nuer ('ordered anarchy')",
   415	    persistent=True,
   416	    axioms=frozenset(Axiom),
   417	    practices=(
   418	        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
   419	                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
   420	        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
   421	                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
   422	        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
   423	                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
   424	        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
   425	                  {"prophets", "lineages"}, "evanspritchard1940"),
   426	        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
   427	                  {"agnatic kin"}, "evanspritchard1940"),
   428	        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
   429	                  "evanspritchard1940"),
   430	    ),
   431	    # Derived relations observed in minimal form; J->P: settled-feud precedent alters norms.
   432	    dependencies=DERIVED_EDGES | {(Pillar.J, Pillar.P)},
   433	    note="no office holds coercive authority; functions exist without separation",
   434	)
   435	
   436	JU_HOANSI = GovernanceSystem(
   437	    name="Ju/'hoansi (!Kung)",
   438	    persistent=True,
   439	    axioms=frozenset(Axiom),
   440	    practices=(
   441	        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
   442	                  {"hunters", "camp members"}, "lee2013; marshall1976"),
   443	        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
   444	                  {"camp members"}, "lee2013"),
   445	        _informal("disputes talked out with kin mediators", Axiom.Ax3,
   446	                  {"kin mediators"}, "lee1979; wiessner2005"),
   447	        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
   448	                  {"healers", "camp members"}, "marshall1976"),
   449	        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
   450	                  {"camp members"}, "wiessner2005; lee2013"),
   451	        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
   452	    ),
   453	    # Derived relations only; no specialist office, so no conditional relation is coded.
   454	    dependencies=DERIVED_EDGES,
   455	    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
   456	)
   457	
   458	OSTROM_COMMONS = GovernanceSystem(
   459	    name="Ostrom commons (design principles)",
   460	    persistent=True,
   461	    axioms=frozenset(Axiom),
   462	    practices=(
   463	        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
   464	                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
   465	        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
   466	                  {"appropriators"}, "ostrom1990"),
   467	        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
   468	                  {"appropriators"}, "ostrom1990; cox2010"),
   469	        _informal("shared norms; minimal recognition of rights to organize (DP7)",
   470	                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),
   471	        _informal("monitoring and graduated sanctions by appropriators (DP4, DP5)",
   472	                  Axiom.Ax5, {"appropriators"}, "ostrom1990; cox2010"),
   473	        _informal("appropriation and maintenance labor", Axiom.Ax6, {"appropriators"},
   474	                  "ostrom1990"),
   475	    ),
   476	    # F->C: some commons compensate monitors from the resource (ostrom1990).
   477	    dependencies=DERIVED_EDGES | {(Pillar.F, Pillar.C)},
   478	    note="checks in minimal form; monitors are appropriators or accountable to them",
   479	)
   480	
   481	CONSENSUS_VILLAGE = GovernanceSystem(
   482	    name="Consensus village (stylized)",
   483	    persistent=True,
   484	    axioms=frozenset(Axiom),
   485	    practices=(
   486	        _informal("household plots; reciprocal labor exchange; sharing norms", Axiom.Ax1,
   487	                  {"households"}, "sahlins1972"),
   488	        _informal("consensus meeting of adults", Axiom.Ax2, {"village meeting"},
   489	                  "clastres1987; boehm1999"),
   490	        _informal("elders mediate disputes", Axiom.Ax3, {"elders"}, "boehm1999"),
   491	        _informal("ritual and myth; moral talk", Axiom.Ax4, {"village meeting", "elders"},
   492	                  "boehm1999"),
   493	        _informal("gossip, shunning, ostracism of would-be dominants", Axiom.Ax5,
   494	                  {"village meeting"}, "boehm1999; woodburn1982"),
   495	        _informal("gardening and household labor", Axiom.Ax6, {"households"},
   496	                  "sahlins1972"),
   497	    ),
   498	    dependencies=DERIVED_EDGES,
   499	    note="stylized composite; reverse dominance hierarchy",
   500	)
   501	
   502	HARD_CASES: tuple[GovernanceSystem, ...] = (NUER, JU_HOANSI, OSTROM_COMMONS, CONSENSUS_VILLAGE)

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
   308	    evidenced link. Both pass the Theorem A check (six pillars realized, required relations
   309	    coded). G1 fails B for every thresholds pair because it has no link (and its indices lie
   310	    below any u* > 0.02, i* > 0); G2 meets B for every thresholds pair in [0, 1]^2.
   311	    """
   312	    return CounterModel(
   313	        plural=assess(plural_polity(), thresholds),
   314	        fused=assess(fused_polity(), thresholds),
   315	    )

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '1,260p'" in /Users/mlong/Documents/Development/the-beast-system
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
    18	Each system codes the relations present in it; a persistent system satisfying Ax1..Ax6 that
    19	lacks a derived relation is also reported as a counterexample. Strong connectivity of D is
    20	flagged in KB Section 4.3 as an OPEN problem: it is computed and reported (for the encoded
    21	graph and for each system) but never enters the Theorem A predicate.
    22	"""
    23	
    24	from __future__ import annotations
    25	
    26	from collections.abc import Iterable, Mapping
    27	from dataclasses import dataclass, field
    28	from typing import Literal
    29	
    30	from .pillars import AXIOM_TO_PILLAR, PILLAR_TO_AXIOM, PILLARS, Axiom, Pillar
    31	
    32	RealizedForm = Literal["formal institution", "fused", "informal/minimal"]
    33	FORMAL: RealizedForm = "formal institution"
    34	FUSED: RealizedForm = "fused"
    35	INFORMAL: RealizedForm = "informal/minimal"
    36	
    37	
    38	@dataclass(frozen=True)
    39	class Practice:
    40	    """A regular activity that discharges the problem generated by axiom ``solves``.
    41	
    42	    ``formal`` is True when the activity is attached to a designated office or organization.
    43	    ``source`` holds the citation key(s) supporting the coding.
    44	    """
    45	
    46	    description: str
    47	    solves: Axiom
    48	    holders: frozenset[str]
    49	    formal: bool = False
    50	    source: str = ""
    51	
    52	    def __post_init__(self) -> None:
    53	        if not isinstance(self.solves, Axiom):
    54	            raise TypeError("Practice.solves must be an Axiom")
    55	        holders = frozenset(self.holders)
    56	        if not holders or any(not isinstance(h, str) or not h for h in holders):
    57	            raise ValueError("a practice needs at least one named holder")
    58	        if not self.description.strip():
    59	            raise ValueError("a practice needs a description")
    60	        object.__setattr__(self, "holders", holders)
    61	
    62	    @property
    63	    def pillar(self) -> Pillar:
    64	        return AXIOM_TO_PILLAR[self.solves]
    65	
    66	
    67	@dataclass(frozen=True)
    68	class GovernanceSystem:
    69	    """A collective that makes and enforces collective decisions (KB Section 4.1).
    70	
    71	    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
    72	    over the period studied. Both are coded independently of ``practices``. ``dependencies``
    73	    lists the (provider, dependent) relations coded as present in THIS system; Theorem A is
    74	    checked against them, not against the global encoding.
    75	    """
    76	
    77	    name: str
    78	    persistent: bool
    79	    axioms: frozenset[Axiom]
    80	    practices: tuple[Practice, ...] = ()
    81	    dependencies: frozenset[tuple[Pillar, Pillar]] = frozenset()
    82	    note: str = ""
    83	
    84	    def __post_init__(self) -> None:
    85	        if not isinstance(self.persistent, bool):
    86	            raise TypeError("persistent must be a bool")
    87	        axioms = frozenset(self.axioms)
    88	        if any(not isinstance(a, Axiom) for a in axioms):
    89	            raise TypeError("axioms must be Axiom members")
    90	        practices = tuple(self.practices)
    91	        if any(not isinstance(p, Practice) for p in practices):
    92	            raise TypeError("practices must be Practice instances")
    93	        deps = frozenset(tuple(e) for e in self.dependencies)
    94	        for e in deps:
    95	            if len(e) != 2 or not all(isinstance(m, Pillar) for m in e):
    96	                raise TypeError("dependencies must be (Pillar, Pillar) pairs")
    97	            if e[0] is e[1]:
    98	                raise ValueError(f"self-dependency {e[0].name}->{e[0].name} is not allowed")
    99	        object.__setattr__(self, "axioms", axioms)
   100	        object.__setattr__(self, "practices", practices)
   101	        object.__setattr__(self, "dependencies", deps)
   102	
   103	    def holds(self, axiom: Axiom) -> bool:
   104	        """Predicate for one axiom (Ax1 scarcity, ..., Ax6 maintenance)."""
   105	        return axiom in self.axioms
   106	
   107	    @property
   108	    def all_axioms_hold(self) -> bool:
   109	        return all(self.holds(a) for a in Axiom)
   110	
   111	
   112	def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
   113	    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
   114	    roles: dict[str, set[Pillar]] = {}
   115	    for p in system.practices:
   116	        for h in p.holders:
   117	            roles.setdefault(h, set()).add(p.pillar)
   118	    return {h: frozenset(ps) for h, ps in roles.items()}
   119	
   120	
   121	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   122	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   123	
   124	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   125	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   126	    """
   127	    practices = [p for p in system.practices if p.pillar is pillar]
   128	    if not practices:
   129	        return None
   130	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   131	    if not formal_holders:
   132	        return INFORMAL
   133	    formal_roles: dict[str, set[Pillar]] = {}
   134	    for p in system.practices:
   135	        if p.formal:
   136	            for h in p.holders:
   137	                formal_roles.setdefault(h, set()).add(p.pillar)
   138	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   139	        return FUSED
   140	    return FORMAL
   141	
   142	
   143	@dataclass(frozen=True)
   144	class Derivation:
   145	    """Result of the lemma for one axiom: required pillar and its realized form."""
   146	
   147	    axiom: Axiom
   148	    pillar: Pillar
   149	    form: RealizedForm | None
   150	    practices: tuple[Practice, ...]
   151	
   152	    @property
   153	    def realized(self) -> bool:
   154	        return self.form is not None
   155	
   156	
   157	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   158	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   159	
   160	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   161	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   162	    """
   163	    out: dict[Axiom, Derivation] = {}
   164	    for axiom in Axiom:
   165	        if not system.holds(axiom):
   166	            continue
   167	        pillar = AXIOM_TO_PILLAR[axiom]
   168	        out[axiom] = Derivation(
   169	            axiom=axiom,
   170	            pillar=pillar,
   171	            form=realized_form(system, pillar),
   172	            practices=tuple(p for p in system.practices if p.solves is axiom),
   173	        )
   174	    return out
   175	
   176	
   177	# Dependency graph -------------------------------------------------------------------------
   178	
   179	DependencyStatus = Literal["derived", "conditional"]
   180	Graph = Mapping[Pillar, Iterable[Pillar]]
   181	
   182	
   183	@dataclass(frozen=True)
   184	class Dependency:
   185	    """Edge provider -> dependent: the dependent pillar needs an output of the provider."""
   186	
   187	    provider: Pillar
   188	    dependent: Pillar
   189	    basis: tuple[Axiom, ...]
   190	    status: DependencyStatus
   191	    rationale: str
   192	
   193	
   194	_A = Axiom
   195	_P = Pillar
   196	
   197	#: Encoded dependency relations D (KB Sections 4.3 item 3 and VII.2). The first six entries are
   198	#: the relations listed in the Part VII brief; the remainder come from the KB list.
   199	DEPENDENCIES: tuple[Dependency, ...] = (
   200	    Dependency(_P.W, _P.C, (_A.Ax6, _A.Ax5), "derived",
   201	               "C needs W's resources: sanctioning consumes time and goods someone produces"),
   202	    Dependency(_P.P, _P.J, (_A.Ax2, _A.Ax3), "derived",
   203	               "J needs P's rules: interpretation presupposes rules to interpret"),
   204	    Dependency(_P.I, _P.P, (_A.Ax4, _A.Ax2), "derived",
   205	               "P needs I's legitimacy: rule-making needs a recognized rule of recognition (Hart)"),
   206	    Dependency(_P.J, _P.F, (_A.Ax3, _A.Ax1), "derived",
   207	               "F needs J's enforcement of claims: contested claims on resources need case rulings"),
   208	    Dependency(_P.F, _P.W, (_A.Ax1, _A.Ax6), "derived",
   209	               "W needs F's allocation: producers need allocated inputs and shares"),
   210	    Dependency(_P.W, _P.I, (_A.Ax6, _A.Ax4), "derived",
   211	               "I needs W's surplus: belief maintenance consumes produced resources"),
   212	    Dependency(_P.W, _P.F, (_A.Ax6, _A.Ax1), "derived",
   213	               "production creates the stock that allocation divides"),
   214	    Dependency(_P.C, _P.F, (_A.Ax5, _A.Ax1), "derived",
   215	               "allocation rules are sometimes defected from; sanctions back them"),
   216	    Dependency(_P.C, _P.J, (_A.Ax5, _A.Ax3), "derived",
   217	               "adjudication without enforcement is advice"),
   218	    Dependency(_P.I, _P.J, (_A.Ax4, _A.Ax3), "derived",
   219	               "rulings settle disputes only if recognized as authoritative"),
   220	    Dependency(_P.I, _P.C, (_A.Ax4, _A.Ax5), "derived",
   221	               "a sanction must be recognized as sanction rather than aggression"),
   222	    Dependency(_P.I, _P.W, (_A.Ax4, _A.Ax6), "derived",
   223	               "norms of work and quasi-voluntary compliance (Levi)"),
   224	    Dependency(_P.F, _P.C, (_A.Ax1, _A.Ax5), "conditional",
   225	               "specialized sanction capacity needs provisioning (Tilly, Levi); gossip does not"),
   226	    Dependency(_P.J, _P.P, (_A.Ax3, _A.Ax2), "conditional",
   227	               "precedent feeds rule change; only where rules change through interpretation"),
   228	    Dependency(_P.J, _P.I, (_A.Ax3, _A.Ax4), "conditional",
   229	               "reasoned judgments act as public symbols; needs public adjudication"),
   230	    Dependency(_P.F, _P.I, (_A.Ax1, _A.Ax4), "conditional",
   231	               "funding of ideology producers; needs specialist belief producers"),
   232	    Dependency(_P.P, _P.I, (_A.Ax2, _A.Ax4), "conditional",
   233	               "legislation as a public symbolic act; needs declared rules"),
   234	)
   235	
   236	#: The six relations named in the Part VII brief, on their own.
   237	BRIEF_DEPENDENCIES: tuple[Dependency, ...] = DEPENDENCIES[:6]
   238	
   239	
   240	def dependency_graph(
   241	    include_conditional: bool = True,
   242	    dependencies: Iterable[Dependency] = DEPENDENCIES,
   243	) -> dict[Pillar, frozenset[Pillar]]:
   244	    """Adjacency provider -> set of dependents over all six pillars."""
   245	    adj: dict[Pillar, set[Pillar]] = {m: set() for m in PILLARS}
   246	    for d in dependencies:
   247	        if include_conditional or d.status == "derived":
   248	            adj[d.provider].add(d.dependent)
   249	    return {m: frozenset(v) for m, v in adj.items()}
   250	
   251	
   252	def _nodes(graph: Graph) -> set[Pillar]:
   253	    nodes = set(graph)
   254	    for targets in graph.values():
   255	        nodes.update(targets)
   256	    return nodes
   257	
   258	
   259	def _reach(graph: Mapping[Pillar, frozenset[Pillar]], start: Pillar) -> set[Pillar]:
   260	    seen = {start}

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/indices.py | sed -n '130,290p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   130	    w = validate_weights(weights)
   131	    u = sum(w[m] * h[m] * (1.0 - q[m]) for m in PILLARS)
   132	    return float(min(max(u, 0.0), 1.0))  # guard against last-ulp rounding
   133	
   134	
   135	def validate_integration_matrix(C: np.ndarray, atol: float = 1e-12) -> np.ndarray:
   136	    """Check C is 6x6, finite, symmetric, with off-diagonal C_mn in [0, 1].
   137	
   138	    The diagonal is unused by the integration statistic; by convention it is set to 1.
   139	    """
   140	    arr = np.array(C, dtype=float)
   141	    if arr.shape != (M, M):
   142	        raise ValueError(f"integration matrix must be {M}x{M}, got {arr.shape}")
   143	    if not np.all(np.isfinite(arr)):
   144	        raise ValueError("integration matrix must be finite")
   145	    if not np.allclose(arr, arr.T, atol=atol, rtol=0.0):
   146	        raise ValueError("integration matrix must be symmetric (C_mn = C_nm)")
   147	    off = arr[~np.eye(M, dtype=bool)]
   148	    if off.min() < 0.0 or off.max() > 1.0:
   149	        raise ValueError("off-diagonal C_mn must lie in [0, 1]")
   150	    np.fill_diagonal(arr, 1.0)
   151	    return arr
   152	
   153	
   154	def integration_matrix(
   155	    pairs: Mapping[tuple[Pillar, Pillar], float], default: float = 0.0
   156	) -> np.ndarray:
   157	    """Build a symmetric C from {(m, n): C_mn}; unspecified pairs take ``default``."""
   158	    validate_unit_interval(default, "default")
   159	    arr = np.full((M, M), float(default))
   160	    seen: set[frozenset[Pillar]] = set()
   161	    for (m, n), value in pairs.items():
   162	        if m == n:
   163	            raise ValueError(f"pair ({m.name}, {n.name}) is not a cross-pillar pair")
   164	        key = frozenset((m, n))
   165	        if key in seen:
   166	            raise ValueError(f"pair {m.name}{n.name} given twice")
   167	        seen.add(key)
   168	        v = validate_unit_interval(value, f"C[{m.name}{n.name}]")
   169	        arr[m.position, n.position] = arr[n.position, m.position] = v
   170	    np.fill_diagonal(arr, 1.0)
   171	    return arr
   172	
   173	
   174	def integration_statistic(C: np.ndarray) -> float:
   175	    """I = 2 / (M (M - 1)) sum_{m<n} C_mn with M = 6, i.e. the mean over 15 pairs (source Eq. I_t)."""
   176	    arr = validate_integration_matrix(C)
   177	    total = sum(arr[m.position, n.position] for m, n in PAIRS)
   178	    return float(2.0 / (M * (M - 1)) * total)
   179	
   180	
   181	def coalition_integration(
   182	    shares: Mapping[Pillar, Mapping[str, float]],
   183	    coalition_of: Mapping[str, str] | None = None,
   184	) -> np.ndarray:
   185	    """A formal variant of C_mn: max over coalitions S of min(s^m(S), s^n(S)).
   186	
   187	    The source describes C_mn only verbally ('the same coalition commands appointments,
   188	    budgets, sanctions or agenda in both m and n'); KB VII.3 (iv) asks Part VII to propose a
   189	    definition. Here s^m(S) is the summed share of coalition S in pillar m. Actors absent from
   190	    ``coalition_of`` form singleton coalitions. The result lies in [0, 1] and is weakly
   191	    increasing when a coalition gains share in either pillar.
   192	    """
   193	    coalition_of = dict(coalition_of or {})
   194	    by_pillar: dict[Pillar, dict[str, float]] = {}
   195	    for m in PILLARS:
   196	        if m not in shares:
   197	            raise ValueError(f"shares missing pillar {m.name}")
   198	        s = shares[m]
   199	        validate_shares(s)
   200	        agg: dict[str, float] = {}
   201	        for actor, v in s.items():
   202	            key = coalition_of.get(actor, actor)
   203	            agg[key] = agg.get(key, 0.0) + float(v)
   204	        by_pillar[m] = agg
   205	    arr = np.eye(M)
   206	    for m, n in PAIRS:
   207	        common = by_pillar[m].keys() & by_pillar[n].keys()
   208	        v = max((min(by_pillar[m][k], by_pillar[n][k]) for k in common), default=0.0)
   209	        v = min(max(v, 0.0), 1.0)
   210	        arr[m.position, n.position] = arr[n.position, m.position] = v
   211	    return arr
   212	
   213	
   214	@dataclass(frozen=True)
   215	class WeightSensitivity:
   216	    """Result of ``weight_sensitivity``. ``draws`` holds U for each sampled weight vector."""
   217	
   218	    baseline: float
   219	    vertex_min: float
   220	    vertex_max: float
   221	    draws: np.ndarray
   222	
   223	    @property
   224	    def quantiles(self) -> tuple[float, float]:
   225	        """5th and 95th percentile of U across draws."""
   226	        lo, hi = np.quantile(self.draws, [0.05, 0.95])
   227	        return float(lo), float(hi)
   228	
   229	    def fraction_at_least(self, u_star: float) -> float:
   230	        """Share of weight draws with U >= u_star (robustness of a threshold call)."""
   231	        validate_unit_interval(u_star, "u_star")
   232	        return float(np.mean(self.draws >= u_star))
   233	
   234	
   235	def weight_sensitivity(
   236	    H: Mapping[Pillar, float],
   237	    Q: Mapping[Pillar, float],
   238	    weights: Mapping[Pillar, float] | None = None,
   239	    n_draws: int = 2000,
   240	    seed: int = 0,
   241	) -> WeightSensitivity:
   242	    """Sensitivity of U to the weights w (source: 'weights preregistered; sensitivity analysis').
   243	
   244	    U is linear in w, so over the whole weight simplex its exact range is
   245	    [min_m H_m (1 - Q_m), max_m H_m (1 - Q_m)] (attained at the vertices). ``draws`` samples
   246	    w uniformly on the simplex (Dirichlet(1, ..., 1)) to show the typical spread.
   247	    """
   248	    if n_draws < 1:
   249	        raise ValueError("n_draws must be positive")
   250	    baseline = unaccountable_concentration(H, Q, weights)
   251	    h = _per_pillar(H, "H")
   252	    q = _per_pillar(Q, "Q")
   253	    terms = np.array([h[m] * (1.0 - q[m]) for m in PILLARS])
   254	    rng = np.random.default_rng(seed)
   255	    w = rng.dirichlet(np.ones(M), size=n_draws)
   256	    return WeightSensitivity(
   257	        baseline=baseline,
   258	        vertex_min=float(terms.min()),
   259	        vertex_max=float(terms.max()),
   260	        draws=(w * terms).sum(axis=1),
   261	    )

exec
/usr/local/bin/zsh -lc 'for f in model/beast_system/dynamics.py model/beast_system/regimes.py; do nl -ba "$f"; done' in /Users/mlong/Documents/Development/the-beast-system
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
    78	    if not np.all(np.isfinite(x)):
    79	        raise ValueError("x0 must be finite")
    80	    if D is not None and z is not None and not (np.all(np.isfinite(D)) and np.all(np.isfinite(z))):
    81	        raise ValueError("D and z must be finite")
    82	    noise_sd = float(noise_sd)
    83	    if not np.isfinite(noise_sd) or noise_sd < 0.0:
    84	        raise ValueError("noise_sd must be finite and non-negative")
    85	    rng = np.random.default_rng(seed)
    86	    path = np.empty((steps + 1, M))
    87	    path[0] = x
    88	    for t in range(steps):
    89	        x = B @ x
    90	        if D is not None and z is not None:
    91	            x = x + D @ z[t]
    92	        if noise_sd > 0.0:
    93	            x = x + rng.normal(0.0, noise_sd, size=M)
    94	        path[t + 1] = x
    95	    return path
    96	
    97	
    98	@dataclass(frozen=True)
    99	class FeedbackExample:
   100	    """Two matrices with the same positive links; only the feedback one has negative entries."""
   101	
   102	    B_positive: np.ndarray
   103	    B_feedback: np.ndarray
   104	    rho_positive: float
   105	    rho_feedback: float
   106	
   107	    @property
   108	    def same_positive_links(self) -> bool:
   109	        return bool(np.array_equal(self.B_positive > 0, self.B_feedback > 0))
   110	
   111	
   112	#: Negative feedback entries (provider, dependent) -> weight: coercion erodes legitimacy and
   113	#: depresses productive effort (source Section 5.3, 'legitimacy loss'). Illustrative values.
   114	NEGATIVE_FEEDBACK: Mapping[tuple[Pillar, Pillar], float] = {
   115	    (Pillar.C, Pillar.I): -0.4,
   116	    (Pillar.C, Pillar.W): -0.3,
   117	}
   118	
   119	
   120	def negative_feedback_example(
   121	    weight: float = 0.25,
   122	    self_weight: float = 0.6,
   123	    feedback: Mapping[tuple[Pillar, Pillar], float] = NEGATIVE_FEEDBACK,
   124	) -> FeedbackExample:
   125	    """Positive dependency links do not guarantee persistence (source Section 5.3).
   126	
   127	    With the derived dependency edges at ``weight`` and ``self_weight`` on the diagonal,
   128	    rho > 1. Adding negative feedback on entries that carry no positive link leaves every
   129	    positive link unchanged yet pushes rho below 1, so deviations decay.
   130	    """
   131	    B_pos = dependency_matrix(dependency_graph(include_conditional=False), weight, self_weight)
   132	    B_fb = B_pos.copy()
   133	    for (provider, dependent), w in feedback.items():
   134	        if w >= 0.0:
   135	            raise ValueError("feedback entries must be negative")
   136	        if B_pos[dependent.position, provider.position] != 0.0:
   137	            raise ValueError("feedback must not overwrite a positive link")
   138	        B_fb[dependent.position, provider.position] = w
   139	    return FeedbackExample(B_pos, B_fb, spectral_radius(B_pos), spectral_radius(B_fb))
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
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '1,180p'" in /Users/mlong/Documents/Development/the-beast-system
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
    18	Each system codes the relations present in it; a persistent system satisfying Ax1..Ax6 that
    19	lacks a derived relation is also reported as a counterexample. Strong connectivity of D is
    20	flagged in KB Section 4.3 as an OPEN problem: it is computed and reported (for the encoded
    21	graph and for each system) but never enters the Theorem A predicate.
    22	"""
    23	
    24	from __future__ import annotations
    25	
    26	from collections.abc import Iterable, Mapping
    27	from dataclasses import dataclass, field
    28	from typing import Literal
    29	
    30	from .pillars import AXIOM_TO_PILLAR, PILLAR_TO_AXIOM, PILLARS, Axiom, Pillar
    31	
    32	RealizedForm = Literal["formal institution", "fused", "informal/minimal"]
    33	FORMAL: RealizedForm = "formal institution"
    34	FUSED: RealizedForm = "fused"
    35	INFORMAL: RealizedForm = "informal/minimal"
    36	
    37	
    38	@dataclass(frozen=True)
    39	class Practice:
    40	    """A regular activity that discharges the problem generated by axiom ``solves``.
    41	
    42	    ``formal`` is True when the activity is attached to a designated office or organization.
    43	    ``source`` holds the citation key(s) supporting the coding.
    44	    """
    45	
    46	    description: str
    47	    solves: Axiom
    48	    holders: frozenset[str]
    49	    formal: bool = False
    50	    source: str = ""
    51	
    52	    def __post_init__(self) -> None:
    53	        if not isinstance(self.solves, Axiom):
    54	            raise TypeError("Practice.solves must be an Axiom")
    55	        holders = frozenset(self.holders)
    56	        if not holders or any(not isinstance(h, str) or not h for h in holders):
    57	            raise ValueError("a practice needs at least one named holder")
    58	        if not self.description.strip():
    59	            raise ValueError("a practice needs a description")
    60	        object.__setattr__(self, "holders", holders)
    61	
    62	    @property
    63	    def pillar(self) -> Pillar:
    64	        return AXIOM_TO_PILLAR[self.solves]
    65	
    66	
    67	@dataclass(frozen=True)
    68	class GovernanceSystem:
    69	    """A collective that makes and enforces collective decisions (KB Section 4.1).
    70	
    71	    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
    72	    over the period studied. Both are coded independently of ``practices``. ``dependencies``
    73	    lists the (provider, dependent) relations coded as present in THIS system; Theorem A is
    74	    checked against them, not against the global encoding.
    75	    """
    76	
    77	    name: str
    78	    persistent: bool
    79	    axioms: frozenset[Axiom]
    80	    practices: tuple[Practice, ...] = ()
    81	    dependencies: frozenset[tuple[Pillar, Pillar]] = frozenset()
    82	    note: str = ""
    83	
    84	    def __post_init__(self) -> None:
    85	        if not isinstance(self.persistent, bool):
    86	            raise TypeError("persistent must be a bool")
    87	        axioms = frozenset(self.axioms)
    88	        if any(not isinstance(a, Axiom) for a in axioms):
    89	            raise TypeError("axioms must be Axiom members")
    90	        practices = tuple(self.practices)
    91	        if any(not isinstance(p, Practice) for p in practices):
    92	            raise TypeError("practices must be Practice instances")
    93	        deps = frozenset(tuple(e) for e in self.dependencies)
    94	        for e in deps:
    95	            if len(e) != 2 or not all(isinstance(m, Pillar) for m in e):
    96	                raise TypeError("dependencies must be (Pillar, Pillar) pairs")
    97	            if e[0] is e[1]:
    98	                raise ValueError(f"self-dependency {e[0].name}->{e[0].name} is not allowed")
    99	        object.__setattr__(self, "axioms", axioms)
   100	        object.__setattr__(self, "practices", practices)
   101	        object.__setattr__(self, "dependencies", deps)
   102	
   103	    def holds(self, axiom: Axiom) -> bool:
   104	        """Predicate for one axiom (Ax1 scarcity, ..., Ax6 maintenance)."""
   105	        return axiom in self.axioms
   106	
   107	    @property
   108	    def all_axioms_hold(self) -> bool:
   109	        return all(self.holds(a) for a in Axiom)
   110	
   111	
   112	def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
   113	    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
   114	    roles: dict[str, set[Pillar]] = {}
   115	    for p in system.practices:
   116	        for h in p.holders:
   117	            roles.setdefault(h, set()).add(p.pillar)
   118	    return {h: frozenset(ps) for h, ps in roles.items()}
   119	
   120	
   121	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   122	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   123	
   124	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   125	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   126	    """
   127	    practices = [p for p in system.practices if p.pillar is pillar]
   128	    if not practices:
   129	        return None
   130	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   131	    if not formal_holders:
   132	        return INFORMAL
   133	    formal_roles: dict[str, set[Pillar]] = {}
   134	    for p in system.practices:
   135	        if p.formal:
   136	            for h in p.holders:
   137	                formal_roles.setdefault(h, set()).add(p.pillar)
   138	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   139	        return FUSED
   140	    return FORMAL
   141	
   142	
   143	@dataclass(frozen=True)
   144	class Derivation:
   145	    """Result of the lemma for one axiom: required pillar and its realized form."""
   146	
   147	    axiom: Axiom
   148	    pillar: Pillar
   149	    form: RealizedForm | None
   150	    practices: tuple[Practice, ...]
   151	
   152	    @property
   153	    def realized(self) -> bool:
   154	        return self.form is not None
   155	
   156	
   157	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   158	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   159	
   160	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   161	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   162	    """
   163	    out: dict[Axiom, Derivation] = {}
   164	    for axiom in Axiom:
   165	        if not system.holds(axiom):
   166	            continue
   167	        pillar = AXIOM_TO_PILLAR[axiom]
   168	        out[axiom] = Derivation(
   169	            axiom=axiom,
   170	            pillar=pillar,
   171	            form=realized_form(system, pillar),
   172	            practices=tuple(p for p in system.practices if p.solves is axiom),
   173	        )
   174	    return out
   175	
   176	
   177	# Dependency graph -------------------------------------------------------------------------
   178	
   179	DependencyStatus = Literal["derived", "conditional"]
   180	Graph = Mapping[Pillar, Iterable[Pillar]]

exec
/usr/local/bin/zsh -lc 'for f in model/beast_system/network.py model/beast_system/pillars.py model/beast_system/__init__.py; do nl -ba "$f"; done' in /Users/mlong/Documents/Development/the-beast-system
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

codex
The seven round-one areas now have corresponding implementation changes: strong connectivity is reported separately, dependencies are stored per system, sensitivity is attached to `assess()`, link endpoints/flags are validated, the fused countermodel reaches `(U, I) = (1, 1)`, index inputs are normalized/clamped safely, and dynamics inputs are checked for finiteness. I’m now checking whether the tests actually lock those fixes down and whether their interaction introduced any new correctness gaps.
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_necessity.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	import pytest
     2	
     3	from beast_system.necessity import (
     4	    BRIEF_DEPENDENCIES,
     5	    DERIVED_EDGES,
     6	    NUER,
     7	    DEPENDENCIES,
     8	    FORMAL,
     9	    FUSED,
    10	    HARD_CASES,
    11	    INFORMAL,
    12	    JU_HOANSI,
    13	    GovernanceSystem,
    14	    Practice,
    15	    check_proposition_a,
    16	    critical_edges,
    17	    dependency_graph,
    18	    derive_functions,
    19	    formal_system,
    20	    is_strongly_connected,
    21	    role_map,
    22	    sinks_and_sources,
    23	)
    24	from beast_system.pillars import PILLARS, Axiom, Pillar
    25	
    26	F, P, J, I, C, W = PILLARS
    27	
    28	
    29	@pytest.mark.parametrize("system", HARD_CASES, ids=lambda s: s.name)
    30	def test_theorem_a_on_hard_cases(system):
    31	    result = check_proposition_a(system)
    32	    assert result.antecedent
    33	    assert result.holds and not result.counterexample
    34	    assert result.realized == frozenset(PILLARS)
    35	    derivs = derive_functions(system)
    36	    assert {d.pillar for d in derivs.values()} == set(PILLARS)
    37	    assert all(d.form == INFORMAL for d in derivs.values())
    38	
    39	
    40	def test_role_map_is_derived_from_practices():
    41	    roles = role_map(JU_HOANSI)
    42	    assert Pillar.C in roles["camp members"] and Pillar.P in roles["camp members"]
    43	
    44	
    45	def test_missing_axiom_drops_pillar_and_is_not_a_counterexample():
    46	    # A perfectly cooperative collective: Ax5 fails and there is no sanction practice.
    47	    practices = tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5)
    48	    system = GovernanceSystem("no defection", True, frozenset(Axiom) - {Axiom.Ax5}, practices)
    49	    derivs = derive_functions(system)
    50	    assert Axiom.Ax5 not in derivs and len(derivs) == 5
    51	    result = check_proposition_a(system)
    52	    assert not result.antecedent
    53	    assert result.missing == {C}
    54	    assert not result.holds and not result.counterexample
    55	
    56	
    57	def test_falsifier_is_reported():
    58	    # All axioms coded as holding, persistent, but no sanction practice: a counterexample.
    59	    practices = tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5)
    60	    system = GovernanceSystem("hypothetical", True, frozenset(Axiom), practices)
    61	    result = check_proposition_a(system)
    62	    assert result.counterexample
    63	    assert derive_functions(system)[Axiom.Ax5].form is None
    64	
    65	
    66	def test_non_persistent_system_does_not_trigger_theorem():
    67	    system = GovernanceSystem("short-lived", False, frozenset(Axiom), ())
    68	    assert not check_proposition_a(system).antecedent
    69	    assert not check_proposition_a(system).counterexample
    70	
    71	
    72	def test_fused_and_formal_forms():
    73	    system = formal_system("toy", {F: ["Treasury"], P: ["Crown"], J: ["Crown"], I: ["Church"],
    74	                                   C: ["Crown"], W: ["Peasants"]})
    75	    derivs = derive_functions(system)
    76	    assert derivs[Axiom.Ax2].form == FUSED
    77	    assert derivs[Axiom.Ax5].form == FUSED
    78	    assert derivs[Axiom.Ax1].form == FORMAL
    79	    assert check_proposition_a(system).holds
    80	
    81	
    82	def test_practice_validation():
    83	    with pytest.raises(ValueError):
    84	        Practice("x", Axiom.Ax1, frozenset())
    85	    with pytest.raises(TypeError):
    86	        Practice("x", Pillar.F, frozenset({"a"}))  # type: ignore[arg-type]
    87	
    88	
    89	def test_dependency_edges_are_documented():
    90	    for d in DEPENDENCIES:
    91	        assert d.provider is not d.dependent
    92	        assert d.rationale and len(d.basis) == 2
    93	        assert d.status in {"derived", "conditional"}
    94	    pairs = [(d.provider, d.dependent) for d in DEPENDENCIES]
    95	    assert len(pairs) == len(set(pairs))
    96	    brief = {(d.provider, d.dependent) for d in BRIEF_DEPENDENCIES}
    97	    assert brief == {(W, C), (P, J), (I, P), (J, F), (F, W), (W, I)}
    98	
    99	
   100	def test_encoded_dependency_graph_strong_connectivity():
   101	    assert is_strongly_connected(dependency_graph(include_conditional=False))
   102	    assert is_strongly_connected(dependency_graph(include_conditional=True))
   103	
   104	
   105	def test_brief_relations_alone_are_not_strongly_connected():
   106	    brief = dependency_graph(dependencies=BRIEF_DEPENDENCIES)
   107	    assert not is_strongly_connected(brief)
   108	    sinks, sources = sinks_and_sources(brief)
   109	    assert sinks == {C} and not sources
   110	
   111	
   112	def test_critical_edges_of_derived_graph():
   113	    crit = critical_edges(dependency_graph(include_conditional=False))
   114	    assert set(crit) == {(F, W), (P, J), (J, F), (I, P), (W, I)}
   115	    assert critical_edges(dependency_graph(include_conditional=True)) == []
   116	
   117	
   118	def test_strong_connectivity_small_cases():
   119	    assert not is_strongly_connected({})
   120	    assert is_strongly_connected({F: set()})
   121	    assert is_strongly_connected({F: {P}, P: {F}})
   122	    assert not is_strongly_connected({F: {P}, P: set()})
   123	    assert is_strongly_connected({F: {P}, P: {F, J}}, nodes={F, P})
   124	
   125	
   126	def test_missing_required_dependency_is_a_counterexample():
   127	    system = GovernanceSystem("no W->C", True, frozenset(Axiom), JU_HOANSI.practices,
   128	                              DERIVED_EDGES - {(W, C)})
   129	    result = check_proposition_a(system)
   130	    assert result.realized == frozenset(PILLARS)
   131	    assert result.missing_dependencies == {(W, C)}
   132	    assert result.counterexample
   133	
   134	
   135	def test_dependencies_are_coded_per_system():
   136	    assert (J, P) in NUER.dependencies and (J, P) not in JU_HOANSI.dependencies
   137	    assert check_proposition_a(NUER).holds and check_proposition_a(JU_HOANSI).holds
   138	    with pytest.raises(ValueError):
   139	        GovernanceSystem("loop", True, frozenset(Axiom), (), frozenset({(F, F)}))
   140	
   141	
   142	def test_strong_connectivity_is_reported_not_required():
   143	    # Theorem A required with only the brief's six relations: they are not strongly
   144	    # connected (C is a sink), yet A holds because connectivity is not part of the predicate.
   145	    edges = frozenset((d.provider, d.dependent) for d in BRIEF_DEPENDENCIES)
   146	    system = GovernanceSystem("brief only", True, frozenset(Axiom), JU_HOANSI.practices, edges)
   147	    result = check_proposition_a(system, required=BRIEF_DEPENDENCIES)
   148	    assert result.holds and not result.strongly_connected
   149	    assert check_proposition_a(NUER).strongly_connected

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

exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_capture.py' in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc 'for f in model/tests/test_dynamics_regimes.py model/tests/test_pillars_network.py model/examples/run_all.py; do nl -ba "$f"; done' in /Users/mlong/Documents/Development/the-beast-system
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
    67	    assert not cm.plural.prop_b.holds and cm.fused.prop_b.holds
    68	    assert cm.demonstrates_non_implication
    69	
    70	
    71	def test_counter_model_index_values():
    72	    g1, g2 = plural_polity(), fused_polity()
    73	    assert g1.U == pytest.approx(0.2 * 0.1)
    74	    assert g1.I == 0.0
    75	    assert g2.U == 1.0
    76	    assert g2.I == 1.0
    77	    assert all(h == pytest.approx(1.0) for h in g2.H.values())
    78	
    79	
    80	def test_counter_model_robust_to_thresholds():
    81	    for u_star, i_star in [(0.0, 0.0), (0.1, 0.1), (0.5, 0.5), (0.9, 0.9), (1.0, 1.0), (0.0, 1.0)]:
    82	        assert a_does_not_imply_b(CaptureThresholds(u_star, i_star)).demonstrates_non_implication
    83	
    84	
    85	def test_capture_link_flags_must_be_bool():
    86	    with pytest.raises(TypeError):
    87	        CaptureLink("a", "b", Pillar.J, "yes", True, False)  # type: ignore[arg-type]
    88	
    89	
    90	def _toy_polity(links=()):
    91	    holders = {m: ["state", "society"] for m in PILLARS}
    92	    return Polity(
    93	        name="toy",
    94	        system=formal_system("toy", holders),
    95	        shares={m: {"state": 1, "society": 1} for m in PILLARS},
    96	        contestability={m: 0.5 for m in PILLARS},
    97	        integration=integration_matrix({}, default=0.3),
    98	        capture_links=tuple(links),
    99	    )
   100	
   101	
   102	def test_capture_link_endpoints_must_be_polity_actors():
   103	    _toy_polity([CaptureLink("state", "society", Pillar.P, True, True, True, "record")])
   104	    with pytest.raises(ValueError):
   105	        _toy_polity([CaptureLink("invented", "society", Pillar.P, True, True, True, "record")])
   106	
   107	
   108	def test_thresholds_are_stored_as_floats_and_typed():
   109	    th = CaptureThresholds(u_star=np.float32(0.25), i_star=1)
   110	    assert type(th.u_star) is float and th.i_star == 1.0
   111	    with pytest.raises(TypeError):
   112	        CaptureThresholds(u_star="0.4")  # type: ignore[arg-type]
   113	
   114	
   115	def test_assess_reports_weight_sensitivity():
   116	    a = assess(_toy_polity())
   117	    assert a.sensitivity.vertex_min <= a.U <= a.sensitivity.vertex_max
   118	    assert 0.0 <= a.u_high_fraction <= 1.0
   119	    cm = a_does_not_imply_b()
   120	    assert cm.fused.u_high_fraction == 1.0 and cm.plural.u_high_fraction == 0.0

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
    37	            f"{_yn(b.thresholds_met):<6}  {a.u_high_fraction:.2f}  {b.n_links}  {_yn(b.holds)}")
    38	
    39	
    40	def main() -> None:
    41	    th = CaptureThresholds()
    42	    head_h = " ".join(f"H_{m.name:<3}" for m in PILLARS)
    43	    header = (f"{'profile':<58} {head_h} U      I      A    U,I>=*  P(U>=u*)  L  B")
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
    55	    print("P(U>=u*) = share of 2000 uniform weight draws with U >= u* (weight sensitivity).")
    56	    print("L = evidenced capture links; regime profiles carry none, so B never holds for them.")
    57	
    58	    print("\nHard cases (Theorem A check):")
    59	    for sys_ in HARD_CASES:
    60	        r = check_proposition_a(sys_)
    61	        forms = ", ".join(f"{d.pillar.name}:{d.form}" for d in r.derivations.values())
    62	        print(f"  {sys_.name:<36} A={_yn(r.holds)} counterexample={_yn(r.counterexample)} "
    63	              f"deps strongly connected={_yn(r.strongly_connected)}  {forms}")
    64	
    65	    derived = dependency_graph(include_conditional=False)
    66	    full = dependency_graph(include_conditional=True)
    67	    brief = dependency_graph(dependencies=BRIEF_DEPENDENCIES)
    68	    print("\nDependency graph (provider -> dependent):")
    69	    print(f"  derived edges only: strongly connected = {is_strongly_connected(derived)}; "
    70	          "critical edges = "
    71	          + ", ".join(f"{u.name}->{v.name}" for u, v in critical_edges(derived)))
    72	    print(f"  derived + conditional: strongly connected = {is_strongly_connected(full)}")
    73	    sinks, _ = sinks_and_sources(brief)
    74	    print(f"  six brief relations alone: strongly connected = {is_strongly_connected(brief)}; "
    75	          f"sinks = {sorted(m.name for m in sinks)}")
    76	
    77	    fb = negative_feedback_example()
    78	    print("\nDynamics: same positive links, rho(B+) = "
    79	          f"{fb.rho_positive:.3f} (persists), rho(B+ with negative feedback) = "
    80	          f"{fb.rho_feedback:.3f} (decays); same positive links = {fb.same_positive_links}")
    81	
    82	
    83	if __name__ == "__main__":
    84	    main()

hook: PreToolUse
hook: PreToolUse Completed
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

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONPATH=model PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -c /dev/null -p no:cacheprovider model/tests' in /Users/mlong/Documents/Development/the-beast-system
 exited 1 in 238ms:
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

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'PYTHONPATH=model PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -s -c /dev/null -p no:cacheprovider model/tests' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 376ms:
.............................................................................
77 passed in 0.17s

hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONPATH=model PYTHONDONTWRITEBYTECODE=1 python -c 'import warnings,numpy as np; from beast_system.indices import control_shares; from beast_system.dynamics import deviation_persists,simulate; warnings.simplefilter(\"ignore\"); print(\"shares\",control_shares({\"a\":1e308,\"b\":1e308})); B=np.diag([2.0,0.5,0,0,0,0]); x0=np.array([0,1,0,0,0,0],dtype=float); print(\"predicate\",deviation_persists(B),\"trajectory_norm\",np.linalg.norm(simulate(B,x0,10)[-1]))'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 121ms:
shares {'a': 0.0, 'b': 0.0}
predicate True trajectory_norm 0.0009765625

codex
- **Medium — `model/beast_system/dynamics.py:3-7,35-37`:** `deviation_persists()` incorrectly claims every deviation persists whenever `rho(B) >= 1`. A matrix can have an unstable eigenvalue while a particular initial deviation lies entirely in a stable subspace and decays. This predicate should describe failure of global asymptotic stability, or accept the deviation being assessed.

- **Medium — `model/beast_system/indices.py:53-59`:** `control_shares()` can violate its defining invariant for large finite inputs. For example, `{a: 1e308, b: 1e308}` makes the NumPy sum overflow to infinity and returns both shares as zero. Normalize using a scale-resistant calculation and add an overflow regression test.

VERDICT: NEEDS_FIX
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
54,603
- **Medium — `model/beast_system/dynamics.py:3-7,35-37`:** `deviation_persists()` incorrectly claims every deviation persists whenever `rho(B) >= 1`. A matrix can have an unstable eigenvalue while a particular initial deviation lies entirely in a stable subspace and decays. This predicate should describe failure of global asymptotic stability, or accept the deviation being assessed.

- **Medium — `model/beast_system/indices.py:53-59`:** `control_shares()` can violate its defining invariant for large finite inputs. For example, `{a: 1e308, b: 1e308}` makes the NumPy sum overflow to infinity and returns both shares as zero. Normalize using a scale-resistant calculation and add an overflow regression test.

VERDICT: NEEDS_FIX
