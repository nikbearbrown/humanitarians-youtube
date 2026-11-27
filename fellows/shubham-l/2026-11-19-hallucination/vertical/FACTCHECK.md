# FACTCHECK — Why AI Makes Things Up

Every on-screen and spoken claim, traced to its source. Medhavy paths are relative to `~/Desktop/medhavy/medhavi-hub`. Code outputs are copied verbatim from `code/*.out.txt`.

## B00 · ASK
- Source: bookend (no factual claim beyond the film summary)
- Narration: Hi, I am Shubham L. and this video is about why language models sometimes state false things confidently, shown with a tiny model I trained on three sentences. The voice you're hearing is Liam, an A I narrator, reading my script. It's the most important limitation to understand before trusting any A I answer.

## B01 · BLUF
- Source: bookend (no factual claim beyond the film summary)
- Narration: It's tempting to say a model makes things up because it's broken. It makes things up because it predicts, not checks. It learns which words tend to follow which. Truth is a different question it was never directly asked.

## B02 · WORKED_EXAMPLE
- Source: stem-ai-5-hallucination/code/bigram.py (run locally)
- Narration: Here's the smallest model I could build. It reads three true sentences: Paris is the capital of France, Berlin of Germany, Rome of Italy. It only learns which word follows which. Then I asked what it would say after Paris is the capital of. Every continuation it can produce is on the right.

## B03 · MECHANISM
- Source: stem-ai-5-hallucination/code/bigram.out.txt
- Narration: And there's the problem in one table. France, Germany and Italy each get a third. Every sentence it produces is perfectly fluent. Two out of three are false: Paris is the capital of Germany. The model isn't lying, and it isn't broken. It learned real patterns from true sentences. It just never learned which pairing was the fact.

## B04 · FRAMEWORK
- Source: general explanation; scaled-up analogy to large language models
- Narration: Real models are vastly better. They use long context, not one word, and they get Paris right. But they share the root: they're trained to predict what usually comes next. When a question lands where the patterns are thin, a rare name, a fake citation, they still produce something fluent. And they learned a confident tone too.

## B05 · FALSIFIABILITY
- Source: standard mitigations; links to the RAG film in this series
- Narration: So what helps? Ground the model: give it the source text to answer from, the R A G idea. Ask for citations, and actually open them. Tell it that I don't know is an acceptable answer. And for anything that matters, names, numbers, dates and quotes, check it yourself. Prediction is the engine. Checking is your job.

## B06 · VERDICT
- Source: bookend (no factual claim beyond the film summary)
- Narration: Why does A I make things up? Because it predicts likely words rather than checking facts. Even my three-sentence model, trained only on true sentences, said something false a third of the time. Fluent isn't true. Ground it, ask for sources, and verify what matters.

## B07 · YOUR_TURN
- Source: bookend (no factual claim beyond the film summary)
- Narration: Your turn. Pick a niche topic you know well and ask Claude to answer five questions about it, then rate its own confidence, name a source that would confirm each answer, and flag anything it may have invented. Compare against what you know. You'll see where fluent and true come apart.

## B08 · OUTRO
- Source: bookend (no factual claim beyond the film summary)
- Narration: That was Why AI Makes Things Up. Shubham L., for Humanitarians A I. Thanks for watching.

