# Writes beat_sheet.json (16:9) for "What Got in the Way" -- Boopesh M., HAI progress video, week of Nov 8-14 2026.
# Every number spoken comes from code/results.json (python3 code/week_stats.py); the asserts below keep
# the script honest if the data is re-run.
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = json.loads((HERE / "code" / "results.json").read_text())
T, L, CMP, FR = R["this_week"], R["last_week"], R["comparison"], R["friction"]
assert (FR["logs_added"], FR["fellows"], FR["logs_describing_obstacles"]) == (32, 13, 31)
assert FR["theme_logs"] == {"layout & picture checks": 19, "facts & data": 11, "length & time": 10,
                            "tools & setup": 10, "timing & pacing": 8, "voice & pronunciation": 5}
assert FR["theme_fellows"]["layout & picture checks"] == 8
assert (FR["found_by_looking_logs"], len(FR["logs_with_no_theme"])) == (17, 2)
assert [e["theme"] for e in R["examples"]] == ["layout & picture checks", "facts & data", "length & time",
                                               "tools & setup", "timing & pacing"]
assert {k: (v["last_week"], v["this_week"]) for k, v in CMP.items() if k in
        ("merged_prs", "new_work_folders", "fellows_with_new_folders", "frictional_logs_added")} == \
    {"merged_prs": (27, 19), "new_work_folders": (75, 53), "fellows_with_new_folders": (19, 17),
     "frictional_logs_added": (95, 32)}
assert (T["merged_prs"]["merge_commits"], T["merged_prs"]["squash_merges"]) == (19, 0)
assert R["last_week_published_vs_recounted"]["published_2026_11_08_at_a953b021"] == [26, 74, 18, 95]
D = R["boopesh"]["last_week_deliveries"]
assert [D[k]["mm_ss"] for k in ("landscape/WhatTheFellowsTaught_BoopeshM.mp4", "vertical/WhatTheFellowsTaught_BoopeshM.mp4",
                                "landscape/BacktestMirage_BoopeshM.mp4", "vertical/BacktestMirage_BoopeshM.mp4")] \
    == ["2:15", "0:50", "2:24", "0:45"]
assert all((v["width"], v["height"]) in ((3840, 2160), (2160, 3840)) for v in D.values())
assert R["boopesh"]["folder_on_main"] is False

VOICE = "am_onyx"
HAI = "@HumanitariansAI"
TOPIC = "Irreducibly Human"
SEG = "What Got in the Way"


def composer(greeting, command, output, running):
    return {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
            "remotion": {"pattern": "ClaudeComposerAsk", "props": {
                "greeting": greeting, "topic": TOPIC, "segment": SEG,
                "command": command, "runningText": running,
                "folderLabel": HAI, "modelLabel": "Claude", "effortLabel": "High",
                "output": output}, "rendered": {"out": "", "at": ""}}}


def manim(cls):
    return {"type": "GRAPHIC", "source": "manim", "motion": "fade",
            "manim": {"scene_class": cls, "file": "scenes.py"}}


def beat(bid, act, note, text, shot, **kw):
    b = {"beat_id": bid, "act": act, "role_note": note, "narration_text": text,
         "shot": shot, "voice": VOICE, "engine": "kokoro", "voice_kokoro": VOICE}
    b.update(kw)
    return b


