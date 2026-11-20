# How Do Websites Know I'm Not a Robot?

**Creator:** Keya G. · **Project:** Humanitarians AI / Brutalist Videos
**Reporting period:** Week 6

The folder is named for Week 6, the week this work counts toward.

[Script](SCRIPT.md) · [Beat sheet](beat_sheet.json) · [Portrait beat sheet](vertical/beat_sheet.json) · [Manim scenes](scenes.py) · [Portrait scenes](vertical/scenes.py) · [Fact check](FACTCHECK.md) · [Shot list](SHOTLIST.md) · [Prompts](PROMPTS.md) · [Frictional log](FRICTIONAL.md)

## This week's contribution

- **Question:** why does a website keep asking me to click traffic lights, and how does it actually decide whether I'm a person or a bot?
- **Prediction:** I thought the picture puzzle was the test.
- **What I built:** a 13-beat, 3:16 Brutalist explainer. It covers what a CAPTCHA is, what the "I'm not a robot" checkbox really checks, reCAPTCHA v3's score with no puzzle, Cloudflare's background challenges, research showing bots beat people on distorted text and image puzzles, and what websites check now.
- **Result:** the picture was never the whole test. Much of it is how you behave: cookies, browsing history and how you move. Puzzles are still around, but more and more checks happen in the background.
- **Next:** the Week 6 progress video.

## Human and AI work

**My decisions:**
- Topic: links to my automation work and to something that annoys me as a user; Cloudflare kept to one part of the story rather than the whole company.
- Research from Wikipedia, a Merchant Risk Council post, Cloudflare's own blog, IT Brew, and the UC Irvine and ETH Zurich studies.
- A rule for this video: nothing goes in that isn't checked against a listed source.
- Story order, overview correction, verdict (combined from two options), Your Turn (combined from three options), and the extra line in beat 4 about the three types of CAPTCHA.
- I reviewed the audio, previews with audio, both review cuts and both masters, and asked for fixes to overlapping and edge-touching text in five beats and to the vertical verdict card.

**AI tools and voices:**
- Claude (chat) guided my research questions, found the two studies, and drafted an example script from my story plan and notes, which I edited and approved.
- Claude Code wrote the beat sheets, Manim scenes, fact check, shot list and prompts, and ran the builds and gate fixes with my approval.
- Narration is AI-generated (Kokoro `af_bella`) and says so in its first beat.

**What I rejected or corrected:**
- Beat 4 dropped "that computers couldn't read"; my sources don't say why.
- Beat 9 first said the ETH model "had to fake human signals"; the paper doesn't say it couldn't pass without them, and the article that did couldn't be opened. It now says what the paper found: the system relies heavily on cookies and browsing history.
- Beat 10's "blocking bad behaviour" is now credited to one Cloudflare leader, as his view.
- The verdict was softened to match the sources: puzzles are still around, and websites are moving "more and more" toward behaviour checks.
- Beat 8's participant counts are cited to the paper, not a news report that gave different numbers.
- The vertical verdict card was rewritten as four complete thoughts, because a numbered list had split one sentence across four items.

**What remains unverified or open:**
- See [FACTCHECK.md](FACTCHECK.md): none of the claims are left partly supported or unsupported; some are simplified or my own experience.
- The bot figures in beat 8 come from earlier studies the UC Irvine paper compares against, as the narration says.
- The outro logo card is marked "sparse by design" in both beat sheets, with a written reason.

## Watch

| Format | File | Link |
|---|---|---|
| 16:9 landscape, 3840×2160, 3:16 | `NotARobot_KeyaG.mp4` | [Watch on Drive](https://drive.google.com/file/d/1PpE-skVRqC7sFqDuWk-9vd6OwWpqiKIq/view?usp=drive_link) |
| 9:16 vertical, 2160×3840, 3:16 | `NotARobot_KeyaG.mp4` | [Watch on Drive](https://drive.google.com/file/d/1kfwZXngWe6TT0LfzJyQRag8MxAZ-DbUi/view?usp=drive_link) |

## Reproduce

Same toolkit and commands as the [Week 1 explainer](../2026-10-13-how-ai-draws-anime-frames/README.md#reproduce), on this folder.

## Sources

See the Sources list in [SCRIPT.md](SCRIPT.md#sources) and the claim-by-claim evidence in [FACTCHECK.md](FACTCHECK.md).
