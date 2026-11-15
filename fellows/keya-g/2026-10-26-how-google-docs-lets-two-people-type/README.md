# How Google Docs Lets Two People Type in the Same Sentence

**Creator:** Keya G. · **Project:** Humanitarians AI / Brutalist Videos
**Reporting period:** Week 3

The folder is named for Week 3, the week this work counts toward.

[Script](SCRIPT.md) · [Beat sheet](beat_sheet.json) · [Portrait beat sheet](vertical/beat_sheet.json) · [Manim scenes](scenes.py) · [Portrait scenes](vertical/scenes.py) · [Fact check](FACTCHECK.md) · [Shot list](SHOTLIST.md) · [Prompts](PROMPTS.md) · [Frictional log](FRICTIONAL.md)

## This week's contribution

- **Question:** when two people type in the same sentence of a shared document, how does it avoid losing or scrambling their words? And if I press Ctrl+Z, will I undo my teammate's work too?
- **Prediction:** I wasn't sure. In shared documents I'd seen text arrive late or overlap for a moment, so I thought the last person to type might simply win.
- **What I built:** a 13-beat, 3:28 Brutalist explainer. It covers why simultaneous edits clash (positions shift), the browser and server each keeping a copy, operational transformation, the collaboration protocol and revision log, live cursors and delay, CRDTs as another approach, and where it still gets messy.
- **Result:** every change is sent as a small operation; clashing operations are transformed to fit each other, and the server puts every change in one order. In my own test, Ctrl+Z undid only my own typing.
- **Next:** the Week 3 progress video.

## Human and AI work

**My decisions:**
- Topic: I looked at what topics other fellows had made, then chose this one, a system design topic about a tool I use every day.
- My own test: one Google Doc open in two windows, typing in both, then Ctrl+Z in one. It undid only my own changes, and that became the hook and the verdict.
- Research from Google's 2010 engineering blog posts and the CRDT article, including finding the blog's lists showing that only changes are sent, not the whole document.
- Story order, overview correction, verdict (combined from three options), Your Turn prompt, and the CRDT beat framed as something I'm just starting to learn.
- I reviewed the audio, previews with audio, both review cuts and both masters, and asked for fixes to overlapping text in vertical beat 2 and to the beat 2 narration.

**AI tools and voices:**
- Claude (chat) guided my research questions and drafted an example script from my story plan, notes and test, which I edited and approved.
- Claude Code wrote the beat sheets, Manim scenes, fact check, shot list and prompts, and ran the builds and gate fixes with my approval.
- Narration is AI-generated (Kokoro `af_bella`) and says so in its first beat.

**What I rejected or corrected:**
- Beat 3 said "nobody's words get lost"; the sources only say everyone ends up with the same document, so the line now says that.
- Beat 7 said the server "sends each person an acknowledgement"; in the blog's example it goes only to the person who made the change, so it was corrected.
- Beat 9 said every character gets a permanent ID and that changes "merge in any order." My source didn't say either, so the beat now follows it: copies change on their own, without coordinating, and still end up the same.
- Beat 6 is attributed to Google's engineers, because the sources are 2010 blog posts and don't say how Docs works today.
- Beat 2 now says "I've worked with shared documents," with "for years" removed.

**What remains unverified or open:**
- See [FACTCHECK.md](FACTCHECK.md): none of the claims are left partly supported or unsupported; some are simplified or my own experience.
- How Google Docs works today may differ from the 2010 posts.
- I haven't studied CRDTs in depth, and the video says so.
- The outro logo card is marked "sparse by design" in both beat sheets, with a written reason.

## Watch

| Format | File | Link |
|---|---|---|
| 16:9 landscape, 3840×2160, 3:28 | `GoogleDocsTyping_KeyaG.mp4` | [Watch on Drive](https://drive.google.com/file/d/1YxS9SQbHZyXcfp8U_SRi9_nfZ9TU6ymr/view?usp=drive_link) |
| 9:16 vertical, 2160×3840, 3:28 | `GoogleDocsTyping_KeyaG.mp4` | [Watch on Drive](https://drive.google.com/file/d/1xGOzscr9giX3aa94Mpb4S8__JnP-KJDs/view?usp=drive_link) |

## Reproduce

Same toolkit and commands as the [Week 1 explainer](../2026-10-13-how-ai-draws-anime-frames/README.md#reproduce), on this folder.

## Sources

See the Sources list in [SCRIPT.md](SCRIPT.md#sources) and the claim-by-claim evidence in [FACTCHECK.md](FACTCHECK.md).
