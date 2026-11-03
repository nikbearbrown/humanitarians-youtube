# QUESTION — knowledge-work-plugins--claude-liam-call-prep

**Question:** Claude, Call Prep.

**Who asked / where:** Redo-mode build. `SUBJECT.json` points at
`anthropics/knowledge-work-plugins/youtube/claude-liam-call-prep/beat_sheet.json` as the
source — a Teardown-register skill-teardown of an Anthropic skill named `call-prep`, built
in a 2026-07-25 batch (`PEDAGOGY.md`: "Batch build — skill teardown format", verdict PASS).

**Source defect found on read:** the source's narration truncates its own trigger-phrase
list mid-quote in three of its seven beats — B03 ("Triggers on 'prep me for my call ."),
BVDT (same fragment), BHTF ("I want to prepare for a customer or prospect call using
common room signals. triggers on '.") — all three cut off right after "prep me for my
call" instead of finishing the quoted phrase. This is the same batch template-truncation
bug already logged on this family's `customize` sibling in `claude-for-legal`, but milder
here: B00 in *this* source carries the complete, untruncated version of the same sentence
— "Triggers on 'prep me for my call with [company]', 'prepare for a meeting with
[company]', 'what should I know before talking to [company]', or any call preparation
request." — so nothing had to be invented; the complete phrase list was recovered directly
from B00 and used everywhere the truncated copies appear in B03/BVDT/BHTF.

**What this redo keeps, and what it does not invent:** every fact the source's readable
text establishes is kept and generalized — a Skill is a folder Claude reads before it
works; the `SKILL.md` file is the full instruction set in plain language, not hidden logic
("the file is the program"); the pipeline lives in a Steps section, read top to bottom,
executed in order, no branching unless a step says so; `call-prep` specifically prepares
for a customer or prospect call using signals from Common Room, and triggers on phrases
like "prep me for my call with [company]" or "what should I know before talking to
[company]"; run the same request through it twice and the same steps produce the same
result; the guarantee holds only for what the file specifies, nothing outside it. This
reel never invents what signals Common Room actually surfaces (account activity, usage,
recent conversations are named generically in B03/mechanism as the kind of signal a CRM
integration of this sort would carry — consistent with "Common Room signals" in the
source, not additional specifics the source never gave).

**The wrong guess this reel corrects:** "call prep" sounds like it could mean Claude joins
or makes the call itself — a live-calling assistant. It doesn't. The skill assembles a
briefing from account signals *before* a human has the call; Claude never participates in
the call. That reading is what the cold-open writer beat states and then corrects.

**Carry-out it's built to defeat:** the newcomer's guess that Claude call-prep means Claude
handles the call. The correction: it preps a person for the call, from the same signals,
the same way every time — and it never joins the call itself.
