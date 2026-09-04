# QUESTION

**The question:** "Claude, Contact Research." — when you ask Claude about a
specific person, is it answering from what it already knows, or is it going
and finding out? Answered using the `contact-research` skill (a
partner-built Anthropic skill for Common Room contact intelligence) as the
concrete case.

**Mode:** redo — source is
`anthropics/knowledge-work-plugins/youtube/claude-liam-contact-research/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at a
`common-room/skills/contact-research/SKILL.md` on Bear's other machine —
not present in this tree, so this build reads the source beat_sheet's own
narration text, which already carries the skill's trigger-phrase language
verbatim, as the record of the source facts). 7 beats — B00 cold open
(`ClaudeComposerAsk`, already REMOTION, not AI-video/pantry, so NO-GENAI/
NO-PANTRY LAW required no substitution beyond the WRITER LAW swap), B01
anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT
outro. This build keeps the question and the source's body facts,
re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, restates the source's B03 "design tell" framing as a
both-directions mechanism fact instead of a design judgment, and closes with
the Humanitarians AI skin.

**Why it earns a reel:** `contact-research` is a SKILL.md file Claude reads
before it acts — the file is the instruction set, not a capability baked
into the model. It fires only when a request's words match its stated
triggers: `who is [name]`, `look up [email]`, `research [contact]`, `is
[name] a warm lead`, or any contact-level question. Once triggered,
execution is a linear pipeline with no branching unless a step says so: read
`SKILL.md`, execute each step in order (pull the contact's Common Room
signals), return the result. Same input, same steps, same kind of output,
every run — that is what a written spec buys over an improvised answer. The
corresponding limit: anything outside what the file specifies isn't
covered, and the newcomer's obvious alternative guess — that Claude already
knows who a person is and what they're up to, the way it knows general
facts — is wrong precisely because a contact's live signals (a recent reply,
a meeting booked, a title change, a shift in "warm lead" status) are dated
today, and nothing dated today lives in anything Claude was trained on.

**Naive framing (B00, corrected on screen):** "You ask about a person.
Claude must already know them, right?" → corrects "know" to "look up" (the
newcomer's default assumption is that Claude answers people-questions from
its own general knowledge; the correction states the real mechanism —
Claude has to go look the person up, via the skill, not recall).

**Body facts carried from source (unchanged):**
- a skill is a folder Claude reads before it works; `contact-research`'s
  `SKILL.md` is the whole instruction set — the file is the program
- the skill fires only on matching trigger language: `who is [name]`, `look
  up [email]`, `research [contact]`, `is [name] a warm lead`, or any
  contact-level question
- execution is linear: read `SKILL.md` → execute each step in order → return
  the result — no branching unless a step says so
- the payoff of a written spec is repeatability: the same request run again
  later walks the same steps and returns the same kind of output
- the limit is exact: anything outside what the file specifies isn't
  covered — a request that doesn't match a trigger never starts the
  pipeline, and the question falls back to whatever Claude would say without
  the skill
- source's Your Turn: paste the contact-research trigger phrase and ask
  Claude to walk through its steps before running them — watching whether it
  names the exact trigger it matched
