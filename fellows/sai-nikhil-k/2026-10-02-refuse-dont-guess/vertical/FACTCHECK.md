# FACTCHECK — Refuse, Don't Guess

Figure by figure: claim → where on screen → how it was verified → result.
Everything was re-measured on 2026-10-02 for this video; nothing is quoted from
the repo's prose without a check. Files are in `evidence/` unless noted.

## Environment

| Thing | Value |
|---|---|
| Machine | Apple M2 Pro, macOS 26.6.2, arm64 |
| Gavia | repo `760e465` = tag `v0.3.1`; installed `/Applications/Gavia.app` reports 0.3.1 |
| Node / vitest | v26.8.1 / 2.1.9 |
| Rust | rustc / cargo 1.97.1 |
| Recording | ffmpeg (Anaconda build) avfoundation screen capture, 60 fps, window crop 3040×1710 |

## The project's own checks

| Check | Result | File |
|---|---|---|
| `npx vitest run` (desktop UI) | 22 files, **257 / 257** passed | `vitest.out` |
| `cargo test --release` (Rust core; unit, model, parity, settings, workflow) | **115 / 115** passed (85 + 9 + 1 + 10 + 10) | `cargo_test.out` |

## The batch rules (B02, B03, B04, B07)

Gavia's shipped `selectImages()` (`src/lib/batch.ts`, unmodified at `760e465`)
run under the repo's vitest config on this reel's real photos
(`batch_rules.test.ts` → `batch_rules.out`):

| Case | Checked | Message / note | On screen |
|---|---|---|---|
| 25 photos picked | 25 | — | B04 row 1 |
| 26 photos picked | **0** | "That's 26 images. You can check up to 25 at a time." | B04 row 2, B04 note, B02 |
| survey.zip (25 inside) | 25 | — | B01 (the app does the same) |
| survey.zip + photo-26.jpg | **0** | "That's 26 images…" | B04 row 3 |
| zip of 25 + notes.txt + `__MACOSX/` | 25 | "Left out 1 file Gavia can't check: notes.txt." (the `__MACOSX` entry is ignored silently as clutter) | B07 line 3 |
| zip of 30 (25 + 5 repeats) | **0** | "That's 30 images…" | B03 narration ("every image is counted, including the ones inside zips") |
| one photo at 20 MiB + 1 byte | 0 | "This image is too large. Please choose an image smaller than 20 MB." | — |
| 24 photos + that one | **24** | "Left out 1 file Gavia can't check: photo-big.jpg." | B04 row 4, B07 line 3 |

The resolver quote on B02 is verbatim from the `selectImages` doc comment:
"A selection over `MAX_BATCH_IMAGES` is refused outright rather than cut short,
because which images got left out would be a guess."

## The rule (B03) — algebra

Read from `batch.ts`: `MAX_BATCH_IMAGES = 25`, `MAX_IMAGE_BYTES = 20 * 1024 * 1024`,
`MAX_ZIP_BYTES = MAX_BATCH_IMAGES * MAX_IMAGE_BYTES`. `found` is incremented for
every acceptable image, loose or inside a zip (the zip filter counts entries even
past `room`, extracting only the first `room`), and `found > MAX_BATCH_IMAGES`
returns `{ok: false}` with no images.

| Row | Expression | Check (`build_beats.py --check`) |
|---|---|---|
| 1 | n = n_photos + n_z1 + n_z2 + ⋯ | the zip-of-30 and zip+1 runs are refused as 30 and 26 |
| 2 | checked(n) = n · [n ≤ 25] | `checked()` reproduces every recorded case: 25→25, 26→0, 26 (zip+1)→0, 30→0, 24→24 |
| 3 | Z_max = 25 × 20 MiB = 500 MiB | 25 × 20 × 2²⁰ = 500 × 2²⁰ = **524,288,000** B (asserted) |

The note's "20 × 2²⁰ bytes" is the code's `20 * 1024 * 1024` = 20,971,520 B.
A zip larger than `MAX_ZIP_BYTES` is skipped (`reason: 'size'`) *before* its
bytes are read — "turned away before it is opened" in the narration.

Reproducible case: `REEL=<reel> npx vitest run src/lib/batch_rules.test.ts` in a
clone at `760e465` (see BUILD-PROMPT.md).

