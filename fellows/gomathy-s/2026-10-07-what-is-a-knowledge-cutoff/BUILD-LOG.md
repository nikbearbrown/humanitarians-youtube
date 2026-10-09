# BUILD-LOG — knowledge-cutoff

Landscape 16:9, 12 beats, 60.5 s review cut (`knowledge-cutoff-slate.mp4`),
built 2026-10-07. Kokoro `af_bella`, Plain register, `claude-hai` channel
(Bella in for Gomathy, `@HumanitariansAI`, kicker "Irreducibly Human").
No toolkit files edited; everything here lives in this folder.

## Lessons carried over from claude-liam-context-window

| Lesson (source) | Applied here |
|---|---|
| Only patterns that passed `./art final` and have a working portrait path | `ClaudeComposerAsk`, `FormBCard`, ink-only Manim, `OutroSeries` (landscape) / Manim title card (portrait). Not used: `ClaudeScienceLayerStack`, `ScaleComparison`, `OutroCTA`, `AttritionChain`, `ClaudeTitleOutro`, `BrutalistHesitantWriter`, `ClaudeVerdictArtifact` |
| Terracotta text fails GATE T §8.3 at largeText size (vertical B10) | `runningText: ""` on both composer beats, both orientations; no terracotta text anywhere |
| Remotion writer can't hit the portrait floor (vertical B01) | B01 hesitant writer authored in Manim for BOTH orientations — same sequence in each |
| FormBCard916 crashes without icons; long subs push the title out of title-safe (vertical B02–B08) | every FormBCard916 item has `icon: "BOX"`; every sub ≤ 26 chars |
| Manim kerning collapses word spaces at small sizes | `_label()` lays out at 4× then scales; 2× for long lines (4× hit Pango's layout width and wrapped B01's corrected line — caught in preview) |
| GATE V on a portrait review cut false-flags the burn-ins (vertical BUILD-LOG) | see vertical/BUILD-LOG.md |

## Deliberate deviations (approved in the script review)

- **B01 is 4.6 s, not ≥ 9 s.** ai-explainer's EXECUTIVE-SUMMARY LAW asks for
  ≥ 9 s and 20–35 words; a 60 s / 12-beat reel can't spend that. Same trade
  as claude-liam-context-window (3.2 s). The correction lands on screen
  (verified in the frame at 85%).
- **B09 summary is `FormBCard`, not `ClaudeVerdictArtifact`** — outside the
  allowed set; its 916 variant only passed via a sparse exemption.
- **B01 is Manim, not `BrutalistHesitantWriter`** — same reason.

## Gates (landscape)

- GATE B (strict): first run caught B02's title at the top safe edge
  (y 3.4); titles moved from y 3.1 → 2.9 in B02/B04. Re-run clean.
- GATE V (`ART_STRICT=1`, no `--lenient`): 24 frames, 0 BLOCKER / 0 MAJOR.
- GATE T: PASS, 0 FAIL. Advisory §8.10 only: B07 (0.80) and B08 (0.88)
  narration echoes the card. B08's wording is the user's approved edit;
  B07 left as approved.
- `[art] WARNING: build stamp failed: 'str' object has no attribute 'get'` —
  known toolkit stamp bug (also in claude-liam-context-window), non-blocking.

## Open, for the reviewer

- `ClaudeComposerAsk` shows its default `modelLabel` chip "Fable 5" (B00,
  B10). It's the app's UI chrome, not a claim, and the prior reel kept the
  default — but it is a model name on screen. `modelLabel` is a prop if you
  want it changed.
- B11 `OutroSeries` renders on its own white ground with a thin red
  underline (component tokens) — same one-beat palette break as the prior reel.
