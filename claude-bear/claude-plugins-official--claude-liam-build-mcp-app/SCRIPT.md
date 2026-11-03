# SCRIPT.md — Return Data. Serve HTML. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-build-mcp-app` (Teardown, walks the Anthropic
`build-mcp-app` Claude plugin-dev Skill) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then
stop, no verdict); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed their tool sends back the widget's HTML directly. It
doesn't — a separate resource serves that. So: how do you make a resource
serve the widget's HTML?

*(Text typed on screen: "How do I make / my tool serve / the widget's
HTML?" — trigger word "tool" corrects to "resource", landing on: "How do I
make my resource serve the widget's HTML?" Text kept short (44
forward-typed chars, 3 lines) and timing params set at the safe-margin
values established on the `claude-plugins-official--claude-liam-agent-
development` sibling's fixed second attempt (42ms/char, 8%
hesitateBetween, 4% mistakeRate) to avoid that sibling's first-attempt
TIMING LAW overrun.)*

## Body — anatomy, design routing, the shared failure mode

**NB01 — Tool returns data, resource serves HTML** (source B01, anatomy)
The two-part registration is the core pattern. Part one: the tool — it
declares a UI resource via `_meta.ui.resourceUri`, and its handler returns
plain data, not the HTML. Part two: the resource — registered separately,
it serves the widget's HTML with the exact MIME type
`text/html;profile=mcp-app`. The host sees that resource URI, fetches the
resource, and renders it in an iframe, piping the tool's return value in
through an `ontoolresult` event. Inside the iframe, an App class bridges
the two sides — methods like `sendMessage`, `updateModelContext`,
`callServerTool`, and `openLink`, set up before it connects. One more step
is mandatory: the iframe's content security policy blocks CDN script
fetches, so the widget's script bundle has to be inlined directly into the
HTML at startup.

**NB02 — Route first: elicitation, widget, or text** (source B02, design)
Before building a widget, route correctly. Elicitation is spec-native,
zero UI code, works in any compliant host — use it for yes-no
confirmation, short enum picks, and flat forms. Build a widget only when
the need can't be met by elicitation: large or searchable lists that need
scrolling, visual previews before choosing, charts and maps, and
live-updating progress. If none of those apply, skip the widget entirely —
text is faster to build and faster for the user. Five design rules that
save rewrites: one widget per tool; the tool's description must mention
the widget, since that's what makes Claude reach for it; graceful
degradation is automatic — hosts that don't support the apps surface just
render the tool's text content; don't block on widget results for
display-only tools — return a text summary alongside; and follow the
host's theme once connected, instead of hard-coding one.

**NB03 — Two causes, one blank rectangle** (source B05, teardown analysis
— re-registered Teardown → Plain, kept as the single most teachable fact
rather than the full "gets it right / where it bites" list)
Two ways to end up with the exact same blank rectangle, and no error
message. Serve the widget with the wrong MIME type, and the host silently
refuses to render it. Or leave the ext-apps bundle un-inlined — the
iframe's content security policy blocks the CDN fetch, and the widget
stays blank there too. Same failure, two different causes, and the browser
console won't tell you which one it was.

## Close

**BCRY — carry-out**
An MCP app is just a server with an extra resource — the tool still
returns data, and it's the resource that serves the widget's HTML. Get the
type or the bundle wrong, and it fails blank, not loud.

**BHTF — your turn**
Your turn. Paste this into Claude: build an MCP app with a file-picker
widget that lets someone choose a file from a list a directory-scan tool
returns. Then check four things. Does it use two-part registration — a
tool with `_meta.ui.resourceUri`, plus a separate resource? Does the
resource use the exact MIME type constant, not a hand-typed string? Is the
ext-apps bundle inlined at startup instead of pulled from a CDN? And does
the tool still return real text content alongside the widget, so a host
without the apps surface sees something useful? Get the type or the bundle
wrong, and the widget renders blank — same failure, no error, either way.

**BOUT — outro**
Return Data. Serve HTML. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a mechanism question — does the tool itself hand back the widget's HTML? |
| Wrong guess | B00 (WRITER LAW) | "tool" corrected to "resource" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the two-part registration split (tool declares + returns data, resource is registered separately and serves HTML) plus the App class bridge and mandatory bundle inlining; then the routing decision (elicitation vs. widget vs. text) and the five design rules |
| Anchor | the build-mcp-app skill itself, named at B00 and never dropped through NB01–NB03 | source is a single worked example throughout (one Skill), not a planted-and-paid-off separate case — there is nothing to return to that hasn't stayed on screen the whole time |
| Both directions | folded into NB03 + BCRY | NB03 states the two distinct causes of the identical failure symptom (wrong MIME vs. un-inlined bundle, both blank with no error); BCRY restates the design's split and its shared failure mode together — together they cover what the split gets you and what breaks it, matching the source's verdict beat, which paired the same two facts |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of what
the build-mcp-app Skill's SKILL.md specifies (the two-part registration,
the exact MIME type constant, the mandatory bundle-inlining step, the App
class methods, the elicitation-vs-widget routing rules, and the two silent
failure modes) — not an inference about hidden host internals. Per
simple's ONE-FLAG LAW, when the source genuinely supports everything as
stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01/B02 (anatomy /
design) + B05 (teardown analysis) + BVDT (verdict) + BHTF (your turn) +
BOUT (outro). This redo keeps that same 7-beat shape: B00 replaced 1:1
with BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER
LAW instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat
each; B05's long "gets it right / where it bites" list (the routing table
called out before any widget code, the two-part registration with working
TypeScript, the bundle-inlining rewrite snippet, the eight-method App
class API, the concrete design rules — versus the cache-flush gotcha
buried in the testing section, the CSP-blank failure documented in a
reference file rather than inline, the frameDomains footnote, the silent
wrong-MIME failure, and the sendMessage-vs-updateModelContext distinction
placed after the method list) is compressed into NB03, keeping only the
single fact a general audience needs and can act on — the two silent
causes of the same blank rectangle — and dropping the tooling-internals
gaps (the Desktop cache-flush requirement, the frameDomains restriction,
the sendMessage/updateModelContext placement complaint) that assume a
technical audience simple/hai-simple doesn't target; Teardown framing
("gets it right," "where it bites") is stripped to a plain
mechanism-and-consequence description, per the NO JUDGMENT register check;
BVDT's verdict facts (the two-part split, and the shared silent-failure
mode) are merged into the single BCRY carry-out sentence rather than kept
as a separate bulleted artifact card, per CARRY-OUT LAW; BHTF kept as the
your-turn handoff, with the source's prompt ("Build an MCP app with a file
picker widget that lets users select a file from a list returned by a
directory scan tool") carried over near-verbatim and all four of its watch
points kept — it was already a concrete, paste-ready prompt needing no
extra setup, so it's actually runnable by any viewer today; BOUT kept,
re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY +
BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`BuildMcpAppAnatomy` / `BuildMcpAppDecision` / `BuildMcpAppTell` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
