# Beat Sheet (APPROVED — Gate P, 2026-09-29): "The All-Clear That Wasn't All There"

**Creator:** Sai Pranavi J. | Weekly work report
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Phase:** 2 — approved for narration lock / audio generation. B06's aside kept as drafted. See
`FACTCHECK.md`.

---

## Premise

**What this covers:** a small, real bug in the pipeline's "all clear" status email — the message
sent when a scheduled run finds nothing high-priority. Its "Monitored Sources" section, a static
hand-written grid, listed only 4 of the pipeline's 5 real RSS feeds. Investment Advisor Rules —
one of the 5 actual source nodes in the workflow — was missing from both the grid and the summary
sentence. Fixed by adding the missing card, verified by diffing every source-card label against
the workflow's real feed-node names.

**What this also covers, briefly:** while tracing the email-generation code to find this bug, an
older open item from `FINDINGS.md` — "apply A4/B4 to Generate Email" — was checked and closed as
stale: both the HTML-escaping and the aligned alert threshold were already present from the very
first hardening commit, before `FINDINGS.md` was even written. No code change was needed there;
this video names that check so it isn't mistaken for still-open.

**What this deliberately leaves out:** this is a display-only fix to a status email. No scoring,
classification, or alert-routing logic changed.

**Source status:** Real engineering work. Every claim traces to
`/Users/pranavijs/mycroft/scripts/regulatory-intel/B5-VERIFICATION.md` (2026-09-29) and the
matching `logs/RUN_LOG.md` entry. See `SOURCES.md` for the full claim → source mapping.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated |
| B03 Setup | The all-clear email's actual "Monitored Sources" grid, as it shipped (4 cards) | Real screenshot-style recreation, not paraphrased |
| B04 Discovery | The 4 shown sources next to the workflow's real 5 RSS feed node names, the 5th highlighted as absent | Both lists visible together, contrast is the point |
| B05 Fix | Before/after grid, 4 cards → 5 cards, the added card highlighted | Full before AND after visible together |
| B06 Aside | The stale `FINDINGS.md` note ("apply A4/B4 to Generate Email"), stamped resolved/already-fixed | Brief, clearly marked as a side-finding, not the main story |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The All-Clear That Wasn't All There" + @HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:20)**
VO: "Hi, I'm Sai Pranavi J.. This video is about the pipeline's own 'all clear' email — the
one it sends when nothing needs your attention — and a small, real gap where it was quietly
under-reporting what it actually watches."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:20–0:34)**
VO: "On a quiet day, this pipeline sends a status email: no critical alerts, here's what we
checked. That second half — here's what we checked — turned out to be wrong."
Visual: the all-clear email's "✅ All Clear!" header and "No new high-priority regulatory items
detected" message.

**B03. Setup (~0:34–0:56)**
VO: "The email lists its monitored sources in a little grid: SEC Press Releases, Federal Register,
FINRA Enforcement, CFTC Regulations. Four boxes. Clean, reassuring, and short one source."
Visual: the real 4-card "Monitored Sources" grid as it shipped, recreated verbatim.
*[Source: B5-VERIFICATION.md "The bug"]*

**B04. Discovery (~0:56–1:20)**
VO: "This pipeline actually pulls from five real feeds — the fifth is Investment Advisor Rules.
It's a real, working source node in the workflow. It's just never been on the card."
Visual: the 4 shown source names next to the workflow's actual 5 RSS-feed node names, the missing
5th name highlighted.
*[Source: B5-VERIFICATION.md "The bug" — real workflow node names]*

**B05. Fix + Proof (~1:20–1:46)**
VO: "The fix: add the missing card, and name it in the summary line too. Then I checked every
source label in the patched email against the workflow's real feed nodes, one for one. Five
listed, five real. Ran the workflow's own conformance check — still valid."
Visual: before/after grid — 4 cards crossed out, 5 cards shown, the new card highlighted.
*[Source: B5-VERIFICATION.md "The fix" and "Verification"]*

**B06. Aside — a stale note closed (~1:46–2:04)**
VO: "One more thing, while I was in this code: an old note said this same email still needed two
earlier fixes — HTML escaping, and an aligned alert threshold. Turns out both were already there,
since the very first hardening pass. Nothing to fix. Just confirmed, and written down, so nobody
re-checks it by accident."
Visual: the stale `FINDINGS.md` line, stamped "ALREADY FIXED — confirmed 2026-09-29."
*[Source: B5-VERIFICATION.md "What's NOT touched"]*

**B07. Takeaway (~2:04–2:18)**
VO: "A status email is supposed to be the boring, trustworthy part of a system. If it can't
accurately describe what it's watching, its silence isn't reassurance — it's just an unchecked
assumption."
Visual: statement card.

**B08. Sign-off (~2:18–2:23)**
VO: "Fixed with Claude Code, verified against the real workflow before it ever ran again."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] B03's 4-card grid is the real shipped content, not a constructed example
- [ ] B04 shows all 5 real feed names, the missing one clearly highlighted as absent from the email
- [ ] B05's before/after both visible together
- [ ] B06 is clearly framed as a closed, stale note — not implied as still open
- [ ] Silent title card present; brand/fellow sign-off card present

**Estimated runtime:** ~2:23 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — not yet run, pending this beat sheet's approval).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-09-29. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
