# SHOTLIST — How Duolingo Decides What You Practice Next

Typed work order. Fourteen beats. Narration is `SCRIPT.md` verbatim. Beat IDs B01–B11 match script sections 1–11, so
"beat 3" and "beat 11" mean the same thing here as in the script. BVDT, BHTF and BOUT are sections 12, 13 and 14.

**Status: review cuts approved; finals built (see `build-state.json`). B03 has no lead silence. No exemptions
are set except `sparse_by_design` on BOUT, with your reason. Nothing is published.**

## Rules for every visual

- Simple illustrative graphics only: a forgetting curve, flashcard boxes, a strength meter, a half-life curve,
  exercise difficulty.
- **No Duolingo logo, owl or mascot, no app screenshots, no Duolingo colour scheme used as branding, no other
  branding.** The word "Duolingo" may appear as plain text only where the narration says it.
- Every meter, bar and tally is an illustration, not data. Mark them "illustrative". No axis numbers. No
  percentages at all: the 12% was dropped from B09.
- **Japanese text must render.** Every Manim `Text` containing kana sets `font="Hiragino Sans"` explicitly (fallbacks in
  the beat sheet: Hiragino Kaku Gothic ProN, YuGothic, Noto Sans JP). The default font drops the glyphs. Check the
  rendered frame for tofu boxes, not the source.
- **Portrait (9:16):** all text sits above 86% of the frame height (y < 0.86 × H); the bottom 14% stays empty. 9:16
  gets its own native layouts, not a crop of 16:9.
- Palette `humanitarians`: ink `#2F2A26`, terracotta `#E4572E` (one accent per beat), ground `#F3EBDD`.
- No dates on screen or in files. The year in beat 4 is spoken in the narration and is not shown on screen.
- Un-highlighted elements never fade below about 40% opacity.
- Math: no formula is shown. The paper's p = 2^(−Δ/h) is described in words and a curve. If you want the formula on
  screen, it must be typeset per `docs/MATH-TYPESETTING.md`, not as a text string.

## Library check

`./art scenes` was searched first for: forgetting curve and decay, spaced repetition schedule, flashcard boxes
(Leitner), strength meter and half-life curve, exercise difficulty band, the typed-then-corrected overview, a line
chart of exponential decay, and a timeline of review gaps.

