# CHECKS-REPORT — building-the-human-review-queue

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the ask and lands three answer lines — motion is the type-on and the result reveal. The interface IS the subject (COLD OPEN LAW). |
| B01 | SHOW | Claim: the software routed, grouped and presented — it did not decide. Enacted: two halves land with the human share in terracotta, three verb chips arrive in sequence, and a fourth chip, `decide`, lands and is **struck through on screen**. The claim is performed, not asserted. |
| B02 | SHOW | Claim: 5,806 holdings, every one decided, none dropped. One full-width bar draws, splits 4,537 / 1,269, and the terracotta segment then fans into the four reasons it stopped. The split is the argument. |
| B03 | SHOW | Claim: 42 cards are only 8 questions. Two counters resolve, then X.AI's 24 REAL filed strings scroll — the repetition does the work. Rows sharing an issuer name light with their security titles beneath. |
| B04 | SHOW | Claim: keying on the company rather than the string is what makes the queue shrink. 24 question marks fan out and dim, collapse into one card carrying the company and its verdict, 24 ticks fill from that single answer, and a 25th card arrives already ticked. |
| B05 | SHOW | Claim: a paused question survives the process exiting. Five graph nodes draw, the third halts and takes the accent, an arrow drops into a Postgres cylinder, then process A greys out and process B reads the same store. The two processes are visibly separate with only the store between them. |
| B06 | SHOW | Claim: the queue came back whole. 42 marks are counted into a block, the frame cuts on the outage, and the identical block is counted back to 42. The number is *shown* to be the same, not asserted to be. |
| B07 | SHOW | Claim: it is a split, not a crash. Two filed rows land, the two identical dollar values are bracketed to the cent, and the naive −90% reading is struck through. |
| B08 | SHOW | Claim: one trigger, three causes. Three step glyphs land in a row, each labelled with its own magnitude (×10, ×10, ×4.0); each then reveals its own evidence, and only the first keeps the accent. The corrected split count is a footnote **inside the frame**. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space ✓ — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B04's
  dimmed question-mark grid at 0.50 and B05's exited process A at 0.45
- Comparisons shown side-by-side, held ≥2s ✓ — B01's two halves, B02's two bar segments,
  B04's wrong-key/right-key pair, B05's two processes, B06's before/after blocks, B07's two
  filed rows and B08's three cases all persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓      B01/B02 — what the queue is for and how the work divides, stated before any
                 mechanism, including the verb the software never performs
WORKED EXAMPLE ✓ B03/B04 — one company, its 24 real filed spellings, and exactly what keying
                 the answer on the company instead of the string buys
FALSIFIABILITY ✓ B06 names its own limit: one unplanned outage is not a durability guarantee,
                 and it was run by accident rather than designed;
                 B08 publishes the corrected count — an earlier write-up said four split
                 questions and "wrong three times out of four"; it is three and two-of-three.
                 The script's "a price falling by exactly ten" is also dropped — two steps
                 are ×10, Anthropic's is ×4.0, and the frame labels each
SCAFFOLDED TASK ✓ B10 — find where your own pipeline gives up and asks you something, then
                 test it against two questions: what is the answer keyed on, and would the
                 question survive the process dying
BOOKENDS ✓       B00 cold open · B01 BLUF · B09 verdict · B10 handoff · B11 outro
NO-SOURCE-NO-VERDICT ✓ every figure is a prop injected by build_beat_sheet.py from
                 figdata_week6.json; the injection ASSERTS the 5,806/4,537/1,269 split, the
                 42-cards-to-8-questions collapse, the 45 recorded decisions, the 24 X.AI
                 spellings and their 278 holdings, the THREE split questions (not four),
                 Perplexity's ×10 shares at an unchanged value to the cent, SpaceX's two
                 asset categories on the same day, and the 28-holding canary — and fails
                 the build otherwise
```

**0 violations.** Three authoring judgment calls are logged in `BUILD-LOG.md` rather than
passed silently: the six script sections split into eight body beats, the trimmed second
opening paragraph (which the script itself nominates as the first cut), and moving the five
source figures into `pantry/`.

## What this cut is asked NOT to do, and does not

The script's Notes and the README's "one thing not to get wrong" carry five prohibitions.
Each is checked here because they are the kind of thing a rebuild quietly loses:

| The source says | This cut |
|---|---|
| **The AI decided nothing** — it routed, grouped, presented | B01 is built entirely around this: the three verbs are chips, and `decide` is a fourth chip struck through on screen. B09 line 5 repeats it with the 45-decision rule. |
| Do not say the matcher is now finished | Nowhere. B01 and B02 frame 78/22 as the design working; the words "finished", "solved" and "done" do not appear. |
| Say "X dot A-I", not "ex ay eye"; "ten-for-one split", not "ten to one" | B03 and B07 narration use exactly those spoken forms. |
| Say the Perplexity numbers slowly, and to the cent | B07 speaks both share counts in full and the screen carries `$4,228,993.75`; the beat is 54 words for 15.3s, the slowest per-word pace in the reel. |
| The strongest beat is the crash | B06 is its own beat rather than a clause inside B05, and it says out loud that the test was an accident — and that one accident is not a guarantee. |
