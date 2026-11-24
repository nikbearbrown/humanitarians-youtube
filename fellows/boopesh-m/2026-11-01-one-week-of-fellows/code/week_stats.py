#!/usr/bin/env python3
"""
One week of fellows: what landed in nikbearbrown/humanitarians-youtube between
2026-10-25 00:00 and 2026-10-31 23:59:59 US Eastern (EDT, UTC-4).

Reads only git history (no network). Writes results.json next to this file.
Privacy: the fellows folder rules allow first name + last initial + GitHub handle only.
No email address or full surname is written to results.json; people appear as folder
names (e.g. "jash-s") or as "First L." initials.

usage: python3 week_stats.py [REPO] [REF]     (defaults: the humanitarians-youtube clone, FETCH_HEAD)
"""
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/user/nikbearbrown/humanitarians-youtube")
REF = sys.argv[2] if len(sys.argv) > 2 else "FETCH_HEAD"
EDT = timezone(timedelta(hours=-4))
START = datetime(2026, 10, 25, 0, 0, 0, tzinfo=EDT)
END = datetime(2026, 10, 31, 23, 59, 59, tzinfo=EDT)
DAYS = [(START + timedelta(days=i)).date() for i in range(7)]


def git(*a):
    return subprocess.run(["git", "-C", str(REPO), *a], check=True, capture_output=True, text=True).stdout


head = git("rev-parse", REF).strip()
# main as it stood when the week began: last first-parent commit before Oct 25 00:00 EDT
base = git("rev-list", "-1", "--first-parent", f"--before={START.isoformat()}", head).strip()
assert git("rev-list", "-1", "--first-parent", f"--before={(END + timedelta(seconds=1)).isoformat()}", head).strip() == head, \
    "REF has commits after the window; pass the last commit of Oct 31"

SEP = "\x1f"
FMT = SEP.join(["%H", "%P", "%an", "%ae", "%cI", "%s"])


def log(*a):
    rows = []
    for line in git("log", f"--format={FMT}", *a).splitlines():
        h, p, an, ae, ci, s = line.split(SEP)
        rows.append({"sha": h, "parents": p.split(), "name": an, "email": ae,
                     "date": datetime.fromisoformat(ci).astimezone(EDT), "subject": s})
    return rows


landed = log(f"{base}..{head}")                  # every commit that arrived on main this week
mainline = log("--first-parent", f"{base}..{head}")  # main's own history this week
assert all(START <= c["date"] <= END for c in mainline), "a mainline commit falls outside the window"

# ---- merged pull requests ---------------------------------------------------------------
pr_merge = re.compile(r"^Merge pull request #(\d+)")
pr_squash = re.compile(r"\(#(\d+)\)\s*$")
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

# coordinator's cross-check: plain date window Oct 24-31 on all reachable commits
coord = log(head, "--since=2026-10-24T00:00:00-04:00", "--until=2026-10-31T23:59:59-04:00")
coord_merges = sum(1 for c in coord if pr_merge.match(c["subject"]))
coord_names = len({c["name"] for c in coord})

# ---- contributors -----------------------------------------------------------------------
def initials(name):
    parts = re.split(r"[\s_]+", name.strip())
    if len(parts) >= 2 and parts[0][:1].isalpha():
        return f"{parts[0].capitalize()} {parts[-1][0].upper()}."
    return name   # a single token is already a GitHub handle


def noreply_login(email):
    m = re.match(r"^(?:\d+\+)?([^@]+)@users\.noreply\.github\.com$", email)
    return m.group(1).lower() if m else None


raw_names = sorted({c["name"] for c in landed})
work_names = sorted({c["name"] for c in landed if len(c["parents"]) == 1})
# union-find over author names; link two names only when the evidence is mechanical
parent = {n: n for n in raw_names}


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b, why, log_):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra
        # privacy: keep only "First L."; a one-word (handle-style) author name is not repeated here
        multi = [n for n in (a, b) if len(re.split(r"[\s_]+", n.strip())) > 1]
        shown = initials(multi[0]) if multi else min((a, b), key=len)
        log_.append({"person": shown, "second_name": "another spelling" if len(multi) == 2 else "handle-style name",
                     "rule": why})


links = []
by_email, by_login = defaultdict(set), defaultdict(set)
for c in landed:
    by_email[c["email"].lower()].add(c["name"])
    lg = noreply_login(c["email"])
    if lg:
        by_login[lg].add(c["name"])
for email, names in by_email.items():
    names = sorted(names)
    for n in names[1:]:
        union(names[0], n, "same commit email", links)
for lg, names in by_login.items():
    names = sorted(names)
    for n in names[1:]:
        union(names[0], n, "same GitHub account (noreply address)", links)
    for n in raw_names:   # a bare handle used as the author name, e.g. "Onkar97"
        if n.lower() == lg and names:
            union(names[0], n, "author name is that GitHub handle", links)
