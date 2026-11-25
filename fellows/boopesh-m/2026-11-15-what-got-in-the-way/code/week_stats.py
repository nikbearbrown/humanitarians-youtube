#!/usr/bin/env python3
"""
What got in the way: the obstacles Humanitarians AI fellows wrote down in the frictional logs they added to
nikbearbrown/humanitarians-youtube between 2026-11-08 00:00 and 2026-11-14 23:59:59 America/New_York
(EST, UTC-5, all week), with last week (Nov 1-7, DST ended Nov 1 02:00) recomputed by the SAME function.

Reused from last week's 2026-11-08-what-the-fellows-taught/code/week_stats.py unchanged: the PR rule
(first-parent "Merge pull request #N" commits + squash merges "... (#N)"), the new-work-folder rule (new
fellows/<fellow>/<folder> paths minus pure renames), the kind sort and the frictional-log rule (added files
matching friction*.md). New this week: a rough THEME sort of the obstacles inside this week's frictional logs.

Reads only git history (no network). Writes results.json next to this file.
Privacy: people appear only as fellow folder names (e.g. "rohan-v"); no email or surname is written.

usage: python3 week_stats.py [REPO] [REF]     (defaults: the humanitarians-youtube clone, origin/main)
"""
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/user/nikbearbrown/humanitarians-youtube")
REF = sys.argv[2] if len(sys.argv) > 2 else "origin/main"
NY = ZoneInfo("America/New_York")


def git(*a):
    return subprocess.run(["git", "-c", "gc.auto=0", "-C", str(REPO), *a], check=True, capture_output=True,
                          text=True).stdout


TIP = git("rev-parse", REF).strip()
SEP = "\x1f"
FMT = SEP.join(["%H", "%P", "%an", "%ae", "%cI", "%s"])


def log(*a):
    rows = []
    for line in git("log", f"--format={FMT}", *a).splitlines():
        h, p, an, ae, ci, s = line.split(SEP)
        rows.append({"sha": h, "parents": p.split(), "name": an, "email": ae,
                     "date": datetime.fromisoformat(ci).astimezone(NY), "subject": s})
    return rows


pr_merge = re.compile(r"^Merge pull request #(\d+)")
pr_squash = re.compile(r"\(#(\d+)\)\s*$")
DATED = re.compile(r"^(\d{4}-\d{2}-\d{2})")


def leaf(d):
    return d.split("/", 2)[2]


def readme_path(ref, d):
    files = git("ls-tree", "--name-only", ref, d + "/").splitlines()
    rd = [f for f in files if f.lower().endswith("/readme.md")]
    return rd[0] if rd else None


def readme_head(ref, d):
    rd = readme_path(ref, d)
    if not rd:
        return ""
    return " ".join(git("show", f"{ref}:{rd}").split()[:80]).lower()


def kind(ref, d):
    """Same rule as last week's script (folder name + first 80 words of README)."""
    name, rh = leaf(d).lower(), readme_head(ref, d) or (h1(ref, d) or "").lower()
    if "renewal" in name:
        return "renewal request"
    if "hours" in name:
        return "hours log"
    if "not a video" in rh or "written work" in rh:
        return "written / code work"
    if re.search(r"stem|explainer", name):
        return "STEM / explainer video"
    if re.search(r"week|weekly|progress|project-update|(^|\d-)work-|mycroft", name):
        return "progress / work video"
    if re.search(r"project update|weekly (work|update|research|implementation)|work video|work report|"
                 r"weekly progress|catch-up report|week \d+ summary", rh[:300]):
        return "progress / work video"
    return "STEM / explainer video"   # default: a topic video (STEM/AI explainer)


