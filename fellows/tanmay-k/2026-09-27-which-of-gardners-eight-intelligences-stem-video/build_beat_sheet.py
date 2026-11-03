#!/usr/bin/env python3
"""Writes beat_sheet.json for the Week 24 topic video: EIGHT ROOMS (draft 2).

The film's structure is Gardner's own list. Each intelligence is a room, and a room's light comes
on only when Gardner's own writing says a machine does that thing. One metaphor, held end to end:
house → rooms → lights → doors. Every factual line cites the FACTCHECK.md row that backs it.

Every Remotion prop is set explicitly. ClaudeComposerAsk ships with another channel's defaults
("Hola, Bear", "@NikBearBrown", "Fable 5") and none of them may leak into this film.
"""
import copy
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from cue_align import spoken_at, spoken_at_whisper

# Beats timed on the WHISPER clock (cue_align.whisper_words: Whisper's words snapped to the audio's
# own pauses). Whisper showed their mid-phrase cues >0.25s off the pause clock (2026-09-27). Every
# other beat stays on the pause clock, which Whisper matched within 0.23s, so its renders stand.
WHISPER_CLOCK = {"B05", "B06", "B07", "B17"}
import json
from pathlib import Path

HERE = Path(__file__).parent
VOICE = "am_onyx"
TITLE = "Which of Gardner's Eight Intelligences Can a Machine Do?"
SIGNOFF = "Tanmay Kulkarni, in for Humanitarians AI"
WPS = 3.3  # measured on Week 23 am_onyx audio (1154 words / 346.0s). Kokoro audio replaces this

SRC_2024 = "Gardner, Furuzawa & Stachura, ‘Who Owns Intelligence?’, MI Oasis, Oct 2024"

# Order is the film's walk-through order, not Gardner's listing order.
ROOMS = ["Linguistic", "Logical-mathematical", "Spatial", "Musical",
         "Bodily-kinesthetic", "Naturalist", "Interpersonal", "Intrapersonal"]


def plan(states, focus, heading, caption, source, reveal_at_s=1.2, built=8, cue=None, caption_cue=None):
    """EightRooms props. states: dict room -> 'dark' | 'lit' | 'ajar'. `built` = rooms drawn so far
    (7 before the naturalist extension). reveal_at_s is ABSOLUTE seconds (PLAYBOOK §2)."""
    return {"type": "GRAPHIC", "status": "PROPS SET", "motion": "illustrate", "remotion": {
        "pattern": "EightRooms",
        "props": {"heading": heading,
                  # built=7: the 1983 house. Naturalist keeps its slot as "unbuilt", so no room
                  # changes position when it's added (continuity across B03 → B06).
                  "rooms": [{"name": r, "state": ("unbuilt" if built == 7 and r == "Naturalist"
                                                   else states.get(r, "dark"))} for r in ROOMS],
                  "focus": focus, "caption": caption, "source": source,
                  "revealAtSeconds": reveal_at_s, "captionAtSeconds": -1,
                  "_cue": cue, "_caption_cue": caption_cue}}}


def tour(plan_shot, kind, title, caption, source, caption_cue, extra_cue=None, in_cue=None,
         light_cue="Light on.", out_cue="Light on.", plan_caption_cue=None):
    """Walk into the focus room (EightRoomsTour): the camera travels in, the room's illustrated
    interior carries the evidence caption, then the camera pulls back to the plan. Cues resolve in
    main(). in_cue=None: walk in at the top of the beat. out_cue=None: stay in until ~1s before the
    end. light_cue: when the plan's light comes on (before the walk-in for B07)."""
    pp = plan_shot["remotion"]["props"]
    pp["_cue"], pp["_caption_cue"] = light_cue, plan_caption_cue
    return {"type": "GRAPHIC", "status": "PROPS SET", "motion": "push-in", "remotion": {
        "pattern": "EightRoomsTour",
        "props": {"plan": pp, "interiorInAt": 1.3, "_in_cue": in_cue, "_out_cue": out_cue,
                  "interior": {"kind": kind, "title": title, "caption": caption, "source": source,
                               "_caption_cue": caption_cue, "_extra_cue": extra_cue}}}}


