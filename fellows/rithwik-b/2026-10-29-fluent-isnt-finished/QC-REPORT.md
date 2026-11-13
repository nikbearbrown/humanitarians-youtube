# VISUAL QC — Fluent Isn't Finished

| Cut | Resolution | Duration | Slots |
|---|---|---|---|
| review cut | 3840×2160 @30 | 171.82 s (2:52) | 13/13, no slates |

**GATE V (final compile):** 26 frames sampled · BLOCKER 0 · MAJOR 0.
History: 8 → 1 → 2 → 0 MAJOR across four compiles.

Frames were also read by eye at 15 / 50 / 85% of every beat (B01 at 50 / 70 / 90%) —
`qc-contact-sheet.png`. That review found defects the gate passed.

## Defects found and fixed

| Log # | What broke | How noticed | Change | Checked |
|---|---|---|---|---|
| 3 | GATE L: topic is None; claude-hai needs kicker "Irreducibly Human" | toolkit (GATE L — nothing rendered) | metadata.topic + B00 eyebrow set; B00 re-rendered | beat-lint clean |
| 4 | GATE V: 8 MAJOR underfill (B12 8%, B01 36%, B09 42%, B06 51%; min 55%) | toolkit (GATE V) | bigger type, new cards, 4-row search, title-layout outro | compiles 2–4 → MAJOR 1, 2, 0 |
| 5 | B06 stack card showed meaningless ball images | a person, contact sheet | swapped to a focus card | still rendered and read before re-render |
| 6 | B01 still typing the correction at 85% of the beat | a person, frame at 85% | typing 50 → 35 ms/char, type 84 → 140 px | frame re-read |

Remaining: 0 BLOCKER, 0 MAJOR. One SKIN LINT warning stands deliberately: the outro is a
`ShowTellCard` layout, because `ClaudeTitleOutro` hardcodes another channel's handle.
