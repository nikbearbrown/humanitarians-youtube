# Fact Check — How AI Hallucinations Happen

| Planned claim | Source | Check and wording limit |
|---|---|---|
| A hallucination is an answer containing false or unsupported information, sometimes confidently presented. | NIST AI 600-1 §2.2; Li et al. ACL 2024 | Keep the definition simple; NIST's term is “confabulation,” also colloquially called hallucination. Do not suggest that fluent style proves confidence or truth. |
| Autoregressive language models generate by predicting tokens from learned patterns. | Brown et al. (2020); NIST AI 600-1 §2.2 | Explain as a simplified description of language-model generation. Do not imply that every AI model works this way. |
| Ordinary generation does not automatically check each new claim against a trusted source. | NIST AI 600-1 §2.2; Lewis et al. (2020) | Qualify: generation without an added verification or retrieval tool. Products may include tools; their presence does not guarantee correct verification. |
| A plausible-sounding answer may still be false or unsupported. | NIST AI 600-1 §2.2 | NIST notes statistical prediction can yield accurate text or inaccurate/inconsistent text, and that confident false content may mislead users. |
| Incorrect outputs matter when people act on them, particularly in consequential contexts. | NIST AI 600-1 §2.2 | Do not overstate prevalence or claim a specific rate. The video mentions consequential decisions generally, not a quantified risk. |
| Retrieval/grounding can help by supplying external passages to generation. | Lewis et al. (2020) | Paper demonstrates the approach on evaluated knowledge-intensive tasks, not universal success. Narration says “can bring relevant documents” and “reduces risk; cannot guarantee truth.” |
| Important claims should be checked against reliable sources; useful context can help. | Practical guidance consistent with NIST risk discussion and evidence-grounded generation research | Present as prudent user practice, not as a scientifically quantified intervention or guarantee. |
| Bellora's capital is “Lumen” in the example. | **Fiction invented for this video only.** | Both names are expressly called fictional. Do not present this as a real country, actual model output, or sourced fact. |

## Claims excluded

No hallucination rates, benchmark scores, fabricated quotations, real-world anecdotal examples, named product accusations, or claims that hallucinations can be eliminated are included.
