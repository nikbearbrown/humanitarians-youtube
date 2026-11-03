# Claude, Grafana API. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-tag-plugins/claude-liam-grafana-api`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone assumed Claude already knows how to work with an outside system like Grafana's API. Not quite — it gets shown, in a file it reads before acting. Here's what that file actually has to spell out." | writer types "Claude already KNOWS how APIs like Grafana work, right?", hesitates on KNOWS, corrects to "has to be shown" — lands "Claude already has to be shown how APIs like Grafana work, right?" |
| B01 | anatomy | Grafana's REST API uses three different time formats depending on the endpoint, and picking the wrong one doesn't return an error — it just comes back empty. The datasource query endpoint and annotations both want Unix milliseconds. State-history wants Unix seconds. Silences want RFC-3339, and the example command only works with GNU date — macOS's built-in date needs a different flag. Every request also carries a role: Viewer, Editor, or Admin — a 403 means the identity is missing the role that call needs. Reading dashboards and querying data only takes Viewer; writing alert rules or silences takes Editor or higher. Datasource query responses come back as Grafana's own frame format, not raw Prometheus JSON — a failure lands inside the response itself, in results dot ref-id dot error, with the HTTP status still reading 200. There's also a one-line helper that wraps the bearer token for you, but it only lives for the session — it isn't saved anywhere. | reused `GrafanaApiAnatomy` — time-format-by-endpoint cards + role model / data-frame / helper cards |
| B02 | design | Alert rules live on two separate surfaces. The Prometheus API gives live state — firing, pending, or inactive — read only. The provisioning API gives the rule's definition: the query, the condition, the labels — full create, update, and delete, but anything written through it is locked in the Grafana UI unless the request adds a header telling Grafana to disable that lock. Dashboards work differently again: there's no partial update, only get the whole thing, change it, and post the whole thing back — leave out the version number and Grafana returns a conflict instead of guessing which copy wins. Datasource queries fan out to the underlying database on every single call, so the design here is to batch several queries into one request instead of looping separate calls. And the annotations endpoint has no page parameter at all — for a long time window, the fix is narrowing the window, not paging through it. | reused `GrafanaApiDesign` — two alert-surface cards + design-gotcha cards |
| **B03** | **5 both directions** | So does having this file mean Claude never trips on Grafana's API? Not exactly. Where the file spells something out plainly — the time-format warning up front, the exact field to check on a datasource error — Claude follows it and skips the mistake entirely. Where it's one line, or buried after the read-only examples, Claude can still get it wrong, the same way a person skimming the same page would. | `MedhavyTwoColumnCard` — "documented plainly" vs. "easy to miss" |
| **BCRY** | **6 carry-out** | A skill doesn't make Claude know an API. It gives Claude a map of where the traps are — and Claude only avoids the ones the map actually marks. | the sentence, alone, serif, large — `WantQuote` |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. Pick an API you've never used with Claude before, even a small public one. Before you let it write any code, ask it to list the three things it would need confirmed first: how requests are authenticated, how paginated results come back, and any known regional or format quirk. Then have it write the first real call, and check whether it actually used what it just told you it needed. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro series | Claude, Grafana API. | `OutroSeries` — title restate |
| BCTA | outro cta | …Liam, in for Bear. | `OutroCTA` — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the same underlying facts as the source's B05/BVDT (the time-format warning up front, the named error field, the session-only helper, the GNU/BSD date gap, the buried provisioning-lock header, the literal "grafana" path segment) as a both-directions split, not a "gets right / where it bites" verdict; the source's `GrafanaApiTell` component and its "Verdict" `ClaudeVerdictArtifact` card are both dropped rather than reused, because their framing (and their `GETS_RIGHT`/`BITES` content) is hardcoded into the visual, not just the narration |
| Stakes → wrong guess → correction | carried entirely by B00 (WRITER LAW): the naive "Claude already knows" framing is spoken, corrected, and the corrected question is read, before any mechanism beat starts |
| Mechanism | B01–B02, reused verbatim from the source (`GrafanaApiAnatomy`, `GrafanaApiDesign`) — already descriptive, not evaluative, in the original narration |
| Both directions | B03 — clearly-documented traps avoided vs. thinly-documented traps still hit |
| Carry-out | BCRY compresses "read vs. know, mapped vs. unmapped," not the Grafana API as a topic |
| Hedge words | none outside a flag; `one_flag` in `beat_sheet.json` metadata is N/A — every claim here is carried directly from the source Teardown's own stated facts, not an inference this build is making |

## Deliberately not claimed

- **Not "Claude never makes this mistake once it has the skill."** B03 states
  both directions explicitly: clear documentation prevents the mistake, thin
  documentation doesn't guarantee catching it. The source's overall verdict is
  not restated — this reel describes the constraint, it doesn't grade the
  skill.
- **Not "Claude was trained on Grafana's API."** B00's correction is
  specifically that Claude is *shown*, in a file it reads before acting — not
  that it already possessed this knowledge from training.
- **No invented technical specifics.** Every time format, role, endpoint, and
  design gotcha in B01–B02 is carried verbatim from the source sheet's own
  narration and its `GrafanaApiAnatomy`/`GrafanaApiDesign` component props
  (already specific, not placeholders — see QUESTION.md's source-file check).

## Handoff prompt (BHTF, read aloud)

> "Pick an API you've never used with Claude before, even a small public one.
> Before you let it write any code, ask it to list the three things it would
> need confirmed first: how requests are authenticated, how paginated results
> come back, and any known regional or format quirk. Then have it write the
> first real call, and check whether it actually used what it just told you it
> needed."

Why it's worth running: it turns the reel's central distinction into
something checkable on any API, not just Grafana's — and the check (did it
actually use what it said it needed?) is the same read-vs-know test B00
opened with.

---
**GATE P — signed:** ______________________  (human)
