# BUILD-PROMPT — Session, Karaoke & Audiogram

Video for the "Brutalist — Claude for Video Production" playlist on @NikBearBrown.
Teaches THREE voice-layer tools in one arc, with Lord Byron threaded through as
the worked example — excerpts of the session-directed reading of *She Walks in
Beauty* (1814, public domain; the performance is the channel's own Suno
generation, youtube/she-walks-in-beauty/pantry/) appearing "here and there":
the poem opens a section, the tools work on it, the poem closes it.

Standing rules #1–#4 (EXAMPLES-CAMPAIGN.md) apply. Read first:
- skills/make/session/SKILL.md              (session notes — direct the reading)
- runtime/scripts/align.py docstring        (the word clock — karaoke timing)
- skills/make/lyric-overlay/SKILL.md        (karaoke lyrics + audiogram overlay)

## The arc (draft the sheet from this; the skill decides final beat count)

1. HOOK — a stanza of the Byron reading plays over a bare audiogram. "That's
   not a voice actor. That's a directed reading — and the direction is text."
2. SESSION — the [spoken word] era and its failure (Suno sings your sentence);
   session notes as the fix: style-box global setup + [spoken word — delivery]
   above every section + THE BREATH RULE. Show the actual she-walks-in-beauty
   session direction on screen (Onda code beat).
3. KARAOKE — the word clock: the text is KNOWN, so align.py never transcribes
   blind — faster-whisper timing + SequenceMatcher = every word on its spoken
   moment (mp3/words.json). Byron again: words landing on the reading.
4. AUDIOGRAM — lyric-overlay decorates a FINISHED video: karaoke layer +
   waveform, never a re-render. Show the overlay landing on the Byron clip.
5. THE RESTRAINT BEAT — karaoke-as-CC (voxlit's law): on a poem, burned-in
   words compete with the listening; on a promo audiogram they ARE the visual.
   You choose per surface. The machine syncs every word; you decide what the
   viewer reads.
6. CLOSE — the three tools as one sentence: session directs the voice,
   karaoke clocks the words, audiogram makes sound visible. CTA.

## Build

- Voice the narration via the Suno path (dogfood: ./art suno → style +
  directed lyrics → human generates → pantry stem → ./art suno-slice).
  GATE P first (PEDAGOGY.md, VERDICT: PASS).
- Byron excerpts: cut short clips from the mastered wav in
  youtube/she-walks-in-beauty/pantry/ (≤15s each, 3–4 placements). Run
  align.py on the excerpt text for the karaoke demonstration; build one real
  audiogram+karaoke overlay via lyric-overlay for the demo beats.
- Onda terminal/code beats for the commands; manim for the word-clock and
  restraint diagrams; hero on beat 5's split. Render per rules #3/#4,
  ./art run, QC BY LOOKING, gate for human review, ./art final (master staged
  AFTER final), captions, publish unlisted to Brutalist (next chapter_number)
  after approval. Log to PUBLISH-LOG.md + CAMPAIGN-FEEDBACK.md.
