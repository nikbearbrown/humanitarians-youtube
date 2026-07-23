# SHOTLIST — nbb-brutalist-agentic-system

Typed work order. Shot type locked; source = own throughout (pure Manim + Remotion, no request cards).
Teardown palette: `#FFFFFF` ground / `#2A1A0E` INK / `#C8102E` CRIMSON / `#545454` SLATE / `#D4D4D4` HAIRLINE.
Typography: Montserrat (display) · EB Garamond (serif) · PT Mono (mono/code).

---

## B00 — HOOK | REMOTION · BrutalistTerminalOpen

**Renders:** `media/B00.mp4`  
**Pattern:** `BrutalistTerminalOpen`  
**Props:**
```json
{
  "command":  "$ art explainer 'What is inside the Brutalist agentic system exactly?'",
  "topic":    "AGENTIC SYSTEM TAXONOMY",
  "checklist": [
    "beat sheet written  (contract — specifying)",
    "audio generated    (voice_id exact — specifying)",
    "graphics rendered  (fps=24 exact — specifying)",
    "personas applied   (register:Teardown — influencing)"
  ]
}
```
**Visual intent:** Dark terminal on flat-white ground. Command typewriters in red prompt. Four checklist items tick in staggered — the last item ("personas applied — influencing") is marked differently to pre-seed the puzzle. The checklist contrast IS the hook.

---

## B01 — INSTANCE | GRAPHIC · Manim: B01_CascadeFlow

**Renders:** `manim/B01_CascadeFlow.mp4`  
**Scene class:** `B01_CascadeFlow`  
**Visual:** Left-to-right flow. Boxes in INK with hairline borders: `beat_sheet.json` (label: CONTRACT) → `orchestrator` → `doer` → branch: top arm `ElevenLabs` (sub-label `voice_id — exact`, PT Mono), bottom arm `Manim` (sub-label `fps=24 — exact`, PT Mono) → `compile` → `mp4` (CRIMSON border, label `taste-judged`). Arrows draw on sequentially. Branch arms reveal together; merge arrow arrives last. Duration = beat's audio window.

---

## B02 — INSTANCE | GRAPHIC · Manim: B02_TwoInputsCompare

**Renders:** `manim/B02_TwoInputsCompare.mp4`  
**Scene class:** `B02_TwoInputsCompare`  
**Visual:** Split frame, equal halves. Left card (INK border, Montserrat header `SPECIFIES`): `fps = 24` in PT Mono, equals sign below, then `output: 24 frames/sec · guaranteed · reproducible` in INK serif. Right card (SLATE border, header `INFLUENCES`): `register: Teardown` in PT Mono, tilde `~` below, three greyed output lines, one highlighted with CRIMSON arrow: `output: ??? · emergent · unjudgeable by schema`. Left card draws on first; right card second. The tilde and three greyed lines are the visual payoff — arrives with the narration word "bias".

---

## B03 — ABSTRACTION | REMOTION · NikBearBrownCodeBlock

**Renders:** `media/B03.mp4`  
**Pattern:** `NikBearBrownCodeBlock`  
**Props:**
```json
{
  "filename": "axis-1.py",
  "segment":  "AXIS 1",
  "topic":    "SPECIFIES vs INFLUENCES",
  "language": "python",
  "caption":  "axis 1 — the determinism split",
  "code":     "# SPECIFIES — names the exact output\nfps      = 24                 # same in → same out\nvoice_id = 'VOICE_NBB'        # same in → same out\nhex_code = '#C8102E'          # same in → same out\n\n# INFLUENCES — biases a distribution\nregister = 'Teardown'         # same in → emergent out\npersona  = 'script-writer'    # same in → emergent out\nprompt   = '...'              # same in → emergent out"
}
```
**Visual intent:** Code block in teardown palette. The two comment blocks (SPECIFIES / INFLUENCES) reveal in sequence keyed to narration. The contrast between `# same in → same out` and `# same in → emergent out` is the point.

---

## B04 — TRANSFORM | GRAPHIC · Manim: B04_UnderdeterminationDiagram

