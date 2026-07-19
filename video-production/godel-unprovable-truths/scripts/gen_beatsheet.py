#!/usr/bin/env python3
# Authors beat_sheet.json for the Godel slate cut (vox-explainer two-axis schema).
# Timing: piecewise word-weighted, pinned to real structural anchors from the
# energy envelope (vocal in ~6s, Godel-intro lift ~40s, reprise ~196s, out ~217s).
import json, os, glob

GODEL="/sessions/affectionate-sharp-rubin/mnt/bear-textbooks/books/unreal-reels/music/godel"
PANTRY=os.path.join(GODEL,"pantry")
REELS=os.path.join(GODEL,"reels","godel-unprovable-truths")
DUR=220.66

# ---- pantry concept prefixes; we pick successive files for reuse ----
CONCEPT={
 "holo":"Floating_holographic_text_This_statement_is_false",
 "fold":"Equations_folding_in_on_themselves",
 "candle":"Gdel_working_by_candlelight",
 "stairs":"An_infinite_staircase_of_axioms",
 "boom":"Boom_effect_mathematical_paradox",
 "gears":"Zoom_on_Gdels_metal_face",
 "typewriter":"Mechanical_typewriter_typing_out_Gdel_numbering",
 "fading":"Black-and-white_stylized_portrait_of_Gdelbot_fading",
 "vines":"Digital_vines_of_logic_branching",
 "recite":"Surreal_mechanical_portrait_of_a_humanoid_AI_reciting",
}
_used={}
def pick(tag):
    files=sorted(glob.glob(os.path.join(PANTRY,CONCEPT[tag]+"*.mp4")))
    i=_used.get(tag,0); _used[tag]=i+1
    return files[i % len(files)] if files else None

# ---- beat table ----
# (id, scene, seg, type, source, motion, lyric, teach, pantry_tag_or_None, prompt, archive_terms, viz)
B=[]
def add(**k): B.append(k)

# SEG A = liar paradox [6,40] ; SEG B = exposition [40,196] ; SEG C = reprise [196,217]
add(id="B00",scene=0,seg="pin_head",type="CARD",source="own",motion="hold",
    lyric="",cap="",teach="Title card.",tag=None,
    prompt="Vox editorial title card on newsprint ground (#F3EBDD), charcoal serif (#2F2A26): 'GODEL' large, 'UNPROVABLE TRUTHS' beneath, hairline underline; small credit line 'Nik Bear Brown · Tuzi Brown · Marley Brown'. One accent: dusty blue.",
    arch=[],viz=None)

# ---------- SCENE 0 : THE LIAR PARADOX ----------
add(id="B01",scene=0,seg="A",type="GRAPHIC",source="ai",motion="hold",
    lyric="Consider dis sentence ya / Dis yah statement is false",
    cap="Consider dis sentence — 'This statement is false'",
    teach="The Liar sentence is typed onto the page and boxed.",tag=None,
    prompt="Manim: a single serif line 'This statement is false.' types on, then a thin ink box draws around it. Newsprint ground, charcoal type, no color.",
    arch=[],viz={"kind":"text","content":"This statement is false."})
add(id="B02",scene=0,seg="A",type="FOOTAGE",source="own",motion="hold",
    lyric="So... it true",cap="So... it true?",
    teach="Holographic paradox loop (pantry).",tag="holo",
    prompt="[pantry] Floating holographic 'This statement is false', looped paradox.",arch=[],viz=None)
add(id="B03",scene=0,seg="A",type="GRAPHIC",source="ai",motion="hold",
    lyric="If a true, dat mean it false / But if a false, den it haffi be true / Yuh see it",
    cap="If true -> it's false. If false -> it's true.",
    teach="Two arrows chase each other: TRUE -> FALSE -> TRUE, a closed loop that never settles.",tag=None,
    prompt="Manim: two labels TRUE and FALSE with curved arrows forming a loop between them; a dot ping-pongs and never rests. Charcoal + one dusty-blue accent.",
    arch=[],viz={"kind":"loop","nodes":["TRUE","FALSE"]})
