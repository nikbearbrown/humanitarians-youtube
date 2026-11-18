# SHOTLIST — How Your Phone Types Japanese

Typed work order. Fourteen beats. Narration is `SCRIPT.md` verbatim. Beat IDs B01–B11 match script
sections 1–11, so "beat 3" and "beat 11" mean the same thing here as in the script. BVDT, BHTF and BOUT are
sections 12, 13 and 14.

**Status: audio and all nine Manim scenes written, previews rendered.** Narration is generated. `scenes.py` (16:9) and
`vertical/scenes.py` (9:16, native layouts) hold every Manim scene. Low-quality previews of all 18 scene-aspect pairs and
a contact sheet per scene are in `_preview/` (not for upload). Not yet run: `./art run`, the review cuts, `./art final`.

## Rules for every visual

- Simple illustrative graphics only: kana, kanji, candidate lists, probability bars, word-split paths.
- No real product logos. No screenshots of commercial apps. Every IME candidate list is an illustrative
  animation, because Keya's own InputKing test showed romaji to kana only.
- **Japanese text must render.** Every Manim `Text` containing kana or kanji sets `font="Hiragino Sans"`
  explicitly (fallbacks in the beat sheet: Hiragino Kaku Gothic ProN, YuGothic, Noto Sans JP). The default
  font drops the glyphs. Check the rendered frame for tofu boxes, not the source.
- **Portrait (9:16):** all text sits above 86% of the frame height (y < 0.86 × H); the bottom 14% stays
  empty. 9:16 gets its own native layouts, not a crop of 16:9.
- Palette `humanitarians`: ink `#2F2A26`, terracotta `#E4572E` (one accent per beat), ground `#F3EBDD`.
- No dates on screen or in files. The year in beat 10 is spoken in the narration and is not repeated on
  screen unless Keya chooses to.
- Un-highlighted elements never fade below about 40% opacity.

## Library check

`./art scenes` was searched first for: the hesitant writer, Japanese text, kana-to-kanji candidate lists,
probability bars, word-split paths, timelines and script comparisons.

