# The Migration That Lost Its Index Names — Akshit

**Project:** MEDAS 2.0 (Medical Emergency Diagnostic Advising System), in beta with a few clinical users · **Video type:** learning video (live-service incident walkthrough)
**Skill:** ai-explainer · **Voice:** Kokoro `am_onyx` (AI narrator, chosen by Akshit) · **Duration:** 3:45 (15 beats)
**Destination:** `fellows/akshit-j/2026-09-04-migration-lost-index-names/`

## This week's contribution

- **Problem:** After we migrated the live MEDAS database to a team-owned database, every document arrived intact, but the indexes lost their names. Weeks later, a fresh instance of the live service failed to boot: at startup the app asked MongoDB for an index named `idx_users_username_lc`, the same keys already existed under a default name (`username_lc_1`), and MongoDB refused with `IndexOptionsConflict` (code 85), crashing worker startup.
- **What I did:** The live data sat in a database under a former teammate's personal account, so I moved it to a team-owned database. Finding no clear guidance, I wrote a reusable script: copy every document, then recreate every index. Document counts matched, so the migration looked complete.
- **Root cause:** The script read each index from `index_information()`, where the index name is the dictionary key, but called `create_index(keys, **options)` without passing that name, so MongoDB gave every index a default name. Queries don't depend on index names, and indexes are only created at app startup, so the mismatch stayed hidden until a fresh boot. Redoing the migration with `mongodump`/`mongorestore` (which keeps index names) was not an option because the old database had been deactivated.
- **Fix:** Together with a teammate, I made index setup idempotent: one `safe_create_index` helper creates every index and treats codes 85, 86, 13 and 67 as no-ops instead of crashing, and every collection's indexes now go through it, so it is safe to run on every boot.
- **Lesson:** Migrate with `mongodump`/`mongorestore`, compare index names and keys between source and target, keep the source until they match, and log skipped index conflicts rather than hiding them. Mature systems use versioned migrations.

## Human and AI work

**My decisions, implementation and verification:** I did the migration and made the fix with a teammate. I supplied the account of the incident, the fix commit message and the incident notes. I chose the topic, the title, the narrator voice and the Humanitarians AI outro; reviewed each draft and the rendered review cuts; and confirmed every row of the fact-check on 2026-09-24.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheets and narration from my account, drafted the fact-check, shot list and prompts, adapted the vertical beat sheet, and made the layout fixes the toolkit's render checks asked for.
- Kokoro TTS (`am_onyx`, local, free) generated all narration. The video says on screen and aloud that the voice is an AI narrator reading my script.
- brutalist.art (Remotion) rendered the visuals. No paid services were used.

**What I rejected or corrected:** kept the video to one story about the live service, said "live" rather than "production", named no people, and credited the fix to me and a teammate ("we").

**What remains unverified or failed:**
- The on-screen code is illustration, not captured evidence: the migration script (B05) and the startup log (B08) are labeled reconstructions of the pattern and the error, not the original script or a captured log.
- The `log.warning` line in B10 is labeled as a recommended addition; it is not part of the applied fix.

## Reproduce

- **Brutalist version:** `nikbearbrown/brutalist.art` commit `6a8380ae169cca81e0633664a65c958f5c12ab4b` (2026-09-20), checked 2026-09-24.
- **Source commit used for this export:** _[this repo's commit after upload]_
- **Beat sheets:** `beat_sheet.json` (16:9 landscape) and `beat_sheet_short.json` (9:16 full-length vertical, all 15 beats). No custom scene code and no screenshots; every beat is a registered Remotion scene.
- **Not in this repo:** the build paperwork (fact-check, shot list, prompts) is kept locally by Akshit and available on request.

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install        # needs Python 3.10+, ffmpeg, Node >= 20

REEL=../humanitarians-youtube/fellows/akshit-j/2026-09-04-migration-lost-index-names
python3 runtime/scripts/generate_audio_kokoro.py $REEL
./art run   $REEL
./art final $REEL --height 2160 --out <16x9-folder>

./art vertical $REEL                              # creates $REEL/vertical/
cp $REEL/beat_sheet_short.json $REEL/vertical/beat_sheet.json
python3 runtime/scripts/remotion_scenes.py $REEL/vertical
./art final $REEL/vertical --height 3840 --out <9x16-folder>
```

Rendered media (`mp3/`, `media/`, `clips/`, MP4s, QC frames) are produced locally and are not checked into this repo.

**Approvals and checks:** fact-check confirmed by Akshit on 2026-09-24. 16:9 and 9:16 exports both passed the toolkit's final gates (GATE T type check, frame checks) with receipts `status: ready`.

## Watch and review

| Version | Drive link | Resolution | Duration | SHA-256 |
|---|---|---|---|---|
| 16:9 | [Drive folder](https://drive.google.com/drive/folders/1A9spSntzYPn6XCcMW-jlI2zhXulkgbNH) | 3840×2160 | 3:45 | `5f2e1a34c9edb1a201bb36a9db22d6ce8be15cfadf853f457e1a5d08933ecfb4` |
| 9:16 | [Drive folder](https://drive.google.com/drive/folders/1A9spSntzYPn6XCcMW-jlI2zhXulkgbNH) | 2160×3840 | 3:45 | `5ea12d21e406c99e1c58c528b501e4d916f859d0e63e87d0ce1f9b918f3dd2a6` |

Drive filenames (same folder): `MigrationLostIndexNames_AkshitJ_16x9.mp4` and `MigrationLostIndexNames_AkshitJ_9x16.mp4`

- **PM review status:** pending
- **YouTube 4K processing check:** pending upload
- **Professors' publication decision:** pending
