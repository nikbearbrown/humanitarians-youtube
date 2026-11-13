# FACTCHECK — What Is RAG?

| Beat | Claim | Verdict | Source / basis | Fix applied |
|---|---|---|---|---|
| B00 | RAG stands for retrieval-augmented generation. | TRUE | Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", NeurIPS 2020 (arXiv:2005.11401). | none |
| B01 | RAG does not make the model smarter; it supplies relevant text at answer time. | TRUE | Retrieved passages are added to the input; model weights are unchanged (Lewis et al. 2020). | Avoids saying RAG "teaches" or "trains" the model. |
| B02 | A model answers from patterns learned in training and has not seen private or recent documents. | TRUE (general) | Training data has a cutoff and excludes private documents. | "may still answer" is kept soft rather than "will hallucinate". |
| B03 | Retrieve → augment → generate; the answer can cite its passages. | TRUE | Standard RAG pipeline description. | "can say where each part came from" is kept soft: citation is possible, not automatic. |
| B04 | Chunks are turned into embeddings, and similar meaning lands close together. | TRUE (dense retrieval) | Dense retrieval, e.g. DPR (Karpukhin et al. 2020), as used in Lewis et al. 2020. | On-screen positions are captioned as schematic, not computed. The script says "search" elsewhere because keyword search is also used. |
| B05 | The search returns three passages; the top one gives the 48-hour, 10% penalty rule. | TRUE (demo) | demo/rag_demo.py over demo/syllabus.md; output in demo/retrieval_output.json (top score 0.392, §3 Late labs). | The syllabus is labeled on screen as made up for the demo. |
| B06 | Short documents can simply be pasted in; retrieval errors produce wrong answers that look sourced. | TRUE (practice) | Long-context models accept short documents directly; a retrieval miss passes wrong context to the model. | none |
| B07 | Verdict restates B01, B03 and B06. | consistent | — | none |

Nothing dates the film: no model names, version numbers or benchmark figures appear in the narration.