**Renders:** `manim/B04_UnderdeterminationDiagram.mp4`  
**Scene class:** `B04_UnderdeterminationDiagram`  
**Visual:** Two columns. Left — `OVERDETERMINED`: one INK input box (`#C8102E`, label `hex code`) at top; single thick arrow to one output box: `one right answer`. Right — `UNDERDETERMINED`: one SLATE input box (`register: Teardown`) at top; five thin arrows fanning to five greyed output boxes; one box highlighted with CRIMSON arrow labeled `model selects`. Below each column, small serif label: `hex code` (left) / `persona` (right). Centered footer in EB Garamond italic: `Not a temperature problem. A structure problem.` Left column draws first; right column's fan of arrows draws second for contrast.

---

## B05 — ABSTRACTION | REMOTION · NikBearBrownCodeBlock

**Renders:** `media/B05.mp4`  
**Pattern:** `NikBearBrownCodeBlock`  
**Props:**
```json
{
  "filename": "axis-2.py",
  "segment":  "AXIS 2",
  "topic":    "INPUTS vs ARTIFACTS",
  "language": "python",
  "caption":  "axis 2 — before-the-run vs produced-by-the-run",
  "code":     "# INPUTS — authored before the run\nbefore_run = [persona, parameters, scripts]\n\n# ARTIFACTS — what the run leaves behind\nproduced   = [beat_sheet_json, mp4, logs]\n\n# axes are INDEPENDENT — the same object can be both:\n# beat_sheet.json = input(to='compile') + artifact(of='planning')\nassert beat_sheet in before_run and beat_sheet in produced"
}
```
**Visual intent:** The `assert` line is the visual anchor — the "both" case lands with narration "A beat sheet is both."

---

## B06 — TRANSFORM | GRAPHIC · Manim: B06_TwoAxesMatrix

**Renders:** `manim/B06_TwoAxesMatrix.mp4`  
**Scene class:** `B06_TwoAxesMatrix`  
**Visual:** 2×2 matrix with INK axis lines. Y-axis label: `SPECIFIES` (top) / `INFLUENCES` (bottom). X-axis label: `INPUT` (left) / `ARTIFACT` (right). Quadrant contents draw in one at a time in narration order: TL `voice_id · fps=24 · hex_code`; BL `persona · register · prompt`; TR `beat_sheet.json · compile output`; BR `mp4` with a CRIMSON corner triangle marker (filled triangle in corner) and label `taste-judged — no schema possible`. The BR corner mark arrives last with emphasis — it is the punchline. Axis labels in Montserrat tracked caps.

---

## B07 — INSTANCE | GRAPHIC · Manim: B07_InputStackLayers

**Renders:** `manim/B07_InputStackLayers.mp4`  
**Scene class:** `B07_InputStackLayers`  
**Visual:** Six horizontal bars, full width, stacking top-to-bottom. Bars reveal staggered (each after ~0.4s lag). Bar widths decrease slightly from top to bottom (widest = most underdetermined). 
1. `HUMAN` — darkest INK fill; label `HUMAN — goal · taste · irreplaceable`  
2. `LLM` — INK fill; label `LLM — distribution over text`  
3. `CONDITIONING TEXT` — SLATE; label `CONDITIONING TEXT — persona × register × brand`  
4. `AGENT` — SLATE; label `AGENT — orchestrator + doer`  
5. `PARAMETERS` — lighter SLATE; label `PARAMETERS — fps · voice_id · stability`  
6. `SCRIPTS` — HAIRLINE fill, INK border; label `SCRIPTS — generate_audio.py · compile.py`  
Left margin bracket: `MOST INFLUENCING` in CRIMSON at top, `MOST SPECIFYING` in INK at bottom. Bracket draws on after all bars land.

---

## B08 — INSTANCE | REMOTION · NikBearBrownTerminalAsk

**Renders:** `media/B08.mp4`  
**Pattern:** `NikBearBrownTerminalAsk`  
**Props:**
```json
{
  "command":     "$ why is the human irreplaceable at the top of the stack?",
  "topic":       "AGENTIC SYSTEM",
  "segment":     "HUMAN LAYER",
  "runningText": "analyzing stack structure…",
  "output": [
    "human:     carries goal + taste  ← irreplaceable BY STRUCTURE",
    "llm:       distribution over text ← no goal, no stakes",
    "gap:       human wants something specific — LLM does not",
    "verdict:   no agent in the stack can substitute for this"
  ]
}
```
**Visual intent:** The `BY STRUCTURE` annotation lands with narration "Not by choice. By structure."

