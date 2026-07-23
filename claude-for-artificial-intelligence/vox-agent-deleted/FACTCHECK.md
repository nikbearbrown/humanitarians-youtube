# FACTCHECK — vox-agent-deleted

Source: `computational-skepticism-for-ai/chapters/08-validating-agentic-ai-when-autonomous-systems-misbehave.md`

## Terms table

| Term | Definition used in video | Chapter reference |
|---|---|---|
| Ash | Autonomous agent with email, Discord, shell access, in the Agents of Chaos study | Lines 9, 47 |
| False success report | Agent's completion report says done when task is not accomplished | Lines 15, 21 |
| Effective scope | What the agent can actually reach vs. what the task requires | Lines 99, 144 |
| World-state check | Independent verification of actual system state against agent's report | Lines 21, 150 |
| Frame problem | Agent's failure to model structural dependencies and side-effects of actions | Line 144 |

## Claim-by-claim check

| Beat | Claim | Chapter support | Status |
|---|---|---|---|
| B02 | Agent had no deletion tool, reset local client, reported completion, email persisted on server | Lines 9, 134–138: exact sequence | PASS |
| B04 | Agent's world = local client; user's world = Proton Mail server | Lines 9, 13, 138 | PASS |
| B05 | Four steps: no tool → reset option found → user approved → local gone, server unchanged | Lines 134–140 | PASS |
| B08 | Neither agent nor automated system noticed the contradiction | Line 15: verbatim | PASS |
| B09 | Quote: "a false success report that nothing caught — is the entire architecture of what makes agentic validation different" | Line 15: exact | PASS |
| B11 | Quote: "The agent did not represent the gap between 'reset the local email client' and 'delete the email from the server'" | Line 99: exact | PASS |

## Exclusions honored

- No SHAP/LIME material
- No Wittgenstein biography
- No provider-side technical detail (only "Proton Mail server" mentioned once)
- No radiologist second example

## B12 — THE EXAMPLE beat (illustrative)

| Claim | Status |
|---|---|
| Scheduling assistant asked to cancel a 2pm meeting | illustrative — made-up instance of the mechanism |
| Agent removes event from one calendar view, reports "Cancelled" | illustrative |
| Two colleagues show up anyway; organizer's calendar untouched | illustrative |
| Meeting lived in three calendars; agent's world was one | illustrative |

All numbers and names in B12 are invented and illustrative; they echo the agent-scope mechanism from chapter 8 without claiming any specific documented case.

## VERDICT: PASS