def scene(pattern, props, motion="stagger"):
    """A RevealScenes card. Any key ending in "Cue" (e.g. atCue, tagAtCue) is a narration phrase that
    main() turns into absolute seconds under the same key without "Cue"."""
    return {"type": "GRAPHIC", "status": "PROPS SET", "motion": motion,
            "remotion": {"pattern": pattern, "props": props}}


def card(title, heading, lines, spark=""):
    # A citation is not a claim, so it never gets a number. A final "Source…" line moves into
    # the card's unnumbered footnote (sparkLine), after any existing spark text.
    if lines and lines[-1].startswith("Source"):
        spark = f"{spark} \u00b7 {lines[-1]}" if spark else lines[-1]
        lines = lines[:-1]
    return {"type": "GRAPHIC", "status": "PROPS SET", "motion": "illustrate", "remotion": {
        "pattern": "ClaudeArtifactCardFull",
        "props": {"chrome": "artifact", "artifactTitle": title, "artifactHeading": heading,
                  "artifactLines": lines, "sparkLine": spark}}}


# No still(): the film uses no third-party images (2026-09-26, Tanmay: no copyright risk at any
# cost). Page screenshots in pantry/ are verification evidence only and never appear on screen.


lit = {}  # cumulative light state as the walk-through proceeds


def light(room, state="lit"):
    lit[room] = state
    return copy.deepcopy(lit)


BEATS = []


def beat(bid, act, tone, text, shot, refs):
    BEATS.append((bid, act, tone, text, shot, refs))


# ── COLD OPEN ─────────────────────────────────────────────────────────────────────────────
beat("B01", "COLD OPEN", "curious",
     "A Humanitarians AI essay I read this week has a sentence I couldn't stop thinking about. It's "
     "about Howard Gardner, the psychologist who split the mind into separate intelligences. It says "
     "he never had to ask which of them a machine might take, because in nineteen eighty-three, technology \"was not "
     "yet a serious competitor to any of them.\" So I went and read what Gardner wrote after nineteen eighty-three. "
     "He did ask. And he answered, one intelligence at a time.",
     {"type": "GRAPHIC", "status": "PROPS SET", "motion": "type-on", "remotion": {
         "pattern": "ClaudeComposerAsk",
         "props": {"greeting": "Hi,", "topic": "INTELLIGENCE · AI",
                   "segment": "Gardner's eight intelligences",
                   "command": "which of Gardner's intelligences can a machine do?",
                   "runningText": "reading Gardner, 1983 to 2026…",
                   "folderLabel": "@HumanitariansAI", "modelLabel": "Claude",
                   "effortLabel": "High", "placeholder": "Ask about the record",
                   "output": ["“not yet a serious competitor to any of them”",
                              "Source: ‘Introducing Theorist.ai’, Humanitarians AI, March 2026"]}}},
     ["0.5"])

# ── PRESENTER + THE PLAN (subject in plain words, the map before any example) ─────────────
beat("B02", "THE PLAN", "warm, clear",
     "Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This video is about Gardner's theory of "
     "multiple intelligences, and which of them, by Gardner's own account, a machine has now walked "
     "into. Think of his theory as a house with eight rooms. We'll go through it room by room, and "
     "a light only comes on when Gardner himself says a machine does what that room is for. By the "
     "end you'll know the count, and why the last two rooms are the ones worth arguing about.",
     plan({}, -1, "Gardner's house: eight rooms",
          "A light comes on only when Gardner's own writing says a machine does it.",
          "Rooms: Gardner, Frames of Mind (1983) + naturalist (mid-1990s)"),
     ["1.2"])

