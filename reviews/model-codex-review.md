Reading additional input from stdin...
2026-10-22T18:39:37.775709Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a164e9-5f03-7e81-8910-04e0b66e94f8
--------
user
Review only model/beast_system/{representation,uniqueness,necessity,pillars}.py and model/tests/{test_representation,test_uniqueness,test_necessity}.py. Do not explore elsewhere. FINAL scoped round on this diff only. (A) Round-9 items: [P1] canonical_form not a complete invariant of p_equal (tolerance vs exact): find_bijection now compares Q, weights, kappa exactly after the same 12-decimal quantization _r as canonical_form (test_p_equal_and_canonical_form_use_one_normalization). [P1] canonical_form not total (max_branch guard): now individualization-refinement (_refine, _interchangeable shortcut, search over the first smallest non-singleton class, lexicographic minimum), no guard (test_canonical_form_is_total_on_symmetric_structures: 9-cycle vs relabeling and vs 4+5 cycles). (B) Part VII alignment: witness_record with a, b performing only the witness pillars and c the rest; drop witnesses add a retained pillar l0 with (1/2,1/2) (Almond l0 = P); Aristotle/Weber witnesses add I with (1/2,1/2); merge witnesses unchanged in shares (tests assert equal actor sets and role maps); bijective coarsenings are P-preserving (test_bijective_coarsenings_are_p_preserving, Thm 7.8 for coarsenings); starred axiom clauses for Ax3, Ax4, Ax5, Ax6; R1_AX4_MODEL as AXIOM_INDEPENDENCE[Ax4] (innate rules, fine d >= g on defiance, ell = 0, Impl_I fails); PROP_4_4A_MODEL and PROP_4_4A_VARIANT (struct True, interdependent False, no arc into W, OR-hyperarc {I,C}->J present without single I->J or C->J); is_admissible (F5) tested on hard cases, corners and negative cases; docstring renumbering (Cor 5.5, Assumptions 5.6 to 5.9, Thm 5.10, Prop 5.11, Remark 5.12, Thm 7.4, Prop 7.5, Thm 7.8, Prop 10.1). Confirm the round-9 items are resolved, check canonical_form soundness and completeness, and flag defects in this diff. Output the findings list (with P1/P2/P3 severity) and the VERDICT line only. End with VERDICT: PASS or VERDICT: NEEDS_FIX.
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T18:39:39.205965Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T18:39:39.863186Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
I’ll inspect exactly the seven named files and the scoped diff, then run only the three named test modules. I’ll use the code-review skill because this is a final defect-focused review.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '1,240p' /Users/mlong/.codex/plugins/cache/claude-cowork/engineering/1.1.0/skills/code-review/SKILL.md && rg -n \"the-beast-system|round-9|canonical_form|Part VII\" /Users/mlong/.codex/memories/MEMORY.md" in /Users/mlong/Documents/Development/the-beast-system
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
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "wc -l 'model/beast_system/representation.py' 'model/beast_system/uniqueness.py' 'model/beast_system/necessity.py' 'model/beast_system/pillars.py' 'model/tests/test_representation.py' 'model/tests/test_uniqueness.py' 'model/tests/test_necessity.py'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     587 model/beast_system/representation.py
     492 model/beast_system/uniqueness.py
     770 model/beast_system/necessity.py
     184 model/beast_system/pillars.py
     303 model/tests/test_representation.py
     356 model/tests/test_uniqueness.py
     388 model/tests/test_necessity.py
    3080 total

exec
/usr/local/bin/zsh -lc "git diff --stat -- 'model/beast_system/representation.py' 'model/beast_system/uniqueness.py' 'model/beast_system/necessity.py' 'model/beast_system/pillars.py' 'model/tests/test_representation.py' 'model/tests/test_uniqueness.py' 'model/tests/test_necessity.py'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 1661ms:
2026-10-22 13:39:56.531 xcodebuild[97714:4330664]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:39:56.672 xcodebuild[97714:4330663] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-rNHHSACV' (errno=Operation not permitted)
2026-10-22 13:39:57.143 xcodebuild[97716:4330686]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:39:57.239 xcodebuild[97716:4330685] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "git diff HEAD --stat -- 'model/beast_system/representation.py' 'model/beast_system/uniqueness.py' 'model/beast_system/necessity.py' 'model/beast_system/pillars.py' 'model/tests/test_representation.py' 'model/tests/test_uniqueness.py' 'model/tests/test_necessity.py'" in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc "git diff --cached --stat -- 'model/beast_system/representation.py' 'model/beast_system/uniqueness.py' 'model/beast_system/necessity.py' 'model/beast_system/pillars.py' 'model/tests/test_representation.py' 'model/tests/test_uniqueness.py' 'model/tests/test_necessity.py'" in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc 'git log -5 --oneline --decorate' in /Users/mlong/Documents/Development/the-beast-system
 exited 128 in 1710ms:
2026-10-22 13:40:02.619 xcodebuild[97755:4330937]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:40:02.724 xcodebuild[97755:4330934] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-qThcMKu8' (errno=Operation not permitted)
2026-10-22 13:40:03.219 xcodebuild[97760:4330970]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:40:03.330 xcodebuild[97760:4330967] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
fatal: your current branch 'main' does not have any commits yet

 exited 128 in 1710ms:
2026-10-22 13:40:02.619 xcodebuild[97754:4330938]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:40:02.724 xcodebuild[97754:4330932] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-m6EyqIFD' (errno=Operation not permitted)
2026-10-22 13:40:03.219 xcodebuild[97762:4330971]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:40:03.330 xcodebuild[97762:4330966] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
fatal: bad revision 'HEAD'

 succeeded in 1710ms:
