#!/usr/bin/env python3
"""
What the fellows taught: what landed in nikbearbrown/humanitarians-youtube between
2026-11-01 00:00 and 2026-11-07 23:59:59 America/New_York (DST ended Nov 1 at 02:00, so the window
starts at UTC-4 and ends at UTC-5), with last week (Oct 25-31) recomputed by the SAME function so the
definitions match.

Based on last week's 2026-11-01-one-week-of-fellows/code/week_stats.py: same PR rule (first-parent
"Merge pull request #N" commits + squash merges "... (#N)"), same new-work-folder rule (new
fellows/<fellow>/<folder> paths minus pure renames), same kind sort, same frictional-log rule.
New this week: a rough SUBJECT sort of the topic (STEM / explainer) videos, and example titles.

Reads only git history (no network). Writes results.json next to this file.
Privacy: people appear only as fellow folder names (e.g. "vineet-s"); no email or surname is written.

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


def week(start, end):
    head = git("rev-list", "-1", "--first-parent", f"--before={end.isoformat()}", TIP).strip()
    base = git("rev-list", "-1", "--first-parent", f"--before={start.isoformat()}", TIP).strip()
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
THIS = week(datetime(2026, 11, 1, 0, 0, 0, tzinfo=NY), datetime(2026, 11, 7, 23, 59, 59, tzinfo=NY))
LAST = week(datetime(2026, 10, 25, 0, 0, 0, tzinfo=NY), datetime(2026, 10, 31, 23, 59, 59, tzinfo=NY))
# the new definitions must reproduce last week's published numbers (2026-11-01 reel)
assert (LAST["merged_prs"]["total"], LAST["folders"]["new_work_folders"], LAST["folders"]["fellows_with_new_folders"],
        LAST["folders"]["frictional_logs_added"]) == (30, 84, 22, 72), "last week no longer reproduces"

# coordinator's cross-check: plain date window on all reachable commits
coord = log(TIP, "--since=2026-11-01T00:00:00-04:00", "--until=2026-11-07T23:59:59-05:00")
coord_x = {"commits": len(coord),
           "two_parent_merges": sum(1 for c in coord if len(c["parents"]) > 1),
           "merge_pull_request_commits": sum(1 for c in coord if pr_merge.match(c["subject"])),
           "squash_merges_first_parent": THIS["merged_prs"]["squash_merges"]}

# ---- example titles, all dated inside this week (folder names only) ----------------------
EXAMPLES = ["anjana-n/2026-11-06-moe-explainer",
            "pranavi-j/2026-11-04-goodharts-law-proxy-metrics",
            "onkar-b/2026-11-05-stem-continuous-integration",
            "uday-s/2026-11-05-likely-false-likely-true",
            "vineet-s/2026-11-01-rag-explained-for-product-managers",
            "yatra-r/2026-11-05-be-the-sentence"]
by_f = {f["folder"]: f for f in THIS["folders"]["list"]}
assert all(by_f[e]["dated"] >= "2026-11-01" and by_f[e]["kind"] == "STEM / explainer video" for e in EXAMPLES)
examples = [{k: by_f[e][k] for k in ("folder", "title", "kind", "subject", "dated")} for e in EXAMPLES]

# ---- Boopesh's own last week (his folder is not on main yet) -------------------------------
boopesh_on_main = bool(git("ls-tree", TIP, "fellows/boopesh-m").strip())
deliv = {}
for rel in ("landscape/OneWeekOfFellows_BoopeshM.mp4", "vertical/OneWeekOfFellows_BoopeshM.mp4",
            "landscape/FraudAccuracyTrap_BoopeshM.mp4", "vertical/FraudAccuracyTrap_BoopeshM.mp4"):
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
    "timezone": "America/New_York (EDT UTC-4 until Nov 1 02:00, then EST UTC-5)",
    "this_week": T,
    "last_week": L,
    "comparison": {
        k: {"last_week": f(L), "this_week": f(T)} for k, f in (
            ("merged_prs", lambda w: w["merged_prs"]["total"]),
            ("new_work_folders", lambda w: w["folders"]["new_work_folders"]),
            ("fellows_with_new_folders", lambda w: w["folders"]["fellows_with_new_folders"]),
            ("frictional_logs_added", lambda w: w["folders"]["frictional_logs_added"]),
            ("stem_explainer_folders", lambda w: w["folders"]["kinds"].get("STEM / explainer video", 0)),
            ("progress_folders", lambda w: w["folders"]["kinds"].get("progress / work video", 0)),
            ("dated_inside_the_week", lambda w: w["folders"]["dated_inside_the_week"]),
        )},
    "coordinator_crosscheck_nov1_7_date_window": coord_x,
    "examples": examples,
    "boopesh": {"folder_on_main": boopesh_on_main, "last_week_deliveries": deliv,
                "status": "two videos made and delivered for review (Drive submission unconfirmed); GitHub pull "
                          "request pending (fork attempt failed); fellows/boopesh-m not on main"},
    "classification_note": "kind = last week's rule on folder name + first 80 words of README. subject = first "
                           "matching keyword rule (SUBJECTS) on folder name + README title + opening. Both heuristic.",
}
out = Path(__file__).with_name("results.json")
out.write_text(json.dumps(res, indent=2, ensure_ascii=False) + "\n")
for name, w in (("THIS WEEK Nov 1-7", T), ("LAST WEEK Oct 25-31 (recomputed)", L)):
    print(f"== {name}: {w['base_commit']}..{w['head_commit']} commits_landed={w['commits_landed']} "
          f"first_parent={w['commits_on_main_first_parent']} direct={w['direct_commits_to_main']}")
    print(" PRs", {k: v for k, v in w["merged_prs"].items() if k != "list"})
    print(" other 2-parent merges", w["other_two_parent_merges_on_main"])
    print(" folders", json.dumps({k: v for k, v in w["folders"].items() if k != "list"}))
print("== comparison", json.dumps(res["comparison"]))
print("== coordinator cross-check", coord_x)
print("== examples", json.dumps(examples, ensure_ascii=False))
print("== boopesh", json.dumps(res["boopesh"]))
print("== this week's STEM folders by subject")
for f in sorted(T["folders"]["list"], key=lambda f: (f["kind"], f["subject"] or "", f["folder"])):
    print(f"  {f['kind'][:8]:8} | {str(f['subject']):28} | {f['folder']} | {f['title']}")
