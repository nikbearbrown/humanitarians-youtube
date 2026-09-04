# QUESTION — knowledge-work-plugins--android

**Question:** Claude, Contact Center/android.

**Who asked / where:** Redo-mode build. `SUBJECT.json` points at
`anthropics/knowledge-work-plugins/youtube/claude-liam-contact-center/android/beat_sheet.json`
as the source — a Teardown-register skill-teardown of an Anthropic skill named
`contact-center/android`, built in a 2026-07-25 batch (`PEDAGOGY.md`: "Batch build — skill
teardown format", verdict PASS).

**What the source establishes, kept and generalized:** a Skill is a folder Claude reads
before it works; the `SKILL.md` file is the full instruction set in plain language, not
hidden logic ("the file is the program"); the source's own file listing (`RUNBOOK.md`,
`SKILL.md`, `concepts/`, `examples/`, `references/`, `troubleshooting/` — 6 files total) is
reused as-is; the pipeline lives in a Steps section, read top to bottom, executed in order,
no branching unless a step says so; `contact-center/android` specifically covers the Zoom
Contact Center SDK for native Android — chat, video, the virtual agent (ZVA), scheduled
callback integrations, campaign mode, service lifecycle, and rejoin handling; run the same
request through it twice and the same steps produce the same integration code; the
guarantee holds only for what the file specifies, nothing outside it.

**What this redo does not invent:** the source never lists a specific trigger-phrase quote
for this skill (unlike some siblings in this family), so none is fabricated here — B03
states only the scope the source itself gives (the named SDK feature areas), not a made-up
"triggers on ..." phrase.

**The wrong guess this reel corrects:** "Claude, Contact Center/android" sounds like it
could mean Claude runs or operates the contact center itself — answering calls, handling
customers live. It doesn't. The skill is a coding aid: it helps build the native Android
app that talks to Zoom's Contact Center SDK. Claude never takes a call; it writes the
integration code. That reading is what the cold-open writer beat states and then corrects.

**Carry-out it's built to defeat:** the newcomer's guess that Claude runs the contact
center. The correction: it writes the Android integration code that connects to one — the
same code, from the same request, every time — and it never takes the call itself.
