# Week 24 work-video — final

*Read the Receipt Backwards.* Tanmay Kulkarni, in for Humanitarians AI.
Assembled 2026-09-28: the record of how both films were made and verified, with their captions and
YouTube descriptions.

Text and code only. **The two masters live in the shared Google Drive**, not in this repository.
See the links below. The working folder (audio, clips, QC frames and the reference builds) is
outside this repo.

## Where the work came from

The film is built on Tanmay Kulkarni's own Week 24 case study and its implementation:

- **Case study:** `14-mastercard-agentic-ai-payments.md`, on how Mastercard Agent Pay lets an AI agent
  pay on a cardholder's behalf, written only from what Mastercard has published.
- **Implementation:** `mastercard-agent-pay-pipeline-v2.zip`, a working reference pipeline of those
  checks: input validation, registration and verification, agent-consumer ownership, permissions and
  limits, the Authorization Gate, and the Verifiable Intent record. It has 82 tests across 9 files,
  all passing in a fresh environment.
- **What the film adds:** one way to read the build's output. Take the receipt it writes and ask of
  every line which step checked it before it was written. Two lines turn out to have been carried
  along in earlier versions. Both were caught (one by the second review round, one while making this
  video) and fixed with tests. That is how the build earns each line. The merchant line stays honestly
  marked, because Mastercard hasn't published how that check works.
- **Uniqueness:** the angle was checked against every earlier work video's narration (Weeks 15–23), so
  no thesis or beat repeats. The audit and the nearest prior beat are in `ANGLE.md`.

## The files

| | File | | |
|---|---|---|---|
| **Long** | `read-the-receipt-backwards-final.mp4` | 3840×2160 · 24 fps · 4:31 (271.1s) | −15.0 LUFS / −1.9 dBFS |
| **Short** | `read-the-receipt-backwards-short-final.mp4` | 2160×3840 · 24 fps · 1:28 (88.0s) | −15.0 LUFS / −1.9 dBFS |

Each film's master is on Drive (below); its captions (`.srt` and `.vtt`) and YouTube title, description and tags
(`*-youtube.md`) are in this folder.

**Structure:**
- **Long, "ONE RECEIPT":** the whole film is a single receipt, read from the bottom up. Each line is
  stamped only when the step that earns it has been shown running.
- **Short:** its own script, not a cut of the long. The same receipt carries across every cut, with
  a written join at each one. It has its own ending and points to the long for the rest.

## Links

Drive links added 2026-09-28. Add the YouTube URL once each film is live.

| | Drive | YouTube |
|---|---|---|
| Long (16:9, 4K) | [Drive](https://drive.google.com/file/d/1PsuSUheQf3agC9CeCh2Je1zOBIXAFpxY/view?usp=drive_link) | *(to add)* |
| Short (9:16, 4K) | [Drive](https://drive.google.com/file/d/1qRm0VWpggINXR8-w34hlhB_sBN53qF6u/view?usp=drive_link) | *(to add)* |
| Repository (the build) | [mycroft · mastercard-agent-pay-workflow](https://github.com/nikbearbrown/mycroft/tree/main/case-study-workflows/mastercard-agent-pay-workflow) | — |

**Links to update later:** both descriptions link the build in `nikbearbrown/mycroft` `main` (live since
PR [#53](https://github.com/nikbearbrown/mycroft/pull/53) merged, 2026-09-28). In
`read-the-receipt-backwards-short-youtube.md`, the full-video line currently points to the long's Drive link. Once the long is live, swap in its YouTube URL and set
  it as the Short's related video in YouTube Studio.

## Uploading: three choices only you can make

1. **Altered or synthetic content.** The narration is a synthetic voice (Kokoro), speaking as Tanmay
   Kulkarni. Both descriptions say so. Whether to also tick YouTube's "altered or synthetic content"
   box is your call. It's meant for realistic content that could mislead, and a voice that introduces
   itself by a real name is the case to think about.
2. **Thumbnail.** Pick a custom thumbnail rather than frame 0.
3. **Captions.** Upload the `.srt` as English captions, not YouTube's auto-captions. They show written
   forms ("$42.50", "2026", "82", "tamper-resistant") where the audio uses the spellings the voice
   needs.

## The record

- **`FACTCHECK.md`:** every claim with its verification level.
  - The Mastercard quotes (M1–M11) were read on Mastercard's own pages.
  - The build facts (B1–B17) are live runs.
  - The opening receipt (B7) is a labelled reconstruction of the early version.
  - Rejected or qualified claims are kept.
- **`ANGLE.md`:** the angle and its uniqueness audit.
- **`SCRIPT.md`** (and `SCRIPT-SHORT.md`): the scripts with a source reference under each beat. The
  Short's includes its continuity table (words and picture at every cut).
- **`PEDAGOGY.md`** (and `PEDAGOGY-SHORT.md`): the signed Gate P records, each read aloud and signed
  by Tanmay Kulkarni on 2026-09-28. The post-sign-off TTS spelling changes are noted there, with the
  words unchanged.
- **`READ-ALOUD.md`** (and `READ-ALOUD-SHORT.md`): the sheets Gate P was read from.
- **`PROOF-REVIEW.md`, `PROOF-REVIEW-SHORT.md`:** every review pass, the defects each found, and
  how each was fixed and re-measured. Both films are **clear-for-public**:
  - long: teaching 12/12, production gate PASS, claims on screen when spoken **22/22**
  - Short: trailer 12/12, production gate PASS, claims **11/11**, 0 Shorts-UI-zone failures
  - both: 0 dark frames
- **`live_runs.py` / `live_runs.json`:** every terminal on screen is real output. Each session is
  typed into a real Python console inside a copy of the build (the current version, or the first
  version for the "before" runs) and captured, never hand-typed.

## Rebuilding

The build runs in the working folder, where the audio, clips, reference builds and QC folders
live; the scripts here are the record of it. `beat_sheet.json` (and `beat_sheet-short.json`) is the
source of truth, generated by `build_beat_sheet.py` (and `build_short_sheet.py`). Measured Kokoro audio is the clock and is never
hand-repaired.

```
python3 script_to_sheet.py && python3 build_beat_sheet.py   # narration + props; cues on the Whisper clock
<toolkit>/generate_audio_kokoro.py <reel>                    # only after Gate P
<toolkit>/remotion_scenes.py <reel> --only <beat> --force    # never while a sheet rebuild is running
<toolkit>/compile.py <reel> --height 2160                    # 3840 for the Short
pacing_pass.py <reel> --hold 0.3                             # then two-pass loudnorm to −14 LUFS / −2 dBTP
python3 make_captions.py . 0.3                               # and: python3 make_captions.py short 0.3
```

**Timing note.** Every beat in both films is timed on the Whisper clock. Whisper (faster-whisper
base.en, run locally) supplies word timings, which are snapped to the pauses in the audio itself.
This covers cues, claims and captions. Whisper also checked what the voice said against the script,
word by word. Two mishears led to TTS respellings ("tamper resistant", "Amount, and date."). The
captions show the written forms.
