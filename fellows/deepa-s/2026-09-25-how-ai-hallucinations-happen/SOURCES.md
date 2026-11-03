# Sources — How AI Hallucinations Happen

Sources checked 2026-09-25. These are technical/primary sources. No statistics or direct quotations are used in the narration.

1. **National Institute of Standards and Technology (NIST), _Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile_ (NIST AI 600-1, 2024).** [Official PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), especially §2.2, pp. 9–10. Defines “confabulation” (commonly called hallucination) as confidently presented erroneous or false content; explains that generative models approximate training-data distributions and that LLMs predict next tokens; discusses risks when people act on false outputs, including consequential decisions. Primary government technical profile.

2. **Tom B. Brown et al., “Language Models are Few-Shot Learners,” NeurIPS 2020.** [arXiv record and paper](https://arxiv.org/abs/2005.14165). Technical paper describing GPT-3 as an autoregressive language model and its next-token prediction setup. Used only as technical context for sequential token prediction, not as a claim about all AI systems.

3. **Patrick Lewis et al., “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks,” NeurIPS 2020.** [arXiv record and paper](https://arxiv.org/abs/2005.11401). Introduces models combining parametric generation with retrieved external passages. The paper reports a factuality improvement over its parametric-only baseline on the evaluated tasks; it also notes that provenance and updating knowledge remain open problems and that the source collection may not answer every question. Supports retrieval as a possible risk-reduction technique, never a guarantee.

4. **Junyi Li et al., “The Dawn After the Dark: An Empirical Study on Factuality Hallucination in Large Language Models,” ACL 2024.** [ACL Anthology](https://aclanthology.org/2024.acl-long.586/). Research study of hallucination detection, sources, and mitigation. Used as additional context that hallucination is studied as a factuality/reliability problem. No numerical results from this study are used in the video.

## Source limits

- “AI hallucination” is used in its common language-model sense of a false or unsupported statement presented as an answer; not every generative output is intended to be factual.
- Token prediction is a simplified explanation of autoregressive language generation. It does not describe every model architecture or every product feature.
- “Does not automatically verify each claim” is scoped to ordinary generation without a verification/retrieval tool; a deployed system may add tools, sources, and checks.
- Retrieval can provide relevant external material, but retrieval quality, source quality, interpretation, and answer generation can still fail.
- Bellora and Lumen are expressly fictional teaching names, not a claim about an actual model response.
