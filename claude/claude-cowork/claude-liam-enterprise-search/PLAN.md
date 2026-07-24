# PLAN — Claude, Finding It (Ch.8: The Enterprise Search Plugin)

**Slug:** `claude-liam-enterprise-search` · **Channel:** claude-liam (Liam, Kokoro `am_onyx`, free) · **Register:** Teardown
**Source:** `chapters/ch08-enterprise-search.txt` · **One idea:** *In a bigger org the answer usually already exists — buried in someone's doc, deck, or thread; enterprise search connects Claude across your sources so it retrieves what the company already knows, bounded strictly by your existing access permissions.*

**Who it's FOR (framing).** The chapter opens by waving off the intimidating name — this is not a Fortune-500-only tool — but its value *compounds when knowledge is scattered across many tools and many people*. So the reel is pitched at teams and orgs where the answer lives in someone else's doc, a deck you weren't on, a thread three teams over. The mechanism is universal; the payoff scales with the org. Mechanism-then-judgment throughout: each Manim states the mechanism, the vox stills land the human feel, and the honest limit (bounded by your access) gets its own act.

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "My company already wrote this down. Can Claude find it?" → ask lands answered ("Yes — bounded by your own access"), Liam signs in "Merhaba… in for Bear."
ACT I    The Buried Answer            it exists, you can't reach it; in a bigger org it isn't even your doc   (B01 PredictCard, B02 Manim scatter, B03 VOX office)
ACT II   Content, Not Filename        search inside documents, across every source at once, in plain language (B04 Manim filename-vs-content, B05 illustration, B06 SourceFlow, B07 Onda code)
ACT III  Graveyard to Living Memory   archive → living resource; context injection grounds Claude in your data (B08 Manim graveyard, B09 illustration inject, B10 Manim grounded-vs-generic)
ACT IV   What You'd Actually Ask      five plain workflows; client-context assembled live                    (B11 ChipGrid, B12 Onda code, B13–B14 VOX run R1, B15 Onda code, B16 Manim accumulate, B17 VOX drawon)
ACT V    Bounded by Your Access       searches only what you can already see; connect-then-index             (B18 Manim boundary, B19 Manim connect+index, B20 VOX drawon)
ACT VI   Build the Habit              name clearly, point it, synthesize, document; synthesis beats search    (B21 ChipGrid, B22 Manim synthesis, B23 VOX note)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (+0.5s lead silence)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — prompt read aloud + discussed
O01  OUTRO     ClaudeTitleOutro — title re-read "Claude, Finding It. Liam, in for Bear."
```

## Lane histogram (body beats only; bookends B00/V01/H01/O01 exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 6 | 20.7% | 20–25% | ✓ in band |
| MANIM | 8 | 27.6% | 25–40% | ✓ |
| REMOTION | 9 | 31.0% | 30–45% | ✓ |
| CARD | 6 | 20.7% | remainder | 6 segment cards (one per act) |

Body beats: **29** · No >2 consecutive same-lane run except inside the vox run (allowed). Est. runtime ≈ 5:30 (measured audio is the only clock).

## Vox runs
- **R1 (B13→B14):** "the dormant client thread reopens" → "the briefing, assembled." One continuous pull-back across the same desk — zoom from the single email out to the full spread. `vox_run: R1` + `handoff` blocks authored in the sheet. Max-3 honored (2 beats); does not cross an act boundary (both in ACT IV).
- Standalone vox (hard cuts, no continuity): **B03** (open office), **B17** (two proposals compared, drawon), **B20** (badge/access boundary, drawon), **B23** (jotting a note into the archive).
- All six vox stills are **Tier 1 illustrative** (no real people, logos, or legible names) — no rights escalation.

## Datable facts STRIPPED (DOUBLE-CHECK LAW; per whole-book FACTCHECK.md)
- **No platform lists on screen or in narration.** Source enumerates "Google Drive, Notion, Confluence, SharePoint, Dropbox, Local File systems" — compressed to generic categories ("your drive, your wiki, your shared folders, your chat"). Product names date the reel and the roster shifts.
- **No counts, no prices, no plugin roster.** "Five workflows" / "four habits" are structural framing (like the gold's "four components"), not datable product facts.
- **"Cloud" → "Claude"** transcription fix applied (source: "connects cloud to wherever your documents live", "cloud finds the answer"). Logged in SOURCES.md.
- **Named third-party tools as fleeting examples only.** Stripe/PayPal survive once (B12) as the book's canonical *documented-decision* example — content of a user's hypothetical question, never the beat's subject or a claim about connectors. B23 keeps it generic ("the vendor with lower international fees").
- **Bounded-by-access is KEPT and elevated to its own act** — verified evergreen (plugins operate within existing credentials/permissions; whole-book FACTCHECK row 7 / Ch.1 SOURCES).

## Gates
1. Plan (this doc) — **approve**.
2. Factcheck — inherits whole-book FACTCHECK.md; per-reel corrections in SOURCES.md.
3. **GATE P** — narration reviewed on animated slate before any audio spend. Kokoro am_onyx, free. No ElevenLabs.
4. Audio lock (Kokoro) → align (word clock).
5. **Gate D2** — tier-0 library pass (`pantry_search.py` per vox still) → write SHOPPING.md from LOCKED durations (six Tier-1 entries: B03, B13, B14, B17, B20, B23).
6. **Gate D1 previz** — full-length SLATE PREVIZ (`art run`), slates in vox slots, Manim/Remotion real, `--review` burn-in. Watch for pacing; source the stills.
7. Pantry fill → review cut → VISUAL QC LAW pass → `art final`. Never publishes.
