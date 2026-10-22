---
reviewer: codex gpt-5.6-sol
target: website
round: 2
date: 2026-10-22T18:22:45Z
---
Reading additional input from stdin...
2026-10-22T18:22:45.895379Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a164d9-ef18-7491-89bf-834f5475c34e
--------
user
Round 2, confirmation review of the Next.js research website. Review only website/app, website/lib, website/components, website/scripts and website/out. Round 1 found these 9 issues; confirm each is resolved, citing evidence from out/: (P1) raw LaTeX inside MathML because DOMPurify stripped semantics/annotation; (P2) six broken equation anchors eq:margin eq:necessity eq:U eq:aggregation-gap eq:integration eq:overlap; (P2) out/og/ empty while og:image URLs point there; (P2) missing global box-sizing border-box causing mobile overflow; (P2) touch targets under 44px; (P2) 50 empty focusable DOI links on the judicial page; (P2) page weight (now reported as at most 235 KB gzip); (P3) unoptimized homepage covers; (P3) fonts under 14px. Also check that rendering math after sanitizing introduces no injection risk (the content is the authors' own static papers built at compile time) and report any NEW issue introduced by the fixes. Output the findings and the VERDICT line only, ending with exactly one of: VERDICT: PASS or VERDICT: NEEDS_FIX
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T18:22:47.380710Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T18:22:47.797619Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
I’m using the code-review skill for this confirmation pass. I’ll verify each of the nine Round 1 findings against generated `website/out` artifacts, then separately assess the post-sanitization math path and look for regressions only within the requested directories.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "sed -n '1,240p' /Users/mlong/.codex/plugins/cache/claude-cowork/engineering/1.1.0/skills/code-review/SKILL.md && rg -n \"the-beast-system|GrokRxiv|research website\" /Users/mlong/.codex/memories/MEMORY.md" in /Users/mlong/Documents/Development/the-beast-system
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

codex
The review contract is loaded. I’m now tracing each fix from its implementation into the exported HTML/CSS/images, with `out/` treated as the acceptance artifact rather than assuming source changes made it into the build.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "git status --short -- website/app website/lib website/components website/scripts website/out; rg --files website/app website/lib website/components website/scripts website/out | sort; find website/out -type f -maxdepth 4 -print0 | xargs -0 stat -f '%z %N' | sort -nr | sed -n '1,120p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 1990ms:
2026-10-22 13:23:09.427 xcodebuild[89021:4282122]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:23:09.619 xcodebuild[89021:4282121] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-BJNmJGrH' (errno=Operation not permitted)
2026-10-22 13:23:10.075 xcodebuild[89023:4282182]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 13:23:10.163 xcodebuild[89023:4282180] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
?? website/app/
?? website/components/
?? website/lib/
?? website/scripts/
website/app/favicon.ico
website/app/globals.css
website/app/layout.tsx
website/app/page.tsx
website/app/papers/[slug]/PaperBody.tsx
website/app/papers/[slug]/page.tsx
website/components/PaperCard.tsx
website/components/PillarDiagram.tsx
website/components/TableOfContents.tsx
website/lib/macros.json
website/lib/papers.ts
website/lib/render-math.ts
website/out/404.html
website/out/404/index.html
website/out/_next/static/chunks/117-373243894bd7fac6.js
website/out/_next/static/chunks/878-34b15e7090e18027.js
website/out/_next/static/chunks/972-17ea62b17795b286.js
website/out/_next/static/chunks/app/_not-found/page-4b9eb8aab41bf6df.js
website/out/_next/static/chunks/app/layout-1388b0197a1cd438.js
website/out/_next/static/chunks/app/page-395b63c66d3f1e55.js
website/out/_next/static/chunks/app/papers/[slug]/page-1bad85e0c5c26278.js
website/out/_next/static/chunks/fd9d1056-9f91b5e418130764.js
website/out/_next/static/chunks/framework-f66176bb897dc684.js
website/out/_next/static/chunks/main-app-0c0f56fdb996b834.js
website/out/_next/static/chunks/main-ed80ab20b1eaf357.js
website/out/_next/static/chunks/pages/_app-72b849fbd24ac258.js
website/out/_next/static/chunks/pages/_error-7ba65e1336b92748.js
website/out/_next/static/chunks/polyfills-42372ed130431b0a.js
website/out/_next/static/chunks/webpack-648529da2731d8e9.js
website/out/_next/static/css/459226f83420bab5.css
website/out/_next/static/css/f4ff6fba389ef1b6.css
website/out/_next/static/media/024ead497118aa23-s.woff2
website/out/_next/static/media/19cfc7226ec3afaa-s.woff2
website/out/_next/static/media/21350d82a1f187e9-s.woff2
website/out/_next/static/media/393d45a2251e223a-s.woff2
website/out/_next/static/media/48410f3df60da620-s.woff2
website/out/_next/static/media/7b89a4fd5e90ede0-s.p.woff2
website/out/_next/static/media/8715d2ed531152f4-s.woff2
website/out/_next/static/media/8e9860b6e62d6359-s.woff2
website/out/_next/static/media/KaTeX_AMS-Regular.1608a09b.woff
website/out/_next/static/media/KaTeX_AMS-Regular.4aafdb68.ttf
website/out/_next/static/media/KaTeX_AMS-Regular.a79f1c31.woff2
website/out/_next/static/media/KaTeX_Caligraphic-Bold.b6770918.woff
website/out/_next/static/media/KaTeX_Caligraphic-Bold.cce5b8ec.ttf
website/out/_next/static/media/KaTeX_Caligraphic-Bold.ec17d132.woff2
website/out/_next/static/media/KaTeX_Caligraphic-Regular.07ef19e7.ttf
website/out/_next/static/media/KaTeX_Caligraphic-Regular.55fac258.woff2
website/out/_next/static/media/KaTeX_Caligraphic-Regular.dad44a7f.woff
website/out/_next/static/media/KaTeX_Fraktur-Bold.9f256b85.woff
website/out/_next/static/media/KaTeX_Fraktur-Bold.b18f59e1.ttf
website/out/_next/static/media/KaTeX_Fraktur-Bold.d42a5579.woff2
website/out/_next/static/media/KaTeX_Fraktur-Regular.7c187121.woff
website/out/_next/static/media/KaTeX_Fraktur-Regular.d3c882a6.woff2
website/out/_next/static/media/KaTeX_Fraktur-Regular.ed38e79f.ttf
website/out/_next/static/media/KaTeX_Main-Bold.b74a1a8b.ttf
website/out/_next/static/media/KaTeX_Main-Bold.c3fb5ac2.woff2
website/out/_next/static/media/KaTeX_Main-Bold.d181c465.woff
website/out/_next/static/media/KaTeX_Main-BoldItalic.6f2bb1df.woff2
website/out/_next/static/media/KaTeX_Main-BoldItalic.70d8b0a5.ttf
website/out/_next/static/media/KaTeX_Main-BoldItalic.e3f82f9d.woff
website/out/_next/static/media/KaTeX_Main-Italic.47373d1e.ttf
website/out/_next/static/media/KaTeX_Main-Italic.8916142b.woff2
website/out/_next/static/media/KaTeX_Main-Italic.9024d815.woff
website/out/_next/static/media/KaTeX_Main-Regular.0462f03b.woff2
website/out/_next/static/media/KaTeX_Main-Regular.7f51fe03.woff
website/out/_next/static/media/KaTeX_Main-Regular.b7f8fe9b.ttf
website/out/_next/static/media/KaTeX_Math-BoldItalic.572d331f.woff2
website/out/_next/static/media/KaTeX_Math-BoldItalic.a879cf83.ttf
website/out/_next/static/media/KaTeX_Math-BoldItalic.f1035d8d.woff
website/out/_next/static/media/KaTeX_Math-Italic.5295ba48.woff
website/out/_next/static/media/KaTeX_Math-Italic.939bc644.ttf
website/out/_next/static/media/KaTeX_Math-Italic.f28c23ac.woff2
website/out/_next/static/media/KaTeX_SansSerif-Bold.8c5b5494.woff2
website/out/_next/static/media/KaTeX_SansSerif-Bold.94e1e8dc.ttf
website/out/_next/static/media/KaTeX_SansSerif-Bold.bf59d231.woff
website/out/_next/static/media/KaTeX_SansSerif-Italic.3b1e59b3.woff2
website/out/_next/static/media/KaTeX_SansSerif-Italic.7c9bc82b.woff
website/out/_next/static/media/KaTeX_SansSerif-Italic.b4c20c84.ttf
website/out/_next/static/media/KaTeX_SansSerif-Regular.74048478.woff
website/out/_next/static/media/KaTeX_SansSerif-Regular.ba21ed5f.woff2
website/out/_next/static/media/KaTeX_SansSerif-Regular.d4d7ba48.ttf
website/out/_next/static/media/KaTeX_Script-Regular.03e9641d.woff2
website/out/_next/static/media/KaTeX_Script-Regular.07505710.woff
website/out/_next/static/media/KaTeX_Script-Regular.fe9cbbe1.ttf
website/out/_next/static/media/KaTeX_Size1-Regular.e1e279cb.woff
website/out/_next/static/media/KaTeX_Size1-Regular.eae34984.woff2
website/out/_next/static/media/KaTeX_Size1-Regular.fabc004a.ttf
website/out/_next/static/media/KaTeX_Size2-Regular.57727022.woff
website/out/_next/static/media/KaTeX_Size2-Regular.5916a24f.woff2
website/out/_next/static/media/KaTeX_Size2-Regular.d6b476ec.ttf
website/out/_next/static/media/KaTeX_Size3-Regular.9acaf01c.woff
website/out/_next/static/media/KaTeX_Size3-Regular.a144ef58.ttf
website/out/_next/static/media/KaTeX_Size3-Regular.b4230e7e.woff2
website/out/_next/static/media/KaTeX_Size4-Regular.10d95fd3.woff2
website/out/_next/static/media/KaTeX_Size4-Regular.7a996c9d.woff
website/out/_next/static/media/KaTeX_Size4-Regular.fbccdabe.ttf
website/out/_next/static/media/KaTeX_Typewriter-Regular.6258592b.woff
website/out/_next/static/media/KaTeX_Typewriter-Regular.a8709e36.woff2
website/out/_next/static/media/KaTeX_Typewriter-Regular.d97aaf4a.ttf
website/out/_next/static/media/ba9851c3c22cd980-s.woff2
website/out/_next/static/media/c48b38fe8bb532f3-s.woff2
website/out/_next/static/media/c5fe6dc8356a8c31-s.woff2
website/out/_next/static/media/df0a9ae256c0569c-s.woff2
website/out/_next/static/media/e18f83c737786aa7-s.p.woff2
website/out/_next/static/media/e4af272ccee01ff0-s.p.woff2
website/out/_next/static/media/e74f24ed7f0e4323-s.woff2
website/out/_next/static/media/ea896c3885e026c1-s.woff2
website/out/_next/static/media/fd3893c623c32b6d-s.woff2
website/out/_next/static/w1tSJbJe_oIt5IOzVSFA8/_buildManifest.js
website/out/_next/static/w1tSJbJe_oIt5IOzVSFA8/_ssgManifest.js
website/out/favicon.ico
website/out/figures/formalized-state-1.svg
website/out/figures/productive-power-1.svg
website/out/images/coercive-power-card.jpg
website/out/images/coercive-power.jpg
website/out/images/financial-power-card.jpg
website/out/images/financial-power.jpg
website/out/images/formalized-state-card.jpg
website/out/images/formalized-state.jpg
website/out/images/ideological-power-card.jpg
website/out/images/ideological-power.jpg
website/out/images/judicial-power-card.jpg
website/out/images/judicial-power.jpg
website/out/images/political-power-card.jpg
website/out/images/political-power.jpg
website/out/images/productive-power-card.jpg
website/out/images/productive-power.jpg
website/out/index.html
website/out/index.txt
website/out/og/coercive-power.png
website/out/og/financial-power.png
website/out/og/formalized-state.png
website/out/og/ideological-power.png
website/out/og/judicial-power.png
website/out/og/og-image.png
website/out/og/political-power.png
website/out/og/productive-power.png
website/out/papers/coercive-power/index.html
website/out/papers/coercive-power/index.txt
website/out/papers/financial-power/index.html
website/out/papers/financial-power/index.txt
website/out/papers/formalized-state/index.html
website/out/papers/formalized-state/index.txt
website/out/papers/ideological-power/index.html
website/out/papers/ideological-power/index.txt
website/out/papers/judicial-power/index.html
website/out/papers/judicial-power/index.txt
website/out/papers/political-power/index.html
website/out/papers/political-power/index.txt
website/out/papers/productive-power/index.html
website/out/papers/productive-power/index.txt
website/out/pdf/coercive-power.pdf
website/out/pdf/financial-power.pdf
website/out/pdf/formalized-state.pdf
website/out/pdf/ideological-power.pdf
website/out/pdf/judicial-power.pdf
website/out/pdf/political-power.pdf
website/out/pdf/productive-power.pdf
website/scripts/extract-macros.mjs
website/scripts/fix-html.mjs
website/scripts/prep-tex.mjs
website/scripts/series.mjs
3853385 website/out/papers/formalized-state/index.html
2130867 website/out/papers/productive-power/index.html
2071776 website/out/papers/ideological-power/index.html
1920144 website/out/papers/coercive-power/index.html
1821391 website/out/papers/political-power/index.html
1653837 website/out/papers/judicial-power/index.html
1519561 website/out/papers/formalized-state/index.txt
1489391 website/out/papers/financial-power/index.html
854150 website/out/papers/productive-power/index.txt
828346 website/out/papers/ideological-power/index.txt
775269 website/out/papers/coercive-power/index.txt
735741 website/out/papers/political-power/index.txt
667711 website/out/papers/judicial-power/index.txt
605954 website/out/pdf/formalized-state.pdf
602466 website/out/papers/financial-power/index.txt
540984 website/out/pdf/political-power.pdf
540226 website/out/pdf/coercive-power.pdf
520377 website/out/pdf/productive-power.pdf
496312 website/out/pdf/ideological-power.pdf
479833 website/out/pdf/judicial-power.pdf
468808 website/out/pdf/financial-power.pdf
202684 website/out/images/judicial-power.jpg
199858 website/out/images/ideological-power.jpg
198211 website/out/images/political-power.jpg
196860 website/out/images/coercive-power.jpg
195802 website/out/images/financial-power.jpg
194505 website/out/images/productive-power.jpg
176609 website/out/images/formalized-state.jpg
172834 website/out/_next/static/chunks/fd9d1056-9f91b5e418130764.js
139978 website/out/_next/static/chunks/framework-f66176bb897dc684.js
124635 website/out/_next/static/chunks/117-373243894bd7fac6.js
116489 website/out/_next/static/chunks/main-ed80ab20b1eaf357.js
112594 website/out/_next/static/chunks/polyfills-42372ed130431b0a.js
111437 website/out/og/og-image.png
101507 website/out/images/judicial-power-card.jpg
99590 website/out/images/ideological-power-card.jpg
99194 website/out/images/coercive-power-card.jpg
98882 website/out/images/political-power-card.jpg
98094 website/out/images/financial-power-card.jpg
95888 website/out/images/productive-power-card.jpg
90101 website/out/og/productive-power.png
88054 website/out/og/financial-power.png
87019 website/out/images/formalized-state-card.jpg
85272 website/out/_next/static/media/8e9860b6e62d6359-s.woff2
81969 website/out/og/ideological-power.png
81820 website/out/og/judicial-power.png
80639 website/out/og/coercive-power.png
79734 website/out/og/formalized-state.png
77983 website/out/og/political-power.png
73119 website/out/figures/productive-power-1.svg
63632 website/out/_next/static/media/KaTeX_AMS-Regular.4aafdb68.ttf
53580 website/out/_next/static/media/KaTeX_Main-Regular.b7f8fe9b.ttf
51336 website/out/_next/static/media/KaTeX_Main-Bold.b74a1a8b.ttf
48432 website/out/_next/static/media/e4af272ccee01ff0-s.p.woff2
47966 website/out/index.html
39304 website/out/_next/static/media/e18f83c737786aa7-s.p.woff2
37910 website/out/_next/static/css/f4ff6fba389ef1b6.css
37776 website/out/_next/static/media/7b89a4fd5e90ede0-s.p.woff2
34444 website/out/_next/static/media/e74f24ed7f0e4323-s.woff2
33740 website/out/_next/static/media/48410f3df60da620-s.woff2
33580 website/out/_next/static/media/KaTeX_Main-Italic.47373d1e.ttf
33516 website/out/_next/static/media/KaTeX_AMS-Regular.1608a09b.woff
32968 website/out/_next/static/media/KaTeX_Main-BoldItalic.70d8b0a5.ttf
31308 website/out/_next/static/media/KaTeX_Math-Italic.939bc644.ttf
31196 website/out/_next/static/media/KaTeX_Math-BoldItalic.a879cf83.ttf
30772 website/out/_next/static/media/KaTeX_Main-Regular.7f51fe03.woff
29912 website/out/_next/static/media/KaTeX_Main-Bold.d181c465.woff
28076 website/out/_next/static/media/KaTeX_AMS-Regular.a79f1c31.woff2
27556 website/out/_next/static/media/KaTeX_Typewriter-Regular.d97aaf4a.ttf
26272 website/out/_next/static/media/KaTeX_Main-Regular.0462f03b.woff2
26066 website/out/_next/static/chunks/972-17ea62b17795b286.js
25931 website/out/favicon.ico
25844 website/out/_next/static/media/ba9851c3c22cd980-s.woff2
25324 website/out/_next/static/media/KaTeX_Main-Bold.c3fb5ac2.woff2
25196 website/out/_next/static/media/fd3893c623c32b6d-s.woff2
24873 website/out/index.txt
24504 website/out/_next/static/media/KaTeX_SansSerif-Bold.94e1e8dc.ttf
24145 website/out/figures/formalized-state-1.svg
23408 website/out/_next/static/media/393d45a2251e223a-s.woff2
22364 website/out/_next/static/media/KaTeX_SansSerif-Italic.b4c20c84.ttf
21264 website/out/_next/static/media/ea896c3885e026c1-s.woff2
21132 website/out/_next/static/media/8715d2ed531152f4-s.woff2
20118 website/out/_next/static/css/459226f83420bab5.css
19676 website/out/_next/static/media/KaTeX_Main-Italic.9024d815.woff
19584 website/out/_next/static/media/KaTeX_Fraktur-Bold.b18f59e1.ttf
19572 website/out/_next/static/media/KaTeX_Fraktur-Regular.ed38e79f.ttf
19436 website/out/_next/static/media/KaTeX_SansSerif-Regular.d4d7ba48.ttf
19412 website/out/_next/static/media/KaTeX_Main-BoldItalic.e3f82f9d.woff
19044 website/out/_next/static/media/19cfc7226ec3afaa-s.woff2
18748 website/out/_next/static/media/KaTeX_Math-Italic.5295ba48.woff
18744 website/out/_next/static/media/21350d82a1f187e9-s.woff2
18668 website/out/_next/static/media/KaTeX_Math-BoldItalic.f1035d8d.woff
16988 website/out/_next/static/media/KaTeX_Main-Italic.8916142b.woff2
16780 website/out/_next/static/media/KaTeX_Main-BoldItalic.6f2bb1df.woff2
16648 website/out/_next/static/media/KaTeX_Script-Regular.fe9cbbe1.ttf
16440 website/out/_next/static/media/KaTeX_Math-Italic.f28c23ac.woff2
16400 website/out/_next/static/media/KaTeX_Math-BoldItalic.572d331f.woff2
16028 website/out/_next/static/media/KaTeX_Typewriter-Regular.6258592b.woff
14408 website/out/_next/static/media/KaTeX_SansSerif-Bold.bf59d231.woff
14112 website/out/_next/static/media/KaTeX_SansSerif-Italic.7c9bc82b.woff
13568 website/out/_next/static/media/KaTeX_Typewriter-Regular.a8709e36.woff2
13307 website/out/_next/static/chunks/878-34b15e7090e18027.js
13296 website/out/_next/static/media/KaTeX_Fraktur-Bold.9f256b85.woff
13208 website/out/_next/static/media/KaTeX_Fraktur-Regular.7c187121.woff
13117 website/out/404/index.html
13117 website/out/404.html
12368 website/out/_next/static/media/KaTeX_Caligraphic-Bold.cce5b8ec.ttf
12344 website/out/_next/static/media/KaTeX_Caligraphic-Regular.07ef19e7.ttf
12316 website/out/_next/static/media/KaTeX_SansSerif-Regular.74048478.woff
12228 website/out/_next/static/media/KaTeX_Size1-Regular.fabc004a.ttf
12216 website/out/_next/static/media/KaTeX_SansSerif-Bold.8c5b5494.woff2
12028 website/out/_next/static/media/KaTeX_SansSerif-Italic.3b1e59b3.woff2
11556 website/out/_next/static/media/024ead497118aa23-s.woff2
11508 website/out/_next/static/media/KaTeX_Size2-Regular.d6b476ec.ttf
11348 website/out/_next/static/media/KaTeX_Fraktur-Bold.d42a5579.woff2
11316 website/out/_next/static/media/KaTeX_Fraktur-Regular.d3c882a6.woff2
11272 website/out/_next/static/media/c5fe6dc8356a8c31-s.woff2
11264 website/out/_next/static/media/c48b38fe8bb532f3-s.woff2
10588 website/out/_next/static/media/KaTeX_Script-Regular.07505710.woff
10364 website/out/_next/static/media/KaTeX_Size4-Regular.fbccdabe.ttf

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba website/lib/render-math.ts; nl -ba website/lib/papers.ts; nl -ba website/app/globals.css; nl -ba website/app/papers/'[slug]'/PaperBody.tsx; nl -ba website/app/papers/'[slug]'/page.tsx; nl -ba website/components/PaperCard.tsx; nl -ba website/components/TableOfContents.tsx; nl -ba website/app/page.tsx; nl -ba website/app/layout.tsx; nl -ba website/scripts/fix-html.mjs" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	// Build-time math: replaces LaTeX delimiters in an HTML string with KaTeX markup.
     2	import katex from 'katex';
     3	import extracted from './macros.json';
     4	
     5	// Macros extracted from the \newcommand / \DeclareMathOperator lines of all seven preambles
     6	// (scripts/extract-macros.mjs), plus a few notation helpers.
     7	export const MACROS: Record<string, string> = {
     8	  '\\slashed': '\\not{#1}',
     9	  '\\bra': '\\langle #1|',
    10	  '\\ket': '|#1\\rangle',
    11	  '\\braket': '\\langle #1\\rangle',
    12	  '\\Hom': '\\operatorname{Hom}',
    13	  '\\Tr': '\\operatorname{Tr}',
    14	  '\\Lan': '\\operatorname{Lan}',
    15	  '\\Ran': '\\operatorname{Ran}',
    16	  ...(extracted as Record<string, string>),
    17	};
    18	
    19	function unescapeHtml(s: string) {
    20	  return s
    21	    .replace(/&lt;/g, '<')
    22	    .replace(/&gt;/g, '>')
    23	    .replace(/&quot;/g, '"')
    24	    .replace(/&#39;/g, "'")
    25	    .replace(/&amp;/g, '&');
    26	}
    27	
    28	function render(tex: string, displayMode: boolean) {
    29	  return katex.renderToString(tex, {
    30	    displayMode,
    31	    throwOnError: false,
    32	    trust: true,
    33	    strict: 'ignore',
    34	    macros: { ...MACROS },
    35	  });
    36	}
    37	
    38	export function renderMath(html: string): string {
    39	  // pandoc output: <span class="math inline">\( ... \)</span>
    40	  let out = html.replace(
    41	    /<span class="math (inline|display)"([^>]*)>\\[(\[]([\s\S]*?)\\[)\]]<\/span>/g,
    42	    (_, kind: string, attrs: string, tex: string) => {
    43	      const display = kind === 'display';
    44	      const rendered = render(unescapeHtml(tex), display);
    45	      return display ? `<div class="math-display"${attrs}>${rendered}</div>` : rendered;
    46	    },
    47	  );
    48	  // any remaining bare delimiters
    49	  out = out.replace(/\$\$([\s\S]+?)\$\$/g, (_, t: string) => render(unescapeHtml(t), true));
    50	  out = out.replace(/\\\[([\s\S]+?)\\\]/g, (_, t: string) => render(unescapeHtml(t), true));
    51	  out = out.replace(/\\\(([\s\S]+?)\\\)/g, (_, t: string) => render(unescapeHtml(t), false));
    52	  return out;
    53	}
     1	import fs from 'node:fs';
     2	import path from 'node:path';
     3	import papersJson from '../papers.json';
     4	
     5	export type Paper = {
     6	  slug: string;
     7	  part: string;
     8	  pillar: string;
     9	  color: string;
    10	  title: string;
    11	  subtitle: string;
    12	  question: string;
    13	  abstract: string;
    14	  abstractHtml: string;
    15	  pages: number;
    16	  references: number;
    17	  date: string;
    18	  pdf: string;
    19	  cover: string;
    20	  coverCard: string;
    21	  category: string;
    22	  hasCode: boolean;
    23	};
    24	
    25	export const papers = papersJson as Paper[];
    26	
    27	export const SITE_TITLE = 'The Six Pillars of the Beast System';
    28	export const AUTHOR = 'Matthew Long';
    29	export const GITHUB = 'https://github.com/YonedaAI/the-beast-system';
    30	export const CODE_URL = `${GITHUB}/tree/main/model`;
    31	
    32	export function paperContent(slug: string): string {
    33	  return fs.readFileSync(path.join(process.cwd(), 'content', `${slug}.html`), 'utf8');
    34	}
    35	
    36	export function excerpt(text: string, n = 150): string {
    37	  if (text.length <= n) return text;
    38	  const cut = text.slice(0, n);
    39	  return cut.slice(0, cut.lastIndexOf(' ')) + '...';
    40	}
     1	@tailwind base;
     2	@tailwind components;
     3	@tailwind utilities;
     4	
     5	*, *::before, *::after { box-sizing: border-box; }
     6	
     7	:root {
     8	  --bg: #0b0a0e;
     9	  --surface: #14121a;
    10	  --surface-hover: #1c1923;
    11	  --accent: #ec5a72;
    12	  --accent-hover: #ff7a90;
    13	  --accent-strong: #b81f38;
    14	  --accent-glow: rgba(236, 90, 114, 0.14);
    15	  --accent-secondary: #d9b25f;
    16	  --text: #ece6dc;
    17	  --text-muted: #b5ada1;
    18	  --text-dim: #8d867b;
    19	  --border: #2b2733;
    20	  --code-bg: #100e15;
    21	  --success: #4fb286;
    22	  --warning: #e8793a;
    23	  --header-h: 3.5rem;
    24	}
    25	
    26	html {
    27	  scroll-behavior: smooth;
    28	  scroll-padding-top: 5.5rem;
    29	  background: var(--bg);
    30	}
    31	body {
    32	  margin: 0;
    33	  background:
    34	    radial-gradient(1200px 500px at 85% -10%, rgba(184, 31, 56, 0.16), transparent 60%),
    35	    radial-gradient(900px 400px at -10% 0%, rgba(217, 178, 95, 0.07), transparent 60%),
    36	    var(--bg);
    37	  background-attachment: fixed;
    38	  color: var(--text);
    39	  font-family: var(--font-body), system-ui, sans-serif;
    40	  line-height: 1.65;
    41	  -webkit-font-smoothing: antialiased;
    42	  overflow-wrap: break-word;
    43	}
    44	a { color: var(--accent); text-decoration: none; }
    45	a:hover { color: var(--accent-hover); }
    46	:focus-visible { outline: 2px solid var(--accent-secondary); outline-offset: 2px; border-radius: 2px; }
    47	.display { font-family: var(--font-display), Georgia, serif; }
    48	
    49	/* header and footer */
    50	.site-header {
    51	  position: sticky; top: 0; z-index: 40;
    52	  background: rgba(11, 10, 14, 0.9);
    53	  backdrop-filter: blur(10px);
    54	  border-bottom: 1px solid var(--border);
    55	}
    56	.site-header-inner {
    57	  max-width: 76rem; margin: 0 auto; padding: 0.6rem 1rem;
    58	  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.25rem 1.25rem;
    59	}
    60	.site-title {
    61	  font-family: var(--font-display), Georgia, serif; font-weight: 600; font-size: 1.25rem; line-height: 1.15;
    62	  color: var(--text); letter-spacing: 0.01em; min-height: 44px; display: inline-flex; align-items: center;
    63	}
    64	.site-title:hover { color: var(--text); }
    65	.site-title span { color: var(--accent); }
    66	.site-nav { display: flex; flex-wrap: wrap; gap: 0 0.5rem; margin-left: -0.4rem; font-size: 0.9rem; }
    67	.site-nav a { color: var(--text-muted); padding: 0 0.4rem; min-height: 44px; display: inline-flex; align-items: center; }
    68	.site-nav a:hover { color: var(--text); }
    69	.site-footer { border-top: 1px solid var(--border); margin-top: 4rem; padding: 2rem 1rem 3rem; color: var(--text-dim); font-size: 0.875rem; }
    70	.site-footer-inner { max-width: 76rem; margin: 0 auto; display: grid; gap: 1rem; }
    71	.site-footer a { display: inline-flex; align-items: center; min-height: 44px; }
    72	.site-footer strong { color: var(--text-muted); font-weight: 600; }
    73	
    74	.container { max-width: 76rem; margin: 0 auto; padding: 0 1rem; }
    75	
    76	/* hero */
    77	.hero { padding: 2.5rem 0 2rem; }
    78	.hero-grid { display: grid; gap: 1.5rem; align-items: center; }
    79	.eyebrow { font-size: 0.875rem; letter-spacing: 0.18em; text-transform: uppercase; color: var(--accent-secondary); font-weight: 600; }
    80	.hero h1 {
    81	  font-family: var(--font-display), Georgia, serif; font-weight: 600; letter-spacing: -0.01em;
    82	  font-size: clamp(2.3rem, 8vw, 4.4rem); line-height: 1.02; margin: 0.6rem 0 1rem;
    83	}
    84	.hero h1 em { color: var(--accent); font-style: italic; }
    85	.thesis {
    86	  font-family: var(--font-display), Georgia, serif; font-style: italic; font-size: clamp(1.3rem, 4vw, 1.75rem);
    87	  color: var(--accent-secondary); margin: 0 0 1rem; line-height: 1.25;
    88	}
    89	.lede { color: var(--text-muted); max-width: 38rem; font-size: 1.04rem; }
    90	.hero-stats { display: flex; flex-wrap: wrap; gap: 0.5rem 1.75rem; margin-top: 1.5rem; }
    91	.hero-stat b { display: block; font-family: var(--font-display), Georgia, serif; font-size: 2rem; color: var(--text); line-height: 1; }
    92	.hero-stat span { font-size: 0.875rem; color: var(--text-dim); letter-spacing: 0.08em; text-transform: uppercase; }
    93	.diagram { width: 100%; max-width: 34rem; margin: 0 auto; color: var(--text); }
    94	.diagram svg { width: 100%; height: auto; display: block; }
    95	@media (min-width: 900px) {
    96	  .hero { padding: 4rem 0 3rem; }
    97	  .hero-grid { grid-template-columns: 1.1fr 0.9fr; gap: 3rem; }
    98	}
    99	
   100	.btn {
   101	  display: inline-flex; align-items: center; justify-content: center; gap: 0.4rem; padding: 0.55rem 1rem; min-height: 44px; border-radius: 0.4rem;
   102	  font-weight: 600; font-size: 0.9rem; border: 1px solid var(--border); color: var(--text); background: var(--surface);
   103	  transition: background 0.2s, border-color 0.2s, transform 0.2s;
   104	}
   105	.btn:hover { background: var(--surface-hover); border-color: var(--accent); color: var(--text); }
   106	.btn-primary { background: var(--accent-strong); border-color: var(--accent-strong); color: #fff; }
   107	.btn-primary:hover { background: #d02542; border-color: #d02542; color: #fff; }
   108	.btn-row { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-top: 1.25rem; }
   109	
   110	.section { padding: 2rem 0; }
   111	.section h2 { font-family: var(--font-display), Georgia, serif; font-size: clamp(1.7rem, 5vw, 2.3rem); font-weight: 600; margin: 0 0 0.5rem; line-height: 1.15; }
   112	.section-intro { color: var(--text-muted); max-width: 44rem; margin: 0 0 1.5rem; }
   113	
   114	/* paper cards */
   115	.grid { display: grid; gap: 1.25rem; grid-template-columns: 1fr; }
   116	@media (min-width: 640px) { .grid { grid-template-columns: repeat(2, 1fr); } }
   117	@media (min-width: 1024px) { .grid { grid-template-columns: repeat(3, 1fr); } }
   118	.card {
   119	  --pc: var(--accent);
   120	  position: relative; display: flex; flex-direction: column; overflow: hidden;
   121	  background: var(--surface); border: 1px solid var(--border); border-radius: 0.75rem;
   122	  transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
   123	}
   124	.card::before { content: ''; position: absolute; inset: 0 0 auto 0; height: 3px; background: var(--pc); z-index: 2; }
   125	.card:hover { transform: translateY(-4px); border-color: var(--pc); box-shadow: 0 10px 30px -12px var(--pc); }
   126	.card-media { position: relative; aspect-ratio: 4 / 3; overflow: hidden; background: #fff; border-bottom: 1px solid var(--border); }
   127	.card-media img { width: 100%; height: 100%; object-fit: cover; object-position: top; display: block; }
   128	.card-body { padding: 1rem 1.1rem 1.2rem; display: flex; flex-direction: column; gap: 0.5rem; flex: 1; }
   129	.card-part { display: flex; align-items: center; gap: 0.5rem; font-size: 0.875rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--pc); font-weight: 700; }
   130	.pillar-glyph {
   131	  display: inline-grid; place-items: center; width: 1.75rem; height: 1.75rem; border-radius: 50%;
   132	  border: 1.5px solid var(--pc); font-family: 'KaTeX_SansSerif', var(--font-body), sans-serif; font-weight: 700; font-size: 0.875rem; letter-spacing: 0;
   133	}
   134	.card h3 { font-family: var(--font-display), Georgia, serif; font-size: 1.45rem; line-height: 1.15; font-weight: 600; margin: 0; }
   135	.card h3 a { color: var(--text); display: block; min-height: 44px; }
   136	.card h3 a:hover { color: var(--pc); }
   137	.card-sub { font-size: 0.9rem; color: var(--text-muted); font-style: italic; margin: -0.2rem 0 0; }
   138	.card-q { color: var(--pc); font-size: 0.9rem; font-weight: 600; margin: 0; }
   139	.card-abs { color: var(--text-muted); font-size: 0.9rem; margin: 0; flex: 1; }
   140	.card-meta { color: var(--text-dim); font-size: 0.875rem; }
   141	.card-actions { display: flex; gap: 0.6rem; margin-top: 0.4rem; }
   142	.card-actions .btn { padding: 0.4rem 1rem; min-width: 44px; font-size: 0.875rem; }
   143	.card-actions .btn-read { background: var(--pc); border-color: var(--pc); color: #0b0a0e; }
   144	.card-actions .btn-read:hover { filter: brightness(1.1); color: #0b0a0e; }
   145	.card-full { grid-column: 1 / -1; }
   146	@media (min-width: 640px) {
   147	  .card-full { flex-direction: row; }
   148	  .card-full .card-media { aspect-ratio: auto; width: 38%; border-bottom: 0; border-right: 1px solid var(--border); min-height: 16rem; }
   149	}
   150	
   151	.scope-note { border-left: 3px solid var(--accent-secondary); padding: 0.4rem 0 0.4rem 1rem; color: var(--text-muted); max-width: 46rem; }
   152	.six-list { display: grid; gap: 0.6rem; grid-template-columns: 1fr; margin-top: 1rem; }
   153	@media (min-width: 640px) { .six-list { grid-template-columns: repeat(2, 1fr); } }
   154	@media (min-width: 1024px) { .six-list { grid-template-columns: repeat(3, 1fr); } }
   155	.six-item { display: flex; gap: 0.7rem; align-items: baseline; padding: 0.7rem 0.9rem; background: var(--surface); border: 1px solid var(--border); border-radius: 0.5rem; }
   156	.six-item .pillar-glyph { flex: none; --pc: var(--accent); }
   157	.six-item b { color: var(--text); display: block; }
   158	.six-item span { color: var(--text-muted); font-size: 0.9rem; }
   159	
   160	/* paper page */
   161	.paper-head { padding: 2rem 0 1rem; }
   162	.paper-head .part-tag { color: var(--pc, var(--accent)); font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; font-size: 0.875rem; }
   163	.paper-head h1 { font-family: var(--font-display), Georgia, serif; font-weight: 600; font-size: clamp(2rem, 6.5vw, 3.2rem); line-height: 1.08; margin: 0.4rem 0 0.4rem; }
   164	.paper-head .subtitle { font-family: var(--font-display), Georgia, serif; font-style: italic; font-size: clamp(1.2rem, 3.5vw, 1.6rem); color: var(--accent-secondary); margin: 0 0 0.6rem; }
   165	.paper-head .question { color: var(--pc, var(--accent)); font-weight: 600; margin: 0 0 0.9rem; }
   166	.byline { color: var(--text-muted); font-size: 0.92rem; }
   167	.byline b { color: var(--text); font-weight: 600; }
   168	.chips { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.8rem; }
   169	.chip { font-size: 0.875rem; padding: 0.15rem 0.6rem; border: 1px solid var(--border); border-radius: 999px; color: var(--text-muted); background: var(--surface); }
   170	.abstract { margin: 1.5rem 0 0; padding: 1rem 1.1rem; background: var(--surface); border: 1px solid var(--border); border-left: 3px solid var(--pc, var(--accent)); border-radius: 0.5rem; }
   171	.abstract h2 { font-size: 0.875rem; letter-spacing: 0.16em; text-transform: uppercase; color: var(--text-dim); margin: 0 0 0.4rem; font-family: var(--font-body), sans-serif; font-weight: 700; }
   172	.abstract p { margin: 0; color: var(--text); font-size: 0.98rem; }
   173	
   174	.paper-layout { display: block; padding-top: 1rem; }
   175	.paper-main { min-width: 0; }
   176	@media (min-width: 1024px) {
   177	  .paper-layout { display: grid; grid-template-columns: 17rem minmax(0, 1fr); gap: 2.5rem; align-items: start; }
   178	  .paper-layout > aside { align-self: stretch; }
   179	}
   180	
   181	/* table of contents */
   182	.toc-wrap { margin-bottom: 1rem; }
   183	@media (min-width: 1024px) { .toc-wrap { position: sticky; top: 4.75rem; margin-bottom: 0; } }
   184	.toc-toggle {
   185	  min-height: 44px; display: flex; width: 100%; align-items: center; justify-content: space-between; gap: 0.6rem; cursor: pointer;
   186	  padding: 0.65rem 0.9rem; background: var(--surface); border: 1px solid var(--border); border-radius: 0.5rem;
   187	  color: var(--text); font: inherit; font-weight: 600; font-size: 0.92rem;
   188	}
   189	.toc-toggle:hover { border-color: var(--accent); }
   190	.burger { width: 1.1rem; height: 0.8rem; position: relative; flex: none; }
   191	.burger i { position: absolute; left: 0; right: 0; height: 2px; background: currentColor; border-radius: 1px; transition: transform 0.2s, opacity 0.2s, top 0.2s; }
   192	.burger i:nth-child(1) { top: 0; } .burger i:nth-child(2) { top: 50%; margin-top: -1px; } .burger i:nth-child(3) { bottom: 0; }
   193	.toc-open .burger i:nth-child(1) { top: 50%; margin-top: -1px; transform: rotate(45deg); }
   194	.toc-open .burger i:nth-child(2) { opacity: 0; }
   195	.toc-open .burger i:nth-child(3) { bottom: 50%; margin-bottom: -1px; transform: rotate(-45deg); }
   196	.toc-panel { display: none; margin-top: 0.4rem; background: var(--surface); border: 1px solid var(--border); border-radius: 0.5rem; max-height: 60vh; overflow-y: auto; padding: 0.4rem; }
   197	.toc-open .toc-panel { display: block; }
   198	@media (min-width: 1024px) {
   199	  .toc-toggle { display: none; }
   200	  .toc-panel { display: block; margin-top: 0; max-height: calc(100vh - 7rem); background: transparent; border: 0; border-left: 1px solid var(--border); border-radius: 0; padding: 0; }
   201	  .toc-title { display: block !important; }
   202	}
   203	.toc-title { display: none; font-size: 0.875rem; letter-spacing: 0.16em; text-transform: uppercase; color: var(--text-dim); font-weight: 700; margin: 0 0 0.5rem 0.9rem; }
   204	.toc-item { display: flex; align-items: center; min-height: 44px; padding: 0.3rem 0.7rem; font-size: 0.875rem; line-height: 1.35; color: var(--text-muted); border-left: 2px solid transparent; margin-left: -1px; }
   205	.toc-item:hover { color: var(--text); }
   206	.toc-sub { padding-left: 1.5rem; font-size: 0.875rem; }
   207	.toc-active { color: var(--accent); border-left: 2px solid var(--accent); background: var(--accent-glow); }
   208	
   209	/* fixed pdf button */
   210	.pdf-fab {
   211	  position: fixed; right: 1rem; bottom: 1rem; z-index: 45; display: inline-flex; align-items: center; gap: 0.4rem;
   212	  padding: 0.65rem 1.1rem; min-height: 44px; min-width: 44px; justify-content: center; border-radius: 999px; background: var(--accent-strong); color: #fff; font-weight: 700; font-size: 0.9rem;
   213	  box-shadow: 0 6px 24px rgba(184, 31, 56, 0.45); border: 1px solid rgba(255, 255, 255, 0.15);
   214	}
   215	.pdf-fab:hover { background: #d02542; color: #fff; }
   216	
   217	.paper-nav { display: grid; gap: 0.8rem; grid-template-columns: 1fr; margin-top: 3rem; }
   218	@media (min-width: 640px) { .paper-nav { grid-template-columns: 1fr 1fr; } }
   219	.paper-nav a { display: block; min-height: 44px; padding: 0.9rem 1rem; background: var(--surface); border: 1px solid var(--border); border-radius: 0.6rem; color: var(--text); }
   220	.paper-nav a:hover { border-color: var(--accent); background: var(--surface-hover); color: var(--text); }
   221	.paper-nav small { display: block; color: var(--text-dim); font-size: 0.875rem; letter-spacing: 0.12em; text-transform: uppercase; }
   222	.paper-nav .next { text-align: right; }
   223	
   224	/* paper content */
   225	.paper-content { font-size: 1.04rem; line-height: 1.75; color: var(--text); min-width: 0; }
   226	.paper-content h2 { font-family: var(--font-display), Georgia, serif; font-size: clamp(1.7rem, 5vw, 2.1rem); font-weight: 600; line-height: 1.15; margin: 3rem 0 1rem; padding-top: 1.2rem; border-top: 1px solid var(--border); }
   227	.paper-content h3 { font-family: var(--font-display), Georgia, serif; font-size: 1.4rem; font-weight: 600; line-height: 1.2; margin: 2rem 0 0.6rem; color: var(--accent-secondary); }
   228	.paper-content h4 { font-size: 1.05rem; margin: 1.5rem 0 0.4rem; }
   229	.paper-content .header-section-number { color: var(--accent); margin-right: 0.6rem; font-variant-numeric: tabular-nums; }
   230	.paper-content p { margin: 0 0 1.05rem; }
   231	.paper-content ol, .paper-content ul { padding-left: 1.4rem; margin: 0 0 1.05rem; }
   232	.paper-content li { margin: 0.3rem 0; }
   233	.paper-content a.xref, .paper-content a.xpart { border-bottom: 1px dotted var(--accent); }
   234	.paper-content code { background: var(--code-bg); padding: 0.1em 0.35em; border-radius: 0.25rem; font-size: 0.9em; }
   235	.paper-content dt { font-weight: 700; margin-top: 0.6rem; }
   236	.paper-content dd { margin-left: 1.2rem; }
   237	
   238	.math-display { overflow-x: auto; overflow-y: hidden; margin: 1rem 0; padding: 0.2rem 0; }
   239	.math-display .katex-display { margin: 0; }
   240	.paper-content .katex { font-size: 1.06em; }
   241	
   242	.thm { --tc: var(--accent-secondary); margin: 1.4rem 0; padding: 0.9rem 1.1rem 0.4rem; background: var(--surface); border: 1px solid var(--border); border-left: 4px solid var(--tc); border-radius: 0.5rem; }
   243	.thm-head { margin: 0 0 0.5rem !important; display: flex; flex-wrap: wrap; gap: 0.1rem 0.6rem; align-items: baseline; }
   244	.thm-label { font-weight: 700; color: var(--tc); letter-spacing: 0.02em; }
   245	.thm-name { color: var(--text); font-weight: 600; }
   246	.thm-theorem, .thm-proposition { --tc: var(--accent); }
   247	.thm-lemma, .thm-corollary { --tc: #6f8fe0; }
   248	.thm-definition { --tc: var(--accent-secondary); }
   249	.thm-assumption { --tc: #b072d8; }
   250	.thm-remark, .thm-example { --tc: var(--text-dim); background: transparent; }
   251	.thm-theorem > p:not(.thm-head), .thm-proposition > p:not(.thm-head), .thm-lemma > p:not(.thm-head), .thm-corollary > p:not(.thm-head) { }
   252	.proof { margin: 0.5rem 0 1.5rem; padding-left: 1rem; border-left: 1px dashed var(--border); color: var(--text-muted); }
   253	.proof > p:last-child::after { content: '\25A1'; color: var(--text-dim); margin-left: 0.6rem; }
   254	
   255	.table-scroll { overflow-x: auto; margin: 1.4rem 0; border: 1px solid var(--border); border-radius: 0.5rem; -webkit-overflow-scrolling: touch; }
   256	.table-scroll table { border-collapse: collapse; width: 100%; min-width: 36rem; font-size: 0.88rem; line-height: 1.5; }
   257	.table-scroll caption { caption-side: top; text-align: left; padding: 0.7rem 0.9rem; color: var(--text-muted); font-size: 0.88rem; border-bottom: 1px solid var(--border); background: var(--surface); }
   258	.table-scroll .cap-label, figcaption .cap-label { color: var(--accent-secondary); font-weight: 700; }
   259	.table-scroll th { text-align: left; padding: 0.55rem 0.8rem; background: var(--surface-hover); color: var(--text); border-bottom: 1px solid var(--border); vertical-align: bottom; }
   260	.table-scroll td { padding: 0.55rem 0.8rem; border-bottom: 1px solid var(--border); vertical-align: top; color: var(--text-muted); }
   261	.table-scroll td:first-child { color: var(--text); font-weight: 500; }
   262	.table-scroll tr:last-child td { border-bottom: 0; }
   263	
   264	.paper-content figure { margin: 1.6rem 0; }
   265	.paper-content figure img { display: block; max-width: 100%; height: auto; margin: 0 auto; background: #f4efe6; padding: 0.75rem; border-radius: 0.5rem; }
   266	.paper-content figcaption { margin-top: 0.6rem; color: var(--text-muted); font-size: 0.9rem; }
   267	
   268	.bibliography { font-size: 0.88rem; line-height: 1.55; color: var(--text-muted); }
   269	.bibliography p { padding-left: 1.4rem; text-indent: -1.4rem; margin: 0 0 0.6rem; }
   270	.bibliography a { word-break: break-all; }
   271	
   272	@media (prefers-reduced-motion: reduce) {
   273	  html { scroll-behavior: auto; }
   274	  .card, .btn { transition: none; }
   275	  .card:hover { transform: none; }
   276	}
     1	// Server component: the pre-rendered pandoc + KaTeX HTML is emitted into the static page,
     2	// so crawlers see the full paper text.
     3	export function PaperBody({ html }: { html: string }) {
     4	  return <div className="paper-content" dangerouslySetInnerHTML={{ __html: html }} />;
     5	}
     1	import type { CSSProperties } from 'react';
     2	import type { Metadata } from 'next';
     3	import Link from 'next/link';
     4	import { notFound } from 'next/navigation';
     5	import DOMPurify from 'isomorphic-dompurify';
     6	import * as cheerio from 'cheerio';
     7	import { PaperBody } from './PaperBody';
     8	import { TableOfContents, type Heading } from '@/components/TableOfContents';
     9	import { AUTHOR, CODE_URL, paperContent, papers } from '@/lib/papers';
    10	import { renderMath } from '@/lib/render-math';
    11	
    12	type Props = { params: { slug: string } };
    13	
    14	export const dynamicParams = false;
    15	
    16	export function generateStaticParams() {
    17	  return papers.map((p) => ({ slug: p.slug }));
    18	}
    19	
    20	export function generateMetadata({ params }: Props): Metadata {
    21	  const paper = papers.find((p) => p.slug === params.slug);
    22	  if (!paper) return {};
    23	  const title = paper.subtitle ? `${paper.title}: ${paper.subtitle}` : paper.title;
    24	  const og = `/og/${paper.slug}.png`;
    25	  return {
    26	    title,
    27	    description: paper.abstract,
    28	    openGraph: {
    29	      title,
    30	      description: paper.abstract,
    31	      type: 'article',
    32	      url: `/papers/${paper.slug}/`,
    33	      images: [{ url: og, width: 1200, height: 630 }],
    34	    },
    35	    twitter: { card: 'summary_large_image', title, description: paper.abstract, images: [og] },
    36	  };
    37	}
    38	
    39	function prepare(slug: string) {
    40	  // sanitize our own HTML first, then render math, so KaTeX's MathML (semantics/annotation) stays intact
    41	  const clean = DOMPurify.sanitize(paperContent(slug), { ADD_ATTR: ['target'], USE_PROFILES: { html: true, svg: true } });
    42	  const html = renderMath(clean);
    43	  const $ = cheerio.load(html, null, false);
    44	  const headings: Heading[] = [];
    45	  $('h2[id], h3[id]').each((_, el) => {
    46	    const $e = $(el);
    47	    const num = $e.find('.header-section-number').text().trim();
    48	    const text = $e.clone().children('.header-section-number').remove().end().text().trim();
    49	    headings.push({ id: $e.attr('id')!, text: num ? `${num} ${text}` : text, level: el.tagName === 'h2' ? 2 : 3 });
    50	  });
    51	  return { html, headings };
    52	}
    53	
    54	export default function PaperPage({ params }: Props) {
    55	  const i = papers.findIndex((p) => p.slug === params.slug);
    56	  if (i < 0) notFound();
    57	  const paper = papers[i];
    58	  const prev = papers[i - 1];
    59	  const next = papers[i + 1];
    60	  const { html, headings } = prepare(paper.slug);
    61	
    62	  return (
    63	    <>
    64	      <header className="paper-head" style={{ '--pc': paper.color } as CSSProperties}>
    65	        <div className="container">
    66	          <div className="part-tag">{paper.part} of {papers.length}</div>
    67	          <h1>{paper.title}</h1>
    68	          {paper.subtitle && <p className="subtitle">{paper.subtitle}</p>}
    69	          <p className="question">{paper.question}</p>
    70	          <div className="byline">
    71	            <b>{AUTHOR}</b>, The YonedaAI Collaboration, YonedaAI Research Collective, Chicago, IL
    72	          </div>
    73	          <div className="chips">
    74	            <span className="chip">{paper.date}</span>
    75	            <span className="chip">{paper.pages} pages</span>
    76	            <span className="chip">{paper.references} references</span>
    77	            <span className="chip">{paper.category}</span>
    78	          </div>
    79	          <div className="btn-row">
    80	            <a className="btn btn-primary" href={paper.pdf}>Download PDF</a>
    81	            <a className="btn" href={CODE_URL}>Code</a>
    82	          </div>
    83	          <section className="abstract" aria-labelledby="abstract-h">
    84	            <h2 id="abstract-h">Abstract</h2>
    85	            <p>{paper.abstract}</p>
    86	          </section>
    87	        </div>
    88	      </header>
    89	
    90	      <div className="container paper-layout" style={{ '--pc': paper.color } as CSSProperties}>
    91	        <aside>
    92	          <TableOfContents headings={headings} />
    93	        </aside>
    94	        <article className="paper-main">
    95	          <PaperBody html={html} />
    96	          <nav className="paper-nav" aria-label="Series navigation">
    97	            {prev ? (
    98	              <Link href={`/papers/${prev.slug}/`} className="prev">
    99	                <small>Previous, {prev.part}</small>
   100	                {prev.title}
   101	              </Link>
   102	            ) : (
   103	              <span />
   104	            )}
   105	            {next ? (
   106	              <Link href={`/papers/${next.slug}/`} className="next">
   107	                <small>Next, {next.part}</small>
   108	                {next.title}
   109	              </Link>
   110	            ) : (
   111	              <Link href="/#papers" className="next">
   112	                <small>Back to</small>
   113	                All papers
   114	              </Link>
   115	            )}
   116	          </nav>
   117	        </article>
   118	      </div>
   119	      <a className="pdf-fab" href={paper.pdf} aria-label={`Download PDF of ${paper.title}`}>PDF</a>
   120	    </>
   121	  );
   122	}
     1	import Link from 'next/link';
     2	import Image from 'next/image';
     3	import type { CSSProperties } from 'react';
     4	import { excerpt, type Paper } from '@/lib/papers';
     5	
     6	export function PaperCard({ paper, full = false }: { paper: Paper; full?: boolean }) {
     7	  return (
     8	    <article className={`card ${full ? 'card-full' : ''}`} style={{ '--pc': paper.color } as CSSProperties}>
     9	      <Link href={`/papers/${paper.slug}/`} className="card-media" aria-hidden="true" tabIndex={-1}>
    10	        <Image src={paper.coverCard} alt="" width={640} height={828} unoptimized />
    11	      </Link>
    12	      <div className="card-body">
    13	        <div className="card-part">
    14	          {paper.pillar && <span className="pillar-glyph" aria-hidden="true">{paper.pillar}</span>}
    15	          {paper.part}
    16	        </div>
    17	        <h3>
    18	          <Link href={`/papers/${paper.slug}/`}>{paper.title}</Link>
    19	        </h3>
    20	        {paper.subtitle && <p className="card-sub">{paper.subtitle}</p>}
    21	        <p className="card-q">{paper.question}</p>
    22	        <p className="card-abs">{excerpt(paper.abstract, full ? 320 : 150)}</p>
    23	        <div className="card-meta">{paper.pages} pages · {paper.references} references</div>
    24	        <div className="card-actions">
    25	          <Link className="btn btn-read" href={`/papers/${paper.slug}/`}>Read</Link>
    26	          <a className="btn" href={paper.pdf}>PDF</a>
    27	        </div>
    28	      </div>
    29	    </article>
    30	  );
    31	}
     1	'use client';
     2	import { useEffect, useState } from 'react';
     3	
     4	export type Heading = { id: string; text: string; level: number };
     5	
     6	export function TableOfContents({ headings }: { headings: Heading[] }) {
     7	  const [activeId, setActiveId] = useState('');
     8	  const [open, setOpen] = useState(false);
     9	
    10	  useEffect(() => {
    11	    const onScroll = () => {
    12	      const scrollY = window.scrollY + 100;
    13	      let current = '';
    14	      for (const { id } of headings) {
    15	        const el = document.getElementById(id);
    16	        if (el && el.getBoundingClientRect().top + window.scrollY <= scrollY) current = id;
    17	      }
    18	      setActiveId(current);
    19	    };
    20	    window.addEventListener('scroll', onScroll, { passive: true });
    21	    window.addEventListener('resize', onScroll);
    22	    const t = window.setTimeout(onScroll, 50); // content is injected after mount
    23	    onScroll();
    24	    return () => {
    25	      window.removeEventListener('scroll', onScroll);
    26	      window.removeEventListener('resize', onScroll);
    27	      window.clearTimeout(t);
    28	    };
    29	  }, [headings]);
    30	
    31	  return (
    32	    <div className={`toc-wrap ${open ? 'toc-open' : ''}`}>
    33	      <button
    34	        type="button"
    35	        className="toc-toggle"
    36	        aria-expanded={open}
    37	        aria-controls="toc-panel"
    38	        onClick={() => setOpen((o) => !o)}
    39	      >
    40	        <span>Contents</span>
    41	        <span className="burger" aria-hidden="true">
    42	          <i />
    43	          <i />
    44	          <i />
    45	        </span>
    46	      </button>
    47	      <nav className="toc-panel" id="toc-panel" aria-label="Table of contents">
    48	        <p className="toc-title">Contents</p>
    49	        {headings.map(({ id, text, level }) => (
    50	          <a
    51	            key={id}
    52	            href={`#${id}`}
    53	            onClick={() => setOpen(false)}
    54	            className={`toc-item ${level === 3 ? 'toc-sub' : ''} ${activeId === id ? 'toc-active' : ''}`}
    55	            aria-current={activeId === id ? 'location' : undefined}
    56	          >
    57	            {text}
    58	          </a>
    59	        ))}
    60	      </nav>
    61	    </div>
    62	  );
    63	}
     1	import type { Metadata } from 'next';
     2	import PillarDiagram from '@/components/PillarDiagram';
     3	import { PaperCard } from '@/components/PaperCard';
     4	import { CODE_URL, papers } from '@/lib/papers';
     5	
     6	const description =
     7	  'The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics.';
     8	
     9	export const metadata: Metadata = {
    10	  description,
    11	  openGraph: {
    12	    title: 'The Six Pillars of the Beast System',
    13	    description,
    14	    url: '/',
    15	    images: [{ url: '/og/og-image.png', width: 1200, height: 630 }],
    16	  },
    17	  twitter: { card: 'summary_large_image', description, images: ['/og/og-image.png'] },
    18	};
    19	
    20	const pillars = papers.filter((p) => p.pillar);
    21	const capstone = papers.find((p) => !p.pillar)!;
    22	const totalPages = papers.reduce((n, p) => n + p.pages, 0);
    23	
    24	export default function Home() {
    25	  return (
    26	    <>
    27	      <section className="hero">
    28	        <div className="container hero-grid">
    29	          <div>
    30	            <div className="eyebrow">A seven-part research series</div>
    31	            <h1>
    32	              The Six Pillars of the <em>Beast System</em>
    33	            </h1>
    34	            <p className="lede">
    35	              {'The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics.'}
    36	            </p>
    37	            <p className="thesis">The ideology changes. The institutional functions remain.</p>
    38	            <p className="lede">
    39	              Six functions appear in every governance system: financial, political, judicial, ideological, coercive and
    40	              productive. The series follows them through capitalism, communist party-states, democratic socialism,
    41	              Islamic states, historical Catholic monarchies and secular democracies.
    42	            </p>
    43	            <div className="hero-stats">
    44	              <div className="hero-stat"><b>{papers.length}</b><span>Papers</span></div>
    45	              <div className="hero-stat"><b>6</b><span>Functions</span></div>
    46	              <div className="hero-stat"><b>{totalPages}</b><span>Pages</span></div>
    47	            </div>
    48	            <div className="btn-row">
    49	              <a className="btn btn-primary" href="#papers">Read the papers</a>
    50	              <a className="btn" href={CODE_URL}>Code</a>
    51	            </div>
    52	          </div>
    53	          <PillarDiagram />
    54	        </div>
    55	      </section>
    56	
    57	      <section className="section" id="papers">
    58	        <div className="container">
    59	          <h2>The papers</h2>
    60	          <p className="section-intro">
    61	            Parts I to VI each take one function and ask who holds it. Part VII states the structure they share.
    62	          </p>
    63	          <div className="grid">
    64	            {pillars.map((p) => (
    65	              <PaperCard key={p.slug} paper={p} />
    66	            ))}
    67	            <PaperCard paper={capstone} full />
    68	          </div>
    69	        </div>
    70	      </section>
    71	
    72	      <section className="section">
    73	        <div className="container">
    74	          <h2>The formalized state</h2>
    75	          <p className="section-intro">
    76	            Part VII presents the Formalized State as a universal abstraction. It proves representation, necessity,
    77	            minimality and uniqueness relative to stated axioms, and shows that having the structure does not imply
    78	            capture.
    79	          </p>
    80	          <div className="six-list">
    81	            {pillars.map((p) => (
    82	              <div key={p.slug} className="six-item" style={{ ['--pc' as string]: p.color }}>
    83	                <span className="pillar-glyph" style={{ color: p.color }} aria-hidden="true">{p.pillar}</span>
    84	                <div>
    85	                  <b>{p.title.split(' and ')[0]}</b>
    86	                  <span>{p.question}</span>
    87	                </div>
    88	              </div>
    89	            ))}
    90	          </div>
    91	        </div>
    92	      </section>
    93	
    94	      <section className="section" id="scope">
    95	        <div className="container">
    96	          <h2>Scope</h2>
    97	          <p className="scope-note">
    98	            &quot;Beast System&quot; is a typological reading of Revelation 13. Here it names a universal six-function
    99	            structure. It is never a label for a religion, a people, a regime or a person.
   100	          </p>
   101	        </div>
   102	      </section>
   103	    </>
   104	  );
   105	}
     1	import type { Metadata, Viewport } from 'next';
     2	import { Cormorant_Garamond, Inter } from 'next/font/google';
     3	import Link from 'next/link';
     4	import 'katex/dist/katex.min.css';
     5	import './globals.css';
     6	import { AUTHOR, CODE_URL, GITHUB, SITE_TITLE } from '@/lib/papers';
     7	
     8	const display = Cormorant_Garamond({ subsets: ['latin'], weight: ['500', '600', '700'], style: ['normal', 'italic'], variable: '--font-display', display: 'swap' });
     9	const body = Inter({ subsets: ['latin'], variable: '--font-body', display: 'swap' });
    10	
    11	const siteUrl = process.env.SITE_URL || 'https://the-beast-system.vercel.app';
    12	const description =
    13	  'The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics.';
    14	
    15	export const metadata: Metadata = {
    16	  metadataBase: new URL(siteUrl),
    17	  title: { default: SITE_TITLE, template: `%s | ${SITE_TITLE}` },
    18	  description,
    19	  authors: [{ name: AUTHOR }],
    20	  openGraph: {
    21	    type: 'website',
    22	    siteName: SITE_TITLE,
    23	    title: SITE_TITLE,
    24	    description,
    25	    images: [{ url: '/og/og-image.png', width: 1200, height: 630 }],
    26	  },
    27	  twitter: { card: 'summary_large_image', title: SITE_TITLE, description, images: ['/og/og-image.png'] },
    28	};
    29	
    30	export const viewport: Viewport = { themeColor: '#0b0a0e' };
    31	
    32	export default function RootLayout({ children }: { children: React.ReactNode }) {
    33	  return (
    34	    <html lang="en" className={`${display.variable} ${body.variable}`}>
    35	      <body>
    36	        <header className="site-header">
    37	          <div className="site-header-inner">
    38	            <Link href="/" className="site-title">
    39	              The Six Pillars of the <span>Beast System</span>
    40	            </Link>
    41	            <nav className="site-nav" aria-label="Main">
    42	              <Link href="/#papers">Papers</Link>
    43	              <Link href="/#scope">Scope</Link>
    44	              <a href={CODE_URL}>Code</a>
    45	              <a href={GITHUB}>GitHub</a>
    46	            </nav>
    47	          </div>
    48	        </header>
    49	        <main>{children}</main>
    50	        <footer className="site-footer">
    51	          <div className="site-footer-inner">
    52	            <div>
    53	              <strong>{AUTHOR}</strong>
    54	              <br />
    55	              The YonedaAI Collaboration, YonedaAI Research Collective
    56	              <br />
    57	              Chicago, IL
    58	            </div>
    59	            <div>
    60	              <a href={GITHUB}>github.com/YonedaAI/the-beast-system</a>
    61	            </div>
    62	            <div>October 2026</div>
    63	          </div>
    64	        </footer>
    65	      </body>
    66	    </html>
    67	  );
    68	}
     1	// Steps 3 and 4: raw-LaTeX sweep and structure fixer for the pandoc HTML.
     2	// Reads docs/papers/<slug>.html, writes website/content/<slug>.html and website/papers.json.
     3	// Usage: node fix-html.mjs <repoRoot>
     4	import fs from 'node:fs';
     5	import path from 'node:path';
     6	import { execFileSync } from 'node:child_process';
     7	import { createRequire } from 'node:module';
     8	import { SERIES, SLUGS } from './series.mjs';
     9	
    10	const require = createRequire(import.meta.url);
    11	const cheerio = require('cheerio');
    12	
    13	const root = path.resolve(process.argv[2] || '.');
    14	const outDir = path.join(root, 'website', 'content');
    15	fs.mkdirSync(outDir, { recursive: true });
    16	
    17	const THM = ['theorem', 'proposition', 'lemma', 'corollary', 'definition', 'assumption', 'remark', 'example'];
    18	const cap = (s) => s[0].toUpperCase() + s.slice(1);
    19	const PLURAL = { Corollary: 'Corollaries' };
    20	const plural = (t) => PLURAL[t] || t + 's';
    21	const stats = {};
    22	const bump = (slug, k, n = 1) => {
    23	  stats[slug] ||= {};
    24	  stats[slug][k] = (stats[slug][k] || 0) + n;
    25	};
    26	const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    27	
    28	const docs = {};
    29	const index = {}; // slug -> { id -> {type,num} }
    30	
    31	function load(slug) {
    32	  const html = fs.readFileSync(path.join(root, 'docs', 'papers', `${slug}.html`), 'utf8');
    33	  return cheerio.load(html, null, false);
    34	}
    35	
    36	// Pass 1: numbering in LaTeX style (theorem counter shared and reset per section).
    37	for (const slug of SLUGS) {
    38	  const $ = load(slug);
    39	  docs[slug] = $;
    40	  const idx = (index[slug] = {});
    41	  let sec = 0;
    42	  let c = 0;
    43	  let eq = 0;
    44	  let tab = 0;
    45	  let fig = 0;
    46	  $('h1, h2, h3, div, table, figure, span.math.display').each((_, el) => {
    47	    const $e = $(el);
    48	    const tag = el.tagName;
    49	    if (tag === 'h1' || tag === 'h2' || tag === 'h3') {
    50	      const num = $e.attr('data-number');
    51	      if (tag === 'h1') { sec = parseInt(num, 10); c = 0; }
    52	      if ($e.attr('id') && num) idx[$e.attr('id')] = { type: 'Section', num };
    53	    } else if (tag === 'div') {
    54	      const cls = THM.find((t) => $e.hasClass(t));
    55	      if (cls) {
    56	        c++;
    57	        const num = `${sec}.${c}`;
    58	        $e.attr('data-num', num);
    59	        $e.attr('data-type', cap(cls));
    60	        if ($e.attr('id')) idx[$e.attr('id')] = { type: cap(cls), num };
    61	      }
    62	    } else if (tag === 'table') {
    63	      tab++;
    64	      $e.attr('data-num', String(tab));
    65	      if ($e.attr('id')) idx[$e.attr('id')] = { type: 'Table', num: String(tab) };
    66	    } else if (tag === 'figure') {
    67	      fig++;
    68	      $e.attr('data-num', String(fig));
    69	      if ($e.attr('id')) idx[$e.attr('id')] = { type: 'Figure', num: String(fig) };
    70	    } else if (tag === 'span') {
    71	      const t = $e.text();
    72	      if (/\\begin\{equation\}/.test(t)) {
    73	        eq++;
    74	        $e.attr('data-num', String(eq));
    75	        const m = t.match(/\\label\{([^}]+)\}/);
    76	        if (m) idx[m[1]] = { type: 'Equation', num: String(eq) };
    77	      }
    78	    }
    79	  });
    80	}
    81	
    82	const slugOfRoman = Object.fromEntries(SERIES.map((s) => [s.roman, s.slug]));
    83	
    84	function walkText($, scope, fn, skip) {
    85	  const visit = (node) => {
    86	    if (node.type === 'text') { fn(node); return; }
    87	    if (node.type !== 'tag' && node.type !== 'root') return;
    88	    if (node.type === 'tag' && skip(node)) return;
    89	    for (const ch of [...(node.children || [])]) visit(ch);
    90	  };
    91	  scope.each((_, n) => visit(n));
    92	}
    93	
    94	function refHtml(slug, ids, kind) {
    95	  const idx = index[slug];
    96	  const items = ids.map((id) => ({ id, ...(idx[id] || {}) }));
    97	  if (items.some((i) => !i.type)) {
    98	    bump(slug, 'unresolvedRefs', items.filter((i) => !i.type).length);
    99	    items.forEach((i) => { if (!i.type) { i.type = 'Section'; i.num = '?'; } });
   100	  }
   101	  const fmt = (i) => (i.type === 'Equation' ? `(${i.num})` : i.num);
   102	  const link = (i, text) => `<a class="xref" href="#${esc(i.id)}">${esc(text)}</a>`;
   103	  if (kind === 'ref' || kind === 'eqref') {
   104	    return items.map((i) => link(i, fmt(i))).join(', ');
   105	  }
   106	  // cleveref style: group consecutive items of the same type
   107	  const groups = [];
   108	  for (const i of items) {
   109	    const g = groups[groups.length - 1];
   110	    if (g && g.type === i.type) g.items.push(i);
   111	    else groups.push({ type: i.type, items: [i] });
   112	  }
   113	  const parts = groups.map((g) => {
   114	    const name = g.items.length > 1 ? plural(g.type) : g.type;
   115	    const nums = g.items.map((i) => link(i, fmt(i)));
   116	    const list = nums.length === 2 ? `${nums[0]} and ${nums[1]}` : nums.length > 2 ? `${nums.slice(0, -1).join(', ')}, and ${nums.at(-1)}` : nums[0];
   117	    return `${name} ${list}`;
   118	  });
   119	  return parts.length === 2 ? `${parts[0]} and ${parts[1]}` : parts.length > 2 ? `${parts.slice(0, -1).join(', ')}, and ${parts.at(-1)}` : parts[0];
   120	}
   121	
   122	const TYPE_RE = '(Theorems?|Propositions?|Lemma|Corollary|Definition|Assumption|Remark|Example|Section|Table|Figure)';
   123	
   124	for (const slug of SLUGS) {
   125	  const $ = docs[slug];
   126	
   127	  // headings: h1 sections become h2 so the page title is the only h1
   128	  for (const [from, to] of [['h3', 'h4'], ['h2', 'h3'], ['h1', 'h2']]) {
   129	    $(from).each((_, el) => { el.tagName = to; });
   130	  }
   131	
   132	  // math: normalize equation environments and add tags
   133	  $('span.math').each((_, el) => {
   134	    const $e = $(el);
   135	    let t = $e.text();
   136	    const display = $e.hasClass('display');
   137	    t = t.replace(/^\\[\(\[]\s*/, '').replace(/\s*\\[\)\]]$/, '');
   138	    const lab = t.match(/\\label\{([^}]*)\}/);
   139	    if (lab && display) $e.attr('id', lab[1].trim());
   140	    t = t.replace(/\\label\{[^}]*\}/g, '');
   141	    const num = $e.attr('data-num');
   142	    t = t.replace(/\\begin\{equation\}/, '').replace(/\\end\{equation\}/, '').trim();
   143	    if (num) t += ` \\tag{${num}}`;
   144	    $e.text(display ? `\\[${t}\\]` : `\\(${t}\\)`);
   145	    $e.removeAttr('data-num');
   146	  });
   147	  const lbl = {};
   148	  void lbl;
   149	
   150	  // theorem-like blocks
   151	  $('div[data-type]').each((_, el) => {
   152	    const $e = $(el);
   153	    const type = $e.attr('data-type');
   154	    const num = $e.attr('data-num');
   155	    const first = $e.children('p').first();
   156	    let inner = first.html() || '';
   157	    let name = '';
   158	    const m = inner.match(/^<(?:strong|em)>[A-Za-z]+ \d+<\/(?:strong|em)>(?: \(([\s\S]*?)\)\.)?\s*/);
   159	    if (m) { name = m[1] || ''; inner = inner.slice(m[0].length); }
   160	    else bump(slug, 'thmHeadMissing');
   161	    const head = `<p class="thm-head"><span class="thm-label">${type} ${num}</span>${name ? `<span class="thm-name">${name}</span>` : ''}</p>`;
   162	    first.replaceWith(head + (inner.trim() ? `<p>${inner}</p>` : ''));
   163	    $e.addClass('thm').addClass(`thm-${type.toLowerCase()}`);
   164	    if (!$e.attr('id')) $e.attr('id', `${type.toLowerCase()}-${num.replace('.', '-')}`);
   165	    $e.removeAttr('data-type').removeAttr('data-num');
   166	    bump(slug, 'blocks');
   167	  });
   168	
   169	  // references
   170	  $('a[data-reference]').each((_, el) => {
   171	    const $e = $(el);
   172	    const ids = $e.attr('data-reference').split(',').map((s) => s.trim());
   173	    const kind = $e.attr('data-reference-type') || 'ref+label';
   174	    $e.replaceWith(refHtml(slug, ids, kind.startsWith('ref+') ? 'cref' : kind));
   175	    bump(slug, 'refs');
   176	  });
   177	
   178	  // tables
   179	  $('table').each((_, el) => {
   180	    const $e = $(el);
   181	    const num = $e.attr('data-num');
   182	    $e.removeAttr('data-num');
   183	    const capEl = $e.children('caption');
   184	    if (capEl.length) capEl.prepend(`<span class="cap-label">Table ${num}.</span> `);
   185	    $e.wrap(`<div class="table-scroll" role="region" aria-label="Table ${num}" tabindex="0"></div>`);
   186	    bump(slug, 'tables');
   187	  });
   188	
   189	  // figures
   190	  $('figure').each((_, el) => {
   191	    const $e = $(el);
   192	    const num = $e.attr('data-num');
   193	    const capEl = $e.children('figcaption');
   194	    const altEl = capEl.clone();
   195	    altEl.find('span.math').each((_, m) => {
   196	      $(m).replaceWith($(m).text().replace(/^\\[(\[]|\\[)\]]$/g, '').replace(/\\[a-zA-Z]+/g, '').replace(/[{}^_]/g, ''));
   197	    });
   198	    const alt = altEl.text().trim();
   199	    capEl.prepend(`<span class="cap-label">Figure ${num}.</span> `);
   200	    $e.find('img').attr('alt', alt).attr('loading', 'lazy');
   201	    $e.removeAttr('data-latex-placement').removeAttr('data-num');
   202	    bump(slug, 'figures');
   203	  });
   204	
   205	  // drop empty anchors (focusable, unnamed)
   206	  $('a').each((_, el) => {
   207	    const $e = $(el);
   208	    if (!$e.text().trim() && !$e.find('img, svg').length) { $e.remove(); bump(slug, 'emptyAnchorsRemoved'); }
   209	  });
   210	
   211	  // bibliography
   212	  $('div.thebibliography').each((_, el) => {
   213	    const $e = $(el);
   214	    $e.children('p').first().remove();
   215	    $e.children('p').each((i, p) => {
   216	      const $p = $(p);
   217	      $p.attr('id', `bib-${i + 1}`);
   218	      walkText($, $p, (node) => {
   219	        const t = esc(node.data);
   220	        const out = t.replace(/doi:(10\.[^\s<]+?)(\.?)(?=\s|$)/g, '<a href="https://doi.org/$1">doi:$1</a>$2');
   221	        if (out !== t) $(node).replaceWith(out);
   222	      }, (n) => n.name === 'a');
   223	    });
   224	    $e.attr('class', 'bibliography');
   225	    $e.before('<h2 id="references"><span class="header-section-number"></span>References</h2>');
   226	    bump(slug, 'bibEntries', $e.children('p').length);
   227	  });
   228	  $('div.small').each((_, el) => { $(el).replaceWith($(el).contents()); });
   229	
   230	  // raw LaTeX sweep and cross-Part links in text nodes
   231	  const sweepCounts = {};
   232	  const countSweep = (k) => { sweepCounts[k] = (sweepCounts[k] || 0) + 1; };
   233	  const skipSweep = (node) =>
   234	    (node.name === 'span' && /\bmath\b/.test(node.attribs?.class || '')) || node.name === 'code' || node.name === 'pre';
   235	  walkText($, $.root(), (node) => {
   236	    let s = node.data;
   237	    if (!/[\\$]/.test(s)) return;
   238	    const orig = s;
   239	    s = esc(s);
   240	    const math = (tex, disp) => {
   241	      countSweep('math');
   242	      return `<span class="math ${disp ? 'display' : 'inline'}">${disp ? '\\[' : '\\('}${tex}${disp ? '\\]' : '\\)'}</span>`;
   243	    };
   244	    s = s.replace(/\$\$([\s\S]+?)\$\$/g, (_, t) => math(t, true));
   245	    s = s.replace(/\\\[([\s\S]+?)\\\]/g, (_, t) => math(t, true));
   246	    s = s.replace(/\\\(([\s\S]+?)\\\)/g, (_, t) => math(t, false));
   247	    s = s.replace(/\$([^$\n]+?)\$/g, (m, t) => (/[\\^_{}=]/.test(t) ? math(t, false) : m));
   248	    s = s.replace(/\\(?:emph|textit)\{([^{}]*)\}/g, (_, t) => (countSweep('emph'), `<em>${t}</em>`));
   249	    s = s.replace(/\\textbf\{([^{}]*)\}/g, (_, t) => (countSweep('textbf'), `<strong>${t}</strong>`));
   250	    s = s.replace(/\\texttt\{([^{}]*)\}/g, (_, t) => (countSweep('texttt'), `<code>${t}</code>`));
   251	    s = s.replace(/\\(?:[Cc]ref|ref|eqref|label)\{([^{}]*)\}/g, (_, ids) => {
   252	      countSweep('ref');
   253	      return refHtml(slug, ids.split(',').map((x) => x.trim()), 'cref');
   254	    });
   255	    s = s.replace(/\\cite[a-z]*\{[^{}]*\}/gi, () => (countSweep('cite'), ''));
   256	    if (s !== esc(orig)) $(node).replaceWith(s);
   257	  }, skipSweep);
   258	  for (const [k, v] of Object.entries(sweepCounts)) bump(slug, `swept_${k}`, v);
   259	
   260	  // cross-Part links
   261	  const partRe = new RegExp(`\\bPart (VII|VI|IV|V|III|II|I)\\b(?:(, | )${TYPE_RE} (\\d+(?:\\.\\d+)*))?`, 'g');
   262	  walkText($, $.root(), (node) => {
   263	    const s = node.data;
   264	    if (!/Part [IVX]/.test(s)) return;
   265	    let changed = false;
   266	    const out = esc(s).replace(partRe, (m, roman, sep, type, num) => {
   267	      const target = slugOfRoman[roman];
   268	      let hash = '';
   269	      if (type) {
   270	        const t = type.replace(/s$/, '').replace('Lemma', 'Lemma');
   271	        const key = Object.entries(index[target]).find(([, v]) => v.type === t && v.num === num);
   272	        if (key) hash = `#${key[0]}`;
   273	        else bump(slug, 'crossPartUnmatched');
   274	      }
   275	      changed = true;
   276	      bump(slug, 'crossPartLinks');
   277	      return `<a class="xpart" href="/papers/${target}/${hash}">${m}</a>`;
   278	    });
   279	    if (changed) $(node).replaceWith(out);
   280	  }, (n) => skipSweep(n) || n.name === 'a' || /^h[1-6]$/.test(n.name) || (n.attribs?.class || '') === 'bibliography');
   281	
   282	  // "Definition 2.5 of Long (2026f)" -> link straight to the target block
   283	  const ofRe = new RegExp(`${TYPE_RE} (\\d+(?:\\.\\d+)*) of $`);
   284	  $('a[href^="/papers/"]').each((_, el) => {
   285	    const $e = $(el);
   286	    const href = $e.attr('href');
   287	    if (href.includes('#')) return;
   288	    const prev = el.prev;
   289	    if (!prev || prev.type !== 'text') return;
   290	    const m = prev.data.match(ofRe);
   291	    if (!m) return;
   292	    const target = href.split('/')[2];
   293	    const t = m[1].replace(/s$/, '');
   294	    const hit = Object.entries(index[target] || {}).find(([, v]) => v.type === t && v.num === m[2]);
   295	    if (hit) { $e.attr('href', `${href}#${hit[0]}`); bump(slug, 'ofLinks'); }
   296	  });
   297	
   298	  const html = $.html();
   299	  fs.writeFileSync(path.join(outDir, `${slug}.html`), html);
   300	  const left = (html.replace(/<span class="math[^]*?<\/span>/g, '').match(/\\(frac|mathcal|mathsf|textbf|emph|cite\w*|ref|cref|Cref)\b|\$\$/g) || []).length;
   301	  bump(slug, 'rawLeftovers', left);
   302	}
   303	
   304	// manifest
   305	function pdfPath(slug) {
   306	  const a = path.join(root, 'papers', 'pdf', `${slug}.pdf`);
   307	  return fs.existsSync(a) ? a : path.join(root, 'papers', 'latex', `${slug}.pdf`);
   308	}
   309	function pages(slug) {
   310	  try {
   311	    const out = execFileSync('pdfinfo', [pdfPath(slug)], { encoding: 'utf8' });
   312	    return parseInt(out.match(/Pages:\s+(\d+)/)[1], 10);
   313	  } catch {
   314	    return 0;
   315	  }
   316	}
   317	const pand = (tex, to) =>
   318	  execFileSync('pandoc', ['-f', 'latex-smart', '-t', to, '--wrap=none'], { input: tex, encoding: 'utf8' }).trim();
   319	
   320	const manifest = SERIES.map((s) => {
   321	  const tex = fs.readFileSync(path.join(root, 'papers', 'latex', `${s.slug}.tex`), 'utf8');
   322	  const abs = tex.match(/\\begin\{abstract\}([\s\S]*?)\\end\{abstract\}/)[1].trim();
   323	  const abstract = pand(abs, 'plain').replace(/\s+/g, ' ');
   324	  const refs = (tex.match(/\\bibitem/g) || []).length;
   325	  return {
   326	    slug: s.slug,
   327	    part: s.part,
   328	    pillar: s.pillar,
   329	    color: s.color,
   330	    title: s.title,
   331	    subtitle: s.subtitle,
   332	    question: s.question,
   333	    abstract,
   334	    abstractHtml: pand(abs, 'html5'),
   335	    pages: pages(s.slug),
   336	    references: refs,
   337	    date: 'October 2026',
   338	    pdf: `/pdf/${s.slug}.pdf`,
   339	    cover: `/images/${s.slug}.jpg`,
   340	    coverCard: `/images/${s.slug}-card.jpg`,
   341	    category: 'econ.GN',
   342	    hasCode: true,
   343	  };
   344	});
   345	fs.writeFileSync(path.join(root, 'website', 'papers.json'), JSON.stringify(manifest, null, 2) + '\n');
   346	fs.writeFileSync(path.join(root, 'website', 'content', 'fix-stats.json'), JSON.stringify(stats, null, 2) + '\n');
   347	console.log(JSON.stringify(stats, null, 1));

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba website/app/globals.css | sed -n '220,420p'; nl -ba website/app/papers/'[slug]'/PaperBody.tsx; nl -ba website/app/papers/'[slug]'/page.tsx; nl -ba website/components/PaperCard.tsx; nl -ba website/components/TableOfContents.tsx; nl -ba website/app/page.tsx | sed -n '1,140p'; nl -ba website/scripts/prep-tex.mjs; nl -ba website/scripts/series.mjs" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   220	.paper-nav a:hover { border-color: var(--accent); background: var(--surface-hover); color: var(--text); }
   221	.paper-nav small { display: block; color: var(--text-dim); font-size: 0.875rem; letter-spacing: 0.12em; text-transform: uppercase; }
   222	.paper-nav .next { text-align: right; }
   223	
   224	/* paper content */
   225	.paper-content { font-size: 1.04rem; line-height: 1.75; color: var(--text); min-width: 0; }
   226	.paper-content h2 { font-family: var(--font-display), Georgia, serif; font-size: clamp(1.7rem, 5vw, 2.1rem); font-weight: 600; line-height: 1.15; margin: 3rem 0 1rem; padding-top: 1.2rem; border-top: 1px solid var(--border); }
   227	.paper-content h3 { font-family: var(--font-display), Georgia, serif; font-size: 1.4rem; font-weight: 600; line-height: 1.2; margin: 2rem 0 0.6rem; color: var(--accent-secondary); }
   228	.paper-content h4 { font-size: 1.05rem; margin: 1.5rem 0 0.4rem; }
   229	.paper-content .header-section-number { color: var(--accent); margin-right: 0.6rem; font-variant-numeric: tabular-nums; }
   230	.paper-content p { margin: 0 0 1.05rem; }
   231	.paper-content ol, .paper-content ul { padding-left: 1.4rem; margin: 0 0 1.05rem; }
   232	.paper-content li { margin: 0.3rem 0; }
   233	.paper-content a.xref, .paper-content a.xpart { border-bottom: 1px dotted var(--accent); }
   234	.paper-content code { background: var(--code-bg); padding: 0.1em 0.35em; border-radius: 0.25rem; font-size: 0.9em; }
   235	.paper-content dt { font-weight: 700; margin-top: 0.6rem; }
   236	.paper-content dd { margin-left: 1.2rem; }
   237	
   238	.math-display { overflow-x: auto; overflow-y: hidden; margin: 1rem 0; padding: 0.2rem 0; }
   239	.math-display .katex-display { margin: 0; }
   240	.paper-content .katex { font-size: 1.06em; }
   241	
   242	.thm { --tc: var(--accent-secondary); margin: 1.4rem 0; padding: 0.9rem 1.1rem 0.4rem; background: var(--surface); border: 1px solid var(--border); border-left: 4px solid var(--tc); border-radius: 0.5rem; }
   243	.thm-head { margin: 0 0 0.5rem !important; display: flex; flex-wrap: wrap; gap: 0.1rem 0.6rem; align-items: baseline; }
   244	.thm-label { font-weight: 700; color: var(--tc); letter-spacing: 0.02em; }
   245	.thm-name { color: var(--text); font-weight: 600; }
   246	.thm-theorem, .thm-proposition { --tc: var(--accent); }
   247	.thm-lemma, .thm-corollary { --tc: #6f8fe0; }
   248	.thm-definition { --tc: var(--accent-secondary); }
   249	.thm-assumption { --tc: #b072d8; }
   250	.thm-remark, .thm-example { --tc: var(--text-dim); background: transparent; }
   251	.thm-theorem > p:not(.thm-head), .thm-proposition > p:not(.thm-head), .thm-lemma > p:not(.thm-head), .thm-corollary > p:not(.thm-head) { }
   252	.proof { margin: 0.5rem 0 1.5rem; padding-left: 1rem; border-left: 1px dashed var(--border); color: var(--text-muted); }
   253	.proof > p:last-child::after { content: '\25A1'; color: var(--text-dim); margin-left: 0.6rem; }
   254	
   255	.table-scroll { overflow-x: auto; margin: 1.4rem 0; border: 1px solid var(--border); border-radius: 0.5rem; -webkit-overflow-scrolling: touch; }
   256	.table-scroll table { border-collapse: collapse; width: 100%; min-width: 36rem; font-size: 0.88rem; line-height: 1.5; }
   257	.table-scroll caption { caption-side: top; text-align: left; padding: 0.7rem 0.9rem; color: var(--text-muted); font-size: 0.88rem; border-bottom: 1px solid var(--border); background: var(--surface); }
   258	.table-scroll .cap-label, figcaption .cap-label { color: var(--accent-secondary); font-weight: 700; }
   259	.table-scroll th { text-align: left; padding: 0.55rem 0.8rem; background: var(--surface-hover); color: var(--text); border-bottom: 1px solid var(--border); vertical-align: bottom; }
   260	.table-scroll td { padding: 0.55rem 0.8rem; border-bottom: 1px solid var(--border); vertical-align: top; color: var(--text-muted); }
   261	.table-scroll td:first-child { color: var(--text); font-weight: 500; }
   262	.table-scroll tr:last-child td { border-bottom: 0; }
   263	
   264	.paper-content figure { margin: 1.6rem 0; }
   265	.paper-content figure img { display: block; max-width: 100%; height: auto; margin: 0 auto; background: #f4efe6; padding: 0.75rem; border-radius: 0.5rem; }
   266	.paper-content figcaption { margin-top: 0.6rem; color: var(--text-muted); font-size: 0.9rem; }
   267	
   268	.bibliography { font-size: 0.88rem; line-height: 1.55; color: var(--text-muted); }
   269	.bibliography p { padding-left: 1.4rem; text-indent: -1.4rem; margin: 0 0 0.6rem; }
   270	.bibliography a { word-break: break-all; }
   271	
   272	@media (prefers-reduced-motion: reduce) {
   273	  html { scroll-behavior: auto; }
   274	  .card, .btn { transition: none; }
   275	  .card:hover { transform: none; }
   276	}
     1	// Server component: the pre-rendered pandoc + KaTeX HTML is emitted into the static page,
     2	// so crawlers see the full paper text.
     3	export function PaperBody({ html }: { html: string }) {
     4	  return <div className="paper-content" dangerouslySetInnerHTML={{ __html: html }} />;
     5	}
     1	import type { CSSProperties } from 'react';
     2	import type { Metadata } from 'next';
     3	import Link from 'next/link';
     4	import { notFound } from 'next/navigation';
     5	import DOMPurify from 'isomorphic-dompurify';
     6	import * as cheerio from 'cheerio';
     7	import { PaperBody } from './PaperBody';
     8	import { TableOfContents, type Heading } from '@/components/TableOfContents';
     9	import { AUTHOR, CODE_URL, paperContent, papers } from '@/lib/papers';
    10	import { renderMath } from '@/lib/render-math';
    11	
    12	type Props = { params: { slug: string } };
    13	
    14	export const dynamicParams = false;
    15	
    16	export function generateStaticParams() {
    17	  return papers.map((p) => ({ slug: p.slug }));
    18	}
    19	
    20	export function generateMetadata({ params }: Props): Metadata {
    21	  const paper = papers.find((p) => p.slug === params.slug);
    22	  if (!paper) return {};
    23	  const title = paper.subtitle ? `${paper.title}: ${paper.subtitle}` : paper.title;
    24	  const og = `/og/${paper.slug}.png`;
    25	  return {
    26	    title,
    27	    description: paper.abstract,
    28	    openGraph: {
    29	      title,
    30	      description: paper.abstract,
    31	      type: 'article',
    32	      url: `/papers/${paper.slug}/`,
    33	      images: [{ url: og, width: 1200, height: 630 }],
    34	    },
    35	    twitter: { card: 'summary_large_image', title, description: paper.abstract, images: [og] },
    36	  };
    37	}
    38	
    39	function prepare(slug: string) {
    40	  // sanitize our own HTML first, then render math, so KaTeX's MathML (semantics/annotation) stays intact
    41	  const clean = DOMPurify.sanitize(paperContent(slug), { ADD_ATTR: ['target'], USE_PROFILES: { html: true, svg: true } });
    42	  const html = renderMath(clean);
    43	  const $ = cheerio.load(html, null, false);
    44	  const headings: Heading[] = [];
    45	  $('h2[id], h3[id]').each((_, el) => {
    46	    const $e = $(el);
    47	    const num = $e.find('.header-section-number').text().trim();
    48	    const text = $e.clone().children('.header-section-number').remove().end().text().trim();
    49	    headings.push({ id: $e.attr('id')!, text: num ? `${num} ${text}` : text, level: el.tagName === 'h2' ? 2 : 3 });
    50	  });
    51	  return { html, headings };
    52	}
    53	
    54	export default function PaperPage({ params }: Props) {
    55	  const i = papers.findIndex((p) => p.slug === params.slug);
    56	  if (i < 0) notFound();
    57	  const paper = papers[i];
    58	  const prev = papers[i - 1];
    59	  const next = papers[i + 1];
    60	  const { html, headings } = prepare(paper.slug);
    61	
    62	  return (
    63	    <>
    64	      <header className="paper-head" style={{ '--pc': paper.color } as CSSProperties}>
    65	        <div className="container">
    66	          <div className="part-tag">{paper.part} of {papers.length}</div>
    67	          <h1>{paper.title}</h1>
    68	          {paper.subtitle && <p className="subtitle">{paper.subtitle}</p>}
    69	          <p className="question">{paper.question}</p>
    70	          <div className="byline">
    71	            <b>{AUTHOR}</b>, The YonedaAI Collaboration, YonedaAI Research Collective, Chicago, IL
    72	          </div>
    73	          <div className="chips">
    74	            <span className="chip">{paper.date}</span>
    75	            <span className="chip">{paper.pages} pages</span>
    76	            <span className="chip">{paper.references} references</span>
    77	            <span className="chip">{paper.category}</span>
    78	          </div>
    79	          <div className="btn-row">
    80	            <a className="btn btn-primary" href={paper.pdf}>Download PDF</a>
    81	            <a className="btn" href={CODE_URL}>Code</a>
    82	          </div>
    83	          <section className="abstract" aria-labelledby="abstract-h">
    84	            <h2 id="abstract-h">Abstract</h2>
    85	            <p>{paper.abstract}</p>
    86	          </section>
    87	        </div>
    88	      </header>
    89	
    90	      <div className="container paper-layout" style={{ '--pc': paper.color } as CSSProperties}>
    91	        <aside>
    92	          <TableOfContents headings={headings} />
    93	        </aside>
    94	        <article className="paper-main">
    95	          <PaperBody html={html} />
    96	          <nav className="paper-nav" aria-label="Series navigation">
    97	            {prev ? (
    98	              <Link href={`/papers/${prev.slug}/`} className="prev">
    99	                <small>Previous, {prev.part}</small>
   100	                {prev.title}
   101	              </Link>
   102	            ) : (
   103	              <span />
   104	            )}
   105	            {next ? (
   106	              <Link href={`/papers/${next.slug}/`} className="next">
   107	                <small>Next, {next.part}</small>
   108	                {next.title}
   109	              </Link>
   110	            ) : (
   111	              <Link href="/#papers" className="next">
   112	                <small>Back to</small>
   113	                All papers
   114	              </Link>
   115	            )}
   116	          </nav>
   117	        </article>
   118	      </div>
   119	      <a className="pdf-fab" href={paper.pdf} aria-label={`Download PDF of ${paper.title}`}>PDF</a>
   120	    </>
   121	  );
   122	}
     1	import Link from 'next/link';
     2	import Image from 'next/image';
     3	import type { CSSProperties } from 'react';
     4	import { excerpt, type Paper } from '@/lib/papers';
     5	
     6	export function PaperCard({ paper, full = false }: { paper: Paper; full?: boolean }) {
     7	  return (
     8	    <article className={`card ${full ? 'card-full' : ''}`} style={{ '--pc': paper.color } as CSSProperties}>
     9	      <Link href={`/papers/${paper.slug}/`} className="card-media" aria-hidden="true" tabIndex={-1}>
    10	        <Image src={paper.coverCard} alt="" width={640} height={828} unoptimized />
    11	      </Link>
    12	      <div className="card-body">
    13	        <div className="card-part">
    14	          {paper.pillar && <span className="pillar-glyph" aria-hidden="true">{paper.pillar}</span>}
    15	          {paper.part}
    16	        </div>
    17	        <h3>
    18	          <Link href={`/papers/${paper.slug}/`}>{paper.title}</Link>
    19	        </h3>
    20	        {paper.subtitle && <p className="card-sub">{paper.subtitle}</p>}
    21	        <p className="card-q">{paper.question}</p>
    22	        <p className="card-abs">{excerpt(paper.abstract, full ? 320 : 150)}</p>
    23	        <div className="card-meta">{paper.pages} pages · {paper.references} references</div>
    24	        <div className="card-actions">
    25	          <Link className="btn btn-read" href={`/papers/${paper.slug}/`}>Read</Link>
    26	          <a className="btn" href={paper.pdf}>PDF</a>
    27	        </div>
    28	      </div>
    29	    </article>
    30	  );
    31	}
     1	'use client';
     2	import { useEffect, useState } from 'react';
     3	
     4	export type Heading = { id: string; text: string; level: number };
     5	
     6	export function TableOfContents({ headings }: { headings: Heading[] }) {
     7	  const [activeId, setActiveId] = useState('');
     8	  const [open, setOpen] = useState(false);
     9	
    10	  useEffect(() => {
    11	    const onScroll = () => {
    12	      const scrollY = window.scrollY + 100;
    13	      let current = '';
    14	      for (const { id } of headings) {
    15	        const el = document.getElementById(id);
    16	        if (el && el.getBoundingClientRect().top + window.scrollY <= scrollY) current = id;
    17	      }
    18	      setActiveId(current);
    19	    };
    20	    window.addEventListener('scroll', onScroll, { passive: true });
    21	    window.addEventListener('resize', onScroll);
    22	    const t = window.setTimeout(onScroll, 50); // content is injected after mount
    23	    onScroll();
    24	    return () => {
    25	      window.removeEventListener('scroll', onScroll);
    26	      window.removeEventListener('resize', onScroll);
    27	      window.clearTimeout(t);
    28	    };
    29	  }, [headings]);
    30	
    31	  return (
    32	    <div className={`toc-wrap ${open ? 'toc-open' : ''}`}>
    33	      <button
    34	        type="button"
    35	        className="toc-toggle"
    36	        aria-expanded={open}
    37	        aria-controls="toc-panel"
    38	        onClick={() => setOpen((o) => !o)}
    39	      >
    40	        <span>Contents</span>
    41	        <span className="burger" aria-hidden="true">
    42	          <i />
    43	          <i />
    44	          <i />
    45	        </span>
    46	      </button>
    47	      <nav className="toc-panel" id="toc-panel" aria-label="Table of contents">
    48	        <p className="toc-title">Contents</p>
    49	        {headings.map(({ id, text, level }) => (
    50	          <a
    51	            key={id}
    52	            href={`#${id}`}
    53	            onClick={() => setOpen(false)}
    54	            className={`toc-item ${level === 3 ? 'toc-sub' : ''} ${activeId === id ? 'toc-active' : ''}`}
    55	            aria-current={activeId === id ? 'location' : undefined}
    56	          >
    57	            {text}
    58	          </a>
    59	        ))}
    60	      </nav>
    61	    </div>
    62	  );
    63	}
     1	import type { Metadata } from 'next';
     2	import PillarDiagram from '@/components/PillarDiagram';
     3	import { PaperCard } from '@/components/PaperCard';
     4	import { CODE_URL, papers } from '@/lib/papers';
     5	
     6	const description =
     7	  'The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics.';
     8	
     9	export const metadata: Metadata = {
    10	  description,
    11	  openGraph: {
    12	    title: 'The Six Pillars of the Beast System',
    13	    description,
    14	    url: '/',
    15	    images: [{ url: '/og/og-image.png', width: 1200, height: 630 }],
    16	  },
    17	  twitter: { card: 'summary_large_image', description, images: ['/og/og-image.png'] },
    18	};
    19	
    20	const pillars = papers.filter((p) => p.pillar);
    21	const capstone = papers.find((p) => !p.pillar)!;
    22	const totalPages = papers.reduce((n, p) => n + p.pages, 0);
    23	
    24	export default function Home() {
    25	  return (
    26	    <>
    27	      <section className="hero">
    28	        <div className="container hero-grid">
    29	          <div>
    30	            <div className="eyebrow">A seven-part research series</div>
    31	            <h1>
    32	              The Six Pillars of the <em>Beast System</em>
    33	            </h1>
    34	            <p className="lede">
    35	              {'The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics.'}
    36	            </p>
    37	            <p className="thesis">The ideology changes. The institutional functions remain.</p>
    38	            <p className="lede">
    39	              Six functions appear in every governance system: financial, political, judicial, ideological, coercive and
    40	              productive. The series follows them through capitalism, communist party-states, democratic socialism,
    41	              Islamic states, historical Catholic monarchies and secular democracies.
    42	            </p>
    43	            <div className="hero-stats">
    44	              <div className="hero-stat"><b>{papers.length}</b><span>Papers</span></div>
    45	              <div className="hero-stat"><b>6</b><span>Functions</span></div>
    46	              <div className="hero-stat"><b>{totalPages}</b><span>Pages</span></div>
    47	            </div>
    48	            <div className="btn-row">
    49	              <a className="btn btn-primary" href="#papers">Read the papers</a>
    50	              <a className="btn" href={CODE_URL}>Code</a>
    51	            </div>
    52	          </div>
    53	          <PillarDiagram />
    54	        </div>
    55	      </section>
    56	
    57	      <section className="section" id="papers">
    58	        <div className="container">
    59	          <h2>The papers</h2>
    60	          <p className="section-intro">
    61	            Parts I to VI each take one function and ask who holds it. Part VII states the structure they share.
    62	          </p>
    63	          <div className="grid">
    64	            {pillars.map((p) => (
    65	              <PaperCard key={p.slug} paper={p} />
    66	            ))}
    67	            <PaperCard paper={capstone} full />
    68	          </div>
    69	        </div>
    70	      </section>
    71	
    72	      <section className="section">
    73	        <div className="container">
    74	          <h2>The formalized state</h2>
    75	          <p className="section-intro">
    76	            Part VII presents the Formalized State as a universal abstraction. It proves representation, necessity,
    77	            minimality and uniqueness relative to stated axioms, and shows that having the structure does not imply
    78	            capture.
    79	          </p>
    80	          <div className="six-list">
    81	            {pillars.map((p) => (
    82	              <div key={p.slug} className="six-item" style={{ ['--pc' as string]: p.color }}>
    83	                <span className="pillar-glyph" style={{ color: p.color }} aria-hidden="true">{p.pillar}</span>
    84	                <div>
    85	                  <b>{p.title.split(' and ')[0]}</b>
    86	                  <span>{p.question}</span>
    87	                </div>
    88	              </div>
    89	            ))}
    90	          </div>
    91	        </div>
    92	      </section>
    93	
    94	      <section className="section" id="scope">
    95	        <div className="container">
    96	          <h2>Scope</h2>
    97	          <p className="scope-note">
    98	            &quot;Beast System&quot; is a typological reading of Revelation 13. Here it names a universal six-function
    99	            structure. It is never a label for a religion, a people, a regime or a person.
   100	          </p>
   101	        </div>
   102	      </section>
   103	    </>
   104	  );
   105	}
     1	// Step 0: prepare each .tex for pandoc.
     2	//  - tabularx -> tabular (pandoc drops tabularx)
     3	//  - natbib citations -> author-year text (links to sibling Parts)
     4	//  - tikz figures -> SVG files in public/figures
     5	// Usage: node prep-tex.mjs <repoRoot>
     6	import fs from 'node:fs';
     7	import path from 'node:path';
     8	import { execFileSync } from 'node:child_process';
     9	import { SLUGS } from './series.mjs';
    10	
    11	const root = path.resolve(process.argv[2] || '.');
    12	const outDir = path.join(root, 'docs', '.build');
    13	const figDir = path.join(root, 'website', 'public', 'figures');
    14	fs.mkdirSync(outDir, { recursive: true });
    15	fs.rmSync(figDir, { recursive: true, force: true });
    16	fs.mkdirSync(figDir, { recursive: true });
    17	
    18	const partKey = Object.fromEntries(SLUGS.map((s) => [s, s]));
    19	const keyToSlug = {
    20	  long2026financial: 'financial-power',
    21	  long2026political: 'political-power',
    22	  long2026judicial: 'judicial-power',
    23	  long2026ideological: 'ideological-power',
    24	  long2026coercive: 'coercive-power',
    25	  long2026productive: 'productive-power',
    26	  long2026formalized: 'formalized-state',
    27	};
    28	
    29	function matchBrace(s, i) {
    30	  // s[i] === '{'; return index of the matching '}'
    31	  let d = 0;
    32	  for (let j = i; j < s.length; j++) {
    33	    if (s[j] === '\\') { j++; continue; }
    34	    if (s[j] === '{') d++;
    35	    else if (s[j] === '}') { d--; if (d === 0) return j; }
    36	  }
    37	  throw new Error('unbalanced brace');
    38	}
    39	
    40	function countCols(spec) {
    41	  let n = 0;
    42	  for (let i = 0; i < spec.length; i++) {
    43	    const c = spec[i];
    44	    if (c === '@' || c === '>' || c === '<' || c === '!') { i = matchBrace(spec, i + 1); continue; }
    45	    if ('LpmbCPR'.includes(c)) { n++; if (spec[i + 1] === '{') i = matchBrace(spec, i + 1); continue; }
    46	    if ('lcrYX'.includes(c)) n++;
    47	  }
    48	  return n;
    49	}
    50	
    51	function fixTabularx(tex) {
    52	  let out = '';
    53	  let i = 0;
    54	  const tag = '\\begin{tabularx}';
    55	  while (true) {
    56	    const k = tex.indexOf(tag, i);
    57	    if (k < 0) { out += tex.slice(i); break; }
    58	    out += tex.slice(i, k);
    59	    let p = k + tag.length;
    60	    const wEnd = matchBrace(tex, p); // width arg
    61	    p = wEnd + 1;
    62	    const sEnd = matchBrace(tex, p);
    63	    const spec = tex.slice(p + 1, sEnd);
    64	    out += `\\begin{tabular}{${'l'.repeat(countCols(spec))}}`;
    65	    i = sEnd + 1;
    66	  }
    67	  return out.replaceAll('\\end{tabularx}', '\\end{tabular}');
    68	}
    69	
    70	function parseBib(tex) {
    71	  const map = {};
    72	  const re = /\\bibitem\[([^\]]*)\]\{([^}]+)\}/g;
    73	  let m;
    74	  while ((m = re.exec(tex))) {
    75	    const raw = m[1].replace(/[{}]/g, '');
    76	    const par = raw.lastIndexOf('(');
    77	    map[m[2]] = { author: raw.slice(0, par).trim(), year: raw.slice(par + 1, raw.lastIndexOf(')')).trim() };
    78	  }
    79	  return map;
    80	}
    81	
    82	function fixCites(tex, bib, slug) {
    83	  const missing = new Set();
    84	  const entry = (k, mode) => {
    85	    const b = bib[k];
    86	    if (!b) { missing.add(k); return k; }
    87	    let txt = mode === 't' ? `${b.author} (${b.year})` : `${b.author} ${b.year}`;
    88	    if (keyToSlug[k]) txt = `\\href{/papers/${keyToSlug[k]}/}{${txt}}`;
    89	    return txt;
    90	  };
    91	  const re = /\\([Cc]ite(?:t|p|alt|alp|author)?)\*?((?:\[[^\]]*\])*)\{([^}]*)\}/g;
    92	  const out = tex.replace(re, (_, cmd, opts, keys) => {
    93	    const o = [...opts.matchAll(/\[([^\]]*)\]/g)].map((x) => x[1]);
    94	    const pre = o.length === 2 ? o[0] : '';
    95	    const post = o.length === 2 ? o[1] : o[0] || '';
    96	    const ks = keys.split(',').map((s) => s.trim());
    97	    const c = cmd.toLowerCase();
    98	    if (c === 'citet') {
    99	      return ks.map((k) => entry(k, 't')).join(', ') + (post ? ` (${post})` : '');
   100	    }
   101	    const body = ks.map((k) => entry(k, 'p')).join('; ');
   102	    const inner = (pre ? pre + ' ' : '') + body + (post ? ', ' + post : '');
   103	    return c === 'citealt' || c === 'citealp' ? inner : `(${inner})`;
   104	  });
   105	  if (missing.size) console.warn(`[${slug}] unresolved cite keys: ${[...missing].join(', ')}`);
   106	  return out;
   107	}
   108	
   109	function tikzToSvg(tex, slug) {
   110	  const preambleEnd = tex.indexOf('\\begin{document}');
   111	  const preamble = tex.slice(0, preambleEnd);
   112	  const keep = preamble
   113	    .split('\n')
   114	    .filter((l) => /^\\(usepackage(\[[^\]]*\])?\{(amsmath,amssymb,amsthm|amsmath|amssymb|tikz|xcolor|lmodern)\}|usetikzlibrary|newcommand|DeclareMathOperator|renewcommand\{\\Pr\})/.test(l))
   115	    .join('\n');
   116	  let n = 0;
   117	  const re = /\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}/g;
   118	  return tex.replace(re, (pic) => {
   119	    n++;
   120	    const name = `${slug}-${n}`;
   121	    const work = path.join(outDir, `fig-${name}`);
   122	    fs.mkdirSync(work, { recursive: true });
   123	    fs.writeFileSync(
   124	      path.join(work, 'fig.tex'),
   125	      `\\documentclass[border=6pt]{standalone}\n\\usepackage[T1]{fontenc}\n${keep}\n\\begin{document}\n${pic}\n\\end{document}\n`,
   126	    );
   127	    execFileSync('pdflatex', ['-interaction=nonstopmode', '-halt-on-error', 'fig.tex'], { cwd: work, stdio: 'pipe' });
   128	    execFileSync('pdftocairo', ['-svg', path.join(work, 'fig.pdf'), path.join(figDir, `${name}.svg`)]);
   129	    fs.rmSync(work, { recursive: true, force: true });
   130	    return `\\includegraphics{/figures/${name}.svg}`;
   131	  });
   132	}
   133	
   134	for (const slug of SLUGS) {
   135	  let tex = fs.readFileSync(path.join(root, 'papers', 'latex', `${slug}.tex`), 'utf8');
   136	  const bib = parseBib(tex);
   137	  tex = fixCites(tex, bib, slug);
   138	  tex = fixTabularx(tex);
   139	  tex = tikzToSvg(tex, slug);
   140	  fs.writeFileSync(path.join(outDir, `${slug}.tex`), tex);
   141	  console.log(`prep ${slug}: ${Object.keys(bib).length} bib entries`);
   142	}
     1	// Series metadata shared by the content scripts.
     2	export const SERIES = [
     3	  { slug: 'financial-power', part: 'Part I', roman: 'I', pillar: 'F', title: 'Financial Power and Resource Command', subtitle: '', question: 'Who controls the resources?', color: '#d9b25f' },
     4	  { slug: 'political-power', part: 'Part II', roman: 'II', pillar: 'P', title: 'Political Power and Rule Making', subtitle: '', question: 'Who makes the laws?', color: '#e0556a' },
     5	  { slug: 'judicial-power', part: 'Part III', roman: 'III', pillar: 'J', title: 'Judicial Power and Legal Interpretation', subtitle: '', question: 'Who interprets the laws?', color: '#6f8fe0' },
     6	  { slug: 'ideological-power', part: 'Part IV', roman: 'IV', pillar: 'I', title: 'Ideological Power and Legitimation', subtitle: '', question: 'Who shapes the beliefs?', color: '#b072d8' },
     7	  { slug: 'coercive-power', part: 'Part V', roman: 'V', pillar: 'C', title: 'Coercive Power and Enforcement', subtitle: '', question: 'Who enforces the rules?', color: '#e8793a' },
     8	  { slug: 'productive-power', part: 'Part VI', roman: 'VI', pillar: 'W', title: 'Productive Power and Social Reproduction', subtitle: '', question: 'Who produces the wealth?', color: '#4fb286' },
     9	  { slug: 'formalized-state', part: 'Part VII', roman: 'VII', pillar: '', title: 'The Formalized State', subtitle: 'The Hierarchy of the Beast System', question: 'What structure do all six functions share?', color: '#ece6dc' },
    10	];
    11	export const SLUGS = SERIES.map((s) => s.slug);

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -l 'eq:(margin|necessity|U|aggregation-gap|integration|overlap)' website/out/papers/*/index.html; for id in margin necessity U aggregation-gap integration overlap; do rg -o \".{0,100}(id|href)=\\\"#?eq:"'${id}'"\\\".{0,100}\" website/out/papers/*/index.html | head -n 8; done" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
website/out/papers/political-power/index.html
website/out/papers/financial-power/index.html
website/out/papers/ideological-power/index.html
website/out/papers/coercive-power/index.html
website/out/papers/coercive-power/index.html:/span></span></span><span class="mclose">)</span></span></span></span> is <div class="math-display" id="eq:margin"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.
website/out/papers/coercive-power/index.html:e product of the detection probability and the sanction magnitude. The general form <a class="xref" href="#eq:margin">(2)</a> also covers sanctions that are not punishments in the legal sense: the loss of future coope
website/out/papers/coercive-power/index.html:tyle="margin-right:0.1389em;">T</span></span></span></span> periods. Then <div class="math-display" id="eq:necessity"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.
website/out/papers/coercive-power/index.html:span><span class="mord mathnormal">p</span></span></span></span>, subtracting gives <a class="xref" href="#eq:necessity">(3)</a>. For the second claim, each term satisfies <span class="katex"><span class="katex-mathml"><
website/out/papers/coercive-power/index.html:normal">p</span></span></span></span>. A trivial regime would make the left side of <a class="xref" href="#eq:necessity">(3)</a> non-positive, contradicting <span class="katex"><span class="katex-mathml"><math xmlns="htt
website/out/papers/political-power/index.html:edible replacement. Unaccountable concentration is the illustrative index <div class="math-display" id="eq:U"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.
website/out/papers/coercive-power/index.html:combines these into an illustrative index of unaccountable concentration, <div class="math-display" id="eq:U"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.
website/out/papers/coercive-power/index.html:t:0.15em;"><span></span></span></span></span></span></span></span></span></span> in <a class="xref" href="#eq:U">(1)</a> is small. This is the case that the source paper’s Proposition&nbsp;4 anticipates: concentr
website/out/papers/financial-power/index.html:pan></span></span></span></span></span></span></span></span></span>. Then <div class="math-display" id="eq:aggregation-gap"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.
website/out/papers/financial-power/index.html:/span><span class="mpunct">,</span></span></span></span></span></div> which is&nbsp;<a class="xref" href="#eq:aggregation-gap">(2)</a>. Each variance is nonnegative and vanishes exactly when <span class="katex"><span class="ka
website/out/papers/ideological-power/index.html:thnormal">n</span></span></span></span>, and the integration statistic is <div class="math-display" id="eq:integration"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.
website/out/papers/ideological-power/index.html:"height:0.6444em;"></span><span class="mord">0</span></span></span></span>, then by <a class="xref" href="#eq:integration">(1)</a> <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/Mat
website/out/papers/political-power/index.html:an></span></span></span></span></span></span></span></span></span> of Equation&nbsp;<a class="xref" href="#eq:overlap">(2)</a> as its operative definition. A capture link <span class="katex"><span class="katex-mathml">
website/out/papers/political-power/index.html:al" style="margin-right:0.0576em;">S</span></span></span></span>, and set <div class="math-display" id="eq:overlap"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.
website/out/papers/political-power/index.html:<p><em>Proof.</em> (a) By Equation&nbsp;<a class="xref" href="#eq:overlap">(2)</a>, <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/Ma

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n \"raw LaTeX|eq:margin|touch targets|235 KB|empty focusable|Round 1|box-sizing|unoptimized homepage|fonts under 14\" . --glob '"'!website/out/**'"' --glob '"'!node_modules/**'"' --glob '"'!*pdf'"' --glob '"'!*tex'"' | head -n 200" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
./reviews/website-codex-review-round-2.md:21:Round 2, confirmation review of the Next.js research website. Review only website/app, website/lib, website/components, website/scripts and website/out. Round 1 found these 9 issues; confirm each is resolved, citing evidence from out/: (P1) raw LaTeX inside MathML because DOMPurify stripped semantics/annotation; (P2) six broken equation anchors eq:margin eq:necessity eq:U eq:aggregation-gap eq:integration eq:overlap; (P2) out/og/ empty while og:image URLs point there; (P2) missing global box-sizing border-box causing mobile overflow; (P2) touch targets under 44px; (P2) 50 empty focusable DOI links on the judicial page; (P2) page weight (now reported as at most 235 KB gzip); (P3) unoptimized homepage covers; (P3) fonts under 14px. Also check that rendering math after sanitizing introduces no injection risk (the content is the authors' own static papers built at compile time) and report any NEW issue introduced by the fixes. Output the findings and the VERDICT line only, ending with exactly one of: VERDICT: PASS or VERDICT: NEEDS_FIX
./reviews/website-codex-review-round-2.md:44:I’m using the code-review skill for this confirmation pass. I’ll verify each of the nine Round 1 findings against generated `website/out` artifacts, then separately assess the post-sanitization math path and look for regressions only within the requested directories.
./reviews/website-codex-review-round-2.md:509:     5	*, *::before, *::after { box-sizing: border-box; }
./reviews/website-codex-review-round-2.md:1404:   230	  // raw LaTeX sweep and cross-Part links in text nodes
./reviews/website-codex-review-round-2.md:2074:website/out/papers/coercive-power/index.html:/span></span></span><span class="mclose">)</span></span></span></span> is <div class="math-display" id="eq:margin"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.
./reviews/website-codex-review-round-2.md:2075:website/out/papers/coercive-power/index.html:e product of the detection probability and the sanction magnitude. The general form <a class="xref" href="#eq:margin">(2)</a> also covers sanctions that are not punishments in the legal sense: the loss of future coope
./reviews/coercive-power-codex-review.md:1198:   132	\label{eq:margin}
./reviews/coercive-power-codex-review.md:1257:   191	The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain \citep{becker1968}. In the simplest regimes $d_{i,t} = \pi\mu$, the product of the detection probability and the sanction magnitude. The general form \eqref{eq:margin} also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.
./reviews/coercive-power-codex-review.md:1329:   263	An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
./reviews/coercive-power-codex-review.md:2386:   263	An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
./reviews/coercive-power-codex-review.md:3043:   132	\label{eq:margin}
./reviews/coercive-power-codex-review.md:3102:   191	The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain \citep{becker1968}. In the simplest regimes $d_{i,t} = \pi\mu$, the product of the detection probability and the sanction magnitude. The general form \eqref{eq:margin} also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.
./reviews/coercive-power-codex-review.md:3193:   132	\label{eq:margin}
./reviews/coercive-power-codex-review.md:3252:   191	The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain \citep{becker1968}. In the simplest regimes $d_{i,t} = \pi\mu$, the product of the detection probability and the sanction magnitude. The general form \eqref{eq:margin} also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.
./reviews/coercive-power-codex-review.md:3330:   263	An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
./reviews/coercive-power-codex-review.md:4017:132:\label{eq:margin}
./reviews/coercive-power-codex-review.md:4029:191:The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain \citep{becker1968}. In the simplest regimes $d_{i,t} = \pi\mu$, the product of the detection probability and the sanction magnitude. The general form \eqref{eq:margin} also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.
./reviews/coercive-power-codex-review.md:4044:263:An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
./reviews/coercive-power-codex-review-round-2.md:1198:   132	\label{eq:margin}
./reviews/coercive-power-codex-review-round-2.md:1257:   191	The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain \citep{becker1968}. In the simplest regimes $d_{i,t} = \pi\mu$, the product of the detection probability and the sanction magnitude. The general form \eqref{eq:margin} also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.
./reviews/coercive-power-codex-review-round-2.md:1329:   263	An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
./reviews/coercive-power-codex-review-round-2.md:2386:   263	An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
./reviews/coercive-power-codex-review-round-2.md:3043:   132	\label{eq:margin}
./reviews/coercive-power-codex-review-round-2.md:3102:   191	The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain \citep{becker1968}. In the simplest regimes $d_{i,t} = \pi\mu$, the product of the detection probability and the sanction magnitude. The general form \eqref{eq:margin} also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.
./reviews/coercive-power-codex-review-round-2.md:3193:   132	\label{eq:margin}
./reviews/coercive-power-codex-review-round-2.md:3252:   191	The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain \citep{becker1968}. In the simplest regimes $d_{i,t} = \pi\mu$, the product of the detection probability and the sanction magnitude. The general form \eqref{eq:margin} also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.
./reviews/coercive-power-codex-review-round-2.md:3330:   263	An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
./reviews/coercive-power-codex-review-round-2.md:4017:132:\label{eq:margin}
./reviews/coercive-power-codex-review-round-2.md:4029:191:The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain \citep{becker1968}. In the simplest regimes $d_{i,t} = \pi\mu$, the product of the detection probability and the sanction magnitude. The general form \eqref{eq:margin} also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.
./reviews/coercive-power-codex-review-round-2.md:4044:263:An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
./reviews/website-codex-review-round-1.md:21:Review only the files under website/app, website/lib, website/components, website/scripts and website/out (do not explore papers/, model/ or reviews/). Review the Next.js research website for: HTML readability (semantic HTML, heading hierarchy, ARIA labels); layout bugs (overflow, z-index, flex/grid); design errors (contrast ratios, font sizes, spacing); mobile responsiveness (touch targets >= 44px, viewport, text readability); broken links or missing assets (check every href/src in out/ resolves to a file in out/); KaTeX math pre-rendered server-side via katex.renderToString (not client useEffect) and no raw LaTeX in the static HTML; sidebar TOC active-section tracking by scroll position (last heading above viewport), not IntersectionObserver with narrow rootMargin; scroll features work in static export; paper body rendered in a server component (no hydration mismatch); OG meta: metadataBase set in root layout, every paper page has og:image, og:url, og:title, og:description, twitter:card and twitter:images with ABSOLUTE URLs, homepage has its own OG image - grep out/ to confirm; performance (bundle size, unoptimized images); any pipeline/process language in site copy (agents as a process term, Gemini, Codex, review rounds). List all issues with file paths and line numbers, severity P1/P2/P3. Output the findings list and the VERDICT line only. End with exactly one of: VERDICT: PASS or VERDICT: NEEDS_FIX
./reviews/website-codex-review-round-1.md:1430:   218	  // raw LaTeX sweep and cross-Part links in text nodes
./reviews/website-codex-review-round-1.md:2084:   218	  // raw LaTeX sweep and cross-Part links in text nodes
./reviews/website-codex-review-round-1.md:3198:    "url": "#eq:margin",
./reviews/website-codex-review-round-1.md:3200:    "frag": "eq:margin"
./reviews/website-codex-review-round-1.md:3479:    "url": "#eq:margin",
./reviews/website-codex-review-round-1.md:3481:    "frag": "eq:margin"
./reviews/website-codex-review-round-1.md:3671:rg -n 'box-sizing|overflow-x' website/app/globals.css" in /Users/mlong/Documents/Development/the-beast-system
./reviews/website-codex-review-round-1.md:3914:rg -n 'eq:margin|eq:necessity|eq:U|eq:aggregation-gap|eq:integration|eq:overlap' website/out/papers/*/index.html | cut -d: -f1-2 | sort -u" in /Users/mlong/Documents/Development/the-beast-system
./reviews/website-codex-review-round-1.md:4122:- **P1** — KaTeX is server-rendered, but sanitizing afterward strips `<semantics>/<annotation>` while preserving their TeX text. All seven exported papers therefore contain raw LaTeX inside MathML—3,984 affected expressions; e.g. `\mathsf{F}`. [page.tsx:40](</Users/mlong/Documents/Development/the-beast-system/website/app/papers/[slug]/page.tsx:40>), [render-math.ts:29](/Users/mlong/Documents/Development/the-beast-system/website/lib/render-math.ts:29), [financial-power/index.html:3](/Users/mlong/Documents/Development/the-beast-system/website/out/papers/financial-power/index.html:3)
./reviews/website-codex-review-round-1.md:4124:- **P2** — Six equation fragment targets are broken: `eq:margin`, `eq:necessity`, `eq:U`, `eq:aggregation-gap`, `eq:integration`, and `eq:overlap`. Labels are indexed, then removed without assigning their IDs to rendered equations. [fix-html.mjs:71](/Users/mlong/Documents/Development/the-beast-system/website/scripts/fix-html.mjs:71), [fix-html.mjs:132](/Users/mlong/Documents/Development/the-beast-system/website/scripts/fix-html.mjs:132), [coercive-power/index.html:55](/Users/mlong/Documents/Development/the-beast-system/website/out/papers/coercive-power/index.html:55), [financial-power/index.html:38](/Users/mlong/Documents/Development/the-beast-system/website/out/papers/financial-power/index.html:38)
./reviews/website-codex-review-round-1.md:4130:- **P2** — Multiple mobile touch targets are below the required 44px: header links are approximately 30px high, ordinary buttons approximately 41px, card buttons approximately 35px, and TOC links approximately 27px. [globals.css:64](/Users/mlong/Documents/Development/the-beast-system/website/app/globals.css:64), [globals.css:97](/Users/mlong/Documents/Development/the-beast-system/website/app/globals.css:97), [globals.css:139](/Users/mlong/Documents/Development/the-beast-system/website/app/globals.css:139), [globals.css:201](/Users/mlong/Documents/Development/the-beast-system/website/app/globals.css:201)
./reviews/website-codex-review-round-1.md:4147:- **P1** — KaTeX is server-rendered, but sanitizing afterward strips `<semantics>/<annotation>` while preserving their TeX text. All seven exported papers therefore contain raw LaTeX inside MathML—3,984 affected expressions; e.g. `\mathsf{F}`. [page.tsx:40](</Users/mlong/Documents/Development/the-beast-system/website/app/papers/[slug]/page.tsx:40>), [render-math.ts:29](/Users/mlong/Documents/Development/the-beast-system/website/lib/render-math.ts:29), [financial-power/index.html:3](/Users/mlong/Documents/Development/the-beast-system/website/out/papers/financial-power/index.html:3)
./reviews/website-codex-review-round-1.md:4149:- **P2** — Six equation fragment targets are broken: `eq:margin`, `eq:necessity`, `eq:U`, `eq:aggregation-gap`, `eq:integration`, and `eq:overlap`. Labels are indexed, then removed without assigning their IDs to rendered equations. [fix-html.mjs:71](/Users/mlong/Documents/Development/the-beast-system/website/scripts/fix-html.mjs:71), [fix-html.mjs:132](/Users/mlong/Documents/Development/the-beast-system/website/scripts/fix-html.mjs:132), [coercive-power/index.html:55](/Users/mlong/Documents/Development/the-beast-system/website/out/papers/coercive-power/index.html:55), [financial-power/index.html:38](/Users/mlong/Documents/Development/the-beast-system/website/out/papers/financial-power/index.html:38)
./reviews/website-codex-review-round-1.md:4155:- **P2** — Multiple mobile touch targets are below the required 44px: header links are approximately 30px high, ordinary buttons approximately 41px, card buttons approximately 35px, and TOC links approximately 27px. [globals.css:64](/Users/mlong/Documents/Development/the-beast-system/website/app/globals.css:64), [globals.css:97](/Users/mlong/Documents/Development/the-beast-system/website/app/globals.css:97), [globals.css:139](/Users/mlong/Documents/Development/the-beast-system/website/app/globals.css:139), [globals.css:201](/Users/mlong/Documents/Development/the-beast-system/website/app/globals.css:201)
./reviews/coercive-power-codex-review-round-1.md:181:   130	\label{eq:margin}
./reviews/coercive-power-codex-review-round-1.md:240:   189	The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain \citep{becker1968}. In the simplest regimes $d_{i,t} = \pi\mu$, the product of the detection probability and the sanction magnitude. The general form \eqref{eq:margin} also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.
./reviews/coercive-power-codex-review-round-1.md:312:   261	An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
./reviews/coercive-power-codex-review-round-1.md:1102:   130	\label{eq:margin}
./reviews/coercive-power-codex-review-round-1.md:1161:   189	The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain \citep{becker1968}. In the simplest regimes $d_{i,t} = \pi\mu$, the product of the detection probability and the sanction magnitude. The general form \eqref{eq:margin} also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.
./reviews/coercive-power-codex-review-round-1.md:1233:   261	An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
./reviews/coercive-power-codex-review-round-1.md:2047:   261	An agent with $r$ periods of exclusion remaining who complies at $t$ is excluded in periods $t+1, \dots, t+r$ and cooperates from $t+r+1$ onward. If it violates, it is excluded in periods $t+1, \dots, t+L$. The two continuations differ only in periods $t+r+1, \dots, t+L$, in which the complier receives $b$ and the violator does not, so $d = b\sum_{k=r+1}^{L}\delta^k$ by \eqref{eq:margin}. For $r = 0$ the sum is $b\,\delta(1-\delta^L)/(1-\delta)$. Exclusion is delivered by each agent withholding its own cooperation, so no agent holds authority over another's response, and under equal participation each holds an equal share $1/n$ of the decision-relevant control over coercive acts. Then $H^{\pC} = n \cdot (1/n)^2 = 1/n$.
./reviews/model-codex-review-round-2.md:32:This is review round 2. Round 1 raised: (1) Prop A holds required strong connectivity; (2) dependencies not checked per system; (3) weight sensitivity disconnected from assess(); (4) capture-link endpoints not tied to polity actors, flags not bool-checked; (5) counter-model failed at thresholds (1,1); (6) tolerance could push U above 1; (7) thresholds stored unconverted, simulate lacked finiteness checks. Verify each is fixed and look for anything new.
./docs/papers/coercive-power.html:30:\label{eq:margin}
./docs/papers/coercive-power.html:61:<p>The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain (Becker 1968). In the simplest regimes <span class="math inline">\(d_{i,t} = \pi\mu\)</span>, the product of the detection probability and the sanction magnitude. The general form <a href="#eq:margin" data-reference-type="eqref" data-reference="eq:margin">[eq:margin]</a> also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.</p>
./website/scripts/fix-html.mjs:230:  // raw LaTeX sweep and cross-Part links in text nodes
./team/integration-review.md:43:## Round 1 items: resolution
./team/integration-review.md:77:Round 1 had one such sentence, at Part V Cor 3.7, "coercion of this kind depends on no other pillar". It now reads (L254): "does not need the $\pF \to \pC$ or $\pI \to \pC$ arc ...; it still depends on the other pillars through the arcs of \cref{sec:depint}, for example $\pW \to \pC$."
./website/app/globals.css:5:*, *::before, *::after { box-sizing: border-box; }
./website/content/coercive-power.html:25:<p class="thm-head"><span class="thm-label">Definition 2.4</span><span class="thm-name">Sanction regime and deterrence margin</span></p><p>Consider agents <span class="math inline">\(i \in N = \{1,\dots,n\}\)</span> who in each period <span class="math inline">\(t\)</span> choose <span class="math inline">\(v_{i,t} \in \{0,1\}\)</span>, where <span class="math inline">\(v_{i,t} = 1\)</span> means violating a given rule. Let <span class="math inline">\(\sigma\)</span> be a strategy profile and <span class="math inline">\(h_t\)</span> a history. For <span class="math inline">\(v \in \{0,1\}\)</span> let <span class="math inline">\(W_i(h_t, v)\)</span> be <span class="math inline">\(i\)</span>’s expected discounted payoff from period <span class="math inline">\(t\)</span> onward, excluding the current temptation term, when <span class="math inline">\(i\)</span> chooses <span class="math inline">\(v\)</span> at <span class="math inline">\((t,h_t)\)</span>, follows <span class="math inline">\(\sigma_i\)</span> thereafter, and the other agents follow <span class="math inline">\(\sigma_{-i}\)</span> throughout. The <em>deterrence margin</em> faced by <span class="math inline">\(i\)</span> at <span class="math inline">\((t,h_t)\)</span> is <span class="math display" id="eq:margin">\[d_{i,t} = W_i(h_t, 0) - W_i(h_t, 1), \tag{2}\]</span> with discount factor <span class="math inline">\(\delta \in [0,1)\)</span>. The <em>sanction regime</em> of <span class="math inline">\(\sigma\)</span> is the map <span class="math inline">\((i, h_t) \mapsto d_{i,t}\)</span>. The regime is <em>trivial</em> if <span class="math inline">\(d_{i,t} \le 0\)</span> at every reachable node.</p>
./website/content/coercive-power.html:55:<p>The lemma is a dynamic version of the deterrence condition in the economics of crime: a rational offender is deterred when the expected cost of punishment exceeds the gain (Becker 1968). In the simplest regimes <span class="math inline">\(d_{i,t} = \pi\mu\)</span>, the product of the detection probability and the sanction magnitude. The general form <a class="xref" href="#eq:margin">(2)</a> also covers sanctions that are not punishments in the legal sense: the loss of future cooperation in a repeated game, a damaged reputation in a trading network, or exclusion from the next meat distribution.</p>

codex
So far, the six named equation fragments now have matching IDs in the same exported documents, and the OG directory is populated. I’m running broader artifact checks now (all fragment links/assets, MathML structure, empty anchors, gzip sizes, image dimensions, and unsafe emitted markup) so the verdict also catches any regression beyond the named cases.
hook: PreToolUse
hook: PreToolUse Completed
2026-10-22T18:24:12.656502Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "node -e '
const fs=require(\"fs\"),path=require(\"path\"),zlib=require(\"zlib\"),cheerio=require(\"./website/node_modules/cheerio\");
const out=path.resolve(\"website/out\"),htmlFiles=[];
function walk(d){for(const n of fs.readdirSync(d)){const p=path.join(d,n),s=fs.statSync(p);if(s.isDirectory())walk(p);else if(n.endsWith(\".html\"))htmlFiles.push(p)}} walk(out);
for(const p of htmlFiles.filter(p=>p.includes(\"/papers/\"))){
 const raw=fs.readFileSync(p,\"utf8\"),"'$=cheerio.load(raw);
 const expr=$(".katex-mathml math").length,sem=$(".katex-mathml math > semantics").length,ann=$(".katex-mathml math > semantics > annotation[encoding='"\\\"application/x-tex\\\"]\").length;
 "'$("annotation").remove(); $("script,style").remove();
 const visibleRaw=($("body").text().match(/'"\\\\\\\\(?:mathsf|mathcal|frac|sum|begin|operatorname|tag|textbf|mathbf|lambda|delta|sigma|p[A-Z])\\\\b/g)||[]).length;
 const empty="'$("a[href]").filter((i,e)=>!$(e).text().trim()&&!$(e).find("img,svg").length).length;
 const ids=new Set($("[id]").map((i,e)=>$(e).attr("id")).get()),badHash=[];
 $("a[href''^='"\\\"#\\\"]\").each((i,e)=>{const h="'$(e).attr("href").slice(1);if(h&&!ids.has(h))badHash.push(h)});
 const unsafe=[]; $("script[src!='"\\\"/_next/\\\"],iframe,object,embed\").each((i,e)=>unsafe.push(e.tagName)); "'$("*").each((i,e)=>{for(const [k,v] of Object.entries(e.attribs||{})){if(/''^on/i.test(k)||((k==="href"||k==="src"||k==="xlink:href")&&/''^'"\\\\s*(?:javascript|vbscript|data):/i.test(v)))unsafe.push("'`${e.tagName}:${k}=${v.slice(0,60)}`)}});
 console.log(JSON.stringify({page:path.basename(path.dirname(p)),bytes:raw.length,gzip:zlib.gzipSync(raw,{level:9}).length,math:expr,semantics:sem,annotations:ann,visibleRaw,emptyLinks:empty,brokenHashes:[...new Set(badHash)],unsafe}));
}'"'
printf '%s\\n' 'FONT SIZES'; rg -o 'font-size:["'^;}]*'"' website/out/_next/static/css/*.css | sort -u
printf '%s\\n' 'BOX/TARGET RULES'; rg -o '.{0,80}(box-sizing:border-box|min-height:44px|min-width:44px).{0,100}' website/out/_next/static/css/*.css
printf '%s\\n' 'IMAGE FILES'; file website/out/images/*-card.jpg website/out/images/*.jpg website/out/og/*.png
printf '%s\\n' 'HOMEPAGE IMAGE MARKUP'; rg -o '<img["'^>]+(?:financial|political|judicial|ideological|coercive|productive|formalized-state)-card'"\\.jpg["'^>]*>'"' website/out/index.html" in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T18:24:26.245066Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 862ms:
{"page":"coercive-power","bytes":1915100,"gzip":185594,"math":497,"semantics":497,"annotations":497,"visibleRaw":0,"emptyLinks":0,"brokenHashes":[],"unsafe":[]}
{"page":"financial-power","bytes":1485449,"gzip":148502,"math":314,"semantics":314,"annotations":314,"visibleRaw":0,"emptyLinks":0,"brokenHashes":[],"unsafe":[]}
{"page":"formalized-state","bytes":3843673,"gzip":239640,"math":1264,"semantics":1264,"annotations":1264,"visibleRaw":0,"emptyLinks":0,"brokenHashes":[],"unsafe":[]}
{"page":"ideological-power","bytes":2065976,"gzip":169824,"math":525,"semantics":525,"annotations":525,"visibleRaw":0,"emptyLinks":0,"brokenHashes":[],"unsafe":[]}
{"page":"judicial-power","bytes":1649043,"gzip":148547,"math":377,"semantics":377,"annotations":377,"visibleRaw":0,"emptyLinks":0,"brokenHashes":[],"unsafe":[]}
{"page":"political-power","bytes":1816593,"gzip":170562,"math":515,"semantics":515,"annotations":515,"visibleRaw":0,"emptyLinks":0,"brokenHashes":[],"unsafe":[]}
{"page":"productive-power","bytes":2124995,"gzip":173019,"math":531,"semantics":531,"annotations":531,"visibleRaw":0,"emptyLinks":0,"brokenHashes":[],"unsafe":[]}
FONT SIZES
website/out/_next/static/css/459226f83420bab5.css:font-size:.875rem
website/out/_next/static/css/459226f83420bab5.css:font-size:.88rem
website/out/_next/static/css/459226f83420bab5.css:font-size:.92rem
website/out/_next/static/css/459226f83420bab5.css:font-size:.98rem
website/out/_next/static/css/459226f83420bab5.css:font-size:.9em
website/out/_next/static/css/459226f83420bab5.css:font-size:.9rem
website/out/_next/static/css/459226f83420bab5.css:font-size:1.04rem
website/out/_next/static/css/459226f83420bab5.css:font-size:1.05rem
website/out/_next/static/css/459226f83420bab5.css:font-size:1.06em
website/out/_next/static/css/459226f83420bab5.css:font-size:1.25rem
website/out/_next/static/css/459226f83420bab5.css:font-size:1.45rem
website/out/_next/static/css/459226f83420bab5.css:font-size:1.4rem
website/out/_next/static/css/459226f83420bab5.css:font-size:100%
website/out/_next/static/css/459226f83420bab5.css:font-size:1em
website/out/_next/static/css/459226f83420bab5.css:font-size:2rem
website/out/_next/static/css/459226f83420bab5.css:font-size:75%
website/out/_next/static/css/459226f83420bab5.css:font-size:80%
website/out/_next/static/css/459226f83420bab5.css:font-size:clamp(1.2rem,3.5vw,1.6rem)
website/out/_next/static/css/459226f83420bab5.css:font-size:clamp(1.3rem,4vw,1.75rem)
website/out/_next/static/css/459226f83420bab5.css:font-size:clamp(1.7rem,5vw,2.1rem)
website/out/_next/static/css/459226f83420bab5.css:font-size:clamp(1.7rem,5vw,2.3rem)
website/out/_next/static/css/459226f83420bab5.css:font-size:clamp(2.3rem,8vw,4.4rem)
website/out/_next/static/css/459226f83420bab5.css:font-size:clamp(2rem,6.5vw,3.2rem)
website/out/_next/static/css/459226f83420bab5.css:font-size:inherit
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.2009646302em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.2410800386em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.2411575563em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.2813504823em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.2892960463em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.2893518519em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.3215434084em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.337512054em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.3472222222em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.3617363344em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.3857280617em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.4019292605em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.4050925926em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.4166666667em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.4339440694em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.462962963em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.4821600771em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.4823151125em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.4861111111em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.5208333333em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.5555555556em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.5785920926em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.5787037037em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.578778135em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.5833333333em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.5em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.625em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.6666666667em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.6943105111em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.6944444444em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.6945337621em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.6em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.7142857143em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.75em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.7777777778em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.7em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.8331726133em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.8333333333em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.8336012862em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.8571428571em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.875em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.8888888889em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.8em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:.9em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.1111111111em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.125em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.1428571429em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.1666666667em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.1996142719em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.2002314815em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.25em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.2857142857em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.2em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.3333333333em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.4285714286em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.4398148148em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.4402777778em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.44em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.4em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.5em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.6666666667em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.6em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.7142857143em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.7277777778em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.7283333333em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.728em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.8em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1.92em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:1px
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2.0571428571em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2.0733333333em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2.074em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2.16em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2.3044444444em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2.4685714286em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2.488em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2.4em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2.5925em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2.7644444444em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2.88em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2.9628571429em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:2em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:3.11em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:3.4566666667em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:3.456em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:3.5542857143em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:4.1466666667em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:4.148em
website/out/_next/static/css/f4ff6fba389ef1b6.css:font-size:4.976em
BOX/TARGET RULES
website/out/_next/static/css/f4ff6fba389ef1b6.css:.katex .boxpad{padding:0 .3em}.katex .fbox,.katex .fcolorbox{border:.04em solid;box-sizing:border-box}.katex .cancel-pad{padding:0 .2em}.katex .cancel-lap{margin-left:-.2em;margin-right:-.2em}.katex .k
website/out/_next/static/css/f4ff6fba389ef1b6.css:ttom-width:.08em}.katex .angl{border-right:.049em solid;border-top:.049em solid;box-sizing:border-box;margin-right:.03889em}.katex .anglpad{padding:0 .03889em}.katex .reflectbox{display:inline-block;tr
website/out/_next/static/css/459226f83420bab5.css:vert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)}*,:after,:before{box-sizing:border-box}:root{--bg:#0b0a0e;--surface:#14121a;--surface-hover:#1c1923;--accent:#ec5a72;--accent-hover:#ff7a9
website/out/_next/static/css/459226f83420bab5.css:a,serif;font-weight:600;font-size:1.25rem;line-height:1.15;letter-spacing:.01em;min-height:44px;display:inline-flex;align-items:center}.site-title,.site-title:hover{color:var(--text)}.site-title 
website/out/_next/static/css/459226f83420bab5.css:left:-.4rem;font-size:.9rem}.site-nav a{color:var(--text-muted);padding:0 .4rem;min-height:44px;display:inline-flex;align-items:center}.site-nav a:hover{color:var(--text)}.site-footer{border-top:
website/out/_next/static/css/459226f83420bab5.css:uto;display:grid;gap:1rem}.site-footer a{display:inline-flex;align-items:center;min-height:44px}.site-footer strong{color:var(--text-muted);font-weight:600}.container{max-width:76rem;margin:0 aut
website/out/_next/static/css/459226f83420bab5.css:ne-flex;align-items:center;justify-content:center;gap:.4rem;padding:.55rem 1rem;min-height:44px;border-radius:.4rem;font-weight:600;font-size:.9rem;border:1px solid var(--border);background:var(-
website/out/_next/static/css/459226f83420bab5.css:height:1.15;font-weight:600;margin:0}.card h3 a{color:var(--text);display:block;min-height:44px}.card h3 a:hover{color:var(--pc)}.card-sub{font-size:.9rem;color:var(--text-muted);font-style:itali
website/out/_next/static/css/459226f83420bab5.css:s{display:flex;gap:.6rem;margin-top:.4rem}.card-actions .btn{padding:.4rem 1rem;min-width:44px;font-size:.875rem}.card-actions .btn-read{background:var(--pc);border-color:var(--pc);color:#0b0a0e
website/out/_next/static/css/459226f83420bab5.css:idth:1024px){.toc-wrap{position:sticky;top:4.75rem;margin-bottom:0}}.toc-toggle{min-height:44px;display:flex;width:100%;align-items:center;justify-content:space-between;gap:.6rem;cursor:pointer;p
website/out/_next/static/css/459226f83420bab5.css:ont-weight:700;margin:0 0 .5rem .9rem}.toc-item{display:flex;align-items:center;min-height:44px;padding:.3rem .7rem;font-size:.875rem;line-height:1.35;color:var(--text-muted);border-left:2px soli
website/out/_next/static/css/459226f83420bab5.css:index:45;display:inline-flex;align-items:center;gap:.4rem;padding:.65rem 1.1rem;min-height:44px;min-width:44px;justify-content:center;border-radius:999px;background:var(--accent-strong);color:#ff
website/out/_next/static/css/459226f83420bab5.css:dth:640px){.paper-nav{grid-template-columns:1fr 1fr}}.paper-nav a{display:block;min-height:44px;padding:.9rem 1rem;background:var(--surface);border:1px solid var(--border);border-radius:.6rem;col
IMAGE FILES
website/out/images/coercive-power-card.jpg:    JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/financial-power-card.jpg:   JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/formalized-state-card.jpg:  JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/ideological-power-card.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/judicial-power-card.jpg:    JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/political-power-card.jpg:   JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/productive-power-card.jpg:  JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/coercive-power-card.jpg:    JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/coercive-power.jpg:         JPEG image data, JFIF standard 1.01, resolution (DPI), density 110x110, segment length 16, baseline, precision 8, 935x1210, components 3
website/out/images/financial-power-card.jpg:   JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/financial-power.jpg:        JPEG image data, JFIF standard 1.01, resolution (DPI), density 110x110, segment length 16, baseline, precision 8, 935x1210, components 3
website/out/images/formalized-state-card.jpg:  JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/formalized-state.jpg:       JPEG image data, JFIF standard 1.01, resolution (DPI), density 110x110, segment length 16, baseline, precision 8, 935x1210, components 3
website/out/images/ideological-power-card.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/ideological-power.jpg:      JPEG image data, JFIF standard 1.01, resolution (DPI), density 110x110, segment length 16, baseline, precision 8, 935x1210, components 3
website/out/images/judicial-power-card.jpg:    JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/judicial-power.jpg:         JPEG image data, JFIF standard 1.01, resolution (DPI), density 110x110, segment length 16, baseline, precision 8, 935x1210, components 3
website/out/images/political-power-card.jpg:   JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/political-power.jpg:        JPEG image data, JFIF standard 1.01, resolution (DPI), density 110x110, segment length 16, baseline, precision 8, 935x1210, components 3
website/out/images/productive-power-card.jpg:  JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 640x829, components 3
website/out/images/productive-power.jpg:       JPEG image data, JFIF standard 1.01, resolution (DPI), density 110x110, segment length 16, baseline, precision 8, 935x1210, components 3
website/out/og/coercive-power.png:             PNG image data, 1200 x 630, 16-bit/color RGBA, non-interlaced
website/out/og/financial-power.png:            PNG image data, 1200 x 630, 16-bit/color RGBA, non-interlaced
website/out/og/formalized-state.png:           PNG image data, 1200 x 630, 16-bit/color RGBA, non-interlaced
website/out/og/ideological-power.png:          PNG image data, 1200 x 630, 16-bit/color RGBA, non-interlaced
website/out/og/judicial-power.png:             PNG image data, 1200 x 630, 16-bit/color RGBA, non-interlaced
website/out/og/og-image.png:                   PNG image data, 1200 x 630, 16-bit/color RGBA, non-interlaced
website/out/og/political-power.png:            PNG image data, 1200 x 630, 16-bit/color RGBA, non-interlaced
website/out/og/productive-power.png:           PNG image data, 1200 x 630, 16-bit/color RGBA, non-interlaced
HOMEPAGE IMAGE MARKUP
<img alt="" loading="lazy" width="640" height="828" decoding="async" data-nimg="1" style="color:transparent" src="/images/formalized-state-card.jpg"/>

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -o '.{0,120}font-size:(?:75%|80%|\\.875rem|\\.88rem).{0,120}' website/out/_next/static/css/459226f83420bab5.css; node -e '
const fs=require(\"fs\"),path=require(\"path\"),cheerio=require(\"./website/node_modules/cheerio\");const out=path.resolve(\"website/out\");
for(const rel of [\"index.html\",...fs.readdirSync(path.join(out,\"papers\")).map(x=>"'`papers/${x}/index.html`)]){const p=path.join(out,rel),$=cheerio.load(fs.readFileSync(p,"utf8"));const metas={};$("meta[property],meta[name]").each((i,e)=>{const k=$(e).attr("property")||$(e).attr("name");if(/''^og:|''^twitter:/.test(k))metas[k]=$(e).attr("content")});console.log(JSON.stringify({page:rel,ogTitle:!!metas["og:title"],ogDesc:!!metas["og:description"],ogUrl:metas["og:url"],ogImage:metas["og:image"],twitterCard:metas["twitter:card"],twitterImage:metas["twitter:image"]}));}
const $=cheerio.load(fs.readFileSync(path.join(out,"index.html"),"utf8"));$("img[src*='"\\\"-card.jpg\\\"]\").each((i,e)=>console.log(JSON.stringify({src:"'$(e).attr("src"),loading:$(e).attr("loading"),width:$(e).attr("width"),height:$(e).attr("height"),srcset:$(e).attr("srcset")||null})));
'"'
printf '%s\\n' 'STATIC IMAGE BYTES'; du -k website/out/images/*-card.jpg | sort -n; du -ch website/out/images/*-card.jpg | tail -n 1
printf '%s\\n' 'OG META RAW'; rg -o '<meta (?:property|name)=\"(?:og:image|og:url|twitter:image|twitter:card)\"["'^>]*>'"' website/out/index.html website/out/papers/*/index.html" in /Users/mlong/Documents/Development/the-beast-system
2026-10-22T18:24:39.423941Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
 succeeded in 498ms:
{"page":"papers/coercive-power/index.html","ogTitle":true,"ogDesc":true,"ogUrl":"https://the-beast-system.vercel.app/papers/coercive-power/","ogImage":"https://the-beast-system.vercel.app/og/coercive-power.png","twitterCard":"summary_large_image","twitterImage":"https://the-beast-system.vercel.app/og/coercive-power.png"}
{"page":"papers/financial-power/index.html","ogTitle":true,"ogDesc":true,"ogUrl":"https://the-beast-system.vercel.app/papers/financial-power/","ogImage":"https://the-beast-system.vercel.app/og/financial-power.png","twitterCard":"summary_large_image","twitterImage":"https://the-beast-system.vercel.app/og/financial-power.png"}
{"page":"papers/formalized-state/index.html","ogTitle":true,"ogDesc":true,"ogUrl":"https://the-beast-system.vercel.app/papers/formalized-state/","ogImage":"https://the-beast-system.vercel.app/og/formalized-state.png","twitterCard":"summary_large_image","twitterImage":"https://the-beast-system.vercel.app/og/formalized-state.png"}
{"page":"papers/ideological-power/index.html","ogTitle":true,"ogDesc":true,"ogUrl":"https://the-beast-system.vercel.app/papers/ideological-power/","ogImage":"https://the-beast-system.vercel.app/og/ideological-power.png","twitterCard":"summary_large_image","twitterImage":"https://the-beast-system.vercel.app/og/ideological-power.png"}
{"page":"papers/judicial-power/index.html","ogTitle":true,"ogDesc":true,"ogUrl":"https://the-beast-system.vercel.app/papers/judicial-power/","ogImage":"https://the-beast-system.vercel.app/og/judicial-power.png","twitterCard":"summary_large_image","twitterImage":"https://the-beast-system.vercel.app/og/judicial-power.png"}
{"page":"papers/political-power/index.html","ogTitle":true,"ogDesc":true,"ogUrl":"https://the-beast-system.vercel.app/papers/political-power/","ogImage":"https://the-beast-system.vercel.app/og/political-power.png","twitterCard":"summary_large_image","twitterImage":"https://the-beast-system.vercel.app/og/political-power.png"}
{"page":"papers/productive-power/index.html","ogTitle":true,"ogDesc":true,"ogUrl":"https://the-beast-system.vercel.app/papers/productive-power/","ogImage":"https://the-beast-system.vercel.app/og/productive-power.png","twitterCard":"summary_large_image","twitterImage":"https://the-beast-system.vercel.app/og/productive-power.png"}
{"src":"/images/financial-power-card.jpg","loading":"lazy","width":"640","height":"828","srcset":null}
{"src":"/images/political-power-card.jpg","loading":"lazy","width":"640","height":"828","srcset":null}
{"src":"/images/judicial-power-card.jpg","loading":"lazy","width":"640","height":"828","srcset":null}
{"src":"/images/ideological-power-card.jpg","loading":"lazy","width":"640","height":"828","srcset":null}
{"src":"/images/coercive-power-card.jpg","loading":"lazy","width":"640","height":"828","srcset":null}
{"src":"/images/productive-power-card.jpg","loading":"lazy","width":"640","height":"828","srcset":null}
{"src":"/images/formalized-state-card.jpg","loading":"lazy","width":"640","height":"828","srcset":null}
STATIC IMAGE BYTES
128	website/out/images/coercive-power-card.jpg
128	website/out/images/financial-power-card.jpg
128	website/out/images/formalized-state-card.jpg
128	website/out/images/ideological-power-card.jpg
128	website/out/images/judicial-power-card.jpg
128	website/out/images/political-power-card.jpg
128	website/out/images/productive-power-card.jpg
896K	total
OG META RAW
website/out/index.html:<meta property="og:url" content="https://the-beast-system.vercel.app/"/>
website/out/index.html:<meta property="og:image" content="https://the-beast-system.vercel.app/og/og-image.png"/>
website/out/index.html:<meta name="twitter:card" content="summary_large_image"/>
website/out/index.html:<meta name="twitter:image" content="https://the-beast-system.vercel.app/og/og-image.png"/>
website/out/papers/financial-power/index.html:<meta property="og:url" content="https://the-beast-system.vercel.app/papers/financial-power/"/>
website/out/papers/financial-power/index.html:<meta property="og:image" content="https://the-beast-system.vercel.app/og/financial-power.png"/>
website/out/papers/financial-power/index.html:<meta name="twitter:card" content="summary_large_image"/>
website/out/papers/financial-power/index.html:<meta name="twitter:image" content="https://the-beast-system.vercel.app/og/financial-power.png"/>
website/out/papers/judicial-power/index.html:<meta property="og:url" content="https://the-beast-system.vercel.app/papers/judicial-power/"/>
website/out/papers/judicial-power/index.html:<meta property="og:image" content="https://the-beast-system.vercel.app/og/judicial-power.png"/>
website/out/papers/judicial-power/index.html:<meta name="twitter:card" content="summary_large_image"/>
website/out/papers/judicial-power/index.html:<meta name="twitter:image" content="https://the-beast-system.vercel.app/og/judicial-power.png"/>
website/out/papers/political-power/index.html:<meta property="og:url" content="https://the-beast-system.vercel.app/papers/political-power/"/>
website/out/papers/political-power/index.html:<meta property="og:image" content="https://the-beast-system.vercel.app/og/political-power.png"/>
website/out/papers/political-power/index.html:<meta name="twitter:card" content="summary_large_image"/>
website/out/papers/political-power/index.html:<meta name="twitter:image" content="https://the-beast-system.vercel.app/og/political-power.png"/>
website/out/papers/productive-power/index.html:<meta property="og:url" content="https://the-beast-system.vercel.app/papers/productive-power/"/>
website/out/papers/productive-power/index.html:<meta property="og:image" content="https://the-beast-system.vercel.app/og/productive-power.png"/>
website/out/papers/productive-power/index.html:<meta name="twitter:card" content="summary_large_image"/>
website/out/papers/productive-power/index.html:<meta name="twitter:image" content="https://the-beast-system.vercel.app/og/productive-power.png"/>
website/out/papers/ideological-power/index.html:<meta property="og:url" content="https://the-beast-system.vercel.app/papers/ideological-power/"/>
website/out/papers/ideological-power/index.html:<meta property="og:image" content="https://the-beast-system.vercel.app/og/ideological-power.png"/>
website/out/papers/ideological-power/index.html:<meta name="twitter:card" content="summary_large_image"/>
website/out/papers/ideological-power/index.html:<meta name="twitter:image" content="https://the-beast-system.vercel.app/og/ideological-power.png"/>
website/out/papers/coercive-power/index.html:<meta property="og:url" content="https://the-beast-system.vercel.app/papers/coercive-power/"/>
website/out/papers/coercive-power/index.html:<meta property="og:image" content="https://the-beast-system.vercel.app/og/coercive-power.png"/>
website/out/papers/coercive-power/index.html:<meta name="twitter:card" content="summary_large_image"/>
website/out/papers/coercive-power/index.html:<meta name="twitter:image" content="https://the-beast-system.vercel.app/og/coercive-power.png"/>
website/out/papers/formalized-state/index.html:<meta property="og:url" content="https://the-beast-system.vercel.app/papers/formalized-state/"/>
website/out/papers/formalized-state/index.html:<meta property="og:image" content="https://the-beast-system.vercel.app/og/formalized-state.png"/>
website/out/papers/formalized-state/index.html:<meta name="twitter:card" content="summary_large_image"/>
website/out/papers/formalized-state/index.html:<meta name="twitter:image" content="https://the-beast-system.vercel.app/og/formalized-state.png"/>

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "cd website && node -e 'const k=require(\"katex\");for(const t of [\"\\\\href{javascript:alert(1)}{x}\",\"\\\\href{data:text/html,<svg onload=alert(1)>}{x}\",\"\\\\htmlClass{evil\\\\\\\" onclick=\\\\\\\"alert(1)}{x}\"]){console.log(t);console.log(k.renderToString(t,{trust:true,throwOnError:false}))}'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
\href{javascript:alert(1)}{x}
<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi href="javascript:alert(1)">x</mi></mrow><annotation encoding="application/x-tex">\href{javascript:alert(1)}{x}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.4306em;"></span><a href="javascript:alert(1)"><span class="mord mathnormal">x</span></a></span></span></span>
\href{data:text/html,<svg onload=alert(1)>}{x}
<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi href="data:text/html,&lt;svg onload=alert(1)&gt;">x</mi></mrow><annotation encoding="application/x-tex">\href{data:text/html,&lt;svg onload=alert(1)&gt;}{x}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.4306em;"></span><a href="data:text/html,&lt;svg onload=alert(1)&gt;"><span class="mord mathnormal">x</span></a></span></span></span>
\htmlClass{evil\" onclick=\"alert(1)}{x}
LaTeX-incompatible input and strict mode is set to 'warn': HTML extension is disabled on strict mode [htmlExtension]
<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">\htmlClass{evil\&quot; onclick=\&quot;alert(1)}{x}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.4306em;"></span><span class="enclosing evil\&quot; onclick=\&quot;alert(1)"><span class="mord mathnormal">x</span></span></span></span></span>

2026-10-22T18:24:53.316930Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "node -e '
const fs=require(\"fs\"),path=require(\"path\"),cheerio=require(\"./website/node_modules/cheerio\");const root=path.resolve(\"website/out\"),files=[\"index.html\",...fs.readdirSync(path.join(root,\"papers\")).map(x=>"'`papers/${x}/index.html`)];let missing=[];
function resolve(url,base){const u=new URL(url,"https://local.test/"+base);if(u.origin!=="https://local.test")return null;let p=decodeURIComponent(u.pathname);let target=path.join(root,p);if(p.endsWith("/"))target=path.join(target,"index.html");else if(!path.extname(p)){if(fs.existsSync(path.join(target,"index.html")))target=path.join(target,"index.html")}return target}
for(const rel of files){const raw=fs.readFileSync(path.join(root,rel),"utf8"),$=cheerio.load(raw),ids=new Map();$("[id]").each((i,e)=>{const x=$(e).attr("id");ids.set(x,(ids.get(x)||0)+1)});for(const [id,n] of ids)if(n>1)missing.push({rel,duplicateId:id,n});$("[href],[src]").each((i,e)=>{for(const a of ["href","src"]){const v=$(e).attr(a);if(!v||v.startsWith("#")||/''^(?:https?:|mailto:|tel:)/.test(v))continue;const target=resolve(v,rel);if(target&&!fs.existsSync(target))missing.push({rel,tag:e.tagName,attr:a,url:v,target:path.relative(root,target)})}});}
console.log("resolutionIssues",JSON.stringify(missing));
for(const id of ["eq:margin","eq:necessity","eq:U","eq:aggregation-gap","eq:integration","eq:overlap"]){for(const rel of files){const $=cheerio.load(fs.readFileSync(path.join(root,rel),"utf8"));const nId=$("[id]").filter((i,e)=>$(e).attr("id")===id).length,nHref=$("a[href]").filter((i,e)=>$(e).attr("href")===`#${id}`).length;if(nId||nHref)console.log(JSON.stringify({id,page:rel,targets:nId,links:nHref}));}}
for(const rel of files){const $=cheerio.load(fs.readFileSync(path.join(root,rel),"utf8"));const p=$(".paper-content");const dangerous=[];p.find("script,iframe,object,embed,form,input,button").each((i,e)=>dangerous.push(e.tagName));p.find("*").each((i,e)=>{for(const [k,v]of Object.entries(e.attribs||{})){if(/''^on/i.test(k)||((k==="href"||k==="src"||k==="xlink:href")&&/''^'"\\\\s*(?:javascript|vbscript|data):/i.test(v)))dangerous.push("'`${e.tagName}:${k}`)}});console.log(JSON.stringify({page:rel,paperDangerous:dangerous,small:p.find("small").length,emptyAnchors:p.find("a[href]").filter((i,e)=>!$(e).text().trim()&&!$(e).find("img,svg").length).length}));}
'"'
printf '%s\\n' 'CSS ASSET CHECK'; node -e 'const fs=require(\"fs\"),path=require(\"path\");for(const f of fs.readdirSync(\"website/out/_next/static/css\")){const p=path.join(\"website/out/_next/static/css\",f),s=fs.readFileSync(p,\"utf8\");for(const m of s.matchAll(/url\\((["'^)]+)'"\\)/g)){const u=m[1].replace(/[\"'\"']/g,\"\");if("'!u.startsWith("data:")){const t=path.resolve(path.dirname(p),u);if(!fs.existsSync(t))console.log(f,u,t)}}}'"'" in /Users/mlong/Documents/Development/the-beast-system
 exited 1 in 0ms:
zsh:9: unmatched "

2026-10-22T18:25:35.850664Z ERROR codex_models_manager::manager: failed to renew cache TTL: missing field `base_instructions` at line 139 column 5
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "node -e '
const fs=require(\"fs\"),path=require(\"path\"),cheerio=require(\"./website/node_modules/cheerio\");const root=path.resolve(\"website/out\"),files=[\"index.html\",...fs.readdirSync(path.join(root,\"papers\")).map(x=>"'`papers/${x}/index.html`)];let issues=[];
function resolve(url,base){const u=new URL(url,"https://local.test/"+base);if(u.origin!=="https://local.test")return null;let p=decodeURIComponent(u.pathname);let target=path.join(root,p);if(p.endsWith("/"))target=path.join(target,"index.html");else if(!path.extname(p)&&fs.existsSync(path.join(target,"index.html")))target=path.join(target,"index.html");return target}
for(const rel of files){const raw=fs.readFileSync(path.join(root,rel),"utf8"),$=cheerio.load(raw),ids=new Map();$("[id]").each((i,e)=>{const x=$(e).attr("id");ids.set(x,(ids.get(x)||0)+1)});for(const [id,n] of ids)if(n>1)issues.push({rel,duplicateId:id,n});$("[href],[src]").each((i,e)=>{for(const a of ["href","src"]){const v=$(e).attr(a);if(!v||v.startsWith("#")||/''^(?:https?:|mailto:|tel:)/.test(v))continue;const target=resolve(v,rel);if(target&&!fs.existsSync(target))issues.push({rel,tag:e.tagName,attr:a,url:v,target:path.relative(root,target)})}})}
console.log("resolutionIssues",JSON.stringify(issues));
for(const id of ["eq:margin","eq:necessity","eq:U","eq:aggregation-gap","eq:integration","eq:overlap"]){for(const rel of files){const $=cheerio.load(fs.readFileSync(path.join(root,rel),"utf8"));const nId=$("[id]").filter((i,e)=>$(e).attr("id")===id).length,nHref=$("a[href]").filter((i,e)=>$(e).attr("href")===`#${id}`).length;if(nId||nHref)console.log(JSON.stringify({id,page:rel,targets:nId,links:nHref}))}}
for(const rel of files){const $=cheerio.load(fs.readFileSync(path.join(root,rel),"utf8")),p=$(".paper-content"),dangerous=[];p.find("script,iframe,object,embed,form,input,button").each((i,e)=>dangerous.push(e.tagName));p.find("*").each((i,e)=>{for(const [k,v]of Object.entries(e.attribs||{})){if(/''^on/i.test(k)||((k==="href"||k==="src"||k==="xlink:href")&&/''^'"\\\\s*(?:javascript|vbscript|data):/i.test(v)))dangerous.push("'`${e.tagName}:${k}`)}});console.log(JSON.stringify({page:rel,paperDangerous:dangerous,small:p.find("small").length,emptyAnchors:p.find("a[href]").filter((i,e)=>!$(e).text().trim()&&!$(e).find("img,svg").length).length}))}
'"'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 3638ms:
resolutionIssues []
{"id":"eq:margin","page":"papers/coercive-power/index.html","targets":1,"links":1}
{"id":"eq:necessity","page":"papers/coercive-power/index.html","targets":1,"links":2}
{"id":"eq:U","page":"papers/coercive-power/index.html","targets":1,"links":1}
{"id":"eq:U","page":"papers/political-power/index.html","targets":1,"links":0}
{"id":"eq:aggregation-gap","page":"papers/financial-power/index.html","targets":1,"links":1}
{"id":"eq:integration","page":"papers/ideological-power/index.html","targets":1,"links":1}
{"id":"eq:overlap","page":"papers/political-power/index.html","targets":1,"links":2}
{"page":"index.html","paperDangerous":[],"small":0,"emptyAnchors":0}
{"page":"papers/coercive-power/index.html","paperDangerous":[],"small":0,"emptyAnchors":0}
{"page":"papers/financial-power/index.html","paperDangerous":[],"small":0,"emptyAnchors":0}
{"page":"papers/formalized-state/index.html","paperDangerous":[],"small":0,"emptyAnchors":0}
{"page":"papers/ideological-power/index.html","paperDangerous":[],"small":0,"emptyAnchors":0}
{"page":"papers/judicial-power/index.html","paperDangerous":[],"small":0,"emptyAnchors":0}
{"page":"papers/political-power/index.html","paperDangerous":[],"small":0,"emptyAnchors":0}
{"page":"papers/productive-power/index.html","paperDangerous":[],"small":0,"emptyAnchors":0}

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "wc -l website/out/index.html website/out/papers/*/index.html website/out/_next/static/css/*.css; rg -n -m1 '<semantics>' website/out/papers/financial-power/index.html; rg -n -m1 'id=\"eq:margin\"' website/out/papers/coercive-power/index.html; rg -n -m1 'id=\"eq:aggregation-gap\"' website/out/papers/financial-power/index.html; rg -n -m1 'id=\"eq:integration\"' website/out/papers/ideological-power/index.html; rg -n -m1 'id=\"eq:overlap\"' website/out/papers/political-power/index.html" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
       0 website/out/index.html
     563 website/out/papers/coercive-power/index.html
     542 website/out/papers/financial-power/index.html
     920 website/out/papers/formalized-state/index.html
     641 website/out/papers/ideological-power/index.html
     516 website/out/papers/judicial-power/index.html
     706 website/out/papers/political-power/index.html
     732 website/out/papers/productive-power/index.html
       2 website/out/_next/static/css/459226f83420bab5.css
       0 website/out/_next/static/css/f4ff6fba389ef1b6.css
    4622 total
3:<p>This paper is the first of seven Parts of a series whose thesis is that the ideology of governance changes while its institutional functions remain. The series follows the framework of Largo (2026), which models a polity as a directed multiplex network whose layers record distinct mechanisms of constraint, and which asks when concentration and coordination across those layers turn into unaccountable domination. The series uses six pillars: financial power&nbsp;<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="sans-serif">F</mi></mrow><annotation encoding="application/x-tex">\mathsf{F}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6944em;"></span><span class="mord mathsf">F</span></span></span></span> (who controls the resources), political power&nbsp;<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="sans-serif">P</mi></mrow><annotation encoding="application/x-tex">\mathsf{P}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6944em;"></span><span class="mord mathsf">P</span></span></span></span> (who makes the laws), judicial power&nbsp;<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="sans-serif">J</mi></mrow><annotation encoding="application/x-tex">\mathsf{J}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6944em;"></span><span class="mord mathsf">J</span></span></span></span> (who interprets them), ideological power&nbsp;<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="sans-serif">I</mi></mrow><annotation encoding="application/x-tex">\mathsf{I}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6944em;"></span><span class="mord mathsf">I</span></span></span></span> (who shapes beliefs), coercive power&nbsp;<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="sans-serif">C</mi></mrow><annotation encoding="application/x-tex">\mathsf{C}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6944em;"></span><span class="mord mathsf">C</span></span></span></span> (who enforces the rules), and productive power&nbsp;<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="sans-serif">W</mi></mrow><annotation encoding="application/x-tex">\mathsf{W}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6944em;"></span><span class="mord mathsf" style="margin-right:0.0139em;">W</span></span></span></span> (who produces the wealth that sustains everything). <a class="xpart" href="/papers/formalized-state/">Part VII</a> (<a href="/papers/formalized-state/">Long 2026b</a>) proves the general claim, called Proposition&nbsp;A, that every functioning governance system contains all six functions and the dependencies among them, and it proves that this structural necessity does not imply Proposition&nbsp;B, the contingent and measurable claim that the functions have been captured by a coalition that escapes independent accountability.</p>
25:<p class="thm-head"><span class="thm-label">Definition 2.4</span><span class="thm-name">Sanction regime and deterrence margin</span></p><p>Consider agents <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>i</mi><mo>∈</mo><mi>N</mi><mo>=</mo><mo stretchy="false">{</mo><mn>1</mn><mo separator="true">,</mo><mo>…</mo><mo separator="true">,</mo><mi>n</mi><mo stretchy="false">}</mo></mrow><annotation encoding="application/x-tex">i \in N = \{1,\dots,n\}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6986em;vertical-align:-0.0391em;"></span><span class="mord mathnormal">i</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.109em;">N</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">{</span><span class="mord">1</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="minner">…</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord mathnormal">n</span><span class="mclose">}</span></span></span></span> who in each period <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>t</mi></mrow><annotation encoding="application/x-tex">t</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6151em;"></span><span class="mord mathnormal">t</span></span></span></span> choose <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>v</mi><mrow><mi>i</mi><mo separator="true">,</mo><mi>t</mi></mrow></msub><mo>∈</mo><mo stretchy="false">{</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo stretchy="false">}</mo></mrow><annotation encoding="application/x-tex">v_{i,t} \in \{0,1\}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.8252em;vertical-align:-0.2861em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0359em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">i</span><span class="mpunct mtight">,</span><span class="mord mathnormal mtight">t</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">{</span><span class="mord">0</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">1</span><span class="mclose">}</span></span></span></span>, where <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>v</mi><mrow><mi>i</mi><mo separator="true">,</mo><mi>t</mi></mrow></msub><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">v_{i,t} = 1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.7167em;vertical-align:-0.2861em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0359em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">i</span><span class="mpunct mtight">,</span><span class="mord mathnormal mtight">t</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.6444em;"></span><span class="mord">1</span></span></span></span> means violating a given rule. Let <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>σ</mi></mrow><annotation encoding="application/x-tex">\sigma</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.4306em;"></span><span class="mord mathnormal" style="margin-right:0.0359em;">σ</span></span></span></span> be a strategy profile and <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>h</mi><mi>t</mi></msub></mrow><annotation encoding="application/x-tex">h_t</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.8444em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">h</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span> a history. For <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>v</mi><mo>∈</mo><mo stretchy="false">{</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo stretchy="false">}</mo></mrow><annotation encoding="application/x-tex">v \in \{0,1\}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.5782em;vertical-align:-0.0391em;"></span><span class="mord mathnormal" style="margin-right:0.0359em;">v</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">{</span><span class="mord">0</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">1</span><span class="mclose">}</span></span></span></span> let <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>W</mi><mi>i</mi></msub><mo stretchy="false">(</mo><msub><mi>h</mi><mi>t</mi></msub><mo separator="true">,</mo><mi>v</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">W_i(h_t, v)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.1389em;">W</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">h</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord mathnormal" style="margin-right:0.0359em;">v</span><span class="mclose">)</span></span></span></span> be <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>i</mi></mrow><annotation encoding="application/x-tex">i</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6595em;"></span><span class="mord mathnormal">i</span></span></span></span>’s expected discounted payoff from period <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>t</mi></mrow><annotation encoding="application/x-tex">t</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6151em;"></span><span class="mord mathnormal">t</span></span></span></span> onward, excluding the current temptation term, when <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>i</mi></mrow><annotation encoding="application/x-tex">i</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6595em;"></span><span class="mord mathnormal">i</span></span></span></span> chooses <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>v</mi></mrow><annotation encoding="application/x-tex">v</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.4306em;"></span><span class="mord mathnormal" style="margin-right:0.0359em;">v</span></span></span></span> at <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mi>t</mi><mo separator="true">,</mo><msub><mi>h</mi><mi>t</mi></msub><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(t,h_t)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord mathnormal">t</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">h</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span>, follows <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>σ</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">\sigma_i</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0359em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span> thereafter, and the other agents follow <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>σ</mi><mrow><mo>−</mo><mi>i</mi></mrow></msub></mrow><annotation encoding="application/x-tex">\sigma_{-i}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6389em;vertical-align:-0.2083em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0359em;">σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathnormal mtight">i</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2083em;"><span></span></span></span></span></span></span></span></span></span> throughout. The <em>deterrence margin</em> faced by <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>i</mi></mrow><annotation encoding="application/x-tex">i</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6595em;"></span><span class="mord mathnormal">i</span></span></span></span> at <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mi>t</mi><mo separator="true">,</mo><msub><mi>h</mi><mi>t</mi></msub><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(t,h_t)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord mathnormal">t</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">h</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span> is <div class="math-display" id="eq:margin"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable width="100%"><mtr><mtd width="50%"></mtd><mtd><mrow><msub><mi>d</mi><mrow><mi>i</mi><mo separator="true">,</mo><mi>t</mi></mrow></msub><mo>=</mo><msub><mi>W</mi><mi>i</mi></msub><mo stretchy="false">(</mo><msub><mi>h</mi><mi>t</mi></msub><mo separator="true">,</mo><mn>0</mn><mo stretchy="false">)</mo><mo>−</mo><msub><mi>W</mi><mi>i</mi></msub><mo stretchy="false">(</mo><msub><mi>h</mi><mi>t</mi></msub><mo separator="true">,</mo><mn>1</mn><mo stretchy="false">)</mo><mo separator="true">,</mo></mrow></mtd><mtd width="50%"></mtd><mtd><mtext>(2)</mtext></mtd></mtr></mtable><annotation encoding="application/x-tex">d_{i,t} = W_i(h_t, 0) - W_i(h_t, 1), \tag{2}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.9805em;vertical-align:-0.2861em;"></span><span class="mord"><span class="mord mathnormal">d</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">i</span><span class="mpunct mtight">,</span><span class="mord mathnormal mtight">t</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.1389em;">W</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">h</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">0</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.1389em;">W</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">h</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">1</span><span class="mclose">)</span><span class="mpunct">,</span></span><span class="katex-tag"><span class="katex-strut" style="height:1.0361em;vertical-align:-0.2861em;"></span><span class="mord text"><span class="mord">(</span><span class="mord"><span class="mord">2</span></span><span class="mord">)</span></span></span></span></span></span></div> with discount factor <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>δ</mi><mo>∈</mo><mo stretchy="false">[</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">\delta \in [0,1)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.7335em;vertical-align:-0.0391em;"></span><span class="mord mathnormal" style="margin-right:0.0379em;">δ</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">[</span><span class="mord">0</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">1</span><span class="mclose">)</span></span></span></span>. The <em>sanction regime</em> of <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>σ</mi></mrow><annotation encoding="application/x-tex">\sigma</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.4306em;"></span><span class="mord mathnormal" style="margin-right:0.0359em;">σ</span></span></span></span> is the map <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mi>i</mi><mo separator="true">,</mo><msub><mi>h</mi><mi>t</mi></msub><mo stretchy="false">)</mo><mo>↦</mo><msub><mi>d</mi><mrow><mi>i</mi><mo separator="true">,</mo><mi>t</mi></mrow></msub></mrow><annotation encoding="application/x-tex">(i, h_t) \mapsto d_{i,t}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord mathnormal">i</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">h</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">↦</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.9805em;vertical-align:-0.2861em;"></span><span class="mord"><span class="mord mathnormal">d</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">i</span><span class="mpunct mtight">,</span><span class="mord mathnormal mtight">t</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span></span></span></span>. The regime is <em>trivial</em> if <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>d</mi><mrow><mi>i</mi><mo separator="true">,</mo><mi>t</mi></mrow></msub><mo>≤</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">d_{i,t} \le 0</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.9805em;vertical-align:-0.2861em;"></span><span class="mord"><span class="mord mathnormal">d</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">i</span><span class="mpunct mtight">,</span><span class="mord mathnormal mtight">t</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.6444em;"></span><span class="mord">0</span></span></span></span> at every reachable node.</p>
35:<p class="thm-head"><span class="thm-label">Proposition 2.5</span><span class="thm-name">Aggregation gap</span></p><p><em>Let the financial pillar consist of subdomains <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>k</mi><mo>=</mo><mn>1</mn><mo separator="true">,</mo><mo>…</mo><mo separator="true">,</mo><mi>K</mi></mrow><annotation encoding="application/x-tex">k=1,\dots,K</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6944em;"></span><span class="mord mathnormal" style="margin-right:0.0315em;">k</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.8778em;vertical-align:-0.1944em;"></span><span class="mord">1</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="minner">…</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord mathnormal" style="margin-right:0.0715em;">K</span></span></span></span> with weights <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>β</mi><mi>k</mi></msub><mo>≥</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">\beta_k\geq 0</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0528em;">β</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361em;"><span style="top:-2.55em;margin-left:-0.0528em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≥</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.6444em;"></span><span class="mord">0</span></span></span></span>, <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mo>∑</mo><mi>k</mi></msub><msub><mi>β</mi><mi>k</mi></msub><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">\sum_k\beta_k=1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1.0497em;vertical-align:-0.2997em;"></span><span class="mop"><span class="mop op-symbol small-op" style="position:relative;top:0em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.1864em;"><span style="top:-2.4003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2997em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0528em;">β</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361em;"><span style="top:-2.55em;margin-left:-0.0528em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.6444em;"></span><span class="mord">1</span></span></span></span>, and control-share vectors <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mi>s</mi><mi>k</mi></msup><mo>=</mo><mo stretchy="false">(</mo><msubsup><mi>s</mi><mi>i</mi><mi>k</mi></msubsup><msub><mo stretchy="false">)</mo><mrow><mi>i</mi><mo>∈</mo><mi>N</mi></mrow></msub></mrow><annotation encoding="application/x-tex">s^{k}=(s^{k}_i)_{i\in N}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.8491em;"></span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8491em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1.1078em;vertical-align:-0.2587em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8491em;"><span style="top:-2.4413em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2587em;"><span></span></span></span></span></span></span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3283em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">i</span><span class="mrel mtight">∈</span><span class="mord mathnormal mtight" style="margin-right:0.109em;">N</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.1774em;"><span></span></span></span></span></span></span></span></span></span>, each summing to one. Define the aggregate share <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mover accent="true"><mi>s</mi><mo>ˉ</mo></mover><mi>i</mi></msub><mo>=</mo><msub><mo>∑</mo><mi>k</mi></msub><msub><mi>β</mi><mi>k</mi></msub><msubsup><mi>s</mi><mi>i</mi><mi>k</mi></msubsup></mrow><annotation encoding="application/x-tex">\bar s_i=\sum_k\beta_k s^{k}_i</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.7178em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord katex-accent"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.5678em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord mathnormal">s</span></span><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="left:-0.1944em;"><span class="mord">ˉ</span></span></span></span></span></span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1.1488em;vertical-align:-0.2997em;"></span><span class="mop"><span class="mop op-symbol small-op" style="position:relative;top:0em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.1864em;"><span style="top:-2.4003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2997em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0528em;">β</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361em;"><span style="top:-2.55em;margin-left:-0.0528em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8491em;"><span style="top:-2.4413em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2587em;"><span></span></span></span></span></span></span></span></span></span>. Then <div class="math-display" id="eq:aggregation-gap"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable width="100%"><mtr><mtd width="50%"></mtd><mtd><mrow><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>K</mi></munderover><msub><mi>β</mi><mi>k</mi></msub><mi>H</mi><mo stretchy="false">(</mo><msup><mi>s</mi><mi>k</mi></msup><mo stretchy="false">)</mo><mo>−</mo><mi>H</mi><mo stretchy="false">(</mo><mover accent="true"><mi>s</mi><mo>ˉ</mo></mover><mo stretchy="false">)</mo><mo>=</mo><munder><mo>∑</mo><mrow><mi>i</mi><mo>∈</mo><mi>N</mi></mrow></munder><msub><mrow><mi mathvariant="normal">Var</mi><mo>⁡</mo></mrow><mi>β</mi></msub><mo fence="true" stretchy="true" minsize="1.2em" maxsize="1.2em">(</mo><msubsup><mi>s</mi><mi>i</mi><mo lspace="0em" rspace="0em">⋅</mo></msubsup><mo fence="true" stretchy="true" minsize="1.2em" maxsize="1.2em">)</mo><mo>≥</mo><mn>0</mn><mo separator="true">,</mo></mrow></mtd><mtd width="50%"></mtd><mtd><mtext>(2)</mtext></mtd></mtr></mtable><annotation encoding="application/x-tex">\sum_{k=1}^{K}\beta_k H(s^{k})-H(\bar s)=\sum_{i\in N}\operatorname{Var}_\beta\bigl(s^{\cdot}_i\bigr)\geq 0, \tag{2}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:3.1304em;vertical-align:-1.3021em;"></span><span class="mop op-limits"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.8283em;"><span style="top:-1.8479em;margin-left:0em;"><span class="pstrut" style="height:3.05em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span><span class="mrel mtight">=</span><span class="mord mtight">1</span></span></span></span><span style="top:-3.05em;"><span class="pstrut" style="height:3.05em;"></span><span><span class="mop op-symbol large-op">∑</span></span></span><span style="top:-4.3em;margin-left:0em;"><span class="pstrut" style="height:3.05em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right:0.0715em;">K</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:1.3021em;"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0528em;">β</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361em;"><span style="top:-2.55em;margin-left:-0.0528em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mord mathnormal" style="margin-right:0.0813em;">H</span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8991em;"><span style="top:-3.113em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span></span></span></span></span></span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.0813em;">H</span><span class="mopen">(</span><span class="mord katex-accent"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.5678em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord mathnormal">s</span></span><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="left:-0.1944em;"><span class="mord">ˉ</span></span></span></span></span></span></span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:2.3717em;vertical-align:-1.3217em;"></span><span class="mop op-limits"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.05em;"><span style="top:-1.8557em;margin-left:0em;"><span class="pstrut" style="height:3.05em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">i</span><span class="mrel mtight">∈</span><span class="mord mathnormal mtight" style="margin-right:0.109em;">N</span></span></span></span><span style="top:-3.05em;"><span class="pstrut" style="height:3.05em;"></span><span><span class="mop op-symbol large-op">∑</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:1.3217em;"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mop"><span class="mop"><span class="mord mathrm">Var</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361em;"><span style="top:-2.55em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0528em;">β</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span><span class="mopen"><span class="delimsizing size1">(</span></span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.7241em;"><span style="top:-2.453em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span><span style="top:-3.113em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">⋅</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.247em;"><span></span></span></span></span></span></span><span class="mclose"><span class="delimsizing size1">)</span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≥</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.8389em;vertical-align:-0.1944em;"></span><span class="mord">0</span><span class="mpunct">,</span></span><span class="katex-tag"><span class="katex-strut" style="height:3.15em;vertical-align:-1.3217em;"></span><span class="mord text"><span class="mord">(</span><span class="mord"><span class="mord">2</span></span><span class="mord">)</span></span></span></span></span></span></div> where <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mrow><mi mathvariant="normal">Var</mi><mo>⁡</mo></mrow><mi>β</mi></msub><mo stretchy="false">(</mo><msubsup><mi>s</mi><mi>i</mi><mo lspace="0em" rspace="0em">⋅</mo></msubsup><mo stretchy="false">)</mo><mo>=</mo><msub><mo>∑</mo><mi>k</mi></msub><msub><mi>β</mi><mi>k</mi></msub><mo stretchy="false">(</mo><msubsup><mi>s</mi><mi>i</mi><mi>k</mi></msubsup><mo>−</mo><msub><mover accent="true"><mi>s</mi><mo>ˉ</mo></mover><mi>i</mi></msub><msup><mo stretchy="false">)</mo><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">\operatorname{Var}_\beta(s^{\cdot}_i)=\sum_k\beta_k(s^{k}_i-\bar s_i)^2</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1.0361em;vertical-align:-0.2861em;"></span><span class="mop"><span class="mop"><span class="mord mathrm">Var</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361em;"><span style="top:-2.55em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0528em;">β</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.6741em;"><span style="top:-2.4413em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">⋅</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2587em;"><span></span></span></span></span></span></span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1.1488em;vertical-align:-0.2997em;"></span><span class="mop"><span class="mop op-symbol small-op" style="position:relative;top:0em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.1864em;"><span style="top:-2.4003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2997em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0528em;">β</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361em;"><span style="top:-2.55em;margin-left:-0.0528em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8491em;"><span style="top:-2.4413em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right:0.0315em;">k</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2587em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1.0641em;vertical-align:-0.25em;"></span><span class="mord"><span class="mord katex-accent"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.5678em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord mathnormal">s</span></span><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="left:-0.1944em;"><span class="mord">ˉ</span></span></span></span></span></span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span> is the <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>β</mi></mrow><annotation encoding="application/x-tex">\beta</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="mord mathnormal" style="margin-right:0.0528em;">β</span></span></span></span>-weighted variance of actor <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>i</mi></mrow><annotation encoding="application/x-tex">i</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6595em;"></span><span class="mord mathnormal">i</span></span></span></span>’s share across subdomains. Equality holds if and only if every actor holds the same share in every subdomain of positive weight.</em></p>
13:<p>Integration across pillars is a separate quantity from concentration within them. Cross-pillar integration <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>C</mi><mrow><mi>m</mi><mi>n</mi><mo separator="true">,</mo><mi>t</mi></mrow></msub><mo>∈</mo><mo stretchy="false">[</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo stretchy="false">]</mo></mrow><annotation encoding="application/x-tex">C_{mn,t}\in[0,1]</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.9694em;vertical-align:-0.2861em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0715em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:-0.0715em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">mn</span><span class="mpunct mtight">,</span><span class="mord mathnormal mtight">t</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">[</span><span class="mord">0</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">1</span><span class="mclose">]</span></span></span></span> measures how far one coalition commands appointments, budgets, sanctions or agenda in both <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>m</mi></mrow><annotation encoding="application/x-tex">m</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.4306em;"></span><span class="mord mathnormal">m</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span>, and the integration statistic is <div class="math-display" id="eq:integration"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable width="100%"><mtr><mtd width="50%"></mtd><mtd><mrow><msub><mi mathvariant="script">I</mi><mi>t</mi></msub><mo>=</mo><mfrac><mn>2</mn><mrow><mi>M</mi><mo stretchy="false">(</mo><mi>M</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mfrac><munder><mo>∑</mo><mrow><mi>m</mi><mo>&lt;</mo><mi>n</mi></mrow></munder><msub><mi>C</mi><mrow><mi>m</mi><mi>n</mi><mo separator="true">,</mo><mi>t</mi></mrow></msub><mo>=</mo><mfrac><mn>1</mn><mn>15</mn></mfrac><munder><mo>∑</mo><mrow><mi>m</mi><mo>&lt;</mo><mi>n</mi></mrow></munder><msub><mi>C</mi><mrow><mi>m</mi><mi>n</mi><mo separator="true">,</mo><mi>t</mi></mrow></msub><mi mathvariant="normal">.</mi></mrow></mtd><mtd width="50%"></mtd><mtd><mtext>(1)</mtext></mtd></mtr></mtable><annotation encoding="application/x-tex">\mathcal{I}_t=\frac{2}{M(M-1)}\sum_{m&lt;n} C_{mn,t}=\frac{1}{15}\sum_{m&lt;n} C_{mn,t}. \tag{1}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.8333em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathcal" style="margin-right:0.0738em;">I</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:-0.0738em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:2.5988em;vertical-align:-1.2774em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.3214em;"><span style="top:-2.314em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.109em;">M</span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.109em;">M</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mord">1</span><span class="mclose">)</span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.677em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.936em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mop op-limits"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.05em;"><span style="top:-1.9em;margin-left:0em;"><span class="pstrut" style="height:3.05em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">m</span><span class="mrel mtight">&lt;</span><span class="mord mathnormal mtight">n</span></span></span></span><span style="top:-3.05em;"><span class="pstrut" style="height:3.05em;"></span><span><span class="mop op-symbol large-op">∑</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:1.2774em;"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0715em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:-0.0715em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">mn</span><span class="mpunct mtight">,</span><span class="mord mathnormal mtight">t</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:2.5988em;vertical-align:-1.2774em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.3214em;"><span style="top:-2.314em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord">15</span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.677em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.686em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mop op-limits"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.05em;"><span style="top:-1.9em;margin-left:0em;"><span class="pstrut" style="height:3.05em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">m</span><span class="mrel mtight">&lt;</span><span class="mord mathnormal mtight">n</span></span></span></span><span style="top:-3.05em;"><span class="pstrut" style="height:3.05em;"></span><span><span class="mop op-symbol large-op">∑</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:1.2774em;"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0715em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:-0.0715em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">mn</span><span class="mpunct mtight">,</span><span class="mord mathnormal mtight">t</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span><span class="mord">.</span></span><span class="katex-tag"><span class="katex-strut" style="height:2.5988em;vertical-align:-1.2774em;"></span><span class="mord text"><span class="mord">(</span><span class="mord"><span class="mord">1</span></span><span class="mord">)</span></span></span></span></span></span></div> A capture link <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mi>i</mi><mo>→</mo><mi>j</mi><mo separator="true">,</mo><mi>m</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(i\to j,m)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord mathnormal">i</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">→</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.0572em;">j</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord mathnormal">m</span><span class="mclose">)</span></span></span></span> is influence that meets three conditions: privileged access or discretion, a resulting weakening of applicable accountability or contestability, and material evidence tying the asymmetry to an institutional output. In the aggregate state vector <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>x</mi><mi>t</mi></msub><mo>=</mo><mo stretchy="false">(</mo><msub><mi>F</mi><mi>t</mi></msub><mo separator="true">,</mo><msub><mi>P</mi><mi>t</mi></msub><mo separator="true">,</mo><msub><mi>J</mi><mi>t</mi></msub><mo separator="true">,</mo><msubsup><mi>I</mi><mi>t</mi><mrow><mi>c</mi><mi>a</mi><mi>p</mi></mrow></msubsup><mo separator="true">,</mo><msub><mi>C</mi><mi>t</mi></msub><mo separator="true">,</mo><msub><mi>W</mi><mi>t</mi></msub><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">x_t=(F_t,P_t,J_t,I^{cap}_t,C_t,W_t)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1.0323em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal" style="margin-right:0.1389em;">F</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.1389em;">P</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0962em;">J</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:-0.0962em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0785em;">I</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.7823em;"><span style="top:-2.4542em;margin-left:-0.0785em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span><span style="top:-3.1809em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">c</span><span class="mord mathnormal mtight">a</span><span class="mord mathnormal mtight">p</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2458em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0715em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:-0.0715em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.1389em;">W</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span> the ideological capacity is written <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msubsup><mi>I</mi><mi>t</mi><mrow><mi>c</mi><mi>a</mi><mi>p</mi></mrow></msubsup></mrow><annotation encoding="application/x-tex">I^{cap}_t</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1.0281em;vertical-align:-0.2458em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0785em;">I</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.7823em;"><span style="top:-2.4542em;margin-left:-0.0785em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span><span style="top:-3.1809em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">c</span><span class="mord mathnormal mtight">a</span><span class="mord mathnormal mtight">p</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2458em;"><span></span></span></span></span></span></span></span></span></span>. The pillar label is the sans-serif <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="sans-serif">I</mi></mrow><annotation encoding="application/x-tex">\mathsf{I}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6944em;"></span><span class="mord mathsf">I</span></span></span></span> and the integration statistic is the calligraphic <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi mathvariant="script">I</mi><mi>t</mi></msub></mrow><annotation encoding="application/x-tex">\mathcal{I}_t</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.8333em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathcal" style="margin-right:0.0738em;">I</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.2806em;"><span style="top:-2.55em;margin-left:-0.0738em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">t</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span>; the two are never interchanged.</p>
443:<p>The appointment channel acquires testable content under one explicit candidate, the coalition-overlap measure. Let <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="script">S</mi></mrow><annotation encoding="application/x-tex">\mathcal{S}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6833em;"></span><span class="mord mathcal" style="margin-right:0.075em;">S</span></span></span></span> be a preregistered list of coherent coalitions, groups such as parties, factions, or dynasties that can issue joint directives. For <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>S</mi><mo>∈</mo><mi mathvariant="script">S</mi></mrow><annotation encoding="application/x-tex">S\in\mathcal{S}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.7224em;vertical-align:-0.0391em;"></span><span class="mord mathnormal" style="margin-right:0.0576em;">S</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.6833em;"></span><span class="mord mathcal" style="margin-right:0.075em;">S</span></span></span></span> let <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mi>s</mi><mi mathvariant="sans-serif">P</mi></msup><mo stretchy="false">(</mo><mi>S</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">s^{\mathsf{P}}(S)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1.0991em;vertical-align:-0.25em;"></span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8491em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathsf mtight">P</span></span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.0576em;">S</span><span class="mclose">)</span></span></span></span> be the Shapley-Shubik share of the bloc player <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>p</mi><mi>S</mi></msub></mrow><annotation encoding="application/x-tex">p_S</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3283em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0576em;">S</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span> in the quotient game on <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>N</mi><mi>S</mi></msub><mo>=</mo><mo stretchy="false">(</mo><mi>N</mi><mo>∖</mo><mi>S</mi><mo stretchy="false">)</mo><mo>∪</mo><mo stretchy="false">{</mo><msub><mi>p</mi><mi>S</mi></msub><mo stretchy="false">}</mo></mrow><annotation encoding="application/x-tex">N_S=(N\setminus S)\cup\{p_S\}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.8333em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.109em;">N</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3283em;"><span style="top:-2.55em;margin-left:-0.109em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0576em;">S</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.109em;">N</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">∖</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.0576em;">S</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">∪</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">{</span><span class="mord"><span class="mord mathnormal">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3283em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0576em;">S</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">}</span></span></span></span>, whose winning coalitions are defined for <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>T</mi><mo>⊆</mo><mi>N</mi><mo>∖</mo><mi>S</mi></mrow><annotation encoding="application/x-tex">T\subseteq N\setminus S</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.8193em;vertical-align:-0.136em;"></span><span class="mord mathnormal" style="margin-right:0.1389em;">T</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">⊆</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.109em;">N</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">∖</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.0576em;">S</span></span></span></span> by <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>T</mi><mo>∈</mo><msub><mi mathvariant="script">W</mi><mi>S</mi></msub></mrow><annotation encoding="application/x-tex">T\in\mathcal{W}_S</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.7224em;vertical-align:-0.0391em;"></span><span class="mord mathnormal" style="margin-right:0.1389em;">T</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.8333em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathcal" style="margin-right:0.0822em;">W</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3283em;"><span style="top:-2.55em;margin-left:-0.0822em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0576em;">S</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span> if and only if <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>T</mi><mo>∈</mo><mi mathvariant="script">W</mi></mrow><annotation encoding="application/x-tex">T\in\mathcal{W}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.7224em;vertical-align:-0.0391em;"></span><span class="mord mathnormal" style="margin-right:0.1389em;">T</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.6833em;"></span><span class="mord mathcal" style="margin-right:0.0822em;">W</span></span></span></span>, and <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>T</mi><mo>∪</mo><mo stretchy="false">{</mo><msub><mi>p</mi><mi>S</mi></msub><mo stretchy="false">}</mo><mo>∈</mo><msub><mi mathvariant="script">W</mi><mi>S</mi></msub></mrow><annotation encoding="application/x-tex">T\cup\{p_S\}\in\mathcal{W}_S</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.1389em;">T</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">∪</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">{</span><span class="mord"><span class="mord mathnormal">p</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3283em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0576em;">S</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">}</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.8333em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathcal" style="margin-right:0.0822em;">W</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3283em;"><span style="top:-2.55em;margin-left:-0.0822em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.0576em;">S</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span> if and only if <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>T</mi><mo>∪</mo><mi>S</mi><mo>∈</mo><mi mathvariant="script">W</mi></mrow><annotation encoding="application/x-tex">T\cup S\in\mathcal{W}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.1389em;">T</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">∪</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.7224em;vertical-align:-0.0391em;"></span><span class="mord mathnormal" style="margin-right:0.0576em;">S</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.6833em;"></span><span class="mord mathcal" style="margin-right:0.0822em;">W</span></span></span></span>. This bloc share is not in general the sum of the members’ separate shares; in the Iranian example of Table&nbsp;<a class="xref" href="#tab:examples">2</a> the two councils hold <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mi mathvariant="normal">/</mi><mn>6</mn><mo>+</mo><mn>1</mn><mi mathvariant="normal">/</mi><mn>6</mn></mrow><annotation encoding="application/x-tex">1/6+1/6</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">1/6</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">1/6</span></span></span></span> separately and <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mi mathvariant="normal">/</mi><mn>2</mn></mrow><annotation encoding="application/x-tex">1/2</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">1/2</span></span></span></span> as a bloc. Let <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>κ</mi><mi mathvariant="normal">ℓ</mi></msub><mo stretchy="false">(</mo><mi>S</mi><mo stretchy="false">)</mo><mo>∈</mo><mo stretchy="false">[</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo stretchy="false">]</mo></mrow><annotation encoding="application/x-tex">\kappa_\ell(S)\in[0,1]</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord"><span class="mord mathnormal">κ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight">ℓ</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.0576em;">S</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">[</span><span class="mord">0</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">1</span><span class="mclose">]</span></span></span></span> be the share of decision-relevant control in pillar <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">ℓ</mi></mrow><annotation encoding="application/x-tex">\ell</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6944em;"></span><span class="mord">ℓ</span></span></span></span> that is exercised in accordance with the directives of <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.0576em;">S</span></span></span></span>, and set <div class="math-display" id="eq:overlap"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mtable width="100%"><mtr><mtd width="50%"></mtd><mtd><mrow><msubsup><mi>C</mi><mrow><mi mathvariant="sans-serif">P</mi><mi mathvariant="normal">ℓ</mi></mrow><mrow><mi mathvariant="normal">o</mi><mi mathvariant="normal">v</mi></mrow></msubsup><mo>=</mo><munder><mrow><mi>max</mi><mo>⁡</mo></mrow><mrow><mi>S</mi><mo>∈</mo><mi mathvariant="script">S</mi></mrow></munder><mi>min</mi><mo>⁡</mo><mo stretchy="false">{</mo><msup><mi>s</mi><mi mathvariant="sans-serif">P</mi></msup><mo stretchy="false">(</mo><mi>S</mi><mo stretchy="false">)</mo><mo separator="true">,</mo><msub><mi>κ</mi><mi mathvariant="normal">ℓ</mi></msub><mo stretchy="false">(</mo><mi>S</mi><mo stretchy="false">)</mo><mo stretchy="false">}</mo><mi mathvariant="normal">.</mi></mrow></mtd><mtd width="50%"></mtd><mtd><mtext>(2)</mtext></mtd></mtr></mtable><annotation encoding="application/x-tex">C^{\mathrm{ov}}_{\mathsf{P}\ell}=\max_{S\in\mathcal{S}}\min\{s^{\mathsf{P}}(S),\kappa_\ell(S)\}. \tag{2}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.9614em;vertical-align:-0.247em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.0715em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.7144em;"><span style="top:-2.453em;margin-left:-0.0715em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathsf mtight">P</span><span class="mord mtight">ℓ</span></span></span></span><span style="top:-3.113em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight"><span class="mord mathrm mtight" style="margin-right:0.0139em;">ov</span></span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.247em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:1.6708em;vertical-align:-0.7717em;"></span><span class="mop op-limits"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.4306em;"><span style="top:-2.3557em;margin-left:0em;"><span class="pstrut" style="height:3em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right:0.0576em;">S</span><span class="mrel mtight">∈</span><span class="mord mathcal mtight" style="margin-right:0.075em;">S</span></span></span></span><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span><span class="mop">max</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.7717em;"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mop">min</span><span class="mopen">{</span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8991em;"><span style="top:-3.113em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathsf mtight">P</span></span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.0576em;">S</span><span class="mclose">)</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">κ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight">ℓ</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.0576em;">S</span><span class="mclose">)}</span><span class="mord">.</span></span><span class="katex-tag"><span class="katex-strut" style="height:1.6708em;vertical-align:-0.7717em;"></span><span class="mord text"><span class="mord">(</span><span class="mord"><span class="mord">2</span></span><span class="mord">)</span></span></span></span></span></span></div> The candidate lies in <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">[</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo stretchy="false">]</mo></mrow><annotation encoding="application/x-tex">[0,1]</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">[</span><span class="mord">0</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">1</span><span class="mclose">]</span></span></span></span>, equals one when a single coalition holds all rule-making control and commands all of pillar <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">ℓ</mi></mrow><annotation encoding="application/x-tex">\ell</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.6944em;"></span><span class="mord">ℓ</span></span></span></span>, and equals zero when no listed coalition has a positive share in both.</p>

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "node -e 'const fs=require(\"fs\"),c=require(\"./website/node_modules/cheerio\"),"'$=c.load(fs.readFileSync("website/out/papers/judicial-power/index.html","utf8"));const a=$("a[href*='"\\\"doi.org\\\"]\");console.log(JSON.stringify({doiLinks:a.length,emptyDoi:a.filter((i,e)=>"'!$(e).text().trim()).length,sample:a.slice(0,3).map((i,e)=>({text:$(e).text(),href:$(e).attr("href")})).get()}));'"' ; stat -f '%z %N' website/out/images/*-card.jpg | awk '{s+="'$1} END {printf "cardTotalBytes=%d cardTotalKiB=%.1f'"\\n\",s,s/1024}' ; node -e 'const x=[185594,148502,239640,169824,148547,170562,173019]; console.log("'`maxGzipBytes=${Math.max(...x)} maxGzipKiB=${(Math.max(...x)/1024).toFixed(1)}`)'"'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 163ms:
{"doiLinks":50,"emptyDoi":0,"sample":[{"text":"doi:10.1017/cbo9780511819858","href":"https://doi.org/10.1017/cbo9780511819858"},{"text":"doi:10.1093/oso/9780195076707.001.0001","href":"https://doi.org/10.1093/oso/9780195076707.001.0001"},{"text":"doi:10.4159/9780674020863","href":"https://doi.org/10.4159/9780674020863"}]}
cardTotalBytes=680174 cardTotalKiB=664.2
maxGzipBytes=239640 maxGzipKiB=234.0

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "command -v chromium || command -v chromium-browser || command -v google-chrome || command -v playwright || true; find website/node_modules -maxdepth 2 \\( -name 'playwright' -o -name 'puppeteer' -o -name 'happy-dom' \\) -type d -print | head" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
codex
The generated-artifact audit is clean: all internal assets and fragment links resolve, all 4,023 math expressions retain a one-to-one `<semantics>/<annotation>` structure, all exported paper bodies contain zero unsafe elements/protocols, and the judicial page has 50 named DOI links with zero empty anchors. The largest paper is 234.0 KiB gzip, within the stated 235 KiB ceiling.
hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "for spec in 'website/out/papers/financial-power/index.html:<semantics>' 'website/out/papers/coercive-power/index.html:id=\"eq:margin\"' 'website/out/papers/coercive-power/index.html:id=\"eq:necessity\"' 'website/out/papers/coercive-power/index.html:id=\"eq:U\"' 'website/out/papers/financial-power/index.html:id=\"eq:aggregation-gap\"' 'website/out/papers/ideological-power/index.html:id=\"eq:integration\"' 'website/out/papers/political-power/index.html:id=\"eq:overlap\"' 'website/out/papers/judicial-power/index.html:doi:10.' 'website/out/index.html:og/og-image.png' 'website/out/index.html:-card.jpg' 'website/out/_next/static/css/459226f83420bab5.css:box-sizing:border-box' 'website/out/_next/static/css/459226f83420bab5.css:min-height:44px' 'website/out/_next/static/css/459226f83420bab5.css:font-size:.875rem'; do f="'${spec%%:*}; p=${spec#*:}; n=$(rg -n -m1 "$p" "$f" | cut -d: -f1); printf '"'%s:%s %s\\n' \""'$f" "$n" "$p"; done' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
website/out/papers/financial-power/index.html:3 <semantics>
website/out/papers/coercive-power/index.html:25 id="eq:margin"
website/out/papers/coercive-power/index.html:57 id="eq:necessity"
website/out/papers/coercive-power/index.html:9 id="eq:U"
website/out/papers/financial-power/index.html:35 id="eq:aggregation-gap"
website/out/papers/ideological-power/index.html:13 id="eq:integration"
website/out/papers/political-power/index.html:443 id="eq:overlap"
website/out/papers/judicial-power/index.html:414 doi:10.
website/out/index.html:1 og/og-image.png
website/out/index.html:reviews/website-codex-review-round-2.md
reviews/website-codex-review-round-1.md -card.jpg
website/out/_next/static/css/459226f83420bab5.css:3 box-sizing:border-box
website/out/_next/static/css/459226f83420bab5.css:3 min-height:44px
website/out/_next/static/css/459226f83420bab5.css:3 font-size:.875rem

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba website/components/PillarDiagram.tsx; nl -ba website/scripts/extract-macros.mjs; wc -c website/lib/macros.json; node -e 'const x=require(\"./website/lib/macros.json\"); console.log({macroCount:Object.keys(x).length,suspicious:Object.entries(x).filter(([k,v])=>/\\\\\\\\(?:href|url|html|includegraphics)|javascript:|data:/i.test(k+\" \"+v))})'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	// Six pillars as nodes with the dependency arcs of the Formalized State (Part VII):
     2	// production feeds every other function; allocation feeds production; the other four feed allocation.
     3	const NODES = [
     4	  { id: 'F', label: 'Financial', x: 300, y: 250, color: '#d9b25f' },
     5	  { id: 'W', label: 'Productive', x: 300, y: 450, color: '#4fb286' },
     6	  { id: 'P', label: 'Political', x: 62, y: 210, color: '#e0556a' },
     7	  { id: 'J', label: 'Judicial', x: 538, y: 210, color: '#6f8fe0' },
     8	  { id: 'I', label: 'Ideological', x: 160, y: 62, color: '#b072d8' },
     9	  { id: 'C', label: 'Coercive', x: 440, y: 62, color: '#e8793a' },
    10	];
    11	
    12	const R = 30;
    13	const pos = Object.fromEntries(NODES.map((n) => [n.id, n]));
    14	
    15	function arc(a: string, b: string, bend: number) {
    16	  const A = pos[a];
    17	  const B = pos[b];
    18	  const dx = B.x - A.x;
    19	  const dy = B.y - A.y;
    20	  const d = Math.hypot(dx, dy);
    21	  const ux = dx / d;
    22	  const uy = dy / d;
    23	  const sx = A.x + ux * (R + 2);
    24	  const sy = A.y + uy * (R + 2);
    25	  const ex = B.x - ux * (R + 8);
    26	  const ey = B.y - uy * (R + 8);
    27	  const mx = (sx + ex) / 2 - uy * bend;
    28	  const my = (sy + ey) / 2 + ux * bend;
    29	  return `M${sx.toFixed(1)} ${sy.toFixed(1)} Q${mx.toFixed(1)} ${my.toFixed(1)} ${ex.toFixed(1)} ${ey.toFixed(1)}`;
    30	}
    31	
    32	const FROM_W = [
    33	  ['W', 'P', -55],
    34	  ['W', 'J', 55],
    35	  ['W', 'I', -95],
    36	  ['W', 'C', 95],
    37	] as const;
    38	const INTO_F = [
    39	  ['P', 'F', 0],
    40	  ['J', 'F', 0],
    41	  ['I', 'F', 0],
    42	  ['C', 'F', 0],
    43	] as const;
    44	
    45	export default function PillarDiagram() {
    46	  return (
    47	    <div className="diagram">
    48	      <svg
    49	        viewBox="0 0 600 510"
    50	        role="img"
    51	        aria-label="Diagram of the six pillars of governance as six nodes: financial, political, judicial, ideological, coercive and productive. Productive power feeds each of the other five. Financial power feeds productive power, and the political, judicial, ideological and coercive pillars each feed financial power."
    52	      >
    53	        <defs>
    54	          <marker id="arrow-solid" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    55	            <path d="M0 0L10 5L0 10z" fill="#ec5a72" />
    56	          </marker>
    57	          <marker id="arrow-soft" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    58	            <path d="M0 0L10 5L0 10z" fill="#8d867b" />
    59	          </marker>
    60	          <radialGradient id="node-glow">
    61	            <stop offset="0" stopColor="#ec5a72" stopOpacity="0.18" />
    62	            <stop offset="1" stopColor="#ec5a72" stopOpacity="0" />
    63	          </radialGradient>
    64	        </defs>
    65	        <circle cx="300" cy="250" r="230" fill="url(#node-glow)" />
    66	        <g fill="none" strokeLinecap="round">
    67	          {FROM_W.map(([a, b, bend]) => (
    68	            <path key={a + b} d={arc(a, b, bend)} stroke="#8d867b" strokeWidth="1.5" strokeDasharray="5 4" markerEnd="url(#arrow-soft)" />
    69	          ))}
    70	          <path d={arc('W', 'F', 20)} stroke="#8d867b" strokeWidth="1.5" strokeDasharray="5 4" markerEnd="url(#arrow-soft)" />
    71	          <path d={arc('F', 'W', 20)} stroke="#ec5a72" strokeWidth="2.2" markerEnd="url(#arrow-solid)" />
    72	          {INTO_F.map(([a, b, bend]) => (
    73	            <path key={a + b} d={arc(a, b, bend)} stroke="#ec5a72" strokeWidth="2.2" markerEnd="url(#arrow-solid)" />
    74	          ))}
    75	        </g>
    76	        {NODES.map((n) => (
    77	          <g key={n.id}>
    78	            <circle cx={n.x} cy={n.y} r={R} fill="#14121a" stroke={n.color} strokeWidth="2.5" />
    79	            <text x={n.x} y={n.y + 8} textAnchor="middle" fontSize="26" fontWeight="700" fontFamily="'KaTeX_SansSerif', Inter, sans-serif" fill={n.color}>
    80	              {n.id}
    81	            </text>
    82	            <text
    83	              x={n.id === 'F' ? n.x + R + 10 : n.x}
    84	              y={n.id === 'W' ? n.y + R + 20 : n.id === 'F' ? n.y + 5 : n.y - R - 10}
    85	              textAnchor={n.id === 'F' ? 'start' : 'middle'}
    86	              fontSize="19"
    87	              fontFamily="Inter, sans-serif"
    88	              fill="currentColor"
    89	            >
    90	              {n.label}
    91	            </text>
    92	          </g>
    93	        ))}
    94	      </svg>
    95	    </div>
    96	  );
    97	}
     1	// Step 2: collect every \newcommand, \renewcommand and \DeclareMathOperator from the paper preambles
     2	// into website/lib/macros.json (KaTeX macro map).
     3	import fs from 'node:fs';
     4	import path from 'node:path';
     5	import { SLUGS } from './series.mjs';
     6	
     7	const root = path.resolve(process.argv[2] || '.');
     8	const macros = {};
     9	const seen = {};
    10	const conflicts = [];
    11	
    12	function group(s, i) {
    13	  let d = 0;
    14	  for (let j = i; j < s.length; j++) {
    15	    if (s[j] === '\\') { j++; continue; }
    16	    if (s[j] === '{') d++;
    17	    else if (s[j] === '}' && --d === 0) return j;
    18	  }
    19	  throw new Error('unbalanced');
    20	}
    21	
    22	for (const slug of SLUGS) {
    23	  const tex = fs.readFileSync(path.join(root, 'papers', 'latex', `${slug}.tex`), 'utf8');
    24	  const pre = tex.slice(0, tex.indexOf('\\begin{document}'));
    25	  const re = /\\(newcommand|renewcommand|providecommand|DeclareMathOperator)(\*?)\s*\{?(\\[A-Za-z]+)\}?(\[\d\])?\s*\{/g;
    26	  let m;
    27	  while ((m = re.exec(pre))) {
    28	    const [, kind, star, name, nargs] = m;
    29	    const start = m.index + m[0].length - 1;
    30	    const end = group(pre, start);
    31	    let body = pre.slice(start + 1, end).trim();
    32	    if (kind === 'DeclareMathOperator') body = `\\operatorname${star}{${body}}`;
    33	    (seen[name] ||= new Set()).add(body);
    34	    if (!(name in macros)) macros[name] = body;
    35	    else if (macros[name] !== body) conflicts.push(`${name} (${slug}): ${body} vs ${macros[name]}`);
    36	  }
    37	}
    38	const out = Object.fromEntries(Object.entries(macros).sort());
    39	fs.writeFileSync(path.join(root, 'website', 'lib', 'macros.json'), JSON.stringify(out, null, 2) + '\n');
    40	console.log(`macros: ${Object.keys(out).length} unique names (${conflicts.length} cross-paper redefinitions)`);
    41	for (const c of conflicts) console.log('  conflict', c);
     878 website/lib/macros.json
{ macroCount: 31, suspicious: [] }

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "node -e 'const fs=require(\"fs\"),path=require(\"path\"),c=require(\"./website/node_modules/cheerio\");for(const d of fs.readdirSync(\"website/out/papers\")){const f="'`website/out/papers/${d}/index.html`,$=c.load(fs.readFileSync(f,"utf8"));$("annotation").remove();const t=$(".paper-content").text();const hits=t.match(/'"\\\\\\\\[A-Za-z]+/g)||[];console.log(d,hits.length,[...new Set(hits)].slice(0,10))}'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 563ms:
coercive-power 0 []
financial-power 0 []
formalized-state 0 []
ideological-power 0 []
judicial-power 0 []
political-power 0 []
productive-power 0 []

codex
- All nine Round 1 issues are resolved:
  - KaTeX: all 4,023 expressions retain matching `<semantics>` and `<annotation>` elements; removing annotations leaves zero visible LaTeX commands. [Exported example](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/financial-power/index.html:3>)
  - Equation anchors: matching targets now exist for [`eq:U`](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/coercive-power/index.html:9>), [`eq:margin`](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/coercive-power/index.html:25>), [`eq:necessity`](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/coercive-power/index.html:57>), [`eq:aggregation-gap`](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/financial-power/index.html:35>), [`eq:integration`](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/ideological-power/index.html:13>), and [`eq:overlap`](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/political-power/index.html:443>). No broken fragment links remain.
  - OG images: all eight referenced 1200×630 PNGs exist, and exported metadata uses absolute URLs. [Homepage HTML](</Users/mlong/Documents/Development/the-beast-system/website/out/index.html:1>) [OG image](</Users/mlong/Documents/Development/the-beast-system/website/out/og/og-image.png>)
  - Mobile sizing: generated CSS contains global `border-box` plus 44px minimums for navigation, buttons, cards, TOC links, paper navigation, and the PDF control. [Generated CSS](</Users/mlong/Documents/Development/the-beast-system/website/out/_next/static/css/459226f83420bab5.css:3>)
  - DOI links: the judicial export contains 50 named DOI links and zero empty focusable anchors. [Judicial output](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/judicial-power/index.html:414>)
  - Page weight: the largest paper export is 239,640 bytes gzip, or 234.0 KiB—within the 235 KiB ceiling. [Largest export](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/formalized-state/index.html:3>)
  - Homepage covers: all seven images use lazy-loaded, 640-pixel-wide card renditions rather than full covers. [Homepage output](</Users/mlong/Documents/Development/the-beast-system/website/out/index.html:1>)
  - Typography: app-authored text bottoms out at `0.875rem`/14px; smaller generated KaTeX glyph components and semantic sub/sup elements are not prose. [Generated CSS](</Users/mlong/Documents/Development/the-beast-system/website/out/_next/static/css/459226f83420bab5.css:3>)
- No injection finding under the stated trust model: sanitization precedes compile-time KaTeX rendering, no runtime/user content reaches it, and exported paper bodies contain no executable elements, event attributes, or unsafe URL protocols. `trust: true` would require reconsideration if paper content ever became untrusted.
- No new issue introduced by the fixes was found.

VERDICT: PASS
hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
94,750
- All nine Round 1 issues are resolved:
  - KaTeX: all 4,023 expressions retain matching `<semantics>` and `<annotation>` elements; removing annotations leaves zero visible LaTeX commands. [Exported example](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/financial-power/index.html:3>)
  - Equation anchors: matching targets now exist for [`eq:U`](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/coercive-power/index.html:9>), [`eq:margin`](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/coercive-power/index.html:25>), [`eq:necessity`](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/coercive-power/index.html:57>), [`eq:aggregation-gap`](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/financial-power/index.html:35>), [`eq:integration`](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/ideological-power/index.html:13>), and [`eq:overlap`](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/political-power/index.html:443>). No broken fragment links remain.
  - OG images: all eight referenced 1200×630 PNGs exist, and exported metadata uses absolute URLs. [Homepage HTML](</Users/mlong/Documents/Development/the-beast-system/website/out/index.html:1>) [OG image](</Users/mlong/Documents/Development/the-beast-system/website/out/og/og-image.png>)
  - Mobile sizing: generated CSS contains global `border-box` plus 44px minimums for navigation, buttons, cards, TOC links, paper navigation, and the PDF control. [Generated CSS](</Users/mlong/Documents/Development/the-beast-system/website/out/_next/static/css/459226f83420bab5.css:3>)
  - DOI links: the judicial export contains 50 named DOI links and zero empty focusable anchors. [Judicial output](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/judicial-power/index.html:414>)
  - Page weight: the largest paper export is 239,640 bytes gzip, or 234.0 KiB—within the 235 KiB ceiling. [Largest export](</Users/mlong/Documents/Development/the-beast-system/website/out/papers/formalized-state/index.html:3>)
  - Homepage covers: all seven images use lazy-loaded, 640-pixel-wide card renditions rather than full covers. [Homepage output](</Users/mlong/Documents/Development/the-beast-system/website/out/index.html:1>)
  - Typography: app-authored text bottoms out at `0.875rem`/14px; smaller generated KaTeX glyph components and semantic sub/sup elements are not prose. [Generated CSS](</Users/mlong/Documents/Development/the-beast-system/website/out/_next/static/css/459226f83420bab5.css:3>)
- No injection finding under the stated trust model: sanitization precedes compile-time KaTeX rendering, no runtime/user content reaches it, and exported paper bodies contain no executable elements, event attributes, or unsafe URL protocols. `trust: true` would require reconsideration if paper content ever became untrusted.
- No new issue introduced by the fixes was found.

VERDICT: PASS
