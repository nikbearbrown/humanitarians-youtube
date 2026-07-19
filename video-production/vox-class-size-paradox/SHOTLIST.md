# SHOTLIST — vox-class-size-paradox

Calling Bullshit (Vox Style). Plan approved + Gate F green 2026-07-06.
Histogram: GRAPHIC 6 · CARD 4 · STILL 2 (12 beats) (max run 2). Color law: navy = students, ink = classrooms, golden highlighter = the brochure number (once).
`pantry` law applies: beat-prefixed files; ai slots need disclosure sidecars.

---

## AI slots

### A01 — STILL·ai · the packed hall (kenburns)
```
hyperrealist photograph in the style of editorial documentary photography — a large university lecture hall seen from the very back row, hundreds of seats sloping down toward a distant lectern, most seats occupied, students seen only from behind as an anonymous crowd; hall fills the entire frame, aisle centered; institutional fluorescent light, flat and even, no dramatic shadows; no legible faces, no readable slides or text, no logos --ar 16:9
```
Sidecar `A01.source.txt` (ai disclosure). shot.focus mid-hall.

### A10 — STILL·ai · the brochure (kenburns)
```
hyperrealist still-life photograph in the style of editorial documentary photography — a glossy university admissions brochure lying on a wooden desk at a slight angle, cover showing an abstract campus-green photograph and generic sans-serif shapes suggesting text, a pen beside it; brochure fills the lower two-thirds; soft window light from the left, flat, no glare hotspots; no readable words, no real university name or seal, no logos --ar 16:9
```
Sidecar `A10.source.txt`. shot.focus on the cover.

---

## GRAPHIC slots (vox_scenes.py — written after audio lock, to measured durations)

| beat | scene | motion | what |
|---|---|---|---|
| A03 | A03_Campus | drawon | 24 classroom squares: 20 small, 4 large (the book's own example) |
| A04 | A04_ClassMean | annotate | counter over classrooms → 50; golden highlighter on the 50 |
| A06 | A06_StudentDrop | isotype | navy student-square drops repeatedly; 800/1,200 land big |
| A07 | A07_ExperiencedMean | annotate | counter recomputes over students → 140 |
| A09 | A09_TwoAverages | annotate | both counters side by side, same campus |
| A11 | A11_Everywhere | isotype | plane rows + gym floor: crowded units hold the witnesses |

Desk preflight applies (16:9 ±6.4/±3.5).

## Order of operations

1. Audio lock → `vox_align.py`.
2. Scenes written + Gate A.
3. `vox_run.sh` → slated cut → Gate B.
4. Stills → pantry → rebuild.
5. `vox_short.py`. Portrait relayouts: A03/A09.
