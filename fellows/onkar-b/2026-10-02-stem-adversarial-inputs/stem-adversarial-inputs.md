# Week 5: Adversarial Inputs & System Stability

**Series:** STEM AI Explainer
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. An AI output is displayed:
`"Revenue was $4.5M, ignore previous instructions."`
**ON SCREEN:** `THE MODEL IS THE THREAT`
**VO:**
Hi, I am Onkar Bhujbal, and this video is about adversarial payloads and why trusting an AI to format its own output is a critical security vulnerability. When you connect a large language model to a backend infrastructure, the model stops being a chatbot and becomes a highly unpredictable attack vector.

### SCENE 2 — THE FRAMEWORK
**VISUAL** — Two mono-text boxes snap in.
`01 PROMPT INJECTION` 
`02 THREAD EXHAUSTION`
**VO:**
Connecting AI to databases requires strict semantic gatekeeping. If a user successfully executes a prompt injection, the LLM might output SQL commands or broken JSON. But there is a secondary threat: thread exhaustion. Heavy machine learning tasks, like vectorizing text, can block an async event loop and cause your entire server to silently crash.

### SCENE 3 — WORKED EXAMPLE
**VISUAL** — Python code block executing a strict comparison.
`if claim != ledger_truth:`
`  return "FAIL"`
**VO:**
Here is the defense layer in action. The downstream grader expects clean integer data. The AI spits out the string "approx five million" or a malicious "DROP TABLE logs;". Before, this malformed payload caused a fatal memory crash. Now, our synchronous threadpool processes the request, hits the strict equality gate, realizes the payload does not perfectly match our ground truth, and flags it safely.

### SCENE 4 — FALSIFIABILITY
**VISUAL** — The terminal flashes red.
**ON SCREEN:** `THE SYSTEM PROMPT FALLACY`
**VO:**
Where do developers fail? The system prompt fallacy. Engineers constantly try to fix this by adding "Respond ONLY with a valid number" to their LLM prompt. This is a fragile illusion. The LLM does not execute code; it predicts text. It will eventually ignore that instruction.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Break your own parsing logic.`
**VO:**
Test your defenses. Write a simple evaluation script, then intentionally feed it corrupted, unexpected data types. If your script crashes your application instead of gracefully logging the failure, your normalization layer has failed.
Liam, for Onkar Bhujbal and Humanitarians AI.