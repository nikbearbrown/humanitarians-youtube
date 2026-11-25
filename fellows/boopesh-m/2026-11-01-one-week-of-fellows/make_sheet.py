# Writes beat_sheet.json (16:9) for "One Week of Fellows" -- Boopesh M., HAI progress video, week of Oct 25-31 2026.
# Every number spoken comes from code/results.json (python3 code/week_stats.py); the asserts below keep
# the script honest if the data is re-run.
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = json.loads((HERE / "code" / "results.json").read_text())
P, C, F = R["merged_prs"], R["contributors"], R["folders"]
assert (P["total"], P["merge_commits"], P["squash_merges"]) == (30, 29, 1)
assert list(P["per_day"].values()) == [4, 4, 1, 5, 12, 4, 0] and P["busiest_day"] == "2026-10-29"
assert R["direct_commits_to_main"] == 35
assert (C["distinct_author_names_raw"], C["distinct_people_after_obvious_dedupe"],
        C["people_who_authored_non_merge_commits"]) == (37, 27, 23)
assert (F["new_work_folders"], F["fellows_with_new_folders"], F["dated_inside_the_week"],
        F["dated_earlier_added_this_week"], F["frictional_logs_added"], F["frictional_logs_fellows"]) == (84, 22, 27, 33, 72, 17)
assert F["kinds"] == {"STEM / explainer video": 42, "progress / work video": 30, "renewal request": 7,
                      "hours log": 3, "written / code work": 2}
assert R["boopesh"]["folder_on_main"] is False

VOICE = "am_onyx"
HAI = "@HumanitariansAI"
TOPIC = "Irreducibly Human"
SEG = "One Week of Fellows"


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
       "Hi, I am Boopesh M., and this video is about one week of fellows: what the Humanitarians AI fellows "
       "shipped into our shared YouTube repository, from October twenty-fifth to the thirty-first. "
       "A quick note: this is an AI voice reading my script. "
       "Every number comes from the git history, counted by a small script.",
       composer("Hi, Boopesh",
                "What did the Humanitarians AI fellows ship into humanitarians-youtube from Oct 25 to Oct 31?",
                ["30 pull requests merged · busiest day: Thursday, Oct 29 (12)",
                 "37 author names → 27 people · 22 fellow folders with new work",
                 "84 new work folders · 72 frictional logs"],
                "reading the git log…")),
  beat("B10", "OVERVIEW", "BLUF -- hesitant writer corrects the misconception",
       "Here's the week in one line. A fellow's week isn't one big video. "
       "It's a folder of small evidence, and this week, eighty-four new folders landed.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "BrutalistHesitantWriter", "props": {
            "text": "A week of work is one big video.",
            "face": "serif", "fontSize": 60, "lineSpacing": 1.3, "align": "center",
            "triggerWords": "one big video",
            "replacementWords": "a folder of small evidence",
            "mistakeRate": 4, "hesitateWithin": 2, "hesitateBetween": 14,
            "charMs": 45, "jitter": 20, "seed": "boopesh-week-01", "showCaret": True,
            "contextTitle": "The week in one line",
            "contextItems": [
                {"label": "Oct 25–31", "detail": "84 new work folders, 22 fellows"},
                {"label": "Evidence", "detail": "README, fact check, frictional log, source"}]},
            "rendered": {"out": "", "at": ""}}},
       lead_silence_s=0.5),
  beat("B20", "PULL REQUESTS", "7-day bar chart of merged PRs per day, from results.json",
       "Start with pull requests. Thirty were merged in seven days: twenty-nine merge commits, "
       "and one squash merge. Sunday and Monday had four each. "
       "Thursday, the twenty-ninth, was the busiest day, with twelve. Saturday had none. "
       "And thirty-five more commits went straight to main, without a pull request.",
       manim("B20_PerDay")),
  beat("B30", "PEOPLE", "37 names -> 27 people -> 23 authors, honest dedupe",
       "Who shipped it? The log shows thirty-seven author names. But one person often appears twice: "
       "a full name on one laptop, a GitHub handle on another. "
       "Merge only the obvious matches, same email or same account, and it's twenty-seven people. "
       "Twenty-three of them wrote the work. The rest only merged it. "
       "Two more pairs look alike, but I left them separate.",
       manim("B30_People")),
  beat("B40", "WORK TYPES", "84 new work folders by kind (heuristic sort) + when they were dated",
       "What did they ship? Eighty-four new work folders, from twenty-two fellows. "
       "By my rough sort: forty-two STEM explainer videos, thirty progress videos, "
       "seven renewal requests, three hours logs, and two pieces of written or code work. "
       "Twenty-seven are dated this week. Thirty-three are older work, filed this week.",
       manim("B40_WorkTypes")),
  beat("B50", "TITLES", "a few real titles as cards + the most common topic words",
       "A few of the titles. What is R L H F? Encrypted Twice. Right Answer, Wrong Chain. Ads in the Picture. "
       "The most common topic word is physics, from one fellow's twelve-week physics engine series. "
       "After that come agents, and memory.",
       manim("B50_Titles")),
  beat("B60", "MY PART", "Boopesh's own two videos; Drive submitted, GitHub PR pending (honest)",
       "And my part. Last week I made two videos: a progress update, Brutalist, Shared, at two minutes thirteen, "
       "and a STEM explainer, Deep Hedging, at two thirty-three. Each has a Short, and all four are 4K. "
       "They're submitted to Drive. My GitHub pull request is still pending: my fork attempt failed, "
       "so I'm asking the maintainer for access. That's why my folder isn't in these numbers yet.",
       manim("B60_MyPart")),
  beat("B70", "TAKEAWAY", "the concrete takeaway: what a good weekly folder contains",
       "So here's the takeaway. Small weekly evidence adds up. A good weekly folder is small and complete: "
       "a README with the result, a fact check, a frictional log of what resisted, and the source that "
       "rebuilds the video. Seventy-two frictional logs landed this week alone.",
       manim("B70_Takeaway")),
  beat("B80", "YOUR TURN", "HANDOFF -- prompt read aloud and explained",
       "Your turn. With your own repository open, paste this into Claude. "
       "Read my git log for the last seven days, and turn it into a five-beat outline for a progress video: "
       "what I shipped, what's still pending, and what's missing. "
       "A good answer cites the commit hashes, and says plainly what isn't merged yet.",
       composer("Your turn.",
                "Read my git log for the last 7 days and turn it into a 5-beat progress-video outline: "
                "what I shipped, what's still pending, what's missing. Cite the commit hashes.",
                [], "paste this into Claude…")),
  beat("B90", "OUTRO", "HAI outro + fellow credit card (name, role, team; no invented links)",
       "One week of fellows. With Boopesh M., for Humanitarians AI. Thanks for watching.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "One Week of Fellows: what Humanitarians AI shipped, Oct 25-31",
    "slug": "one-week-of-fellows",
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
    "note": "HAI progress video for Boopesh M., week of Oct 25-31 2026. Source: nikbearbrown/humanitarians-youtube "
            "git history c9fca929..bc722c05 (code/week_stats.py -> code/results.json). AI narration (Kokoro am_onyx) "
            "disclosed in B00.",
    "tags": ["Humanitarians AI", "fellows", "git", "pull requests", "progress video", "open source",
             "frictional log", "Manim", "Remotion", "Claude"],
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
            if (o.get("shot", {}).get("remotion") or {}).get("rendered"):
                b["shot"]["remotion"]["rendered"] = o["shot"]["remotion"]["rendered"]
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print("wrote", out, len(beats), "beats", sum(len(b["narration_text"].split()) for b in beats), "words")
