# Web Artifacts Builder — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-web-artifacts-builder`, Teardown). Register: **Plain**.
7 beats ≈ 2:15.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** BrutalistHesitantWriter (Remotion, no puppet host — hai-simple's WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Ask Claude for a dashboard with tabs and charts, and it feels like it just handwrites one HTML file. It doesn't — that file is bundled from a real project. So what actually gets built first?" | BrutalistHesitantWriter — types "Ask for a complex dashboard\nwith tabs and charts — it just\nhandwrites one HTML file.\nWait — what's actually built first?", trigger "handwrites" → "bundles" |
| B01 | anatomy | The skill is a four-step pipeline. Step one: initialize with bash scripts/init-artifact.sh, passing a project name — that one command provisions React 18 with TypeScript via Vite, Tailwind CSS 3.4.1 with shadcn/ui theming, path aliases, more than forty shadcn/ui components with Radix UI, and Parcel for bundling. Step two: develop by editing the generated code. Step three: bundle with bash scripts/bundle-artifact.sh — it installs Parcel and html-inline, builds the project, and inlines everything into one self-contained bundle.html. Step four: share bundle.html in the conversation. Testing is step five, and it's explicitly optional — build first, test only if issues come up or the user asks. | WebArtifactsAnatomy — the 4-step pipeline + tech stack |
| B02 | self-demo | The design section names four patterns to avoid: excessive centered layouts, purple gradients, uniform rounded corners, Inter font. That's the whole rule — negative and specific, no positive design system, so taste still does the work. The bundle itself carries React and ReactDOM, Tailwind utility classes, shadcn/ui component styles, every Radix UI primitive, and whatever else your code imports — collapsed into a single HTML file. | WebArtifactsDesign — anti-slop mandate + bundle anatomy |
| B03 | **mechanism (resolves the wrong guess)** | The architectural insight is that init-artifact.sh and bundle-artifact.sh solve two separate problems at once: bootstrapping a real React project, and collapsing it back into one shareable file. Two things worth knowing before you rely on it: bundling requires Node 18 or higher and an index.html in the project root — skip either and bundle-artifact.sh fails. And the skill's description mentions routing support, but the init script does not install react-router — that piece isn't wired in for you. | SkillTeardownMechanism — heading "Provisioned first. Bundled after." |
| **BCRY** | **carry-out** | That single HTML file isn't handwritten — it's bundled from a real React project. One script provisions the stack, one script collapses it back down to a file you can share. | WantQuote — the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Paste this into Claude: build me a note-taking app with tags, search, and a markdown editor, as a shareable claude.ai artifact — use the Web Artifacts Builder. Watch four things: does Claude run init-artifact.sh before writing any component code? Does it use shadcn/ui components from the pre-installed set instead of writing its own UI from scratch? Does it run bundle-artifact.sh and share bundle.html at the end, not a raw index.html or a dev server link? And does the result actually avoid the four named patterns — no dominant centered layout, no purple gradient, no every-corner-the-same-radius, no Inter font? | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Web Artifacts Builder. Liam, in for Bear. | OutroCTA — HAI skin, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the naive framing (one handwritten HTML file) before any mechanism is shown |
| Wrong guess surfaced *and corrected* | B00 types "handwrites" → corrected to "bundles"; B03 resolves it in narration ("bootstrapping a real React project, and collapsing it back into one shareable file") |
| No inference — the reel makes no claim beyond the skill's own documented pipeline and requirements, so no flag is needed | n/a |
| Carry-out compresses the distinction, not the topic | BCRY: provisioned-then-bundled, not "this video is about an artifact-building skill" |
| No design judgment | B03 states the pipeline split and the two hard requirements (Node 18+/index.html, no react-router in the scaffold) as fact, never "what it gets right / what it bites" — that framing is the source's Teardown language (`WebArtifactsTell`'s gets-right/bites card, `ClaudeVerdictArtifact`) and is dropped here |
| Host handoff | B00 is Remotion (BrutalistHesitantWriter), not a puppet — hai-simple's WRITER LAW substitution for `simple`'s HOST LAW |

## What changed from the source (redo contract)

