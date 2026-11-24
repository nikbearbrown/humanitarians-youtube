#!/usr/bin/env python3
"""make_sheet.py -- writes beat_sheet.json (16:9) and short/beat_sheet.json (9:16).

Every number in the narration is derived from code/results.json and asserted here, so
a re-run of the simulation that changed a number stops this script instead of
shipping a stale line. Re-running preserves what the pipeline wrote back:
metadata.approvals, metadata.build, and per beat (when its narration is unchanged)
actual_duration_s / audio_file / build / render_duration_s / shot.remotion.rendered.
Remotion beats get props.durationSeconds from the measured audio.
"""
import json
from pathlib import Path

REEL = Path(__file__).resolve().parent
R = json.loads((REEL / "code" / "results.json").read_text())
P, S, H = R["params"], R["strategies"], R["headline"]

# ---- numbers -> words (only the ones the script speaks), each asserted -------------
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen " \
       "fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def words(n):
    n = int(n)
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + ("" if n % 10 == 0 else "-" + ONES[n % 10])
    if n < 1000:
        return ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + words(n % 100))
    if n < 1_000_000:
        return words(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + words(n % 1000))
    return words(n // 1_000_000) + " million" + ("" if n % 1_000_000 == 0 else " " + words(n % 1_000_000))


assert R["synthetic"] is True
X, N, S0 = P["X"], P["N"], P["S0"]
assert (X, N, S0) == (10_000, 10, 50.0)
DUMP_PRICE = S0 - P["eta"] * X                         # every share in the one big sale
assert abs(DUMP_PRICE - 49.50) < 1e-9
assert S["dump"]["mean_bps"] == 100.0 and S["dump"]["std_bps"] == 0.0
assert abs(S["dump"]["mean_usd"] - 5000) < 0.01
TWAP_MEAN = round(S["twap"]["mean_bps"])               # 9.89  -> 10
TWAP_P95 = round(S["twap"]["p95_bps"])                 # 65.37 -> 65
RL_MEAN = round(S["rl"]["mean_bps"])                   # 13.31 -> 13
RL_P95 = round(S["rl"]["p95_bps"])                     # 53.59 -> 54
DAYS = P["episodes"]                                   # practice runs
TEST = P["test_days"]
assert (TWAP_MEAN, TWAP_P95, RL_MEAN, RL_P95, DAYS, TEST) == (10, 65, 13, 54, 40_000_000, 20_000), \
    "results changed -- rewrite the narration numbers"
assert S["rl"]["std_bps"] < S["twap"]["std_bps"] and S["rl"]["p95_bps"] < S["twap"]["p95_bps"]
assert S["rl"]["mean_bps"] > S["twap"]["mean_bps"]     # "pays a little more on average"
assert R["rl_objective_gap_vs_ac_pct"] < 2.0           # "its bars land close to it"
assert R["rl_max_abs_dev_shares"] <= 400
rl = S["rl"]["schedule"]
assert all(a >= b for a, b in zip(rl, rl[1:]))         # "sell more early, then taper off"
assert round(S["dump"]["mean_bps"] / S["twap"]["mean_bps"]) == 10   # "impact falls about ten times"

TITLE = "How an AI Sells a Big Order"
SLUG = "ai-sells-a-big-order"
TOPIC = "Irreducibly Human"
COMPOSER = {"topic": TOPIC, "segment": TITLE, "folderLabel": "@HumanitariansAI",
            "modelLabel": "Claude"}

META = {
    "title": TITLE,
    "slug": SLUG,
    "skill": "ai-explainer",
    "kind_note": "weekly STEM explainer (AI in finance)",
    "creator": "Boopesh M.",
    "fellow": "Boopesh M.",
    "brand": "claude-hai",
    "channel": "claude-hai",
    "channel_title": "",
    "topic": TOPIC,
    "audience": "HAI",
    "register": "Plain",
    "engine": "kokoro",
    "voice_kokoro": "am_onyx",
    "voice_policy": "persistent-fellow-selected",
    "palette": "claude",
    "pronounce": {"Kokoro": "kˈoʊkəɹoʊ"},
    "date": "2026-11-22",
    "source": [
        "code/execution_rl.py -> code/results.json + code/run.log (numpy only, seeds "
        f"{P['seed_train']} train / {P['seed_test']} held-out; SYNTHETIC market, run twice, identical)",
        "Almgren R, Chriss N. Optimal Execution of Portfolio Transactions. Author version dated "
        "December 2000 (read in full: sections 1.1-2.3, eqs. 1-20); published Journal of Risk 3(2), "
        "2000/2001 (journal volume/pages seen only in search listings).",
        "Nevmyvaka Y, Feng Y, Kearns M. Reinforcement Learning for Optimized Trade Execution. ICML 2006 "
        "(NOT READ: author page blocked from this machine; cited as further reading only, nothing quoted).",
    ],
    "visual_policy": "Every chart and number is drawn from code/results.json at render time. "
                     "'Synthetic market' is said in the narration and shown on every data beat. "
                     "No logos except the HAI mark on the outro; no person icons.",
    "library_check": "./art scenes --check: ClaudeComposerAsk, ClaudeComposerAsk916, "
                     "BrutalistHesitantWriter all RENDERABLE. Body beats are custom Manim (sell "
                     "schedule bars, price fan, state table, cost bars) drawn from results.json.",
}


def rem(bid, act, narration, pattern, props, show):
    return {"beat_id": bid, "act": act, "narration_text": narration,
            "shot": {"type": "GRAPHIC", "source": "remotion", "lane": "bookend",
                     "motion": "illustrate", "show": show,
                     "remotion": {"pattern": pattern, "props": props}}}


def man(bid, act, narration, scene, intent, show):
    return {"beat_id": bid, "act": act, "narration_text": narration,
            "visual_intent": intent,
            "shot": {"type": "GRAPHIC", "source": "manim", "lane": "manim", "motion": "illustrate",
                     "show": show, "manim": {"scene_class": scene, "file": "scenes.py"}}}


ASK = "How should an AI sell 10,000 shares without moving the price against it?"
ASK_OUT = ["all at once: the price drops under you",
           "equal slices: the price can drift away",
           "learned schedule: sell more early, then taper"]

LANDSCAPE = [
    rem("B00", "INTRO",
        "Hi, I am Boopesh M., and this video is about how an AI sells a big order, using "
        "reinforcement learning. This is an AI voice reading my script.",
        "ClaudeComposerAsk",
        dict(COMPOSER, greeting="Hi, Boopesh", command=ASK,
             runningText="simulating a synthetic market…", output=ASK_OUT),
        [{"at": 0.1, "event": "the ask types into the composer under 'Hi, Boopesh'"},
         {"at": 0.45, "event": "three result lines land: all at once, equal slices, learned schedule"},
         {"at": 0.8, "event": "the AI-voice disclosure is spoken over the answered composer"}]),
    rem("B10", "OVERVIEW",
        "Here's the idea. Dumping a big order all at once pushes the price against you. Selling "
        "it in slices costs less, and an AI can learn how big each slice should be.",
        "BrutalistHesitantWriter",
        {"text": "Sell a big order all at once.", "face": "serif", "fontSize": 104,
         "lineSpacing": 1.3, "align": "center", "ink": "#2B2A26", "accent": "#A64B2A",
         "bg": "#FAF9F5", "triggerWords": "all at once", "replacementWords": "in slices",
         "mistakeRate": 4, "charMs": 45, "hesitateBetween": 15, "seed": "boopesh-big-order",
         "yOffset": -40, "contextTitle": TITLE,
         "contextItems": [{"label": "Impact", "detail": "one big sale pushes the price down"},
                          {"label": "Risk", "detail": "waiting lets the price wander"},
                          {"label": "The agent", "detail": "learns the size of each slice"}]},
        [{"at": 0.05, "event": "'Sell a big order all at once.' types in the serif"},
         {"at": 0.3, "event": "'all at once' turns accent, pauses, deletes; 'in slices' types in"},
         {"at": 0.6, "event": "the corrected line holds above three cards: impact, risk, the agent"}]),
    man("B20", "THE PROBLEM",
        f"Say you need to sell ten thousand shares at fifty dollars. Buyers at the best price only "
        f"want so many, so one huge order walks the price down. In my synthetic market, dumping them "
        f"all gets forty-nine fifty a share. That costs five thousand dollars, or "
        f"{words(S['dump']['mean_bps'])} basis points. That's market impact.",
        "B20_Impact",
        "One tall accent bar '10,000 shares, all at once' at step 1 of a 10-step time axis; a price "
        "line beside it steps from $50.00 down to $49.50 as the bar lands; a cost card: $5,000 = 100 bps. "
        "Tag: SYNTHETIC MARKET.",
        [{"at": "ten thousand shares", "event": "the empty 10-step axis is there as a ghost; one tall bar rises at step 1"},
         {"at": "walks the price down", "event": "the price marker slides from $50.00 to $49.50"},
         {"at": "five thousand dollars", "event": "cost card lights: $5,000 = 100 bps (accent number)"}]),
    man("B30", "THE OTHER RISK",
        "So slice it instead: ten equal pieces, one per time step. Small orders barely move the "
        "price, so impact falls about ten times. But now you hold shares longer, and the price keeps "
        "wandering. On a bad day it drifts down while you wait. That's the other risk.",
        "B30_Drift",
        "Ten equal teal bars (1,000 each) fill the time axis; above them a fan of 40 simulated price "
        "paths from the same random walk spreads wider with time; one bad-day path is drawn in accent.",
        [{"at": "ten equal pieces", "event": "ten equal teal bars grow left to right"},
         {"at": "about ten times", "event": "impact chip: 100 bps -> 10 bps"},
         {"at": "keeps wandering", "event": "simulated price paths fan out over the ten steps"},
         {"at": "On a bad day", "event": "one low path turns accent"}]),
    man("B40", "THE AGENT",
        "Enter reinforcement learning. The agent sees just two things: time left and shares left. "
        f"Each step, it picks what fraction to sell now. Its score is the cash it gets, minus a small "
        f"penalty for shares it still holds. It practiced {words(DAYS)} times on simulated days, "
        f"keeping a table of what paid off.",
        "B40_Agent",
        "A table: columns = time steps left (10..1), rows = shares left; one cell lights as the state; "
        "an action strip 0%..100% with one choice picked; a score line; a practice counter to 40,000,000.",
        [{"at": "time left and shares left", "event": "the two table axes light"},
         {"at": "what fraction to sell now", "event": "action strip: one fraction is picked, the cell moves"},
         {"at": "Its score", "event": "score line: cash received - small penalty for shares held"},
         {"at": "It practiced", "event": "counter runs to 40,000,000; cells fill in"}]),
    man("B50", "WHAT IT LEARNED",
        "Here's what it learned: sell more early, then taper off. The dots are the textbook answer "
        "for this exact model, the Almgren and Chriss formula from 2000. The agent never saw that "
        "formula, and its bars land close to it.",
        "B50_Schedule",
        "Ten teal bars = the learned schedule (from results.json); ten accent dots = the Almgren-Chriss "
        "closed form; the one formula x_j = X sinh(kappa(T - t_j)) / sinh(kappa T) typeset beside it.",
        [{"at": "sell more early", "event": "the learned bars grow, tall at the start, tapering"},
         {"at": "The dots", "event": "the closed-form dots drop onto the bars; the formula appears"},
         {"at": "land close to it", "event": "gap readout: within 1.7% on cost plus risk"}]),
    man("B60", "THE TEST",
        f"Then I tested all three on {words(TEST)} new simulated days. All at once: "
        f"{words(S['dump']['mean_bps'])} basis points, every time. Equal slices: about "
        f"{words(TWAP_MEAN)} on average, but one day in twenty costs {words(TWAP_P95)} or more. The agent "
        f"pays a little more on average, about {words(RL_MEAN)}, and that bad-day line drops to about "
        f"{words(RL_P95)}.",
        "B60_Costs",
        "Three rows, one per strategy: an average-cost bar and a bad-day (95th percentile) tick, in bps, "
        "on held-out simulated days. The agent's bad-day number is the accent.",
        [{"at": "All at once", "event": "row 1: a 100 bps bar fills the axis"},
         {"at": "Equal slices", "event": "row 2: short 10 bps bar, bad-day tick at 65"},
         {"at": "The agent", "event": "row 3: 13 bps bar, bad-day tick at 54 (accent)"}]),
    man("B70", "TAKEAWAY",
        "A big order is a trade-off: sell fast and pay impact, or sell slowly and carry risk. "
        "The agent learned the balance from practice. But this was a synthetic market. Real markets "
        "have order books, other traders who react, and sudden jumps. For the research version, see "
        "Nevmyvaka, Feng and Kearns, from 2006.",
        "B70_Takeaway",
        "Dark takeaway beat: a balance with 'impact' and 'risk' on its pans settling level; a caveat card "
        "'synthetic market' listing what real markets add; a further-reading line.",
        [{"at": "a trade-off", "event": "the balance tips, then settles level"},
         {"at": "synthetic market", "event": "caveat card lights: what real markets add"},
         {"at": "For the research version", "event": "further-reading line lands"}]),
    rem("B80", "YOUR TURN",
        "Your turn. Paste this into Claude: numpy code that sells ten thousand shares over ten steps, "
        "comparing all at once, equal slices and a Q-learning agent. Before you run it, guess: if "
        "impact doubles, does the agent sell faster or slower at the start?",
        "ClaudeComposerAsk",
        dict(COMPOSER, greeting="Your turn.",
             command="Write numpy code that sells 10,000 shares over 10 steps with price impact. "
                     "Compare all at once, equal slices and a Q-learning agent. Then double the "
                     "impact: does the agent sell faster or slower at the start?",
             runningText="guess first, then run it…"),
        [{"at": 0.15, "event": "the suggested prompt types into the composer"},
         {"at": 0.6, "event": "the prompt holds while the voice explains the guess-first task"}]),
    man("B90", "OUTRO",
        f"{TITLE}. Built with Claude, for Humanitarians AI. Subscribe for next week's video.",
        "B90_Outro",
        "Manim outro: film title, SUBSCRIBE pill, HAI mark + @HumanitariansAI, credit lines, narration "
        "and data-source lines.",
        [{"at": 0.1, "event": "title and HAI mark land"},
         {"at": "Subscribe", "event": "SUBSCRIBE pill presses"}]),
]

SHORT = [
    rem("B00", "INTRO",
        "Hi, I am Boopesh M., and this video is about how an AI sells a big order. This is an AI "
        "voice reading my script.",
        "ClaudeComposerAsk916",
        dict(COMPOSER, greeting="Hi, Boopesh", command=ASK,
             runningText="simulating a synthetic market…", output=ASK_OUT),
        [{"at": 0.1, "event": "the ask types into the portrait composer"},
         {"at": 0.5, "event": "three result lines land"}]),
    man("B20", "THE PROBLEM",
        f"Sell ten thousand shares at once, and you push the price down. In my synthetic market, that "
        f"costs {words(S['dump']['mean_bps'])} basis points. Sell in equal slices instead, and the "
        f"price can drift while you wait.",
        "B20_Problem",
        "Portrait: a tall accent bar 'all at once' with cost 100 bps; below, ten equal teal bars with a "
        "fan of simulated price paths drifting.",
        [{"at": "at once", "event": "the one tall bar lands; price $50.00 -> $49.50"},
         {"at": "equal slices", "event": "ten small bars; the price paths fan out"}]),
    man("B30", "WHAT IT LEARNED",
        f"So a Q-learning agent practiced {words(DAYS)} times on simulated days. It learned to sell "
        f"more early, then taper off, close to the Almgren and Chriss formula.",
        "B30_Schedule",
        "Portrait: learned schedule as ten teal bars, Almgren-Chriss closed form as accent dots, the "
        "one formula above.",
        [{"at": "practiced", "event": "counter to 40,000,000"},
         {"at": "sell more early", "event": "bars grow, tapering"},
         {"at": "Almgren and Chriss", "event": "dots drop onto the bars"}]),
    man("B40", "THE TEST",
        f"On {words(TEST)} new days, it averaged about {words(RL_MEAN)} basis points, and its bad days "
        f"stayed lower than equal slices.",
        "B40_Costs",
        "Portrait: three cost rows (average bar + bad-day tick); the agent's bad-day number in accent.",
        [{"at": "averaged", "event": "three rows fill"},
         {"at": "bad days", "event": "bad-day ticks: 65 vs 54 (accent)"}]),
    man("B50", "TAKEAWAY",
        "The trade-off is impact versus risk. And remember, this is a synthetic market, not a real one.",
        "B50_Takeaway",
        "Dark portrait takeaway: 'impact vs risk' balance, 'synthetic market' caveat card.",
        [{"at": "impact versus risk", "event": "the balance settles"},
         {"at": "synthetic market", "event": "caveat card lights"}]),
    man("B90", "OUTRO",
        f"{TITLE}. Subscribe to Humanitarians AI.",
        "B90_Outro",
        "Portrait Manim outro: title, SUBSCRIBE pill, HAI mark + @HumanitariansAI, credits.",
        [{"at": 0.1, "event": "title and HAI mark land"},
         {"at": "Subscribe", "event": "SUBSCRIBE pill presses"}]),
]

KEEP_BEAT = ("actual_duration_s", "audio_file", "build", "render_duration_s")


def write(folder, beats, extra_meta):
    path = folder / "beat_sheet.json"
    old = json.loads(path.read_text()) if path.exists() else {"metadata": {}, "beats": []}
    oldb = {b["beat_id"]: b for b in old.get("beats", [])}
    meta = dict(META, **extra_meta)
    for k in ("approvals", "build"):
        if k in old.get("metadata", {}):
            meta[k] = old["metadata"][k]
    for b in beats:
        o = oldb.get(b["beat_id"])
        words_n = len(b["narration_text"].split())
        b["estimated_duration_s"] = round(words_n / 2.6 + 0.8, 1)
        if o and o.get("narration_text") == b["narration_text"]:
            for k in KEEP_BEAT:
                if k in o:
                    b[k] = o[k]
            orem = (o.get("shot") or {}).get("remotion") or {}
            if "rendered" in orem and (b["shot"].get("remotion") or {}).get("props") is not None:
                b["shot"]["remotion"]["rendered"] = orem["rendered"]
        rem_ = b["shot"].get("remotion")
        if rem_ is not None:
            d = b.get("actual_duration_s") or b["estimated_duration_s"]
            rem_["props"]["durationSeconds"] = float(d)
    total = sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in beats)
    meta["total_estimated_duration_seconds"] = round(total, 2)
    path.write_text(json.dumps({"metadata": meta, "beats": beats}, indent=2, ensure_ascii=False) + "\n")
    print(f"{path}: {len(beats)} beats, ~{total:.1f}s")
    return total


if __name__ == "__main__":
    t1 = write(REEL, LANDSCAPE, {"aspect_ratio": "16:9", "resolution": "3840x2160"})
    t2 = write(REEL / "short", SHORT, {
        "aspect_ratio": "9:16", "resolution": "2160x3840", "slug": SLUG + "-short",
        "kind": "short", "derived_from": SLUG,
        "reformat": "native portrait: its own beat sheet and scenes, never a crop",
        "short_validation": {"status": "ready", "errors": []}})
    assert t1 < 180 and t2 < 180
