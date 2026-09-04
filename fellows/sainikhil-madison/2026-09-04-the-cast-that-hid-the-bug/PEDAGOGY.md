# PEDAGOGY — The Cast That Hid the Bug

Reel: `claude-sai-the-cast-that-hid-the-bug`
Subject: ScoutAI, the "Production hardening" week (commit `6aea97e`)
Host: Sai · Kokoro `am_onyx` · `@HumanitariansAI`

---

## The ONE idea

**A defence against bad input is evidence that something upstream is already
producing bad input.** Scout's tool registry told the model that `days` and
`limit` were strings. Nobody noticed, because both tool functions cast to `int`
on the way in — the defence was absorbing the symptom of its own cause. The
week's real product is not the five fixes; it is the two interfaces
(`ChatBackend`, `ConversationalAgent`) that made finding them cheap.

## Act structure

| Beat | Act | Pattern | Job |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Frames the week as one question: works ≠ production-ready. Three headline results. |
| B01 | WHAT-IT-REACHES | `ClaudeScienceChipGrid` | Orients the viewer in the codebase — six sources, one contract. Sets up "the model only sees schemas." |
| B02 | THE-BUG | `DivergentFates` | The hero beat. Two fates for one annotation: read off the signature (told: string) vs `get_type_hints` (told: integer). |
| B03 | DEPLOY-FORK | `BinaryBranch` | A real fork the author could not design around, plus what actually shipped. |
| B05 | VERDICT | `ClaudeVerdictArtifact` | Four bare sentences. Names the two interfaces as the week's actual asset. |
| B06 | HANDOFF | `ClaudeComposerAsk` | Generalizes the idea into a prompt the viewer runs on their own code. |
| B07 | OUTRO | `ClaudeTitleOutro` | Title restate, handle, sign-off. |

B04 is deliberately absent: the week had no fourth distinct body move, and
padding it would have meant a second ChipGrid. Seven beats, not eight.

## ILLUSTRATE LAW check

- Claude UI appears at **B00, B05, B06, B07** only. ✅
- Body beats are B01, B02, B03 — `ClaudeScienceChipGrid`, `DivergentFates`,
  `BinaryBranch`. Three different patterns, no two consecutive body beats
  sharing one. ✅
- Every body beat carries an ordered `show` block; none would survive as a
  static slide with a voiceover (B02's whole point is the divergence, B03's is
  the fork resolving). ✅

## 9:16 constraint (why these patterns and not the guide's defaults)

The guide's default B01/B02 are `ClaudeScienceLayerStack` and
`ClaudeScienceSourceFlow`. **Neither has a registered `916` sibling**, so a
portrait cut would flag them rather than render. Every pattern in this reel was
chosen because both the landscape composition *and* a `<Pattern>916` sibling are
registered in `Root.tsx` **and** share the same props type — so `shorts.py` can
rewire the sheet and re-render portrait with no prop edits. Verified per pattern
before authoring.

## Evidence / honesty

Every number on screen was measured locally rather than quoted from the README —
`pytest` was actually run (`170 passed in 0.26s`), the Greenhouse board count was
imported live. Dollar estimates from the README are excluded because they are
estimates. Full audit in `SOURCES.md`.

## Human review checklist

- [ ] The ONE idea above is the idea you actually want this week to carry.
- [ ] B02's account of the annotations bug matches your intent (the cast masked it;
      `get_type_hints` fixed it).
- [ ] B03 fairly represents the deployment decision — worker shipped, ping-to-wake
      documented rather than built.
- [ ] "Next week, persistence" (B07) is a commitment you want on record.
- [ ] The B06 handoff prompt is one you would actually tell a viewer to run.
- [ ] No number on screen is one you would not defend. See `SOURCES.md`.
- [ ] Title and sign-off are right: "The Cast That Hid the Bug." / "Sai."

## Signature

Sign below to record that a human reviewed the narration. Claude does not sign
this file. Replace the blank with the single word that means "approved".

VERDICT: PASS   — reviewer: Sai Nikhil Kunapareddy  date: 09-04-2026
