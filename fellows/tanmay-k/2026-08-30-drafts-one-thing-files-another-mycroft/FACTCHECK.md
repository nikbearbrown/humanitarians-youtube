# FACTCHECK — Morgan Stanley's AI Drafts One Thing and Files Another

Week 20 work video · Tanmay Kulkarni, in for Humanitarians AI

Every claim the film makes on screen or in narration, with what was checked and how. Re-run
2026-08-30 against the primary source and the repository; **12/12 verified mechanically**, not
by re-reading.

Two sources only: Morgan Stanley's own 26 June 2024 press release, fetched directly from
`morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch`; and the reference
implementation `morgan_stanley_reference/`, which runs and is filed in the **Mycroft
repository** alongside this series' case study.

---

## Claims about Morgan Stanley

| # | Claim | Verified | How |
|---|---|:---:|---|
| 1 | The release says Debrief "creates an email for an Advisor to edit and send at their discretion" | ✅ | substring match against the fetched page |
| 2 | The release says it "saves a note into Salesforce" | ✅ | substring match against the fetched page |
| 3 | The word **"drafts" appears nowhere** in the release | ✅ | 0 occurrences, case-insensitive |
| 4 | The word **"follow-up" appears nowhere** in the release | ✅ | 0 occurrences, case-insensitive |
| 5 | "98% of Financial Advisor **teams** have adopted the Assistant" | ✅ | verbatim in the release |
| 6 | The 20%→80% retrieval figure is **OpenAI's**, not Morgan Stanley's | ✅ | traced to OpenAI's case study, cited separately on frame |

**Claim 3 and 4 are the film's central evidence.** The case study this project started from
renders the middle clause as *"drafts a follow-up email"*. The release does not. "Drafts"
implies an incompleteness Morgan Stanley's own verb does not carry, which is why the
paraphrase was *easier* to read correctly than the original — the point B06B is built on.

### The scoping claim, stated narrowly on purpose

| # | Claim | Verified | How |
|---|---|:---:|---|
| 7 | The Salesforce save is the only one of Debrief's outputs confirmed **finished** rather than waiting on an adviser | ✅ | the case study's §4 table marks **five** steps `Autonomous (confirmed function)`; only the note-save is `Autonomous, confirmed complete` |

The film does **not** say "the only thing either tool does on its own." That phrasing was in an
earlier cut and was removed before build — see `PROOF-REVIEW-PREBUILD.md` F1. Debrief also
transcribes and generates notes autonomously; so does the Assistant when it retrieves and
synthesises. The distinction is *completed action on a system of record*, and it is narrow
deliberately.

## Claims about the reference implementation

| # | Claim | Verified | How |
|---|---|:---:|---|
| 8 | 29 tests across 10 files, all passing | ✅ | counted and executed: 29/29 |
| 9 | 12 source modules, 2 pipelines | ✅ | file count, excluding tests and `__init__.py` |
| 10 | The assertion exists at `tests/test_orchestrator_debrief.py:30` | ✅ | `assert result["email_status"] != result["salesforce_note_status"]` — on screen **verbatim**, including the dict access |
| 11 | `write` is guarded on the Debrief modules only | ✅ | forbidden-word lists diffed across all 4 test files |
| 12 | No forbidden name exists in any of the four terminal modules | ✅ | full list re-run against all four: 0 hits |

**Claim 10 was corrected late.** The plate previously showed a tidied
`assert email_status != salesforce_note_status` under a file-and-line citation, which implies
verbatim quotation. The dict access changes no meaning — unlike the drafts/creates paraphrase
this film is about — but a film arguing you must quote your source precisely cannot paraphrase
its own. Fixed in both cuts and both descriptions.

**Claims 11 and 12 together are the film's second-pass finding**, and they must be read as a
pair: the property holds everywhere (12), but it is only *enforced* on half the modules (11).
The code is correct; the coverage is not. The film says exactly that and no more.

## What the film does not claim

- **Not a disclosure of Morgan Stanley's architecture.** The repository runs on fabricated
  mock data with no connection to any Morgan Stanley system, and says so on the outro plate.
- **No mechanism claim.** Morgan Stanley publishes what the tools produce, not how they work.
  The film states this as normal for a bank rather than as a criticism.
- **No claim that the `write` gap has caused a failure.** It has not. B11 concedes there is no
  failure to show, and that the argument is about risk.
- **No independent audit.** Every Morgan Stanley figure is self-reported by the firm or by
  OpenAI. Nothing here was verified against a third party.

## Provenance note

The project initially worked from this series' own case study, which cites the release. That
is a reading of a source, not the source. The primary was fetched during the pre-build review
(`PROOF-REVIEW-PREBUILD.md` F3), and doing so changed the film rather than tidying a citation
— see claims 3 and 4.