# ── THE HOUSE ─────────────────────────────────────────────────────────────────────────────
# Years are written in words in narration (TTS only; captions keep digits): Kokoro reads digit
# years as "nineteen hundred eighty three" / "mid nineteen hundred ninety z" (found 2026-09-27).
# B03: "kinnesthetic" is the spoken form. Kokoro reads "kinesthetic" as kaɪnsθˈɛɾɪk.
beat("B03", "THE HOUSE", "explanatory",
     "The house was built in nineteen eighty-three, in a book called Frames of Mind. Seven rooms at first: "
     "linguistic, logical-mathematical, spatial, musical, bodily-kinnesthetic, and two personal "
     "ones, understanding other people and understanding yourself. In the mid nineteen-nineties he added an "
     "eighth: naturalist, the knack for telling kinds of living things apart.",
     plan({}, -1, "Frames of Mind, 1983: seven rooms. Mid-1990s: an eighth",  # fix 4
          "Naturalist was added later, the only extension to the house.",
          "Davis, Christodoulou, Seider & Gardner, ‘The Theory of Multiple Intelligences’, Harvard Project Zero",
          built=7),
     ["1.1", "1.2"])

beat("B04", "SURVEYOR'S NOTE", "honest, measured",
     "One honest note about the architecture before we go in. Most of academic psychology would "
     "draw this house with one big room, a single general ability called gee. A handbook chapter "
     "Gardner co-wrote admits as much: his theory \"would seem to put M-I theory at odds with gee.\" "
     "It also notes how few studies were built to test it as a whole. So this is Gardner's floor "
     "plan, not settled science. "
     "It's his house. We're asking what he says walked into it.",
     card("A note on the architecture.", "\u201cat odds with \u2018g\u2019\u201d",
          ["p. 12: the theory \u201cwould seem to put MI theory at odds with \u2018g\u2019\u201d",
           "p. 9: \u201cthe relative lack of empirical studies specifically designed to test the theory as a whole\u201d",
           "Source: Davis, Christodoulou, Seider & Gardner, \u2018The Theory of Multiple Intelligences\u2019, Harvard Project Zero"]),
     ["2.5", "2.6"])

beat("B05", "THE WALKTHROUGH", "turning, curious",
     "In twenty nineteen, Gardner said we'd built machines that \"equal or surpass human capacities,\" but he "
     "didn't say which. Then, in October twenty twenty-four, he and two colleagues, Shinri Foo-roo-zah-wah and "
     "Annie Sta-hoo-ra, walked the house themselves.",
     # Spoken-form spellings (TTS only; every on-screen label keeps the real spelling). Chosen by
     # checking Kokoro's phonemes: "Stachura" -> stæʃjˈʊɹɹə, "Sta-hoo-ra" -> stɑː-hˈuː-ɹɑː
     # (Tanmay, Gate P: sta-HOO-ra). "Furuzawa" -> fjʊɹ…, "Foo-roo-zah-wah" -> fuː-ɹuː-zɑː-wɑː.
     scene("TimelineReveal", {
         "eyebrow": "Did Gardner ask?", "heading": "2019, then room by room in 2024",
         "nodes": [
             {"label": "2019", "text": "machines \u201cwhich equal or surpass human capacities\u201d. Gardner, interviewed by Dario Ruggiero, Long Term Economy", "atCue": "In twenty nineteen"},
             {"label": "Oct 2024", "text": "\u2018Who Owns Intelligence? Reflections After a Quarter Century\u2019 \u00b7 Howard Gardner, Shinri Furuzawa & Annie Stachura", "atCue": "Then, in October twenty"}],
         "source": "Sources: Long Term Economy interview (Jul 2019, via howardgardner.com) \u00b7 MI Oasis (Oct 23 2024)"}),
     ["3.1", "3.2"])

# ── ROOMS 1–6 ─────────────────────────────────────────────────────────────────────────────
beat("B06", "ROOM 1 · LINGUISTIC", "brisk",
     "Room one: words. Their verdict on large language models is blunt. They \"clearly exhibit the "
     "signs\" of high linguistic intelligence. Light on.",
     tour(plan(light("Linguistic"), 0, "Room 1 · Linguistic",
               "“clearly exhibit the signs of … high linguistic intelligence”", SRC_2024),
          "linguistic", "Room 1 · Linguistic",
          "“clearly exhibit the signs of … high linguistic intelligence”", SRC_2024,
          caption_cue='They "clearly'),
     ["3.3"])

