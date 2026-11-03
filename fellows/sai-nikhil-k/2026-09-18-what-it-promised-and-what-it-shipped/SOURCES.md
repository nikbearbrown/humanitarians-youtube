# SOURCES — What It Promised, And What It Shipped

Every figure and quotation in this reel traces to one of two things: the DMG the
author supplied, or a command run locally against it. **Nothing was taken from
git history, from the author's prose, or from memory of an earlier week.**

## What the author supplied

| File | What it is |
|---|---|
| `data/Gavia_0.1.0_aarch64-1.dmg` | The packaged application, 84 MB. Mounted read-only; not modified. |
| `data/WhatsApp Image 2026-09-17 at 13.43.38.jpeg` | Capture of the "Check an image" result screen — 1 loon detected, 82%. → `images/B02-source-detect.jpg` |
| `data/WhatsApp Image 2026-09-17 at 13.40.35.jpeg` | Capture of "Previous checks" — two entries, 89% and 82%, Sept 15 2026. → `images/B02-source-history.jpg` |
| `data/WhatsApp Image 2026-09-17 at 13.40.57.jpeg` | Capture of "About" — "Built to support loon research." → `images/B02-source-about.jpg` |

## Figure-by-figure map

### From the model card shipped inside the app
Path inside the bundle:
`Gavia.app/Contents/Resources/gavia-backend/_internal/models/loon_v1.json`

| On screen | Value | Card field |
|---|---|---|
| B00, B03, B06 | precision 0.930 | `metrics.precision` = 0.92957 |
| B00, B03, B05, B06 | recall 0.800 | `metrics.recall` = 0.80012 |
| B03, B06 | mAP50 0.894 | `metrics.mAP50` = 0.89423 |
| B03, B06 | mAP50-95 0.614 | `metrics["mAP50-95"]` = 0.61357 |
| B03 note | YOLO11s, 100 epochs, 640 px | `architecture`, `provenance.epochs`, `provenance.image_size` |
| B05 | confidence threshold 0.25 | `defaults.confidence_threshold` |
| B00, B01 | `loon_v1.onnx`, 36 MB | `file`, `size_bytes` = 37,927,878 |

The card's own note on those metrics: *"Ultralytics validation split, recorded in
the best.pt checkpoint."* Provenance: dataset `loonnet_v1`, run
`runs/loonnet_v1_yolo11s`, weights `weights/best.pt`
(sha256 `7f4a1453…ae3c35`), trained 2026-09-02, exported 2026-09-09 with
ultralytics 8.4.138 from pytorch 2.14.0, onnx opset 17, simplified, static.
Model sha256 `172fa54f…2e2029`.

### From `Gavia.app/Contents/Info.plist`

| On screen | Value | Key |
|---|---|---|
| B00, B01, B02, B06 | Gavia 0.1.0 | `CFBundleShortVersionString` |
| B00 | `ai.humanitarians.gavia` | `CFBundleIdentifier` |
| B01 | macOS 10.15+ | `LSMinimumSystemVersion` |

### Measured locally

| On screen | Value | Command |
|---|---|---|
| B01 | 84 MB download | `ls -lh` on the dmg |
| B01 | 176 MB installed | `du -sh Gavia.app` |
| B00, B01 | arm64 | `lipo -info Gavia.app/Contents/MacOS/gavia` |
| B01 | Rust shell · Python 3.11 service · onnxruntime · SQLite | bundle tree: `MacOS/gavia`, `gavia-backend/_internal/libpython3.11.dylib`, `_internal/onnxruntime/`, `libsqlite3.0.dylib` |

### Observed by running the shipped backend
`gavia-backend --host 127.0.0.1 --port 8777 --data-dir ./gavia_data`, then five
`POST /api/detect` calls. Recorded output, not a screen recording:

