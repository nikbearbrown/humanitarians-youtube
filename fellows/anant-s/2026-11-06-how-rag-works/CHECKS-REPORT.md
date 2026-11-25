# CHECKS-REPORT: How RAG Works

Current as built (ai-explainer, converted 2026-11-24 from show-tell). Words are counted from the narration; seconds are the measured audio. Body classes are carried over from the original proof-gate table; the new beats are SHOW.

| Beat | Role | Class | Words | Sec | On-screen artifact |
|---|---|---|---:|---:|---|
| B00 | ASK | SHOW | 33 | 9.5 | Claude composer: greeting, the ask types in, three result lines |
| B01 | BLUF | SHOW | 33 | 12.1 | hesitant writer: "from what it memorized" → "from what it just looked up" |
| B10 | HERO | SHOW | 33 | 9.1 | box drops in; model block's dashed line stops short |
| B11 | OPEN | SHOW | 31 | 10.2 | box opens; three pages rise |
| B12 | STEP | SHOW | 33 | 10.9 | cut line splits pages into six slips |
| B13 | STEP | SHOW | 44 | 13.9 | scanner stamps each slip with a bar strip (29 numbers) |
| B14 | STEP | SHOW | 31 | 10.1 | strips file into drawers; lamps light |
| B15 | STEP | SHOW | 34 | 9.3 | question slip scanned into its own strip |
| B16 | STEP | SHOW | 47 | 15.3 | drawn ranking: question strip vs chunk strips, score bars 0.58 / 0.25 / 0.00 |
| B17 | STEP | SHOW | 39 | 10.9 | two slips and the question land on the prompt sheet |
| B18 | STEP | SHOW | 36 | 10.3 | prompt into model; "30 days" card; thread back to source |
| B19 | FAILS | SHOW (card) | 46 | 14.4 | tabs card: Before → After ranking flip (0.68 over 0.38) |
| B20 | FAILS | SHOW | 34 | 11.6 | stale page flows through; "14 days"; ring on the drawer |
| B21 | FIX | SHOW | 34 | 10.3 | stale slip removed; ranking restored; "30 days" |
| B22 | WHY_NOW | SHOW | 38 | 13.4 | cabinets multiply; counter to 21M; index swapped |
| BVDT | VERDICT | SHOW | 69 | 18.6 | verdict artifact, six lines |
| BHTF | YOUR_TURN | SHOW | 85 | 21.9 | composer prompt plus two check lines |
| BOUT | OUTRO | CARD | 7 | 3.9 | locked title outro |

**Total: 707 words · 215.6 s (3:35).**

## ai-explainer spine audit

