# QUESTION

**The question:** "Claude, First Run." — what actually happens the first time Claude
picks up a documented skill, using the real Anthropic skill named `first-run` as the
specimen.

**Mode:** redo — source is
`anthropics/claude-quickstarts/youtube/claude-liam-first-run/beat_sheet.json`
(Teardown register, already built as claude-liam content). This reel keeps the
question, the facts about how a skill works, and the body argument (skill = folder,
SKILL.md = instruction set, Steps section = linear pipeline, first-run's own spec =
env check + one safe browser task + open the trajectory viewer), and keeps the
7-beat count. It re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, and closes with the Humanitarians AI skin.

**Why it earns a reel:** a newcomer watching Claude execute a documented workflow
reasonably assumes the behavior is built into the model — some hidden "first-run
mode." It isn't. `first-run` is a folder with one file, `SKILL.md`, written in plain
language; Claude reads it before acting and follows its Steps section in order.
Nothing about the behavior is hardwired, and nothing outside what the file
describes is covered either.

**Naive framing (B00, corrected on screen):** "Claude just knows what to do first —
it's built in, right? So what's actually there?" → corrects "built" to "written."

**Source-beat audit:** every beat in the source (`claude-liam-first-run`) is already a
REMOTION pattern — `ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeComposerAsk`, `ClaudeTitleOutro`.
None is `ai-video-prompt`, pantry, or a human-drop slot, so NO-GENAI/NO-PANTRY LAW
requires no substitution on those grounds. The body beats (B01–B03) are nonetheless
rebuilt as GRAPHIC (Manim) in the humanitarians palette rather than kept as the fixed
Claude-palette Remotion components, matching this skill's established channel-skin
practice (see `claude-basics--anthropic-retrieval-demo-wrapping-same-text-xml-changes`)
and the CHANNEL SKIN row of `skills/make/hai-simple/SKILL.md` (humanitarians palette,
not the Claude fidelity skin).
