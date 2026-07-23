#!/usr/bin/env python3
"""Build beat_sheet.json + SHOTLIST.md for vox-prufrock (music film).

Clock: music bed (music/prufrock/Prufrock-mastered.wav, 525.08s).
First pass = uniform lyric-line timing (137 lines) snapped to the librosa
bar grid (music/prufrock/beat_grid.json, 172.3bpm ticks = double-time of
~86bpm; 8 ticks = one 4/4 bar = 2.786s). Refine later with forced
alignment (lyric-match faster-whisper machinery) — timing_source records this.

Run from books/unreal-reels/:  python3 reels/vox-prufrock/_build_beat_sheet.py
"""
import json, sys, urllib.parse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _gen_prompts import GEN_PROMPTS, TRUE_ARCHIVE

ROOT = Path(__file__).resolve().parents[2]          # books/unreal-reels
HERE = Path(__file__).resolve().parent
SONG = ROOT / "music" / "prufrock"

DUR = 525.079979
LINES = [l for l in (SONG / "song-13.txt").read_text().splitlines()
         if l.strip() and not l.startswith(("TITLE", "ARTIST"))]
assert len(LINES) == 137, len(LINES)
UNIT = DUR / len(LINES)

grid = json.loads((SONG / "beat_grid.json").read_text())
BARS = grid["beat_times"][::8]                       # 4/4 bars at ~86bpm

# recitation clock: if the Mac align step has run, line times are real
ALIGN = HERE / "align" / "lines.json"
ALIGNED = ALIGN.exists()
LINE_T = None
if ALIGNED:
    LINE_T = json.loads(ALIGN.read_text())["lines"]   # [{i, start, end}, ...]

def line_end_t(n):                                    # end of 1-indexed line n
    if LINE_T:
        return LINE_T[n-1]["end"]
    return n * UNIT

def snap(t):
    if ALIGNED:                                       # breaths beat bars
        return t
    return min(BARS, key=lambda b: abs(b - t))

