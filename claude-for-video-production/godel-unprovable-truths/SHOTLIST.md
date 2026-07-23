# SHOTLIST — Godel: Unprovable Truths

*Unreal Reels — music · Nik Bear Brown · Tuzi Brown · Marley Brown · slate cut (vox-explainer pass 1)*

**Master audio:** `GodelUnprovabletruths-mastered.wav` · **220.667s** · 1280×720 @ 24fps · style: vox-explainer (editorial paper-collage / newsprint / isotype)

**Slots:** 40 beats — **14 filled** from the pantry, **26 slates** to build/source.

**How the slot contract works:** every beat on the timeline is a per-beat mp4 in `clips/`. To fill or swap a slot, drop a file in `media/` named after the beat (`media/B08.png` as a still/i2v seed, or `media/B08.mp4` to upgrade). Precedence at rebuild: `media/B08.mp4` > `media/B08.png` > slate placeholder. Re-run the assembler to recompile only changed slots. Timing is **EST** (word-weighted, pinned to the song's energy anchors at 6 / 40 / 196 / 217 s) — replace with forced alignment when ready; it is the master clock.

---

## Scene 0

### B00 · 0.0–6.0s (6.0s) · CARD × own · SLATE (to build)

**On-screen caption:** —

**Teaches:** Title card.

**Build prompt:** Vox editorial title card on newsprint ground (#F3EBDD), charcoal serif (#2F2A26): 'GODEL' large, 'UNPROVABLE TRUTHS' beneath, hairline underline; small credit line 'Nik Bear Brown · Tuzi Brown · Marley Brown'. One accent: dusty blue.
*Fill:* `media/B00.png` (placeholder / i2v seed) or `media/B00.mp4` (final).

---

### B01 · 6.0–10.875s (4.875s) · GRAPHIC × ai · SLATE (to build)
> Consider dis sentence ya / Dis yah statement is false

**On-screen caption:** Consider dis sentence — 'This statement is false'

**Teaches:** The Liar sentence is typed onto the page and boxed.

**Build prompt:** Manim: a single serif line 'This statement is false.' types on, then a thin ink box draws around it. Newsprint ground, charcoal type, no color.
**viz:** `{"kind": "text", "content": "This statement is false."}`
*Fill:* `media/B01.png` (placeholder / i2v seed) or `media/B01.mp4` (final).

---

### B02 · 10.875–12.5s (1.625s) · FOOTAGE × own · FILLED (pantry)
> So... it true

**On-screen caption:** So... it true?

**Teaches:** Holographic paradox loop (pantry).

**Filled from pantry:** `Floating_holographic_text_This_statement_is_false_looped_para_6178e362-8ef2-49f3-b2e0-4cc5057afd8c_0.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 1.625s.
*Swap:* replace `media/B02.mp4` to change this shot.

---

### B03 · 12.5–22.75s (10.25s) · GRAPHIC × ai · SLATE (to build)
> If a true, dat mean it false / But if a false, den it haffi be true / Yuh see it

**On-screen caption:** If true -> it's false. If false -> it's true.

**Teaches:** Two arrows chase each other: TRUE -> FALSE -> TRUE, a closed loop that never settles.

**Build prompt:** Manim: two labels TRUE and FALSE with curved arrows forming a loop between them; a dot ping-pongs and never rests. Charcoal + one dusty-blue accent.
**viz:** `{"kind": "loop", "nodes": ["TRUE", "FALSE"]}`
*Fill:* `media/B03.png` (placeholder / i2v seed) or `media/B03.mp4` (final).

---

### B04 · 22.75–30.833s (8.083s) · FOOTAGE × own · FILLED (pantry)
> Just by talkin 'bout itself / It mash up reason like it twis' back pon itself

**On-screen caption:** It talks about itself — reason twists back on itself

**Teaches:** Equations folding into recursion (pantry).

**Filled from pantry:** `Equations_folding_in_on_themselves_in_endless_recursion_a_mat_09adc18f-ba99-440f-a7ea-6c9bdb0efef4_0.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 8.083s.
*Swap:* replace `media/B04.mp4` to change this shot.

---

### B05 · 30.833–40.0s (9.167s) · GRAPHIC × ai · SLATE (to build)
> A real paradox, bredda / So if it nah true, and it nah false / Wha it really be

**On-screen caption:** A real paradox — not true, not false. So what is it?

**Teaches:** Label chip 'PARADOX'; the sentence sits with a '?' where its truth value should be.

**Build prompt:** Manim: accent block chip reading 'PARADOX' (white serif on dusty-blue), the boxed sentence below with a large '?' where TRUE/FALSE would be.
**viz:** `{"kind": "chip", "label": "PARADOX"}`
*Fill:* `media/B05.png` (placeholder / i2v seed) or `media/B05.mp4` (final).

---

## Scene 1

### B06 · 40.0–44.833s (4.833s) · DOCUMENT × archive · SLATE (to build)
> Mi know it might sound like some fool-fool brain game / But round di early 1900s

**On-screen caption:** Sounds like a brain game — but around the early 1900s...

**Teaches:** A century timeline; a pin drops on 'early 1900s'.

**Build prompt:** Manim/DOCUMENT: horizontal timeline 1900..2000 on newsprint, a marker pin lands near 1900-1910 with serif label 'early 1900s'.
**viz:** `{"kind": "timeline", "span": [1900, 2000], "pin": 1905}`
**Archive search:**
  - `Chronicling America 1900s mathematics` — [LOC](https://www.loc.gov/search/?q=Chronicling%20America%201900s%20mathematics&fo=json) · [Wikimedia](https://commons.wikimedia.org/w/index.php?search=Chronicling%20America%201900s%20mathematics) · [Internet Archive](https://archive.org/search?query=Chronicling%20America%201900s%20mathematics) · [Smithsonian](https://www.si.edu/search?edan_q=Chronicling%20America%201900s%20mathematics)
  - `LOC early 20th century mathematics` — [LOC](https://www.loc.gov/search/?q=LOC%20early%2020th%20century%20mathematics&fo=json) · [Wikimedia](https://commons.wikimedia.org/w/index.php?search=LOC%20early%2020th%20century%20mathematics) · [Internet Archive](https://archive.org/search?query=LOC%20early%2020th%20century%20mathematics) · [Smithsonian](https://www.si.edu/search?edan_q=LOC%20early%2020th%20century%20mathematics)
*Fill:* `media/B06.png` (placeholder / i2v seed) or `media/B06.mp4` (final).

---

### B07 · 44.833–49.042s (4.208s) · FOOTAGE × own · FILLED (pantry)
> One man name Kurt Gödel / Tek it serious—an' change di whole maths game

**On-screen caption:** One man — Kurt Gödel — took it seriously

**Teaches:** Gödel by candlelight (pantry); name plate 'KURT GÖDEL, 1906–1978' at assembly.

**Filled from pantry:** `Gdel_working_by_candlelight_in_a_mechanical_study_blackboard__b6aef71b-ff0c-4058-99a9-5c5c647cb773_0.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 4.208s.
*Swap:* replace `media/B07.mp4` to change this shot.

---

### B08 · 49.042–52.583s (3.542s) · GRAPHIC × ai · SLATE (to build)
> Him discovery / It show seh math have limits, yuh zee it

**On-screen caption:** His discovery: math has limits

**Teaches:** A bounded region labelled MATH; one star (a truth) sits OUTSIDE the boundary.

**Build prompt:** Manim: a rounded boundary labelled 'MATH (what we can prove)'; inside, small ticks; one star clearly outside the line, labelled 'true'. Terracotta accent on the star only.
**viz:** `{"kind": "boundary", "inside": "provable", "outside": "a truth"}`
*Fill:* `media/B08.png` (placeholder / i2v seed) or `media/B08.mp4` (final).

---

## Scene 2

### B09 · 52.583–58.375s (5.792s) · GRAPHIC × ai · SLATE (to build)
> A proof now, dat a just a solid argument / Fi show why one number statement haffi be true

**On-screen caption:** A proof = a solid chain of steps to a true statement

**Teaches:** Definition: PROOF = step -> step -> step => statement TRUE.

**Build prompt:** Manim: three stacked step boxes connected by down-arrows, terminating in a chip 'TRUE'. Serif labels, one accent.
**viz:** `{"kind": "chain", "steps": ["axiom", "step", "step"], "end": "TRUE"}`
*Fill:* `media/B09.png` (placeholder / i2v seed) or `media/B09.mp4` (final).

---

### B10 · 58.375–65.792s (7.417s) · GRAPHIC × ai · SLATE (to build)
> But fi build dem kinda argument / Yuh start wid some base—called axioms / Dem a di rule dem / Dat nuh need no more proof

**On-screen caption:** Every proof starts from axioms — base rules that need no proof

**Teaches:** Isotype row of 'axiom' blocks at the foundation; a small seal 'no proof needed'.

**Build prompt:** Manim: a foundation row of identical square blocks labelled AXIOM (isotype, one unit per mark); a serif caption 'assumed, not proved'.
**viz:** `{"kind": "isotype", "unit": "axiom", "count": 5}`
*Fill:* `media/B10.png` (placeholder / i2v seed) or `media/B10.mp4` (final).

---

### B11 · 65.792–71.25s (5.458s) · FOOTAGE × own · FILLED (pantry)
> Everything inna math / From di likkle one-two-three / To di biggest theory dem / All start from axiom dem

**On-screen caption:** From 1-2-3 to the biggest theorems — all from axioms

**Teaches:** Infinite staircase of axioms (pantry).

**Filled from pantry:** `An_infinite_staircase_of_axioms_leading_into_fog_unreachable__0fcc117a-848d-44cb-9565-3c7abda3d99d_0.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 5.458s.
*Swap:* replace `media/B11.mp4` to change this shot.

---

### B12 · 71.25–76.75s (5.5s) · GRAPHIC × ai · SLATE (to build)
> So if a statement bout numbers true / Yuh shoulda be able fi prove it / Using dem axioms

**On-screen caption:** If a statement about numbers is true, you should be able to prove it

**Teaches:** Pipeline: STATEMENT + AXIOMS -> PROOF -> TRUE. The dream of completeness.

**Build prompt:** Manim: 'statement about numbers' + 'axioms' feed an arrow into 'proof' into 'TRUE'. Clean flow, one accent.
**viz:** `{"kind": "pipeline", "in": ["statement", "axioms"], "out": "proof -> true"}`
*Fill:* `media/B12.png` (placeholder / i2v seed) or `media/B12.mp4` (final).

---

### B13 · 76.75–83.208s (6.458s) · DOCUMENT × archive · SLATE (to build)
> From Ancient Greece till now / Mathematician been using dat method / Fi prove or disprove everything / Clean and neat, no doubt

**On-screen caption:** From Ancient Greece onward — prove or disprove, clean and neat

**Teaches:** Euclid's Elements scan; a long arrow 'Ancient Greece -> now'.

**Build prompt:** DOCUMENT: a page of Euclid's Elements (archival scan), desaturated on newsprint, a highlighter bar under a proposition; arrow spanning 'Ancient Greece -> now'.
**Archive search:**
  - `Internet Archive Euclid Elements` — [LOC](https://www.loc.gov/search/?q=Internet%20Archive%20Euclid%20Elements&fo=json) · [Wikimedia](https://commons.wikimedia.org/w/index.php?search=Internet%20Archive%20Euclid%20Elements) · [Internet Archive](https://archive.org/search?query=Internet%20Archive%20Euclid%20Elements) · [Smithsonian](https://www.si.edu/search?edan_q=Internet%20Archive%20Euclid%20Elements)
  - `LOC Euclid Elements scan` — [LOC](https://www.loc.gov/search/?q=LOC%20Euclid%20Elements%20scan&fo=json) · [Wikimedia](https://commons.wikimedia.org/w/index.php?search=LOC%20Euclid%20Elements%20scan) · [Internet Archive](https://archive.org/search?query=LOC%20Euclid%20Elements%20scan) · [Smithsonian](https://www.si.edu/search?edan_q=LOC%20Euclid%20Elements%20scan)
  - `Wikimedia Euclid Elements page` — [LOC](https://www.loc.gov/search/?q=Wikimedia%20Euclid%20Elements%20page&fo=json) · [Wikimedia](https://commons.wikimedia.org/w/index.php?search=Wikimedia%20Euclid%20Elements%20page) · [Internet Archive](https://archive.org/search?query=Wikimedia%20Euclid%20Elements%20page) · [Smithsonian](https://www.si.edu/search?edan_q=Wikimedia%20Euclid%20Elements%20page)
*Fill:* `media/B13.png` (placeholder / i2v seed) or `media/B13.mp4` (final).

---

## Scene 3

### B14 · 83.208–89.958s (6.75s) · FOOTAGE × own · FILLED (pantry)
> But when Gödel step inna di scene / Di math world did a wobble / Paradoxes start show up / An people start fret

**On-screen caption:** Gödel steps in — the math world wobbles

**Teaches:** Paradox explodes into fractal shards (pantry).

**Filled from pantry:** `Boom_effect_mathematical_paradox_explodes_into_fractals_shard_6a85fcbf-4bf5-440b-a230-42af98d12558_0.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 6.75s.
*Swap:* replace `media/B14.mp4` to change this shot.

---

### B15 · 89.958–93.833s (3.875s) · GRAPHIC × ai · SLATE (to build)
> Big name mathematicians / Did want fi prove seh math cyaan go wrong

**On-screen caption:** Hilbert's dream: prove math can never contradict itself

**Teaches:** Hilbert's program: a seal reading COMPLETE + CONSISTENT stamped over 'all of mathematics'.

**Build prompt:** Manim: a wax-seal / stamp motif stamping 'COMPLETE + CONSISTENT' onto a block 'ALL OF MATHEMATICS'. Name chip 'Hilbert, 1900'.
**viz:** `{"kind": "seal", "text": "COMPLETE + CONSISTENT"}`
**Archive search:**
  - `Wikimedia David Hilbert portrait` — [LOC](https://www.loc.gov/search/?q=Wikimedia%20David%20Hilbert%20portrait&fo=json) · [Wikimedia](https://commons.wikimedia.org/w/index.php?search=Wikimedia%20David%20Hilbert%20portrait) · [Internet Archive](https://archive.org/search?query=Wikimedia%20David%20Hilbert%20portrait) · [Smithsonian](https://www.si.edu/search?edan_q=Wikimedia%20David%20Hilbert%20portrait)
*Fill:* `media/B15.png` (placeholder / i2v seed) or `media/B15.mp4` (final).

---

### B16 · 93.833–100.583s (6.75s) · FOOTAGE × own · FILLED (pantry)
> But Gödel / Him never too sure / Matter of fact—him doubt if math / Even di right tool fi ask di big question

**On-screen caption:** But Gödel doubted math was even the right tool

**Teaches:** Zoom on Gödel-bot metal face, gears turning (pantry).

**Filled from pantry:** `Zoom_on_Gdels_metal_face_gears_rotating_slowly_inside_his_hea_0d793849-767a-473d-816c-ad5252423dd3_0.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 6.75s.
*Swap:* replace `media/B16.mp4` to change this shot.

---

## Scene 4

### B17 · 100.583–105.417s (4.833s) · GRAPHIC × ai · SLATE (to build)
> Words / Dem easy fi tangle up pon demself / But numbers / Dem usually straight—true or false

**On-screen caption:** Words tangle. Numbers stay straight — true or false.

**Teaches:** Left: a knotted word 'sentence'. Right: a clean number with TRUE/FALSE tags.

**Build prompt:** Manim split: left a tangled scribble labelled 'words'; right a crisp integer labelled 'numbers' with two tags TRUE / FALSE. Terracotta vs dusty-blue.
**viz:** `{"kind": "contrast", "left": "words tangle", "right": "numbers: true/false"}`
*Fill:* `media/B17.png` (placeholder / i2v seed) or `media/B17.mp4` (final).

---

### B18 · 105.417–108.958s (3.542s) · FOOTAGE × own · FILLED (pantry)
> Still... Gödel get one idea / Him turn equations into numbers—code dem

**On-screen caption:** Gödel's idea: turn equations into numbers — code them

**Teaches:** Typewriter typing Gödel-numbering code (pantry).

**Filled from pantry:** `Mechanical_typewriter_typing_out_Gdel_numbering_code_numbers__0757f8cf-b3f1-435e-99b6-bfc41feb0de6_0.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 3.542s.
*Swap:* replace `media/B18.mp4` to change this shot.

---

### B19 · 108.958–114.417s (5.458s) · GRAPHIC × ai · SLATE (to build)
> So now, yuh can write one big statement / An represent it with just one number / Crazy, right

**On-screen caption:** A whole statement becomes a single number

**Teaches:** Gödel numbering: symbols -> primes -> one big number. Show a tiny worked encoding.

**Build prompt:** Manim: a short formula's symbols each map to a small number, combined (2^a·3^b·5^c...) into one large integer, which is boxed and labelled 'the statement, as a number'.
**viz:** `{"kind": "encode", "example": "symbol -> prime power -> product"}`
*Fill:* `media/B19.png` (placeholder / i2v seed) or `media/B19.mp4` (final).

---

## Scene 5

### B20 · 114.417–117.958s (3.542s) · FOOTAGE × own · FILLED (pantry)
> By doing dat, math start chat 'bout itself / Math get self-aware

**On-screen caption:** Now math can talk about itself — math becomes self-aware

**Teaches:** Equations folding recursion, second instance (pantry).

**Filled from pantry:** `Equations_folding_in_on_themselves_in_endless_recursion_a_mat_09adc18f-ba99-440f-a7ea-6c9bdb0efef4_1.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 3.542s.
*Swap:* replace `media/B20.mp4` to change this shot.

---

### B21 · 117.958–121.5s (3.542s) · GRAPHIC × ai · SLATE (to build)
> And him write / Dis statement cyaan be proved / As one equation

**On-screen caption:** He writes G: 'This statement cannot be proved' — as a number

**Teaches:** The sentence G appears in words, then collapses into its Gödel number G.

**Build prompt:** Manim: 'G:  This statement cannot be proved.' typed, then the words dissolve into a single boxed integer labelled G. One accent on G.
**viz:** `{"kind": "text", "content": "G: This statement cannot be proved."}`
*Fill:* `media/B21.png` (placeholder / i2v seed) or `media/B21.mp4` (final).

---

### B22 · 121.5–129.25s (7.75s) · GRAPHIC × ai · SLATE (to build)
> Now, dis different from di sentence we start wid / Cah math nuh play / It must be true or false / So which one it be

**On-screen caption:** Unlike the Liar, math must be true or false. So which is G?

**Teaches:** A fork: G branches into two boxes, TRUE and FALSE — which one?

**Build prompt:** Manim: node 'G' forks into two boxes TRUE and FALSE with a hand-drawn '?' ring around the fork.
**viz:** `{"kind": "fork", "node": "G", "branches": ["TRUE", "FALSE"]}`
*Fill:* `media/B22.png` (placeholder / i2v seed) or `media/B22.mp4` (final).

---

## Scene 6

### B23 · 129.25–139.583s (10.333s) · GRAPHIC × ai · SLATE (to build)
> If it false—dat mean it can be proved / But if it can be proved—den it true / But wait… if it true / An still cyaan prove it / Dat mean it true, but unprovable

**On-screen caption:** If false -> provable -> true (contradiction). So G is TRUE but UNPROVABLE.

**Teaches:** The core deduction as a decision tree ending on a chip 'TRUE but UNPROVABLE'.

**Build prompt:** Manim decision tree: 'G false' -> 'G provable' -> 'G true' flagged CONTRADICTION (terracotta); the surviving branch resolves to a chip 'TRUE but UNPROVABLE' (dusty-blue). This is the payoff frame.
**viz:** `{"kind": "decision", "result": "TRUE but UNPROVABLE"}`
*Fill:* `media/B23.png` (placeholder / i2v seed) or `media/B23.mp4` (final).

---

### B24 · 139.583–141.208s (1.625s) · FOOTAGE × own · FILLED (pantry)
> Madness / But genius same way

**On-screen caption:** Madness — but genius, same way

**Teaches:** Gödel-bot fading into infinity (pantry).

**Filled from pantry:** `Black-and-white_stylized_portrait_of_Gdelbot_fading_into_infi_51f02b07-3ac3-4975-b614-40ca535c1f92_0.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 1.625s.
*Swap:* replace `media/B24.mp4` to change this shot.

---

### B25 · 141.208–147.333s (6.125s) · GRAPHIC × ai · SLATE (to build)
> Dis shake up di whole foundation / Math cyaan hold every truth / Some truth always ago hide / Just outta reach

**On-screen caption:** Incompleteness: math can't hold every truth

**Teaches:** The MATH boundary from B08 returns, now cracked; several truths sit outside, out of reach.

**Build prompt:** Manim: the boundary 'MATH' develops a hairline crack; three stars labelled 'true' float outside it, dimmed, tagged 'unreachable'.
**viz:** `{"kind": "boundary_cracked"}`
*Fill:* `media/B25.png` (placeholder / i2v seed) or `media/B25.mp4` (final).

---

## Scene 7

### B26 · 147.333–153.458s (6.125s) · GRAPHIC × ai · SLATE (to build)
> Even if yuh try patch di gap / By adding more axioms / Guess wha / More unprovable truth ago pop up

**On-screen caption:** Patch the gap with a new axiom -> a new unprovable truth appears

**Teaches:** Add an axiom block to the foundation; immediately a new star pops OUTSIDE. Repeat gesture implied.

**Build prompt:** Manim: an AXIOM block slides into the foundation; the boundary grows; but a fresh 'true' star blinks into existence just outside the new line.
**viz:** `{"kind": "patch_loop"}`
*Fill:* `media/B26.png` (placeholder / i2v seed) or `media/B26.mp4` (final).

---

### B27 · 153.458–160.208s (6.75s) · FOOTAGE × own · FILLED (pantry)
> No matter how much yuh add / Unprovable truth still deh deh / It's Gödel pon top a Gödel / All di way down

**On-screen caption:** Gödel on top of Gödel — all the way down

**Teaches:** Digital vines of logic branching endlessly (pantry).

**Filled from pantry:** `Digital_vines_of_logic_branching_out_endlessly_roots_made_of__13c49d06-d50d-40bd-8632-d667009c9cde_0.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 6.75s.
*Swap:* replace `media/B27.mp4` to change this shot.

---

### B28 · 160.208–165.042s (4.833s) · GRAPHIC × ai · SLATE (to build)
> It mash up plenty dreams / Of one perfect math world / Where every question get answer

**On-screen caption:** It broke the dream of a perfect math where every question is answered

**Teaches:** Hilbert's COMPLETE+CONSISTENT seal from B15 returns, now cracked / stamped VOID.

**Build prompt:** Manim: the 'COMPLETE + CONSISTENT' seal from earlier cracks down the middle; a faint stamp 'incomplete' overlays it.
**viz:** `{"kind": "seal_broken"}`
*Fill:* `media/B28.png` (placeholder / i2v seed) or `media/B28.mp4` (final).

---

### B29 · 165.042–170.833s (5.792s) · DOCUMENT × ai · SLATE (to build)
> Some mathematicians accept it / Some fight it / Some even try ignore di hole / Wha open up under dem

**On-screen caption:** Reactions: accept it · fight it · ignore the hole

**Teaches:** Three labelled reaction cards: ACCEPT / FIGHT / IGNORE, one with a hole beneath it.

**Build prompt:** Manim: three serif cards in a row — ACCEPT, FIGHT, IGNORE — the last with a dark circular 'hole' opening under its feet.
**viz:** `{"kind": "cards", "items": ["ACCEPT", "FIGHT", "IGNORE"]}`
*Fill:* `media/B29.png` (placeholder / i2v seed) or `media/B29.mp4` (final).

---

### B30 · 170.833–177.292s (6.458s) · GRAPHIC × ai · SLATE (to build)
> But truth / More and more problems / Start show demself unprovable / People start worry / If dem whole career based pon smoke

**On-screen caption:** More and more problems turn out unprovable

**Teaches:** A tally that keeps ticking up: 'proven unprovable' count climbs (isotype squares filling).

**Build prompt:** Manim: an isotype tally labelled 'shown unprovable' fills square by square, count climbing; a couple of name-stubs (Halting problem, Continuum hypothesis) fade in as examples.
**viz:** `{"kind": "isotype_count", "label": "shown unprovable"}`
*Fill:* `media/B30.png` (placeholder / i2v seed) or `media/B30.mp4` (final).

---

## Scene 8

### B31 · 177.292–181.167s (3.875s) · GRAPHIC × ai · SLATE (to build)
> But still, Gödel's work / Never just close doors / It open new one

**On-screen caption:** Gödel's work didn't just close doors — it opened new ones

**Teaches:** One door labelled 'certainty' closes; an adjacent door labelled 'new math' opens with light.

**Build prompt:** Manim: two serif-labelled doors; the left ('certainty') swings shut, the right ('new mathematics') opens, a golden highlighter bar of light across the threshold.
**viz:** `{"kind": "doors"}`
*Fill:* `media/B31.png` (placeholder / i2v seed) or `media/B31.mp4` (final).

---

### B32 · 181.167–188.583s (7.417s) · FOOTAGE × own · FILLED (pantry)
> Unprovable truths / Light di path fi early computers / An even today / Some genius still out deh / Try spot di truths / Yuh cyaan prove

**On-screen caption:** Unprovable truths lit the path to the first computers

**Teaches:** Digital vines / logic -> machines (pantry); name-stub 'Turing, 1936' at assembly.

**Filled from pantry:** `Digital_vines_of_logic_branching_out_endlessly_roots_made_of__13c49d06-d50d-40bd-8632-d667009c9cde_1.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 7.417s.
*Swap:* replace `media/B32.mp4` to change this shot.

---

### B33 · 188.583–196.0s (7.417s) · GRAPHIC × ai · SLATE (to build)
> So yeah, some certainty get lost / But thanks to Gödel / We find beauty inna di unknown / Right inna di heart / Of truth itself

**On-screen caption:** Some certainty lost — but beauty found in the unknown

**Teaches:** The 'unreachable' stars from B25 re-render as quiet points of light — reframed as beauty, not loss.

**Build prompt:** Manim: the outside 'true / unreachable' stars brighten gently into a small constellation labelled 'the unknown'; the crack stays but reads calm, not alarming.
**viz:** `{"kind": "constellation"}`
*Fill:* `media/B33.png` (placeholder / i2v seed) or `media/B33.mp4` (final).

---

## Scene 9

### B34 · 196.0–199.625s (3.625s) · FOOTAGE × own · FILLED (pantry)
> Him build a code fi numbers talk 'bout numbers / Fi math start reason wid itself

**On-screen caption:** He built a code for numbers to talk about numbers

**Teaches:** Typewriter code reprise (pantry).

**Filled from pantry:** `Mechanical_typewriter_typing_out_Gdel_numbering_code_numbers__0757f8cf-b3f1-435e-99b6-bfc41feb0de6_1.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 3.625s.
*Swap:* replace `media/B34.mp4` to change this shot.

---

### B35 · 199.625–203.0s (3.375s) · FOOTAGE × own · FILLED (pantry)
> An' den... boom / Him write a ting weh seh / This statement cyaan be proved

**On-screen caption:** And then — boom — 'This statement cannot be proved'

**Teaches:** Boom -> fractals reprise (pantry).

**Filled from pantry:** `Boom_effect_mathematical_paradox_explodes_into_fractals_shard_6a85fcbf-4bf5-440b-a230-42af98d12558_1.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 3.375s.
*Swap:* replace `media/B35.mp4` to change this shot.

---

### B36 · 203.0–208.292s (5.292s) · GRAPHIC × ai · SLATE (to build)
> If it false—den it get proved / But if it get proved—den it cyaan false / So it haffi be true / But still... unprovable

**On-screen caption:** False -> proved -> true. So: TRUE but unprovable.

**Teaches:** The B23 payoff chip restated fast: 'TRUE but UNPROVABLE'.

**Build prompt:** Manim: quick restatement of the decision, landing hard on the chip 'TRUE but UNPROVABLE'.
**viz:** `{"kind": "decision", "result": "TRUE but UNPROVABLE"}`
*Fill:* `media/B36.png` (placeholder / i2v seed) or `media/B36.mp4` (final).

---

### B37 · 208.292–214.583s (6.292s) · GRAPHIC × ai · SLATE (to build)
> Dat mash up di whole idea seh math can hold all truth / Cause no matter how much yuh add / New truths always a hide outta reach

**On-screen caption:** No matter how much you add, new truths always hide out of reach

**Teaches:** The patch-loop from B26, sped up: add axiom -> new star -> add -> new star, receding.

**Build prompt:** Manim: the add-axiom / new-star gesture repeats and recedes into the distance (Godel all the way down).
**viz:** `{"kind": "patch_loop_recede"}`
*Fill:* `media/B37.png` (placeholder / i2v seed) or `media/B37.mp4` (final).

---

### B38 · 214.583–217.0s (2.417s) · FOOTAGE × own · FILLED (pantry)
> It deep / It paradox / It Gödel / All di way down

**On-screen caption:** It's deep. It's paradox. It's Gödel — all the way down.

**Teaches:** Gödel-bot fading into infinity, final (pantry).

**Filled from pantry:** `Black-and-white_stylized_portrait_of_Gdelbot_fading_into_infi_51f02b07-3ac3-4975-b614-40ca535c1f92_1.mp4` → treated (desaturate ~80%, contrast 1.12, cream wash) and conformed to 2.417s.
*Swap:* replace `media/B38.mp4` to change this shot.

---

### B39 · 217.0–220.667s (3.667s) · CARD × own · SLATE (to build)

**On-screen caption:** —

**Teaches:** Endcard + credits.

**Build prompt:** Vox endcard on newsprint: 'KURT GODEL · 1931 · On Formally Undecidable Propositions'; small line 'Incompleteness'; credits 'Nik Bear Brown · Tuzi Brown · Marley Brown'.
*Fill:* `media/B39.png` (placeholder / i2v seed) or `media/B39.mp4` (final).

---
