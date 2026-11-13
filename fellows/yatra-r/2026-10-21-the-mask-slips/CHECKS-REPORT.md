# CHECKS-REPORT — The Mask Slips.

`yatra-the-mask-slips` · written before the first cut compiled, per the PROOF GATE.

---

## Beat classification

**13 SHOW · 0 justified-HOLD · 0 PUNT-flagged**

| Beat | Class | The artifact it names |
|---|---|---|
| B00 | SHOW | composer types the ask; three result lines land — the ask is ANSWERED |
| B01 | SHOW | two phases build on either side of a divider that draws on the spoken pivot |
| B02 | SHOW | three figures land in spoken order; an accent tick marks how early the spike came |
| B03 | SHOW | one figure sets huge; the REPORTED chip lands against it |
| B04 | SHOW | composer types the generation prompt for the beat that follows |
| B05 | SHOW | the curve draws, crests, takes a marker, and falls away from it |
| B06 | SHOW | the wire turns dashed along its whole length — retroactively, not by snapping |
| B07 | SHOW | each bar visibly HALVES on the spoken "lost roughly half" |
| B08 | SHOW | three explanations set and rule through; the survivor lands alone |
| B09 | SHOW | two ledgers stack; the refusals take the accent; the falsifier lands last |
| B10 | SHOW | artifact page, five verdict lines stagger |
| B11 | SHOW | the handoff prompt types itself as it is read aloud; rubric stacks |
| B12 | SHOW | title restates poster-style with the terracotta period |

---

## Teaching arc

| Item | Status | Where |
|---|---|---|
| FRAMEWORK before examples | ✓ | B01 states the two-phase arc before any figure |
| WORKED EXAMPLE | ✓ | B02–B03 run one real account through the rise |
| FALSIFIABILITY | ✓ | B09 — required `falsifier`: "Check the accounts yourself…" |
| SCAFFOLDED TASK | ✓ | B11 — prompt read aloud verbatim, graded against three checks |
| BOOKENDS (4) | ✓ | B00 cold open · B01 BLUF · B10 verdict · B11 handoff · B12 outro |
| NO-SOURCE-NO-VERDICT | ✓ | every figure carries a required `source`; the verdict repeats the citations |

---

## Frame laws

| Law | Status |
|---|---|
| COLD OPEN LAW | ✓ B00 is `ClaudeComposerAsk` with RESULT lines |
| EXECUTIVE-SUMMARY LAW | ✓ B01 is the BLUF — plain language, gist not teaser |
| ILLUSTRATE LAW | ✓ UI at B00, B04, B10, B11, B12 only; eight purpose-built `Msk*` body scenes, no two consecutive beats sharing a scheme |
| ASK→RESULT LAW | ✓ one pair: B04 asks, B05 is the result |
| SHOW-DON'T-TELL | ✓ every beat carries a `show` block authored before its narration |
| HANDOFF LAW | ✓ B11 — prompt read aloud, then discussed |
| OUTRO LAW | ✓ B12 restates the title; `@Yatra`; NO subline |
| LOGO LAW | ✓ `@Yatra` wordmark bug, low opacity, inside the safe inset, every beat |
| IN-FOR-BEAR LAW (Yatra form) | ✓ B00 names the voice; B12 signs off; greeting carries the narrator's name; chip stays `@Yatra` |
| One terracotta per beat | ✓ thirteen for thirteen — see `SHOTLIST.md` |

---

## Honesty

Full detail in `FACTCHECK.md`:

- **Figures:** six, all from one report (Garbage Day, Oct 2026), all rendered verbatim as
  strings with their hedges intact. Sweep over every on-screen string found no numeric
  token that wasn't either a supplied figure or the citation year.
- **Attribution:** `MskSpike`, `MskMoney` and `MskDrop` each **require** a `source`.
- **Identification:** no `name`/`handle`/`platform` prop exists, so neither account can be
  identified.
- **Hedges:** `MskMoney` requires a `stamp` ("reported"); "roughly 50%" keeps its qualifier.

---

## Known deviations

**GATE T (`scripts/type_check.py`) — NOT RUN; the script is not present in this toolkit
tree.** Substituted by the frame inspection in `_qc/QC-LOG.md` and the numeral sweep in
`FACTCHECK.md`. Logged rather than silently passed.

**GATE V (`runtime/qc/final_frame_check.py`) — not used.** Its `BURN_IN_EXCLUDE` masks the
bottom strip while the review cut's beat label is drawn top-right, so it reports BLOCKERs
on every reel built in this tree. Ink coverage measured directly with its own
`analyze_frame()` on the clean master instead. Toolkit bug, not a reel defect.
