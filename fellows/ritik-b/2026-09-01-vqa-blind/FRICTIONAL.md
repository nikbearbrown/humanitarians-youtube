# Frictional log — Week of 2026-09-01

Process log for this piece of work, kept beside the evidence it describes. Entries are dated
and appended; earlier entries are never rewritten. See <https://www.humanitarians.ai/fellows>.

## Week of 2026-09-01 — reconstructed 2026-11-25

### Visual Question Answering, Blind?

**What I was working on.** An explainer on visual question answering with transformers, as two 4K masters with the same content — 16:9 and 9:16 — under two minutes.

**What I tried and expected.** One responsive React component per beat, registered at both canvases, so the portrait cut would be the same content rather than a crop or a derived Short. I expected parity between the cuts to come almost for free.

**Where the work resisted, and what I did next.** QC found 16 defects, three of them blockers: an entrance animation slid a row into the title-safe margin, a content-sized flex row pushed a token strip past the portrait edge, and the toolkit's 9:16 verdict scene never rendered its citation. B06's bracket spanned all four bars instead of blind-versus-sighted, so it asserted the wrong comparison; it is now composed from the rows themselves. Fixing the outro's fill by scaling the type created a new edge-bleed blocker, so fill and width were separated. Two of the toolkit fixes ship as `patches/brutalist-toolkit.patch`.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent, wrote the scenes, narration and patches, and ran the gates. GATE P (narration) was self-signed by the build agent at my instruction; it still needs a human read before anyone sees the video.

**What I understand now, and what I still don't.** Size everything from the safe box rather than magic numbers, read frames in both orientations, and remember that GATE V can't see a clip of the wrong length. Still open: B05 shows an illustrative softmax rather than a real checkpoint's output, so it is the one beat that still asks the viewer for trust.

### BLIP: Noisier Data, Better Model?

**What I was working on.** An explainer on BLIP's bootstrapping — a captioner writes new captions for web images and a separate filter throws out the ones that don't match — as two 4K masters, 16:9 and 9:16, from one beat sheet. It was my second dual-orientation reel, after VQA.

**What I tried and expected.** I expected the VQA approach (one responsive component per beat, registered at both canvases) to carry straight over, and I expected the story to be BLIP's architecture.

**Where the work resisted, and what I did next.** The story turned out not to be the architecture: it's that BLIP tests its own training data and publishes the evidence — the run with the bootstrap switched off (Table 1), the cost of letting the filter share weights with the captioner (rejection drops from 25% to 8%, Table 4), and nucleus sampling winning despite being rejected more often (Table 2). I rebuilt the reel around a four-question audit a viewer can run on any paper. QC found canvas-fill and legibility defects (a filter strike that read as an underline, an axis label clipped to "ViT-B/1"), plus two defects that only appeared in 9:16, both traced to a missing `minWidth: 0` on the scene roots. The narration first ran over the two-minute cap and was cut back to 1:58.7. A deleted temp file crashed the render pass; the retry skipped a clip that existed at the wrong length, and the compile step silently centre-cut B09 from 30.1 s to 11.9 s — the wrong eleven seconds. I added `check_clips.py` to assert every clip's length before compiling.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent, wrote the scenes, narration, authoring and check scripts, and ran the gates. Accepted: the audit-first restructure and every QC fix in BUILD-LOG-blip-bootstrap.md. The narration review (GATE P) still needs a human read.

**What I understand now, and what I still don't.** Emitting both beat sheets from one `author_sheets.py` makes the two cuts identical by construction, and frame-level QC can't see a clip of the wrong length — that has to be checked separately. Still open: the GATE P signature.

## 2026-11-25 — GATE P signed off

I reviewed both masters of each video — Visual Question Answering, Blind? and BLIP: Noisier Data,
Better Model? — and signed off the narration review (GATE P) for both. The open GATE P items above
are closed.

## 2026-11-25 — Week 1 progress update (made later than the week it describes)

### Week 1 Progress: VQA and BLIP

**What I was working on.** The week's progress update, which wasn't made during the week of 2026-09-01: a one-minute
16:9 video on what the two explainers shipped, what broke on the way and what is still open. Written and built
2026-11-25 from this folder's build logs, READMEs and PROOF reviews, and labelled on screen as made later.

**What I tried and expected.** The same six toolkit patterns as the later weeks' updates, with every figure taken from
a file in this folder, so nothing new had to be researched.

**Where the work resisted, and what I did next.** The VQA defect count isn't stated anywhere as one number; I counted
the two defect tables in `BUILD-LOG.md` (12 + 4 = 16). The first narration measured 0:51, so three beats each gained a
sentence voiced over a caption already on screen — 0:56.6.

**What Claude or another person contributed — and what I accepted, changed or rejected.** Claude, as the build agent,
drafted the update from this folder's records, ran a short PROOF check on it and rendered it. I asked for it and
accepted it.

**What I understand now, and what I still don't.** The week's real lesson was reading both orientations by hand: two of
BLIP's defects existed only in 9:16. Still open: the illustrative softmax beat in VQA and two BLIP captions on trust.
