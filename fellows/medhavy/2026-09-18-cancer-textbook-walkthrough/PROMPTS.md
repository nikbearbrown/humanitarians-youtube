# PROMPTS.md — claude-liam-medhavy-cancer-textbook-walkthrough

No paid generation. No image or video model called. Every visual is a real browser capture of the live hub and the live cancer textbook, or a Remotion bookend from the Claude scene library.

## Reconstructed prompts on screen (labelled "Suggested prompt · reconstruction")

**B00** — What if my textbook could actually answer my questions and show its work? Show me what a student sees in the Medhavy Hub cancer biology textbook.

**B15 (Your Turn)** — Open your textbook from hub.medhavy.com, go to the section you are stuck on, and ask: Explain this section in simple terms, then give me a worked example with my own numbers. Read the sources it lists before you trust it.

## Questions typed into the book's AI tutor on camera (real, answered by the site)

1. What is the difference between an oncogene and a proto-oncogene?
2. Give me a worked example with my own numbers: a cell with 2 copies of MYC amplified to 20.
3. Explain retroviral transduction in simpler terms, with a real-world analogy.
4. Give me a summary of this section in three lines.

Search query typed: "Warburg effect".

## Capture
`scripts/capture_admin.py` with `capture/plan-signin.json` (`--no-session`) and `capture/plan-book.json`; session from `scripts/save_session.py` (human sign-in). Narration: Kokoro `am_onyx`, Teardown register, Liam in for Bear, adapted from Bear's reference script for this walkthrough.
