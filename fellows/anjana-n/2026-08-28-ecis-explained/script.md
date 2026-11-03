# ECIS Episode 4 — Not Just What. Who, How Clean, and What Came Before.

**Skill:** ai-explainer
**Target length:** ~60 seconds
**Voice:** am_onyx (Onyx)
**Narrator:** Anjana
**Style:** Same register as Episodes 1-3. The system keeps maturing — this episode is about context: who spoke, how clean the source was, and what happened last quarter.

---

## Beat 1 — Recap

**Duration:** ~5 seconds

**Narration:**

ECIS could read earnings calls with three models, gate its own quality, and trace every signal. That was episode three. Now it understands context.

**Visual direction:**

A composite flash of Episode 3's key visuals — the triple model nodes (purple, teal, amber), the conveyor-belt quality gates, the provenance stack — layered into a single compact image. Hold for two seconds. The composite dims and the word "Context." fades in below it, large and clean. Frame opens up for Beat 2.

---

## Beat 2 — Who Said It

**Duration:** ~15 seconds

**Narration:**

Not all speakers are equal. When a CFO says "we are raising guidance," that is the most authoritative voice on the call. When an analyst says the same words in a question, that is speculation. The system now assigns a weight to every speaker. CFO, one point zero. CEO, zero point eight. Analyst, zero point three. Operator, zero. The same sentence, the same confidence score, lands completely differently depending on who said it.

**Visual direction:**

A quote card lands center screen: "We are raising our full-year revenue outlook." A speaker label animates in — "CFO — Sarah Chen" with a weight badge "1.0" in green — and the equation 0.85 × 1.0 = **0.85** appears; the output glows green, strong. The label swaps to "Analyst — David Park," weight badge changes to "0.3" amber, same confidence 0.85, equation updates to 0.85 × 0.3 = **0.26**; output dims. The quote slides left and a role-hierarchy bar stack appears on the right: CFO 1.0, CEO 0.8, COO 0.7, IR 0.6, Analyst 0.3, Operator 0.0 (greyed out). Label: "Same words. Different authority." Speaker names are fictional.

---

## Beat 3 — How Clean

**Duration:** ~12 seconds

**Narration:**

Even the right speaker can be reading from a noisy chunk. Safe harbour disclaimers mixed in with real guidance. A sentence cut mid-thought by the chunker. Three different speakers in one chunk. The system now scores every chunk on four dimensions: boilerplate ratio, token count, section completeness, and speaker transitions. The scores combine into a single quality multiplier. Clean chunks keep their weight. Noisy chunks get suppressed before they reach the triangulator.

**Visual direction:**

A messy chunk card on the left: red-highlighted boilerplate mixed into real content, a sentence cut off mid-word, two speaker labels visible ("CEO" and "Analyst"). Four score meters fill in sequence — boilerplate 0.35 (amber), token count 0.72 (light green), completeness 0.50 (amber), transitions 0.40 (amber) — merging into "Quality: 0.49" in amber. A clean chunk card on the right: single speaker, complete sentences, meters filling high (0.05 / 0.95 / 0.98 / 1.0) merging into "Quality: 0.94" in bright green. Both chunks flow toward a compact triangulator icon — the clean chunk's arrow thick and bright, the noisy chunk's arrow thin and nearly invisible. Label: "Quality gates the signal, not the data."

---

## Beat 4 — What Came Before

**Duration:** ~12 seconds

**Narration:**

A single quarter means nothing in isolation. "Revenue guidance raised" hits different when the company raised guidance last quarter too. The system now links signals across time. Consecutive raises. Consecutive lowers. Reversals. Stable maintained. Every signal carries its trend context. Two quarters of raised guidance in a row is a pattern. A sudden reversal after three stable quarters is a different pattern. The scorecard can now measure which patterns actually predict market returns.

**Visual direction:**

A horizontal timeline for one illustrative ticker ("Company A") with four quarterly markers: Q1 raised (green up), Q2 raised (green up), Q3 raised (green up), Q4 lowered (red down). Trend tags animate between markers: Q1→Q2 and Q2→Q3 "consecutive_raise" in green connecting bands; Q3→Q4 "reversal" in a pulsing red band that stands out against the green run before it. A second, smaller timeline below for another illustrative ticker ("Company B") shows four quarters all "maintained" — steady blue arrows, tagged "stable_maintained" as one calm band. The contrast between a volatile reversal and a steady pattern is the point. Label: "Patterns, not snapshots."

---

## Beat 5 — All Together

**Duration:** ~8 seconds

**Narration:**

Three multipliers now flow into every signal. Reader confidence, scaled by speaker authority, scaled by chunk quality. Trend context rides alongside. The triangulator does not just ask what the readers found. It asks who said it, how clean the source was, and whether it fits the pattern.

**Visual direction:**

The triangulator node sits center, same style as prior episodes. Three inputs stack in from the left: reader confidence 0.85 (white/neutral), speaker weight 0.8 CEO (green), chunk quality 0.92 (green). An equation animates step by step: 0.85 × 0.8 = 0.68, then 0.68 × 0.92 = **0.63**. The output signal exits right at confidence 0.63 with a trend tag "consecutive_raise" riding alongside it like a luggage tag. Below: "What. Who. How clean. What came before." — each word mapped visually to its input above.

---

## Beat 6 — Close

**Duration:** ~5 seconds

**Narration:**

Three models. Three multipliers. Trend across quarters. ECIS, episode four.

**Visual direction:**

Quick montage, three flashes: the triple-node architecture (purple/teal/amber) on "three models"; the reader × speaker × quality equation from Beat 5 on "three multipliers"; the Company A Q1–Q4 timeline with the reversal tag on "trend across quarters." Title lands: **ECIS — Episode 4**. Same sign-off style as Episodes 1-3. Fade to Claude-branded outro bookend.

---

## Production Notes

**Total estimated duration:** ~57 seconds of narration + bookends = ~63 seconds total

**Continuity:** Purple/teal/amber model nodes, the triangulator node style, and the signal-card format all carry over unchanged from Episodes 1-3. Illustrative tickers (Company A, Company B) match the precedent already set in Episodes 2 and 3's dashboard beats.

**Voice:** am_onyx, same as Episodes 1-3. Tone: confident, precise — the system is maturing through added discipline, not just added scale.

**Visual mix:** All Remotion. Beat 2's CFO-to-analyst swap and Beat 4's timeline reversal are the two signature visual moments.

**Numbers to confirm before audio (real-system specifics, not yet verified):**
- Speaker weight scale — CFO 1.0 / CEO 0.8 / COO 0.7 / IR 0.6 / Analyst 0.3 / Operator 0.0
- The four chunk-quality dimensions (boilerplate ratio, token count, section completeness, speaker transitions) and that they combine into a single multiplier
- The illustrative worked numbers: 0.85×1.0=0.85, 0.85×0.3=0.26, noisy-chunk quality 0.49, clean-chunk quality 0.94, and the Beat 5 chain 0.85×0.8=0.68→×0.92=0.63
- The four trend-tag categories (consecutive_raise, consecutive_lower, reversal, stable_maintained) as the system's actual terminology