# ---------------------------------------------------------------- the table
# (lines a..b 1-indexed inclusive, type, source, motion, scene, find-terms, extra)
T = [
 ((1,1),  "CARD", None, "hold",
  None, None,
  {"card": {"kind": "title", "text": "PRUFROCK",
            "sub": "after T. S. Eliot · Nik Bear Brown"}}),
 ((2,2),  "STILL", "archive", "kenburns",
  "archival photograph, evening sky spread over city rooftops and chimneys, "
  "early twentieth century, desaturated print reproduction on aged newsprint",
  "city rooftops evening sky 1910 photograph", {}),
 ((3,3),  "COMPOSITE", "archive", "annotate",
  "archival photograph of an operating theater around 1900, patient on the "
  "table, gowned surgeons, flat print look",
  "operating theater 1900 surgery photograph",
  {"annotation": {"kind": "ring", "color": "#D35F43",
                  "timed_to_word": "etherized"}}),
 ((4,5),  "FOOTAGE", "archive", "pan",
  "early film footage, half-deserted city street at dusk, a few figures "
  "retreating, gaslight, desaturated print look",
  "city street dusk 1910 film footage", {}),
 ((6,6),  "STILL", "archive", "kenburns",
  "archival photograph, cheap one-night hotel exterior at night, lettered "
  "sign, narrow doorway",
  "cheap hotel exterior night 1910 photograph", {}),
 ((7,7),  "STILL", "archive", "kenburns",
  "archival photograph, oyster house interior with sawdust floor and "
  "oyster shells, patrons at counter",
  "oyster house interior sawdust photograph", {}),
 ((8,10), "GRAPHIC", None, "map",
  None, None,
  {"viz": {"pattern": "map_path", "manim": "StreetArgumentMap",
           "note": "winding street path inked across a newsprint city map, "
                   "tedious switchbacks, path arrives at a large serif '?'"}}),
 ((11,12),"DOCUMENT", "archive", "annotate",
  "scan of Poetry: A Magazine of Verse, June 1915, The Love Song of "
  "J. Alfred Prufrock first printing, page with the opening lines",
  "Poetry magazine June 1915 Prufrock first printing scan",
  {"annotation": {"kind": "highlighter", "color": "#F5D061",
                  "timed_to_word": "ask"}}),
 ((13,14),"COMPOSITE", "archive", "annotate",
  "archival photograph, gallery or drawing room interior, women in long "
  "dresses mid-stride, sculpture casts on pedestals",
  "art gallery interior women 1910 photograph",
  {"annotation": {"kind": "label_chip", "text": "MICHELANGELO",
                  "color": "#3E5559", "timed_to_word": "Michelangelo"}}),
 ((15,16),"FOOTAGE", "archive", "hold",
  "early film footage, thick yellow fog rolling down a street against "
  "window-panes, figures dissolving in it",
  "fog city street film footage 1900s", {}),
 ((17,18),"COMPOSITE", "archive", "drawon",
  "archival photograph, wet street corner in fog, standing pools by the "
  "drains, evening",
  "fog street corner evening photograph",
  {"annotation": {"kind": "drawon_cat", "color": "#D35F43",
   "note": "hand-drawn terracotta cat outline over the fog plate — muzzle at "
           "the pane, tongue into the corners; the conceit made visible"}}),
 ((19,20),"STILL", "archive", "kenburns",
  "archival photograph, factory chimneys dropping soot over terraced "
  "houses, a leap of smoke off the terrace",
  "factory chimneys soot terrace houses photograph", {}),
 ((21,22),"COMPOSITE", "archive", "annotate",
  "archival photograph, quiet house at night in soft October fog",
  "house night fog october photograph",
  {"annotation": {"kind": "drawon_cat", "color": "#D35F43",
   "note": "the drawn cat-fog curls once about the house and settles asleep; "
           "stroke ends motionless on the downbeat"}}),
 ((23,25),"FOOTAGE", "archive", "pan",
  "early film footage, smoke sliding along a street at rooftop level, "
  "slow lateral drift",
  "smoke street rooftops film footage", {}),
 ((26,26),"DOCUMENT", None, "annotate",
  None, None,
  {"annotation": {"kind": "quote", "text": "There will be time, there will be time",
                  "color": "#F5D061", "timed_to_word": "time"},
   "note": "serif pull-quote on newsprint; golden highlighter sweeps the repeat"}),
 ((27,27),"GRAPHIC", None, "isotype",
  None, None,
  {"viz": {"pattern": "isotype", "manim": "IsotypeDotGrid",
           "note": "a grid of small face marks; one face mark 'prepared' front "
                   "and center, the met faces count up around it"}}),
 ((28,29),"STILL", "archive", "kenburns",
  "archival photograph, close crop of working hands — lifting, setting "
  "down, mid-task at a table",
  "hands working table close photograph", {}),
 ((30,31),"COMPOSITE", "archive", "annotate",
  "archival photograph, a set dinner plate on a white cloth, single place",
  "dinner plate table setting photograph",
  {"annotation": {"kind": "drop_mark", "color": "#2F2A26",
   "note": "a serif '?' drops onto the plate and lands on the word 'plate'"}}),
 ((32,33),"GRAPHIC", None, "isotype",
  None, None,
  {"viz": {"pattern": "isotype", "manim": "IsotypeDotGrid",
           "note": "one hundred charcoal squares count up (indecisions); "
                   "then terracotta revision strokes strike through rows "
                   "(visions, revisions). Verify count = 100 as claimed."}}),
 ((34,34),"STILL", "archive", "kenburns",
  "archival photograph, toast and tea service on a tray, close still life",
  "tea service toast tray photograph", {}),
 ((35,36),"COMPOSITE", "archive", "annotate",
  "archival photograph of a Michelangelo sculpture cast in a museum hall, "
  "visitors passing",
  "Michelangelo sculpture cast museum photograph",
  {"annotation": {"kind": "label_chip", "text": "MICHELANGELO",
                  "color": "#3E5559", "timed_to_word": "Michelangelo"},
   "note": "reprise — identical chip treatment as B09; the repetition IS the joke"}),
 ((37,38),"DOCUMENT", None, "annotate",
  None, None,
  {"annotation": {"kind": "quote", "text": "Do I dare?",
                  "color": "#D35F43", "timed_to_word": "dare"},
   "note": "the question typed twice, second underlined by hand"}),
 ((39,40),"STILL", "archive", "kenburns",
  "archival photograph, narrow staircase seen from below, bannister "
  "curving up into shadow",
  "staircase from below 1910 photograph",
  {"shot_focus": [0.5, 0.15]}),
 ((41,41),"COMPOSITE", "archive", "annotate",
  "archival portrait photograph from behind and above, crown of a man's "
  "head, hair thinning",
  "bald spot crown head portrait photograph",
  {"annotation": {"kind": "ring", "color": "#D35F43",
                  "timed_to_word": "thin",
   "note": "ring on the bald spot + gossip chip: 'how his hair is growing thin!'"}}),
 ((42,43),"COMPOSITE", "archive", "annotate",
  "Edwardian menswear fashion plate, morning coat, high collar, modest "
  "necktie with a simple pin, full figure",
  "morning coat fashion plate 1910 menswear",
  {"annotation": {"kind": "label_chips",
   "note": "the vox labeled-diagram move: chips MORNING COAT / COLLAR / "
           "NECKTIE / SIMPLE PIN land on their words"}}),
 ((44,44),"DOCUMENT", None, "annotate",
  None, None,
  {"annotation": {"kind": "quote",
                  "text": "“But how his arms and legs are thin!”",
                  "color": "#BF3339", "timed_to_word": "thin"},
   "note": "the gossip gets its own card — crimson chip, THE REBUKE VOICE "
           "(reserved accent, returns at B54/B60)"}),
 ((45,46),"CARD", None, "hold",
  None, None,
  {"card": {"kind": "big_text", "text": "Do I dare\ndisturb the universe?"},
   "note": "ink on cream, dead center, nothing else — the biggest line gets "
           "the emptiest screen"}),
 ((47,48),"GRAPHIC", None, "kinetic",
  None, None,
  {"viz": {"pattern": "clock_reverse", "manim": "MinuteReversal",
           "note": "a mono clock hand sweeps one minute forward, then "
                   "reverses exactly; decisions/revisions as tick labels"}}),
 ((49,50),"FOOTAGE", "archive", "hold",
  "early film footage, society evening — dining room, guests, courses "
  "passing, repetitive elegance",
  "dinner party society 1910 film footage", {}),
 ((51,51),"GRAPHIC", None, "isotype",
  None, None,
  {"viz": {"pattern": "isotype", "manim": "IsotypeDotGrid",
           "note": "rows of tiny coffee-spoon marks measuring out a life — "
                   "the isotype joke; count up briskly, no flourish"}}),
 ((52,53),"STILL", "archive", "kenburns",
  "archival photograph, parlor with upright piano, door ajar to a farther "
  "room, music implied",
  "parlor piano farther room photograph", {}),
 ((54,54),"DOCUMENT", None, "annotate",
  None, None,
  {"annotation": {"kind": "quote", "text": "So how should I presume?",
                  "color": "#F5D061", "timed_to_word": "presume"}}),
 ((55,56),"COMPOSITE", "archive", "annotate",
  "collage grid of cropped archival portrait eyes, direct gaze, varied, "
  "pinned like specimens on the newsprint",
  "portrait eyes close crop archival photographs",
  {"annotation": {"kind": "label_chip", "text": "A FORMULATED PHRASE",
                  "color": "#3E5559", "timed_to_word": "formulated"}}),
 ((57,58),"GRAPHIC", None, "drawon",
  None, None,
  {"viz": {"pattern": "specimen", "manim": "SpecimenPin",
           "note": "entomology board: a hand-drawn butterfly pinned; the pin "
                   "strikes on 'pinned', wriggle strokes on 'wriggling'"}}),
 ((59,61),"STILL", "archive", "kenburns",
  "archival photograph, cigarette butt-ends heaped in a tray, hard light, "
  "close still life",
  "ashtray cigarette ends still life photograph", {}),
 ((62,63),"STILL", "archive", "kenburns",
  "archival portrait photograph, bare braceleted arms, white, lamplight, "
  "cropped below the face",
  "braceleted arms lamplight portrait photograph", {}),
 ((64,66),"COMPOSITE", "archive", "annotate",
  "same register as previous plate — arm in lamplight, downed with light "
  "brown hair, dress fabric at the edge of frame",
  "arm lamplight dress fabric photograph",
  {"annotation": {"kind": "ring", "color": "#D35F43", "timed_to_word": "hair",
   "note": "ring on the down of hair; a pencil perfume-swirl drifts off the "
           "dress — the digression drawn, not said"}}),
 ((67,69),"STILL", "archive", "kenburns",
  "archival photograph, arms lying along a table edge, a shawl wrapped, "
  "quiet interior",
  "shawl arms table interior photograph", {}),
 ((70,71),"FOOTAGE", "archive", "pan",
  "early film footage, narrow streets at dusk, pipe smoke rising past "
  "upper windows",
  "narrow street dusk smoke film footage", {}),
 ((72,72),"STILL", "archive", "kenburns",
  "archival photograph, men in shirt-sleeves leaning out of tenement "
  "windows, evening",
  "men shirtsleeves leaning windows tenement photograph", {}),
 ((73,74),"GRAPHIC", None, "drawon",
  None, None,
  {"viz": {"pattern": "drawon", "manim": "RaggedClaws",
           "note": "an ink crab draws itself and scuttles across a newsprint "
                   "sea floor, silent; the film's one pure creature-beat"}}),
 ((75,78),"STILL", "archive", "kenburns",
  "archival photograph, afternoon interior asleep — long fingers smoothing "
  "a coverlet, low sun through curtains",
  "afternoon interior sleep curtains photograph", {}),
 ((79,80),"COMPOSITE", "archive", "annotate",
  "archival photograph, tea table spread — cakes and ices on stands, "
  "porcelain",
  "tea cakes ices table spread photograph",
  {"annotation": {"kind": "label_chips",
   "note": "chips TEA / CAKES / ICES land politely; then a terracotta ring "
           "tightens around empty tablecloth on 'crisis'"}}),
 ((81,82),"DOCUMENT", "archive", "annotate",
  "public-domain engraving, the head brought in upon a platter (Salome / "
  "John the Baptist), museum scan",
  "Salome head platter engraving public domain scan",
  {"annotation": {"kind": "label_chip", "text": "BROUGHT IN UPON A PLATTER",
                  "color": "#3E5559", "timed_to_word": "platter"}}),
 ((83,83),"DOCUMENT", None, "annotate",
  None, None,
  {"annotation": {"kind": "quote",
                  "text": "I am no prophet — and here’s no great matter",
                  "color": "#F5D061", "timed_to_word": "prophet"}}),
 ((84,85),"COMPOSITE", "archive", "annotate",
  "archival photograph, a liveried footman holding a coat by a doorway, "
  "formal, faintly amused",
  "footman livery coat doorway photograph",
  {"annotation": {"kind": "drawon", "color": "#D35F43",
   "note": "a terracotta snicker-stroke curls at the footman's mouth on "
           "'snicker' — one stroke, then gone"}}),
 ((86,86),"CARD", None, "hold",
  None, None,
  {"card": {"kind": "big_text", "text": "And in short, I was afraid."},
   "note": "held in silence-of-image; no annotation, no motion"}),
 ((87,88),"STILL", "archive", "kenburns",
  "archival photograph, table after tea — cups, marmalade jar, crumbs, "
  "afternoon light going",
  "tea table cups marmalade afternoon photograph", {}),
 ((89,90),"STILL", "archive", "kenburns",
  "archival photograph, porcelain close-up, two chairs angled toward each "
  "other, talk implied",
  "porcelain tea cups two chairs photograph", {}),
 ((91,93),"GRAPHIC", None, "kinetic",
  None, None,
  {"viz": {"pattern": "squeeze", "manim": "UniverseBall",
           "note": "a dotted sphere of everything compresses to a ball and "
                   "rolls toward the serif '?' from B07 — the map's question "
                   "returns; same glyph, same weight"}}),
 ((94,95),"DOCUMENT", "archive", "annotate",
  "public-domain print, the raising of Lazarus (Rembrandt etching), "
  "museum scan",
  "Rembrandt raising Lazarus etching public domain scan",
  {"annotation": {"kind": "label_chip", "text": "LAZARUS, COME FROM THE DEAD",
                  "color": "#3E5559", "timed_to_word": "Lazarus"}}),
 ((96,98),"COMPOSITE", "archive", "annotate",
  "archival photograph, a woman settling a pillow against a chair back, "
  "half-turned away, lamplight",
  "woman settling pillow chair lamplight photograph",
  {"annotation": {"kind": "speech_chip",
                  "text": "“That is not what I meant at all.”",
                  "color": "#BF3339", "timed_to_word": "meant",
   "note": "THE REBUKE — crimson chip, second appearance (B44 was first)"}}),
 ((99,100),"FOOTAGE", "archive", "pan",
  "early film footage, sunset over dooryards, a water cart sprinkling a "
  "street",
  "street sprinkler water cart film footage", {}),
 ((101,103),"GRAPHIC", None, "isotype",
  None, None,
  {"viz": {"pattern": "isotype", "manim": "IsotypeDotGrid",
           "note": "the afters: three labeled rows of marks — NOVELS / "
                   "TEACUPS / SKIRTS THAT TRAIL — counting up in reading "
                   "order, then '…and so much more' overflows the frame"}}),
 ((104,104),"DOCUMENT", None, "annotate",
  None, None,
  {"annotation": {"kind": "quote",
                  "text": "It is impossible to say just what I mean!",
                  "color": "#F5D061", "timed_to_word": "impossible"}}),
 ((105,105),"FOOTAGE", "archive", "hold",
  "early film footage, a magic lantern beam in a dark parlor, patterns "
  "thrown on a stretched sheet",
  "magic lantern projection parlor film footage", {}),
 ((106,108),"STILL", "archive", "kenburns",
  "archival photograph, a figure turning toward a window, shawl thrown "
  "off a shoulder, lamplight behind",
  "figure window shawl lamplight photograph", {}),
 ((109,110),"COMPOSITE", "archive", "annotate",
  "the previous window plate held, dimming",
  "figure window lamplight photograph",
  {"annotation": {"kind": "speech_chip",
                  "text": "“That is not it at all.”",
                  "color": "#BF3339", "timed_to_word": "all",
   "note": "the rebuke chip returns verbatim — third and last crimson"}}),
 ((111,112),"COMPOSITE", "archive", "annotate",
  "public-domain Hamlet playbill or theatrical poster, nineteenth century",
  "Hamlet playbill nineteenth century poster scan",
  {"annotation": {"kind": "strike_x", "color": "#D35F43",
                  "timed_to_word": "Hamlet",
   "note": "terracotta X through the Prince; a tin deputy star sketches in "
           "at the corner — THE TURN: same chassis, register goes country. "
           "One margin voice: the ELIOT EXITS HERE teach chip owns the text; "
           "the deputy is named by B61's role cards"}}),
 ((113,114),"STILL", "archive", "kenburns",
  "archival photograph, a stagehand holding a theater door, half in "
  "shadow, polite, mid-exit",
  "stagehand theater door photograph", {}),
 ((115,116),"GRAPHIC", None, "isotype",
  None, None,
  {"viz": {"pattern": "cards", "manim": "StateCardPair",
           "note": "two slate-teal role cards: THE PRINCE (struck through) "
                   "vs THE DEPUTY (hairline-underlined); serif white labels"}}),
 ((117,118),"DOCUMENT", None, "annotate",
  None, None,
  {"annotation": {"kind": "highlighter", "color": "#F5D061",
                  "timed_to_word": "concise",
   "note": "typed index card: 'careful · precise · polite · "
           "…not all that concise' — highlighter lands on the "
           "contradiction"}}),
 ((119,120),"COMPOSITE", "archive", "annotate",
  "archival photograph, vaudeville comic in frilled costume mid-bow, "
  "stage lights flat",
  "vaudeville comic frilled costume photograph",
  {"annotation": {"kind": "ring", "color": "#D35F43", "timed_to_word": "frilly",
   "note": "ring on the frills; one beat of self-deprecation, no pile-on"}}),
 ((121,122),"CARD", None, "hold",
  None, None,
  {"card": {"kind": "big_text",
            "text": "I’m gettin’ old.",
            "sub": "— might just roll up my trousers"},
   "note": "ink card; a small hand-drawn trouser-cuff roll doodles itself "
           "under the sub line (design system, no media)"}),
 ((123,123),"COMPOSITE", "ai", "annotate",
  "barber-shop head chart, four numbered heads showing hair parted front "
  "and back, flat diagram style, aged print",
  "barber chart hair part diagram vintage",
  {"annotation": {"kind": "drawon_arrow", "color": "#D35F43",
   "note": "terracotta arrow re-routes the part to the back on 'back'"}}),
 ((124,124),"COMPOSITE", "archive", "annotate",
  "archival photograph, a single peach on a plate, hard focus, nothing "
  "else on the table",
  "peach on plate still life photograph",
  {"annotation": {"kind": "ring", "color": "#D35F43", "timed_to_word": "peach",
   "note": "ring around the peach + tiny chip callback: 'DO I DARE?' — "
           "the B23 question, now about fruit; the film's thesis in one gag"}}),
 ((125,125),"STILL", "archive", "kenburns",
  "menswear plate or archival photograph, white flannel trousers, seaside "
  "resort dress, full figure",
  "white flannel trousers seaside fashion photograph", {}),
 ((126,126),"FOOTAGE", "archive", "pan",
  "early film footage, boardwalk beach stroll, slow walkers, parasols, "
  "surf at the edge",
  "boardwalk beach stroll film footage 1910s", {}),
 ((127,128),"STILL", "archive", "kenburns",
  "public-domain painting, sirens or mermaids singing among waves "
  "(Waterhouse / Draper school), museum scan",
  "mermaids sirens painting public domain museum scan",
  {"shot_focus": [0.5, 0.4]}),
 ((129,129),"CARD", None, "hold",
  None, None,
  {"card": {"kind": "big_text",
            "text": "But I don’t reckon\nthey’d sing for me."},
   "note": "the gut line. Ink on cream, longest hold in the film; nothing "
           "moves"}),
 ((130,131),"FOOTAGE", "archive", "hold",
  "early film footage, open sea waves riding seaward, whitecaps blown "
  "back, no shore in frame",
  "ocean waves whitecaps film footage", {}),
 ((132,132),"GRAPHIC", None, "kinetic",
  None, None,
  {"viz": {"pattern": "split_field", "manim": "TideTurn",
           "note": "the frame splits to pure ink and pure cream wave-bands — "
                   "the wind turning the water black and white; the film's "
                   "palette reduced to its two poles"}}),
 ((133,133),"STILL", "archive", "kenburns",
  "archival photograph, southern night falling over a porch and yard, "
  "last light on the horizon",
  "southern night porch dusk photograph", {}),
 ((134,135),"COMPOSITE", "archive", "annotate",
  "public-domain painting or photograph, figures wreathed in seaweed "
  "beneath the surface, dreamlike, museum scan",
  "sea nymphs seaweed painting public domain scan",
  {"annotation": {"kind": "tint", "color": "#BF3339",
   "note": "the red weed hand-tinted crimson on the desaturated plate — "
           "the reserved accent's final, non-verbal appearance"}}),
 ((136,136),"FOOTAGE", "archive", "hold",
  "early film footage or photograph, the sea surface seen from below, "
  "light breaking through, figures above",
  "underwater surface light film footage", {}),
 ((137,137),"STILL", "archive", "hold",
  "the underwater plate holds, darkening from the edges to ink",
  "underwater dark surface photograph",
  {"note": "PEAK — margin silent (law 3). No annotation event: the darkening "
           "is baked into the plate/motion itself. Any wash-off of lingering "
           "margin marks completes by the END of B75; B76 plays clean and "
           "drowns to ink; hard cut to the outro"}),
]

