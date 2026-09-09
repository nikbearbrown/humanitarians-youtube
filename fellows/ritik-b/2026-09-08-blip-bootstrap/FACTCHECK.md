# FACTCHECK — "BLIP: Noisier Data, Better Model?"

Every number that appears on screen, and where it comes from. One primary source:

> Junnan Li, Dongxu Li, Caiming Xiong, Steven C. H. Hoi. **BLIP: Bootstrapping
> Language-Image Pre-training for Unified Vision-Language Understanding and Generation.**
> ICML 2022 (PMLR 162), pp. 12888–12900. arXiv:2201.12086v2 (15 Feb 2022).

Tables were read from the paper body, not from a summary. The rule for this reel: if a
figure is not in Table 1, Table 2, Table 4, or §3.1–3.3, it does not go on screen.

## Table 1 — the CapFilt ablation (14M block, ViT-B/16, finetuned COCO 5K test)

| C | F | TR@1 | IR@1 | COCO CIDEr |
|---|---|---|---|---|
| ✗ | ✗ | **78.4** | 60.7 | **127.8** |
| ✗ | ✓ | **79.1** | 61.5 | 128.2 |
| ✓ | ✗ | **79.7** | 62.0 | 128.9 |
| ✓ | ✓ | **80.6** | 63.1 | **129.7** |

129M block (COCO+VG+CC+SBU+LAION, ViT-B/16): no bootstrap **79.6** / 62.0 / **130.1**;
with captioner + filter 81.9 / 64.3 / 131.4.

**Used at:** B00 output lines, B01 card 3, B07 (all five bars, the reference line, and the
exception), B08 verdict line 4.

- The five B07 bars are the four 14M rows plus the 129M no-bootstrap row. Same vision
  backbone (ViT-B/16) and same evaluation in every row, so the bootstrap is the only
  variable — which is the whole point of using this block rather than the SOTA tables.
- **The exception is published, not softened.** On COCO captioning the raw 129M run scores
  CIDEr 130.1 against the bootstrapped 14M's 129.7. The reel says so on the same beat as
  the retrieval claim.
- "Nine times the data" is arithmetic on the paper's own dataset sizes: 129M / 14M ≈ 9.2.

## Table 2 — generation method for the captioner (14M images)

| Method | Noise ratio | COCO TR@1 | IR@1 | COCO CIDEr |
|---|---|---|---|---|
| None | N.A. | **78.4** | 60.7 | 127.8 |
| Beam | **19%** | **79.6** | 61.9 | 128.9 |
| Nucleus | **25%** | **80.6** | 63.1 | 129.7 |

**Used at:** B04 (the 25% rate and the twenty tiles), B06 (all three rows, both wings),
B08 verdict line 3.

- "Noise ratio" is the paper's own term for the share the filter rejects. §4.3: nucleus
  sampling "leads to evidently better performance, despite being more noisy as suggested by
  a higher noise ratio from the filter."
- The None row's 78.4 is the same baseline as Table 1's ✗/✗ row, so B06's first row and
  B07's first bar are the same measurement and cannot disagree.
- Nucleus threshold p = 0.9 (§4.3), shown as B06's row subtitle.
- §4.3's explanation, paraphrased in B06's closing line: nucleus sampling "generates more
  diverse and surprising captions, which contain more new information that the model could
  benefit from," whereas "beam search tends to generate safe captions that are common in
  the dataset."

## Table 4 — captioner and filter sharing parameters (14M images)

| | Noise ratio | COCO TR@1 | IR@1 | COCO CIDEr | NoCaps ZS CIDEr |
|---|---|---|---|---|---|
| Share parameters | **8%** | **79.8** | **62.2** | **129.0** | **103.5** |
| Decoupled | **25%** | **80.6** | **63.1** | **129.7** | **105.1** |

**Used at:** B02 (axis 2's receipt), B05 (both rejection rates and all four metric rows),
B08 verdict line 2.

- §4.4 attributes the drop to confirmation bias: "noisy captions produced by the captioner
  are less likely to be filtered out by the filter, as indicated by the lower noise ratio
  (8% compared to 25%)."
- The four deltas B05 prints (+0.8, +0.9, +0.7, +1.6) are **computed at render time** from
  the two columns beside them, so they cannot drift from the numbers they describe.

## §3.1–3.3 — the mechanism (no numbers, all structural)

| On screen (B03, B04) | Paper |
|---|---|
| Three functionalities: unimodal encoder / image-grounded text encoder / image-grounded text decoder | §3.1, verbatim naming |
| Unimodal encoder has no cross-attention; text encoder same as BERT with a `[CLS]` token | §3.1(1) |
| Image-grounded encoder inserts one cross-attention layer between SA and FFN | §3.1(2) |
| Image-grounded decoder replaces bi-directional SA with causal SA | §3.1(3) |
| ITC aligns the two feature spaces · ITM is binary matched/unmatched · LM generates captions | §3.2 |
| "share every parameter except the self-attention layers" | §3.2, verbatim claim |
| Captioner = image-grounded text decoder finetuned with LM; filter = image-grounded text encoder finetuned with ITC + ITM | §3.3 |
| The filter removes noisy texts from **both** the web texts and the synthetic ones | §3.3 |
| Both modules initialised from the same pre-trained MED and finetuned individually on COCO | §3.3 |

## Illustrative, and labelled as such on screen

| Item | Beat | What is real, what is not |
|---|---|---|
| The web image | B04 | **Drawn** (REBUILD LAW — the reel lifts no photos). A stand-in for a web image, not a paper figure. |
| `Tw` = "IMG_2043 · 1200x800 · stock photo" and `Ts` = "a dog running on the beach near the water" | B04 | **Invented strings** showing the CLASS of failure §3.3 describes ("the alt-texts often do not accurately describe the visual content"). Figure 4's actual examples are raster text in the PDF and were not transcribed, so nothing is passed off as quoted. The beat carries the line "Illustrative: the mechanism and the rate are the paper's, the two strings are not a paper figure." |

## Chart parameters declared on screen

Both B06 and B07 plot spreads of about two points, which are invisible on a 0–100 axis.
Both truncate, and both say so: B06 prints "COCO TR@1 — axis starts at 77" and
"NOISE RATIO — 0 to 30%"; B07 draws a real axis strip with a break glyph and both tick
values (77 and 81.5). Nothing is plotted on an undeclared axis.

## Deliberately NOT claimed

- The abstract's **+2.7 recall@1 / +2.8 CIDEr / +1.6 VQA score** are gains over prior state
  of the art, not the bootstrap's contribution. The reel never uses them — it uses the
  ablations, where the bootstrap is the only variable.
- No VQA, NLVR², or video-retrieval numbers, though the paper reports them. Out of scope
  for a two-minute reel about the data loop.
- No claim about BLIP-2, CLIP, or any model after 2022, and no claim that CapFilt is what
  modern VLMs do.
- No claim about LAION's absolute quality — only that 129M raw web images with no
  bootstrap score 79.6 where 14M bootstrapped score 80.6 on this benchmark.
