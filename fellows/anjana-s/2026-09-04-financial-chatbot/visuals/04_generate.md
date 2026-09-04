# Beat 4 — Generate

**Visual type:** Remotion
**Duration:** ~15 seconds

## What the viewer sees

**The prompt assembly (0-7s):**
A prompt window builds vertically in three color-coded sections:

Section 1 (grey): "System: You are a financial analyst. Answer only from the provided context. Cite your sources."

Section 2 (blue): "Context:" followed by the three retrieved chunks from Beat 3, each numbered [1], [2], [3]. The chunk text is partially visible, enough to see real content.

Section 3 (white): "Question: Did Company A raise revenue guidance last quarter?"

The three sections visually lock together into a single prompt package. An arrow sends the assembled prompt into the LLM node, which activates and glows.

**Answer generation (7-11s):**
The LLM node pulses as it processes. On the right side, an answer streams out character by character:

"Yes, Company A raised full-year revenue guidance from $12B to $12.5B during Q3 prepared remarks. [1] The increase was driven by stronger than expected demand. [2] Prior guidance of $12B was revised upward. [3]"

As each citation tag appears ([1], [2], [3]), a faint glowing line draws back to the corresponding chunk in the context section. The citations are traceable.

**Return to chat (11-15s):**
The answer flows upward into the chat interface (still in the top-left corner from Beat 1). The chat interface grows back to full size. The answer is now displayed with the three citation badges glowing. The pipeline diagram below fades away.

The viewer is back where they started, but now they know what happened underneath.

Label: "RAG. The model reads your documents. Not its memory."

## Technical notes

- The three-section prompt should visually convey that the model receives instructions + evidence + question, not just a question
- The citation lines connecting answer back to source chunks are the key visual payoff
- The return to the chat interface closes the loop from Beat 1
- The streaming text effect should feel natural, like watching a chatbot type
- The label is the takeaway: the model does not hallucinate because it was given the evidence
