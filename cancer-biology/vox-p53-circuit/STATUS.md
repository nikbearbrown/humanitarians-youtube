# STATUS — vox-p53-circuit
## Why Cancer Cannot Read Its Own Death Instructions

**State:** slate cut complete — review MP4 ready

---

## Build summary

| field | value |
|---|---|
| Slug | vox-p53-circuit |
| Beats | 15 |
| Duration | 241.66s (~4:01) |
| Gate A | PASS — 13/13 scenes clean |
| Gate W | 4 W6 WARNs (white-on-filled-circle labels, cosmetic) — no ERRORs |
| Gate P | PASS |
| Gate 0 (audio) | PASS — 15 mp3s + timings.json |
| Gate B | WARNING (manim_layout_audit.py could not import manim — slotted anyway) |
| Slots filled | 13/15 (MANIM) |
| Slots open | B02 (STILL · ai — keratinocyte monolayer), B08 (STILL · ai — MOMP diagram) |
| Review MP4 | `vox-p53-circuit/vox-p53-circuit-review.mp4` |

---

## Open slots (fill to finalize)

| Beat | Type | Description |
|---|---|---|
| B02 | STILL · ai | keratinocyte monolayer, one apoptotic cell; see PROMPTS.md |
| B08 | STILL · ai | MOMP / cytochrome c release diagram; see PROMPTS.md |

Drop the filled stills into `media/B02.png` and `media/B08.png`, then rerun
`bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-p53-circuit` — only
those two slots recompile.

---

## Review command

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-p53-circuit/vox-p53-circuit-review.mp4
```

---

## Motion histogram note

`drawon` carries 66% at slate stage (10/15 beats). Once B02 and B08 are filled as
`kenburns`, the ratio drops to 10/15 → the MOTION.md warning is expected for a
slate cut and resolves when the ai stills are filled.

---

## Color law
- TEAL = p53 wild-type / damage sensed / death executed
- CRIMSON = p53 mutant / hub absent / lineage drifts
- GOLD = editor's-pen fill (B07 BCL-2 balance label, once)
- No swaps mid-film

## Exclusions confirmed
No extrinsic pathway, no necroptosis/ferroptosis/pyroptosis, no venetoclax/BH3
mimetics, no p53 tetramer/dominant-negative detail, no p53 arrest-vs-senescence
choice mechanism.