# ------------------------------------------------------------ voxlit layer
# beat.role: illustrate | teach | breathe  (aspects/explainer/voxlit/SKILL.md)
# Margin laws: chips in breaths; <=5 words unless quoting the line in the ear;
# peaks are breathe; teach <= 1/3 and never consecutive.
ROLES = {   # default: illustrate. IDs verified against table order.
  "B03": "teach",   # GLOSS — ether (line 3)
  "B08": "teach",   # PROVENANCE — Poetry, June 1915 (ll. 11–12)
  "B17": "teach",   # ALLUSION — Hesiod (ll. 28–29)
  "B21": "teach",   # ALLUSION+STRUCTURE — Michelangelo refrain ×2 (ll. 35–36)
  "B31": "teach",   # ALLUSION — Twelfth Night 'dying fall' (ll. 52–53)
  "B44": "teach",   # ALLUSION — Matthew 14 platter (ll. 81–82)
  "B50": "teach",   # ALLUSION — Marvell, universe/ball (ll. 91–93)
  "B59": "teach",   # ADAPTATION MARKER — Eliot exits (ll. 111–112)
  # B09 Michelangelo & B51 Lazarus chips quote the line in the ear →
  # illustrate (law-2 exemption), cite lives in FACTCHECK only.
  "B27": "breathe", "B42": "breathe", "B47": "breathe", "B70": "breathe",
  "B73": "breathe", "B76": "breathe", "B77": "breathe",
}
PEAK_LINES = {45, 46, 86, 129, 137}   # margin law 3 — declared peaks

