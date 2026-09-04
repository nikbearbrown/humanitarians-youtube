# QUESTION — claude-tag-plugins--claude-liam-grafana-api

**Mode:** redo (`SUBJECT.json.mode == "redo"`).
**Source:** `anthropics/claude-tag-plugins/youtube/claude-liam-grafana-api/beat_sheet.json`
(Teardown register, 7 beats, `source_skill` field points at
`../anthropics/claude-tag-plugins/grafana/skills/grafana-api/SKILL.md`).

## Source-file check

`../anthropics/claude-tag-plugins/grafana/skills/grafana-api/SKILL.md` does **not**
exist on this machine (checked directly and via `find` across the whole
`claude-tag-plugins` tree — only `grafana-api`'s YouTube folder is present
locally, same situation as the `datadog-api` sibling redo). This is not a
missing-content problem: the source `beat_sheet.json` carries no unfilled `>`
template placeholders. Every beat's `narration_text` is a complete, specific,
fully-written Teardown of the real Grafana API skill (three time formats by
endpoint, the role model, the two alert-rule surfaces, dashboard GET-then-
replace, query batching, and the five things it documents well plus the five
gaps). The missing file just means this build cannot cross-check the source
sheet against the original `SKILL.md` text directly — it reuses the source
sheet's own stated facts as the record, which is what the redo contract calls
for regardless.

## The question, translated for a newcomer

The source is written for an audience that already knows what a Claude Skill
is and wants a teardown of one specific skill's API quirks. `hai-simple`'s
audience is a newcomer to Claude. The redo contract requires keeping the
source's question, facts, and body argument — so the question is generalized
to what a newcomer is actually asking when they see Claude successfully call
an unfamiliar API for the first time (the same generalization used for the
`datadog-api` sibling, since both sources are Claude-plugin API teardowns
answering the identical underlying question):

> **Does Claude already know how an outside system like Grafana's API works,
> or does something have to tell it?**

The wrong guess a newcomer makes: that Claude's training already covers this
— it "knows" the API the way it knows common knowledge. The correction:
Claude is *shown* — it reads a Skill (a file) before acting, and that file is
what carries the account-specific, format-specific, and trap-specific detail
training alone would not reliably have.

## What carries over from the source (facts, unchanged)

- Three different time formats depending on the endpoint: Unix milliseconds
  for `/api/ds/query` and `/api/annotations`, Unix seconds for state-history,
  RFC-3339 for silences — wrong format returns *empty results*, not an error.
- A three-tier role model (Viewer / Editor / Admin); a 403 means the identity
  lacks the role the call needs.
- Datasource query responses come back as Grafana data frames, not raw
  Prometheus JSON; a datasource-side failure lands inside a 200 response, in
  `results.<refId>.error`.
- Two separate alert-rule surfaces: the Prometheus API (live state, read-only)
  and the provisioning API (definitions, full CRUD, UI-locked unless the
  request disables provenance).
- Dashboard updates are GET-then-full-replace, not a partial PATCH; a 412
  means a version conflict.
- `/api/ds/query` fans out to the underlying database per call, so the design
  guidance is to batch queries rather than loop.
- Real, documented gaps in how legible the skill makes its own traps — the
  session-only `grafana()` helper, the GNU/BSD `date` difference for silence
  timestamps, the provisioning-lock header buried after the read examples,
  the literal `grafana` path segment that reads like a placeholder, and
  `/api/annotations` having no page parameter — not a claim that the skill is
  poorly built overall.

## What changes (register, per the redo contract)

- **Teardown → Plain.** The source's `B05` beat and its component
  (`GrafanaApiTell`) are built around an explicit "what it gets right / where
  it bites" verdict frame (`GETS_RIGHT`/`BITES` arrays are hardcoded inside
  the component's JSX, not props), and the source's `BVDT` beat is a
  `ClaudeVerdictArtifact` card literally titled "Verdict." Both are a
  design-quality judgment on the skill's documentation — exactly what Plain
  drops, and exactly the same defect shape as the `datadog-api` sibling's
  `DatadogApiTell`/`BVDT` pair. This build keeps `B01` (`GrafanaApiAnatomy`)
  and `B02` (`GrafanaApiDesign`) reused verbatim — their narration and their
  components' fixed row content were already descriptive, not evaluative —
  but replaces the B05/BVDT pair with a single **both-directions** beat
  (`MedhavyTwoColumnCard`, prop-driven, no baked-in verdict framing) stating
  the same underlying facts as two directions (documented plainly / easy to
  miss) rather than a grade, and a plain carry-out sentence (`WantQuote`)
  instead of a verdict card.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`
  (WRITER LAW).
- **Outro:** source's single `ClaudeTitleOutro` → the fixed hai-simple
  `OutroSeries` + `OutroCTA` split, Humanitarians AI skin.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
