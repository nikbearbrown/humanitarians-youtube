# Writes beat_sheet.json (16:9) for "What the Fellows Taught" -- Boopesh M., HAI progress video, week of Nov 1-7 2026.
# Every number spoken comes from code/results.json (python3 code/week_stats.py); the asserts below keep
# the script honest if the data is re-run.
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = json.loads((HERE / "code" / "results.json").read_text())
T, L, CMP = R["this_week"], R["last_week"], R["comparison"]
F = T["folders"]
assert (T["merged_prs"]["total"], T["merged_prs"]["merge_commits"], T["merged_prs"]["squash_merges"]) == (26, 25, 1)
assert (F["new_work_folders"], F["fellows_with_new_folders"], F["dated_inside_the_week"],
        F["dated_earlier_added_this_week"], F["undated_new_folders"]) == (74, 18, 28, 45, 1)
assert F["kinds"] == {"STEM / explainer video": 50, "progress / work video": 23, "hours log": 1}
assert F["stem_subjects"] == {"AI for product managers": 12, "testing & metrics": 10, "how AI models work": 9,
                              "making videos with AI": 8, "software & data tools": 5, "other topics": 4,
                              "AI in marketing & business": 2}
assert F["stem_subject_fellows"]["testing & metrics"] == 6 and F["stem_subject_fellows"]["AI for product managers"] == 1
assert {k: (v["last_week"], v["this_week"]) for k, v in CMP.items() if k in
        ("merged_prs", "new_work_folders", "fellows_with_new_folders", "frictional_logs_added")} == \
    {"merged_prs": (30, 26), "new_work_folders": (84, 74), "fellows_with_new_folders": (22, 18),
     "frictional_logs_added": (72, 95)}
D = R["boopesh"]["last_week_deliveries"]
assert [D[k]["mm_ss"] for k in ("landscape/OneWeekOfFellows_BoopeshM.mp4", "vertical/OneWeekOfFellows_BoopeshM.mp4",
                                "landscape/FraudAccuracyTrap_BoopeshM.mp4", "vertical/FraudAccuracyTrap_BoopeshM.mp4")] \
    == ["2:24", "0:47", "2:23", "0:53"]
assert all((v["width"], v["height"]) in ((3840, 2160), (2160, 3840)) for v in D.values())
assert R["boopesh"]["folder_on_main"] is False

