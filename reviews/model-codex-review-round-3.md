Reading additional input from stdin...
2026-10-22T17:24:38.338953Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a164a4-b791-7ae3-bd92-d69952aa9f52
--------
user
Review only model/ (beast_system/, tests/, examples/). Do not explore outside model/. Output the findings list and the VERDICT line only.

Definitions the code must implement (Largo 2026 source objects plus the Part VII spec):
- Pillars M = {F, P, J, I, C, W}, M = 6, 15 pairs. Multiplex network with weights a^m_ij in [0,1]; many-to-many role map.
- Shares s^m_i >= 0 summing to 1; H_m = sum_i s^2 (monopoly 1, uniform 1/n); Q_m in [0,1]; U = sum_m w_m H_m (1 - Q_m), w >= 0, sum w = 1, with weight-sensitivity analysis; C_mn in [0,1] symmetric; I = 2/(M(M-1)) sum_{m<n} C_mn. Degree decomposition I = (sum_m deg_m)/30, deg_m = sum_{n!=m} C_mn. Hub bound: if C_mn = 0 whenever both m,n lie outside a set of k pillars, I <= (k(6-k) + k(k-1)/2)/15. Coalition overlap C_mn = max_S min(kappa_m(S), kappa_n(S)), additive kappa as special case.
- Capture link needs all of: privileged access; weakens accountability; material evidence. Proposition B: U >= u* AND I >= i* AND >= 1 capture link. a_does_not_imply_b(): two systems that both satisfy A, only one satisfies B.
- Dependencies: AND/OR hypergraph, hyperarc (T, h) provider(s) -> dependent, h needs AT LEAST ONE member of T. D0 (unconditional): W->F, W->P, W->J, W->I, W->C, ({I,C} -> J). Conditional: K_C ({F,I}->C); K_F C->F; K_P P->J, P->I, I->P; K_J J->F; K_W F->W. Underlying digraph replaces (T,h) by t->h. Cascade closure cl(S): least superset of S with T subset cl(S) => h in cl(S). Required results: D0 underlying not strongly connected; D0+K_P+K_J+K_W underlying strongly connected, cl({n}) = M for n != C and cl({C}) = {C}; adding K_F gives cascade completeness; splitting the OR-hyperarc into C->J, I->J would put J in cl({C}).
- Proposition A check: A.holds = all six pillars realized (from coded practices) AND D0 relations coded present in the system. Strong connectivity and cascade completeness are reported only. A persistent system satisfying Ax1..Ax6 failing A is reported as a counterexample. Axiom-independence fixtures: for each k, Ax_k dropped and pillar k missing (antecedent false, not a counterexample), plus a consistent baseline.
- Linear dynamics x_{t+1} = B x_t + D z_t + eps; rho(B) >= 1 means some deviation does not decay; positive links do not guarantee persistence (negative-feedback example).
- Coalition conversion: y, delta in [0,1]^6; K >= 0, zero diagonal, row sums <= 1, K[n,m] = eta[n,m](1 - Q_n); T(y) = (1-delta)y + (1-y)(K y); A = diag(1-delta) + K. Claims: T maps [0,1]^6 into itself; T(y) <= A y; rho(A) < 1 => y_t -> 0; Q_n = 1, delta_n > 0 => y_n,t <= (1-delta_n)^t y_n,0 and coalition integration share asymptotically <= 10/15; rho(A) nonincreasing in each Q_n; K irreducible, max delta < 1, rho(A) > 1 => v.y_t >= min(v.y_0, (1 - max delta)(rho-1)/(2c)), v left Perron vector, c = v_max kappa / v_min^2, kappa = max column sum of K.
- Regime profiles are illustrative assumptions, not measurements; none may imply a religion is inherently captured.

Review for: correctness against these definitions, validation gaps, test coverage of each claim, whether necessity / A-not-implies-B / cascade / foothold code demonstrates what it claims, numerical issues, idiomatic style. This is round 3; round 2 raised (a) deviation_persists overclaimed for rho >= 1, (b) control_shares overflow for huge weights; verify fixed. List issues with file:line. End with VERDICT: PASS or VERDICT: NEEDS_FIX.
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T17:24:39.720477Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T17:24:40.414066Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
warning: Exceeded skills context budget of 2%. All skill descriptions were removed and 107 additional skills were not included in the model-visible skills list.
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
2026-10-22T17:24:46.647638Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
I’ll confine inspection to `model/beast_system`, `model/tests`, and `model/examples`, then return only concrete findings and the verdict. I’m using the code-review skill because this is an adversarial, source-grounded review.
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

2026-10-22T17:24:52.002185Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'rg --files model/beast_system model/tests model/examples' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
model/beast_system/dynamics.py
model/beast_system/pillars.py
model/beast_system/indices.py
model/beast_system/network.py
model/tests/test_necessity.py
model/beast_system/capture.py
model/tests/test_capture.py
model/beast_system/necessity.py
model/tests/test_dynamics_regimes.py
model/beast_system/__init__.py
model/tests/test_pillars_network.py
model/beast_system/regimes.py
model/tests/test_indices.py
model/examples/run_all.py
model/tests/test_conversion.py

2026-10-22T17:24:55.080315Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'for f in $(rg --files model/beast_system model/tests model/examples | sort); do wc -l "$f"; done' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
      53 model/beast_system/__init__.py
     315 model/beast_system/capture.py
     258 model/beast_system/dynamics.py
     281 model/beast_system/indices.py
     565 model/beast_system/necessity.py
     102 model/beast_system/network.py
     105 model/beast_system/pillars.py
     183 model/beast_system/regimes.py
     100 model/examples/run_all.py
     120 model/tests/test_capture.py
      96 model/tests/test_conversion.py
     103 model/tests/test_dynamics_regimes.py
     180 model/tests/test_indices.py
     209 model/tests/test_necessity.py
      67 model/tests/test_pillars_network.py

