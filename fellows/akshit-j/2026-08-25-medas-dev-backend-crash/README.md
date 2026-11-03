# Tracing a Crash-Looping Backend — Akshit

**Project:** MEDAS 2.0 (Medical Emergency Diagnostic Advising System), pre-release · **Video type:** learning video (project incident walkthrough)
**Skill:** ai-explainer · **Voice:** Kokoro `am_onyx` (AI narrator, chosen by Akshit) · **Duration:** 4:14 (16 beats)
**Destination:** `fellows/akshit-j/2026-08-25-medas-dev-backend-crash/`

## This week's contribution

- **Question:** Why did the MEDAS dev backend on Cloud Run return `Service Unavailable` on every request, including `/health`?
- **Prediction:** A missing secret or a broken route.
- **What I built/tried:** Confirmed `JWT_SECRET` and `MONGODB_URI` existed in Secret Manager (ruled out). Read the Cloud Run logs: gunicorn booted, the worker crashed seconds later, repeating on every request. The traceback ended in pymongo resolving the `mongodb+srv` DNS records. The `MONGODB_URI` secret pointed at an old personal MongoDB cluster that had been terminated, and because `init_database()` runs at module import time, the failed connection crashed every worker boot. Fixed it with a new, properly owned dev cluster under Prof. Tayyar's institutional Atlas account, seeded with example test data (no real patient data), and a new version of the `MONGODB_URI` secret. No redeploy was needed: the deploy reads `MONGODB_URI:latest`, so the next instance picked it up.
- **Observed result:** `/health` returned healthy JSON, and a wrong-password login returned `Invalid credentials`, proving a real database query. A Cloud Run request log on 2026-08-27 shows `POST /auth/login` → `200` in 0.054 s (revision `medas-aggregation-dev-00012-fqd`).

The dev URLs returning 503 since 2026-09-20 is a separate billing issue and is not part of this incident.

## Human and AI work

**My decisions, implementation and verification:** I diagnosed and fixed the incident (week of 2026-08-25) and supplied the incident notes, the 2026-08-27 Cloud Run log and the login screenshot. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; reviewed each draft and the rendered review cuts; and confirmed every row of `FACTCHECK.md`.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration from my notes, wrote the `FACTCHECK.md` / `SHOTLIST.md` / `PROMPTS.md` drafts, made the layout fixes the render checks asked for, composed the screenshot layouts (`media/B11.png`, `pantry/B11-916.png`) and adapted the vertical beat sheet.
- Kokoro TTS (`am_onyx`, local, free) generated all narration. The video says on screen and aloud that the voice is an AI narrator reading my script.
- brutalist.art (Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** changed the title (to "Tracing a Crash-Looping Backend"), changed the opening greeting from "Hej" to "Hi", kept `@HumanitariansAI` on the outro instead of the @NikBearBrown outro the toolkit's lint suggests, and corrected how the seeded data is described (example test data, not production data).

**What remains unverified or failed:**
- The terminal and log views in B04 and B06 are **reconstructions from my incident notes**, labeled as such on screen; the original crash-loop logs were not captured. B08 is a labeled illustration of the pattern, not MEDAS source.
- The log shown in B12 is real but **sanitized** (client IP, instance, trace/span IDs, project ID and URLs removed).
- The login screenshot is 1968×1416, enlarged for the 4K frames, so it is slightly soft at full resolution.
- Known toolkit issues hit while building (reported to PM): `./art smoke` fails on the `_smoke` slug check, and `./setup` stops at its ElevenLabs guard because of files under `youtube/brutalist/`.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `6a8380ae169cca81e0633664a65c958f5c12ab4b` (2026-09-20), checked 2026-09-23.
- **Source commit used for this export:** _[this repo's commit after upload]_
- **Beat sheets:** `beat_sheet.json` (16:9 landscape) and `beat_sheet_short.json` (9:16 full-length vertical, all 16 beats). No custom scene code.
- **Not in this repo:** the MEDAS login screenshot used in B11 (and its landscape/portrait layouts) and the build paperwork (fact-check, shot list, prompts) are kept locally by Akshit and available on request. B11 renders as a slate without the screenshot.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/akshit-j/2026-08-25-medas-dev-backend-crash
python3 runtime/scripts/generate_audio_kokoro.py $REEL
./art run   $REEL
./art final $REEL --height 2160 --out <landscape-folder>

./art vertical $REEL                              # creates $REEL/vertical/
cp $REEL/beat_sheet_short.json $REEL/vertical/beat_sheet.json
python3 runtime/scripts/remotion_scenes.py $REEL/vertical
./art final $REEL/vertical --height 3840 --out <vertical-folder>
```

Rendered media (`mp3/`, `media/`, `clips/`, MP4s, QC frames) are produced locally and are not checked into this repo.

**Approvals and checks:** fact-check confirmed by Akshit on 2026-09-23. Landscape and vertical exports both passed the toolkit's final gates (GATE T type check, frame checks) with receipts `status: ready`.

## Watch and review

| Version | Drive link | Resolution | Duration | SHA-256 |
|---|---|---|---|---|
| Landscape | [Drive folder](https://drive.google.com/drive/folders/19LldycGJHxildCDzBwDanU4fCvRu8R9G) | 3840×2160 | 4:14 | `13e8499b2b7b901fc98fd08ab4c7e7bf5545fda64da6ee4161edd68ebe3c5af0` |
| Vertical | [Drive folder](https://drive.google.com/drive/folders/10RfFXUvs2IXb4e3ga_F3d7YQINfxQnxr) | 2160×3840 | 4:14 | `1c7dc54a00d7a591d24513895eba4e6167cda5fef1e198e18198d58afe4ab37c` |

Drive filename for both: `MEDASBackendCrash_AkshitJ.mp4` (Drive folder `08-27-2026/landscape/` and `08-27-2026/vertical/`)

- **PM review status:** pending
- **YouTube 4K processing check:** pending upload
- **Professors' publication decision:** pending
