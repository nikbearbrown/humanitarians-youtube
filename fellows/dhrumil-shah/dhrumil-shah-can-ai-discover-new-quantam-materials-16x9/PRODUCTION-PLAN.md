# PRODUCTION PLAN — 10-scene visual and evidence map

The film is framework-first: the reusable rubric is on screen at 00:26, ahead
of every example. Each scene below names what is asserted, what is shown at the
moment of assertion, and which source tag carries it.

---

## 01 · Executive summary — 00:00–00:12

**Asserts:** AI does not discover superconductors; it reorders the search queue.
**Shows:** the title, the answer in an accent card, and the five-stage pipeline
the film will walk (Search → Rank → Synthesize → Measure → Confirm) with the
final stage accented.
**Source tag:** presenter thesis; the pipeline is this film's review structure.
**Why first:** the conclusion is stated before the argument so the viewer knows
what is being defended and can disagree early.

## 02 · The problem and the review frame — 00:12–00:35

**Asserts:** Tc is a measured quantity with a documented century-long record;
and here are the five questions every later claim will be held to.
**Shows:** a Tc definition card, the measured critical-temperature scatter
(1911–2019) with high-pressure records in accent and their pressures stated,
then the five CLAIM cards.
**Source tag:** Kamerlingh Onnes 1911; BCS 1957; published measured Tc record;
CLAIM is the presenter's framework.
**Gate:** this is the framework-before-examples beat. Nothing in the film is
scored before this lands.

## 03 · What enters the model — 00:35–01:00

**Asserts:** the standard public training table is 21,263 measured
superconductors with 81 composition-derived features — and no structural inputs.
**Shows:** the full Hamidieh 2018 citation, a 2x2 stat block, then the feature
families beside an accented NOT-IN-THE-TABLE column.
**Source tag:** Hamidieh 2018, Computational Materials Science 154:346–354; UCI
Superconductivty Data; NIMS SuperCon.
**Why it matters:** the exclusion column is the load-bearing fact of the film.

## 04 · The method and what it learned — 01:00–01:15

**Asserts:** a gradient-boosted model reaches roughly ±9.5 K out-of-sample —
and that number describes interpolation over known chemistry.
**Shows:** the metric at 190 px with its model and split beside it, then an
accented reframe card.
**Source tag:** Hamidieh 2018 §4, reported out-of-sample performance.
**Open item:** the ±9.5 K figure is flagged VERIFY in `FACTCHECK.md`.

## 05 · The screening funnel — 01:15–01:34

**Asserts:** ranking plus filtering collapses a candidate space to a shortlist.
**Shows:** five proportional bars collapsing, then an accented disclosure that
the schematic is illustrative and no campaign was run.
**Source tag:** ILLUSTRATIVE SCREENING SCHEMATIC.
**Known weakness:** this scene would be far stronger with a real, cited
campaign. Two prepared slots exist in `FACTCHECK.md`.

## 06 · The limit that matters most — 01:34–01:51

**Asserts:** the field's real jumps came from outside the known distribution,
which is exactly where a trained model is weakest.
**Shows:** inside-versus-outside columns, then the 1986 cuprate and 2008
pnictide discoveries with dates and discoverers.
**Source tag:** Bednorz & Müller 1986; Kamihara et al. 2008; presenter
interpretation.

## 07 · What actually confirms a superconductor — 01:51–02:10

**Asserts:** confirmation is a five-link chain and AI touches one link.
**Shows:** the chain with only the first link accented, a divider labelling the
remaining four as physical and human-owned, then the rule that zero resistance
alone is insufficient without field expulsion.
**Source tag:** standard experimental practice; Meissner & Ochsenfeld 1933.

## 08 · The case that tests the rubric — 02:10–02:33

**Asserts:** LK-99 was claimed as a room-temperature ambient-pressure
superconductor in July 2023, and it failed.
**Shows:** two columns — WHAT WAS CLAIMED and WHAT REPLICATION FOUND — entering
at 02:10 and 02:22 and **both held together until 02:33**, 11.2 seconds of
side-by-side.
**Source tag:** Lee, Kim et al., arXiv July 2023; independent replication
reports, Aug–Sep 2023.
**Why this case:** it is the falsifiability test. A rubric that cannot catch
LK-99 is decoration.

## 09 · Scoring the case — 02:33–02:46

**Asserts:** the verdict lives in the last two axes, and those are the two no
model produces.
**Shows:** the five CLAIM rows scored against LK-99 with per-row justification
and solid FAILED chips on I and M.
**Source tag:** presenter framework applied to the published replication record.

## 10 · Your turn and close — 02:46–03:00

**Asserts:** the viewer can run this on any headline.
**Shows:** the five-row scaffold with a decision rule — if I or M is
unresolved, record "candidate", not "discovery" — then the title close and a
held disclaimer.
**Source tag:** presenter CLAIM scaffold, reusable on any AI-materials claim.

---

## Production order actually followed

1. Beat sheet authored with unique beat IDs and shot intent.
2. Narration generated locally with Kokoro; durations measured.
3. Composition built against the measured durations — no hand timing.
4. Preflight still rendered and **inspected**; a chart legibility defect was
   found and fixed before the master render.
5. Master rendered at 4K, verified against the technical contract.
6. Eleven QC stills extracted and inspected.
7. PROOF review written against the rendered master, not against the plan.
