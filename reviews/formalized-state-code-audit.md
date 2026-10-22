---
reviewer: codex (OpenAI) gpt-5.6-sol
type: code-evidence audit
paper: formalized-state
invocation: 2 (final)
date: 2026-10-22T19:14:55Z
note: pytest run by the author outside the sandbox: 335 passed
---
Reading additional input from stdin...
2026-10-22T19:14:55.943878Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
OpenAI Codex v0.145.0
--------
workdir: /Users/mlong/Documents/Development/the-beast-system
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a16509-b1c3-7e83-814b-9ab152316ab2
--------
user
Final audit of the code-evidence appendix of papers/latex/formalized-state.tex (section 'Code evidence', table tab:code, 18 rows). Rows 4, 7, 9, 12 and 16 were reworded after a first audit to claim only what the named tests check. For each of the 18 rows: read the named functions in model/beast_system/ and the named tests in model/tests/, and judge whether the code and tests support the claim in the 'What the code checks' column exactly as now worded. The test suite passes (335 tests) when run outside your sandbox; judge by static inspection. Judge each row SUPPORTS, PARTIAL or NO with one sentence of evidence, and for PARTIAL or NO the exact fix. Do not judge the paper's mathematics. Output a markdown table: Row | Result | Verdict | Evidence | Fix. End with a line COUNTS: SUPPORTS=x PARTIAL=y NO=z.
warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
2026-10-22T19:14:57.469128Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
2026-10-22T19:14:58.430329Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
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
I’ll audit the appendix row-by-row against the exact named implementation functions and tests. I’m using the repository’s recorded context only to locate prior framing, then I’ll base every verdict on the live files.
codex
I’m also applying the code-review skill because this is a source-and-test evidence audit; it will structure the inspection but won’t broaden the task beyond the 18 claims.
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
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

exec
/usr/local/bin/zsh -lc 'rg -n "the-beast-system|formalized-state|Code evidence|tab:code" /Users/mlong/.codex/memories/MEMORY.md' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
75:# Task Group: the-beast-system comparative research-paper setup
77:applies_to: cwd=/Users/mlong/the-beast-system; reuse_rule=project contents and research conclusions must be inspected from the current files; observed planning activity is not a validated paper or published claim.
83:- extensions/skysight/resources/2026-10-22T13-40-00-mOWP-10min-memory-summary.md (cwd=/Users/mlong/the-beast-system, rollout_path=extensions/skysight/resources/2026-10-22T13-40-00-mOWP-10min-memory-summary.md, updated_at=2026-10-22T13:40:00+00:00, thread_id=None, research framing continued; no response or artifact outcome captured) [skysight memory]
84:- extensions/skysight/resources/2026-10-22T13-20-00-YYQx-10min-memory-summary.md (cwd=/Users/mlong/the-beast-system, rollout_path=extensions/skysight/resources/2026-10-22T13-20-00-YYQx-10min-memory-summary.md, updated_at=2026-10-22T13:20:00+00:00, thread_id=None, project and `context` directory created; draft revised) [skysight memory]
88:- `the-beast-system`, `context`, `six-pillars-beast-system-papers`, comparative research, Apple Notes, paper scoping, Parallels error 521
92:- The user created `the-beast-system` and a `context` subdirectory, organized source material, revised a related Apple Notes draft, and began an initial paper-scoping session. Subsequent conceptual questions and “more context” in `six-pillars-beast-system-papers` did not yield a captured research response, source inspection, plan, or artifact. [Task 1] [skysight memory]

