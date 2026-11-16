# PEDAGOGY — Same Idea, Different Words

**Reel** `weekly_updates/2026-11-13-same-idea-different-words/` · **slug** `claude-sai-same-idea-different-words`
**Subject** Ethan Mollick, "Fable 5.2 and Jagged AGI" (One Useful Thing, 9 Nov 2026), tested against his Portals repo · **week of** 2026-11-13 (built 2026-11-16), second reel
**Host** Sai, in his own name · **Voice** Kokoro `am_onyx`, free and local
**Chassis** Remotion + one image plate (three Portals worlds rendered locally), no Manim, nothing paid
**Length** ~1 minute, Sai's choice — a 7-beat cut of the usual spine (deliberate deviation)

---

## The ONE idea

> Mollick says Fable 5.2 is "almost AGI" and that its jaggedness is now in
> judgement, not facts. His own repo shows one case: three of 471 AI-built
> worlds are the same circling-animal idea, and their descriptions share no
> words at all, while almost half of all world pairs share one. The sameness
> is in the idea, where a word-matching check can't see it; a person still has
> to ask "too repetitive?".

Sai's brief (2026-11-16): "Make the 2nd video based on this blog", the URL;
then chose ~1 minute and approved showing Portals worlds under CC BY-NC-SA 4.0,
credited. Angle and title proposed by the assistant; Sai can overrule.

## Act structure

| Beat | Act | Pattern | Why |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Mollick: almost AGI, but jagged. Jagged where? Test one example in his code. |
| B01 | THREE CYCLONES | image plate · three | 471 worlds; reindeer, mantas, storks — one idea; by his account no agent noticed. |
| B02 | HOW A CHECK SCORES SAMENESS | `TypesetMath` | cos θ = a·b / (‖a‖‖b‖); no shared word ⇒ a·b = 0 ⇒ cos θ = 0. |
| B03 | WHAT THE WORDS MISS | `ExecutedData` | 471 worlds; 45.5% of pairs share a word; the cyclone pairs 0%. |
| B04 | VERDICT | `ClaudeVerdictArtifact` | Builds like experts; misses the step back; a person has to ask. |
| B05 | HANDOFF | `ClaudeComposerAsk` | Ask for 20 ideas, ask which are the same idea in different words, check it. |
| B06 | OUTRO | `LogoOutro` | `@HumanitariansAI`. |

## ILLUSTRATE LAW check

Claude UI at B00, B05 and the verdict only. Body: `plate → TypesetMath →
ExecutedData`. No repeats; every beat has an ordered `show` block.

## 9:16

Every Remotion pattern has a `*916` sibling; the plate has a re-composed
portrait plate (`pantry/B01-916.mp4`: reindeer on top, mantas and storks below).

## Evidence and honesty

- **The post has no benchmarks.** Every number in it is Mollick's own count or
  the AI's own estimate. So the reel tests one example rather than restating
  his figures; none of his unverifiable numbers (84 → 204 rule-book sections,
  87,500 words, 12 → 30 worlds a day) is on screen.
- **The three worlds exist:** `reindeer-cyclone` ("The Turning Herd",
  wilderness), `manta-cyclone` ("Inside the Manta Cyclone", ocean),
  `stork-kettle-riso` ("A Kettle of Storks", sky) in `src/worlds/index.js` at
  `210133f`. `design/shipped.json` puts the first two in the same release (r2s)
  and the storks in r3g — consistent with his "three separate teams", which the
  repo cannot confirm.
- **The measurement** (`evidence/overlap.py` → `overlap.out`): TF-IDF with
  scikit-learn 1.8.0's English stop words over the 471 descriptions in
  `design/descriptions.json`. 110,685 pairs; 50,315 (45.5%) share at least one
  content word; the three cyclone pairs share none (a·b = 0.000000 computed by
  hand, not just the library's cosine).
- **Where the claim would flip — said on screen:** the one-line captions in
  `index.js` for the reindeer and manta both use the word "cyclone" (cosine
  0.167). The reel's claim is about the *descriptions*, and B03's note says the
  captions differ. Note that sklearn's stop list includes number words
  ("three"), which both the reindeer and stork texts use.
- **"No agent noticed"** is Mollick's account ("Most critically, the AI did not
  notice these problems itself"; "None of them asked whether the work was too
  long, too repetitive, or no fun"), attributed in narration ("By his account").
- **A fourth candidate, not used:** `still-lake-in-the-herd` (Moby-Dick's whale
  herd) is "a circling herd of sperm whales" with calves at the still centre —
  arguably the same idea again. Left out: it's a literary adaptation, and it
  shares "calves" with the reindeer, so it would muddy the zero.
- **Images:** rendered locally from the repo with its own `?freeze&grab` test
  harness on the Mac's GPU (`evidence/portal_shots.mjs`); poses and seeds in the
  sidecars. CC BY-NC-SA 4.0, credited on every panel and in DESCRIPTION.md.
  **ShareAlike:** if this video is ever offered under a licence, it has to be
  CC BY-NC-SA-compatible; NC: no paid use.

## Attribution

Hosted by Sai. The essay and Portals are Ethan Mollick's; Portals' code was
written by AI agents (README). Fable 5.2 is Anthropic's model. The test, the
renders and the measurements were made for this reel on 2026-11-16.

## Pronunciation (narration only)

- `Fable 5.2` → "Fable five point two". `AGI`, `Mollick` read correctly.

## Expected build noise (not bugs)

- SKIN LINT at B06 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).

---

## Human review checklist

Nothing below has been done by the assistant.

- [ ] Title and angle "Same Idea, Different Words" — keep, or overrule?
- [ ] Fair to Mollick? The reel agrees with his thesis and tests one example; it
      does not dispute anything he wrote.
- [ ] OK with the CC BY-NC-SA terms carrying over to this video (no paid use)?
- [ ] Anything here better left out of a public video?

VERDICT: __________ — reviewer: ___ date: ___

---

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 12.4s measured (37 words)

> This is Sai. Ethan Mollick calls Anthropic's Fable five point two almost AGI:
> as good as most experts at most computer work, but jagged. Jagged where? I
> tested one of his examples in the code he published.

### B01 · THREE CYCLONES — `image plate · three` · 12.9s measured (39 words)

> His agents built four hundred and seventy-one worlds to fly through. Three are
> one idea: reindeer turning in rings on a frozen lake, mantas in a turning
> column, storks circling up a thermal. By his account, no agent noticed.

### B02 · HOW A CHECK SCORES SAMENESS — `TypesetMath` · 9.6s measured (29 words)

> A word-matching check scores two texts by the cosine of their word vectors. If
> two descriptions share no words, the dot product is zero, and so is the score.

### B03 · WHAT THE WORDS MISS — `ExecutedData` · 10.6s measured (34 words)

> Across all four hundred and seventy-one worlds, almost half of all pairs share
> at least one word. The three cyclones share none. The sameness is in the idea,
> where word matching can't see it.

### B04 · VERDICT — `ClaudeVerdictArtifact` · 8.8s measured (31 words)

> So Fable builds like a team of experts. What it still misses is the step back:
> is this too long, too repetitive, any fun? For now, a person has to ask.

### B05 · HANDOFF — `ClaudeComposerAsk` · 7.8s measured (24 words)

> Your turn. Ask your AI for twenty ideas, then ask which ones are the same idea
> in different words. Then check its answer yourself.

### B06 · OUTRO — `LogoOutro` · 2.8s measured (5 words)

> Same idea, different words. Sai.

**Total: 199 words** → 65.0s measured (1:04). Audio remains the master clock.

<!-- NARRATION:END -->
