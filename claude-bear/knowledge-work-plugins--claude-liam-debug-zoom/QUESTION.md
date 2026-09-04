# QUESTION

**The question:** "Claude, Debug Zoom." — when you point Claude at a broken
Zoom integration using the `debug-zoom` skill, does it go fix the problem, or
does it hand back something else? Answered using the skill's own stated
output — a ranked hypothesis list plus verification steps — as the concrete
case.

**Mode:** redo — source is
`anthropics/knowledge-work-plugins/youtube/claude-liam-debug-zoom/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at a
partner-built `debug-zoom` SKILL.md under `knowledge-work-plugins/partner-built/
zoom-plugin/skills/debug-zoom/` — that path lives only on Bear's other
machine, not locally, so this redo relies on the source reel's own narration
as the record of the skill's content; B00's narration carries the skill's
full, un-truncated description). 7 beats — B00 cold open, B01 anatomy, B02
pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro. B00 was
already `ClaudeComposerAsk` REMOTION, not AI-video/pantry, so NO-GENAI/
NO-PANTRY LAW required no substitution beyond the WRITER LAW swap.

**Note on the source text:** three of the source's later beats (B03, BVDT,
BHTF) truncate the skill's own description mid-word ("...routing into the
right Zoom refer[ences]") — an interpolation-budget bug in the source
reel, not a fact to carry forward. This redo uses B00's complete, untruncated
sentence as the record of what the skill actually does and does not repeat
the truncation.

**Why it earns a reel:** `debug-zoom` is a Claude skill — a folder containing
one file, `SKILL.md`, read before Claude acts. Its stated job: "Debug a
broken Zoom integration by isolating the failure point and routing into the
right Zoom references. Use when auth, API, webhook, SDK, or MCP behavior is
failing and you need a ranked hypothesis list plus verification steps." The
pipeline is linear: read `SKILL.md`, execute each step in order, return the
result — no branching unless a step says so. The output is diagnostic, not
corrective: a ranked hypothesis list (which failure is most likely, in what
order to check it) plus verification steps for each hypothesis — not an
automatic fix. It's scoped to five failure categories named in the file:
auth, API, webhook, SDK, MCP. Inside that scope, the same input reliably
produces the same ranked path forward. Outside it — a failure that isn't one
of those five categories, or isn't actually a Zoom-integration bug at all —
the file has nothing to say, because a skill only knows what's written in it.

**Naive framing (B00, corrected on screen):** "My Zoom integration is broken
— can Claude just fix it?" → corrects "fix" to "diagnose" (the newcomer's
default read of "debug" is "repair"; the skill's actual output is a ranked
list to check, not a repair).

**Body facts carried from source (unchanged):**
- a skill is a folder Claude reads before it acts; `debug-zoom` is one file,
  `SKILL.md`, plain language, no hidden logic — the file is the program
- pipeline: read `SKILL.md` → execute each step in order → return the result;
  linear, no branching unless a step says so
- the skill's job, verbatim from the source: isolate the failure point in a
  broken Zoom integration and route into the right Zoom references, scoped
  to auth, API, webhook, SDK, or MCP behavior
- the output is a ranked hypothesis list plus verification steps — diagnosis,
  not an automatic fix
- same input → same output, every run, inside the five named categories;
  outside them, the file has nothing to say — the limit is only what the
  file specifies
- source's Your Turn worked example: paste a description of a broken
  integration and ask Claude to walk through what it will do, before doing
  it, using the debug-zoom skill

**Anchor (new, invented for the Plain cut to make the mechanism
visualizable):** a Zoom webhook that stops delivering events — walked
through the ranked-hypothesis order (signing secret, then timestamp
tolerance, then endpoint URL) at B02 (planted) and B03 (paid off with the
verification step for each). Anchor invention is necessary because the
source's own body content, past its verbatim skill description, is generic
teardown boilerplate (folder/file/pipeline) with no worked example of its
own; the failure categories the skill itself names (auth, API, webhook, SDK,
MCP) supply the concrete anchor, not an invented fact about the skill.
