# CARRY-OUT — financial-services--claude-liam-kyc-doc-parse

**The line (written first, GATE C):**

> kyc-doc-parse doesn't decide whether a client passes KYC — it turns a
> messy onboarding packet into five structured fields a rules engine can
> actually screen. A complete parse means the fields were captured, not
> that the client was cleared.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land
(extraction into structured fields vs. a screening decision, and
captured-not-cleared), not the topic (KYC compliance generally).

**The wrong guess it defeats:** that a skill whose job is to "parse KYC
fields" is also judging the client — clearing or flagging them for risk.
It isn't. The `kyc-doc-parse` skill reads a written SKILL.md and only
extracts what's already on the page into five structured categories —
identity, ownership, control, source of funds, document inventory. Feed it
a packet with the beneficial-owner section left blank, and it doesn't raise
an alarm: it records that field as missing and returns the rest of the
packet, parsed, exactly as instructed. The screening decision belongs to
the rules engine downstream, which is a separate step the skill only feeds.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's five-field scope, its first-step-of-screening role, and
its input-feeds-rules-engine boundary; this line compresses it into the
reel's carry-out.
