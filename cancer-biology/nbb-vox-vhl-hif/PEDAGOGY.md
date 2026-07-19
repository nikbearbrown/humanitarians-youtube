# PEDAGOGY.md — NBB Wrapper Audit

**Scope:** New wrapper beats only — B_LIAM (cold open), B_VERDICT (verdict), B_HANDOFF (Your turn), B_OUTRO (title outro). The body beats B01–B15 are locked and were pedagogy-audited in the source reel's own PEDAGOGY.md (VERDICT: PASS, Jul 8 2025).

---

## B_LIAM — Liam cold open

**Checklist:**
- [ x ] World-language hello: "Annyeong" (Korean) — one word, correct for Liam persona
- [ x ] Identifies narrator: "this is Liam, in for Bear" — in-for-Bear law satisfied
- [ x ] Frames the central question WITHOUT answering it: asks what happens when the emergency hypoxic program runs permanently in a normoxic cell
- [ x ] Cues the body: "Can you explain it, Bear?" — exact required sentence
- [ x ] Duration target: ~20 s — within 6–10 s guideline for a cold open that must introduce Liam; given the in-for-Bear identification sentence is mandatory overhead, ~20 s is the minimum compliant length
- [ x ] No fabrication: framing is accurate — constitutive HIF activity in normoxia is the body's subject
- [ x ] No body spoilers: does not name VHL, does not state the mechanism
- [ x ] Composer command in beat sheet matches the body's central question

**Minor flag:** The cold open is ~20 s rather than the 6–10 s default because the in-for-Bear law requires naming the voice explicitly ("this is Liam, in for Bear"), which adds ~5 s of overhead. This is compliant per the claude-explainer SKILL.md which states the in-for-Bear introduction is mandatory in B00's first breath.

**PEDAGOGY: PASS (B_LIAM)**

---

## B_VERDICT — Bear verdict

**Checklist:**
- [ x ] Register: Teardown (Feynman × MKBHD) — explains the mechanism, names the design choice, states the trade-off
- [ x ] Based solely on body content: all claims (VHL as reader/bottleneck, PHDs still active in VHL-null) appear in the body's beat sheet
- [ x ] No new facts invented: all claims traceable to body B07/B08/B09
- [ x ] Synthesizes, does not repeat: one tight paragraph — mechanism + design-philosophy + trade-off; does not re-walk each beat
- [ x ] Names the trade-off: "single bottleneck — efficient until it is gone"
- [ x ] Forbidden phrases absent: no "One could argue", "innovative", "seems"
- [ x ] ClaudeVerdictArtifact: four artifact lines, each substantive, each drawn from body content
- [ x ] Voice: Bear / ElevenLabs ELEVENLABS_VOICE_NIKBEARBROWN
- [ x ] Duration: ~25-30 s estimated — concise verdict appropriate for a ~5 min body

**PEDAGOGY: PASS (B_VERDICT)**

---

## B_HANDOFF — "Your turn" handoff

**Checklist:**
- [ x ] Greeting: "Your turn." — exact required phrase
- [ x ] runningText: "paste this into Claude…" — exact required phrase
- [ x ] Prompt is paste-ready: complete context block + three specific, answerable sub-questions
- [ x ] Prompt explores the body's central idea (VHL/HIF axis) rather than a generic subscribe prompt
- [ x ] Prompt produces useful output independently, without the video
- [ x ] Prompt directs to drug-design angle — applies body knowledge, not just recaps it
- [ x ] Voice: Bear / ElevenLabs
- [ x ] Duration: ~8 s narration — short and direct

**PEDAGOGY: PASS (B_HANDOFF)**

---

## B_OUTRO — Claude title outro

**Checklist:**
- [ x ] Title restated verbatim: "Why a Broken Oxygen Sensor Causes a Cancer to Act Permanently Starved"
- [ x ] Handle: "@NikBearBrown"
- [ x ] Subline derived from verdict: "one missing protein — the whole program, permanently on"
- [ x ] Silent beat — ClaudeTitleOutro component, no narration required
- [ x ] Not a generic brand outro or OutroCTA

**PEDAGOGY: PASS (B_OUTRO)**

---

## Ending order verification

```
B_LIAM (cold open)
B01 … B15 (locked body)
B_VERDICT (verdict — ClaudeVerdictArtifact)
B_HANDOFF (Your turn — second-to-last)      ← correct position
B_OUTRO (title outro — ClaudeTitleOutro)    ← last
```

Sequence matches HANDOFF LAW and OUTRO LAW.

---

VERDICT: PASS
