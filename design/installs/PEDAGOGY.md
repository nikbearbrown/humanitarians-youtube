# PEDAGOGY.md — Installs, .env & Credentials

Pedagogy audit against the SLATE-RUNNER checklist. Written before audio credits are spent.

## Act structure (required: hook → argument → reveal → how → close)

| Act | Beats | Present? |
|-----|-------|----------|
| Hook / cold open | B00 | ✓ — terminal command; "set up once" frames the promise immediately |
| Argument | B01–B03 | ✓ — one file feeds every feature; blank = off; credentials are OAuth files, not keys |
| Tools | B04–B07 | ✓ — npx (why pinned), pip (what it installs), venv (what isolation means) |
| Doctor | B08–B09 | ✓ — readiness check; Claude Code must run inside the venv |
| Paid services + hero | B10–B12 | ✓ — four services; voice clone as the highest-leverage move; caveat |
| Verify | B13 | ✓ — `./art keys` live validation |
| Outro / CTA | B99 | ✓ — brutalist.art · @NikBearBrown |

Act structure: **PASS**

## Key-case cold open (must open on a problem or question, not a title card)

B00: Terminal command types out — `$ art installs "set up once"` — with a checklist that
immediately sets expectations. The hook is the promise: one-time setup, then just make
videos. It opens on the action, not a slide. **PASS**

## Gap-formula question beat (the question that creates the gap)

B10 narration creates the gap: "Four services cost money, and none is required to start."
This raises the question — which one matters most? B11 answers it immediately with the hero
beat (voice clone). The tension is: why spend money on cloning your voice? B11 resolves it
by showing the time cost of NOT doing it: 30 minutes wasted every session vs. 30 minutes
spent once. **PASS**

## Utility-framing lint (every beat must be FOR the viewer, not about the tool)

Checked each narration against "what does this do FOR the viewer":
- B01: explains that blank keys don't break things → viewer can start partial
- B03: explains OAuth files vs. keys → viewer knows where to put them
- B04: explains npx pin → viewer understands why the command works everywhere
- B07: explains venv isolation → viewer understands why numpy<2 doesn't break their machine
- B09: explains Claude Code + venv → viewer knows exactly how to invoke Claude Code correctly
- B11: quantifies time saved per session → viewer sees the ROI of voice cloning
- B12: reframes mispronounce as a review note → viewer isn't alarmed

No beat reads as feature inventory without viewer benefit. **PASS**

## Vocabulary law (no jargon without a definition in the same beat or the prior beat)

- "npx" defined in B04 narration before B05 shows the command
- "pip" defined in B06 narration before it appears in commands
- "virtual environment / venv" defined in B07 narration with isolation metaphor
- "voice clone" introduced in B11 narration alongside the split-screen visual
- "art keys" shown in B13 with output that explains what it checks

All new terms are visually anchored on first use. **PASS**

## Equation tangents (none in this reel — no math; n/a)

**N/A** — this is a setup / tooling explainer, not a math video.

## Recap + chapter pointer (close must point toward next step or next video)

B99 CTA: "Clone your voice. Then make videos." — points to the immediate next action.
B13 narration: "art keys checks every key you've set, live and free, without spending a
thing" — leaves the viewer with a concrete verification step. The CTA closes on the
highest-leverage unlock, not generic marketing. **PASS**

## Length law (target ≤ 4:00 for an explainer intro)

Total estimated duration: ~205s = 3:25. **PASS** (under 4:00)

## Narration script review (spot-check key beats)

- B04 "npx runs a Node package's command-line tool without installing it globally" —
  technically precise, one sentence, immediately useful. Good.
- B07 venv metaphor — "isolated Python: its own interpreter, its own packages, in a folder
  inside the project" — concrete enough to be actionable. Good.
- B11 hero beat — "thirty minutes gone before you keep one good take" vs. "every video
  narrates itself from the beat sheet, in your voice, instantly" — strong contrast, rhythm
  works. Best narration in the reel.
- B12 "a rounding error against never fighting a microphone again" — memorably dismissive
  of the caveat. Good punchline.

No narration text flagged for revision. **PASS**

---

VERDICT: PASS
