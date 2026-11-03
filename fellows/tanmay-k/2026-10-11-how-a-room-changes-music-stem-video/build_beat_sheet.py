#!/usr/bin/env python3
"""Writes beat_sheet.json for the Week 26 topic video: THE VOICE CHANGES ROOMS (draft 1).

Source: claude-for-music/how-music-works-audible (Nik Bear Brown's review of David Byrne's
How Music Works). Angle in ANGLE.md, every factual line cites a FACTCHECK.md row (A1-A22, B1-B5).

The film's structure is its own sound. The cold open plays one sentence inside a measured
cathedral impulse response, then slower; the ending replays it in two rooms like the ones the
cellist slowed down in. DEMO beats carry `audio_fx` (impulse response + Kokoro speed), applied by a
local room_voice.py (planned) after generate_audio_kokoro.py, because that script only takes one
global --speed. The toolkit itself is not modified.

Edit this script, not the JSON. Every Remotion prop is set explicitly (PLAYBOOK §2/§10).
RoomVoice, HallTempo and AskAnswer are NEW components, specified here and built in the
component phase (see BEATS-DRAFT.md → Components).
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
VOICE = "am_onyx"
TITLE = "How a Room Changes Music: One Cellist, Seven Concert Halls"
SIGNOFF = "Tanmay Kulkarni, in for Humanitarians AI"
WPS = 3.3  # planning rate (W23–W25 am_onyx). Measured Kokoro audio replaces it
MP3 = HERE / "mp3"
MEASURED = json.loads((MP3 / "timings.json").read_text()) if (MP3 / "timings.json").exists() else {}
sys.path.insert(0, str(HERE))
from cue_align import spoken_at  # noqa: E402  (copied from W25: pause-anchored cue clock)

SENTENCE = "Every room you play in is asking you a question."
# D02/D03 delivery: these phrases at speed 1.0, joined by 0.6 s of silence (experiment/demo_final.json)
PHRASES = ["Every room", "you play in", "is asking you", "a question."]

SRC_BYRNE_NPR = "David Byrne, TED Radio Hour, NPR, 24 July 2020"
SRC_BYRNE_BOOK = "David Byrne, How Music Works (2012), ch. 1 “Creation in Reverse”"
SRC_SKW = ("Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, "
           "pp. 215–219 · Psychomusicology 25(3)")
SRC_IR = "Simulated echo: our own impulse response (T30 4.7 s, measured). Not a measured room."
SRC_BIRDS = "Slabbekoorn & Peet (2003), Nature 424:267"
SRC_STRAV = "Boosey & Hawkes, Stravinsky: Serenade in A (1925)"
SRC_LG = ("Léveillé Gauvin (2018), Musicae Scientiae 22(3) · figures: Ohio State news, 2017")

IR_MINSTER = "ir/simulated-cathedral.wav"   # made by make_ir.py (FACTCHECK B5); measured IR cut (A23)


# ── shot helpers ─────────────────────────────────────────────────────────────────────────
def room_voice(heading, room, rt_label, passes, caption, source, caption_cue=None, active_cue=None):
    """RoomVoice (NEW): the sentence drawn as its own waveform with the room's decay tail smeared
    after every word. passes: [{"label", "speed", "ir"}] stacked vertically, newest on its cue.
    The envelope is drawn from the rendered DEMO audio (no invented shapes)."""
    return {"type": "GRAPHIC", "status": "PROPS SET (component planned)", "motion": "illustrate",
            "remotion": {"pattern": "RoomVoice", "props": {
                "heading": heading, "roomLabel": room, "rtLabel": rt_label, "sentence": SENTENCE,
                "passes": passes, "envelopeFrom": "mp3 of the DEMO beats (room_voice.py output)",
                "caption": caption, "source": source,
                "captionAtCue": caption_cue, "activeAtCue": active_cue}}}


def hall_tempo(heading, show_dry, stat, caption, source, dry_cue=None, stat_cue=None):
    """HallTempo (NEW): x = how much echo the hall has, y = his tempo. Drawn as a SCHEMATIC curve
    with no data points, because the paper reports a fitted quadratic, not per-hall values
    (FACTCHECK A9). The 'shape only' label is a prop and must always render."""
    return {"type": "GRAPHIC", "status": "PROPS SET (component planned)", "motion": "illustrate",
            "remotion": {"pattern": "HallTempo", "props": {
                "heading": heading, "xLabel": "how much echo the hall has",
                "yLabel": "his tempo", "leftLabel": "driest halls", "rightLabel": "most echoing halls",
                "showWetSide": True, "showDrySide": show_dry, "drySideAtCue": dry_cue,
                "schematicNote": "Shape only. The paper reports a fitted curve, not these points.",
                "stat": stat, "statAtCue": stat_cue, "caption": caption, "source": source}}}


def ask_answer(heading, asks, hears, answers, source, answers_cue=None, rule="", evidence=()):
    """AskAnswer (NEW): the film's one framework, three stations top to bottom (9:16-safe):
    THE ROOM ASKS → A PLAYER HEARS → THE ANSWER. Not numbered, not accumulated beat to beat.
    rule: the test's decide/ask line (B13 only, else ""). evidence: the case's sourced lines
    (numbers, quotes) under the stations, so moving a card's facts here never drops them."""
    return {"type": "GRAPHIC", "status": "PROPS SET (component planned)", "motion": "illustrate",
            "remotion": {"pattern": "AskAnswer", "props": {
                "heading": heading, "asksLabel": "the room asks", "hearsLabel": "a player hears",
                "answersLabel": "the answer", "asks": asks, "hears": hears, "answers": answers,
                "answersAtCue": answers_cue, "rule": rule, "evidence": list(evidence),
                "source": source}}}


