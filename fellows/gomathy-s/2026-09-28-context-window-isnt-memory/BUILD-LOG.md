# BUILD-LOG — claude-liam-context-window

Justifications for the two items `CHECKS-REPORT.md` flags as open rather than
fully closed. Neither is a PUNT; both are deliberate, logged decisions per
`ai-explainer/SKILL.md`'s PROOF GATE ("the loop resolves it or the author
explicitly justifies it in BUILD-LOG.md").

## 1. RESOLVED (12-beat rework) — three-outcome list

Originally: `AttritionChain` had no built-in slot for the three named
outcomes (error / summarize / drop oldest), and no registered card component
had been confirmed for it. Resolved in the 60s/12-beat rework: the outcome
list now gets its own beat (B07) using `FormBCard` — a registered, renderable
component built exactly for "a short list of named things" (`nopunt`'s own
catalog). `AttritionChain` (B06) now covers only the room-remaining climb, no
longer double-booked with the outcome list.

## 2. B05 (B03 in the long cut) — inference caveat removed from the on-screen tag

`prose/plain/PROSE.md` (the Plain register's own doctrine) asks for exactly
one flagged inference point to be visible on screen when a claim isn't a
stated fact — Move 3: "insert exactly one explicit flag at the moment the
leap happens." B05's "code, numbers, jargon, and non-English text tend to cost
more per word" claim is exactly that kind of claim (confirmed in
`SOURCES.md` as general tokenizer knowledge, not something Anthropic's own
docs state). An on-screen flag was authored and then explicitly removed on
the user's direct instruction ("remove... the on-screen INFERENCE tag... leave
the caveat in SOURCES.md"). Recorded here as a deliberate, informed exception
to that doctrine line, not an oversight — the claim still has on-screen
support: B05's `FormBCard` names the four content types (Code, Numbers,
Jargon, Non-English text), so the beat remains SHOW-classified; only the
explicit "this is inference" disclaimer is gone from the frame.

## Final master

Clean master built 2026-10-01 with `./art final`:
`claude-liam-context-window.mp4` (3840×2160, 63.4 s) + `.verified.json`.
Masters are in the shared Drive. The 9:16 master is logged in
`vertical/BUILD-LOG.md`.