beats = [
  beat("B00", "INTRO", "COLD OPEN -- required fellow intro line + AI-voice disclosure; ask lands answered",
       "Hi, I am Boopesh M., and this video is about what got in the way for the Humanitarians AI fellows this week, "
       "November eighth to the fourteenth. A quick note: this is an AI voice reading my script. "
       "Every number comes from the git history and the fellows' own frictional logs, counted by a small script.",
       composer("Hi, Boopesh",
                "What got in the way for the Humanitarians AI fellows from Nov 8 to Nov 14? Read their frictional logs.",
                ["32 frictional logs from 13 fellows · 31 describe obstacles",
                 "top theme: layout & picture checks, in 19 logs",
                 "17 logs: the problem was found by someone looking"],
                "reading the frictional logs…")),
  beat("B10", "OVERVIEW", "BLUF -- hesitant writer corrects the misconception",
       "Here's the week in one line. You might guess the hardest part was installing the tools. "
       "But the most common obstacle was checking the result.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "BrutalistHesitantWriter", "props": {
            "text": "The hardest part was installing the tools.",
            "face": "serif", "fontSize": 60, "lineSpacing": 1.3, "align": "center",
            "triggerWords": "installing the tools",
            "replacementWords": "checking the result",
            "mistakeRate": 4, "hesitateWithin": 2, "hesitateBetween": 14,
            "charMs": 45, "jitter": 20, "seed": "boopesh-week-05", "showCaret": True,
            "contextTitle": "The week in one line",
            "contextItems": [
                {"label": "Nov 8–14", "detail": "32 frictional logs, 13 fellows"},
                {"label": "Top theme", "detail": "layout & picture checks, 19 logs"}]},
            "rendered": {"out": "", "at": ""}}},
       lead_silence_s=0.5),
  beat("B20", "THEMES", "31 logs with obstacles sorted into six plain themes (rough keyword sort), bar chart",
       "Thirty-two frictional logs were added this week, by thirteen fellows, and thirty-one describe obstacles. "
       "I sorted them by keywords into six plain themes. It's my rough sort, and one log can land in several. "
       "Layout and picture checks led, in nineteen logs from eight fellows: "
       "things running off the edge, overlapping, or too small to read. "
       "Then facts and data, in eleven. Length and time, ten. Tools and setup, ten. "
       "Timing and pacing, eight. And the AI voice saying a word wrong, five.",
       manim("B20_Themes")),
  beat("B30", "EXAMPLES", "five short paraphrased examples, obstacle -> fix, one per theme, folder names only",
       "A few examples, in my words. A chart passed the frame checks, but showed the opposite of the narration. "
       "A working title didn't survive the data, so the title changed. "
       "A script ran four minutes twenty-two for a four-minute slot, and was trimmed five times without cutting a number. "
       "A checking script took over forty minutes; now it streams frames, in eighty-seven seconds. "
       "And words on screen appeared late, until each reveal was timed to the voice.",
       manim("B30_Examples")),
  beat("B40", "WHAT FIXED IT", "what fixed them: 17 of 31 logs found a problem by looking; the takeaway",
       "So what fixed them? Most often, someone looked. "
       "In seventeen of the thirty-one logs, a problem was found by watching the cut, viewing the frames, "
       "or re-reading the words. A passing check tells you the frame fits. Only looking tells you it's right.",
       manim("B40_Looked")),
  beat("B50", "COMPARE", "ONE comparison with last week (same script, recounted today)",
       "One comparison with last week, recounted today by the same script. "
       "Merged pull requests: nineteen, down from twenty-seven. New work folders: fifty-three, from seventy-five. "
       "Fellows with new folders: seventeen, from nineteen. "
       "And frictional logs: thirty-two, from ninety-five.",
       manim("B50_Compare")),
  beat("B60", "MY PART", "Boopesh's own two videos last week; delivered for review; his own obstacle: access",
       "And my part. Last week I made two videos. What the Fellows Taught runs two fifteen. "
       "The Backtest Mirage, on AI in finance, runs two twenty-four. "
       "Each has a Short, all four are 4K, delivered for review. "
       "My own obstacle is access: my fork attempt failed, so my pull request is still pending, "
       "and my folder isn't on main, or in these counts.",
       manim("B60_MyPart")),
  beat("B80", "YOUR TURN", "HANDOFF -- prompt read aloud and explained",
       "Your turn. With your own project open, paste this into Claude. "
       "Read my frictional log from this week. Sort what got in the way into three plain themes, "
       "and for each one, suggest one check I can do by eye before my next build. "
       "A good answer quotes the line each theme comes from.",
       composer("Your turn.",
                "Read my frictional log from this week. Sort what got in the way into three plain themes, and for "
                "each one, suggest one check I can do by eye before my next build. Quote the lines.",
                [], "paste this into Claude…")),
  beat("B90", "OUTRO", "HAI outro + fellow credit card (name, role, team; no invented links)",
       "What got in the way. With Boopesh M., for Humanitarians AI. Thanks for watching.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "What Got in the Way: Humanitarians AI, Nov 8-14",
    "slug": "what-got-in-the-way",
    "topic": "Irreducibly Human",
    "register": "Plain / Teardown-warm",
    "audience": "Humanitarians AI",
    "brand": "claude-hai",
    "channel_title": "",   # no burned-in footer text (review checklist); brand is in the composer chip + outro
    "creator": "Boopesh M.",
    "engine": "kokoro",
    "palette": "claude",
    "style_preset": "claude",
    "style": "claude-explainer",
    "voice_kokoro": VOICE,
    "voice_policy": "persistent-fellow-selected",
    "aspect_ratio": "16:9",
    "pronounce": {"Kokoro": "kˈoʊkəɹoʊ"},
    "brutalist_commit": "a99b5323",
    "note": "HAI progress video for Boopesh M., week of Nov 8-14 2026. Source: nikbearbrown/humanitarians-youtube "
            f"git history {T['base_commit']}..{T['head_commit']} and the frictional logs added in it "
            f"(code/week_stats.py -> code/results.json); last week {L['base_commit']}..{L['head_commit']} recounted "
            "by the same function. AI narration (Kokoro am_onyx) disclosed in B00.",
    "tags": ["Humanitarians AI", "fellows", "frictional log", "progress video", "what got in the way", "git",
             "quality checks", "Manim", "Remotion", "Claude"],
  },
  "beats": beats,
}
out = HERE / "beat_sheet.json"
if out.exists():   # keep approvals/build stamps written by the pipeline
    old = json.loads(out.read_text())
    for k in ("approvals", "build"):
        if k in old.get("metadata", {}):
            sheet["metadata"][k] = old["metadata"][k]
    prev = {b["beat_id"]: b for b in old.get("beats", [])}
    for b in beats:   # keep audio measurements when the spoken line is unchanged
        o = prev.get(b["beat_id"])
        if o and o.get("narration_text") == b["narration_text"]:
            for k in ("actual_duration_s", "audio_file", "render_duration_s", "build", "shot_rendered"):
                if k in o:
                    b[k] = o[k]
            if (o.get("shot", {}).get("remotion") or {}).get("rendered") and \
                    o["shot"]["remotion"].get("props") == b["shot"]["remotion"].get("props"):
                b["shot"]["remotion"]["rendered"] = o["shot"]["remotion"]["rendered"]
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print("wrote", out, len(beats), "beats", sum(len(b["narration_text"].split()) for b in beats), "words")
