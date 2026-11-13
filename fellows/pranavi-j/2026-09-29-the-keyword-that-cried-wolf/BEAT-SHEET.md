# Beat Sheet (APPROVED — Gate P, 2026-09-29): "The Keyword That Cried Wolf"

**Creator:** Sai Pranavi J. | Weekly work report
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Phase:** 2 — approved for narration lock / audio generation. B06 gets a small "not reviewed —
below alert threshold" label for clarity; B07 kept at full weight. See `FACTCHECK.md`.

---

## Premise

**What this covers:** a real, named noise problem the pipeline's own `FINDINGS.md` had flagged and
deliberately left unfixed as a future baseline — the keyword scorer marks items "Critical" purely
because their title contains a trigger word, with no understanding of context. Two real,
previously-measured examples: a routine Medicare payment rule scored 10/Critical because its title
mentions "Emergency Medical Treatment and Labor Act" (a law's proper name, not an actual
emergency), and a cluster of boilerplate Nasdaq procedural filings scored 9/Critical because they're
titled "Notice of Filing and Immediate Effectiveness." This video covers building and verifying a
second-pass fix: a local LLM (Ollama) review that catches exactly these two patterns without
touching a single line of the original keyword scorer, and fails open if the LLM step itself
breaks.

**What this deliberately leaves out:** this is not a full labeled-benchmark evaluation of the
scorer (the pipeline's own roadmap named that as a separate, still-unbuilt step). It's a targeted
fix for the two specific patterns already named and measured in `FINDINGS.md`, verified against
those two real cases plus one genuine true positive — not a general claim about all possible
misfires.

**Source status:** Real engineering work. Every claim traces to
`/Users/pranavijs/mycroft/scripts/regulatory-intel/C2-VERIFICATION.md` (2026-09-29) and the
matching `logs/RUN_LOG.md` entry, plus the original `FINDINGS.md` (2026-07-24) for the two named
patterns. See `SOURCES.md` for the full claim → source mapping.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated |
| B03 Setup | The scoring rule that adds +3 for "immediate"/"emergency", quoted verbatim | Legible before any example shown |
| B04 Discovery | Both real titles (Medicare, Nasdaq) shown with the trigger word highlighted in context | The word alone vs. the word in its real, harmless context |
| B05 Design | The review flow: item → Ollama prompt → confirm/downgrade verdict, shown as a diagram | Fail-open path shown explicitly, not just the happy path |
| B06 Proof | Live verdicts for all 3 test cases (2 false positives, 1 true positive) shown together | All 3 outcomes visible at once, not sequential reveals that hide the comparison |
| B07 Honest limits | The 3 named limitations (conservative correction, small sample, added latency) | Not glossed over |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The Keyword That Cried Wolf" + @HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:22)**
VO: "Hi, I'm Sai Pranavi J.. This video is about a keyword scorer that was crying wolf —
marking routine filings as Critical because of one word in the title — and a second-opinion pass,
running locally, that catches it."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:22–0:38)**
VO: "Two real items landed in this pipeline's Critical bucket last month. One was a routine
Medicare payment rule. The other was a boilerplate filing about cabinet wiring at Nasdaq. Neither
one was actually urgent."
Visual: two title cards side by side, each stamped "10/CRITICAL" and "9/CRITICAL."

**B03. Setup (~0:38–1:00)**
VO: "Here's why. The scorer reads the full text and adds three points the moment it sees the word
'immediate' or 'emergency' — anywhere in the title, no matter what it's actually attached to."
Visual: the real scoring rule, quoted verbatim:
`if (text.includes('immediate') || text.includes('emergency')) score += 3;`
*[Source: C2-VERIFICATION.md "The problem", quoting the scorer's own code]*

**B04. Discovery (~1:00–1:28)**
VO: "Look at where that word actually shows up. The Medicare rule's 'emergency' comes from
'Emergency Medical Treatment and Labor Act' — a law's full legal name. The Nasdaq filing's
'immediate' comes from 'Notice of Filing and Immediate Effectiveness' — standard boilerplate every
routine rule change uses. The scorer can't see the difference between a real emergency and a law's
title."
Visual: both real titles, the trigger word highlighted in place, with a caption showing what it's
actually part of.
*[Source: C2-VERIFICATION.md "The problem"; real titles from live DB rows id 4 and id 966/967]*

**B05. The fix — a second opinion, not a rewrite (~1:28–1:58)**
VO: "The fix doesn't touch the original scorer at all. Every item that would trigger an alert gets
a second look — a small model running locally on this machine reads the title and asks: is this
actually urgent, or is that just an incidental word? If it says the alert would be noise, that one
item gets held back. If the model itself fails for any reason, nothing breaks — the item just goes
through exactly as it would have before this check ever existed."
Visual: flow diagram — item -> local model review -> confirm (goes through) or downgrade (held
back); a third branch labeled "model fails -> goes through anyway (fail-open)."
*[Source: C2-VERIFICATION.md "The design"]*

**B06. Proof (~1:58–2:26)**
VO: "I tested it against exactly those two cases, plus a real enforcement case, an actual SEC
insider-trading charge, to make sure it doesn't just downgrade everything. Both routine filings:
flagged as noise. The real enforcement case: left alone, exactly as it should be."
Visual: a 3-row results table — Medicare (downgrade), Nasdaq (downgrade), SEC insider-trading case
(untouched, small label: "not reviewed — below alert threshold") — all 3 visible together.
*[Source: C2-VERIFICATION.md "Live verification" table. Label added per FACTCHECK.md item #1 —
resolved: the SEC case was never sent to the model, not reviewed-and-approved.]*

**B07. Honest limits (~2:26–2:50)**
VO: "Three things this doesn't claim. The correction is cautious — it moves these off 'Critical,'
not all the way down to where a person might put them. It's tested against two known patterns, not
a full benchmark. And it adds real time — reviewing everything above the alert line could add
several minutes to a single run."
Visual: 3 limitation cards, stated plainly, not minimized.
*[Source: C2-VERIFICATION.md "What's honest and NOT overclaimed here"]*

**B08. Sign-off (~2:50–2:56)**
VO: "Fixed with Claude Code, verified against two real false alarms and one real true one."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] B03's scoring rule quoted verbatim, not paraphrased
- [ ] B04's two real titles shown with the trigger word in its actual context
- [ ] B05 explicitly shows the fail-open branch, not just the happy path
- [ ] B06 shows all 3 outcomes together, including the true positive that was correctly left alone
- [ ] B07 states real limitations, not softened into non-issues
- [ ] Silent title card present; brand/fellow sign-off card present

**Estimated runtime:** ~2:56 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — not yet run, pending this beat sheet's approval).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-09-29. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
