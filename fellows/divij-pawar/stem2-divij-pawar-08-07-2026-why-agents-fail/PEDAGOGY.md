# PEDAGOGY GATE — Why Agents Fail

## Narration Review

**Topic:** The four ways AI agents fail, and the three guardrails that contain them
**Register:** Teardown (narrated by Divij Pawar)
**Audience:** Smart non-technical viewers; high-school technicality per the source script
**Series:** STEM — Agents, 2 of 3 (siblings: STEM1 *What Makes an AI Agentic?*, STEM3 *The Agent's Dilemma*)

### Source & Adaptation

Body narration (B01–B07) is carried **verbatim** from
`02_narration_tts_ready.txt`, split on its own paragraph boundaries. The
source is already TTS-normalized; no rewriting was needed or done.

What was **added**, because the source script has no bookends:

- **B00 (cold open)** — reuses source ¶1 verbatim; the composer props are new.
- **B08 (your turn)** — source ¶17 and ¶18 verbatim, plus a **new** prompt and
  3-item rubric. HANDOFF LAW requires a prompt read aloud and discussed; the
  source has a rhetorical question ("did anything actually check that?") but
  no runnable prompt.
- **B09 (outro)** — new, matching the series sign-off.

Nothing was cut. Every paragraph of the source narration appears in the reel.

### Teaching Arc ✓

- **B00 (Cold open):** An agent stuck right now, still reporting success
- **B01 (BLUF):** Executive summary — four failure modes named, one to be fixed live
- **B02 (Mode 1):** The infinite tool-call loop; nothing in the cycle guarantees it stops
- **B03 (Mode 2):** Context drift; the original goal crowded out of the window
- **B04 (Mode 3):** Hallucinated function arguments that look like facts
- **B05 (Mode 4):** Confidently wrong — the gap between what happened and what's reported
- **B06 (Worked example):** The twelve-attempt deploy, with all four modes visibly firing
- **B07 (Verdict):** Three guardrails — turn limit, verifier, human gate
- **B08 (Your turn):** Scaffolded prompt + 3-item rubric
- **B09 (Outro):** Title restate + handle

**EXECUTIVE-SUMMARY LAW:** satisfied at B01 — the four modes are named as a
set, and the promise ("we're going to fix one, live") is made, before mode 1
is described. The viewer holds the whole shape first.

**FRAMEWORK-BEFORE-EXAMPLES:** B01 puts all four panels on screen empty;
B02–B05 fill them one at a time; B06 replays all four at once inside a single
trace. The framework is stated, then instantiated, then used.

### Factual Check ✓

| Claim | Verdict | Note |
|---|---|---|
| The agent loop is observe → decide → act → check → repeat | ✓ | Standard agent-loop description |
| Nothing intrinsic to the loop guarantees termination | ✓ | Correct — termination is an external constraint, which is exactly the beat's point |
| Models have a bounded context window | ✓ | True of all current transformer-based LMs |
| Older context gets crowded out or deprioritized as a task runs long | ✓ | Correct; stated qualitatively, no numbers claimed |
| A hallucinated tool argument may error *or* silently do the wrong thing | ✓ | Both failure paths are real; the silent one is correctly named as worse |
| An agent has no intrinsic signal for "I am stuck" | ✓ | Correct absent an explicit verifier or limit — which is the setup for B07 |
| Turn limits / verifiers / human gates are the standard mitigations | ✓ | Matches established agent-engineering practice |
| "Repeats twelve times" (B06) | ⚠ **illustrative** | A constructed worked example, not a logged incident — see SOURCES.md |

No model names, vendors, versions, or benchmark figures appear anywhere. The
reel should not date.

### Register & Tone ✓

- Mechanism first, judgment second: each mode is explained by what the loop
  actually does, then judged for why it matters.
- The strongest Teardown line is B05's — a stuck agent and a successful agent
  are *visually identical* until someone checks. The reel holds that.
- B07 refuses the easy ending: "None of these fixes make an agent smarter."
  The verdict is deflationary and correct.
- Narration budget: body beats run 103–148 words. Above the ~70-word guidance,
  consistent with the sibling reel `accountability-mesh` and with this series.

### Falsifiability ✓

**B05** is the dedicated stress-test beat, and it stress-tests *observation
itself*: it establishes that the reel's own subject matter is undetectable by
the obvious method (reading what the agent says). **B06** then demonstrates it
concretely across twelve attempts. This is why the guardrails in B07 are all
external checks rather than better prompting — the video earns that conclusion
rather than asserting it.

### Known deviations from house defaults

1. **Runtime.** The source script header says "~9 minutes." At the rate Kokoro
   `am_onyx` actually produced on `accountability-mesh` (~195 wpm), this
   narration runs **≈5.1 minutes**. Audio is the master clock and cannot be
   stretched at compile. **Flagged for the human — no content was invented to
   close the gap.**
2. **Body-beat length.** B02–B07 run 32–46s, past the 14–22s in `agents.md`
   but matching the established series shape.
3. **The three fixes sit on the verdict card (B07), not a body beat.** The
   source `[VISUAL]` proposed replaying the twelve-step example with
   guardrails applied. That replay would need its own 45s beat, which would
   push the sheet past ten beats. The fixes are instead carried as the four
   verdict artifact lines, and B06's Manim scene keeps the trace that makes
   them legible. Logged here as a deliberate structural choice.

---

## VERDICT: PASS

**Prepared by:** Claude (beat-sheet authoring pass)
**Approved by:** Divij Pawar
**Date:** 2026-08-17

Approved for audio generation and render as documented above, including the
runtime deviation (~5.1 min vs. the source header's ~9 min target) and the
B08 restructure (¶17/¶18 now bracket the prompt so the beat closes on the
source's own aphorism rather than a new call to action).