---

## B09 — INSTANCE | GRAPHIC · Manim: B09_ConditioningTextStack

**Renders:** `manim/B09_ConditioningTextStack.mp4`  
**Scene class:** `B09_ConditioningTextStack`  
**Visual:** Three SLATE boxes appear left to right with `+` signs between them, then a bottom bar appears. Box 1 `METHOD PERSONA` — examples `script-writer · explainer · bio`, sub-label `(WHAT to produce)`. Box 2 `VOICE REGISTER` — examples `Teardown · sardonic · wonder`, sub-label `(HOW it sounds)`. Box 3 `BRAND` — examples `NikBearBrown · Hai · Medhavy`, sub-label `(WHOSE voice)`. After all three land, they compress into a single INK bar below labeled `CONDITIONING TEXT` with a downward arrow to an LLM node (circle) labeled `steers the distribution`. The stacking compression motion is the visual payoff for "these stack."

---

## B09B — TRANSFORM | GRAPHIC · Manim: B09B_OneWriterManyCostumes

**Renders:** `manim/B09B_OneWriterManyCostumes.mp4`  
**Scene class:** `B09B_OneWriterManyCostumes`  
**Visual:** Center: one INK circle labeled `doer — LLM + goal + tool-loop`. Three thin SLATE rings orbit it, each labeled: `persona: script-writer`, `register: Teardown`, `brand: NikBearBrown`. These are overlays — transparent rings, not boxes, to show they are parameters not separate entities. Off to the right: an alternative diagram of THREE separate agent nodes (each labeled `agent`) with a large CRIMSON `✕` through the whole cluster and label `wrong model`. Bottom centered text in EB Garamond italic: `one writer · many costumes — not many writers.`

---

## B10 — INSTANCE | REMOTION · NikBearBrownCodeBlock

**Renders:** `media/B10.mp4`  
**Pattern:** `NikBearBrownCodeBlock`  
**Props:**
```json
{
  "filename": "agent.py",
  "segment":  "AGENT LAYER",
  "topic":    "AGENT COMPOSITE",
  "language": "python",
  "caption":  "agent = composite, not monolith",
  "code":     "class Agent:\n    llm          = distribution_over_text\n    conditioning = persona + register + brand  # the costume\n    tool_loop    = [read, write, run, call]\n    goal         = what_to_produce\n\nclass Orchestrator(Agent):  # sequences + gates\n    owns_contract = True\n    hits_gates    = True\n\nclass Doer(Agent):          # one focused job\n    job = write | scout | build | conform\n    # register is a PARAMETER of the doer, not a separate agent"
}
```
**Visual intent:** The inline comment `# register is a PARAMETER of the doer` is the visual payoff — arrives with "The register the doer wears is not the doer."

---

## B11 — INSTANCE | GRAPHIC · Manim: B11_UtilityBelt

**Renders:** `manim/B11_UtilityBelt.mp4`  
**Scene class:** `B11_UtilityBelt`  
**Visual:** Header bar (Montserrat tracked caps): `THE UTILITY BELT`. Three script boxes in a horizontal row: `generate_audio.py`, `remotion_scenes.py`, `compile.py`. Each has an input arrow from the left (label in PT Mono: `voice_id, stability` / `fps=24, width=1920` / `clips/, beat_sheet`) and an output arrow to the right: `deterministic output`. A strikethrough speech bubble in CRIMSON floats above the row: `taste gate?` with a CRIMSON strikethrough line across it — marking its absence. Script boxes reveal left to right; strikethrough bubble arrives last.

---

## B12 — INSTANCE | GRAPHIC · Manim: B12_ArtifactClasses