| Need | Result |
|---|---|
| Typed and corrected overview | **Hit:** `BrutalistHesitantWriter` and `BrutalistHesitantWriter916` |
| Cold open, Your Turn | **Hit:** `ClaudeComposerAsk` and `ClaudeComposerAsk916` |
| Verdict page | **Hit:** `ClaudeVerdictArtifact` and `ClaudeVerdictArtifact916` |
| Outro | **Hit:** `LogoOutro` and `LogoOutro916` (same as Keya's earlier films) |
| Forgetting curve, half-life decay curve | **Miss.** Leads read and rejected: `TtScaleDecay` (reel-local scale decay), `K12Fig07ExpertiseReversal` (fixed reel-local chart). Custom Manim. |
| Spaced-repetition timeline of review gaps | **Miss.** `CwcMemoryTimeline` is about agent sessions. Custom Manim. |
| Leitner flashcard boxes | **Miss.** Only reel-local box diagrams for other films. Custom Manim. |
| Strength meter | **Miss.** `ThemeFactoryContrastMeter` is a contrast-ratio meter. Custom Manim. |
| Exercise difficulty ladder | **Miss.** Custom Manim. |

The toolkit says a genuine miss is logged to `TEMPLATE-MISSES.md` automatically. `./art scene-index` is not needed
because no component was added to the library. The misses are custom scenes in this reel's own `scenes.py`.

## Audio (the master clock)

Kokoro `af_bella`, generated. Pronounce: `Keya`, `shimasu` (option B), `mimasu` (option B) and `Leitner`
("LITE-ner"); see `PROMPTS.md`. Seconds are from the generated files.

| Beat | s | Beat | s |
|---|---|---|---|
| B01 | 9.69 | B08 | 19.61 |
| B02 | 16.02 | B09 | 10.88 |
| B03 | 9.11 | B10 | 16.73 |
| B04 | 12.31 | B11 | 11.09 |
| B05 | 17.39 | BVDT | 17.64 |
| B06 | 15.96 | BHTF | 17.60 |
| B07 | 19.18 | BOUT | 5.85 |

Total narration about 3:07 before any pauses. B03 narration is 9.11 s, above the 9 s minimum the hesitant-writer rule
needs. There is no lead silence on B03: audio and typing start together, as in the week 2 film.

## Beats

### B01 — Intro (bookend, Remotion `ClaudeComposerAsk`)
Greeting "Hi, Keya", topic "Irreducibly Human", ask: "Explain how Duolingo decides which word I should practice
next." Three result lines: Memory fades over time · Every word gets its own half-life · Practice lands just before
you forget. The AI-voice disclosure is spoken over the answered composer.

### B02 — Hook (Manim `B02_Hook`)
Two word cards slide in: します "do" and みます "look". A lane of ticks fills under each as the narration says they
kept coming back; early ticks are crosses and the last ones turn to checks. A question mark lands over the gaps:
"How did it decide when?" Your own experience, so nothing here claims data. Japanese in Hiragino Sans.

### B03 — Overview (bookend, Remotion `BrutalistHesitantWriter`)
Types "Reviews are random." in terracotta, deletes the whole sentence, types "Duolingo
predicts when you'll forget each word." in ink over three lines (five in 9:16, bigger type, week 2 recipe). The whole sentence is the trigger so the correction
replaces the sentence, not one word. Seed `keya-how-duolingo-decides-what-you-practice`. After render: media at
least 8 s, corrected sentence fully on screen before the cut.

### B04 — The forgetting curve (Manim `B04_ForgettingCurve`)
Axes "what you remember" against "time", no numbers. A notebook outline and the name "Hermann Ebbinghaus" on "studied
his own memory". The curve draws from high to low on "fades away over time", then is labelled "the forgetting curve"
with the note "no effort to keep it". The year is spoken only.

### B05 — Spaced repetition (Manim `B05_SpacedRepetition`)
Two stacked lanes on one time axis. Top, cramming: one big block of practice, then a long slide down. Bottom, spaced:
short blocks with growing gaps; each lifts the curve and each drop is flatter. A marker lands on the dip just before
the next block ("just before you're likely to forget"), then the label "spaced repetition".

### B06 — Leitner boxes (Manim `B06_LeitnerBoxes`)
Three boxes: review often · review less often · review rarely. A card is answered right and slides one box right.
Another is answered wrong and slides one box left. Three cards follow the same moves; badge "every card, the same
fixed rules". No box numbers or day counts on screen: York's schedule is only an example.

### B07 — Half-life (Manim `B07_HalfLife`)
A decay curve for one word. A span marks its half-life; the curve is at half height where it ends. A "time since you
last practiced" marker slides along until it meets the half-life: "about a fifty-fifty chance". Then the curve fades to
40% and a separate drawn strength meter for a skill slips to half-full: "time to practice", with a small
"illustrative meter". The meter is per skill, as in the script, so it is not read off the single word's curve.

### B08 — Half-life regression (Manim `B08_HalfLifeRegression`)
A generic word card with three drawn tallies: times seen · got it right · got it wrong. They flow into a box labelled
"half-life regression" (with "machine learning + data science" folding into it). A bar comes out: "predicted
half-life: how long this word will last in your memory". Tallies are marks, not real numbers.

### B09 — Did it work? (Manim `B09_DidItWork`)
"Did it work?" Two empty bars, "Leitner" and "half-life regression". Leitner grows long; half-life regression grows
to about 0.55 of its length (0.128 to 0.235 in the paper), no numbers, captioned "as reported by Duolingo". The bars
fade to 40% and a second panel, "tests with real learners", shows the word "mixed" with a flat line beside
"overall activity" and an arrow down beside "practice sessions". No up arrow, no percentages.

### B10 — Birdbrain (Manim `B10_Birdbrain`)
A box labelled "Birdbrain" lands. A ladder of exercise blocks, easy at the
bottom and hard at the top, each with a "right?" guess. Top blocks tagged "too hard: frustrated", bottom blocks
"too easy: already mastered", both readable; the middle is highlighted "just the right difficulty".

### B11 — Where it falls short (Manim `B11_FallsShort`)
"In my view" small at the top. A rounded rectangle "inside the app: what I do" with tick marks. Dashed outlines
outside it: "my interests", "Japanese I use somewhere else", "a mistake while speaking", each marked "not seen". All
held at readable opacity. No screenshots.

### BVDT — Verdict (bookend, Remotion `ClaudeVerdictArtifact`)
Title page, then the heading "The right word, just before I forget it", then your four verdict lines (the artifact
shows two lines at a time) ending "That's how shimasu and mimasu finally stuck."

### BHTF — Your turn (bookend, Remotion `ClaudeComposerAsk`)
Greeting "Your turn." The suggested prompt types into the composer and holds while the voice reads and discusses it.
Running text "paste this into Claude…".

### BOUT — Outro (bookend, Remotion `LogoOutro`)
The Humanitarians AI mark springs in, `@HumanitariansAI` settles beneath. Same outro as your earlier films
(`LogoOutro`, not `ClaudeTitleOutro`, which hardcodes `@NikBearBrown`).

## Portrait (9:16) notes

Each Manim scene gets a native vertical layout in `vertical/scenes.py`, stacked top to bottom, text above 86% of the
height. B05 stacks its two lanes; B06 stacks the boxes in a column or shrinks them in a row; B09 stacks the two bars;
B10 and B11 stay vertical by nature. The bookends use their `916` variants (`BrutalistHesitantWriter916`,
`ClaudeComposerAsk916`, `ClaudeVerdictArtifact916`, `LogoOutro916`).
