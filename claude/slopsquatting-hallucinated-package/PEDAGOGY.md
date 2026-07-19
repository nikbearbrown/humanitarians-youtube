# PEDAGOGY AUDIT — slopsquatting-hallucinated-package

---

## Act Structure

| Act | Beats | Present? |
|-----|-------|----------|
| COLD OPEN | B01 | YES — Fatima: Claude writes the import, pip install succeeds, attacker's code runs. Concrete (Fatima, OAuth, env vars), no thesis before B02. |
| THE QUESTION | B02 | YES — "A package that exists should be safe. Why did this one run the attacker's code?" Named on screen AND in narration. |
| THE PROBLEM | B03–B04 | YES — ~20% hallucinated names; 58% recur — predictable and targetable |
| THE MECHANISM | B05–B07 | YES — three-step attack; slopsquatting named; Fatima's default workflow is the exploit |
| THE PRACTICE | B08 | YES — verify on pypi.org/npmjs.com before every install |
| RECAP | B09 | YES — Claude's import is not verified; verify before installing |

Order confirmed correct. ✓

---

## Key-Case Cold Open

B01: Fatima asks Claude for OAuth tokens; Claude writes the import; pip install succeeds; attacker's code exfiltrates env vars. Concrete (Fatima, OAuth tokens, environment variables). No thesis before B02. ✓

---

## Gap Formula — THE QUESTION Beat (B02)

"A package that exists should be safe to install [X should predict Y]. This one existed — an attacker put it there [the case where it didn't]. Why did it run the attacker's code? [the question]"

On screen: "A package that exists should be safe to install. / Why did this one run the attacker's code?" ✓
In narration: "A student running pip install on a Claude-suggested package should be safe if the package exists. The package existed. An attacker put it there. Why does the install succeed and execute malicious code?" ✓

---

## Utility-Framing Lint

No "is critical for" / "important to understand" / "we'll cover" / "in this video" in narration. ✓
Mystery framing: the anomaly (package exists, install succeeds, attacker's code runs) opens the film. ✓

---

## Vocabulary Law

- "slopsquatting" — debuts B06 after B05 describes the three-step attack in full

No term before its setup. ✓

---

## Anchor-Not-Transcript Law

| Beat | On-screen | Narration | Redundant? |
|------|-----------|-----------|------------|
| B01 | "Claude writes: import requests_oauth_helper / pip install: succeeds. / Attacker's code runs." | Full Fatima story | No — card is the kicker; narration is the case |
| B02 | "A package that exists should be safe to install. / Why did this one run the attacker's code?" | Full question argument | No — anchor phrase vs full argument |
| B04 | "58% of hallucinated names / repeat across queries. / Attackers can predict them." | Full explanation of recurrence | No — card is the numbers; narration is the mechanism |
| B06 | "The hallucination is predictable. / Which means it is targetable." | Full slopsquatting definition | No — card is the compressed kicker; narration names the attack |
| B09 | "Claude's suggested import / is not a verified package. / Verify before you install." | Full recap | Near-match as endcard — acceptable |

All clean. ✓

---

## Simulation-First Check

B05 (three-step attack): three steps animate in sequence with arrows — model hallucinates → attacker registers → student installs → attacker's code runs. Each step appears as a chain. Process in time. ✓

B08 (practice): step-by-step defense — before pip install → open pypi.org → confirm exists → confirm maintained → then install. Process sequential with checkboxes. ✓

---

## Length Law

Estimated duration: ~168s ≈ 2:48. Within 2–3 min band. ✓

---

## Practice Present

B08: "Before you run pip install or npm install on any Claude-suggested package, open pypi.org or npmjs.com and verify the package exists, is the one you meant, and is maintained by who you think it is." Concrete (three named checks: exists, correct, maintained), checkable. ✓

---

VERDICT: PASS
