# SHOTLIST — vox-silent-omission

**Why an Agent That Finishes First Can Be Worse Than One That Stops** · 16:9 · ~150s est. (12 beats)
Accents: TEAL `#1F6F5C` = read / processed / reached · CRIMSON `#BF3339` = unread / skipped / silently missing · GOLD `#F5D061` = editor's pen (once per graphic, maximum).
Source: chapter 09, silent-omission failure mode — one mechanism only: an agent reports success from successful operations and does not surface what it could not reach.
Card exclusions honored: no taxonomy of all eight failure modes · no prompt injection · no hallucination probability formalism.

Shot-type histogram: STILL 1 · GRAPHIC 7 · CARD 4 — max consecutive same-type: 2. Lint: pass.
Act map: COLD OPEN (B01) · QUESTION (B03) · PROBLEM (B04–B05) · MECHANISM (B06–B08) · EXAMPLE (B08) · PRACTICE (B09–B10) · IMPLICATION (B11) · RECAP (B12).
Color law: TEAL = reached/processed, CRIMSON = silently skipped — never swapped.

---

## B01 — STILL · ai · kenburns · ~11s  ← MEDIA SLOT
Cue: "The brief looked good. Six bullets. A clear recommendation…"
Slot: `media/B01.png`
Archive search: none — synthetic plate.

```
B01, a clean executive brief document printed on cream newsprint — six crisp bullet points visible, a confident recommendation paragraph at the bottom, editorial collage treatment desaturated, pinned to aged newsprint ground, flat print reproduction, no people
```

`shot.focus` toward the recommendation line (bottom-center). Disclosure line in credits (synthetic).

---

## B02 — GRAPHIC · own · manim · ~12s
Cue: "Two days later, a colleague pointed out three dissenting documents…"
Manim: `B02_FolderTree` — folder tree: top node 'project/', five document leaves in TEAL ('read'), three leaves in 'dissenting/' subfolder in CRIMSON ('unread'), summary doc glowing green at bottom labeled 'COMPLETE'.

## B03 — CARD (question) · own · hold · ~11s
Cue: "Here is the mechanism…"
Copy: **Why does a completion report look identical whether the scan was complete or not?**

## B04 — GRAPHIC · own · manim · ~13s
Cue: "…it works operation by operation."
Manim: `B04_OperationChain` — horizontal chain of three boxes (READ, SUMMARIZE, NEXT), each filling TEAL with a checkmark in sequence; chain repeats for a second file.

## B05 — GRAPHIC · own · manim · ~13s
Cue: "But the agent does not know what it could not reach…"
Manim: `B05_InvisibleFiles` — TEAL chain on left; three CRIMSON file icons on right (no access, unreadable scan, not listed); vertical dashed dividing line.

## B06 — CARD (section) · own · hold · ~11s
Cue: "A completion report is built from successful operations…"
Copy: **The completion report sees only what completed.**

## B07 — GRAPHIC · own · manim · ~14s
Cue: "…twenty-three files processed, brief generated, task complete."
Manim: `B07_CountMismatch` — two rows of squares: top row 23 TEAL (report); bottom row 23 TEAL + 3 CRIMSON (folder). The 3 CRIMSON squares have no counterpart above.

## B08 — GRAPHIC · own · manim · ~12s
Cue: "Maya ran an agent over twelve client PDFs…"
Manim: `B08_MayaExample` — 12 file icons: 9 TEAL with check, 3 CRIMSON labeled 'scan — unreadable'; arrow from 9 to 'DIGEST' doc labeled 'old targets'; label 'Q4 revision' points to one CRIMSON file.
Note: illustrative example, numbers labeled illustrative in FACTCHECK.

## B09 — GRAPHIC · own · manim · ~13s
Cue: "The practice: before you accept a completion report, ask for an inventory."
Manim: `B09_InventoryCheck` — three stacked question rows animate in: 'In scope: ?' / 'Processed: ?' / 'Skipped/failed: ?'; skipped row highlights CRIMSON when nonzero.

## B10 — CARD (section) · own · hold · ~11s
Cue: "A confident completion is not evidence of a complete scan."
Copy: **The count mismatch is the signal.**

## B11 — GRAPHIC · own · compare · ~12s
Cue: "A crash tells you something went wrong. A confident completion might not."
Manim: `B11_CrashVsSilent` — two columns: left 'CRASH' with red error box (problem visible); right 'SILENT OMISSION' with green 'COMPLETE' box; arrow under right to 'gap in brief' in CRIMSON.

## B12 — CARD (endcard) · own · hold · ~12s
Cue: "A completion report should predict a complete scan. Here is why it does not…"
Copy: **Ask for the inventory, not just the result.** / sub: AGENTIC AI