# teach-chip upgrades (chip text <=5 words; every one gets a FACTCHECK.md
# source line — the scholarship gate). One margin voice per beat: a teach
# chip REPLACES the beat's textual label chip if both exist.
TEACH_CHIPS = {
  "B03": {"kind": "gloss_chip", "text": "ETHER: 1846", "color": "#3E5559",
          "at_line_end": 3,
          "source": "Morton's ether demonstration, Mass General, Oct 1846"},
  "B17": {"kind": "cite_chip", "text": "HESIOD, WORKS AND DAYS", "color": "#3E5559",
          "at_line_end": 29,
          "source": "Hesiod, Works and Days (c. 700 BC); Eliot's l. 29"},
  "B21": {"kind": "tally_chip", "text": "MICHELANGELO ×2", "color": "#3E5559",
          "at_line_end": 36,
          "source": "refrain, second occurrence — ll. 13–14 / 35–36"},
  "B31": {"kind": "cite_chip", "text": "TWELFTH NIGHT, I.i", "color": "#3E5559",
          "at_line_end": 53,
          "source": "Shakespeare, Twelfth Night I.i.4 — 'that strain again, it had a dying fall'"},
  "B44": {"kind": "cite_chip", "text": "MATTHEW 14", "color": "#3E5559",
          "at_line_end": 82,
          "source": "Matt 14:1–11, John the Baptist's head on a platter"},
  "B50": {"kind": "cite_chip", "text": "MARVELL, 1681", "color": "#3E5559",
          "at_line_end": 93,
          "source": "'To His Coy Mistress' — 'roll all our strength… into one ball'"},
  "B59": {"kind": "provenance_chip", "text": "ELIOT EXITS HERE", "color": "#D35F43",
          "at_line_end": 110,
          "source": "adaptation boundary: ll. 111+ are Nik Bear Brown's country register"},
}
# B08's teaching IS its DOCUMENT plate (the 1915 scan) — no chip needed.

