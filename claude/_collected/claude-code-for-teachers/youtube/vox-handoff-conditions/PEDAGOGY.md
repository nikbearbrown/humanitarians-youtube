# PEDAGOGY AUDIT — vox-handoff-conditions

## Act structure map
| Act | Beats | Status |
|---|---|---|
| COLD OPEN | B01, B02 | Concrete: About page reviewed, pushed; student reports broken link three days later |
| THE QUESTION | B03 | Named on screen AND in narration |
| THE MECHANISM | B04, B05 | Three properties; weak vs strong pair |
| THE EXAMPLE | B06 | lint-html check against deployment — specific concrete case |
| THE IMPLICATION | B07 | Forward correction compounds context pollution |
| THE PRACTICE | B08, B09 | Revert-and-respecify; three-row practical card |
| RECAP | B10 | Specific, testable, binary — written before the step |

Act structure present and in order: PASS

## Cold open check
B01: concrete mystery — looks right, pushes, student emails three days later. No thesis.
B02: the failure mechanism shown — local dev passes, school server fails, same link.
PASS — no verdict before THE QUESTION beat.

## Gap formula check
B03 card: "Exit 0. Looks good. Link broken three days later. Why?"
Narration: "Here is the question. Reviewing the output visually and verifying exit zero should be sufficient to catch link failures before deployment. Here is the case where a link passed both checks and failed in production. Why?"
Named on screen AND in narration: PASS

## Utility-framing lint
Scan for "is critical for" / "important to understand" / "we'll cover" / "in this video":
- None found. Mystery framing throughout. PASS

## Vocabulary law
- "handoff condition" debuts B04 — after B01-B02 show the failure mode that needs a name. PASS
- "revert-and-respecify" and "/rewind" debut B08 — after B07 shows why forward correction fails. PASS
Vocabulary law: PASS

## Anchor-not-transcript check
| Beat | On screen | Narration |
|---|---|---|
| B03 | "Exit 0. Looks good. Link broken three days later. Why?" | "Here is the question. Reviewing the output visually..." |
| B10 | "Not 'looks good.' A specific, testable, binary condition written before the step." | "Exit zero is not a handoff condition. Looks good is not a handoff condition..." |
On screen is anchor phrase; narration carries the full sentence. PASS

## Equations check
No equations. PASS

## Recap endcard
B10: question → answer. "Not 'looks good.' A specific, testable, binary condition written before the step." Topic: "CLAUDE CODE FOR TEACHERS". No chapter number, no book title. PASS

## Example act (16:9)
B06: lint-html against deployment — specific, concrete, shows the command that would have caught the bug. PASS

## Practice present (takeaway law)
B09: three-row practical card — write condition before approving; if fails, /rewind; two failures, /clear. Concrete and checkable. PASS

## Simulation-first check
B02 (link failure): two columns animate showing local vs server — the failure is shown as diverging states. PASS
B04 (three properties): rows draw in with teal checks, then crimson X column for "looks good" — the comparison is staged. PASS
B05 (weak vs strong): two-column table fills with weak entries then strong entries — animated comparison. PASS
B07 (context pollution): context bar fills with crimson segments as failures accumulate. PASS
Simulation-first: PASS

## Length law
10 beats × ~11.3 s average = ~113 s = 1:53. Within 5:00 cap. PASS

## Length band match
Card specifies 2-3 min. Derived duration ~1:53-2:20 after audio lock. PASS

VERDICT: PASS
