#!/usr/bin/env python3
"""Cue times on the Whisper clock (beat time, seconds), robust to Whisper writing numerals and ordinals.
Reads mp3/timings.json (words) and beats_text.py (signed narration). Writes CUES.json.
Every cue leads its anchor by LEAD_S so the picture arrives just before the word (lesson: lead swaps before the cue)."""
import difflib, json, re, sys
from pathlib import Path
HERE = Path(__file__).parent; sys.path.insert(0, str(HERE))
from beats_text import B
LEAD_S = 0.15
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
ORD1 = {"one":"first","two":"second","three":"third","five":"fifth","eight":"eighth","nine":"ninth","twelve":"twelfth"}
def below100(n): return [ONES[n]] if n < 20 else [TENS[n // 10]] + ([ONES[n % 10]] if n % 10 else [])
def below1000(n):
    if n < 100: return below100(n)
    return [ONES[n // 100], "hundred"] + (below100(n % 100) if n % 100 else [])
def num_words(n):
    if n >= 1000: return below1000(n // 1000) + ["thousand"] + (below1000(n % 1000) if n % 1000 else [])
    return below1000(n)
def ordinal(words):
    w = words[-1]
    if w in ORD1: w = ORD1[w]
    elif w.endswith("y"): w = w[:-1] + "ieth"
    elif w == "hundred": w = "hundredth"
    else: w = w + "th"
    return words[:-1] + [w]
def spoken(tok):
    t = tok.strip().rstrip(".,?!:;").replace(",", "")
    m = re.fullmatch(r"(\d+)(st|nd|rd|th)", t)
    if m: return ordinal(num_words(int(m.group(1))))
    pct = t.endswith("%"); t = t.rstrip("%")
    if re.fullmatch(r"\d+(\.\d+)?", t):
        whole, _, dec = t.partition("."); out = num_words(int(whole))
        if dec: out += ["point"] + [ONES[int(c)] for c in dec]
        return out + (["percent"] if pct else [])
    return [tok]
def norm(w): return re.sub(r"[^a-z0-9]", "", w.lower())
def heard_tokens(words):
    out = []
    for w, s, e in words:
        toks = [n for n in (norm(x) for x in spoken(w)) if n]
        for j, n in enumerate(toks): out.append((n, s + (e - s) * j / len(toks), s + (e - s) * (j + 1) / len(toks)))
    return out
def align(text, words):
    """signed tokens -> (start, end) on the Whisper clock; returns list aligned to text.split() tokens."""
    ref = [norm(w) for w in text.split()]; keep = [i for i, r in enumerate(ref) if r]
    rr = [ref[i] for i in keep]; heard = heard_tokens(words)
    sm = difflib.SequenceMatcher(None, rr, [h[0] for h in heard], autojunk=False)
    st = {}; 
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): st[keep[a + k]] = (heard[b + k][1], heard[b + k][2])
    return st
T = json.loads((HERE / "mp3" / "timings.json").read_text())
TEXT = {bid: narr for bid, _t, narr, _v, _s in B}

def sentences(bid):
    text = TEXT[bid]; st = align(text, T[bid]["words"])
    toks = text.split(); sents = re.split(r"(?<=[.?!])\s+", text.strip()); out = []; i = 0
    for s in sents:
        n = len(s.split()); idx = [k for k in range(i, i + n) if k in st]; i += n
        out.append({"text": s, "start": st[idx[0]][0] if idx else None, "end": st[idx[-1]][1] if idx else None, "first": i - n, "n": n})
    return out, st, toks
def word_t(bid, phrase_word, nth=1):
    """start time of the nth occurrence of a signed word."""
    text = TEXT[bid]; st = align(text, T[bid]["words"]); c = 0
    for k, w in enumerate(text.split()):
        if norm(w) == norm(phrase_word) and k in st:
            c += 1
            if c == nth: return st[k][0]
    raise KeyError((bid, phrase_word, nth))

def build():
    cues = {}
    for bid in TEXT:
        S, st, toks = sentences(bid)
        if bid == "B13" and S[4]["start"] is None:   # Whisper writes "Point two two five" as the numeral 225; place it at the end of the inner hold
            h1 = T["B13"]["inner_hold_at_s"] + T["B13"]["inner_hold_s"]; S[4]["start"], S[4]["end"] = h1, h1 + 1.0
        miss = [i for i, s in enumerate(S) if s["start"] is None]
        assert not miss, (bid, "sentences not aligned", miss)
        cues[bid] = {"duration_s": T[bid]["duration_s"], "narration_end_s": T[bid]["narration_end_s"], "sentences": [
            {"i": i, "start": round(s["start"], 3), "end": round(s["end"], 3), "text": s["text"][:60]} for i, s in enumerate(S)]}
    ev = {}
    def at(bid, name, i=None, word=None, nth=1, t=None):
        if t is None: t = cues[bid]["sentences"][i]["start"] if word is None else word_t(bid, word, nth)
        ev.setdefault(bid, []).append({"event": name, "t": round(max(0.0, t - LEAD_S), 3)})
    # B00
    at("B00","rally_start",0); at("B00","paddles_play",1)
    for k in range(1, 6): at("B00", f"counter_{k}", 1 + k)
    at("B00","mistake_line",7); at("B00","counter_6_ball_goes_past",8); at("B00","gap_callout",word="past"); at("B00","why_hold",9)
    # B01
    at("B01","chip_no_perfect_defense",0); at("B01","chip_game_to_eleven",1); at("B01","question_line",3)
    # B02
    at("B02","field",0); at("B02","paddle_arrows",2); at("B02","bounce_note",3); at("B02","steering_card",4); at("B02","name_chip",5); at("B02","constants_card_lit",6)
    # B03
    at("B03","ball_launch_path",0); at("B03","defender_sees",1); at("B03","timer_bar",3); at("B03","bars_highlight",4); at("B03","can_bar_pulse",5); at("B03","must_bar_pulse",6)
    # B04
    at("B04","attacker",0); at("B04","fan_all_aims",2); at("B04","defender_waits_middle",3); at("B04","extremes_lit",4); at("B04","half_field_card",word="away")
    # B05
    at("B05","bars_large",0); at("B05","compare",1); at("B05","exists",2); at("B05","none_exists",3); at("B05","ratio_0_27",4); at("B05","form_card",5)
    # B06
    at("B06","rows_appear",0); at("B06","row1_break_1",1); at("B06","row2_fill_to_6",2); at("B06","row3_fill_to_14",3); at("B06","same_rules",4); at("B06","one_number",5)
    # B07
    at("B07","chart_axes",0); at("B07","ball_speeds_up",1); at("B07","curves_draw",2); at("B07","bars_sink",3); at("B07","in_my_model",4); at("B07","clock_line",5)
    # B08
    at("B08","header",0); at("B08","row1_arithmetic",1); at("B08","row1_found",2); at("B08","row2_arith_and_found",3); at("B08","fourteenth_found",word="fourteenth",nth=2)
    # B09
    at("B09","second_dial",0); at("B09","aim_anywhere",1); at("B09","wedge_narrows",2); at("B09","line_drops",3)
    at("B09","tick_tenth",word="tenth",nth=1); at("B09","tick_nineteenth",word="nineteenth",nth=1); at("B09","count_starts",5)
    at("B09","count_lands_tenth",word="tenth",nth=2); at("B09","count_lands_nineteenth",word="nineteenth",nth=2)
    # B10
    at("B10","new_field",0); at("B10","size_chip",1); at("B10","line_0_1875",2); at("B10","two_speeds",3); at("B10","predicted_col",4); at("B10","found_col",5); at("B10","same_form",6)
    # B11
    at("B11","question",0); at("B11","dial_one",word="fast"); at("B11","dial_two",word="much"); at("B11","conditional",3); at("B11","no_speedup_card",4); at("B11","speeding_up_line",5)
    # B12
    at("B12","header",0); at("B12","model_line",1)
    for nm, w in (("spin","spin"),("reaction","reaction"),("paddle_edges","edges"),("real_machine","real")): at("B12", f"item_{nm}", word=w)
    at("B12","shows_line",3); at("B12","does_not_line",4)
    # B13: whisper writes the answer as numerals; the answer starts after the inner hold
    b13 = T["B13"]; h0 = b13["inner_hold_at_s"]; h1 = h0 + b13["inner_hold_s"]
    at("B13","your_turn",0); at("B13","case_numbers",1); at("B13","line_formula",2); at("B13","hold_start",t=h0 + LEAD_S); at("B13","answer_0_225",t=h1 + LEAD_S)
    at("B13","verdict_cards",5); at("B13","last_question",6); at("B13","dial_question",7); at("B13","signoff",8)
    for bid, L in ev.items():
        ts = [e["t"] for e in L]; assert ts == sorted(ts), (bid, "cues out of order", L)
        assert max(ts) < T[bid]["narration_end_s"], (bid, "cue after narration")
        cues[bid]["events"] = L
    (HERE / "CUES.json").write_text(json.dumps(cues, indent=1)); return cues

if __name__ == "__main__":
    c = build()
    for bid, v in c.items():
        print(f"{bid} dur {v['duration_s']:.2f}  " + "  ".join(f"{e['event']}@{e['t']:.2f}" for e in v["events"]))
