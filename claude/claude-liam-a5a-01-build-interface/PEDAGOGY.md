# PEDAGOGY — claude-liam-a5a-01-build-interface

## Video: Wrap It in a UI

**Series:** Wrap It & Test It — INFO 7375 Assignment 5A  
**Episode:** 1 of 6  
**Register:** Pragmatist (Kore, in for Humanitarians AI)  
**Audience:** claude-liam (students in INFO 7375)

---

## Learning objective

Students can wrap their existing Madison CLI tool in a Gradio or Streamlit interface that a stranger can use without their help — with labeled inputs, human-readable output, and plain-English error messages.

## Instructional design

| Beat | Role | Pattern |
|---|---|---|
| B00 | Frame the task: "a stranger opens a URL" | Cold open — ClaudeComposerAsk |
| B01 | Decision gate: Gradio vs Streamlit | Custom scene — 20-second rule, pick one |
| B02 | Input wiring from data contract | Custom scene — field → widget → label |
| B03 | Output format anti-trap | Custom scene — JSON blob wrong, formatted right |
| B04 | Error handling pattern | Code beat — empty-input + try/except |
| BVDT | Verdict: four requirements | ClaudeVerdictArtifact |
| BHTF | Handoff: scaffold prompt | Your Turn — ClaudeComposerAsk |
| BOUT | Outro | ClaudeTitleOutro |

## Pedagogical moves

- **Decision before build:** B01 forces a concrete pick (Gradio or Streamlit) before any code — prevents analysis paralysis.
- **Label-as-instruction:** B02 reframes the label field as the primary user interaction, not the Python variable.
- **Anti-trap (B03):** Names the failure mode explicitly ("JSON blob is wrong") before students encounter it.
- **Two-case error handling (B04):** Reduces the infinite error space to two tractable cases students can actually write.
- **The test question (BVDT):** "Could my Part 2 user finish a task without me in the room?" ties all four requirements to one actionable criterion.

## VERDICT: PASS