add(id="B04",scene=0,seg="A",type="FOOTAGE",source="own",motion="kenburns",
    lyric="Just by talkin 'bout itself / It mash up reason like it twis' back pon itself",
    cap="It talks about itself — reason twists back on itself",
    teach="Equations folding into recursion (pantry).",tag="fold",
    prompt="[pantry] Equations folding in on themselves, endless recursion.",arch=[],viz=None)
add(id="B05",scene=0,seg="A",type="GRAPHIC",source="ai",motion="hold",
    lyric="A real paradox, bredda / So if it nah true, and it nah false / Wha it really be",
    cap="A real paradox — not true, not false. So what is it?",
    teach="Label chip 'PARADOX'; the sentence sits with a '?' where its truth value should be.",tag=None,
    prompt="Manim: accent block chip reading 'PARADOX' (white serif on dusty-blue), the boxed sentence below with a large '?' where TRUE/FALSE would be.",
    arch=[],viz={"kind":"chip","label":"PARADOX"})

# ---------- SCENE 1 : ENTER GODEL ----------
add(id="B06",scene=1,seg="B",type="DOCUMENT",source="archive",motion="hold",
    lyric="Mi know it might sound like some fool-fool brain game / But round di early 1900s",
    cap="Sounds like a brain game — but around the early 1900s...",
    teach="A century timeline; a pin drops on 'early 1900s'.",tag=None,
    prompt="Manim/DOCUMENT: horizontal timeline 1900..2000 on newsprint, a marker pin lands near 1900-1910 with serif label 'early 1900s'.",
    arch=["Chronicling America 1900s mathematics","LOC early 20th century mathematics"],
    viz={"kind":"timeline","span":[1900,2000],"pin":1905})
add(id="B07",scene=1,seg="B",type="FOOTAGE",source="own",motion="kenburns",
    lyric="One man name Kurt Gödel / Tek it serious—an' change di whole maths game",
    cap="One man — Kurt Gödel — took it seriously",
    teach="Gödel by candlelight (pantry); name plate 'KURT GÖDEL, 1906–1978' at assembly.",tag="candle",
    prompt="[pantry] Godel working by candlelight in a mechanical study, blackboard. (Assembly overlays name plate KURT GODEL 1906-1978.)",
    arch=["Wikimedia Commons Kurt Godel portrait","LOC Kurt Godel"],viz=None)
add(id="B08",scene=1,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="Him discovery / It show seh math have limits, yuh zee it",
    cap="His discovery: math has limits",
    teach="A bounded region labelled MATH; one star (a truth) sits OUTSIDE the boundary.",tag=None,
    prompt="Manim: a rounded boundary labelled 'MATH (what we can prove)'; inside, small ticks; one star clearly outside the line, labelled 'true'. Terracotta accent on the star only.",
    arch=[],viz={"kind":"boundary","inside":"provable","outside":"a truth"})

# ---------- SCENE 2 : PROOF & AXIOMS ----------
add(id="B09",scene=2,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="A proof now, dat a just a solid argument / Fi show why one number statement haffi be true",
    cap="A proof = a solid chain of steps to a true statement",
    teach="Definition: PROOF = step -> step -> step => statement TRUE.",tag=None,
    prompt="Manim: three stacked step boxes connected by down-arrows, terminating in a chip 'TRUE'. Serif labels, one accent.",
    arch=[],viz={"kind":"chain","steps":["axiom","step","step"],"end":"TRUE"})
add(id="B10",scene=2,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="But fi build dem kinda argument / Yuh start wid some base—called axioms / Dem a di rule dem / Dat nuh need no more proof",
    cap="Every proof starts from axioms — base rules that need no proof",
    teach="Isotype row of 'axiom' blocks at the foundation; a small seal 'no proof needed'.",tag=None,
    prompt="Manim: a foundation row of identical square blocks labelled AXIOM (isotype, one unit per mark); a serif caption 'assumed, not proved'.",
    arch=[],viz={"kind":"isotype","unit":"axiom","count":5})
