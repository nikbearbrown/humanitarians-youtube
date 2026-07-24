Teaching an AI to Grade Its Own Homework

Human harmlessness labeling has three structural problems: it's expensive (annotators spend time on specifically disturbing content), inconsistent (two humans on the same output won't always agree), and doesn't generalize (2022 labels don't cover harm categories that emerge later). Constitutional AI replaces most of that labeling with a loop.

The CAI method: write sixteen principles, use a red-team prompt to elicit a problematic response, ask Claude to critique that response against a specific principle, ask Claude to revise it, and use the revised response as the preferred training label. The critique and revision replace human annotation. The loop runs at scale. The constitution is auditable; the annotators weren't.

The result matched human-labeled RLHF on harmlessness — and beat it on helpfulness. RLHF models over-refuse because annotators reward caution. CAI models refuse when the constitution says to refuse, not when a human would feel safer refusing. And CAI models can explain their refusals by citing the specific principle. That transparency is the part RLHF cannot replicate.

Source: Bai et al. (2022) · arXiv:2212.08073

Every claim in this video was fact-checked against the source chapter and primary sources before rendering.

#AI #AIAlignment #Anthropic #Claude #MachineLearning #AIResearch #NikBearBrown #constitutionalAI #RLHF #AISafety

youtube.com/@HumanitariansAI