2026-10-22T17:24:57.154203Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/indices.py; nl -ba model/tests/test_indices.py' in /Users/mlong/Documents/Development/the-beast-system
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
   152	    np.fill_diagonal(arr, 1.0)
   153	    return arr
   154	
   155	
   156	def integration_matrix(
   157	    pairs: Mapping[tuple[Pillar, Pillar], float], default: float = 0.0
   158	) -> np.ndarray:
   159	    """Build a symmetric C from {(m, n): C_mn}; unspecified pairs take ``default``."""
   160	    validate_unit_interval(default, "default")
   161	    arr = np.full((M, M), float(default))
   162	    seen: set[frozenset[Pillar]] = set()
   163	    for (m, n), value in pairs.items():
   164	        if m == n:
   165	            raise ValueError(f"pair ({m.name}, {n.name}) is not a cross-pillar pair")
   166	        key = frozenset((m, n))
   167	        if key in seen:
   168	            raise ValueError(f"pair {m.name}{n.name} given twice")
   169	        seen.add(key)
   170	        v = validate_unit_interval(value, f"C[{m.name}{n.name}]")
   171	        arr[m.position, n.position] = arr[n.position, m.position] = v
   172	    np.fill_diagonal(arr, 1.0)
   173	    return arr
   174	
   175	
   176	def integration_statistic(C: np.ndarray) -> float:
   177	    """I = 2 / (M (M - 1)) sum_{m<n} C_mn with M = 6, i.e. the mean over 15 pairs (source Eq. I_t)."""
   178	    arr = validate_integration_matrix(C)
   179	    total = sum(arr[m.position, n.position] for m, n in PAIRS)
   180	    return float(2.0 / (M * (M - 1)) * total)
   181	
   182	
   183	def integration_degrees(C: np.ndarray) -> dict[Pillar, float]:
   184	    """deg_m = sum_{n != m} C_mn, so that I = (sum_m deg_m) / 30 (Part VII spec, item 5)."""
   185	    arr = validate_integration_matrix(C)
   186	    return {m: float(arr[m.position].sum() - arr[m.position, m.position]) for m in PILLARS}
   187	
   188	
   189	def hub_bound(k: int) -> float:
   190	    """Upper bound on I when every C_mn with both m, n outside a hub set of k pillars is 0.
   191	
   192	    Only pairs touching the hub can be non-zero: k(6 - k) + k(k - 1)/2 of the 15 pairs.
   193	    k = 1 gives 1/3, k = 2 gives 0.6, k = 3 gives 0.8.
   194	    """
   195	    if not 0 <= k <= M:
   196	        raise ValueError(f"k must lie in 0..{M}")
   197	    return (k * (M - k) + k * (k - 1) / 2) / 15.0
   198	
   199	
   200	def coalition_integration(
   201	    shares: Mapping[Pillar, Mapping[str, float]],
   202	    coalition_of: Mapping[str, str] | None = None,
   203	) -> np.ndarray:
   204	    """A formal variant of C_mn: max over coalitions S of min(s^m(S), s^n(S)).
   205	
   206	    This is the additive special case kappa_m(S) = sum of member shares of the Part II
   207	    coalition-overlap definition C_mn = max_S min(kappa_m(S), kappa_n(S)). The source describes C_mn only verbally ('the same coalition commands appointments,
   208	    budgets, sanctions or agenda in both m and n'); KB VII.3 (iv) asks Part VII to propose a
   209	    definition. Here s^m(S) is the summed share of coalition S in pillar m. Actors absent from
   210	    ``coalition_of`` form singleton coalitions. The result lies in [0, 1] and is weakly
   211	    increasing when a coalition gains share in either pillar.
   212	    """
   213	    coalition_of = dict(coalition_of or {})
   214	    by_pillar: dict[Pillar, dict[str, float]] = {}
   215	    for m in PILLARS:
   216	        if m not in shares:
   217	            raise ValueError(f"shares missing pillar {m.name}")
   218	        s = shares[m]
   219	        validate_shares(s)
   220	        agg: dict[str, float] = {}
   221	        for actor, v in s.items():
   222	            key = coalition_of.get(actor, actor)
   223	            agg[key] = agg.get(key, 0.0) + float(v)
   224	        by_pillar[m] = agg
   225	    arr = np.eye(M)
   226	    for m, n in PAIRS:
   227	        common = by_pillar[m].keys() & by_pillar[n].keys()
   228	        v = max((min(by_pillar[m][k], by_pillar[n][k]) for k in common), default=0.0)
   229	        v = min(max(v, 0.0), 1.0)
   230	        arr[m.position, n.position] = arr[n.position, m.position] = v
   231	    return arr
   232	
   233	
   234	@dataclass(frozen=True)
   235	class WeightSensitivity:
   236	    """Result of ``weight_sensitivity``. ``draws`` holds U for each sampled weight vector."""
   237	
   238	    baseline: float
   239	    vertex_min: float
   240	    vertex_max: float
   241	    draws: np.ndarray
   242	
   243	    @property
   244	    def quantiles(self) -> tuple[float, float]:
   245	        """5th and 95th percentile of U across draws."""
   246	        lo, hi = np.quantile(self.draws, [0.05, 0.95])
   247	        return float(lo), float(hi)
   248	
   249	    def fraction_at_least(self, u_star: float) -> float:
   250	        """Share of weight draws with U >= u_star (robustness of a threshold call)."""
   251	        validate_unit_interval(u_star, "u_star")
   252	        return float(np.mean(self.draws >= u_star))
   253	
   254	
   255	def weight_sensitivity(
   256	    H: Mapping[Pillar, float],
   257	    Q: Mapping[Pillar, float],
   258	    weights: Mapping[Pillar, float] | None = None,
   259	    n_draws: int = 2000,
   260	    seed: int = 0,
   261	) -> WeightSensitivity:
   262	    """Sensitivity of U to the weights w (source: 'weights preregistered; sensitivity analysis').
   263	
   264	    U is linear in w, so over the whole weight simplex its exact range is
   265	    [min_m H_m (1 - Q_m), max_m H_m (1 - Q_m)] (attained at the vertices). ``draws`` samples
   266	    w uniformly on the simplex (Dirichlet(1, ..., 1)) to show the typical spread.
   267	    """
   268	    if n_draws < 1:
   269	        raise ValueError("n_draws must be positive")
   270	    baseline = unaccountable_concentration(H, Q, weights)
   271	    h = _per_pillar(H, "H")
   272	    q = _per_pillar(Q, "Q")
   273	    terms = np.array([h[m] * (1.0 - q[m]) for m in PILLARS])
   274	    rng = np.random.default_rng(seed)
   275	    w = rng.dirichlet(np.ones(M), size=n_draws)
   276	    return WeightSensitivity(
   277	        baseline=baseline,
   278	        vertex_min=float(terms.min()),
   279	        vertex_max=float(terms.max()),
   280	        draws=(w * terms).sum(axis=1),
   281	    )
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

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/capture.py; nl -ba model/tests/test_capture.py' in /Users/mlong/Documents/Development/the-beast-system
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

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/pillars.py; nl -ba model/beast_system/network.py; nl -ba model/tests/test_pillars_network.py' in /Users/mlong/Documents/Development/the-beast-system
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

