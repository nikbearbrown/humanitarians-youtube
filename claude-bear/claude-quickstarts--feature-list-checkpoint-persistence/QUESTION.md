# QUESTION

**The question:** "Persisting Progress Across Context Windows." — how does a coding
agent working through a long feature list pick up correctly in a brand-new session,
using the real Anthropic Claude Quickstarts pattern (`autonomous-coding/autonomous_agent_demo.py`)
as the specimen.

**Mode:** redo — source is
`anthropics/claude-quickstarts/youtube/feature-list-checkpoint-persistence/beat_sheet.json`
(Teardown register, already built as claude-liam content). This reel keeps the question,
the facts about how the checkpoint mechanism works, and the body argument (a context
window is a workspace, not memory; `feature_list.json` is the external source of truth;
git is the immutable ledger; each session reads the file, finds the first incomplete
entry, and resumes there), and keeps the 8-beat count (B00–B07 in the source). It
re-registers the narration to Plain, replaces the cold open with the Brutalist Hesitant
Writer, and closes with the Humanitarians AI skin.

**Why it earns a reel:** a newcomer watching an agent resume a long task across two
separate sessions reasonably assumes it "remembers" — some kind of continuity carried
in the model itself. It doesn't. The agent's context window empties completely between
sessions; what survives is a plain file on disk (`feature_list.json`, one entry per
feature, marked `incomplete` or `passing`) plus a git commit history. The new session
rereads that file, finds the first entry still marked incomplete, and starts exactly
there.

**Naive framing (B00, corrected on screen):** "Claude just / remembers where / it left
off? / How does it resume?" → corrects "remembers" to "rereads."

**Source-beat audit:** the source (`feature-list-checkpoint-persistence`) has B00
(`ClaudeComposerAsk`, cold open) as REMOTION, B01–B04 as GRAPHIC (own Manim, filled),
B05 (`ClaudeVerdictArtifact`) as REMOTION, B06 (`ClaudeComposerAsk`, your turn) as
REMOTION, B07 (`ClaudeTitleOutro`) as REMOTION. None is `ai-video-prompt`, pantry, or
a human-drop slot, so NO-GENAI/NO-PANTRY LAW requires no substitution on those grounds.
The body beats (B01–B04) are rebuilt fresh as GRAPHIC (Manim) in the humanitarians
palette rather than the source's Claude-palette `ClaudeComposerAsk` command-card
treatment, matching this skill's established channel-skin practice (see
`claude-quickstarts--claude-liam-first-run`) and the CHANNEL SKIN row of
`skills/make/hai-simple/SKILL.md`. The source also carries three unused, empty-narration
`BOOKEND`-lane template beats (`BVDT`, `BHTF`, `BOUT`) left over from an older pipeline
scaffold — these are not part of the rendered 8-beat sequence (`build.filled`/`of` in
the source sheet count only B00–B07) and are not carried into this redo; this reel's
own `BCRY`/`BHTF`/`BOUT` are authored fresh per the hai-simple spine, not copied from
those empty placeholders.
