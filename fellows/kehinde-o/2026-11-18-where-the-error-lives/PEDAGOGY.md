# Pedagogy Review

## Topic
Where the Error Lives: why searching harder could not fix a compressed vector
index, measured on my own IVF-PQ implementation

## Learning Objective
Before trying to fix a system built on a compressed summary, find out where its
error lives. If the error is in the summary, searching it harder is wasted effort;
an exact check of a wider shortlist against the original is what works. The
viewer leaves able to apply that to any summary they rely on.

## Audience
General audience interested in AI and data. No prior knowledge of vector search
assumed: the index is described by what it does (sort, compress, look up) before
any term is used.

## Key Findings Reported
All measured in this session by running github.com/Kenny0bi/hive-index at the
benchmark's settings: 100,000 SIFT vectors, 1,000 queries, k = 10, 256 cells,
8 subspaces, seed 0.
- 512 bytes per vector become 8: 64 times smaller.
- Recall at 10 by cells searched: 1 cell 30.3, 4 cells 42.4, 16 cells 45.9,
  128 cells 46.0 percent. 16 to 128 cells is 7.4 times slower for +0.05 points.
- Coverage (true neighbours inside the searched cells) reaches 100 percent at
  128 cells while recall stays at 46.0. The error is in the codes.
- Exact re-check at 64 cells: top 10 stays 46.0 (it only reorders the answers),
  top 50 83.6, top 100 93.0, top 200 97.6 percent, all near 75 queries a second.

## Accuracy Gate
See FACTCHECK.md. The algebra on screen was verified numerically against the
repo's own code.

## Restraint Gate
- No claim that IVF-PQ is a bad method. The ceiling is documented in the original
  paper, and so is the fix.
- The re-check is not free in memory: it needs the original vectors kept. The
  narration says so.
- The comparison to AI-written text is presented as an analogy of shape, not as a
  claim about how language models store information.
- The narration is an AI voice. The outro says so on screen.

## Takeaway
Find where a summary's error lives before fixing it, and check more than you trust
against the original.

## VERDICT: PASS
