# Frictional log — Explainer: How KV Cache Works



## 2026-08-31 — script written, production not recorded

- **Video:** 
- **Drive:** https://drive.google.com/drive/folders/1-H-vE7c3x-pJmIU_Jw5rjhPBydSJfA8q 
- **Report:** [REPORT.md](REPORT.md)
- **Paired sprint:** [Sprint 2 — connecting the three model tiers](../09032026mycroft-gateway/)


**What I was working on.** A STEM deep-dive on how the KV cache works: the
key and value vectors for a token, once computed under causal masking, never
change — so caching them turns the expensive part of decoding from quadratic
work into linear work, at the cost of memory that grows with every generated
token. Eleven beats, ~3:40, persona Simba, voice Kokoro `af_bella`

**What I tried, and what I expected.**
- I expected the hard part to be explaining causal masking without a wall of
  matrix notation  that the cache only works because a token can never attend
  to a later one, so its K and V are final the moment they are computed.
- I expected to be able to quote a concrete cache size and speedup figure.

**Where it resisted, and what I did next.**
- **I could not honestly put numbers on it.** Cache size and speedup depend
  entirely on which model and which hardware, and I had measured neither. The
  script keeps those claims qualitative rather than borrowing a figure from
  somewhere it did not apply. Same discipline my sprint reports use: a number
  with no measurement behind it is not evidence.
- **Runtime is arithmetic, not a measurement, and the script says so**  word
  count divided by Kokoro's measured speaking rate, not the duration of a render
  that had happened.
- **Most of the visuals had no component to build on.** Beats B02 through B08 are
  marked "Custom scene  needs building"; only B00, B01, B09 and B11 map to
  existing house components. GATE L  search the library before authoring  had
  not been run when the script was written, and the script says as much rather
  than implying the scenes existed.
- **No 9:16 cut was drafted**, because none was asked for.
- **Production has no record at all.** No render, no audio, no compiled file, and
  no video on the tracker. The script exists; that is not the same as the video
  existing, and I am not going to write a build narrative I have no evidence for.

**What Claude contributed, and what I did with it.**
- Mine: the research and the diagrams  working out the causal-masking argument
  and what each beat needed to show.
- Claude's: the beat sheet built from those, in the pipeline's own conventions.
  That is why the script reads in the pipeline's voice, with its GATE L
  references and series conventions, while the material underneath it is mine.
  An earlier draft of this log flagged that voice as a possible attribution
  contradiction; it is not one, and this line settles it.
- Not applicable: production. There is no record of any having happened.

**What I understand now, and what I still do not.**
- Understood: the cache is not an optimisation bolted onto attention, it is a
  consequence of causal masking. Nothing about an earlier token's K and V can
  change, so recomputing them is pure waste.
- Understood: the cost moves rather than disappearing. You trade quadratic
  recomputation for memory that grows with every token  which is exactly the
  problem PagedAttention exists to manage, and why that topic follows this one.
- Not resolved: whether this video was ever produced. If a render, audio or a
  finished file turns up, this entry gets an appended update rather than an edit.
- Not resolved: the script file's modification date is 2026-09-03. That falls
  inside the 31 Aug  4 Sep window, so it is consistent with the tracker, but it
  is not evidence of when the research was done.