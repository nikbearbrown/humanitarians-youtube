# Final review-cut QC — 2026-09-25

**Agent QC complete; ready for the mandatory human watch-the-cut gate. Human approval remains pending.**

## Deliverables

- 16:9: `/Users/deepashenoy/Downloads/brutalist.art-main/fellows/deepa-s/2026-09-25-how-ai-hallucinations-happen/HowAIHallucinationsHappen_DeepaShenoy-slate.mp4` — 3840×2160, 24 fps, 87.958 seconds. SHA-256 `2fcf4f05be1cfd2a86d906665f8130541f1e5b352dd733fd3a436c5f4bd63a01`.
- 9:16: `/Users/deepashenoy/Downloads/brutalist.art-main/fellows/deepa-s/2026-09-25-how-ai-hallucinations-happen/vertical/HowAIHallucinationsHappen_DeepaShenoy-slate.mp4` — 2160×3840, 24 fps, 87.958 seconds. SHA-256 `786bdbc81956bfe528c974622cc98e52db0da0035743bee9f0f4423b2099d5e6`.

## Completed work and preservation

- Resumed the existing project; all 20 scene renders and both review cuts already existed. Status documentation lagged actual disk state.
- Landscape cut and all ten landscape scene files remain byte-for-byte unchanged.
- Corrected and rerendered only portrait B05, B04, B06 and B08. B05 keeps the saved “IF BELIEVED → it could affect a decision” copy and gains clear card separation. B04/B06 output no longer intersects the decorative rule; B08's final instruction is fully visible.
- Only the portrait review cut was reassembled. All six other portrait scenes remain byte-for-byte unchanged.
- Narration text, all MP3s, the approved review WAV and approval records are unchanged. The approved WAV's recorded SHA-256 matches. Both final cuts decode to identical audio (hash in `_qc/final-verification.json`). No narration was generated.
- Pre-resume versions of replaced assets are preserved under `_qc/resume-originals/`. Nothing was moved/deleted, uploaded, published or copied into submission folders.

## Visual / frame / typography

- Inspected early, late and end samples for every beat in both aspect ratios, the automated mid/late samples, and fresh late/end frames of every corrected portrait scene in the final compiled MP4.
- Text and cards are readable with no remaining observed clipping or text/card collisions. Bellora and Lumen remain explicitly fictional; source lines, Deepa attribution, Liam disclosure and HAI close remain intact. Font sizes were not reduced by the corrections.
- Portrait B05 has a visible gap between the answer card and the risk callout. All corrected content fits the existing native portrait composition; no landscape cropping was introduced.
- Agent inspection is sampled visual QC, not human approval of the complete real-time playback. Human watch-the-cut review remains mandatory.

## Automated flags — inspected and adjudicated

The raw frame checker does **not** return an unconditional pass. Its reports are retained unchanged in `_qc/REPORT.md` and `vertical/_qc/REPORT.md`.

- Landscape: six bottom-safe-margin flags across B03/B05/B07, plus two B09 underfill flags. Footers are fully inside the canvas with approximately 3.7% bottom clearance; the centered title-restating end card intentionally uses negative space. No clipped glyphs or overlap observed. These are documented layout exceptions, not additional rebuild requirements.
- Final portrait: two B00 right-safe-margin flags. The attribution is fully visible with approximately 3% right clearance (418px last ink in a 432px-wide review sample). No clipping or collisions observed. Retained to preserve existing work. B06/B08 flags cleared after fixes.
- The summary verdict is agent visual acceptance with these explicit exceptions, not a claim that the raw automated gate passed.

## Audio / technical

- Both complete MP4s decode with ffmpeg `-xerror` and no errors.
- Both: native 4K scene inputs and output, H.264, yuv420p, 24 fps; AAC stereo at 48 kHz; ten filled beats, no placeholder slates.
- Runtime: 87.958 seconds; resolved beat timeline: 87.958333 seconds. Difference is under 1 ms. Video stream: 87.916667 seconds; audio stream: 87.958 seconds, a one-frame tail difference. No timeline shifts introduced.
- Loudness: −24.06 LUFS; true peak −4.68 dBTP. All ten narration windows are non-silent; no clipping. Final rebuilt audio has the same decoded SHA-256 as the measured cut.
- Both master-spec checks pass. Their optional clock-check import was unavailable; timeline/runtime and A/V tail alignment were independently verified above.
- Final output and every recorded media/audio input match build-state hashes.

## Gate

STOPPED: Deepa must watch both complete cuts and approve or request changes. No human visual approval has been inferred or recorded. Submission-copy and publication work have not begun.