add(id="B11",scene=2,seg="B",type="FOOTAGE",source="own",motion="kenburns",
    lyric="Everything inna math / From di likkle one-two-three / To di biggest theory dem / All start from axiom dem",
    cap="From 1-2-3 to the biggest theorems — all from axioms",
    teach="Infinite staircase of axioms (pantry).",tag="stairs",
    prompt="[pantry] An infinite staircase of axioms leading into fog, unreachable.",arch=[],viz=None)
add(id="B12",scene=2,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="So if a statement bout numbers true / Yuh shoulda be able fi prove it / Using dem axioms",
    cap="If a statement about numbers is true, you should be able to prove it",
    teach="Pipeline: STATEMENT + AXIOMS -> PROOF -> TRUE. The dream of completeness.",tag=None,
    prompt="Manim: 'statement about numbers' + 'axioms' feed an arrow into 'proof' into 'TRUE'. Clean flow, one accent.",
    arch=[],viz={"kind":"pipeline","in":["statement","axioms"],"out":"proof -> true"})
add(id="B13",scene=2,seg="B",type="DOCUMENT",source="archive",motion="kenburns",
    lyric="From Ancient Greece till now / Mathematician been using dat method / Fi prove or disprove everything / Clean and neat, no doubt",
    cap="From Ancient Greece onward — prove or disprove, clean and neat",
    teach="Euclid's Elements scan; a long arrow 'Ancient Greece -> now'.",tag=None,
    prompt="DOCUMENT: a page of Euclid's Elements (archival scan), desaturated on newsprint, a highlighter bar under a proposition; arrow spanning 'Ancient Greece -> now'.",
    arch=["Internet Archive Euclid Elements","LOC Euclid Elements scan","Wikimedia Euclid Elements page"],
    viz=None)

# ---------- SCENE 3 : THE CRISIS / HILBERT ----------
add(id="B14",scene=3,seg="B",type="FOOTAGE",source="own",motion="hold",
    lyric="But when Gödel step inna di scene / Di math world did a wobble / Paradoxes start show up / An people start fret",
    cap="Gödel steps in — the math world wobbles",
    teach="Paradox explodes into fractal shards (pantry).",tag="boom",
    prompt="[pantry] Boom effect: mathematical paradox explodes into fractal shards.",arch=[],viz=None)
add(id="B15",scene=3,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="Big name mathematicians / Did want fi prove seh math cyaan go wrong",
    cap="Hilbert's dream: prove math can never contradict itself",
    teach="Hilbert's program: a seal reading COMPLETE + CONSISTENT stamped over 'all of mathematics'.",tag=None,
    prompt="Manim: a wax-seal / stamp motif stamping 'COMPLETE + CONSISTENT' onto a block 'ALL OF MATHEMATICS'. Name chip 'Hilbert, 1900'.",
    arch=["Wikimedia David Hilbert portrait"],
    viz={"kind":"seal","text":"COMPLETE + CONSISTENT"})
add(id="B16",scene=3,seg="B",type="FOOTAGE",source="own",motion="kenburns",
    lyric="But Gödel / Him never too sure / Matter of fact—him doubt if math / Even di right tool fi ask di big question",
    cap="But Gödel doubted math was even the right tool",
    teach="Zoom on Gödel-bot metal face, gears turning (pantry).",tag="gears",
    prompt="[pantry] Zoom on Godel's metal face, gears rotating slowly inside his head.",arch=[],viz=None)

# ---------- SCENE 4 : GODEL NUMBERING ----------
add(id="B17",scene=4,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="Words / Dem easy fi tangle up pon demself / But numbers / Dem usually straight—true or false",
    cap="Words tangle. Numbers stay straight — true or false.",
    teach="Left: a knotted word 'sentence'. Right: a clean number with TRUE/FALSE tags.",tag=None,
    prompt="Manim split: left a tangled scribble labelled 'words'; right a crisp integer labelled 'numbers' with two tags TRUE / FALSE. Terracotta vs dusty-blue.",
    arch=[],viz={"kind":"contrast","left":"words tangle","right":"numbers: true/false"})
