# Beat Sheet (APPROVED — Gate P, 2026-08-30): "The Check That Never Once Fired"

**Creator:** Sai Pranavi Jeedigunta | Weekly work report
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Phase:** 2 — approved for narration lock / audio generation. Both FACTCHECK items resolved
2026-08-30: the "today's live test" framing confirmed sufficient as written; confirmed no real
downstream incident is implied anywhere in the script. See `FACTCHECK.md`.

---

## Premise

**What this covers:** a second fix from this week's continued Layer 1 hardening pass on the same
pipeline as the two prior reports: the source classifier had a rule specifically written to catch
CFTC filings and route them to a `CFTC Regulations` label — and when tested against every live
CFTC item available today, it matched **zero of them**. Chosen because it's a clean, fully
measured before/after with a sharp general lesson: a rule that never fires isn't a safeguard, it's
dead code wearing a safeguard's name.

**What this deliberately leaves out:** the still-open 21 "Unknown Source" Google-News items (no
reliable classification signal exists there) and B3 (Google News link unwrapping) are candidates
for a future report, not this one.

**Source status:** Real engineering work. Every number below traces to
`/Users/pranavijs/mycroft/scripts/regulatory-intel/B2-VERIFICATION.md` (2026-08-30) and
`logs/RUN_LOG.md`'s 2026-08-30 B2 entry. See `SOURCES.md` for the full claim → source mapping.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated |
| B03 Setup | The classifier's CFTC-detection condition, quoted verbatim | Legible before any live data is shown |
| B04 Discovery | A real CFTC feed item's actual link + title side by side with the condition it's supposed to trip | Both visible together, not narrated only |
| B05 Proof | Live test result table: feed name, items tested, items reclassified | All 5 feed rows visible, not just the CFTC one |
| B06 Fix | Before/after `identifySource()` snippet, the `dc:creator` line highlighted | Full before AND after both visible |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi Jeedigunta |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The Check That Never Once Fired" + @HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:18)**
VO: "Hi, I'm Sai Pranavi Jeedigunta. This video is about a classifier in the same regulatory
pipeline I've been working on — a check specifically written to catch CFTC filings that,
tested against real data, never once matched — and the fix that reads the actual source instead
of guessing."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:18–0:28)**
VO: "This pipeline has a rule whose entire job is spotting CFTC filings. I tested it against
every real CFTC item I could pull live. It caught none of them."
Visual: the classifier's CFTC-detection condition on screen, a red "0 matches" stamp beside it.

**B03. Setup (~0:28–0:50)**
VO: "Every incoming filing gets labeled by source — SEC, FINRA, CFTC — so alerts and reports can
be filtered by regulator. For anything from the Federal Register, the rule was: check if the link
contains 'commodity-futures,' or the title says 'CFTC.' If neither, default to 'Securities.'"
Visual: the actual code condition, quoted verbatim, with the two checks highlighted.
*[Source: `B2-VERIFICATION.md` "The bug"]*

**B04. Discovery (~0:50–1:15)**
VO: "Here's a real CFTC filing, pulled live today: 'Swap Execution Facility Order Book
Requirement for Permitted Transactions.' No 'CFTC' in the title. And the link — Federal Register
permalinks never include the agency name at all. The rule was checking for something that
structurally can't appear."
Visual: the real title and link on screen, side by side with the condition from B03, both
highlighted phrases (the two things the rule looks for) shown as absent.
*[Source: `B2-VERIFICATION.md` "The bug", item 1 of the CFTC feed test]*

**B05. Proof (~1:15–1:40)**
VO: "So I tested it properly — pulled all five live feeds today and ran the classifier against
every item. Every single one of the twelve real CFTC filings came back mislabeled 'Securities.'
Eighty-three of the hundred forty-six items from the general securities search were actually
other agencies entirely — the FCC, the EEOC, the Department of Transportation — also called
'Securities.' And the three feeds that were already working — SEC, FINRA, Investment Advisor —
didn't change at all."
Visual: the results table on screen — five feed rows, items tested, items reclassified, with the
CFTC row (12/12) and the zero-regression rows highlighted.
*[Source: `B2-VERIFICATION.md` "Live verification (2026-08-30)" — full table there. NOTE for
FACTCHECK: this is a live test run today against feeds as they existed today, not a claim about
every run in the pipeline's history.]*

**B06. Fix (~1:40–2:00)**
VO: "The fix: stop guessing from the link and title. Every Federal Register item already carries
its real issuing agency in the feed data — it was being pulled in and thrown away. Now the
classifier reads it directly."
Visual: before/after `identifySource()` snippet, the new `dc:creator`-based check highlighted.
*[Source: `B2-VERIFICATION.md` "The fix"; commit `d59fbd5` in `mycroft`]*

**B07. Takeaway (~2:00–2:15)**
VO: "A safeguard that's never once tested against real input isn't protecting anything. It's just
code that looks like protection — until someone actually runs the data through it."
Visual: statement card.

**B08. Sign-off (~2:15–2:20)**
VO: "Fixed with Claude Code, verified against all five live feeds before it ever ran again in
production."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi Jeedigunta.

---

## Production Gate Self-Check (pre-review)

- [ ] B03's condition quoted verbatim, not paraphrased
- [ ] B04 shows a real title/link, not a constructed example
- [ ] B05's results table shows all 5 feeds, not just the favorable CFTC row
- [ ] B05 narration frames this as today's live test, not an eternal historical claim (see FACTCHECK.md)
- [ ] Before/after code (B06) both visible together
- [ ] Silent title card present; brand/fellow sign-off card present

**Estimated runtime:** ~2:20 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — not yet run, pending this beat sheet's approval).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-08-30. Both FACTCHECK open items
resolved (see `FACTCHECK.md`). Cleared to generate Kokoro audio and proceed to previz.