B07_CAPTION = ("Essay: technology in 1983 “was not yet a serious competitor to any of them” · Record: 1956 programs "
               "“carried out mathematical and logical operations” that “might have been considered intelligent” · "
               "“By no means clear” then: passing the Turing Test, winning games of strategy")
B07_SOURCE = SRC_2024 + " · ‘Introducing Theorist.ai’, Humanitarians AI, March 2026"

beat("B07", "ROOM 2 · LOGICAL-MATHEMATICAL", "a small double-take",
     "Room two: logic and numbers. Same sentence, same verdict. Light on. But here's the thing. "
     "In that same paper, the authors tell the history of the field. Programs at the nineteen fifty-six "
     "Dartmouth meeting, they write, already \"carried out mathematical and logical operations which, if carried out by human beings, might "
     "have been considered intelligent.\" So this light may have been on since before the house was "
     "built. What was \"by no means clear\" back then was conversation, and games of strategy. The "
     "essay's sentence needs that one correction.",
     # The light comes on early ("Same sentence… Light on."), then we step inside for the 1956 story.
     # PROOF-REVIEW-FINAL fix 2: both sides of the correction at the same size, in the caption.
     # Visual-variety review edit 1: "by no means clear" on screen too (FACTCHECK 3.4) → 35/35.
     tour(plan(light("Logical-mathematical"), 1, "Room 2 · Logical-mathematical", B07_CAPTION, B07_SOURCE),
          "logical", "Room 2 · Logical-mathematical", B07_CAPTION, B07_SOURCE,
          caption_cue="In that same paper", in_cue="But here's the thing", light_cue="Same sentence",
          out_cue=None),
     ["3.3", "3.4", "0.3", "0.5"])

beat("B08", "ROOM 3 · SPATIAL", "surprised",
     "Room three: space. And this one surprised me. Chess and Go are filed here, under spatial, not "
     "logic. \"Mastering games like chess or Go,\" and robots \"remembering and navigating complex "
     "terrains.\" Light on.",
     # Room-interior sample (Tanmay, 2026-09-26): walk into the room instead of a static plan.
     tour(plan(light("Spatial"), 2, "Room 3 · Spatial",
               "“Mastering games like chess or Go, robots remembering and navigating complex terrains”",
               SRC_2024),
          "spatial", "Room 3 · Spatial",
          "“Mastering games like chess or Go, robots remembering and navigating complex terrains”",
          SRC_2024, caption_cue="Chess and Go are filed", extra_cue="robots"),
     ["3.3", "3.11"])

B09_CAPTION = "recognizing pieces · “creating credible new ones in distinctive styles” · performing “with appropriate nuances”"

beat("B09", "ROOM 4 · MUSICAL", "brisk",
     "Room four: music. Recognizing pieces, \"creating credible new ones in distinctive styles,\" "
     "performing \"with appropriate nuances.\" Light on.",
     tour(plan(light("Musical"), 3, "Room 4 · Musical", B09_CAPTION, SRC_2024),
          "musical", "Room 4 · Musical", B09_CAPTION, SRC_2024,
          caption_cue="Recognizing pieces", extra_cue='"creating credible'),
     ["3.3", "3.11"])

B10_CAPTION = "playing instruments · “adroitly manipulating objects” · “competing successfully in athletic events”"

beat("B10", "ROOM 5 · BODILY-KINESTHETIC", "a beat of disbelief",
     "Room five is the one I'd have bet stayed dark. The body. But properly built and trained, they write, programs can play instruments, pick up and "
     "\"adroitly\" handle objects of different shapes, even compete \"successfully in athletic "
     "events.\" Light on.",
     tour(plan(light("Bodily-kinesthetic"), 4, "Room 5 · Bodily-kinesthetic", B10_CAPTION, SRC_2024),
          "bodily", "Room 5 · Bodily-kinesthetic", B10_CAPTION, SRC_2024,
          caption_cue="properly built", extra_cue="even compete"),
     ["3.3", "3.11"])

