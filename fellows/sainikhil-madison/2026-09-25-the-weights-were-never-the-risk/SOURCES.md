# SOURCES — The Weights Were Never the Risk

Reel: `weekly_updates/2026-09-25-the-weights-were-never-the-risk/` · slug `claude-sai-the-weights-were-never-the-risk`
Week of 2026-09-25. Subject: **Gavia v0.2.0** — the Python backend rewritten in
Rust, three operating systems, CI-built installers.

## Raw-material provenance

The author (Sai) supplied the repository as this week's update ("This is my
update for the week") in place of dictated bullets, the same arrangement as
`09-11-2` and `09-18-2`. The repository's own prose — `README.md`,
`CHANGELOG.md` §0.2.0, `ROADMAP.md` and the commit messages — is the raw
material. Every narrative claim traces to one of those documents, to a line of
source read by hand, or to a computation recorded in `evidence/`.

Where the prose and a measurement disagreed, the **measurement** is on screen
and the disagreement is logged below.

## External sources

| Source | Used for |
|---|---|
| `https://github.com/nikhil-kunapareddy/gavia` | The subject. Cloned at `78b383e` (merge of PR #11, release/v0.2.0). |
| `CHANGELOG.md` §0.2.0 | B00, B01, B07: backend rewritten in Rust; no sidecar/server/port/token; Settings, Help, icon; Take-a-photo, FastAPI, PyInstaller and Playwright removed. |
| `ROADMAP.md` | B06: the six required features and their status; "survey counting" as the next item. |
| Commit `9cace7b` message | B02, B04: python_reference.json frozen before removal; the parity figures; "brings in origin/swara's loon count". |
| `desktop/src-tauri/src/detection/loader.rs` | B03: `draft_factor` read directly; the comment that jpeg-decoder's own `scale()` "feeds the model different pixels". |
| `desktop/src-tauri/src/detection/preprocess.rs` | B02 resolver, B07: Pillow-compatible bilinear resampling, round-half-to-even. |
| `desktop/src-tauri/tests/parity.rs`, `examples/evaluate.rs` | B04: run locally. |
| `backend/scripts/evaluate.py` @ `663feeb` | B04: the deleted Python evaluator, run locally. |
| `desktop/src-tauri/resources/models/loon_v1.json` | B05: the model card's Ultralytics recall, 0.80012. |
| GitHub Releases API, `v0.2.0` | B00, B01, B07: DMG size 47,183,690 bytes. |
| GitHub Actions runs `35841358212`, `35841549615` | B01, B07: rust + installer jobs green on macOS, Windows, Linux. |
| `weekly_updates/09-18-1/data/Gavia_0.1.0_aarch64-1.dmg` | B01: the 0.1.0 DMG, 87,879,427 bytes (supplied by Sai last week). |
| Local dataset `~/Documents/loonet/data/annotated/loonnet_v1/val.txt` | B03, B04, B05: the 26 validation photos, 33 labelled loons. Not published. |

## Week scope

Commits after last week's reel (09-18) through the release:

| Commit | Author | Subject |
|---|---|---|
| `f7a9928` | **Swara Joshi** | Adding changes for windows and adding features |
| `663feeb` | **Swara Joshi** | Adding count feature for loons |
| `9cace7b` | Sai | Move the detection core to Rust and run on macOS, Windows and Linux |
| `1f1a1e6` | Sai | Build, test and release installers in CI on all three systems |
| `6637cc3` | Sai | Document Gavia as a cross-platform open-source project |
| `49d30ac` | Sai | Format index.css with Prettier |
| `448b77c` | Sai | Add a Settings page with theme, storage location and model choice |
| `ba612aa` | Sai | Keep macOS history in ~/Library/Gavia and name the model Loonet 1.0 |
| `1a3551b` | Sai | Trim the home, history and settings screens and add a Help page |
| `7887bc3` | Sai | Set out Gavia's six required features in the README and roadmap |
| `f9d4964` | Sai | Give Gavia a loon icon and artwork for its installers and README |
| `c91d3d4` | Sai | Drop the icon from the README header; the banner is enough |
| `a2b07ac` | Sai | Use as_chunks for fixed-size pixel chunks |
| `46363ca` | Sai | Release 0.2.0 |

`v0.2.0` was published 2026-09-23 as a GitHub **pre-release**.

## Honesty log

- **"84 MB to 43 MB" is not repeated.** README, CHANGELOG and ROADMAP all say
  43 MB. The released `Gavia_0.2.0_aarch64.dmg` is 47,183,690 bytes — 45.0 MiB
  by the same `ls -lh` convention that gave last week's 84 (87,879,427 bytes =
  83.8 MiB). The reel says **84 → 45**. Flagged to Sai to fix in the repo.
- **Recall 0.879 is not presented as an improvement.** The weights are
  byte-identical to last week's (`model_sha256.out`). Last week's 0.800 is the
  Ultralytics validator's figure recorded in `best.pt` and still printed on the
  shipped model card; 0.879 is the app's own pipeline at the shipped 0.25
  threshold. B05 is built to say exactly that.
- **B04's "one extra faint guess" is stated as a fact, not a cause.** Rust
  produces 90 predictions above 0.001 against Python's 89, and AP scores every
  one. Whether that extra row or the ≤0.0151 confidence shifts account for the
  −0.0011 was not isolated, so the narration does not say which.
- **B02's warn branch is a constructed contrast**, not a recorded failure: it
  names what *could* drift. Its support is B03's measurement (15 of 26 photos
  would decode differently) and the source comment that the naive decoder moved
  confidences "by tenths rather than hundredths".
- **No adoption, speed or cost-to-run figures.** One recorded DMG download, zero
  stars; neither appears. No inference timing was measured.
- **Tiling is not in the reel.** The README's tiled-precision figure (0.074)
  reproduced (Rust 0.0736, `evaluate_rust.out`) but is not this week's work.

## Attribution

Gavia is Sai's project. **Swara Joshi** authored two of this week's commits —
the Windows run changes and the per-photo loon count — and the count survived
the Rust port (commit `9cace7b`: "Brings in origin/swara's loon count"). She is
credited by name in B06's narration and B07's last line. No other person is
named.