# rough SUBJECT sort of the topic videos: first matching rule wins, on folder name + title + the README's
# one-line description (metadata lines such as runtime/voice tables are skipped on purpose)
SUBJECTS = [
    ("AI for product managers", r"product manag|for product managers|\bai pms?\b|ai product"),
    ("making videos with AI", r"\bvoices?\b|caption|beat sheet|look at the frames|workflow is the lesson|"
                              r"show what broke|fluent isn|ai figures"),
    ("how AI models work", r"embedding|mixture of experts|\bmoe\b|deep sets|rlhf|\bdpo\b|probabilistic|diffusion|"
                           r"\bgpt\b|world model|transformer|neural|adversarial|\bvla\b"),
    ("testing & metrics", r"\beval|\btest\b|test that|metric|goodhart|verify|benchmark|both sides passed|"
                          r"likely false|got zero|causal"),
    ("software & data tools", r"continuous integration|ci/cd|github actions|jboss|kiro|\bide\b|index|job board|"
                              r"ticker|deploy"),
    ("AI in marketing & business", r"brand|marketing|influencer|\bseo\b|search everywhere|customer service|"
                                   r"social media"),
]


def blurb(ref, d):
    rd = readme_path(ref, d)
    if not rd:
        return ""
    seen_h1 = False
    for line in git("show", f"{ref}:{rd}").splitlines():
        s_ = line.strip()
        if s_.startswith("# "):
            seen_h1 = True
            continue
        if seen_h1 and s_ and not re.match(r"^[|*\-#>!<\[]", s_) and not s_.lower().startswith(("fellow", "date")):
            return s_[:300]
    return ""


def subject(ref, d, title):
    text = " ".join([leaf(d).replace("-", " "), (title or ""), blurb(ref, d)]).lower()
    for lab, rx in SUBJECTS:
        if re.search(rx, text):
            return lab
    return "other topics"


def h1(ref, d):
    rd = readme_path(ref, d)
    for line in (git("show", f"{ref}:{rd}").splitlines() if rd else []):
        if line.startswith("# "):
            return line[2:].strip()
    files = git("ls-tree", "--name-only", ref, d + "/").splitlines()
    bs = sorted(f for f in files if re.search(r"/beat_sheet[^/]*\.json$", f))   # no README: use the beat sheet's title
    if bs:
        try:
            return json.loads(git("show", f"{ref}:{bs[0]}")).get("metadata", {}).get("title")
        except Exception:
            return None
    return None


def level3(ref):
    out = git("ls-tree", "-d", "-r", "--name-only", ref, "fellows")
    return {p for p in out.splitlines() if p.count("/") == 2}


