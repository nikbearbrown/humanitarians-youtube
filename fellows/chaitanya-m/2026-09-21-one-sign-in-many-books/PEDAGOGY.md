# GATE P — One Sign-In, Many Books

**Reel:** `claude-hai-one-sign-in-many-books` · ai-explainer · claude palette (fidelity)
**Channel:** claude-hai · @HumanitariansAI · Bella (`af_bella`) · Pragmatist
**Beats:** 14 (B00–B13) · estimated ~3:52 after the trim pass
**Reviewer:** Chaitanya (author)
**Date:** 2026-09-21

> Nothing downstream of this file runs until it reads `VERDICT: PASS`.
> `generate_audio_kokoro.py` refuses without it.

---

## 1. The one idea

**A separate website can let you in without ever knowing you — because the hub hands you a signed ticket, the website calls the hub to check it, and one logout timestamp retires every ticket at once.**

The reel is sized to land that and nothing else. The author's Scene 4 (the logout
timestamp) is designated the payoff and gets three beats — the most of any scene.

## 2. Structure — the mandatory ai-explainer spine, intact

| Beat | Act | Surface |
|---|---|---|
| B00 | ASK | Claude composer, cold open, **ask lands answered** |
| B01–B10 | BODY | concept illustrations (the author's 5 scenes) |
| B11 | VERDICT | Claude artifact page |
| B12 | HANDOFF | Claude composer, "Your turn.", prompt read aloud and discussed |
| B13 | OUTRO | title restate, terracotta period, handle beneath |

The five source scenes map onto the ten body beats as follows. Scenes were **split, never cut** —
splitting is what lets every beat carry one idea. Word counts below are post-trim.

| Source scene | Beats | Words | Trim |
|---|---|---|---|
| 1 · The problem | B01, B02 | 38 + 44 | moderate |
| 2 · The ticket | B03, B04 | 37 + 35 | **hardest — the author's named release valve** |
| 3 · The double-check | B05, B06 | 41 + 45 | moderate |
| **4 · Logging out everywhere (the payoff)** | **B07, B08, B09** | **53 + 54 + 58** | **none — untouched, word for word** |
| 5 · Close | B10 | 52 | light |

## 3. Does each beat teach, or just say?

Every body beat carries a `show` block of ordered visual events keyed to spoken phrases.
The PPT test, beat by beat:

- **B01** the sites physically fan apart with visible gaps — the separateness is *seen* before it is claimed.
- **B02** three denials strike through one per spoken clause; "ticket" then types into the vacuum they leave.
- **B03** three stamps land on the stub on the three spoken items. The access check resolves *before* the stub is drawn — the order of operations is the teaching.
- **B04** the seal presses, a glyph flips, the seal cracks. "Impossible to alter" is demonstrated, not asserted.
- **B05** two columns: the hub has ticket + seal, the textbook has ticket + an empty slot. Two identical stubs arrive and the site cannot sort them.
- **B06** the six checks tick down in the hub's real order. This is the beat where the evidence lives on screen and the voice only reacts.
- **B07** countdowns keep running *after* the logout press — the failure is watched, not described.
- **B08** the list replicates outward and overruns its panel; four cost labels stack.
- **B09** the sprawling list collapses to one field; a cutoff sweeps; everything to its left greys at once while a later ticket stays live.
- **B10** B01's fan reconnects; three mechanism words settle; the list panel fades away.

No two consecutive body beats share a visual scheme. B01 and B10 use the same component in
opposite modes (fan / converge) nine beats apart — a deliberate open/close rhyme, not repetition.

## 4. Register check (Pragmatist)

Same flag as `claude-hai-introduction-to-cells`: hai's usual spine question ("when to use AI and
when NOT to") does not apply — this is a systems explainer, not an AI-tool topic. Pragmatist is
kept as a **delivery tone** (plain, method-first, no hedging) plus the register's mandatory
"where it fails", which is carried honestly and in three places:

- **B08** concedes the revocation list works before pricing it ("That works. It also means…").
- **B10** names what the trick does *not* buy: "The trick doesn't remove the call home — it removes the list."
- **B12** hands the viewer the two real weaknesses — clock skew, and a copied ticket that stays good until it expires or you log out.

The AI-use angle stays confined to the handoff prompt, per house law, rather than being forced
into the body.

## 5. The author's constraints — how each is met

| Constraint | Status |
|---|---|
| Avoid the word "JWT" | Zero instances in narration, on-screen copy, card text, props, or the outro |
| One metaphor, end to end | Ticket only. "Secret" and "seal" are the script's own and belong to the stub; no key, passport, or wristband appears in any `show` block or prop |
| Protect Scene 4 in full | Three beats, the most of any scene; also `--keep`-protected when the 9:16 short is planned |
| Trim Scene 2 first if over | Applied twice: Scene 2 took the deepest cut in the 16:9 trim pass (109 → 72 words), and it is the first beat group offered up if the 9:16 short needs more headroom |
| No real token string on screen | B04 is the only beat showing an identifier: `TCKT-EXAMPLE-0000`, invented, captioned "example — not a real ticket" for the whole beat. No token was captured, pasted, or recorded during the build |
| `auth-debug.txt` never on camera | Never opened, displayed, or referenced. The B06 check list comes from `DEVELOPER.md` §4.2, not from that log |

## 6. Flagged for the reviewer

1. **The requested sign-in line conflicts with the skill's built-in structure — resolved, not silently.**
   COLD OPEN LAW puts B00 on the Claude composer with the greeting `[cue], HAI`; there is no
   presenter-intro slot, and a synthetic voice must not claim to be a named person. Agreed
   resolution (2026-09-21): B00 narrates **"Hi — this is Bella, for Chaitanya."** followed by the
   author's topic clause verbatim, and the Chaitanya credit is restated on the outro — the same
   handling used in `claude-hai-introduction-to-cells`.

2. **Runtime — RESOLVED.** The first draft ran ~5:00. The author asked for 2–4 minutes, so a trim
   pass re-cut every non-protected beat (Scene 2 hardest, Scene 4 not at all) to land ~3:52. Nothing
   was dropped and the voice was not sped up: the lever was word count, beat by beat. The cost, stated
   plainly: several body beats now run 35–45 words, under the 45–70 house budget. All stay well above
   the consolidation floor for their `content_type`.

3. **Nine new Remotion components — BUILT** in `runtime/remotion/src/ClaudeHaiTicketIllu.tsx`
   (`ClaudeHaiHubAndBooks`, `StrangerSite`, `TicketStub`, `TicketSeal`, `SecretAsymmetry`,
   `CallBackChecks`, `TicketsInTheWild`, `RevocationList`, `LogoutTimestamp`), plus three bookend
   wrappers that add the HAI bug without touching the shared Claude scenes. 24 compositions
   registered (each with a `…916` portrait sibling so `shorts.py`'s ONDA CHECK re-lays them out for
   vertical rather than centre-cutting them). All at 1920×1080 / 1080×1920, so `--scale=2` yields
   true 3840×2160 at source.

4. **"Six checks" is new information** relative to the author's script, which says only "runs
   through its checks". It is verified against `DEVELOPER.md` §4.2 and matches the script's own
   source note ("the six things it verifies in order"). It earns its place: it puts the evidence on
   screen and lets the voice stay short.

## 7. Full narration, in order (TRIM PASS — author direction, 2026-09-21)

**B00 · ASK** (37 words) — Hi — this is Bella, for Chaitanya. This video is about how a student signs in once and can open every textbook they're entitled to. Every book is a separate site. None of them has your password.

**B01 · PROBLEM** (38 words) — Start with the shape of it. There's no one big website with all the textbooks inside. Each one is its own site, at its own address, on its own server. And a student should only sign in once.

**B02 · QUESTION** (44 words) — So how does a separate website know who you are, and know you're allowed in? It has never seen you. It doesn't have your password. It has no idea who you are. It needs something it can be handed at the door. A ticket.

**B03 · THE TICKET** (37 words) — When a student clicks a textbook, the hub checks first: should this person be allowed in? If yes, it writes a ticket. Three things — who you are, which one book, and when it expires. Twenty-four hours.

**B04 · THE SEAL** (35 words) — And it's signed — not with a signature you could copy, but with a secret only the hub knows. Change one character and the signature stops matching. Then the ticket is handed to the textbook.

**B05 · THE ASYMMETRY** (41 words) — Here's the surprising part. The textbook doesn't trust that ticket on its own. It can't — it doesn't know the secret, so it can't tell a real signature from a forged one. Holding a ticket and checking one are different powers.

**B06 · THE CALL BACK** (45 words) — So it asks the hub directly: is this ticket real, and is this person allowed in my book? The hub runs six checks in order and answers yes or no. Only then does the textbook let the student in, and remember them for later pages.

**B07 · THE HARD PROBLEM** (53 words)  **[Scene 4 — PROTECTED, unchanged]** — Which leaves one hard problem. What happens when someone logs out? The tickets are already out there. Each one is valid for twenty-four hours, sitting on a site the hub doesn't control. You can't reach into a textbook site and snatch a ticket back. Logging out of the hub, by itself, changes nothing.

**B08 · THE OBVIOUS FIX** (54 words)  **[Scene 4 — PROTECTED, unchanged]** — The obvious fix is a list of cancelled tickets, checked every time. That works. It also means keeping a list, keeping it in sync everywhere, keeping it fast, and keeping it forever. You've traded one hard problem for a permanent one. That is the moment to ask whether the list is necessary at all.

**B09 · THE PAYOFF** (58 words)  **[Scene 4 — PROTECTED, unchanged]** — This system does something simpler. When you log out, it writes down one thing: the time you logged out. After that, any ticket issued before that moment is dead. Not cancelled — just older than your logout, so it no longer counts. One timestamp instead of a list. Every outstanding ticket, everywhere, invalid the instant you log out.

**B10 · CLOSE** (52 words) — So one sign-in reaches many separate sites. A signed ticket good for one book, for one day. A check back to the hub before anyone gets in. And one timestamp that shuts it all down. The trick doesn't remove the call home — it removes the list. Separate websites. One front door.

**B11 · VERDICT** (45 words) — Let's recap with Claude. Each textbook is a separate site; the hub is the only place you sign in. The hub writes a signed ticket — one book, twenty-four hours. The textbook calls the hub before letting anyone in. Logging out retires every older ticket.

**B12 · HANDOFF** (75 words) — Your turn. Take this into Claude: I run a service where one sign-in opens several separate sites I control. Walk me through the ticket approach: what goes in the ticket, what the receiving site must check before trusting it, and how logging out can kill every outstanding ticket without a cancellation list. Then tell me where it breaks. That last line is the one that matters. Ask for the failure cases, not the happy path.

**B13 · OUTRO** (9 words) — One Sign-In, Many Books. For Chaitanya and Humanitarians AI.


**Total:** 623 words · estimated 232s (~3:52) at Bella's measured 2.68 words/sec. Real durations replace this at audio lock.

---

## VERDICT

Reviewed by the author (Chaitanya) on 2026-09-21 against the contact sheet
(`GATE-P-contact-sheet.png` — all ten body beats as real renders, not a text slate)
and the narration above. One change required and applied:

> *"reduce the length of the video to 2-4 min and also make a short video as well
> following the rules"*

Applied as a TRIM PASS, not a re-author: no beat deleted, every visual and every
`show` block preserved, Scene 4 untouched word for word, Scene 2 cut hardest per the
author's own release-valve rule. Runtime target met (see §7).

VERDICT: PASS
