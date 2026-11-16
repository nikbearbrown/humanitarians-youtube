# SOURCES — Word2Vec: King − Man + Woman ≈ Queen

## Primary sources (cited on screen)

1. **Mikolov, Chen, Corrado & Dean (2013).** *Efficient Estimation of Word Representations in Vector Space.* arXiv:1301.3781 (Google). Introduces the skip-gram and CBOW models (B05).
2. **Mikolov, Sutskever, Chen, Corrado & Dean (2013).** *Distributed Representations of Words and Phrases and their Compositionality.* NeurIPS 2013, arXiv:1310.4546. Skip-gram with negative sampling, trained on Google News text (about 100 billion words). Google released 300-dimensional vectors for 3 million words and phrases (word2vec project page, code.google.com/archive/p/word2vec). Backs "billions of words" and "300 numbers per word" (B05).
3. **Mikolov, Yih & Zweig (2013).** *Linguistic Regularities in Continuous Space Word Representations.* NAACL-HLT 2013. The vector-offset analogy method and king − man + woman ≈ queen (B02, B06).
4. **Firth, J. R. (1957).** "A synopsis of linguistic theory, 1930–1955." In *Studies in Linguistic Analysis* (Special volume of the Philological Society), Oxford: Blackwell, pp. 1–32; the quote is on p. 11 (B04). Origin check: Quote Investigator, https://quoteinvestigator.com/2022/09/18/word-company/ ; Brunila & LaViolette 2022, arXiv:2205.07750.
5. **Bolukbasi, Chang, Zou, Saligrama & Kalai (2016).** *Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings.* NeurIPS 2016, arXiv:1607.06520. Bias analogies found in the 300-dimensional Google News Word2Vec vectors (B07).

## Supporting source (not on screen)

6. **Nissim, van Noord & van der Goot (2020).** *Fair Is Better than Sensational: Man Is to Doctor as Woman Is to Doctor.* Computational Linguistics 46(2): 487–498, https://aclanthology.org/2020.cl-2.7. The standard analogy code never lets an input word be returned; their "fair" version allows it, which changes the famous answers. Backs B07's "queen only wins with the inputs excluded" for the real Google vectors.

## Our own evidence (every number on screen)

`evidence/w2v_toy.py` (numpy 2.5.3, seed 2026): skip-gram with negative sampling written from scratch, trained in about 35 s on a **built-in template corpus** (30,000 sentences, 194,145 tokens, 173-word vocabulary). Outputs: `w2v_toy.out.txt`, `w2v_toy.json`. `make_scene_data.py` turns the JSON into `runtime/remotion/src/word2vecData.ts`, the only source of numbers in `Word2Vec.tsx`.

The toy corpus was **written for this video**, so the toy shows the mechanism; it is not evidence that Word2Vec behaves this way on real text. Sources 2, 3, 5 and 6 are that evidence. On screen, every toy number carries an "our toy" label. Corpus revisions are logged in BUILD-LOG.md: v1 and v2 logs are kept, and `evidence/sweep/SWEEP.md` shows the trade-off from varying one setting.

## Corrections applied (DOUBLE-CHECK LAW)

- "About 300 numbers": Google's released vectors are exactly 300-dimensional, so the narration says "300 numbers". The toy also uses 300 dimensions.
- "Man to woman about the same as king to queen": in our toy the two steps line up at cosine 0.406 (Paris→France vs Tokyo→Japan: 0.975; man→woman vs Paris→France: −0.015, unrelated). The narration says "roughly matches" to stay honest to that.
- Point 7: modern models (ChatGPT, Claude) learn their own embeddings, for word pieces (tokens), with no Word2Vec inside. The screen says so in small type; the narration's "vectors like these" means the idea, not the same vectors.
- Bias analogy: the narration follows the paper's title ("computer programmer"), not "programmer".
