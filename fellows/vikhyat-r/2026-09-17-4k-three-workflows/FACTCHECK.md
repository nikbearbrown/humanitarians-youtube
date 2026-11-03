# FACTCHECK.md — hai-4k-three-workflows

Every claim that reaches the screen or the narration. Paths are relative to the
`brutalist.art` toolkit root; verified 2026-09-17 against the working copy at
`Documents/Claude/brutalist.art-main`.

This reel describes **proposed** workflows, so most of its content is design
reasoning rather than repo fact. The table marks which is which, because a
design claim and a verified claim should not be presented in the same voice.

No claim in this reel names a person, a decision, or who made it.

| Beat | Claim | Verdict | Source |
|---|---|---|---|
| B00 | The five packages sit at different points in the chain | AUTHOR'S FRAMING | Established in the companion reel; not a repo claim |
| B01 | A prevents, B describes, C organises | AUTHOR'S FRAMING | The organising idea of the proposal |
| B02 | The toolkit can refuse to write a file | SUPPORTED | `runtime/scripts/compile.py:686-692` — THE MASTER LAW raises `BuildError` and writes nothing when a clean master would carry a slate. `compile.py:622-623` rejects `--allow-slates` for a final. The proposed resolution check is the same mechanism applied to size |
| B02 | Two approved sizes: 3840×2160 and 2160×3840 | SUPPORTED | `RENDER-TARGETS.md:45`; `docs/PIPELINE-SAFETY.md:158`; `docs/FELLOWS-SUBMISSION.md:22`; `skills/make/fellows/SKILL.md:243` |
| B02 | A failed write leaves nothing behind | SUPPORTED | `compile.py:801-822` encodes to a temp candidate and only `os.replace`s after verification; a failure leaves the previous file untouched |
| B03 | Drive stores width, height and duration for video files | SUPPORTED (external) | Google Drive API `files.videoMediaMetadata`. Not a repo claim. Populated after Drive finishes processing, so the reel does not claim it is present for every file |
| B03 | The filename is the only place a fellow's name is carried on a video file | SUPPORTED | No author field in `runtime/schema/beat_sheet.schema.json:12-20`; `runtime/scripts/provenance.py:37-51` classifies machine-vs-human, not which human; the `.verified.json` receipt (`compile.py:824-829`) records a SHA-256 and timestamps, no identity |
| B03 | A filename convention exists | SUPPORTED | `docs/FELLOWS-SUBMISSION.md:80-93` — `ProjectName_VolunteerName.mp4` |
| B03 | Frame sampling is cheap to implement — the machinery exists | SUPPORTED | `runtime/qc/final_frame_check.py:142` `sample_frames()`, `:182` `sample_beats()`, `:92` `analyze_frame()` |
| B03 | A correct-size file can still be a stretched one | SUPPORTED | `compile.py:189-193` `vf_fit()` scales unconditionally; the under-size warning at `:278-280` fires only for stills, never for the `VIDEO`/`MANIM` branch at `:247-274`. Also `docs/PIPELINE-SAFETY.md:127` |
| B04 | C runs B's steps first and settles verdicts before moving anything | AUTHOR'S DESIGN | Design property of the proposal |
| B04 | A move log makes an error traceable | AUTHOR'S DESIGN | Design property; stated as reasoning |
| B05 | B changes nothing | AUTHOR'S DESIGN | Read-only by construction |
| B05 | C adds no information over B | AUTHOR'S REASONING | Follows from the two running identical checks |
| B06 | A is upstream of B; C follows once B is trusted | AUTHOR'S REASONING | The ordering argument of the proposal |
| B07 | The definitive 4K check happens on YouTube after processing | SUPPORTED | `docs/FELLOWS-SUBMISSION.md:147-148` — "Native 4K source/export is checked; after upload, verify the actual YouTube 4K playback option once processing completes. Local export alone cannot prove it." Reinforced by `docs/PIPELINE-SAFETY.md:127` |
| B07 | None of these workflows removes that check | AUTHOR'S POSITION | Stated deliberately, so the proposal is not read as replacing the reviewer's judgement |

## Numbers that appear on screen

Only these:

- `3840 × 2160`, `2160 × 3840` — the two approved sizes
- `1080 × 1920` — used once, as the example of a corrected value in a failure note

No submission counts, no time-saved figures, no percentages. None of those have
been measured, so none are shown.

## Deliberately not claimed

- No figure for how many submissions arrive at the wrong resolution, or how
  many upload cycles the proposal would save.
- No claim that any workflow is best, essential, or the only real fix. Each
  keeps its limit on screen, delivered at the same weight as the rest.
- No claim that the toolkit is broken or that documentation is wrong. The
  framing throughout is that guidance has not kept pace with a codebase that
  grew quickly.