def week(start, end, tip=None):
    tip = tip or TIP
    head = git("rev-list", "-1", "--first-parent", f"--before={end.isoformat()}", tip).strip()
    base = git("rev-list", "-1", "--first-parent", f"--before={start.isoformat()}", tip).strip()
    landed = log(f"{base}..{head}")
    mainline = log("--first-parent", f"{base}..{head}")
    assert all(start <= c["date"] <= end for c in mainline), "a mainline commit falls outside the window"
    days = [(start + timedelta(days=i)).date() for i in range(7)]

    prs = []
    for c in mainline:
        m = pr_merge.match(c["subject"])
        if m:
            prs.append({"pr": int(m.group(1)), "kind": "merge commit", "sha": c["sha"][:8], "date": c["date"]})
        elif len(c["parents"]) == 1 and pr_squash.search(c["subject"]):
            prs.append({"pr": int(pr_squash.search(c["subject"]).group(1)), "kind": "squash merge",
                        "sha": c["sha"][:8], "date": c["date"]})
    per_day = Counter(p["date"].date() for p in prs)
    direct = [c for c in mainline if len(c["parents"]) == 1 and not pr_squash.search(c["subject"])]
    other_merges = [c for c in mainline if len(c["parents"]) > 1 and not pr_merge.match(c["subject"])]

    before, after = level3(base), level3(head)
    new_dirs = sorted(after - before)
    gone = sorted(before - after)
    status = git("diff", "-M", "--name-status", base, head, "--", "fellows/").splitlines()
    added, renamed_into = defaultdict(int), defaultdict(int)
    friction_added = []
    for line in status:
        parts = line.split("\t")
        st, path = parts[0], parts[-1]
        d = "/".join(path.split("/")[:3])
        if st == "A":
            added[d] += 1
            if re.search(r"/friction(al)?[^/]*\.md$", path, re.I):
                friction_added.append(path)
        elif st.startswith("R"):
            renamed_into[d] += 1
    renames = [d for d in new_dirs if renamed_into[d] > added[d]]
    real_new = [d for d in new_dirs if d not in renames]

    folders = []
    for d in real_new:
        m = DATED.match(leaf(d))
        k = kind(head, d)
        title = h1(head, d)
        folders.append({"folder": d.removeprefix("fellows/"), "fellow": d.split("/")[1],
                        "dated": m.group(1) if m else None, "kind": k, "title": title,
                        "subject": subject(head, d, title) if k == "STEM / explainer video" else None,
                        "files_added": added[d]})
    dated = [f for f in folders if f["dated"]]
    in_week = [f for f in dated if start.date().isoformat() <= f["dated"] <= end.date().isoformat()]
    kinds = Counter(f["kind"] for f in folders)
    stem = [f for f in folders if f["kind"] == "STEM / explainer video"]
    subjects = Counter(f["subject"] for f in stem)
    fellows_with_new = sorted({f["fellow"] for f in folders})
    per_fellow = Counter(f["fellow"] for f in folders)
    stem_fellows = Counter(f["fellow"] for f in stem)
    by_subject_fellows = {s: len({f["fellow"] for f in stem if f["subject"] == s}) for s in subjects}

    return {
        "window": {"start": start.isoformat(), "end": end.isoformat()},
        "base_commit": base[:8], "head_commit": head[:8],
        "base_subject": git("log", "-1", "--format=%s", base).strip(),
        "head_subject": git("log", "-1", "--format=%s", head).strip(),
        "head_date": git("log", "-1", "--format=%cI", head).strip(),
        "commits_landed": len(landed),
        "commits_on_main_first_parent": len(mainline),
        "merged_prs": {
            "total": len(prs),
            "merge_commits": sum(p["kind"] == "merge commit" for p in prs),
            "squash_merges": sum(p["kind"] == "squash merge" for p in prs),
            "per_day": {d.isoformat(): per_day.get(d, 0) for d in days},
            "busiest_day": max(days, key=lambda d: per_day.get(d, 0)).isoformat(),
            "pr_numbers": sorted(p["pr"] for p in prs),
            "list": [{"pr": p["pr"], "kind": p["kind"], "sha": p["sha"], "date_local": p["date"].isoformat()}
                     for p in sorted(prs, key=lambda p: p["date"])],
        },
        "direct_commits_to_main": len(direct),
        "other_two_parent_merges_on_main": [{"sha": c["sha"][:8], "subject": c["subject"]} for c in other_merges],
        "folders": {
            "new_level3_folders_under_fellows": len(new_dirs),
            "pure_renames_of_existing_work": len(renames),
            "renamed_folders": [d.removeprefix("fellows/") for d in renames],
            "removed_old_names": len(gone),
            "new_work_folders": len(folders),
            "new_dated_work_folders": len(dated),
            "dated_inside_the_week": len(in_week),
            "dated_earlier_added_this_week": len(dated) - len(in_week),
            "undated_new_folders": len(folders) - len(dated),
            "fellows_with_new_folders": len(fellows_with_new),
            "fellow_folders": fellows_with_new,
            "folders_per_fellow_top": per_fellow.most_common(5),
            "kinds": dict(kinds.most_common()),
            "stem_subjects": dict(subjects.most_common()),
            "stem_subject_fellows": by_subject_fellows,
            "stem_fellows": len(stem_fellows),
            "stem_per_fellow_top": stem_fellows.most_common(5),
            "frictional_logs_added": len(friction_added),
            "frictional_logs_fellows": len({p.split("/")[1] for p in friction_added}),
            "list": folders,
        },
    }




