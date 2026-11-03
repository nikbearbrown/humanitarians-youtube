# STEM Video: What Is AI Red Teaming? — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video is about red teaming — the real practice of deliberately attacking an AI system before someone else does it for real.

## B00 — Cold open
A single passing test doesn't mean a vulnerability is fixed. With a real AI system, the same attack can fail once and succeed the next time, on the exact same model.

## B01 — The real, formal definition
Method: the 2023 Executive Order on AI defines red teaming as structured testing to find flaws and vulnerabilities in an AI system, often in collaboration with the people who built it. Red teamers adopt adversarial methods on purpose — looking for harmful outputs, unexpected behavior, and ways the system could be misused.

## B02 — Why it's not just old-school penetration testing
Traditional security testing looks for misconfigurations and unpatched code. AI red teaming tests something genuinely different: whether a model can be talked into violating its own rules, what it leaks from its training data or context, and how it behaves once it's wired into real tools with real permissions.

## B03 — The real, structural difference
Here's the part that makes AI red teaming harder than normal security work: outputs are non-deterministic. A passing test is only provisional evidence, not proof. Teams have to rerun the same attack and require repeated success before they'll call something closed.

## B04 — Who's actually doing this
This isn't theoretical. OpenAI has run external red teaming on every major model release since twenty twenty-two, starting with DALL-E 2, and published real public findings for GPT-4, GPT-4 with vision, DALL-E 3, GPT-4o, and o1.

## B05 — Handoff
Your turn. Before trusting any AI system you've built, try to break it yourself first — a single clean test run proves far less than you'd think.

## B06 — Outro
What Is AI Red Teaming? Built with Claude, for Humanitarians AI.
