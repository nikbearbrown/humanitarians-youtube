# Script — "Can You Trust Your AI? How We Test Large Language Models"

**Narrator:** Yeshwanth Balaji, voiced by the local AI voice Kokoro `am_onyx` (speed 0.95; not a recording) · **Channel:** @HumanitariansAI · **Skill:** `ai-explainer` (claude-hai)

Full narration, every beat, exactly as synthesized. Total 283.2 s. The audio is the master clock.

**B00 · ASK · 12.8 s**

Ciao, this is Yeshwanth Balaji. AI can write an answer that sounds perfect and is completely wrong. So how do engineers decide whether a model can be trusted? Let's open the toolbox researchers use to test it.

**B01 · BLUF · 13.2 s**

Trusting an AI isn't a feeling. It's something you measure: with scores, with bias tests, by looking inside the model, and by asking people. Each one catches something the others miss.

**B02 · BODY · 18.0 s**

Start with the problem. Ask a model what temperature water boils at on top of Mount Everest. It answers: one hundred degrees, the same as at sea level. Fluent, confident, and wrong. Up there the air is thinner, so water boils at about seventy. A confident answer that isn't true is called a hallucination.

**B03 · BODY · 18.1 s**

Hallucination is one of three reasons we can't take an output on faith. Bias: models can learn unfair patterns from their training data. And the black box: billions of numbers, and no easy way to see why the model said what it said. You wouldn't hire someone because they sound confident. You'd check their work.

**B04 · BODY · 18.2 s**

So how do you check the work? Researchers use a toolbox. Metrics that score answers against reference answers. Benchmarks: one test for every model. Head-to-head comparisons. Bias tests. Ways to look inside the model. And human review. Nik Bear Brown's survey paper collects most of these. Let's open them.

**B05 · BODY · 20.7 s**

First, metrics. Scores like BLEU and ROUGE count the words an answer shares with a reference answer. Here's a real calculation. The wrong answer, one hundred degrees, scores zero point eight seven. A correct answer in different words scores zero point two five. The score measured overlap, not truth. The survey notes these metrics often track human judgment poorly.

**B06 · BODY · 22.6 s**

Benchmarks solve a different problem: comparing models fairly. Every model takes the same test, scored the same way, and a leaderboard ranks them. A-B testing does the same for two versions of one model: same prompts, side by side, and you count which answers people prefer. But the survey warns that chasing a leaderboard can mean over-optimizing for the test. One score never tells the whole story.

**B07 · BODY · 20.5 s**

Now fairness. One simple test: keep the prompt the same, and swap one sensitive detail, like a name, a gender, or a region. Write a reference letter for Emily, a nurse. Then the same request for Jamal. Compare the two answers. If the quality shifts with who it's about, that's a bias signal. The survey calls this a counterfactual: change one thing, and watch the output.

**B08 · BODY · 22.9 s**

Next, looking inside. A model turns words into points in a space with hundreds of dimensions. These are called embeddings. This is a real one: a small open model, sixteen words, flattened to two dimensions. Similar ideas cluster: animals, fruit, sports, music. Add kitten, and it lands next to cat. Engineers use maps like this to check what a model has grouped together, and what it shouldn't have.

**B09 · BODY · 21.8 s**

Another way in: ask the model to explain its reasoning. Back on Everest, the explanation shows the faulty step. It assumed water always boils at one hundred degrees. Now you can see where it went wrong, and fix it. That turns the black box into a glass box, at least partly. One caution from the survey: an explanation isn't proof. What a model attends to isn't always what caused its answer.

**B10 · BODY · 20.5 s**

So why do people still matter? Metrics are good at overlap with a reference, and at running the same test thousands of times. But they miss tone, context, and subtle errors. People judge whether an answer is coherent, helpful, and fits the real situation. The survey calls human evaluation indispensable. The strongest evaluations combine both.

**B11 · BODY · 16.4 s**

Here's your checklist before you trust an AI answer. One: can I verify this from another source? Two: would the answer change if I reworded the question? Three: is it explaining its reasoning, and does that reasoning hold up? Four: is this a high-stakes decision that needs a human check?

**B12 · BODY · 14.2 s**

This video follows Enhancing Trust in LLMs, by Nik Bear Brown. It's a survey of evaluation techniques, so it reports no experiments of its own. The examples here are ours, built to show how each one works.

**B13 · VERDICT · 10.4 s**

Recap. Trust in AI isn't a feeling. It's measured: with performance metrics, bias tests, interpretability, and human review. Each one catches what the others miss.

**B14 · HANDOFF · 26.3 s**

Your turn. Paste this into Claude: Here's an answer an AI gave me. Before I rely on it, list every factual claim it makes, tell me how I could check each one against an independent source, give me two rewordings of my original question to test whether the answer holds, and tell me whether this decision needs a human expert. Watch the list of claims: the ones with no source to check against are where you start. The smarter AI gets, the more it matters to test it. Don't just ask whether an answer sounds right. Ask how you'd know.

**B15 · OUTRO · 6.8 s**

Can You Trust Your AI? How We Test Large Language Models Humanitarians AI.

