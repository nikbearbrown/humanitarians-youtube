# SHOTLIST — vox-prosecutors-fallacy

Calling Bullshit (Vox Style). Plan approved + Gate F green 2026-07-06.
Histogram: GRAPHIC 4 · CARD 4 · STILL 2 (10 beats) (max run 2). Color law: crimson = false matches, ink = the one guilty, navy = the reading direction.
`pantry` law applies: beat-prefixed files; ai slots need disclosure sidecars.

---

## AI slots

### A01 — STILL·ai · the witness stand (kenburns)
```
hyperrealist photograph in the style of editorial documentary photography — an American courtroom seen from the jury box, the witness stand lit by high windows, wood paneling, the judge's bench in soft blur behind; witness stand at the golden-section point, no occupants sharply resolved, any figures distant and indistinct; flat daylight through tall windows; no legible faces, no text, no seals or emblems in focus --ar 16:9
```
Sidecar `A01.source.txt`. shot.focus on the empty stand.

### A09 — STILL·ai · the dragnet (kenburns)
```
hyperrealist photograph in the style of editorial documentary photography — a dim control room with a wall of surveillance monitors, each screen showing abstract blurred street scenes and bounding-box rectangles, operator chairs empty in the foreground; monitor wall fills the upper two-thirds; cool screen glow as the only light source, flat; NO legible faces on any screen, no readable text, no logos --ar 16:9
```
Sidecar `A09.source.txt`. shot.focus on the center screen.

---

## GRAPHIC slots (vox_scenes.py — written after audio lock, to measured durations)

| beat | scene | motion | what |
|---|---|---|---|
| A03 | A03_Database | isotype | scaled grid standing for 50 million prints, count chip |
| A05 | A05_SixMatches | isotype | six squares surface: five crimson, one ink |
| A06 | A06_TwoReadings | annotate | 2×2 table; navy highlight pivots row → column (the book's own device) |
| A08 | A08_BiggerDatabase | isotype | the field grows; crimson matches multiply |

Desk preflight applies (16:9 ±6.4/±3.5).

## Order of operations

1. Audio lock → `vox_align.py`.
2. Scenes written + Gate A.
3. `vox_run.sh` → slated cut → Gate B.
4. Stills → pantry → rebuild.
5. `vox_short.py`. Portrait relayouts: A05/A06.
