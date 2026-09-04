# FACTCHECK — One Tool a Week. (Brandy)

## The governing rule

Everything in this reel comes from the human's own account of her week, given 2026-08-30,
with an explicit instruction: *"Please don't invent stats or specific findings I haven't
described — keep the tool descriptions and article summaries at the level of what I've told
you here. Use my own framing for the audit and coaching experience, not invented details."*

So the reel states what was made, and deliberately does **not** state what any of it found.

## Claim ledger

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00/B01 | A weekly series: one Humanitarians AI tool per week, used, then written up | stated | ✓ |
| 2 | B02 | This week's tool is **Brandy**, a brand-audit tool | stated, verbatim | ✓ |
| 3 | B02 | Link: humanitarians.ai/ai1/tools/brandy-tool | supplied by the human | ✓ |
| 4 | B03 | Three pieces shipped: a LinkedIn post, and two Substack articles | stated | ✓ |
| 5 | B04 | Article one, "I Ran Our Own Brand Audit Tool On…", ran Brandy on Humanitarians AI itself | stated | ✓ |
| 6 | B05 | **Ogilvy** is an AI copywriting coach, also from Humanitarians AI | stated, verbatim | ✓ |
| 7 | B05 | Article two, "I Told an AI Copywriting Coach I…", is about taking the coaching | stated | ✓ |
| 8 | B06 | Nina has **proposed** a fashion sustainability team — Yatra, Agrima, Bhakti, with Komal — on articles and AI tools for luxury brands | stated | ✓ — and rendered as PROPOSED throughout |

## What the reel deliberately does NOT say

- **What the brand audit found.** B04 says the audit was run and written up. It never
  characterises the result. The human did not describe the findings, so the reel has none.
- **What the copywriting coach said**, or whether the coaching was good. B05 says the
  coaching was taken and written up, nothing more.
- **What Brandy or Ogilvy do beyond their one-line descriptions.** "A brand-audit tool" and
  "an AI copywriting coach" are the human's own words and the reel does not extend them.
- **Any statistic** — no engagement figures, no counts of tools, no dates beyond "this week".
- **That the fashion team exists or has started.** It is proposed. See below.

## Partial titles, rendered verbatim

Both article titles arrived truncated with an ellipsis:

- "I Ran Our Own Brand Audit Tool On…"
- "I Told an AI Copywriting Coach I…"

They render exactly like that, ellipsis included. Completing them would have meant
inventing the half of each title the human did not supply. B04's narration works *with* the
truncation — "and the answer to that sentence is us" — rather than around it.

## Structural enforcement

- `RcpCard` takes `lines: string[]` and renders them verbatim. There is deliberately **no**
  "summary" or "findings" field: a field like that is an invitation to fill it.
- `RcpTeam` **requires** a `status` string and renders it in the terracotta accent as the
  most prominent element on the card — "Proposed by Nina — not started yet". The component
  cannot display a proposed initiative as though it were underway. The verdict card repeats
  the same qualifier.

## Named people

Nina, Agrima, Bhakti and Komal appear by first name, as supplied by the human about her own
team. No roles, quotes or attributes are asserted beyond Nina having made the proposal and
Komal being the person the team would work with. No pronouns are used for any of them.

## Dating risk

The composer chrome renders a model chip ("Fable 5") on B00 and B08 — shipped component
chrome, never referenced by narration. The reel is a dated weekly recap by design, so its
"this week" framing is correct rather than a liability.

## Register check

The Teardown move is B02 and B06: the reel refuses to describe Brandy beyond its own
one-line description ("I'll let the write-ups do the describing"), and refuses to let a
proposal read as an achievement ("It's proposed, not started, so that's all I'll claim for
now"). A recap that inflated either would have failed DOUBLE-CHECK LAW.