ARCHIVES = [
 ("LOC", "https://www.loc.gov/free-to-use/?q={q}"),
 ("Smithsonian", "https://www.si.edu/openaccess?edan_q={q}"),
 ("InternetArchive", "https://archive.org/search?query={q}"),
 ("Wikimedia", "https://commons.wikimedia.org/w/index.php?search={q}&title=Special:MediaSearch&type=image"),
 ("Prelinger", "https://archive.org/search?query={q}+AND+collection%3Aprelinger"),
]

def links(terms):
    q = urllib.parse.quote_plus(terms)
    return {n: u.format(q=q) for n, u in ARCHIVES}

beats, t_prev, lint_prev, lint_run, flags = [], 0.0, None, 0, []
for i, ((a, b), typ, src, motion, scene, find, extra) in enumerate(T, 1):
    bid = f"B{i:02d}"
    t_end = DUR if (a, b) == (137, 137) or i == len(T) else snap(line_end_t(b))
    if t_end <= t_prev + 2.0:
        t_end = t_prev + 2.786
    lyric = "\n".join(LINES[a-1:b])
    beat = {
        "beat_id": bid,
        "t_start": round(t_prev, 3),
        "actual_duration_s": round(t_end - t_prev, 3),
        "lyric_lines": [a, b],
        "narration_text": lyric,
        "shot": {"type": typ, "source": src, "motion": motion},
        "scene_description": scene,
        "chosen_media": None,
        "audio_file": None,
    }
    if extra.get("shot_focus"):
        beat["shot"]["focus"] = extra["shot_focus"]
    for k in ("annotation", "viz", "card", "note"):
        if k in extra:
            beat[k] = extra[k]
    beat["role"] = ROLES.get(bid, "illustrate")
    if bid in TEACH_CHIPS:
        c = dict(TEACH_CHIPS[bid])
        c["timing"] = "line_end"                          # margin law 1
        c["timing_trust"] = ("TRUSTED — align/words.json" if ALIGNED else
                             "UNTRUSTED — uniform first pass")
        beat["teach_chip"] = c
        # one margin voice per beat: teach chip replaces a textual label chip
        if beat.get("annotation", {}).get("kind") in ("label_chip", "speech_chip"):
            beat.pop("annotation")
    if find:
        beat["archive_queries"] = links(find)
        beat["find_terms"] = find
    # source axis (Bear, 2026-07-05): generic scenes GENERATE (nano-banana /
    # Midjourney, detailed prompts, beat-id lead, --ar 16:9); only beats
    # where the real object IS the teaching stay archive-mandatory.
    if GEN_PROMPTS.get(bid):
        beat["shot"]["source"] = "ai"
        beat["image_prompt"] = GEN_PROMPTS[bid]
        beat["mj_prompt"] = f"{bid}, {GEN_PROMPTS[bid]} --ar 16:9"
    elif bid in TRUE_ARCHIVE:
        beat["shot"]["source"] = "archive"
        beat["archive_target"] = TRUE_ARCHIVE[bid]
    if typ in ("STILL", "COMPOSITE", "FOOTAGE", "DOCUMENT") and scene and "image_prompt" not in beat:
        beat["image_prompt"] = scene
    if typ == "FOOTAGE" and scene:
        beat["video_prompt"] = ("slow documentary motion, constant velocity, "
                                "key action in the first 60%: " + scene)
    beats.append(beat)
    if typ == lint_prev:
        lint_run += 1
        if lint_run > 2:
            flags.append(f"{bid}: {typ} run of {lint_run}")
    else:
        lint_prev, lint_run = typ, 1
    t_prev = t_end

