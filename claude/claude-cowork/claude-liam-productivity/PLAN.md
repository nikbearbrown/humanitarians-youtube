# PLAN — Claude, In Order (Ch.3: The Productivity Plugin)

**Slug:** `claude-liam-productivity` · **Channel:** claude-liam (Kore, Kokoro `af_kore`, free) · **Register:** Teardown
**Source:** `chapters/ch03-productivity.txt` · **One idea:** *The productivity plugin is the generalist of the collection — it specializes in YOU (task tracking, meeting prep, email triage, note synthesis), works immediately out of the box with no connections, gets sharper the more Claude knows about how you work, and is the foundation layer most people keep on permanently under their domain plugins.*

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "Which plugin should I turn on first?" → ask lands answered ("The productivity plugin"), Kore signs in
ACT I    The Generalist        others pick a domain; this picks you        (C01, B01 PredictCard, B02 Manim divergence, B03 orbits illustration)
ACT II   What It Does          the five moves + the one caution            (C02, B04 ChipGrid, B05 talk→structured, B06 VOX note-synthesis, B07 spark)
ACT III  Out of the Box        zero setup; calendar is optional            (C03, B08 install→live, B09 Manim threshold, B10 connect-flow)
ACT IV   The Workflows         morning brief · meeting prep · triage · capture (C04, B11 VOX morning, B12 Onda prompt, B13 Manim accumulate, B14–B15 VOX run R1, B16 Manim triage, B17 VOX capture)
ACT V    It Learns You         adopts your method; compounds; global instr.  (C05, B18 Manim branch, B19 Manim accumulate, B20 Onda global-instructions)
ACT VI   The Foundation Layer  base under the specialists; never turned off  (C06, B21 LayerStack, B22 Manim base-holds, B23 VOX tidy-desk, B24 Manim operating-system)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (+0.5s lead)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — first-person multi-part prompt read aloud + discussed
O01  OUTRO     ClaudeTitleOutro — title re-read "Claude, In Order." + "Kore, in for Humanitarians AI."
```

Acts are 4–8 beats each (Act IV is the 8-beat max, the workflow act the reel exists for). Every act opens with a Title-Case SegmentCard.

## Lane histogram (body beats only; B00 / V01 / H01 / O01 exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 6 | 20.0% | 20–25% | ✓ (B06, B11, B14, B15, B17, B23) |
| MANIM | 8 | 26.7% | 25–40% | ✓ (B02, B09, B13, B16, B18, B19, B22, B24) |
| REMOTION | 9 | 30.0% | 30–45% | ✓ (B01, B03, B04, B05, B08, B10, B12, B20, B21) |
| CARD | 7 | 23.3% | remainder | 6 SegmentCards + 1 SparkBeat (B07) |

**Body beats: 30** · Bookends: 4 (B00, V01, H01, O01) · Est. runtime ≈ 5:40–6:00 (measured audio is the only clock).
Consecutive-lane check: no run of >2 same-lane beats (the REM pair B04–B05 and MANIM pair B18–B19 are exactly 2; the VOX pair B14–B15 is the sanctioned vox run). PASS.

## Vox runs (the ONLY frame-continuity chains; hard cuts everywhere else)

- **R1 (B14 → B15):** "prep before the room" → "walk in ready." One continuous camera move across a single room — a person reviewing a briefing at a desk (B14) rises and steps toward the meeting-room doorway (B15). Handoff block authored on B14 (camera + `prepper` object); B15 is the run's last beat (no handoff). Never crosses the Act IV boundary; length 2 (≤3).

Other VOX beats (B06, B11, B17, B23) are standalone — hard cut in, hard cut out, no continuity contract.

## VOX pantry stills (all Tier 1 illustrative — no rights escalation, no real people/logos)

| Beat | Subject | Motion |
|---|---|---|
| B06 | desk of scattered notes gathering into one stack (note synthesis) | kenburns |
| B11 | person opening a laptop in early morning light, coffee (the morning) | kenburns |
| B14 | person reviewing a one-page briefing before a meeting (run R1) | kenburns |
| B15 | same person entering a meeting room, briefing in hand (run R1) | kenburns |
| B17 | a hand jotting a note beside a screen mid-task (capture) | drawon (terracotta ring) |
| B23 | a tidy, ordered workspace at the start of a day (the always-on base) | kenburns |

## Datable facts STRIPPED / compressed (DOUBLE-CHECK LAW; see book FACTCHECK.md; log in SOURCES.md)

- **Calendar platform list** ("Google Calendar, Outlook, Apple Calendar") → "your calendar." No vendor list on screen or in narration.
- **"Gmail connector"** → "your inbox" / "an email connector." Named third-party tool never becomes the beat's subject.
- **No counts on screen.** The email-triage Manim (B16) shows lanes (Today · Later · Archive), never "40 unread." The "45 minutes → 10 minutes" and "five minutes on Friday" numbers stay in *spoken* narration as clearly illustrative examples only — never rendered as on-screen data.
- **No prices, no plugin count, no platform list** anywhere on screen.
- **Transcription fixes** carried from the source: "general list" → "generalist"; "co-work / co-works" → "Cowork" (one word); "This is in a replacement" → "this isn't a replacement"; any "Cloud" → "Claude."
- Eisenhower / urgency-importance matrix (B18) is a **public, evergreen** prioritization framework named in the source as a user's own method — kept, framed as an example of "tell it how you work," not a dating risk.

## Gates

1. **Plan** (this doc) — approve the act map + lane histogram + vox run.
2. **Factcheck** — inherits book-level FACTCHECK.md; per-reel corrections in SOURCES.md.
3. **GATE P** — full narration (B00 → O01) reviewed on an animated slate before ANY audio spend. Channel claude-liam (Kokoro `af_kore`, free — no ElevenLabs).
4. **Audio lock** (Kokoro) → align (word clock).
5. **Gate D2** — tier-0 library pass (`pantry_search.py` per vox still), then write `SHOPPING.md` from LOCKED durations (6 VOX stills, all Tier 1).
6. **Gate D1 previz** — full-length compile, slates in vox slots, Manim/Remotion rendered for real, `--review` burn-in.
7. **Pantry fill → review cut** (only changed slots recompile; set `shot.focus` per still).
8. **VISUAL QC LAW** pass → `art final`. Never publishes.