def card(title, heading, lines, source):
    return {"type": "GRAPHIC", "status": "PROPS SET", "motion": "illustrate", "remotion": {
        "pattern": "ClaudeArtifactCardFull",
        "props": {"chrome": "artifact", "artifactTitle": title, "artifactHeading": heading,
                  "artifactLines": lines, "sparkLine": source}}}


BEATS = []


def beat(bid, act, tone, text, shot, refs, audio_fx=None, hold_after=None):
    # hold_after: seconds of held frame + silence after the beat (pacing_pass.py), for the viewer task
    BEATS.append((bid, act, tone, text, shot, refs, audio_fx, hold_after))


# ── COLD OPEN: the sentence in the cathedral ─────────────────────────────────────────────
beat("B01", "LISTEN", "quiet, inviting",
     "Listen to one sentence, inside a simulated cathedral.",
     room_voice("One sentence, one cathedral", "Simulated cathedral", "about a 5-second echo",
                [], "Listen.", SRC_IR),
     ["B5"])

beat("D01", "DEMO", "(the sentence, normal pace, in the cathedral)",
     SENTENCE,
     room_voice("One sentence, one cathedral", "Simulated cathedral", "about a 5-second echo",
                [{"label": "normal pace", "speed": 1.0, "ir": IR_MINSTER}],
                "", SRC_IR, active_cue="Every room"),
     ["B1", "B5"], audio_fx={"ir": IR_MINSTER, "speed": 1.0, "wet": 1.0})

beat("B02", "LOST", "curious, a little amused",
     "Hear that? Every word is still ringing when the next one arrives. Same sentence, same "
     "cathedral. This time, slower, with room between the phrases.",
     room_voice("Same sentence, same cathedral", "Simulated cathedral", "about a 5-second echo",
                [{"label": "normal pace", "speed": 1.0, "ir": IR_MINSTER}],
                "Each word still ringing when the next arrives.", SRC_IR,
                caption_cue="Every word is still ringing"),
     ["B1"])

beat("D02", "DEMO", "(the sentence, with pauses, in the cathedral)",
     SENTENCE,
     room_voice("Same sentence, same cathedral", "Simulated cathedral", "about a 5-second echo",
                [{"label": "normal pace", "speed": 1.0, "ir": IR_MINSTER},
                 {"label": "room between the phrases", "speed": 1.0, "ir": IR_MINSTER}],
                "", SRC_IR, active_cue="Every room"),
     ["B1", "B5"], audio_fx={"ir": IR_MINSTER, "speed": 1.0, "pause_s": 0.6, "phrases": PHRASES, "wet": 1.0})

beat("B03", "THE SPEAKER CHANGED", "pleased, then direct",
     "Nobody touched the cathedral. The speaker changed. Hold on to that, because it's the whole "
     "video.",
     room_voice("Nobody touched the cathedral", "Simulated cathedral", "about a 5-second echo",
                [{"label": "normal pace", "speed": 1.0, "ir": IR_MINSTER},
                 {"label": "room between the phrases", "speed": 1.0, "ir": IR_MINSTER}],
                "The room stayed the same. The speaker changed.", SRC_IR + " · our demonstration",
                caption_cue="The speaker changed"),
     ["B1"])