add(id="B18",scene=4,seg="B",type="FOOTAGE",source="own",motion="hold",
    lyric="Still... Gödel get one idea / Him turn equations into numbers—code dem",
    cap="Gödel's idea: turn equations into numbers — code them",
    teach="Typewriter typing Gödel-numbering code (pantry).",tag="typewriter",
    prompt="[pantry] Mechanical typewriter typing out Godel-numbering code, numbers.",arch=[],viz=None)
add(id="B19",scene=4,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="So now, yuh can write one big statement / An represent it with just one number / Crazy, right",
    cap="A whole statement becomes a single number",
    teach="Gödel numbering: symbols -> primes -> one big number. Show a tiny worked encoding.",tag=None,
    prompt="Manim: a short formula's symbols each map to a small number, combined (2^a·3^b·5^c...) into one large integer, which is boxed and labelled 'the statement, as a number'.",
    arch=[],viz={"kind":"encode","example":"symbol -> prime power -> product"})

# ---------- SCENE 5 : SELF-REFERENCE / THE SENTENCE G ----------
add(id="B20",scene=5,seg="B",type="FOOTAGE",source="own",motion="kenburns",
    lyric="By doing dat, math start chat 'bout itself / Math get self-aware",
    cap="Now math can talk about itself — math becomes self-aware",
    teach="Equations folding recursion, second instance (pantry).",tag="fold",
    prompt="[pantry] Equations folding in on themselves, endless recursion (self-reference).",arch=[],viz=None)
add(id="B21",scene=5,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="And him write / Dis statement cyaan be proved / As one equation",
    cap="He writes G: 'This statement cannot be proved' — as a number",
    teach="The sentence G appears in words, then collapses into its Gödel number G.",tag=None,
    prompt="Manim: 'G:  This statement cannot be proved.' typed, then the words dissolve into a single boxed integer labelled G. One accent on G.",
    arch=[],viz={"kind":"text","content":"G: This statement cannot be proved."})
add(id="B22",scene=5,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="Now, dis different from di sentence we start wid / Cah math nuh play / It must be true or false / So which one it be",
    cap="Unlike the Liar, math must be true or false. So which is G?",
    teach="A fork: G branches into two boxes, TRUE and FALSE — which one?",tag=None,
    prompt="Manim: node 'G' forks into two boxes TRUE and FALSE with a hand-drawn '?' ring around the fork.",
    arch=[],viz={"kind":"fork","node":"G","branches":["TRUE","FALSE"]})

# ---------- SCENE 6 : TRUE BUT UNPROVABLE ----------
add(id="B23",scene=6,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="If it false—dat mean it can be proved / But if it can be proved—den it true / But wait… if it true / An still cyaan prove it / Dat mean it true, but unprovable",
    cap="If false -> provable -> true (contradiction). So G is TRUE but UNPROVABLE.",
    teach="The core deduction as a decision tree ending on a chip 'TRUE but UNPROVABLE'.",tag=None,
    prompt="Manim decision tree: 'G false' -> 'G provable' -> 'G true' flagged CONTRADICTION (terracotta); the surviving branch resolves to a chip 'TRUE but UNPROVABLE' (dusty-blue). This is the payoff frame.",
    arch=[],viz={"kind":"decision","result":"TRUE but UNPROVABLE"})
add(id="B24",scene=6,seg="B",type="FOOTAGE",source="own",motion="hold",
    lyric="Madness / But genius same way",
    cap="Madness — but genius, same way",
    teach="Gödel-bot fading into infinity (pantry).",tag="fading",
    prompt="[pantry] Black-and-white stylized portrait of Godel-bot fading into infinity.",arch=[],viz=None)
