# SOURCES — hai-agents-on-their-own

Every on-screen artifact is listed here with how it was obtained. Claim-level verdicts are
in [FACTCHECK.md](FACTCHECK.md); this file records provenance.

## Primary sources — first-party, produced during this build

**1. An unattended task that reported its own completion**
Task `bvg1cuail`, exit code 0. A real background job from this build session; the id, the
status and the exit code are the actual values rather than a mock. Shown in B04. The id is
session-scoped and will be stale later — the claim is that it happened, not that it repeats.

**2. A guardrail string, quoted verbatim**
The rule the system attaches telling the agent that an automated event is **not** a message
from the user and must not be read as acknowledgement or consent. Taken word for word from
a notification received in this session. Line breaks were added to fit the card; no wording
was changed. Shown in B05. This one must stay verbatim — the exact phrasing is the beat.

**3. Six refusals, counted**
Building the companion video `hai-mcp-explained` earlier the same day, the toolkit refused
to produce a final cut six separate times. The breakdown: GATE F twice, GATE T three times,
and one gate-v BLOCKER. Causes were missing paperwork, text outside the safe area, and a
glyph under the size floor. Shown in B06. The figure is a count of real refusals and must be
recounted if the beats change.

Row 3 is self-referential on purpose. The evidence that an agent needs limits imposed from
outside is the set of limits that stopped this very build.

## Attributed position, not a finding

B06's claim that the toolkit cannot judge whether a film is good — only whether it matches
what a human already decided mattered — is brutalist.art's own stated position, argued in
its README ("Claude cannot watch the video"). It is carried as the project's view, not as a
proven fact.

## Described, not quoted

B01-B03 describe the common agent architecture: the same model in a loop, able to act
between turns, with the human pause removed. Consistent with the evidence above but not
checked against a primary agent-architecture reference during the build. Marked
SPEC-ASSERTED in FACTCHECK.md.

## Advice, explicitly not a measurement

B07's test — the work is checkable, a mistake is cheap to undo, a rule can be written
ahead of time, and if you cannot say what would make it stop it is not ready — is offered
as judgement. It is narrated as a test, never as a citation.

## Narration

Kokoro `am_onyx`, generated locally. Disclosed aloud in B00.