| Slot | Required (ai-explainer SKILL.md) | This film | ✓ |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` cold open with result lines; Liam introduced in the first breath | "Hello, this is Liam, in for Bear. The ask: how c…"; three output lines | ✓ |
| B01 | `BrutalistHesitantWriter` BLUF, 20–35 words, `lead_silence_s: 0.8`, window ≥ 9 s, whole-phrase correction | 33 words; lead 0.8 s; 12.1 s | ✓ |
| Body | Manim lesson beats | B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22 | ✓ |
| BVDT | `ClaudeVerdictArtifact`, opens "Let's recap with Claude." | 6 lines | ✓ |
| BHTF | `ClaudeComposerAsk`, greeting "Your turn.", prompt read verbatim | unchanged | ✓ |
| BOUT | `ClaudeTitleOutro` (locked) | unchanged | ✓ |

The final passed GATE V, GATE T, the bookend check, the label and bottom-strip check, the master check and loudness. See BUILD-LOG.md for the values.

## History: original show-tell checks report (2026-11-22, kept verbatim)

Beat ids in this history are the pre-conversion ones: B00 → B10, B01 → B11, B02 → B12, B03 → B13, B04 → B14, B05 → B15, B06 → B16, B07 → B17, B08 → B18, B09 → B19, B10 → B20, B11 → B21, B12 → B22. Retired beats: BIDEA, BDEFS.

> # CHECKS-REPORT — written before the first slate (PROOF GATE)
>
> The 17 beats break down as 15 SHOW, 0 HOLD, 2 CARD and 0 PUNT:
> - **SHOW (15):** BIDEA (the correction is its motion), B00–B12 (12 drawn, 1 `ShowTellCard`) and BHTF.
> - **CARD (2):** BDEFS (terms, by design) and BOUT (locked outro).
> - **HOLD and PUNT:** none.
>
> | Beat | Class | On-screen artifact named in `shot.show` |
> |---|---|---|
> | BIDEA | SHOW | hesitant writer: "memorize my files" → "look them up" |
> | BDEFS | CARD | four terms land one by one |
> | B00 | SHOW | box drops in; model block's dashed line stops short |
> | B01 | SHOW | box opens; three pages rise |
> | B02 | SHOW | cut line splits pages into six slips |
> | B03 | SHOW | scanner stamps each slip with a bar strip (29 numbers) |
> | B04 | SHOW | strips file into drawers; lamps light |
> | B05 | SHOW | question slip scanned into its own strip |
> | B06 | SHOW | drawn ranking: question strip vs chunk strips, score bars 0.58 / 0.25 / 0.00 |
> | B07 | SHOW | two slips and the question land on the prompt sheet |
> | B08 | SHOW | prompt into model; "30 days" card; thread back to source |
> | B09 | SHOW (card) | tabs card: Before → After ranking flip (0.68 over 0.38) |
> | B10 | SHOW | stale page flows through; "14 days"; ring on the drawer |
> | B11 | SHOW | stale slip removed; ranking restored; "30 days" |
> | B12 | SHOW | cabinets multiply; counter to 21M; index swapped |
> | BHTF | SHOW | composer prompt plus two check lines |
> | BOUT | CARD | locked title outro |
>
> ## Show-tell laws
>
> | Law | Status | Where |
> |---|---|---|
> | ONE IMAGE PER BEAT | ✓ | every body beat is one drawing or one card |
> | THE VOICE EXPLAINS | ✓ | labels are 1–3 words; the one longer caption is the attribution "per Lewis et al. 2020" (Law 8 requires it) |
> | SAME OBJECTS, WHOLE FILM | ✓ | box → pages → slips → scanner/strips → drawers → prompt → model → answer, reused through B12 |
> | MOTION CARRIES THE CLAIM | ✓ | every `show` list has a motion per spoken point; no beat passes the still-frame test |
> | ATTRIBUTE THIN NUMBERS | ✓ | 21M spoken "Lewis and colleagues", captioned "per Lewis et al. 2020" |
> | CARD TEST | ✓ | B09 only; reason in SHOTLIST "Why a card" and its `why_card` (B06 drawn since 2026-11-23) |
> | ≤ ⅓ cards | ✓ | 1 / 13 |
> | AS LONG AS IT NEEDS | ✓ | one beat per pipeline step (chunk, embed, store, query, retrieve, prompt, answer), plus fail (B09–B10), fix (B11) and why-now (B12). No recap beat |
>
> ## Teaching arc
>
> | Item | Status | Where |
> |---|---|---|
> | FRAMEWORK | ✓ | BDEFS terms, then B00–B01 (what is being searched) |
> | WORKED EXAMPLE | ✓ | B02–B08: one question carried through every step with executed numbers |
> | FALSIFIABILITY | ✓ | B09–B10: a stale page wins retrieval and the answer goes wrong; B11 shows the fix |
> | SCAFFOLDED TASK | ✓ | BHTF: a prompt plus a two-point rubric |
> | BOOKENDS | ✓ | BIDEA, BDEFS, BHTF, BOUT; `bookend_check` PASS with `bookend_exempt: [cold-open, bvdt]` |
> | NO-SOURCE-NO-VERDICT | ✓ | every number traces to `evidence.json` or Lewis et al. 2020 |
>
> ## Machine checks run at planning (2026-11-22, from the toolkit root)
> - `python3 runtime/scripts/bookend_check.py <reel>` → `[bookend] PASS — four bookends correct for show-tell-how-rag-works`
> - `python3 runtime/qc/beat_lint.py <reel>` → `[beat-lint] clean — beat mix OK`
> - `python3 runtime/qc/factcheck_check.py <reel>` → see BUILD-LOG
>
