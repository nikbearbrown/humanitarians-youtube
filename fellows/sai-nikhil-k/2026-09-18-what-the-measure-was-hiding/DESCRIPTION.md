Did Prot2Vec get bigger this week? Wrong question — breadth is not the release. The defences are, and one of them caught the instrument doing the measuring.

This weekly progress reel opens two Prot2Vec releases that landed in the same week — v0.2.0 and v0.3.0 — and reads them for what they defend against rather than what they add. Prot2Vec is a benchmark harness for protein sequence embeddings: you hand it sequences with group labels, it runs every embedding method against every dimensionality reducer, and it scores all of them with the same metrics, so the comparison is actually like for like. It went from two representations to nine, two projections to thirteen, ten metrics to thirty-one, and 208 tests to 411. Six of the nine ways to turn a sequence into a vector need no PyTorch at all. Every one of those counts was recounted from the source at the merge commit, not read off the changelog.

Most of what is new is not capability, it is control. Neighbourhood preservation asks what fraction of each point's true nearest neighbours survive the projection — and that number has a floor, because even a projection carrying no information keeps k/(n−1) of them by luck. So the release ships the chance-corrected form, LCMC(k) = NP(k) − k/(n−1), and the reel evaluates that floor for the project's own quick-start shape: k = 10, n = 90, 10/89 ≈ 0.1124. Run against seeded random matrices, the shipped functions return NP = 0.1092 ± 0.0108 and LCMC = −0.0032 ± 0.0108 over forty trials — the floor is exactly where the algebra says it is. Two more defences sit beside it: a random-projection control that fits nothing, and a confound group that reports the accuracy reachable from sequence length alone. Two protein families separating cleanly on screen can mean the representation found real homology, or it can mean the representation encoded length. In a scatter plot those two look identical.

Then the same release caught its own instrument. Coverage had been told to ignore any line that is just an ellipsis — the abstract-method placeholder — but the pattern was never anchored, so it also matched a type annotation, tuple of string and ellipsis, and coverage discards the entire statement a matching line belongs to. Sixty-one statements quietly left the report. Forty-seven of them sat in suite.py, the module that scores everything else: thirteen of its sixty statements were being measured, and the function that runs the evaluation was one of the hidden ones. The tree-wide percentage moved about three points the whole time. That is the same mistake the tool exists to find — a number that looked fine while quietly measuring less than it claimed. Breadth changes the cost of ordinary failures too: NMF refuses signed input, a manifold method can fail on a disconnected neighbour graph, and at four pairs those are exceptions while across a full matrix they are expected traffic. One of them used to discard every pair that had already succeeded. Now the pair is isolated, named, and recorded under skipped_pairs in the run manifest.

Try it yourself: if you are about to publish a benchmark score, don't start with whether it is good. Say what a random control would have scored on the same data, say what the result becomes if your representation encodes only length, and say whether the tooling you used to check your own work is itself being checked. Then go find the one you forgot — there is almost always one.

Prot2Vec, the project in this reel — https://github.com/nikhil-kunapareddy/Prot2Vec

Chapters:
0:00 Nine representations, thirteen projections, thirty-one metrics
0:19 What it is — every method against every reducer
0:38 The floor — what a projection carrying nothing scores
0:57 Real homology, or length in disguise
1:17 Sixty-one statements that left the report
1:38 Abort the matrix, or isolate the pair
1:57 Verdict — the defences are the release
2:11 Your turn
2:30 Outro

Hosted by Sai. Voice: Kokoro am_onyx — free, local, no account. AI-generated narration. Motion graphics built with Remotion; equations typeset locally as outlined SVG, with real fraction bars and a real summation, not text cards. Every count on screen was recounted from the repository at the merge commit rather than taken from the changelog, and the statement counts in the coverage table are the recorded output of a script driving coverage.py 7.8.2 over that same tree. The changelog's own coverage percentage is deliberately not quoted, because reproducing it needs the full suite under optional extras and that run was not made. No runtime, accuracy or adoption figure appears anywhere, because none was measured. No human-performed audio or video in this production.

Prot2Vec — https://github.com/nikhil-kunapareddy/Prot2Vec
Humanitarians AI — https://humanitarians.ai
Musinique — https://musinique.com
Medhavy AI — https://medhavy.com

#AI #Bioinformatics #ProteinML #MachineLearning #Benchmarking #OpenSource #Reproducibility #HumanitariansAI #WeeklyUpdate

TAGS

Prot2Vec, protein embeddings, protein language models, ESM-2, benchmarking, benchmark harness, bioinformatics, computational biology, Pfam, dimensionality reduction, UMAP, t-SNE, PCA, PHATE, PaCMAP, neighborhood preservation, LCMC, trustworthiness, chance baseline, random projection control, confound, sequence length confound, code coverage, coverage.py, test coverage, scientific software, reproducibility, computational skepticism, Python, open source, Humanitarians AI, weekly progress

HASHTAGS

#AI #Bioinformatics #ProteinML #MachineLearning #Benchmarking #OpenSource #Reproducibility #HumanitariansAI #WeeklyUpdate
