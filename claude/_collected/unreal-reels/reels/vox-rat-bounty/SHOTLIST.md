# SHOTLIST — vox-rat-bounty

Calling Bullshit (Vox Style). Plan approved + Gate F green 2026-07-06.
Histogram: GRAPHIC 6 · CARD 4 · STILL 2 (12 beats) (max run 2). Color law: navy = tails counter, crimson = rat population, terracotta annotation.
`pantry` law applies: beat-prefixed files; ai slots need disclosure sidecars.

---

## AI slots

### A01 — STILL·ai · colonial Hanoi over a grate (kenburns)
```
hyperrealist photograph in the style of early-20th-century documentary photography — a quiet French-colonial street corner, pale shuttered facades and a wrought-iron lamppost, a heavy cast-iron sewer grate in the cobblestone foreground; grate in the lower third, street receding behind; flat overcast daylight, muted tones; no people, no vehicles, no signage, no readable text --ar 16:9
```
Sidecar `A01.source.txt`. shot.focus on the grate.

### A05 — STILL·ai · the tailless rat (kenburns)
```
hyperrealist photograph in the style of natural-history documentary photography — a single brown rat in profile beside a cast-iron sewer grate on wet cobblestones, its tail conspicuously absent, stub visible, otherwise healthy; rat centered in the lower half, shallow background of dark brick; flat diffuse light, no dramatic shadows; no people, no text, no gore, no injury detail beyond the missing tail --ar 16:9
```
Sidecar `A05.source.txt`. shot.focus on the stub.

---

## GRAPHIC slots (vox_scenes.py — written after audio lock, to measured durations)

| beat | scene | motion | what |
|---|---|---|---|
| A03 | A03_SewerBounty | drawon | ink sewer map under a street grid; bounty chip: cash per tail |
| A04 | A04_TailsPourIn | isotype | navy tail-tally climbing by thousands |
| A07 | A07_TheLoop | drawon | catch → snip → release → breed, ink arrows, closed cycle |
| A08 | A08_TwoCurves | drawon | navy tails curve vs crimson rat curve, diverging |
| A10 | A10_RatFarms | isotype | captive-rat grid multiplying ('raised in captivity' — verbatim) |
| A11 | A11_ModernEcho | drawon | class-size histogram cliff at 19|20 (verified) |

Desk preflight applies (16:9 ±6.4/±3.5).

## Order of operations

1. Audio lock → `vox_align.py`.
2. Scenes written + Gate A.
3. `vox_run.sh` → slated cut → Gate B.
4. Stills → pantry → rebuild.
5. `vox_short.py`. Portrait relayouts: A07/A08.
