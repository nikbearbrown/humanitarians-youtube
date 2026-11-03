# BUILD-LOG — financial-services--claude-liam-buyer-list

## 2026-09-01 — hai-simple redo, review cut + delivery

**Mode:** `redo`. Source: `/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-buyer-list/beat_sheet.json`
— a Teardown-register skill-teardown of the Anthropic-style `buyer-list` Skill (builds
and organizes a buyer universe for sell-side M&A: strategic + financial buyers, fit,
prioritized outreach). 7 beats in the source; 7 beats in this redo (B00, B01, B02, B03,
BCRY [was BVDT], BHTF, BOUT).

**What changed from source:**
- B00: `ClaudeComposerAsk` → `BrutalistHesitantWriter` (WRITER LAW). Wrong word "app"
  corrected to "skill" on screen, tied to the reel's actual mechanism (a Skill isn't an
  autonomous app — it's a folder of instructions Claude follows). Narration 33 words +
  `lead_silence_s: 0.8`; rendered B00.mp4 = 10.62s (≥ the 8s / 9s-window floor).
- B03 ("design tell" in the source, with Teardown verdict language — "what it gets
  right" / "what it bites"): rewritten as a plain mechanism + scope statement, no
  trade-off verdict. Facts (the skill's stated job) unchanged.
- BVDT (verdict artifact) → BCRY (carry-out, `WantQuote`): "A Skill doesn't make Claude
  smarter — it makes Claude follow your steps, in order, every time." Written first,
  ties back to B00's wrong guess.
- BHTF: kept `ClaudeComposerAsk` (composer only appears at the Your Turn handoff, per
  WRITER LAW) but replaced the source's proprietary-skill prompt with a generically
  runnable one (explain a Claude Skill + walk through a 3-step coffee SKILL.md) since
  viewers don't have the buyer-list SKILL.md file.
- BOUT: `ClaudeTitleOutro` (locked to @NikBearBrown) → `OutroSeries` with the
  Humanitarians AI skin, same title-restate narration as source.
- No AI-VIDEO, pantry, or human-drop beats existed in the source (it was already
  all-REMOTION), so NO-GENAI/NO-PANTRY LAW required no beat substitution beyond the
  B00 WRITER LAW swap.

**Known template limitation (not a blocker):** `OutroSeries`/`OutroCTA` import
`tokens/vox` (teardown: white/near-black/crimson), not `tokens/humanitarians.ts` — no
registered scene imports the true humanitarians hex set, confirmed by `./art scenes`
search and by grep across `runtime/remotion/src/scenes/*.tsx`. `SkillTeardownAnatomy` /
`Pipeline` / `Mechanism` and `WantQuote` likewise hardcode the Claude palette with no
override props. `BrutalistHesitantWriter` (B00) DOES expose `ink`/`accent`/`bg` and was
built with the true humanitarians hex values (`#2F2A26` / `#E4572E` / `#F3EBDD`). This
is a componentry gap in the shared scene library, not a defect in this reel's sheet —
editing shared Remotion scene source was out of scope for a single-reel build. Logged
here per GATE L rather than silently declared "done."

**GATE T:** one FAIL on first pass (B03 on-screen body: 20 words > 12-word pull-quote
limit) — fixed by shortening the on-screen card text to 9 words while narration kept
the full sentence. Re-run: PASS.

**Build:**
- Audio: `generate_audio_kokoro.py`, 7/7 beats, am_onyx, $0.00.
- Render: `remotion_scenes.py`, 7/7 REMOTION beats, foreground, --concurrency=1.
- Compile: `compile.py` → forced 4K master directly (720p→2160p, no slates) —
  `financial-services--claude-liam-buyer-list.mp4`, 73.7s, 3840×2160.
- GATE AUDIO: PASS, mean_volume −24.0 dB (independently reconfirmed via
  `ffmpeg -af volumedetect`: mean −24.0 dB, max −2.9 dB — both far above the −40 dB
  floor).
- Gate V: 7 frames pulled at 3s stride and read directly — B00's correction
  ("skill") visible late in the beat with `@HumanitariansAI` footer burned on the
  first beat only; B01–BHTF legible, no overlap, no overflow; BOUT outro clean
  (modulo the palette limitation above).
- 4K deliverable: the compiled master was already true 4K (3840×2160), so
  `<slug>-4k.mp4` is a direct copy — no separate upscale render needed.

**Delivered (Phase 4):** `deliver.py --push` — staged 4K + description to
`DELIVERY/financial-services--claude-liam-buyer-list/` (synced Drive
`Claude_Bear/` outbox); committed + pushed `claude-bear/financial-services--claude-liam-buyer-list/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md) to
`github.com/nikbearbrown/humanitarians-youtube`.

**Status: DONE.** Review cut passes every gate; 4K delivered to both targets.
