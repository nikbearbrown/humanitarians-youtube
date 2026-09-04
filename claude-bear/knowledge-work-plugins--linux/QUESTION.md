# QUESTION — knowledge-work-plugins--linux

**Question:** Claude, Meeting SDK/Linux.

**Who asked / where:** Redo-mode build. `SUBJECT.json` points at
`anthropics/knowledge-work-plugins/youtube/claude-liam-meeting-sdk/linux/beat_sheet.json`
as the source — a Teardown-register skill-teardown of an Anthropic skill named
`meeting-sdk/linux` (brand `claude-liam`, audience `Claude`, 7 beats: B00 cold open, B01
anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro — all
already REMOTION).

**Source is intact.** Every beat carries the full skill-description sentence: "Zoom
Meeting SDK for Linux - C++ headless meeting bots with raw audio/video access,
transcription, recording, and AI integration for server-side automation." Nothing to
recover — the domain-specific fact set survives completely and is what this redo keeps.

**What survives in the source, and is what this redo keeps:** a Skill is a folder Claude
reads before it works; this one, `meeting-sdk/linux`, holds six files/folders —
`linux.md`, `meeting-sdk-bot.md`, `RUNBOOK.md`, `SKILL.md`, `concepts/`, `references/` —
with `SKILL.md` the instruction set ("the file is the program"); the pipeline lives in a
Steps section, read top to bottom, executed in order, no branching unless a step says so;
the job is a C++ meeting bot that connects to Zoom via the Meeting SDK, runs headless on a
Linux server (no window, nobody at a keyboard), and from there has raw access to the
meeting's audio and video — enough to transcribe, record, and feed further AI steps, as
server-side automation; the guarantee is repeatable results (same input, same output,
every run); the limit is "anything outside the spec" — ask for something the file doesn't
cover and the skill has nothing to say about it.

**The wrong guess this reel corrects:** a newcomer hears "meeting bot" and pictures
something with a visible presence — a window, a screen, an avatar sitting in the call
that a person could watch work. The source's own line reads the opposite way: "headless
meeting bots ... for server-side automation" — there is no screen and nobody watching;
it is a process on a server, not a window on a desk. The cold-open writer beat states the
over-read (needing a screen to run on) and corrects it (needing a server).

**Carry-out it's built to defeat:** the newcomer's guess that a Zoom meeting bot needs a
screen or a window somewhere to exist in. The correction: it needs a server, nothing more
— one instruction file that runs Claude as a headless bot doing exactly what the file
says, the same way every run.