2026-10-22 13:40:02.620 xcodebuild[97756:4330936]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:40:02.724 xcodebuild[97756:4330933] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-QbQSpDDJ' (errno=Operation not permitted)
2026-10-22 13:40:03.219 xcodebuild[97761:4330969]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:40:03.330 xcodebuild[97761:4330965] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/pillars.py | sed -n '1,240p'" in /Users/mlong/Documents/Development/the-beast-system
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
    64	    """Working axioms about collective life (KB Section 4.2; notation.md CENTRAL THESIS).
    65	
    66	    Statements follow Part VII's starred versions (Ax3*, Ax4*, Ax5*, Ax6* add clauses).
    67	    """
    68	
    69	    Ax1 = "scarcity"
    70	    Ax2 = "plurality"
    71	    Ax3 = "generality"
    72	    Ax4 = "coordination"
    73	    Ax5 = "defection"
    74	    Ax6 = "maintenance"
    75	
    76	    @property
    77	    def label(self) -> str:
    78	        return self.value
    79	
    80	    @property
    81	    def statement(self) -> str:
    82	        return _STATEMENTS[self]
    83	
    84	    @property
    85	    def pillar(self) -> Pillar:
    86	        """The pillar whose function solves the problem this axiom generates."""
    87	        return AXIOM_TO_PILLAR[self]
    88	
    89	
    90	_STATEMENTS = {
    91	    Axiom.Ax1: "resources are finite and claims on them conflict",
    92	    Axiom.Ax2: "members' preferences diverge and some collective choices must be made",
    93	    Axiom.Ax3: (
    94	        "rules are general, cases are particular, and disputes arise; each residual dispute "
    95	        "reaches a disposition at a finite time; the loser complies iff ell + sigma >= g, "
    96	        "with ell > 0 only via a legitimation practice and sigma > 0 only via a sanction "
    97	        "practice"
    98	    ),
    99	    Axiom.Ax4: (
   100	        "compliance and cooperation need shared beliefs or common knowledge; settlement "
   101	        "procedures belong to the common-knowledge rule system; entrants are parties to "
   102	        "conflicts in infinitely many periods"
   103	    ),
   104	    Axiom.Ax5: "some members sometimes break rules; members best-respond",
   105	    Axiom.Ax6: (
   106	        "the group and its institutions consume resources that someone produces; every "
   107	        "practice is performed by agents whose consumption is counted, in a period only if "
   108	        "that consumption is met"
   109	    ),
   110	}
   111	
   112	#: Axiom -> pillar map (KB Section 4.2 table, 'Yields' column). It is a bijection.
   113	AXIOM_TO_PILLAR: dict[Axiom, Pillar] = {
   114	    Axiom.Ax1: Pillar.F,
   115	    Axiom.Ax2: Pillar.P,
   116	    Axiom.Ax3: Pillar.J,
   117	    Axiom.Ax4: Pillar.I,
   118	    Axiom.Ax5: Pillar.C,
   119	    Axiom.Ax6: Pillar.W,
   120	}
   121	PILLAR_TO_AXIOM: dict[Pillar, Axiom] = {p: a for a, p in AXIOM_TO_PILLAR.items()}
   122	
   123	
   124	class IncidenceAxiom(Enum):
   125	    """Incidence axioms X_k (Part VII Assumptions 5.6 to 5.9: X1, X2, X3, X5).
   126	
   127	    X_k states that the problem of Ax_k arises about the inputs or rules of a named pillar,
   128	    which generates the arc pillar(Ax_k) -> that pillar. Each is an empirical premise with a
   129	    stated falsifier, not a logical truth.
   130	    """
   131	
   132	    X1 = "contested inputs"
   133	    X2 = "changing environment"
   134	    X3 = "open-textured allocation rules"
   135	    X5 = "tempting allocation rules"
   136	
   137	    @property
   138	    def label(self) -> str:
   139	        return self.value
   140	
   141	    @property
   142	    def base(self) -> Axiom:
   143	        """The axiom whose problem the incidence locates."""
   144	        return _INCIDENCE[self][0]
   145	
   146	    @property
   147	    def target(self) -> Pillar:
   148	        """The pillar whose inputs or rules the problem arises about."""
   149	        return _INCIDENCE[self][1]
   150	
   151	    @property
   152	    def statement(self) -> str:
   153	        return _INCIDENCE[self][2]
   154	
   155	    @property
   156	    def falsifier(self) -> str:
   157	        return _INCIDENCE[self][3]
   158	
   159	
   160	_INCIDENCE: dict[IncidenceAxiom, tuple[Axiom, Pillar, str, str]] = {
   161	    IncidenceAxiom.X1: (
   162	        Axiom.Ax1, Pillar.W,
   163	        "productive activity uses inputs under conflicting claims, used only under an "
   164	        "anticipable assignment",
   165	        "a persistent collective whose productive inputs never meet conflicting claims",
   166	    ),
   167	    IncidenceAxiom.X2: (
   168	        Axiom.Ax2, Pillar.F,
   169	        "the environment changes infinitely often (Part II Ass 3.2) and each change creates "
   170	        "conflicts no prior settlement procedure can settle",
   171	        "a persistent collective whose prior settlement procedures settle every new conflict",
   172	    ),
   173	    IncidenceAxiom.X3: (
   174	        Axiom.Ax3, Pillar.F,
   175	        "some settlement procedure has open texture and generates infinitely many residual "
   176	        "disputes",
   177	        "settlement procedures that leave only finitely many residual disputes",
   178	    ),
   179	    IncidenceAxiom.X5: (
   180	        Axiom.Ax5, Pillar.F,
   181	        "Ax5 holds for some settlement procedure",
   182	        "no member ever breaks any settlement procedure",
   183	    ),
   184	}

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/representation.py | sed -n '1,650p'" in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/uniqueness.py | sed -n '1,560p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Representation theorem and minimality (Part VII Thm 7.4, Prop 7.5).
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
    77	    """The coded record of a governance system: practices plus index inputs (Part VII F6,
    78	    well-formed record; Thm 7.4 assumes it).
    79	
    80	    Well-formedness (enforced): ``shares`` has a probability vector for EVERY implemented
    81	    pillar and none for an unimplemented one, each supported on the performers of that
    82	    pillar's practices; Q has one value in [0, 1] per pillar; ``weights`` (None = 1/M each)
    83	    are non-negative and sum to 1; ``coalitions`` maps a non-empty coalition (frozenset of
    84	    actors) to kappa_m(S) in [0, 1] (None = singleton coalitions, kappa_m({v}) = s^m_v).
    85	    On this domain F2 and F3 hold for every image, so the theorem's content rests on F1, F4.
    86	    """
    87	
    88	    system: GovernanceSystem
    89	    shares: Mapping[Pillar, Mapping[str, float]]
    90	    contestability: Mapping[Pillar, float]
    91	    weights: Mapping[Pillar, float] | None = None
    92	    coalitions: Mapping[frozenset[str], Mapping[Pillar, float]] | None = None
    93	    links: tuple[CaptureLink, ...] = ()
    94	
    95	    def __post_init__(self) -> None:
    96	        roles = role_map(self.system)
    97	        implemented = {m for m in PILLARS if realized_form(self.system, m) is not None}
    98	        if any(not isinstance(m, Pillar) for m in self.shares):
    99	            raise TypeError("share keys must be Pillars")
   100	        if set(self.shares) != implemented:
   101	            raise ValueError("shares must cover exactly the implemented pillars")
   102	        for m, s in self.shares.items():
   103	            vals = [float(v) for v in s.values()]
   104	            if not vals or any(not math.isfinite(v) or v < 0 for v in vals):
   105	                raise ValueError(f"shares[{m.name}] must be finite and non-negative")
   106	            if abs(sum(vals) - 1.0) > _ATOL:
   107	                raise ValueError(f"shares[{m.name}] must sum to 1")
   108	            for actor, v in s.items():
   109	                if float(v) > 0 and m not in roles.get(actor, frozenset()):
   110	                    raise ValueError(f"{actor!r} has share in {m.name} but performs no practice")
   111	        if set(self.contestability) != set(PILLARS):
   112	            raise ValueError("contestability must give one value per pillar")
   113	        for m in PILLARS:
   114	            validate_unit_interval(self.contestability[m], f"Q[{m.name}]")
   115	        object.__setattr__(self, "weights", validate_weights(self.weights))
   116	        if self.coalitions is not None:
   117	            known = set(roles) | {a for s in self.shares.values() for a in s}
   118	            known |= {e for lk in self.links for e in (lk.source, lk.target)}
   119	            for members, row in self.coalitions.items():
   120	                if not isinstance(members, frozenset) or not members:
   121	                    raise TypeError("coalition keys must be non-empty frozensets of actors")
   122	                if any(not isinstance(v, str) for v in members):
   123	                    raise TypeError("coalition members must be actor names (str)")
   124	                if not members <= known:
   125	                    raise ValueError(f"coalition {sorted(members)} names unknown actors")
   126	                if any(not isinstance(m, Pillar) for m in row):
   127	                    raise TypeError("kappa keys must be Pillars")
   128	                for m, x in row.items():
   129	                    validate_unit_interval(x, f"kappa[{sorted(members)}][{m.name}]")
   130	
   131	
   132	def minimal_record(system: GovernanceSystem, q: float = 0.5) -> CodedRecord:
   133	    """Record with PLACEHOLDER index inputs: uniform shares over performers, Q = q everywhere.
   134	
   135	    For systems such as the hard cases, which are coded only by practices. Representability
   136	    does not depend on these values; preserved quantities computed from them are not data.
   137	    """
   138	    roles = role_map(system)
   139	    shares = {}
   140	    for m in PILLARS:
   141	        hs = sorted(a for a, ps in roles.items() if m in ps)
   142	        if hs:
   143	            shares[m] = {a: 1.0 / len(hs) for a in hs}
   144	    return CodedRecord(system, shares, {m: q for m in PILLARS})
   145	
   146	
   147	def record_from_polity(
   148	    polity: Polity, coalitions: Mapping[frozenset[str], Mapping[Pillar, float]] | None = None
   149	) -> CodedRecord:
   150	    """The coded record of a Polity (shares normalized, zero-share pillars of unimplemented
   151	    functions omitted, weights validated)."""
   152	    implemented = {m for m in PILLARS if realized_form(polity.system, m) is not None}
   153	    return CodedRecord(
   154	        system=polity.system,
   155	        shares={m: s for m, s in polity.normalized_shares.items() if m in implemented},
   156	        contestability=polity.contestability,
   157	        weights=polity.weights,
   158	        coalitions=coalitions,
   159	        links=polity.capture_links,
   160	    )
   161	
   162	
   163	def represent(record: CodedRecord) -> FormalizedStructure:
   164	    """The profile map pi: G -> F_G.
   165	
   166	    V = practice performers plus actors named in shares or links (roles come only from
   167	    practices). m in rho(v) iff v performs a practice of pillar m and m is implemented.
   168	    Shares, Q, weights, coalitions and links are copied; D = arcs generated from G's axioms.
   169	    Layers: a^m_ij = s^m_i for i != j, so out-strength shares reproduce s^m.
   170	    """
   171	    system = record.system
   172	    implemented = {m for m in PILLARS if realized_form(system, m) is not None}
   173	    performers = role_map(system)
   174	    named = {a for s in record.shares.values() for a in s}
   175	    named |= {e for link in record.links for e in (link.source, link.target)}
   176	    actors = tuple(sorted(set(performers) | named))
   177	    roles = {
   178	        v: frozenset(m.name for m in performers.get(v, frozenset()) if m in implemented)
   179	        for v in actors
   180	    }
   181	    shares = {
   182	        m.name: {v: float(record.shares.get(m, {}).get(v, 0.0)) for v in actors}
   183	        for m in PILLARS
   184	    }
   185	    idx = {v: k for k, v in enumerate(actors)}
   186	    layers = {}
   187	    for m in M_LABELS:
   188	        arr = np.zeros((len(actors), len(actors)))
   189	        for v, s in shares[m].items():
   190	            arr[idx[v], :] = s
   191	        np.fill_diagonal(arr, 0.0)
   192	        layers[m] = arr
   193	    weights = record.weights
   194	    if record.coalitions is None:
   195	        kappa = {frozenset({v}): {m: shares[m][v] for m in M_LABELS} for v in actors}
   196	    else:
   197	        kappa = {members: {m.name: float(row.get(m, 0.0)) for m in PILLARS}
   198	                 for members, row in record.coalitions.items()}
   199	    links = frozenset((lk.source, lk.target, lk.pillar.name) for lk in record.links if lk.holds)
   200	    arcs = frozenset(
   201	        (frozenset(t.name for t in tail), head.name)
   202	        for tail, head in generate_dependencies(system)
   203	    )
   204	    return FormalizedStructure(
   205	        actors=actors, pillars=M_LABELS, roles=roles, layers=layers, shares=shares,
   206	        contestability={m.name: float(record.contestability[m]) for m in PILLARS},
   207	        weights={m.name: float(weights[m]) for m in PILLARS},
   208	        kappa=kappa, links=links, arcs=arcs,
   209	    )
   210	
   211	
   212	# Formalized class --------------------------------------------------------------------------
   213	
   214	
   215	def _underlying(arcs: Iterable[LabelArc], labels: Iterable[Label]) -> dict[Label, set[Label]]:
   216	    adj: dict[Label, set[Label]] = {m: set() for m in labels}
   217	    for tail, head in arcs:
   218	        for t in tail:
   219	            adj.setdefault(t, set()).add(head)
   220	    return adj
   221	
   222	
   223	def _closure(arcs: Iterable[LabelArc], start: Iterable[Label]) -> frozenset[Label]:
   224	    """cl(S) on string labels (same rule as necessity.cascade_closure)."""
   225	    arcs = list(arcs)
   226	    closed = set(start)
   227	    changed = True
   228	    while changed:
   229	        changed = False
   230	        for tail, head in arcs:
   231	            if head not in closed and tail <= closed:
   232	                closed.add(head)
   233	                changed = True
   234	    return frozenset(closed)
   235	
   236	
   237	def _cascade_complete(arcs: Iterable[LabelArc], labels: tuple[Label, ...]) -> bool:
   238	    keep = frozenset(labels)
   239	    inside = [(t, h) for t, h in arcs if h in keep and t <= keep]
   240	    return bool(keep) and all(_closure(inside, {n}) >= keep for n in keep)
   241	
   242	
   243	@dataclass(frozen=True)
   244	class ClassMembership:
   245	    """Conditions F1..F4 of the formalized class."""
   246	
   247	    f1: bool
   248	    f2: bool
   249	    f3: bool
   250	    f4: bool
   251	
   252	    @property
   253	    def holds(self) -> bool:
   254	        return self.f1 and self.f2 and self.f3 and self.f4
   255	
   256	
   257	def well_formed(F: FormalizedStructure) -> bool:
   258	    """Domain check: every component is indexed by exactly V and the pillar labels, layers
   259	    are |V| x |V| and finite, every number is finite, and every hyperarc (T, h) has a
   260	    non-empty tail of labels and a label head outside T."""
   261	    actors, labels = set(F.actors), set(F.pillars)
   262	    if len(actors) != len(F.actors) or len(labels) != len(F.pillars):
   263	        return False
   264	    if set(F.roles) != actors or any(not ps <= labels for ps in F.roles.values()):
   265	        return False
   266	    if set(F.shares) != labels or any(set(F.shares[m]) != actors for m in labels):
   267	        return False
   268	    if set(F.layers) != labels or set(F.contestability) != labels or set(F.weights) != labels:
   269	        return False
   270	    n = len(F.actors)
   271	    for m in labels:
   272	        arr = np.asarray(F.layers[m], dtype=float)
   273	        if arr.shape != (n, n) or not np.all(np.isfinite(arr)):
   274	            return False
   275	    nums = [*(x for m in labels for x in F.shares[m].values()), *F.contestability.values(),
   276	            *F.weights.values(), *(x for r in F.kappa.values() for x in r.values())]
   277	    if not all(math.isfinite(float(x)) for x in nums):
   278	        return False
   279	    for members, row in F.kappa.items():
   280	        if not isinstance(members, frozenset) or not members or not members <= actors:
   281	            return False
   282	        if not set(row) <= labels:
   283	            return False
   284	    for tail, head in F.arcs:
   285	        if not isinstance(tail, frozenset) or not tail or not tail <= labels:
   286	            return False
   287	        if head not in labels or head in tail:
   288	            return False
   289	    return all(a in actors and b in actors and m in labels for a, b, m in F.links)
   290	
   291	
   292	def in_formalized_class(F: FormalizedStructure) -> ClassMembership:
   293	    """F1 every layer has a holder; F2 s^m a probability vector on holders of m, a^m_ij in
   294	    [0, 1] and > 0 only if i holds m; F3 Q, omega, kappa in range (omega summing to 1), link
   295	    endpoints in V; F4 D contains D0 and is strongly connected and cascade-complete.
   296	
   297	    A structure that is not ``well_formed`` (or whose labels are not the six pillars) fails
   298	    every condition.
   299	    """
   300	    if F.pillars != M_LABELS or not F.actors or not well_formed(F):
   301	        return ClassMembership(False, False, False, False)
   302	    f1 = all(F.holders(m) for m in F.pillars)
   303	    f2 = True
   304	    for m in F.pillars:
   305	        s = np.array([F.shares[m][v] for v in F.actors], dtype=float)
   306	        holders = F.holders(m)
   307	        arr = np.asarray(F.layers[m], dtype=float)
   308	        on_holders = all(F.shares[m][v] == 0.0 or v in holders for v in F.actors)
   309	        rows_ok = all(not arr[i].any() or v in holders for i, v in enumerate(F.actors))
   310	        if (s.min() < 0 or abs(s.sum() - 1.0) > _ATOL or not on_holders or not rows_ok
   311	                or arr.min() < 0.0 or arr.max() > 1.0):
   312	            f2 = False
   313	    vals = [*F.contestability.values(), *F.weights.values(),
   314	            *(x for row in F.kappa.values() for x in row.values())]
   315	    f3 = (all(0.0 <= float(x) <= 1.0 for x in vals)
   316	          and abs(sum(F.weights.values()) - 1.0) <= _ATOL)
   317	    f4 = (
   318	        D0_LABELS <= F.arcs
   319	        and is_strongly_connected(_underlying(F.arcs, F.pillars), set(F.pillars))
   320	        and _cascade_complete(F.arcs, F.pillars)
   321	    )
   322	    return ClassMembership(f1, f2, f3, f4)
   323	
   324	
   325	def representable(record: CodedRecord) -> bool:
   326	    """G is representable iff its image F_G lies in the formalized class."""
   327	    return in_formalized_class(represent(record)).holds
   328	
   329	
   330	# Preserved quantities and A-equivalence ----------------------------------------------------
   331	
   332	
   333	@dataclass(frozen=True)
   334	class PreservedQuantities:
   335	    H: dict[Label, float]
   336	    U: float
   337	    C: dict[frozenset[Label], float]
   338	    I: float  # noqa: E741  (integration statistic, math cal I)
   339	    cap: bool
   340	    inter: bool
   341	
   342	
   343	def preserved_quantities(
   344	    F: FormalizedStructure, thresholds: CaptureThresholds = CaptureThresholds()
   345	) -> PreservedQuantities:
   346	    """H_m, U, C_mn (coalition overlap), I, Cap (Proposition B) and Inter on F's own labels."""
   347	    H = {m: hhi([F.shares[m].get(v, 0.0) for v in F.actors]) if F.holders(m) else 0.0
   348	         for m in F.pillars}
   349	    U = sum(F.weights[m] * H[m] * (1.0 - F.contestability[m]) for m in F.pillars)
   350	    pairs = list(itertools.combinations(F.pillars, 2))
   351	    C = {frozenset((m, n)): max((min(row.get(m, 0.0), row.get(n, 0.0))
   352	                                 for row in F.kappa.values()), default=0.0)
   353	         for m, n in pairs}
   354	    I = sum(C.values()) / len(pairs) if pairs else 0.0  # noqa: E741
   355	    cap = U >= thresholds.u_star and I >= thresholds.i_star and bool(F.links)
   356	    inter = (is_strongly_connected(_underlying(F.arcs, F.pillars), set(F.pillars))
   357	             and _cascade_complete(F.arcs, F.pillars))
   358	    return PreservedQuantities(H, float(U), C, float(I), cap, inter)
   359	
   360	
   361	def _r(x: float) -> float:
   362	    return round(float(x), _ROUND) + 0.0
   363	
   364	
   365	def _same(a: float, b: float) -> bool:
   366	    return abs(a - b) <= _ATOL
   367	
   368	
   369	def _actor_signature(F: FormalizedStructure, k: int, with_layers: bool) -> tuple:
   370	    v = F.actors[k]
   371	    sig = (
   372	        tuple(sorted(F.roles[v])),
   373	        tuple(_r(F.shares[m][v]) for m in F.pillars),
   374	        tuple(sorted((m, a == v, b == v) for a, b, m in F.links if v in (a, b))),
   375	        tuple(sorted(tuple(_r(r.get(m, 0.0)) for m in F.pillars)
   376	                     for S, r in F.kappa.items() if v in S)),
   377	    )
   378	    if with_layers:
   379	        sig += tuple((tuple(sorted(_r(x) for x in F.layers[m][k])),
   380	                      tuple(sorted(_r(x) for x in F.layers[m][:, k]))) for m in F.pillars)
   381	    return sig
   382	
   383	
   384	def find_bijection(F: FormalizedStructure, G: FormalizedStructure,
   385	                   with_layers: bool) -> dict[str, str] | None:
   386	    """An actor bijection phi: V_F -> V_G under which roles, shares, Q, omega, kappa
   387	    (transported: kappa_F(S) = kappa_G(phi(S))), links and D agree, and, if ``with_layers``,
   388	    every layer entry. None if there is none.
   389	
   390	    Numbers are compared EXACTLY after quantization to 12 decimals (``_r``), the same
   391	    normalization the canonical form uses, so equality is an equivalence relation.
   392	
   393	    Backtracking within classes of equal actor signatures; the identity on names is tried
   394	    first. Both structures must be ``well_formed``.
   395	    """
   396	    if not (well_formed(F) and well_formed(G)):
   397	        return None
   398	    if F.pillars != G.pillars or len(F.actors) != len(G.actors) or F.arcs != G.arcs:
   399	        return None
   400	    if any(_r(F.contestability[m]) != _r(G.contestability[m])
   401	           or _r(F.weights[m]) != _r(G.weights[m]) for m in F.pillars):
   402	        return None
   403	    if len(F.kappa) != len(G.kappa) or len(F.links) != len(G.links):
   404	        return None
   405	    sig_f = [_actor_signature(F, k, with_layers) for k in range(len(F.actors))]
   406	    sig_g = [_actor_signature(G, k, with_layers) for k in range(len(G.actors))]
   407	    if sorted(sig_f) != sorted(sig_g):
   408	        return None
   409	    gi = {v: k for k, v in enumerate(G.actors)}
   410	    fi = {v: k for k, v in enumerate(F.actors)}
   411	    order = sorted(range(len(F.actors)), key=lambda k: sig_f[k])
   412	    assign: dict[int, int] = {}
   413	    used: set[int] = set()
   414	
   415	    def consistent(i: int, j: int) -> bool:
   416	        if with_layers:
   417	            for i2, j2 in assign.items():
   418	                for m in F.pillars:
   419	                    if (_r(F.layers[m][i, i2]) != _r(G.layers[m][j, j2])
   420	                            or _r(F.layers[m][i2, i]) != _r(G.layers[m][j2, j])):
   421	                        return False
   422	        mapped = {**assign, i: j}
   423	        for a, b, m in F.links:
   424	            ia, ib = fi[a], fi[b]
   425	            if ia in mapped and ib in mapped:
   426	                if (G.actors[mapped[ia]], G.actors[mapped[ib]], m) not in G.links:
   427	                    return False
   428	        return True
   429	
   430	    def kappa_ok() -> bool:
   431	        to_g = {F.actors[i]: G.actors[j] for i, j in assign.items()}
   432	        for S, row in F.kappa.items():
   433	            other = G.kappa.get(frozenset(to_g[v] for v in S))
   434	            if other is None or set(other) != set(row):
   435	                return False
   436	            if any(_r(row[m]) != _r(other[m]) for m in row):
   437	                return False
   438	        return True
   439	
   440	    def search(pos: int) -> bool:
   441	        if pos == len(order):
   442	            return kappa_ok()
   443	        i = order[pos]
   444	        cands = [j for j in range(len(G.actors)) if j not in used and sig_g[j] == sig_f[i]]
   445	        pref = gi.get(F.actors[i])
   446	        if pref in cands:
   447	            cands.remove(pref)
   448	            cands.insert(0, pref)
   449	        for j in cands:
   450	            if consistent(i, j):
   451	                assign[i] = j
   452	                used.add(j)
   453	                if search(pos + 1):
   454	                    return True
   455	                del assign[i]
   456	                used.discard(j)
   457	        return False
   458	
   459	    if not search(0):
   460	        return None
   461	    return {F.actors[i]: G.actors[j] for i, j in assign.items()}
   462	
   463	
   464	def equivalent_A(F: FormalizedStructure, G: FormalizedStructure) -> bool:  # noqa: N802
   465	    """F and G agree on roles, shares, Q, omega, kappa, links and D under an actor bijection
   466	    (layers not compared; see ``uniqueness.p_equal`` for the version with layers)."""
   467	    return find_bijection(F, G, with_layers=False) is not None
   468	
   469	
   470	# Coarsenings (minimality) ------------------------------------------------------------------
   471	
   472	
   473	def drop(F: FormalizedStructure, m: Label) -> FormalizedStructure:
   474	    """Delete pillar m: its layer, shares, Q, kappa column and every hyperarc involving m.
   475	
   476	    Remaining weights are renormalized to sum 1.
   477	    """
   478	    if m not in F.pillars:
   479	        raise ValueError(f"unknown pillar {m!r}")
   480	    keep = tuple(p for p in F.pillars if p != m)
   481	    total = sum(F.weights[p] for p in keep)
   482	    weights = {p: (F.weights[p] / total if total > 0 else 1.0 / len(keep)) for p in keep}
   483	    return FormalizedStructure(
   484	        actors=F.actors, pillars=keep,
   485	        roles={v: ps - {m} for v, ps in F.roles.items()},
   486	        layers={p: F.layers[p] for p in keep},
   487	        shares={p: dict(F.shares[p]) for p in keep},
   488	        contestability={p: F.contestability[p] for p in keep},
   489	        weights=weights,
   490	        kappa={s: {p: row.get(p, 0.0) for p in keep} for s, row in F.kappa.items()},
   491	        links=frozenset(lk for lk in F.links if lk[2] != m),
   492	        arcs=frozenset((t, h) for t, h in F.arcs if h != m and m not in t),
   493	    )
   494	
   495	
   496	def merge(F: FormalizedStructure, m: Label, n: Label, lam: float) -> FormalizedStructure:
   497	    """Replace m, n by one pillar 'm+n': holders united, shares, layers, Q and kappa mixed with
   498	    weight lam on m; omega_m + omega_n; arcs relabeled, self-loops removed."""
   499	    if m == n or m not in F.pillars or n not in F.pillars:
   500	        raise ValueError("merge needs two distinct existing pillars")
   501	    lam = validate_unit_interval(lam, "lam")
   502	    new = f"{m}+{n}"
   503	    keep = tuple(new if p == m else p for p in F.pillars if p != n)
   504	    relabel = lambda p: new if p in (m, n) else p  # noqa: E731
   505	
   506	    def mix(a: float, b: float) -> float:
   507	        return lam * a + (1.0 - lam) * b
   508	
   509	    shares = {p: dict(F.shares[p]) for p in keep if p != new}
   510	    shares[new] = {v: mix(F.shares[m].get(v, 0.0), F.shares[n].get(v, 0.0)) for v in F.actors}
   511	    layers = {p: F.layers[p] for p in keep if p != new}
   512	    layers[new] = lam * F.layers[m] + (1.0 - lam) * F.layers[n]
   513	    contest = {p: F.contestability[p] for p in keep if p != new}
   514	    contest[new] = mix(F.contestability[m], F.contestability[n])
   515	    weights = {p: F.weights[p] for p in keep if p != new}
   516	    weights[new] = F.weights[m] + F.weights[n]
   517	    kappa = {}
   518	    for s, row in F.kappa.items():
   519	        r = {p: row.get(p, 0.0) for p in keep if p != new}
   520	        r[new] = mix(row.get(m, 0.0), row.get(n, 0.0))
   521	        kappa[s] = r
   522	    arcs = set()
   523	    for t, h in F.arcs:
   524	        t2, h2 = frozenset(relabel(x) for x in t), relabel(h)
   525	        if h2 not in t2:
   526	            arcs.add((t2, h2))
   527	    return FormalizedStructure(
   528	        actors=F.actors, pillars=keep,
   529	        roles={v: frozenset(relabel(p) for p in ps) for v, ps in F.roles.items()},
   530	        layers=layers, shares=shares, contestability=contest, weights=weights, kappa=kappa,
   531	        links=frozenset((a, b, relabel(p)) for a, b, p in F.links),
   532	        arcs=frozenset(arcs),
   533	    )
   534	
   535	
   536	def structurally_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   537	    """Equality of every component with the identity on actor names (floats within 1e-9)."""
   538	    if not (well_formed(F) and well_formed(G)):
   539	        return False
   540	    if (F.actors, F.pillars, F.links, F.arcs) != (G.actors, G.pillars, G.links, G.arcs):
   541	        return False
   542	    if any(F.roles[v] != G.roles[v] for v in F.actors) or set(F.kappa) != set(G.kappa):
   543	        return False
   544	    return (
   545	        all(_same(F.shares[m][v], G.shares[m][v]) for m in F.pillars for v in F.actors)
   546	        and all(np.allclose(F.layers[m], G.layers[m], atol=_ATOL, rtol=0) for m in F.pillars)
   547	        and all(_same(F.contestability[m], G.contestability[m]) for m in F.pillars)
   548	        and all(_same(F.weights[m], G.weights[m]) for m in F.pillars)
   549	        and all(set(F.kappa[S]) == set(G.kappa[S])
   550	                and all(_same(F.kappa[S][m], G.kappa[S][m]) for m in F.kappa[S])
   551	                for S in F.kappa)
   552	    )
   553	
   554	
   555	D_STAR_LABELS: frozenset[LabelArc] = frozenset(
   556	    (frozenset(t.name for t in tail), head.name) for tail, head in D_STAR_KEYS
   557	)
   558	
   559	
   560	def make_structure(
   561	    shares: Mapping[Label, Mapping[str, float]],
   562	    contestability: Mapping[Label, float],
   563	    weights: Mapping[Label, float] | None = None,
   564	    kappa: Mapping[frozenset[str], Mapping[Label, float]] | None = None,
   565	    links: Iterable[tuple[str, str, Label]] = (),
   566	    arcs: Iterable[LabelArc] = D_STAR_LABELS,
   567	) -> FormalizedStructure:
   568	    """Build F directly: holders are actors with positive share, a^m_ij = s^m_i (i != j),
   569	    singleton coalitions by default. Used for the minimality fixtures."""
   570	    pillars = tuple(shares)
   571	    actors = tuple(sorted({v for s in shares.values() for v in s}))
   572	    full = {m: {v: float(shares[m].get(v, 0.0)) for v in actors} for m in pillars}
   573	    roles = {v: frozenset(m for m in pillars if full[m][v] > 0) for v in actors}
   574	    layers = {}
   575	    for m in pillars:
   576	        arr = np.tile(np.array([full[m][v] for v in actors])[:, None], (1, len(actors)))
   577	        np.fill_diagonal(arr, 0.0)
   578	        layers[m] = arr
   579	    if kappa is None:
   580	        kappa = {frozenset({v}): {m: full[m][v] for m in pillars} for v in actors}
   581	    return FormalizedStructure(
   582	        actors=actors, pillars=pillars, roles=roles, layers=layers, shares=full,
   583	        contestability=dict(contestability),
   584	        weights=dict(weights) if weights else {m: 1.0 / len(pillars) for m in pillars},
   585	        kappa={s: dict(r) for s, r in kappa.items()},
   586	        links=frozenset(links), arcs=frozenset(arcs),
   587	    )

 succeeded in 0ms:
     1	"""Uniqueness and novelty: coarsenings, factorization through Phi, predecessor encodings.
     2	
     3	Part VII Def 7.6 (Abs_P), Thm 7.7 (uniqueness), Thm 7.8 (six dimensions, stated for
     4	coarsenings Phi_c: Phi_c is P-preserving iff c is a bijection onto K with |K| = 6),
     5	Prop 10.1 (witnesses), Thm 10.2 (novelty).
     6	
     7	Part VII (uniqueness and novelty by proof). P(G) is the isomorphism class of represent(G):
     8	roles, shares, Q, omega, kappa, links, D and layers up to an actor bijection (``p_equal``).
     9	A coarsening c: M -> K or None merges pillars into blocks (lam-weighted) or drops them. Every
    10	c that is not a total injection collapses a witness pair (``witness_coarsening``): two
    11	systems satisfying all axioms with equal coarsened profiles but different P. Classical
    12	schemes (Parsons, Mann, Easton, Luhmann, Almond) are coarsenings; Aristotle and Weber are
    13	typologies; each has a witness pair. No uniqueness claim is made beyond these statements.
    14	"""
    15	
    16	from __future__ import annotations
    17	
    18	import itertools
    19	import math
    20	from collections.abc import Callable, Iterable, Mapping, Sequence
    21	from dataclasses import dataclass
    22	
    23	from .capture import CaptureLink
    24	from .necessity import EXTENDED_AXIOMS, GovernanceSystem, Practice
    25	from .pillars import PILLAR_TO_AXIOM, PILLARS
    26	from .representation import (
    27	    CodedRecord,
    28	    FormalizedStructure,
    29	    Label,
    30	    M_LABELS,
    31	    find_bijection,
    32	    represent,
    33	    structurally_equal,
    34	    well_formed,
    35	)
    36	
    37	_ROUND = 12
    38	_ATOL = 1e-9
    39	Coarsening = Mapping[Label, "Label | None"]
    40	
    41	
    42	# Coarsening --------------------------------------------------------------------------------
    43	
    44	
    45	def _blocks(F: FormalizedStructure, c: Coarsening) -> dict[Label, list[Label]]:
    46	    if set(c) != set(F.pillars):
    47	        raise ValueError("a coarsening must assign every pillar (None drops it)")
    48	    blocks: dict[Label, list[Label]] = {}
    49	    for m in F.pillars:
    50	        if c[m] is not None:
    51	            blocks.setdefault(c[m], []).append(m)
    52	    return blocks
    53	
    54	
    55	def _block_weights(blocks: Mapping[Label, list[Label]],
    56	                   lam: Mapping[Label, float] | None) -> dict[Label, float]:
    57	    out: dict[Label, float] = {}
    58	    for members in blocks.values():
    59	        for m in members:
    60	            out[m] = 1.0 / len(members) if lam is None else float(lam[m])
    61	        if any(not math.isfinite(out[m]) or out[m] <= 0.0 for m in members):
    62	            raise ValueError("lam_m must be positive")
    63	        if abs(sum(out[m] for m in members) - 1.0) > _ATOL:
    64	            raise ValueError("lam must sum to 1 within each block")
    65	    return out
    66	
    67	
    68	def coarsen(F: FormalizedStructure, c: Coarsening,
    69	            lam: Mapping[Label, float] | None = None) -> FormalizedStructure:
    70	    """Coarsen F by c: M -> K or None (drop), lam-weighted within each block (default equal).
    71	
    72	    Block holders are the union; shares, layers, Q and kappa are lam-weighted sums; omega_k is
    73	    the sum of omega_m (not renormalized); hyperarcs with no dropped element map to their image
    74	    under c, self-loops removed; links in dropped pillars are removed.
    75	    """
    76	    blocks = _blocks(F, c)
    77	    w = _block_weights(blocks, lam)
    78	    keys = tuple(blocks)
    79	
    80	    def mix(get: Callable[[Label], float], k: Label) -> float:
    81	        return sum(w[m] * get(m) for m in blocks[k])
    82	
    83	    shares = {k: {v: mix(lambda m: F.shares[m].get(v, 0.0), k) for v in F.actors} for k in keys}
    84	    layers = {k: sum(w[m] * F.layers[m] for m in blocks[k]) for k in keys}
    85	    arcs = set()
    86	    for tail, head in F.arcs:
    87	        if c[head] is None or any(c[t] is None for t in tail):
    88	            continue
    89	        t2, h2 = frozenset(c[t] for t in tail), c[head]
    90	        if h2 not in t2:
    91	            arcs.add((t2, h2))
    92	    return FormalizedStructure(
    93	        actors=F.actors, pillars=keys,
    94	        roles={v: frozenset(c[m] for m in ps if c[m] is not None) for v, ps in F.roles.items()},
    95	        layers=layers, shares=shares,
    96	        contestability={k: mix(lambda m: F.contestability[m], k) for k in keys},
    97	        weights={k: sum(F.weights[m] for m in blocks[k]) for k in keys},
    98	        kappa={s: {k: mix(lambda m: row.get(m, 0.0), k) for k in keys} for s, row in F.kappa.items()},
    99	        links=frozenset((a, b, c[m]) for a, b, m in F.links if c[m] is not None),
   100	        arcs=frozenset(arcs),
   101	    )
   102	
   103	
   104	IDENTITY: dict[Label, Label] = {m: m for m in M_LABELS}
   105	
   106	
   107	def phi(record: CodedRecord) -> FormalizedStructure:
   108	    """Phi = coarsen(represent(G), identity)."""
   109	    return coarsen(represent(record), IDENTITY)
   110	
   111	
   112	# P-equality --------------------------------------------------------------------------------
   113	
   114	
   115	def _r(x: float) -> float:
   116	    return round(float(x), _ROUND) + 0.0
   117	
   118	
   119	def p_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   120	    """P(F) = P(G): roles, shares, Q, omega, kappa (transported), links, D and layers agree
   121	    under an actor bijection (``representation.find_bijection`` with layers)."""
   122	    return find_bijection(F, G, with_layers=True) is not None
   123	
   124	
   125	def _global(F: FormalizedStructure) -> tuple:
   126	    return (
   127	        F.pillars,
   128	        tuple(_r(F.contestability[m]) for m in F.pillars),
   129	        tuple(_r(F.weights[m]) for m in F.pillars),
   130	        tuple(sorted((tuple(sorted(S)), tuple(_r(r.get(m, 0.0)) for m in F.pillars))
   131	                     for S, r in F.kappa.items())),
   132	        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
   133	        len(F.actors),
   134	    )
   135	
   136	
   137	def freeze(F: FormalizedStructure) -> tuple:
   138	    """Hashable encoding of F with its actor names (equality = identity on names)."""
   139	    return (
   140	        F.actors, F.pillars,
   141	        tuple(tuple(sorted(F.roles[v])) for v in F.actors),
   142	        tuple(tuple(_r(F.shares[m][v]) for v in F.actors) for m in F.pillars),
   143	        tuple(tuple(_r(x) for x in F.layers[m].ravel()) for m in F.pillars),
   144	        _global(F), tuple(sorted(F.links)),
   145	    )
   146	
   147	
   148	# Factorization through Phi -----------------------------------------------------------------
   149	
   150	
   151	@dataclass(frozen=True)
   152	class Factorization:
   153	    """alpha factors through Phi on the fixtures: alpha(G) = alpha(G2) implies P(G) = P(G2)
   154	    (``well_defined``: h(alpha(G)) = Phi(G) is a function); ``bijective``: h is also
   155	    injective onto the P-classes of the fixtures."""
   156	
   157	    well_defined: bool
   158	    bijective: bool
   159	
   160	
   161	def factor_through_phi(alpha: Callable[[CodedRecord], object],
   162	                       records: Sequence[CodedRecord]) -> Factorization:
   163	    """Check that the P-preserving abstraction ``alpha`` factors through Phi on ``records``."""
   164	    images = [alpha(r) for r in records]
   165	    phis = [phi(r) for r in records]
   166	    well_defined = injective = True
   167	    for i in range(len(records)):
   168	        for j in range(i + 1, len(records)):
   169	            same_alpha = images[i] == images[j]
   170	            same_p = p_equal(phis[i], phis[j])
   171	            if same_alpha and not same_p:
   172	                well_defined = False
   173	            if same_p and not same_alpha:
   174	                injective = False
   175	    return Factorization(well_defined, well_defined and injective)
   176	
   177	
   178	def alpha_represent(record: CodedRecord) -> tuple:
   179	    """NOT P-preserving (negative control): the frozen profile keeps actor names, so two
   180	    actor-renamed copies of one system get different values."""
   181	    return freeze(represent(record))
   182	
   183	
   184	# Canonical form (a complete invariant of P) ------------------------------------------------
   185	
   186	
   187	def _encode(F: FormalizedStructure, order: Sequence[int]) -> tuple:
   188	    """Name-free encoding of F with actors listed in ``order``."""
   189	    pos = {F.actors[k]: i for i, k in enumerate(order)}
   190	    return (
   191	        F.pillars,
   192	        tuple(tuple(sorted(F.roles[F.actors[k]])) for k in order),
   193	        tuple(tuple(_r(F.shares[m][F.actors[k]]) for k in order) for m in F.pillars),
   194	        tuple(tuple(_r(F.layers[m][i, j]) for i in order for j in order) for m in F.pillars),
   195	        tuple(_r(F.contestability[m]) for m in F.pillars),
   196	        tuple(_r(F.weights[m]) for m in F.pillars),
   197	        tuple(sorted((tuple(sorted(pos[v] for v in S)),
   198	                      tuple(_r(r.get(m, 0.0)) for m in F.pillars)) for S, r in F.kappa.items())),
   199	        tuple(sorted((pos[a], pos[b], m) for a, b, m in F.links)),
   200	        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
   201	    )
   202	
   203	
   204	def _relabel(sigs: Sequence) -> list[int]:
   205	    table = {sg: c for c, sg in enumerate(sorted(set(sigs)))}
   206	    return [table[sg] for sg in sigs]
   207	
   208	
   209	def _initial_colors(F: FormalizedStructure) -> list[int]:
   210	    return _relabel([(tuple(sorted(F.roles[v])), tuple(_r(F.shares[m][v]) for m in F.pillars))
   211	                     for v in F.actors])
   212	
   213	
   214	def _refine(F: FormalizedStructure, colors: list[int]) -> list[int]:
   215	    """Colour refinement from ``colors``, iterated until the partition is stable. The result
   216	    depends only on the structure and the input colouring, never on actor names."""
   217	    n = len(F.actors)
   218	    idx = {v: k for k, v in enumerate(F.actors)}
   219	    while True:
   220	        sigs = []
   221	        for k in range(n):
   222	            v = F.actors[k]
   223	            sigs.append((
   224	                colors[k],
   225	                tuple(sorted((colors[j],
   226	                              tuple(_r(F.layers[m][k, j]) for m in F.pillars),
   227	                              tuple(_r(F.layers[m][j, k]) for m in F.pillars))
   228	                             for j in range(n) if j != k)),
   229	                tuple(sorted((colors[idx[b]], m, "out") for a, b, m in F.links if a == v)
   230	                      + sorted((colors[idx[a]], m, "in") for a, b, m in F.links if b == v)),
   231	                tuple(sorted((tuple(sorted(colors[idx[u]] for u in S)),
   232	                              tuple(_r(r.get(m, 0.0)) for m in F.pillars))
   233	                             for S, r in F.kappa.items() if v in S)),
   234	            ))
   235	        new = _relabel(sigs)
   236	        if len(set(new)) == len(set(colors)):
   237	            return new
   238	        colors = new
   239	
   240	
   241	def _interchangeable(F: FormalizedStructure, colors: list[int], cls: list[int]) -> bool:
   242	    """True if every transposition (cls[0] cls[t]) is an automorphism of F that preserves
   243	    ``colors``; these transpositions generate all permutations of the class."""
   244	    order = sorted(range(len(F.actors)), key=lambda k: (colors[k], k))
   245	    ref = _encode(F, order)
   246	    pos = {k: i for i, k in enumerate(order)}
   247	    for other in cls[1:]:
   248	        swapped = list(order)
   249	        a, b = pos[cls[0]], pos[other]
   250	        swapped[a], swapped[b] = swapped[b], swapped[a]
   251	        if _encode(F, swapped) != ref:
   252	            return False
   253	    return True
   254	
   255	
   256	def canonical_form(F: FormalizedStructure) -> tuple:
   257	    """A complete invariant of P: canonical_form(F) == canonical_form(G) iff p_equal(F, G).
   258	
   259	    Individualization-refinement: refine colours; if every class is a singleton, encode in
   260	    colour order; otherwise branch on each member of the first smallest non-singleton class
   261	    (individualize it, refine, recurse) and return the lexicographic minimum. When all
   262	    transpositions within that class are automorphisms, the branches give identical results
   263	    and only one is explored. Total on well-formed structures (worst-case exponential time).
   264	    Numbers enter quantized to 12 decimals, as in ``p_equal``.
   265	    """
   266	    if not well_formed(F):
   267	        raise ValueError("canonical_form needs a well-formed structure")
   268	    n = len(F.actors)
   269	    if n == 0:
   270	        return _encode(F, [])
   271	
   272	    def search(colors: list[int]) -> tuple:
   273	        colors = _refine(F, colors)
   274	        classes: dict[int, list[int]] = {}
   275	        for k, c in enumerate(colors):
   276	            classes.setdefault(c, []).append(k)
   277	        open_ = [cl for c, cl in sorted(classes.items()) if len(cl) > 1]
   278	        if not open_:
   279	            return _encode(F, sorted(range(n), key=lambda k: colors[k]))
   280	        cls = min(open_, key=len)
   281	        branches = cls[:1] if _interchangeable(F, colors, cls) else cls
   282	        best = None
   283	        for v in branches:
   284	            individualized = _relabel([(colors[k], 0 if k == v else 1) for k in range(n)])
   285	            enc = search(individualized)
   286	            if best is None or enc < best:
   287	                best = enc
   288	        return best
   289	
   290	    return search(_initial_colors(F))
   291	
   292	
   293	def alpha_canonical(record: CodedRecord) -> tuple:
   294	    """A P-preserving abstraction: the canonical form of represent(G)."""
   295	    return canonical_form(represent(record))
   296	
   297	
   298	def alpha_canonical_phi(record: CodedRecord) -> tuple:
   299	    """A second, differently built one: the canonical form of Phi(G) (coarsen by identity)
   300	    plus a redundant field (the number of hyperarcs)."""
   301	    F = phi(record)
   302	    return (canonical_form(F), len(F.arcs))
   303	
   304	
   305	def rename_record(record: CodedRecord, mapping: Mapping[str, str]) -> CodedRecord:
   306	    """The same coded system with actors renamed by ``mapping`` (missing names kept)."""
   307	    ren = lambda v: mapping.get(v, v)  # noqa: E731
   308	    sys_ = record.system
   309	    names = set(represent(record).actors)
   310	    if len({ren(v) for v in names}) != len(names):
   311	        raise ValueError("renaming must be injective on the record's actors")
   312	    practices = tuple(
   313	        Practice(p.description, p.solves, frozenset(ren(h) for h in p.holders), p.formal,
   314	                 p.source)
   315	        for p in sys_.practices
   316	    )
   317	    system = GovernanceSystem(sys_.name, sys_.persistent, sys_.axioms, practices,
   318	                              sys_.absent_incidences, sys_.note)
   319	    links = tuple(CaptureLink(ren(lk.source), ren(lk.target), lk.pillar, lk.privileged_access,
   320	                              lk.weakens_accountability, lk.material_evidence, lk.evidence)
   321	                  for lk in record.links)
   322	    coalitions = None if record.coalitions is None else {
   323	        frozenset(ren(v) for v in S): row for S, row in record.coalitions.items()}
   324	    return CodedRecord(system, {m: {ren(v): x for v, x in sh.items()}
   325	                                for m, sh in record.shares.items()},
   326	                       record.contestability, record.weights, coalitions, links)
   327	
   328	
   329	# Witnesses ---------------------------------------------------------------------------------
   330	
   331	
   332	def witness_record(ab_shares: Mapping[Label, tuple[float, float]], q: float = 0.5,
   333	                   links: Iterable = ()) -> CodedRecord:
   334	    """Witness system (Part VII Prop 7.5, Prop 10.1): actors a and b perform exactly the
   335	    pillars in ``ab_shares`` with shares (s^m_a, s^m_b); actor c alone performs every other
   336	    pillar (share 1). Ax1..Ax6 and X1, X2, X3, X5 hold, so Proposition A holds. Both members
   337	    of a witness pair use the same keys, hence the same actor set and role map.
   338	    """
   339	    if not ab_shares or not set(ab_shares) <= set(M_LABELS):
   340	        raise ValueError("ab_shares must name at least one pillar label")
   341	    practices = tuple(
   342	        Practice(f"{m.label} practice", PILLAR_TO_AXIOM[m],
   343	                 frozenset({"a", "b"}) if m.name in ab_shares else frozenset({"c"}),
   344	                 source="synthetic witness")
   345	        for m in PILLARS
   346	    )
   347	    system = GovernanceSystem("witness", True, EXTENDED_AXIOMS, practices)
   348	    shares = {m: (dict(zip(("a", "b"), ab_shares[m.name])) if m.name in ab_shares
   349	                  else {"c": 1.0}) for m in PILLARS}
   350	    return CodedRecord(system, shares, {m: q for m in PILLARS}, links=tuple(links))
   351	
   352	
   353	def _drop_witness(m: Label, l0: Label) -> tuple[CodedRecord, CodedRecord]:
   354	    """Drop m: G1 s^m = (1, 0), G2 s^m = (1/2, 1/2); a and b also hold (1/2, 1/2) in the
   355	    retained pillar l0 in both, so b is an actor of G1 too."""
   356	    return (witness_record({m: (1.0, 0.0), l0: (0.5, 0.5)}),
   357	            witness_record({m: (0.5, 0.5), l0: (0.5, 0.5)}))
   358	
   359	
   360	def _merge_witness(m: Label, n: Label, mu: float) -> tuple[CodedRecord, CodedRecord]:
   361	    """Merge {m, n}: G1 s^m = (1, 0), s^n = (0, 1); G2 s^m = s^n = (mu, 1 - mu)."""
   362	    return (witness_record({m: (1.0, 0.0), n: (0.0, 1.0)}),
   363	            witness_record({m: (mu, 1.0 - mu), n: (mu, 1.0 - mu)}))
   364	
   365	
   366	def witness_coarsening(c: Coarsening, lam: Mapping[Label, float] | None = None
   367	                       ) -> tuple[CodedRecord, CodedRecord]:
   368	    """(G1, G2) with coarsen(Phi(G1), c) = coarsen(Phi(G2), c) and P(G1) != P(G2)
   369	    (Part VII Prop 7.5).
   370	
   371	    If c drops a pillar m, the drop witness with l0 the first retained pillar; otherwise, for
   372	    the first pair {m, n} in one block, the merge witness with mu = lam_m / (lam_m + lam_n).
   373	    Raises if c is a total injection (then Phi_c is P-preserving, Thm 7.8).
   374	    """
   375	    if set(c) != set(M_LABELS):
   376	        raise ValueError("c must assign all six pillars")
   377	    dropped = [m for m in M_LABELS if c[m] is None]
   378	    kept = [m for m in M_LABELS if c[m] is not None]
   379	    if dropped:
   380	        if not kept:
   381	            raise ValueError("c drops every pillar; the image K is empty")
   382	        return _drop_witness(dropped[0], kept[0])
   383	    for i, m in enumerate(M_LABELS):
   384	        for n in M_LABELS[i + 1:]:
   385	            if c[m] == c[n]:
   386	                if lam is None:
   387	                    size = sum(1 for x in M_LABELS if c[x] == c[m])
   388	                    lm = ln = 1.0 / size
   389	                else:
   390	                    lm, ln = float(lam[m]), float(lam[n])
   391	                return _merge_witness(m, n, lm / (lm + ln))
   392	    raise ValueError("c is a total injection; no collapse witness")
   393	
   394	
   395	# Predecessor encodings ---------------------------------------------------------------------
   396	
   397	PARSONS: dict[Label, Label | None] = {"F": "A", "W": "A", "P": "G", "J": "I", "C": "I", "I": "L"}
   398	MANN: dict[Label, Label | None] = {"I": "Ideological", "F": "Economic", "W": "Economic",
   399	                                   "C": "Military", "P": "Political", "J": "Political"}
   400	EASTON: dict[Label, Label | None] = {"I": "Inputs", "W": "Inputs", "F": "Outputs",
   401	                                     "P": "Outputs", "J": "Outputs", "C": "Outputs"}
   402	LUHMANN: dict[Label, Label | None] = {"F": "Economy", "W": "Economy", "P": "Politics",
   403	                                      "C": "Politics", "J": "Law", "I": "Culture"}
   404	ALMOND: dict[Label, Label | None] = {"F": None, "W": None, "P": "RuleMaking",
   405	                                     "J": "RuleAdjudication", "C": "RuleApplication",
   406	                                     "I": "Inputs"}
   407	
   408	
   409	def encode_parsons(F: FormalizedStructure) -> FormalizedStructure:
   410	    """AGIL: A = {F, W}, G = {P}, I = {J, C}, L = {I}."""
   411	    return coarsen(F, PARSONS)
   412	
   413	
   414	def encode_mann(F: FormalizedStructure) -> FormalizedStructure:
   415	    """IEMP: Ideological = {I}, Economic = {F, W}, Military = {C}, Political = {P, J}."""
   416	    return coarsen(F, MANN)
   417	
   418	
   419	def encode_easton(F: FormalizedStructure) -> FormalizedStructure:
   420	    """Inputs = {I, W}, Outputs = {F, P, J, C}."""
   421	    return coarsen(F, EASTON)
   422	
   423	
   424	def encode_luhmann(F: FormalizedStructure) -> FormalizedStructure:
   425	    """Economy = {F, W}, Politics = {P, C}, Law = {J}, Culture = {I} (Luhmann splits it
   426	    further; the split does not affect the witness)."""
   427	    return coarsen(F, LUHMANN)
   428	
   429	
   430	def encode_almond(F: FormalizedStructure) -> FormalizedStructure:
   431	    """F and W dropped; RuleMaking = {P}, RuleAdjudication = {J}, RuleApplication = {C},
   432	    Inputs = {I}."""
   433	    return coarsen(F, ALMOND)
   434	
   435	
   436	def encode_aristotle(F: FormalizedStructure) -> tuple[str, str]:
   437	    """(rulers, aim): 'one' if exactly one actor has s^P > 0, 'few' if 2 to n/2, else 'many';
   438	    'deviant' if any capture link, else 'correct'. A typology, not a coarsening."""
   439	    k = sum(1 for v in F.actors if F.shares["P"].get(v, 0.0) > 0.0)
   440	    n = len(F.actors)
   441	    rulers = "one" if k == 1 else ("few" if 2 <= k <= n / 2 else "many")
   442	    return rulers, ("deviant" if F.links else "correct")
   443	
   444	
   445	WEBER_TYPES = ("traditional", "charismatic", "legal-rational")
   446	
   447	
   448	def encode_weber(F: FormalizedStructure, legitimation: str, has_staff: bool) -> tuple[str, bool]:
   449	    """(legitimation type, administrative staff). Both come from a coded field the profile
   450	    does NOT contain, so the encoding does not factor through P (nor P through it)."""
   451	    if legitimation not in WEBER_TYPES:
   452	        raise ValueError(f"legitimation must be one of {WEBER_TYPES}")
   453	    return legitimation, bool(has_staff)
   454	
   455	
   456	ENCODINGS: dict[str, Callable[[FormalizedStructure], object]] = {
   457	    "parsons": encode_parsons,
   458	    "mann": encode_mann,
   459	    "easton": encode_easton,
   460	    "luhmann": encode_luhmann,
   461	    "almond": encode_almond,
   462	    "aristotle": encode_aristotle,
   463	    "weber": lambda F: encode_weber(F, "legal-rational", True),
   464	}
   465	
   466	_WITNESSES: dict[str, Callable[[], tuple[CodedRecord, CodedRecord]]] = {
   467	    "parsons": lambda: _merge_witness("F", "W", 0.5),
   468	    "mann": lambda: _merge_witness("P", "J", 0.5),
   469	    "easton": lambda: _merge_witness("P", "J", 0.5),
   470	    "luhmann": lambda: _merge_witness("F", "W", 0.5),
   471	    "almond": lambda: _drop_witness("F", "P"),
   472	    "aristotle": lambda: (witness_record({"J": (1.0, 0.0), "I": (0.5, 0.5)}),
   473	                          witness_record({"J": (0.5, 0.5), "I": (0.5, 0.5)})),
   474	    "weber": lambda: (witness_record({"C": (1.0, 0.0), "I": (0.5, 0.5)}),
   475	                      witness_record({"C": (0.5, 0.5), "I": (0.5, 0.5)})),
   476	}
   477	
   478	
   479	def witness_pair(k: str) -> tuple[CodedRecord, CodedRecord]:
   480	    """Two systems satisfying all axioms that encoding ``k`` cannot tell apart, with P
   481	    differing (Part VII Prop 10.1). Merge witnesses use mu = 1/2 (equal lam; Easton's
   482	    four-member Outputs block also gives mu = 1/2 for (P, J)); Almond drops F with l0 = P;
   483	    Aristotle and Weber differ in s^J or s^C with a and b also holding (1/2, 1/2) in I.
   484	    """
   485	    if k not in _WITNESSES:
   486	        raise ValueError(f"unknown encoding {k!r}")
   487	    return _WITNESSES[k]()
   488	
   489	
   490	def coarsenings_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   491	    """Coarsened profiles equal component by component (identity on actor names)."""
   492	    return structurally_equal(F, G)

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/uniqueness.py | sed -n '1,520p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	"""Uniqueness and novelty: coarsenings, factorization through Phi, predecessor encodings.
     2	
     3	Part VII Def 7.6 (Abs_P), Thm 7.7 (uniqueness), Thm 7.8 (six dimensions, stated for
     4	coarsenings Phi_c: Phi_c is P-preserving iff c is a bijection onto K with |K| = 6),
     5	Prop 10.1 (witnesses), Thm 10.2 (novelty).
     6	
     7	Part VII (uniqueness and novelty by proof). P(G) is the isomorphism class of represent(G):
     8	roles, shares, Q, omega, kappa, links, D and layers up to an actor bijection (``p_equal``).
     9	A coarsening c: M -> K or None merges pillars into blocks (lam-weighted) or drops them. Every
    10	c that is not a total injection collapses a witness pair (``witness_coarsening``): two
    11	systems satisfying all axioms with equal coarsened profiles but different P. Classical
    12	schemes (Parsons, Mann, Easton, Luhmann, Almond) are coarsenings; Aristotle and Weber are
    13	typologies; each has a witness pair. No uniqueness claim is made beyond these statements.
    14	"""
    15	
    16	from __future__ import annotations
    17	
    18	import itertools
    19	import math
    20	from collections.abc import Callable, Iterable, Mapping, Sequence
    21	from dataclasses import dataclass
    22	
    23	from .capture import CaptureLink
    24	from .necessity import EXTENDED_AXIOMS, GovernanceSystem, Practice
    25	from .pillars import PILLAR_TO_AXIOM, PILLARS
    26	from .representation import (
    27	    CodedRecord,
    28	    FormalizedStructure,
    29	    Label,
    30	    M_LABELS,
    31	    find_bijection,
    32	    represent,
    33	    structurally_equal,
    34	    well_formed,
    35	)
    36	
    37	_ROUND = 12
    38	_ATOL = 1e-9
    39	Coarsening = Mapping[Label, "Label | None"]
    40	
    41	
    42	# Coarsening --------------------------------------------------------------------------------
    43	
    44	
    45	def _blocks(F: FormalizedStructure, c: Coarsening) -> dict[Label, list[Label]]:
    46	    if set(c) != set(F.pillars):
    47	        raise ValueError("a coarsening must assign every pillar (None drops it)")
    48	    blocks: dict[Label, list[Label]] = {}
    49	    for m in F.pillars:
    50	        if c[m] is not None:
    51	            blocks.setdefault(c[m], []).append(m)
    52	    return blocks
    53	
    54	
    55	def _block_weights(blocks: Mapping[Label, list[Label]],
    56	                   lam: Mapping[Label, float] | None) -> dict[Label, float]:
    57	    out: dict[Label, float] = {}
    58	    for members in blocks.values():
    59	        for m in members:
    60	            out[m] = 1.0 / len(members) if lam is None else float(lam[m])
    61	        if any(not math.isfinite(out[m]) or out[m] <= 0.0 for m in members):
    62	            raise ValueError("lam_m must be positive")
    63	        if abs(sum(out[m] for m in members) - 1.0) > _ATOL:
    64	            raise ValueError("lam must sum to 1 within each block")
    65	    return out
    66	
    67	
    68	def coarsen(F: FormalizedStructure, c: Coarsening,
    69	            lam: Mapping[Label, float] | None = None) -> FormalizedStructure:
    70	    """Coarsen F by c: M -> K or None (drop), lam-weighted within each block (default equal).
    71	
    72	    Block holders are the union; shares, layers, Q and kappa are lam-weighted sums; omega_k is
    73	    the sum of omega_m (not renormalized); hyperarcs with no dropped element map to their image
    74	    under c, self-loops removed; links in dropped pillars are removed.
    75	    """
    76	    blocks = _blocks(F, c)
    77	    w = _block_weights(blocks, lam)
    78	    keys = tuple(blocks)
    79	
    80	    def mix(get: Callable[[Label], float], k: Label) -> float:
    81	        return sum(w[m] * get(m) for m in blocks[k])
    82	
    83	    shares = {k: {v: mix(lambda m: F.shares[m].get(v, 0.0), k) for v in F.actors} for k in keys}
    84	    layers = {k: sum(w[m] * F.layers[m] for m in blocks[k]) for k in keys}
    85	    arcs = set()
    86	    for tail, head in F.arcs:
    87	        if c[head] is None or any(c[t] is None for t in tail):
    88	            continue
    89	        t2, h2 = frozenset(c[t] for t in tail), c[head]
    90	        if h2 not in t2:
    91	            arcs.add((t2, h2))
    92	    return FormalizedStructure(
    93	        actors=F.actors, pillars=keys,
    94	        roles={v: frozenset(c[m] for m in ps if c[m] is not None) for v, ps in F.roles.items()},
    95	        layers=layers, shares=shares,
    96	        contestability={k: mix(lambda m: F.contestability[m], k) for k in keys},
    97	        weights={k: sum(F.weights[m] for m in blocks[k]) for k in keys},
    98	        kappa={s: {k: mix(lambda m: row.get(m, 0.0), k) for k in keys} for s, row in F.kappa.items()},
    99	        links=frozenset((a, b, c[m]) for a, b, m in F.links if c[m] is not None),
   100	        arcs=frozenset(arcs),
   101	    )
   102	
   103	
   104	IDENTITY: dict[Label, Label] = {m: m for m in M_LABELS}
   105	
   106	
   107	def phi(record: CodedRecord) -> FormalizedStructure:
   108	    """Phi = coarsen(represent(G), identity)."""
   109	    return coarsen(represent(record), IDENTITY)
   110	
   111	
   112	# P-equality --------------------------------------------------------------------------------
   113	
   114	
   115	def _r(x: float) -> float:
   116	    return round(float(x), _ROUND) + 0.0
   117	
   118	
   119	def p_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   120	    """P(F) = P(G): roles, shares, Q, omega, kappa (transported), links, D and layers agree
   121	    under an actor bijection (``representation.find_bijection`` with layers)."""
   122	    return find_bijection(F, G, with_layers=True) is not None
   123	
   124	
   125	def _global(F: FormalizedStructure) -> tuple:
   126	    return (
   127	        F.pillars,
   128	        tuple(_r(F.contestability[m]) for m in F.pillars),
   129	        tuple(_r(F.weights[m]) for m in F.pillars),
   130	        tuple(sorted((tuple(sorted(S)), tuple(_r(r.get(m, 0.0)) for m in F.pillars))
   131	                     for S, r in F.kappa.items())),
   132	        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
   133	        len(F.actors),
   134	    )
   135	
   136	
   137	def freeze(F: FormalizedStructure) -> tuple:
   138	    """Hashable encoding of F with its actor names (equality = identity on names)."""
   139	    return (
   140	        F.actors, F.pillars,
   141	        tuple(tuple(sorted(F.roles[v])) for v in F.actors),
   142	        tuple(tuple(_r(F.shares[m][v]) for v in F.actors) for m in F.pillars),
   143	        tuple(tuple(_r(x) for x in F.layers[m].ravel()) for m in F.pillars),
   144	        _global(F), tuple(sorted(F.links)),
   145	    )
   146	
   147	
   148	# Factorization through Phi -----------------------------------------------------------------
   149	
   150	
   151	@dataclass(frozen=True)
   152	class Factorization:
   153	    """alpha factors through Phi on the fixtures: alpha(G) = alpha(G2) implies P(G) = P(G2)
   154	    (``well_defined``: h(alpha(G)) = Phi(G) is a function); ``bijective``: h is also
   155	    injective onto the P-classes of the fixtures."""
   156	
   157	    well_defined: bool
   158	    bijective: bool
   159	
   160	
   161	def factor_through_phi(alpha: Callable[[CodedRecord], object],
   162	                       records: Sequence[CodedRecord]) -> Factorization:
   163	    """Check that the P-preserving abstraction ``alpha`` factors through Phi on ``records``."""
   164	    images = [alpha(r) for r in records]
   165	    phis = [phi(r) for r in records]
   166	    well_defined = injective = True
   167	    for i in range(len(records)):
   168	        for j in range(i + 1, len(records)):
   169	            same_alpha = images[i] == images[j]
   170	            same_p = p_equal(phis[i], phis[j])
   171	            if same_alpha and not same_p:
   172	                well_defined = False
   173	            if same_p and not same_alpha:
   174	                injective = False
   175	    return Factorization(well_defined, well_defined and injective)
   176	
   177	
   178	def alpha_represent(record: CodedRecord) -> tuple:
   179	    """NOT P-preserving (negative control): the frozen profile keeps actor names, so two
   180	    actor-renamed copies of one system get different values."""
   181	    return freeze(represent(record))
   182	
   183	
   184	# Canonical form (a complete invariant of P) ------------------------------------------------
   185	
   186	
   187	def _encode(F: FormalizedStructure, order: Sequence[int]) -> tuple:
   188	    """Name-free encoding of F with actors listed in ``order``."""
   189	    pos = {F.actors[k]: i for i, k in enumerate(order)}
   190	    return (
   191	        F.pillars,
   192	        tuple(tuple(sorted(F.roles[F.actors[k]])) for k in order),
   193	        tuple(tuple(_r(F.shares[m][F.actors[k]]) for k in order) for m in F.pillars),
   194	        tuple(tuple(_r(F.layers[m][i, j]) for i in order for j in order) for m in F.pillars),
   195	        tuple(_r(F.contestability[m]) for m in F.pillars),
   196	        tuple(_r(F.weights[m]) for m in F.pillars),
   197	        tuple(sorted((tuple(sorted(pos[v] for v in S)),
   198	                      tuple(_r(r.get(m, 0.0)) for m in F.pillars)) for S, r in F.kappa.items())),
   199	        tuple(sorted((pos[a], pos[b], m) for a, b, m in F.links)),
   200	        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
   201	    )
   202	
   203	
   204	def _relabel(sigs: Sequence) -> list[int]:
   205	    table = {sg: c for c, sg in enumerate(sorted(set(sigs)))}
   206	    return [table[sg] for sg in sigs]
   207	
   208	
   209	def _initial_colors(F: FormalizedStructure) -> list[int]:
   210	    return _relabel([(tuple(sorted(F.roles[v])), tuple(_r(F.shares[m][v]) for m in F.pillars))
   211	                     for v in F.actors])
   212	
   213	
   214	def _refine(F: FormalizedStructure, colors: list[int]) -> list[int]:
   215	    """Colour refinement from ``colors``, iterated until the partition is stable. The result
   216	    depends only on the structure and the input colouring, never on actor names."""
   217	    n = len(F.actors)
   218	    idx = {v: k for k, v in enumerate(F.actors)}
   219	    while True:
   220	        sigs = []
   221	        for k in range(n):
   222	            v = F.actors[k]
   223	            sigs.append((
   224	                colors[k],
   225	                tuple(sorted((colors[j],
   226	                              tuple(_r(F.layers[m][k, j]) for m in F.pillars),
   227	                              tuple(_r(F.layers[m][j, k]) for m in F.pillars))
   228	                             for j in range(n) if j != k)),
   229	                tuple(sorted((colors[idx[b]], m, "out") for a, b, m in F.links if a == v)
   230	                      + sorted((colors[idx[a]], m, "in") for a, b, m in F.links if b == v)),
   231	                tuple(sorted((tuple(sorted(colors[idx[u]] for u in S)),
   232	                              tuple(_r(r.get(m, 0.0)) for m in F.pillars))
   233	                             for S, r in F.kappa.items() if v in S)),
   234	            ))
   235	        new = _relabel(sigs)
   236	        if len(set(new)) == len(set(colors)):
   237	            return new
   238	        colors = new
   239	
   240	
   241	def _interchangeable(F: FormalizedStructure, colors: list[int], cls: list[int]) -> bool:
   242	    """True if every transposition (cls[0] cls[t]) is an automorphism of F that preserves
   243	    ``colors``; these transpositions generate all permutations of the class."""
   244	    order = sorted(range(len(F.actors)), key=lambda k: (colors[k], k))
   245	    ref = _encode(F, order)
   246	    pos = {k: i for i, k in enumerate(order)}
   247	    for other in cls[1:]:
   248	        swapped = list(order)
   249	        a, b = pos[cls[0]], pos[other]
   250	        swapped[a], swapped[b] = swapped[b], swapped[a]
   251	        if _encode(F, swapped) != ref:
   252	            return False
   253	    return True
   254	
   255	
   256	def canonical_form(F: FormalizedStructure) -> tuple:
   257	    """A complete invariant of P: canonical_form(F) == canonical_form(G) iff p_equal(F, G).
   258	
   259	    Individualization-refinement: refine colours; if every class is a singleton, encode in
   260	    colour order; otherwise branch on each member of the first smallest non-singleton class
   261	    (individualize it, refine, recurse) and return the lexicographic minimum. When all
   262	    transpositions within that class are automorphisms, the branches give identical results
   263	    and only one is explored. Total on well-formed structures (worst-case exponential time).
   264	    Numbers enter quantized to 12 decimals, as in ``p_equal``.
   265	    """
   266	    if not well_formed(F):
   267	        raise ValueError("canonical_form needs a well-formed structure")
   268	    n = len(F.actors)
   269	    if n == 0:
   270	        return _encode(F, [])
   271	
   272	    def search(colors: list[int]) -> tuple:
   273	        colors = _refine(F, colors)
   274	        classes: dict[int, list[int]] = {}
   275	        for k, c in enumerate(colors):
   276	            classes.setdefault(c, []).append(k)
   277	        open_ = [cl for c, cl in sorted(classes.items()) if len(cl) > 1]
   278	        if not open_:
   279	            return _encode(F, sorted(range(n), key=lambda k: colors[k]))
   280	        cls = min(open_, key=len)
   281	        branches = cls[:1] if _interchangeable(F, colors, cls) else cls
   282	        best = None
   283	        for v in branches:
   284	            individualized = _relabel([(colors[k], 0 if k == v else 1) for k in range(n)])
   285	            enc = search(individualized)
   286	            if best is None or enc < best:
   287	                best = enc
   288	        return best
   289	
   290	    return search(_initial_colors(F))
   291	
   292	
   293	def alpha_canonical(record: CodedRecord) -> tuple:
   294	    """A P-preserving abstraction: the canonical form of represent(G)."""
   295	    return canonical_form(represent(record))
   296	
   297	
   298	def alpha_canonical_phi(record: CodedRecord) -> tuple:
   299	    """A second, differently built one: the canonical form of Phi(G) (coarsen by identity)
   300	    plus a redundant field (the number of hyperarcs)."""
   301	    F = phi(record)
   302	    return (canonical_form(F), len(F.arcs))
   303	
   304	
   305	def rename_record(record: CodedRecord, mapping: Mapping[str, str]) -> CodedRecord:
   306	    """The same coded system with actors renamed by ``mapping`` (missing names kept)."""
   307	    ren = lambda v: mapping.get(v, v)  # noqa: E731
   308	    sys_ = record.system
   309	    names = set(represent(record).actors)
   310	    if len({ren(v) for v in names}) != len(names):
   311	        raise ValueError("renaming must be injective on the record's actors")
   312	    practices = tuple(
   313	        Practice(p.description, p.solves, frozenset(ren(h) for h in p.holders), p.formal,
   314	                 p.source)
   315	        for p in sys_.practices
   316	    )
   317	    system = GovernanceSystem(sys_.name, sys_.persistent, sys_.axioms, practices,
   318	                              sys_.absent_incidences, sys_.note)
   319	    links = tuple(CaptureLink(ren(lk.source), ren(lk.target), lk.pillar, lk.privileged_access,
   320	                              lk.weakens_accountability, lk.material_evidence, lk.evidence)
   321	                  for lk in record.links)
   322	    coalitions = None if record.coalitions is None else {
   323	        frozenset(ren(v) for v in S): row for S, row in record.coalitions.items()}
   324	    return CodedRecord(system, {m: {ren(v): x for v, x in sh.items()}
   325	                                for m, sh in record.shares.items()},
   326	                       record.contestability, record.weights, coalitions, links)
   327	
   328	
   329	# Witnesses ---------------------------------------------------------------------------------
   330	
   331	
   332	def witness_record(ab_shares: Mapping[Label, tuple[float, float]], q: float = 0.5,
   333	                   links: Iterable = ()) -> CodedRecord:
   334	    """Witness system (Part VII Prop 7.5, Prop 10.1): actors a and b perform exactly the
   335	    pillars in ``ab_shares`` with shares (s^m_a, s^m_b); actor c alone performs every other
   336	    pillar (share 1). Ax1..Ax6 and X1, X2, X3, X5 hold, so Proposition A holds. Both members
   337	    of a witness pair use the same keys, hence the same actor set and role map.
   338	    """
   339	    if not ab_shares or not set(ab_shares) <= set(M_LABELS):
   340	        raise ValueError("ab_shares must name at least one pillar label")
   341	    practices = tuple(
   342	        Practice(f"{m.label} practice", PILLAR_TO_AXIOM[m],
   343	                 frozenset({"a", "b"}) if m.name in ab_shares else frozenset({"c"}),
   344	                 source="synthetic witness")
   345	        for m in PILLARS
   346	    )
   347	    system = GovernanceSystem("witness", True, EXTENDED_AXIOMS, practices)
   348	    shares = {m: (dict(zip(("a", "b"), ab_shares[m.name])) if m.name in ab_shares
   349	                  else {"c": 1.0}) for m in PILLARS}
   350	    return CodedRecord(system, shares, {m: q for m in PILLARS}, links=tuple(links))
   351	
   352	
   353	def _drop_witness(m: Label, l0: Label) -> tuple[CodedRecord, CodedRecord]:
   354	    """Drop m: G1 s^m = (1, 0), G2 s^m = (1/2, 1/2); a and b also hold (1/2, 1/2) in the
   355	    retained pillar l0 in both, so b is an actor of G1 too."""
   356	    return (witness_record({m: (1.0, 0.0), l0: (0.5, 0.5)}),
   357	            witness_record({m: (0.5, 0.5), l0: (0.5, 0.5)}))
   358	
   359	
   360	def _merge_witness(m: Label, n: Label, mu: float) -> tuple[CodedRecord, CodedRecord]:
   361	    """Merge {m, n}: G1 s^m = (1, 0), s^n = (0, 1); G2 s^m = s^n = (mu, 1 - mu)."""
   362	    return (witness_record({m: (1.0, 0.0), n: (0.0, 1.0)}),
   363	            witness_record({m: (mu, 1.0 - mu), n: (mu, 1.0 - mu)}))
   364	
   365	
   366	def witness_coarsening(c: Coarsening, lam: Mapping[Label, float] | None = None
   367	                       ) -> tuple[CodedRecord, CodedRecord]:
   368	    """(G1, G2) with coarsen(Phi(G1), c) = coarsen(Phi(G2), c) and P(G1) != P(G2)
   369	    (Part VII Prop 7.5).
   370	
   371	    If c drops a pillar m, the drop witness with l0 the first retained pillar; otherwise, for
   372	    the first pair {m, n} in one block, the merge witness with mu = lam_m / (lam_m + lam_n).
   373	    Raises if c is a total injection (then Phi_c is P-preserving, Thm 7.8).
   374	    """
   375	    if set(c) != set(M_LABELS):
   376	        raise ValueError("c must assign all six pillars")
   377	    dropped = [m for m in M_LABELS if c[m] is None]
   378	    kept = [m for m in M_LABELS if c[m] is not None]
   379	    if dropped:
   380	        if not kept:
   381	            raise ValueError("c drops every pillar; the image K is empty")
   382	        return _drop_witness(dropped[0], kept[0])
   383	    for i, m in enumerate(M_LABELS):
   384	        for n in M_LABELS[i + 1:]:
   385	            if c[m] == c[n]:
   386	                if lam is None:
   387	                    size = sum(1 for x in M_LABELS if c[x] == c[m])
   388	                    lm = ln = 1.0 / size
   389	                else:
   390	                    lm, ln = float(lam[m]), float(lam[n])
   391	                return _merge_witness(m, n, lm / (lm + ln))
   392	    raise ValueError("c is a total injection; no collapse witness")
   393	
   394	
   395	# Predecessor encodings ---------------------------------------------------------------------
   396	
   397	PARSONS: dict[Label, Label | None] = {"F": "A", "W": "A", "P": "G", "J": "I", "C": "I", "I": "L"}
   398	MANN: dict[Label, Label | None] = {"I": "Ideological", "F": "Economic", "W": "Economic",
   399	                                   "C": "Military", "P": "Political", "J": "Political"}
   400	EASTON: dict[Label, Label | None] = {"I": "Inputs", "W": "Inputs", "F": "Outputs",
   401	                                     "P": "Outputs", "J": "Outputs", "C": "Outputs"}
   402	LUHMANN: dict[Label, Label | None] = {"F": "Economy", "W": "Economy", "P": "Politics",
   403	                                      "C": "Politics", "J": "Law", "I": "Culture"}
   404	ALMOND: dict[Label, Label | None] = {"F": None, "W": None, "P": "RuleMaking",
   405	                                     "J": "RuleAdjudication", "C": "RuleApplication",
   406	                                     "I": "Inputs"}
   407	
   408	
   409	def encode_parsons(F: FormalizedStructure) -> FormalizedStructure:
   410	    """AGIL: A = {F, W}, G = {P}, I = {J, C}, L = {I}."""
   411	    return coarsen(F, PARSONS)
   412	
   413	
   414	def encode_mann(F: FormalizedStructure) -> FormalizedStructure:
   415	    """IEMP: Ideological = {I}, Economic = {F, W}, Military = {C}, Political = {P, J}."""
   416	    return coarsen(F, MANN)
   417	
   418	
   419	def encode_easton(F: FormalizedStructure) -> FormalizedStructure:
   420	    """Inputs = {I, W}, Outputs = {F, P, J, C}."""
   421	    return coarsen(F, EASTON)
   422	
   423	
   424	def encode_luhmann(F: FormalizedStructure) -> FormalizedStructure:
   425	    """Economy = {F, W}, Politics = {P, C}, Law = {J}, Culture = {I} (Luhmann splits it
   426	    further; the split does not affect the witness)."""
   427	    return coarsen(F, LUHMANN)
   428	
   429	
   430	def encode_almond(F: FormalizedStructure) -> FormalizedStructure:
   431	    """F and W dropped; RuleMaking = {P}, RuleAdjudication = {J}, RuleApplication = {C},
   432	    Inputs = {I}."""
   433	    return coarsen(F, ALMOND)
   434	
   435	
   436	def encode_aristotle(F: FormalizedStructure) -> tuple[str, str]:
   437	    """(rulers, aim): 'one' if exactly one actor has s^P > 0, 'few' if 2 to n/2, else 'many';
   438	    'deviant' if any capture link, else 'correct'. A typology, not a coarsening."""
   439	    k = sum(1 for v in F.actors if F.shares["P"].get(v, 0.0) > 0.0)
   440	    n = len(F.actors)
   441	    rulers = "one" if k == 1 else ("few" if 2 <= k <= n / 2 else "many")
   442	    return rulers, ("deviant" if F.links else "correct")
   443	
   444	
   445	WEBER_TYPES = ("traditional", "charismatic", "legal-rational")
   446	
   447	
   448	def encode_weber(F: FormalizedStructure, legitimation: str, has_staff: bool) -> tuple[str, bool]:
   449	    """(legitimation type, administrative staff). Both come from a coded field the profile
   450	    does NOT contain, so the encoding does not factor through P (nor P through it)."""
   451	    if legitimation not in WEBER_TYPES:
   452	        raise ValueError(f"legitimation must be one of {WEBER_TYPES}")
   453	    return legitimation, bool(has_staff)
   454	
   455	
   456	ENCODINGS: dict[str, Callable[[FormalizedStructure], object]] = {
   457	    "parsons": encode_parsons,
   458	    "mann": encode_mann,
   459	    "easton": encode_easton,
   460	    "luhmann": encode_luhmann,
   461	    "almond": encode_almond,
   462	    "aristotle": encode_aristotle,
   463	    "weber": lambda F: encode_weber(F, "legal-rational", True),
   464	}
   465	
   466	_WITNESSES: dict[str, Callable[[], tuple[CodedRecord, CodedRecord]]] = {
   467	    "parsons": lambda: _merge_witness("F", "W", 0.5),
   468	    "mann": lambda: _merge_witness("P", "J", 0.5),
   469	    "easton": lambda: _merge_witness("P", "J", 0.5),
   470	    "luhmann": lambda: _merge_witness("F", "W", 0.5),
   471	    "almond": lambda: _drop_witness("F", "P"),
   472	    "aristotle": lambda: (witness_record({"J": (1.0, 0.0), "I": (0.5, 0.5)}),
   473	                          witness_record({"J": (0.5, 0.5), "I": (0.5, 0.5)})),
   474	    "weber": lambda: (witness_record({"C": (1.0, 0.0), "I": (0.5, 0.5)}),
   475	                      witness_record({"C": (0.5, 0.5), "I": (0.5, 0.5)})),
   476	}
   477	
   478	
   479	def witness_pair(k: str) -> tuple[CodedRecord, CodedRecord]:
   480	    """Two systems satisfying all axioms that encoding ``k`` cannot tell apart, with P
   481	    differing (Part VII Prop 10.1). Merge witnesses use mu = 1/2 (equal lam; Easton's
   482	    four-member Outputs block also gives mu = 1/2 for (P, J)); Almond drops F with l0 = P;
   483	    Aristotle and Weber differ in s^J or s^C with a and b also holding (1/2, 1/2) in I.
   484	    """
   485	    if k not in _WITNESSES:
   486	        raise ValueError(f"unknown encoding {k!r}")
   487	    return _WITNESSES[k]()
   488	
   489	
   490	def coarsenings_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   491	    """Coarsened profiles equal component by component (identity on actor names)."""
   492	    return structurally_equal(F, G)

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/representation.py | sed -n '350,620p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   350	    pairs = list(itertools.combinations(F.pillars, 2))
   351	    C = {frozenset((m, n)): max((min(row.get(m, 0.0), row.get(n, 0.0))
   352	                                 for row in F.kappa.values()), default=0.0)
   353	         for m, n in pairs}
   354	    I = sum(C.values()) / len(pairs) if pairs else 0.0  # noqa: E741
   355	    cap = U >= thresholds.u_star and I >= thresholds.i_star and bool(F.links)
   356	    inter = (is_strongly_connected(_underlying(F.arcs, F.pillars), set(F.pillars))
   357	             and _cascade_complete(F.arcs, F.pillars))
   358	    return PreservedQuantities(H, float(U), C, float(I), cap, inter)
   359	
   360	
   361	def _r(x: float) -> float:
   362	    return round(float(x), _ROUND) + 0.0
   363	
   364	
   365	def _same(a: float, b: float) -> bool:
   366	    return abs(a - b) <= _ATOL
   367	
   368	
   369	def _actor_signature(F: FormalizedStructure, k: int, with_layers: bool) -> tuple:
   370	    v = F.actors[k]
   371	    sig = (
   372	        tuple(sorted(F.roles[v])),
   373	        tuple(_r(F.shares[m][v]) for m in F.pillars),
   374	        tuple(sorted((m, a == v, b == v) for a, b, m in F.links if v in (a, b))),
   375	        tuple(sorted(tuple(_r(r.get(m, 0.0)) for m in F.pillars)
   376	                     for S, r in F.kappa.items() if v in S)),
   377	    )
   378	    if with_layers:
   379	        sig += tuple((tuple(sorted(_r(x) for x in F.layers[m][k])),
   380	                      tuple(sorted(_r(x) for x in F.layers[m][:, k]))) for m in F.pillars)
   381	    return sig
   382	
   383	
   384	def find_bijection(F: FormalizedStructure, G: FormalizedStructure,
   385	                   with_layers: bool) -> dict[str, str] | None:
   386	    """An actor bijection phi: V_F -> V_G under which roles, shares, Q, omega, kappa
   387	    (transported: kappa_F(S) = kappa_G(phi(S))), links and D agree, and, if ``with_layers``,
   388	    every layer entry. None if there is none.
   389	
   390	    Numbers are compared EXACTLY after quantization to 12 decimals (``_r``), the same
   391	    normalization the canonical form uses, so equality is an equivalence relation.
   392	
   393	    Backtracking within classes of equal actor signatures; the identity on names is tried
   394	    first. Both structures must be ``well_formed``.
   395	    """
   396	    if not (well_formed(F) and well_formed(G)):
   397	        return None
   398	    if F.pillars != G.pillars or len(F.actors) != len(G.actors) or F.arcs != G.arcs:
   399	        return None
   400	    if any(_r(F.contestability[m]) != _r(G.contestability[m])
   401	           or _r(F.weights[m]) != _r(G.weights[m]) for m in F.pillars):
   402	        return None
   403	    if len(F.kappa) != len(G.kappa) or len(F.links) != len(G.links):
   404	        return None
   405	    sig_f = [_actor_signature(F, k, with_layers) for k in range(len(F.actors))]
   406	    sig_g = [_actor_signature(G, k, with_layers) for k in range(len(G.actors))]
   407	    if sorted(sig_f) != sorted(sig_g):
   408	        return None
   409	    gi = {v: k for k, v in enumerate(G.actors)}
   410	    fi = {v: k for k, v in enumerate(F.actors)}
   411	    order = sorted(range(len(F.actors)), key=lambda k: sig_f[k])
   412	    assign: dict[int, int] = {}
   413	    used: set[int] = set()
   414	
   415	    def consistent(i: int, j: int) -> bool:
   416	        if with_layers:
   417	            for i2, j2 in assign.items():
   418	                for m in F.pillars:
   419	                    if (_r(F.layers[m][i, i2]) != _r(G.layers[m][j, j2])
   420	                            or _r(F.layers[m][i2, i]) != _r(G.layers[m][j2, j])):
   421	                        return False
   422	        mapped = {**assign, i: j}
   423	        for a, b, m in F.links:
   424	            ia, ib = fi[a], fi[b]
   425	            if ia in mapped and ib in mapped:
   426	                if (G.actors[mapped[ia]], G.actors[mapped[ib]], m) not in G.links:
   427	                    return False
   428	        return True
   429	
   430	    def kappa_ok() -> bool:
   431	        to_g = {F.actors[i]: G.actors[j] for i, j in assign.items()}
   432	        for S, row in F.kappa.items():
   433	            other = G.kappa.get(frozenset(to_g[v] for v in S))
   434	            if other is None or set(other) != set(row):
   435	                return False
   436	            if any(_r(row[m]) != _r(other[m]) for m in row):
   437	                return False
   438	        return True
   439	
   440	    def search(pos: int) -> bool:
   441	        if pos == len(order):
   442	            return kappa_ok()
   443	        i = order[pos]
   444	        cands = [j for j in range(len(G.actors)) if j not in used and sig_g[j] == sig_f[i]]
   445	        pref = gi.get(F.actors[i])
   446	        if pref in cands:
   447	            cands.remove(pref)
   448	            cands.insert(0, pref)
   449	        for j in cands:
   450	            if consistent(i, j):
   451	                assign[i] = j
   452	                used.add(j)
   453	                if search(pos + 1):
   454	                    return True
   455	                del assign[i]
   456	                used.discard(j)
   457	        return False
   458	
   459	    if not search(0):
   460	        return None
   461	    return {F.actors[i]: G.actors[j] for i, j in assign.items()}
   462	
   463	
   464	def equivalent_A(F: FormalizedStructure, G: FormalizedStructure) -> bool:  # noqa: N802
   465	    """F and G agree on roles, shares, Q, omega, kappa, links and D under an actor bijection
   466	    (layers not compared; see ``uniqueness.p_equal`` for the version with layers)."""
   467	    return find_bijection(F, G, with_layers=False) is not None
   468	
   469	
   470	# Coarsenings (minimality) ------------------------------------------------------------------
   471	
   472	
   473	def drop(F: FormalizedStructure, m: Label) -> FormalizedStructure:
   474	    """Delete pillar m: its layer, shares, Q, kappa column and every hyperarc involving m.
   475	
   476	    Remaining weights are renormalized to sum 1.
   477	    """
   478	    if m not in F.pillars:
   479	        raise ValueError(f"unknown pillar {m!r}")
   480	    keep = tuple(p for p in F.pillars if p != m)
   481	    total = sum(F.weights[p] for p in keep)
   482	    weights = {p: (F.weights[p] / total if total > 0 else 1.0 / len(keep)) for p in keep}
   483	    return FormalizedStructure(
   484	        actors=F.actors, pillars=keep,
   485	        roles={v: ps - {m} for v, ps in F.roles.items()},
   486	        layers={p: F.layers[p] for p in keep},
   487	        shares={p: dict(F.shares[p]) for p in keep},
   488	        contestability={p: F.contestability[p] for p in keep},
   489	        weights=weights,
   490	        kappa={s: {p: row.get(p, 0.0) for p in keep} for s, row in F.kappa.items()},
   491	        links=frozenset(lk for lk in F.links if lk[2] != m),
   492	        arcs=frozenset((t, h) for t, h in F.arcs if h != m and m not in t),
   493	    )
   494	
   495	
   496	def merge(F: FormalizedStructure, m: Label, n: Label, lam: float) -> FormalizedStructure:
   497	    """Replace m, n by one pillar 'm+n': holders united, shares, layers, Q and kappa mixed with
   498	    weight lam on m; omega_m + omega_n; arcs relabeled, self-loops removed."""
   499	    if m == n or m not in F.pillars or n not in F.pillars:
   500	        raise ValueError("merge needs two distinct existing pillars")
   501	    lam = validate_unit_interval(lam, "lam")
   502	    new = f"{m}+{n}"
   503	    keep = tuple(new if p == m else p for p in F.pillars if p != n)
   504	    relabel = lambda p: new if p in (m, n) else p  # noqa: E731
   505	
   506	    def mix(a: float, b: float) -> float:
   507	        return lam * a + (1.0 - lam) * b
   508	
   509	    shares = {p: dict(F.shares[p]) for p in keep if p != new}
   510	    shares[new] = {v: mix(F.shares[m].get(v, 0.0), F.shares[n].get(v, 0.0)) for v in F.actors}
   511	    layers = {p: F.layers[p] for p in keep if p != new}
   512	    layers[new] = lam * F.layers[m] + (1.0 - lam) * F.layers[n]
   513	    contest = {p: F.contestability[p] for p in keep if p != new}
   514	    contest[new] = mix(F.contestability[m], F.contestability[n])
   515	    weights = {p: F.weights[p] for p in keep if p != new}
   516	    weights[new] = F.weights[m] + F.weights[n]
   517	    kappa = {}
   518	    for s, row in F.kappa.items():
   519	        r = {p: row.get(p, 0.0) for p in keep if p != new}
   520	        r[new] = mix(row.get(m, 0.0), row.get(n, 0.0))
   521	        kappa[s] = r
   522	    arcs = set()
   523	    for t, h in F.arcs:
   524	        t2, h2 = frozenset(relabel(x) for x in t), relabel(h)
   525	        if h2 not in t2:
   526	            arcs.add((t2, h2))
   527	    return FormalizedStructure(
   528	        actors=F.actors, pillars=keep,
   529	        roles={v: frozenset(relabel(p) for p in ps) for v, ps in F.roles.items()},
   530	        layers=layers, shares=shares, contestability=contest, weights=weights, kappa=kappa,
   531	        links=frozenset((a, b, relabel(p)) for a, b, p in F.links),
   532	        arcs=frozenset(arcs),
   533	    )
   534	
   535	
   536	def structurally_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   537	    """Equality of every component with the identity on actor names (floats within 1e-9)."""
   538	    if not (well_formed(F) and well_formed(G)):
   539	        return False
   540	    if (F.actors, F.pillars, F.links, F.arcs) != (G.actors, G.pillars, G.links, G.arcs):
   541	        return False
   542	    if any(F.roles[v] != G.roles[v] for v in F.actors) or set(F.kappa) != set(G.kappa):
   543	        return False
   544	    return (
   545	        all(_same(F.shares[m][v], G.shares[m][v]) for m in F.pillars for v in F.actors)
   546	        and all(np.allclose(F.layers[m], G.layers[m], atol=_ATOL, rtol=0) for m in F.pillars)
   547	        and all(_same(F.contestability[m], G.contestability[m]) for m in F.pillars)
   548	        and all(_same(F.weights[m], G.weights[m]) for m in F.pillars)
   549	        and all(set(F.kappa[S]) == set(G.kappa[S])
   550	                and all(_same(F.kappa[S][m], G.kappa[S][m]) for m in F.kappa[S])
   551	                for S in F.kappa)
   552	    )
   553	
   554	
   555	D_STAR_LABELS: frozenset[LabelArc] = frozenset(
   556	    (frozenset(t.name for t in tail), head.name) for tail, head in D_STAR_KEYS
   557	)
   558	
   559	
   560	def make_structure(
   561	    shares: Mapping[Label, Mapping[str, float]],
   562	    contestability: Mapping[Label, float],
   563	    weights: Mapping[Label, float] | None = None,
   564	    kappa: Mapping[frozenset[str], Mapping[Label, float]] | None = None,
   565	    links: Iterable[tuple[str, str, Label]] = (),
   566	    arcs: Iterable[LabelArc] = D_STAR_LABELS,
   567	) -> FormalizedStructure:
   568	    """Build F directly: holders are actors with positive share, a^m_ij = s^m_i (i != j),
   569	    singleton coalitions by default. Used for the minimality fixtures."""
   570	    pillars = tuple(shares)
   571	    actors = tuple(sorted({v for s in shares.values() for v in s}))
   572	    full = {m: {v: float(shares[m].get(v, 0.0)) for v in actors} for m in pillars}
   573	    roles = {v: frozenset(m for m in pillars if full[m][v] > 0) for v in actors}
   574	    layers = {}
   575	    for m in pillars:
   576	        arr = np.tile(np.array([full[m][v] for v in actors])[:, None], (1, len(actors)))
   577	        np.fill_diagonal(arr, 0.0)
   578	        layers[m] = arr
   579	    if kappa is None:
   580	        kappa = {frozenset({v}): {m: full[m][v] for m in pillars} for v in actors}
   581	    return FormalizedStructure(
   582	        actors=actors, pillars=pillars, roles=roles, layers=layers, shares=full,
   583	        contestability=dict(contestability),
   584	        weights=dict(weights) if weights else {m: 1.0 / len(pillars) for m in pillars},
   585	        kappa={s: dict(r) for s, r in kappa.items()},
   586	        links=frozenset(links), arcs=frozenset(arcs),
   587	    )

codex
The repository has no commits, so there is no Git baseline to diff against; I’m treating the current contents of the seven scoped files as the review target. I’ve confirmed the two round-9 implementations are present and am now stress-checking their invariance logic rather than relying on the added tests alone.
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '421,820p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   421	
   422	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   423	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   424	
   425	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   426	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   427	    """
   428	    out: dict[Axiom, Derivation] = {}
   429	    for axiom in Axiom:
   430	        if not system.holds(axiom):
   431	            continue
   432	        pillar = AXIOM_TO_PILLAR[axiom]
   433	        out[axiom] = Derivation(
   434	            axiom=axiom,
   435	            pillar=pillar,
   436	            form=realized_form(system, pillar),
   437	            practices=tuple(p for p in system.practices if p.solves is axiom),
   438	        )
   439	    return out
   440	
   441	
   442	# Proposition A and interdependence --------------------------------------------------------
   443	
   444	
   445	@dataclass(frozen=True)
   446	class PropositionAResult:
   447	    """Outcome of checking Proposition A on one coded system (Part VII Cor 5.5, Thm 5.10).
   448	
   449	    ``struct``: all six pillars realized (Thm 4.3) AND every D0 relation generated (Cor 5.5,
   450	    from Ax1..Ax6). ``interdependent``: all six realized and the generated hypergraph strongly
   451	    connected (underlying digraph) AND cascade-complete (Thm 5.10, from Ax1..Ax6 plus
   452	    Assumptions 5.6 to 5.9, i.e. X1, X2, X3, X5; the role of each premise is Prop 5.11).
   453	    ``holds`` is Proposition A in full: struct AND interdependent.
   454	
   455	    ``counterexample``: persistent, the extended axiom set holds, yet ``holds`` is False.
   456	    ``struct_counterexample``: persistent, Ax1..Ax6 hold, yet ``struct`` is False.
   457	    """
   458	
   459	    system: str
   460	    antecedent: bool
   461	    realized: frozenset[Pillar]
   462	    missing: frozenset[Pillar]
   463	    dependencies: frozenset[ArcKey]
   464	    missing_dependencies: frozenset[ArcKey]
   465	    strongly_connected: bool
   466	    cascade_complete: bool
   467	    struct: bool
   468	    interdependence_antecedent: bool
   469	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   470	
   471	    @property
   472	    def interdependent(self) -> bool:
   473	        return not self.missing and self.strongly_connected and self.cascade_complete
   474	
   475	    @property
   476	    def holds(self) -> bool:
   477	        return self.struct and self.interdependent
   478	
   479	    @property
   480	    def struct_counterexample(self) -> bool:
   481	        return self.antecedent and not self.struct
   482	
   483	    @property
   484	    def counterexample(self) -> bool:
   485	        return self.interdependence_antecedent and not self.holds
   486	
   487	
   488	def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
   489	    """Check Proposition A (struct and interdependence) on ``system`` (Part VII; KB 4.3).
   490	
   491	    A D0 relation is demanded when its head and every tail member are realized.
   492	    """
   493	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   494	    deps = generate_dependencies(system)
   495	    needed = frozenset((t, h) for t, h in D0_KEYS if h in realized and t <= realized)
   496	    missing_deps = needed - deps
   497	    return PropositionAResult(
   498	        system=system.name,
   499	        antecedent=system.persistent and system.all_axioms_hold,
   500	        realized=realized,
   501	        missing=frozenset(PILLARS) - realized,
   502	        dependencies=deps,
   503	        missing_dependencies=missing_deps,
   504	        strongly_connected=is_strongly_connected(underlying_digraph(deps), realized),
   505	        cascade_complete=is_cascade_complete(deps, realized),
   506	        struct=realized == frozenset(PILLARS) and not missing_deps,
   507	        interdependence_antecedent=system.persistent and system.extended_axioms_hold,
   508	        derivations=derive_functions(system),
   509	    )
   510	
   511	
   512	def formal_system(
   513	    name: str,
   514	    holders: Mapping[Pillar, Iterable[str]],
   515	    persistent: bool = True,
   516	    source: str = "",
   517	    axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS,
   518	) -> GovernanceSystem:
   519	    """A persistent system whose pillars are held by formal organizations.
   520	
   521	    An actor listed under several pillars is fused. By default the extended axiom set is
   522	    coded as holding: an assumption of the stylized model, not an observation. Used for regime
   523	    profiles and counter-models.
   524	    """
   525	    practices = tuple(
   526	        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
   527	                 frozenset(hs), formal=True, source=source)
   528	        for m, hs in holders.items()
   529	        if hs
   530	    )
   531	    return GovernanceSystem(name, persistent, frozenset(axioms), practices)
   532	
   533	
   534	# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
   535	# Each codes the extended axiom set as holding. The X1, X2, X3, X5 codings are QUALITATIVE
   536	# readings of the ethnography (sources in X_CODING_SOURCES), each open to the falsifier
   537	# stated on IncidenceAxiom.
   538	
   539	
   540	def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
   541	    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)
   542	
   543	
   544	NUER = GovernanceSystem(
   545	    name="Nuer ('ordered anarchy')",
   546	    persistent=True,
   547	    axioms=EXTENDED_AXIOMS,
   548	    practices=(
   549	        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
   550	                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
   551	        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
   552	                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
   553	        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
   554	                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
   555	        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
   556	                  {"prophets", "lineages"}, "evanspritchard1940"),
   557	        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
   558	                  {"agnatic kin"}, "evanspritchard1940"),
   559	        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
   560	                  "evanspritchard1940"),
   561	    ),
   562	    note="no office holds coercive authority; functions exist without separation",
   563	)
   564	
   565	JU_HOANSI = GovernanceSystem(
   566	    name="Ju/'hoansi (!Kung)",
   567	    persistent=True,
   568	    axioms=EXTENDED_AXIOMS,
   569	    practices=(
   570	        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
   571	                  {"hunters", "camp members"}, "lee2013; marshall1976"),
   572	        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
   573	                  {"camp members"}, "lee2013"),
   574	        _informal("disputes talked out with kin mediators", Axiom.Ax3,
   575	                  {"kin mediators"}, "lee1979; wiessner2005"),
   576	        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
   577	                  {"healers", "camp members"}, "marshall1976"),
   578	        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
   579	                  {"camp members"}, "wiessner2005; lee2013"),
   580	        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
   581	    ),
   582	    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
   583	)
   584	
   585	OSTROM_COMMONS = GovernanceSystem(
   586	    name="Ostrom commons (design principles)",
   587	    persistent=True,
   588	    axioms=EXTENDED_AXIOMS,
   589	    practices=(
   590	        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
   591	                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
   592	        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
   593	                  {"appropriators"}, "ostrom1990"),
   594	        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
   595	                  {"appropriators"}, "ostrom1990; cox2010"),
   596	        _informal("shared norms; minimal recognition of rights to organize (DP7)",
   597	                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),
   598	        _informal("monitoring and graduated sanctions by appropriators (DP4, DP5)",
   599	                  Axiom.Ax5, {"appropriators"}, "ostrom1990; cox2010"),
   600	        _informal("appropriation and maintenance labor", Axiom.Ax6, {"appropriators"},
   601	                  "ostrom1990"),
   602	    ),
   603	    note="checks in minimal form; monitors are appropriators or accountable to them",
   604	)
   605	
   606	CONSENSUS_VILLAGE = GovernanceSystem(
   607	    name="Consensus village (stylized)",
   608	    persistent=True,
   609	    axioms=EXTENDED_AXIOMS,
   610	    practices=(
   611	        _informal("household plots; reciprocal labor exchange; sharing norms", Axiom.Ax1,
   612	                  {"households"}, "sahlins1972"),
   613	        _informal("consensus meeting of adults", Axiom.Ax2, {"village meeting"},
   614	                  "clastres1987; boehm1999"),
   615	        _informal("elders mediate disputes", Axiom.Ax3, {"elders"}, "boehm1999"),
   616	        _informal("ritual and myth; moral talk", Axiom.Ax4, {"village meeting", "elders"},
   617	                  "boehm1999"),
   618	        _informal("gossip, shunning, ostracism of would-be dominants", Axiom.Ax5,
   619	                  {"village meeting"}, "boehm1999; woodburn1982"),
   620	        _informal("gardening and household labor", Axiom.Ax6, {"households"},
   621	                  "sahlins1972"),
   622	    ),
   623	    note="stylized composite; reverse dominance hierarchy",
   624	)
   625	
   626	HARD_CASES: tuple[GovernanceSystem, ...] = (NUER, JU_HOANSI, OSTROM_COMMONS, CONSENSUS_VILLAGE)
   627	
   628	_X1, _X2, _X3, _X5 = IncidenceAxiom
   629	#: Qualitative codings of the incidence axioms for the hard cases (Part VII), with sources.
   630	X_CODING_SOURCES: dict[str, dict[IncidenceAxiom, str]] = {
   631	    NUER.name: {
   632	        _X1: "cattle and grazing rights (evanspritchard1940)",
   633	        _X2: "norms adjusted by negotiation among lineages (evanspritchard1940)",
   634	        _X3: "cattle compensation fixed through the leopard-skin chief (evanspritchard1940)",
   635	        _X5: "feud over cattle (evanspritchard1940)",
   636	    },
   637	    JU_HOANSI.name: {
   638	        _X1: "kin-based n!ore rights to territory and water (lee2013)",
   639	        _X2: "camp talk and fission (lee2013)",
   640	        _X3: "disputes over sharing talked out (lee2013; wiessner2005)",
   641	        _X5: "criticism of failures to share (wiessner2005)",
   642	    },
   643	    OSTROM_COMMONS.name: {
   644	        _X1: "boundary and appropriation rules (ostrom1990)",
   645	        _X2: "users modify their rules (ostrom1990)",
   646	        _X3: "conflict-resolution arenas (ostrom1990; cox2010)",
   647	        _X5: "monitoring and graduated sanctions (ostrom1990)",
   648	    },
   649	    CONSENSUS_VILLAGE.name: {
   650	        _X1: "household plots under sharing norms (sahlins1972)",
   651	        _X2: "seasonal re-arrangement (graeber2021)",
   652	        _X3: "elders mediate residual disputes (boehm1999)",
   653	        _X5: "sharing enforced against hoarders (boehm1999)",
   654	    },
   655	}
   656	
   657	
   658	# Axiom independence fixtures (Part VII spec, item 7). ---------------------------------------
   659	
   660	#: Consistency model: the extended axiom set holds and all six pillars are realized (the
   661	#: consensus village coding).
   662	BASELINE_MODEL: GovernanceSystem = CONSENSUS_VILLAGE
   663	
   664	
   665	def without_axiom(axiom: AnyAxiom, base: GovernanceSystem = BASELINE_MODEL) -> GovernanceSystem:
   666	    """``base`` with one axiom removed; for Ax_k the practices solving Ax_k are removed too."""
   667	    practices = base.practices
   668	    if isinstance(axiom, Axiom):
   669	        practices = tuple(p for p in practices if p.solves is not axiom)
   670	    return GovernanceSystem(
   671	        name=f"{base.name} without {axiom.name} ({axiom.label})",
   672	        persistent=base.persistent,
   673	        axioms=base.axioms - {axiom},
   674	        practices=practices,
   675	        absent_incidences=base.absent_incidences,
   676	        note="hypothetical: one axiom removed",
   677	    )
   678	
   679	
   680	#: Part VII R1, the k = 4 independence model: innate rules, no initiation, a fine d >= g on
   681	#: defiance of a determination (so rulings bind through C alone), ell = 0, Pr(Pi) = 1;
   682	#: Impl_I fails.
   683	R1_AX4_MODEL = GovernanceSystem(
   684	    name="R1: independence model for Ax4",
   685	    persistent=True,
   686	    axioms=BASELINE_MODEL.axioms - {Axiom.Ax4},
   687	    practices=tuple(p for p in BASELINE_MODEL.practices if p.solves is not Axiom.Ax4) + (
   688	        Practice("fine d >= g on defiance of a determination", Axiom.Ax5,
   689	                 frozenset({"village meeting"}), source="Part VII R1"),
   690	    ),
   691	    note="innate rules, no initiation, ell = 0, Pr(Pi) = 1; Impl_I fails",
   692	)
   693	
   694	#: For each k: persistent, Ax_k removed, pillar k missing (k = 4 is the R1 model). Theorem A's
   695	#: antecedent is false, so none is a counterexample; each shows pillar k is not forced by the
   696	#: other five axioms.
   697	AXIOM_INDEPENDENCE: dict[Axiom, GovernanceSystem] = {
   698	    a: (R1_AX4_MODEL if a is Axiom.Ax4 else without_axiom(a)) for a in Axiom
   699	}
   700	
   701	
   702	# Part VII Prop 4.4(a) model and its Lemma 5.4 variant (Ax1..Ax6, no incidence axioms). ------
   703	
   704	_M = frozenset({"members"})
   705	PROP_4_4A_MODEL = GovernanceSystem(
   706	    name="Prop 4.4(a) model",
   707	    persistent=True,
   708	    axioms=frozenset(Axiom),
   709	    practices=(
   710	        Practice("plot claimed each period by the most recent entrant and one other member; "
   711	                 "assigned by lot", Axiom.Ax1, _M, source="Part VII Prop 4.4(a)"),
   712	        Practice("members make their own rules; the longest-serving member is replaced every "
   713	                 "L periods", Axiom.Ax2, _M, source="Part VII Prop 4.4(a)"),
   714	        Practice("the lot determines each residual dispute", Axiom.Ax3, _M,
   715	                 source="Part VII Prop 4.4(a)"),
   716	        Practice("the lot is presented as rightful at initiation (ell from I); entrants do not "
   717	                 "know the rules at entry; no forgetting", Axiom.Ax4, _M,
   718	                 source="Part VII Prop 4.4(a)"),
   719	        Practice("camp chores rule with fine d; members best-respond", Axiom.Ax5, _M,
   720	                 source="Part VII Prop 4.4(a)"),
   721	        Practice("each member forages alone at any campsite", Axiom.Ax6, _M,
   722	                 source="Part VII Prop 4.4(a)"),
   723	    ),
   724	    note="struct holds, interdependence fails: no arc into W (Prop 5.11(a))",
   725	)
   726	
   727	#: Lemma 5.4 variant: the fine d >= g also attaches to defiance of a determination, so J is
   728	#: served by C as well as I; neither I -> J nor C -> J alone is forced (the OR-hyperarc).
   729	PROP_4_4A_VARIANT = GovernanceSystem(
   730	    name="Prop 4.4(a) model, Lemma 5.4 variant",
   731	    persistent=True,
   732	    axioms=frozenset(Axiom),
   733	    practices=PROP_4_4A_MODEL.practices + (
   734	        Practice("fine d >= g on defiance of a determination", Axiom.Ax5, _M,
   735	                 source="Part VII Lemma 5.4"),
   736	    ),
   737	    note="witness that neither I -> J nor C -> J is forced",
   738	)
   739	
   740	
   741	# Admissible assignments (Part VII F5) ----------------------------------------------------
   742	
   743	
   744	def is_admissible(
   745	    system: GovernanceSystem,
   746	    members: Iterable[str],
   747	    organizations: Mapping[str, Iterable[str]] | None = None,
   748	    dispute_parties: Mapping[str, Iterable[str]] | None = None,
   749	) -> bool:
   750	    """Admissible Lambda (Part VII F5), on the coded information available.
   751	
   752	    (i) every assigned agent is a member or an organization of members (whose consumption
   753	    is counted); (ii) no party to a residual dispute alone controls its determination: a J
   754	    practice with a single holder may not have that holder, or any of its members, among
   755	    ``dispute_parties[practice.description]``; (iii) rule-making (P) practices are the
   756	    members' own, which (i) already requires of their holders.
   757	    """
   758	    mem = frozenset(members)
   759	    orgs = {k: frozenset(v) for k, v in (organizations or {}).items()}
   760	    parties = {k: frozenset(v) for k, v in (dispute_parties or {}).items()}
   761	    for p in system.practices:
   762	        for h in p.holders:
   763	            if h not in mem and not (h in orgs and orgs[h] and orgs[h] <= mem):
   764	                return False
   765	        if p.solves is Axiom.Ax3 and len(p.holders) == 1:
   766	            (h,) = p.holders
   767	            involved = parties.get(p.description, frozenset())
   768	            if h in involved or orgs.get(h, frozenset()) & involved:
   769	                return False
   770	    return True