add(id="B25",scene=6,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="Dis shake up di whole foundation / Math cyaan hold every truth / Some truth always ago hide / Just outta reach",
    cap="Incompleteness: math can't hold every truth",
    teach="The MATH boundary from B08 returns, now cracked; several truths sit outside, out of reach.",tag=None,
    prompt="Manim: the boundary 'MATH' develops a hairline crack; three stars labelled 'true' float outside it, dimmed, tagged 'unreachable'.",
    arch=[],viz={"kind":"boundary_cracked"})

# ---------- SCENE 7 : GODEL ALL THE WAY DOWN ----------
add(id="B26",scene=7,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="Even if yuh try patch di gap / By adding more axioms / Guess wha / More unprovable truth ago pop up",
    cap="Patch the gap with a new axiom -> a new unprovable truth appears",
    teach="Add an axiom block to the foundation; immediately a new star pops OUTSIDE. Repeat gesture implied.",tag=None,
    prompt="Manim: an AXIOM block slides into the foundation; the boundary grows; but a fresh 'true' star blinks into existence just outside the new line.",
    arch=[],viz={"kind":"patch_loop"})
add(id="B27",scene=7,seg="B",type="FOOTAGE",source="own",motion="kenburns",
    lyric="No matter how much yuh add / Unprovable truth still deh deh / It's Gödel pon top a Gödel / All di way down",
    cap="Gödel on top of Gödel — all the way down",
    teach="Digital vines of logic branching endlessly (pantry).",tag="vines",
    prompt="[pantry] Digital vines of logic branching out endlessly, roots made of numbers.",arch=[],viz=None)
add(id="B28",scene=7,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="It mash up plenty dreams / Of one perfect math world / Where every question get answer",
    cap="It broke the dream of a perfect math where every question is answered",
    teach="Hilbert's COMPLETE+CONSISTENT seal from B15 returns, now cracked / stamped VOID.",tag=None,
    prompt="Manim: the 'COMPLETE + CONSISTENT' seal from earlier cracks down the middle; a faint stamp 'incomplete' overlays it.",
    arch=[],viz={"kind":"seal_broken"})
add(id="B29",scene=7,seg="B",type="DOCUMENT",source="ai",motion="hold",
    lyric="Some mathematicians accept it / Some fight it / Some even try ignore di hole / Wha open up under dem",
    cap="Reactions: accept it · fight it · ignore the hole",
    teach="Three labelled reaction cards: ACCEPT / FIGHT / IGNORE, one with a hole beneath it.",tag=None,
    prompt="Manim: three serif cards in a row — ACCEPT, FIGHT, IGNORE — the last with a dark circular 'hole' opening under its feet.",
    arch=[],viz={"kind":"cards","items":["ACCEPT","FIGHT","IGNORE"]})
add(id="B30",scene=7,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="But truth / More and more problems / Start show demself unprovable / People start worry / If dem whole career based pon smoke",
    cap="More and more problems turn out unprovable",
    teach="A tally that keeps ticking up: 'proven unprovable' count climbs (isotype squares filling).",tag=None,
    prompt="Manim: an isotype tally labelled 'shown unprovable' fills square by square, count climbing; a couple of name-stubs (Halting problem, Continuum hypothesis) fade in as examples.",
    arch=[],viz={"kind":"isotype_count","label":"shown unprovable"})

# ---------- SCENE 8 : NEW DOORS / COMPUTERS ----------
add(id="B31",scene=8,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="But still, Gödel's work / Never just close doors / It open new one",
    cap="Gödel's work didn't just close doors — it opened new ones",
    teach="One door labelled 'certainty' closes; an adjacent door labelled 'new math' opens with light.",tag=None,
    prompt="Manim: two serif-labelled doors; the left ('certainty') swings shut, the right ('new mathematics') opens, a golden highlighter bar of light across the threshold.",
    arch=[],viz={"kind":"doors"})
