# Week 26 — FACTCHECK

**Film:** *How a Room Changes Music* (working title) · angle in `ANGLE.md`
**Base source:** `claude-for-music/how-music-works-audible`, Nik Bear Brown's review of David Byrne,
*How Music Works* (McSweeney's 2012; expanded edition 2017)
**Checked:** 2026-10-10

Verdicts: **SUPPORTED** (checked against the primary or the author's own words) · **QUALIFY** (true
with a stated condition or wording fix) · **VERIFY-BOOK** (from secondary summaries of the book; must
be checked against the book text before audio) · **CUT** (researched, left out, reason given)

Access note: the LibKey connector was not available in this session. Papers were read from open
repositories (TU Berlin DepositOnce / Vienna Talk proceedings PDF, Europe PMC, the publisher's Pure
record). The Vienna Talk PDF was read in full for this audit.

---

## A. Claims the film makes

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| A1 | *How Music Works* ch. 1, "Creation in Reverse", argues that music is made, consciously or not, to fit the places where it will be heard; the chapter expands Byrne's TED talk on architecture and music | VERIFY-BOOK | Consistent across reviews and summaries (Jack Knowlson ch. 1 summary; Kirkus; Stereophile). Say "argues", never quote the book until checked |
| A2 | Byrne: the church Bach's music was played in was smaller than the Gothic cathedrals before it, and Bach could write busier, more "pointillistic" lines; that material "would just turn into mush in a Gothic cathedral" | SUPPORTED | Byrne, *TED Radio Hour*, NPR, 2020-07-24, "David Byrne: How Do Spaces Shape The Music We Make?" transcript. The quote is verbatim from the transcript |
| A3 | Byrne: Gregorian chant doesn't change key, so in a Gothic cathedral the notes that hang in the air stay in tune and enhance the music | SUPPORTED | Same transcript ("that music doesn't change key … it's still in tune") |
| A4 | CBGB was a small, long, narrow club in New York | SUPPORTED | Same transcript: "kind of long and sort of narrow", "not that large of a place" |
| A5 | In the book Byrne describes CBGB as absorbent with little reverberation, so every detail of the music could be heard | VERIFY-BOOK | Two independent summaries (Knowlson; a ch. 1 review) say this. One summary garbles it as "great acoustics"; the point is **little reverberation**. Check the page |
| A6 | Byrne later played Carnegie Hall and noticed some of the music he'd written didn't sound all that great in halls like that | SUPPORTED | NPR transcript (TED talk excerpt): "didn't sound all that great in some of those halls" |
| A7 | Quantz (1752) described notes blurring in reverberant rooms and advised a slower tempo | QUALIFY | Cited **through** Schärer Kalkandjiev & Weinzierl (2015), §1, ref. [1] (Quantz, *Versuch einer Anweisung die Flöte traversiere zu spielen*, 1752). The film says "Quantz advised", with the paper on screen as the source |
| A8 | The field study: cellist Jean-Guihen Queyras played Bach's six cello suites in **seven** European concert halls; the researchers measured each hall and his tempo | SUPPORTED | Schärer Kalkandjiev, Z. & Weinzierl, S. (2015). "Playing slow in reverberant rooms: Examination of a common concept based on empirical data." *Proc. Third Vienna Talk on Music Acoustics*, pp. 215–219; also *Psychomusicology* 25(3), 195–207, doi:10.1037/pmu0000065 |
| A9 | He slowed down in halls with long reverberation **and also** in halls with short reverberation (a quadratic, U-shaped relation) | SUPPORTED | Vienna Talk paper §4: "significantly reduced his tempo in rooms with long EDT and RT … he also reduced his tempo with low EDT and RT"; quadratic relation for duration measures |
| A10 | One measure of the hall's echo (early decay time, squared term) accounted for **74.36%** of the variation in his tempo | SUPPORTED | Same paper: "the strongest effect on tempo … EDTvlc² with an explained variance of 74.36%". Say "about seventy-four percent", **one cellist, seven halls** |
| A11 | In interviews he said he slows in reverberant halls to avoid a muddled sound, and lengthens pauses | SUPPORTED | Same paper, §4, interview statements |
| A12 | Why he slows in **dry** halls: lengthening notes to make up for the missing decay | QUALIFY | The paper's **hypothesis** ("might be due to the prolongation of notes as a strategy to compensate for the lack of sound decay"), citing other musicians' reports. Not the cellist's own statement. The film must say "the researchers' explanation" |
| A13 | Lab study: 12 musicians, 14 simulated concert halls | SUPPORTED | Same paper, abstract and §3 |
| A14 | In the lab, the hall's reverberation explained only **8.73%** of tempo, even with each musician's individual strategy modelled; strategies were "very individual" | SUPPORTED | Same paper, §4: "the adjustment strategies of the performers were very individual … explained variance of 8.73%" |
| A15 | Lab interviews: almost all musicians lengthen pauses in reverberant rooms, mainly for slow pieces; for fast pieces they focus on clear, short articulation | SUPPORTED | Same paper, §4 (interview paragraph) |
| A16 | Two earlier studies (the Cleveland Orchestra across halls of 1–2.1 s reverberation; a MIDI grand piano in a variable-acoustics room) did not find the simple "more echo, slower" relation | SUPPORTED | Same paper, §1, refs [4], [5]. Cleveland implied a different correlation (with hall quality); the MIDI study found no influence on mean tempo. Say "neither found the simple pattern" |
| A17 | Great tits in noisy parts of Leiden sang with a higher minimum frequency, above mostly low-frequency traffic noise | SUPPORTED | Slabbekoorn, H. & Peet, M. (2003). "Birds sing at a higher pitch in urban noise." *Nature* 424, 267, doi:10.1038/424267a (Europe PMC record verified). Do **not** voice a bird count; it wasn't verified |
| A18 | Byrne's book also argues that recording technology shaped music; it opens that discussion with Edison's cylinders, which had to be re-performed batch after batch | VERIFY-BOOK | Base source (Nik Bear Brown's review, via `beat_sheet.json` B03). Book chapter "Technology Shapes Music" (two parts, analog/digital) per reviews. Check the book's wording on re-performance |
| A19 | Stravinsky was contracted to record his music during his first American tour (1925) and wrote a piano suite, *Serenade in A*, each movement fitting one 78 rpm side, a maximum of about three minutes | SUPPORTED | Boosey & Hawkes work page (Serenade in A, 1925; duration 12'). The label (Brunswick) is from Wikipedia only, so leave it unnamed |
| A20 | Léveillé Gauvin analysed 303 US top-10 singles, 1986–2015; the time before the voice enters fell from more than 20 seconds (mid-1980s average) to about 5 | QUALIFY | Paper: Léveillé Gauvin, H. (2018), *Musicae Scientiae* 22(3), 291–304, doi:10.1177/1029864917698010 (record verified: 303 songs, 1986–2015, "time before vocals enter" is one of five features). The 20 → 5 s figures are from Ohio State's news release (2017), not yet read in the paper. AFP gives 23 s for 1986. Say "more than twenty seconds … about five" and cite both |
| A21 | Léveillé Gauvin, asked about it: "it's just adapting yourself to your environment whether you're aware of it or not" | QUALIFY | AFP interview (2017), carried by Dunya News / Malay Mail. Secondary (wire) but direct quotation. Put it on screen with "AFP, 2017" |
| A22 | His second study (2015 hits vs less popular songs by the same artists) did not support the attention-economy hypotheses | SUPPORTED | Paper record (Pure, ÉTS): 60 vs 60 songs, "data were not consistent" with the hypotheses |

## B. Our own demonstration (label it as ours)

| # | Claim | Verdict | Note |
|---|---|---|---|
| B1 | Cold open: at normal pace in the simulated cathedral, every word is still ringing when the next arrives; slower, with room between the phrases, the echo dies away in the gaps | OURS (measured) | `envelopes/D01.json`, `D02.json`. D01 has **no** gaps. In D02 the room's echo falls **11–14 dB** in each of its three gaps before the next phrase (0.6 s silence). **No intelligibility claim is made.** Whisper small.en heard 0.65 (normal) vs 0.70 (pauses), a negligible difference (`experiment/demo_final.json`, pre-registered rule: did not qualify), so B02 no longer says "most of that got lost". Full history of runs 1–5 in `experiment/demo_grid.py` |
| B2 | The final dry-room reading is the same sentence with no reverb, spoken slower | OURS | Dry = our narration with no impulse response. Not a real room, so never call it a measured hall |
| B3 | Viewer task: a clap that audibly hangs after your hands stop means the room has echo; one that dies right away means it's dry | OURS | A qualitative listening heuristic, labelled "not a measurement" on screen. **No** reverberation-time threshold is stated, so no number needs a source. The task asks what the viewer *did*, not what their room measures |
| B5 | The cathedral echo is a simulated impulse response we generate (`make_ir.py`): exponentially decaying noise, darkening as it decays. Measured T30 **4.7 s** (Schroeder integration in `make_ir.py`); the tail sits at 0.25 of its first level, chosen by Whisper measurement (`experiment/demo_grid.json`) | OURS | Labelled on screen as "Simulated echo: our own impulse response (T30 4.7 s, measured). Not a measured room." Card shorthand: "about a 5-second echo" Narration says "a simulated cathedral" (B01). For scale only, not voiced or shown: York Minster's nave measured about 5.9 s at 31.5 Hz and 7.24 s at 125 Hz (ISO 3382 T30, 2006, seen only in a search snippet, **unverified**, so it is not used on screen or in narration). A 5 s decay is within the range of a large stone church, not a claim about any particular one |
| B4 | The test: if every player answers a room the same way, the room is close to deciding; if they answer differently, it's only asking | OURS (interpretation) | Our reading of A10 vs A14. One cellist, consistent within himself: 74.36%. Twelve players, "very individual": 8.73%. Shown with both figures and labelled "Our test". Not a claim the paper makes |

## C. Researched and left out

| Item | Why |
|---|---|
| CD length set by Beethoven's Ninth (74 min) | Conflicting anecdotes, different people credited. Not needed |
| Violin vibrato spreading with the phonograph (Katz, *Capturing Sound*) | Only secondary summaries read. Keep for a later film, or add once the chapter is read |
| Spotify's 30-second payout threshold | Not checked; the argument doesn't need it |
| African drumming suits open air (Byrne) | Supported by summaries, but the film has enough cases. Easy to add later |
| **A23 (was): measured York Minster impulse response** | **Cut, licence.** OpenAIR's York Minster page is offline (the host serves a suspended-account page, 2026-10-10). The replacement dataset, York Minster Chapter House (Zenodo 4040994; Álvarez-Morales, Lopez & Álvarez-Corbacho 2020, doi:10.3390/acoustics2010003), is listed as CC BY 4.0 on Zenodo, but its own `LICENCE.txt` says **CC BY-NC-SA 4.0**. When the two conflict, the stricter licence governs, and non-commercial rules out a monetised channel. Downloaded (MD5 `ade45f29…` matched Zenodo), licence read, then deleted. Replaced by B5 |
| Anything about mixing, phones, earbuds, loudness, codecs, Auto-Tune | Neighbour boundary: a fellow's audio-engineering series covers this (`ANGLE.md` §6) |

## D. Before audio (blocking)

1. VERIFY-BOOK rows **A1, A5, A18**: check against the book. If a row fails, rewrite the beat.
2. **A20**: read the paper's results table for the intro figures, or keep the Ohio State citation on screen.
3. ~~A23~~: measured IR cut on licence grounds (§C). Simulated echo instead (B5); `make_ir.py` is the record of how it was made.