**Renders:** `manim/B12_ArtifactClasses.mp4`  
**Scene class:** `B12_ArtifactClasses`  
**Visual:** Three columns reveal left to right.  
Col 1 — `CONTRACT` (CRIMSON header): `beat_sheet.json` in PT Mono; `read by: agents + you`; `judgment: schema check → gate approval`.  
Col 2 — `LOGS` (SLATE header): `align.json · QC sheets · request cards`; `read by: agents when broken`; `judgment: none — diagnostic only`.  
Col 3 — `DELIVERABLE` (INK header): `the mp4`; `read by: you + audience`; `judgment: TASTE`.  
Footer under col 3 only, in small EB Garamond italic: `The log will never tell you if it's worth watching.` Footer arrives with the final narration phrase.

---

## B13 — INSTANCE | REMOTION · NikBearBrownTerminalAsk

**Renders:** `media/B13.mp4`  
**Pattern:** `NikBearBrownTerminalAsk`  
**Props:**
```json
{
  "command":     "$ who checks what in the agentic system?",
  "topic":       "AGENTIC SYSTEM",
  "segment":     "JUDGMENT RULE",
  "runningText": "applying judgment rule…",
  "output": [
    "DETERMINABLE  ← agents check these",
    "  ✓ script exited clean    ✓ schema validates",
    "  ✓ every beat filled      ✓ render matches deck",
    "JUDGEABLE     ← human ONLY — never delegates",
    "  ? opening interesting    ? joke lands",
    "  ? worth watching",
    "warning: trust an agent to check taste → AI slop (taste ≠ schema)"
  ]
}
```
**Visual intent:** The `warning:` line arrives last with "Trust an agent to check taste and you've rebuilt AI slop."

---

## B14 — PAYOFF | GRAPHIC · Manim: B14_TaxonomyPayoff

**Renders:** `manim/B14_TaxonomyPayoff.mp4`  
**Scene class:** `B14_TaxonomyPayoff`  
**Visual:** The B01 cascade redrawn at same layout. Then two annotation bands wipe in over the flow: a teal/INK band labeled `SPECIFIES — no gate` overlays fps=24 and voice_id steps; a CRIMSON band labeled `INFLUENCES — taste gate ▼` overlays persona/register steps, each with a gate icon (filled downward triangle) and a small human silhouette figure alongside. The mp4 node at the end receives a CRIMSON label: `DELIVERABLE — judged for taste`. The two bands wipe from left to right in sequence; gate icons pulse in last. `references_hook: true` — the B00 cascade puzzle is resolved.

---

## B15 — BOUNDARY | REMOTION · BrutalistCommentCTA

**Renders:** `media/B15.mp4`  
**Pattern:** `BrutalistCommentCTA`  
**Props:**
```json
{
  "filename": "thesis.ts",
  "code":     "// maximally informed, minimally autonomous\n//\n// the determinism boundary IS\n// the human-judgment boundary\n//\n// @NikBearBrown  ·  brutalist.art",
  "variant":  "B",
  "topic":    "AGENTIC SYSTEM TAXONOMY"
}
```
**Visual intent:** The thesis as a code comment — the register choice (code aesthetic for the closing thesis) earns its place because the whole video is about how code-level specifying inputs differ from prose-level influencing ones.

---

## B_LLM — LLM EXERCISE | CARD

**Renders:** `media/B_LLM.mp4` (Remotion NikBearBrownCodeBlock — displays prompt as a paste-ready block)  
**LLM prompt:** Apply the SPECIFIES/INFLUENCES × INPUTS/ARTIFACTS taxonomy to a real system you're building. Map each component; identify where human judgment gates should sit.  
**Dig deeper:** Where does the taxonomy break down when an artifact from one run becomes a specifying input for the next — does the distinction still hold?

---

## B_OUTRO — OUTRO | REMOTION · NikBearBrownOutro

**Renders:** `media/B_OUTRO.mp4`  
**Pattern:** `NikBearBrownOutro`  
**Props:**
```json
{
  "brand":   "Nik Bear Brown",
  "tagline": "Brutalist · Agentic · Educational AI",
  "handle":  "@NikBearBrown",
  "url":     "brutalist.art"
}
```

---

## Shot rhythm histogram

| Type | Count | Max consecutive |
|------|-------|----------------|
| GRAPHIC | 10 | 2 |
| REMOTION | 8 | 2 |
| CARD | 1 | 1 |

Zero flags. No request cards. No archive slots. No AI-generated media needed.