# ---- the two windows (America/New_York, DST-aware) ----------------------------------------
THIS = week(datetime(2026, 11, 8, 0, 0, 0, tzinfo=NY), datetime(2026, 11, 14, 23, 59, 59, tzinfo=NY))
LAST = week(datetime(2026, 11, 1, 0, 0, 0, tzinfo=NY), datetime(2026, 11, 7, 23, 59, 59, tzinfo=NY))
# the same function must reproduce last week's published numbers (2026-11-08 reel) on the history as it was then
# (main = a953b021) ...
PUB = week(datetime(2026, 11, 1, 0, 0, 0, tzinfo=NY), datetime(2026, 11, 7, 23, 59, 59, tzinfo=NY), tip="a953b021")


def key4(w):
    return (w["merged_prs"]["total"], w["folders"]["new_work_folders"], w["folders"]["fellows_with_new_folders"],
            w["folders"]["frictional_logs_added"])


assert key4(PUB) == (26, 74, 18, 95), "last week's published numbers no longer reproduce"
# ... and recounted on today's history, one more PR landed inside last week's window after that count
# (#375, merged Sat Nov 7 21:07 EST, one new work folder from a fellow with no other new folder that week)
late = [p for p in LAST["merged_prs"]["list"] if p["pr"] not in PUB["merged_prs"]["pr_numbers"]]
late_folders = sorted({f["folder"] for f in LAST["folders"]["list"]} - {f["folder"] for f in PUB["folders"]["list"]})

# coordinator's cross-check: plain date window on all reachable commits
coord = log(TIP, "--since=2026-11-08T00:00:00-05:00", "--until=2026-11-14T23:59:59-05:00")
coord_x = {"commits": len(coord),
           "two_parent_merges": sum(1 for c in coord if len(c["parents"]) > 1),
           "merge_pull_request_commits": sum(1 for c in coord if pr_merge.match(c["subject"])),
           "squash_merges_first_parent": THIS["merged_prs"]["squash_merges"]}


# ---- what got in the way: a rough THEME sort of this week's frictional logs ----------------
# Unit = one frictional log (a log counts once per theme however often it mentions it).
# Text used = the log minus the parts that are not obstacles (who contributed what, what is understood now,
# what was planned or expected, links, hours). A part is a heading's section, a bold-label line/bullet, or
# a paragraph. First, a log must describe at least one obstacle at all (OBSTACLE).
SKIP = re.compile(r"contribut|understood|understand now|what i understand|what is understood|still open|"
                  r"unresolved|still unsure|still don.t|^evidence|record provenance|^drive|^folder|^hours|"
                  r"topic source|^outcome|preceding|your own notes|sign-off|working on|what i was working|"
                  r"tried|expected|focus|^what i did$|video links|references|^report|^project|^week|"
                  r"^\*?written|^date and focus|^ai tools|^topic", re.I)
OBSTACLE = re.compile(r"resist|stuck|friction|didn.t work|did not|failed|fail |broke|wrong|caught|flagged|"
                      r"hung|stall|too (small|long|large)|ran long|overshot", re.I)
THEMES = [
    ("layout & picture checks",
     r"safe(-| )?(area|edge|zone|inset|half)|title-safe|overlap|edge-bleed|edge overflow|underfill|"
     r"fills? (too )?little|text-size|size floor|min(imum)?-size|too-small text|too small on a phone|"
     r"\bgate (b|v|t)\b|layout gate|frame check|ran past|crowding|touching|collid|below 4k|not in 4k"),
    ("timing & pacing",
     r"\bthe pacing\b|pacing (near|was|around)|appeared late|appear(ed)? (all )?at once|"
     r"before (it was|she|he) (spoken|named|said)|reveal (time|schedule|cue)|cue word|word clock|word time|"
     r"pinned to the word|empty-screen gap|nothing changing|on its own clock|lines together"),
    ("facts & data",
     r"fact[- ]check|did not reproduce|didn.t reproduce|didn.t match the \\d|not like for like|rigged|"
     r"over-?states|verbatim|title didn.t survive|number (drifted|conflation)|wrong line|"
     r"no source supports|says otherwise|drops out-of-range|wrong question|near-duplicate"),
    ("length & time",
     r"ran long|trimm|overshoot|overshot|first narration pass|came in short|took (longer|more)|"
     r"more than making|minutes of training|ran for over|\bruntime\.|runtime after"),
    ("tools & setup",
     r"install|homebrew|micromamba|python was too old|headless browser|\bhung\b|"
     r"render script stopped|stopped after the scene clips|needed (a )?re-runs?|pipeline stall|"
     r"\d+ ?gb\b|c: was full|imports? |log path|tunnel|notebook|kaggle|module file"),
    ("voice & pronunciation",
     r"\bnarrator read|\bread \"|\bvoiced \"|respell|pronunc|whisper heard|sound the same|"
     r"said \"reed\"|as \"oak doctor\"|\"uh star\""),
]
THEME_RX = [(n, re.compile(rx, re.I)) for n, rx in THEMES]