| Need | Result |
|---|---|
| Typed and corrected overview | **Hit:** `BrutalistHesitantWriter` and `BrutalistHesitantWriter916` |
| Cold open, Your Turn | **Hit:** `ClaudeComposerAsk` and `ClaudeComposerAsk916` |
| Verdict page | **Hit:** `ClaudeVerdictArtifact` and `ClaudeVerdictArtifact916` |
| Outro | **Hit:** `LogoOutro` and `LogoOutro916` (same as Keya's earlier film) |
| Kana and kanji display, candidate fans | **Miss.** Only code-display and chart components came back. Custom Manim. |
| Scored paths / probability bars | **Partial lead:** `ExecutedData` (rows or zero-baseline probability comparison). It is for measured data, and these scores are illustrative, so it was not used. |
| Word-split paths | **Miss.** Custom Manim. |
| Timeline | **Leads only:** reel-local timelines for other films. Not reusable as they are. Custom Manim. |

The toolkit says a genuine miss is logged to `TEMPLATE-MISSES.md` automatically. That file showed no change after these searches, so the logging was not confirmed. `./art scene-index` is not needed because no component was added to the library.

## Beats

| Beat | Section | Lane | Asset | What the viewer sees | Audio (s) |
|---|---|---|---|---|---|
| B01 | 1 Intro | remotion | `ClaudeComposerAsk` | Composer: "Hi, Keya"; the ask types in; three result lines | 11.75 |
| B02 | 2 Hook | manim | `B02_Hook` | hana splits to 花 flower / 鼻 nose; "hashi" typed; 橋 / 箸 / 端 fan out; a question mark | 13.27 |
| B03 | 3 Overview | remotion | `BrutalistHesitantWriter` | Types "Autocomplete is a new AI trick." in terracotta, deletes it, types "Japanese keyboards were predicting words long before chatbots." in ink | 9.90 |
| B04 | 4 About Japanese | manim | `B04_AboutJapanese` | Speaker counter to 120 million+; a run of Japanese text with no gaps | 8.38 |
| B05 | 5 Three scripts | manim | `B05_ThreeScripts` | One mixed sentence tinted by script; hiragana, katakana, kanji land in order; 花 and 鼻 share "hana" | 17.43 |
| B06 | 6 Typing | manim | `B06_Typing` | Keys H, A, S, H, I light; letters fold into はし; a kana-only keyboard stops; an IME box opens | 16.92 |
| B07 | 7 Homophones | manim | `B07_Homophones` | Four rows build: はし, はな, あめ, しろ, each splitting into its kanji | 13.01 |
| B08 | 8 How the IME chooses | manim | `B08_HowImeChooses` | Every split, every kanji, two score bars per path; the highest path lights up | 17.05 |
| B09 | 9 No spaces | manim | `B09_NoSpaces` | ここではきものをぬぐ large with romaji; split two ways (は highlighted) to ここで履物を脱ぐ with a shoe outline and ここでは着物を脱ぐ with a kimono outline; then "You: where you are" (door outline to footwear) beside "IME: which split is more common in text" (two illustrative bars, no numbers) | 16.49 |
| B10 | 10 Old vs. new | manim | `B10_OldVsNew` | Three-stop timeline: dictionary and grammar with homophones weighed by context and frequency, counted text, Transformer networks converting as you type (no ChatGPT logo) | 26.28 |
| B11 | 11 Where it fails | manim | `B11_WhereItFails` | A name and a brand-new word fail a dictionary lookup; the kana is cut in the wrong place and two wrong kanji (毛, 矢) are marked | 8.73 |
| BVDT | 12 Verdict | remotion | `ClaudeVerdictArtifact` | Artifact page: title, heading "Predicting what comes next" | 21.48 |
| BHTF | 13 Your turn | remotion | `ClaudeComposerAsk` | "Your turn."; the suggested prompt types in | 19.65 |
| BOUT | 14 Outro | remotion | `LogoOutro` | Humanitarians AI mark and `@HumanitariansAI` | 4.82 |

Total narration: 205.2 s (about 3:25).

## Checks run on the scenes

- **Gates A, W and B** (`static_scene_check.py`, `wcag_margin_check.py`, `manim_layout_audit.py --png --curve-strict`, with
  `--portrait` for 9:16) were run on all 18 scene-aspect pairs, in a scratch copy: all clean after fixes.
- **Timing:** every cue starts on its spoken word (measured with Whisper word times from the audio). The worst cue is 0.07 s late.
- **Portrait:** every sampled frame of all nine scenes keeps content at or below 85.5% of the height (limit 86%), with margins
  on both sides.
- **Japanese:** set in Hiragino Sans, explicit in every `Text`. All kana and kanji were checked in rendered frames.
- **Fixes made along the way:** the gates found real overlaps and out-of-frame text (cut marks drawn through text, cross-outs
  on kanji, captions colliding). They were fixed in the scenes. No gate was loosened. Scenes use only Manim calls the static
  gate's stand-in supports, so a few effects were swapped for equivalents.

## On-screen examples that are illustrative

- **B08** shows three paths for はしをわたる (橋を渡る, 箸を渡る, 端を渡る). jisho.org confirms the words and readings
  (渡る is わたる, "to cross over") but lists no entry for the phrase itself. The bars have no numbers and are labelled
  illustrative.
- **B11** shows けや cut in the wrong place and offered 毛 and 矢. jisho.org confirms 毛 is け (hair) and 矢 is や (arrow).
  The failure is an illustration, not a measured result.
- **B09** is as in the approved version.

## Beat 9 details

- Japanese is set in **Hiragino Sans** (explicit in every `Text`), checked in rendered frames: kana, 履物, 着物 and 脱ぐ all
  draw correctly, no missing-glyph boxes. The kanji and readings were verified on jisho.org.
- Romaji under the first line is the unsegmented string as typed: `kokodehakimonowonugu`.
- は is crimson in both splits (start of はきもの in the top path, end of ここでは in the bottom path). It is the beat's one accent.
- Icons are simple outlines (shoe, kimono, door). No person icon, no logo.
- The bars are labelled "illustrative bars, not real numbers". No frequencies are invented.
- **9:16** is its own layout, not a crop: the two paths stack, and "You" sits above "IME" instead of beside it, so the text
  stays large enough to read. Every sampled frame keeps all content above 86% of the frame height (lowest 84.2%) and inside
  the portrait safe band the toolkit's layout gate uses.
- Cue times come from word timings of beat 9's audio. That audio is unchanged. If it is regenerated, re-time the cues.

## Decisions recorded

- Beat 10 and beat 11 narration changed as Keya decided (script and beat sheet).
- Pronunciation: clip A for hashi, はし and ame, plus the H-A-S-H-I letter-name fix.
- Claude composer and verdict bookends kept. They are redrawn graphics, not screenshots.
- Keya's name in katakana is ケヤ (beats 5 and 11 plan; beat 11 no longer mentions it).

## Open questions for Keya

1. **Listen to** beats 2, 6, 7, 10 and 11 (regenerated). Whisper read them back correctly. It heard ame as "Aimee" in
   beat 7, so that one is for your ear: you wanted "AH-meh".
2. **B03 timing.** The typing needs about 8 s and the audio is 9.9 s. After rendering, confirm the corrected sentence is
   fully on screen before the cut.
3. **Beat 10, "the same design behind ChatGPT".** Both are Transformers, but the paper's models are encoder-decoders and
   ChatGPT-style models are decoder-only. See `FACTCHECK.md`. Narration kept as you wrote it.
