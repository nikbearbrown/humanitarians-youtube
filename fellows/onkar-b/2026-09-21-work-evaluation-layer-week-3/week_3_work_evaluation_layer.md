# Week 3: Evaluation Layer — Video Script

**Series:** Provenance Gatekeeper Development Log
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. 
`AI CLAIM: $5M` vs `LEDGER TRUTH: $4M`
**ON SCREEN:** `CATCHING THE LIE`
**VO:**
I am Onkar Bhujbal, a software engineer. Large language models are highly prone to numeric hallucinations. If an AI misreports financial data, the system must catch it before a human ever reads it. This week, we engineered the core of the Provenance Gatekeeper: the mathematical evaluation layer.

### SCENE 2 — THE FRAMEWORK
**VISUAL** — Two text boxes snap in.
`01 RETRIEVAL` 
`02 MAGNITUDE & DIRECTION`
**VO:**
Our grading logic is deterministic. When the AI generates a claim, the Gatekeeper first queries our ChromaDB ledger for the factual ground truth. We then run a strict programmatic comparison. The evaluation layer doesn't just return a pass or fail; it calculates the exact mathematical variance, categorizing the hallucination into a magnitude and directional error.

### SCENE 3 — WORKED EXAMPLE
**VISUAL** — Python code block executing.
`def evaluate(claim, truth):`
`  variance = claim - truth`
`  return "FAIL: +25% Directional Error"`
**VO:**
Here is the logic in practice. The AI claims revenue was five million dollars. The Gatekeeper pulls the truth: four million dollars. The Python script calculates a one million dollar discrepancy, categorizing it as a positive 25 percent directional error, and immediately flags the claim with a hard fail verdict.

### SCENE 4 — FALSIFIABILITY
**VISUAL** — The screen flashes red.
**ON SCREEN:** `THE FALSE POSITIVE TRAP`
**VO:**
Where does the evaluation layer fail? Format mismatches causing false positives. If the ledger truth is stored as "4.0M" but the AI generates "4,000,000", a poorly written validation script will crash and falsely flag the output as a hallucination, simply because it couldn't parse the commas.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Write a numeric parser that ignores currency symbols.`
**VO:**
Test your logic. Write a function that successfully compares the string "$4.5M" to the integer 4,500,000 and evaluates to true. You must normalize the data before you can grade it.
Liam, for Onkar Bhujbal and Humanitarians AI.