add(id="B32",scene=8,seg="B",type="FOOTAGE",source="own",motion="kenburns",
    lyric="Unprovable truths / Light di path fi early computers / An even today / Some genius still out deh / Try spot di truths / Yuh cyaan prove",
    cap="Unprovable truths lit the path to the first computers",
    teach="Digital vines / logic -> machines (pantry); name-stub 'Turing, 1936' at assembly.",tag="vines",
    prompt="[pantry] Digital vines of logic branching, roots of numbers, resolving toward machine forms. (Assembly overlays 'Turing, 1936'.)",
    arch=["Wikimedia Alan Turing portrait","LOC early computers ENIAC"],viz=None)
add(id="B33",scene=8,seg="B",type="GRAPHIC",source="ai",motion="hold",
    lyric="So yeah, some certainty get lost / But thanks to Gödel / We find beauty inna di unknown / Right inna di heart / Of truth itself",
    cap="Some certainty lost — but beauty found in the unknown",
    teach="The 'unreachable' stars from B25 re-render as quiet points of light — reframed as beauty, not loss.",tag=None,
    prompt="Manim: the outside 'true / unreachable' stars brighten gently into a small constellation labelled 'the unknown'; the crack stays but reads calm, not alarming.",
    arch=[],viz={"kind":"constellation"})

# ---------- SCENE 9 : REPRISE / OUTRO (loud) ----------
add(id="B34",scene=9,seg="C",type="FOOTAGE",source="own",motion="hold",
    lyric="Him build a code fi numbers talk 'bout numbers / Fi math start reason wid itself",
    cap="He built a code for numbers to talk about numbers",
    teach="Typewriter code reprise (pantry).",tag="typewriter",
    prompt="[pantry] Mechanical typewriter typing Godel-numbering code (reprise).",arch=[],viz=None)
add(id="B35",scene=9,seg="C",type="FOOTAGE",source="own",motion="hold",
    lyric="An' den... boom / Him write a ting weh seh / This statement cyaan be proved",
    cap="And then — boom — 'This statement cannot be proved'",
    teach="Boom -> fractals reprise (pantry).",tag="boom",
    prompt="[pantry] Boom effect, paradox explodes into fractal shards (reprise).",arch=[],viz=None)
add(id="B36",scene=9,seg="C",type="GRAPHIC",source="ai",motion="hold",
    lyric="If it false—den it get proved / But if it get proved—den it cyaan false / So it haffi be true / But still... unprovable",
    cap="False -> proved -> true. So: TRUE but unprovable.",
    teach="The B23 payoff chip restated fast: 'TRUE but UNPROVABLE'.",tag=None,
    prompt="Manim: quick restatement of the decision, landing hard on the chip 'TRUE but UNPROVABLE'.",
    arch=[],viz={"kind":"decision","result":"TRUE but UNPROVABLE"})
add(id="B37",scene=9,seg="C",type="GRAPHIC",source="ai",motion="hold",
    lyric="Dat mash up di whole idea seh math can hold all truth / Cause no matter how much yuh add / New truths always a hide outta reach",
    cap="No matter how much you add, new truths always hide out of reach",
    teach="The patch-loop from B26, sped up: add axiom -> new star -> add -> new star, receding.",tag=None,
    prompt="Manim: the add-axiom / new-star gesture repeats and recedes into the distance (Godel all the way down).",
    arch=[],viz={"kind":"patch_loop_recede"})
add(id="B38",scene=9,seg="C",type="FOOTAGE",source="own",motion="kenburns",
    lyric="It deep / It paradox / It Gödel / All di way down",
    cap="It's deep. It's paradox. It's Gödel — all the way down.",
    teach="Gödel-bot fading into infinity, final (pantry).",tag="fading",
    prompt="[pantry] Black-and-white Godel-bot fading into infinity (final).",arch=[],viz=None)
add(id="B39",scene=9,seg="pin_tail",type="CARD",source="own",motion="hold",
    lyric="",cap="",teach="Endcard + credits.",tag=None,
    prompt="Vox endcard on newsprint: 'KURT GODEL · 1931 · On Formally Undecidable Propositions'; small line 'Incompleteness'; credits 'Nik Bear Brown · Tuzi Brown · Marley Brown'.",
    arch=[],viz=None)

