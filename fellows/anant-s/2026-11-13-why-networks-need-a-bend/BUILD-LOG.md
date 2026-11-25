# BUILD-LOG — Why Neural Networks Need a Bend

## 2026-11-22 — planning (film 6 of 7, planning session; stops at GATE P)
- **Choices.** The human chose the topic, the skill (ai-explainer) and the branding (default claude-liam / @NikBearBrown). The planning session picked the title.
- **Greeting:** "Jambo, Liam", Swahili, one word from the lexicon. It is unique in the series (film 1 used Ciao), and Liam never takes "Wagwan".
- **Title and slug:** "Why Neural Networks Need a Bend", slug `claude-liam-nonlinearity`.
- **Evidence.**
  - `demo/nonlinearity_demo.py` was executed in about 60 s, and its output is the only source of on-screen numbers.
  - Seed 0 was the first seed for the collapse matrices. Seeds 0–11 were previewed for small, legible integers, and seed 0 was kept.
- **DOUBLE-CHECK corrections:** five, recorded in FACTCHECK #2, #3, #23 and #28 plus the B00 result line.
- **Pronunciation.** Checked with `--phonemize`; the fixes are pinned in `metadata.pronounce` and verified through `apply_lexicon`, with no audio made.

  | Word | espeak default | Problem | Pinned IPA |
  |---|---|---|---|
  | ReLU | /ɹˌiː ˌɛljˈuː/ | spelled out | /ɹˈɛluː/ |
  | XOR | /ˌɛksˌoʊˈɑːɹ/ | spelled out | /ˈɛksɔːɹ/ |
  | numpy | /nˈʌmpi/ | wrong final vowel | /nˈʌmpaɪ/ |
  | Jambo | /dʒˈæmboʊ/ | wrong first vowel | /dʒˈɑːmboʊ/ (Swahili JAHM-boh) |

  Confirm them by ear at GATE 0 with a whisper check.
- **Duration.** 840 words is about 4.0 min at film 1's measured Kokoro pace (3.51 words/s: 674 words in 192.3 s). That is longer than film 1 (3:12) and the typical 1–3 min ai-explainer. Duration is an output, not a target. Trim candidates, if wanted:
  - B10 (−68 words, about 19 s; B09 still carries FALSIFIABILITY).
  - B04 (−67 words, about 19 s; B03 still proves the collapse).
- **ASK→RESULT** is applied at the cold open only. Body graphics illustrate the B00 ask; this is film 1's precedent.
- **Library-first.** Eight `scene_search.py --no-log` queries returned no reusable hit (see SHOTLIST). Body visuals are Manim.
- **Gates passed:**
  - `bookend_check` PASS.
  - `beat_lint` clean.
  - `math_layout_check` returns no errors. It was called as a function; nothing was written.
- **Not done, by design.** No audio, no rendering, no `scenes.py`, and nothing written inside `C:\Users\anant\brutalist.art`.
- **Status:** waiting for narration approval (GATE P). Then the main session runs audio (GATE 0) and the render, one film at a time.

## Plan for the render session (design rules to honour)
- **GATE A stub-safety.** GATE A pre-flights `scenes.py` as an isolated copy. Copy film 1's pattern:
  - `REEL = Path(os.environ.get("ART_REEL", r"C:/Users/anant/stem-films/youtube/claude-liam-nonlinearity"))` with a `_load()` fallback for `beat_sheet.json`, `mp3/words.json` and `demo/evidence.json`.
  - Wrap every `c2p` or point call in the stub-safe `P()` / `V()` helpers.
  - Put no fake `class Bxx_` lines in docstrings.
  - Name scene classes literally `B02_TwoMoves` … `B10_StraightAgain`, each subclassing `Scene`.
- **Frame clock.** Count frames as `ceil(run_time·fps)`; reuse film 1's `Clock` class. Key reveals to spoken words in `mp3/words.json` (run `align.py` after audio). Land each scene within ±3% of its audio.
- **Spotlights are boxes, never underlines,** with a minimum height. This covers the "=" in B03, the right-hand side in B04, the clip in B07 and the kinks in B10. An underlined "−" reads as "=", and an underlined "=" reads as "≡" (film 1 lesson).
- **GATE V needs ≥55% canvas fill.** Specific risks:
  - B03: two 2×2 matrix paths must span the width. Put the paths left and right with the equation across the bottom, at a MathTex scale near 1.1–1.3.
  - B07: five table columns must be wide.
  - B09: two 10×10 grids side by side should each be about 5 units wide.
  - B01: fontSize 150 was chosen for a longer first line than film 1's. Re-check fill at render, since film 1 needed 160.
- **Keep all text within x ±6.0 and y ±3.2** (Manim units), inside title-safe.
- **One terracotta moment per beat**, as named in each `shot.show`. Ink and grey everywhere else.
- **Point colouring.** XOR points use hollow vs filled ink, so colour is not the only cue and terracotta stays free for the event.
- **Evidence assertions in scenes.**
  - B06 plots `deep_linear.run.curve` directly.
  - B09 colours tiles from `seeds.*.solved_mask`.
  - B10 recomputes the trace from `relu_hand` weights and asserts it equals `kinks.samples`.
- **Outro.** The locked `ClaudeTitleOutro` may wrap the 31-character title. That is accepted as in film 1, because the lock forbids altering the title.

