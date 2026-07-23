# SHOTLIST — vox-fluency-seam
*The Seam Where Fluency Sneaks Back In*

---

## Histogram

| Beat | Type | Source | Motion | Act | Est. duration |
|------|------|--------|--------|-----|--------------|
| B01 | CARD | own | hold | COLD OPEN | 9s |
| B02 | GRAPHIC | own | drawon | COLD OPEN | 13s |
| B03 | CARD | own | hold | THE QUESTION | 10s |
| B04 | STILL | ai | kenburns | THE PROBLEM | 12s |
| B05 | GRAPHIC | own | annotate | THE PROBLEM | 11s |
| B06 | GRAPHIC | own | drawon | THE MECHANISM | 13s |
| B07 | GRAPHIC | own | annotate | THE IMPLICATION | 12s |
| B08 | GRAPHIC | own | annotate | THE EXAMPLE | 20s |
| B09 | CARD | own | hold | RECAP | 10s |

Total estimated: ~110s (1:50) — within 2–3 min band

## Rhythm check
- CARD → GRAPHIC → CARD → STILL → GRAPHIC → GRAPHIC → GRAPHIC → GRAPHIC → CARD
- No more than 2 consecutive same-type beats: B06/B07/B08 are three consecutive GRAPHICs — acceptable as they serve the core mechanism with distinct motions (drawon, annotate, annotate)

## Act map
- B01–B02: COLD OPEN (concrete situation, stakes)
- B03: THE QUESTION (on screen + narration, gap formula)
- B04–B05: THE PROBLEM (naive expectation, invisible seam)
- B06: THE MECHANISM (the one-question test, decision tree)
- B07: THE IMPLICATION (authority borrowing, real-world bite)
- B08: THE EXAMPLE (illustrative full walkthrough — mandatory 16:9)
- B09: RECAP (question answered, one line)

## Color law
TEAL #1F6F5C = verified data claim / traceable / counting
CRIMSON #BF3339 = model judgment / unsourced / fluent fabrication
Never swap mid-film. Gold = editor's pen, once (B07 only).

## Exclusion confirmations
- NO full verified-data pipeline architecture: confirmed absent
- NO three-pipeline technical detail (SEC/ATS/BLS): confirmed absent
- NO caching mechanism explanation: confirmed absent
- Only the seam at the reading layer: confirmed

---

## Open slots (fill-in beats)

### B04 — STILL · ai

**Beat:** B04 — THE PROBLEM — DOL database record printout

**Archive search:**
- Wikimedia Commons: search "Department of Labor" "LCA" or "Labor Condition Application"
- archive.org: historical DOL disclosure file screenshots
- Any public DOL disclosure data screenshot (rows of company/filing data)

**Generative prompt:**
```
B04, printed Department of Labor Labor Condition Application disclosure database record, rows of employer names and H-1B filing counts in a plain government table, printed on aged cream newsprint, flat editorial collage reproduction, desaturated photography, no people, camera push-in framing centered on count columns, muted institutional feel
```

**Provenance note:** DOL H-1B disclosure data is public record (dol.gov). A screenshot of the actual disclosure file is archival; a generated editorial illustration is a stand-in.

---

## Shots requiring no fill (own-Manim)

| Beat | Manim class | Description |
|------|------------|-------------|
| B01 | B01_Title | Title card with eyebrow "THE REALLOCATION ENGINE" |
| B02 | B02_ModelOutput | Five sentences appear sequentially, all ink, no color yet |
| B03 | B03_QuestionCard | Question card: "Where does a real number end and a fabricated conclusion begin?" |
| B05 | B05_SeamInvisible | Paragraph reappears with a vertical dashed seam line between sentence 2 and 3 |
| B06 | B06_DecisionTree | Decision tree, split move — teal YES branch, crimson NO branch |
| B07 | B07_AuthorityBorrow | Teal verified block → gold highlight → crimson judgment chain |
| B08 | B08_ColorCodedParagraph | Five sentences colored one by one: 2 teal, 3 crimson |
| B09 | B09_End | Endcard recap |
