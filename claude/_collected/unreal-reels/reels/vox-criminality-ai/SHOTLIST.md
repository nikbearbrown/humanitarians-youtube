# SHOTLIST — vox-criminality-ai

Calling Bullshit (Vox Style). Plan approved + Gate F green 2026-07-06.
Histogram: GRAPHIC 5 · CARD 4 · STILL 2 (11 beats) (max run 2). Color law: crimson = the bias entering, navy = the three measurements. VISUAL SAFETY: no photoreal faces anywhere.
`pantry` law applies: beat-prefixed files; ai slots need disclosure sidecars.

---

## AI slots

### A01 — STILL·ai · the dataset, face-down (kenburns)
```
hyperrealist still-life photograph in the style of editorial documentary photography — a gray archive box filled with hundreds of printed photographs stacked ALL FACE-DOWN, one photo lifted at the corner by its edge showing only white photo-paper backing, catalog dividers between sections; box fills the frame at a three-quarter angle; single soft key light from the left; NO visible faces, no readable text, no labels --ar 16:9
```
Sidecar `A01.source.txt`. shot.focus on the lifted corner.

### A03 — STILL·ai · the old pseudoscience, as objects (kenburns)
```
hyperrealist still-life photograph in the style of museum documentation photography — antique brass measuring calipers lying open on aged paper beside a 19th-century-style engraved diagram of an abstract head divided into unlabeled regions, a magnifying glass at the edge; objects arranged on dark wood, filling the frame; raking light from the upper left, gentle shadows; the diagram is abstract with NO readable words, no real face, no labels --ar 16:9
```
Sidecar `A03.source.txt`. shot.focus on the calipers.

---

## GRAPHIC slots (vox_scenes.py — written after audio lock, to measured durations)

| beat | scene | motion | what |
|---|---|---|---|
| A04 | A04_BlackBox | drawon | data → box → verdicts; two drawn photo-stacks feed in (stacks, never faces) |
| A05 | A05_ThreeMeasures | annotate | schematic ink line-face; three navy measurement lines, serif labels |
| A07 | A07_TwoSources | annotate | two labeled stacks: professional headshots vs official ID documents |
| A08 | A08_TheMorph | drawon | THE beat: schematic face relaxes smile → flat; all three navy lines shift together |
| A10 | A10_BoxStaysClosed | drawon | crimson bias flows through the untouched ink box into the verdicts |

Desk preflight applies (16:9 ±6.4/±3.5).

## Order of operations

1. Audio lock → `vox_align.py`.
2. Scenes written + Gate A.
3. `vox_run.sh` → slated cut → Gate B.
4. Stills → pantry → rebuild.
5. `vox_short.py`. Portrait relayouts: A05/A08. Description must carry the corrected citation (Xiaolin Wu & Xi Zhang, arXiv:1611.04135).
