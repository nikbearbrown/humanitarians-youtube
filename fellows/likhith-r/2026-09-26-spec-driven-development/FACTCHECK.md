# FACTCHECK — Spec-Driven Development

Status: claims checked by Claude Code against the GitHub Spec Kit post. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | Prompt-only projects break as they grow, in hard-to-explain ways | CORRECTED | GitHub: code "looks right, but doesn't quite work", "misses the actual intent" | Framed as the hook, examples labelled illustrative |
| 2 | B03 | Spec-driven = requirements first; the spec is the source of truth | PASS | GitHub: the spec "is a contract for how your code should behave and becomes the source of truth" | — |
| 3 | B04 | A spec reduces guesswork; the model builds what you meant | PASS | GitHub: a vague prompt "forces the model to guess at potentially thousands of unstated requirements" | — |
| 4 | B05 | Review changes against the spec | PASS | GitHub: checkpoints "to critique what's been generated, spot gaps, and course correct" against the spec | — |
| 5 | B06 | The spec is living documentation, versioned with the code | PASS | GitHub: specs are "living, executable artifacts that evolve with the project"; Spec Kit keeps specs in the repo | — |
| 6 | B07 | Code not in the spec stands out (drift) | PASS | GitHub: "When something doesn't make sense, you go back to the spec" — derivation: a spec gives a reference to compare against | — |
| 7 | B08 | Specs keep fast AI coding maintainable | EXEMPT | Thesis of the reel (requester's close); qualitative sketch labelled, no data implied | — |
