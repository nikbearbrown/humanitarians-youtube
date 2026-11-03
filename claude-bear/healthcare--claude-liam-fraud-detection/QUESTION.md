# QUESTION.md — healthcare--claude-liam-fraud-detection

**Mode:** redo. There is no literal asked question — this reel re-registers
an existing Teardown reel (`claude-liam-fraud-detection`, a skill-teardown
walk through the Anthropic `fraud-detection` Claude Skill from the
`healthcare` book's plugin set) into the Plain register for
@HumanitariansAI, per hai-simple's redo contract.

**The question this reel answers**, framed as a newcomer would ask it:

> When Claude screens a pile of Medicare/Medicaid claims for fraud, does it
> decide which providers committed fraud, or just flag candidates for a
> person to investigate?

**The naive framing (what B00 types and corrects):** "Does Claude convict
fraudulent claims?" — the newcomer's assumption is that Claude renders a
fraud determination, like a verdict. It doesn't. `fraud-detection` screens
a Medicare/Medicaid claims corpus and produces ranked, fully-cited
investigation referrals for an SIU / program-integrity team — it flags and
ranks candidates; it never decides guilt. That correction ("convict" →
"flag") is the wrong-guess pedagogy per WRITER LAW.

**Source facts carried over unchanged** (from
`/Users/nik/Documents/books/anthropics/healthcare/youtube/claude-liam-fraud-detection/beat_sheet.json`):
a skill is a folder Claude reads before it works, containing eight files
(ARCHITECTURE.html, claims-schema.sql, LOAD-CLAIMS.md, package.json,
PROPOSE-DETECTORS.md, README.md, REFERENCE-DATA.md, SKILL.md) — SKILL.md is
the instruction set; the skill's job is to screen a Medicare/Medicaid
claims corpus for fraud, waste, and abuse and produce ranked, fully-cited
investigation referrals for an SIU / program-integrity team; used when
asked to run a fraud sweep, screen claims for FWA, find billing anomalies,
or generate investigation referrals over a claims dataset; the pipeline
relays one output — a ranked list of referrals, each carrying the
provider's NPI, the suspected scheme, the dollar exposure, and a confidence
score; same input produces the same output every run; the skill only
handles what its file specifies, and it does not decide whether fraud
occurred — that call stays with the SIU / program-integrity team.
