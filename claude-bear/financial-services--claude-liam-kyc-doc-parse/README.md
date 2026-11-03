# Does Claude "Approve" a KYC Packet, or Just Parse It?

Ask whether Claude's `kyc-doc-parse` skill decides if a client passes KYC
screening and it's tempting to picture it clearing or flagging clients on
its own. That's not what's happening. Anthropic's `kyc-doc-parse` skill
reads a written SKILL.md and only extracts what's already on the page into
five structured fields — identity, ownership, control, source of funds,
and document inventory. Watch the anchor: one onboarding packet's data
landing in all five field buckets, nothing here judging the client, only
structuring what the document says. Feed it a packet where the
beneficial-owner section is left blank, and it doesn't raise an alarm — it
records that field as missing and returns the rest of the packet, parsed,
exactly as instructed. A full set of fields isn't a cleared client, it's
captured data waiting on a rules engine to actually screen it. And a field
marked missing isn't proof of fraud either — the document might simply
not have been submitted yet. kyc-doc-parse doesn't decide whether a
client passes KYC — a complete parse means the fields were captured, not
that the client was cleared.

**Topic:** KYC-DOC-PARSE · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-kyc-doc-parse

---

## Chapters

0:00 What does the skill do with a KYC packet — approve it?
0:11 Decides, or extracts?
0:34 One packet, five fields
0:53 Filled in, with a catch
1:11 Carry-out
1:25 Your turn
1:45 Outro

---

## YOUR TURN

"Take a messy document — a lease, an invoice, an onboarding form, whatever
you have on hand. Ask Claude to read it and sort the information into a
fixed set of categories you specify in advance. Then hand it a version
with one section blank, and see whether it flags the gap as a missing
field rather than guessing what was probably there."

Watching the parser mark a gap as missing instead of inventing a
plausible fill is the fastest way to see that structuring a document and
judging its contents are two different jobs.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-kyc-doc-parse`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
parses an onboarding packet into five structured KYC fields as the first
step of KYC screening, feeding a downstream rules engine — it does not
itself judge whether a client passes screening. This script makes no
claim about any specific client, institution, or document format — only
the general mechanism (extraction into structured fields) and its two
failure directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #FinTech #KYC #Compliance #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