2026-10-22T17:25:02.448287Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '181,380p' model/beast_system/indices.py | nl -ba -v181" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   181	
   182	
   183	def integration_degrees(C: np.ndarray) -> dict[Pillar, float]:
   184	    """deg_m = sum_{n != m} C_mn, so that I = (sum_m deg_m) / 30 (Part VII spec, item 5)."""
   185	    arr = validate_integration_matrix(C)
   186	    return {m: float(arr[m.position].sum() - arr[m.position, m.position]) for m in PILLARS}
   187	
   188	
   189	def hub_bound(k: int) -> float:
   190	    """Upper bound on I when every C_mn with both m, n outside a hub set of k pillars is 0.
   191	
   192	    Only pairs touching the hub can be non-zero: k(6 - k) + k(k - 1)/2 of the 15 pairs.
   193	    k = 1 gives 1/3, k = 2 gives 0.6, k = 3 gives 0.8.
   194	    """
   195	    if not 0 <= k <= M:
   196	        raise ValueError(f"k must lie in 0..{M}")
   197	    return (k * (M - k) + k * (k - 1) / 2) / 15.0
   198	
   199	
   200	def coalition_integration(
   201	    shares: Mapping[Pillar, Mapping[str, float]],
   202	    coalition_of: Mapping[str, str] | None = None,
   203	) -> np.ndarray:
   204	    """A formal variant of C_mn: max over coalitions S of min(s^m(S), s^n(S)).
   205	
   206	    This is the additive special case kappa_m(S) = sum of member shares of the Part II
   207	    coalition-overlap definition C_mn = max_S min(kappa_m(S), kappa_n(S)). The source describes C_mn only verbally ('the same coalition commands appointments,
   208	    budgets, sanctions or agenda in both m and n'); KB VII.3 (iv) asks Part VII to propose a
   209	    definition. Here s^m(S) is the summed share of coalition S in pillar m. Actors absent from
   210	    ``coalition_of`` form singleton coalitions. The result lies in [0, 1] and is weakly
   211	    increasing when a coalition gains share in either pillar.
   212	    """
   213	    coalition_of = dict(coalition_of or {})
   214	    by_pillar: dict[Pillar, dict[str, float]] = {}
   215	    for m in PILLARS:
   216	        if m not in shares:
   217	            raise ValueError(f"shares missing pillar {m.name}")
   218	        s = shares[m]
   219	        validate_shares(s)
   220	        agg: dict[str, float] = {}
   221	        for actor, v in s.items():
   222	            key = coalition_of.get(actor, actor)
   223	            agg[key] = agg.get(key, 0.0) + float(v)
   224	        by_pillar[m] = agg
   225	    arr = np.eye(M)
   226	    for m, n in PAIRS:
   227	        common = by_pillar[m].keys() & by_pillar[n].keys()
   228	        v = max((min(by_pillar[m][k], by_pillar[n][k]) for k in common), default=0.0)
   229	        v = min(max(v, 0.0), 1.0)
   230	        arr[m.position, n.position] = arr[n.position, m.position] = v
   231	    return arr
   232	
   233	
   234	@dataclass(frozen=True)
   235	class WeightSensitivity:
   236	    """Result of ``weight_sensitivity``. ``draws`` holds U for each sampled weight vector."""
   237	
   238	    baseline: float
   239	    vertex_min: float
   240	    vertex_max: float
   241	    draws: np.ndarray
   242	
   243	    @property
   244	    def quantiles(self) -> tuple[float, float]:
   245	        """5th and 95th percentile of U across draws."""
   246	        lo, hi = np.quantile(self.draws, [0.05, 0.95])
   247	        return float(lo), float(hi)
   248	
   249	    def fraction_at_least(self, u_star: float) -> float:
   250	        """Share of weight draws with U >= u_star (robustness of a threshold call)."""
   251	        validate_unit_interval(u_star, "u_star")
   252	        return float(np.mean(self.draws >= u_star))
   253	
   254	
   255	def weight_sensitivity(
   256	    H: Mapping[Pillar, float],
   257	    Q: Mapping[Pillar, float],
   258	    weights: Mapping[Pillar, float] | None = None,
   259	    n_draws: int = 2000,
   260	    seed: int = 0,
   261	) -> WeightSensitivity:
   262	    """Sensitivity of U to the weights w (source: 'weights preregistered; sensitivity analysis').
   263	
   264	    U is linear in w, so over the whole weight simplex its exact range is
   265	    [min_m H_m (1 - Q_m), max_m H_m (1 - Q_m)] (attained at the vertices). ``draws`` samples
   266	    w uniformly on the simplex (Dirichlet(1, ..., 1)) to show the typical spread.
   267	    """
   268	    if n_draws < 1:
   269	        raise ValueError("n_draws must be positive")
   270	    baseline = unaccountable_concentration(H, Q, weights)
   271	    h = _per_pillar(H, "H")
   272	    q = _per_pillar(Q, "Q")
   273	    terms = np.array([h[m] * (1.0 - q[m]) for m in PILLARS])
   274	    rng = np.random.default_rng(seed)
   275	    w = rng.dirichlet(np.ones(M), size=n_draws)
   276	    return WeightSensitivity(
   277	        baseline=baseline,
   278	        vertex_min=float(terms.min()),
   279	        vertex_max=float(terms.max()),
   280	        draws=(w * terms).sum(axis=1),
   281	    )

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/__init__.py; nl -ba model/examples/run_all.py' in /Users/mlong/Documents/Development/the-beast-system
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
    27	    D0,
    28	    HARD_CASES,
    29	    HYPERARCS,
    30	    GovernanceSystem,
    31	    Practice,
    32	    cascade_closure,
    33	    check_proposition_a,
    34	    dependency_graph,
    35	    derive_functions,
    36	    hyperarcs,
    37	    is_cascade_complete,
    38	    is_strongly_connected,
    39	)
    40	from .network import MultiplexNetwork
    41	from .pillars import AXIOM_TO_PILLAR, M, PAIRS, PILLARS, Axiom, Pillar
    42	from .regimes import regime_profiles
    43	
    44	__all__ = [
    45	    "AXIOM_TO_PILLAR", "Axiom", "CaptureLink", "CaptureThresholds", "D0", "HYPERARCS",
    46	    "GovernanceSystem", "HARD_CASES", "M", "MultiplexNetwork", "PAIRS", "PILLARS", "Pillar",
    47	    "Polity", "Practice", "a_does_not_imply_b", "assess", "cascade_closure", "check_proposition_a",
    48	    "coalition_integration", "control_shares", "dependency_graph", "derive_functions", "hhi",
    49	    "hyperarcs", "integration_matrix", "integration_statistic", "is_capture_link",
    50	    "is_cascade_complete", "is_strongly_connected",
    51	    "negative_feedback_example", "proposition_b", "regime_profiles", "simulate",
    52	    "spectral_radius", "unaccountable_concentration", "weight_sensitivity",
    53	]
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
    19	    CONDITIONS,
    20	    HARD_CASES,
    21	    cascade_closure,
    22	    check_proposition_a,
    23	    critical_edges,
    24	    hyperarcs,
    25	    is_cascade_complete,
    26	    is_strongly_connected,
    27	    sinks_and_sources,
    28	    underlying_digraph,
    29	)
    30	from beast_system.pillars import PILLARS, Pillar  # noqa: E402
    31	from beast_system.regimes import regime_profiles  # noqa: E402
    32	
    33	
    34	def _yn(flag: bool) -> str:
    35	    return "yes" if flag else "no"
    36	
    37	
    38	def _row(label: str, a: Assessment) -> str:
    39	    hs = " ".join(f"{a.H[m]:.2f}" for m in PILLARS)
    40	    b = a.prop_b
    41	    return (f"{label:<58} {hs}  {a.U:.3f}  {a.I:.3f}  {_yn(a.prop_a.holds):<3}  "
    42	            f"{_yn(b.thresholds_met):<6}  {a.u_high_fraction:.2f}  {b.n_links}  {_yn(b.holds)}")
    43	
    44	
    45	def main() -> None:
    46	    th = CaptureThresholds()
    47	    head_h = " ".join(f"H_{m.name:<3}" for m in PILLARS)
    48	    header = (f"{'profile':<58} {head_h} U      I      A    U,I>=*  P(U>=u*)  L  B")
    49	    print(f"Thresholds u* = {th.u_star}, i* = {th.i_star}. "
    50	          "Regime values: ILLUSTRATIVE ASSUMPTIONS, not measurements.")
    51	    print(header)
    52	    print("-" * len(header))
    53	    for prof in regime_profiles():
    54	        print(_row(prof.label, assess(prof.polity, th)))
    55	    print("-" * len(header))
    56	    cm = a_does_not_imply_b(th)
    57	    print(_row("[counter-model] " + cm.plural.name, cm.plural))
    58	    print(_row("[counter-model] " + cm.fused.name, cm.fused))
    59	    print(f"A does not imply B (constructive counter-model): {cm.demonstrates_non_implication}")
    60	    print("P(U>=u*) = share of 2000 uniform weight draws with U >= u* (weight sensitivity).")
    61	    print("L = evidenced capture links; regime profiles carry none, so B never holds for them.")
    62	
    63	    print("\nHard cases (Theorem A check):")
    64	    for sys_ in HARD_CASES:
    65	        r = check_proposition_a(sys_)
    66	        forms = ", ".join(f"{d.pillar.name}:{d.form}" for d in r.derivations.values())
    67	        print(f"  {sys_.name:<36} A={_yn(r.holds)} counterexample={_yn(r.counterexample)} "
    68	              f"SC={_yn(r.strongly_connected)} cascade={_yn(r.cascade_complete)}  {forms}")
    69	
    70	    print("\nAxiom independence models (Ax_k dropped, pillar k absent):")
    71	    for ax, sys_ in AXIOM_INDEPENDENCE.items():
    72	        r = check_proposition_a(sys_)
    73	        print(f"  without {ax.name}: missing={sorted(m.name for m in r.missing)} "
    74	              f"antecedent={_yn(r.antecedent)} counterexample={_yn(r.counterexample)}")
    75	
    76	    print("\nDependency hypergraph (provider -> dependent; OR-hyperarcs {I,C}->J, {F,I}->C):")
    77	    for label, conds in [("D0", ()), ("D0+K_P+K_J+K_W", ("K_P", "K_J", "K_W")),
    78	                         ("D0+K_P+K_J+K_W+K_F", ("K_P", "K_J", "K_W", "K_F")),
    79	                         ("D0+all conditions", CONDITIONS)]:
    80	        arcs = hyperarcs(conds)
    81	        print(f"  {label:<20} underlying strongly connected = "
    82	              f"{is_strongly_connected(underlying_digraph(arcs))}; cascade-complete = "
    83	              f"{is_cascade_complete(arcs)}; cl({{C}}) = "
    84	              f"{sorted(m.name for m in cascade_closure(arcs, {Pillar.C}))}")
    85	    full = underlying_digraph(hyperarcs(CONDITIONS))
    86	    print("  critical arcs of the full underlying digraph: "
    87	          + ", ".join(f"{u.name}->{v.name}" for u, v in critical_edges(full)))
    88	    brief = underlying_digraph(BRIEF_ARCS)
    89	    sinks, _ = sinks_and_sources(brief)
    90	    print(f"  six brief relations alone: strongly connected = {is_strongly_connected(brief)}; "
    91	          f"sinks = {sorted(m.name for m in sinks)}")
    92	
    93	    fb = negative_feedback_example()
    94	    print("\nDynamics: same positive links, rho(B+) = "
    95	          f"{fb.rho_positive:.3f} (persists), rho(B+ with negative feedback) = "
    96	          f"{fb.rho_feedback:.3f} (decays); same positive links = {fb.same_positive_links}")
    97	
    98	
    99	if __name__ == "__main__":
   100	    main()

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

exec
/usr/local/bin/zsh -lc "sed -n '1,180p' model/beast_system/indices.py | nl -ba" in /Users/mlong/Documents/Development/the-beast-system
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
   152	    np.fill_diagonal(arr, 1.0)
   153	    return arr
   154	
   155	
   156	def integration_matrix(
   157	    pairs: Mapping[tuple[Pillar, Pillar], float], default: float = 0.0
   158	) -> np.ndarray:
   159	    """Build a symmetric C from {(m, n): C_mn}; unspecified pairs take ``default``."""
   160	    validate_unit_interval(default, "default")
   161	    arr = np.full((M, M), float(default))
   162	    seen: set[frozenset[Pillar]] = set()
   163	    for (m, n), value in pairs.items():
   164	        if m == n:
   165	            raise ValueError(f"pair ({m.name}, {n.name}) is not a cross-pillar pair")
   166	        key = frozenset((m, n))
   167	        if key in seen:
   168	            raise ValueError(f"pair {m.name}{n.name} given twice")
   169	        seen.add(key)
   170	        v = validate_unit_interval(value, f"C[{m.name}{n.name}]")
   171	        arr[m.position, n.position] = arr[n.position, m.position] = v
   172	    np.fill_diagonal(arr, 1.0)
   173	    return arr
   174	
   175	
   176	def integration_statistic(C: np.ndarray) -> float:
   177	    """I = 2 / (M (M - 1)) sum_{m<n} C_mn with M = 6, i.e. the mean over 15 pairs (source Eq. I_t)."""
   178	    arr = validate_integration_matrix(C)
   179	    total = sum(arr[m.position, n.position] for m, n in PAIRS)
   180	    return float(2.0 / (M * (M - 1)) * total)

