# PEDAGOGY.md — chain-of-trust (Video 2)

**GATE P VERDICT: PASS** — ready for audio generation.

## Teaching arc ✓

- **B00 (Cold open — welcome + self-intro):** Standard Brutalist welcome screen (Claude composer UI) paired with spoken self-intro — who's talking, what series, what today's video is about
- **B01 (Cold open — continuation):** The tagline recap + today's reframe question (if we can't prove truth, what CAN we prove?)
- **B02 (Execution tracing):** The new tool — a security camera metaphor for what LangFuse actually does (records behavior, not judgment)
- **B03 (Chain of trust):** Four-link chain, three solid (proved), one broken (unresolved)
- **B04 (Cautions):** Three ways a trace/camera can fool you — correlation vs causation, length ≠ truth, access control
- **B05 (Honest ceiling):** The reframe — proof of what ran, not proof it was right
- **B06–B07 (Three ways forward):** Ablation testing (Jenga), interpretability (locked box), calibration/grading (weather forecast)
- **B08 (What's holding us back):** Three blockers — frontier models are closed, calibration takes time, building a shiny fake is cheaper
- **B09 (Where this project ends):** Honest scorecard — what's real (structure, visibility), what's open (reasoning genuineness)
- **B10 (Outro):** Tagline completion — structure enforceable, behavior observable, truth still open

## Comprehension anchors ✓

| Beat | Anchor | Phrase | Why it lands |
|------|--------|--------|--------------|
| B00 | Self-intro | "Hi — I'm Divij Pawar... part two of the Accountability Mesh series" | Orients a first-time viewer before the callback in B01 assumes context |
| B01 | Tagline recap | "if we can't prove truth yet — what CAN we actually prove?" | Opens with a real question, not a lecture |
| B02 | Metaphor | "security camera" | Doesn't know if you lied, just knows you were there |
| B03 | Visual | Broken chain link | Shows what's missing, not just what exists |
| B04 | Gag | Rooster crows before sunrise | Correlation ≠ causation without effort |
| B05 | Boundary | "That's just where the line actually is" | Moves from problem to acceptance |
| B06–B07 | Tools | Jenga / lock / forecast | Visual metaphors, not jargon |
| B08 | Irony | "ships Friday" vs "6 months" | Dry humor lands the hard truth |
| B09 | Honesty | Yellow question mark, not red X | Uncertainty is OK; dishonesty isn't |
| B10 | Completion | "behavior observable" (new) | Closes the loop opened in Video 1 |

## Factual grounding ✓

All narration traces to `../context/video_script_2.md`, plus a new self-intro beat (B00) added per production feedback — a standard Brutalist welcome/intro pattern, no new factual claims. LangFuse execution tracing is the only new system detail (B02); it's explained via metaphor ("security camera") not jargon.

## Tone check ✓

Matches Video 1's register (plain-language, high school reading level, visuals-first). B08 has dry humor per the script. B09 stays calm/uncertain, not triumphant.

## Cross-video continuity ✓

- B00 is the standard welcome/self-intro bookend (mirrors Video 1's B00 `ClaudeComposerAsk` pattern) — establishes presenter and topic for viewers arriving fresh
- B01 opens with exact tagline from Video 1's B09, immediately after the welcome screen
- B05 mirrors Video 1's B06 ("proof of what ran, not proof it was right") — same pacing, same idea
- B06–B07 set up three approaches (ablation, interpretability, calibration) not covered in Video 1
- B10 outro reuses Video 1's title + adds a second line to the tagline (both taglines visible together)

## Scene placeholder check ✓

All `scene_class` names are present, descriptive, and renumbered to match their new beat IDs:
- B00 (Remotion `ClaudeComposerAsk`) — welcome screen + self-intro
- B01_ChainOpen — Video 1 B09 card cracks open
- B02_SecurityCamera — split screen (foggy vs. sharp log)
- B03_ChainOfTrust — four links, last one broken
- B04_ThreeWaysFooled — three vignettes (rooster, timeline loops, access control)
- B05_HonestCeiling — two-line text card, slow zoom (mirrors Video 1 B06 pattern)
- B06_ToolboxPartOne — toolbox opens, two tools out, one slot empty
- B07_ToolboxPartTwo — picks up exact frame from B06, tool 3 slides in, closes
- B08_WhatsHoldingUsBack — three quick vignettes (locked box, calendar, dashboard choice)
- B09_Scorecard — two-column table (PROVEN / STILL OPEN) draws in
- B10 (Remotion `ClaudeTitleOutro`) — reuses Video 1 title, adds subline

## Audio gate sign-off

✓ All narration is final, grammar-checked, timed to visuals. Ready to generate Kokoro `am_onyx` audio for all 11 beats (10 carried over unchanged + 1 new welcome beat).
