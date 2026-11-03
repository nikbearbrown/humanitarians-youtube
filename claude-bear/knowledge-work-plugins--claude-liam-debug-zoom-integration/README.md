# Claude, Debug Zoom Integration.

When a Zoom integration breaks, does Claude jump straight to a fix? Its
real `debug-zoom-integration` skill runs its steps in a fixed order —
checking authentication, webhooks, the SDK join call, MCP transport, and
the real-time media stream — and only proposes a fix once the failing
layer is actually confirmed. Walked through an invented "join button
spins and never connects" example: auth, webhooks, and SDK join all check
out clean; the break lands in MCP transport; only then does a fix get
proposed. Ask about something outside those five layers, and the skill has
nothing to add — the same steps just don't run.

**Topic:** SKILLS · DEBUG-ZOOM-INTEGRATION
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-debug-zoom-integration

---

## Chapters

0:00 A Zoom join breaks — does Claude just fix it right away?
0:11 Five places it could be
0:29 One layer at a time
0:37 Confirmed, then fixed
0:52 Carry-out
1:00 Your turn
1:18 Outro

---

## YOUR TURN

"Before you propose any fix for this bug, walk me through every layer that
could be responsible, and check them one at a time, out loud, in order —
don't jump to a patch until you've isolated which one actually broke."

Paste it onto a bug you're stuck on right now, then watch whether Claude
actually isolates first, or guesses.

---

## Deliberately not claimed

This reel's real `debug-zoom-integration` `SKILL.md` lives on a partner's
private build path, unreachable from this workspace — the facts used here
(the skill's purpose, the linear step order, the "isolate before fix" rule)
are recovered from the untruncated narration already present in the source
batch build, not invented. The source's own B03/BVDT/BHTF beats truncate
that same purpose sentence mid-word; this redo carries the complete
version instead. The "join button spins, break is in MCP transport"
scenario is this reel's own invented anchor, built to make the five layers
and the isolate-first order visualizable — not a claim about what actually
breaks in any real Zoom integration. Not a verdict on the skill's design:
the isolate-then-fix structure is stated as a sequencing fact, never a
critique of how much checking it asks for.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudeCode #Zoom #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