def parts(text):
    """Split a log into (headings, body) parts. Markdown headings open sections (a sub-heading keeps its parent
    headings); a line that is only bold acts as a sub-heading; each top-level bullet or paragraph is a part."""
    out, stack = [], []          # stack of (level, heading)
    for block in re.split(r"\n\s*\n", text):
        cur = []
        for ln in block.strip("\n").splitlines():
            s_ = ln.strip()
            m = re.match(r"^(#+)\s*(.*)", s_)
            bold_line = re.fullmatch(r"\*\*(.+?)\*\*:?", s_)
            if m or bold_line:
                if cur:
                    out.append(([h for _, h in stack], "\n".join(cur)))
                    cur = []
                lvl, h = (len(m.group(1)), m.group(2)) if m else (9, bold_line.group(1))
                while stack and stack[-1][0] >= lvl:
                    stack.pop()
                stack.append((lvl, h))
                continue
            if re.match(r"^(-|\d+\.)\s", s_) and cur and not ln.startswith((" ", "\t")):
                out.append(([h for _, h in stack], "\n".join(cur)))
                cur = []
            cur.append(ln)
        if cur:
            out.append(([h for _, h in stack], "\n".join(cur)))
    return out


def _skip(label):
    label = label.strip(" .:*")
    return bool(SKIP.search(label)) and not re.search(r"resist|stuck|friction|didn.t work", label, re.I)


def obstacle_text(text):
    keep = []
    for heads, body in parts(text):
        if any(_skip(h) for h in heads[1:] or heads):   # the log's title (first heading) never skips the log
            continue
        lab = re.match(r"^\s*(?:-|\d+\.)?\s*\*\*(.+?)\*\*", body)
        if lab and _skip(lab.group(1)):
            continue
        keep.append(body)
    return "\n".join(keep)


fric_paths = sorted(p for p in git("diff", "-M", "--name-status", THIS["base_commit"], THIS["head_commit"],
                                   "--", "fellows/").splitlines() if p.startswith("A\t")
                    and re.search(r"/friction(al)?[^/]*\.md$", p, re.I))
fric_paths = [p.split("\t")[1] for p in fric_paths]
assert len(fric_paths) == THIS["folders"]["frictional_logs_added"]
logs = []
for p in fric_paths:
    full = git("show", f"{TIP}:{p}")
    ob = obstacle_text(full)
    themes = [n for n, rx in THEME_RX if rx.search(ob)] if OBSTACLE.search(ob) else []
    hits = {n: sorted({m.group(0).lower() for m in rx.finditer(ob)})[:6] for n, rx in THEME_RX if n in themes}
    logs.append({"log": p.removeprefix("fellows/"), "fellow": p.split("/")[1], "words": len(full.split()),
                 "obstacle_words": len(ob.split()), "describes_obstacles": bool(OBSTACLE.search(ob)),
                 "themes": themes, "hits": hits})
with_obs = [l for l in logs if l["describes_obstacles"]]
theme_logs = Counter(t_ for l in logs for t_ in l["themes"])
theme_fellows = {n: len({l["fellow"] for l in logs if n in l["themes"]}) for n, _ in THEMES}
per_log = Counter(len(l["themes"]) for l in with_obs)