# ── PRESENTER + SUBJECT IN PLAIN WORDS (PLAYBOOK §1c) + the one framework ─────────────────
beat("B04", "THE PLAN", "warm, clear",
     "Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This video is about a book: How Music "
     "Works, by David Byrne, the singer from Talking Heads. Its big idea is that music is shaped "
     "by the room it's played in. I wanted to know how that shaping actually happens, so I went "
     "looking for people who measured it. Here's what I found. The room doesn't write the music. "
     "It asks a question. A player hears it, and answers. And different players answer the same "
     "room in different ways.",
     ask_answer("How a room shapes music", "too much echo, too little, too much noise",
                "the player, every night", "slower, shorter, higher, sparser",
                SRC_BYRNE_BOOK + " · the research in this video", answers_cue="A player hears it"),
     ["A1"])

# ── BYRNE'S CLAIM, in his own words ───────────────────────────────────────────────────────
beat("B05", "BYRNE'S CLAIM", "storytelling",
     "In the book's first chapter, Byrne argues that music gets made, knowingly or not, to fit the "
     "places it'll be heard. On the radio he gave the clearest example I've found. Bach's church was "
     "smaller than the Gothic cathedrals before it, so Bach could write fast, busy lines. All of "
     "that, Byrne said, would just turn into mush in a Gothic cathedral. And the chant that came "
     "before barely changes key. So in a huge stone room, every note left hanging in the air is "
     "still in tune.",
     card("Byrne on churches and chant", "“would just turn into mush in a Gothic cathedral”",
          ["Bach's church: smaller than the Gothic cathedrals before it → fast, busy lines",
           "Gregorian chant: barely changes key → the hanging notes stay in tune",
           "The book: music is made, knowingly or not, to fit where it will be heard"],
          SRC_BYRNE_NPR + " · " + SRC_BYRNE_BOOK),
     ["A1", "A2", "A3"])

beat("B06", "CBGB", "fond, specific",
     "His own band is his best example. CBGB, in New York, was a small, long, narrow club. In the "
     "book he describes a room with very little echo, where every detail of a song came through. "
     "Later, Talking Heads played Carnegie Hall. And Byrne noticed that some of the songs he'd "
     "written didn't sound all that great in halls like that.",
     card("CBGB and Carnegie Hall", "A small, dry club, then a grand hall",
          ["CBGB: “kind of long and sort of narrow”, “not that large of a place”",
           "The book: very little echo, so every detail came through",
           "Carnegie Hall and halls like it: the songs “didn't sound all that great”"],
          SRC_BYRNE_NPR + " · " + SRC_BYRNE_BOOK),
     ["A4", "A5", "A6"])

# ── ONE PLAYER, ONE EVENING ───────────────────────────────────────────────────────────────
beat("B07", "THE OLD ADVICE", "thoughtful",
     "That's composers adjusting over centuries. But if Byrne is right, it should show up in a "
     "single player on a single night. Musicians have said so for a long time. In seventeen "
     "fifty-two, the flautist Johann Joachim Quantz told players to slow down in echoing rooms, so "
     "the notes don't blur together. Which is exactly what I did with that sentence.",
     card("Quantz, 1752", "Slow down in echoing rooms",
          ["Played fast in a reverberant room, notes blur into each other",
           "His advice: take a slower tempo"],
          "J. J. Quantz, Versuch einer Anweisung die Flöte traversiere zu spielen (1752), "
          "as cited in " + SRC_SKW),
     ["A7"])

beat("B08", "SEVEN HALLS", "investigative, building",
     "And then someone actually checked. Two researchers in Berlin recorded the cellist Jean-Guihen "
     "Queyras playing all six of Bach's cello suites in seven European concert halls. They "
     "measured how much each hall echoed, and how fast he played every movement. In the most "
     "echoing halls, he slowed down. Quantz would have nodded.",
     hall_tempo("One cellist, seven halls", False, "",
                "Most echoing halls → he played slower.", SRC_SKW),
     ["A8", "A9"])

