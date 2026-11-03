# What Is a Concept Map — Research Week, Aug 28 2026

**Series:** Medhavy research log
**Runtime target:** 5:15
**Format:** 3840 × 2160 (4K UHD), 24 fps, 16:9
**Style:** Brutalist
**Source:** Concept Map subsystem audit — schema, S3 layer, 6 API routes, editor client, admin tab, both sample fixtures

Every number in this script was read off the code or the fixtures. Sources are listed in Appendix C.

---

## Art direction

**Principle:** show the structure, don't decorate it. Brutalism here means the grid is visible, the labels are exposed, and nothing is softened. If an element looks designed, strip it back.

### Palette — four values, no more

| Role | Hex | Use |
|---|---|---|
| Ground | `#0A0A0A` | Background. Near-black, never pure black. |
| Paper | `#F2F0EB` | Type and rules. Warm off-white, never pure white. |
| Signal | `#E8452C` | One accent. Reserved for the single most important thing on screen. Never two red things at once. |
| Mute | `#6B6B6B` | Secondary labels, inactive states. |

### Type

- **Display/headline:** one grotesk — Archivo, Inter Tight, or Helvetica Now. Weight 700+. Tracking tight to −2%.
- **Data/labels:** one mono — JetBrains Mono or IBM Plex Mono. Weight 400/700.
- Two families total. No third.

Sizes at 4K:

| Element | px |
|---|---|
| Display | 320 |
| H1 | 180 |
| H2 | 96 |
| Body | 64 |
| Mono data | 44 |
| Mono label / caption | 32 |

### Grid

12 columns · 160 px outer margin · 120 px gutter. **Leave the grid faintly visible** — 1 px `#6B6B6B` at 12% opacity. The scaffolding is part of the look.

### Hard rules

- `border-radius: 0`. Everywhere.
- No gradients. No drop shadows. No glows. No blur.
- No crossfades or dissolves — **hard cuts only**.
- Text arrives by 2-frame step-reveal or hard snap. Nothing eases in.
- Borders are 4 px, visible, `#F2F0EB`.
- Every panel gets an exposed label in mono caps: `FIG. 03`, `§2.1`, `SOURCE: export/route.ts:76`.
- No stock footage, no people, no photography. Type, rule, and diagram only.

### Audio

- No music bed. One sustained low drone (~55 Hz) under the whole piece, or silence.
- Mechanical SFX on text snaps — a relay click, not a whoosh.
- VO dry, close, no reverb. Flat delivery. This is a lab note, not a trailer.

---

## Script

### SCENE 1 — COLD OPEN
**0:00 – 0:18**

> **VISUAL** — Ground fill. Silence, 1 second of empty frame. Then a table of contents snaps in as plain mono text, left column, unstyled:
> ```
> CH 21  CELL CYCLE CONTROL
> CH 22  CHEMOTHERAPEUTIC AGENTS
> CH 23  CLINICAL ONCOLOGY
> ```
> Hold 2 s. Then a red `#E8452C` line strikes through all three, left to right, 6 frames, linear.
>
> **ON SCREEN** (display, centered, hard snap): `THIS IS NOT A MAP`

**VO:**
A table of contents tells you the order the author wrote things. It tells you nothing about the order a student can actually learn them. This week I went through the Concept Map subsystem — the part of the hub that tries to fix that.

---

### SCENE 2 — THE DEFINITION
**0:18 – 0:55**

> **VISUAL** — Split frame, 6 cols / 6 cols, hard 4 px rule down the center.
> **LEFT**, label `FIG. 01 — SEQUENCE`: the same three chapters, stacked vertically, connected by plain grey arrows top to bottom.
> **RIGHT**, label `FIG. 02 — DEPENDENCY`: five nodes as hard-edged boxes, connected by red arrows pointing *backwards* into prerequisites. Deliberately not a neat tree — let it be lopsided.

**VO:**
A concept map is a knowledge graph of a textbook. Every teachable idea becomes a node. Every edge records what you need to understand first. Not what comes next in the book — what has to already be in your head for the next thing to mean anything.