exec
/usr/local/bin/zsh -lc "nl -ba model/tests/test_uniqueness.py | sed -n '1,420p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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
    39	    witness_record,
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
   259	    F_ = represent(witness_record({"P": (1.0, 0.0)}))
   260	    assert encode_aristotle(F_) == ("one", "correct")
   261	    assert encode_aristotle(represent(record_from_polity(fused_polity()))) == ("one", "deviant")
   262	    assert encode_aristotle(represent(record_from_polity(plural_polity())))[0] == "few"
   263	
   264	
   265	def test_weber_label_is_not_determined_by_p():
   266	    rec = witness_record({"I": (0.5, 0.5)})
   267	    F_ = represent(rec)
   268	    assert p_equal(F_, represent(rec))
   269	    assert encode_weber(F_, "traditional", False) != encode_weber(F_, "legal-rational", True)
   270	    with pytest.raises(ValueError):
   271	        encode_weber(F_, "theocratic", True)
   272	
   273	
   274	def test_drop_witness_keeps_b_as_actor_via_retained_pillar():
   275	    g1, g2 = witness_pair("almond")
   276	    r1, r2 = represent(g1), represent(g2)
   277	    assert r1.actors == r2.actors == ("a", "b", "c")
   278	    assert r1.shares["F"]["b"] == 0.0 and "F" in r1.roles["b"]
   279	    assert r1.shares["P"] == r2.shares["P"] == {"a": 0.5, "b": 0.5, "c": 0.0}
   280	
   281	
   282	def test_merge_witness_actors_hold_only_the_merged_pillars():
   283	    g1, _ = witness_pair("mann")
   284	    r1 = represent(g1)
   285	    assert r1.roles["a"] == r1.roles["b"] == frozenset({"P", "J"})
   286	    assert r1.roles["c"] == frozenset({"F", "I", "C", "W"})
   287	
   288	
   289	def test_bijective_coarsenings_are_p_preserving():
   290	    # Thm 7.8 (coarsenings): Phi_c is P-preserving iff c is a bijection onto |K| = 6.
   291	    rng = np.random.default_rng(3)
   292	    F_ = represent(record_from_polity(regime_profiles()[0].polity))
   293	    for _ in range(10):
   294	        perm = rng.permutation(6)
   295	        c = {m: f"k{perm[i]}" for i, m in enumerate(M_LABELS)}
   296	        back = {f"k{perm[i]}": m for i, m in enumerate(M_LABELS)}
   297	        G_ = coarsen(F_, c)
   298	        assert len(G_.pillars) == 6
   299	        restored = coarsen(G_, back)
   300	        reordered = FormalizedStructure(**{**restored.__dict__, "pillars": M_LABELS})
   301	        assert structurally_equal(reordered, F_)
   302	        with pytest.raises(ValueError):
   303	            witness_coarsening(c)
   304	
   305	
   306	def _cycle(n: int, x: float = 0.4) -> FormalizedStructure:
   307	    from beast_system.representation import make_structure
   308	
   309	    base = make_structure({p: {f"v{k}": 1.0 / n for k in range(n)} for p in M_LABELS},
   310	                          {p: 0.5 for p in M_LABELS})
   311	    layers = {}
   312	    for p in M_LABELS:
   313	        arr = np.zeros((n, n))
   314	        for k in range(n):
   315	            arr[k, (k + 1) % n] = x
   316	        layers[p] = arr
   317	    return FormalizedStructure(**{**base.__dict__, "layers": layers})
   318	
   319	
   320	def test_canonical_form_is_total_on_symmetric_structures():
   321	    from beast_system.uniqueness import canonical_form
   322	
   323	    nine = _cycle(9)
   324	    form = canonical_form(nine)  # previously exceeded the 9! branch guard
   325	    ren = {v: f"w{(k * 4) % 9}" for k, v in enumerate(nine.actors)}
   326	    relabeled = FormalizedStructure(
   327	        actors=tuple(sorted(ren.values())), pillars=nine.pillars,
   328	        roles={ren[v]: r for v, r in nine.roles.items()},
   329	        layers={p: a[np.ix_([nine.actors.index(v) for v in sorted(nine.actors, key=lambda v: ren[v])],
   330	                            [nine.actors.index(v) for v in sorted(nine.actors, key=lambda v: ren[v])])]
   331	                for p, a in nine.layers.items()},
   332	        shares={p: {ren[v]: x for v, x in sh.items()} for p, sh in nine.shares.items()},
   333	        contestability=nine.contestability, weights=nine.weights,
   334	        kappa={frozenset(ren[v] for v in S): r for S, r in nine.kappa.items()},
   335	        links=nine.links, arcs=nine.arcs)
   336	    assert p_equal(nine, relabeled) and canonical_form(relabeled) == form
   337	    # Two cycles of 4 and 5 are not isomorphic to one 9-cycle.
   338	    split = _cycle(9)
   339	    layers = {p: a.copy() for p, a in split.layers.items()}
   340	    for p in layers:
   341	        layers[p][3, 4] = 0.0
   342	        layers[p][3, 0] = 0.4
   343	        layers[p][8, 0] = 0.0
   344	        layers[p][8, 4] = 0.4
   345	    split = FormalizedStructure(**{**split.__dict__, "layers": layers})
   346	    assert not p_equal(nine, split) and canonical_form(split) != form
   347	
   348	
   349	def test_p_equal_and_canonical_form_use_one_normalization():
   350	    from beast_system.uniqueness import canonical_form
   351	
   352	    F_ = represent(record_from_polity(fused_polity()))
   353	    for eps in (5e-10, 1e-14):
   354	        G_ = FormalizedStructure(**{**F_.__dict__, "contestability":
   355	                                    {**F_.contestability, "J": F_.contestability["J"] + eps}})
   356	        assert p_equal(F_, G_) == (canonical_form(F_) == canonical_form(G_))

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '1,420p'" in /Users/mlong/Documents/Development/the-beast-system
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
   237	#: Further rules (Part VII Remark 5.12): reported, not needed for interdependence. Each rests on a premise beyond
   238	#: the extended axiom set (stated in ``premise``); ``rules_holding`` skips non-core rules, so
   239	#: none is ever generated for a system.
   240	FURTHER_RULES: tuple[DependencyRule, ...] = (
   241	    _inc(_A.Ax4, _P.P, "X2 + Ax4", (_A.Ax2, _X.X2), "recognition of rule change", core=False),
   242	    _inc(_A.Ax2, _P.J, "X2 + Ax4", (_A.Ax4, _X.X2), "new rules to interpret", core=False),
   243	    _inc(_A.Ax2, _P.I, "X2 + Ax4", (_A.Ax4, _X.X2), "new rules to be made common knowledge",
   244	         core=False),
   245	    _inc(_A.Ax3, _P.P, "precedent (Hart)", (), "interpretation feeds rule change", core=False),
   246	    _inc(_A.Ax4, _P.C, "Ax4 at C's rules", (),
   247	         "an entrant is deterred only once informed of the sanction rule", core=False),
   248	    DependencyRule(frozenset({_P.F, _P.I}), _P.C, "Part V Cor 3.7 conditions",
   249	                   frozenset({_A.Ax1, _A.Ax4, _A.Ax5}),
   250	                   "costly public-good sanctions at large n, no higher-order sanctions",
   251	                   core=False),
   252	)
   253	
   254	D_STAR_KEYS: frozenset[ArcKey] = frozenset(r.key for r in CORE_RULES)
   255	#: D0: the core relations generated by Ax1..Ax6 alone (W -> m for m != W, the OR-hyperarc
   256	#: {I, C} -> J, and I -> F); Part VII Thm 4.3.
   257	D0_KEYS: frozenset[ArcKey] = frozenset(
   258	    r.key for r in CORE_RULES if not any(isinstance(a, IncidenceAxiom) for a in r.requires)
   259	)
   260	
   261	#: The six single arcs named in the original model brief (kept for comparison only).
   262	BRIEF_ARCS: frozenset[ArcKey] = frozenset(
   263	    arc_key(t, h) for t, h in [(_P.W, _P.C), (_P.P, _P.J), (_P.I, _P.P), (_P.J, _P.F),
   264	                               (_P.F, _P.W), (_P.W, _P.I)]
   265	)
   266	
   267	
   268	def rules_holding(
   269	    axioms: Iterable[AnyAxiom], rules: Iterable[DependencyRule] = CORE_RULES
   270	) -> tuple[DependencyRule, ...]:
   271	    """The CORE rules whose premises all hold under ``axioms``.
   272	
   273	    Non-core (further) rules are never generated, whatever ``axioms`` contains.
   274	    """
   275	    held = frozenset(axioms)
   276	    return tuple(r for r in rules if r.core and r.requires <= held)
   277	
   278	
   279	def dependency_graph(axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS) -> dict[Pillar, frozenset[Pillar]]:
   280	    """Underlying digraph of the core rules generated under ``axioms`` (default: all)."""
   281	    return underlying_digraph(rules_holding(axioms))
   282	
   283	
   284	# Governance systems ------------------------------------------------------------------------
   285	
   286	
   287	@dataclass(frozen=True)
   288	class Practice:
   289	    """A regular activity that discharges the problem generated by axiom ``solves``.
   290	
   291	    ``formal`` is True when the activity is attached to a designated office or organization.
   292	    ``source`` holds the citation key(s) supporting the coding.
   293	    """
   294	
   295	    description: str
   296	    solves: Axiom
   297	    holders: frozenset[str]
   298	    formal: bool = False
   299	    source: str = ""
   300	
   301	    def __post_init__(self) -> None:
   302	        if not isinstance(self.solves, Axiom):
   303	            raise TypeError("Practice.solves must be an Axiom")
   304	        holders = frozenset(self.holders)
   305	        if not holders or any(not isinstance(h, str) or not h for h in holders):
   306	            raise ValueError("a practice needs at least one named holder")
   307	        if not self.description.strip():
   308	            raise ValueError("a practice needs a description")
   309	        object.__setattr__(self, "holders", holders)
   310	
   311	    @property
   312	    def pillar(self) -> Pillar:
   313	        return AXIOM_TO_PILLAR[self.solves]
   314	
   315	
   316	@dataclass(frozen=True)
   317	class GovernanceSystem:
   318	    """A collective that makes and enforces collective decisions (KB Section 4.1).
   319	
   320	    ``axioms`` lists the axioms that hold of the collective; ``persistent`` means it survives
   321	    over the period studied; it may include the incidence axioms X1, X2, X3, X5. Both are
   322	    coded independently of ``practices``. Dependencies are generated from ``axioms``;
   323	    ``absent_incidences`` records incidences Inc(k, m) OBSERVED not to arise in this system,
   324	    which suppress the arcs they would generate (the route by which a case can falsify D0 or
   325	    interdependence).
   326	    """
   327	
   328	    name: str
   329	    persistent: bool
   330	    axioms: frozenset[AnyAxiom]
   331	    practices: tuple[Practice, ...] = ()
   332	    absent_incidences: frozenset[tuple[Axiom, Pillar]] = frozenset()
   333	    note: str = ""
   334	
   335	    def __post_init__(self) -> None:
   336	        if not isinstance(self.persistent, bool):
   337	            raise TypeError("persistent must be a bool")
   338	        axioms = frozenset(self.axioms)
   339	        if any(not isinstance(a, (Axiom, IncidenceAxiom)) for a in axioms):
   340	            raise TypeError("axioms must be Axiom or IncidenceAxiom members")
   341	        practices = tuple(self.practices)
   342	        if any(not isinstance(p, Practice) for p in practices):
   343	            raise TypeError("practices must be Practice instances")
   344	        object.__setattr__(self, "axioms", axioms)
   345	        object.__setattr__(self, "practices", practices)
   346	        absent = frozenset(tuple(i) for i in self.absent_incidences)
   347	        if any(len(i) != 2 or not isinstance(i[0], Axiom) or not isinstance(i[1], Pillar)
   348	               for i in absent):
   349	            raise TypeError("absent_incidences must be (Axiom, Pillar) pairs")
   350	        object.__setattr__(self, "absent_incidences", absent)
   351	
   352	    def holds(self, axiom: AnyAxiom) -> bool:
   353	        """Predicate for one axiom (Ax1..Ax6 or an incidence axiom X_k)."""
   354	        return axiom in self.axioms
   355	
   356	    @property
   357	    def all_axioms_hold(self) -> bool:
   358	        """Ax1..Ax6 all hold (the antecedent of Theorem A)."""
   359	        return all(self.holds(a) for a in Axiom)
   360	
   361	    @property
   362	    def extended_axioms_hold(self) -> bool:
   363	        """Ax1..Ax6 and X1, X2, X3, X5 all hold (the antecedent of interdependence)."""
   364	        return EXTENDED_AXIOMS <= self.axioms
   365	
   366	
   367	def generate_dependencies(
   368	    system: GovernanceSystem, rules: Iterable[DependencyRule] = CORE_RULES
   369	) -> frozenset[ArcKey]:
   370	    """Hyperarcs generated in ``system``: rules whose premises hold, minus absent incidences."""
   371	    return frozenset(
   372	        r.key for r in rules_holding(system.axioms, rules)
   373	        if r.incidence is None or r.incidence not in system.absent_incidences
   374	    )
   375	
   376	
   377	def role_map(system: GovernanceSystem) -> dict[str, frozenset[Pillar]]:
   378	    """Role map V -> 2^M derived from practices (notation.md 'Role map')."""
   379	    roles: dict[str, set[Pillar]] = {}
   380	    for p in system.practices:
   381	        for h in p.holders:
   382	            roles.setdefault(h, set()).add(p.pillar)
   383	    return {h: frozenset(ps) for h, ps in roles.items()}
   384	
   385	
   386	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   387	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   388	
   389	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   390	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   391	    """
   392	    practices = [p for p in system.practices if p.pillar is pillar]
   393	    if not practices:
   394	        return None
   395	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   396	    if not formal_holders:
   397	        return INFORMAL
   398	    formal_roles: dict[str, set[Pillar]] = {}
   399	    for p in system.practices:
   400	        if p.formal:
   401	            for h in p.holders:
   402	                formal_roles.setdefault(h, set()).add(p.pillar)
   403	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   404	        return FUSED
   405	    return FORMAL
   406	
   407	
   408	@dataclass(frozen=True)
   409	class Derivation:
   410	    """Result of the lemma for one axiom: required pillar and its realized form."""
   411	
   412	    axiom: Axiom
   413	    pillar: Pillar
   414	    form: RealizedForm | None
   415	    practices: tuple[Practice, ...]
   416	
   417	    @property
   418	    def realized(self) -> bool:
   419	        return self.form is not None
   420	

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/tests/test_representation.py | sed -n '1,360p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '386,703p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   386	def realized_form(system: GovernanceSystem, pillar: Pillar) -> RealizedForm | None:
   387	    """How ``pillar`` is implemented in ``system``, or None if no practice implements it.
   388	
   389	    'fused' if some formal holder of the pillar also holds another pillar; 'formal
   390	    institution' if there are formal holders and none is fused; otherwise 'informal/minimal'.
   391	    """
   392	    practices = [p for p in system.practices if p.pillar is pillar]
   393	    if not practices:
   394	        return None
   395	    formal_holders = {h for p in practices if p.formal for h in p.holders}
   396	    if not formal_holders:
   397	        return INFORMAL
   398	    formal_roles: dict[str, set[Pillar]] = {}
   399	    for p in system.practices:
   400	        if p.formal:
   401	            for h in p.holders:
   402	                formal_roles.setdefault(h, set()).add(p.pillar)
   403	    if any(len(formal_roles[h]) >= 2 for h in formal_holders):
   404	        return FUSED
   405	    return FORMAL
   406	
   407	
   408	@dataclass(frozen=True)
   409	class Derivation:
   410	    """Result of the lemma for one axiom: required pillar and its realized form."""
   411	
   412	    axiom: Axiom
   413	    pillar: Pillar
   414	    form: RealizedForm | None
   415	    practices: tuple[Practice, ...]
   416	
   417	    @property
   418	    def realized(self) -> bool:
   419	        return self.form is not None
   420	
   421	
   422	def derive_functions(system: GovernanceSystem) -> dict[Axiom, Derivation]:
   423	    """For each axiom that holds, the pillar it requires and how that pillar is realized.
   424	
   425	    Lemma schema (KB Section 4.3, item 2): Ax_k + persistence => problem_k is solved by some
   426	    regularity. Axioms that fail yield no requirement, so their pillars are not derived.
   427	    """
   428	    out: dict[Axiom, Derivation] = {}
   429	    for axiom in Axiom:
   430	        if not system.holds(axiom):
   431	            continue
   432	        pillar = AXIOM_TO_PILLAR[axiom]
   433	        out[axiom] = Derivation(
   434	            axiom=axiom,
   435	            pillar=pillar,
   436	            form=realized_form(system, pillar),
   437	            practices=tuple(p for p in system.practices if p.solves is axiom),
   438	        )
   439	    return out
   440	
   441	
   442	# Proposition A and interdependence --------------------------------------------------------
   443	
   444	
   445	@dataclass(frozen=True)
   446	class PropositionAResult:
   447	    """Outcome of checking Proposition A on one coded system (Part VII Cor 5.5, Thm 5.10).
   448	
   449	    ``struct``: all six pillars realized (Thm 4.3) AND every D0 relation generated (Cor 5.5,
   450	    from Ax1..Ax6). ``interdependent``: all six realized and the generated hypergraph strongly
   451	    connected (underlying digraph) AND cascade-complete (Thm 5.10, from Ax1..Ax6 plus
   452	    Assumptions 5.6 to 5.9, i.e. X1, X2, X3, X5; the role of each premise is Prop 5.11).
   453	    ``holds`` is Proposition A in full: struct AND interdependent.
   454	
   455	    ``counterexample``: persistent, the extended axiom set holds, yet ``holds`` is False.
   456	    ``struct_counterexample``: persistent, Ax1..Ax6 hold, yet ``struct`` is False.
   457	    """
   458	
   459	    system: str
   460	    antecedent: bool
   461	    realized: frozenset[Pillar]
   462	    missing: frozenset[Pillar]
   463	    dependencies: frozenset[ArcKey]
   464	    missing_dependencies: frozenset[ArcKey]
   465	    strongly_connected: bool
   466	    cascade_complete: bool
   467	    struct: bool
   468	    interdependence_antecedent: bool
   469	    derivations: Mapping[Axiom, Derivation] = field(repr=False, default_factory=dict)
   470	
   471	    @property
   472	    def interdependent(self) -> bool:
   473	        return not self.missing and self.strongly_connected and self.cascade_complete
   474	
   475	    @property
   476	    def holds(self) -> bool:
   477	        return self.struct and self.interdependent
   478	
   479	    @property
   480	    def struct_counterexample(self) -> bool:
   481	        return self.antecedent and not self.struct
   482	
   483	    @property
   484	    def counterexample(self) -> bool:
   485	        return self.interdependence_antecedent and not self.holds
   486	
   487	
   488	def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
   489	    """Check Proposition A (struct and interdependence) on ``system`` (Part VII; KB 4.3).
   490	
   491	    A D0 relation is demanded when its head and every tail member are realized.
   492	    """
   493	    realized = frozenset(m for m in PILLARS if realized_form(system, m) is not None)
   494	    deps = generate_dependencies(system)
   495	    needed = frozenset((t, h) for t, h in D0_KEYS if h in realized and t <= realized)
   496	    missing_deps = needed - deps
   497	    return PropositionAResult(
   498	        system=system.name,
   499	        antecedent=system.persistent and system.all_axioms_hold,
   500	        realized=realized,
   501	        missing=frozenset(PILLARS) - realized,
   502	        dependencies=deps,
   503	        missing_dependencies=missing_deps,
   504	        strongly_connected=is_strongly_connected(underlying_digraph(deps), realized),
   505	        cascade_complete=is_cascade_complete(deps, realized),
   506	        struct=realized == frozenset(PILLARS) and not missing_deps,
   507	        interdependence_antecedent=system.persistent and system.extended_axioms_hold,
   508	        derivations=derive_functions(system),
   509	    )
   510	
   511	
   512	def formal_system(
   513	    name: str,
   514	    holders: Mapping[Pillar, Iterable[str]],
   515	    persistent: bool = True,
   516	    source: str = "",
   517	    axioms: Iterable[AnyAxiom] = EXTENDED_AXIOMS,
   518	) -> GovernanceSystem:
   519	    """A persistent system whose pillars are held by formal organizations.
   520	
   521	    An actor listed under several pillars is fused. By default the extended axiom set is
   522	    coded as holding: an assumption of the stylized model, not an observation. Used for regime
   523	    profiles and counter-models.
   524	    """
   525	    practices = tuple(
   526	        Practice(f"{m.label} function held by formal organizations", PILLAR_TO_AXIOM[m],
   527	                 frozenset(hs), formal=True, source=source)
   528	        for m, hs in holders.items()
   529	        if hs
   530	    )
   531	    return GovernanceSystem(name, persistent, frozenset(axioms), practices)
   532	
   533	
   534	# Hard-case fixtures (KB Section 5). Codings are minimal forms, not offices. ---------------
   535	# Each codes the extended axiom set as holding. The X1, X2, X3, X5 codings are QUALITATIVE
   536	# readings of the ethnography (sources in X_CODING_SOURCES), each open to the falsifier
   537	# stated on IncidenceAxiom.
   538	
   539	
   540	def _informal(desc: str, axiom: Axiom, holders: Iterable[str], source: str) -> Practice:
   541	    return Practice(desc, axiom, frozenset(holders), formal=False, source=source)
   542	
   543	
   544	NUER = GovernanceSystem(
   545	    name="Nuer ('ordered anarchy')",
   546	    persistent=True,
   547	    axioms=EXTENDED_AXIOMS,
   548	    practices=(
   549	        _informal("cattle rights via kinship and bridewealth; sharing of meat and milk",
   550	                  Axiom.Ax1, {"lineages", "households"}, "evanspritchard1940"),
   551	        _informal("lineage moots; precedent of settled feuds", Axiom.Ax2,
   552	                  {"lineage elders"}, "evanspritchard1940; fortes1940"),
   553	        _informal("leopard-skin chief mediates blood-feud compensation", Axiom.Ax3,
   554	                  {"leopard-skin chief", "lineage elders"}, "evanspritchard1940"),
   555	        _informal("segmentary lineage ideology; Kwoth cosmology; prophets", Axiom.Ax4,
   556	                  {"prophets", "lineages"}, "evanspritchard1940"),
   557	        _informal("feud and threat of retaliation by agnates", Axiom.Ax5,
   558	                  {"agnatic kin"}, "evanspritchard1940"),
   559	        _informal("pastoralism, horticulture, fishing", Axiom.Ax6, {"households"},
   560	                  "evanspritchard1940"),
   561	    ),
   562	    note="no office holds coercive authority; functions exist without separation",
   563	)
   564	
   565	JU_HOANSI = GovernanceSystem(
   566	    name="Ju/'hoansi (!Kung)",
   567	    persistent=True,
   568	    axioms=EXTENDED_AXIOMS,
   569	    practices=(
   570	        _informal("arrow-owner meat distribution; hxaro exchange; demand sharing", Axiom.Ax1,
   571	                  {"hunters", "camp members"}, "lee2013; marshall1976"),
   572	        _informal("camp-level talk; fission when disagreement persists", Axiom.Ax2,
   573	                  {"camp members"}, "lee2013"),
   574	        _informal("disputes talked out with kin mediators", Axiom.Ax3,
   575	                  {"kin mediators"}, "lee1979; wiessner2005"),
   576	        _informal("n/um healing dance; egalitarian ethos; myth", Axiom.Ax4,
   577	                  {"healers", "camp members"}, "marshall1976"),
   578	        _informal("gossip, teasing, 'insulting the meat', avoidance", Axiom.Ax5,
   579	                  {"camp members"}, "wiessner2005; lee2013"),
   580	        _informal("foraging by both sexes", Axiom.Ax6, {"households"}, "lee1979"),
   581	    ),
   582	    note="most cited 'no hierarchy' case; leveling sanctions sustain the ethos (woodburn1982)",
   583	)
   584	
   585	OSTROM_COMMONS = GovernanceSystem(
   586	    name="Ostrom commons (design principles)",
   587	    persistent=True,
   588	    axioms=EXTENDED_AXIOMS,
   589	    practices=(
   590	        _informal("boundary rules; appropriation proportional to provision (DP1, DP2)",
   591	                  Axiom.Ax1, {"appropriators"}, "ostrom1990"),
   592	        _informal("collective-choice arrangements: users modify the rules (DP3)", Axiom.Ax2,
   593	                  {"appropriators"}, "ostrom1990"),
   594	        _informal("low-cost local conflict-resolution arenas (DP6)", Axiom.Ax3,
   595	                  {"appropriators"}, "ostrom1990; cox2010"),
   596	        _informal("shared norms; minimal recognition of rights to organize (DP7)",
   597	                  Axiom.Ax4, {"appropriators"}, "ostromdesign2010"),
   598	        _informal("monitoring and graduated sanctions by appropriators (DP4, DP5)",
   599	                  Axiom.Ax5, {"appropriators"}, "ostrom1990; cox2010"),
   600	        _informal("appropriation and maintenance labor", Axiom.Ax6, {"appropriators"},
   601	                  "ostrom1990"),
   602	    ),
   603	    note="checks in minimal form; monitors are appropriators or accountable to them",
   604	)
   605	
   606	CONSENSUS_VILLAGE = GovernanceSystem(
   607	    name="Consensus village (stylized)",
   608	    persistent=True,
   609	    axioms=EXTENDED_AXIOMS,
   610	    practices=(
   611	        _informal("household plots; reciprocal labor exchange; sharing norms", Axiom.Ax1,
   612	                  {"households"}, "sahlins1972"),
   613	        _informal("consensus meeting of adults", Axiom.Ax2, {"village meeting"},
   614	                  "clastres1987; boehm1999"),
   615	        _informal("elders mediate disputes", Axiom.Ax3, {"elders"}, "boehm1999"),
   616	        _informal("ritual and myth; moral talk", Axiom.Ax4, {"village meeting", "elders"},
   617	                  "boehm1999"),
   618	        _informal("gossip, shunning, ostracism of would-be dominants", Axiom.Ax5,
   619	                  {"village meeting"}, "boehm1999; woodburn1982"),
   620	        _informal("gardening and household labor", Axiom.Ax6, {"households"},
   621	                  "sahlins1972"),
   622	    ),
   623	    note="stylized composite; reverse dominance hierarchy",
   624	)
   625	
   626	HARD_CASES: tuple[GovernanceSystem, ...] = (NUER, JU_HOANSI, OSTROM_COMMONS, CONSENSUS_VILLAGE)
   627	
   628	_X1, _X2, _X3, _X5 = IncidenceAxiom
   629	#: Qualitative codings of the incidence axioms for the hard cases (Part VII), with sources.
   630	X_CODING_SOURCES: dict[str, dict[IncidenceAxiom, str]] = {
   631	    NUER.name: {
   632	        _X1: "cattle and grazing rights (evanspritchard1940)",
   633	        _X2: "norms adjusted by negotiation among lineages (evanspritchard1940)",
   634	        _X3: "cattle compensation fixed through the leopard-skin chief (evanspritchard1940)",
   635	        _X5: "feud over cattle (evanspritchard1940)",
   636	    },
   637	    JU_HOANSI.name: {
   638	        _X1: "kin-based n!ore rights to territory and water (lee2013)",
   639	        _X2: "camp talk and fission (lee2013)",
   640	        _X3: "disputes over sharing talked out (lee2013; wiessner2005)",
   641	        _X5: "criticism of failures to share (wiessner2005)",
   642	    },
   643	    OSTROM_COMMONS.name: {
   644	        _X1: "boundary and appropriation rules (ostrom1990)",
   645	        _X2: "users modify their rules (ostrom1990)",
   646	        _X3: "conflict-resolution arenas (ostrom1990; cox2010)",
   647	        _X5: "monitoring and graduated sanctions (ostrom1990)",
   648	    },
   649	    CONSENSUS_VILLAGE.name: {
   650	        _X1: "household plots under sharing norms (sahlins1972)",
   651	        _X2: "seasonal re-arrangement (graeber2021)",
   652	        _X3: "elders mediate residual disputes (boehm1999)",
   653	        _X5: "sharing enforced against hoarders (boehm1999)",
   654	    },
   655	}
   656	
   657	
   658	# Axiom independence fixtures (Part VII spec, item 7). ---------------------------------------
   659	
   660	#: Consistency model: the extended axiom set holds and all six pillars are realized (the
   661	#: consensus village coding).
   662	BASELINE_MODEL: GovernanceSystem = CONSENSUS_VILLAGE
   663	
   664	
   665	def without_axiom(axiom: AnyAxiom, base: GovernanceSystem = BASELINE_MODEL) -> GovernanceSystem:
   666	    """``base`` with one axiom removed; for Ax_k the practices solving Ax_k are removed too."""
   667	    practices = base.practices
   668	    if isinstance(axiom, Axiom):
   669	        practices = tuple(p for p in practices if p.solves is not axiom)
   670	    return GovernanceSystem(
   671	        name=f"{base.name} without {axiom.name} ({axiom.label})",
   672	        persistent=base.persistent,
   673	        axioms=base.axioms - {axiom},
   674	        practices=practices,
   675	        absent_incidences=base.absent_incidences,
   676	        note="hypothetical: one axiom removed",
   677	    )
   678	
   679	
   680	#: Part VII R1, the k = 4 independence model: innate rules, no initiation, a fine d >= g on
   681	#: defiance of a determination (so rulings bind through C alone), ell = 0, Pr(Pi) = 1;
   682	#: Impl_I fails.
   683	R1_AX4_MODEL = GovernanceSystem(
   684	    name="R1: independence model for Ax4",
   685	    persistent=True,
   686	    axioms=BASELINE_MODEL.axioms - {Axiom.Ax4},
   687	    practices=tuple(p for p in BASELINE_MODEL.practices if p.solves is not Axiom.Ax4) + (
   688	        Practice("fine d >= g on defiance of a determination", Axiom.Ax5,
   689	                 frozenset({"village meeting"}), source="Part VII R1"),
   690	    ),
   691	    note="innate rules, no initiation, ell = 0, Pr(Pi) = 1; Impl_I fails",
   692	)
   693	
   694	#: For each k: persistent, Ax_k removed, pillar k missing (k = 4 is the R1 model). Theorem A's
   695	#: antecedent is false, so none is a counterexample; each shows pillar k is not forced by the
   696	#: other five axioms.
   697	AXIOM_INDEPENDENCE: dict[Axiom, GovernanceSystem] = {
   698	    a: (R1_AX4_MODEL if a is Axiom.Ax4 else without_axiom(a)) for a in Axiom
   699	}
   700	
   701	
   702	# Part VII Prop 4.4(a) model and its Lemma 5.4 variant (Ax1..Ax6, no incidence axioms). ------
   703	

exec
/usr/local/bin/zsh -lc "nl -ba model/tests/test_necessity.py | sed -n '1,460p'" in /Users/mlong/Documents/Development/the-beast-system
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
   271	    # Part VII Prop 5.11(a): Ax1..Ax6 without the incidence axioms.
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
   337	
   338	
   339	def test_prop_4_4a_model_and_variant():
   340	    from beast_system.necessity import PROP_4_4A_MODEL, PROP_4_4A_VARIANT
   341	
   342	    for system in (PROP_4_4A_MODEL, PROP_4_4A_VARIANT):
   343	        r = check_proposition_a(system)
   344	        assert r.struct and not r.interdependent and not r.holds
   345	        assert not r.struct_counterexample and not r.counterexample
   346	        graph = underlying_digraph(r.dependencies)
   347	        assert not any(W in targets for targets in graph.values())  # Prop 5.11(a)
   348	        assert arc_key({I, C}, J) in r.dependencies
   349	        assert arc_key(I, J) not in r.dependencies and arc_key(C, J) not in r.dependencies
   350	
   351	
   352	def test_r1_independence_model_for_ax4():
   353	    from beast_system.necessity import R1_AX4_MODEL
   354	
   355	    assert AXIOM_INDEPENDENCE[Axiom.Ax4] is R1_AX4_MODEL
   356	    r = check_proposition_a(R1_AX4_MODEL)
   357	    assert r.missing == {I} and not r.antecedent and not r.counterexample
   358	    assert any("defiance of a determination" in p.description for p in R1_AX4_MODEL.practices
   359	               if p.solves is Axiom.Ax5)
   360	    assert "ell = 0" in R1_AX4_MODEL.note and "Impl_I fails" in R1_AX4_MODEL.note
   361	
   362	
   363	def test_starred_axiom_clauses():
   364	    assert "finite time" in Axiom.Ax3.statement and "ell + sigma >= g" in Axiom.Ax3.statement
   365	    assert "common-knowledge rule system" in Axiom.Ax4.statement
   366	    assert "infinitely many periods" in Axiom.Ax4.statement
   367	    assert "best-respond" in Axiom.Ax5.statement
   368	    assert "consumption is counted" in Axiom.Ax6.statement
   369	
   370	
   371	def test_admissibility():
   372	    from beast_system.necessity import is_admissible, role_map
   373	
   374	    from beast_system.capture import corner_polities
   375	
   376	    for system in HARD_CASES:
   377	        assert is_admissible(system, role_map(system)), system.name
   378	    for polity in corner_polities().values():  # corner polities, all holders as members
   379	        assert is_admissible(polity.system, role_map(polity.system)), polity.name
   380	    holders = set(role_map(JU_HOANSI))
   381	    assert not is_admissible(JU_HOANSI, holders - {"kin mediators"})  # outsider holder
   382	    assert is_admissible(JU_HOANSI, holders - {"camp members"} | {"m1", "m2"},
   383	                         organizations={"camp members": {"m1", "m2"}})
   384	    assert not is_admissible(JU_HOANSI, holders - {"camp members"},
   385	                             organizations={"camp members": set()})
   386	    mediation = next(p for p in JU_HOANSI.practices if p.solves is Axiom.Ax3)
   387	    assert not is_admissible(JU_HOANSI, holders,
   388	                             dispute_parties={mediation.description: {"kin mediators"}})

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/tests/test_necessity.py | sed -n '95,340p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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
   271	    # Part VII Prop 5.11(a): Ax1..Ax6 without the incidence axioms.
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
   337	
   338	
   339	def test_prop_4_4a_model_and_variant():
   340	    from beast_system.necessity import PROP_4_4A_MODEL, PROP_4_4A_VARIANT

exec
/usr/local/bin/zsh -lc "nl -ba model/tests/test_representation.py | sed -n '180,330p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'rg -n "(Cor|Assumptions?|Thm|Theorem|Prop|Remark) [0-9]" model/beast_system/representation.py model/beast_system/uniqueness.py model/beast_system/necessity.py model/beast_system/pillars.py model/tests/test_representation.py model/tests/test_uniqueness.py model/tests/test_necessity.py' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
model/beast_system/representation.py:1:"""Representation theorem and minimality (Part VII Thm 7.4, Prop 7.5).
model/beast_system/representation.py:78:    well-formed record; Thm 7.4 assumes it).
model/tests/test_necessity.py:271:    # Part VII Prop 5.11(a): Ax1..Ax6 without the incidence axioms.
model/tests/test_necessity.py:302:        arc_key({F, I}, C): "Part V Cor 3.7 conditions",
model/tests/test_necessity.py:347:        assert not any(W in targets for targets in graph.values())  # Prop 5.11(a)
model/beast_system/pillars.py:125:    """Incidence axioms X_k (Part VII Assumptions 5.6 to 5.9: X1, X2, X3, X5).
model/beast_system/uniqueness.py:3:Part VII Def 7.6 (Abs_P), Thm 7.7 (uniqueness), Thm 7.8 (six dimensions, stated for
model/beast_system/uniqueness.py:5:Prop 10.1 (witnesses), Thm 10.2 (novelty).
model/beast_system/uniqueness.py:334:    """Witness system (Part VII Prop 7.5, Prop 10.1): actors a and b perform exactly the
model/beast_system/uniqueness.py:369:    (Part VII Prop 7.5).
model/beast_system/uniqueness.py:373:    Raises if c is a total injection (then Phi_c is P-preserving, Thm 7.8).
model/beast_system/uniqueness.py:481:    differing (Part VII Prop 10.1). Merge witnesses use mu = 1/2 (equal lam; Easton's
model/tests/test_uniqueness.py:290:    # Thm 7.8 (coarsenings): Phi_c is P-preserving iff c is a bijection onto |K| = 6.
model/beast_system/necessity.py:19:Part III Prop 3.6 ({I, C} -> J), Ax4 with Part I Def 2.2(b) (I -> F), and the incidence axioms
model/beast_system/necessity.py:224:    DependencyRule(frozenset({_P.I, _P.C}), _P.J, "Part III Prop 3.6",
model/beast_system/necessity.py:230:         "only through legitimation (Part IV Lem 3.4, Thm 3.5)"),
model/beast_system/necessity.py:233:    _inc(_A.Ax3, _P.F, "X3", (_X.X3,), "open-textured allocation rules (Part III Thm 3.3)"),
model/beast_system/necessity.py:234:    _inc(_A.Ax5, _P.F, "X5", (_X.X5,), "tempting allocation rules (Part V Thm 3.4)"),
model/beast_system/necessity.py:237:#: Further rules (Part VII Remark 5.12): reported, not needed for interdependence. Each rests on a premise beyond
model/beast_system/necessity.py:248:    DependencyRule(frozenset({_P.F, _P.I}), _P.C, "Part V Cor 3.7 conditions",
model/beast_system/necessity.py:256:#: {I, C} -> J, and I -> F); Part VII Thm 4.3.
model/beast_system/necessity.py:447:    """Outcome of checking Proposition A on one coded system (Part VII Cor 5.5, Thm 5.10).
model/beast_system/necessity.py:449:    ``struct``: all six pillars realized (Thm 4.3) AND every D0 relation generated (Cor 5.5,
model/beast_system/necessity.py:451:    connected (underlying digraph) AND cascade-complete (Thm 5.10, from Ax1..Ax6 plus
model/beast_system/necessity.py:452:    Assumptions 5.6 to 5.9, i.e. X1, X2, X3, X5; the role of each premise is Prop 5.11).
model/beast_system/necessity.py:702:# Part VII Prop 4.4(a) model and its Lemma 5.4 variant (Ax1..Ax6, no incidence axioms). ------
model/beast_system/necessity.py:706:    name="Prop 4.4(a) model",
model/beast_system/necessity.py:711:                 "assigned by lot", Axiom.Ax1, _M, source="Part VII Prop 4.4(a)"),
model/beast_system/necessity.py:713:                 "L periods", Axiom.Ax2, _M, source="Part VII Prop 4.4(a)"),
model/beast_system/necessity.py:715:                 source="Part VII Prop 4.4(a)"),
model/beast_system/necessity.py:718:                 source="Part VII Prop 4.4(a)"),
model/beast_system/necessity.py:720:                 source="Part VII Prop 4.4(a)"),
model/beast_system/necessity.py:722:                 source="Part VII Prop 4.4(a)"),
model/beast_system/necessity.py:724:    note="struct holds, interdependence fails: no arc into W (Prop 5.11(a))",
model/beast_system/necessity.py:730:    name="Prop 4.4(a) model, Lemma 5.4 variant",

hook: PreToolUse
hook: PreToolUse Completed
codex
The scoped test command is currently blocked by a stale `pytest` launcher pointing to removed Python 3.7, plus the read-only environment preventing pyenv’s temp-file hook. I’m switching to a direct interpreter invocation and will separately reproduce any invariant counterexample in memory only.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc 'command -v -a python3 python && /usr/bin/python3 --version && /opt/homebrew/bin/python3 --version 2>/dev/null || true' in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 0ms:
zsh:1: command not found: -v

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -c 'type -a python3 python; /usr/bin/python3 --version; /opt/homebrew/bin/python3 --version 2>/dev/null || true' in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 1533ms:
2026-10-22 13:41:13.135 xcodebuild[98303:4334138]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:41:13.227 xcodebuild[98303:4334131] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-fCIVNgVm' (errno=Operation not permitted)
2026-10-22 13:41:13.658 xcodebuild[98305:4334164]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:41:13.752 xcodebuild[98305:4334163] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
Python 3.9.6
Python 3.15.0

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -c '/opt/homebrew/bin/python3 -m pytest --version' in /Users/mlong/Documents/Development/the-beast-system/model
 exited 1 in 0ms:
/opt/homebrew/opt/python@3.15/bin/python3.15: No module named pytest

exec
/usr/local/bin/zsh -c '/usr/bin/python3 -m pytest --version' in /Users/mlong/Documents/Development/the-beast-system/model
 exited 1 in 1452ms:
2026-10-22 13:41:17.605 xcodebuild[98327:4334265]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:41:17.693 xcodebuild[98327:4334264] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-SCaqytfN' (errno=Operation not permitted)
2026-10-22 13:41:18.083 xcodebuild[98331:4334280]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:41:18.170 xcodebuild[98331:4334278] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
/Applications/Xcode.app/Contents/Developer/usr/bin/python3: No module named pytest

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -c "/usr/bin/python3 -c 'import numpy; print(numpy.__version__)'" in /Users/mlong/Documents/Development/the-beast-system/model
exec
/usr/local/bin/zsh -c "/opt/homebrew/bin/python3 -c 'import numpy; print(numpy.__version__)'" in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 198ms:
2.5.4

 succeeded in 1492ms:
2026-10-22 13:41:23.704 xcodebuild[98352:4334466]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:41:23.796 xcodebuild[98352:4334464] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
python3: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
python3: error: couldn't create cache file '/tmp/xcrun_db-tzvyjWpa' (errno=Operation not permitted)
2026-10-22 13:41:24.181 xcodebuild[98354:4334476]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:41:24.267 xcodebuild[98354:4334475] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
2.0.2

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -c "PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3 -c 'from beast_system.representation import M_LABELS, FormalizedStructure, make_structure, well_formed; from beast_system.uniqueness import canonical_form,p_equal; F=make_structure({p:{\"a\":.5,\"b\":.5} for p in M_LABELS},{p:.3 for p in M_LABELS},kappa={frozenset({\"a\"}):{\"F\":.9},frozenset({\"b\"}):{\"F\":.1}}); G=FormalizedStructure(**{**F.__dict__,\"kappa\":{S:{**r,\"P\":0.0} for S,r in F.kappa.items()}}); print(well_formed(F),well_formed(G),p_equal(F,G),canonical_form(F)==canonical_form(G))'" in /Users/mlong/Documents/Development/the-beast-system/model
 succeeded in 176ms:
True True False True

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -c "PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3 -c 'import time,numpy as np; from beast_system.representation import M_LABELS,FormalizedStructure,make_structure; from beast_system.uniqueness import canonical_form,p_equal; n=9; B=make_structure({p:{f\"v{k}\":1/n for k in range(n)} for p in M_LABELS},{p:.5 for p in M_LABELS}); layers={};
for p in M_LABELS:
 a=np.zeros((n,n));
 for k in range(n): a[k,(k+1)%n]=.4
 layers[p]=a
F=FormalizedStructure(**{**B.__dict__,\"layers\":layers}); t=time.time(); cf=canonical_form(F); print(\"cycle9\",round(time.time()-t,3),len(cf),p_equal(F,F))'" in /Users/mlong/Documents/Development/the-beast-system/model
2026-10-22T18:42:23.644692Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 208ms:
cycle9 0.011 9 True

codex
- P1 — `canonical_form` is still not a complete invariant of `p_equal`. [_encode](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/uniqueness.py:197) encodes missing `kappa` columns as zero, while [find_bijection](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py:434) requires exact row-key equality. Confirmed: two well-formed structures differing only by missing `"P"` versus explicit `"P": 0.0` produce `p_equal == False` but identical canonical forms. The numeric-normalization fix and total search are resolved, but this leaves the complete-invariant claim false.

- P2 — [witness_coarsening](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/uniqueness.py:379) rejects the all-pillars-dropped map, although `coarsen` accepts that non-bijective coarsening and the function claims coverage of every non-total injection. Either empty-image coarsenings must be rejected consistently or this case needs a collapse witness.

VERDICT: NEEDS_FIX
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
82,109
- P1 — `canonical_form` is still not a complete invariant of `p_equal`. [_encode](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/uniqueness.py:197) encodes missing `kappa` columns as zero, while [find_bijection](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/representation.py:434) requires exact row-key equality. Confirmed: two well-formed structures differing only by missing `"P"` versus explicit `"P": 0.0` produce `p_equal == False` but identical canonical forms. The numeric-normalization fix and total search are resolved, but this leaves the complete-invariant claim false.

- P2 — [witness_coarsening](/Users/mlong/Documents/Development/the-beast-system/model/beast_system/uniqueness.py:379) rejects the all-pillars-dropped map, although `coarsen` accepts that non-bijective coarsening and the function claims coverage of every non-total injection. Either empty-image coarsenings must be rejected consistently or this case needs a collapse witness.

VERDICT: NEEDS_FIX
exit 0

---

## Resolution (model/, written after Codex round 10)

Final state: `cd model && python3 -m pytest -q` gives **335 passed**, also clean with `-W error`.

### Round 10 items (fixed after the last allowed round, so not reviewed by Codex)

| Item | Fix | Test |
|---|---|---|
| P1: `canonical_form` encoded a missing kappa column as 0, so a missing column and an explicit zero got the same canonical form although `p_equal` told them apart | Every kappa entry is now encoded with an explicit presence flag via `_kv(row, m)`: `(0, 0.0)` if missing, `(1, value)` if present. The flag is used in `uniqueness._encode`, `_refine`, `_global` and `representation._actor_signature` | `tests/test_uniqueness.py::test_missing_kappa_column_differs_from_explicit_zero` |
| P2: `witness_coarsening` rejected the all-dropped map (K = empty) | For K = empty it now returns a witness in which a and b hold only m and c holds the rest. Both images reduce to the shared actor set {a, b, c} (Part VII Prop 7.5(a)) | `tests/test_uniqueness.py::test_all_dropped_coarsening_has_a_witness` |

### Review history

| Round | Scope | Verdict | Items, all fixed |
|---|---|---|---|
| 1 | full model | NEEDS_FIX | 7 (A.holds tied to SC; per-system dependencies; weight sensitivity; capture-link actors and bool flags; counter-model thresholds; bounds rounding; numeric validation) |
| 2 | full model | NEEDS_FIX | 2 (`deviation_persists` overclaim; `control_shares` overflow) |
| 3 | full model with hypergraph spec | NEEDS_FIX | 4 (general coalition overlap; symmetrization; integer k in `hub_bound`; asymmetric foothold test) |
| 4 | full model with generated arcs | NEEDS_FIX | 1 (overflow in the foothold bound) |
| 5 | scoped to round 4 | PASS | none |
| 6 | scoped to the Part VII arc map | NEEDS_FIX | 2 (further rules could be generated; missing assertions) |
| 7 | round 6 + representation | NEEDS_FIX | 4 (record domain; class domain; equivalence strictness; falsifier tests) |
| 8 | round 7 + uniqueness | NEEDS_FIX | 4 (totality on empty V; P-preserving alphas; coalition member validation; arc domain) |
| 9 | round 8 fixes | NEEDS_FIX | 2 (one normalization for `p_equal` and `canonical_form`; total canonical form) |
| 10 | round 9 fixes + Part VII alignment | NEEDS_FIX | 2, listed above (fixed but unreviewed) |