beat("B09", "THE DRIEST HALL", "surprised",
     "Then the part that made me stop. In the driest halls, the ones with almost no echo, he slowed "
     "down too. Too much echo, slower. Too little echo, also slower. And one measure of the hall's "
     "echo accounted for about seventy-four percent of how his tempo moved. That's one player in "
     "seven rooms. But it's a strong pattern.",
     hall_tempo("He slowed down at both ends", True, "74% of his tempo variation",
                "Driest halls → also slower. One cellist, seven halls.", SRC_SKW,
                dry_cue="In the driest halls", stat_cue="seventy-four percent"),
     ["A9", "A10"])

beat("B10", "WHY BOTH ENDS", "pulling back, careful",
     "So why slow down in a dry room? He told them that in echoing halls he slows down to avoid a "
     "muddy sound, and lets the pauses run longer. For the dry halls, the explanation is the "
     "researchers' own. With no echo to carry a note, a player may hold notes longer, to make up for "
     "sound that isn't there. That's their reading, not his words. But look at what it means. The "
     "same answer, slower, to two opposite questions.",
     card("Why both ends", "Same answer, two opposite questions",
          ["Echoing hall (his words): slow down to avoid mud, let the pauses run longer",
           "Dry hall (the researchers' explanation): hold notes longer, to replace the missing decay"],
          SRC_SKW + ", interviews and discussion"),
     ["A11", "A12"])

# ── FRICTION: the same question, different answers ───────────────────────────────────────
beat("B11", "TWELVE PLAYERS", "curious, then quietly delighted",
     "So the same team tried it on more people. Twelve musicians, fourteen simulated concert halls. "
     "And here, the hall's echo explained under nine percent of their tempo, even after allowing "
     "for each player's own habits. The paper calls their strategies very individual. Almost all of "
     "them said they lengthen pauses in echoing rooms, but mostly in slow pieces. In fast pieces, "
     "they kept the notes short and clean instead.",
     card("Twelve musicians, fourteen simulated halls", "The same question. Different answers.",
          ["The hall's reverberation explained 8.73% of tempo (one cellist, real halls: 74.36%)",
           "Strategies: “very individual”",
           "Slow pieces: longer pauses · fast pieces: short, clear notes"],
          SRC_SKW + ", lab study"),
     ["A13", "A14", "A15"])

beat("B12", "NO SIMPLE RULE", "fair, measured",
     "And to be fair to the simpler story, two earlier studies looked for it. One used the Cleveland "
     "Orchestra, the other a grand piano in a room with adjustable echo. Neither found the simple "
     "pattern: more echo, slower playing. That fits. The room doesn't set the tempo. It sets a problem, and each "
     "player solves it their own way.",
     card("Two earlier studies", "Neither found “more echo, slower playing”",
          ["Cleveland Orchestra, halls of 1 to 2.1 s reverberation: not the expected pattern",
           "MIDI grand piano, variable-acoustics room: no effect on mean tempo",
           "The room sets a problem. Each player solves it their own way."],
          SRC_SKW + ", §1 (refs 4–5)"),
     ["A16", "A14"])

beat("B13", "THE TEST", "clear, confident",
     "So here's a way to listen for this anywhere. When a place seems to have shaped some music, "
     "listen for what the room takes away, who's hearing it, and what they changed to get it back. "
     "Then the test. If every player answers the same way, the room is close to "
     "deciding. If they answer differently, it's only asking.",
     ask_answer("Listen for it anywhere", "what the room takes away", "who's hearing it",
                "what they changed to get it back",
                "Our test, from " + SRC_SKW + " (one cellist 74.36% · twelve players 8.73%)",
                answers_cue="what they changed",
                rule="Every player answers the same → the room is close to deciding. "
                     "Different answers → it's only asking."),
     ["A10", "A14", "B4"])

# ── BEYOND THE HALL ───────────────────────────────────────────────────────────────────────
beat("B14", "OUTDOORS", "light, curious",
     "It isn't only people. In two thousand three, researchers in Leiden recorded great tits, a "
     "small songbird, in quiet and noisy parts of the city. Traffic noise is mostly low rumble. The "
     "birds in the noisy spots sang with a higher lowest note, lifting their songs above it. Here the "
     "room isn't echo. It's noise. And the answer isn't tempo. It's pitch.",
     ask_answer("A city is a room too", "low traffic rumble", "a great tit, in Leiden",
                "a higher lowest note", SRC_BIRDS, answers_cue="sang with a higher lowest note"),
     ["A17"])