2026-10-22T17:25:06.077881Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
codex
The two round-2 defects appear addressed in source: persistence is now framed existentially, and raw control weights are scaled before summation. I’m checking whether the implementation and tests actually establish the narrower claims and all hypergraph/foothold edge cases.
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '401,620p' model/beast_system/necessity.py | nl -ba -v401" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   401	) -> PropositionAResult:
   402	    """Check Theorem A on ``system`` (Part VII Theorem A; KB Section 4.3).
   403	
   404	    A hyperarc in ``required`` is demanded when its head and every tail member are realized.
   405	    """
   406	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   407	    needed = frozenset((t, h) for t, h in _keys(required) if h in realized and t <= realized)
   408	    missing_deps = needed - system.dependencies
   409	    coded = underlying_digraph(system.dependencies)
   410	    return PropositionAResult(
   411	        system=system.name,
   412	        antecedent=system.persistent and system.all_axioms_hold,
   413	        realized=realized,
   414	        missing=frozenset(PILLARS) - realized,
   415	        missing_dependencies=missing_deps,
   416	        strongly_connected=is_strongly_connected(coded, realized),
   417	        cascade_complete=is_cascade_complete(system.dependencies, realized),
   418	        holds=realized == frozenset(PILLARS) and not missing_deps,
   419	        derivations=derive_functions(system),
   420	    )
   421	
   422	
   423	def formal_system(
   424	    name: str,
   425	    holders: Mapping[Pillar, Iterable[str]],
   426	    persistent: bool = True,
   427	    source: str = "",
   428	    dependencies: Iterable[Hyperarc | ArcKey] = D0,
   429	) -> GovernanceSystem:
   430	    """A persistent system satisfying Ax1..Ax6 whose pillars are held by formal organizations.
   431	
   432	    An actor listed under several pillars is fused. By default D0 is coded as present: an
   433	    assumption of the stylized model, not an observation. Used for regime profiles and
   434	    counter-models.
   435	    """
   436	    practices = tuple(
   437	        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
   438	                 frozenset(hs), formal=True, source=source)
   439	        for m, hs in holders.items()
   440	        if hs
   441	    )
   442	    return GovernanceSystem(name, persistent, frozenset(Axiom), practices,
   443	                            _keys(dependencies))
   444	
   445	
   446	# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
   447	
   448	
   449	def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
   450	    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)
   451	
   452	
   453	NUER = GovernanceSystem(
   454	    name="Nuer ('ordered anarchy')",
   455	    persistent=True,
   456	    axioms=frozenset(Axiom),
   457	    practices=(
   458	        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
   459	                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
   460	        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
   461	                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
   462	        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
   463	                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
   464	        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
   465	                  {"prophets", "lineages"}, "evanspritchard1940"),
   466	        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
   467	                  {"agnatic kin"}, "evanspritchard1940"),
   468	        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
   469	                  "evanspritchard1940"),
   470	    ),
   471	    dependencies=D0_KEYS,
   472	    note="no office holds coercive authority; functions exist without separation",
   473	)
   474	
   475	JU_HOANSI = GovernanceSystem(
   476	    name="Ju/'hoansi (!Kung)",
   477	    persistent=True,
   478	    axioms=frozenset(Axiom),
   479	    practices=(
   480	        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
   481	                  {"hunters", "camp members"}, "lee2013; marshall1976"),
   482	        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
   483	                  {"camp members"}, "lee2013"),
   484	        _informal("disputes talked out with kin mediators", Axiom.Ax3,
   485	                  {"kin mediators"}, "lee1979; wiessner2005"),
   486	        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
   487	                  {"healers", "camp members"}, "marshall1976"),
   488	        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
   489	                  {"camp members"}, "wiessner2005; lee2013"),
   490	        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
   491	    ),
   492	    dependencies=D0_KEYS,
   493	    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
   494	)
   495	
   496	OSTROM_COMMONS = GovernanceSystem(
   497	    name="Ostrom commons (design principles)",
   498	    persistent=True,
   499	    axioms=frozenset(Axiom),
   500	    practices=(
   501	        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
   502	                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
   503	        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
   504	                  {"appropriators"}, "ostrom1990"),
   505	        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
   506	                  {"appropriators"}, "ostrom1990; cox2010"),
   507	        _informal("shared norms; minimal recognition of rights to organize (DP7)",
   508	                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),
   509	        _informal("monitoring and graduated sanctions by appropriators (DP4, DP5)",
   510	                  Axiom.Ax5, {"appropriators"}, "ostrom1990; cox2010"),
   511	        _informal("appropriation and maintenance labor", Axiom.Ax6, {"appropriators"},
   512	                  "ostrom1990"),
   513	    ),
   514	    dependencies=D0_KEYS,
   515	    note="checks in minimal form; monitors are appropriators or accountable to them",
   516	)
   517	
   518	CONSENSUS_VILLAGE = GovernanceSystem(
   519	    name="Consensus village (stylized)",
   520	    persistent=True,
   521	    axioms=frozenset(Axiom),
   522	    practices=(
   523	        _informal("household plots; reciprocal labor exchange; sharing norms", Axiom.Ax1,
   524	                  {"households"}, "sahlins1972"),
   525	        _informal("consensus meeting of adults", Axiom.Ax2, {"village meeting"},
   526	                  "clastres1987; boehm1999"),
   527	        _informal("elders mediate disputes", Axiom.Ax3, {"elders"}, "boehm1999"),
   528	        _informal("ritual and myth; moral talk", Axiom.Ax4, {"village meeting", "elders"},
   529	                  "boehm1999"),
   530	        _informal("gossip, shunning, ostracism of would-be dominants", Axiom.Ax5,
   531	                  {"village meeting"}, "boehm1999; woodburn1982"),
   532	        _informal("gardening and household labor", Axiom.Ax6, {"households"},
   533	                  "sahlins1972"),
   534	    ),
   535	    dependencies=D0_KEYS,
   536	    note="stylized composite; reverse dominance hierarchy",
   537	)
   538	
   539	HARD_CASES: tuple[GovernanceSystem, ...] = (NUER, JU_HOANSI, OSTROM_COMMONS, CONSENSUS_VILLAGE)
   540	
   541	
   542	# Axiom independence fixtures (Part VII spec, item 7). ---------------------------------------
   543	
   544	#: Consistency model: all six axioms hold and all six pillars are realized (the consensus
   545	#: village coding, which also carries D0).
   546	BASELINE_MODEL: GovernanceSystem = CONSENSUS_VILLAGE
   547	
   548	
   549	def _drop_axiom(axiom: Axiom) -> GovernanceSystem:
   550	    gone = axiom.pillar
   551	    return GovernanceSystem(
   552	        name=f"independence model without {axiom.name} ({axiom.label})",
   553	        persistent=True,
   554	        axioms=frozenset(Axiom) - {axiom},
   555	        practices=tuple(p for p in BASELINE_MODEL.practices if p.solves is not axiom),
   556	        dependencies=frozenset(
   557	            (t, h) for t, h in BASELINE_MODEL.dependencies if h is not gone and gone not in t
   558	        ),
   559	        note="hypothetical: persistent, Ax_k removed, pillar k absent",
   560	    )
   561	
   562	
   563	#: For each k: persistent, Ax_k removed, pillar k missing. Theorem A's antecedent is false,
   564	#: so none is a counterexample; each shows pillar k is not forced by the other five axioms.
   565	AXIOM_INDEPENDENCE: dict[Axiom, GovernanceSystem] = {a: _drop_axiom(a) for a in Axiom}