> **ON SCREEN** (mono, lower third, step-reveal): `NODE = ONE TEACHABLE IDEA` / `EDGE = PREREQUISITE`

---

### SCENE 3 — ANATOMY OF A NODE
**0:55 – 1:35**

> **VISUAL** — Single node record fills frame as a bordered data table, mono, real values from the cancer fixture. Fields reveal one row at a time, 4 frames apart, top to bottom. `canonical_name` and `prerequisite_nodes` highlight in `#E8452C` as the VO reaches them.
>
> ```
> canonical_name      Paclitaxel
> aliases             ["Taxol", "paclitaxel"]
> chapter / section   22 / 1
> knowledge_type      factual
> prerequisite_nodes  ["cancer_22_1_microtubules"]
> confidence          high
> thin_content        false
> ```
>
> Label: `FIG. 03 — NODE RECORD` · `SOURCE: types/concept-map.ts:10`

**VO:**
Here's one, from the cancer textbook. Paclitaxel. Also called Taxol, which is what students will actually type. Chapter twenty-two, section one. It's a factual node — a drug name, not a mechanism. And it has one prerequisite: microtubules. Because Paclitaxel is meaningless until you know what it binds to.

> **ON SCREEN** (hard cut, display): `THE EDGE IS THE POINT`

**VO:**
The name is the easy part. The edge is the part that's worth building a whole review tool for.

---

### SCENE 4 — WHY HUMANS
**1:35 – 2:15**

> **VISUAL** — Full-frame bar chart, brutalist: solid blocks, no axis decoration, values printed in mono directly on each bar. Bars snap in left to right on 3-frame steps.
>
> ```
> CONFIDENCE, 25-NODE RUN
> HIGH    ████████████████████  9
> MEDIUM  ██████████████████████  10
> LOW     █████████████  6
> ```
> The `LOW 6` bar fills `#E8452C`. Everything else Paper.
>
> Then hard cut to: `THIN_CONTENT: 2` in display type, red.

**VO:**
The nodes are machine-generated. A Python pipeline reads the book, cross-references Wikipedia, and emits candidates. Machine extraction like this is roughly right and locally wrong — it invents concepts the book doesn't teach, merges two ideas into one, and picks the Wikipedia title over the term the professor actually uses.

The pipeline knows this about itself. In the sample run: twenty-five nodes, and it flags six as low confidence and two as thin on source material.

> **ON SCREEN** (mono, snap): `THE PIPELINE MARKS ITS OWN WEAK SPOTS`

**VO:**
So the whole editor is one thing. A human gate between a machine guess and a trusted artifact.

---

### SCENE 5 — THE FOUR STAGES
**2:15 – 3:10**

> **VISUAL** — Horizontal four-panel band across the full 3840 width, each panel 4 px bordered, numbered `01`–`04` in mono caps at 96 px. Panels light one at a time — inactive panels at `#6B6B6B`, active panel Paper with a red top rule. Hard cut between each, no slide.
>
> `01 GENERATE` · `02 IMPORT` · `03 REVIEW` · `04 EXPORT`
>
> Under the active panel, the relevant path or action in mono 44 px.

**VO:**
Four stages.

**One — generate.** The pipeline writes JSON to S3, under the pipeline prefix, one file per run. That part is external. Not in this repo.

**Two — import.** An admin pulls a run into the hub. It gets validated, and every node lands in the database marked *pending*.

**Three — review.** A domain expert goes node by node. Three verdicts only: **accept** — the pipeline got it right. **Edit** — right concept, wrong name. **Remove** — this isn't something the book teaches. They can also add what the pipeline missed entirely.

> **VISUAL** — On "three verdicts", the three words snap in as stacked red blocks, then the removal one gets struck through.

**Four — export.** And this is the part I'd underline: export is hard-blocked while a single node is still pending. There's no ship-it-mostly-reviewed path. One unreviewed node out of twenty-five, and the button stays dead.

> **ON SCREEN** (display, red, held 2 s): `ZERO PENDING OR NOTHING`

---

### SCENE 6 — WHAT GETS THROWN AWAY
**3:10 – 3:45**