friction = {
    "logs_added": len(logs),
    "fellows": len({l["fellow"] for l in logs}),
    "logs_describing_obstacles": len(with_obs),
    "logs_without_obstacles": [l["log"] for l in logs if not l["describes_obstacles"]],
    "theme_logs": {n: theme_logs.get(n, 0) for n, _ in sorted(THEMES, key=lambda x: -theme_logs.get(x[0], 0))},
    "theme_fellows": theme_fellows,
    "themes_per_log": dict(sorted(per_log.items())),
    "logs_with_no_theme": [l["log"] for l in with_obs if not l["themes"]],
    "rule": "unit = one frictional log; text = the log minus contributions / understood-now / expected / links; "
            "a log counts once per theme if any keyword rule (THEMES) matches; heuristic ('my rough sort')",
    "list": logs,
}

# ---- examples: obstacle -> fix, paraphrased; each one asserted against the log's own words -------------
EXAMPLES = [
    {"theme": "layout & picture checks", "log": "jainil-s/2026-11-06-ai-significant-on-tuesday/FRICTIONAL.md",
     "must": ["passed GATE V and GATE T", "asserted the opposite of the narration",
              "Fixed by tinting the two outer regions instead"],
     "obstacle": "a chart passed the frame checks, but showed the opposite of the narration",
     "fix": "looking at the frame caught it; the shading was fixed"},
    {"theme": "facts & data", "log": "gomathy-s/2026-11-10-most-insider-trades-arent-buys/FRICTIONAL.md",
     "must": ["The title didn't survive the data", "The title became"],
     "obstacle": "the working title didn't survive the data",
     "fix": "changed the title to what the data shows"},
    {"theme": "length & time", "log": "agrima-p/2026-11-11-foundation-search-research/FRICTIONAL.md",
     "must": ["first narration pass measured 262 s", "five rounds of trimming",
              "no figure, source, hedge or label removed", "239.9 s"],
     "obstacle": "the first script ran 262 s for a 4:00 slot",
     "fix": "five rounds of trimming, no figure or source cut"},
    {"theme": "tools & setup", "log": "tanmay-k/2026-11-08-where-the-eighty-lives-stem-video/FRICTIONAL.md",
     "must": ["ran for over 40 minutes", "streams frames", "runs in 87 seconds"],
     "obstacle": "a checking script ran for over 40 minutes",
     "fix": "made it stream frames: now 87 seconds"},
    {"theme": "timing & pacing", "log": "tanishaa-r/2026-10-30-what-is-rag/FRICTIONAL.md",
     "must": ["items appeared late", "word times were measured from Bella's audio"],
     "obstacle": "words on screen appeared late",
     "fix": "timed each reveal to the voice's measured words"},
]
by_log = {l["log"]: l for l in logs}
for e in EXAMPLES:
    txt = " ".join(git("show", f"{TIP}:fellows/{e['log']}").split())
    assert all(m in txt for m in e["must"]), e["log"]
    assert e["theme"] in by_log[e["log"]]["themes"], (e["log"], by_log[e["log"]]["themes"])
    e["fellow"] = e["log"].split("/")[0]
assert len({e["fellow"] for e in EXAMPLES}) == len(EXAMPLES)

# ---- what fixed them: how many logs say a problem was found by LOOKING (watching the cut, viewing frames or
# previews, re-reading the words) -- keyword rule on the whole log, rough count
LOOKED = re.compile(r"sampling frames|viewing preview|previews? showed|snapshots? showed|snapshot review|"
                    r"looking at (the )?(frames|phone)|inspected (both flagged|real) frames|personally inspected|"
                    r"gate and by eye|re-read(ing)? the|after watching|watched the first preview|"
                    r"frame review found|listened", re.I)
for l in logs:
    full = " ".join(git("show", f"{TIP}:fellows/{l['log']}").split())
    l["found_by_looking"] = sorted({m.group(0).lower() for m in LOOKED.finditer(full)}) if l["describes_obstacles"] else []
friction["found_by_looking_logs"] = sum(1 for l in logs if l["found_by_looking"])
friction["found_by_looking_fellows"] = len({l["fellow"] for l in logs if l["found_by_looking"]})