exec
/usr/local/bin/zsh -lc "sed -n '1,200p' model/beast_system/necessity.py | nl -ba" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Structural necessity: Proposition A and the pillar dependency hypergraph (Part VII Theorem A).
     2	
     3	Theorem A (notation.md CENTRAL THESIS; KB Section 4): if a governance system G persists and
     4	satisfies Ax1..Ax6, then every pillar in M is implemented in G, and the unconditional
     5	dependency relations D0 are present. Implementation is role-level, not institution-level
     6	(Hempel 1959): a function may be held by a formal institution, fused with other functions
     7	inside one institution, or exercised informally (gossip and shunning as C, mediators as J).
     8	
     9	What this module does and does not do. It cannot prove Theorem A. It encodes the lemma schema
    10	'Ax_k + persistence => some practice solves problem_k' and checks it against coded cases. The
    11	role map is DERIVED from independently coded practices, never declared, so a persistent case
    12	that satisfies all six axioms yet has no practice for some problem, or lacks a D0 relation, is
    13	reported as a counterexample (the falsifier required by KB Section 4.4).
    14	
    15	Dependencies form an AND/OR hypergraph (Part VII spec). A hyperarc (T, h) is written
    16	provider(s) -> dependent and means: h needs an output of AT LEAST ONE member of T. Single arcs
    17	have |T| = 1. D0 holds unconditionally; every other hyperarc is tagged with the condition
    18	(K_C, K_F, K_P, K_J, K_W) under which a pillar Part derives it. Two connectivity notions are
    19	computed and reported, and NEITHER enters the Theorem A predicate:
    20	  (a) the underlying digraph (each (T, h) replaced by arcs t -> h) is strongly connected;
    21	  (b) cascade completeness: cl({n}) = M for every n, where cl(S) is the least superset of S
    22	      such that T subset of cl(S) implies h in cl(S) for every hyperarc (T, h).
    23	"""
    24	
    25	from __future__ import annotations
    26	
    27	from collections.abc import Iterable, Mapping
    28	from dataclasses import dataclass, field
    29	from typing import Literal
    30	
    31	from .pillars import AXIOM_TO_PILLAR, PILLAR_TO_AXIOM, PILLARS, Axiom, Pillar
    32	
    33	RealizedForm = Literal["formal institution", "fused", "informal/minimal"]
    34	FORMAL: RealizedForm = "formal institution"
    35	FUSED: RealizedForm = "fused"
    36	INFORMAL: RealizedForm = "informal/minimal"
    37	
    38	# Dependency hypergraph ---------------------------------------------------------------------
    39	
    40	#: A hyperarc key (T, h): tail set T, head h.
    41	ArcKey = tuple[frozenset[Pillar], Pillar]
    42	Graph = Mapping[Pillar, Iterable[Pillar]]
    43	
    44	#: Condition names (Part VII spec). None marks the unconditional set D0.
    45	CONDITIONS: tuple[str, ...] = ("K_C", "K_F", "K_P", "K_J", "K_W")
    46	
    47	
    48	def arc_key(tail: Pillar | Iterable[Pillar], head: Pillar) -> ArcKey:
    49	    """Normalize (T, h) to an ArcKey, validating T non-empty, h a Pillar and h not in T."""
    50	    t = frozenset((tail,) if isinstance(tail, Pillar) else tail)
    51	    if not t or not all(isinstance(m, Pillar) for m in t) or not isinstance(head, Pillar):
    52	        raise TypeError("a hyperarc needs a non-empty tail of Pillars and a Pillar head")
    53	    if head in t:
    54	        raise ValueError(f"head {head.name} may not belong to its own tail")
    55	    return t, head
    56	
    57	
    58	@dataclass(frozen=True)
    59	class Hyperarc:
    60	    """Hyperarc (T, h): h needs an output of at least one member of T (provider -> dependent)."""
    61	
    62	    tail: frozenset[Pillar]
    63	    head: Pillar
    64	    condition: str | None
    65	    rationale: str
    66	    source: str
    67	
    68	    def __post_init__(self) -> None:
    69	        tail, head = arc_key(self.tail, self.head)
    70	        if self.condition is not None and self.condition not in CONDITIONS:
    71	            raise ValueError(f"unknown condition {self.condition!r}")
    72	        object.__setattr__(self, "tail", tail)
    73	
    74	    @property
    75	    def key(self) -> ArcKey:
    76	        return self.tail, self.head
    77	
    78	
    79	_P = Pillar
    80	_W_NEED = "practitioners consume produced resources (Ax6; Part VI no-manna)"
    81	
    82	#: The encoded hypergraph (Part VII spec, item 1).
    83	HYPERARCS: tuple[Hyperarc, ...] = (
    84	    *(Hyperarc(frozenset({_P.W}), m, None, _W_NEED, "Part VI")
    85	      for m in (_P.F, _P.P, _P.J, _P.I, _P.C)),
    86	    Hyperarc(frozenset({_P.I, _P.C}), _P.J, None,
    87	             "rulings settle disputes if recognized or if enforced", "Part III Prop 3.6"),
    88	    Hyperarc(frozenset({_P.F, _P.I}), _P.C, "K_C",
    89	             "costly public-good sanctions at large n, no higher-order sanctions",
    90	             "Part V Cor 3.7"),
    91	    Hyperarc(frozenset({_P.C}), _P.F, "K_F",
    92	             "the allocation rule faces temptation p > theta", "Part V Thm 3.4"),
    93	    Hyperarc(frozenset({_P.P}), _P.J, "K_P", "environmental change", "Part II Ass 3.2"),
    94	    Hyperarc(frozenset({_P.P}), _P.I, "K_P", "environmental change", "Part II Ass 3.2"),
    95	    Hyperarc(frozenset({_P.I}), _P.P, "K_P", "environmental change with Ax4",
    96	             "Part II Ass 3.2; Part IV Ax4"),
    97	    Hyperarc(frozenset({_P.J}), _P.F, "K_J",
    98	             "allocation rules have open texture with residual disputes", "Part III Thm 3.3"),
    99	    Hyperarc(frozenset({_P.F}), _P.W, "K_W", "productive inputs are contested goods", "Part I"),
   100	)
   101	
   102	D0: tuple[Hyperarc, ...] = tuple(a for a in HYPERARCS if a.condition is None)
   103	D0_KEYS: frozenset[ArcKey] = frozenset(a.key for a in D0)
   104	
   105	#: The six single arcs named in the original model brief (kept for comparison only).
   106	BRIEF_ARCS: frozenset[ArcKey] = frozenset(
   107	    arc_key(t, h) for t, h in [(_P.W, _P.C), (_P.P, _P.J), (_P.I, _P.P), (_P.J, _P.F),
   108	                               (_P.F, _P.W), (_P.W, _P.I)]
   109	)
   110	
   111	
   112	def hyperarcs(conditions: Iterable[str] = ()) -> tuple[Hyperarc, ...]:
   113	    """D0 plus the hyperarcs whose condition is in ``conditions``."""
   114	    conds = set(conditions)
   115	    unknown = conds - set(CONDITIONS)
   116	    if unknown:
   117	        raise ValueError(f"unknown conditions {sorted(unknown)}")
   118	    return tuple(a for a in HYPERARCS if a.condition is None or a.condition in conds)
   119	
   120	
   121	def _keys(arcs: Iterable[Hyperarc | ArcKey]) -> frozenset[ArcKey]:
   122	    return frozenset(a.key if isinstance(a, Hyperarc) else arc_key(*a) for a in arcs)
   123	
   124	
   125	def underlying_digraph(arcs: Iterable[Hyperarc | ArcKey]) -> dict[Pillar, frozenset[Pillar]]:
   126	    """Replace each hyperarc (T, h) by the arcs t -> h; adjacency over all six pillars."""
   127	    adj: dict[Pillar, set[Pillar]] = {m: set() for m in PILLARS}
   128	    for tail, head in _keys(arcs):
   129	        for t in tail:
   130	            adj[t].add(head)
   131	    return {m: frozenset(v) for m, v in adj.items()}
   132	
   133	
   134	def dependency_graph(conditions: Iterable[str] = CONDITIONS) -> dict[Pillar, frozenset[Pillar]]:
   135	    """Underlying digraph of D0 plus the named conditional hyperarcs (default: all)."""
   136	    return underlying_digraph(hyperarcs(conditions))
   137	
   138	
   139	def cascade_closure(arcs: Iterable[Hyperarc | ArcKey], start: Iterable[Pillar]) -> frozenset[Pillar]:
   140	    """cl(S): least superset of S with T subset of cl(S) => h in cl(S) for every (T, h).
   141	
   142	    Read as a failure cascade: h fails once every provider in its tail has failed.
   143	    """
   144	    keys = _keys(arcs)
   145	    closed = set(start)
   146	    changed = True
   147	    while changed:
   148	        changed = False
   149	        for tail, head in keys:
   150	            if head not in closed and tail <= closed:
   151	                closed.add(head)
   152	                changed = True
   153	    return frozenset(closed)
   154	
   155	
   156	def is_cascade_complete(
   157	    arcs: Iterable[Hyperarc | ArcKey], nodes: Iterable[Pillar] = PILLARS
   158	) -> bool:
   159	    """True iff cl({n}) contains every node, for every node n (restricted to ``nodes``)."""
   160	    keep = frozenset(nodes)
   161	    if not keep:
   162	        return False
   163	    inside = [(t, h) for t, h in _keys(arcs) if h in keep and t <= keep]
   164	    return all(cascade_closure(inside, {n}) >= keep for n in keep)
   165	
   166	
   167	def _nodes(graph: Graph) -> set[Pillar]:
   168	    nodes = set(graph)
   169	    for targets in graph.values():
   170	        nodes.update(targets)
   171	    return nodes
   172	
   173	
   174	def _reach(graph: Mapping[Pillar, frozenset[Pillar]], start: Pillar) -> set[Pillar]:
   175	    seen = {start}
   176	    stack = [start]
   177	    while stack:
   178	        for nxt in graph.get(stack.pop(), frozenset()):
   179	            if nxt not in seen:
   180	                seen.add(nxt)
   181	                stack.append(nxt)
   182	    return seen
   183	
   184	
   185	def is_strongly_connected(graph: Graph, nodes: Iterable[Pillar] | None = None) -> bool:
   186	    """True iff every node of the graph is reachable from every other node.
   187	
   188	    ``nodes`` restricts the graph to an induced subgraph (default: all nodes that appear).
   189	    The empty graph is not strongly connected; a single node is.
   190	    """
   191	    keep = set(nodes) if nodes is not None else _nodes(graph)
   192	    if not keep:
   193	        return False
   194	    fwd: dict[Pillar, frozenset[Pillar]] = {
   195	        u: frozenset(v for v in graph.get(u, ()) if v in keep) for u in keep
   196	    }
   197	    rev: dict[Pillar, set[Pillar]] = {u: set() for u in keep}
   198	    for u, vs in fwd.items():
   199	        for v in vs:
   200	            rev[v].add(u)

exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_necessity.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	import pytest
     2	
     3	from beast_system.necessity import (
     4	    AXIOM_INDEPENDENCE,
     5	    BASELINE_MODEL,
     6	    BRIEF_ARCS,
     7	    CONDITIONS,
     8	    D0,
     9	    D0_KEYS,
    10	    HYPERARCS,
    11	    NUER,
    12	    Hyperarc,
    13	    arc_key,
    14	    cascade_closure,
    15	    hyperarcs,
    16	    is_cascade_complete,
    17	    underlying_digraph,
    18	    FORMAL,
    19	    FUSED,
    20	    HARD_CASES,
    21	    INFORMAL,
    22	    JU_HOANSI,
    23	    GovernanceSystem,
    24	    Practice,
    25	    check_proposition_a,
    26	    critical_edges,
    27	    derive_functions,
    28	    formal_system,
    29	    is_strongly_connected,
    30	    role_map,
    31	    sinks_and_sources,
    32	)
    33	from beast_system.pillars import PILLARS, Axiom, Pillar
    34	
    35	F, P, J, I, C, W = PILLARS
    36	
    37	
    38	@pytest.mark.parametrize("system", HARD_CASES, ids=lambda s: s.name)
    39	def test_theorem_a_on_hard_cases(system):
    40	    result = check_proposition_a(system)
    41	    assert result.antecedent
    42	    assert result.holds and not result.counterexample
    43	    assert result.realized == frozenset(PILLARS)
    44	    derivs = derive_functions(system)
    45	    assert {d.pillar for d in derivs.values()} == set(PILLARS)
    46	    assert all(d.form == INFORMAL for d in derivs.values())
    47	
    48	
    49	def test_role_map_is_derived_from_practices():
    50	    roles = role_map(JU_HOANSI)
    51	    assert Pillar.C in roles["camp members"] and Pillar.P in roles["camp members"]
    52	
    53	
    54	def test_missing_axiom_drops_pillar_and_is_not_a_counterexample():
    55	    # A perfectly cooperative collective: Ax5 fails and there is no sanction practice.
    56	    practices = tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5)
    57	    system = GovernanceSystem("no defection", True, frozenset(Axiom) - {Axiom.Ax5}, practices)
    58	    derivs = derive_functions(system)
    59	    assert Axiom.Ax5 not in derivs and len(derivs) == 5
    60	    result = check_proposition_a(system)
    61	    assert not result.antecedent
    62	    assert result.missing == {C}
    63	    assert not result.holds and not result.counterexample
    64	
    65	
    66	def test_falsifier_is_reported():
    67	    # All axioms coded as holding, persistent, but no sanction practice: a counterexample.
    68	    practices = tuple(p for p in JU_HOANSI.practices if p.solves is not Axiom.Ax5)
    69	    system = GovernanceSystem("hypothetical", True, frozenset(Axiom), practices)
    70	    result = check_proposition_a(system)
    71	    assert result.counterexample
    72	    assert derive_functions(system)[Axiom.Ax5].form is None
    73	
    74	
    75	def test_non_persistent_system_does_not_trigger_theorem():
    76	    system = GovernanceSystem("short-lived", False, frozenset(Axiom), ())
    77	    assert not check_proposition_a(system).antecedent
    78	    assert not check_proposition_a(system).counterexample
    79	
    80	
    81	def test_fused_and_formal_forms():
    82	    system = formal_system("toy", {F: ["Treasury"], P: ["Crown"], J: ["Crown"], I: ["Church"],
    83	                                   C: ["Crown"], W: ["Peasants"]})
    84	    derivs = derive_functions(system)
    85	    assert derivs[Axiom.Ax2].form == FUSED
    86	    assert derivs[Axiom.Ax5].form == FUSED
    87	    assert derivs[Axiom.Ax1].form == FORMAL
    88	    assert check_proposition_a(system).holds
    89	
    90	
    91	def test_practice_validation():
    92	    with pytest.raises(ValueError):
    93	        Practice("x", Axiom.Ax1, frozenset())
    94	    with pytest.raises(TypeError):
    95	        Practice("x", Pillar.F, frozenset({"a"}))  # type: ignore[arg-type]
    96	
    97	
    98	def test_hyperarcs_are_documented():
    99	    for a in HYPERARCS:
   100	        assert a.head not in a.tail and a.rationale and a.source
   101	        assert a.condition is None or a.condition in CONDITIONS
   102	    assert len({a.key for a in HYPERARCS}) == len(HYPERARCS)
   103	    assert {c for a in HYPERARCS for c in [a.condition] if c} == set(CONDITIONS)
   104	
   105	
   106	def test_d0_is_w_to_all_plus_or_hyperarc():
   107	    singles = {arc_key(W, m) for m in (F, P, J, I, C)}
   108	    assert D0_KEYS == singles | {arc_key({I, C}, J)}
   109	    # The separate single arcs C->J and I->J are not unconditional relations.
   110	    assert arc_key(C, J) not in D0_KEYS and arc_key(I, J) not in D0_KEYS
   111	
   112	
   113	def test_d0_underlying_not_strongly_connected():
   114	    assert not is_strongly_connected(underlying_digraph(D0))
   115	    assert not is_cascade_complete(D0)
   116	
   117	
   118	def test_kp_kj_kw_strongly_connected_but_c_isolated_in_cascade():
   119	    arcs = hyperarcs(["K_P", "K_J", "K_W"])
   120	    assert is_strongly_connected(underlying_digraph(arcs))
   121	    for n in PILLARS:
   122	        expected = {C} if n is C else set(PILLARS)
   123	        assert cascade_closure(arcs, {n}) == expected, n
   124	    assert not is_cascade_complete(arcs)
   125	
   126	
   127	def test_adding_kf_makes_cascade_complete():
   128	    assert is_cascade_complete(hyperarcs(["K_P", "K_J", "K_W", "K_F"]))
   129	    assert is_cascade_complete(hyperarcs(CONDITIONS))
   130	
   131	
   132	def test_splitting_or_hyperarc_would_put_j_in_cl_c():
   133	    arcs = [a.key for a in hyperarcs(["K_P", "K_J", "K_W"]) if a.key != arc_key({I, C}, J)]
   134	    split = arcs + [arc_key(C, J), arc_key(I, J)]
   135	    assert J in cascade_closure(split, {C})
   136	    assert J not in cascade_closure(hyperarcs(["K_P", "K_J", "K_W"]), {C})
   137	
   138	
   139	def test_or_hyperarc_needs_whole_tail_to_fail():
   140	    arcs = [arc_key({I, C}, J)]
   141	    assert cascade_closure(arcs, {I}) == {I}
   142	    assert cascade_closure(arcs, {I, C}) == {I, C, J}
   143	
   144	
   145	def test_brief_relations_alone_are_not_strongly_connected():
   146	    brief = underlying_digraph(BRIEF_ARCS)
   147	    assert not is_strongly_connected(brief)
   148	    sinks, sources = sinks_and_sources(brief)
   149	    assert sinks == {C} and not sources
   150	
   151	
   152	def test_critical_edges_of_full_graph():
   153	    full = underlying_digraph(hyperarcs(CONDITIONS))
   154	    assert set(critical_edges(full)) == {(F, W), (J, F)}
   155	    assert critical_edges(underlying_digraph(D0)) == []
   156	
   157	
   158	def test_hyperarc_validation():
   159	    with pytest.raises(ValueError):
   160	        arc_key({J, C}, J)
   161	    with pytest.raises(TypeError):
   162	        arc_key(set(), J)
   163	    with pytest.raises(ValueError):
   164	        Hyperarc(frozenset({F}), W, "K_X", "r", "s")
   165	    with pytest.raises(ValueError):
   166	        hyperarcs(["K_X"])
   167	
   168	
   169	def test_missing_d0_relation_is_a_counterexample():
   170	    system = GovernanceSystem("no W->C", True, frozenset(Axiom), JU_HOANSI.practices,
   171	                              D0_KEYS - {arc_key(W, C)})
   172	    result = check_proposition_a(system)
   173	    assert result.realized == frozenset(PILLARS)
   174	    assert result.missing_dependencies == {arc_key(W, C)}
   175	    assert result.counterexample
   176	
   177	
   178	def test_connectivity_is_reported_not_required():
   179	    # Hard cases code D0 only: A holds although neither connectivity notion holds.
   180	    result = check_proposition_a(NUER)
   181	    assert result.holds and not result.strongly_connected and not result.cascade_complete
   182	    full = GovernanceSystem("full", True, frozenset(Axiom), JU_HOANSI.practices,
   183	                            frozenset(a.key for a in HYPERARCS))
   184	    r_full = check_proposition_a(full)
   185	    assert r_full.holds and r_full.strongly_connected and r_full.cascade_complete
   186	
   187	
   188	@pytest.mark.parametrize("axiom", list(Axiom), ids=lambda a: a.name)
   189	def test_axiom_independence_fixtures(axiom):
   190	    system = AXIOM_INDEPENDENCE[axiom]
   191	    assert system.persistent and not system.holds(axiom)
   192	    result = check_proposition_a(system)
   193	    assert result.missing == {axiom.pillar}
   194	    assert not result.antecedent and not result.counterexample
   195	
   196	
   197	def test_baseline_model_is_consistent():
   198	    result = check_proposition_a(BASELINE_MODEL)
   199	    assert BASELINE_MODEL.all_axioms_hold and result.antecedent and result.holds
   200	
   201	
   202	def test_strong_connectivity_small_cases():
   203	    assert not is_strongly_connected({})
   204	    assert is_strongly_connected({F: set()})
   205	    assert is_strongly_connected({F: {P}, P: {F}})
   206	    assert not is_strongly_connected({F: {P}, P: set()})
   207	    assert is_strongly_connected({F: {P}, P: {F, J}}, nodes={F, P})
   208	
   209	

exec
/usr/local/bin/zsh -lc "sed -n '201,400p' model/beast_system/necessity.py | nl -ba -v201" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   201	    start = next(iter(keep))
   202	    rev_f = {u: frozenset(v) for u, v in rev.items()}
   203	    return _reach(fwd, start) == keep and _reach(rev_f, start) == keep
   204	
   205	
   206	def critical_edges(graph: Graph) -> list[tuple[Pillar, Pillar]]:
   207	    """Edges whose single removal breaks strong connectivity (empty if not connected)."""
   208	    nodes = _nodes(graph)
   209	    base = {u: frozenset(graph.get(u, ())) for u in nodes}
   210	    if not is_strongly_connected(base):
   211	        return []
   212	    out = []
   213	    for u in PILLARS:
   214	        for v in sorted(base.get(u, ()), key=lambda p: p.position):
   215	            pruned = dict(base)
   216	            pruned[u] = base[u] - {v}
   217	            if not is_strongly_connected(pruned, nodes):
   218	                out.append((u, v))
   219	    return out
   220	
   221	
   222	def sinks_and_sources(graph: Graph) -> tuple[frozenset[Pillar], frozenset[Pillar]]:
   223	    """Pillars with no outgoing edge (sinks) and with no incoming edge (sources)."""
   224	    nodes = _nodes(graph)
   225	    has_out = {u for u in nodes if any(True for _ in graph.get(u, ()))}
   226	    has_in = {v for u in nodes for v in graph.get(u, ())}
   227	    return frozenset(nodes - has_out), frozenset(nodes - has_in)
   228	
   229	
   230	# Governance systems ------------------------------------------------------------------------
   231	
   232	
   233	@dataclass(frozen=True)
   234	class Practice:
   235	    """A regular activity that discharges the problem generated by axiom ``solves``.
   236	
   237	    ``formal`` is True when the activity is attached to a designated office or organization.
   238	    ``source`` holds the citation key(s) supporting the coding.
   239	    """
   240	
   241	    description: str
   242	    solves: Axiom
   243	    holders: frozenset[str]
   244	    formal: bool = False
   245	    source: str = ""
   246	
   247	    def __post_init__(self) -> None:
   248	        if not isinstance(self.solves, Axiom):
   249	            raise TypeError("Practice.solves must be an Axiom")
   250	        holders = frozenset(self.holders)
   251	        if not holders or any(not isinstance(h, str) or not h for h in holders):
   252	            raise ValueError("a practice needs at least one named holder")
   253	        if not self.description.strip():
   254	            raise ValueError("a practice needs a description")
   255	        object.__setattr__(self, "holders", holders)
   256	
   257	    @property
   258	    def pillar(self) -> Pillar:
   259	        return AXIOM_TO_PILLAR[self.solves]
   260	
   261	
   262	@dataclass(frozen=True)
   263	class GovernanceSystem:
   264	    """A collective that makes and enforces collective decisions (KB Section 4.1).
   265	
   266	    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
   267	    over the period studied. Both are coded independently of ``practices``. ``dependencies``
   268	    lists the hyperarcs coded as present in THIS system (Hyperarc objects or (T, h) pairs);
   269	    Theorem A is checked against them, not against the global encoding.
   270	    """
   271	
   272	    name: str
   273	    persistent: bool
   274	    axioms: frozenset[Axiom]
   275	    practices: tuple[Practice, ...] = ()
   276	    dependencies: frozenset[ArcKey] = frozenset()
   277	    note: str = ""
   278	
   279	    def __post_init__(self) -> None:
   280	        if not isinstance(self.persistent, bool):
   281	            raise TypeError("persistent must be a bool")
   282	        axioms = frozenset(self.axioms)
   283	        if any(not isinstance(a, Axiom) for a in axioms):
   284	            raise TypeError("axioms must be Axiom members")
   285	        practices = tuple(self.practices)
   286	        if any(not isinstance(p, Practice) for p in practices):
   287	            raise TypeError("practices must be Practice instances")
   288	        object.__setattr__(self, "axioms", axioms)
   289	        object.__setattr__(self, "practices", practices)
   290	        object.__setattr__(self, "dependencies", _keys(self.dependencies))
   291	
   292	    def holds(self, axiom: Axiom) -> bool:
   293	        """Predicate for one axiom (Ax1 scarcity, ..., Ax6 maintenance)."""
   294	        return axiom in self.axioms
   295	
   296	    @property
   297	    def all_axioms_hold(self) -> bool:
   298	        return all(self.holds(a) for a in Axiom)
   299	
   300	
   301	def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
   302	    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
   303	    roles: dict[str, set[Pillar]] = {}
   304	    for p in system.practices:
   305	        for h in p.holders:
   306	            roles.setdefault(h, set()).add(p.pillar)
   307	    return {h: frozenset(ps) for h, ps in roles.items()}
   308	
   309	
   310	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   311	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   312	
   313	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   314	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   315	    """
   316	    practices = [p for p in system.practices if p.pillar is pillar]
   317	    if not practices:
   318	        return None
   319	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   320	    if not formal_holders:
   321	        return INFORMAL
   322	    formal_roles: dict[str, set[Pillar]] = {}
   323	    for p in system.practices:
   324	        if p.formal:
   325	            for h in p.holders:
   326	                formal_roles.setdefault(h, set()).add(p.pillar)
   327	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   328	        return FUSED
   329	    return FORMAL
   330	
   331	
   332	@dataclass(frozen=True)
   333	class Derivation:
   334	    """Result of the lemma for one axiom: required pillar and its realized form."""
   335	
   336	    axiom: Axiom
   337	    pillar: Pillar
   338	    form: RealizedForm | None
   339	    practices: tuple[Practice, ...]
   340	
   341	    @property
   342	    def realized(self) -> bool:
   343	        return self.form is not None
   344	
   345	
   346	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   347	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   348	
   349	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   350	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   351	    """
   352	    out: dict[Axiom, Derivation] = {}
   353	    for axiom in Axiom:
   354	        if not system.holds(axiom):
   355	            continue
   356	        pillar = AXIOM_TO_PILLAR[axiom]
   357	        out[axiom] = Derivation(
   358	            axiom=axiom,
   359	            pillar=pillar,
   360	            form=realized_form(system, pillar),
   361	            practices=tuple(p for p in system.practices if p.solves is axiom),
   362	        )
   363	    return out
   364	
   365	
   366	# Proposition A ----------------------------------------------------------------------------
   367	
   368	
   369	@dataclass(frozen=True)
   370	class PropositionAResult:
   371	    """Outcome of checking Theorem A on one coded system.
   372	
   373	    ``holds`` is the structural predicate Struct(G): all six pillars realized AND every
   374	    required (D0) hyperarc coded as present in this system. ``counterexample`` is True when the
   375	    theorem's antecedent holds (persistent, Ax1..Ax6) but Struct(G) fails: a falsifier of
   376	    Theorem A (a missing pillar or a missing D0 relation).
   377	
   378	    ``strongly_connected`` (underlying digraph) and ``cascade_complete`` are computed on the
   379	    system's coded hyperarcs over its realized pillars. They are reported only and do NOT
   380	    enter ``holds``.
   381	    """
   382	
   383	    system: str
   384	    antecedent: bool
   385	    realized: frozenset[Pillar]
   386	    missing: frozenset[Pillar]
   387	    missing_dependencies: frozenset[ArcKey]
   388	    strongly_connected: bool
   389	    cascade_complete: bool
   390	    holds: bool
   391	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   392	
   393	    @property
   394	    def counterexample(self) -> bool:
   395	        return self.antecedent and not self.holds
   396	
   397	
   398	def check_proposition_a(
   399	    system: GovernanceSystem,
   400	    required: Iterable[Hyperarc | ArcKey] = D0,

2026-10-22T17:25:16.136299Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
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
/usr/local/bin/zsh -lc "sed -n '1,180p' model/beast_system/dynamics.py | nl -ba" in /Users/mlong/Documents/Development/the-beast-system
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
   122	    (Pillar.C, Pillar.I): -0.4,
   123	    (Pillar.C, Pillar.W): -0.3,
   124	}
   125	
   126	
   127	def negative_feedback_example(
   128	    weight: float = 0.2,
   129	    self_weight: float = 0.6,
   130	    feedback: Mapping[tuple[Pillar, Pillar], float] = NEGATIVE_FEEDBACK,
   131	) -> FeedbackExample:
   132	    """Positive dependency links do not guarantee persistence (source Section 5.3).
   133	
   134	    With every arc of the underlying dependency digraph (D0 plus all conditions) at ``weight``
   135	    and ``self_weight`` on the diagonal, rho > 1. Adding negative feedback on entries that carry no positive link leaves every
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

