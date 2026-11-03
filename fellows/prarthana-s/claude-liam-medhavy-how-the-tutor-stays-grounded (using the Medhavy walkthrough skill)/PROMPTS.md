# PROMPTS.md — How the Tutor Stays Grounded in Your Textbook

No paid generation. No image or video model is called by this reel.

- Every product visual is a real browser capture of the live hub and the live cancer textbook.
- Every other visual is a Remotion scene. Most come from the brutalist.art library; the reel-local scenes were built for this reel and used in the finals:
  - `GroundingFlow` (landscape B10)
  - `GroundingFlow916` (vertical B10)
  - `PanelFocus916` (vertical footage framing)
- Narration is local Kokoro TTS (`am_onyx`).

## Reconstructed prompts on screen (labelled as such)

**B00 (ClaudeComposerAsk)**
- Command: "When I ask Medhavy's tutor a question, what connects its answer back to the textbook?"
- Running text: "AI narration (Kokoro am_onyx) · central question"

**B14 (Your Turn, ClaudeComposerAsk)**
- Command: "Ask your textbook a question. Open one of the sources it lists. Check the answer against it."
- Running text: "Suggested prompt · reconstruction"

## Questions typed into the book's tutor on camera (real; answered by the site)

These go to the production tutor, which is the site's own OpenAI-backed service. Its answers are shown unedited.

| # | Step | Text | Why this question |
|---|---|---|---|
| Q1 | final `plan-book.json` / `plan-portrait.json` step 10 | **How does gene amplification turn a proto-oncogene into an oncogene?** | A content question squarely covered by Chapter 5 (§5.2.3, §5.4.2 "Gene Amplification"). It is asked from the 5.1 page, so an opened source may sit on a different page (V4). It is not conversational, so search runs. |
| Q2 | final `plan-book.json` / `plan-portrait.json` step 29 | **Can you explain that in simpler terms, with an analogy?** | Only makes sense with the prior turn ("that"), so it shows the conversation context. Its own words give the search little to go on, which is the honest V6 test. |
| Q3 | pilot plan only | **Thanks!** | **Pilot verification only.** Asked in `run-pilot` (V7: no source cards appeared). It was removed from the corrected `run-book` and from `run-portrait`, and is not in either final video. |

Q1 and Q2 were asked once in each of `run-pilot`, `run-book` and `run-portrait`. The final videos use the `run-book` answers (landscape) and the `run-portrait` answers (vertical).

Rejected alternatives:
- The suggested chips: they are page-title templates, so they're less natural as a "strong content question".
- The 2026-09-18 reel's questions: we want fresh footage, not a repeat.

## Capture

Every run went through the reel-local wrapper `capture/capture_masked.py`, which drives the toolkit's `capture_admin.py`. The plans used:

| Plan | Run(s) |
|---|---|
| `capture/plan-signin.json` | `run-signin`, with `--no-session` |
| `capture/plan-book.json` | `run-pilot`, then `run-book` after correction |
| `capture/plan-portrait-test.json` | `run-portrait-test` |
| `capture/plan-portrait.json` | `run-portrait` |

The session came from `save_session.py`, where Prarthana signed in herself. The agent typed no credentials.
