# VISUAL QC — Show What Broke

| Cut | Resolution | Duration | Slots |
|---|---|---|---|
| review cut | 3840×2160 @30 | 167.99 s (2:48) | 13/13, no slates |

**GATE V (final compile):** 26 frames sampled · BLOCKER 0 · MAJOR 0.
History: 1 → 0 MAJOR.

Frames were also read by eye at 15 / 50 / 85% of every beat (B01 at 50 / 70 / 90%) —
`qc-contact-sheet.png`. That review found defects the gate passed.

## Defects found and fixed

| Log # | What broke | How noticed | Change | Checked |
|---|---|---|---|---|
| 12 | corrections landed at ~85% of B01; film 6 B01 was 8.7 s (skill minimum 9 s) | a person, frames at 75% and 90% (GATE V passed film 6) | one sentence added to each B01's narration; B01 audio regenerated (13.0 s / 12.0 s) | frames at 50/70/90% — correction on screen by 70% |

Remaining: 0 BLOCKER, 0 MAJOR. One SKIN LINT warning stands deliberately: the outro is a
`ShowTellCard` layout, because `ClaudeTitleOutro` hardcodes another channel's handle.
