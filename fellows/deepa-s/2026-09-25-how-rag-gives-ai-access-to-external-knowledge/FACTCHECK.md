# Fact-check and claim boundaries

## Established by primary research and technical documentation

- Lewis et al. describe RAG as combining a pre-trained generative model (parametric memory) with an external, non-parametric memory and retrieval mechanism. Their original system used a dense vector index of Wikipedia and a neural retriever. This video simplifies that architecture to an approved company knowledge base; the fictional company system is an illustrative modern use case, not a claim about the paper’s exact system.
- In a standard RAG flow, an application retrieves relevant content in response to a question, adds retrieved content to the model input, and then generates an answer. Retrieval therefore precedes answer generation in the workflow shown.
- Retrieved knowledge can come from sources such as documents and databases. Whether it is current, private, and accessible depends on how a particular system’s sources are maintained and permissioned.
- RAG supplements the context at inference time; it does not retrain the model for every question. This describes the educational workflow here and is not a claim that every architecture or RAG system is identical.
- Grounding may reduce unsupported answers, but retrieval can be irrelevant or incomplete, source content can be poor or stale, and generation can still be inaccurate. RAG does not guarantee correctness.

## Simplified explanation

The four-stage flow—question → retrieve relevant information → add it to context → generate an answer—is a beginner-friendly simplification of a common RAG pattern. Implementations can add indexing, chunking, ranking, query rewriting, access checks, citations, or multiple retrieval steps. The video does not imply a single search method or that all RAG products work identically.

The remote-work policy and the “two days a week” rule are explicitly fictional and conditional on what the imagined policy says. They are not a statement about a real company.

The link to Content #3 (“How AI Hallucinations Happen”) is limited: relevant retrieved context can help ground a response and may reduce unsupported claims; RAG does not eliminate hallucinations or guarantee a correct answer.

No statistics, experiments, quotations, policy facts, or product capabilities are invented or attributed to a source.
