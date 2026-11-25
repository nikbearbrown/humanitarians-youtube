#!/usr/bin/env python3
"""make_sheet.py -- writes beat_sheet.json (16:9) and short/beat_sheet.json (9:16).

Every number spoken or shown comes from code/results.json (written by
code/week_stats.py). Numbers are spelled from the results here and asserted
against them, so a stale or edited narration cannot drift from the data.

Re-running is safe: human approval records, build stamps, measured audio
(actual_duration_s / audio_file) and Remotion render stamps are carried over
from the existing sheet, the audio ones only while a beat's narration is
unchanged (changed narration must be re-voiced).

Usage: python3 make_sheet.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = json.loads((HERE / "code" / "results.json").read_text())
S, TW, LW = R["summary"], R["this_week"], R["last_week_recount"]
PUB, LATE = R["last_week_published"], R["late_merge_check"]

ONES = ("zero one two three four five six seven eight nine ten eleven twelve thirteen "
        "fourteen fifteen sixteen seventeen eighteen nineteen").split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def w(n):
    """Spell 0..99 for the narrator (Kokoro reads words more steadily than digits)."""
    assert isinstance(n, int) and 0 <= n < 100, n
    if n < 20:
        return ONES[n]
    t, o = divmod(n, 10)
    return TENS[t] + ("" if o == 0 else "-" + ONES[o])


pc = {lab: n for lab, n in S["piece_counts_sorted"]}
N = {
    "prs": TW["merged_prs"], "folders": TW["new_work_folders"], "fellows": TW["fellows"],
    "pieces": S["n_pieces"], "beat": pc["beat sheet"], "fric": pc["FRICTIONAL log"],
    "readme": pc["README"], "desc": pc["description"], "proof": pc["PROOF"],
    "max": S["max_pieces"], "at_max": S["folders_at_max_count"], "all": S["folders_with_all_pieces"],
    "lw_prs": LW["merged_prs"], "lw_fric": LW["frictional_logs"], "lw_folders": LW["new_work_folders"],
    "pub_prs": PUB["merged_prs"], "pub_fric": PUB["frictional_logs"],
}
# The story's claims, asserted against the run (fail loudly if the data changed).
assert S["least_common"][0] == "PROOF" and S["most_common"][0] == "beat sheet"
assert S["missing_from_every_top_folder"] == ["PROOF"]
assert N["all"] == 0 and N["max"] == 8 and N["pieces"] == 9
assert [lab for lab, _ in S["piece_counts_sorted"][-2:]] == ["description", "PROOF"]
assert R["recount_differs"] and LATE["merged_prs"] == PUB["merged_prs"]
assert LATE["frictional_logs_all_dirs"] == PUB["frictional_logs"]
assert R["boopesh_m_on_main"] is False
EX1 = "fellows/rohan-v/2026-11-20-how-auto-tune-works"
EX2 = "fellows/likhith-r/2026-11-14-word2vec-king-man-woman-queen"
assert EX1 in S["folders_at_max"] and EX2 in S["folders_at_max"]

TITLE = "What a Finished Folder Looks Like"
TOPIC = "Irreducibly Human"
APPROVED_WORDS = "I approve am_onyx as my narrator voice."
# Boopesh's own sign-off (chat, 2026-10-24), bound to the fingerprint printed by
# `./art approvals <reel> --fingerprints` (engine kokoro + voice am_onyx). The time of
# day was not recorded, so the record carries the date at 00:00 New York time.
VOICE_APPROVAL = {
    "status": "approved",
    "reviewer_type": "human",
    "reviewed_by": "Boopesh M.",
    "reviewed_at": "2026-10-24T00:00:00-04:00",
    "subject_sha256": "9fbee75cc6f2e9898f416028987763bde5975fea9179425289a870171991c85e",
    "note": f'Approved in chat on 2026-10-24: "{APPROVED_WORDS}" (date from the chat; time of day not recorded).',
}

COMMON_META = {
    "title": TITLE,
    "topic": TOPIC,
    "channel_title": "",
    "creator": "Boopesh M.",
    "brand": "claude-hai",
    "palette": "claude",
    "engine": "kokoro",
    "voice_kokoro": "am_onyx",
    "voice_policy": "persistent-fellow-selected",
    "folderLabel": "@HumanitariansAI",
    "audience": "Humanitarians AI",
    "register": "Plain",
    "pronounce": {"Kokoro": "kˈoʊkəɹoʊ"},
    "data": "code/results.json (code/week_stats.py over humanitarians-youtube main @ "
            + R["ref"][:8] + ", window Nov 15-21 2026 America/New_York)",
}


def composer(pattern, greeting, command, running, output, segment=TITLE):
    return {"type": "REMOTION", "source": "own", "lane": "bookend", "motion": "fade",
            "remotion": {"pattern": pattern, "props": {
                "command": command, "topic": TOPIC, "segment": segment,
                "greeting": greeting, "runningText": running, "output": output,
                "folderLabel": "@HumanitariansAI", "modelLabel": "Claude"}}}


def manim(scene):
    return {"type": "GRAPHIC", "source": "manim", "lane": "manim", "motion": "manim",
            "manim": {"scene_class": scene, "file": "scenes.py"}}


INTRO = ("Hi, I am Boopesh M., and this video is about what a finished folder looks like: "
         "the paperwork beside each piece of fellows' work. This is an AI voice reading my script, "
         "and I asked Claude to count that paperwork in this past week's git history.")

ASK = 'claude "check every new fellows folder from Nov 15-21 for the nine pieces of paperwork"'
ASK_OUT = [
    f"{N['prs']} merged PRs · {N['folders']} new work folders · {N['fellows']} fellows",
    f"most common: beat_sheet.json in {N['beat']} of {N['folders']}",
    f"least common: PROOF.md in {N['proof']} of {N['folders']}",
]

TURN_CMD = ("List every file in this folder. Check it against these nine: README.md, FACTCHECK.md, "
            "FRICTIONAL.md, PROOF.md, SHOTLIST.md, PROMPTS.md, beat_sheet.json, code/, description.txt. "
            "Tell me which are missing, then draft the shortest missing one.")

LANDSCAPE = [
    ("B00", "INTRO", INTRO,
     composer("ClaudeComposerAsk", "Hi, Boopesh", ASK, "reading the git history…", ASK_OUT)),
    ("B10", "THE WEEK",
     f"This past week, November fifteenth to twenty-first, {w(N['prs'])} pull requests merged into main. "
     f"With direct uploads, {w(N['folders'])} new dated work folders landed, from {w(N['fellows'])} fellows. "
     "Each folder is one piece of work, almost always a video and its notes.",
     manim("B10_TheWeek")),
    ("B20", "NINE PIECES",
     f"A finished folder carries {w(N['pieces'])} pieces: a README, a fact-check, a frictional log, "
     "a proof self-review, a shot list, the prompts, the beat sheet, the code behind the numbers, "
     "and an upload description. My script checked every folder for each one, by file name.",
     manim("B20_NinePieces")),
    ("B30", "THE COUNT",
     f"The beat sheet is almost everywhere: {w(N['beat'])} of {w(N['folders'])} folders. "
     f"Frictional logs come next, at {w(N['fric'])}, then the README, at {w(N['readme'])}. "
     f"At the bottom, only {w(N['desc'])} have a description, and just {w(N['proof'])} have a proof self-review.",
     manim("B30_TheCount")),
    ("B40", "WHAT COMPLETE LOOKS LIKE",
     f"No folder had all {w(N['pieces'])}. {w(N['at_max']).capitalize()} folders had {w(N['max'])}, "
     "like how-auto-tune-works, and word-two-vec, king, man, woman, queen. Each holds the README, "
     "fact-check, frictional log, shot list, prompts, beat sheet, code and description. "
     f"The one gap in all {w(N['at_max'])}: the proof.",
     manim("B40_EightOfNine")),
    ("B50", "LAST WEEK, RECOUNTED",
     f"One comparison with the week before, re-counted with the same code: {w(N['lw_prs'])} pull requests, and "
     f"{w(N['lw_fric'])} of {w(N['lw_folders'])} folders with a frictional log. We published "
     f"{w(N['pub_prs'])} and {w(N['pub_fric'])}; one pull request merged late Saturday night, after that count. "
     f"This week: {w(N['fric'])} of {w(N['folders'])}.",
     manim("B50_LastWeek")),
    ("B60", "MY WEEK",
     "My own week. My last two videos were What Got in the Way, and Why Did the AI Say No?, "
     "on AI credit decisions. Both, and their Shorts, were delivered for review in 4K. "
     "My pull request is still pending: the fork attempt failed. And this week the build machine "
     "was wiped, so I rebuilt the toolkit from its own setup script first.",
     manim("B60_MyWeek")),
    ("B70", "TAKEAWAY",
     f"So, the takeaway. Before you open a pull request, check your folder for these {w(N['pieces'])} names. "
     "Start with the two most often missing: the proof self-review and the description. "
     "A folder with all nine shows the work, the checks and the friction, not just the video.",
     manim("B70_Takeaway")),
    ("B80", "YOUR TURN",
     "Your turn. Paste this into Claude inside your own work folder. It lists every file, "
     f"checks them against the {w(N['pieces'])} names, says which are missing, and drafts the shortest "
     "missing piece. You get a list for your folder, not a general reminder.",
     composer("ClaudeComposerAsk", "Your turn.", TURN_CMD,
              "paste this into Claude and run it in your own work folder…", [])),
    ("B90", "OUTRO", "I'm Boopesh M., a Humanitarians AI fellow on the Brutalist team. "
     "Thanks for watching, and please subscribe.", manim("B90_Outro")),
]

SHORT = [
    ("B00", "INTRO",
     "Hi, I am Boopesh M., and this video is about what a finished folder looks like. "
     "This is an AI voice reading my script.",
     composer("ClaudeComposerAsk916", "Hi, Boopesh", ASK, "reading the git history…", ASK_OUT[1:],
              segment="A Finished Folder")),   # the full title overruns the 9:16 title-safe edge
    ("B10", "THE COUNT",
     f"This past week, fellows added {w(N['folders'])} new work folders. I checked each one for "
     f"{w(N['pieces'])} pieces of paperwork. The beat sheet was in {w(N['beat'])}. "
     f"The proof self-review was in just {w(N['proof'])}.",
     manim("B10_TheCount")),
    ("B20", "EIGHT OF NINE",
     f"No folder had all {w(N['pieces'])}. {w(N['at_max']).capitalize()} had {w(N['max'])}, like "
     "how-auto-tune-works. It has the README, fact-check, frictional log, shot list, prompts, "
     "beat sheet, code and description. Its one gap, like the other seven: the proof.",
     manim("B20_EightOfNine")),
    ("B30", "TAKEAWAY",
     f"So before your next pull request, check your folder for these {w(N['pieces'])} names, "
     "and start with the two most often missing: the proof and the description.",
     manim("B30_Takeaway")),
    ("B90", "OUTRO", "I'm Boopesh M., a Humanitarians AI fellow. Thanks for watching, and please subscribe.",
     manim("B90_Outro")),
]
assert N["at_max"] - 1 == 7  # "like the other seven"


def check_ids(beats):
    for bid, *_ in beats:
        assert re.fullmatch(r"B[0-9]0", bid), bid       # B00, B10 ... B90 only
        assert bid not in ("B04", "B05", "B06"), bid


SPEED = 0.94   # Kokoro 1.0 reads brisk; the toolkit suggests ~0.94 for a steady read
KEEP_BEAT = ("actual_duration_s", "audio_file", "render_duration_s", "build")


def build(path, beats, extra_meta):
    check_ids(beats)
    old = json.loads(path.read_text()) if path.exists() else {"metadata": {}, "beats": []}
    old_beats = {b["beat_id"]: b for b in old.get("beats", [])}
    meta = dict(COMMON_META)
    meta.update(extra_meta)
    for k in ("approvals", "build", "total_render_duration_s"):
        if k in old.get("metadata", {}):
            meta[k] = old["metadata"][k]
    meta.setdefault("approvals", {}).setdefault("voice", VOICE_APPROVAL)
    out = []
    for bid, act, text, shot in beats:
        b = {"beat_id": bid, "act": act, "narration_text": text, "engine": "kokoro", "speed": SPEED,
             "lane": shot["lane"], "shot": shot,
             "estimated_duration_s": round(len(text.split()) / 2.6, 1)}
        ob = old_beats.get(bid)
        if ob and ob.get("narration_text") == text and ob.get("speed") == SPEED:
            for k in KEEP_BEAT:
                if k in ob:
                    b[k] = ob[k]
            rem_old = (ob.get("shot") or {}).get("remotion") or {}
            rem_new = shot.get("remotion")
            if rem_new and rem_old.get("rendered") and rem_old.get("props", {}).get("command") == rem_new["props"]["command"]:
                rem_new["rendered"] = rem_old["rendered"]
        if shot.get("remotion") and shot["remotion"]["pattern"] == "ClaudeComposerAsk" and b.get("actual_duration_s"):
            # the landscape composer sizes itself from durationSeconds (default 30 s)
            shot["remotion"]["props"]["durationSeconds"] = round(float(b["actual_duration_s"]) + 0.5, 2)
        out.append(b)
    total = sum(float(b.get("actual_duration_s") or b["estimated_duration_s"]) for b in out)
    meta["total_estimated_duration_seconds"] = round(total, 2)
    if meta.get("kind") == "short":
        meta["short_validation"] = {"status": "ready" if total < 180 else "blocked",
                                    "errors": [] if total < 180 else [f"{total:.1f}s >= 180s"]}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"metadata": meta, "beats": out}, indent=2, ensure_ascii=False) + "\n")
    print(f"{path.relative_to(HERE)}: {len(out)} beats, ~{total:.1f}s "
          f"({sum(len(b['narration_text'].split()) for b in out)} words)")


build(HERE / "beat_sheet.json", LANDSCAPE,
      {"slug": "finished-folder-master", "aspect_ratio": "16:9"})
build(HERE / "short" / "beat_sheet.json", SHORT,
      {"slug": "finished-folder-short-master", "aspect_ratio": "9:16", "kind": "short", "fit": "pad",
       "derived_from": "finished-folder-master",
       "reformat": "native portrait beat sheet and scenes (not a crop of the landscape master)"})
