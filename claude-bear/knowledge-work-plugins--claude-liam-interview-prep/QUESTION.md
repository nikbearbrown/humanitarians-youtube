# QUESTION — knowledge-work-plugins--claude-liam-interview-prep

**Question:** Claude, Interview Prep.

**Who asked / where:** Redo-mode build. `SUBJECT.json` points at
`anthropics/knowledge-work-plugins/youtube/claude-liam-interview-prep/beat_sheet.json` as
the source — a Teardown-register skill-teardown of an Anthropic skill named
`interview-prep`, built in a 2026-08-03 batch (`PEDAGOGY.md`: "Batch build — skill
teardown format", verdict PASS).

**Source defect found on read:** the source's B03 narration truncates its own quoted
trigger-phrase list mid-sentence — "Claude's job: Create structured interview plans with
competency-based questions and scorecards. Trigger with \"inte." — cut off right after
opening the quote. This is the same batch template-truncation bug already logged on this
family's `call-prep` and `claude-for-legal/customize` siblings. Milder here too: the
source's own B00 carries the complete, untruncated sentence — "Create structured interview
plans with competency-based questions and scorecards. Trigger with 'interview plan for',
'interview questions for', 'how should we interview', 'scorecard for', or when the user is
preparing to interview candidates." Nothing had to be invented; the complete phrase list
was recovered from B00 and used wherever B03's truncated copy would otherwise appear.

**What this redo keeps, and what it does not invent:** every fact the source's readable
text establishes is kept and generalized — a Skill is a folder Claude reads before it
works; the `SKILL.md` file (1k, the only file in the source's B01 anatomy card) is the full
instruction set in plain language, not hidden logic ("the file is the program"); the
pipeline lives in a Steps section, read top to bottom, executed in order, no branching
unless a step says so; `interview-prep` specifically creates structured interview plans
with competency-based questions and scorecards, and triggers on phrases like "interview
plan for", "interview questions for", "how should we interview", "scorecard for", or any
request to prepare for interviewing candidates; run the same request through it twice and
the same steps produce the same result; the guarantee holds only for what the file
specifies, nothing outside it. This reel never invents which competencies, question banks,
or scorecard fields the skill actually produces — the source never gave those specifics,
so neither does this redo.

**The wrong guess this reel corrects:** "interview prep" sounds like it could mean Claude
does the interviewing itself — sits across from the candidate and runs the conversation. It
doesn't. The skill builds the plan, the questions, and the scorecard *before* a human
conducts the interview; Claude never conducts the interview itself. That reading is what
the cold-open writer beat states and then corrects.

**Carry-out it's built to defeat:** the newcomer's guess that Claude, interview prep means
Claude runs the interview. The correction: it preps the plan from a role, the same way
every time — and it never conducts the interview itself.
