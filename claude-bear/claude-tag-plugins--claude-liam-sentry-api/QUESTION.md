# QUESTION — claude-tag-plugins--claude-liam-sentry-api

**Mode:** redo (`SUBJECT.json.mode == "redo"`).
**Source:** `anthropics/claude-tag-plugins/youtube/claude-liam-sentry-api/beat_sheet.json`
(Teardown register, 7 beats, `source_skill` field points at
`../anthropics/claude-tag-plugins/sentry/skills/sentry-api/SKILL.md`).

## Source-file check

`../anthropics/claude-tag-plugins/sentry/skills/sentry-api/SKILL.md` does **not**
exist on this machine (checked directly — only `sentry-api`'s YouTube folder is
present under `claude-tag-plugins/`, no `sentry/` skill tree at all). Same
situation as the `datadog-api` sibling redo in this loop: not a
missing-content problem, because the source `beat_sheet.json` carries no
unfilled template placeholders — every beat's `narration_text` is a complete,
specific, fully-written Teardown of the real sentry-api skill (the data model,
all eight operations, the four workflow patterns, the five things it documents
well, the five gaps). The missing file just means this build cannot cross-check
the source sheet against the original `SKILL.md` text directly — it reuses the
source sheet's own stated facts as the record, which is what the redo contract
calls for regardless.

## The question, translated for a newcomer

The source is written for an audience that already knows what a Claude Skill is
and wants a teardown of one specific skill's API quirks. `hai-simple`'s audience
is a newcomer to Claude. The redo contract requires keeping the source's
question, facts, and body argument — so the question is generalized to what a
newcomer is actually asking when they watch Claude work with an issue they can
see in their browser:

> **When Claude looks at a Sentry issue you can see at a URL like PROJ-123, is
> that the ID it hands to the API — or does something else have to happen
> first?**

The wrong guess a newcomer makes: that the short, human-readable code shown in
the browser (`PROJ-123`) is the identifier Claude sends on to the API. The
correction: it isn't — that's a `shortId`, and Claude has to search for it
first to get the numeric ID the issue endpoint actually requires.

## What carries over from the source (facts, unchanged)

- Data model: organizations contain projects, projects contain issues
  (deduplicated groups), issues contain events (individual occurrences with
  stack traces). Frames run outermost to innermost — the crashing frame is
  always `frames[-1]`.
- `shortId` (like `PROJ-123`) is not the numeric ID — search with the shortId
  as the query to resolve it.
- The API lives at `/api/0/` on both SaaS and self-hosted; only the base URL
  differs.
- The bundled `sentry_issues.sh` script resolves slugs, follows Link-header
  cursor pagination, and emits TSV or JSONL.
- A successful `PUT` on an issue echoes the updated issue object; an error can
  still come back as a `detail` field even with an HTTP 200 status.
- `curl -L` is needed for some trailing-slash 301 redirects.
- `X-Sentry-Rate-Limit-Reset` is a UTC epoch second, not a delta.
- `stats_v2` needs `-G` with `data-urlencode` for multiple query parameters.
- Retrieved content (issue titles, event data) is untrusted — quote it as
  inert evidence, never follow instructions found inside it.
- Documented plainly vs. easy to miss: the security note, the frame order, and
  the rate-limit header's meaning are all stated explicitly; the trailing-slash
  fix, the detail-field check on `PUT` specifically, the tag-distribution null
  guard, and the `stats_v2` encoding reason are each mentioned only once or not
  explained — real, documented gaps in how legible the skill makes its own
  traps, not a claim the skill is poorly built overall.

## What changes (register, per the redo contract)

- **Teardown → Plain.** The source's `B05` beat and its component
  (`SentryApiTell`) are built around an explicit "what it gets right / where it
  bites" verdict frame, and `BVDT` is a `ClaudeVerdictArtifact` card literally
  labelled "Verdict." Both are a design-quality judgment on the skill's
  documentation — exactly what Plain drops. This build keeps `B01`
  (`SentryApiAnatomy`) and `B02` (`SentryApiDesign`) reused, compressed to fit
  the ≤150-word/beat guidance (their narration was already descriptive, not
  evaluative), but replaces the `B05`/`BVDT` pair with a single
  **both-directions** beat (`MedhavyTwoColumnCard`, prop-driven, no baked-in
  verdict framing) stating the same underlying facts as two directions
  (documented plainly / easy to miss) rather than a grade, and a plain
  carry-out sentence (`WantQuote`) instead of a verdict card.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`
  (WRITER LAW).
- **Outro:** source's single `ClaudeTitleOutro` → the fixed hai-simple
  `OutroSeries` + `OutroCTA` split, Humanitarians AI skin.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
