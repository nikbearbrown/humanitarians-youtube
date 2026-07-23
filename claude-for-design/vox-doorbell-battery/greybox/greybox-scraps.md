# Greybox scraps — Why a Perfect AI Model Killed the Doorbell

One prompt per cutout/portrait. The leading 3-char id lands in Midjourney's output filename; drop the images into `greybox/scraps/` (keep the id in the filename) and re-run `greybox.py` — each image replaces its stand-in glyph.

Provenance lives in `scraps/sources.json` (`{"<id>": {"source": "generated|archive|user", "url": "..."}}`). A portrait of a real person whose image is generated or unsourced renders with an ink X (STAND-IN) and blocks final packaging — the X is removed by replacing the file, never by editing.

| id | kind | maps to | image | source | status |
|----|------|---------|-------|--------|--------|
| SYX | element | B01 | — | — | todo |
| VVE | element | B03 | — | — | todo |
| SzZ | element | B04 | — | — | todo |
| ZAr | element | B07 | — | — | todo |
| UjE | element | B11 | — | — | todo |

## Prompts (paste-ready)

```
SYX, PHOTO — Suburban front door in flat November light, a sleek smart video doorbell mounted beside it, indicator LED dark; set shot.focus on the doorbell, archival documentary photograph, desaturated, high contrast crushed blacks, aged newsprint grain, early 20th-century press-photo tone, clear margins, no modern objects --ar 4:3
VVE, PHOTO+ANNOTATION·ai — Product-teardown style plate: doorbell casing opened flat, board and battery visible. Remotion chips land on cue: 'HARDWARE — unchanged' (keyed to 'hardware'), 'BATTERY — unchanged' (keyed to 'battery'), terracotta chip 'FIRMWARE v2.1 — +person detection' (keyed to 'firmware update'). Degrades to clean plate., archival documentary photograph, desaturated, high contrast crushed blacks, aged newsprint grain, early 20th-century press-photo tone, clear margins, no modern objects --ar 4:3
SzZ, SCAN·prop — Designed 'INTEGRATION TEST REPORT' prop sheet (typewriter serif on aged paper, three checklist rows + one conspicuously absent fourth row of empty space). REMOTION PLANE: golden highlighter sweeps each row keyed to 'accuracy', 'processor', 'memory'; hand-drawn tick lands after each. The empty bottom of the page is the setup for B05. Degrades to hold+slow-zoom. Regions in annotations.json., archival documentary photograph, desaturated, high contrast crushed blacks, aged newsprint grain, early 20th-century press-photo tone, clear margins, no modern objects --ar 4:3
ZAr, PHOTO+ANNOTATION·ai — Macro plate of the doorbell's circuit board, processor centered. Remotion overlay: a horizontal awake/asleep timeline strip across the lower third — terracotta AWAKE blocks against a long dusty-blue ASLEEP floor — drawing left-to-right keyed to 'seconds of thinking'; label chip 'DUTY CYCLE = awake ÷ total' lands on the spoken 'duty cycle'. Degrades to clean plate., archival documentary photograph, desaturated, high contrast crushed blacks, aged newsprint grain, early 20th-century press-photo tone, clear margins, no modern objects --ar 4:3
UjE, PHOTO+ANNOTATION·ai — The B01 doorbell again, closer, lens dark. Remotion chips land in sequence: 'MODEL — correct' (dusty blue, keyed to 'accurate'), 'HARDWARE — correct' (dusty blue, keyed to 'perfectly'), 'DESIGN — wrong' (terracotta, keyed to the final 'wrong'). Degrades to clean plate., archival documentary photograph, desaturated, high contrast crushed blacks, aged newsprint grain, early 20th-century press-photo tone, clear margins, no modern objects --ar 4:3
```