# outro law slot (vox_outro.py owns rendering; reserve the beat)
beats.append({
    "beat_id": f"B{len(T)+1:02d}", "t_start": round(t_prev, 3),
    "actual_duration_s": round(DUR - t_prev, 3) if DUR - t_prev > 2 else 4.0,
    "lyric_lines": None, "narration_text": "",
    "shot": {"type": "CARD", "source": None, "motion": "hold"},
    "card": {"kind": "outro", "handle": "@nikbearbrown",
             "next_line": "Next: Miniver Cheevy, but make it Vox."},
    "chosen_media": None, "audio_file": None,
    "note": "outro law — vox_outro.py; mascot variant deterministic from slug",
})

from collections import Counter
hist = Counter(b["shot"]["type"] for b in beats)

sheet = {
  "metadata": {
    "slug": "vox-prufrock",
    "title": "Prufrock (Vox style)",
    "purpose": "MUSIC FILM in the vox-explainer chassis — the music extension. "
               "Clock = the mastered track; beats are lyric-line groups "
               "snapped to the librosa bar grid.",
    "clock": "music bed — music/prufrock/Prufrock-mastered.wav (525.08s). "
             "librosa 172.3bpm ticks = double-time of ~86bpm; bar = 2.786s. "
             "First-pass uniform lyric-line mapping snapped to bars.",
    "timing_source": "uniform-line + bar-snap; REFINE with faster-whisper "
                     "forced alignment (lyric-match machinery) before "
                     "annotation timing is trusted",
    "master_audio": "../../music/prufrock/Prufrock-mastered.wav",
    "aspect_ratio": "16:9", "fps": 24,
    "duration_s": DUR,
    "style_preset": "vox-editorial",
    "isotype_mark": "square",
    "ground": "#F3EBDD",
    "accents": {
      "general": ["#5B7B9C", "#D35F43"],
      "rebuke": "#BF3339",
      "highlighter": "#F5D061",
      "entity_cards": "#3E5559"
    },
    "accent_rule": "terracotta is the editor's pen; crimson appears exactly "
                   "four times (B26 gossip, B52 + B58 the rebuke chip, B74 "
                   "the red weed) and never otherwise; golden highlighter "
                   "only on DOCUMENT quotes",
    "voxlit": {
      "skill": "aspects/explainer/voxlit/SKILL.md",
      "clock_mode": "recitation",
      "aligned": ALIGNED,
      "peak_lines": sorted(PEAK_LINES),
      "karaoke": "CC overlay — vox-prufrock.srt cut at verse lines; "
                 "word-timed highlight is a Remotion burn-in variant on "
                 "request, never a second cut",
      "cc_rule": "chips stay out of the lower third so CC and marginalia "
                 "can coexist",
    },
    "style_bible": {
      "visual_style": "editorial paper collage on real newsprint scan; "
                      "desaturated archival plates; flat annotation plane; "
                      "serif labels with hairline underlines",
      "lighting_style": "flat print, no digital effects",
      "prompt_rule": "prompts describe plates only; lyric text NEVER "
                     "rendered inside media — quotes live on the "
                     "annotation plane"
    },
    "provenance": "Eliot's poem: Poetry (June 1915); US public domain. "
                  "Country-register closing sections are Nik Bear Brown's "
                  "adaptation. Paintings/engravings named in prompts are PD; "
                  "sidecars still required per slot.",
    "counts": {"beats": len(beats), "lyric_lines": 137},
    "shot_type_histogram": dict(hist),
    "rhythm_lint_flags": flags,
  },
  "beats": beats,
}

