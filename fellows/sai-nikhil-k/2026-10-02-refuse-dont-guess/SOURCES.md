# SOURCES — Refuse, Don't Guess

Reel: `weekly_updates/2026-10-02-refuse-dont-guess/` · slug `claude-sai-refuse-dont-guess`
Week of 2026-10-02. Subject: **Gavia 0.3.0 and 0.3.1** (2026-09-29) — updates
from GitHub Releases, and checking up to 25 images or a zip at once.

## Raw-material provenance

Sai supplied the repository as this week's update ("This is my repo:
https://github.com/nikhil-kunapareddy/gavia.git"), the same arrangement as
`09-11-2`, `09-18-2` and last week's reel. He then chose, from three proposals:
the ONE idea and title ("Refuse, Don't Guess"), that Claude record the real app,
which screens (the batch flow; Settings → Updates) and which photos (freely
licensed Wikimedia Commons). He named nothing to leave out.

The repository's own prose — `README.md`, `CHANGELOG.md` §0.3.0–0.3.1,
`ROADMAP.md` and the commit messages in the week window — is the raw material.
Every claim traces to one of those, to source read by hand, or to a run recorded
in `evidence/`. Where prose and measurement disagreed, the **measurement** is on
screen and the disagreement is logged below.

## External sources

| Source | Used for |
|---|---|
| `https://github.com/nikhil-kunapareddy/gavia` | The subject. Cloned at `760e465` (merge of PR #17, tag `v0.3.1`). |
| `CHANGELOG.md` §0.3.1, §0.3.0 | B00, B01, B05, B07: 25 images or a zip; progress bar and Stop; files left out and named; updates, never a forced restart, Settings → Updates; Linux .deb/.rpm not self-updating. |
| `ROADMAP.md` "Required features" §2, "Now" | B06: survey counts, CSV export and correctable counts still to do. |
| `desktop/src/lib/batch.ts` @ `760e465` | B02 resolver (quoted), B03 (all three rows), B04 (run). |
| `desktop/src/pages/SettingsPage.tsx`, `services/updateService.ts`, `lib/updates.ts` | B05: the Updates wording; check → download → offer restart; switch kept in `localStorage`. |
| `desktop/src-tauri/tauri.conf.json` @ `v0.3.1` | B05: the updater endpoint (`releases/latest/download/latest.json`) and minisign public key. |
| Commit messages `aa638f6`, `9639c83`, `fe49c3a`, `86daa7b` | B07 line 4: the two release steps that broke on 0.3.0. |
| GitHub Releases API, `v0.2.0`/`v0.3.0`/`v0.3.1` | Asset sizes, manifest uploader and times (`evidence/release_and_ci.out`). |
| GitHub Actions runs `36518938985` (v0.3.0), `36522924272` (v0.3.1) | B07 line 4: update-manifest job skipped, then succeeded. |
| `gh api meta` | B05: 140.82.112.0/20 is GitHub's address range. |
| Last week's reel `2026-09-25-the-weights-were-never-the-risk` B06 | B00, B06: continuity — "a whole folder, one total, one CSV". |
| The installed app `/Applications/Gavia.app` 0.3.1 | B01, B05: screen recordings (`ui/takes/`), scratch `GAVIA_DATA_DIR`. |
| Wikimedia Commons — 26 files | B01 and B04 inputs. Titles, authors, licences, sha256 in `evidence/batch_manifest.json`; sidecars in `images/src/`. |

## Week scope

Commits after last week's reel (merge `78b383e`, 2026-09-23) through the release
(`760e465`), non-merge, on `main`:

| Commit | Date | Author | Message |
|---|---|---|---|
| `aa638f6` | 2026-09-28 19:55 -0700 | Sai Nikhil Kunapareddy | Check up to 25 images, or a zip of them, at once |
| `9639c83` | 2026-09-28 20:06 -0700 | Sai Nikhil Kunapareddy | Update from GitHub Releases, with a switch in Settings |
| `0f5535f` | 2026-09-28 20:13 -0700 | Sai Nikhil Kunapareddy | Keep the npm Tauri packages on the Rust crates' minor versions |
| `1663b4f` | 2026-09-28 20:32 -0700 | Sai Nikhil Kunapareddy | Release 0.3.0 |
| `fe49c3a` | 2026-09-28 21:09 -0700 | Sai Nikhil Kunapareddy | Fix the two release steps that broke on v0.3.0 |
| `86daa7b` | 2026-09-28 21:24 -0700 | Sai Nikhil Kunapareddy | Release 0.3.1 |

Also in the window, **not on `main`** and not narrated: Dependabot branches
(`fdef5d6`, `cfaa854`, `f3651a8` Tailwind 4, `68fa410`, …), several with failing
CI. Every narrated commit is Sai's; no collaborator work this week.

## Honesty log — where the prose and the measurement disagreed

| Prose says | Measured | What the reel does |
|---|---|---|
| README: "a 43 MB download" | `Gavia_0.3.1_aarch64.dmg` = 48,342,473 B = **46.1 MiB** (`release_and_ci.out`) | Shows no download size this week. Logged for Sai. (Last week's 45.0 MiB, for 0.2.0, was already a correction of the same line.) |
| App/README: "20 MB each" | `MAX_IMAGE_BYTES = 20 * 1024 * 1024` = 20,971,520 B = **20 MiB** | B03 typesets MiB and states the bytes; narration keeps the app's word "megabytes". |
| 0.3.1 commit: "the first release an installed copy should update to on its own" | 0.3.0's `update manifest` CI job was **skipped**; its `latest.json` was uploaded by hand (`nikhil-kunapareddy`, 04:03:20Z); 0.3.1's by `github-actions[bot]` (04:52:49Z) | B07 line 4 says so. The two are consistent: 0.3.0 had a manifest only because Sai uploaded it. |
| Settings: "That is the only thing Gavia sends over the internet" | One TCP socket, to 140.82.114.4:443 (GitHub), at launch; none in any of the other 406 samples, 14 of them taken while the 25 photos were checked (`ui_network.out`) | B05 states the measurement, with its limit (0.3 s sampling). |
| README: "finds 88% of labelled loons, and 91% of the boxes it draws are real loons" | Not re-measured this week (no model change since `172fa54f…`). On this video's 25 photos: all 22 loon photos flagged, plus 1 of 3 empty lakes (box on a pine branch, 41%) | B01 shows the false box; no accuracy figure is put on screen. |
| CHANGELOG 0.3.1: Stop button | Exists (seen in the take) but a 25-photo batch finishes in 3.5 s, too fast to demonstrate | Mentioned only on the B06 card; not demonstrated. |

## A bug found while recording (for Sai, not in the reel)

Opening the file picker, cancelling and opening it again quickly crashed the
installed 0.3.1: `unexpected NULL returned from +[NSOpenPanel openPanel]`, then
`fatal runtime error: failed to initiate panic, error 5, aborting`
(macOS crash report `~/Library/Logs/DiagnosticReports/gavia-2026-10-02-105126.ips`
on the recording Mac; not copied into this public folder). Reported to Sai separately.
