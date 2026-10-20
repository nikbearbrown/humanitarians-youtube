# Week 7: CI/CD Pipeline & Automated Testing

**Series:** Provenance Gatekeeper Development Log
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A split screen shows a green terminal on the left saying "PASS" and a burning server rack on the right. 
**ON SCREEN:** `IT WORKS ON MY MACHINE`
**VO:**
Hi, I am Onkar Bhujbal. Last week, we successfully built a regex parser for the Provenance Gatekeeper that intelligently extracts financial data from unpredictable AI text. It worked perfectly on my local machine. But enterprise software isn't about what works locally; it is about what survives in production. This week, we are stripping away manual testing and building an automated Continuous Integration pipeline.

### SCENE 2 — THE PYTEST HARNESS
**VISUAL** — Two Brutalist text boxes snap in.
`01 UNIT TESTS` 
`02 PYTEST AUTOMATION`
**VO:**
We started by writing strict unit tests using `pytest`. We codified every possible adversarial scenario—valid strings, magnitude errors, and SQL injections—into our `test_main.py` file. Instead of manually running our Python scripts and eyeballing the results, we now have a programmatic harness that mathematically proves our normalization layer behaves exactly as intended.

### SCENE 3 — THE GITHUB ACTIONS PIPELINE
**VISUAL** — A dynamic flowchart builds on screen. A git commit node connects to an Ubuntu server node, which spawns Docker containers.
**VO:**
But developers forget to run tests. To remove human error, we integrated GitHub Actions. We configured a workflow using path filtering so that every time new code is pushed to the Gatekeeper directory, GitHub automatically spins up a pristine Ubuntu runner, installs our dependencies, and boots our FastAPI and ChromaDB architecture inside Docker. 

### SCENE 4 — THE ADVERSARIAL STRESS TEST
**VISUAL** — Terminal output scrolls rapidly. The GitHub Actions check mark turns green. A red `X` flashes as a simulation shows a bad pull request being blocked.
**VO:**
Once the environment is live, the pipeline bombards our own API with the adversarial stress test. If a single hallucinated payload slips through our logic, the build fails and the code is blocked from merging. We have effectively created a self-healing perimeter where regressions cannot physically enter our main branch.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to a terminal command block.
`python -m pytest tests/test_main.py -v`
**VO:**
Stop testing your AI logic manually. Write unit tests for your extraction layers and force your repository to run them on every commit. Unautomated security is just a suggestion.
Liam, for Onkar Bhujbal and Humanitarians AI.