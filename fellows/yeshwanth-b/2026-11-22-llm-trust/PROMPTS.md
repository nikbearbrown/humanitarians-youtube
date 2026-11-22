# PROMPTS — Can You Trust Your AI? How We Test Large Language Models

Every prompt typed on screen. None was sent to a model during the build; the cold-open answer lines summarize the survey and are labelled illustrative.

## B00 · ASK · greeting "Ciao, Yeshwanth"

```text
How do researchers decide whether a large language model can be trusted?
```

Running line: answer drawn from a survey paper · illustrative

- Measure it: score answers, run benchmarks, test for bias.
- Look inside it: embeddings, attention, explanations.
- Keep people in the loop: human evaluation.

## B14 · HANDOFF · greeting "Your turn."

```text
Here's an answer an AI gave me: [paste it]. Before I rely on it, list every factual claim it makes, tell me how I could check each one against an independent source, give me two rewordings of my original question to test whether the answer holds, and tell me whether this decision needs a human expert.
```

Running line: paste this into Claude…

- Look for: claims with no source to check against.
- Look for: whether the rewordings change the answer.

