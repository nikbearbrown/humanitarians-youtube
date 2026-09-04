# CARRY-OUT — knowledge-work-plugins--claude-liam-legal-response

**The line (written first, GATE C):**

> legal-response doesn't decide how to handle a legal matter or send
> anything on its own — it drafts a reply from a template and holds it for
> human review, or flags the request when nothing fits. A finished draft
> means the words are ready, not that anyone approved sending it.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land
(drafting from a template vs. deciding and sending, and ready-not-sent), not
the topic (legal correspondence generally).

**The wrong guess it defeats:** that a skill whose job is to "respond to a
legal inquiry" reads the request, drafts a reply, and sends it — handling
the matter start to finish, the way a person would. It isn't. The
`legal-response` skill reads a written SKILL.md and only matches the
inquiry to one of its configured templates, assembles a draft, and runs an
escalation check before anything moves further. Send it a request that
doesn't fit any template — a subpoena with unusual terms, say — and it
doesn't force a templated reply anyway: it flags the situation for
escalation and stops. The decision to send, and the judgment on anything
unusual, stays with a human.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's template-and-escalation mechanism, its
present-for-review design constraint, and its input-feeds-a-human-decision
boundary; this line compresses it into the reel's carry-out.
