# SOURCES.md — why-agents-fail

Primary source: `02_why_agents_fail.md` (the authored script with inline
`[VISUAL: …]` stage directions) and `02_narration_tts_ready.txt` (the
TTS-normalized narration derived from it). Both live in this folder.

This is an explanatory piece about general agent-system behaviour, not a
first-person project account — claims are checked against common engineering
description rather than a project's own files.

## Factual claims (DOUBLE-CHECK LAW)

| Beat | Claim | Verdict | Basis |
|------|-------|---------|-------|
| B00 | An agent can loop indefinitely while reporting success | ✓ | The reel's premise; demonstrated concretely in B06 |
| B02 | The agent loop is observe → decide → act → check result → repeat | ✓ | Standard description of the agent execution loop |
| B02 | Nothing in the loop intrinsically guarantees termination | ✓ | Correct — termination comes from an external limit, which is the beat's point |
| B02 | The agent has no built-in "I've tried this three times" check | ✓ | Correct absent explicit retry accounting |
| B03 | Models have a bounded working context window | ✓ | True of current transformer-based language models |
| B03 | Long-running tasks pack the window with tool results, errors, retries | ✓ | Standard, uncontroversial |
| B03 | Older content gets crowded out or deprioritized | ✓ | Stated qualitatively; no attention-mechanism specifics claimed |
| B03 | Drift means optimizing for the last error, not the original goal | ✓ | Correct characterization of the failure |
| B04 | Tools expect strict field shapes and formats | ✓ | True of function/tool schemas generally |
| B04 | A model can emit a plausible, well-formatted, invented argument | ✓ | Well-attested failure mode |
| B04 | Such a call may error, or may silently do something different | ✓ | Both paths real; the silent one correctly named as worse |
| B05 | An agent has no intrinsic alarm for being stuck | ✓ | Correct absent an explicit verifier |
| B05 | A stuck agent's output can be indistinguishable from a successful one | ✓ | The reel's central claim; follows from the above |
| B06 | The twelve-attempt deploy trace | ⚠ **illustrative** | A constructed worked example, not a logged incident. Every step is a realistic composition of the four modes already established. Declared as illustrative here per DOUBLE-CHECK LAW; the narration presents it as a walkthrough ("Let's walk through one"), never as a case study |
| B07 | Turn limits, verifier steps, and human gates are the standard mitigations | ✓ | Matches established agent-engineering practice |
| B07 | These fixes limit damage rather than improve capability | ✓ | Correct, and stated explicitly as the beat's judgment |

## Anti-staleness check (DOUBLE-CHECK LAW)

No model, vendor, version number, benchmark score, or drifting count appears
in the narration. The failure modes described are properties of the agent
loop itself, not of any particular system, so the reel should not date.

## Simplifications (declared)

- **Four discrete failure modes are a teaching device.** Real failures
  compound and interleave — which the reel demonstrates rather than hides:
  B06 shows three of the four firing inside a single trace.
- **Context drift is described behaviourally, not mechanically.** Attention
  dilution, position effects, and summarization strategies are all omitted.
  The behavioural account is correct at this level and is what the fix
  depends on.
- **"Ten failed attempts" (B05) and "twelve times" (B06) are illustrative
  counts**, chosen for narrative concreteness. They are not measurements and
  are not presented as such.
- **The verifier is described as "a second model call or a hard rule."** Real
  verification spans a wide range (assertions, integration tests, health
  checks, human review). The two named cases are the common ends of it.

## Content carried and cut

| Source | Status | Note |
|---|---|---|
| ¶1–¶18 narration | **All carried, verbatim and complete** | Every paragraph of the source narration appears in the reel, none abridged. ¶17 and ¶18 both land in B08: ¶17 opens it, the prompt and rubric sit in the middle, and ¶18 closes the beat — so the reel still ends on the author's own aphorism ("a system that's never once had to know the difference between succeeding, and just saying so") rather than on the call to action |
| `[VISUAL]` title card — terminal scrolling "Retrying…" | Rebuilt | Carried into B02's accelerating loop and attempt counter rather than a static title card; B00 is locked to `ClaudeComposerAsk` by COLD OPEN LAW |
| `[VISUAL]` B05 — "clean green checkmark box" | Retinted | Green is not in the Claude fidelity palette. Rebuilt as an ink summary card against the terracotta-marked failure log; the good/bad distinction is carried by label and position, not by a second hue |
| `[VISUAL]` fixes — replay with guardrails applied | Restructured | Would need its own ~45s beat and push the sheet past ten. The three fixes are carried as the B07 verdict artifact lines instead; see PEDAGOGY.md "Known deviations" |
| `[VISUAL]` end card — four panels with green checkmarks | Retinted + relocated | Same palette reason; the recap is carried by the B07 artifact card |

## Scene / beat map

| Beat | Scene / pattern | Notes |
|------|------------------|-------|
| B00 | ClaudeComposerAsk (Remotion) | Cold open — the agent that's stuck right now |
| B01 | B01_FourFailures (Manim) | BLUF — four empty panels named |
| B02 | B02_InfiniteLoop (Manim) | The ring runs, then keeps running; attempt counter climbs |
| B03 | B03_ContextDrift (Manim) | Goal block pushed to the window edge and faded |
| B04 | B04_HallucinatedArgs (Manim) | Tool form fills clean; one field has no schema match |
| B05 | B05_ConfidentlyWrong (Manim) | Ten failures beside one success card; the gap bracketed |
| B06 | B06_TwelveAttempts (Manim) | The worked trace; three of four modes light in the legend |
| B07 | ClaudeVerdictArtifact (Remotion) | Three guardrails + the deflationary fourth line |
| B08 | ClaudeComposerAsk (Remotion) | Your Turn — prompt + 3-item rubric |
| B09 | ClaudeTitleOutro (Remotion) | Title restate + @DivijPawar |

## Correction (post-build)

B00 was revised after the initial render to add an explicit self-introduction
and topic statement ("Hi — I'm Divij Pawar. This video is about why AI agents
fail silently…") ahead of the existing hook, per the house B00 cold-open rule:
every reel's opening beat must have the narrator say who they are and what the
video covers, not just show the welcome-screen UI — a returning-series viewer
still needs the self-intro; it is never assumed to carry over from a prior
video. The original narration, adapted directly from the source script's cold
open, had no self-intro convention and jumped straight into the hook. B00
audio, its Remotion render, the compiled master, and captions were all
regenerated to match.

## Free pipeline — no paid spend

Kokoro `am_onyx` (local, free) for all narration. No ElevenLabs, no FLUX, no
paid services. No publishing — the master stays in this folder.
