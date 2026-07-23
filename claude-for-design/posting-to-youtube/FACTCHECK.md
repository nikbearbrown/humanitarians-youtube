# FACTCHECK — posting-to-youtube

All terminal output is **real session output, lightly trimmed** from `youtube/PUBLISH-LOG.md`.

## Figures — all real from PUBLISH-LOG.md

| Figure | Claim | Source |
|--------|-------|--------|
| `xXKgCXc1nm4` | Video ID for "What is Brutalist?" | PUBLISH-LOG.md — uploaded 2026-07-13 |
| `7rUcwkFOhvM` | Video ID for "Installs, .env & Credentials" | PUBLISH-LOG.md |
| `AhdmP75PBY0` | Video ID for "When Cowork Can Help Claude Code" | PUBLISH-LOG.md |
| `PLG9H-C6rp5RU` | Playlist ID for "Brutalist" | PUBLISH-LOG.md — found existing |
| **1,600 units** | Cost of one `videos.insert` upload | YouTube Data API v3 quota table |
| **10,000/day** | Default daily quota | YouTube Data API project default |
| **~6/day** | 10,000 ÷ 1,600 ≈ 6.25 | derived from above |
| **3 uploaded, 1 bug found & fixed** | Three videos uploaded; one bug: `manualSortRequired` | PUBLISH-LOG.md |

## The bug — exactly as it happened

`HttpError 400 manualSortRequired` — the "Brutalist" playlist uses auto-sort, and the script
sent `"position": pos` in the `playlistItems.insert` body. Removed `position=` — clean on re-run.

## Privacy

All three landed `unlisted` (API confirmed via `videos.list`). Not PRIVATE — the compliance
audit warning in the SKILL.md only applies to `public`, not `unlisted`.

## Source doc

`docs/posting-to-youtube.md` — the written form this video is the spoken form of.
All narrative claims trace to that doc and to `youtube/PUBLISH-LOG.md`.
