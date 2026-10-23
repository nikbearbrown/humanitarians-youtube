# Frictional log — 2026-08-22

**Week 4 · entity resolution · A 322-string golden set, and a matcher measured against it**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to
`docs/entity_resolution.md`, `tests/fixtures/golden_set_v1.json` or `docs/worklog.md`.

*(There is no week 3 episode. Week 3's deterministic half was built inside this week because
week 4's deliverable needs a matcher to measure; week 3's other half — the live EDGAR path —
is still not done, and is stated as such in §8 rather than quietly folded in.)*

---

## What I was working on

The hard problem underneath everything else: **the same company is filed under dozens of
different names, and nothing in the filing tells you they are the same company.**

Databricks appears under 51 spellings. X.AI reaches the pipeline under 24. If the matcher is
wrong, every price series downstream is wrong in a way no amount of careful arithmetic will
catch. So this week built a labelled answer key — 322 issuer strings covering 7,276 holdings —
and measured the matcher against it honestly.

## What I tried, and what I expected

I built the matcher as a cascade: LEI exact match → aliasx table → SPV wrapper parse → gated
fuzzy score, using `rapidfuzz`. I expected the fuzzy scorer to do most of the work and the
threshold to be a tuning exercise.

I also expected the golden set to *validate* the matcher.

## Where it resisted, and what I did next

**`token_set_ratio` cannot be the thing that decides, and I measured that rather than
suspecting it.** It scores `FIGURE` vs `FIGURE AI` at 100, `ANDURIL ENGINEERING` vs `ANDURIL`
at 100 — and `OPEN BAY AUTOS AI` vs `OPEN AI` at 100. Two right, one catastrophically wrong,
all at the very top of the range. There is no threshold that separates them, because they are
the same score.

I tried IDF weighting first, on the theory that distinctive tokens should count more. I
abandoned it on measurement: **79% of the corpus's normalised tokens are hapax** — they appear
exactly once — so IDF cannot tell distinctive from generic in this data. What replaced it is a
coverage gate evaluated *before* any score is computed.

**The threshold is a band, not a number, and I had to stop looking for the number.** The only
false positive — `OPEN BAY AUTOS AI INC.`, a used-car marketplace whose name happens to contain
the tokens OPEN and AI in that order — scores **0.80**. So do three *correct* blended SpaceX
SPVs. No cut-off separates them. The operating point is auto-accept ≥ 0.90, human review
0.80–0.90, reject below — which is the concrete argument for building a review queue, and the
band holds only 4 strings per full re-resolution, a bounded amount of human attention.

**Three findings came out of reading the corpus, not from the scores:**

1. **The `%X.AI%` pattern misses `XAI CORP` — 85 holdings, and Fidelity is X.AI's largest
   holder.** One literal dot. The largest single recall gap in the shipped pattern set.
2. **`Anthropics Technology Ltd., Series G` is Anthropic.** That is a real British software
   company's name, filed by BlackRock, priced at **259.13640004** on a period end where
   fourteen LEI-confirmed holdings price Anthropic Series G at **259.1364**. Ten significant
   figures of agreement. The filing's `INVESTMENT_COUNTRY` says `GB`, inherited from the wrong
   entity in somebody's security master.
3. **231 OpenAI holdings have a price that is not a share price.** `OPEN AI GLOBAL LLC
   CONVERTIBLE INTEREST RT PP` carries balance equal to value, so it prices at exactly $1.00 —
   a dollar commitment, not a share. OpenAI's range runs $1.00 to $769.43 and the bottom of it
   is an artefact. `price_basis` became a first-class label because of this.

**My sampling frame was not reproducible, which invalidates the fixture.** Rebuilt from
scratch it came out with 322 strings on one run and **323** on the next. Three causes, all
ordering:

- DuckDB's `DISTINCT` gives no ordering guarantee, so the 3.2M-name candidate list arrived in
  a different order each run.
- `process.extract` breaks equal scores by input position, so that order propagated into which
  equal-volume name was picked as a stratum representative.
- `price_evidence` iterated a **set** of company names, letting `PYTHONHASHSEED` decide which
  anchor got credited for a price coincidence.

Fixed with an explicit `ORDER BY`, a name tie-break and a sorted list. The frame now rebuilds
**byte-identically, sha256-verified across two runs**, and a test re-derives every label from
the committed frame. No metric moved — the varying string was a near-miss negative — but the
published figure was 323 until I found this.