> **VISUAL** — The FIG. 03 node record returns, same position, same values. Then three rows are struck through in red and fall out of frame on a 2-frame step, and the remaining rows close the gap with a hard snap:
> ```
> wikipedia_categories   ─────────
> confidence             ─────────
> source_url             ─────────
> ```
> Label: `FIG. 04 — VERIFIED OUTPUT` · `SOURCE: export/route.ts:62`

**VO:**
On the way out, three fields get stripped. Wikipedia categories, confidence, and source URL — gone.

That's deliberate, and it's the cleanest design decision in the subsystem. Those fields aren't facts about the book. They're scaffolding for the reviewer. Confidence is the machine telling a human where to look hardest. Once a human has looked, the number has done its job and it would be misleading to ship it downstream.

> **ON SCREEN** (mono): `SCAFFOLDING ≠ CONTENT`

---

### SCENE 7 — THE HONEST FINDING
**3:45 – 4:25**

> **VISUAL** — Full frame goes Ground. A single pipeline diagram draws left to right in Paper hairlines: `PIPELINE → IMPORT → REVIEW → EXPORT → S3`. Then a final arrow extends right from S3 toward the frame edge — and terminates in nothing. Empty space held for 3 full seconds. No sound.
>
> Then, mono, small, bottom right: `grep: 0 consumers`

**VO:**
Now the part I want on the record.

I checked what reads these verified maps back. Nothing does. The write function has no counterpart. The verified type is imported by exactly two files — the thing that writes it, and the thing that defines it. Nothing in the hub ever opens the verified prefix again.

The consumers are supposed to be the textbook sites, and that work is still roadmap — it's listed as a deliverable for the next-generation chassis, not as shipped code.

> **ON SCREEN** (display, red, hard snap): `STORED, NOT SPENT`

**VO:**
The review pipeline is complete and correct. The consumption side is empty. That's worth knowing before anyone invests another week in the editor.

---

### SCENE 8 — THE CRACK
**4:25 – 4:55**

> **VISUAL** — Three connected node boxes: `PACLITAXEL`, `CISPLATIN`, `DOXORUBICIN`, all with red edges pointing into a fourth box, `MICROTUBULE DYNAMICS`.
> On "removes it", the fourth box hard-cuts out of existence — no fade. The three red edges remain, now pointing at empty frame.
> Hold 3 s.
> Label: `FIG. 05 — DANGLING EDGE` · `SOURCE: export/route.ts:76`

**VO:**
One more thing, and it follows directly from how the graph is built.

Prerequisites are stored as ID references. Removal is a valid verdict. So a reviewer can quietly break the graph — remove a node that three other nodes depend on, and the export drops it but copies every surviving node's prerequisite list through untouched. No re-validation. You get a verified map with edges pointing at something that isn't in the file.

Both sample fixtures are clean right now — eighteen edges each, nothing dangling. So it hasn't bitten anyone. But nothing prevents it, and the reviewer gets no warning that the node they're about to remove is load-bearing.

> **ON SCREEN** (mono): `18 EDGES · 0 DANGLING · TODAY`

---

### SCENE 9 — CLOSE
**4:55 – 5:15**

> **VISUAL** — Hard cut to Ground. Four lines of mono, 64 px, left-aligned on the 2nd column, step-revealed one per beat. Then everything cuts to black except the last line.

**VO:**
So: this week's summary.

**A concept map is a dependency graph of a textbook.** The editor exists because the machine that builds it is confidently wrong in local ways. The review gate is strict and it works. The output is correct, complete, and currently going nowhere.

Next week I'm looking at what it would take to actually spend it.

> **ON SCREEN:**
> ```
> CONCEPT MAP = DEPENDENCY GRAPH
> REVIEW GATE = STRICT, WORKING
> OUTPUT      = CORRECT
> CONSUMERS   = 0
> ```
> Hold `CONSUMERS 0` in red for 2 s. Hard cut to black.

---

## Appendix A — On-screen text assets

Every string that must be set. Mono unless marked DISPLAY.

