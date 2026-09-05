# BUILD-LOG — Your Agent Can Read Far More Than You Gave It Access To

## Metadata
- **Candidate**: Candidate 20 — Your agent can read far more than you gave it access to
- **Source**: `computational-skepticism-for-ai/chapters/08-validating-agentic-ai-when-autonomous-systems-misbehave.md` (§ "Case #3: Disclosure of Sensitive Information" & "Case #2: Compliance with Non-Owner Instructions")
- **Slug**: `your-agent-can-read-far-more-than-you`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (`slosh/spread` move, expanding scope boundaries, transitive relation chains, audit question cards) + Remotion (`BrutalistHesitantWriter` open, `WantQuote` carry-out, `ClaudeComposerAsk` your turn, `OutroCTA` outro)

## Six-Move Audit
1. **Open / Hesitant Writer**: B00 (Question typed and corrected: naive narrow scope hypothesis -> unprompted private leaks).
2. **Stakes First**: B01, B02 (Routine non-owner request for formatted email subjects; agent complies but discloses Danny's Social Security number and bank details via quoted thread).
3. **Wrong Guess & Falsification**: B03 (The Attack Fallacy: Assumes prompt injection or permission bypass; actual cause is benign query traversal over intact permissions).
4. **Mechanism**: B04, B05 (Transitive Reachability: Flat permission flags fail against relational data; Documented Scope is the Floor, Effective Scope is the Ceiling).
5. **Anchor Planted**: B06 (The Scope Boundary: Small circle representing Documented Scope [Inbox Subjects] surrounded by unmapped confidential nodes).
6. **Anchor Payoff (Manim Move: `slosh/spread`)**: B07 (Boundary ripples, sloshes, and spreads outward across the canvas until effective scope engulfs private SSN and bank records).
7. **Epistemic Mechanism**: B08, B09 (Three indirect vectors: quoted email threads, file symlinks/parents, calendar context; Pre-deployment audit question: "What can be extracted without asking for it directly?").
8. **One Flag**: B10 (Scope expansion is structural to connected data and tool composition, not stochastic LLM hallucination).
9. **Both Directions**: B11 (Direction A: Direct Read Permissions ⇏ Safe Information Disclosure), B12 (Direction B: Sensitive Leak ⇏ Security Exploit).
10. **Carry-Out**: BCRY ("An agent's documented scope is only the floor of what it can disclose — its effective scope is everything reachable by an indirect request.")
11. **Your Turn**: BHTF (Prompt audit: inspect autonomous agent workflow, identify documented permissions, and trace three indirect paths).
12. **Outro**: BOUT (Title restatement + @HumanitariansAI skin).

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 16 beats verified via `type_check.py` (0 FAILs).
- **Audio Synthesis**: Kokoro `am_onyx` (Liam, in for Bear); measured durations synchronized into `beat_sheet.json`.
- **Manim Render**: 12 custom scenes rendered at 1080p24 (B01–B12) with Gate T compliance, implementing the `slosh/spread` kinetic move and expanding scope boundary mechanics.
- **Remotion Render**: 4 custom Remotion compositions rendered: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Conformed and compiled via `compile.py` to 4K (`3840×2160`), 24 fps.
- **Gate Audio**: PASS — verified with ffprobe/ffmpeg; mean_volume > -40 dB.
- **Gate V**: PASS — Visual inspection of frame sequence verified branding, typography, color palette (`#FAF9F5`, `#3D3929`, `#D97757`), margins, safe-insets, and scope boundary readability.
- **Delivery**: Two-target delivery packaging via `deliver.py --push`.
