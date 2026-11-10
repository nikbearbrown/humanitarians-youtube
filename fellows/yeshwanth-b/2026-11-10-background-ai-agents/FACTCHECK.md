# FACTCHECK — Background AI Agents: How AI Works While You Don't

Each claim in the film, where it comes from, and how it was checked. Background references are listed in `SOURCES.md`.

| Beat | Claim | Source / check | Status |
|---|---|---|---|
| B00 | A chatbot answers a question; an agent takes a goal and returns finished work | supplied script (hook); standard definition | conceptual |
| B00 | "one of the biggest [shifts] in AI right now" | supplied script, softened from "the biggest AI trends of 2026" | opinion, labelled as such by phrasing |
| B00 | On-screen answer lines: 1 of 3 failing; month and day swapped; one-line fix; 3 of 3 passing | `evidence-run1.txt`, `evidence-fix.diff`, `evidence-run2.txt` | measured; composer labelled illustrative |
| B02 | A chatbot responds once per message; the user carries results back (the user is the loop) | supplied script | conceptual |
| B02 | An agent decides the next step, uses a tool, checks the result, repeats until the goal is met | supplied script; ReAct (Yao et al., 2022) | conceptual, sourced |
| B03 | Goal → plan → act (tools) → observe → repeat; the model is the brain, tools are the hands | supplied script; ReAct | conceptual, sourced |
| B03 | "A well-built agent caps the loop with a step limit or a budget" | design guidance, not a claim about any product | guidance |
| B04 | `python3 -m unittest -v` fails 1 of 3 with `(2026, 1, 3) != (2026, 3, 1)` | `evidence-run1.txt` (real run) | measured |
| B04 | The fix swaps `day, month` to `month, day` on one line | `evidence-fix.diff`; `git diff HEAD~1 --stat` = 1 file, +1 −1 | measured |
| B04 | After the fix, 3 of 3 pass | `evidence-run2.txt` (real run) | measured |
| B04 | The session around those outputs is a reconstruction; the fix was applied by a script during the build | on-screen note; `SOURCES.md` | disclosed |
| B05 | Background = cloud-hosted, asynchronous (assign, notified when done), can run in parallel | supplied script | conceptual |
| B05 | Example task types: code fix, research report, data cleanup, game assets | supplied script | as stated |
| B06 | What changed: dates.py, one line | `evidence-fix.diff` | measured |
| B06 | The tests went from 1 failing to 3 passing | `evidence-run1.txt`, `evidence-run2.txt` | measured |
| B06 | The fixed parser accepts "2026-02-30" and raises ValueError on "20260301"; no test covers either | `evidence-unchecked.txt`; `demo-repo/test_dates.py` | measured |
| B07 | Mistakes compound; prompt injection; cost of long loops; accountability | supplied script; OWASP LLM01 | conceptual, sourced |
| B08 | Hidden instructions in content an agent reads can try to redirect it; a model can't always tell data from instructions | OWASP LLM01 Prompt Injection | conceptual, sourced |
| B08 | The issue, the hidden line and the blocked `cat .env` | invented example | labelled illustrative on screen |
| B09 | Scoped goal with a definition of done; least privilege; human review before shipping; treat it as a junior teammate | supplied script; Saltzer and Schroeder (1975) for least privilege | guidance, sourced |
| B10 | Tasks with clear steps and a clear finish line suit agents; irreversible actions, the decision of what to build, and graded work stay with you | supplied closing line, extended | guidance |
| B11 | Chatbot: you drive the loop · Agent: it drives the loop · Background agent: it drives while you're away | supplied recap, verbatim in meaning | as stated |
| B12 | The Your Turn prompt | written for the film | prompt |

No product names, versions, prices or usage statistics are claimed.