- **Facts kept, unchanged:** the four-step pipeline (init-artifact.sh provisions
  React 18 + TypeScript + Vite, Tailwind 3.4.1 + shadcn/ui theming, 40+ shadcn/ui
  components with Radix UI, Parcel → develop → bundle-artifact.sh inlines everything
  into bundle.html → share bundle.html); testing explicitly deferred to step five and
  optional; the anti-slop design mandate's four named patterns (centered layouts,
  purple gradients, uniform rounded corners, Inter font) as a negative-only rule with
  no positive replacement; the bundle's contents (React/ReactDOM, Tailwind classes,
  shadcn/ui styles, Radix primitives, imported deps); the two hard requirements
  (Node 18+, index.html in project root) for bundling to succeed; the routing gap
  (description mentions it, init script doesn't scaffold react-router).
- **Register: Teardown → Plain.** The source's B05 (`WebArtifactsTell` — "what it gets
  right" / "where it bites" judgment) and BVDT ("Verdict" artifact,
  `ClaudeVerdictArtifact`) explicitly rank the design's trade-offs. Plain states the
  identical mechanics and limits as fact (this reel's B03) and lands the source's own
  framing — bootstrapping and bundling solved together, design taste left to you — as
  the carry-out (BCRY) instead of a verdict artifact or gets-right/bites card.
- **B00:** `ClaudeComposerAsk` (source's cold open — a composer ask showing a
  dashboard request and the pipeline's expected output) → `BrutalistHesitantWriter`,
  per hai-simple's WRITER LAW. The naive framing ("it just handwrites one HTML file")
  is the exact misconception the source's own B00 pre-empted ("It is not for simple
  single-file HTML") — restated here as the wrong guess instead of an opening ask.
- **B05 (`WebArtifactsTell`) + BVDT (`ClaudeVerdictArtifact`) → B03
  (`SkillTeardownMechanism`) + BCRY (`WantQuote`):** the source's two judgment-carrying
  beats (gets-right/bites card, verdict artifact) collapse into one factual mechanism
  beat (the provision-then-bundle framing, plus the two hard requirements) and the
  bare carry-out sentence — matching `simple`'s law that the verdict-recap position
  becomes the carry-out line in Plain register. Same beat count (7 → 7), renumbered
  sequentially (B00, B01, B02, B03, BCRY, BHTF, BOUT vs. source's B00, B01, B02, B05,
  BVDT, BHTF, BOUT).
- **BHTF:** kept the source's note-taking-app handoff prompt near-verbatim — already a
  real, paste-ready Claude prompt a general viewer can run today, and it drills the
  exact wrong guess (assuming raw output instead of a bundled artifact) B00 opened
  with, via the same four watch-for gates the source specified (init script runs
  first, shadcn/ui reused not reinvented, bundle.html shared not index.html, anti-slop
  patterns avoided).
- **Close:** BOUT's `ClaudeTitleOutro` (`@NikBearBrown`) → `OutroCTA` (Humanitarians AI
  skin, `@HumanitariansAI`), per hai-simple's channel-skin law. Voice/persona
  unchanged — Liam, Kokoro `am_onyx`, "in for Bear" (source already used this voice).
- **No AI-VIDEO, pantry, or human-drop beats existed in the source** — every source
  beat was already a registered Remotion component (`ClaudeComposerAsk`,
  `WebArtifactsAnatomy`, `WebArtifactsDesign`, `WebArtifactsTell`,
  `ClaudeVerdictArtifact`). B01/B02 reuse `WebArtifactsAnatomy`/`WebArtifactsDesign`
  as-is — their content is purely factual (the pipeline, the tech stack, the named
  anti-slop patterns, the bundle contents), no judgment baked into either component,
  so no NO-GENAI/NO-PANTRY substitution was needed beyond B00 (mandatory writer-open
  swap), B03 (mandatory judgment-card swap, since `WebArtifactsTell`'s gets-right/bites
  columns are baked into the component pixels and can't be neutralized by narration
  alone), and BOUT (mandatory HAI-skin swap).
- **Beat count:** 7 → 7 (B00, B01, B02, B03, BCRY, BHTF, BOUT). Unchanged.

## Handoff prompt (BHTF, read aloud in full)

> "Build me a note-taking app with tags, search, and a markdown editor, as a
> shareable claude.ai artifact. Use the Web Artifacts Builder."

Why it's worth running: it hands Claude a scenario complex enough to trigger the
skill, and the four things to watch — init script before any component code,
shadcn/ui components reused instead of hand-rolled, bundle.html shared instead of a
raw index.html or dev server link, and the four anti-slop patterns actually absent —
are the gates that tell you whether the pipeline ran or whether Claude just wrote a
page and called it an artifact.

---
**GATE P — signed:** ______________________  (human)