- startup log: `"model warmed up", "model": "loon_v1", "seconds": 0.128`
- startup log: `"provider": "CPUExecutionProvider", "tiling": false`
- `processingTime` across five calls: 0.231 (cold), 0.143, 0.132, 0.126, 0.124 s
  → **B06's "about an eighth of a second" refers to the four warm calls.**
- local store: `gavia_data/gavia.db`, SQLite, tables `results` and `detections`
- `gavia-backend --help`, quoted on B06: *"Interface to bind. Loopback by
  default; this is not a network service."*

### Read off the author's captures (per-image confidences, NOT metrics)

| On screen | Value |
|---|---|
| B02 plate + narration | "1 loon detected", 82% on the box, "Highlighted areas show where a loon was found." |
| B02 landscape plate thumbnail | history list: 89% and 82% highest confidence, both Sept 15 2026 |
| B02 landscape plate thumbnail | "PROTOTYPE FOR CONSERVATION RESEARCH", "GAVIA — A PRODUCT OF HUMANITARIANS AI" |
| B06 | the About page's own caution that AI results contain errors and should be reviewed |

### Derived, and labelled as derived on screen

| On screen | Value | Derivation |
|---|---|---|
| B04 | F₁ = 0.860 | 2PR/(P+R) with P=0.92957, R=0.80012 → 0.860001. Checked in `FACTCHECK.md`. The card does **not** print this. |
| B05, B06 | "one loon in five" | 1/(1−0.80012) = 5.00 |

## Honesty log — what was avoided, and what is still open

1. **No invented numbers.** Everything quantitative above has a source column.
   Nothing was rounded in a direction that flatters the model: 0.92957 → 0.930,
   0.80012 → 0.800, 0.89423 → 0.894, 0.61357 → 0.614.

2. **The conflation that was available and refused.** The captures show 82% and
   89%; the card shows mAP50 = 0.894. These are unrelated quantities that happen
   to look alike. B02 is the only beat that speaks about 82%, and it calls it the
   score on one box in one photograph. Its portrait plate says so in type.

3. **Zero-detection result NOT used.** A crop of the loon taken out of the
   author's own screen capture was submitted to the shipped backend and returned
   `"detections": []` at 0.149 s. This is an artifact of re-compressing an
   already-displayed, already-downscaled image — **not** a miss by the model. The
   original photograph was not supplied, so the test could not be run properly.
   It appears nowhere in the reel and should not be reinstated without the
   original file.

4. **OPEN ITEM FOR THE AUTHOR — licence.** The shipped model card carries:
   `"license": {"spdx": "AGPL-3.0-only", "reason": "Derived from Ultralytics
   YOLO11, which is AGPL-3.0 licensed.", "url": "https://ultralytics.com/license"}`.
   On the author's explicit instruction this session, it is **kept out of the reel
   entirely** — no beat, no on-screen text, no narration, not in `DESCRIPTION.md`.
   It is logged here because AGPL-3.0 copyleft on an application distributed by a
   nonprofit is a decision worth settling before a v1 release, and because the
   fact is inside the artifact that ships. **Not a reel item. An author item.**

5. **Unverified by us — stated as the app's own words, not as fact.** The About
   page's claims about supporting researchers and conservation teams, and the
   "prototype for conservation research" footer, are quoted as what the
   application says about itself. The reel does not independently assert an
   accuracy level in the field.

6. **Class change not narrated.** 09-11-1 reported two classes ("common loon" and
   "non loon"); this card is single-class (`"classes": ["common loon"]`, display
   label "Loon"). The change is real and visible in the card, but the author did
   not explain it, so the reel does not claim a reason for it. Raised here in case
   it belongs in a later week.

## External links

| Link | Used for |
|---|---|
| https://humanitarians.ai | Channel/org attribution in `DESCRIPTION.md` |
| https://ultralytics.com/license | Not on screen. Recorded here for open item 4 only. |

No other external source was consulted. No web search, no paper, no dataset
outside the supplied DMG informed any on-screen claim.
