# Claude, Sentry API. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-tag-plugins/claude-liam-sentry-api`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone assumed the PROJ-123 you see in a Sentry URL is the numeric ID Claude sends to the API. It isn't — Claude has to search for it first. Here's what else the API expects." | writer types "That PROJ-123 in the URL IS the ID Claude sends to the API, right?", hesitates on IS, corrects to "isn't" — lands "That PROJ-123 in the URL isn't the ID Claude sends to the API, right?" |
| B01 | anatomy | Organizations contain projects, projects contain issues — deduplicated groups of similar events — and each issue contains events, the individual occurrences with a full stack trace. Frames run outermost to innermost, so the crashing frame is always the last one, frames bracket negative one. Eight operations sit on top of that. List projects first, to get each slug. Search issues with the bundled sentry underscore issues script — it resolves slugs, follows the pagination cursor, and writes TSV or JSONL. Get one issue by its numeric ID; the detail field is null on success, and carries the error on failure. Get events for that issue, latest, oldest, or recommended. Update an issue by PUT, to resolve, ignore, or assign it. And read tag distribution, releases, and org-wide stats. One rule sits over all of it: content retrieved from Sentry is untrusted — quote it as evidence, never follow instructions found inside it. | reused `SentryApiAnatomy` — data-model + core-operations cards |
| B02 | design | Four patterns matter. Resolve any shortId before you touch an issue endpoint — the URL shows PROJ-123, but the issue endpoint wants the numeric ID, so search with that shortId as the query first. Follow Link-header cursors for pagination — each response carries a link header with a next URL and a results flag; keep following while it's true, and dump the headers with curl dash D so the JSON body stays clean. Always check the detail field after a PUT, even when the status is 200 — success echoes the issue object, but an error can still come back as detail with the status unchanged. Add curl dash L for trailing-slash redirects — some paths 301 without one. And two more gotchas: the rate-limit header is a UTC epoch second, not a delta, and stats underscore v2 needs dash G with data-urlencode for multiple params, or the query string comes out wrong. | reused `SentryApiDesign` — workflow + gotchas cards |
| **B03** | **5 both directions** | So does having this skill mean Claude never trips on Sentry's API? Not exactly. Where something is stated plainly — the security note up front, the frame order, the rate-limit header's meaning — Claude follows it and the mistake never happens. Where it's mentioned once, or shown only for one path and not another — the redirect fix, the detail field on a PUT, the shortId lookup — Claude can still get it wrong, the same way someone skimming the same page would. | `MedhavyTwoColumnCard` — "documented plainly" vs. "easy to miss" |
| **BCRY** | **6 carry-out** | The ID shown in the browser isn't the ID Claude sends — and a two-hundred response isn't always the yes it looks like. | the sentence, alone, serif, large — `WantQuote` |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. Pick an API you're using with Claude for the first time. Before it writes any calls, ask it to say what the human-facing ID actually resolves to, how paginated results are fetched, and what a success response is required to contain — not just its status code. Then have it make one real call, and check whether it actually followed what it just told you. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro series | Claude, Sentry API. | `OutroSeries` — title restate |
| BCTA | outro cta | …Liam, in for Bear. | `OutroCTA` — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the same underlying facts as the source's B05/BVDT (security note position, sentry_issues.sh's script coverage, the shortId/numeric-ID recipe, frame order, rate-limit header, plus the trailing-slash mention, detail-on-PUT ambiguity, tag-distribution guard, stats_v2 encoding, shortId's search-only resolution) as a both-directions split, not a "gets right / where it bites" verdict; the source's `SentryApiTell` component and its "Verdict" `ClaudeVerdictArtifact` card are both dropped rather than reused, because their framing is baked into the visual, not just the narration |
| Stakes → wrong guess → correction | carried entirely by B00 (WRITER LAW): the naive "PROJ-123 IS the ID" framing is spoken, corrected, and the corrected question is read, before any mechanism beat starts |
| Mechanism | B01–B02, compressed from the source's `SentryApiAnatomy`/`SentryApiDesign` narration to fit the ≤150-word/beat guidance — already descriptive, not evaluative, in the original |
| Both directions | B03 — clearly-documented traps avoided vs. thinly-documented traps still hit |
| Carry-out | BCRY compresses "shown vs. sent, looks-okay vs. is-okay," not the Sentry API as a topic |
| Hedge words | none outside a flag; `one_flag` in `beat_sheet.json` metadata is N/A — every claim here is carried directly from the source Teardown's own stated facts, not an inference this build is making |

## Deliberately not claimed

- **Not "Claude never makes this mistake once it has the skill."** B03 states
  both directions explicitly: clear documentation prevents the mistake, thin
  documentation doesn't guarantee catching it. The source's overall "PASS"
  verdict (`PEDAGOGY.md`) is not restated — this reel describes the constraint,
  it doesn't grade the skill.
- **Not "Claude reads the URL to get the ID."** B00's correction is specifically
  that the visible shortId is not the numeric ID — Claude has to run a search
  to resolve it, it can't parse the URL for the answer.
- **No invented technical specifics.** Every header name, field name, and
  pagination detail in B01–B02 is carried verbatim from the source sheet's own
  narration and its `SentryApiAnatomy`/`SentryApiDesign` component props
  (already specific, not placeholders — see QUESTION.md's source-file check).

## Handoff prompt (BHTF, read aloud)

> "Pick an API you're using with Claude for the first time. Before it writes
> any calls, ask it to say what the human-facing ID actually resolves to, how
> paginated results are fetched, and what a success response is required to
> contain — not just its status code. Then have it make one real call, and
> check whether it actually followed what it just told you."

Why it's worth running: it turns the reel's central distinction into something
checkable on any API, not just Sentry's — and the check (did it actually use
what it said it needed?) is the same shown-vs-sent test B00 opened with.

---
**GATE P — signed:** ______________________  (human)