# ---- Boopesh's own last week (his folder is not on main yet) -------------------------------
boopesh_on_main = bool(git("ls-tree", TIP, "fellows/boopesh-m").strip())
deliv = {}
for rel in ("landscape/WhatTheFellowsTaught_BoopeshM.mp4", "vertical/WhatTheFellowsTaught_BoopeshM.mp4",
            "landscape/BacktestMirage_BoopeshM.mp4", "vertical/BacktestMirage_BoopeshM.mp4"):
    p = Path("/home/user/weekly-submission") / rel
    if p.exists():
        o = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                            "stream=width,height,duration", "-of", "json", str(p)],
                           capture_output=True, text=True).stdout
        s = json.loads(o)["streams"][0]
        sec = round(float(s["duration"]))
        deliv[rel] = {"width": s["width"], "height": s["height"], "video_duration_s": round(float(s["duration"]), 2),
                      "mm_ss": f"{sec // 60}:{sec % 60:02d}"}

T, L = THIS, LAST
res = {
    "repo": "nikbearbrown/humanitarians-youtube",
    "ref": REF, "tip": TIP[:8],
    "timezone": "America/New_York (EST UTC-5 for all of Nov 8-14; last week starts EDT UTC-4 until Nov 1 02:00)",
    "this_week": T,
    "last_week": L,
    "comparison": {
        k: {"last_week": f(L), "this_week": f(T)} for k, f in (
            ("merged_prs", lambda w: w["merged_prs"]["total"]),
            ("new_work_folders", lambda w: w["folders"]["new_work_folders"]),
            ("fellows_with_new_folders", lambda w: w["folders"]["fellows_with_new_folders"]),
            ("frictional_logs_added", lambda w: w["folders"]["frictional_logs_added"]),
            ("frictional_logs_fellows", lambda w: w["folders"]["frictional_logs_fellows"]),
        )},
    "coordinator_crosscheck_nov8_14_date_window": coord_x,
    "last_week_published_vs_recounted": {"published_2026_11_08_at_a953b021": key4(PUB), "recounted_today": key4(L),
                                         "late_prs": late, "late_folders": late_folders,
                                         "order": "merged_prs, new_work_folders, fellows_with_new_folders, "
                                                  "frictional_logs_added"},
    "friction": friction,
    "examples": [{k: e[k] for k in ("theme", "log", "fellow", "obstacle", "fix")} for e in EXAMPLES],
    "boopesh": {"folder_on_main": boopesh_on_main, "last_week_deliveries": deliv,
                "status": "two videos made and delivered for review (Drive submission not claimed); GitHub pull "
                          "request pending (fork attempt failed); fellows/boopesh-m not on main"},
}
out = Path(__file__).with_name("results.json")
out.write_text(json.dumps(res, indent=2, ensure_ascii=False, default=str) + "\n")
for name, w in (("THIS WEEK Nov 8-14", T), ("LAST WEEK Nov 1-7 (recomputed)", L)):
    print(f"== {name}: {w['base_commit']}..{w['head_commit']} commits_landed={w['commits_landed']} "
          f"first_parent={w['commits_on_main_first_parent']} direct={w['direct_commits_to_main']}")
    print(" PRs", {k: v for k, v in w["merged_prs"].items() if k != "list"})
    print(" other 2-parent merges", w["other_two_parent_merges_on_main"])
    print(" folders", json.dumps({k: v for k, v in w["folders"].items() if k != "list"}))
print("== comparison", json.dumps(res["comparison"]))
print("== coordinator cross-check", coord_x)
print("== last week published vs recounted", key4(PUB), key4(L), late, late_folders)
print("== friction", json.dumps({k: v for k, v in friction.items() if k != "list"}))
print("   logs per fellow", Counter(l["fellow"] for l in logs).most_common())
for l in logs:
    print(f"  {l['log'][:70]:70} | {','.join(l['themes'])} | looked: {l['found_by_looking']}")
    for n, h in l["hits"].items():
        print(f"      {n:24} {h}")
print("== examples", json.dumps(res["examples"], ensure_ascii=False))
print("== boopesh", json.dumps(res["boopesh"]))