exec
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_dynamics_regimes.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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
/usr/local/bin/zsh -lc 'nl -ba model/tests/test_conversion.py' in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc "sed -n '181,340p' model/beast_system/dynamics.py | nl -ba -v181" in /Users/mlong/Documents/Development/the-beast-system
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

 succeeded in 0ms:
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

exec
/usr/local/bin/zsh -lc 'nl -ba model/beast_system/regimes.py' in /Users/mlong/Documents/Development/the-beast-system
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

2026-10-22T17:25:20.792486Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'python3 -m pytest -c /dev/null -q tests' in /Users/mlong/Documents/Development/the-beast-system/model
2026-10-22T17:25:43.596490Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 exited 1 in 2483ms:
2026-10-22 12:25:41.828 xcodebuild[42403:4004047]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:25:42.069 xcodebuild[42403:4004035] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-FuB0pH2r' (errno=Operation not permitted)
2026-10-22 12:25:42.645 xcodebuild[42415:4004264]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:25:42.760 xcodebuild[42415:4004262] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
/Applications/Xcode.app/Contents/Developer/usr/bin/python3: No module named pytest

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'command -v -a python3 pytest uv || true' in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 0ms:
zsh:1: command not found: -v

2026-10-22T17:25:48.504606Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'which -a python3 pytest uv 2>/dev/null || true' in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 0ms:
/usr/bin/python3
/Users/mlong/.pyenv/shims/python3
/opt/homebrew/bin/python3
/usr/local/bin/pytest
/Users/mlong/.pyenv/shims/pytest
/Users/mlong/.pyenv/shims/uv
/opt/homebrew/bin/uv

