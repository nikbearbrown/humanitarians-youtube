# PROMPTS.md — claude-liam-hawthorne-effect

Required by run.sh Gate F before Manim renders.

Records the prompt behind every AI-generated asset in this reel.

---

## ClaudeComposerAsk beats (Remotion renders)

### B00 — Cold Open
```
In 1924, researchers at the Hawthorne Works raised the lights and productivity went up.
Then they dimmed the lights — and productivity went up again. How is that possible?
What was the actual independent variable, and what did this broken experiment actually
discover about how work and organizations function?
```
*Output lines: "The variable was attention, not light." / "Workers knew someone was watching." / "A factory is a social system."*

### B01 — Ask for Figure 1
```
Draw a step chart of the Hawthorne relay experiment. X-axis: three interventions labeled
Brighter, Dimmer, Restored. Y-axis: output (qualitative — no invented numbers). The output
line steps UP at every intervention. Above the x-axis, a small lamp glyph that brightens,
dims, then resets. On the third step — unchanged light, output still rising — add a
terracotta callout: 'That is not a finding.' Then fade in an eye symbol (the hidden observer)
behind the lamp.
```

### B03 — Ask for Figure 2
```
Draw the reanalysis of the Hawthorne data. Show Mayo's original single 'OBSERVATION' block
fracturing into four labeled factors: worker selection, supervision changes, wage incentives,
and observation — with the observation piece visibly smaller than the others. No invented
percentages. Caption: 'Real. Smaller than the story. Still the right lesson.'
```

### B05 — Ask for Figure 3
```
Draw five cards revealing in sequence: Economic, Social, Status, Identity, Actualization —
each with a one-line description. Between cards, show paraphrased Terkel vignettes: a
steelworker pointing to a house he built; a sanitation driver whose wife was proud; a
receptionist dismissed at a party. Add a stat chip: $45,000 in meaningful work beats
$65,000 in pointless work. Then animate a raise token dropped onto each card — it only
repairs Economic. Terracotta on the failed repairs.
```

### B07 — Ask for Figure 4
```
Draw the management pyramid: executive at top, middle in the middle, first-line at the
bottom. Each level shows qualitative proportions of how time splits across planning,
organizing, directing, controlling — executives mostly plan, first-line mostly directs.
Then beside it, draw the skills triangle: Technical, Human, Conceptual — showing how
technical skills shrink and conceptual skills grow as you move from first-line to
executive, while human skills stay constant. Mark the promotion trap at both transition
points with terracotta annotation rings.
```

### B10 — Ask for Figure 5
```
Draw a left-to-right timeline from 1890s to present: Scientific Management, Human
Relations, Systems Thinking (1960s), Contingency, Evidence-Based Management. Each school
gets two chips: its genuine contribution and its key limitation. Mark Hawthorne 1924-1932
as the terracotta pivot between Scientific Management and Human Relations. At the end,
side-by-side chips for MBTI ('no predictive validity for job performance') vs Big Five
('predicts modestly').
```

### B12 — Ask for Figure 6
```
Draw five interlocking blocks as a connected system: Individuals & Groups, Tasks &
Technology, Organization Design, Processes, Management (the connective tissue). Show one
symptom card 'output down, not responding to feedback' branching into five hypothesis
chips — one per block. Animate the wrong-diagnosis path: Block 1 assumed → escalation →
termination → same symptom card reappears on the next hire. Terracotta on the loop.
Final overlay: Hawthorne mapped onto the blocks — researchers testing Block 2, workers
responding to Block 4.
```

### B15 — Verdict
*No user-visible prompt: ClaudeVerdictArtifact auto-renders from props.*

### B16 — Your Turn
```
Someone on my team has disengaged — output down, not responding to feedback. Before I
assume it's them, walk me through the five-block diagnostic: give me one hypothesis and
one testable question for the person, the task, the org design, the processes, and my
own management.
```
*(Read verbatim in narration per HANDOFF LAW.)*

### B17 — Outro
*No user-visible prompt: ClaudeTitleOutro auto-renders from props.*

---

## Manim scenes (no external AI generation — pure code)

All seven Manim scenes in `scenes.py` are hand-coded animated graphics.
No generative image or video tools were used. Palette: claude token set.
Figures 1 and 2 carry no invented numbers (qualitative only, by design).

---

*Recorded: 2026-07-17*
