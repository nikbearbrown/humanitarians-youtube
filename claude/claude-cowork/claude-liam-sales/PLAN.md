# PLAN — Claude, Closing (Ch.5: The Sales Plugin)

**Slug:** `claude-liam-sales` · **Channel:** claude-liam (Liam, Kokoro `am_onyx`, free) · **Register:** Teardown
**Source:** `chapters/ch05-sales.txt` · **One idea:** *The sales plugin meets you where you are — not built only for a big SaaS sales org with a Salesforce admin. It researches a prospect from public info, preps you for the conversation, tracks where deals stand, and drafts personalized follow-ups; configured with your process it stops being generic. A research-and-prep accelerator, not a closer — the relationship is still yours.*

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "Do I have to be a salesperson to use it?" → ask lands answered, Liam signs in ("Konnichiwa — this is Liam, in for Bear.")
ACT I    Meets You Where You Are      audience, not just a SaaS sales org         (B01 PredictCard, B02 Manim range, B03 VOX)
ACT II   What It Does                 five capabilities, mechanism by mechanism   (B04 ChipGrid, B05 SourceFlow, B06 Manim accumulate, B07 illustration, B08 Manim sort, B09 spark)
ACT III  A Call, End to End           research → in-room → capture → follow-up    (B10 Onda code, B11 Manim assemble, B12–B13 VOX run R1, B14 Manim threshold)
ACT IV   Keeping the Pipeline Honest  pipeline review · prospecting · outreach    (B15 Manim sort, B16 SourceFlow, B17 illustration, B18 VOX drawon)
ACT V    Configured, Not Generic      install → tell it 3 things → CRM optional   (B19 ChipGrid, B20 Manim threshold)
ACT VI   Prep, Not a Closer           wins · admin · be present · keep data fresh (B21 Manim accumulate, B22 VOX, B23 ChipGrid, B24 VOX)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (+0.5s lead)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — prompt read aloud + discussed
O01  OUTRO     ClaudeTitleOutro — title re-read "Claude, Closing. Liam, in for Bear."
```

## Lane histogram (body beats only; bookends B00/V01/H01/O01 exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 6 | 20.0% | 20–25% | ✓ (B03, B12, B13, B18, B22, B24) |
| MANIM | 8 | 26.7% | 25–40% | ✓ |
| REMOTION | 9 | 30.0% | 30–45% | ✓ |
| CARD | 7 | 23.3% | remainder | ✓ (6 segment cards + 1 spark B09) |

Body beats: **30** · Est. runtime ≈ 5:00 (measured audio is the only clock).
Adjacency check: no run of >2 same-lane beats except inside vox run R1 (by contract). Two-REMOTION pairs (B04–B05, B16–B17) are legal (≤2).

## Vox runs
- **R1 (B12→B13):** "in the room" → "capture it fresh." One continuous camera move across the same meeting table — push toward the two people (B12), then continue to the same person alone after the call (B13). Handoff block authored on B12 (camera x0.45/y0.5/scale1.7; table object pinned). Two beats, never crosses the Act III boundary. Max-length rule satisfied.
- All other VOX beats (B03, B18, B22, B24) are standalone — hard cuts, no continuity chain.

## VOX stills (all Tier 1 illustrative — no real people, no logos, no rights escalation)
- **B03** solo worker at a home table, scattered notes — "the you."
- **B12** two people talking across a meeting table (R1 head).
- **B13** same person alone afterward, typing notes (R1 tail).
- **B18** empty manager's chair beside a working desk; terracotta ring drawn on at previz (`drawon`).
- **B22** warm handshake / eye contact across a table — "be present."
- **B24** hand jotting in a notebook beside a laptop — "keep it current."

## Datable facts STRIPPED / corrected (per whole-book FACTCHECK.md + DOUBLE-CHECK LAW)
- **"a 50% sales team … sales force administrator"** → **"a SaaS sales team with a Salesforce admin"** (transcription artifact; Salesforce kept only as a *fleeting* example of the big-org persona, never the beat's subject).
- **"Cloud" → "Claude"** throughout (speech-to-text artifact).
- **"HubSpot's free tier"** → **"a CRM — even a free one, or a spreadsheet"** (named third-party tool + price detail genericized; CRM is the mechanism, brand would date).
- **"$30,000 budget"** (the Meridian follow-up example) → dropped; follow-up described by *mechanism* (hits every point, suggests next step), not a dollar figure. No prices anywhere.
- **No plugin counts, no prices, no platform lists** on screen or in narration. "Five kinds of help" describes *this plugin's own* functions (not a catalog roster), so it stays.
- Meridian Design Studio / discovery-call scenario kept as the source's fictional worked example (illustrative, not a datable fact).

## Gates
1. Plan (this doc) — **approve**.
2. Factcheck — inherits whole-book FACTCHECK.md; per-reel corrections logged in SOURCES.md.
3. **GATE P** — narration reviewed on an animated slate before any audio spend. Kokoro `am_onyx`, free. No ElevenLabs.
4. Audio lock (Kokoro) → align → **Gate D2** SHOPPING.md (vox stills, from LOCKED durations) → **Gate D1** slate previz → pantry fill → review cut → VISUAL QC → `art final`.