beat("B11", "ROOM 6 · NATURALIST", "building to the peak",
     "Room six, the one he added later: naturalist. Recognizing and grouping living things, and "
     "made things too, \"from thimbles to airplanes.\" Light on. That's six rooms out of eight. And "
     "the paper's next line is almost cheerful: \"So far, computational systems emerge as multiply "
     "intelligent!\"",
     # Inside: the naturalist evidence, verbatim ("thimbles to airplanes", PROOF optional fix 6).
     # Back on the plan: the peak line, at the moment it is spoken.
     tour(plan(light("Naturalist"), 5, "Room 6 · Naturalist",
               "“So far, computational systems emerge as multiply intelligent!”", SRC_2024),
          "naturalist", "Room 6 · Naturalist",
          "“Recognizing and grouping” living things and human-created things, “ranging from thimbles to airplanes”", SRC_2024,
          caption_cue="Recognizing and grouping", plan_caption_cue="the paper's next line"),
     ["3.3", "3.11"])

# ── INTERLUDE: who inspected the lights? ──────────────────────────────────────────────────
beat("B12", "THE INSPECTION", "pulling back, careful",
     "But hold on. Before the last two doors, I went back to check how a room was supposed to be "
     "earned. In nineteen eighty-three, a capacity had to meet eight criteria to count. Four of them are about "
     "biology: brains, childhoods, evolution, and people with unusual minds, like prodigies, "
     "savants, stroke patients. As I read it, you can't walk a machine through half of that "
     "inspection at all.",
     card("The 1983 inspection.", "eight criteria, four of them biological",
          # Two lines, not eight numbered criteria: the card numbers its own lines, and criterion
          # numbers inside them rendered as "1 1 isolation…" (caught on the B12 slate, 2026-09-26).
          ["Biological: isolation in prodigies, savants, stroke patients · distinct neural representation · distinct developmental path · basis in evolutionary biology",
           "The rest: symbol systems · psychometric support · experimental tasks · a core information-processing system",
           "Source: Davis, Christodoulou, Seider & Gardner, Table 1 (after Gardner 1983)"]),
     ["1.3", "1.4"])

beat("B13", "THE NEW INSPECTION", "quiet realisation",
     "So for animals, plants and machines, the twenty twenty-four paper uses a different inspection: six "
     "\"symptoms.\" Solving a problem, making a product, communicating, improving with practice, "
     "teaching others, and awareness. Five of those six you can watch happen. To me, that means the "
     "six lights came on under a performance test, not the one the house was built with. And even "
     "then, nobody scored it symptom by symptom. The paper just says these systems show \"a "
     "reasonable sample.\"",
     scene("TileReveal", {
         "eyebrow": "The 2024 inspection.", "heading": "six symptoms, for any candidate",
         "sub": "judged: easily \u00b7 possibly \u00b7 fails \u00b7 not possible to determine",
         "tiles": [
             {"label": "solving a problem", "atCue": "Solving a problem"},
             {"label": "creating a product", "atCue": "making a product"},
             {"label": "communicating information", "atCue": "communicating,"},
             {"label": "improving through practice", "atCue": "improving with practice"},
             {"label": "teaching others", "atCue": "teaching others"},
             {"label": "awareness or consciousness", "atCue": "and awareness", "dimLater": True}],
         "tagAtCue": "Five of those six", "tag": "YOU CAN WATCH IT HAPPEN", "dimTag": "NOT WATCHABLE",
         "footnote": "No per-symptom AI scores, only \u201ca reasonable sample\u201d", "footnoteAtCue": "nobody scored it",
         "source": "Source: " + SRC_2024}),
     ["3.6", "3.7"])

# ── ROOMS 7–8 ─────────────────────────────────────────────────────────────────────────────
B14_CAPTION = "evidence: diplomacy · salesmanship · gamesmanship · therapeutic interactions → “one should be more cautious”"

