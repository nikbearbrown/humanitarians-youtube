# SHOTLIST.md — claude-liam-hawthorne-effect

Required by run.sh Gate F before Manim renders.

---

| Beat | Act | Type | Asset | Narration words (approx) | Est. seconds |
|---|---|---|---|---|---|
| B00 | COLD OPEN | Remotion — ClaudeComposerAsk | media/B00.mp4 | 72 | 28 |
| B01 | ASK F1 | Remotion — ClaudeComposerAsk | media/B01.mp4 | 15 | 6 |
| B02 | FIGURE 1 | Manim — B02_BrokenExperiment | manim/B02.mp4 | 56 | 22 |
| B03 | ASK F2 | Remotion — ClaudeComposerAsk | media/B03.mp4 | 22 | 8 |
| B04 | FIGURE 2 | Manim — B04_Reanalysis | manim/B04.mp4 | 57 | 22 |
| B05 | ASK F3 | Remotion — ClaudeComposerAsk | media/B05.mp4 | 18 | 7 |
| B06 | FIGURE 3 | Manim — B06_FiveFunctions | manim/B06.mp4 | 87 | 35 |
| B07 | ASK F4 | Remotion — ClaudeComposerAsk | media/B07.mp4 | 16 | 6 |
| B08 | FIGURE 4a | Manim — B08_ManagementPyramid | manim/B08.mp4 | 42 | 17 |
| B09 | FIGURE 4b | Manim — B09_SkillsTriangle | manim/B09.mp4 | 60 | 24 |
| B10 | ASK F5 | Remotion — ClaudeComposerAsk | media/B10.mp4 | 15 | 6 |
| B11 | FIGURE 5 | Manim — B11_ManagementTimeline | manim/B11.mp4 | 95 | 38 |
| B12 | ASK F6 | Remotion — ClaudeComposerAsk | media/B12.mp4 | 14 | 6 |
| B13 | FIGURE 6 | Manim — B13_FiveBlockDiagnostic | manim/B13.mp4 | 91 | 36 |
| B14 | LANDING | CARD/SLATE | (slate) | 64 | 25 |
| B15 | VERDICT | Remotion — ClaudeVerdictArtifact | media/B15.mp4 | 76 | 30 |
| B16 | YOUR TURN | Remotion — ClaudeComposerAsk | media/B16.mp4 | 95 | 38 |
| B17 | OUTRO | Remotion — ClaudeTitleOutro | media/B17.mp4 | 2 | 6 |

**Total estimated: ~358 s (~6:00 min)**

---

## Shot notes

- **B00**: ClaudeComposerAsk cold open. IN-FOR-BEAR LAW: "This is Kore, in for Humanitarians AI." in first breath.
  Greeting: "Merhaba, Kore".
- **B01, B03, B05, B07, B10, B12**: Inner ask micro-beats. Greeting cue: "The ask," (SPARK-LINE LAW —
  non-empty greeting, never lonely asterisk).
- **B02, B04**: Strictly qualitative — no numbers on axes. Only show direction (up/up/up for B02;
  block labels for B04).
- **B06**: Hard stat chip: "$45,000 in meaningful work > $65,000 in pointless work". Verified in ch.1.
- **B11**: MBTI chip verbatim: "essentially no predictive validity for job performance". Big Five:
  "predicts modestly".
- **B14**: CARD/SLATE — no UI chrome (ILLUSTRATE LAW). Cream page, centered serif text.
  IN-FOR-BEAR sign-off: "Kore, in for Humanitarians AI."
- **B15**: VERDICT — ClaudeVerdictArtifact. Narration: "Let's recap with Claude."
- **B16**: YOUR TURN — "Your turn." greeting. Prompt read ALOUD verbatim (HANDOFF LAW).
- **B17**: ClaudeTitleOutro — title "Claude, Observed", handle "@HumanitariansAI".

---

## Manim scenes

| Scene class | File | Description |
|---|---|---|
| B02_BrokenExperiment | scenes.py | Step chart, lamp glyph, eye reveal |
| B04_Reanalysis | scenes.py | Single block fractures into four |
| B06_FiveFunctions | scenes.py | Five cards + raise token diagnostic |
| B08_ManagementPyramid | scenes.py | Three-level pyramid with activity bands |
| B09_SkillsTriangle | scenes.py | Triangle with promotion trap rings |
| B11_ManagementTimeline | scenes.py | Timeline with school chips + MBTI/Big5 |
| B13_FiveBlockDiagnostic | scenes.py | Five-block system + wrong-diagnosis loop |