2026-10-22T17:25:51.014369Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc '/usr/local/bin/pytest -c /dev/null -q tests' in /Users/mlong/Documents/Development/the-beast-system/model
 exited 127 in 0ms:
zsh:1: /usr/local/bin/pytest: bad interpreter: /usr/local/opt/python/bin/python3.7: no such file or directory

2026-10-22T17:25:53.924951Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
2026-10-22T17:25:56.071653Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc '/opt/homebrew/bin/python3 -m pytest -c /dev/null -q tests' in /Users/mlong/Documents/Development/the-beast-system/model
 exited 1 in 0ms:
/opt/homebrew/opt/python@3.15/bin/python3.15: No module named pytest

2026-10-22T17:25:58.104183Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
2026-10-22T17:26:35.337949Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "PYTHONPATH=. /usr/bin/python3 -c 'import numpy as np; from beast_system.dynamics import negative_feedback_example; ex=negative_feedback_example(); print(np.__version__, ex.rho_positive, ex.rho_feedback)'" in /Users/mlong/Documents/Development/the-beast-system/model
2026-10-22T17:26:39.135065Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 exited 1 in 1653ms:
2026-10-22 12:26:37.598 xcodebuild[43059:4008041]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:26:37.734 xcodebuild[43059:4008040] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-3nfAvnlt' (errno=Operation not permitted)
2026-10-22 12:26:38.173 xcodebuild[43061:4008057]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 12:26:38.264 xcodebuild[43061:4008056] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/Users/mlong/Documents/Development/the-beast-system/model/beast_system/__init__.py", line 7, in <module>
    from .capture import (
  File "/Users/mlong/Documents/Development/the-beast-system/model/beast_system/capture.py", line 16, in <module>
    from .indices import (
  File "/Users/mlong/Documents/Development/the-beast-system/model/beast_system/indices.py", line 28, in <module>
    ShareLike = Mapping[str, float] | Sequence[float] | np.ndarray
TypeError: unsupported operand type(s) for |: 'types.GenericAlias' and 'types.GenericAlias'

codex
- [P1] `model/beast_system/indices.py:200` implements coalition overlap only for additive, mutually exclusive coalition partitions (`actor -> one coalition`). It cannot represent the required general \(\max_S \min(\kappa_m(S),\kappa_n(S))\), non-additive \(\kappa\), or overlapping candidate coalitions. `model/tests/test_indices.py:120` covers only this restricted case.
- [P2] `model/beast_system/indices.py:137` accepts matrices asymmetric within tolerance but does not symmetrize them. `integration_statistic` then uses one triangle while `integration_degrees` uses both, so an accepted matrix can violate symmetry and the claimed degree decomposition. The tests at `model/tests/test_indices.py:105` and `model/tests/test_indices.py:164` cover only exact symmetry.
- [P2] `model/beast_system/indices.py:189` does not enforce that hub size `k` is an integer: values such as `1.5` and `True` produce meaningless bounds instead of failing. `model/tests/test_indices.py:173` has no invalid-input coverage.
- [P2] `model/tests/test_conversion.py:80` tests the foothold theorem only with symmetric \(K\) and uniform \(\delta\), where left and right Perron vectors coincide. It therefore does not validate the implementation’s crucial left-Perron-vector orientation or bound for heterogeneous, asymmetric irreducible systems.

VERDICT: NEEDS_FIX
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
88,432
- [P1] `model/beast_system/indices.py:200` implements coalition overlap only for additive, mutually exclusive coalition partitions (`actor -> one coalition`). It cannot represent the required general \(\max_S \min(\kappa_m(S),\kappa_n(S))\), non-additive \(\kappa\), or overlapping candidate coalitions. `model/tests/test_indices.py:120` covers only this restricted case.
- [P2] `model/beast_system/indices.py:137` accepts matrices asymmetric within tolerance but does not symmetrize them. `integration_statistic` then uses one triangle while `integration_degrees` uses both, so an accepted matrix can violate symmetry and the claimed degree decomposition. The tests at `model/tests/test_indices.py:105` and `model/tests/test_indices.py:164` cover only exact symmetry.
- [P2] `model/beast_system/indices.py:189` does not enforce that hub size `k` is an integer: values such as `1.5` and `True` produce meaningless bounds instead of failing. `model/tests/test_indices.py:173` has no invalid-input coverage.
- [P2] `model/tests/test_conversion.py:80` tests the foothold theorem only with symmetric \(K\) and uniform \(\delta\), where left and right Perron vectors coincide. It therefore does not validate the implementation’s crucial left-Perron-vector orientation or bound for heterogeneous, asymmetric irreducible systems.

VERDICT: NEEDS_FIX