beat("B14", "ROOM 7 · INTERPERSONAL", "slower, genuinely unsure",
     "Room seven: understanding other people. And here the paper actually lists evidence. Programs "
     "doing diplomacy, salesmanship, gamesmanship, therapeutic interactions. On the new inspection, as I "
     "read it, that looks like a pass. And still: \"one should be more cautious.\" So the door's open a crack, and the "
     "light stays off. What I can't tell is why. Is it waiting on a better test? Or is it waiting "
     "on something no test could show? The paper doesn't say.",
     tour(plan(light("Interpersonal", "ajar"), 6, "Room 7 · Interpersonal", B14_CAPTION, SRC_2024),
          "interpersonal", "Room 7 · Interpersonal", B14_CAPTION, SRC_2024,
          caption_cue="Programs doing", light_cue="So the door's", out_cue="So the door's"),
     ["3.5"])

B15_CAPTION = "“a ‘category error’” · “can be trained to testify to or feign consciousness”"

beat("B15", "ROOM 8 · INTRAPERSONAL", "still",
     "Room eight: understanding yourself. This door they don't try to open. Using that word for a "
     "program at all, the authors write, \"can be seen as a 'category error.'\" Machines, they note, "
     "\"can be trained to testify to or feign consciousness.\" So this room isn't dark because a "
     "machine failed the inspection. It's dark because, on their reading, the inspection doesn't "
     "apply.",
     tour(plan(light("Intrapersonal", "dark"), 7, "Room 8 · Intrapersonal", B15_CAPTION, SRC_2024),
          "intrapersonal", "Room 8 · Intrapersonal", B15_CAPTION, SRC_2024,
          caption_cue='"can be seen', light_cue="So this room isn't dark", out_cue="So this room isn't dark"),
     ["3.5", "3.7"])

# ── CODA: who holds the keys ──────────────────────────────────────────────────────────────
beat("B16", "THE KEYS", "reflective, firmer",
     "This February, Gardner stepped back from the rooms altogether: \"Our social, ethical, and "
     "moral lives cannot and should not be consigned to any artificial entity.\" Listen to those two "
     "words. Cannot is about the machine. Should not is about us. The first might be checkable, "
     "one day. The second isn't something any test could settle. It's not an inspection. It's who holds the keys.",
     scene("KeyPair", {
         "eyebrow": "Gardner, February 2026.",
         "quote": "\u201cOur social, ethical, and moral lives cannot and should not be consigned to any artificial entity\u201d",
         "keys": [
             {"word": "cannot", "note": "about the machine: might be checkable, one day", "atCue": "Cannot is about"},
             {"word": "should not", "note": "about us: no test could settle it", "atCue": "Should not is about", "accent": True}],
         "closer": "Not an inspection. Who holds the keys.", "closerAtCue": "It's not an inspection",
         "source": "Source: Howard Gardner, \u2018The Fate of our Species in an AI-Infused Planet\u2019, howardgardner.com, Feb 6 2026"}),
     ["4.2"])

beat("B17", "OPTIONAL", "warm, unhurried",
     "Which brings me back to that essay. It called AI \"not obsolescence, its opposite.\" Its "
     "picture is a forklift: the smart response isn't to practise lifting heavier things, it's to "
     "learn to run the machine. This August, Gardner reached for a third word. He was talking about "
     "a different list, from his 2007 book Five Minds for the Future. The disciplined, synthesizing "
     "and creating minds, he said, will be handled by AI \"so well that pursuing them will become "
     "optional for our species.\" The respectful and ethical minds \"need to stay distinctly "
     "human.\" Not obsolete. Not its opposite. Optional. Rooms you no longer have to enter, but are "
     "still allowed to.",
     scene("WordTriptych", {
         "eyebrow": "Three words for the same house.", "heading": "obsolete \u00b7 its opposite \u00b7 optional",
         "columns": [
             {"word": "obsolete", "atCue": "It called AI", "resolveAtCue": "Not obsolete.", "resolve": "strike",
              "lines": [{"text": "the word the essay rules out", "atCue": "It called AI"}]},
             {"word": "its opposite", "atCue": "It called AI", "resolveAtCue": "Not its opposite.", "resolve": "dim",
              "lines": [{"text": "\u2018Introducing Theorist.ai\u2019, Humanitarians AI: \u201cNot obsolescence \u2014 its opposite.\u201d", "atCue": "It called AI"},
                        {"text": "\u201cThe intelligent response to a forklift is not to practice lifting heavier objects.\u201d", "atCue": "Its picture is a forklift"}]},
             {"word": "optional", "atCue": "This August", "resolveAtCue": "Optional.", "resolve": "choose",
              "lines": [{"text": "Gardner, Aug 2026, on Five Minds for the Future (2007)", "atCue": "He was talking about"},
                        {"text": "disciplined, synthesizing, creating minds \u2192 \u201cwill become optional for our species\u201d", "atCue": "\"so well that"},
                        {"text": "respectful, ethical minds \u2192 \u201cneed to stay distinctly human\u201d", "atCue": "The respectful and ethical"}]}],
         "source": "Sources: \u2018Introducing Theorist.ai\u2019, Humanitarians AI, March 2026 \u00b7 Education Next, \u2018Keeping an Open\u2014and Optional\u2014Mind About AI\u2019, Aug 26 2026 \u00b7 Five Minds for the Future, Harvard Business School Press, 2007"}),
     ["0.4", "0.6", "4.3", "4.4"])

