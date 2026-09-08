# PEDAGOGY GATE — How Do You Actually Know It Worked?

## Narration Review

**Topic:** The three real mechanisms this project uses to check an agent's
own reasoning against something outside itself — claim extraction,
citation verification, and consistency probing — and exactly what each one
can't prove.
**Register:** Investigative / forensic (narrated by Divij Pawar)
**Audience:** High-school technicality, per the source script's own header
**Series:** STEM — Accountability, 1 of 5 (siblings scripted in
`youtube/STEM6`-`STEM9`: when two agents disagree, memory vs. pretending to
remember, grading the machine, and the agent that was told what to do).
This series follows directly from `STEM1`-`STEM4` ("Agents"): B00 opens on
"last time, we ended on an uncomfortable fact" — the STEM4/STEM2 thread
about an agent that can look stuck-but-successful — and B12 closes by
teasing the next problem (multi-agent disagreement), which is already
scripted as `youtube/STEM6/06_when_two_agents_disagree.md`.

### Source & Adaptation

Narration is condensed from `05_how_do_you_know_it_worked.md`, split into
13 beats rather than the source's 7 prose sections, because two of those
sections (verification, consistency probing) and one falsifiability
section each contain enough independently-checkable content to need two
beats apiece — see CHECKS-REPORT.md "Beat-count deviation" for the full
reasoning per beat.

**What was added, because the source script has no bookends and its
mechanism paragraphs are otherwise abstract:**

- **B00 (cold open)** — condenses the source's opening paragraph; the
  composer props are new.
