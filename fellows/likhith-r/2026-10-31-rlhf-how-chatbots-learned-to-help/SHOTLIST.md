# SHOTLIST — RLHF: How Chatbots Learned to Help

Native 16:9 (3840×2160) and 9:16 (2160×3840, `vertical/`). 12 beats · Kokoro `am_onyx` (speed 1.25 body, 1.2 for B00 / B10) · @HumanitariansAI · 60.000 s.

| # | Act | Pattern (→ 916 twin) | Show |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | "Namaskaram, Likhith" (9:16 "Hey, Likhith") · ask · 4 lines, first = "narrated by an AI voice" |
| B01 | BLUF | BrutalistHesitantWriter | "Chatbots learn to help from rules people give." → "rankings" |
| B02 | HOOK | RlHook | "How do I bake bread?" → raw model lists more questions (illustrative) vs. the recipe we wanted |
| B03 | FRAMEWORK | RlPretrain | text snippets stream into the model · 300,000,000,000 tokens (GPT-3) · ✓ continue any text · ✗ know a good answer |
| B04 | MECHANISM | RlSft | step 1 · person-written answer → model imitates word by word · ~13,000 prompts |
| B05 | MECHANISM | RlRank | step 2 · answers A–D sort into a ranking · 4 → 6 comparisons · toy reward model 50 → 77.7 % |
| B06 | MECHANISM | RlLoop | step 3 · assistant → reward model → nudge · histogram mean +0.05 → +2.34 · KL 1.18 leash |
| B07 | EVIDENCE | RlScale | OpenAI logo · GPT-3 175B bar vs 1.3B sliver · "people preferred its answers" · 175 ÷ 1.3 ≈ 135 |
| B08 | TRADEOFF | RlHack | toy: reward climbs, substance peaks at KL 1.18 then falls · pleasers 6.3 % → 99.9 % · agrees with you · sounds sure |
| B09 | VERDICT | RlNow | RLHF / DPO / RLAIF lanes (Anthropic logo, Constitutional AI) · "All three learn from preferences." |
| B10 | YOUR TURN | ClaudeComposerAsk | prompt read aloud |
| B11 | OUTRO | HaiOutro | HAI mark · title · Subscribe · "Narrated by an AI voice." |
