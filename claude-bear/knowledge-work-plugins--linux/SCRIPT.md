# Claude, Meeting SDK/Linux. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-meeting-sdk/linux`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone assumes meeting-sdk slash linux needs a screen to run on, something to watch. It doesn't. meeting-sdk/linux needs a server to run the bot on. Right?" | writer types "meeting-sdk/linux needs\na SCREEN to run\nthe bot on.\nRight?", hesitates on SCREEN, corrects to "server" — lands "meeting-sdk/linux needs a server to run the bot on. Right?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is meeting-sdk slash linux. The SKILL.md holds the full instruction set — plain language, no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: linux.md, meeting-sdk-bot.md, RUNBOOK.md, SKILL.md, concepts/, references/ (6 total) |
| B02 | pipeline | The pipeline is in the Steps section. Claude reads each step in order and runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → RESULT |
| B03 | 3 mechanism | Here's the part worth knowing. meeting-sdk slash linux specifies one exact job: a C plus plus bot that joins a Zoom meeting headless, on a Linux server, with raw access to its audio and video. From there it can transcribe the call, record it, and hand any of that to further AI steps — automation that runs unattended, with no one watching a screen. | heading card: "The interesting constraint." + headless/server statement |
| **BCRY** | **6 carry-out** | meeting-sdk/linux isn't a Zoom app with a window — it's one instruction file that runs Claude as a headless bot on a server, doing exactly what that file says, every time. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. I want a Zoom meeting bot running headless on Linux. Read the meeting-sdk slash linux skill in this folder and walk me through exactly which steps you'd run, in order, before you run any of them. Watching it explain first shows you where headless stops being an idea and starts being a real constraint. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Meeting SDK/Linux. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the headless/server-side mechanism and the same-input/same-output scope, then stops; the source's "Teardown moment," "what it gets right / what it bites," and "Verdict" framing are all dropped |
| Stakes → mechanism | B00 states the misconception (a meeting bot needs a screen/window); B01–B02 explain the file and pipeline before B03's scope statement |
| Wrong guess surfaced and falsified | B00: the naive read is "needs a screen to run on, something to watch"; the source's own spec falsifies it in the same beat — "headless ... server-side automation" means no screen, nobody watching |
| Carry-out | BCRY compresses the distinction (no window, one file, same behavior every run) rather than summarizing the topic |
| Host handoff | B00 hands narration to Liam implicitly; no puppet host in hai-simple |
| Hedge words | none used — every claim is read directly off the source's own intact narration text |

## Deliberately not claimed

- **Not "the bot has no video access."** The source is explicit: raw audio/video access,
  transcription, and recording are all real capabilities — what's corrected is the *screen*
  the bot supposedly needs, not the audio/video access itself.
- **No invented field beyond the source's own list.** The skill's job is stated exactly as
  the source names it — C++, headless, Linux server, raw audio/video access, transcription,
  recording, AI integration, server-side automation — nothing added.
- **No verdict on the skill's design.** The source's Teardown register judged the skill
  ("what it gets right," "what it bites," "know the limit"); this Plain redo describes the
  same headless/server-side, same-input/same-output scope without ruling on whether it was
  well designed.

## Handoff prompt (BHTF, read aloud)

> "I want a Zoom meeting bot running headless on Linux. Read the meeting-sdk/linux skill
> in this folder and walk me through exactly which steps you'd run, in order, before you
> run any of them."

Why it's worth running: it forces Claude to state its own steps before acting, on a request
that only makes sense headless — the same "explain first" clause the source reel's own
handoff used to surface a skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
