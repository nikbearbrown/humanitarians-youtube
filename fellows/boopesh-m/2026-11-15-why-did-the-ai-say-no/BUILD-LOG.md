# BUILD-LOG — Why Did the AI Say No?

Brutalist toolkit `a99b5323` (main, not upgraded), built 2026-11-15 in a Linux cloud container (Python 3.13 venv,
numpy 2.5.4, scikit-learn 1.9.1, Manim 0.20.1, Remotion 4.0.535, Kokoro `am_onyx`). Another builder shared the 4 CPUs.

## Commands
```bash
cd code && python3 credit_reasons.py > run.log && python3 typeset.py ../assets ../short/assets && cd ..   # ~9 s
python3 make_sheet.py && (cd short && python3 make_sheet.py)
python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <reel>         # and <reel>/short
python3 <brutalist>/runtime/scripts/remotion_scenes.py <reel> --only B00    # B10, B80; short: B00
<brutalist>/art run <reel>                # Manim 4K + gates A/W/B, review cut   (and <reel>/short)
python3 <brutalist>/runtime/scripts/type_check.py <reel>                    # GATE T: PASS (both)
<brutalist>/art final <reel> --height 2160 --out weekly-submission/landscape
<brutalist>/art final <reel>/short --height 3840 --out weekly-submission/vertical
```
Experiment reproducibility: a second run of `credit_reasons.py` in a scratch folder gave an identical `run.log` and an
identical `results.json` apart from `runtime_s` (checked after every change to the script; `OMP_NUM_THREADS=1`,
no early stopping).

## Gates and fixes (in order)
- Voice approval: `metadata.approvals.voice` copied from Boopesh's 2026-10-24 chat approval ("I approve am_onyx as my
  narrator voice."), subject fingerprint `9fbee75c…991c85e` from `./art approvals --fingerprints` (both reels).
- Length: first narration measured 161 s → cut the circular number from the spoken line (Kokoro read "2022-03" as
  "two thousand twenty-two dash zero three"; years now spelled "twenty twenty-two"), shortened B30/B40/B60/B80:
  146.6 s landscape / 45.6 s Short (inside 2:00–2:40 and 0:40–0:60).
- B10 hesitant writer: correction ("the model said no" → "your debt is too high for your income") checked frame by
  frame; the corrected line is complete at ≈6.0 s of the 7.3 s beat, then holds.
- Preview frames: B30 tree icon touching its caption; B40/B70 marker labels crossing the cutoff line and each other
  (labels now sit beside the stem, away from the line, staggered); B50 caption under the dark card and small reason
  text (wrapped onto two lines in a wider card); B60 "list can shift" text too small (rebuilt as five lines);
  Short B20 title overlapping the first card → all moved. Scorecard icon bars now drawn from the fitted weights.
- Fill pre-check (`fillcheck.sh`, 1920×1080 and 1080×1920): Clean on both reels.
- GATE B (layout, strict): B20 footer "what the rule asks for, not legal advice" 0.04 below the safe area → raised
  (other bottom captions raised with it); B70 "scorecard 53.2%" label ran past the shaded deny zone (label-on-line) →
  meter widened and the before-labels shortened to whole percents.
- GATE T (type): PASS on both reels first time.
- Gate V on the review cuts: only `edge-bleed` BLOCKERs from the burned-in review labels (false positives per the
  brief); the clean finals passed (`art final` exit 0; `_qc/REPORT.md` 0 BLOCKER / 0 MAJOR for both).
- Skin lint (warning only, same as the reference reels): B90 outro is a Manim scene, not `ClaudeTitleOutro`; Short
  B00 uses `ClaudeComposerAsk916` (the portrait composer).

## Exports
| File | Size | Duration | Loudness | SHA-256 |
|---|---|---|---|---|
| toolkit master `landscape/why-did-the-ai-say-no-master.mp4` (verified receipt `why-did-the-ai-say-no-master.verified.json`) | 3840×2160 | 146.79 s | −24.5 LUFS | cbadb94fd18067b001d93aa0473cc181593338c991ac0c03fedc34edceb1b283 |
| **delivered** `landscape/WhyDidTheAISayNo_BoopeshM.mp4` | 3840×2160 | 146.8 s | −14.2 LUFS, −0.9 dBTP | 494e9c394b7acd0ae387fafb41a861bf34a315cc2e7b907a16bbb81525d661d2 |
| toolkit master `vertical/why-did-the-ai-say-no-short-master.mp4` (verified receipt) | 2160×3840 | 45.71 s | −24.2 LUFS | b09068b5b1af139034b1c4bfd4424c8f9d5ed6d89d529d898a7c253096b7fc42 |
| **delivered** `vertical/WhyDidTheAISayNo_BoopeshM.mp4` | 2160×3840 | 45.8 s | −14.2 LUFS, −1.0 dBTP | 7a5d69adb8c42a7dcb82203e7720e588918c7ab061219114bdc0def31869772c |

Delivered files = verified masters with the video stream copied bit-for-bit (checked: identical hash of the copied video stream)
and only the audio loudness-normalised (two-pass ffmpeg `loudnorm`, I=−14, TP=−1, LRA=11, linear; AAC 320k,
`+faststart`) to YouTube's reference level. The master was renamed `<slug>-master.mp4` after verification (the
receipt's `output` field still names the original path). Eight frames of each delivery file were looked at.