beat("B15", "THE RECORD AS A ROOM", "storytelling, brisk",
     "Byrne's book makes the same argument about machines. He starts with Edison's cylinders, when "
     "bands had to perform the same song again and again for each batch of recordings. A recording "
     "format is a room made of minutes. In nineteen twenty-five, Igor Stravinsky had a contract to "
     "record his music. So he wrote a piano suite, his Serenade in A, with every movement short "
     "enough to fit one side of a seventy-eight R P M record. About three minutes, at most.",
     ask_answer("A room made of minutes", "one 78 rpm side: three minutes at most",
                "Stravinsky, 1925, with a recording contract",
                "Serenade in A: every movement short enough for one side",
                SRC_STRAV + " · " + "David Byrne, How Music Works, “Technology Shapes Music”",
                answers_cue="So he wrote a piano suite",
                evidence=["Contracted to record on his first American tour",
                          "Byrne opens the technology chapters with Edison's cylinders"]),
     ["A18", "A19"])

beat("B16", "THE SKIP BUTTON", "building, then struck",
     "The newest room is a playlist you can skip. A researcher at Ohio State, Hubert Léveillé "
     "Gauvin, studied three hundred and three US top ten hits from nineteen eighty-six to two "
     "thousand fifteen. The wait before the voice comes in fell from more than twenty seconds in the "
     "mid eighties to about five. And talking to a reporter, he put it like this. It's just adapting "
     "yourself to your environment, whether you're aware of it or not. That's Byrne's argument, "
     "from someone who counted.",
     ask_answer("303 US top-10 hits, 1986–2015", "a skip button, seconds in",
                "songwriters and producers", "the voice arrives sooner: 20+ s → about 5 s",
                SRC_LG, answers_cue="The wait before the voice",
                evidence=["Mid-1980s: more than 20 seconds before the voice · 2015: about 5",
                          "“It's just adapting yourself to your environment whether you're aware "
                          "of it or not” (AFP, 2017)"]),
     ["A20", "A21"])

beat("B17", "THE ROOM DOESN'T DECIDE", "cooling down, honest",
     "One caution. In a second study, he compared hits with less popular songs by the same artists, "
     "and the pattern didn't hold. A short intro doesn't make a hit. So the room shapes the music. "
     "It still doesn't decide it.",
     card("The second study", "Hits vs. less popular songs by the same artists",
          ["2015: 60 popular vs 60 less popular songs",
           "The data did not support the attention-economy predictions"],
          SRC_LG),
     ["A22"])

# ── THE TASK: the viewer's own room asks (before the payoff, so the ending stays the callback) ─
beat("B18", "YOUR ROOM", "direct, inviting",
     "Before I play mine, try yours. In a moment, clap once, wherever you are. If the clap hangs in "
     "the air after your hands stop, your room has echo. If it dies right away, it's dry. Go ahead.",
     card("Try it in your room", "First: clap once, and listen.",
          ["Clap hangs after your hands stop → echo · dies right away → dry",
           "“Every room you play in is asking you a question.”",
           "Strong answer: names what the room did (blurred your words, or swallowed them)",
           "Weak answer: “it felt different”"],
          "Our listening heuristic, not a measurement"),
     ["B3"], hold_after=2.5)

beat("B19", "SAY IT", "direct, unhurried",
     "Now say the sentence, every room you play in is asking you a question, at the pace your room "
     "seems to want.",
     card("Try it in your room", "Now: say the sentence at the pace your room wants.",
          ["Clap hangs after your hands stop → echo · dies right away → dry",
           "“Every room you play in is asking you a question.”",
           "Strong answer: names what the room did (blurred your words, or swallowed them)",
           "Weak answer: “it felt different”"],
          "Our listening heuristic, not a measurement"),
     ["B3"], hold_after=4.0)

beat("B20", "YOUR ANSWER", "warm, firm",
     "Did you speed up, or slow down? That's your answer. A real answer names what your room was "
     "doing, blurring your words or swallowing them. Just saying it felt different doesn't count.",
     card("Try it in your room", "Did you speed up, or slow down?",
          ["Clap hangs after your hands stop → echo · dies right away → dry",
           "“Every room you play in is asking you a question.”",
           "Strong answer: names what the room did (blurred your words, or swallowed them)",
           "Weak answer: “it felt different”"],
          "Our listening heuristic, not a measurement"),
     ["B3"])

