# QUESTION — claude-tag-plugins--claude-liam-datadog-api

**Mode:** redo (`SUBJECT.json.mode == "redo"`).
**Source:** `anthropics/claude-tag-plugins/youtube/claude-liam-datadog-api/beat_sheet.json`
(Teardown register, 7 beats, `source_skill` field points at
`../anthropics/claude-tag-plugins/datadog/skills/datadog-api/SKILL.md`).

## Source-file check

`../anthropics/claude-tag-plugins/datadog/skills/datadog-api/SKILL.md` does **not**
exist on this machine (checked directly and via `find` across the whole
`claude-tag-plugins` tree — only `datadog-api`'s YouTube folder is present locally).
**Unlike the `claude-for-legal--*` sibling redos** (`fto-triage`,
`marketing-claims-review`, `material-contract-schedule`, …), this is not a
missing-content problem: the source `beat_sheet.json` carries no unfilled `>`
template placeholders. Every beat's `narration_text` is a complete, specific,
fully-written Teardown of the real Datadog API skill (resource split, header
names, regional-site 403 trap, `curl -g` requirement, three pagination schemes,
JSON:API envelope asymmetry, dashboard PUT behavior, the five things it documents
well and the five gaps). The missing file just means this build cannot
cross-check the source sheet against the original `SKILL.md` text directly — it
reuses the source sheet's own stated facts as the record, which is what the redo
contract calls for regardless.

## The question, translated for a newcomer

The source is written for an audience that already knows what a Claude Skill is
and wants a teardown of one specific skill's API quirks. `hai-simple`'s audience
is a newcomer to Claude. The redo contract requires keeping the source's
question, facts, and body argument — so the question is generalized to what a
newcomer is actually asking when they see Claude successfully call an unfamiliar
API for the first time:

> **Does Claude already know how an outside system like Datadog's API works, or
> does something have to tell it?**

The wrong guess a newcomer makes: that Claude's training already covers this —
it "knows" the API the way it knows common knowledge. The correction: Claude is
*shown* — it reads a Skill (a file) before acting, and that file is what carries
the account-specific, version-specific, and trap-specific detail training alone
would not reliably have.

## What carries over from the source (facts, unchanged)

- v1/v2 split by **resource type**, not by which is newer.
- Two headers travel on every call: one identifies the org, one identifies the
  user's permissions.
- Regional site is the sharpest trap: the wrong region returns a flat
  permission error even with valid credentials — the skill's fix is to set the
  region and validate before doing anything real.
- Bracketed query parameters need a specific curl flag or the request never
  sends.
- Three different pagination schemes apply to different groups of endpoints.
- Two JSON:API asymmetries (spans-vs-logs envelope depth, the events
  double-`.attributes` path) and the dashboard-PUT-replaces-everything
  behavior are real, documented gaps in how legible the skill makes its own
  traps — not a claim that the skill is poorly built overall.

## What changes (register, per the redo contract)

- **Teardown → Plain.** The source's B05 beat and its component
  (`DatadogApiTell`) are built around an explicit "what it gets right / where
  it bites" verdict frame, and the source's `BVDT` beat is a `ClaudeVerdictArtifact`
  card literally labelled "Verdict." Both are a design-quality judgment on the
  skill's documentation — exactly what Plain drops. This build keeps `B01`
  (`DatadogApiAnatomy`) and `B02` (`DatadogApiDesign`) reused verbatim — their
  narration was already descriptive, not evaluative — but replaces the B05/BVDT
  pair with a single **both-directions** beat (`MedhavyTwoColumnCard`, prop-driven,
  no baked-in verdict framing) stating the same underlying facts as two directions
  (documented plainly / easy to miss) rather than a grade, and a plain carry-out
  sentence (`WantQuote`) instead of a verdict card.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`
  (WRITER LAW).
- **Outro:** source's single `ClaudeTitleOutro` → the fixed hai-simple
  `OutroSeries` + `OutroCTA` split, Humanitarians AI skin.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
