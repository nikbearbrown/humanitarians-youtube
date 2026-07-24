# BUILD-PROMPT — claude-liam-frontend-design

## How this reel was built

Skill: `claude-explainer` · Modifier: `skill-teardown`
Brand: `claude-liam` · Voice: Kokoro `am_onyx` · Engine: free/local

## Beat map

| Beat | Pattern | Content |
|---|---|---|
| B00 | ClaudeComposerAsk | Cold open — Hei Liam, frontend-design fires on design request |
| B01 | FrontendDesignAnatomy | 5 principles + TRIGGER + 3 defaults to avoid |
| B02 | FrontendDesignProcess | 2-pass process: 4-part plan → critique gate → code |
| B03 | FrontendDesignRestraint | Restraint (Chanel rule) + writing in design |
| B05 | FrontendDesignTell | Teardown — 2-pass gate insight + gets right / bites |
| BVDT | ClaudeVerdictArtifact | Verdict — 6 lines |
| BHTF | ClaudeComposerAsk | Handoff — prompt read aloud + what to watch for |
| BOUT | ClaudeTitleOutro | Outro — Frontend Design · Liam, in for Bear |

## Custom Remotion components

- `FrontendDesignAnatomy` — trigger + 5 principles + 3 defaults blocked
- `FrontendDesignProcess` — 2-pass plan template + critique gate
- `FrontendDesignRestraint` — restraint rules + writing principles
- `FrontendDesignTell` — teardown: 2-pass insight callout + gets right/bites card-rows

## Build command

```bash
cd books
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  anthropics/skills/youtube/claude-liam-frontend-design/

python3 brutalist-art/runtime/scripts/remotion_scenes.py \
  anthropics/skills/youtube/claude-liam-frontend-design/

python3 brutalist-art/runtime/scripts/compile.py \
  anthropics/skills/youtube/claude-liam-frontend-design/
```
