# BUILD-PROMPT — The Beat Sheet Is the Prompt

Paste-ready rebuild. Free, local, no keys. **Never publishes.**

```bash
cd brutalist.art && source .venv/bin/activate
R=../ai-fluency/youtube/hai-beat-sheet-is-the-prompt

# 1. AUDIO — the master clock. Every remotion prop's durationSeconds = actual_duration_s.
python runtime/scripts/generate_audio_kokoro.py $R

# 2. VISUALS — Remotion scenes only, rendered at --scale=2 (4K).
python runtime/scripts/remotion_scenes.py $R

# 3. REVIEW CUT (fact-check not yet signed).
ART_FACTS=0 ./art run $R

# 4. LOOK AT THE FRAMES — B01 at 50/70/90%: the correction must be on screen by 70%.

# 5. FINAL MASTER — only after FACTCHECK-DRAFT.md is checked and renamed FACTCHECK.md.
./art final $R
```

Known traps: the hesitant writer splits trigger/replacement words on commas; tab labels
clip past ~12 characters; set `language` on every code card (default label is PYTHON).
