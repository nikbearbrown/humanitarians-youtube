# Frictional log — Explainer: Agent Harness

## 2026-09-11 — claude-hai explainer, 16:9 + 9:16

- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G
Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `PROOF-REVIEW.md`
(11/12, gate PASS), `_qc/REPORT.md`, `agent-harness.mp4`, `short/agent-harness-short.mp4`.
(YouTube / Drive links: TBD.)

**What I was working on.** An explainer on what an "agent harness" is — a model
wrapped in a loop (decide → act → observe → repeat) with tools. Framework-first.
Added a reusable "loop" visual to the card generator since a harness is literally a loop.

**What I tried, and what I expected.**
* To save time, I had the audio generation and the Remotion bookend render run in
  parallel.
* I expected the measured audio durations (`actual_duration_s`) to survive that.

**Where it resisted, and what I did next.**
* They did not survive. Both `generate_audio_kokoro.py` and `remotion_scenes.py` write
  `beat_sheet.json`, and running them at once raced — `actual_duration_s` came back
  null. The compiler then fell back to the *estimated* durations and produced a 236s
  cut instead of ~155s: every beat freeze-held to its estimate, narration plus long
  silent padding. No error.
* Caught because a QC frame sampled at the "verdict" timestamp showed the wrong beat —
  the timeline didn't match. Re-ran audio first, then Remotion, sequentially. Timing
  then correct (160s matched the audio sum).
* Also made the flow diagram center any number of inputs (this reel uses two:
  "the model" + "the tools").

**What Claude contributed, and what I did with it.**
* Mine: the topic, the framework, GATE P approval, review.
* Claude's: the beat sheet; extended `make_cards.py` (the loop kind + dynamic flow);
  all rendering/compiling; diagnosed the 236s stretch and re-ran sequentially; PROOF.

**What I understand now, and what I still do not.**
* Understood, and this is the lesson that keeps recurring: never run the audio and the
  Remotion render in parallel — they both mutate the beat sheet, and the race produces
  a plausible-but-wrong-length file with no error. Audio → verify durations → render.
* Not resolved: the worked example is asserted, not a captured real agent run.