# ------------------------------------------------- MARGIN LINT (voxlit laws)
margin = []
prev_teach = False
n_teach = 0
for b in beats:
    role = b.get("role", "illustrate")
    chip = b.get("teach_chip")
    if role == "teach":
        n_teach += 1
        if prev_teach:
            margin.append(f"{b['beat_id']}: consecutive teach beats (law 4)")
    prev_teach = (role == "teach")
    if chip:
        n_words = len(chip["text"].replace("×", " ").split())
        if n_words > 5:
            margin.append(f"{b['beat_id']}: chip '{chip['text']}' >5 words (law 2)")
        if role == "breathe":
            margin.append(f"{b['beat_id']}: chip on a breathe beat")
    span = b.get("lyric_lines")
    if span and set(range(span[0], span[1]+1)) & PEAK_LINES:
        if role != "breathe":
            margin.append(f"{b['beat_id']}: peak line but role={role} (law 3)")
        if chip or b.get("annotation"):
            margin.append(f"{b['beat_id']}: margin voice on a peak (law 3)")
if n_teach > len(beats) // 3:
    margin.append(f"teach beats {n_teach}/{len(beats)} exceed 1/3 cap (law 4)")
sheet["metadata"]["voxlit"]["teach_beats"] = n_teach
sheet["metadata"]["voxlit"]["margin_lint"] = margin or "clean"

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))

