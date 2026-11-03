# Beat Sheet (APPROVED — Gate P, 2026-10-27): "The Correction That Never Reached The Email"

**Creator:** Sai Pranavi J. | Weekly work video
**Format:** `work-report`, same register as this fellow's prior Project 29 reports
**Phase:** 2 — approved for narration lock / audio generation.

---

## Premise

**What this covers:** a real bug found and fixed this week (C3) in Project 29's regulatory
intelligence pipeline (`mycroft`), `scripts/regulatory-intel/workflow.dev.json`'s `Generate Email`
node. `Layer 2 - LLM Re-Score` (added in C2) reviews any item with `urgency_score > 6` and writes
back `llm_reviewed`, `llm_verdict`, `llm_corrected_impact_level`, and `llm_downgrade` — the whole
point being that the LLM can correct a keyword-scorer severity that's wrong (e.g. downgrade a
"Critical"-flagged item, or recategorize it to "High" without rejecting it outright). But
`Generate Email` — the node that actually buckets items into the Critical/High sections of the
alert email and counts them — never read `llm_corrected_impact_level` anywhere; it only used the
original keyword-based `impact_level`. An item the LLM confirmed as real but recategorized (e.g.
Critical -> High) still passed `High Priority Filter` (which only gates on the binary
`llm_downgrade` flag) and then landed back in the email under its stale, pre-LLM label. The
correction was computed, written to the item's JSON, and never looked at again — since the day
the Layer 2 LLM step shipped (C2).

**The fix:** `Generate Email` now computes an effective severity — `effectiveImpact()` — that
prefers the LLM's correction when the item was reviewed and a correction exists, falling back to
the keyword scorer's original label otherwise. `criticalItems`/`highItems` now filter on
`effectiveImpact(i)`, not the raw `impact_level` field. Items never sent to the LLM (below the
`urgency_score > 6` review threshold) are unaffected.

**Continuity note:** this is the third fix in this same `Generate Email` node this cycle (after
B5's under-reported sources and B6's dropped-on-exactly-1-item bug), and the second bug
specifically in the Layer 2 LLM pipeline C2 introduced. It means the LLM review step's own stated
purpose — correcting severity, not just confirming/rejecting — had never actually worked for any
item reaching this node, since C2 shipped.

**What this deliberately avoids:** no claim that this ever caused a human operator to act on a
wrong severity in a real incident — this closes a defect confirmed by this session's own live
harness against a 3-item synthetic batch reflecting the 3 real cases this node sees, not a claim
about how many real historical emails were affected (that count isn't measured or shown). A
separate, unrelated defect found the same week (dashboard `get_stats()` re-bucketing by raw
`urgency_score`) is flagged as an open issue, not fixed this week — kept at full weight, not rolled
into this video's claim of what was fixed.

**Source status:** real Project 29 (`mycroft`) engineering fix, closed 2026-10-27
(`scripts/regulatory-intel/workflow.dev.json`, `Generate Email` node; see `RUN_LOG.md`'s
2026-10-27 entry and `C3-VERIFICATION.md`). Verified live this session via a Node.js `vm` harness
running the real, extracted `jsCode` from the real file on disk — not a rewritten copy — against a
3-item batch matching every real case. See `SOURCES.md` and `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Setup | The real fields `Layer 2 - LLM Re-Score` writes, verbatim, next to the real pre-fix bucketing lines from `Generate Email` | Verbatim from `workflow.dev.json`, not paraphrased |
| B04 Discovery/fix | The real diff: `effectiveImpact()` added, matches `C3-VERIFICATION.md`'s "The fix" exactly | Real diff, not illustrative |
| B05 Verification | The real before/after table from this session's own live Node.js harness | Real measured results, not illustrative |
| B06 Honest limits | What this fix does NOT touch, plus a separate open issue found but not fixed this week | Full weight, no softening |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The Correction That Never Reached The Email" + @HumanitariansAI. No
narration.

**B01. Exec summary (~0:04–0:21)**
VO: "Hi, I'm Sai Pranavi J. This video is about a severity correction an LLM review step computes
and writes down, that the email generator downstream never actually reads, so a corrected label
keeps shipping under its old, wrong value, every single time."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:21–0:41)**
VO: "Our pipeline added a second opinion. An LLM reviews every high-urgency alert and can correct a
wrong severity label, downgrade a false Critical to High, without rejecting the item outright. But
the node that actually counts and buckets items for the alert email never learned to read that
correction."
Visual: two labels side by side — what the LLM corrected the severity to, versus what the email
actually showed — visually flagged as a mismatch.

**B03. Setup (~0:41–1:08)**
VO: "Here's the real code. Layer 2, the LLM re-score step, writes back four fields on every item it
reviews: llm reviewed, llm verdict, llm corrected impact level, llm downgrade. The whole point is
it can correct a label, not just reject an item. But Generate Email, the node that buckets Critical
and High for the alert, only ever reads impact level, the original keyword score. The correction is
computed, written, and never looked at again."
Visual: the real fields Layer 2 writes back, shown verbatim, next to the real two-line bucketing
from `Generate Email` that reads only the original `impact_level`.

**B04. Discovery and fix (~1:08–1:28)**
VO: "The fix adds one helper: effective impact. It prefers the LLM's correction when the item was
reviewed and a correction exists, and falls back to the original label otherwise. Critical and High
now filter on that, not the raw field. An item the LLM never touched behaves exactly as it did
before."
Visual: the real diff from the `Generate Email` node: the old two-line bucketing struck through,
the new `effectiveImpact` helper and its two filter lines added.

**B05. Verification (~1:28–1:57)**
VO: "I extracted the real, patched code from Generate Email and ran it in a live Node harness
against three items covering every real case: confirmed and recategorized, confirmed with no
change, and never reviewed. Before the fix: two Critical, one High. The recategorized item still
counted Critical. After the fix: one Critical, two High. That same item now counts correctly. The
other two are unchanged, no regression. Ran it again against the real patched file on disk, same
result."
Visual: the real before/after table from this session's live Node.js harness run (per-item bucket,
plus `critical_count`/`high_count` totals, before and after).

**B06. Honest limits (~1:57–2:27)**
VO: "Two honest limits. First: this only changes Generate Email's bucketing. Layer 2's own review
logic, the High Priority Filter's downgrade gate, and the two earlier fixes already closed in this
same node are all untouched. Second, a separate defect turned up the same week in the dashboard's
own stats endpoint. It re-buckets by raw urgency score with cutoffs that disagree with impact
level, affecting fifty seven of four hundred eleven real rows. Not fixed this week, flagged for
later."
Visual: 2 honest-limit cards, side by side, full weight, no softening language.

**B07. Takeaway (~2:27–2:38)**
VO: "A correction that's computed but never read isn't a correction. If a review step is allowed to
change a label, every downstream consumer of that label has to actually check whether it did."
Visual: statement card.

**B08. Sign-off (~2:38–2:40)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] B03's field names and pre-fix bucketing lines shown verbatim, match the real
      `workflow.dev.json`
- [ ] B04's diff matches the real committed fix exactly (per `C3-VERIFICATION.md`)
- [ ] B05's table uses real measured harness results from this session, not illustrative numbers
- [ ] B06's honest limits kept at full weight, not softened; the separate open issue (dashboard
      stats) is clearly flagged as NOT fixed this week
- [ ] Silent title card present; brand/fellow sign-off card present
- [ ] No claim that this bug was observed to mislead a real human operator in a real incident

**Estimated runtime:** ~2:40 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — measured total 159.61s, see `SHOTLIST.md`).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-10-27. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