exec
/usr/local/bin/zsh -lc 'find .. -name AGENTS.md -print' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 41462ms:
../rustoleum/moldex-site-jss/AGENTS.md
../magneton_work/tax-strategy-dashboard/node_modules/recharts/AGENTS.md
../magneton_work/tax-strategy-dashboard/.next/standalone/AGENTS.md
../magneton_work/tax-strategy-dashboard/AGENTS.md
../magneton_work/arithmetic-positivity-program/website/node_modules/next/AGENTS.md
../magneton_work/arithmetic-positivity-program/website/AGENTS.md
../magneton_work/agentfolio/codex/AGENTS.md
../magneton_work/agentfolio/AGENTS.md
../magneton_work/adelic-polarization-conjecture/website/node_modules/next/AGENTS.md
../magneton_work/riemann-hypothesis-proof/website/node_modules/next/AGENTS.md
../magneton_work/riemann-hypothesis-proof/website/AGENTS.md
../magneton_work/hott-riemann-hypothesis-vol6/website/AGENTS.md
../magneton_work/ai-preprint-forge/AGENTS.md
../MDReader/node_modules/.pnpm/cytoscape@3.34.0/node_modules/cytoscape/AGENTS.md
../MDReader/AGENTS.md
../ai_price_dashboard/AGENTS.md
../copied-reverse-engineer/AGENTS.md
../ai-tui/.external/opencode-ai-tui/opencode/packages/effect-drizzle-sqlite/AGENTS.md
../ai-tui/.external/opencode-ai-tui/opencode/packages/llm/AGENTS.md
../ai-tui/.external/opencode-ai-tui/opencode/packages/app/AGENTS.md
../ai-tui/.external/opencode-ai-tui/opencode/packages/desktop/AGENTS.md
../ai-tui/.external/opencode-ai-tui/opencode/packages/opencode/test/server/AGENTS.md
../ai-tui/.external/opencode-ai-tui/opencode/packages/opencode/test/AGENTS.md
../ai-tui/.external/opencode-ai-tui/opencode/packages/opencode/AGENTS.md
../ai-tui/.external/opencode-ai-tui/opencode/packages/opencode/src/server/routes/instance/httpapi/AGENTS.md
../ai-tui/.external/opencode-ai-tui/opencode/packages/opencode/src/session/llm/AGENTS.md
../ai-tui/.external/opencode-ai-tui/opencode/AGENTS.md
../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/effect-drizzle-sqlite/AGENTS.md
../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/llm/AGENTS.md
../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/app/AGENTS.md
../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/desktop/AGENTS.md
../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/opencode/test/server/AGENTS.md
../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/opencode/test/AGENTS.md
../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/opencode/AGENTS.md
../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/opencode/src/server/routes/instance/httpapi/AGENTS.md
../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/opencode/src/session/llm/AGENTS.md
../ai-tui/.external/opencode-ai-tui-accept/opencode/AGENTS.md
../ai-tui/AGENTS.md
../agenthero-platform/crates/AGENTS.md
../agenthero-platform/node_modules/.pnpm/@supabase+auth-js@2.112.3/node_modules/@supabase/auth-js/AGENTS.md
../agenthero-platform/node_modules/.pnpm/@supabase+realtime-js@2.112.3/node_modules/@supabase/realtime-js/AGENTS.md
../agenthero-platform/node_modules/.pnpm/@supabase+postgrest-js@2.112.3/node_modules/@supabase/postgrest-js/AGENTS.md
../agenthero-platform/node_modules/.pnpm/@supabase+functions-js@2.112.3/node_modules/@supabase/functions-js/AGENTS.md
../agenthero-platform/node_modules/.pnpm/@supabase+storage-js@2.112.3/node_modules/@supabase/storage-js/AGENTS.md
../agenthero-platform/node_modules/.pnpm/@supabase+supabase-js@2.112.3/node_modules/@supabase/supabase-js/AGENTS.md
../agenthero-platform/agenthero/control-plane-web/AGENTS.md
../agenthero-platform/agenthero/apps/AGENTS.md
../agenthero-platform/agenthero/apps/grokrxiv/skills/skills/codex/AGENTS.md
../agenthero-platform/.worktrees/codex-r9/crates/AGENTS.md
../agenthero-platform/.worktrees/codex-r9/agenthero/control-plane-web/AGENTS.md
../agenthero-platform/.worktrees/codex-r9/agenthero/apps/AGENTS.md
../agenthero-platform/.worktrees/codex-r9/agenthero/apps/grokrxiv/skills/skills/codex/AGENTS.md
../agenthero-platform/.worktrees/codex-r9/AGENTS.md
../agenthero-platform/.worktrees/k1-scheduler-fixlist/crates/AGENTS.md
../agenthero-platform/.worktrees/k1-scheduler-fixlist/agenthero/control-plane-web/AGENTS.md
../agenthero-platform/.worktrees/k1-scheduler-fixlist/agenthero/apps/AGENTS.md
../agenthero-platform/.worktrees/k1-scheduler-fixlist/agenthero/apps/grokrxiv/skills/skills/codex/AGENTS.md
../agenthero-platform/.worktrees/k1-scheduler-fixlist/AGENTS.md
../agenthero-platform/.worktrees/batch-27/crates/AGENTS.md
../agenthero-platform/.worktrees/batch-27/node_modules/.pnpm/@supabase+auth-js@2.112.3/node_modules/@supabase/auth-js/AGENTS.md
../agenthero-platform/.worktrees/batch-27/node_modules/.pnpm/@supabase+realtime-js@2.112.3/node_modules/@supabase/realtime-js/AGENTS.md
../agenthero-platform/.worktrees/batch-27/node_modules/.pnpm/@supabase+postgrest-js@2.112.3/node_modules/@supabase/postgrest-js/AGENTS.md
../agenthero-platform/.worktrees/batch-27/node_modules/.pnpm/@supabase+functions-js@2.112.3/node_modules/@supabase/functions-js/AGENTS.md
../agenthero-platform/.worktrees/batch-27/node_modules/.pnpm/@supabase+storage-js@2.112.3/node_modules/@supabase/storage-js/AGENTS.md
../agenthero-platform/.worktrees/batch-27/node_modules/.pnpm/@supabase+supabase-js@2.112.3/node_modules/@supabase/supabase-js/AGENTS.md
../agenthero-platform/.worktrees/batch-27/agenthero/control-plane-web/AGENTS.md
../agenthero-platform/.worktrees/batch-27/agenthero/apps/AGENTS.md
../agenthero-platform/.worktrees/batch-27/agenthero/apps/grokrxiv/skills/skills/codex/AGENTS.md
../agenthero-platform/.worktrees/batch-27/AGENTS.md
../agenthero-platform/AGENTS.md
../agenthero-platform/.superpowers/sdd/2026-09-12-agentapp-v2-part3-integration/task-11ae-ae1-resume-evidence/single-agh-runtime-runs/canonical-ae1-1/catalog-source/grokrxiv/skills/skills/codex/AGENTS.md
../agenthero-platform/.superpowers/sdd/2026-09-12-agentapp-v2-part3-integration/task-11ae-ae1-resume-evidence/single-agh-runtime-runs/canonical-ae1-1/catalog/agenthero/apps/grokrxiv/skills/skills/codex/AGENTS.md
../agenthero-platform/.superpowers/sdd/2026-09-16-agent-owned-git-workflow-plan/market-brief-runs/job-a-install/pre-restage-backup/catalog-source/grokrxiv/skills/skills/codex/AGENTS.md
../agenthero-platform/.superpowers/sdd/2026-09-16-agent-owned-git-workflow-plan/market-brief-runs/job-a-install/pre-restage-backup/catalog-apps/grokrxiv/skills/skills/codex/AGENTS.md
../CatDB/.worktrees/dev/AGENTS.md
../CatDB/AGENTS.md
../CatDB-Web/node_modules/.pnpm/cytoscape@3.34.0/node_modules/cytoscape/AGENTS.md
../yonedarepo/plugins/codex/AGENTS.md
../yonedarepo/.local/stream-c-egress/contribution/AGENTS.md
../yonedarepo/.local/public-source-final-code/fixtures/website/AGENTS.md
../yonedarepo/.local/public-source-final-code/AGENTS.md
../yonedarepo/.local/export-budget-c3433d2/fixtures/website/AGENTS.md
../yonedarepo/.local/export-budget-c3433d2/AGENTS.md
../yonedarepo/.local/submission-export-322ef3f/fixtures/website/AGENTS.md
../yonedarepo/.local/submission-export-322ef3f/AGENTS.md
../yonedarepo/.local/submission-export-48b5618/fixtures/website/AGENTS.md
../yonedarepo/.local/submission-export-48b5618/AGENTS.md
../yonedarepo/.local/public-source-r14-4d4cf2b/fixtures/website/AGENTS.md
../yonedarepo/.local/public-source-r14-4d4cf2b/AGENTS.md
../yonedarepo/.local/export-462f439/fixtures/website/AGENTS.md
../yonedarepo/.local/export-462f439/AGENTS.md
../yonedarepo/.local/public-source-autonomy-13eccb1/fixtures/website/AGENTS.md
../yonedarepo/.local/public-source-autonomy-13eccb1/AGENTS.md
../yonedarepo/.local/submission-publish-48b5618/fixtures/website/AGENTS.md
../yonedarepo/.local/submission-publish-48b5618/AGENTS.md
../yonedarepo/.local/export-comparison-f0f1307/fixtures/website/AGENTS.md
../yonedarepo/.local/export-comparison-f0f1307/AGENTS.md
../yonedarepo/.local/export-autonomy-13eccb1/fixtures/website/AGENTS.md
../yonedarepo/.local/export-autonomy-13eccb1/AGENTS.md
../yonedarepo/.local/submission-export-final-e8cc3f5/fixtures/website/AGENTS.md
../yonedarepo/.local/submission-export-final-e8cc3f5/AGENTS.md
../yonedarepo/.local/public-source-api-r12-3c52f65/fixtures/website/AGENTS.md
../yonedarepo/.local/public-source-api-r12-3c52f65/AGENTS.md
../yonedarepo/.local/public-source-api-r11-ebdac98/fixtures/website/AGENTS.md
../yonedarepo/.local/public-source-api-r11-ebdac98/AGENTS.md
../yonedarepo/.local/export-current-checked-repair-20261013/fixtures/website/AGENTS.md
../yonedarepo/.local/export-current-checked-repair-20261013/AGENTS.md
../yonedarepo/.local/export-simple-workflow-35e2783/fixtures/website/AGENTS.md
../yonedarepo/.local/export-simple-workflow-35e2783/AGENTS.md
../yonedarepo/.local/public-source/fixtures/website/AGENTS.md
../yonedarepo/.local/public-source/AGENTS.md
../yonedarepo/.local/submission-export-fc5126c/fixtures/website/AGENTS.md
../yonedarepo/.local/submission-export-fc5126c/AGENTS.md
../yonedarepo/.local/public-source-api-r9-ef311f6/fixtures/website/AGENTS.md
../yonedarepo/.local/public-source-api-r9-ef311f6/AGENTS.md
../yonedarepo/.local/export-autonomy-0a0eeb5/fixtures/website/AGENTS.md
../yonedarepo/.local/export-autonomy-0a0eeb5/AGENTS.md
../yonedarepo/.local/export-r4-82d900f/fixtures/website/AGENTS.md
../yonedarepo/.local/export-r4-82d900f/AGENTS.md
../yonedarepo/.local/export-final-4555ce9/fixtures/website/AGENTS.md
../yonedarepo/.local/export-final-4555ce9/AGENTS.md
../yonedarepo/.local/layout-fresh-checkout/fixtures/website/AGENTS.md
../yonedarepo/.local/layout-fresh-checkout/AGENTS.md
../yonedarepo/.local/public-source-modern-picker-9a30eca/fixtures/website/AGENTS.md
../yonedarepo/.local/public-source-modern-picker-9a30eca/AGENTS.md
../yonedarepo/.local/comparison-acceptance/calibration/correct/AGENTS.md
../yonedarepo/.local/comparison-acceptance/calibration/bundle/AGENTS.md
../yonedarepo/.local/comparison-acceptance/calibration/missing/AGENTS.md
../yonedarepo/.local/comparison-acceptance/calibration/trim_only/AGENTS.md
../yonedarepo/.local/public-source-final-wave/fixtures/website/AGENTS.md
../yonedarepo/.local/public-source-final-wave/AGENTS.md
../yonedarepo/.local/export-comparison-ebb08f4/fixtures/website/AGENTS.md
../yonedarepo/.local/export-comparison-ebb08f4/AGENTS.md
../yonedarepo/.local/export-autonomy-acbb3b1/fixtures/website/AGENTS.md
../yonedarepo/.local/export-autonomy-acbb3b1/AGENTS.md
../yonedarepo/.local/submission-export-native-final/fixtures/website/AGENTS.md
../yonedarepo/.local/submission-export-native-final/AGENTS.md
../yonedarepo/.local/export-07b3a8f/fixtures/website/AGENTS.md
../yonedarepo/.local/export-07b3a8f/AGENTS.md
../yonedarepo/.local/source-api/hosted-compare/calibration/correct/AGENTS.md
../yonedarepo/.local/source-api/hosted-compare/calibration/bundle/AGENTS.md
../yonedarepo/.local/source-api/hosted-compare/calibration/missing/AGENTS.md
../yonedarepo/.local/source-api/hosted-compare/calibration/trim_only/AGENTS.md
../yonedarepo/.local/export-simple-workflow-final-20261013/fixtures/website/AGENTS.md
../yonedarepo/.local/export-simple-workflow-final-20261013/AGENTS.md
../yonedarepo/.local/platform-acceptance/contribution-0/AGENTS.md
../yonedarepo/.local/platform-acceptance/contribution-1/AGENTS.md
../yonedarepo/.local/platform-acceptance/load-benchmark/contribution-0/AGENTS.md
../yonedarepo/.local/platform-acceptance/load-benchmark/contribution-1/AGENTS.md
../yonedarepo/.local/platform-acceptance/load-benchmark/contribution-4/AGENTS.md
../yonedarepo/.local/platform-acceptance/load-benchmark/contribution-3/AGENTS.md
../yonedarepo/.local/platform-acceptance/load-benchmark/contribution-2/AGENTS.md
../yonedarepo/.local/platform-acceptance/load-benchmark/contribution-5/AGENTS.md
../yonedarepo/.local/platform-acceptance/contribution-2/AGENTS.md
../yonedarepo/.local/platform-acceptance/history/2026-10-13T03-52-17.693Z-repo-367d034ceab238815b06a8ee238b8e78/contribution-0/AGENTS.md
../yonedarepo/.local/platform-acceptance/history/2026-10-13T03-52-17.693Z-repo-367d034ceab238815b06a8ee238b8e78/contribution-1/AGENTS.md
../yonedarepo/.local/platform-acceptance/history/2026-10-13T03-52-17.693Z-repo-367d034ceab238815b06a8ee238b8e78/contribution-2/AGENTS.md
../yonedarepo/.claude/worktrees/agent-a42de161bd00fca20/fixtures/website/AGENTS.md
../yonedarepo/.claude/worktrees/agent-a42de161bd00fca20/AGENTS.md
../yonedarepo/.claude/worktrees/staging/fixtures/website/AGENTS.md
../yonedarepo/.claude/worktrees/staging/AGENTS.md
../yonedarepo/.claude/worktrees/native-p95/fixtures/website/AGENTS.md
../yonedarepo/.claude/worktrees/native-p95/AGENTS.md
../yonedarepo/.claude/worktrees/agent-a00c9e8b324c29ac8/plugins/codex/AGENTS.md
../yonedarepo/.claude/worktrees/agent-a00c9e8b324c29ac8/fixtures/website/AGENTS.md
../yonedarepo/.claude/worktrees/agent-a00c9e8b324c29ac8/AGENTS.md
../yonedarepo/fixtures/website/AGENTS.md
../yonedarepo/AGENTS.md
../MDReader-Web/node_modules/.pnpm/cytoscape@3.34.0/node_modules/cytoscape/AGENTS.md
../MDReader-Web/AGENTS.md
../rad-belden/.local/worktree-retention/shared-domain-77523af/local-evidence/dev017d-evidence/replay-1/linux-source/AGENTS.md
../rad-belden/.local/worktree-retention/shared-domain-77523af/local-evidence/dev017d-evidence/linux-source/AGENTS.md
../rad-belden/.local/products/rad-local-ca8b45cf463b4422/source/AGENTS.md
../rad-belden/.local/products/rad-local-2e25a184d9614055/source/AGENTS.md
../rad-belden/.local/products/rad-local-6ba78c6752a84d81/source/AGENTS.md
../rad-belden/.local/products/rad-local-b8d491e481f443d2/source/AGENTS.md
../rad-belden/.local/products/rad-local-b8d491e481f443d2/update-8d655d8c01794b52a6feb54c3d5511dc/source/AGENTS.md
../rad-belden/.local/products/rad-local-26a1a43bcdba4a55/source/AGENTS.md
../rad-belden/.local/products/rad-local-a6eec87604f347bf/update-e5b2273aea224206a8651f8eddf2cafa/source/AGENTS.md
../rad-belden/.local/products/rad-local-a6eec87604f347bf/update-122a564f7a56421bb514dd0bcabcd9ac/source/AGENTS.md
../rad-belden/.local/products/rad-local-a6eec87604f347bf/source/AGENTS.md
../rad-belden/.local/products/rad-local-fc773c74a4d94855/update-1b16996e2efa4592a8c4344f8aecc731/source/AGENTS.md
../rad-belden/.local/products/rad-local-fc773c74a4d94855/update-15e30e929650433db9179feb12d57cf7/source/AGENTS.md
../rad-belden/.local/products/rad-local-fc773c74a4d94855/update-37f8818aab5845909d7a93265e97f9f9/source/AGENTS.md
../rad-belden/.local/products/rad-local-fc773c74a4d94855/source/AGENTS.md
../rad-belden/.local/products/rad-local-fc773c74a4d94855/update-e1a4eb06137a4e348e4f1151c7c448f2/source/AGENTS.md
../rad-belden/.local/products/rad-local-65988578693b4eb2/source/AGENTS.md
../rad-belden/.local/products/rad-local-429b21e0dfee4937/source/AGENTS.md
../rad-belden/.local/products/rad-local-887bbb82da3e4118/source/AGENTS.md
../rad-belden/.local/products/rad-local-96364f818c654e6b/update-1b796bd08fe24606924234f029e60306/source/AGENTS.md
../rad-belden/.local/products/rad-local-96364f818c654e6b/source/AGENTS.md
../rad-belden/.local/products/rad-local-96364f818c654e6b/update-14f6263e2324486aac57c0cfae11f9e2/source/AGENTS.md
../rad-belden/.local/products/rad-local-96364f818c654e6b/update-db9216e6bc384436b66d94dfc78d0bd8/source/AGENTS.md
../rad-belden/.local/products/rad-local-c309ed6bbc5246b9/source/AGENTS.md
../rad-belden/.local/products/rad-local-4cac6890fe6f49f1/update-d522e15508f445c2b91224c62310bf25/source/AGENTS.md
../rad-belden/.local/products/rad-local-4cac6890fe6f49f1/update-62ec864bbde64e6fb32b7c8d04747ad4/source/AGENTS.md
../rad-belden/.local/products/rad-local-4cac6890fe6f49f1/update-d2e5b79237bc4591a4dc3e6e1c468ed8/source/AGENTS.md
../rad-belden/.local/products/rad-local-4cac6890fe6f49f1/source/AGENTS.md
../rad-belden/.local/products/rad-local-4cac6890fe6f49f1/update-814caeb2583d4734b95f21dba2fde57c/source/AGENTS.md
../rad-belden/.local/products/rad-local-4cac6890fe6f49f1/update-dbe9b85acde44ca185781d7e978c70da/source/AGENTS.md
../rad-belden/.local/products/rad-local-c64fbf8d2a7c41fc/source/AGENTS.md
../rad-belden/.local/products/rad-local-c64fbf8d2a7c41fc/update-80d126d0508f4d0e8f46aefcfa77d7f0/source/AGENTS.md
../rad-belden/.local/products/rad-local-41ed481fc09042e7/source/AGENTS.md
../rad-belden/.local/products/rad-local-8cb0b87be95d4ff1/source/AGENTS.md
../rad-belden/.local/products/rad-local-24420d86c23e4920/update-e53a116fbf3c436a8dd81cee3b7281d2/source/AGENTS.md
../rad-belden/.local/products/rad-local-24420d86c23e4920/update-aa30e58be2bb43ce95833a81755f02da/source/AGENTS.md
../rad-belden/.local/products/rad-local-24420d86c23e4920/update-6ba2b57f38424980a9d61a77074bedd4/source/AGENTS.md
../rad-belden/.local/products/rad-local-24420d86c23e4920/update-64015b4472bc4c24ad9ebddf38dec55c/source/AGENTS.md
../rad-belden/.local/products/rad-local-24420d86c23e4920/source/AGENTS.md
../rad-belden/.local/products/rad-local-24420d86c23e4920/update-9fe51906ab50470093944d36093c6d38/source/AGENTS.md
../rad-belden/.local/products/rad-local-24420d86c23e4920/update-67e077c5ddb84e0f98c2de8e1a08c3a3/source/AGENTS.md
../rad-belden/.local/products/rad-local-24420d86c23e4920/update-f58a1fcebdbf4d158ecd688c649ab82a/source/AGENTS.md
../rad-belden/.local/products/rad-local-24420d86c23e4920/update-74bcba457bb44391925322491b9876a8/source/AGENTS.md
../rad-belden/.local/products/rad-local-24420d86c23e4920/update-d8bce0a369a04eefbb10ae8dadd6d76d/source/AGENTS.md
../rad-belden/.local/products/rad-local-24420d86c23e4920/update-905d6f8f39c04947a67dedffd37a899b/source/AGENTS.md
../rad-belden/.local/products/rad-local-24420d86c23e4920/update-6d8e14dffd7f4a91b74d7293c5e3b3c6/source/AGENTS.md
../rad-belden/.local/products/rad-local-7a307cea767c411b/source/AGENTS.md
../rad-belden/.local/products/rad-local-a33a4e5641c64e0a/source/AGENTS.md
../rad-belden/.local/products/rad-local-5f62b05d76664252/update-c31d39f7398d428bac4cc7e775114ce7/source/AGENTS.md
../rad-belden/.local/products/rad-local-5f62b05d76664252/source/AGENTS.md
../rad-belden/.local/products/rad-local-0c78bdc06ee94649/source/AGENTS.md
../rad-belden/.local/products/rad-local-4745cc4fdf404f17/update-be61a751ded54cfb826050f605a46d40/source/AGENTS.md
../rad-belden/.local/products/rad-local-4745cc4fdf404f17/source/AGENTS.md
../rad-belden/.local/products/rad-local-6677e8f077074feb/source/AGENTS.md
../rad-belden/.local/products/rad-local-6677e8f077074feb/update-2b27a10908db42469fa4b4e2f942d057/source/AGENTS.md
../rad-belden/.local/products/rad-local-e9a51b7d287549a5/source/AGENTS.md
../rad-belden/.local/products/rad-local-2a566c2f63d14d84/update-f5b45897debe4eed98f4cb31637bb36b/source/AGENTS.md
../rad-belden/.local/products/rad-local-2a566c2f63d14d84/update-570981c2627a455ea6b9d768fa2ec7dc/source/AGENTS.md
../rad-belden/.local/products/rad-local-2a566c2f63d14d84/source/AGENTS.md
../rad-belden/.local/products/rad-local-2a566c2f63d14d84/update-1572eeb69a8445479df44f4ff86e6254/source/AGENTS.md
../rad-belden/.local/products/rad-local-2a566c2f63d14d84/update-625dda91d2e94568965c9d193dd6b67b/source/AGENTS.md
../rad-belden/.local/products/rad-local-2a566c2f63d14d84/update-f68d2488486545b8b32f61bdf52816db/source/AGENTS.md
../rad-belden/.local/products/rad-local-2a566c2f63d14d84/update-491681335099466ca0819dbc687fd1c4/source/AGENTS.md
../rad-belden/.local/products/rad-local-2a566c2f63d14d84/update-ade81d015f564f9c89dccc68f1719b75/source/AGENTS.md
../rad-belden/.local/products/rad-local-2a566c2f63d14d84/update-eb4b5d38b4284e229e4b808406b5c966/source/AGENTS.md
../rad-belden/.local/products/rad-local-356663f12c39416e/source/AGENTS.md
../rad-belden/.local/products/rad-local-f1bad1be7a5d4d0c/update-3bd824d409ef43ad96f0f61accb3d6dc/source/AGENTS.md
../rad-belden/.local/products/rad-local-f1bad1be7a5d4d0c/update-9ed1e236d8ea4f3398dc4cf03fccd708/source/AGENTS.md
../rad-belden/.local/products/rad-local-f1bad1be7a5d4d0c/source/AGENTS.md
../rad-belden/.local/products/rad-local-f1bad1be7a5d4d0c/update-587969f689024e7c9a9870a7657a3a4b/source/AGENTS.md
../rad-belden/.local/products/rad-local-f1bad1be7a5d4d0c/update-7c233033495b4e269025eaa141e8cc15/source/AGENTS.md
../rad-belden/.local/products/rad-local-f1bad1be7a5d4d0c/update-873a8dc8360c4eb9ae56ad7d041ff997/source/AGENTS.md
../rad-belden/.local/products/rad-local-f1bad1be7a5d4d0c/update-9e5c4265e30545859f6224d8deed9026/source/AGENTS.md
../rad-belden/.local/products/rad-local-f1bad1be7a5d4d0c/update-abf74e6bdc8e49eaa1becc6a3f0b571b/source/AGENTS.md
../rad-belden/.local/products/rad-local-6667388763d848ed/update-28d3253c165842bd9c03b5f95b068bc3/source/AGENTS.md
../rad-belden/.local/products/rad-local-6667388763d848ed/source/AGENTS.md
../rad-belden/.local/products/rad-local-43b10997095e4fd3/source/AGENTS.md
../rad-belden/.local/products/rad-local-e3615c86863d41fc/source/AGENTS.md
../rad-belden/.local/products/rad-local-e3615c86863d41fc/update-b6eb84b9a9a3439db0f111000337d148/source/AGENTS.md
../rad-belden/.local/products/rad-local-e3615c86863d41fc/update-81f878e826864fff838fc71d7b3fbace/source/AGENTS.md
../rad-belden/.local/products/rad-local-fe77b48a17ca4049/source/AGENTS.md
../rad-belden/.local/products/rad-local-6343a76954a24a06/source/AGENTS.md
../rad-belden/.local/products/rad-local-734a90000a5f4f53/source/AGENTS.md
../rad-belden/.local/products/rad-local-883d80d36c7c450c/source/AGENTS.md
../rad-belden/.local/products/rad-local-5aa93bc12199480f/source/AGENTS.md
../rad-belden/.local/products/rad-local-02ba806c8466481b/source/AGENTS.md
../rad-belden/.local/products/rad-local-f31e87ae28454541/source/AGENTS.md
../rad-belden/.local/products/rad-local-fab42eaca70e4302/source/AGENTS.md
../rad-belden/.local/products/rad-local-feb652658fb84256/update-120cd62005674c248aad69bc8e5c1c4b/source/AGENTS.md
../rad-belden/.local/products/rad-local-feb652658fb84256/source/AGENTS.md
../rad-belden/.local/products/rad-local-feb652658fb84256/update-06a89a0fa9ea4716ba8de7748e423b04/source/AGENTS.md
../rad-belden/.local/products/rad-local-feb652658fb84256/update-c420f6bb374241439e60d99787c72616/source/AGENTS.md
../rad-belden/.local/products/rad-local-9b1c9ea880354a9b/source/AGENTS.md
../rad-belden/.local/products/rad-local-4c1421c923654ccf/source/AGENTS.md
../rad-belden/.local/products/rad-local-ab3bb1dbab2643c9/source/AGENTS.md
../rad-belden/.local/products/rad-local-4ddab18284b246d7/source/AGENTS.md
../rad-belden/.local/products/rad-local-e1b46c90bde14b9e/source/AGENTS.md
../rad-belden/.local/products/rad-local-ba68a45f59aa4187/source/AGENTS.md
../rad-belden/.local/products/rad-local-4add10c53e6d48f4/update-b211886c7e0144e093e6e1a61e7f5f39/source/AGENTS.md
../rad-belden/.local/products/rad-local-4add10c53e6d48f4/source/AGENTS.md
../rad-belden/.local/products/rad-local-4add10c53e6d48f4/update-dbfe736f785e47a68d06da01af9ade5e/source/AGENTS.md
../rad-belden/.local/products/rad-local-4add10c53e6d48f4/update-ed089aba047a4814ae20db421b75c24e/source/AGENTS.md
../rad-belden/.local/products/rad-local-b8efe2ebe02b48f9/source/AGENTS.md
../rad-belden/.local/products/rad-local-6a887bf283b94124/source/AGENTS.md
../rad-belden/.local/products/rad-local-8b99a2c787604887/source/AGENTS.md
../rad-belden/.local/products/rad-local-8b99a2c787604887/update-51988065662b48ad8f7aa9f11433f6a8/source/AGENTS.md
../rad-belden/.local/products/rad-local-8b99a2c787604887/update-99a021a8a0bf486f86702775460fb531/source/AGENTS.md
../rad-belden/.local/products/rad-local-ad668d175f4a446e/source/AGENTS.md
../rad-belden/.local/products/rad-local-cd3ea3395bc945b9/source/AGENTS.md
../rad-belden/.local/products/rad-local-110c40c6490544f9/update-f071d5148877495bbd9e1d3935888665/source/AGENTS.md
../rad-belden/.local/products/rad-local-110c40c6490544f9/update-af09aaa98e0c433a9c648e97af9294d3/source/AGENTS.md
../rad-belden/.local/products/rad-local-110c40c6490544f9/source/AGENTS.md
../rad-belden/.local/products/rad-local-110c40c6490544f9/update-dfb7c13f7d2340d8b5eb83998a2706bf/source/AGENTS.md
../rad-belden/.local/products/rad-local-110c40c6490544f9/update-798fa974a0b04e85acdd0da6b7a0bb0e/source/AGENTS.md
../rad-belden/.local/products/rad-local-110c40c6490544f9/update-a7149dfd45084aafa953135b0c21189b/source/AGENTS.md
../rad-belden/.local/products/rad-local-05e6c47759344f3e/source/AGENTS.md
../rad-belden/.local/products/rad-local-05e6c47759344f3e/update-bd476becbc6a4558ab2cc0bd95fb1ecf/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-36689aec185f46ae964e8c367cffd059/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-0198fb9128fb49808d23c381a6cf1868/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-34f527a87f894609bdf9c5b0e9d8fb99/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-47ea30fd1eae42858a277f0cab251ab8/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-4c63c02f708d4f4bb17f1b0f47814dc5/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-8b902e5cc8f14d2f8f76dea00ca938e8/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-8235ff64407b4d0f90afbaa4b96ad40e/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-fd31cda3f5104fa8a3f0c9a6668ce86e/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-cae37ad1f34641c782071c02cbcde0ac/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-3e67e1564a444be195d821495e4714c0/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-8902dbefbc3d46f98ecd2b2341cb2d0f/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-1a23e50b9956430baf0e1f7e833e90e2/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-a97274615fe74e12ad128c178584fef7/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-8f29df1f28524a408d06b0001ed06c2b/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-e97266b1bfd943039e0b69da439d0ee7/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-3b30b18c6bca42868100de868120ca0c/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-0f5dc8d3f04941d7b0527123cc5f80ef/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-f443bceb62d54efe9b3ae91840d8833b/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-205678e501b843c595a4e5a15ccb0ca8/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-a2637908fe86447683b01d0b30412876/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-1a6d23271f934c6e9cce61f2a13417d6/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-eaeff83b279c4602bacda0913fe81ab9/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-8471ff4de16b4d89ab2176331059c7aa/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-d4e5f7ed9a034651982e792f029f1e89/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-b52ff363c4394bc4b76fc4ccd5cde111/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-fa2eab524bc54857a7defe4abbf14096/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-df86e0d0878049de9cb82577362353c8/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-465f858aea164627879464d92449d9be/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-a62c7aebde904e51ba5d52ccc692619d/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-62251d27ea4345489e313dd37aeb4d06/source/AGENTS.md
../rad-belden/.local/products/rad-local-dbed816f78e445e8/update-10e7315fca4245e09ba0203110da12c0/source/AGENTS.md
../rad-belden/.local/products/rad-local-1205ab406a9d4e67/source/AGENTS.md
../rad-belden/.local/products/rad-local-9b67cb594a95487d/source/AGENTS.md
../rad-belden/.local/archives/task-notes-20261020T173159Z/commit-policy-20261008/AGENTS.md
../rad-belden/.local/previews/postgres-d026d1441877/source/AGENTS.md
../rad-belden/.local/previews/rad-product-260e47af7010/browser-200e1a4bd5cb/source/AGENTS.md
../rad-belden/.local/previews/rad-product-260e47af7010/source-protocol6/AGENTS.md
../rad-belden/.local/previews/rad-product-260e47af7010/browser-82349145628a/source/AGENTS.md
../rad-belden/.local/previews/rad-product-260e47af7010/source/AGENTS.md
../rad-belden/.local/previews/rad-product-260e47af7010/browser-180431bd980e/source/AGENTS.md
../rad-belden/.local/previews/rad-product-260e47af7010/browser-bcc583d771ba/source/AGENTS.md
../rad-belden/.local/previews/rad-product-260e47af7010/browser-519090e01376/source/AGENTS.md
../rad-belden/.local/previews/rad-product-260e47af7010/browser-0668bff86658/source/AGENTS.md
../rad-belden/.local/previews/postgres-b9013a862f15/source/AGENTS.md
../rad-belden/.local/previews/postgres-f019440e2e68/source/AGENTS.md
../rad-belden/.local/previews/postgres-17073b2cc7d4/source/AGENTS.md
../rad-belden/.local/reviews/dev017h/repaired/AGENTS.md
../rad-belden/.local/reviews/dev017h/source/AGENTS.md
../rad-belden/.local/reviews/dev017g/source-0k9ljrr6/AGENTS.md
../rad-belden/.local/reviews/dev014c-independent/run-0deee16d2592/source/AGENTS.md
../rad-belden/.local/reviews/dev014c-independent/run-789a63009a36/source/AGENTS.md
../rad-belden/.local/reviews/dev014c-independent/run-a9186a1618a8/source/AGENTS.md
../rad-belden/.local/reviews/dev014c-independent/run-03f1da52da92/source/AGENTS.md
../rad-belden/AGENTS.md
../topological-phases-of-matter/AGENTS.md
../yonedarepo-research/website/node_modules/next/AGENTS.md
../yonedarepo-research/website/AGENTS.md
../CodexBar/AGENTS.md
../test-me/dashboard/node_modules/next/AGENTS.md
../test-me/dashboard/AGENTS.md
../deepseek-harness/native/system/AGENTS.md
../deepseek-harness/snapshots/AGENTS.md
../deepseek-harness/snapshots/session/agent-instructions/workspace/AGENTS.md
../deepseek-harness/snapshots/session/agent-instructions/workspace/nested/AGENTS.md
../deepseek-harness/snapshots/session/ptc-workspace-context/workspace/AGENTS.md
../deepseek-harness/snapshots/session/ptc-workspace-context/workspace/nested/AGENTS.md
../deepseek-harness/website/AGENTS.md
../deepseek-harness/.agents/notes/implemented/AGENTS.md
../deepseek-harness/.agents/notes/AGENTS.md
../deepseek-harness/.agents/notes/archived/AGENTS.md
../deepseek-harness/docs/AGENTS.md
../deepseek-harness/benchmarks/AGENTS.md
../deepseek-harness/scripts/AGENTS.md
../deepseek-harness/packages/experimental/AGENTS.md
../deepseek-harness/packages/schedule/AGENTS.md
../deepseek-harness/packages/web/AGENTS.md
../deepseek-harness/packages/AGENTS.md
../deepseek-harness/packages/client/AGENTS.md
../deepseek-harness/.github/AGENTS.md
../deepseek-harness/AGENTS.md
../deepseek-harness/apps/cli/tests/profiles/AGENTS.md
../deepseek-harness/vendor/AGENTS.md
../formal-proofs/formal-conjectures/AGENTS.md
../.worktrees/MDReader-ios-compact-acceptance/AGENTS.md
../.worktrees/MDReader-ios-runtime-acceptance/node_modules/.pnpm/cytoscape@3.34.0/node_modules/cytoscape/AGENTS.md
../.worktrees/MDReader-ios-runtime-acceptance/AGENTS.md
../.worktrees/MDReader-mobile-controls-selector-repair/AGENTS.md
../.worktrees/MDReader-e2e-ci/node_modules/.pnpm/cytoscape@3.34.0/node_modules/cytoscape/AGENTS.md
../.worktrees/MDReader-e2e-ci/AGENTS.md
../.worktrees/MDReader-ios-search-ready/AGENTS.md
../.worktrees/MDReader-mobile-account-entry/AGENTS.md
../.worktrees/MDReader-simple-agents/AGENTS.md
../.worktrees/MDReader-agent-install-button/AGENTS.md
../.worktrees/MDReader-cloud-document-creation/AGENTS.md
../.worktrees/MDReader-agent-settings-polish/AGENTS.md
../.worktrees/MDReader-agent-skill-portability/AGENTS.md
../.worktrees/MDReader-Web-conflict-resolution/AGENTS.md
../.worktrees/MDReader-public-skill-ui/AGENTS.md
../.worktrees/MDReader-sidebar-recents-readiness/AGENTS.md
../.worktrees/MDReader-folder-indexing/AGENTS.md
../.worktrees/MDReader-Web-sharing/AGENTS.md
../.worktrees/MDReader-agent-command/AGENTS.md
../.worktrees/MDReader-batch-wiring/AGENTS.md
../.worktrees/MDReader-agent-project-setup/AGENTS.md
../.worktrees/MDReader-sync-request-redisplay/AGENTS.md
../.worktrees/MDReader-agent-public-distribution/AGENTS.md
../codex_desktop/commercial-pulse-dashboard/node_modules/recharts/AGENTS.md
../agentherowork/agent-hero/AGENTS.md
../agentherowork/agent-os/AGENTS.md
../agentherowork/agent-os/src/agent_os_web/deps/phoenix/priv/templates/phx.gen.auth/AGENTS.md
../humanizer/AGENTS.md
../nyctax/node_modules/.pnpm/@supabase+auth-js@2.110.9/node_modules/@supabase/auth-js/AGENTS.md
../nyctax/node_modules/.pnpm/@supabase+realtime-js@2.110.9/node_modules/@supabase/realtime-js/AGENTS.md
../nyctax/node_modules/.pnpm/@supabase+postgrest-js@2.110.9/node_modules/@supabase/postgrest-js/AGENTS.md
../nyctax/node_modules/.pnpm/@supabase+functions-js@2.110.9/node_modules/@supabase/functions-js/AGENTS.md
../nyctax/node_modules/.pnpm/@supabase+storage-js@2.110.9/node_modules/@supabase/storage-js/AGENTS.md
../nyctax/node_modules/.pnpm/@supabase+supabase-js@2.110.9/node_modules/@supabase/supabase-js/AGENTS.md
../ai_price_dashboard-auth-providers/AGENTS.md

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n -A120 -B15 \"label\\{tab:code\\}|Code evidence|What the code checks\" papers/latex/formalized-state.tex" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
1003-\emph{The abstraction forgets too much.} The equivalence $\cong_A$ forgets the content of rules and beliefs, the procedures that implement each function, and the moral quality of outcomes (\cref{lem:formalized-state:preserved}). A medieval monarchy and a modern republic can have the same image if their control shares, contestability, couplings and dependencies coincide. This is the price of a representation that covers every governance system, and it is why the abstraction says nothing about justice. The properties it keeps are the ones that the capture predicate needs, and the properties it forgets are left to history, law and theology.
1004-
1005-\emph{Uniqueness is built into the definitions.} The universal property of \cref{thm:formalized-state:uniqueness} follows quickly once the preserved properties are fixed, and \cref{rem:formalized-state:scope} says so. The substantive content is that the coarsest abstraction is a class of six-layer structures with an interdependent dependency hypergraph, which needs necessity, and that no coarsening of it works, which needs the witness pairs. A reader who wants to preserve other properties obtains another abstraction, unique for those properties.
1006-
1007-\emph{Class relations are underdeveloped.} A Marxian reader may find that the six pillars dissolve class into functions. The productive pillar is the place where the objection is met. Part VI shows that producers hold a latent veto over every institution that cannot replace their output (Proposition 3.6 of Part VI), and the dependency structure makes every function depend on production. The framework is a middle-range theory of institutions, and it leaves the theory of class formation to others.
1008-
1009-\section{Conclusion}
1010-\label{sec:conclusion}
1011-
1012-The six-pillar framework identifies an invariant structure of human governance, supported by historical observation and given precise expression through mathematics. Relative to six axioms about collective life, four incidence axioms and a stated set of preserved properties, the Formalized State has four properties. It represents every governance system that satisfies the axioms, preserving roles, control shares, concentration, contestability, integration and dependencies and forgetting content, ideology and procedure. Its components are necessary, because the axioms force each function and each dependency and each axiom can fail in a persistent model. It is minimal, because every way of dropping or merging pillars confuses two systems with different preserved properties. And it is unique, as the coarsest abstraction that preserves those properties, up to a unique isomorphism, with exactly six dimensions. Encodings of seven classical frameworks each confuse a pair of systems that it distinguishes.
1013-
1014-Capture belongs to instances. Structures that satisfy every axiom occupy every corner of the concentration and integration square, so the existence of the structure settles nothing about its capture, and the conversion model shows how replacement and contestability decide whether a coalition's foothold dies out. The open questions are empirical: whether every functioning collective satisfies the axioms, which has been tested against the ethnographic and historical record only qualitatively; and the quantitative scoring of real polities on indices whose ranges are proved here. The series calls the abstraction the Hierarchy of the Beast System. The structure is universal, its capture is contingent, and the difference between them is a matter of measurement.
1015-
1016-\appendix
1017-
1018:\section{Code evidence}
1019-\label{app:code}
1020-
1021-The reference implementation is the Python package \texttt{beast\_system} in the directory \texttt{model/} of the project, with its tests in \texttt{model/tests/}; the suite of 335 tests passes. The code encodes the formal objects of this paper and checks, on coded fixtures, the results that admit a computational check. A passing test is evidence that the encoding agrees with the stated result on the fixtures it covers, not a proof; the proofs are in the text. The codings of the hard cases, including the incidence axioms, are qualitative readings of the sources cited in \cref{sec:necessity}, recorded with those sources in the code. \Cref{tab:code} maps each result to the functions that encode it and the tests that check it. Function names refer to modules of \texttt{beast\_system}, and test names to files in \texttt{model/tests/}. Results proved only in the text, such as \cref{lem:formalized-state:forcing,lem:formalized-state:pillars}, \cref{cor:formalized-state:michels} and \cref{prop:formalized-state:perron}, are not listed.
1022-
1023-{\footnotesize
1024-\makeatletter\g@addto@macro\UrlBreaks{\do\_\do\.}\makeatother
1025-\newcommand{\code}[1]{\nolinkurl{#1}}
1026-\setlength{\tabcolsep}{3pt}
1027-\renewcommand{\arraystretch}{1.1}
1028-\begin{longtable}{@{}>{\raggedright\arraybackslash}p{2.3cm}>{\raggedright\arraybackslash}p{4.4cm}>{\raggedright\arraybackslash}p{4.3cm}@{}}
1029:\caption{Results of this paper, the code that encodes them, and the tests that check them on fixtures.}\label{tab:code}\\
1030-\toprule
1031:Result & What the code checks & Functions and tests \\
1032-\midrule
1033-\endfirsthead
1034-\toprule
1035:Result & What the code checks & Functions and tests \\
1036-\midrule
1037-\endhead
1038-\bottomrule
1039-\endfoot
1040-\Cref{def:formalized-state:implementation}, \cref{thm:formalized-state:A}, \cref{cor:formalized-state:struct} & Every hard-case and baseline fixture that satisfies the axioms realizes all six functions with the relations $\Dzero$ present, and none is a counterexample. & \code{necessity.check_proposition_a}; \code{test_necessity}: \code{test_theorem_a_on_hard_cases}, \code{test_baseline_model_is_consistent} \\
1041-\Cref{prop:formalized-state:independence} & The model of part (a) has $\Struct$; each of the six independence fixtures persists, violates exactly its axiom and lacks exactly its function, including the repaired model for Ax4$^{*}$. & \code{necessity.PROP_4_4A_MODEL}, \code{AXIOM_INDEPENDENCE}, \code{R1_AX4_MODEL}; \code{test_necessity}: \code{test_prop_4_4a_model_and_variant}, \code{test_axiom_independence_fixtures}, \code{test_r1_independence_model_for_ax4} \\
1042-\Cref{lem:formalized-state:D0} & The hyperarc $(\{\pI,\pC\},\pJ)$ is generated, and in the variant with a fine on defiance neither $\pI\to\pJ$ nor $\pC\to\pJ$ is. & \code{necessity.generate_dependencies}, \code{PROP_4_4A_VARIANT}; \code{test_necessity}: \code{test_prop_4_4a_model_and_variant} \\
1043-\Cref{thm:formalized-state:interdependence} & The arcs of $\Dstar$ are generated from the axiom encodings; $\Dstar$ is strongly connected, and the cascade of every single function is all six; every hard-case fixture with the full axiom set and all six coded practices is interdependent. & \code{necessity.D_STAR_KEYS}, \code{generate_dependencies}, \code{is_strongly_connected}, \code{cascade_closure}; \code{test_necessity}: \code{test_d_star_is_strongly_connected_and_cascade_complete}, \code{test_interdependence_holds_for_every_axiom_built_fixture} \\
1044-\Cref{prop:formalized-state:minimality} & The six axioms without X1 to X5 give $\Struct$ but not interdependence; without X1 no arc enters $\pW$; without X2 $\pP$ has no outgoing arc; without X5 the structure is strongly connected and $\cl(\{\pC\})=\{\pC\}$, while splitting the hyperarc puts $\pJ$ in that cascade; precedent can replace X3. & \code{test_necessity}: \code{test_d0_axioms_without_x_give_struct_but_not_interdependence}, \code{test_without_x1_no_arc_into_w}, \code{test_without_x2_p_has_no_out_arc}, \code{test_without_x5_strongly_connected_but_c_isolated}, \code{test_replacing_x3_by_precedent_keeps_strong_connectivity} \\
1045-\Cref{def:formalized-state:overlap} & The overlap measure is computed for general, non-additive coalition shares. & \code{indices.coalition_overlap}; \code{test_indices}: \code{test_coalition_overlap_general_kappa} \\
1046-\Cref{lem:formalized-state:hub} & $\Integ$ equals the sum of degrees over thirty; the hub-set bounds for $k=1,2,3$ ($1/3$, $0.6$ and $0.8$) hold and are attained; the clique bound and the pure-star bound hold on test matrices. & \code{indices.integration_degrees}, \code{hub_bound}, \code{clique_lower_bound}, \code{star_upper_bound}; \code{test_indices}: \code{test_degree_decomposition_of_integration}, \code{test_hub_bound_values_and_validity}, \code{test_clique_lower_bound}, \code{test_star_upper_bound} \\
1047-\Cref{def:formalized-state:cap}, \cref{lem:formalized-state:U} & Each of the three conditions of a capture link is necessary; $U$ lies in $[0,1]$ and, for any weights, between the smallest and largest pillar terms. & \code{capture.proposition_b}, \code{indices.unaccountable_concentration}, \code{weight_sensitivity}; \code{test_capture}: \code{test_each_capture_condition_is_necessary}; \code{test_indices}: \code{test_u_bounds_random}, \code{test_weight_sensitivity_within_vertex_bounds} \\
1048-\Cref{lem:formalized-state:separation} & The admissibility check returns true for the hard cases and the four corner assignments when every coded holder is supplied as a member; these fixtures do not exercise the clause on parties to a dispute. & \code{necessity.is_admissible}; \code{test_necessity}: \code{test_admissibility} \\
1049-\Cref{thm:formalized-state:nonimplication} & Four polities satisfying every axiom attain $(U,\Integ)$ equal to $(0,0)$, $(0,1)$, $(1,0)$ and $(1,1)$, all interdependent, and only $(1,1)$ has a capture link; the counter-model holds for several threshold pairs. & \code{capture.corner_polities}, \code{a_does_not_imply_b}; \code{test_capture}: \code{test_corner_polities_attain_the_four_corners}, \code{test_counter_model_robust_to_thresholds} \\
1050-\Cref{def:formalized-state:F,def:formalized-state:profile}, \cref{thm:formalized-state:representation} & A coded record is representable exactly when Proposition A holds for it, on the fixtures and on random well-formed records; independence models fail (F1), and the baseline without X1 to X5 fails only (F4). & \code{representation.CodedRecord}, \code{represent}, \code{in_formalized_class}, \code{representable}; \code{test_representation}: \code{test_representable_iff_proposition_a}, \code{test_theorem_on_random_well_formed_records}, \code{test_independence_models_are_not_representable_empty_layer}, \code{test_baseline_without_x_fails_only_f4} \\
1051-\Cref{lem:formalized-state:preserved} & Representation preserves $H$, $U$, $\Integ$, the capture predicate and interdependence; equivalence under an actor bijection preserves these and every coupling $C^{\ov}_{mn}$. & \code{representation.preserved_quantities}, \code{equivalent_A}; \code{test_representation}: \code{test_represent_preserves_quantities}, \code{test_equivalent_a_under_actor_bijection_preserves_quantities} \\
1052-\Cref{prop:formalized-state:minimality6} & Every drop and every merge of pillars, including the all-dropped map, identifies the two witnesses of the proposition while their preserved properties differ; drop witnesses keep both actors through a retained pillar. & \code{uniqueness.coarsen}, \code{witness_coarsening}; \code{representation.drop}, \code{merge}; \code{test_uniqueness}: \code{test_every_drop_collapses_a_witness}, \code{test_every_merge_collapses_a_witness}, \code{test_all_dropped_coarsening_has_a_witness}, \code{test_drop_witness_keeps_b_as_actor_via_retained_pillar} \\
1053-\Cref{def:formalized-state:abstraction}, \cref{thm:formalized-state:uniqueness} & Two $P$-preserving abstractions built differently factor through $\Phi$ by a well-defined map that is a bijection on the fixtures; the canonical form is a complete invariant for $P$. & \code{uniqueness.phi}, \code{canonical_form}, \code{factor_through_phi}; \code{test_uniqueness}: \code{test_p_preserving_abstractions_factor_through_phi}, \code{test_canonical_form_is_a_complete_invariant} \\
1054-\Cref{thm:formalized-state:six} & Bijective coarsenings are renamings that preserve the structure; each of the 202 partitions of the six pillars into fewer than six blocks collapses a witness pair. & \code{uniqueness.coarsen}; \code{test_uniqueness}: \code{test_bijective_coarsenings_are_p_preserving}, \code{test_pigeonhole_every_partition_with_fewer_than_six_blocks} \\
1055-\Cref{def:formalized-state:conversion}, \cref{thm:formalized-state:conversion} & Parts (a), (b), (c), (e) and (f), on the tested fixtures and samples: the map stays in the cube and below $Ay$ on 300 samples; one $\rho(A)<1$ path decays below $10^{-6}$; the fully contestable pillar obeys its geometric bound and integration cap; $\rho(A)$ is nonincreasing on each tested grid of $Q_n$; and the foothold bound holds for 500 steps. & \code{dynamics.conversion_step}, \code{comparison_matrix}, \code{foothold_bound}; \code{test_conversion}: \code{test_t_maps_cube_into_itself_and_is_dominated_by_a}, \code{test_rho_below_one_means_reversible}, \code{test_full_contestability_drains_pillar_and_caps_integration}, \code{test_rho_nonincreasing_in_each_q}, \code{test_foothold_never_vanishes} \\
1056-\Cref{rem:formalized-state:sign} & A six-pillar pair of matrices with the same positive entries has spectral radii above and below one. & \code{dynamics.negative_feedback_example}; \code{test_dynamics_regimes}: \code{test_positive_links_do_not_guarantee_persistence} \\
1057-\Cref{prop:formalized-state:witnesses}, \cref{thm:formalized-state:novelty} & For each of the seven encoded predecessors, the two witness systems have the same actors and the same encoding and different $P$; the Weber label is not determined by $P$. & \code{uniqueness.encode_parsons} and the six other encodings, \code{witness_pair}; \code{test_uniqueness}: \code{test_predecessor_encoding_collapses_its_witness}, \code{test_weber_label_is_not_determined_by_p} \\
1058-\end{longtable}
1059-}
1060-
1061-%APPENDIX-CODE-EVIDENCE
1062-
1063-\begin{small}
1064-\begin{thebibliography}{999}
1065-
1066-\bibitem[Aberle et al.(1950)]{aberle1950}
1067-Aberle, D. F., A. K. Cohen, A. K. Davis, M. J. Levy Jr. and F. X. Sutton. 1950. ``The Functional Prerequisites of a Society.'' \emph{Ethics} 60(2): 100-111. \url{https://doi.org/10.1086/290705}.
1068-
1069-\bibitem[Acemoglu and Robinson(2006)]{acemoglu2006}
1070-Acemoglu, Daron and James A. Robinson. 2006. \emph{Economic Origins of Dictatorship and Democracy}. Cambridge University Press. \url{https://doi.org/10.1017/CBO9780511510809}.
1071-
1072-\bibitem[Acemoglu and Robinson(2019)]{acemoglu2019}
1073-Acemoglu, Daron and James A. Robinson. 2019. \emph{The Narrow Corridor: States, Societies, and the Fate of Liberty}. Penguin Press.
1074-
1075-\bibitem[Almond and Coleman(1960)]{almond1960}
1076-Almond, Gabriel A. and James S. Coleman, eds. 1960. \emph{The Politics of the Developing Areas}. Princeton University Press. \url{https://doi.org/10.1515/9781400866977}.
1077-
1078-\bibitem[Almond and Powell(1966)]{almond1966}
1079-Almond, Gabriel A. and G. Bingham Powell. 1966. \emph{Comparative Politics: A Developmental Approach}. Little, Brown. \url{https://openlibrary.org/works/OL2693586W}.
1080-
1081-\bibitem[Aristotle(1996)]{aristotle1996}
1082-Aristotle. 1996. \emph{The Politics, and the Constitution of Athens}. Cambridge University Press. \url{https://openlibrary.org/works/OL14998298W}.
1083-
1084-\bibitem[Arrow(1951)]{arrow1951}
1085-Arrow, Kenneth J. 1951. \emph{Social Choice and Individual Values}. Yale University Press edition. \url{https://doi.org/10.12987/9780300186987}.
1086-
1087-\bibitem[Aumann(1976)]{aumann1976}
1088-Aumann, Robert J. 1976. ``Agreeing to Disagree.'' \emph{The Annals of Statistics} 4(6): 1236-1239. \url{https://doi.org/10.1214/aos/1176343654}.
1089-
1090-\bibitem[Axelrod(1984)]{axelrod1984}
1091-Axelrod, Robert. 1984. \emph{The Evolution of Cooperation}. Basic Books.
1092-
1093-\bibitem[Barkey(2008)]{barkey2008}
1094-Barkey, Karen. 2008. \emph{Empire of Difference: The Ottomans in Comparative Perspective}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511790645}.
1095-
1096-\bibitem[Bauckham(1991)]{bauckham1991}
1097-Bauckham, Richard. 1991. ``The Economic Critique of Rome in Revelation 18.'' In \emph{Images of Empire}, edited by Loveday Alexander, 47-90. Sheffield: JSOT Press.
1098-
1099-\bibitem[Bauckham(1993)]{bauckham1993}
1100-Bauckham, Richard. 1993. \emph{The Theology of the Book of Revelation}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511819858}.
1101-
1102-\bibitem[Becker(1968)]{becker1968}
1103-Becker, Gary S. 1968. ``Crime and Punishment: An Economic Approach.'' \emph{Journal of Political Economy} 76(2): 169-217. \url{https://doi.org/10.1086/259394}.
1104-
1105-\bibitem[Beik(1985)]{beik1985}
1106-Beik, William. 1985. \emph{Absolutism and Society in Seventeenth-Century France: State Power and Provincial Aristocracy in Languedoc}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511583797}.
1107-
1108-\bibitem[Boehm(1999)]{boehm1999}
1109-Boehm, Christopher. 1999. \emph{Hierarchy in the Forest: The Evolution of Egalitarian Behavior}. Harvard University Press. \url{https://doi.org/10.2307/j.ctvjf9xr4}.
1110-
1111-\bibitem[Boyer(1992)]{boyer1992}
1112-Boyer, Paul. 1992. \emph{When Time Shall Be No More: Prophecy Belief in Modern American Culture}. Harvard University Press (Belknap). \url{https://doi.org/10.2307/jj.41480279}.
1113-
1114-\bibitem[Cassinelli(1953)]{cassinelli1953}
1115-Cassinelli, C. W. 1953. ``The Law of Oligarchy.'' \emph{American Political Science Review} 47(3): 773-784. \url{https://doi.org/10.2307/1952904}.
1116-
1117-\bibitem[Clastres(1987)]{clastres1987}
1118-Clastres, Pierre. 1987. \emph{Society against the State: Essays in Political Anthropology (1974), trans. Robert Hurley}. Zone Books. \url{https://doi.org/10.2307/j.ctv1595m3p}.
1119-
1120-\bibitem[Collins(1984)]{collins1984}
1121-Collins, Adela Yarbro. 1984. \emph{Crisis and Catharsis: The Power of the Apocalypse}. Westminster Press.
1122-
1123-\bibitem[Cox et al.(2010)]{cox2010}
1124-Cox, Michael, Gwen Arnold and Sergio Villamayor Tomas. 2010. ``A Review of Design Principles for Community-based Natural Resource Management.'' \emph{Ecology and Society} 15(4): 38. \url{https://doi.org/10.5751/ES-03704-150438}.
1125-
1126-\bibitem[Dahl(1961)]{dahl1961}
1127-Dahl, Robert A. 1961. \emph{Who Governs? Democracy and Power in an American City}. Yale University Press.
1128-
1129-\bibitem[Easton(1965)]{easton1965}
1130-Easton, David. 1965. \emph{A Systems Analysis of Political Life}. John Wiley \& Sons.
1131-
1132-\bibitem[Ellickson(1991)]{ellickson1991}
1133-Ellickson, Robert C. 1991. \emph{Order without Law: How Neighbors Settle Disputes}. Harvard University Press. \url{https://doi.org/10.4159/9780674036437}.
1134-
1135-\bibitem[Elster(1979)]{elster1979}
1136-Elster, Jon. 1979. \emph{Ulysses and the Sirens: Studies in Rationality and Irrationality}. Cambridge University Press.
1137-
1138-\bibitem[Elster(1983)]{elster1983}
1139-Elster, Jon. 1983. \emph{Explaining Technical Change: A Case Study in the Philosophy of Science}. Cambridge University Press.
1140-
1141-\bibitem[Ertman(1997)]{ertman1997}
1142-Ertman, Thomas. 1997. \emph{Birth of the Leviathan: Building States and Regimes in Medieval and Early Modern Europe}. Cambridge University Press. \url{https://doi.org/10.1017/cbo9780511529016}.
1143-
1144-\bibitem[Evans-Pritchard(1940)]{evanspritchard1940}
1145-Evans-Pritchard, E. E. 1940. \emph{The Nuer: A Description of the Modes of Livelihood and Political Institutions of a Nilotic People}. Clarendon Press.
1146-
1147-\bibitem[Friesen(2001)]{friesen2001}
1148-Friesen, Steven J. 2001. \emph{Imperial Cults and the Apocalypse of John: Reading Revelation in the Ruins}. Oxford University Press. \url{https://doi.org/10.1093/0195131533.001.0001}.
1149-
1150-\bibitem[Fuller(1995)]{fuller1995}
1151-Fuller, Robert C. 1995. \emph{Naming the Antichrist: The History of an American Obsession}. Oxford University Press. \url{https://doi.org/10.1093/acprof:oso/9780195109795.001.0001}.
1152-
1153-\bibitem[Gallo et al.(1993)]{gallo1993}
1154-Gallo, Giorgio, Giustino Longo, Stefano Pallottino and Sang Nguyen. 1993. ``Directed Hypergraphs and Applications.'' \emph{Discrete Applied Mathematics} 42(2-3): 177-201. \url{https://doi.org/10.1016/0166-218X(93)90045-P}.
1155-

exec
/usr/local/bin/zsh -lc 'rg --files model/beast_system model/tests | sort' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
model/beast_system/__init__.py
model/beast_system/capture.py
model/beast_system/dynamics.py
model/beast_system/indices.py
model/beast_system/necessity.py
model/beast_system/network.py
model/beast_system/pillars.py
model/beast_system/regimes.py
model/beast_system/representation.py
model/beast_system/uniqueness.py
model/tests/test_capture.py
model/tests/test_conversion.py
model/tests/test_dynamics_regimes.py
model/tests/test_indices.py
model/tests/test_necessity.py
model/tests/test_pillars_network.py
model/tests/test_representation.py
model/tests/test_uniqueness.py

exec
/usr/local/bin/zsh -lc 'git status --short && git branch --show-current && git log -1 --oneline' in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 4805ms:
2026-10-22 14:15:54.798 xcodebuild[10918:4423895]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 14:15:55.001 xcodebuild[10918:4423894] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-WEcSJH4W' (errno=Operation not permitted)
2026-10-22 14:15:55.471 xcodebuild[10920:4423919]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 14:15:55.561 xcodebuild[10920:4423917] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
 M papers/latex/formalized-state.tex
?? reviews/formalized-state-code-audit-2.md
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-o5y1qX5y' (errno=Operation not permitted)
2026-10-22 14:15:56.446 xcodebuild[10925:4423973]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 14:15:56.537 xcodebuild[10925:4423971] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-xf6KodFw' (errno=Operation not permitted)
2026-10-22 14:15:56.926 xcodebuild[10927:4423997]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 14:15:57.014 xcodebuild[10927:4423996] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
main
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-5akWsG6D' (errno=Operation not permitted)
2026-10-22 14:15:57.855 xcodebuild[10931:4424025]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 14:15:57.952 xcodebuild[10931:4424024] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-eP84hjAD' (errno=Operation not permitted)
2026-10-22 14:15:58.354 xcodebuild[10954:4424306]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 14:15:58.447 xcodebuild[10954:4424270] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
6356a72 The Six Pillars of the Beast System: seven papers, formal model, website

codex
I found the current 18-row table and confirmed the five revised rows are present in the working copy. I’ll now trace each cited test’s assertions through the called functions; I will not treat comments, names, or a passing-suite report as sufficient by themselves.
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/capture.py | sed -n '1,420p'; nl -ba model/tests/test_capture.py | sed -n '1,520p'" in /Users/mlong/Documents/Development/the-beast-system
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

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '1,420p'; nl -ba model/tests/test_necessity.py | sed -n '1,520p'" in /Users/mlong/Documents/Development/the-beast-system
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

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/indices.py | sed -n '1,420p'; nl -ba model/tests/test_indices.py | sed -n '1,520p'" in /Users/mlong/Documents/Development/the-beast-system
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
    17	from beast_system.pillars import PAIRS, PILLARS
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

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "rg -n '"'^def (coalition_overlap|integration_degrees|hub_bound|clique_lower_bound|star_upper_bound|unaccountable_concentration|weight_sensitivity)'"' model/beast_system/indices.py; rg -n '"'^def test_(coalition_overlap_general_kappa|degree_decomposition_of_integration|hub_bound_values_and_validity|clique_lower_bound|star_upper_bound|u_bounds_random|weight_sensitivity_within_vertex_bounds)'"' model/tests/test_indices.py" in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc "rg -n '"'^def (represent|in_formalized_class|representable|preserved_quantities|equivalent_A|drop|merge)|''^class CodedRecord'"' model/beast_system/representation.py; rg -n '"'^def test_(representable_iff_proposition_a|theorem_on_random_well_formed_records|independence_models_are_not_representable_empty_layer|baseline_without_x_fails_only_f4|represent_preserves_quantities|equivalent_a_under_actor_bijection_preserves_quantities)'"' model/tests/test_representation.py" in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc "rg -n '"'^def (phi|canonical_form|factor_through_phi|coarsen|witness_coarsening|encode_parsons|encode_|witness_pair)'"' model/beast_system/uniqueness.py; rg -n '"'^def test_(every_drop_collapses_a_witness|every_merge_collapses_a_witness|all_dropped_coarsening_has_a_witness|drop_witness_keeps_b_as_actor_via_retained_pillar|p_preserving_abstractions_factor_through_phi|canonical_form_is_a_complete_invariant|bijective_coarsenings_are_p_preserving|pigeonhole_every_partition_with_fewer_than_six_blocks|predecessor_encoding_collapses_its_witness|weber_label_is_not_determined_by_p)'"' model/tests/test_uniqueness.py" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
119:def unaccountable_concentration(
184:def integration_degrees(C: np.ndarray) -> dict[Pillar, float]:
190:def hub_bound(k: int) -> float:
203:def coalition_overlap(kappa: Mapping[str, Mapping[Pillar, float]]) -> np.ndarray:
249:def clique_lower_bound(c: float, k: int) -> float:
260:def star_upper_bound(C: np.ndarray, hub: Pillar) -> float:
294:def weight_sensitivity(
54:def test_u_bounds_random():
133:def test_weight_sensitivity_within_vertex_bounds():
164:def test_degree_decomposition_of_integration():
174:def test_hub_bound_values_and_validity(k, expected):
183:def test_coalition_overlap_general_kappa():
216:def test_clique_lower_bound(k):
228:def test_star_upper_bound():

 succeeded in 0ms:
69:def coarsen(F: FormalizedStructure, c: Coarsening,
108:def phi(record: CodedRecord) -> FormalizedStructure:
162:def factor_through_phi(alpha: Callable[[CodedRecord], object],
257:def canonical_form(F: FormalizedStructure) -> tuple:
367:def witness_coarsening(c: Coarsening, lam: Mapping[Label, float] | None = None
413:def encode_parsons(F: FormalizedStructure) -> FormalizedStructure:
418:def encode_mann(F: FormalizedStructure) -> FormalizedStructure:
423:def encode_easton(F: FormalizedStructure) -> FormalizedStructure:
428:def encode_luhmann(F: FormalizedStructure) -> FormalizedStructure:
434:def encode_almond(F: FormalizedStructure) -> FormalizedStructure:
440:def encode_aristotle(F: FormalizedStructure) -> tuple[str, str]:
452:def encode_weber(F: FormalizedStructure, legitimation: str, has_staff: bool) -> tuple[str, bool]:
483:def witness_pair(k: str) -> tuple[CodedRecord, CodedRecord]:
494:def coarsenings_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
132:def test_p_preserving_abstractions_factor_through_phi(alpha):
147:def test_canonical_form_is_a_complete_invariant():
197:def test_every_merge_collapses_a_witness(m, n, lam_m):
204:def test_every_drop_collapses_a_witness(m):
208:def test_pigeonhole_every_partition_with_fewer_than_six_blocks():
238:def test_predecessor_encoding_collapses_its_witness(k):
265:def test_weber_label_is_not_determined_by_p():
274:def test_drop_witness_keeps_b_as_actor_via_retained_pillar():
289:def test_bijective_coarsenings_are_p_preserving():
371:def test_all_dropped_coarsening_has_a_witness():

 succeeded in 0ms:
76:class CodedRecord:
163:def represent(record: CodedRecord) -> FormalizedStructure:
292:def in_formalized_class(F: FormalizedStructure) -> ClassMembership:
325:def representable(record: CodedRecord) -> bool:
343:def preserved_quantities(
470:def equivalent_A(F: FormalizedStructure, G: FormalizedStructure) -> bool:  # noqa: N802
479:def drop(F: FormalizedStructure, m: Label) -> FormalizedStructure:
502:def merge(F: FormalizedStructure, m: Label, n: Label, lam: float) -> FormalizedStructure:
58:def test_representable_iff_proposition_a(name, record):
70:def test_independence_models_are_not_representable_empty_layer(axiom):
76:def test_baseline_without_x_fails_only_f4():
84:def test_represent_preserves_quantities(polity):
121:def test_equivalent_a_under_actor_bijection_preserves_quantities():
214:def test_theorem_on_random_well_formed_records():

exec
/usr/local/bin/zsh -lc "rg -n '"'^def (check_proposition_a|generate_dependencies|is_strongly_connected|cascade_closure|is_admissible)|''^(PROP_4_4A_MODEL|AXIOM_INDEPENDENCE|R1_AX4_MODEL|D_STAR_KEYS)'"' model/beast_system/necessity.py; rg -n '"'^def test_(theorem_a_on_hard_cases|baseline_model_is_consistent|prop_4_4a_model_and_variant|axiom_independence_fixtures|r1_independence_model_for_ax4|d_star_is_strongly_connected_and_cascade_complete|interdependence_holds_for_every_axiom_built_fixture|d0_axioms_without_x_give_struct_but_not_interdependence|without_x1_no_arc_into_w|without_x2_p_has_no_out_arc|without_x5_strongly_connected_but_c_isolated|replacing_x3_by_precedent_keeps_strong_connectivity|admissibility)'"' model/tests/test_necessity.py" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
78:def cascade_closure(
126:def is_strongly_connected(graph: Graph, nodes: Iterable[Pillar] | None = None) -> bool:
254:D_STAR_KEYS: frozenset[ArcKey] = frozenset(r.key for r in CORE_RULES)
367:def generate_dependencies(
488:def check_proposition_a(system: GovernanceSystem) -> PropositionAResult:
683:R1_AX4_MODEL = GovernanceSystem(
697:AXIOM_INDEPENDENCE: dict[Axiom, GovernanceSystem] = {
705:PROP_4_4A_MODEL = GovernanceSystem(
744:def is_admissible(
46:def test_theorem_a_on_hard_cases(system):
148:def test_d_star_is_strongly_connected_and_cascade_complete():
155:def test_without_x5_strongly_connected_but_c_isolated():
166:def test_without_x1_no_arc_into_w():
176:def test_without_x2_p_has_no_out_arc():
182:def test_replacing_x3_by_precedent_keeps_strong_connectivity():
197:def test_interdependence_holds_for_every_axiom_built_fixture(system):
247:def test_axiom_independence_fixtures(axiom):
256:def test_baseline_model_is_consistent():
270:def test_d0_axioms_without_x_give_struct_but_not_interdependence():
339:def test_prop_4_4a_model_and_variant():
352:def test_r1_independence_model_for_ax4():
371:def test_admissibility():

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba reviews/formalized-state-code-audit-2.md | sed -n '1,260p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
     1	---
     2	reviewer: codex (OpenAI) gpt-5.6-sol
     3	type: code-evidence audit
     4	paper: formalized-state
     5	invocation: 2 (final)
     6	date: 2026-10-22T19:14:55Z
     7	note: pytest run by the author outside the sandbox: 335 passed
     8	---
     9	Reading additional input from stdin...
    10	2026-10-22T19:14:55.943878Z ERROR codex_models_manager::cache: failed to load models cache: missing field `base_instructions` at line 139 column 5
    11	OpenAI Codex v0.145.0
    12	--------
    13	workdir: /Users/mlong/Documents/Development/the-beast-system
    14	model: gpt-5.6-sol
    15	provider: openai
    16	approval: never
    17	sandbox: read-only
    18	reasoning effort: high
    19	reasoning summaries: none
    20	session id: 01a16509-b1c3-7e83-814b-9ab152316ab2
    21	--------
    22	user
    23	Final audit of the code-evidence appendix of papers/latex/formalized-state.tex (section 'Code evidence', table tab:code, 18 rows). Rows 4, 7, 9, 12 and 16 were reworded after a first audit to claim only what the named tests check. For each of the 18 rows: read the named functions in model/beast_system/ and the named tests in model/tests/, and judge whether the code and tests support the claim in the 'What the code checks' column exactly as now worded. The test suite passes (335 tests) when run outside your sandbox; judge by static inspection. Judge each row SUPPORTS, PARTIAL or NO with one sentence of evidence, and for PARTIAL or NO the exact fix. Do not judge the paper's mathematics. Output a markdown table: Row | Result | Verdict | Evidence | Fix. End with a line COUNTS: SUPPORTS=x PARTIAL=y NO=z.
    24	warning: Under-development features enabled: chronicle. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in /Users/mlong/.codex/config.toml.
    25	warning: clamping SessionEnd hook timeout to 3s in /Users/mlong/.codex/plugins/cache/openai-codex/codex/1.0.6/hooks/hooks.json
    26	2026-10-22T19:14:57.469128Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server linear: OAuth token refresh failed: Server returned error response: invalid_grant: Grant not found
    27	2026-10-22T19:14:58.430329Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=failed to refresh OAuth tokens for server resend: OAuth token refresh failed: Server returned error response: invalid_grant: Refresh token has been revoked
    28	warning: Exceeded skills context budget of 2%. All skill descriptions were removed and 108 additional skills were not included in the model-visible skills list.
    29	hook: SessionStart
    30	hook: SessionStart
    31	hook: SessionStart
    32	hook: SessionStart
    33	hook: SessionStart
    34	hook: SessionStart
    35	hook: SessionStart
    36	hook: SessionStart Completed
    37	hook: SessionStart Completed
    38	hook: SessionStart Completed
    39	hook: SessionStart Completed
    40	hook: SessionStart Completed
    41	hook: SessionStart Completed
    42	hook: SessionStart Completed
    43	hook: UserPromptSubmit
    44	hook: UserPromptSubmit Completed
    45	codex
    46	I’ll audit the appendix row-by-row against the exact named implementation functions and tests. I’m using the repository’s recorded context only to locate prior framing, then I’ll base every verdict on the live files.
    47	codex
    48	I’m also applying the code-review skill because this is a source-and-test evidence audit; it will structure the inspection but won’t broaden the task beyond the 18 claims.
    49	hook: PreToolUse
    50	hook: PreToolUse
    51	hook: PreToolUse
    52	hook: PreToolUse Completed
    53	hook: PreToolUse Completed
    54	hook: PreToolUse Completed
    55	exec
    56	/usr/local/bin/zsh -lc "sed -n '1,240p' /Users/mlong/.codex/plugins/cache/claude-cowork/engineering/1.1.0/skills/code-review/SKILL.md" in /Users/mlong/Documents/Development/the-beast-system
    57	 succeeded in 0ms:
    58	---
    59	name: code-review
    60	description: Review code for bugs, security vulnerabilities, performance issues, and maintainability. Trigger with "review this code", "check this PR", "look at this diff", "is this code safe?", or when the user shares code and asks for feedback.
    61	---
    62	
    63	# Code Review
    64	
    65	Structured code review covering security, performance, correctness, and maintainability. Works on diffs, PRs, files, or pasted code snippets.
    66	
    67	## Review Dimensions
    68	
    69	### Security
    70	- SQL injection, XSS, CSRF
    71	- Authentication and authorization flaws
    72	- Secrets or credentials in code
    73	- Insecure deserialization
    74	- Path traversal
    75	- SSRF
    76	
    77	### Performance
    78	- N+1 queries
    79	- Unnecessary memory allocations
    80	- Algorithmic complexity (O(n²) in hot paths)
    81	- Missing database indexes
    82	- Unbounded queries or loops
    83	- Resource leaks
    84	
    85	### Correctness
    86	- Edge cases (empty input, null, overflow)
    87	- Race conditions and concurrency issues
    88	- Error handling and propagation
    89	- Off-by-one errors
    90	- Type safety
    91	
    92	### Maintainability
    93	- Naming clarity
    94	- Single responsibility
    95	- Duplication
    96	- Test coverage
    97	- Documentation for non-obvious logic
    98	
    99	## Output Format
   100	
   101	Rate each dimension and provide specific, actionable findings with file and line references. Prioritize critical issues first. Always include positive observations alongside issues.
   102	
   103	exec
   104	/usr/local/bin/zsh -lc 'rg -n "the-beast-system|formalized-state|Code evidence|tab:code" /Users/mlong/.codex/memories/MEMORY.md' in /Users/mlong/Documents/Development/the-beast-system
   105	 succeeded in 0ms:
   106	75:# Task Group: the-beast-system comparative research-paper setup
   107	77:applies_to: cwd=/Users/mlong/the-beast-system; reuse_rule=project contents and research conclusions must be inspected from the current files; observed planning activity is not a validated paper or published claim.
   108	83:- extensions/skysight/resources/2026-10-22T13-40-00-mOWP-10min-memory-summary.md (cwd=/Users/mlong/the-beast-system, rollout_path=extensions/skysight/resources/2026-10-22T13-40-00-mOWP-10min-memory-summary.md, updated_at=2026-10-22T13:40:00+00:00, thread_id=None, research framing continued; no response or artifact outcome captured) [skysight memory]
   109	84:- extensions/skysight/resources/2026-10-22T13-20-00-YYQx-10min-memory-summary.md (cwd=/Users/mlong/the-beast-system, rollout_path=extensions/skysight/resources/2026-10-22T13-20-00-YYQx-10min-memory-summary.md, updated_at=2026-10-22T13:20:00+00:00, thread_id=None, project and `context` directory created; draft revised) [skysight memory]
   110	88:- `the-beast-system`, `context`, `six-pillars-beast-system-papers`, comparative research, Apple Notes, paper scoping, Parallels error 521
   111	92:- The user created `the-beast-system` and a `context` subdirectory, organized source material, revised a related Apple Notes draft, and began an initial paper-scoping session. Subsequent conceptual questions and “more context” in `six-pillars-beast-system-papers` did not yield a captured research response, source inspection, plan, or artifact. [Task 1] [skysight memory]
   112	
   113	exec
   114	/usr/local/bin/zsh -lc 'find .. -name AGENTS.md -print' in /Users/mlong/Documents/Development/the-beast-system
   115	 succeeded in 41462ms:
   116	../rustoleum/moldex-site-jss/AGENTS.md
   117	../magneton_work/tax-strategy-dashboard/node_modules/recharts/AGENTS.md
   118	../magneton_work/tax-strategy-dashboard/.next/standalone/AGENTS.md
   119	../magneton_work/tax-strategy-dashboard/AGENTS.md
   120	../magneton_work/arithmetic-positivity-program/website/node_modules/next/AGENTS.md
   121	../magneton_work/arithmetic-positivity-program/website/AGENTS.md
   122	../magneton_work/agentfolio/codex/AGENTS.md
   123	../magneton_work/agentfolio/AGENTS.md
   124	../magneton_work/adelic-polarization-conjecture/website/node_modules/next/AGENTS.md
   125	../magneton_work/riemann-hypothesis-proof/website/node_modules/next/AGENTS.md
   126	../magneton_work/riemann-hypothesis-proof/website/AGENTS.md
   127	../magneton_work/hott-riemann-hypothesis-vol6/website/AGENTS.md
   128	../magneton_work/ai-preprint-forge/AGENTS.md
   129	../MDReader/node_modules/.pnpm/cytoscape@3.34.0/node_modules/cytoscape/AGENTS.md
   130	../MDReader/AGENTS.md
   131	../ai_price_dashboard/AGENTS.md
   132	../copied-reverse-engineer/AGENTS.md
   133	../ai-tui/.external/opencode-ai-tui/opencode/packages/effect-drizzle-sqlite/AGENTS.md
   134	../ai-tui/.external/opencode-ai-tui/opencode/packages/llm/AGENTS.md
   135	../ai-tui/.external/opencode-ai-tui/opencode/packages/app/AGENTS.md
   136	../ai-tui/.external/opencode-ai-tui/opencode/packages/desktop/AGENTS.md
   137	../ai-tui/.external/opencode-ai-tui/opencode/packages/opencode/test/server/AGENTS.md
   138	../ai-tui/.external/opencode-ai-tui/opencode/packages/opencode/test/AGENTS.md
   139	../ai-tui/.external/opencode-ai-tui/opencode/packages/opencode/AGENTS.md
   140	../ai-tui/.external/opencode-ai-tui/opencode/packages/opencode/src/server/routes/instance/httpapi/AGENTS.md
   141	../ai-tui/.external/opencode-ai-tui/opencode/packages/opencode/src/session/llm/AGENTS.md
   142	../ai-tui/.external/opencode-ai-tui/opencode/AGENTS.md
   143	../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/effect-drizzle-sqlite/AGENTS.md
   144	../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/llm/AGENTS.md
   145	../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/app/AGENTS.md
   146	../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/desktop/AGENTS.md
   147	../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/opencode/test/server/AGENTS.md
   148	../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/opencode/test/AGENTS.md
   149	../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/opencode/AGENTS.md
   150	../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/opencode/src/server/routes/instance/httpapi/AGENTS.md
   151	../ai-tui/.external/opencode-ai-tui-accept/opencode/packages/opencode/src/session/llm/AGENTS.md
   152	../ai-tui/.external/opencode-ai-tui-accept/opencode/AGENTS.md
   153	../ai-tui/AGENTS.md
   154	../agenthero-platform/crates/AGENTS.md
   155	../agenthero-platform/node_modules/.pnpm/@supabase+auth-js@2.112.3/node_modules/@supabase/auth-js/AGENTS.md
   156	../agenthero-platform/node_modules/.pnpm/@supabase+realtime-js@2.112.3/node_modules/@supabase/realtime-js/AGENTS.md
   157	../agenthero-platform/node_modules/.pnpm/@supabase+postgrest-js@2.112.3/node_modules/@supabase/postgrest-js/AGENTS.md
   158	../agenthero-platform/node_modules/.pnpm/@supabase+functions-js@2.112.3/node_modules/@supabase/functions-js/AGENTS.md
   159	../agenthero-platform/node_modules/.pnpm/@supabase+storage-js@2.112.3/node_modules/@supabase/storage-js/AGENTS.md
   160	../agenthero-platform/node_modules/.pnpm/@supabase+supabase-js@2.112.3/node_modules/@supabase/supabase-js/AGENTS.md
   161	../agenthero-platform/agenthero/control-plane-web/AGENTS.md
   162	../agenthero-platform/agenthero/apps/AGENTS.md
   163	../agenthero-platform/agenthero/apps/grokrxiv/skills/skills/codex/AGENTS.md
   164	../agenthero-platform/.worktrees/codex-r9/crates/AGENTS.md
   165	../agenthero-platform/.worktrees/codex-r9/agenthero/control-plane-web/AGENTS.md
   166	../agenthero-platform/.worktrees/codex-r9/agenthero/apps/AGENTS.md
   167	../agenthero-platform/.worktrees/codex-r9/agenthero/apps/grokrxiv/skills/skills/codex/AGENTS.md
   168	../agenthero-platform/.worktrees/codex-r9/AGENTS.md
   169	../agenthero-platform/.worktrees/k1-scheduler-fixlist/crates/AGENTS.md
   170	../agenthero-platform/.worktrees/k1-scheduler-fixlist/agenthero/control-plane-web/AGENTS.md
   171	../agenthero-platform/.worktrees/k1-scheduler-fixlist/agenthero/apps/AGENTS.md
   172	../agenthero-platform/.worktrees/k1-scheduler-fixlist/agenthero/apps/grokrxiv/skills/skills/codex/AGENTS.md
   173	../agenthero-platform/.worktrees/k1-scheduler-fixlist/AGENTS.md
   174	../agenthero-platform/.worktrees/batch-27/crates/AGENTS.md
   175	../agenthero-platform/.worktrees/batch-27/node_modules/.pnpm/@supabase+auth-js@2.112.3/node_modules/@supabase/auth-js/AGENTS.md
   176	../agenthero-platform/.worktrees/batch-27/node_modules/.pnpm/@supabase+realtime-js@2.112.3/node_modules/@supabase/realtime-js/AGENTS.md
   177	../agenthero-platform/.worktrees/batch-27/node_modules/.pnpm/@supabase+postgrest-js@2.112.3/node_modules/@supabase/postgrest-js/AGENTS.md
   178	../agenthero-platform/.worktrees/batch-27/node_modules/.pnpm/@supabase+functions-js@2.112.3/node_modules/@supabase/functions-js/AGENTS.md
   179	../agenthero-platform/.worktrees/batch-27/node_modules/.pnpm/@supabase+storage-js@2.112.3/node_modules/@supabase/storage-js/AGENTS.md
   180	../agenthero-platform/.worktrees/batch-27/node_modules/.pnpm/@supabase+supabase-js@2.112.3/node_modules/@supabase/supabase-js/AGENTS.md
   181	../agenthero-platform/.worktrees/batch-27/agenthero/control-plane-web/AGENTS.md
   182	../agenthero-platform/.worktrees/batch-27/agenthero/apps/AGENTS.md
   183	../agenthero-platform/.worktrees/batch-27/agenthero/apps/grokrxiv/skills/skills/codex/AGENTS.md
   184	../agenthero-platform/.worktrees/batch-27/AGENTS.md
   185	../agenthero-platform/AGENTS.md
   186	../agenthero-platform/.superpowers/sdd/2026-09-12-agentapp-v2-part3-integration/task-11ae-ae1-resume-evidence/single-agh-runtime-runs/canonical-ae1-1/catalog-source/grokrxiv/skills/skills/codex/AGENTS.md
   187	../agenthero-platform/.superpowers/sdd/2026-09-12-agentapp-v2-part3-integration/task-11ae-ae1-resume-evidence/single-agh-runtime-runs/canonical-ae1-1/catalog/agenthero/apps/grokrxiv/skills/skills/codex/AGENTS.md
   188	../agenthero-platform/.superpowers/sdd/2026-09-16-agent-owned-git-workflow-plan/market-brief-runs/job-a-install/pre-restage-backup/catalog-source/grokrxiv/skills/skills/codex/AGENTS.md
   189	../agenthero-platform/.superpowers/sdd/2026-09-16-agent-owned-git-workflow-plan/market-brief-runs/job-a-install/pre-restage-backup/catalog-apps/grokrxiv/skills/skills/codex/AGENTS.md
   190	../CatDB/.worktrees/dev/AGENTS.md
   191	../CatDB/AGENTS.md
   192	../CatDB-Web/node_modules/.pnpm/cytoscape@3.34.0/node_modules/cytoscape/AGENTS.md
   193	../yonedarepo/plugins/codex/AGENTS.md
   194	../yonedarepo/.local/stream-c-egress/contribution/AGENTS.md
   195	../yonedarepo/.local/public-source-final-code/fixtures/website/AGENTS.md
   196	../yonedarepo/.local/public-source-final-code/AGENTS.md
   197	../yonedarepo/.local/export-budget-c3433d2/fixtures/website/AGENTS.md
   198	../yonedarepo/.local/export-budget-c3433d2/AGENTS.md
   199	../yonedarepo/.local/submission-export-322ef3f/fixtures/website/AGENTS.md
   200	../yonedarepo/.local/submission-export-322ef3f/AGENTS.md
   201	../yonedarepo/.local/submission-export-48b5618/fixtures/website/AGENTS.md
   202	../yonedarepo/.local/submission-export-48b5618/AGENTS.md
   203	../yonedarepo/.local/public-source-r14-4d4cf2b/fixtures/website/AGENTS.md
   204	../yonedarepo/.local/public-source-r14-4d4cf2b/AGENTS.md
   205	../yonedarepo/.local/export-462f439/fixtures/website/AGENTS.md
   206	../yonedarepo/.local/export-462f439/AGENTS.md
   207	../yonedarepo/.local/public-source-autonomy-13eccb1/fixtures/website/AGENTS.md
   208	../yonedarepo/.local/public-source-autonomy-13eccb1/AGENTS.md
   209	../yonedarepo/.local/submission-publish-48b5618/fixtures/website/AGENTS.md
   210	../yonedarepo/.local/submission-publish-48b5618/AGENTS.md
   211	../yonedarepo/.local/export-comparison-f0f1307/fixtures/website/AGENTS.md
   212	../yonedarepo/.local/export-comparison-f0f1307/AGENTS.md
   213	../yonedarepo/.local/export-autonomy-13eccb1/fixtures/website/AGENTS.md
   214	../yonedarepo/.local/export-autonomy-13eccb1/AGENTS.md
   215	../yonedarepo/.local/submission-export-final-e8cc3f5/fixtures/website/AGENTS.md
   216	../yonedarepo/.local/submission-export-final-e8cc3f5/AGENTS.md
   217	../yonedarepo/.local/public-source-api-r12-3c52f65/fixtures/website/AGENTS.md
   218	../yonedarepo/.local/public-source-api-r12-3c52f65/AGENTS.md
   219	../yonedarepo/.local/public-source-api-r11-ebdac98/fixtures/website/AGENTS.md
   220	../yonedarepo/.local/public-source-api-r11-ebdac98/AGENTS.md
   221	../yonedarepo/.local/export-current-checked-repair-20261013/fixtures/website/AGENTS.md
   222	../yonedarepo/.local/export-current-checked-repair-20261013/AGENTS.md
   223	../yonedarepo/.local/export-simple-workflow-35e2783/fixtures/website/AGENTS.md
   224	../yonedarepo/.local/export-simple-workflow-35e2783/AGENTS.md
   225	../yonedarepo/.local/public-source/fixtures/website/AGENTS.md
   226	../yonedarepo/.local/public-source/AGENTS.md
   227	../yonedarepo/.local/submission-export-fc5126c/fixtures/website/AGENTS.md
   228	../yonedarepo/.local/submission-export-fc5126c/AGENTS.md
   229	../yonedarepo/.local/public-source-api-r9-ef311f6/fixtures/website/AGENTS.md
   230	../yonedarepo/.local/public-source-api-r9-ef311f6/AGENTS.md
   231	../yonedarepo/.local/export-autonomy-0a0eeb5/fixtures/website/AGENTS.md
   232	../yonedarepo/.local/export-autonomy-0a0eeb5/AGENTS.md
   233	../yonedarepo/.local/export-r4-82d900f/fixtures/website/AGENTS.md
   234	../yonedarepo/.local/export-r4-82d900f/AGENTS.md
   235	../yonedarepo/.local/export-final-4555ce9/fixtures/website/AGENTS.md
   236	../yonedarepo/.local/export-final-4555ce9/AGENTS.md
   237	../yonedarepo/.local/layout-fresh-checkout/fixtures/website/AGENTS.md
   238	../yonedarepo/.local/layout-fresh-checkout/AGENTS.md
   239	../yonedarepo/.local/public-source-modern-picker-9a30eca/fixtures/website/AGENTS.md
   240	../yonedarepo/.local/public-source-modern-picker-9a30eca/AGENTS.md
   241	../yonedarepo/.local/comparison-acceptance/calibration/correct/AGENTS.md
   242	../yonedarepo/.local/comparison-acceptance/calibration/bundle/AGENTS.md
   243	../yonedarepo/.local/comparison-acceptance/calibration/missing/AGENTS.md
   244	../yonedarepo/.local/comparison-acceptance/calibration/trim_only/AGENTS.md
   245	../yonedarepo/.local/public-source-final-wave/fixtures/website/AGENTS.md
   246	../yonedarepo/.local/public-source-final-wave/AGENTS.md
   247	../yonedarepo/.local/export-comparison-ebb08f4/fixtures/website/AGENTS.md
   248	../yonedarepo/.local/export-comparison-ebb08f4/AGENTS.md
   249	../yonedarepo/.local/export-autonomy-acbb3b1/fixtures/website/AGENTS.md
   250	../yonedarepo/.local/export-autonomy-acbb3b1/AGENTS.md
   251	../yonedarepo/.local/submission-export-native-final/fixtures/website/AGENTS.md
   252	../yonedarepo/.local/submission-export-native-final/AGENTS.md
   253	../yonedarepo/.local/export-07b3a8f/fixtures/website/AGENTS.md
   254	../yonedarepo/.local/export-07b3a8f/AGENTS.md
   255	../yonedarepo/.local/source-api/hosted-compare/calibration/correct/AGENTS.md
   256	../yonedarepo/.local/source-api/hosted-compare/calibration/bundle/AGENTS.md
   257	../yonedarepo/.local/source-api/hosted-compare/calibration/missing/AGENTS.md
   258	../yonedarepo/.local/source-api/hosted-compare/calibration/trim_only/AGENTS.md
   259	../yonedarepo/.local/export-simple-workflow-final-20261013/fixtures/website/AGENTS.md
   260	../yonedarepo/.local/export-simple-workflow-final-20261013/AGENTS.md

exec
/usr/local/bin/zsh -lc "nl -ba /Users/mlong/.codex/memories/MEMORY.md | sed -n '72,94p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
    72	
    73	- Symptom: selecting a tools image or completing VM configuration is called a working guest environment. Fix: verify tools installer completion and actual guest-app/settings behavior separately; neither was captured here. [Task 1] [skysight memory]
    74	
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
    94	## Failures and how to do differently

exec
/usr/local/bin/zsh -lc "rg -n '"'^def (conversion_step|comparison_matrix|foothold_bound|negative_feedback_example)'"' model/beast_system/dynamics.py; rg -n '"'^def test_(t_maps_cube_into_itself_and_is_dominated_by_a|rho_below_one_means_reversible|full_contestability_drains_pillar_and_caps_integration|rho_nonincreasing_in_each_q|foothold_never_vanishes)'"' model/tests/test_conversion.py; rg -n '"'^def test_positive_links_do_not_guarantee_persistence'"' model/tests/test_dynamics_regimes.py" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
127:def negative_feedback_example(
185:def conversion_step(y: np.ndarray, delta: np.ndarray, K: np.ndarray) -> np.ndarray:
194:def comparison_matrix(delta: np.ndarray, K: np.ndarray) -> np.ndarray:
241:def foothold_bound(y0: np.ndarray, delta: np.ndarray, K: np.ndarray) -> Foothold:
36:def test_t_maps_cube_into_itself_and_is_dominated_by_a():
48:def test_rho_below_one_means_reversible():
56:def test_full_contestability_drains_pillar_and_caps_integration():
68:def test_rho_nonincreasing_in_each_q():
80:def test_foothold_never_vanishes():
32:def test_positive_links_do_not_guarantee_persistence():

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/indices.py | sed -n '90,330p'; nl -ba model/tests/test_indices.py | sed -n '35,245p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '540,770p'; nl -ba model/tests/test_necessity.py | sed -n '235,385p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '360,540p'; nl -ba model/tests/test_necessity.py | sed -n '1,110p'; nl -ba model/tests/test_necessity.py | sed -n '140,215p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '630,765p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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

exec
/usr/local/bin/zsh -lc "nl -ba model/tests/test_necessity.py | sed -n '235,385p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '215,285p'; nl -ba model/tests/test_necessity.py | sed -n '110,145p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/necessity.py | sed -n '744,785p'; nl -ba model/tests/test_necessity.py | sed -n '371,410p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/capture.py | sed -n '35,125p'; nl -ba model/beast_system/capture.py | sed -n '318,365p'; nl -ba model/tests/test_capture.py | sed -n '20,38p'; nl -ba model/tests/test_capture.py | sed -n '80,87p'; nl -ba model/tests/test_capture.py | sed -n '124,136p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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
    80	
    81	def test_counter_model_robust_to_thresholds():
    82	    for u_star, i_star in [(0.0, 0.0), (0.1, 0.1), (0.5, 0.5), (0.9, 0.9), (1.0, 1.0), (0.0, 1.0)]:
    83	        assert a_does_not_imply_b(CaptureThresholds(u_star, i_star)).demonstrates_non_implication
    84	
    85	
    86	def test_capture_link_flags_must_be_bool():
    87	    with pytest.raises(TypeError):
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

codex
The necessity, admissibility, index, and capture rows now line up closely with the cited assertions. I’m at the representation/uniqueness rows, where the key distinction is whether a test merely checks selected fixtures or actually exercises the claimed equivalence/invariant.
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/representation.py | sed -n '1,220p'; nl -ba model/tests/test_representation.py | sed -n '1,145p'" in /Users/mlong/Documents/Development/the-beast-system
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

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/representation.py | sed -n '220,530p'; nl -ba model/tests/test_representation.py | sed -n '200,270p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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
   365	def _kv(row: Mapping[Label, float], m: Label) -> tuple[int, float]:
   366	    """kappa entry with an explicit presence flag: a missing column is (0, 0.0), a present
   367	    one (1, value), so missing and explicit zero stay distinct (as in ``find_bijection``)."""
   368	    return (1, _r(row[m])) if m in row else (0, 0.0)
   369	
   370	
   371	def _same(a: float, b: float) -> bool:
   372	    return abs(a - b) <= _ATOL
   373	
   374	
   375	def _actor_signature(F: FormalizedStructure, k: int, with_layers: bool) -> tuple:
   376	    v = F.actors[k]
   377	    sig = (
   378	        tuple(sorted(F.roles[v])),
   379	        tuple(_r(F.shares[m][v]) for m in F.pillars),
   380	        tuple(sorted((m, a == v, b == v) for a, b, m in F.links if v in (a, b))),
   381	        tuple(sorted(tuple(_kv(r, m) for m in F.pillars)
   382	                     for S, r in F.kappa.items() if v in S)),
   383	    )
   384	    if with_layers:
   385	        sig += tuple((tuple(sorted(_r(x) for x in F.layers[m][k])),
   386	                      tuple(sorted(_r(x) for x in F.layers[m][:, k]))) for m in F.pillars)
   387	    return sig
   388	
   389	
   390	def find_bijection(F: FormalizedStructure, G: FormalizedStructure,
   391	                   with_layers: bool) -> dict[str, str] | None:
   392	    """An actor bijection phi: V_F -> V_G under which roles, shares, Q, omega, kappa
   393	    (transported: kappa_F(S) = kappa_G(phi(S))), links and D agree, and, if ``with_layers``,
   394	    every layer entry. None if there is none.
   395	
   396	    Numbers are compared EXACTLY after quantization to 12 decimals (``_r``), the same
   397	    normalization the canonical form uses, so equality is an equivalence relation.
   398	
   399	    Backtracking within classes of equal actor signatures; the identity on names is tried
   400	    first. Both structures must be ``well_formed``.
   401	    """
   402	    if not (well_formed(F) and well_formed(G)):
   403	        return None
   404	    if F.pillars != G.pillars or len(F.actors) != len(G.actors) or F.arcs != G.arcs:
   405	        return None
   406	    if any(_r(F.contestability[m]) != _r(G.contestability[m])
   407	           or _r(F.weights[m]) != _r(G.weights[m]) for m in F.pillars):
   408	        return None
   409	    if len(F.kappa) != len(G.kappa) or len(F.links) != len(G.links):
   410	        return None
   411	    sig_f = [_actor_signature(F, k, with_layers) for k in range(len(F.actors))]
   412	    sig_g = [_actor_signature(G, k, with_layers) for k in range(len(G.actors))]
   413	    if sorted(sig_f) != sorted(sig_g):
   414	        return None
   415	    gi = {v: k for k, v in enumerate(G.actors)}
   416	    fi = {v: k for k, v in enumerate(F.actors)}
   417	    order = sorted(range(len(F.actors)), key=lambda k: sig_f[k])
   418	    assign: dict[int, int] = {}
   419	    used: set[int] = set()
   420	
   421	    def consistent(i: int, j: int) -> bool:
   422	        if with_layers:
   423	            for i2, j2 in assign.items():
   424	                for m in F.pillars:
   425	                    if (_r(F.layers[m][i, i2]) != _r(G.layers[m][j, j2])
   426	                            or _r(F.layers[m][i2, i]) != _r(G.layers[m][j2, j])):
   427	                        return False
   428	        mapped = {**assign, i: j}
   429	        for a, b, m in F.links:
   430	            ia, ib = fi[a], fi[b]
   431	            if ia in mapped and ib in mapped:
   432	                if (G.actors[mapped[ia]], G.actors[mapped[ib]], m) not in G.links:
   433	                    return False
   434	        return True
   435	
   436	    def kappa_ok() -> bool:
   437	        to_g = {F.actors[i]: G.actors[j] for i, j in assign.items()}
   438	        for S, row in F.kappa.items():
   439	            other = G.kappa.get(frozenset(to_g[v] for v in S))
   440	            if other is None or set(other) != set(row):
   441	                return False
   442	            if any(_r(row[m]) != _r(other[m]) for m in row):
   443	                return False
   444	        return True
   445	
   446	    def search(pos: int) -> bool:
   447	        if pos == len(order):
   448	            return kappa_ok()
   449	        i = order[pos]
   450	        cands = [j for j in range(len(G.actors)) if j not in used and sig_g[j] == sig_f[i]]
   451	        pref = gi.get(F.actors[i])
   452	        if pref in cands:
   453	            cands.remove(pref)
   454	            cands.insert(0, pref)
   455	        for j in cands:
   456	            if consistent(i, j):
   457	                assign[i] = j
   458	                used.add(j)
   459	                if search(pos + 1):
   460	                    return True
   461	                del assign[i]
   462	                used.discard(j)
   463	        return False
   464	
   465	    if not search(0):
   466	        return None
   467	    return {F.actors[i]: G.actors[j] for i, j in assign.items()}
   468	
   469	
   470	def equivalent_A(F: FormalizedStructure, G: FormalizedStructure) -> bool:  # noqa: N802
   471	    """F and G agree on roles, shares, Q, omega, kappa, links and D under an actor bijection
   472	    (layers not compared; see ``uniqueness.p_equal`` for the version with layers)."""
   473	    return find_bijection(F, G, with_layers=False) is not None
   474	
   475	
   476	# Coarsenings (minimality) ------------------------------------------------------------------
   477	
   478	
   479	def drop(F: FormalizedStructure, m: Label) -> FormalizedStructure:
   480	    """Delete pillar m: its layer, shares, Q, kappa column and every hyperarc involving m.
   481	
   482	    Remaining weights are renormalized to sum 1.
   483	    """
   484	    if m not in F.pillars:
   485	        raise ValueError(f"unknown pillar {m!r}")
   486	    keep = tuple(p for p in F.pillars if p != m)
   487	    total = sum(F.weights[p] for p in keep)
   488	    weights = {p: (F.weights[p] / total if total > 0 else 1.0 / len(keep)) for p in keep}
   489	    return FormalizedStructure(
   490	        actors=F.actors, pillars=keep,
   491	        roles={v: ps - {m} for v, ps in F.roles.items()},
   492	        layers={p: F.layers[p] for p in keep},
   493	        shares={p: dict(F.shares[p]) for p in keep},
   494	        contestability={p: F.contestability[p] for p in keep},
   495	        weights=weights,
   496	        kappa={s: {p: row.get(p, 0.0) for p in keep} for s, row in F.kappa.items()},
   497	        links=frozenset(lk for lk in F.links if lk[2] != m),
   498	        arcs=frozenset((t, h) for t, h in F.arcs if h != m and m not in t),
   499	    )
   500	
   501	
   502	def merge(F: FormalizedStructure, m: Label, n: Label, lam: float) -> FormalizedStructure:
   503	    """Replace m, n by one pillar 'm+n': holders united, shares, layers, Q and kappa mixed with
   504	    weight lam on m; omega_m + omega_n; arcs relabeled, self-loops removed."""
   505	    if m == n or m not in F.pillars or n not in F.pillars:
   506	        raise ValueError("merge needs two distinct existing pillars")
   507	    lam = validate_unit_interval(lam, "lam")
   508	    new = f"{m}+{n}"
   509	    keep = tuple(new if p == m else p for p in F.pillars if p != n)
   510	    relabel = lambda p: new if p in (m, n) else p  # noqa: E731
   511	
   512	    def mix(a: float, b: float) -> float:
   513	        return lam * a + (1.0 - lam) * b
   514	
   515	    shares = {p: dict(F.shares[p]) for p in keep if p != new}
   516	    shares[new] = {v: mix(F.shares[m].get(v, 0.0), F.shares[n].get(v, 0.0)) for v in F.actors}
   517	    layers = {p: F.layers[p] for p in keep if p != new}
   518	    layers[new] = lam * F.layers[m] + (1.0 - lam) * F.layers[n]
   519	    contest = {p: F.contestability[p] for p in keep if p != new}
   520	    contest[new] = mix(F.contestability[m], F.contestability[n])
   521	    weights = {p: F.weights[p] for p in keep if p != new}
   522	    weights[new] = F.weights[m] + F.weights[n]
   523	    kappa = {}
   524	    for s, row in F.kappa.items():
   525	        r = {p: row.get(p, 0.0) for p in keep if p != new}
   526	        r[new] = mix(row.get(m, 0.0), row.get(n, 0.0))
   527	        kappa[s] = r
   528	    arcs = set()
   529	    for t, h in F.arcs:
   530	        t2, h2 = frozenset(relabel(x) for x in t), relabel(h)
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

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/uniqueness.py | sed -n '1,300p'; nl -ba model/tests/test_uniqueness.py | sed -n '1,180p'" in /Users/mlong/Documents/Development/the-beast-system
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
    31	    _kv,
    32	    find_bijection,
    33	    represent,
    34	    structurally_equal,
    35	    well_formed,
    36	)
    37	
    38	_ROUND = 12
    39	_ATOL = 1e-9
    40	Coarsening = Mapping[Label, "Label | None"]
    41	
    42	
    43	# Coarsening --------------------------------------------------------------------------------
    44	
    45	
    46	def _blocks(F: FormalizedStructure, c: Coarsening) -> dict[Label, list[Label]]:
    47	    if set(c) != set(F.pillars):
    48	        raise ValueError("a coarsening must assign every pillar (None drops it)")
    49	    blocks: dict[Label, list[Label]] = {}
    50	    for m in F.pillars:
    51	        if c[m] is not None:
    52	            blocks.setdefault(c[m], []).append(m)
    53	    return blocks
    54	
    55	
    56	def _block_weights(blocks: Mapping[Label, list[Label]],
    57	                   lam: Mapping[Label, float] | None) -> dict[Label, float]:
    58	    out: dict[Label, float] = {}
    59	    for members in blocks.values():
    60	        for m in members:
    61	            out[m] = 1.0 / len(members) if lam is None else float(lam[m])
    62	        if any(not math.isfinite(out[m]) or out[m] <= 0.0 for m in members):
    63	            raise ValueError("lam_m must be positive")
    64	        if abs(sum(out[m] for m in members) - 1.0) > _ATOL:
    65	            raise ValueError("lam must sum to 1 within each block")
    66	    return out
    67	
    68	
    69	def coarsen(F: FormalizedStructure, c: Coarsening,
    70	            lam: Mapping[Label, float] | None = None) -> FormalizedStructure:
    71	    """Coarsen F by c: M -> K or None (drop), lam-weighted within each block (default equal).
    72	
    73	    Block holders are the union; shares, layers, Q and kappa are lam-weighted sums; omega_k is
    74	    the sum of omega_m (not renormalized); hyperarcs with no dropped element map to their image
    75	    under c, self-loops removed; links in dropped pillars are removed.
    76	    """
    77	    blocks = _blocks(F, c)
    78	    w = _block_weights(blocks, lam)
    79	    keys = tuple(blocks)
    80	
    81	    def mix(get: Callable[[Label], float], k: Label) -> float:
    82	        return sum(w[m] * get(m) for m in blocks[k])
    83	
    84	    shares = {k: {v: mix(lambda m: F.shares[m].get(v, 0.0), k) for v in F.actors} for k in keys}
    85	    layers = {k: sum(w[m] * F.layers[m] for m in blocks[k]) for k in keys}
    86	    arcs = set()
    87	    for tail, head in F.arcs:
    88	        if c[head] is None or any(c[t] is None for t in tail):
    89	            continue
    90	        t2, h2 = frozenset(c[t] for t in tail), c[head]
    91	        if h2 not in t2:
    92	            arcs.add((t2, h2))
    93	    return FormalizedStructure(
    94	        actors=F.actors, pillars=keys,
    95	        roles={v: frozenset(c[m] for m in ps if c[m] is not None) for v, ps in F.roles.items()},
    96	        layers=layers, shares=shares,
    97	        contestability={k: mix(lambda m: F.contestability[m], k) for k in keys},
    98	        weights={k: sum(F.weights[m] for m in blocks[k]) for k in keys},
    99	        kappa={s: {k: mix(lambda m: row.get(m, 0.0), k) for k in keys} for s, row in F.kappa.items()},
   100	        links=frozenset((a, b, c[m]) for a, b, m in F.links if c[m] is not None),
   101	        arcs=frozenset(arcs),
   102	    )
   103	
   104	
   105	IDENTITY: dict[Label, Label] = {m: m for m in M_LABELS}
   106	
   107	
   108	def phi(record: CodedRecord) -> FormalizedStructure:
   109	    """Phi = coarsen(represent(G), identity)."""
   110	    return coarsen(represent(record), IDENTITY)
   111	
   112	
   113	# P-equality --------------------------------------------------------------------------------
   114	
   115	
   116	def _r(x: float) -> float:
   117	    return round(float(x), _ROUND) + 0.0
   118	
   119	
   120	def p_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   121	    """P(F) = P(G): roles, shares, Q, omega, kappa (transported), links, D and layers agree
   122	    under an actor bijection (``representation.find_bijection`` with layers)."""
   123	    return find_bijection(F, G, with_layers=True) is not None
   124	
   125	
   126	def _global(F: FormalizedStructure) -> tuple:
   127	    return (
   128	        F.pillars,
   129	        tuple(_r(F.contestability[m]) for m in F.pillars),
   130	        tuple(_r(F.weights[m]) for m in F.pillars),
   131	        tuple(sorted((tuple(sorted(S)), tuple(_kv(r, m) for m in F.pillars))
   132	                     for S, r in F.kappa.items())),
   133	        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
   134	        len(F.actors),
   135	    )
   136	
   137	
   138	def freeze(F: FormalizedStructure) -> tuple:
   139	    """Hashable encoding of F with its actor names (equality = identity on names)."""
   140	    return (
   141	        F.actors, F.pillars,
   142	        tuple(tuple(sorted(F.roles[v])) for v in F.actors),
   143	        tuple(tuple(_r(F.shares[m][v]) for v in F.actors) for m in F.pillars),
   144	        tuple(tuple(_r(x) for x in F.layers[m].ravel()) for m in F.pillars),
   145	        _global(F), tuple(sorted(F.links)),
   146	    )
   147	
   148	
   149	# Factorization through Phi -----------------------------------------------------------------
   150	
   151	
   152	@dataclass(frozen=True)
   153	class Factorization:
   154	    """alpha factors through Phi on the fixtures: alpha(G) = alpha(G2) implies P(G) = P(G2)
   155	    (``well_defined``: h(alpha(G)) = Phi(G) is a function); ``bijective``: h is also
   156	    injective onto the P-classes of the fixtures."""
   157	
   158	    well_defined: bool
   159	    bijective: bool
   160	
   161	
   162	def factor_through_phi(alpha: Callable[[CodedRecord], object],
   163	                       records: Sequence[CodedRecord]) -> Factorization:
   164	    """Check that the P-preserving abstraction ``alpha`` factors through Phi on ``records``."""
   165	    images = [alpha(r) for r in records]
   166	    phis = [phi(r) for r in records]
   167	    well_defined = injective = True
   168	    for i in range(len(records)):
   169	        for j in range(i + 1, len(records)):
   170	            same_alpha = images[i] == images[j]
   171	            same_p = p_equal(phis[i], phis[j])
   172	            if same_alpha and not same_p:
   173	                well_defined = False
   174	            if same_p and not same_alpha:
   175	                injective = False
   176	    return Factorization(well_defined, well_defined and injective)
   177	
   178	
   179	def alpha_represent(record: CodedRecord) -> tuple:
   180	    """NOT P-preserving (negative control): the frozen profile keeps actor names, so two
   181	    actor-renamed copies of one system get different values."""
   182	    return freeze(represent(record))
   183	
   184	
   185	# Canonical form (a complete invariant of P) ------------------------------------------------
   186	
   187	
   188	def _encode(F: FormalizedStructure, order: Sequence[int]) -> tuple:
   189	    """Name-free encoding of F with actors listed in ``order``."""
   190	    pos = {F.actors[k]: i for i, k in enumerate(order)}
   191	    return (
   192	        F.pillars,
   193	        tuple(tuple(sorted(F.roles[F.actors[k]])) for k in order),
   194	        tuple(tuple(_r(F.shares[m][F.actors[k]]) for k in order) for m in F.pillars),
   195	        tuple(tuple(_r(F.layers[m][i, j]) for i in order for j in order) for m in F.pillars),
   196	        tuple(_r(F.contestability[m]) for m in F.pillars),
   197	        tuple(_r(F.weights[m]) for m in F.pillars),
   198	        tuple(sorted((tuple(sorted(pos[v] for v in S)),
   199	                      tuple(_kv(r, m) for m in F.pillars)) for S, r in F.kappa.items())),
   200	        tuple(sorted((pos[a], pos[b], m) for a, b, m in F.links)),
   201	        tuple(sorted((tuple(sorted(t)), h) for t, h in F.arcs)),
   202	    )
   203	
   204	
   205	def _relabel(sigs: Sequence) -> list[int]:
   206	    table = {sg: c for c, sg in enumerate(sorted(set(sigs)))}
   207	    return [table[sg] for sg in sigs]
   208	
   209	
   210	def _initial_colors(F: FormalizedStructure) -> list[int]:
   211	    return _relabel([(tuple(sorted(F.roles[v])), tuple(_r(F.shares[m][v]) for m in F.pillars))
   212	                     for v in F.actors])
   213	
   214	
   215	def _refine(F: FormalizedStructure, colors: list[int]) -> list[int]:
   216	    """Colour refinement from ``colors``, iterated until the partition is stable. The result
   217	    depends only on the structure and the input colouring, never on actor names."""
   218	    n = len(F.actors)
   219	    idx = {v: k for k, v in enumerate(F.actors)}
   220	    while True:
   221	        sigs = []
   222	        for k in range(n):
   223	            v = F.actors[k]
   224	            sigs.append((
   225	                colors[k],
   226	                tuple(sorted((colors[j],
   227	                              tuple(_r(F.layers[m][k, j]) for m in F.pillars),
   228	                              tuple(_r(F.layers[m][j, k]) for m in F.pillars))
   229	                             for j in range(n) if j != k)),
   230	                tuple(sorted((colors[idx[b]], m, "out") for a, b, m in F.links if a == v)
   231	                      + sorted((colors[idx[a]], m, "in") for a, b, m in F.links if b == v)),
   232	                tuple(sorted((tuple(sorted(colors[idx[u]] for u in S)),
   233	                              tuple(_kv(r, m) for m in F.pillars))
   234	                             for S, r in F.kappa.items() if v in S)),
   235	            ))
   236	        new = _relabel(sigs)
   237	        if len(set(new)) == len(set(colors)):
   238	            return new
   239	        colors = new
   240	
   241	
   242	def _interchangeable(F: FormalizedStructure, colors: list[int], cls: list[int]) -> bool:
   243	    """True if every transposition (cls[0] cls[t]) is an automorphism of F that preserves
   244	    ``colors``; these transpositions generate all permutations of the class."""
   245	    order = sorted(range(len(F.actors)), key=lambda k: (colors[k], k))
   246	    ref = _encode(F, order)
   247	    pos = {k: i for i, k in enumerate(order)}
   248	    for other in cls[1:]:
   249	        swapped = list(order)
   250	        a, b = pos[cls[0]], pos[other]
   251	        swapped[a], swapped[b] = swapped[b], swapped[a]
   252	        if _encode(F, swapped) != ref:
   253	            return False
   254	    return True
   255	
   256	
   257	def canonical_form(F: FormalizedStructure) -> tuple:
   258	    """A complete invariant of P: canonical_form(F) == canonical_form(G) iff p_equal(F, G).
   259	
   260	    Individualization-refinement: refine colours; if every class is a singleton, encode in
   261	    colour order; otherwise branch on each member of the first smallest non-singleton class
   262	    (individualize it, refine, recurse) and return the lexicographic minimum. When all
   263	    transpositions within that class are automorphisms, the branches give identical results
   264	    and only one is explored. Total on well-formed structures (worst-case exponential time).
   265	    Numbers enter quantized to 12 decimals, as in ``p_equal``.
   266	    """
   267	    if not well_formed(F):
   268	        raise ValueError("canonical_form needs a well-formed structure")
   269	    n = len(F.actors)
   270	    if n == 0:
   271	        return _encode(F, [])
   272	
   273	    def search(colors: list[int]) -> tuple:
   274	        colors = _refine(F, colors)
   275	        classes: dict[int, list[int]] = {}
   276	        for k, c in enumerate(colors):
   277	            classes.setdefault(c, []).append(k)
   278	        open_ = [cl for c, cl in sorted(classes.items()) if len(cl) > 1]
   279	        if not open_:
   280	            return _encode(F, sorted(range(n), key=lambda k: colors[k]))
   281	        cls = min(open_, key=len)
   282	        branches = cls[:1] if _interchangeable(F, colors, cls) else cls
   283	        best = None
   284	        for v in branches:
   285	            individualized = _relabel([(colors[k], 0 if k == v else 1) for k in range(n)])
   286	            enc = search(individualized)
   287	            if best is None or enc < best:
   288	                best = enc
   289	        return best
   290	
   291	    return search(_initial_colors(F))
   292	
   293	
   294	def alpha_canonical(record: CodedRecord) -> tuple:
   295	    """A P-preserving abstraction: the canonical form of represent(G)."""
   296	    return canonical_form(represent(record))
   297	
   298	
   299	def alpha_canonical_phi(record: CodedRecord) -> tuple:
   300	    """A second, differently built one: the canonical form of Phi(G) (coarsen by identity)
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

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/uniqueness.py | sed -n '300,530p'; nl -ba model/tests/test_uniqueness.py | sed -n '180,315p'; nl -ba model/tests/test_uniqueness.py | sed -n '350,390p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   300	    """A second, differently built one: the canonical form of Phi(G) (coarsen by identity)
   301	    plus a redundant field (the number of hyperarcs)."""
   302	    F = phi(record)
   303	    return (canonical_form(F), len(F.arcs))
   304	
   305	
   306	def rename_record(record: CodedRecord, mapping: Mapping[str, str]) -> CodedRecord:
   307	    """The same coded system with actors renamed by ``mapping`` (missing names kept)."""
   308	    ren = lambda v: mapping.get(v, v)  # noqa: E731
   309	    sys_ = record.system
   310	    names = set(represent(record).actors)
   311	    if len({ren(v) for v in names}) != len(names):
   312	        raise ValueError("renaming must be injective on the record's actors")
   313	    practices = tuple(
   314	        Practice(p.description, p.solves, frozenset(ren(h) for h in p.holders), p.formal,
   315	                 p.source)
   316	        for p in sys_.practices
   317	    )
   318	    system = GovernanceSystem(sys_.name, sys_.persistent, sys_.axioms, practices,
   319	                              sys_.absent_incidences, sys_.note)
   320	    links = tuple(CaptureLink(ren(lk.source), ren(lk.target), lk.pillar, lk.privileged_access,
   321	                              lk.weakens_accountability, lk.material_evidence, lk.evidence)
   322	                  for lk in record.links)
   323	    coalitions = None if record.coalitions is None else {
   324	        frozenset(ren(v) for v in S): row for S, row in record.coalitions.items()}
   325	    return CodedRecord(system, {m: {ren(v): x for v, x in sh.items()}
   326	                                for m, sh in record.shares.items()},
   327	                       record.contestability, record.weights, coalitions, links)
   328	
   329	
   330	# Witnesses ---------------------------------------------------------------------------------
   331	
   332	
   333	def witness_record(ab_shares: Mapping[Label, tuple[float, float]], q: float = 0.5,
   334	                   links: Iterable = ()) -> CodedRecord:
   335	    """Witness system (Part VII Prop 7.5, Prop 10.1): actors a and b perform exactly the
   336	    pillars in ``ab_shares`` with shares (s^m_a, s^m_b); actor c alone performs every other
   337	    pillar (share 1). Ax1..Ax6 and X1, X2, X3, X5 hold, so Proposition A holds. Both members
   338	    of a witness pair use the same keys, hence the same actor set and role map.
   339	    """
   340	    if not ab_shares or not set(ab_shares) <= set(M_LABELS):
   341	        raise ValueError("ab_shares must name at least one pillar label")
   342	    practices = tuple(
   343	        Practice(f"{m.label} practice", PILLAR_TO_AXIOM[m],
   344	                 frozenset({"a", "b"}) if m.name in ab_shares else frozenset({"c"}),
   345	                 source="synthetic witness")
   346	        for m in PILLARS
   347	    )
   348	    system = GovernanceSystem("witness", True, EXTENDED_AXIOMS, practices)
   349	    shares = {m: (dict(zip(("a", "b"), ab_shares[m.name])) if m.name in ab_shares
   350	                  else {"c": 1.0}) for m in PILLARS}
   351	    return CodedRecord(system, shares, {m: q for m in PILLARS}, links=tuple(links))
   352	
   353	
   354	def _drop_witness(m: Label, l0: Label) -> tuple[CodedRecord, CodedRecord]:
   355	    """Drop m: G1 s^m = (1, 0), G2 s^m = (1/2, 1/2); a and b also hold (1/2, 1/2) in the
   356	    retained pillar l0 in both, so b is an actor of G1 too."""
   357	    return (witness_record({m: (1.0, 0.0), l0: (0.5, 0.5)}),
   358	            witness_record({m: (0.5, 0.5), l0: (0.5, 0.5)}))
   359	
   360	
   361	def _merge_witness(m: Label, n: Label, mu: float) -> tuple[CodedRecord, CodedRecord]:
   362	    """Merge {m, n}: G1 s^m = (1, 0), s^n = (0, 1); G2 s^m = s^n = (mu, 1 - mu)."""
   363	    return (witness_record({m: (1.0, 0.0), n: (0.0, 1.0)}),
   364	            witness_record({m: (mu, 1.0 - mu), n: (mu, 1.0 - mu)}))
   365	
   366	
   367	def witness_coarsening(c: Coarsening, lam: Mapping[Label, float] | None = None
   368	                       ) -> tuple[CodedRecord, CodedRecord]:
   369	    """(G1, G2) with coarsen(Phi(G1), c) = coarsen(Phi(G2), c) and P(G1) != P(G2)
   370	    (Part VII Prop 7.5).
   371	
   372	    If c drops a pillar m, the drop witness with l0 the first retained pillar (if c drops
   373	    every pillar, a and b hold only m and both images are the actor set); otherwise, for
   374	    the first pair {m, n} in one block, the merge witness with mu = lam_m / (lam_m + lam_n).
   375	    Raises if c is a total injection (then Phi_c is P-preserving, Thm 7.8).
   376	    """
   377	    if set(c) != set(M_LABELS):
   378	        raise ValueError("c must assign all six pillars")
   379	    dropped = [m for m in M_LABELS if c[m] is None]
   380	    kept = [m for m in M_LABELS if c[m] is not None]
   381	    if dropped:
   382	        if not kept:
   383	            # K is empty: both images reduce to the shared actor set {a, b, c} (Prop 7.5(a)).
   384	            m = dropped[0]
   385	            return witness_record({m: (1.0, 0.0)}), witness_record({m: (0.5, 0.5)})
   386	        return _drop_witness(dropped[0], kept[0])
   387	    for i, m in enumerate(M_LABELS):
   388	        for n in M_LABELS[i + 1:]:
   389	            if c[m] == c[n]:
   390	                if lam is None:
   391	                    size = sum(1 for x in M_LABELS if c[x] == c[m])
   392	                    lm = ln = 1.0 / size
   393	                else:
   394	                    lm, ln = float(lam[m]), float(lam[n])
   395	                return _merge_witness(m, n, lm / (lm + ln))
   396	    raise ValueError("c is a total injection; no collapse witness")
   397	
   398	
   399	# Predecessor encodings ---------------------------------------------------------------------
   400	
   401	PARSONS: dict[Label, Label | None] = {"F": "A", "W": "A", "P": "G", "J": "I", "C": "I", "I": "L"}
   402	MANN: dict[Label, Label | None] = {"I": "Ideological", "F": "Economic", "W": "Economic",
   403	                                   "C": "Military", "P": "Political", "J": "Political"}
   404	EASTON: dict[Label, Label | None] = {"I": "Inputs", "W": "Inputs", "F": "Outputs",
   405	                                     "P": "Outputs", "J": "Outputs", "C": "Outputs"}
   406	LUHMANN: dict[Label, Label | None] = {"F": "Economy", "W": "Economy", "P": "Politics",
   407	                                      "C": "Politics", "J": "Law", "I": "Culture"}
   408	ALMOND: dict[Label, Label | None] = {"F": None, "W": None, "P": "RuleMaking",
   409	                                     "J": "RuleAdjudication", "C": "RuleApplication",
   410	                                     "I": "Inputs"}
   411	
   412	
   413	def encode_parsons(F: FormalizedStructure) -> FormalizedStructure:
   414	    """AGIL: A = {F, W}, G = {P}, I = {J, C}, L = {I}."""
   415	    return coarsen(F, PARSONS)
   416	
   417	
   418	def encode_mann(F: FormalizedStructure) -> FormalizedStructure:
   419	    """IEMP: Ideological = {I}, Economic = {F, W}, Military = {C}, Political = {P, J}."""
   420	    return coarsen(F, MANN)
   421	
   422	
   423	def encode_easton(F: FormalizedStructure) -> FormalizedStructure:
   424	    """Inputs = {I, W}, Outputs = {F, P, J, C}."""
   425	    return coarsen(F, EASTON)
   426	
   427	
   428	def encode_luhmann(F: FormalizedStructure) -> FormalizedStructure:
   429	    """Economy = {F, W}, Politics = {P, C}, Law = {J}, Culture = {I} (Luhmann splits it
   430	    further; the split does not affect the witness)."""
   431	    return coarsen(F, LUHMANN)
   432	
   433	
   434	def encode_almond(F: FormalizedStructure) -> FormalizedStructure:
   435	    """F and W dropped; RuleMaking = {P}, RuleAdjudication = {J}, RuleApplication = {C},
   436	    Inputs = {I}."""
   437	    return coarsen(F, ALMOND)
   438	
   439	
   440	def encode_aristotle(F: FormalizedStructure) -> tuple[str, str]:
   441	    """(rulers, aim): 'one' if exactly one actor has s^P > 0, 'few' if 2 to n/2, else 'many';
   442	    'deviant' if any capture link, else 'correct'. A typology, not a coarsening."""
   443	    k = sum(1 for v in F.actors if F.shares["P"].get(v, 0.0) > 0.0)
   444	    n = len(F.actors)
   445	    rulers = "one" if k == 1 else ("few" if 2 <= k <= n / 2 else "many")
   446	    return rulers, ("deviant" if F.links else "correct")
   447	
   448	
   449	WEBER_TYPES = ("traditional", "charismatic", "legal-rational")
   450	
   451	
   452	def encode_weber(F: FormalizedStructure, legitimation: str, has_staff: bool) -> tuple[str, bool]:
   453	    """(legitimation type, administrative staff). Both come from a coded field the profile
   454	    does NOT contain, so the encoding does not factor through P (nor P through it)."""
   455	    if legitimation not in WEBER_TYPES:
   456	        raise ValueError(f"legitimation must be one of {WEBER_TYPES}")
   457	    return legitimation, bool(has_staff)
   458	
   459	
   460	ENCODINGS: dict[str, Callable[[FormalizedStructure], object]] = {
   461	    "parsons": encode_parsons,
   462	    "mann": encode_mann,
   463	    "easton": encode_easton,
   464	    "luhmann": encode_luhmann,
   465	    "almond": encode_almond,
   466	    "aristotle": encode_aristotle,
   467	    "weber": lambda F: encode_weber(F, "legal-rational", True),
   468	}
   469	
   470	_WITNESSES: dict[str, Callable[[], tuple[CodedRecord, CodedRecord]]] = {
   471	    "parsons": lambda: _merge_witness("F", "W", 0.5),
   472	    "mann": lambda: _merge_witness("P", "J", 0.5),
   473	    "easton": lambda: _merge_witness("P", "J", 0.5),
   474	    "luhmann": lambda: _merge_witness("F", "W", 0.5),
   475	    "almond": lambda: _drop_witness("F", "P"),
   476	    "aristotle": lambda: (witness_record({"J": (1.0, 0.0), "I": (0.5, 0.5)}),
   477	                          witness_record({"J": (0.5, 0.5), "I": (0.5, 0.5)})),
   478	    "weber": lambda: (witness_record({"C": (1.0, 0.0), "I": (0.5, 0.5)}),
   479	                      witness_record({"C": (0.5, 0.5), "I": (0.5, 0.5)})),
   480	}
   481	
   482	
   483	def witness_pair(k: str) -> tuple[CodedRecord, CodedRecord]:
   484	    """Two systems satisfying all axioms that encoding ``k`` cannot tell apart, with P
   485	    differing (Part VII Prop 10.1). Merge witnesses use mu = 1/2 (equal lam; Easton's
   486	    four-member Outputs block also gives mu = 1/2 for (P, J)); Almond drops F with l0 = P;
   487	    Aristotle and Weber differ in s^J or s^C with a and b also holding (1/2, 1/2) in I.
   488	    """
   489	    if k not in _WITNESSES:
   490	        raise ValueError(f"unknown encoding {k!r}")
   491	    return _WITNESSES[k]()
   492	
   493	
   494	def coarsenings_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   495	    """Coarsened profiles equal component by component (identity on actor names)."""
   496	    return structurally_equal(F, G)
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
   350	    from beast_system.uniqueness import canonical_form
   351	
   352	    F_ = represent(record_from_polity(fused_polity()))
   353	    for eps in (5e-10, 1e-14):
   354	        G_ = FormalizedStructure(**{**F_.__dict__, "contestability":
   355	                                    {**F_.contestability, "J": F_.contestability["J"] + eps}})
   356	        assert p_equal(F_, G_) == (canonical_form(F_) == canonical_form(G_))
   357	
   358	
   359	def test_missing_kappa_column_differs_from_explicit_zero():
   360	    from beast_system.uniqueness import canonical_form
   361	
   362	    F_ = represent(record_from_polity(fused_polity()))
   363	    missing = {S: {m: x for m, x in row.items() if m != "P"} for S, row in F_.kappa.items()}
   364	    zero = {S: {**row, "P": 0.0} for S, row in missing.items()}
   365	    G1 = FormalizedStructure(**{**F_.__dict__, "kappa": missing})
   366	    G2 = FormalizedStructure(**{**F_.__dict__, "kappa": zero})
   367	    assert not p_equal(G1, G2)
   368	    assert canonical_form(G1) != canonical_form(G2)
   369	
   370	
   371	def test_all_dropped_coarsening_has_a_witness():
   372	    c = {m: None for m in M_LABELS}
   373	    g1, g2 = witness_coarsening(c)
   374	    F1, F2 = phi(g1), phi(g2)
   375	    assert not p_equal(F1, F2)
   376	    i1, i2 = coarsen(F1, c), coarsen(F2, c)
   377	    assert i1.pillars == () and i1.actors == i2.actors == ("a", "b", "c")
   378	    assert coarsenings_equal(i1, i2)

exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/dynamics.py | sed -n '90,285p'; nl -ba model/tests/test_conversion.py | sed -n '1,105p'; nl -ba model/tests/test_dynamics_regimes.py | sed -n '1,48p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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
   223	_REFINE_STEPS = 200
   224	
   225	
   226	@dataclass(frozen=True)
   227	class Foothold:
   228	    """Foothold bound: v . y_t >= min(v . y_0, (1 - max delta)(rho - 1) / (2c)) for all t.
   229	
   230	    v is the left Perron vector of A (normalized to sum 1), c = v_max kappa / v_min^2 and
   231	    kappa the largest column sum of K. Proof sketch: v . T(y) = rho v . y - sum_n v_n y_n (K y)_n
   232	    >= rho s - c s^2 with s = v . y, and v . T(y) >= (1 - max delta) s.
   233	    """
   234	
   235	    rho: float
   236	    v: np.ndarray
   237	    c: float  # may be inf for near-reducible K; ``bound`` is computed without forming c
   238	    bound: float
   239	
   240	
   241	def foothold_bound(y0: np.ndarray, delta: np.ndarray, K: np.ndarray) -> Foothold:
   242	    """Lower bound on v . y_t when K is irreducible, max delta < 1 and rho(A) > 1."""
   243	    y0 = _unit_vector(y0, "y0")
   244	    d = _unit_vector(delta, "delta")
   245	    K = validate_conversion_matrix(K)
   246	    if not _is_irreducible(K):
   247	        raise ValueError("the foothold bound needs an irreducible K")
   248	    if d.max() >= 1.0:
   249	        raise ValueError("the foothold bound needs max delta < 1")
   250	    A = comparison_matrix(d, K)
   251	    vals, vecs = np.linalg.eig(A.T)
   252	    k = int(np.argmax(vals.real))
   253	    rho = float(vals[k].real)
   254	    if rho <= 1.0:
   255	        raise ValueError("the foothold bound needs rho(A) > 1")
   256	    v = np.abs(vecs[:, k].real)
   257	    v = v / v.max()
   258	    # Refine with v <- v A / rho. Every step sums non-negative terms, so entries many orders
   259	    # of magnitude below max(v) regain relative accuracy lost in the dense eigensolver.
   260	    for _ in range(_REFINE_STEPS):
   261	        v = (A * v[:, None]).sum(axis=0) / rho
   262	        v = v / v.max()
   263	    if v.min() <= 0.0:
   264	        raise ValueError("left Perron vector underflows; the bound is not representable")
   265	    v = v / v.sum()
   266	    kappa = float(K.sum(axis=0).max())
   267	    v_min, v_max = float(v.min()), float(v.max())
   268	    c = v_max * kappa / v_min**2 if v_min > 0.0 else float("inf")
   269	    # (1 - max delta)(rho - 1) / (2c), ordered so no intermediate overflows or underflows early.
   270	    margin = (1.0 - float(d.max())) * (rho - 1.0) / (2.0 * kappa) * (v_min / v_max) * v_min
   271	    bound = min(float((v * y0).sum()), margin)
   272	    return Foothold(rho=rho, v=v, c=float(c), bound=bound)
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

hook: PreToolUse
hook: PreToolUse
hook: PreToolUse
hook: PreToolUse Completed
hook: PreToolUse Completed
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/uniqueness.py | sed -n '360,530p'; nl -ba model/tests/test_uniqueness.py | sed -n '225,305p'" in /Users/mlong/Documents/Development/the-beast-system
exec
/usr/local/bin/zsh -lc "nl -ba model/beast_system/uniqueness.py | sed -n '290,410p'; nl -ba model/tests/test_uniqueness.py | sed -n '120,230p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
   360	
   361	def _merge_witness(m: Label, n: Label, mu: float) -> tuple[CodedRecord, CodedRecord]:
   362	    """Merge {m, n}: G1 s^m = (1, 0), s^n = (0, 1); G2 s^m = s^n = (mu, 1 - mu)."""
   363	    return (witness_record({m: (1.0, 0.0), n: (0.0, 1.0)}),
   364	            witness_record({m: (mu, 1.0 - mu), n: (mu, 1.0 - mu)}))
   365	
   366	
   367	def witness_coarsening(c: Coarsening, lam: Mapping[Label, float] | None = None
   368	                       ) -> tuple[CodedRecord, CodedRecord]:
   369	    """(G1, G2) with coarsen(Phi(G1), c) = coarsen(Phi(G2), c) and P(G1) != P(G2)
   370	    (Part VII Prop 7.5).
   371	
   372	    If c drops a pillar m, the drop witness with l0 the first retained pillar (if c drops
   373	    every pillar, a and b hold only m and both images are the actor set); otherwise, for
   374	    the first pair {m, n} in one block, the merge witness with mu = lam_m / (lam_m + lam_n).
   375	    Raises if c is a total injection (then Phi_c is P-preserving, Thm 7.8).
   376	    """
   377	    if set(c) != set(M_LABELS):
   378	        raise ValueError("c must assign all six pillars")
   379	    dropped = [m for m in M_LABELS if c[m] is None]
   380	    kept = [m for m in M_LABELS if c[m] is not None]
   381	    if dropped:
   382	        if not kept:
   383	            # K is empty: both images reduce to the shared actor set {a, b, c} (Prop 7.5(a)).
   384	            m = dropped[0]
   385	            return witness_record({m: (1.0, 0.0)}), witness_record({m: (0.5, 0.5)})
   386	        return _drop_witness(dropped[0], kept[0])
   387	    for i, m in enumerate(M_LABELS):
   388	        for n in M_LABELS[i + 1:]:
   389	            if c[m] == c[n]:
   390	                if lam is None:
   391	                    size = sum(1 for x in M_LABELS if c[x] == c[m])
   392	                    lm = ln = 1.0 / size
   393	                else:
   394	                    lm, ln = float(lam[m]), float(lam[n])
   395	                return _merge_witness(m, n, lm / (lm + ln))
   396	    raise ValueError("c is a total injection; no collapse witness")
   397	
   398	
   399	# Predecessor encodings ---------------------------------------------------------------------
   400	
   401	PARSONS: dict[Label, Label | None] = {"F": "A", "W": "A", "P": "G", "J": "I", "C": "I", "I": "L"}
   402	MANN: dict[Label, Label | None] = {"I": "Ideological", "F": "Economic", "W": "Economic",
   403	                                   "C": "Military", "P": "Political", "J": "Political"}
   404	EASTON: dict[Label, Label | None] = {"I": "Inputs", "W": "Inputs", "F": "Outputs",
   405	                                     "P": "Outputs", "J": "Outputs", "C": "Outputs"}
   406	LUHMANN: dict[Label, Label | None] = {"F": "Economy", "W": "Economy", "P": "Politics",
   407	                                      "C": "Politics", "J": "Law", "I": "Culture"}
   408	ALMOND: dict[Label, Label | None] = {"F": None, "W": None, "P": "RuleMaking",
   409	                                     "J": "RuleAdjudication", "C": "RuleApplication",
   410	                                     "I": "Inputs"}
   411	
   412	
   413	def encode_parsons(F: FormalizedStructure) -> FormalizedStructure:
   414	    """AGIL: A = {F, W}, G = {P}, I = {J, C}, L = {I}."""
   415	    return coarsen(F, PARSONS)
   416	
   417	
   418	def encode_mann(F: FormalizedStructure) -> FormalizedStructure:
   419	    """IEMP: Ideological = {I}, Economic = {F, W}, Military = {C}, Political = {P, J}."""
   420	    return coarsen(F, MANN)
   421	
   422	
   423	def encode_easton(F: FormalizedStructure) -> FormalizedStructure:
   424	    """Inputs = {I, W}, Outputs = {F, P, J, C}."""
   425	    return coarsen(F, EASTON)
   426	
   427	
   428	def encode_luhmann(F: FormalizedStructure) -> FormalizedStructure:
   429	    """Economy = {F, W}, Politics = {P, C}, Law = {J}, Culture = {I} (Luhmann splits it
   430	    further; the split does not affect the witness)."""
   431	    return coarsen(F, LUHMANN)
   432	
   433	
   434	def encode_almond(F: FormalizedStructure) -> FormalizedStructure:
   435	    """F and W dropped; RuleMaking = {P}, RuleAdjudication = {J}, RuleApplication = {C},
   436	    Inputs = {I}."""
   437	    return coarsen(F, ALMOND)
   438	
   439	
   440	def encode_aristotle(F: FormalizedStructure) -> tuple[str, str]:
   441	    """(rulers, aim): 'one' if exactly one actor has s^P > 0, 'few' if 2 to n/2, else 'many';
   442	    'deviant' if any capture link, else 'correct'. A typology, not a coarsening."""
   443	    k = sum(1 for v in F.actors if F.shares["P"].get(v, 0.0) > 0.0)
   444	    n = len(F.actors)
   445	    rulers = "one" if k == 1 else ("few" if 2 <= k <= n / 2 else "many")
   446	    return rulers, ("deviant" if F.links else "correct")
   447	
   448	
   449	WEBER_TYPES = ("traditional", "charismatic", "legal-rational")
   450	
   451	
   452	def encode_weber(F: FormalizedStructure, legitimation: str, has_staff: bool) -> tuple[str, bool]:
   453	    """(legitimation type, administrative staff). Both come from a coded field the profile
   454	    does NOT contain, so the encoding does not factor through P (nor P through it)."""
   455	    if legitimation not in WEBER_TYPES:
   456	        raise ValueError(f"legitimation must be one of {WEBER_TYPES}")
   457	    return legitimation, bool(has_staff)
   458	
   459	
   460	ENCODINGS: dict[str, Callable[[FormalizedStructure], object]] = {
   461	    "parsons": encode_parsons,
   462	    "mann": encode_mann,
   463	    "easton": encode_easton,
   464	    "luhmann": encode_luhmann,
   465	    "almond": encode_almond,
   466	    "aristotle": encode_aristotle,
   467	    "weber": lambda F: encode_weber(F, "legal-rational", True),
   468	}
   469	
   470	_WITNESSES: dict[str, Callable[[], tuple[CodedRecord, CodedRecord]]] = {
   471	    "parsons": lambda: _merge_witness("F", "W", 0.5),
   472	    "mann": lambda: _merge_witness("P", "J", 0.5),
   473	    "easton": lambda: _merge_witness("P", "J", 0.5),
   474	    "luhmann": lambda: _merge_witness("F", "W", 0.5),
   475	    "almond": lambda: _drop_witness("F", "P"),
   476	    "aristotle": lambda: (witness_record({"J": (1.0, 0.0), "I": (0.5, 0.5)}),
   477	                          witness_record({"J": (0.5, 0.5), "I": (0.5, 0.5)})),
   478	    "weber": lambda: (witness_record({"C": (1.0, 0.0), "I": (0.5, 0.5)}),
   479	                      witness_record({"C": (0.5, 0.5), "I": (0.5, 0.5)})),
   480	}
   481	
   482	
   483	def witness_pair(k: str) -> tuple[CodedRecord, CodedRecord]:
   484	    """Two systems satisfying all axioms that encoding ``k`` cannot tell apart, with P
   485	    differing (Part VII Prop 10.1). Merge witnesses use mu = 1/2 (equal lam; Easton's
   486	    four-member Outputs block also gives mu = 1/2 for (P, J)); Almond drops F with l0 = P;
   487	    Aristotle and Weber differ in s^J or s^C with a and b also holding (1/2, 1/2) in I.
   488	    """
   489	    if k not in _WITNESSES:
   490	        raise ValueError(f"unknown encoding {k!r}")
   491	    return _WITNESSES[k]()
   492	
   493	
   494	def coarsenings_equal(F: FormalizedStructure, G: FormalizedStructure) -> bool:
   495	    """Coarsened profiles equal component by component (identity on actor names)."""
   496	    return structurally_equal(F, G)
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

 succeeded in 0ms:
   290	
   291	    return search(_initial_colors(F))
   292	
   293	
   294	def alpha_canonical(record: CodedRecord) -> tuple:
   295	    """A P-preserving abstraction: the canonical form of represent(G)."""
   296	    return canonical_form(represent(record))
   297	
   298	
   299	def alpha_canonical_phi(record: CodedRecord) -> tuple:
   300	    """A second, differently built one: the canonical form of Phi(G) (coarsen by identity)
   301	    plus a redundant field (the number of hyperarcs)."""
   302	    F = phi(record)
   303	    return (canonical_form(F), len(F.arcs))
   304	
   305	
   306	def rename_record(record: CodedRecord, mapping: Mapping[str, str]) -> CodedRecord:
   307	    """The same coded system with actors renamed by ``mapping`` (missing names kept)."""
   308	    ren = lambda v: mapping.get(v, v)  # noqa: E731
   309	    sys_ = record.system
   310	    names = set(represent(record).actors)
   311	    if len({ren(v) for v in names}) != len(names):
   312	        raise ValueError("renaming must be injective on the record's actors")
   313	    practices = tuple(
   314	        Practice(p.description, p.solves, frozenset(ren(h) for h in p.holders), p.formal,
   315	                 p.source)
   316	        for p in sys_.practices
   317	    )
   318	    system = GovernanceSystem(sys_.name, sys_.persistent, sys_.axioms, practices,
   319	                              sys_.absent_incidences, sys_.note)
   320	    links = tuple(CaptureLink(ren(lk.source), ren(lk.target), lk.pillar, lk.privileged_access,
   321	                              lk.weakens_accountability, lk.material_evidence, lk.evidence)
   322	                  for lk in record.links)
   323	    coalitions = None if record.coalitions is None else {
   324	        frozenset(ren(v) for v in S): row for S, row in record.coalitions.items()}
   325	    return CodedRecord(system, {m: {ren(v): x for v, x in sh.items()}
   326	                                for m, sh in record.shares.items()},
   327	                       record.contestability, record.weights, coalitions, links)
   328	
   329	
   330	# Witnesses ---------------------------------------------------------------------------------
   331	
   332	
   333	def witness_record(ab_shares: Mapping[Label, tuple[float, float]], q: float = 0.5,
   334	                   links: Iterable = ()) -> CodedRecord:
   335	    """Witness system (Part VII Prop 7.5, Prop 10.1): actors a and b perform exactly the
   336	    pillars in ``ab_shares`` with shares (s^m_a, s^m_b); actor c alone performs every other
   337	    pillar (share 1). Ax1..Ax6 and X1, X2, X3, X5 hold, so Proposition A holds. Both members
   338	    of a witness pair use the same keys, hence the same actor set and role map.
   339	    """
   340	    if not ab_shares or not set(ab_shares) <= set(M_LABELS):
   341	        raise ValueError("ab_shares must name at least one pillar label")
   342	    practices = tuple(
   343	        Practice(f"{m.label} practice", PILLAR_TO_AXIOM[m],
   344	                 frozenset({"a", "b"}) if m.name in ab_shares else frozenset({"c"}),
   345	                 source="synthetic witness")
   346	        for m in PILLARS
   347	    )
   348	    system = GovernanceSystem("witness", True, EXTENDED_AXIOMS, practices)
   349	    shares = {m: (dict(zip(("a", "b"), ab_shares[m.name])) if m.name in ab_shares
   350	                  else {"c": 1.0}) for m in PILLARS}
   351	    return CodedRecord(system, shares, {m: q for m in PILLARS}, links=tuple(links))
   352	
   353	
   354	def _drop_witness(m: Label, l0: Label) -> tuple[CodedRecord, CodedRecord]:
   355	    """Drop m: G1 s^m = (1, 0), G2 s^m = (1/2, 1/2); a and b also hold (1/2, 1/2) in the
   356	    retained pillar l0 in both, so b is an actor of G1 too."""
   357	    return (witness_record({m: (1.0, 0.0), l0: (0.5, 0.5)}),
   358	            witness_record({m: (0.5, 0.5), l0: (0.5, 0.5)}))
   359	
   360	
   361	def _merge_witness(m: Label, n: Label, mu: float) -> tuple[CodedRecord, CodedRecord]:
   362	    """Merge {m, n}: G1 s^m = (1, 0), s^n = (0, 1); G2 s^m = s^n = (mu, 1 - mu)."""
   363	    return (witness_record({m: (1.0, 0.0), n: (0.0, 1.0)}),
   364	            witness_record({m: (mu, 1.0 - mu), n: (mu, 1.0 - mu)}))
   365	
   366	
   367	def witness_coarsening(c: Coarsening, lam: Mapping[Label, float] | None = None
   368	                       ) -> tuple[CodedRecord, CodedRecord]:
   369	    """(G1, G2) with coarsen(Phi(G1), c) = coarsen(Phi(G2), c) and P(G1) != P(G2)
   370	    (Part VII Prop 7.5).
   371	
   372	    If c drops a pillar m, the drop witness with l0 the first retained pillar (if c drops
   373	    every pillar, a and b hold only m and both images are the actor set); otherwise, for
   374	    the first pair {m, n} in one block, the merge witness with mu = lam_m / (lam_m + lam_n).
   375	    Raises if c is a total injection (then Phi_c is P-preserving, Thm 7.8).
   376	    """
   377	    if set(c) != set(M_LABELS):
   378	        raise ValueError("c must assign all six pillars")
   379	    dropped = [m for m in M_LABELS if c[m] is None]
   380	    kept = [m for m in M_LABELS if c[m] is not None]
   381	    if dropped:
   382	        if not kept:
   383	            # K is empty: both images reduce to the shared actor set {a, b, c} (Prop 7.5(a)).
   384	            m = dropped[0]
   385	            return witness_record({m: (1.0, 0.0)}), witness_record({m: (0.5, 0.5)})
   386	        return _drop_witness(dropped[0], kept[0])
   387	    for i, m in enumerate(M_LABELS):
   388	        for n in M_LABELS[i + 1:]:
   389	            if c[m] == c[n]:
   390	                if lam is None:
   391	                    size = sum(1 for x in M_LABELS if c[x] == c[m])
   392	                    lm = ln = 1.0 / size
   393	                else:
   394	                    lm, ln = float(lam[m]), float(lam[n])
   395	                return _merge_witness(m, n, lm / (lm + ln))
   396	    raise ValueError("c is a total injection; no collapse witness")
   397	
   398	
   399	# Predecessor encodings ---------------------------------------------------------------------
   400	
   401	PARSONS: dict[Label, Label | None] = {"F": "A", "W": "A", "P": "G", "J": "I", "C": "I", "I": "L"}
   402	MANN: dict[Label, Label | None] = {"I": "Ideological", "F": "Economic", "W": "Economic",
   403	                                   "C": "Military", "P": "Political", "J": "Political"}
   404	EASTON: dict[Label, Label | None] = {"I": "Inputs", "W": "Inputs", "F": "Outputs",
   405	                                     "P": "Outputs", "J": "Outputs", "C": "Outputs"}
   406	LUHMANN: dict[Label, Label | None] = {"F": "Economy", "W": "Economy", "P": "Politics",
   407	                                      "C": "Politics", "J": "Law", "I": "Culture"}
   408	ALMOND: dict[Label, Label | None] = {"F": None, "W": None, "P": "RuleMaking",
   409	                                     "J": "RuleAdjudication", "C": "RuleApplication",
   410	                                     "I": "Inputs"}
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

exec
/usr/local/bin/zsh -lc "nl -ba model/tests/test_conversion.py | sed -n '98,145p'; nl -ba model/beast_system/dynamics.py | sed -n '1,90p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 0ms:
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
   118	
   119	
   120	def test_foothold_bound_is_overflow_safe_for_near_reducible_k():
   121	    # Codex round 4 fixture: a 5-node core with weights 0.22 and 1e-155 links to node 6.
   122	    K = np.zeros((6, 6))
   123	    K[:5, :5] = 0.22
   124	    np.fill_diagonal(K, 0.0)
   125	    K[0, 5] = 1e-155
   126	    K[5, 1] = 1e-155  # asymmetric attachment
   127	    delta = np.full(6, 0.1)
   128	    y0 = np.full(6, 0.05)
   129	    fh = foothold_bound(y0, delta, K)
   130	    assert np.isfinite(fh.bound) and fh.bound > 0.0
   131	    assert fh.rho == pytest.approx(0.9 + 0.88)
   132	    A = comparison_matrix(delta, K)
   133	    assert (A * fh.v[:, None]).sum(axis=0) == pytest.approx(fh.rho * fh.v, rel=1e-9, abs=0)
   134	    path = simulate_conversion(y0, delta, K, 300)
   135	    assert np.all((path * fh.v).sum(axis=1) >= fh.bound)
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

hook: PreToolUse
hook: PreToolUse Completed
exec
/usr/local/bin/zsh -lc "git --no-pager diff -- papers/latex/formalized-state.tex | sed -n '1,220p'" in /Users/mlong/Documents/Development/the-beast-system
 succeeded in 1631ms:
2026-10-22 14:17:28.217 xcodebuild[11904:4430755]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 14:17:28.351 xcodebuild[11904:4430753] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
git: error: couldn't create cache file '/tmp/xcrun_db-zFUB0rbV' (errno=Operation not permitted)
2026-10-22 14:17:28.805 xcodebuild[11919:4430870]  DVTFilePathFSEvents: Failed to start fs event stream.
2026-10-22 14:17:28.894 xcodebuild[11919:4430858] [MT] DVTDeveloperPaths: Failed to get length of DARWIN_USER_CACHE_DIR from confstr(3), error = Error Domain=NSPOSIXErrorDomain Code=5 "Input/output error". Using NSCachesDirectory instead.
diff --git a/papers/latex/formalized-state.tex b/papers/latex/formalized-state.tex
index e1041b5..6edbdf0 100644
--- a/papers/latex/formalized-state.tex
+++ b/papers/latex/formalized-state.tex
@@ -1040,19 +1040,19 @@ Result & What the code checks & Functions and tests \\
 \Cref{def:formalized-state:implementation}, \cref{thm:formalized-state:A}, \cref{cor:formalized-state:struct} & Every hard-case and baseline fixture that satisfies the axioms realizes all six functions with the relations $\Dzero$ present, and none is a counterexample. & \code{necessity.check_proposition_a}; \code{test_necessity}: \code{test_theorem_a_on_hard_cases}, \code{test_baseline_model_is_consistent} \\
 \Cref{prop:formalized-state:independence} & The model of part (a) has $\Struct$; each of the six independence fixtures persists, violates exactly its axiom and lacks exactly its function, including the repaired model for Ax4$^{*}$. & \code{necessity.PROP_4_4A_MODEL}, \code{AXIOM_INDEPENDENCE}, \code{R1_AX4_MODEL}; \code{test_necessity}: \code{test_prop_4_4a_model_and_variant}, \code{test_axiom_independence_fixtures}, \code{test_r1_independence_model_for_ax4} \\
 \Cref{lem:formalized-state:D0} & The hyperarc $(\{\pI,\pC\},\pJ)$ is generated, and in the variant with a fine on defiance neither $\pI\to\pJ$ nor $\pC\to\pJ$ is. & \code{necessity.generate_dependencies}, \code{PROP_4_4A_VARIANT}; \code{test_necessity}: \code{test_prop_4_4a_model_and_variant} \\
-\Cref{thm:formalized-state:interdependence} & The arcs of $\Dstar$ are generated from the axiom encodings; $\Dstar$ is strongly connected, and the cascade of every single function is all six; every fixture built from the full axiom set is interdependent. & \code{necessity.D_STAR_KEYS}, \code{generate_dependencies}, \code{is_strongly_connected}, \code{cascade_closure}; \code{test_necessity}: \code{test_d_star_is_strongly_connected_and_cascade_complete}, \code{test_interdependence_holds_for_every_axiom_built_fixture} \\
+\Cref{thm:formalized-state:interdependence} & The arcs of $\Dstar$ are generated from the axiom encodings; $\Dstar$ is strongly connected, and the cascade of every single function is all six; every hard-case fixture with the full axiom set and all six coded practices is interdependent. & \code{necessity.D_STAR_KEYS}, \code{generate_dependencies}, \code{is_strongly_connected}, \code{cascade_closure}; \code{test_necessity}: \code{test_d_star_is_strongly_connected_and_cascade_complete}, \code{test_interdependence_holds_for_every_axiom_built_fixture} \\
 \Cref{prop:formalized-state:minimality} & The six axioms without X1 to X5 give $\Struct$ but not interdependence; without X1 no arc enters $\pW$; without X2 $\pP$ has no outgoing arc; without X5 the structure is strongly connected and $\cl(\{\pC\})=\{\pC\}$, while splitting the hyperarc puts $\pJ$ in that cascade; precedent can replace X3. & \code{test_necessity}: \code{test_d0_axioms_without_x_give_struct_but_not_interdependence}, \code{test_without_x1_no_arc_into_w}, \code{test_without_x2_p_has_no_out_arc}, \code{test_without_x5_strongly_connected_but_c_isolated}, \code{test_replacing_x3_by_precedent_keeps_strong_connectivity} \\
 \Cref{def:formalized-state:overlap} & The overlap measure is computed for general, non-additive coalition shares. & \code{indices.coalition_overlap}; \code{test_indices}: \code{test_coalition_overlap_general_kappa} \\
-\Cref{lem:formalized-state:hub} & $\Integ$ equals the sum of degrees over thirty; the star bounds $1/3$, $0.6$ and $0.8$ hold and are attained; the clique and star bounds hold on test matrices. & \code{indices.integration_degrees}, \code{hub_bound}, \code{clique_lower_bound}, \code{star_upper_bound}; \code{test_indices}: \code{test_degree_decomposition_of_integration}, \code{test_hub_bound_values_and_validity}, \code{test_clique_lower_bound}, \code{test_star_upper_bound} \\
+\Cref{lem:formalized-state:hub} & $\Integ$ equals the sum of degrees over thirty; the hub-set bounds for $k=1,2,3$ ($1/3$, $0.6$ and $0.8$) hold and are attained; the clique bound and the pure-star bound hold on test matrices. & \code{indices.integration_degrees}, \code{hub_bound}, \code{clique_lower_bound}, \code{star_upper_bound}; \code{test_indices}: \code{test_degree_decomposition_of_integration}, \code{test_hub_bound_values_and_validity}, \code{test_clique_lower_bound}, \code{test_star_upper_bound} \\
 \Cref{def:formalized-state:cap}, \cref{lem:formalized-state:U} & Each of the three conditions of a capture link is necessary; $U$ lies in $[0,1]$ and, for any weights, between the smallest and largest pillar terms. & \code{capture.proposition_b}, \code{indices.unaccountable_concentration}, \code{weight_sensitivity}; \code{test_capture}: \code{test_each_capture_condition_is_necessary}; \code{test_indices}: \code{test_u_bounds_random}, \code{test_weight_sensitivity_within_vertex_bounds} \\
-\Cref{lem:formalized-state:separation} & The hard cases and the four corner assignments are admissible. & \code{necessity.is_admissible}; \code{test_necessity}: \code{test_admissibility} \\
+\Cref{lem:formalized-state:separation} & The admissibility check returns true for the hard cases and the four corner assignments when every coded holder is supplied as a member; these fixtures do not exercise the clause on parties to a dispute. & \code{necessity.is_admissible}; \code{test_necessity}: \code{test_admissibility} \\
 \Cref{thm:formalized-state:nonimplication} & Four polities satisfying every axiom attain $(U,\Integ)$ equal to $(0,0)$, $(0,1)$, $(1,0)$ and $(1,1)$, all interdependent, and only $(1,1)$ has a capture link; the counter-model holds for several threshold pairs. & \code{capture.corner_polities}, \code{a_does_not_imply_b}; \code{test_capture}: \code{test_corner_polities_attain_the_four_corners}, \code{test_counter_model_robust_to_thresholds} \\
 \Cref{def:formalized-state:F,def:formalized-state:profile}, \cref{thm:formalized-state:representation} & A coded record is representable exactly when Proposition A holds for it, on the fixtures and on random well-formed records; independence models fail (F1), and the baseline without X1 to X5 fails only (F4). & \code{representation.CodedRecord}, \code{represent}, \code{in_formalized_class}, \code{representable}; \code{test_representation}: \code{test_representable_iff_proposition_a}, \code{test_theorem_on_random_well_formed_records}, \code{test_independence_models_are_not_representable_empty_layer}, \code{test_baseline_without_x_fails_only_f4} \\
-\Cref{lem:formalized-state:preserved} & Representation and equivalence under an actor bijection preserve $H$, $U$, $C^{\ov}$, $\Integ$, the capture predicate and interdependence. & \code{representation.preserved_quantities}, \code{equivalent_A}; \code{test_representation}: \code{test_represent_preserves_quantities}, \code{test_equivalent_a_under_actor_bijection_preserves_quantities} \\
+\Cref{lem:formalized-state:preserved} & Representation preserves $H$, $U$, $\Integ$, the capture predicate and interdependence; equivalence under an actor bijection preserves these and every coupling $C^{\ov}_{mn}$. & \code{representation.preserved_quantities}, \code{equivalent_A}; \code{test_representation}: \code{test_represent_preserves_quantities}, \code{test_equivalent_a_under_actor_bijection_preserves_quantities} \\
 \Cref{prop:formalized-state:minimality6} & Every drop and every merge of pillars, including the all-dropped map, identifies the two witnesses of the proposition while their preserved properties differ; drop witnesses keep both actors through a retained pillar. & \code{uniqueness.coarsen}, \code{witness_coarsening}; \code{representation.drop}, \code{merge}; \code{test_uniqueness}: \code{test_every_drop_collapses_a_witness}, \code{test_every_merge_collapses_a_witness}, \code{test_all_dropped_coarsening_has_a_witness}, \code{test_drop_witness_keeps_b_as_actor_via_retained_pillar} \\
 \Cref{def:formalized-state:abstraction}, \cref{thm:formalized-state:uniqueness} & Two $P$-preserving abstractions built differently factor through $\Phi$ by a well-defined map that is a bijection on the fixtures; the canonical form is a complete invariant for $P$. & \code{uniqueness.phi}, \code{canonical_form}, \code{factor_through_phi}; \code{test_uniqueness}: \code{test_p_preserving_abstractions_factor_through_phi}, \code{test_canonical_form_is_a_complete_invariant} \\
 \Cref{thm:formalized-state:six} & Bijective coarsenings are renamings that preserve the structure; each of the 202 partitions of the six pillars into fewer than six blocks collapses a witness pair. & \code{uniqueness.coarsen}; \code{test_uniqueness}: \code{test_bijective_coarsenings_are_p_preserving}, \code{test_pigeonhole_every_partition_with_fewer_than_six_blocks} \\
-\Cref{def:formalized-state:conversion}, \cref{thm:formalized-state:conversion} & Parts (a), (b), (c), (e) and (f): the map stays in the cube and below $Ay$; $\rho(A)<1$ drains every foothold; a fully contestable pillar drains and caps integration; $\rho(A)$ falls as $Q$ rises; the foothold bound holds over 500 steps. & \code{dynamics.conversion_step}, \code{comparison_matrix}, \code{foothold_bound}; \code{test_conversion}: \code{test_t_maps_cube_into_itself_and_is_dominated_by_a}, \code{test_rho_below_one_means_reversible}, \code{test_full_contestability_drains_pillar_and_caps_integration}, \code{test_rho_nonincreasing_in_each_q}, \code{test_foothold_never_vanishes} \\
+\Cref{def:formalized-state:conversion}, \cref{thm:formalized-state:conversion} & Parts (a), (b), (c), (e) and (f), on the tested fixtures and samples: the map stays in the cube and below $Ay$ on 300 samples; one $\rho(A)<1$ path decays below $10^{-6}$; the fully contestable pillar obeys its geometric bound and integration cap; $\rho(A)$ is nonincreasing on each tested grid of $Q_n$; and the foothold bound holds for 500 steps. & \code{dynamics.conversion_step}, \code{comparison_matrix}, \code{foothold_bound}; \code{test_conversion}: \code{test_t_maps_cube_into_itself_and_is_dominated_by_a}, \code{test_rho_below_one_means_reversible}, \code{test_full_contestability_drains_pillar_and_caps_integration}, \code{test_rho_nonincreasing_in_each_q}, \code{test_foothold_never_vanishes} \\
 \Cref{rem:formalized-state:sign} & A six-pillar pair of matrices with the same positive entries has spectral radii above and below one. & \code{dynamics.negative_feedback_example}; \code{test_dynamics_regimes}: \code{test_positive_links_do_not_guarantee_persistence} \\
 \Cref{prop:formalized-state:witnesses}, \cref{thm:formalized-state:novelty} & For each of the seven encoded predecessors, the two witness systems have the same actors and the same encoding and different $P$; the Weber label is not determined by $P$. & \code{uniqueness.encode_parsons} and the six other encodings, \code{witness_pair}; \code{test_uniqueness}: \code{test_predecessor_encoding_collapses_its_witness}, \code{test_weber_label_is_not_determined_by_p} \\
 \end{longtable}

codex
The final static pass found no remaining claim/test mismatch: each revised sentence is now scoped to what its cited fixtures or samples actually assert, and the other thirteen rows are likewise supported by their named implementations and tests.
codex
| Row | Result | Verdict | Evidence | Fix |
|---:|---|---|---|---|
| 1 | Implementation / Theorem A / structure | SUPPORTS | The hard-case test asserts the antecedent, all six realized pillars, `holds`, and no counterexample, while the baseline test asserts `holds`, whose implementation requires all six pillars and every applicable \(D_0\) relation. | — |
| 2 | Axiom independence | SUPPORTS | `AXIOM_INDEPENDENCE` removes exactly one axiom and its corresponding practice, and the cited tests verify persistence, that precise missing axiom and pillar, the structure of the part-(a) model, and the repaired Ax4* fixture. | — |
| 3 | \(D_0\) hyperarc | SUPPORTS | The cited test verifies that both part-(a) fixtures generate \((\{I,C\},J)\) while generating neither singleton arc \(I\to J\) nor \(C\to J\). | — |
| 4 | Interdependence | SUPPORTS | The tests establish strong connectivity and six-pillar cascade closure for `D_STAR_KEYS`, then verify that every hard-case fixture has the full antecedent, dependencies exactly equal to \(D^*\), and interdependence. | — |
| 5 | Dependency minimality | SUPPORTS | The five cited tests directly check the stated no-X, no-X1, no-X2, no-X5, split-hyperarc, and precedent-substitution outcomes. | — |
| 6 | Coalition overlap | SUPPORTS | `coalition_overlap` takes arbitrary candidate-coalition control mappings without additivity assumptions, and the test checks an overlapping, explicitly non-additive fixture and its expected pairwise overlaps. | — |
| 7 | Hub, clique, and star bounds | SUPPORTS | The tests verify the degree decomposition, the \(k=1,2,3\) hub values and their attaining full-hub matrices, the clique inequality on generated matrices, and the pure-star inequality for every possible hub. | — |
| 8 | Capture link and \(U\) | SUPPORTS | The capture test removes each of the three conditions separately, while the index tests check \(U\in[0,1]\) on 200 random inputs and confirm that its validated convex weighting remains between the exact minimum and maximum pillar terms. | — |
| 9 | Admissibility / separation | SUPPORTS | The positive loops pass all coded holders as members for every hard case and corner polity without supplying dispute parties, exactly matching the claim’s stated scope. | — |
| 10 | Nonimplication | SUPPORTS | The corner test verifies all four exact \((U,I)\) values, Proposition A and interdependence at every corner, and a capture link only at \((1,1)\), while the threshold test checks six threshold pairs. | — |
| 11 | Representation theorem | SUPPORTS | The tests compare representability with Proposition A across the fixture set and 300 random well-formed records, and separately verify the claimed F1 and F4 failures. | — |
| 12 | Preserved quantities | SUPPORTS | The representation test compares \(H,U,I\), capture, and interdependence with the source polity, while the actor-renaming test additionally compares every computed coupling \(C^{\mathrm{ov}}_{mn}\). | — |
| 13 | Six-pillar minimality | SUPPORTS | The witness tests cover every single-pillar drop, every pillar pair at three merge weights, the all-dropped map, unequal \(P\)-profiles with equal coarsenings, and retention of both actors through a retained pillar. | — |
| 14 | Abstraction and uniqueness | SUPPORTS | Both differently constructed canonical abstractions pass the finite factorization check as well-defined and bijective, and pairwise fixture comparisons verify canonical-form equality exactly when \(P\)-equality holds. | — |
| 15 | Exactly six dimensions | SUPPORTS | Random bijective pillar renamings are inverted back to the original structure, and the exhaustive partition generator checks all \(B_6-1=202\) partitions with fewer than six blocks and finds a collapsed witness for each. | — |
| 16 | Conversion dynamics | SUPPORTS | The cited tests perform exactly the claimed 300 cube/domination samples, one subcritical 300-step decay, the contestability fixture, eleven-point grids for each \(Q_n\), and the 500-step foothold-bound check. | — |
| 17 | Sign and spectral radius | SUPPORTS | `negative_feedback_example` preserves the positive-entry mask while adding two negative entries, and the test verifies spectral radii respectively above and below one. | — |
| 18 | Predecessor witnesses and novelty | SUPPORTS | The parametrized test covers all seven encodings and checks equal actors, equal encoded outputs, and unequal \(P\), while the Weber test changes its label and staff field without changing the underlying \(P\)-profile. | — |

COUNTS: SUPPORTS=18 PARTIAL=0 NO=0


hook: Stop
hook: Stop
hook: Stop Completed
hook: Stop Completed
tokens used
121,079
| Row | Result | Verdict | Evidence | Fix |
|---:|---|---|---|---|
| 1 | Implementation / Theorem A / structure | SUPPORTS | The hard-case test asserts the antecedent, all six realized pillars, `holds`, and no counterexample, while the baseline test asserts `holds`, whose implementation requires all six pillars and every applicable \(D_0\) relation. | — |
| 2 | Axiom independence | SUPPORTS | `AXIOM_INDEPENDENCE` removes exactly one axiom and its corresponding practice, and the cited tests verify persistence, that precise missing axiom and pillar, the structure of the part-(a) model, and the repaired Ax4* fixture. | — |
| 3 | \(D_0\) hyperarc | SUPPORTS | The cited test verifies that both part-(a) fixtures generate \((\{I,C\},J)\) while generating neither singleton arc \(I\to J\) nor \(C\to J\). | — |
| 4 | Interdependence | SUPPORTS | The tests establish strong connectivity and six-pillar cascade closure for `D_STAR_KEYS`, then verify that every hard-case fixture has the full antecedent, dependencies exactly equal to \(D^*\), and interdependence. | — |
| 5 | Dependency minimality | SUPPORTS | The five cited tests directly check the stated no-X, no-X1, no-X2, no-X5, split-hyperarc, and precedent-substitution outcomes. | — |
| 6 | Coalition overlap | SUPPORTS | `coalition_overlap` takes arbitrary candidate-coalition control mappings without additivity assumptions, and the test checks an overlapping, explicitly non-additive fixture and its expected pairwise overlaps. | — |
| 7 | Hub, clique, and star bounds | SUPPORTS | The tests verify the degree decomposition, the \(k=1,2,3\) hub values and their attaining full-hub matrices, the clique inequality on generated matrices, and the pure-star inequality for every possible hub. | — |
| 8 | Capture link and \(U\) | SUPPORTS | The capture test removes each of the three conditions separately, while the index tests check \(U\in[0,1]\) on 200 random inputs and confirm that its validated convex weighting remains between the exact minimum and maximum pillar terms. | — |
| 9 | Admissibility / separation | SUPPORTS | The positive loops pass all coded holders as members for every hard case and corner polity without supplying dispute parties, exactly matching the claim’s stated scope. | — |
| 10 | Nonimplication | SUPPORTS | The corner test verifies all four exact \((U,I)\) values, Proposition A and interdependence at every corner, and a capture link only at \((1,1)\), while the threshold test checks six threshold pairs. | — |
| 11 | Representation theorem | SUPPORTS | The tests compare representability with Proposition A across the fixture set and 300 random well-formed records, and separately verify the claimed F1 and F4 failures. | — |
| 12 | Preserved quantities | SUPPORTS | The representation test compares \(H,U,I\), capture, and interdependence with the source polity, while the actor-renaming test additionally compares every computed coupling \(C^{\mathrm{ov}}_{mn}\). | — |
| 13 | Six-pillar minimality | SUPPORTS | The witness tests cover every single-pillar drop, every pillar pair at three merge weights, the all-dropped map, unequal \(P\)-profiles with equal coarsenings, and retention of both actors through a retained pillar. | — |
| 14 | Abstraction and uniqueness | SUPPORTS | Both differently constructed canonical abstractions pass the finite factorization check as well-defined and bijective, and pairwise fixture comparisons verify canonical-form equality exactly when \(P\)-equality holds. | — |
| 15 | Exactly six dimensions | SUPPORTS | Random bijective pillar renamings are inverted back to the original structure, and the exhaustive partition generator checks all \(B_6-1=202\) partitions with fewer than six blocks and finds a collapsed witness for each. | — |
| 16 | Conversion dynamics | SUPPORTS | The cited tests perform exactly the claimed 300 cube/domination samples, one subcritical 300-step decay, the contestability fixture, eleven-point grids for each \(Q_n\), and the 500-step foothold-bound check. | — |
| 17 | Sign and spectral radius | SUPPORTS | `negative_feedback_example` preserves the positive-entry mask while adding two negative entries, and the test verifies spectral radii respectively above and below one. | — |
| 18 | Predecessor witnesses and novelty | SUPPORTS | The parametrized test covers all seven encodings and checks equal actors, equal encoded outputs, and unequal \(P\), while the Weber test changes its label and staff field without changing the underlying \(P\)-profile. | — |

COUNTS: SUPPORTS=18 PARTIAL=0 NO=0