norm = defaultdict(set)
for n in raw_names:
    norm[re.sub(r"[^a-z]", "", n.lower())].add(n)
for k, names in norm.items():
    names = sorted(names)
    for n in names[1:]:
        union(names[0], n, "same name, different spacing/case", links)
people = defaultdict(set)
for n in raw_names:
    people[find(n)].add(n)
MAINTAINERS = {"Nik Bear Brown"}   # repository owner; merges others' PRs
fellow_people = [g for g in people.values() if not (g & MAINTAINERS)]
work_people = [g for g in people.values() if g & set(work_names)]
# not merged automatically (looks like the same person, but no mechanical link) -- reported, not deduped
first = defaultdict(set)
for root, g in people.items():
    first[re.split(r"[\s_]+", sorted(g)[0])[0].lower()[:4]].add(root)
possible = [sorted(initials(r) for r in roots) for roots in first.values() if len(roots) > 1]

# ---- folders ----------------------------------------------------------------------------
def level3(ref):
    out = git("ls-tree", "-d", "-r", "--name-only", ref, "fellows")
    return {p for p in out.splitlines() if p.count("/") == 2}


before, after = level3(base), level3(head)
new_dirs = sorted(after - before)
gone = sorted(before - after)
# a "new" folder whose every file was renamed from an existing path is a rename, not new work
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
renames = [d for d in new_dirs if renamed_into[d] > added[d]]   # moved old work (+ maybe a new FRICTIONAL.md)
real_new = [d for d in new_dirs if d not in renames]
DATED = re.compile(r"^(\d{4}-\d{2}-\d{2})")


def leaf(d):
    return d.split("/", 2)[2]


def readme_head(d):
    files = git("ls-tree", "--name-only", head, d + "/").splitlines()
    rd = [f for f in files if f.lower().endswith("/readme.md")]
    if not rd:
        return ""
    txt = git("show", f"{head}:{rd[0]}")
    return " ".join(txt.split()[:80]).lower()


def kind(d):
    name, rh = leaf(d).lower(), readme_head(d)
    if "renewal" in name:
        return "renewal request"
    if "hours" in name:
        return "hours log"
    if "not a video" in rh or "written work" in rh:
        return "written / code work"
    if re.search(r"stem|explainer", name):
        return "STEM / explainer video"
    if re.search(r"week|weekly|progress|project-update|work-|mycroft", name):
        return "progress / work video"
    if re.search(r"project update|weekly (work|update|research|implementation)|work video|work report|"
                 r"weekly progress|catch-up report", rh[:300]):
        return "progress / work video"
    return "STEM / explainer video"   # default: a topic video (STEM/AI explainer)


folders = []
for d in real_new:
    m = DATED.match(leaf(d))
    folders.append({"folder": d.removeprefix("fellows/"), "fellow": d.split("/")[1],
                    "dated": m.group(1) if m else None, "kind": kind(d), "files_added": added[d]})
dated = [f for f in folders if f["dated"]]
in_week = [f for f in dated if START.date().isoformat() <= f["dated"] <= END.date().isoformat()]
kinds = Counter(f["kind"] for f in folders)
fellows_with_new = sorted({f["fellow"] for f in folders})

# topic words from the new work-folder names (dates and filler words removed)
STOP = set("a an the of in on to and for is it its how what why that with vs not your my our week weekly "
           "update updates video videos work progress project stem explainer part new same".split())
words = Counter()
for f in folders:
    if f["kind"] in ("renewal request", "hours log"):
        continue
    for w in re.split(r"[^a-z0-9]+", DATED.sub("", leaf("x/x/" + f["folder"].split("/", 1)[1])).lower()):
        if len(w) > 2 and w not in STOP and not w.isdigit():
            words[w] += 1


# ---- a few representative titles (README first heading), work dated inside the week -----
REPRESENTATIVE = ["aishwarya-p/2026-10-29-what-is-rlhf", "chinnasurya-v/2026-10-28-encrypted-twice",
                  "uday-s/2026-10-30-right-answer-wrong-chain", "yatra-r/2026-10-29-ads-in-the-picture",
                  "anjana-n/2026-10-30-distributed-training-explainer", "pranavi-j/2026-10-28-in-context-learning-limits",
                  "satwik-s/2026-10-25-prereq-recall-gap", "jash-s/physics-engine-week-01"]


def h1(folder):
    files = git("ls-tree", "--name-only", head, "fellows/" + folder + "/").splitlines()
    rd = [f for f in files if f.lower().endswith("/readme.md")]
    for line in (git("show", f"{head}:{rd[0]}").splitlines() if rd else []):
        if line.startswith("# "):
            return line[2:].strip()
    bs = [f for f in files if f.endswith("/beat_sheet.json")]   # no README: use the beat sheet's title
    if bs:
        return json.loads(git("show", f"{head}:{bs[0]}")).get("metadata", {}).get("title")
    return None