VOICE = "am_onyx"
HAI = "@HumanitariansAI"
TOPIC = "Irreducibly Human"
SEG = "What the Fellows Taught"


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
       "Hi, I am Boopesh M., and this video is about what the Humanitarians AI fellows taught this week, "
       "November first to the seventh. A quick note: this is an AI voice reading my script. "
       "Every number comes from the git history, counted by a small script.",
       composer("Hi, Boopesh",
                "What did the Humanitarians AI fellows teach in their new work folders from Nov 1 to Nov 7?",
                ["74 new work folders from 18 fellows · 50 teach a topic",
                 "top subjects: AI for product managers 12 · testing & metrics 10 · how AI models work 9",
                 "vs last week: 26 pull requests (30) · 95 frictional logs (72)"],
                "reading the git log…")),
  beat("B10", "OVERVIEW", "BLUF -- hesitant writer corrects the misconception",
       "Here's the week in one line. You might expect a pile of status updates. "
       "But most new folders are lessons: fifty of seventy-four teach a topic.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "BrutalistHesitantWriter", "props": {
            "text": "This week's new folders were mostly status updates.",
            "face": "serif", "fontSize": 60, "lineSpacing": 1.3, "align": "center",
            "triggerWords": "status updates",
            "replacementWords": "lessons",
            "mistakeRate": 4, "hesitateWithin": 2, "hesitateBetween": 14,
            "charMs": 45, "jitter": 20, "seed": "boopesh-week-02", "showCaret": True,
            "contextTitle": "The week in one line",
            "contextItems": [
                {"label": "Nov 1–7", "detail": "74 new work folders, 18 fellows"},
                {"label": "Lessons", "detail": "50 STEM / explainer videos"}]},
            "rendered": {"out": "", "at": ""}}},
       lead_silence_s=0.5),
  beat("B20", "FOLDERS", "74 new work folders as a grid of squares, coloured by kind; dated strip",
       "Start with the folders. Seventy-four new work folders landed, from eighteen fellows. "
       "By my rough sort, fifty are STEM explainer videos, twenty-three are progress videos, "
       "and one is an hours log. Twenty-eight are dated this week. "
       "Forty-five are older work, filed this week.",
       manim("B20_Folders")),
  beat("B30", "SUBJECTS", "the 50 topic videos by subject (rough keyword sort), bar chart",
       "So what did they teach? I sorted the fifty topic videos by subject. "
       "Twelve teach AI to product managers: one fellow's full series. "
       "Ten are about testing and metrics, from six different fellows. "
       "Nine explain how AI models work. Eight are about making videos with AI. "
       "Five cover software and data tools, and the last six are marketing and other topics.",
       manim("B30_Subjects")),
  beat("B40", "TITLES", "six real titles dated this week, as cards with folder name + subject",
       "A few of the titles. Mixture of Experts. Goodhart's Law: when the proxy stops being the target. "
       "Integration Hell. Likely False, Likely True. RAG Explained for Product Managers. "
       "And Be the Sentence, about getting quoted by AI search.",
       manim("B40_Titles")),
  beat("B50", "COMPARE", "ONE comparison with last week (same script, same definitions)",
       "One comparison with last week, counted by the same script. "
       "Merged pull requests went from thirty to twenty-six. New work folders, from eighty-four to seventy-four. "
       "Fellows with new folders, from twenty-two to eighteen. "
       "But frictional logs went up, from seventy-two to ninety-five.",
       manim("B50_Compare")),
  beat("B60", "MY PART", "Boopesh's own two videos last week; delivered for review; GitHub PR pending (honest)",
       "And my part. Last week I made two videos. One Week of Fellows, a progress update, runs two twenty-four. "
       "The ninety-nine point nine percent Accuracy Trap, on AI fraud detection, runs two twenty-three. "
       "Each has a Short, and all four are 4K, delivered for review. "
       "My GitHub pull request is still pending: my fork attempt failed, so my folder isn't on main yet, "
       "and isn't in these counts.",
       manim("B60_MyPart")),
  beat("B70", "TAKEAWAY", "the concrete takeaway: turn a week of work into one lesson",
       "So here's the takeaway. Your weekly update can teach, too. "
       "Take one idea from your week, show one worked example, and say where it breaks. "
       "That's a lesson, not just a status report.",
       manim("B70_Takeaway")),
  beat("B80", "YOUR TURN", "HANDOFF -- prompt read aloud and explained",
       "Your turn. With your own project open, paste this into Claude. "
       "Find the one idea from my work this week that a newcomer would find hardest, "
       "and outline a two-minute explainer: the idea, one worked example, and where it breaks. "
       "A good answer points to the files where the idea shows up.",
       composer("Your turn.",
                "Find the one idea from my work this week that a newcomer would find hardest. Outline a "
                "2-minute explainer: the idea, one worked example, where it breaks. Point to the files.",
                [], "paste this into Claude…")),
  beat("B90", "OUTRO", "HAI outro + fellow credit card (name, role, team; no invented links)",
       "What the fellows taught. With Boopesh M., for Humanitarians AI. Thanks for watching.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "What the Fellows Taught: Humanitarians AI, Nov 1-7",
    "slug": "what-the-fellows-taught",
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
    "note": "HAI progress video for Boopesh M., week of Nov 1-7 2026. Source: nikbearbrown/humanitarians-youtube "
            f"git history {T['base_commit']}..{T['head_commit']} (code/week_stats.py -> code/results.json); last week "
            f"{L['base_commit']}..{L['head_commit']} recomputed by the same function. AI narration (Kokoro am_onyx) "
            "disclosed in B00.",
    "tags": ["Humanitarians AI", "fellows", "STEM explainers", "progress video", "teaching", "git",
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
            if (o.get("shot", {}).get("remotion") or {}).get("rendered") and \
                    o["shot"]["remotion"].get("props") == b["shot"]["remotion"].get("props"):
                b["shot"]["remotion"]["rendered"] = o["shot"]["remotion"]["rendered"]
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print("wrote", out, len(beats), "beats", sum(len(b["narration_text"].split()) for b in beats), "words")