# ── PAYOFF: the sentence, in the two rooms the cellist slowed down in ─────────────────────
beat("B21", "TWO ROOMS", "quiet, deliberate",
     "Here's mine, in two rooms like the ones the cellist slowed down in. First, the cathedral.",
     room_voice("Two rooms like the ones he slowed down in", "Simulated cathedral", "about a 5-second echo",
                [], "First: the cathedral.", SRC_IR, caption_cue="First"),
     ["A9", "B5"])

beat("D03", "DEMO", "(the sentence, with pauses, in the cathedral)",
     SENTENCE,
     room_voice("Two rooms like the ones he slowed down in", "Simulated cathedral", "about a 5-second echo",
                [{"label": "cathedral, room between phrases", "speed": 1.0, "ir": IR_MINSTER}],
                "", SRC_IR, active_cue="Every room"),
     ["B1"], audio_fx={"ir": IR_MINSTER, "speed": 1.0, "pause_s": 0.6, "phrases": PHRASES, "wet": 1.0})

beat("B22", "NO ECHO", "quiet",
     "And now, almost no echo at all.",
     room_voice("Two rooms like the ones he slowed down in", "no room: dry voice", "no impulse response",
                [{"label": "cathedral, room between phrases", "speed": 1.0, "ir": IR_MINSTER}],
                "Second: no echo.", "Our narration with no impulse response applied",
                caption_cue="almost no echo"),
     ["B2"])

beat("D04", "DEMO", "(the sentence, held longer, dry)",
     SENTENCE,
     room_voice("Two rooms like the ones he slowed down in", "no room: dry voice", "no impulse response",
                [{"label": "cathedral, room between phrases", "speed": 1.0, "ir": IR_MINSTER},
                 {"label": "dry, held longer", "speed": 0.85, "ir": None}],
                "", "Our narration with no impulse response applied", active_cue="Every room"),
     ["B2"], audio_fx={"ir": None, "speed": 0.85, "wet": 0.0})

beat("B23", "SAME ANSWER", "landing, unhurried",
     "Both slower than I'd normally say it. One is waiting for the echo to clear. The other is "
     "filling in for an echo that never comes. Same answer. Opposite questions.",
     room_voice("Same answer. Opposite questions.", "Simulated cathedral · dry", "both passes",
                [{"label": "cathedral, room between phrases: waiting for the echo to clear", "speed": 1.0,
                  "ir": IR_MINSTER},
                 {"label": "dry, held longer: filling in for an echo that never comes", "speed": 0.85,
                  "ir": None}],
                "", SRC_IR + " · " + SRC_SKW),
     ["A9", "A12", "B1", "B2"])

beat("B24", "OUTRO", "warm",
     "Every room is asking. Tanmay Kulkarni, in for Humanitarians AI, signing off.",
     {"type": "GRAPHIC", "status": "PROPS SET", "motion": "fade", "remotion": {
         "pattern": "ClaudeTitleOutroFull",
         "props": {"title": "Every room is asking.", "handle": "@HumanitariansAI",
                   "subline": SIGNOFF}}},
     [])


# ── guards (BEATS.md Part 1) ──────────────────────────────────────────────────────────────
PLACEHOLDER = re.compile(r"\b(PLACEHOLDER|TODO|TBD|TK|XXX|lorem)\b", re.I)
DIGIT_YEAR = re.compile(r"\b1[0-9]{3}\b|\b20[0-9]{2}\b")  # Kokoro: years in words (memory, W23)


def walk_strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from walk_strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from walk_strings(v)


def factcheck_rows():
    text = (HERE / "FACTCHECK.md").read_text()
    return set(re.findall(r"^\| ([AB]\d+) \|", text, re.M))


