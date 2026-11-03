# FACTCHECK — Why AI-Generated Code Still Needs a Human Who Understands the System

Status: **Open, but not blocking** — this video makes no claim that requires an external source. It teaches a rubric (editorial framework) and applies it to a generic illustrative example, not a claim about a specific real system.

| # | Beat | Claim (as spoken/shown) | Verdict | Note |
|---|---|---|---|---|
| 1 | B00 | A fix that "looks right" (escaped quotes) can still crash production | PASS (illustrative) | Generic, well-known failure mode of ad-hoc string escaping; not attributed to a specific system |
| 2 | B01 | The 3-question rubric (Trace / Consequence / Why) | PASS (editorial framework, not an empirical claim) | Reusable method, not a factual claim requiring a citation |
| 3 | B02 | Worked example: hand-escaped SQL insert vs. parameterized-query fix | PASS (illustrative, explicitly generic) | See "No-fabrication note" below — deliberately not sourced to a real incident |
| 4 | B02 | "One unescaped special character crashes the whole batch insert" | PASS (illustrative, generic failure mode) | Standard, well-documented behavior of string-concatenated SQL vs. parameterized queries; not a claim about a specific vendor/codebase |
| 5 | B03 | A date-formatter function is low-stakes / doesn't need the same scrutiny | PASS (editorial framing) | Illustrative falsifiability case, not an empirical claim |
| 6 | B04 | The 3-step viewer task | PASS (editorial scaffold, not an empirical claim) | Concrete, repeatable procedure — not "ask your AI tool" |
| 7 | B05 | Closing thesis: "the code that looks right and the code that is right aren't always the same thing" | PASS (editorial framing) | Restates the teachable claim; not an empirical claim |

## No-fabrication note (worked example, B02)

An earlier draft considered sourcing the B02 worked example from this fellow's
real Project 29 (`mycroft`) engineering work — a matching real bug/fix exists
there (a hand-rolled quote-escaping insert vs. a parameterized-query fix).
That real fix was explicitly set aside by the fellow, both because her
sibling weekly-report video already reserved it as "a candidate for a future
episode, not this one" (see that project's `PEDAGOGY.md`), and because this
is a general-AI-topic film, not a Project 29 engineering report.

**Decision (2026-08-17, fellow):** use a generic, illustrative version of the
same code pattern instead. No beat in this video claims the worked example
comes from a real codebase or incident — `scenes.py` (when authored) and the
narration must not name a real repo, company, or system for B02. If a future
revision wants to use the real fix as evidence, it needs its own `SOURCES.md`
entry citing the real file paths and a fresh fact-check pass — see
`BUILD-LOG.md`.

## Balance check

No claim in this script is empirical in a way that requires external
verification — the video teaches a method and demonstrates it on a labeled
generic example, which is the deliberate design (see falsifiability case,
B03). Nothing here asserts a fact about any real product, vendor, or
incident.
