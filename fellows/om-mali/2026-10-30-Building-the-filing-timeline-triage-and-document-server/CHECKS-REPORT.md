# CHECKS-REPORT — building-the-filing-timeline-triage-and-document-server

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the week's actual instruction — *find the debt news, and prove nothing was thrown away* — and lands three answer lines, which are the three findings. COLD OPEN LAW: the ask lands ANSWERED. |
| B01 | SHOW | Claim: one of these two scores is evidence. Two bars on a shared per-report scale, and the two drawn reports with nothing to grade are **drawn as a dashed, excluded tail** beyond the second bar rather than dropped. |
| B02 | SHOW | Claim: two new defects, left open. Three named reports land with what each showed; the two disagreements carry their defect id as a chip reading `P38 · open`. A defect you can name is a defect someone can check next week. |
| B03 | SHOW | Claim: a window that closes before the answer. The quarter is drawn as a band, filings arrive inside it as ticks, and the window's right edge is the **one solid accent rule** on the frame. |
| B04 | SHOW | Claim: rules first, model last. Four stages, each filling inside the **same full-width 593 outline**, so every row is visibly a slice of one population and what fell away stays visible as the gap. The five rules land as chips. |
| B05 | SHOW | Claim: it found everything — now look at the three numbers under that one. Four bars on one scale under **one dashed pass line drawn through all four tracks**, with the two false alarms named beneath. |
| B06 | SHOW | Claim: three failures, each with what it changed. The consequence takes the accent and the failure does not, because a list of failures is a confession and a list of consequences is a record. |
| B07 | SHOW | Claim: cite the sentence, never retype the number. The query is shown **resolving** — query, id, the actual sentence — and the refusal of the graded report lands beneath it in the same shape. |
| B08 | SHOW | Claim: five numbers and the limit that narrows each. Each limit is drawn **beside the claim it narrows**. The 24 of 24 takes the accent, because it is the number most likely to be over-read. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## ILLUSTRATE LAW — no two consecutive body beats share a scheme

```
B01  two bars on a per-report scale, with an EXCLUDED dashed tail
B02  three named rows with defect-id chips, no chart
B03  a time band with filings as ticks and a hard right edge
B04  four stages NESTED inside one shared full-width outline
B05  four score bars under ONE dashed pass line, plus named alarms
B06  failure/consequence pairs joined by an arrow, no chart
B07  a query resolving to an id and a sentence, then a refusal
B08  claim/limit pairs, then a next-steps list
```

The adjacency to watch is **B04 / B05**, both of which are horizontal bars. They are
deliberately different objects: B04 keeps the full 593 outline on every row so each stage reads
as a slice of one narrowing population, and carries no pass line at all; B05's four bars have
four different denominators and share a single mark that was written down before the check ran.
If B04 is ever "simplified" to four free-standing bars it starts claiming four populations, and
if B05 loses its shared rule the 95% stops being a commitment and becomes a label.

B02, B06 and B08 are all text-pair beats and are deliberately **not adjacent to each other**.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B04's last
  stage fill at 0.60 and B03's filing ticks at 0.55
- Comparisons shown side-by-side, held ≥2s ✓ — B01's two bars with the excluded tail, B04's
  four nested stages, B05's four bars under one rule, and B07's hit against its refusal all
  persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓      B01/B02 — what last week's fixes are worth, checked on reports nobody had
                 read, with the defects that survived named and left open
WORKED EXAMPLE ✓ B03/B04 — one quarter's window, then the same 593 filings narrowed to 184
                 by five rules and a small model
MEASUREMENT ✓    B05 — a sample labelled before the run, with recall, precision and event
                 type on the same scale
COMPLICATION ✓   B06 — three things that broke, and what each one changed
CAPABILITY ✓     B07 — a filing turned into something the agent can cite rather than retype
LIMITS ✓         B08 — every number above, paired with what narrows it
HANDOFF ✓        B10 — label a sample before you run your filter, and report both numbers
```

## SHOW-DON'T-TELL spot checks

- "There was nothing to grade" is drawn as two dashed, empty cells past the end of the bar —
  present on the frame, excluded from the fraction.
- "Left open" is drawn as a chip reading `P38 · open`, not stated.
- "Nothing later can get in" is drawn by making the window's right edge the only solid accent
  rule on B03.
- "Rules first" is drawn by letting every funnel row keep the full 593 outline behind it.
- "It found everything" is drawn by filling one bar past a mark that was already on the frame.
- "Cites instead of retyping" is drawn by showing the query resolve to `s5` and then showing
  the sentence that id points at.
- B04's model note and B08's last row are the two places the reel tells rather than shows:
  there is no honest way to *draw* a thing that has not been built.

## Known risks carried into QC

1. **B01's excluded tail must never read as part of the score.** It is dashed, unfilled, and
   labelled `+2`, and the fraction beside it says `1 of 3`. If the dash weight ever drops, the
   tail starts looking like an empty bar segment, which is the opposite claim.
2. **B03's ticks are decorative in count, not in meaning.** 44 ticks stand for 593 filings and
   the frame never implies otherwise — the count is printed beside the band at headline size.
   Do not let anyone label the ticks.
3. **B04 and B05 are adjacent bar beats.** See the ILLUSTRATE LAW note above.
4. **B05's pass line sits inside a full bar.** At 95% of a filled track it can read as a seam
   in the fill rather than a mark. Check at 4K that the dashes are visible against the accent.
5. **B07's hit card holds a long sentence.** It is a real quoted sentence from a filing and is
   not shortened; check it wraps rather than clipping, in both orientations.
6. **Portrait will underfill.** It has every week since week 5. Budget for a rescale pass.