**Two bugs in my own evidence pipeline, found before I trusted it.** Databricks term loans are
tagged `LON` with balance equal to value, so they price at exactly 1.00 — with those in the
price anchor, every unrelated issuer priced at 1.00 "confirmed" as Databricks. And one
Databricks row prices at **−0.005**, which made a ratio tolerance test pass for literally
anything, because the denominator was negative.

**Then the human review reversed one of my own labels.** I had labelled `OPENAIR.COM` as
`NOT_IN_UNIVERSE` on the stated ground that its price coincided with an OpenAI anchor "in
exactly one period". **That statement was false.** There are five holdings across *two* period
ends, all at **687.6869**, titled `OpenAir.com, Series C` — and 687.6869 is the OpenAI Series C
consensus, reported to the same four decimals by eight holdings across six registrants whose
identity is not in dispute.

The label is now `OpenAI Group PBC`. Because the original approval was obtained on a bad
statement of the evidence, I recorded it as **withdrawn** rather than carried over, and added a
test asserting the withdrawn name is not counted among the confirmed ones. An approval given on
wrong information is not an approval.

**A matcher defect fell out of that reversal.** De-dotting fuses a domain suffix into the stem:
`OPENAIR.COM` became the single token `OPENAIRCOM`, scoring 75 against the alias `OPENAI` and
getting rejected. So matcher v1 was *worse* than the frozen patterns on this row. Fixed by
stripping a dot-TLD (`.COM`, `.NET`, `.ORG`, `.IO`) **before** de-dotting — with `.AI`
deliberately excluded and required to stay excluded, because `X.AI` is a company's entire
identity and stripping it would undo the 85-holding recall fix that motivated de-dotting in
the first place.

## What Claude contributed, and what I did with it

Claude wrote the normaliser, the share-class grammar, the matcher cascade and 56 tests. It also
produced the first draft of the golden-set labelling procedure.

**Two of my own test assertions were wrong and the tests caught them.** I claimed
`token_set_ratio('RELATIVITY SPACE','SPACE EXPLORATION')` was 100; it is **66.67**, and the
docstring had to be corrected along with the test. I also asserted blocking would return zero
candidates for `PUBLIC JOINT STOCK COMPANY PHOSAGRO`; it returns two, on the trigram `GRO` it
shares with GROQ. That is blocking working correctly — it is recall-preserving and is
*supposed* to let that through for the scorer to reject.

**The two things I insisted on stating, against the grain of a good-looking result:**

First, **v1's recall of 1.0000 is not independent.** The fix that produced it was written
because this golden set exposed the miss. The golden set drove a real improvement, which is
what it is for — it did not validate that improvement and cannot. Claude's draft reported the
1.0000 as a clean headline. It is not clean.

Second, **on the hard subset the frozen patterns now have perfect precision and v1 does not.**
v1 claims `OPEN BAY AUTOS AI INC.` and the old patterns don't. v1's case is recall, not
precision, and there is a test asserting that ordering so it cannot quietly disappear from a
future write-up.

I also read both directions of the 426 share-class disagreements rather than assuming the
parser was right: 414 are filers tagging `Databricks, Inc., Series G` as common stock (my
grammar is right); **12 are Baron's X.AI `CLASS B`/`CLASS C` tagged preferred, where the filer
is probably right and my rule is a real approximation.** Left as-is because it changes no mark,
and recorded as owed work.

## What I understand now, and what I still do not

**Understood.** Name matching here is not a scoring problem with a threshold; it is a
structured problem where coverage has to be decided before similarity is computed. Price
agreement to four decimals across independent registrants is stronger identity evidence than
any string metric. Reproducibility of a *sampling frame* is as load-bearing as reproducibility
of a result — a fixture that rebuilds differently is not a fixture.

**Not understood, and left open.** **314 of 322 labels remain unattested** — I reviewed 10 and
confirmed 8, and nobody has looked at the rest. The fixture's `human_attestation` field records
exactly that scope, and a test asserts it rather than letting the set look fully blessed. The
206 unexplained price-consistency disagreements are still unexplained. The 16 `NPORT-P/A`
amendments are unadjudicated. And week 3's live EDGAR path, which I partly consumed to build
this week, is still not done.