### Rendered-frame review (MATH-TYPESETTING.md)

**16:9 (`media/B03.mp4`, 3840×2160)** — reviewed at each row's reveal (rows at
1.67 s, 5.34 s, 9.29 s) and at 15/50/85%:
- Row 1: subscripts "photos", z₁, z₂ legible; ⋯ renders; no tofu.
- Row 2: "checked" upright, n italic; Iverson brackets [ ] full height; ≤ correct.
- Row 3: Z with upright "max"; × and MiB render; nothing clipped; rows 1–2 span
  ~8–92% of the width, inside title-safe.
- First pass had row 1 written with Σ and limits; its glyphs rendered visibly
  smaller than rows 2–3. Rewritten as an explicit sum (same meaning), re-rendered.

**9:16** — see the vertical section below (filled after the portrait render).

## The app run (B01)

From the take (`ui_batch.out`, the app's own log + accessibility labels):

| Claim | Measured |
|---|---|
| one zip, 25 photos, 3 empty lakes | `batch_manifest.json`: photo-04/12/19 = lake-01/02/03; 22 loon photos |
| "all twenty-five took about three and a half seconds" | button press 15.633 s → "Loons in 23 of 25 images" 19.150 s in the 60 fps recording = **3.52 s**; app log: detection 3,074 ms in total, 123 ms mean, 89–196 ms |
| "loons in twenty-three of twenty-five" | the app's heading, verbatim |
| "the truth is twenty-two" | by construction (22 loon photos, 3 lakes); all 22 loon photos were flagged |
| "an empty lake, with a box on a pine branch at forty-one percent" | photo-19 = lake-03 (Little Gabro Lake, CC BY-SA 4.0); detail view: 1 box, top-right pine branch, "Highest confidence 41%" |
| shown in real time | `make_ui.py` plays every segment at 1×; the cuts are listed in its caption |

## The update check (B05, B07)

| Claim | Verified |
|---|---|
| asks GitHub for a small file naming the newest release | endpoint `…/releases/latest/download/latest.json` (`tauri.conf.json`); the file is **1,833 B** and names version + per-platform URL + signature |
| downloads in the background, checks its signature, offers a restart, never restarts by itself | `updateService.ts`: `check()` → `update.download()`; `install()` + `relaunch()` only on the banner's button; Tauri's updater verifies the minisign signature against the configured public key; `.sig` assets exist for all three platforms |
| "one, to GitHub, at launch, and none while the photos were checked" | `ui_network.out`: 407 lsof samples; 1 socket (140.82.114.4:443, inside GitHub's 140.82.112.0/20) at 17:56:40; 0 in the 14 samples while checking. Limit: sub-0.3 s sockets could be missed |
| the switch turns it off | Settings → Updates checkbox; `readAutoUpdate()` returns false when `gavia.autoUpdate` = `off` (`lib/updates.ts`); shown turned off in the take |
| 0.3.0's manifest uploaded by hand; 0.3.1's by CI, 53 minutes later | `release_and_ci.out`: v0.3.0 `update manifest: skipped`, `latest.json` uploader `nikhil-kunapareddy` 04:03:20Z; v0.3.1 `update manifest: success`, uploader `github-actions[bot]` 04:52:49Z; releases published 03:50:43Z and 04:43:55Z (53 min) |

## Against last week's plan (B00, B06)

| Claim | Verified |
|---|---|
| last week: "a whole folder, one total, one CSV" | 2026-09-25 reel B06 narration, verbatim |
| shipped: 25 per check, progress bar + Stop, a count of photos with loons | CHANGELOG 0.3.1; the take ("Checking N of 25", Stop button, "Loons in 23 of 25 images") |
| not yet: whole folder, a total of loons, a CSV | ROADMAP §2 "Still to do"; "Now: … CSV export next" |

## Claims deliberately softened or left out

- No download size on screen (README's 43 MB is wrong; the measured 46.1 MiB is
  in SOURCES.md only).
- No accuracy figure: the model is unchanged and the 25 photos are not a test set.
- Speed is only "this laptop, this run".
- "The only thing it sends" is attributed to the app; the reel adds the
  measurement and its sampling limit.
