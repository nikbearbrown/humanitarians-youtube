# FACTCHECK.md — hai-4k-five-packages

Every claim that reaches the screen or the narration, with the file and line it
came from. Paths are relative to the `brutalist.art` toolkit root. Verified
2026-09-17 against the working copy at
`Documents/Claude/brutalist.art-main`.

No claim in this reel names a person, a decision, or who made it.

| Beat | Claim | Verdict | Source |
|---|---|---|---|
| B00 | Resolution is currently established after upload rather than from the file | SUPPORTED (process, supplied by the requester) | Not a repo claim — stated as current practice, not as a repo fact |
| B00 | The resolution is readable from the file itself | SUPPORTED | `ffprobe -show_entries stream=width,height` — the same call `compile.py:58-66` `probe_wh()` already makes |
| B01 | The 4K capability exists and works | SUPPORTED | `art:93` appends `--height 2160`; `compile.py:647-651` derives `w` from `h`; landscape master lands at 3840×2160 |
| B01 | Four different resolutions are in circulation | SUPPORTED | 2160 — `art:93`; 1080 — `skills/make/hai/SKILL.md:193` and `skills/make/nbb/SKILL.md:197`; 720 — `runtime/scripts/compile.py:592` (`default=720`); 1920 — `runtime/scripts/shorts.py:482` |
| B01 | A fellow can follow an instruction exactly and get a half-size file | SUPPORTED | `skills/make/hai/SKILL.md:193` prints `compile.py [hai-dir] --height 1080` with no `--review`, i.e. a clean master at 1920×1080. `hai` is FELLOW TIER per `skills/TIERS.md:13` |
| B02 | Prevent / catch / detect positions | AUTHOR'S FRAMING | Not a repo claim — the organising idea of the proposal |
| B03 | Landscape 3840×2160, vertical 2160×3840 are the stated targets | SUPPORTED | `RENDER-TARGETS.md:45`; `docs/PIPELINE-SAFETY.md:158`; `docs/FELLOWS-SUBMISSION.md:22`; `skills/make/fellows/SKILL.md:243` |
| B03 | A filename pattern exists | SUPPORTED | `docs/FELLOWS-SUBMISSION.md:80-93` — `ProjectName_VolunteerName.mp4`, no spaces, dates, `v2` or `final`; both aspects share a basename in sibling `landscape/` and `vertical/` folders |
| B04 | The toolkit already declines to save a video carrying placeholder cards | SUPPORTED | `runtime/scripts/compile.py:686-692` — THE MASTER LAW raises `BuildError` listing the slated beats. `compile.py:622-623` additionally rejects `--allow-slates` for a final |
| B04 | Nothing currently checks the written file's resolution | SUPPORTED | `runtime/scripts/compile.py:433-443` `verify_output()` asserts streams, duration, full decode and audibility. No width or height assertion exists anywhere in the file |
| B05 | The filename is the only place a fellow's name is carried on a video file | SUPPORTED | No author field in `runtime/schema/beat_sheet.schema.json:12-20`; `runtime/scripts/provenance.py:37-51` classifies machine-vs-human, not which human; the `.verified.json` receipt (`compile.py:824-829`) records a SHA-256 and timestamps, no identity |
| B06 | Forty-eight built-in scene templates are defined at 1280×720 | SUPPORTED | Parsed from `runtime/remotion/src/Root.tsx`: of 610 registered compositions, 485 are 1920×1080, 65 are 1080×1920, **48 are 1280×720**, 9 are 3840×2160, 2 are 2160×3840, 1 is 1080×1080 |
| B06 | Those are scaled up without warning | SUPPORTED | `remotion_scenes.py:92` renders `--scale=2` → 2560×1440; `compile.py:189-193` `vf_fit()` applies `scale={w}:{h}:force_original_aspect_ratio=increase,crop` unconditionally. The under-size warning at `compile.py:278-280` fires only for `status == "STILL"`; the `VIDEO`/`MANIM` branch (`:247-274`) never probes dimensions |
| B06 | A sharpness check is already described in the toolkit's own documentation | SUPPORTED | `skills/make/ai-explainer/SKILL.md:780` — "GATE SHARPNESS (run.sh, after GATE T) enforces this via Laplacian-variance audit." No such code exists: `grep -ri laplacian` over the tree returns zero hits |
| B06 | Frame-sampling machinery already exists | SUPPORTED | `runtime/qc/final_frame_check.py:142` `sample_frames()`, `:182` `sample_beats()`, `:92` `analyze_frame()`, `:199` `contact_sheet()` |
| B06 | A 4K-sized file can still be soft | SUPPORTED | `docs/PIPELINE-SAFETY.md:127` — "4K output dimensions do not certify native source quality or YouTube processing." Also `docs/FELLOWS-SUBMISSION.md:24-25` |
| B07 | Sorting adds no information over the report | AUTHOR'S REASONING | Follows from the two using identical checks; stated as reasoning, not as a repo fact |
| B08 | Packages 1, 3 and 4 read the same folder and can be one build | AUTHOR'S REASONING | Design claim about proposed work, not a claim about the repo |

## Numbers that appear on screen

Only these, and each carries its source in the frame or in the narration:

- `3840×2160`, `2160×3840` — the two stated targets
- `2160`, `1080`, `720`, `1920` — the four heights in circulation
- `1280×720` and `48` — the sub-1080p composition count
- `2560×1440` — what `--scale=2` produces from a 1280×720 composition

## Deliberately not claimed

- No count of how many submissions arrive at the wrong resolution. That figure
  has not been measured and is not asserted anywhere in the reel.
- No claim that any workflow removes the post-upload YouTube check. The
  organisation's own guidance (`docs/FELLOWS-SUBMISSION.md:147-148`) keeps it,
  and reel 2 states that explicitly.
- No claim that the toolkit is broken, that documentation is wrong, or that any
  person made an error. The framing throughout is that guidance has not kept
  pace with a fast-growing codebase.