# ---------- TIMING : piecewise word-weighted between pinned anchors ----------
def words(b):
    t=(b["lyric"] or b["teach"] or "x").replace("/"," ")
    return max(2, len(t.split()))

HEAD_END=6.0        # title over intro
A_END=40.0          # liar paradox -> Godel-intro lift
C_START=196.0       # reprise onset (loud)
TAIL_START=217.0    # endcard/fade

def layout(seg_beats, t0, t1):
    tot=sum(words(b) for b in seg_beats)
    t=t0
    for b in seg_beats:
        d=(t1-t0)*words(b)/tot
        b["t_start"]=round(t,2); b["t_end"]=round(t+d,2); t+=d
    seg_beats[-1]["t_end"]=round(t1,2)

segA=[b for b in B if b["seg"]=="A"]
segB=[b for b in B if b["seg"]=="B"]
segC=[b for b in B if b["seg"]=="C"]
B[0]["t_start"]=0.0; B[0]["t_end"]=HEAD_END
layout(segA,HEAD_END,A_END)
layout(segB,A_END,C_START)
layout(segC,C_START,TAIL_START)
B[-1]["t_start"]=TAIL_START; B[-1]["t_end"]=round(DUR,2)

# ---------- assign pantry media ----------
for b in B:
    if b["tag"]:
        f=pick(b["tag"])
        b["media"]=os.path.basename(f) if f else None
        b["media_src"]=f
    else:
        b["media"]=None; b["media_src"]=None

# ---------- emit ----------
beats=[]
for b in B:
    beats.append({
        "beat_id":b["id"],"scene_index":b["scene"],
        "t_start_s":b["t_start"],"t_end_s":b["t_end"],
        "duration_s":round(b["t_end"]-b["t_start"],2),
        "timing":"EST (word-weighted, pinned to energy anchors 6/40/196/217s)",
        "shot":{"type":b["type"],"source":b["source"],"motion":b["motion"]},
        "lyric":b["lyric"],"caption":b["cap"],
        "teach":b["teach"],
        "fill_prompt":b["prompt"],
        "archive_queries":b["arch"],
        "viz":b["viz"],
        "slot_status":"FILLED (pantry)" if b["media"] else "SLATE (to build)",
        "media":b["media"],
        "approval_status":"pending",
    })

meta={
 "slug":"godel-unprovable-truths",
 "title":"Godel: Unprovable Truths",
 "series":"Unreal Reels — music",
 "artists":["Nik Bear Brown","Tuzi Brown","Marley Brown"],
 "master_audio":"GodelUnprovabletruths-mastered.wav",
 "total_duration_s":DUR,"fps":24,"width":1280,"height":720,"aspect_ratio":"16:9",
 "style":"vox-explainer (editorial paper-collage / newsprint / isotype)",
 "palette":{"ground":"#F3EBDD","ink":"#2F2A26","accent_blue":"#3D5A80",
            "accent_terracotta":"#D35F43","highlight":"#F5D061","card":"#3E5559"},
 "clock":"audio-first; EST word-weighting until forced alignment replaces it",
 "n_beats":len(beats),
 "n_slate":sum(1 for x in beats if x["slot_status"].startswith("SLATE")),
 "n_filled":sum(1 for x in beats if x["slot_status"].startswith("FILLED")),
}
os.makedirs(REELS,exist_ok=True)
json.dump({"metadata":meta,"beats":beats},
          open(os.path.join(REELS,"beat_sheet.json"),"w"),indent=2)
print("beats",len(beats),"| slate",meta["n_slate"],"filled",meta["n_filled"])
print("last t_end",beats[-1]["t_end_s"])
for x in beats:
    print(f'{x["beat_id"]} s{x["scene_index"]} {x["t_start_s"]:6.1f}-{x["t_end_s"]:6.1f} {x["shot"]["type"]:9} {x["slot_status"][:6]} {(x["caption"] or x["teach"])[:44]}')