## 2026-11-22 — GATE P: narration and title approved
- In the main session the human wrote "approve all six". The main session relayed it here.
- That approves the narration as drafted (all 14 beats, B10 kept) and the title "Why Neural Networks Need a Bend".
- Next: Kokoro audio (GATE 0), silence padding, whisper pronunciation check, align, `scenes.py`, gates A/W/B, then low-res previews. No 4K render in this session.

## 2026-11-22 — audio, word clock, scenes.py, low-res previews (no 4K)
- **GATE 0 (audio).** Kokoro am_onyx, 14 beats.
  - `pad_silence.py` applied B01 lead 0.8 s, BVDT lead 0.5 s and BOUT tail 1.0 s.
  - **Measured total: 251.7 s (4:11.7).**
- **Whisper check** (faster-whisper base, every beat diffed against `narration_text`). No real mispronunciation, so no fixes and no regeneration.
  - Pins confirmed by ear-proxy:
    - ReLU heard as "relu"/"relo".
    - XOR heard as "XOR"/"Exor"/"X or".
    - numpy heard as "numpy".
    - Jambo heard as "Jombo" (≈ JAHM-boh).
  - The remaining diffs are digit normalisation and whisper homophones: plain/plane, two/to, seeded/ceded, weights/wait, "Nik Bear Brown" as one word.
  - Worth a human listen: B02 "flatten negatives" (heard "flat negatives") and B04 "Add a shift" (heard "At a shift").
- **Word clock.** `align.py` aligned 14/14 beats with 0 fallback.
- **scenes.py.** Nine Manim scenes, B02_TwoMoves … B10_StraightAgain, in the house pattern: `_load` with REEL fallback, `cue()`, a frame-quantised `Clock`, `P`/`V`, and `box()`.
  - Every number comes from `demo/evidence.json`. B04 re-runs the seed-1 draw and asserts it against the evidence; B06, B07, B09 and B10 assert their values.
  - Terracotta appears only on non-text shapes: box outlines, the B02 crease lines, the B05 ring, the B08 folded segment and the B10 kink dots. Text, numbers and arrows are INK (main-session rule, GATE T §8.3).
- **Gates per scene** (scenes copied in isolation for GATE A): **A=0, W=0, B=0 for all nine.**
- **Previews.** `manim -ql --fps 24`, rendered to scratch outside the film folder, with frames at 15/50/85/99%.
  - Duration vs audio:

    | Beat | Diff |
    |---|---|
    | B02 | −0.2% |
    | B03 | +1.1% |
    | B04 | 0.0% |
    | B05 | 0.0% |
    | B06 | +0.3% |
    | B07 | +0.9% |
    | B08 | −0.1% |
    | B09 | +0.6% |
    | B10 | +1.2% |

  - GATE V (`final_frame_check.py --frames-dir` on the 50/85/99% frames): **0 BLOCKER, 0 MAJOR.**
  - An extra dry-run check confirms all text is within ±6.0 x / ±3.2 y and every font is ≥ 32.
- **Fixes found by looking at frames:**
  - B07 matrices bled right; they were shrunk and moved.
  - B02, B07 and B09 underfilled at 50%. B02 now draws the ReLU axes from t=0.2, B07 shows the x column early, and B09 ghosts the 8-unit grid and uses a callout card.
  - B08 band contrast was too low; it is now SOFT at 50%.
  - B06 per-bar values collided and became "each 0.5". B10 piece equations were struck through by the t-axis and moved to the lower left.
  - Several overruns were tightened.
- **Known small lag:** B02's strip lands 0.19 s after "A network alternates". This is within tolerance.
- **The human also wrote "Approve as drafted" in this session**, matching the GATE P approval above.
- **Not done (by instruction):** no 4K render, no `remotion_scenes.py`, no `./art run` or `final`.

## 2026-11-22 — B02 bottom strip removed (human request)
- At the human's request ("try to remove bottom strip"), B02 no longer draws the `x → W₁ → bend → W₂ → y` strip.
- On "layer, bend, layer", the word "bend" in the ReLU header is boxed in ink instead. This removes the 0.19 s lag noted above.
- The show event was updated in `make_sheet.py`, `beat_sheet.json` (narration, audio and timing untouched), `SCRIPT.md`, `SHOTLIST.md` and `CHECKS-REPORT.md`.
- Re-checked B02: A=0, W=0, B=0. The preview is 19.12 s against 19.16 s of audio (−0.2%), and the clock is never late. GATE V on the 15/50/85/99% frames shows 0 BLOCKER and 0 MAJOR.

## 2026-11-23 — final (main session)
- **Build chain:** `./art run` exit 0; GATE V clean across 28 frames; GATE T PASS; `./art final` exit 0.
- **Master:** `exports/landscape/claude-liam-nonlinearity.mp4`, 3840×2160, 24 fps, 251.9 s. Its hash matches `.verified.json`, status `ready`.
- **Strip check** (`check_no_labels`, background-relative, label corner and full bottom band): PASS on 126 samples.
  - An earlier run of the absolute-darkness version falsely flagged the dark-polarity outro.
- **Master check:** PASS. **Loudness:** PASS at −24.67 LUFS.
- **Hand QC:** every beat checked on the final at 15/50/85%. The garbled-looking B03 "x" at 85% is a mid-Write frame and settles correctly.
- **Not published.**
