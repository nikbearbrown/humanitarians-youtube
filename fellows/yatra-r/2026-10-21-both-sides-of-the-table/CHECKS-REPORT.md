# CHECKS-REPORT — Both Sides of the Table.

`yatra-both-sides-of-the-table` · written before the first cut compiled, per the PROOF GATE.

---

## Beat classification

**14 SHOW · 0 justified-HOLD · 0 PUNT-flagged**

| Beat | Class | The artifact it names |
|---|---|---|
| B00 | SHOW | composer types the ask; three result lines land — the ask is ANSWERED |
| B01 | SHOW | three claims land on alternating sides; the third takes the accent |
| B02 | SHOW | the employer side fills while the other side stays drawn but faint |
| B03 | SHOW | the frame mirrors; the candidate side fills |
| B04 | SHOW | composer types the generation prompt for the beat that follows |
| B05 | SHOW | four seats fill, then traffic runs ONLY between the two machines |
| B06 | SHOW | the figure sets, its bar fills, the delta chip lands |
| B07 | SHOW | a share of the applicant marks MOVES OUT of the row |
| B08 | SHOW | two figures held side by side, each with its own citation |
| B09 | SHOW | a hidden layer fades up INSIDE an ordinary page |
| B10 | SHOW | two ledgers; the refusals take the accent; the falsifier lands last |
| B11 | SHOW | artifact page, five verdict lines stagger |
| B12 | SHOW | the handoff prompt types itself as it is read aloud; rubric stacks |
| B13 | SHOW | title restates poster-style with the terracotta period |

---

## Teaching arc

| Item | Status | Where |
|---|---|---|
| FRAMEWORK before examples | ✓ | B01 states the standoff before any figure |
| WORKED EXAMPLE | ✓ | B02–B03 run both sides of one real adoption picture |
| FALSIFIABILITY | ✓ | B10 — required `falsifier`: "Different studies. Read them before you stack them." |
| SCAFFOLDED TASK | ✓ | B12 — prompt read aloud verbatim, graded against three checks |
| BOOKENDS (4) | ✓ | B00 · B01 BLUF · B11 verdict · B12 handoff · B13 outro |
| NO-SOURCE-NO-VERDICT | ✓ | every figure carries a required `source`; `TblTrust` requires one PER FIGURE |

---

## Frame laws

| Law | Status |
|---|---|
| COLD OPEN LAW | ✓ `ClaudeComposerAsk` with RESULT lines |
| EXECUTIVE-SUMMARY LAW | ✓ B01 is the BLUF, plain language, reveals unspent |
| ILLUSTRATE LAW | ✓ UI at B00, B04, B11, B12, B13 only; eight purpose-built `Tbl*` body scenes |
| ASK→RESULT LAW | ✓ one pair: B04 asks, B05 is the result |
| SHOW-DON'T-TELL | ✓ every beat carries a `show` block authored before its narration |
| HANDOFF LAW | ✓ B12 — prompt read aloud, then discussed |
| OUTRO LAW | ✓ B13 restates the title; `@Yatra`; NO subline |
| LOGO LAW | ✓ `@Yatra` bug, low opacity, inside the safe inset, every beat |
| IN-FOR-BEAR LAW (Yatra form) | ✓ B00 names the voice; B13 signs off; chip stays `@Yatra` |
| One terracotta per beat | ✓ and never on an adoption figure — see `SHOTLIST.md` |

---

## Honesty

Full detail in `FACTCHECK.md`:

- **Eight figures, five publishers, all cited on screen.** `TblTrust` requires a
  **separate** source per figure so two studies can never be merged into one claim.
- **`value` is verbatim, `bar` is separate** — "4 in 5" is never rendered as "80%".
- **No remainder is captioned** (74% never appears), **no earlier interview figure is
  implied** (required `deltaNote` says why), **the 41% is stamped self-reported**.
- Sweep over every on-screen string found only the eight supplied figures plus citation
  years.

---

## Known deviations

**GATE T (`scripts/type_check.py`) — NOT RUN; not present in this toolkit tree.**
Substituted by frame inspection (`_qc/QC-LOG.md`) and the numeral sweep. Logged.

**GATE V — not used; it reports false BLOCKERs on every reel built in this tree.** Ink
coverage measured with its own `analyze_frame()` on the clean master instead.

**Render environment.** This build hit two toolkit-level render failures that are not reel
defects and are documented in `BUILD-PROMPT.md`: orphaned `chrome-headless-shell`
processes after a machine sleep (fixed by killing them and clearing stale puppeteer
profile dirs), and Remotion's 30s per-frame default being too low for scale=2 frames of
full-bleed EB Garamond (fixed by adding an `ART_TIMEOUT` knob to
`runtime/scripts/remotion_scenes.py`, defaulting to 120000).
