# PEDAGOGY.md — NBB wrapper: vox-spindle-checkpoint

**Date:** 2026-07-16  
**Scope:** New wrapper beats only (NBB00, NBB01, NBB02, NBB03). Body beats B01–B13 inherit the source reel's PEDAGOGY (VERDICT: PASS already on file at `../vox-spindle-checkpoint/PEDAGOGY.md`).

---

## NBB00 — Kore cold open

**Beat type:** Cold open (new)  
**Voice:** Kore / Kokoro af_kore  
**Greeting:** "Bonjour, Kore"

**Pedagogical check:**

- Does the cold open frame the central question without answering it? YES — "a dividing cell does something strange: it reaches the moment of maximum readiness and then stops" names the phenomenon but does not explain the mechanism.
- Does it end with the exact handoff sentence "Can you explain it, Bear?"? YES.
- Is the composer command a concise version of the video's real central question? YES — "Why does a cell stop and wait at the moment chromosomes are ready to separate?" matches the body's question beat (B03) faithfully.
- Does the output block hand directly into the first body frame without redundancy? YES — the output lines are three-word teaser statements, not a full summary; they pique curiosity rather than preempt the body.
- Is the beat appropriately short (6–10 s target)? YES — estimated ~8 s.
- Does it introduce Kore as the voice? YES — "Bonjour, Kore — in for Humanitarians AI."
- Does it avoid answering the question or summarizing the body? YES.

**Verdict:** PASS

---

## NBB01 — Bear verdict

**Beat type:** Verdict (new)  
**Voice:** Bear / ElevenLabs ELEVENLABS_VOICE_NIKBEARBROWN  
**Register:** Teardown

**Pedagogical check:**

- Does the verdict synthesize rather than repeat the whole body? YES — it restates the mechanism as a chain (MCC → APC/C → securin → separase) in one compressed sentence, then immediately moves to the design trade-off.
- Does it name the mechanism the body demonstrated? YES — the MCC cascade is named correctly.
- Does it name the trade-off or limit? YES — "speed for accuracy … costs real minutes at every division" is the explicit trade-off statement.
- Does it use only claims supported by the body (B01–B13)? YES — all claims (single-condition veto, MCC/APC/C/securin/separase cascade, 92 kinetochores, aneuploidy as cancer driver) are present in the body beats.
- Is it in the Teardown register? YES — "Here's what the body just demonstrated…" / "The mechanism:" / "The trade-off:" / "The checkpoint optimizes for fidelity over throughput" are characteristic Teardown patterns.
- Forbidden phrases absent? YES — no "innovative," "one could argue," "it seems as though," or specs without context.
- Is the verdict beat rendered as ClaudeVerdictArtifact? YES.
- Do the artifact lines match the narration's claims? YES — all four lines are supported by the narration.

**Verdict:** PASS

---

## NBB02 — "Your turn" handoff

**Beat type:** Handoff (new)  
**Voice:** Bear / ElevenLabs ELEVENLABS_VOICE_NIKBEARBROWN  
**Greeting:** "Your turn." (exact)  
**runningText:** "paste this into Claude…" (exact)

**Pedagogical check:**

- Is the greeting exactly "Your turn."? YES.
- Is runningText exactly "paste this into Claude…"? YES.
- Is the prompt genuinely useful and paste-ready? YES — it has context (cancer type), a specific structured question (mutations, chromosome errors, aneuploidy mechanism), and produces a useful output on its own in any frontier LLM.
- Does it extend and apply the body's central idea rather than being generic? YES — it directs the viewer to apply the spindle checkpoint mechanism to a specific cancer of their choice.
- Is this a Claude-paste prompt (not a CLI command)? YES.
- Is it the second-to-last beat? YES (NBB02 precedes NBB03/OUTRO).

**Verdict:** PASS

---

## NBB03 — Claude title outro

**Beat type:** Outro (new)  
**Rendered with:** ClaudeTitleOutro  
**Handle:** @HumanitariansAI

**Pedagogical check:**

- Is the title the episode title restated? YES — exact title from metadata.
- Does the subline derive from the verdict? YES — "one unattached kinetochore, entire cell arrested" directly summarizes the verdict's core claim.
- Does it replace (not supplement) the source's OutroSeries/OutroCTA? YES — B14/B15 are excluded from the assembly.
- Is it the final beat? YES.

**Verdict:** PASS

---

## Overall wrapper verdict

All four new beats pass their individual pedagogy checks. Body (B01–B13) is locked and inherits source PEDAGOGY.

VERDICT: PASS
