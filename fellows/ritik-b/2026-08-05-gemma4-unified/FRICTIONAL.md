# Frictional log — Gemma 4, Unified?

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## 2026-08-05 — reconstructed 2026-11-25

**What I was working on.** A teardown of Gemma 4's encoder-free 12B model: which perception front-ends Google removed, and what the technical report's numbers do and don't show.

**What I tried and expected.** The brief framed Gemma 4 as an "any-to-any" model and as an example of generator/discriminator convergence. I expected to build the reel around those two claims.

**Where the work resisted, and what I did next.** Neither claim held up. Gemma 4 emits text only; "any-to-any" is Hugging Face's pipeline name for its inputs. It has no generative visual head and no discriminator. Both claims are logged as REJECTED in FACTCHECK.md, and the reel was reframed around encoder convergence. The research also showed the encoder-free 12B shipped two months after the rest of the family, which became the spine of the reel, and that the report never runs a controlled comparison (its comparisons change size and architecture at once), which became the twist. The first cut failed GATE V with 4 MAJOR defects, fixed in revision 2. The PROOF review then failed on sources-on-screen, fixed in revision 4 by adding source notes to the exhibit scenes. Revision 5 caught that B00 still greeted the wrong presenter.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent, did the research, wrote the scenes and narration, and ran the gates. Accepted: the encoder-convergence reframe and every revision-log fix. Rejected: the two brief claims above, kept on record rather than quietly dropped.

**What I understand now, and what I still don't.** Sourcing has to be a contract every claim beat takes, not a per-scene afterthought. Still open, as BUILD-LOG.md names: the figures are redrawn rather than shown from the source page, and the narration never tells the viewer the three questions are reusable.
