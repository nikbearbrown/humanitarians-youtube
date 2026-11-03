# PEDAGOGY — Claude, Shipped. (deep-explainer, claude-liam)

Fresh technical build covering CI/CD and deployment practices on GCP:
GitHub Actions, Pull Requests, dev/staging/production environments,
Docker, Kubernetes (importance + GKE setup), and the three deployment
strategies (Rolling/Blue-Green/Canary) with use cases, pros, and cons.
Thesis: merging code and shipping code are different problems solved by
different gates — and each stage of the pipeline (PR review, environment
promotion, containerization, orchestration, rollout strategy) exists to
catch one specific class of failure the others can't.

## Spine check

- B00 cold open, signed for Divyank from the start ✓
- 4 acts × (1 `FluencySegmentCard` + 6 content beats) = 28 body beats:
  I GitHub Actions + PRs, II environments, III Docker + Kubernetes (incl.
  GKE setup), IV deployment strategies ✓
- VERDICT → HANDOFF ("Your turn.") → title-restate OUTRO ✓

## Beat-mix contract

28 body beats — VOX 5/28 = **17.9%** (inside 15-30%), REMOTION 19/28 =
67.9% (absorbing the MANIM share, no Manim on this machine), CARD 4/28.

## Narration budget

Body beats mostly 12-27 words except A3-5 (52 words — carries both
Kubernetes' core job AND the concrete GKE setup steps; judged acceptable
as dense real content rather than trimmed to a word-count target, same
discipline as prior builds).

## Portrait (9:16 Short) plan, decided up front

`BinaryBranch`/`DivergentFates` assigned to A1-4, A2-3, A2-5, A4-3, A4-4
— for clean 9:16 Short derivation. Per the pattern observed across all
four prior Shorts this session, expect `shorts.py`'s auto cap-check to
still require a manual `--drop` override (it optimizes on duration alone,
not portrait-composition support) — plan to curate manually rather than
trust the auto-plan.

## Honesty discipline

Every claim is kept at the level of stable, publicly documented mechanism
(GitHub Actions/branch-protection behavior, Docker's core value
proposition, Kubernetes' core responsibilities, GKE's Autopilot/Standard
distinction, deployment-strategy definitions) — no version numbers,
pricing, quotas, or copy-pasteable command syntax presented as
guaranteed-current. See `FACTCHECK.md`.

## Time-limit expectation

Estimate: 517s (8.62 min) — inside the 5-10 min band with margin.

## Status

**VERDICT: PASS** — signed off by the human (Divyank Singh,
singh.divya@northeastern.edu) in chat, 2026-09-27, on review of this
PEDAGOGY.md, FACTCHECK.md, and the beat sheet's narration.