def main():
    rows = factcheck_rows()
    ids = [b[0] for b in BEATS]
    assert len(ids) == len(set(ids)), "duplicate beat_id"
    errors = []
    beats = []
    for bid, act, tone, text, shot, refs, fx, hold in BEATS:
        for r in refs:
            if r not in rows:
                errors.append(f"{bid}: FACTCHECK row {r} missing (drift)")
        for s in [text, *walk_strings(shot)]:
            if PLACEHOLDER.search(s):
                errors.append(f"{bid}: placeholder text: {s[:60]!r}")
        if DIGIT_YEAR.search(text):
            errors.append(f"{bid}: digit year in narration (write it in words): {DIGIT_YEAR.search(text).group()}")
        words = len(text.split())
        est = MEASURED.get(bid, round(words / WPS, 1))
        if act == "DEMO":
            # the demo's real length (room_voice.py output, echo tail included) is its clock
            env = json.loads((HERE / "envelopes" / f"{bid}.json").read_text())
            est = env["seconds"]
        rem = shot.get("remotion")
        if rem:
            rem["pattern"] += "OFL"   # open-licence fonts only, as W24/W25
            props = rem["props"]
            if rem["pattern"].startswith("RoomVoice"):
                # real envelopes only: each pass is drawn from the DEMO audio it shows
                props.pop("envelopeFrom", None)
                for ps in props["passes"]:
                    src = "D04" if ps["ir"] is None else ("D01" if "normal" in ps["label"] else "D02")
                    env = json.loads((HERE / "envelopes" / f"{src}.json").read_text())
                    for k in ("speed", "ir"):
                        ps.pop(k)
                    ps.update({"dry": env["dry"], "room": env["room"], "fps": env["fps"],
                               "dryLabel": "the voice", "roomLabel": "what the room adds"})
                props["floorDb"] = -48
                props["emptyLabel"] = ""   # set explicitly: no placeholder text before the voice
            props["durationSeconds"] = round(est + 0.1, 2)
            for k in [k for k in props if k.endswith("Cue")]:
                cue = props.pop(k)
                if cue is None:
                    props[k[:-3]] = None   # carried from the previous beat: on screen from frame 0
                    continue
                if cue not in text:
                    errors.append(f"{bid}: cue not in narration: {cue!r}")
                    continue
                mp3 = MP3 / f"beat-{bid}.mp3"
                if bid in MEASURED and mp3.exists():
                    props[k[:-3]] = spoken_at(text, str(mp3), cue)   # measured: when it's actually said
                else:
                    props[k[:-3]] = round(len(text[:text.index(cue)].split()) / WPS, 2)   # planning clock
        beats.append({"beat_id": bid, "act": act, "tone": tone, "narration_text": text,
                      "shot": shot, "estimated_duration_s": est,
                      "word_count": words, "audio_file": f"mp3/beat-{bid}.mp3",
                      **({"actual_duration_s": MEASURED[bid]} if bid in MEASURED else {}),
                      **({"audio_fx": fx} if fx else {}),
                      **({"hold_after_s": hold} if hold else {}),
                      "engine": "kokoro", "voice": VOICE,
                      "factcheck_ref": [f"FACTCHECK.md {r}" for r in refs] or None})
    if errors:
        sys.exit("BUILD FAILED\n  " + "\n  ".join(errors))
    sheet = {"metadata": {
        "title": TITLE, "title_status": "WORKING", "structure": "THE VOICE CHANGES ROOMS",
        "slug": "how-a-room-changes-music",
        "topic": "MUSIC", "register": "Pragmatist", "audience": "hai",
        "brand": "claude-liam", "channel": "hai", "chip": "@HumanitariansAI",
        "voice": VOICE, "engine": "kokoro", "voice_kokoro": VOICE,
        "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "thesis": ("A room doesn't write music. It asks a question, and every player hears it and "
                   "answers differently. One cellist slowed down in both the most echoing and the "
                   "driest of seven halls (74% of his tempo variation), while twelve musicians in "
                   "fourteen simulated halls answered so individually that the room explained under 9%."),
        "source_project": ("claude-for-music/how-music-works-audible (10-beat auto-conversion of Nik Bear "
                           "Brown's review of David Byrne's How Music Works; base topic, template discarded)"),
        "note": ("DRAFT 1 (THE VOICE CHANGES ROOMS). Generated by build_beat_sheet.py. Edit that, not this "
                 "file. Runtime is a words/sec estimate until Kokoro audio exists. RoomVoice, HallTempo, "
                 "AskAnswer are planned components. DEMO beats need room_voice.py (planned)."),
    }, "beats": beats}
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
    total = sum(b["word_count"] for b in beats)
    est = sum(b["estimated_duration_s"] + b.get("hold_after_s", 0) for b in beats)
    print(f"{len(beats)} beats · {total} words · ~{int(est // 60)}:{int(est % 60):02d} estimated")
    for b in beats:
        print(f"  {b['beat_id']:4} {b['act']:24} {b['word_count']:3}w ~{b['estimated_duration_s']:5}s  {b['tone']}")


if __name__ == "__main__":
    main()
