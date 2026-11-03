# Frictional log — Continuous Integration

## 2026-10-16 — the project update, in two aspect ratios

**What I was working on.** A STEM AI explainer distinguishing between testing static code and testing non-deterministic machine learning outputs.

**What I tried, and what I expected.** 
- I initially tried to explain CI/CD as just a tool for running standard unit tests, hoping to keep the script simple and accessible.

**Where it resisted, and what I did next.** 
- Explaining CI/CD as standard testing missed the nuance of why it is *critical* for AI. If an LLM is probabilistic, how do you write a test that expects a specific string? You can't.
- I pivoted the narrative to focus on "Testing the Shield, Not the Sword." The script shifted to explain that CI for AI isn't about testing the language model itself; it is about bombarding your custom parsers and fail-safes with adversarial data to ensure they don't break.

**What Claude contributed, and what I did with it.** 
- Mine: The central metaphor of the CI pipeline acting as a physical gatekeeper that blocks bad code from reaching production.
- Claude's: Highlighting the "Regression Problem" and the juxtaposition between Static Code and Dynamic Inference. I used this contrast to frame the hook of the video.

**What I understand now, and what I still do not.**
- Understood: Continuous integration in AI engineering is fundamentally defensive. You are not verifying that the model is smart; you are mathematically proving that your application can survive when the model inevitably acts stupid.