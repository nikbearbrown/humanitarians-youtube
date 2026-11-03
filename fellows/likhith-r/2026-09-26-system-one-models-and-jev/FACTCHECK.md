# FACTCHECK — System One Models and Jev

Status: claims checked by Claude Code against TypeSafe's primary sources. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B03 | LLMs generate a string token by token | PASS | Launch post: "Sequential. Generates one token at a time" | — |
| 2 | B04 | Jev returns typed answers in parallel, in one pass | PASS | Launch post: "Parallel. Generates all outputs in a single query"; docs: questions "evaluated in parallel … in one go" | — |
| 3 | B04 | No parsing | PASS | Docs: "No text generation, no parsing" | — |
| 4 | B05 | Outputs follow the schema, so no type errors | PASS | Launch post: "The model never makes type errors" | — |
| 5 | B05 | Typed isn't always right | PASS | Follows from #4 — type-correct ≠ correct; confidence exists because answers can be wrong | Added as caveat |
| 6 | B06 | TypeSafe reports 70–500 ms | PASS | Launch post: "End-to-end response time is 70ms-500ms" | Attributed to TypeSafe |
| 7 | B06 | LLM calls often take seconds | CORRECTED | Launch post frames Jev as 40x–200x faster than LLMs; no single LLM figure shown | Softened to "often seconds", no number |
| 8 | B07 | Built for classify / route / score / extract, not chat or coding | PASS | Launch post: "classify, route, score, extract, or branch"; "not optimized for" chat/code | — |
| 9 | B08 | Every answer carries a calibrated confidence, trained with RLCD | PASS | Launch post: calibrated probabilities "Always"; "Reinforcement Learning for Calibrated Decisions (RLCD)" | — |
| 10 | B08 | Unsure answers can go to a human | PASS | Docs: confidence "your code can use to decide whether and how to act" | — |
| 11 | B09 | A tool for smart if-statements, not a chatbot replacement | PASS | Launch post: "smart if-statements" | — |
