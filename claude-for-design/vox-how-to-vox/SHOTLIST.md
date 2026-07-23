# SHOTLIST — vox-how-to-vox (rev. 2026-07-06, the interface decision)

Typed work order. `pantry` command applies: beat-prefixed assets only;
archival copies use `source-` names; never two same-beat files in the pantry
at once. Portrait CLIPS auto-916; images need hand `-916` overrides.

Shot-type histogram: GRAPHIC 7 · FOOTAGE 5 · STILL 3 · CARD 4 · DOCUMENT 4 ·
COMPOSITE 3 (26 beats, no 3-in-a-row — lint clean).

Source axis: **ai 1** (B18 — the film's entire generated-image budget, kept
deliberately: the STAND-IN X needs an object) · **own 21** (Cowork captures
of THIS conversation, live terminal recordings, editor scans, Bear's photo,
self-harvested frames — all free) · CARD 4. No archive slots: nothing
depicts a real person or event, so nothing needs hunting.

CAPTURE RULES (all screen material): **light mode** — dark UI turns to mud
under the newsprint treatment; **crop to the app window** — no tabs, no menu
bar, no sidebar recents, no personal content; terminal runs recorded LIVE,
never restaged; Screen Studio exports flat (no drop shadows, no wallpaper
padding — the treatment is the frame).

**PLANE BEATS: B06, B11, B12, B16 (document annotation), B19 (the ring demo),
B04/B18/B23 (chips + labels). Regions in `annotations.json` — document
regions are needs_review until the grabs exist.**

---

## THE SHOOT PLAN (own-source slots, in shoot order)

| # | beat | window | capture |
|---|---|---|---|
| 1 | B01 | Cowork — still | the origin prompt pasted in the composer (do NOT send), tight crop on the message |
| 2 | B13 | Cowork — footage | the audio-lock exchange (the pasted run output) — slow scroll; do NOT re-run audio for footage |
| 3 | B11, B16, B12, B06 | editor — stills | script.md at the B11 paragraph · SHOTLIST at the B18 prompt · FACTCHECK verdicts · beat_sheet at the B06 entry (real durations visible) |
| 4 | B14 | terminal — footage | `vox_run.sh reels/vox-how-to-vox` running LIVE (this run also produces the slates) |
| 5 | B15 | frame grab | ffmpeg-extract B15's own slate frame from the pass-1 cut, drop back into B15 |
| 6 | B21 | frame grab | a burn-in frame from the `--review` cut |
| 7 | B17 | terminal — footage | `vox_pantry.py` intake LIVE (after media lands in pantry/) |
| 8 | B09 | Cowork — footage | the rebuild exchange — one changed slot recompiles, the rest report unchanged |
| 9 | B25 | Cowork — footage | a REAL AskUserQuestion gate (the shorts drop-list question, raised on request) being clicked |
| 10 | B23 | collage plates | the three final documents (beat_sheet, SHOTLIST, FACTCHECK) as treated scans — last, after docs freeze |

Each rebuild upgrades the film with footage of the build that produced it.
Two full machine passes minimum: pass 1 makes the slates and captures; pass 2
(after harvest) is the real cut. Exact paste-ready text for every Cowork and
terminal capture: see the conversation (the six numbered paste blocks).

Screen-grab spec: editor at readable zoom, light theme, crop 16:9. All grabs
land in `pantry/` beat-prefixed (`B06 — beatsheet-grab.png`), then `pantry`.

---

## Bear's photo slot

### B04 — COMPOSITE·own · the plate that gets treated (PENDING UPLOAD)
Any photograph Bear owns with **strong saturated color** — market stall,
flowers, neon, a red barn — the more color, the harder the treatment lands.
Compile applies the house look; the viewer watches saturated reality drain
to newsprint. Chips (−80% sat · ×1.15 contrast · newsprint ground) live on
the plane, not in the image. Drop in pantry as `B04 — <name>.jpg`.
Sidecar: `B04.source.txt` — "photograph by Nik Bear Brown, own work."

---

## AI slot (the whole generated-image budget — 1 still)

### B18 — COMPOSITE·ai · the generic stand-in (wears the X honestly)
PROMPT LAW (aspects/stock-styles.md): object, size, geometry, distribution,
material, light, ground, exclusions.
```
hyper-realistic portrait of an anonymous newspaper editor, 1920s newsroom, a face with no famous likeness, mid-forties, wire spectacles, rolled shirtsleeves, seated three-quarter view at a typesetting desk, one column of lead type in the foreground; single soft key light from the right, deep newsroom shadow behind; in the style of Lewis Hine documentary photography, clean sharp focus, clear facial features; no real person's likeness, no text, no labels --ar 16:9
```
MUST read as generic — if it resembles any identifiable person, regenerate.
The StrikeX and the sidecar chip render on the plane. Sidecar: `B18.source.txt`
with the ai-disclosure line. This is deliberately the film's ONLY generated
image — the beat about generated media shows generated media, nothing else does.

---

## GRAPHIC slots (PIPELINE — vox_scenes.py, render via vox_run)

| beat | scene | what |
|---|---|---|
| B03 | B03_LaunderingFunnel | three mismatched plates → treatment bar → matched on plane |
| B05 | B05_RestraintRules | token card; StrikeX lands on a decorative flourish on the spoken word |
| B07 | B07_AudioClock | duration bars from THIS sheet (self-updating at import); B07's bar fills live |
| B08 | B08_TwoAxisGrid | 5×3 type/source matrix from the sheet; B01's mark slides ai → own (its true history) |
| B19 | B19_AnnotationPlane | exploded 3-layer diagram; ring keyed to "now" via mp3/words.json |
| B20 | B20_Reband | side-by-side elements slide into a vertical stack (16:9 → 9:16) |
| B22 | B22_CostIsotype | 26 free squares vs 1 crimson narration + 1 terracotta still; final wait reads the sheet (B22 audio was regenerated) |

Desk preflight applies: explicit safe-area arithmetic in scene comments +
Gate A static check (16:9 ±6.4/±3.5; portrait ±1.95/±3.4).

**RENDER ORDER NOTE:** regen B22 audio and re-run vox_align BEFORE the first
vox_run — B07's bars and B22's tail read the sheet, and the word clock must
match the new mp3.

---

## Short (vox_short.py, after the master)

Candidate drops: B21 (burn-in still reads poorly at phone size), B23
(document collage too dense vertical), B26 outro (bear belongs to 16:9;
endcard inherits the Next line). Portrait relayouts needed for B07, B08,
B20, B22 (re-band, never scale). Decide at the short gate — the gate itself
is B25's footage.