| # | Scene | Text |
|---|---|---|
| 01 | 1 | `THIS IS NOT A MAP` **(DISPLAY)** |
| 02 | 2 | `FIG. 01 — SEQUENCE` / `FIG. 02 — DEPENDENCY` |
| 03 | 2 | `NODE = ONE TEACHABLE IDEA` / `EDGE = PREREQUISITE` |
| 04 | 3 | Node record, 7 rows (values in Appendix C) |
| 05 | 3 | `THE EDGE IS THE POINT` **(DISPLAY)** |
| 06 | 4 | `HIGH 9` / `MEDIUM 10` / `LOW 6` / `THIN_CONTENT: 2` |
| 07 | 4 | `THE PIPELINE MARKS ITS OWN WEAK SPOTS` |
| 08 | 5 | `01 GENERATE` `02 IMPORT` `03 REVIEW` `04 EXPORT` |
| 09 | 5 | `ACCEPT` / `EDIT` / `REMOVE` |
| 10 | 5 | `ZERO PENDING OR NOTHING` **(DISPLAY)** |
| 11 | 6 | `wikipedia_categories` `confidence` `source_url` — struck |
| 12 | 6 | `SCAFFOLDING ≠ CONTENT` |
| 13 | 7 | `grep: 0 consumers` |
| 14 | 7 | `STORED, NOT SPENT` **(DISPLAY)** |
| 15 | 8 | `FIG. 05 — DANGLING EDGE` |
| 16 | 8 | `18 EDGES · 0 DANGLING · TODAY` |
| 17 | 9 | Four-line summary block |

## Appendix B — Shot list

| Scene | Shot | Duration | Build |
|---|---|---|---|
| 1 | TOC + strike | 0:18 | Static + 6f line wipe |
| 2 | Split diagram | 0:37 | Two static diagrams, hard cut between |
| 3 | Node table | 0:40 | 7 rows × 4f step-reveal |
| 4 | Bar chart | 0:40 | 3 bars × 3f step |
| 5 | Four-panel band | 0:55 | 4 hard cuts, panel state change only |
| 6 | Strip-out | 0:35 | 3 strikethroughs + gap close |
| 7 | Pipeline to nowhere | 0:40 | Hairline draw + 3 s hold |
| 8 | Dangling edge | 0:30 | Box removal, edges persist, 3 s hold |
| 9 | Summary block | 0:20 | 4 lines × 1 beat |

Nine setups. No camera moves, no 3D, no particle work — every shot is type and rule on a fixed frame. Renders fast at 4K.

## Appendix C — Facts used, with sources

All paths below are relative to the `medhavi-hub` repository root, verified against branch `chaitanya` at commit `7f10aaa` (2026-08-24). This script lives outside that repo, so the paths are references, not links.

| Claim in script | Source |
|---|---|
| Node fields and shape | `types/concept-map.ts:10` |
| Paclitaxel record, prereq = microtubules | `scripts/20260421_120000.json` |
| 25 nodes, 18 prerequisite edges, 0 dangling | Both fixtures, verified by count |
| Confidence 9 high / 10 medium / 6 low | `scripts/20260421_120000.json` |
| 2 nodes flagged `thin_content` | `scripts/20260421_120000.json` |
| Knowledge types 13 factual / 9 conceptual / 3 procedural | `scripts/20260421_120000.json` |
| Export blocked while any node pending | `app/api/concept-map/sessions/[id]/export/route.ts:38` |
| Three fields stripped on export | `app/api/concept-map/sessions/[id]/export/route.ts:62` |
| Prerequisites copied verbatim, not re-validated | `app/api/concept-map/sessions/[id]/export/route.ts:76` |
| Zero readers of the verified prefix | `grep` across repo — `writeVerifiedMap` has no counterpart |
| `VerifiedConceptMap` imported by 2 files only | `lib/concept-map/s3.ts`, `.../export/route.ts` |
| Consumption is roadmap, not shipped | `DEVELOPER.md:569` |

**Not claimed on camera, deliberately:** the import/permissions defects from the audit (missing run picker, instructor import contradiction, unenforced `textbook_id` invariants). They're implementation bugs, not part of *what a concept map is*. Hold them for a separate segment.
