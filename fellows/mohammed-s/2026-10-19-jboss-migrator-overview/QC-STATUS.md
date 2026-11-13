# QC STATUS — Prove Nothing Broke.

Build date: 2026-10-28 · 13 beats · 3:35 measured audio · Kokoro `am_onyx` · $0.00

| File | Spec | Duration |
|---|---|---|
| `hussain-jboss-migrator-overview-4k-16x9.mp4` | 3840×2160, 24fps, AAC 48kHz stereo | 215.0s |
| `hussain-jboss-migrator-overview-4k-9x16.mp4` | 2160×3840, 24fps, AAC 48kHz stereo | 215.0s |

The 9:16 is a native reflow (`./art vertical` → all 13 beats on `*916` compositions,
re-rendered portrait), never a centre-crop. Both files decode end to end with zero errors.

## GATE V

| Aspect | BLOCKER | MAJOR |
|---|---|---|
| 16:9 | 0 | 2 (B01_50, B01_85 underfill) |
| 9:16 | 0 | 2 (B01_50, B01_85 underfill) |

B01 is the BrutalistHesitantWriter typing beat: at 50%/85% the overview is still being
typed, so the frame is mostly empty by construction (same finding as the Cortex and
Snowshift reels). The final frame shows both corrections landed:
"It migrates the mechanics. / You prove nothing broke."

As with those reels, `compile.py` refused to promote a clean master because of this, so
the masters were joined from the compiler's own conformed clips (`clips/concat.txt`,
`vertical/clips/concat.txt`) with its narration track (`clips/_work/master.wav`).
They have **not** passed `./art final` formally; that is a human call.

## Frame review (read by eye, both aspects)

Preview stills of every new scene in both aspects, then GATE V samples and extra frames
from the masters. Fixed before the 4K render: portrait annotation grid holes (B02),
empty pipeline cards (B03), dead space in log/test cards (B04), sparse MTA rows and a
clipped "MANDATORY" pill (B05), small type (B06–B08), truncated recipe column (B08).

## Not verified

- Presenter has not reviewed the cut yet.
- Recipe package paths in FACTCHECK.md should be confirmed before code is scaffolded.