titles = [{"folder": f, "title": h1(f), "kind": next(x["kind"] for x in folders if x["folder"] == f)}
          for f in REPRESENTATIVE]

# ---- Boopesh's own week (his folder is not on main yet) ----------------------------------
boopesh_on_main = bool(git("ls-tree", head, "fellows/boopesh-m").strip())
deliv = {}
for rel in ("landscape/BrutalistShared_BoopeshM.mp4", "vertical/BrutalistShared_BoopeshM.mp4",
            "landscape/DeepHedging_BoopeshM.mp4", "vertical/DeepHedging_BoopeshM.mp4"):
    p = Path("/home/user/weekly-submission") / rel
    if p.exists():
        o = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                            "stream=width,height:format=duration", "-of", "json", str(p)],
                           capture_output=True, text=True).stdout
        j = json.loads(o)
        deliv[rel] = {"width": j["streams"][0]["width"], "height": j["streams"][0]["height"],
                      "duration_s": round(float(j["format"]["duration"]), 1)}

res = {
    "repo": "nikbearbrown/humanitarians-youtube",
    "window": {"start": START.isoformat(), "end": END.isoformat(), "timezone": "US Eastern (EDT, UTC-4)"},
    "base_commit": base[:8], "head_commit": head[:8],
    "base_subject": git("log", "-1", "--format=%s", base).strip(),
    "commits_landed": len(landed),
    "commits_on_main_first_parent": len(mainline),
    "merged_prs": {
        "total": len(prs),
        "merge_commits": sum(p["kind"] == "merge commit" for p in prs),
        "squash_merges": sum(p["kind"] == "squash merge" for p in prs),
        "per_day": {d.isoformat(): per_day.get(d, 0) for d in DAYS},
        "busiest_day": max(DAYS, key=lambda d: per_day.get(d, 0)).isoformat(),
        "pr_numbers": sorted(p["pr"] for p in prs),
        "list": [{"pr": p["pr"], "kind": p["kind"], "sha": p["sha"], "date_edt": p["date"].isoformat()} for p in
                 sorted(prs, key=lambda p: p["date"])],
    },
    "direct_commits_to_main": len(direct),
    "coordinator_crosscheck_oct24_31_date_window": {"merge_pull_request_commits": coord_merges,
                                                     "distinct_author_names": coord_names},
    "contributors": {
        "distinct_author_names_raw": len(raw_names),
        "distinct_people_after_obvious_dedupe": len(people),
        "dedupe_links": links,
        "possible_same_person_not_merged": possible + [["Tanny (laptop name)", "Tanmay K."]],
        "possible_note": "Uday S. / Uday S. (two spellings, PR from the uday-s fork) and Tanny / Tanmay K. "
                         "(laptop-name author, merged from his own branch) look like the same people but have no "
                         "mechanical link; if merged, 25 people, still 23 who authored work.",
        "maintainer_accounts_excluded_from_fellow_count": len(people) - len(fellow_people),
        "fellows_and_staff_excluding_repo_owner": len(fellow_people),
        "people_who_authored_non_merge_commits": len(work_people),
        "note": "Counted over every commit that landed on main this week (base..head). Names linked only by "
                "same email, same GitHub noreply account, author-name = handle, or same letters. "
                "Names are not written here (privacy rule).",
    },
    "folders": {
        "new_level3_folders_under_fellows": len(new_dirs),
        "pure_renames_of_existing_work": len(renames),
        "removed_old_names": len(gone),
        "new_work_folders": len(folders),
        "new_dated_work_folders": len(dated),
        "dated_inside_the_week": len(in_week),
        "dated_earlier_added_this_week": len(dated) - len(in_week),
        "undated_new_folders": len(folders) - len(dated),
        "fellows_with_new_folders": len(fellows_with_new),
        "fellow_folders": fellows_with_new,
        "kinds": dict(kinds.most_common()),
        "frictional_logs_added": len(friction_added),
        "frictional_logs_fellows": len({p.split("/")[1] for p in friction_added}),
        "list": folders,
    },
    "topic_words_top": words.most_common(15),
    "representative_titles": titles,
    "boopesh": {"folder_on_main": boopesh_on_main, "last_week_deliveries": deliv,
                "status": "videos submitted to Drive; GitHub pull request pending (fork attempt failed; "
                          "asking the maintainer for access)"},
    "classification_note": "kind = rule on folder name + first 80 words of its README (renewal, hours, "
                           "'not a video', stem/explainer, week/weekly/progress/project update). Heuristic.",
}
out = Path(__file__).with_name("results.json")
out.write_text(json.dumps(res, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({k: res[k] for k in ("base_commit", "head_commit", "commits_landed", "merged_prs",
                                      "direct_commits_to_main", "coordinator_crosscheck_oct24_31_date_window",
                                      "contributors")}, indent=1, default=str)[:4000])
print(json.dumps({k: v for k, v in res["folders"].items() if k != "list"}, indent=1))
print(res["topic_words_top"])
