# VISUAL QC — Look at the Frames

| Cut | Resolution | Duration | Slots |
|---|---|---|---|
| review cut | 3840×2160 @30 | 167.71 s (2:48) | 13/13, no slates |

**GATE V (final compile):** 26 frames sampled · BLOCKER 0 · MAJOR 0.
History: 1 → 0 MAJOR.

Frames were also read by eye at 15 / 50 / 85% of every beat (B01 at 50 / 70 / 90%) —
`qc-contact-sheet.png`. That review found defects the gate passed.

## Defects found and fixed

| Log # | What broke | How noticed | Change | Checked |
|---|---|---|---|---|
| 7 | B01 beats ran ~10 s; corrections not on screen by 75% | a person, contact sheets (GATE V passed film 2) | typing 35 → 20 ms/char, fewer pauses | frames at 50% and 90% re-read, all three films |
| 9 | "The gate caugh / Only eyes caug" | a person, contact sheet | labels → "Gate caught" / "Eyes caught" | frame re-read |
| 10 | JSON diff, log and Markdown cards all labeled PYTHON | a person, contact sheet | language set per card | frames re-read |

Remaining: 0 BLOCKER, 0 MAJOR. One SKIN LINT warning stands deliberately: the outro is a
`ShowTellCard` layout, because `ClaudeTitleOutro` hardcodes another channel's handle.