# --------------------------------------- CC track (karaoke = captions, srt)
def ts(sec):
    h, r = divmod(sec, 3600); m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1)*1000):03d}"

cues = []
for n, line in enumerate(LINES, 1):
    t0 = LINE_T[n-1]["start"] if LINE_T else (n-1) * UNIT
    t1 = line_end_t(n)
    cues.append(f"{n}\n{ts(t0)} --> {ts(t1)}\n{line}\n")
(HERE / "vox-prufrock.srt").write_text("\n".join(cues))

# ----------------------------- STILL_PROMPTS.md (copy-paste generation list)
sp = ["# STILL_PROMPTS — vox-prufrock (nano-banana via Higgsfield / Midjourney)",
      "",
      "Format: `<BEAT>, <prompt> --ar 16:9`. One line = one generation.",
      "No lyric text / lettering / watermarks in any plate. FOOTAGE beats:",
      "this makes the SEED still; i2v motion is the beat's video_prompt.",
      "Drop results in pantry/ prefixed with the beat id, then `pantry`.",
      "", "## Generate", ""]
for b in beats:
    if b.get("mj_prompt"):
        sp.append(b["mj_prompt"])
        sp.append("")
sp += ["## True archive — do NOT generate (the real object is the teaching)", ""]
for bid, why in TRUE_ARCHIVE.items():
    sp.append(f"- **{bid}** — {why}")
(HERE / "STILL_PROMPTS.md").write_text("\n".join(sp))
n_gen = sum(1 for b in beats if b.get("mj_prompt"))
print(f"STILL_PROMPTS.md: {n_gen} generate · {len(TRUE_ARCHIVE)} true-archive")

print("beats:", len(beats), "| histogram:", dict(hist))
print("shot lint:", flags or "clean")
print(f"roles: teach {n_teach} · breathe "
      f"{sum(1 for b in beats if b.get('role')=='breathe')} · illustrate rest")
print("MARGIN LINT:", margin or "CLEAN")
print("clock:", "ALIGNED (recitation)" if ALIGNED else
      "uniform first pass — run _align.py on the Mac")
print(f"CC: vox-prufrock.srt — {len(cues)} verse-line cues")
durs = [b["actual_duration_s"] for b in beats]
print(f"beat dur: min {min(durs):.1f} med {sorted(durs)[len(durs)//2]:.1f} max {max(durs):.1f}")
