# Will AI Replace My Test Scripts?

**Creator:** Keya G. · **Project:** Humanitarians AI / Brutalist Videos
**Reporting period:** Week 2

The folder is named for Week 2, the week this work counts toward.

[Script](SCRIPT.md) · [Beat sheet](beat_sheet.json) · [Portrait beat sheet](vertical/beat_sheet.json) · [Manim scenes](scenes.py) · [Portrait scenes](vertical/scenes.py) · [Fact check](FACTCHECK.md) · [Shot list](SHOTLIST.md) · [Prompts](PROMPTS.md) · [Frictional log](FRICTIONAL.md)

## This week's contribution

- **Question:** AI can now test a website from plain English instructions. Will it replace the Selenium and JUnit test scripts I write?
- **Prediction:** I wasn't sure. Scripts that break whenever a locator changes looked like exactly the kind of work AI could take over.
- **What I built:** a 14-beat, 3:29 Brutalist explainer. It covers what software testing is, how Selenium and JUnit tests find, act and check, why scripts break when IDs change, how self-healing locators like Healenium pick the best match and report it, how vision-based AI agents look, decide, act and check from screenshots, my own RPA link, where AI helps, and where it fails.
- **Result:** AI is an addition to test automation, not a replacement. It can keep scripts running and suggest edge cases, but it costs money per run, can make different choices on different runs, and can heal to the wrong button. A human still decides what correct looks like.
- **Next:** the Week 2 progress video.

## Human and AI work

**My decisions:**
- Topic from my own work as an automation developer with Selenium and JUnit.
- The hook from my own experience: a test that kept failing because a button's ID changed, and the popup "X" example that runs through the video.
- Story order, overview correction, verdict, Your Turn prompt, and which beats are my own experience (beats 6, 9 and 10).
- Asked for beats 2, 8, 9 and 10 to be redesigned for the vertical cut, and approved each preview with audio.
- I reviewed the audio, previews with audio, both review cuts and both masters.

**AI tools and voices:**
- Claude (chat) guided my research and drafted an example script from my story plan and notes, which I edited and approved.
- Claude Code wrote the beat sheets, Manim scenes, fact check, shot list and prompts, and ran the builds and gate fixes with my approval.
- Narration is AI-generated (Kokoro `af_bella`) and says so in its first beat.

**What I rejected or corrected:**
- Beats 1 and 2 both said I write test scripts for a living. I removed it from both, including the on-screen text in the intro.
- Beat 7 first said Healenium uses machine learning and "page structure". It was rewritten to match Healenium's own documentation: it saves a working locator, scores elements when it breaks, uses the best match and reports it.
- Beat 10 is marked on screen as my own experience ("In my experience"), not a general claim.
- Beat 11's "different choices on different runs" was given a source (Anthropic's glossary on temperature).
- No employer names or project details, no product logos and no screenshots of commercial tools are used.

**What remains unverified or open:**
- See [FACTCHECK.md](FACTCHECK.md): 39 claims, none contradicted. Some are my own experience or framing, and two are simplified.
- Healenium is voiced with the default pronunciation, hee-LEE-nee-um.
- The outro logo card is marked "sparse by design" in both beat sheets, with a written reason.
- In the vertical cut, beat 7's label shows just "Healenium"; the narration still says "open-source".

## Watch

| Format | File | Link |
|---|---|---|
| 16:9 landscape, 3840×2160, 3:29 | `AITestScripts_KeyaG.mp4` | [Watch on Drive](https://drive.google.com/file/d/1XV2Hw2tAISymZfaXfiE7SS3T73iOWHVv/view?usp=drive_link) |
| 9:16 vertical, 2160×3840, 3:29 | `AITestScripts_KeyaG.mp4` | [Watch on Drive](https://drive.google.com/file/d/1Ptm9ROj9V7Z4leL3Xd01fk6D_TwA5GXn/view?usp=drive_link) |

## Reproduce

Same toolkit and commands as the [Week 1 explainer](../2026-10-13-how-ai-draws-anime-frames/README.md#reproduce), on this folder.

## Sources

See the Sources list in [SCRIPT.md](SCRIPT.md#sources) and the claim-by-claim evidence in [FACTCHECK.md](FACTCHECK.md).
