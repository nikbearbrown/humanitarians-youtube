# PEDAGOGY — medhavy-ch1-classical-sims

## What the learner already knows
Advanced undergraduate or master's student in physics or a related quantitative field.
Has seen classical mechanics, electromagnetism, and basic thermodynamics. Familiar with
Python. Has access to Claude Code (or is curious about it). May have heard of Manim
but never used it to build a physics simulation.

## What this reel teaches

**The subject is the workflow, not the physics.**

The learner will be able to:
1. Write a Claude Code prompt that generates a runnable Manim scene — pin the
   physical rule, the parameters, and what to render.
2. Read the generated script and locate the one line that encodes the physics;
   check it against a reference before running.
3. Verify a rendered simulation against exactly two testable predictions.
4. Issue a one-line change command and close the prompt→read→run→check→change loop.

The three physics experiments (photoelectric effect, Compton scattering, UV
catastrophe) are the running example — the excuse to run the loop three times with
real numbers. The physics facts must be correct (gate below), but they are not the
lesson.

## Loop structure (per segment)
Each of the three segments follows: **PROMPT → SCRIPT → RUN → CHANGE**
- **PROMPT**: The real `claude "..."` terminal command that generates the scene.
  Riff: what every generation prompt must specify.
- **SCRIPT**: The actual generated Python/ManimCE file. Riff: find the key line
  and check it against the textbook — this is where you catch errors before running.
- **RUN**: The Manim simulation. Riff: name the two concrete things to verify for
  this specific sim.
- **CHANGE**: A follow-up `claude "update ..."` command. Riff: closing the loop is
  the skill; the physics was the vehicle.

## Pedagogical contract
- Wonder register: first-principles, no hand-holding, honest about what the
  workflow demands. Not a tutorial — a demonstration.
- No exercises, no quizzes — this is a companion alongside the learner's own work.
- All physics numbers are gate-verified (see FACTCHECK.md). The narration is
  about prompting; the simulation shows the correct physics.

## Physics gate (numbers verified for the running example)
- Photoelectric: E = hc/λ in eV (h·c = 1240 eV·nm), Na work function Φ = 2.28 eV.
  Red 700 nm → 1.77 eV < Φ, blocked. Green 546 nm → 2.27 eV < Φ, blocked.
  UV 300 nm → 4.13 eV > Φ, K = 1.85 eV, speed ∝ √1.85. ✓
- Compton: Δλ = λ_C (1 − cos θ), λ_C = h/m_e c = 2.426 pm. ✓
- Planck: u(ν,T) ∝ ν³/(e^{hν/kT}−1). Normalised plot: x = hν/kT, peak at
  x = 2.821, f_P(2.821) ≈ 1.419 used as normalisation. ✓
- Rayleigh-Jeans: classical limit u ∝ ν² (Equipartition + wave density of states). ✓

## Medhavy register bookends (permanent rule)
- **B00**: Medhavy brand intro (MedhavyOpen terminal). TTS: "med davy A-I…" (never the literal spelling; "med havy" → ElevenLabs hears "med heavy").
- **B13**: Medhavy brand outro (MedhavyOutro card). TTS: "med davy. A-I-powered…"

## 9:16 Short (permanent rule)
One segment only — UV Catastrophe (most dramatic). Beats: B00 + B09–B12 + B13 = 95.2s. Hard cap 3:00.

## Length
14 beats: B00 (intro) + 12 content beats + B13 (outro) = 241.1s. Under the 5:00 cap.

VERDICT: PASS

---

## Refactor addendum — Claude cut, claude-medhavy channel (claude-refactor)

**Changes applied:**
- B00 `MedhavyOpen` → `ClaudeComposerAsk` cold open. Greeting: "Habari, Medhavy" (Swahili; Medhavy 1-word budget). Topic eyebrow: `QUANTUM MECHANICS · BUILD PHYSICS SIMS`. New Wonder-register narration. New audio: beat-B00.mp3 (replaces old intro).
- No ASK micro-beats inserted — inner beats are screen recordings/code displays, not Manim-generated graphics.
- B13 `MedhavyOutro` → `HANDOFF` beat. Greeting: "Your turn." New audio needed.
- B14 new `ClaudeTitleOutro` beat added. New audio needed.
- Inner beats B01–B12 narration, audio files, and remotion references untouched.
- All inner mp3s must be regenerated with kokoro af_kore (existing use voice_id 1sgY6Voq1aexKOB1IJ2D directly): `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims`
- New beats needing audio: `python3 runtime/scripts/generate_audio.py quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims --only B00,B13,B14`

VERDICT: PASS