beat("B18", "THE DOOR", "direct, inviting",
     "So that's the house. Six lights on, one door ajar, one room dark on purpose. If you think "
     "room seven is next, tell me in the comments. What would a machine actually have to show "
     "you, in a conversation with you, before you'd switch that light on?",
     plan(copy.deepcopy(lit), 6, "Six on · one ajar · one dark",
          "What would a machine have to show you before you'd switch room seven on?",
          SRC_2024),
     ["3.3", "3.5"])

beat("B19", "OUTRO", "warm",
     "Eight rooms, six lights. " + SIGNOFF + ", signing off.",
     {"type": "GRAPHIC", "status": "PROPS SET", "motion": "fade", "remotion": {
         "pattern": "ClaudeTitleOutroFull",
         "props": {"title": "Eight rooms. Six lights. One door ajar.",
                   "handle": "@HumanitariansAI", "subline": SIGNOFF}}},
     [])


def main():
    beats = []
    # Measured Kokoro durations are the master clock once audio exists (mp3/timings.json, written
    # by generate_audio_kokoro.py). Rebuilding must never throw them away.
    tpath = HERE / "mp3" / "timings.json"
    measured = json.loads(tpath.read_text()) if tpath.exists() else {}

    def at(text, cue, words, bid):
        # Seconds at which `cue` is spoken. With measured audio: PAUSE-ANCHORED (cue_align.py), i.e.
        # sentences pinned to the real pauses in the beat's audio, letters interpolated between them.
        # The old word-position fraction drifted 0.5s on average, up to 1.2s (PROOF, 2026-09-27).
        # Without audio: the planning rate.
        before = len(text[:text.index(cue)].split())
        mp3 = HERE / "mp3" / f"beat-{bid}.mp3"
        return ((bid in WHISPER_CLOCK and spoken_at_whisper(text, mp3, cue)) or spoken_at(text, mp3, cue)) if bid in measured and mp3.exists() else round(before / WPS, 2)

    for bid, act, tone, text, shot, refs in BEATS:
        words = len(text.split())
        rem = shot.get("remotion")
        if rem and not rem["pattern"].endswith("OFL"):
            # Open-licence fonts only (scenes/withOflFonts.tsx). No system or commercial fonts
            # reach the frame. shorts.py maps <Pattern>916 → <Pattern>OFL916, which is registered.
            rem["pattern"] += "OFL"
        props = shot.get("remotion", {}).get("props", {})
        cue = props.pop("_cue", None)
        if cue:
            # Reveal lands on the cue phrase, not before it (PLAYBOOK §2 / §4 moment of assertion).
            # Estimated from word position; rescale to measured audio once Kokoro has run.
            props["revealAtSeconds"] = at(text, cue, words, bid)
        ccue = props.pop("_caption_cue", None)
        if ccue:
            props["captionAtSeconds"] = at(text, ccue, words, bid)
        if rem and rem["pattern"].startswith("EightRoomsTour"):
            TRAVEL = 1.1   # must match EightRoomsTour.tsx
            ic, oc = props.pop("_in_cue"), props.pop("_out_cue")
            if ic:
                props["interiorInAt"] = round(at(text, ic, words, bid) + TRAVEL, 2)
            end_s = measured.get(bid, words / WPS)
            out_t = (end_s - 1.0) if oc is None else (at(text, oc, words, bid) - 0.25)
            props["interiorOutAt"] = round(max(props["interiorInAt"] + 1.0, out_t), 2)
            pp, ip = props["plan"], props["interior"]
            pp["revealAtSeconds"] = at(text, pp.pop("_cue"), words, bid)
            pcc = pp.pop("_caption_cue", None)
            pp["captionAtSeconds"] = at(text, pcc, words, bid) if pcc else props["interiorOutAt"]
            ip["captionAtSeconds"] = at(text, ip.pop("_caption_cue"), words, bid)
            ec = ip.pop("_extra_cue")
            ip["extraAtSeconds"] = at(text, ec, words, bid) if ec else props["interiorInAt"]
        def resolve(d):
            # "<key>Cue": narration phrase → "<key>": absolute seconds (RevealScenes props)
            if isinstance(d, dict):
                for k in [k for k in d if k.endswith("Cue") and isinstance(d[k], str)]:
                    d[k[:-3]] = at(text, d.pop(k), words, bid)
                for v in d.values():
                    resolve(v)
            elif isinstance(d, list):
                for v in d:
                    resolve(v)
        if rem:
            resolve(props)
            # Render length = measured audio. Without it the composition renders at its registered
            # length and remotion_scenes freezes the last frame to fill the rest, which silently
            # dropped B17's closing resolve and B07's pull-back (caught on the frames, 2026-09-27).
            if rem["pattern"].split("OFL")[0] in ("EightRooms", "EightRoomsTour", "TimelineReveal",
                                                  "TileReveal", "KeyPair", "WordTriptych") and bid in measured:
                props["durationSeconds"] = round(measured[bid] + 0.1, 2)
        beats.append({"beat_id": bid, "act": act, "tone": tone, "narration_text": text,
                      "shot": shot, "estimated_duration_s": round(words / WPS, 1),
                      "word_count": words, "audio_file": f"mp3/beat-{bid}.mp3",
                      **({"actual_duration_s": measured[bid]} if bid in measured else {}),
                      "engine": "kokoro", "voice": VOICE,
                      "factcheck_ref": [f"FACTCHECK.md {r}" for r in refs] or None})
    sheet = {"metadata": {
        "title": TITLE, "title_status": "WORKING", "structure": "EIGHT ROOMS",
        "slug": "gardner-eight-intelligences-machine",
        "topic": "INTELLIGENCE · AI", "register": "Pragmatist", "audience": "hai",
        "brand": "claude-liam", "channel": "hai", "chip": "@HumanitariansAI",
        "voice": VOICE, "engine": "kokoro", "voice_kokoro": VOICE,
        "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "thesis": ("Gardner did ask which intelligences machines can do. By his own 2024 account six of "
                   "eight rooms are lit, but under a performance test, not the 1983 one. The last "
                   "two stay dark for reasons no test result supplies."),
        "source_project": "claude-for-design/introducing-theoristai (10-beat auto-conversion, Substack byline Humanitarians AI, March 2026; used as base topic, template discarded)",
        "note": "DRAFT 2 (EIGHT ROOMS). Supersedes draft 1 (three-questions), archived in _superseded/. Generated by build_beat_sheet.py. Edit that, not this file. Runtime is a words/sec estimate until Kokoro audio exists.",
    }, "beats": beats}
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
    total = sum(b["word_count"] for b in beats)
    est = sum(b["estimated_duration_s"] for b in beats)
    print(f"{len(beats)} beats · {total} words · ~{int(est // 60)}:{int(est % 60):02d} estimated")


if __name__ == "__main__":
    main()
