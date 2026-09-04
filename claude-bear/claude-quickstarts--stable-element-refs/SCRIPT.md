# Stable Reference IDs Survive Viewport Chaos — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a Teardown scaffold). Register: **Plain**.*
*Carry-out written first (CARRY-OUT.md). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (free Remotion, WRITER LAW — no puppet, no
Seedance). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer / stakes+wrong-guess | "You'd think a button's pixel position survives a resize. It doesn't — the window resizes, the pixel goes stale, and your automation misses. So what actually stays put: the pixel, or the ref?" | Writer types "Button at 960, 540 resize same pixel right?", corrects "pixel" → "ref" |
| B01 | 1 stakes / 2 wrong guess / **4 anchor planted** | Say your automation finds a "Confirm Order" button at pixel 960, 540 on a 1920 by 1080 page. The plan: remember that spot, click it again whenever needed. Resize the browser to 1440 by 900, and the page reflows — the button drifts to roughly 720, 405. The remembered pixel now points at empty space. | THE ANCHOR — the button on a 1920×1080 page at (960,540); the page reflows to 1440×900; the same pixel now sits on empty space |
| B02 | 3 mechanism (**ONE FLAG**) | The fix runs before Claude ever looks at the page. A script tags every clickable element with a stable reference id, independent of where it sits on screen. Flagged: the exact tagging method varies tool to tool — this is the general pattern, not one fixed API. Claude targets the id, not a pixel, so the tag travels with the button no matter where the layout puts it. | Code card: `element.setAttribute('data-ref', 'confirm_order_1')`; FLAG marker; source credit |
| B03 | **4 anchor payoff** | Watch it happen: the "Confirm Order" button sits at pixel 960, 540 on the 1920 by 1080 page, tagged with the id confirm_order_1. Resize the window to 1440 by 900 — the button reflows to roughly 720, 405. The pixel changed. The id, confirm_order_1, never did. Claude clicks the id and lands on the button either way. | THE ANCHOR RETURNS — same button, same id label glued to it through the resize; the pixel chip changes, the id chip doesn't |
| B04 | **5 both directions** | This holds for every element tagged before Claude reads the page — resize, reflow, anything that only moves things around. It does not cover elements that appear later: a modal that opens after a click, a list that loads after scroll. Those need their own tagging pass once they exist, or Claude is aiming at nothing. | Split card: "tagged before load" holds through resize; "appears after load" — untagged, struck, captioned "needs its own pass" |
| **BCRY** | **6 carry-out** | A pixel coordinate describes where a button was, once. A ref names the button itself — so it survives every resize the coordinate doesn't. | The sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me: assign stable refs to every clickable element on this page, so my automation survives a resize. Paste that into Claude. Does it tag elements that load in later? Does it guard against duplicate ids? Run it and see. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Stable Reference IDs Survive Viewport Chaos. Liam, in for Bear. | OutroCTA |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B01 states the naive plan (remember the pixel, click it again), then breaks it: resize to 1440×900, the button reflows to (720,405), and the remembered (960,540) lands on empty space |
| Exactly one inference flag | **B02** — the tagging pattern is real, but the exact implementation (attribute name, injection timing, duplicate-id handling) is not pinned to one verified API in this checkout; see SOURCES.md |
| One anchor, planted early, paid off late | B01 → B03 (the "Confirm Order" button, id `confirm_order_1`, at (960,540)/1920×1080 → (720,405)/1440×900) |
| Both failure directions | B04: holds for anything tagged before Claude reads the page; does not cover elements that appear after page load without a fresh tagging pass |
| No design judgment | B02 explains what the fix does and flags the one place it's under-specified; it never rules on whether the tagging approach is well designed |

## Deliberately not claimed

- **No single verified API.** The source's own citation (`browser_tool_utils/`,
  a `browser_element_script.js`-style pattern) is not a file this checkout can
  re-open and quote, unlike the sibling `browser-coordinate-scaling` redo which
  could read `coordinate_scaling.py` directly. B02 states the pattern generically
  and carries the reel's one flag — see SOURCES.md.
- **No fixed reflow formula.** Unlike a uniform browser-chrome resize (a single
  scale ratio), a page reflow can move an element anywhere the layout engine
  decides; the anchor's (720, 405) is illustrative, not derived from a formula.
  That unpredictability is the reason a pixel coordinate can't be trusted after
  a resize, and the reel says so rather than implying a computable relationship.
- **No accusation.** The pixel-coordinate approach is described as brittle for a
  stated reason (reflow moves things unpredictably), never judged as a bad
  design choice — that's Teardown's lane, not Plain's.

## Handoff prompt (BHTF, read aloud)

> "Assign stable refs to every clickable element on this page so my automation
> survives a resize."

This is the source scaffold's own original worked prompt, kept verbatim as the
Your Turn ask per redo law — the question and underlying facts carry over
unchanged even though B01–B04's telling of the mechanism is freshly written for
the Plain register.

---
**GATE P — signed:** unattended build, no human gate for hai-simple (VOICE-LOCK.md: the slate cut IS the review).
