# How AI Draws Anime Frames

**Creator:** Keya G. · **Project:** Humanitarians AI / Brutalist Videos
**Reporting period:** Week 1

The folder is named for Week 1, the week this work counts toward.

[Script](SCRIPT.md) · [Beat sheet](beat_sheet.json) · [Portrait beat sheet](vertical/beat_sheet.json) · [Manim scenes](scenes.py) · [Portrait scenes](vertical/scenes.py) · [Fact check](FACTCHECK.md) · [Shot list](SHOTLIST.md) · [Prompts](PROMPTS.md) · [Frictional log](FRICTIONAL.md)

## This week's contribution

- **Question:** what does AI actually do when it "draws" the frames between an animator's drawings, and should it replace the animator?
- **Prediction:** I thought the animation market was heading into a difficult stage, since AI is everywhere now.
- **What I built:** a 12-beat, 3:35 Brutalist explainer. It covers how anime is drawn (key frames, in-betweens, drawing on twos and threes), how frame interpolation guesses a middle frame with optical flow, the three ways anime breaks that guess (flat colors, big movement, hidden parts), what fans and critics say about 60 fps edits, and AnimeInterp, research built for anime.
- **Result:** as an anime fan, I believe most people would agree with me: AI can help animators reduce their workload and make a quality product, but it should be a helping hand, not a replacement. The timing, where the feeling lives, stays the animator's choice.
- **Next:** make the Week 1 progress video, then the Week 2 explainer.

## Human and AI work

**My decisions:**
- Topic from my own interest in anime; story order, hook, overview and verdict.
- Naruto examples (Rock Lee vs Gaara, Naruto vs Sasuke), named only as examples; no frames or characters from any real anime are shown.
- Narrator voice: Kokoro `af_bella`. I tested and chose the pronunciations of my name ("Kay-yeah") and "Sasuke" ("Saa-suh-kay").
- I reviewed every audio clip, the low-quality scenes, the review cuts and both masters, and approved each.
- After the fact check, I changed beats 5 and 7, and kept the wording of the hook and beat 4 knowingly (recorded in [FACTCHECK.md](FACTCHECK.md)).
- I chose to fix every failed quality gate rather than bypass any of them.

**AI tools and voices:**
- Claude (chat) guided my research and drafted an example script from my story plan, which I approved.
- Claude Code, in the Brutalist toolkit, wrote the beat sheets, Manim scenes, fact check, shot list and prompts, ran the builds and fixed gate failures, with my approval at each step.
- Narration is AI-generated (Kokoro `af_bella`) and reads my script. The video says so in its first beat.

**What I rejected or corrected:**
- "Sasuke" was mispronounced; fixed by ear with three test clips.
- "Most anime is drawn on twos" became "drawn on twos or threes", and "smears" became "blur", to match the sources.
- Crunchyroll was dropped as a source because it could not be read; the AnimeInterp link was switched to arXiv.
- A requested nudge to one label in the portrait B05 scene was tested, made things worse, and was reverted.

**What remains unverified or open:**
- Claims 2, 5 and 6 in [FACTCHECK.md](FACTCHECK.md) are not fully supported by a source that was read; I kept that wording knowingly.
- Gate exemptions in use, each with a written reason in the beat sheet: B05 and the portrait B06 text regions; B02 and the outro marked "sparse by design".
- Toolkit bugs found and fixed locally in my copy of Brutalist, not pushed: kept as a local patch for now. The small `@HumanitariansAI` label on the portrait typing card is still too small to read on a phone.

## Watch

| Format | File | Link |
|---|---|---|
| 16:9 landscape, 3840×2160, 3:35 | `AnimeFrames_KeyaG.mp4` | [Watch on Drive](https://drive.google.com/file/d/1SGGspGKrS5v_L5wrWxDmJ4mVcPUpkFv6/view?usp=drive_link) |
| 9:16 vertical, 2160×3840, 3:35 | `AnimeFrames_KeyaG.mp4` | [Watch on Drive](https://drive.google.com/file/d/1EeXdpRFPII1lqPfbw0TjKhE6XaejNxUI/view?usp=drive_link) |

## Reproduce

Brutalist version: `nikbearbrown/brutalist.art` commit `a99b5323`, plus four small local portrait fixes (kept as a local patch for now). The portrait outro needs Playwright's headless Chromium (`npx playwright install chromium-headless-shell`).

```bash
cd brutalist.art
python3 runtime/scripts/generate_audio_kokoro.py <this folder>
./art run   <this folder>
./art final <this folder>
./art run   <this folder>/vertical --height 3840
./art final <this folder>/vertical --height 3840
```

## Sources

- Li Siyao et al., "Deep Animation Video Interpolation in the Wild" (AnimeInterp), CVPR 2021 — https://arxiv.org/abs/2104.02495
- Yossi Kreinin, "The state of AI for hand-drawn animation inbetweening", 2024 — https://yosefk.com/blog/the-state-of-ai-for-hand-drawn-animation-inbetweening.html
- Wikipedia, "Inbetweening" — https://en.wikipedia.org/wiki/Inbetweening
- Huang et al., "RIFE: Real-Time Intermediate Flow Estimation for Video Frame Interpolation" — https://arxiv.org/abs/2011.06294
- Anime Corner, "Toei Animation Responds After Backlash to AI Plans", May 19 2025 — https://animecorner.me/toei-animation-ai-backlash-denies/
- Elijah Gonzalez, The A.V. Club, Nov 5 2025 — https://www.avclub.com/ai-brained-sickos-who-upscale-anime-to-60-fps-need-to-be-stopped
- "Stop AI interpolation", uhighmidway (student opinion) — https://uhighmidway.com/19415/opinion/stop-ai-interpolation-people-should-listen-to-animators-and-authentic-animation/
