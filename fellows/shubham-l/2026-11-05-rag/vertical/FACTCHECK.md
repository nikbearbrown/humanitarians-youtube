# FACTCHECK — RAG: How AI Looks Things Up Before Answering

Every on-screen and spoken claim, traced to its source. Medhavy paths are relative to `~/Desktop/medhavy/medhavi-hub`. Code outputs are copied verbatim from `code/*.out.txt`.

## B00 · ASK
- Source: bookend (no factual claim beyond the film summary)
- Narration: Hi, I am Shubham L. and this video is about retrieval-augmented generation, R A G: how an A I finds the right passage before it answers. The voice you're hearing is Liam, an A I narrator, reading my script. It's how a tutor like Medhavy's can answer from the textbook instead of from memory.

## B01 · BLUF
- Source: bookend (no factual claim beyond the film summary)
- Narration: Many people think R A G means the model learns your notes. Nothing is learned. The model looks them up: find the most relevant passage, paste it into the prompt, then answer from it.

## B02 · FRAMEWORK
- Source: general RAG pattern (Lewis et al., 2020)
- Narration: R A G has three moves. Retrieve: score every passage in your collection against the question and keep the best. Augment: paste those passages into the prompt. Generate: the model answers, using the text right in front of it. The model itself never changes. It just gets the right page, every time it's asked.

## B03 · WORKED_EXAMPLE
- Source: stem-ai-3-rag/code/retrieve.py (run locally)
- Narration: Here's the retrieve step, written small enough to read. Four physics passages, and a student asking what launch angle gives a projectile the longest range. The script turns each text into word weights, rare words count more, and measures how closely each passage points the same way as the question.

## B04 · MECHANISM
- Source: stem-ai-3-rag/code/retrieve.out.txt
- Narration: And the scores. The projectile passage wins clearly at point six four, because it shares launch, angle, range and projectile with the question. Circular motion scores point one nine mostly from tiny shared words. Units scores zero. Only the winner gets pasted into the prompt, so the answer comes from chapter three.

## B05 · FALSIFIABILITY
- Source: general RAG trade-offs; docs/ai-models.md (Medhavy uses a local Orama index)
- Narration: R A G fixes a lot. Answers are grounded in your text, they can cite it, and you update documents instead of retraining. But it's only as good as retrieval. If the right passage isn't found, or word overlap misleads the scorer, the answer is built on the wrong page. Real systems, Medhavy included, use proper search indexes for exactly this reason.

## B06 · VERDICT
- Source: bookend (no factual claim beyond the film summary)
- Narration: R A G, then. Look up, paste in, answer. The model learns nothing new; it reads what it's handed. In my run, the right chapter won clearly. And when a R A G system gets something wrong, the first question isn't about the model. It's what did it retrieve?

## B07 · YOUR_TURN
- Source: bookend (no factual claim beyond the film summary)
- Narration: Your turn. Ask Claude for a tiny R A G demo over ten paragraphs of your own notes: print the top three passages and their scores, then the exact prompt that would go to the model, and include one question where retrieval fails. That failure case is the lesson. Find out why the wrong passage won.

## B08 · OUTRO
- Source: bookend (no factual claim beyond the film summary)
- Narration: That was RAG: How AI Looks Things Up Before Answering. Shubham L., for Humanitarians A I. Thanks for watching.

