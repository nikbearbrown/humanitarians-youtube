# How Duolingo Decides What You Practice Next

**Creator:** Keya G. · **Project:** Humanitarians AI / Brutalist Videos
**Reporting period:** Week 5

The folder is named for Week 5, the week this work counts toward.

[Script](SCRIPT.md) · [Beat sheet](beat_sheet.json) · [Portrait beat sheet](vertical/beat_sheet.json) · [Manim scenes](scenes.py) · [Portrait scenes](vertical/scenes.py) · [Fact check](FACTCHECK.md) · [Shot list](SHOTLIST.md) · [Prompts](PROMPTS.md) · [Frictional log](FRICTIONAL.md)

## This week's contribution

- **Question:** I've learned Japanese on Duolingo for over a year. How does it decide which words I should practice next, and why did shimasu and mimasu keep coming back?
- **Prediction:** I thought it used stored data or some model to pick lessons.
- **What I built:** a 14-beat, 3:17 Brutalist explainer. It covers the forgetting curve, spaced repetition, Leitner flashcard boxes, a word's half-life and the strength meter, Duolingo's half-life regression model, how well it worked, Birdbrain, and what the model can't see.
- **Result:** it does use a model, and a specific one: half-life regression predicts how long each word will last in my memory, so a word comes back just before I'm likely to forget it. Its prediction error was nearly half that of the Leitner system, but live tests with learners were more mixed.
- **Next:** the Week 5 progress video.

## Human and AI work

**My decisions:**
- Topic from my own Duolingo learning; the hook from my own confusion between します (shimasu, "do") and みます (mimasu, "look").
- Research from the forgetting curve, spaced repetition and Leitner sources, the Duolingo blog and Birdbrain post, and the Settles & Meeder paper.
- Story order, overview correction, verdict (combined from three options), Your Turn prompt, and the limits beat as my own view.
- Pronunciations chosen by ear from test clips (shimasu and mimasu option B, Leitner as "LITE-ner").
- I reviewed the audio, previews with audio, both review cuts and both masters, and asked for fixes to the beat 3 sync and the beat 9 spacing.

**AI tools and voices:**
- Claude (chat) guided my research questions, checked my notes against the sources, and drafted an example script from my story plan, which I approved.
- Claude Code wrote the beat sheets, Manim scenes, fact check, shot list and prompts, and ran the builds and gate fixes with my approval.
- Narration is AI-generated (Kokoro `af_bella`) and says so in its first beat.

**What I rejected or corrected:**
- An AI answer for why spaced repetition works; I used the source's own wording instead ("just before you're most likely to forget").
- Two links that didn't support my claims (a third-party blog and a page about Duolingo's video calls) were dropped.
- Beat 9 first said half-life regression improved engagement by 12%. The paper shows that figure compares two versions of the model; against Leitner, live results were mixed. The 12% was removed, and "far more accurate" became "prediction error nearly half," because on another measure (AUC) Leitner scored slightly higher.
- Beat 7's strength meter is per skill, not per word, so the wording follows Duolingo's blog.
- Beat 10 no longer says Birdbrain "doesn't predict when you'll forget"; the source doesn't say that.
- Beat 13's prompt says "Use example numbers," because Claude would otherwise invent a half-life.

**What remains unverified or open:**
- See [FACTCHECK.md](FACTCHECK.md): 38 claims, none partly supported or unsupported; some are simplified or my own experience.
- The Birdbrain post does not say whether half-life regression is still used, so the video only says Duolingo "added another model."
- The outro logo card is marked "sparse by design" in both beat sheets, with a written reason.

## Watch

| Format | File | Link |
|---|---|---|
| 16:9 landscape, 3840×2160, 3:17 | `DuolingoPractice_KeyaG.mp4` | [Watch on Drive](https://drive.google.com/file/d/1MEv0HYcgRhY3lB-KX5PnNp7fYmzCF5nd/view?usp=drive_link) |
| 9:16 vertical, 2160×3840, 3:17 | `DuolingoPractice_KeyaG.mp4` | [Watch on Drive](https://drive.google.com/file/d/1BihWWLNagvOA3PH8b9FVMLnWEDQLzMuh/view?usp=drive_link) |

## Reproduce

Same toolkit and commands as the [Week 1 explainer](../2026-10-13-how-ai-draws-anime-frames/README.md#reproduce), on this folder.

## Sources

See the Sources list in [SCRIPT.md](SCRIPT.md#sources) and the claim-by-claim evidence in [FACTCHECK.md](FACTCHECK.md).
