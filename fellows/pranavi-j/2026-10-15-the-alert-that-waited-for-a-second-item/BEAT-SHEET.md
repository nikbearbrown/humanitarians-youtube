# Beat Sheet (APPROVED — Gate P, 2026-10-15): "The Alert That Waited for a Second Item"

**Creator:** Sai Pranavi J. | Weekly work video
**Format:** `work-report`, same register as this fellow's prior Project 29 reports
**Phase:** 2 — approved for narration lock / audio generation.

---

## Premise

**What this covers:** a real bug found and fixed this week in Project 29's regulatory
intelligence pipeline (`mycroft`). The node that builds the real alert email (`Generate Email`)
gated on `newItems.length > 1` — strictly more than one qualifying item — before it would build an
email at all. A run with exactly **one** new high-priority/critical item fell into the empty
branch and silently produced no alert. The one scenario this alert path exists for — a single
urgent filing — could go completely unreported, with no error and no visible symptom.

**What this deliberately avoids:** no claim this ever actually happened in a live run (not
instrumented/logged at that granularity); framed honestly as "found and fixed before it could
cause real harm," not "this already caused a miss."

**Source status:** real Project 29 (`mycroft`) engineering fix, verified live this session against
the actual extracted node code (not a rewritten copy) via a Node.js harness, and re-verified
against the real patched file on disk. See `SOURCES.md` and `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Setup | The real buggy line of code, `newItems.length > 1`, highlighted | Verbatim from `workflow.dev.json`, not paraphrased |
| B04 Discovery/fix | Before/after diff of the one-character-class change | Real diff, matches `B6-VERIFICATION.md` |
| B05 Verification | The real before/after harness table (0/1/2 items) | Real measured results, not illustrative |
| B07 Honest limits | What this fix does NOT claim | Full weight, no softening |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The Alert That Waited for a Second Item" + @HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:22)**
VO: "Hi, I'm Sai Pranavi J.. This video is about a one-character bug in our regulatory
intelligence pipeline that meant a single urgent filing — the exact case our alert system exists
for — could silently generate no alert at all."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:22–0:38)**
VO: "Our alert email only fires when there's something urgent to report. This week, I found the
one case it was never built to handle: exactly one urgent item. Not zero. Not two. One."
Visual: a counter showing 0, 1 (highlighted/flagged), 2 — with 1 visually distinct from the other
two.

**B03. Setup (~0:38–1:04)**
VO: "Here's the real line, straight from the workflow. The alert node only builds an email if
there's more than one new high-priority item. `newItems.length` greater than 1. Greater than —
not greater than or equal. A single critical filing doesn't clear that bar."
Visual: the real verbatim line of code shown large, `newItems.length > 1`, with `1` visually
flagged.

**B04. Discovery and fix (~1:04–1:34)**
VO: "I traced where a failed check actually goes — it lands on an empty branch with nowhere to go.
No error, no log line, nothing a person would notice. Just an alert that never arrives. The fix is
one character: greater than one becomes greater than zero."
Visual: the before/after diff, `> 1` struck through, `> 0` added, with an arrow showing the failed
branch's dead end.

**B05. Verification (~1:34–2:04)**
VO: "Before trusting the fix, I ran the real extracted code — not a rewritten copy — against zero,
one, and two items, before and after. Zero stayed correctly silent. One went from silently
skipped to a real email. Two already worked, and still does. Then I re-ran it against the actual
patched file on disk, to confirm the real change behaves the same way."
Visual: the real 3-row before/after table (0/1/2 items), with the "1 item" row visually
highlighted as the one that changed.

**B06. Honest limits (~2:04–2:26)**
VO: "Two honest limits. First: this wasn't caught by a live incident, it was caught by re-reading
the code — I don't have evidence this specific case ever occurred on a real run. Second: while
tracing this, I found a related but separate compatibility gap — a downstream service's source
list doesn't yet account for a newer classification change — flagged for a future week, not fixed
yet."
Visual: 2 honest-limit cards, side by side, full weight, no softening language.

**B07. Takeaway (~2:26–2:40)**
VO: "An alert system is only as good as the cases it was actually built to handle. The scariest
bugs aren't the ones that crash — they're the ones that quietly do nothing at all."
Visual: statement card.

**B08. Sign-off (~2:40–2:45)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] B03's code line shown verbatim, matches the real pre-fix `workflow.dev.json`
- [ ] B04's diff matches the real fix exactly (`> 1` -> `> 0`)
- [ ] B05's table uses real measured harness results, not illustrative numbers
- [ ] B06's honest limits kept at full weight, not softened
- [ ] Silent title card present; brand/fellow sign-off card present
- [ ] No claim that this bug caused a real, observed miss on a live run

**Estimated runtime:** ~2:45 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — not yet run, pending this beat sheet's approval).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-10-15. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
