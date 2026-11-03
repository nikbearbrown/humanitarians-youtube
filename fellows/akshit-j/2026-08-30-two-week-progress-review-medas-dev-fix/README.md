# Two-Week Progress Review: MEDAS Dev Fix — Akshit

**Project:** MEDAS 2.0 (Medical Emergency Diagnostic Advising System), pre-release · **Video type:** two-week progress review (weeks of 2026-08-17 and 2026-08-24)
**Skill:** ai-explainer · **Voice:** Kokoro `am_onyx` (AI narrator, chosen by Akshit) · **Duration:** 3:14 (13 beats)
**Destination:** `fellows/akshit-j/2026-08-30-two-week-progress-review-medas-dev-fix/`

## This period's contribution

- **Role:** automating deployment for the MEDAS backend. Today the backend is built into Docker images and deployed to Cloud Run by hand; my dev setup builds and deploys automatically when a git tag is created.
- **Cadence:** Monday 2 h all-teams meeting and Thursday 2 h Aggregation System team meeting, both weeks (4 meetings, 8 hours).
- **Week of Aug 17:** created `TayyarH/medas-aggregation-frontend` and pushed the initial code (Aug 19) so Darshil could build the frontend CI/CD; granted him GCP dev project permissions and collaborator access. His Dockerfile and Cloud Run deploy workflow landed Aug 20, and his CI and rollback workflows were merged Aug 30. Planned dev and stage environments with Jiang: I take the backend stage setup next, Darshil the frontend side.
- **Week of Aug 24:** the dev backend was crash-looping (Service Unavailable on every request), which blocked Jiang from testing the dev setup. I prioritized the fix: worked with Prof. Tayyar Haitham to create a separate dev MongoDB, seeded it with example test data (no real patient data) and updated the secret. Verified on Aug 27 (`POST /auth/login` → 200). Documented as incident 01 in the MEDAS-docs repo I created for incidents and setup instructions.
- **Next:** automated stage deploys for the backend. The automation is proven on dev only so far.

## Human and AI work

**My decisions, implementation and verification:** I did the work described above, supplied the evidence (Cloud Run log screenshot, GitHub commit screenshot, incident notes) and chose the title, voice and outro. I reviewed each draft and the rendered review cuts and confirmed every row of the fact-check.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheets and narration from my account, drafted the fact-check, shot list and prompts, cropped and laid out my screenshots, adapted the vertical beat sheet, and made the layout fixes the toolkit's render checks asked for.
- Kokoro TTS (`am_onyx`, local, free) generated all narration. The video says on screen and aloud that the voice is an AI narrator reading my script.
- brutalist.art (Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** set the two-week window and the title, and chose which evidence to show: the Cloud Run logs (cropped, request URLs removed) and the GitHub commits. Chat messages used as proof are not shown in the video.

**What remains unverified or failed:**
- Stage is not built yet; the automated deployment is proven on dev only.
- The screenshots in the video are cropped; request URLs in the Cloud Run logs are removed.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `6a8380ae169cca81e0633664a65c958f5c12ab4b` (2026-09-20), checked 2026-09-24.
- **Source commit used for this export:** _[this repo's commit after upload]_
- **Beat sheets:** `beat_sheet.json` (16:9 landscape) and `beat_sheet_short.json` (9:16 full-length vertical, all 13 beats). No custom scene code.
- **Not in this repo:** the two screenshots used in B04 and B07 (and their landscape/portrait layouts) and the build paperwork (fact-check, shot list, prompts) are kept locally by Akshit and available on request. B04 and B07 render as slates without them.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/akshit-j/2026-08-30-two-week-progress-review-medas-dev-fix
python3 runtime/scripts/generate_audio_kokoro.py $REEL
./art run   $REEL
./art final $REEL --height 2160 --out <landscape-folder>

./art vertical $REEL                              # creates $REEL/vertical/
cp $REEL/beat_sheet_short.json $REEL/vertical/beat_sheet.json
python3 runtime/scripts/remotion_scenes.py $REEL/vertical
./art final $REEL/vertical --height 3840 --out <vertical-folder>
```

Rendered media (`mp3/`, `media/`, `clips/`, MP4s, QC frames) are produced locally and are not checked into this repo.

**Approvals and checks:** fact-check confirmed by Akshit on 2026-09-23. 16:9 and 9:16 exports both passed the toolkit's final gates (GATE T type check, frame checks) with receipts `status: ready`.

## Watch and review

| Version | Drive link | Resolution | Duration | SHA-256 |
|---|---|---|---|---|
| 16:9 | [Drive folder](https://drive.google.com/drive/folders/19LldycGJHxildCDzBwDanU4fCvRu8R9G) | 3840×2160 | 3:14 | `9224a37f48169f1d07070dab2de8f65b97719ae045390b8bf064441512c47ff2` |
| 9:16 | [Drive folder](https://drive.google.com/drive/folders/10RfFXUvs2IXb4e3ga_F3d7YQINfxQnxr) | 2160×3840 | 3:14 | `8b5044eca1c3c2f48a6043772efbfd771a6b9965e904cd03556fa07598f0c759` |

Drive filename for both: `TwoWeekProgressReviewMedasDevFix_AkshitJ.mp4` (Drive folder `08-27-2026`)

- **PM review status:** pending
- **YouTube 4K processing check:** pending upload
- **Professors' publication decision:** pending
