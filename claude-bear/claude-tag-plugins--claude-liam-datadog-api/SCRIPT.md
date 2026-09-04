# Claude, Datadog API. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-tag-plugins/claude-liam-datadog-api`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone assumed Claude already knows how to work with an outside system like Datadog's API. Not quite — it gets shown, in a file it reads before acting. Here's what that file actually has to spell out." | writer types "Claude already KNOWS how APIs like Datadog work, right?", hesitates on KNOWS, corrects to "has to be shown" — lands "Claude already has to be shown how APIs like Datadog work, right?" |
| B01 | anatomy | The Datadog API splits in two by what you're asking for, not by which version is newer. v1 covers metrics, monitors, dashboards, and service levels. v2 covers logs, traces, incidents, and session data. Two headers ride on every request Claude sends: one says which account you're in, one says who you are and what you're allowed to touch. The sharpest trap is regional — Datadog runs several separate regional addresses, and calling the wrong one returns a flat permission error even with valid keys. The skill's fix: set the region first, then make one throwaway call — the validate endpoint — just to confirm it before doing anything real. | reused `DatadogApiAnatomy` — v1/v2 resource cards + header/site setup rows |
| B02 | design | Long results come back a page at a time, and Datadog uses three different schemes for that, depending which endpoint you're calling. Logs, events, and traces hand back a cursor — pass it forward, and stop once it's empty. Monitors use a page number instead. Incidents and users use a page size and offset. Two more things Claude has to track: one endpoint wraps its results one layer deeper than the rest, so the exact same shape of request needs extra nesting most other endpoints skip — miss it, and the error that comes back doesn't say which field was wrong. And updating a dashboard replaces the whole document: leave a widget out of the update, and it's gone, not skipped. | reused `DatadogApiDesign` — pagination scheme cards + JSON:API gotcha cards |
| **B03** | **5 both directions** | So does having this file mean Claude never trips? Not exactly. Where the file spells something out plainly — the region check, the exact error text a missing flag produces — Claude follows it and skips the mistake entirely. Where it's buried in one line, or never flagged as a trap at all, Claude can still get it wrong, the same way a person skimming the same page would. | `MedhavyTwoColumnCard` — "documented plainly" vs. "easy to miss" |
| **BCRY** | **6 carry-out** | A skill doesn't make Claude know an API. It gives Claude a map of where the traps are — and Claude only avoids the ones the map actually marks. | the sentence, alone, serif, large — `WantQuote` |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. Pick an API you've never used with Claude before, even a small public one. Before you let it write any code, ask it to list the three things it would need confirmed first: how requests are authenticated, how paginated results come back, and any known regional or versioning quirk. Then have it write the first real call, and check whether it actually used what it just told you it needed. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro series | Claude, Datadog API. | `OutroSeries` — title restate |
| BCTA | outro cta | …Liam, in for Bear. | `OutroCTA` — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the same underlying facts as the source's B05/BVDT (only one bundled script, the one-line dashboard warning, the unflagged envelope asymmetry) as a both-directions split, not a "gets right / where it bites" verdict; the source's `DatadogApiTell` component and its "Verdict" `ClaudeVerdictArtifact` card are both dropped rather than reused, because their framing is baked into the visual, not just the narration |
| Stakes → wrong guess → correction | carried entirely by B00 (WRITER LAW): the naive "Claude already knows" framing is spoken, corrected, and the corrected question is read, before any mechanism beat starts |
| Mechanism | B01–B02, reused verbatim from the source (`DatadogApiAnatomy`, `DatadogApiDesign`) — already descriptive, not evaluative, in the original narration |
| Both directions | B03 — clearly-documented traps avoided vs. thinly-documented traps still hit |
| Carry-out | BCRY compresses "read vs. know, mapped vs. unmapped," not the Datadog API as a topic |
| Hedge words | none outside a flag; `one_flag` in `beat_sheet.json` metadata is N/A — every claim here is carried directly from the source Teardown's own stated facts, not an inference this build is making |

## Deliberately not claimed

- **Not "Claude never makes this mistake once it has the skill."** B03 states
  both directions explicitly: clear documentation prevents the mistake, thin
  documentation doesn't guarantee catching it. The source's overall "PASS"
  verdict (`PEDAGOGY.md`) is not restated — this reel describes the constraint,
  it doesn't grade the skill.
- **Not "Claude was trained on Datadog's API."** B00's correction is specifically
  that Claude is *shown*, in a file it reads before acting — not that it already
  possessed this knowledge from training.
- **No invented technical specifics.** Every header name, trap, and pagination
  scheme in B01–B02 is carried verbatim from the source sheet's own narration
  and its `DatadogApiAnatomy`/`DatadogApiDesign` component props (already
  specific, not placeholders — see QUESTION.md's source-file check).

## Handoff prompt (BHTF, read aloud)

> "Pick an API you've never used with Claude before, even a small public one.
> Before you let it write any code, ask it to list the three things it would
> need confirmed first: how requests are authenticated, how paginated results
> come back, and any known regional or versioning quirk. Then have it write the
> first real call, and check whether it actually used what it just told you it
> needed."

Why it's worth running: it turns the reel's central distinction into something
checkable on any API, not just Datadog's — and the check (did it actually use
what it said it needed?) is the same read-vs-know test B00 opened with.

---
**GATE P — signed:** ______________________  (human)