- **One constructed worked example** ("Revenue grew 34% YoY, driven by
  international expansion — source: 10-K") threads through B02-B06 so the
  three mechanisms are demonstrated on one continuous thread instead of
  three disconnected illustrations. Declared illustrative in SOURCES.md,
  matching the precedent STEM2 set for its own constructed "twelve-attempt
  deploy" trace.
- **B04's pooling caveat** — a real, previously-unstated precision gap in
  `verification.py` (global number-pooling, not per-citation scoping),
  found by reading the live source per `youtube/CLAUDE.md` §4's
  DOUBLE-CHECK LAW, not present in the source script. Logged in SOURCES.md
  with exact line references.
- **B11 (your turn)** — a new, concrete 3-step task (tag a real trace by
  hand, check one citation, probe with a second run) built from the
  source's closing paragraphs, which pose the idea rhetorically but don't
  give a runnable scaffold.
- **B10 (verdict)** and **B09 (the framework)** both carry the same
  three-rule recap in two registers (Manim body beat + Remotion verdict
  card) — mirrors STEM2's structure exactly.

Nothing from the source's substantive content was cut; the mechanism
descriptions, the tri-state verification outcomes, the consistency scoring
weights, and the closing tease all survive intact.

### Teaching Arc ✓

- **B00 (Cold open):** Picks up the "stuck-looks-like-succeeded" thread
  from the prior series and poses today's question
- **B01 (Framework/BLUF):** The reasoning-vs-narration gap stated as a
  thesis, before any mechanism; three mechanisms previewed as named, empty
  panels
- **B02 (Mechanism 1):** Claim extraction — prose mechanically sorted into
  four typed claims
- **B03 (Mechanism 2a):** Verification — a citation actually leaves the
  model and gets checked against a real, independently fetched source
- **B04 (Mechanism 2b):** The verification rollup — one rate a reviewer
  can act on, plus the honest caveat about how that rate is actually
  computed
- **B05 (Mechanism 3a):** Consistency probing — the same query, asked
  twice, independently
- **B06 (Mechanism 3b):** Classify and flag — the worked example agreeing,
  then deliberately diverging against a fabricated number
- **B07 (Falsifiability i):** PROOF struck through, replaced with EVIDENCE
- **B08 (Falsifiability ii):** What these mechanisms can catch, set against
  what they can never certify
- **B09 (The framework):** Three transferable, numbered rules
- **B10 (Verdict):** Condensed recap card
- **B11 (Your turn):** A concrete, ordered 3-step audit task
- **B12 (Outro):** Title restate, handle, bridge to STEM6

**EXECUTIVE-SUMMARY LAW:** satisfied at B01 — the three mechanisms are
named as a set and the whole episode's thesis is stated before mechanism 1
is described.

**FRAMEWORK-BEFORE-EXAMPLES:** B01 puts three ghost panels on screen named
but empty; B02-B06 fill them one at a time (with a persistent legend
tracking which is active); B09 replays all three, collapsed into
transferable rules.

### Factual Check ✓

See SOURCES.md for the full line-referenced table against
`claims.py`/`verification.py`/`consistency.py`. Summary:

| Claim | Verdict |
|---|---|
| Four claim types (citation/quantitative/hedge/causal), extracted by regex | ✓ exact match to `claims.py` |
| Citations verified via real HTTP fetch, EDGAR structured data or generic text search, ~1% tolerance | ✓ exact match to `verification.py`, including the quoted `_close_enough(a, b, tol=0.01)` code line |
| Three-way outcome: confirmed / not found / unattainable | ✓ exact match to `verify_claims()`'s `True`/`False`/`None` |
| Verification-rate rollup pools numbers globally, not per-citation | ✓ **new finding**, verified directly against `verification.py:160-183` |
| Consistency scoring: word overlap × 0.4, number overlap × 0.6 | ✓ exact match to `consistency.py:123` |
| HIGH/MEDIUM/LOW thresholds at 0.70/0.40 | ✓ exact match to `consistency.py:127-132` |
| Hard number-divergence flag | ✓ exact match to `consistency.py`'s `number_divergence_flag` |
| "34% YoY... 10-K" worked example; "41%" divergent run | ⚠ **declared illustrative** — not a logged trace |
| "0.82" / "0.21" / "67%" example scores | ⚠ **illustrative but carried from the source script's own `[VISUAL]` directions**, not newly invented |

No model names, vendors, versions, or benchmark figures appear anywhere.
The reel should not date, aside from the code line references above, which
should be re-verified if the cited files change before building.

### Register & Tone ✓

- Mechanism first, judgment second, exactly as the source script's header
  promises ("investigative, evidence-procedural, forensic"): each
  mechanism is shown doing its actual work before being judged for what it
  can't prove.
- B07/B08 refuse the easy ending — the reel explicitly stress-tests its
  own subject's tools rather than presenting them as solved.
- B04's caveat is the strongest tone marker: an episode about "no source,
  no verdict" would be self-refuting if it hid a real gap in its own
  verification code, so it doesn't.
- Narration budget: body beats (B01-B09) run roughly 90-155 words each,
  consistent with the sibling series' established body-beat length
  (STEM2's B02-B07 ran 103-148 words).

### Falsifiability ✓

**B07+B08** are the dedicated stress-test beats and they stress-test the
reel's *own* subject: PROOF is visibly struck and replaced with EVIDENCE,
then a two-column card states plainly what these mechanisms can never
prove (correct causal reasoning, sound judgment) beside what they're
actually strong at (fabrication, drift, absent evidence). **B04** adds a
second, code-level falsifiability moment mid-mechanism: the verification
rollup's own honest limitation (global number pooling), which is not in
the source script and was only found by reading the live implementation.
This is why the framework in B09/B10 concludes "check what can be
checked... log honestly when something can't be" rather than presenting
verification as airtight.

### Known deviations from house defaults

1. **Beat count.** 13 beats (B00-B12), not the ai-explainer default of 10.
   See CHECKS-REPORT.md "Beat-count deviation" for the per-beat
   justification. **Flagged for the human reviewer** — this is a
   structural choice, not an oversight.
2. **Runtime.** The source script header says "~9 minutes." Against a
   rough per-beat word-count estimate (not yet measured by real Kokoro
   output — see BUILD-PROMPT.md Step 2/3), this narration is likely to run
   **shorter than 9 minutes**, matching the pattern already seen on STEM2
   (source said ~9 min there too; Kokoro measured ≈5.1 min). **The actual
   number is unknown until Step 2 runs — flagged here so the human
   reviewer isn't surprised by the gap, not resolved by inventing content
   to close it.**
3. **Body-beat length.** Several body beats (B02: est. 63s, B03: est. 52s)
   run past the 14-22s range in `agents.md`'s default table, matching the
   established pattern in this series (STEM2's body beats ran 32-46s).
4. **One worked example threads five consecutive beats (B02-B06)** rather
   than each mechanism getting an independent illustration. This is a
   deliberate WORKED-EXAMPLE strengthening (see CHECKS-REPORT.md), not a
   simplification of content.

---

## VERDICT: PASS

**Prepared by:** Claude (beat-sheet authoring pass)
**Approved by:** Divij Pawar 
**Date:** 08/28/2026

**What a human reviewer should check before flipping this to PASS:**

1. **The beat-count deviation (13, not 10)** — confirm the per-beat
   splitting in CHECKS-REPORT.md is worth the added Manim scene count
   (9 scenes to build/render/QC instead of 6), or decide to consolidate
   before Step 2 spends any time.
2. **The constructed worked example** ("34% YoY... source: 10-K") — confirm
   it's acceptable as a declared-illustrative teaching device (per the
   STEM2 precedent) rather than something that should be replaced with an
   real anonymized trace from this project's own test suite, if one
   exists and is presentable on screen.
3. **The B04 pooling caveat** — this is the one piece of narration in this
   reel that wasn't in the original script; confirm the finding is stated
   accurately and isn't overstated as a "bug" when it may be an
   intentional design tradeoff in `verification.py` (the SOURCES.md entry
   states it neutrally as "a real gap," not a defect — confirm that's the
   right framing).
4. **The runtime gap** — once Step 2 (Kokoro) runs, compare actual runtime
   to the source's "~9 min" header and decide whether that's acceptable
   (as it was for STEM2) or whether beats need lengthening.
5. **The retint** (no literal green/red per the source's `[VISUAL]`
   directions) — confirm ink/terracotta substitution reads clearly in
   B06's agree/diverge pair and B03's tri-state outcome chips once
   actually rendered.

Once satisfied, replace this line with `VERDICT: PASS`, sign, and date it.
**No audio generation (Step 2 of BUILD-PROMPT.md) may run until this line
reads PASS** — this is GATE P, per `youtube/CLAUDE.md` §4 and
`brutalist.art/CLAUDE.md` rule 3.
