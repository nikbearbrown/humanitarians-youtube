#!/usr/bin/env python3
"""week_stats.py -- "What a finished folder looks like" (HAI weekly, Nov 15-21 2026).

Reads the humanitarians-youtube git history (trees and commit metadata only, no
file contents) and writes results.json + run.log next to this script.

Definitions (applied identically to this week and last week):
  * Week window: Sunday 00:00:00 to Saturday 23:59:59 in America/New_York
    (zoneinfo, DST-aware -- never a fixed UTC offset).
  * Merged PR: a "Merge pull request #N" merge commit on main's FIRST-PARENT line
    whose committer time is in the window, plus squash merges (a non-merge
    first-parent commit whose subject carries "(#N)"). De-duplicated by N.
    "Merge branch 'main' into ..." commits and direct (non-PR) merges are excluded.
  * Snapshot at a time T: the newest first-parent commit of main with committer
    time <= T.
  * New work folder: a directory fellows/<fellow>/<folder>/ that exists in the
    end-of-week snapshot but not in the start-of-week snapshot AND whose name
    carries a date (YYYY-MM-DD, MM-DD-YYYY or MMDDYYYY) -- the fellows README
    rule "one dated folder per piece of work". Undated admin folders (hours,
    renewal requests) are listed in run.log but not counted as work.
  * Paperwork pieces: a folder "has" a piece when any file anywhere inside it
    matches the piece's filename rule (case-insensitive) -- see PIECES.

Usage: python3 week_stats.py [--repo PATH] [--ref SHA]
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")
HERE = Path(__file__).resolve().parent
DEFAULT_REPO = HERE.parents[3]          # .../humanitarians-youtube
DEFAULT_REF = "2a32d04e"                # origin/main as cloned for this video

THIS_WEEK = ("2026-11-15", "2026-11-21")
LAST_WEEK = ("2026-11-08", "2026-11-14")
LAST_WEEK_PUBLISHED = {"merged_prs": 19, "new_work_folders": 53,
                       "fellows": 17, "frictional_logs": 32}

CODE_EXT = (".py", ".ipynb", ".js", ".mjs", ".ts", ".tsx", ".jsx", ".r", ".sh", ".sql")

# piece id -> (label shown on screen, rule on a lower-cased file path relative to the folder)
PIECES = [
    ("readme",      "README",        lambda b, p: b == "readme.md"),
    ("factcheck",   "FACTCHECK",     lambda b, p: b.startswith("factcheck")),
    ("frictional",  "FRICTIONAL log", lambda b, p: "frictional" in b),
    ("proof",       "PROOF",         lambda b, p: b.startswith("proof")),
    ("shotlist",    "SHOTLIST",      lambda b, p: "shotlist" in b),
    ("prompts",     "PROMPTS",       lambda b, p: b == "prompts.md"),
    ("beat_sheet",  "beat sheet",    lambda b, p: re.match(r"beat[_-]?sheet.*\.json$", b) is not None),
    ("code",        "code",          lambda b, p: p.startswith("code/") or b.endswith(CODE_EXT)),
    ("description", "description",   lambda b, p: "description" in b),
]
DATED = re.compile(r"(20\d\d-\d\d-\d\d)|(\d\d-\d\d-20\d\d)|((0[1-9]|1[0-2])\d\d20\d\d)")

LOG = []


def log(msg=""):
    LOG.append(msg)
    print(msg)


def git(repo, *args):
    out = subprocess.run(["git", "-C", str(repo), *args], check=True,
                         capture_output=True)
    return out.stdout.decode("utf-8", "surrogateescape")


def ny_epoch(day, end=False):
    y, m, d = map(int, day.split("-"))
    t = datetime(y, m, d, 23, 59, 59, tzinfo=NY) if end else datetime(y, m, d, 0, 0, 0, tzinfo=NY)
    return int(t.timestamp()), t.isoformat()


def first_parent(repo, ref):
    rows = []
    raw = git(repo, "log", "--first-parent", "--format=%H%x1f%ct%x1f%P%x1f%s%x1e", ref)
    for rec in raw.split("\x1e"):
        rec = rec.strip("\n")
        if not rec:
            continue
        h, ct, parents, subj = rec.split("\x1f", 3)
        rows.append({"sha": h, "ct": int(ct), "parents": parents.split(), "subject": subj})
    return rows  # newest first


def snapshot(fp, t):
    for r in fp:                       # newest first
        if r["ct"] <= t:
            return r
    raise SystemExit("no snapshot before %s" % t)


def folders_at(repo, sha):
    raw = git(repo, "ls-tree", "-r", "-d", "-z", "--name-only", sha, "--", "fellows/")
    return {p for p in raw.split("\0") if p and p.count("/") == 2}


def files_in(repo, sha, folder):
    raw = git(repo, "ls-tree", "-r", "-z", "--name-only", sha, "--", folder + "/")
    return sorted(p[len(folder) + 1:] for p in raw.split("\0") if p)


def pieces_of(files):
    have = {}
    for pid, _label, rule in PIECES:
        have[pid] = any(rule(f.rsplit("/", 1)[-1].lower(), f.lower()) for f in files)
    return have


def week(repo, ref, fp, days, tag):
    t0, iso0 = ny_epoch(days[0])
    t1, iso1 = ny_epoch(days[1], end=True)
    log(f"== {tag}: {iso0} .. {iso1}  (epoch {t0}..{t1})")

    # plain counts, all ancestry, committer date (cross-check only)
    plain = int(git(repo, "rev-list", "--count", f"--since={t0}", f"--until={t1}", ref).strip())
    plain_m = int(git(repo, "rev-list", "--count", "--merges", f"--since={t0}", f"--until={t1}", ref).strip())
    log(f"plain count (all ancestry, committer date): {plain} commits, {plain_m} merge commits")

    in_win = [r for r in fp if t0 <= r["ct"] <= t1]
    prs, excluded = {}, []
    for r in in_win:
        m = re.match(r"Merge pull request #(\d+)\b", r["subject"])
        if m and len(r["parents"]) >= 2:
            prs.setdefault(int(m.group(1)), r)
            continue
        s = re.search(r"\(#(\d+)\)", r["subject"])
        if s and len(r["parents"]) == 1:
            prs.setdefault(int(s.group(1)), r)
            continue
        if len(r["parents"]) >= 2:
            excluded.append(r)
    log(f"first-parent commits in window: {len(in_win)}")
    for n in sorted(prs):
        r = prs[n]
        when = datetime.fromtimestamp(r["ct"], NY).strftime("%a %m-%d %H:%M")
        log(f"  PR #{n:<4} {when}  {r['sha'][:8]}  {r['subject'][:70]}")
    for r in excluded:
        log(f"  excluded merge (not a PR): {r['sha'][:8]}  {r['subject'][:70]}")
    squash = [n for n, r in prs.items() if len(r["parents"]) == 1]
    log(f"merged PRs: {len(prs)}  (squash merges among them: {len(squash)})")

    s_start, s_end = snapshot(fp, t0 - 1), snapshot(fp, t1)
    log(f"snapshot start {s_start['sha'][:8]}  end {s_end['sha'][:8]}")
    new_dirs = sorted(folders_at(repo, s_end["sha"]) - folders_at(repo, s_start["sha"]))
    gone = sorted(folders_at(repo, s_start["sha"]) - folders_at(repo, s_end["sha"]))
    work = [d for d in new_dirs if DATED.search(d.split("/")[2])]
    undated = [d for d in new_dirs if d not in work]
    log(f"new fellows/<fellow>/<folder> dirs: {len(new_dirs)}; dated work folders: {len(work)}; "
        f"undated (not counted): {undated}; removed: {len(gone)}")

    rows = []
    for d in work:
        files = files_in(repo, s_end["sha"], d)
        have = pieces_of(files)
        rows.append({"folder": d, "fellow": d.split("/")[1], "n_files": len(files),
                     "pieces": have, "n_pieces": sum(have.values())})
    counts = {pid: sum(r["pieces"][pid] for r in rows) for pid, _, _ in PIECES}
    fellows = sorted({r["fellow"] for r in rows})
    log(f"fellows with a new work folder: {len(fellows)}")
    for pid, label, _ in PIECES:
        log(f"  {label:<15} {counts[pid]:>3} / {len(rows)}")
    return {
        "window_start": iso0, "window_end": iso1,
        "plain_commits": plain, "plain_merge_commits": plain_m,
        "merged_prs": len(prs), "pr_numbers": sorted(prs),
        "squash_merges": len(squash),
        "excluded_merges": [r["subject"] for r in excluded],
        "latest_pr": None if not prs else {
            "number": max(prs, key=lambda n: prs[n]["ct"]),
            "merged_at": datetime.fromtimestamp(max(r["ct"] for r in prs.values()), NY).isoformat()},
        "snapshot_start": s_start["sha"], "snapshot_end": s_end["sha"],
        "new_dirs_all": len(new_dirs), "undated_dirs": undated,
        "new_work_folders": len(rows), "fellows": len(fellows),
        "frictional_logs": counts["frictional"],
        "piece_counts": counts, "folders": rows,
        "_t": (t0, t1),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(DEFAULT_REPO))
    ap.add_argument("--ref", default=DEFAULT_REF)
    a = ap.parse_args()
    ref = git(a.repo, "rev-parse", a.ref).strip()
    log(f"repo {a.repo}  ref {ref}")
    fp = first_parent(a.repo, ref)
    nonmono = sum(1 for x, y in zip(fp, fp[1:]) if x["ct"] < y["ct"])
    log(f"first-parent commits: {len(fp)}; non-monotonic committer times: {nonmono}")

    tw = week(a.repo, ref, fp, THIS_WEEK, "THIS WEEK")
    lw = week(a.repo, ref, fp, LAST_WEEK, "LAST WEEK (recount)")

    # Why might the recount differ from what was published? Re-run last week with the
    # snapshot taken just before its latest PR merge (the "late merge" hypothesis).
    t0, t1 = lw["_t"]
    late = lw["latest_pr"]
    before_late = [r for r in fp if t0 <= r["ct"] <= t1]
    late_ct = int(datetime.fromisoformat(late["merged_at"]).timestamp())
    s_end = snapshot(fp, late_ct - 1)
    s_start = snapshot(fp, t0 - 1)
    nd = sorted(folders_at(a.repo, s_end["sha"]) - folders_at(a.repo, s_start["sha"]))
    nd_work = [d for d in nd if DATED.search(d.split("/")[2])]
    fr = sum(pieces_of(files_in(a.repo, s_end["sha"], d))["frictional"] for d in nd)
    hyp = {"snapshot": s_end["sha"],
           "merged_prs": sum(1 for r in before_late if r["ct"] < late_ct and
                             re.match(r"Merge pull request #\d+", r["subject"]) and len(r["parents"]) >= 2),
           "new_dirs_all": len(nd), "new_work_folders": len(nd_work),
           "fellows_all_dirs": len({d.split('/')[1] for d in nd}),
           "frictional_logs_all_dirs": fr}
    log(f"late-merge check: before PR #{late['number']} ({late['merged_at']}): {hyp}")

    by_n = sorted(tw["folders"], key=lambda r: (-r["n_pieces"], r["folder"]))
    hist = {}
    for r in tw["folders"]:
        hist[r["n_pieces"]] = hist.get(r["n_pieces"], 0) + 1
    order = sorted(PIECES, key=lambda p: -tw["piece_counts"][p[0]])
    most, least = order[0], order[-1]
    full_ish = [r["folder"] for r in by_n if r["n_pieces"] == by_n[0]["n_pieces"]]
    median_pieces = sorted(r["n_pieces"] for r in tw["folders"])[len(tw["folders"]) // 2]
    log(f"pieces-per-folder histogram: {dict(sorted(hist.items()))}")
    log(f"most common: {most[1]} {tw['piece_counts'][most[0]]}; least: {least[1]} {tw['piece_counts'][least[0]]}")
    log(f"top folders ({by_n[0]['n_pieces']} of {len(PIECES)}): {full_ish}")

    # Sensitivity: the same counts if every new folder (dated or not) counted as work.
    def all_dirs_counts(days):
        t0, t1 = ny_epoch(days[0])[0], ny_epoch(days[1], end=True)[0]
        s0, s1 = snapshot(fp, t0 - 1)["sha"], snapshot(fp, t1)["sha"]
        nd = sorted(folders_at(a.repo, s1) - folders_at(a.repo, s0))
        return {"new_dirs_all": len(nd), "fellows_all_dirs": len({d.split('/')[1] for d in nd}),
                "frictional_logs_all_dirs": sum(pieces_of(files_in(a.repo, s1, d))["frictional"] for d in nd)}
    sens = {"this_week": all_dirs_counts(THIS_WEEK), "last_week": all_dirs_counts(LAST_WEEK)}
    log(f"sensitivity (undated folders counted too): {sens}")

    # Example folders for the "what complete looks like" beat: the 8-of-9 folders.
    examples = {r["folder"]: [l for p, l, _ in PIECES if r["pieces"][p]]
                for r in by_n if r["n_pieces"] == by_n[0]["n_pieces"]}
    missing_at_max = sorted({l for r in by_n if r["n_pieces"] == by_n[0]["n_pieces"]
                             for p, l, _ in PIECES if not r["pieces"][p]})
    log(f"pieces missing from every top folder: {missing_at_max}")

    # The narrator's own folder: is fellows/boopesh-m on main at this ref?
    on_main = bool(git(a.repo, "ls-tree", ref, "--", "fellows/boopesh-m").strip())
    log(f"fellows/boopesh-m on main at {ref[:8]}: {on_main}")

    for w in (tw, lw):
        w.pop("_t")
    diff = {k: lw[k] - LAST_WEEK_PUBLISHED[k] for k in LAST_WEEK_PUBLISHED}
    results = {
        "generated_by": "code/week_stats.py",
        "ref": ref,
        "timezone": "America/New_York",
        "pieces": [{"id": p, "label": l} for p, l, _ in PIECES],
        "this_week": tw,
        "last_week_recount": lw,
        "last_week_published": LAST_WEEK_PUBLISHED,
        "recount_minus_published": diff,
        "recount_differs": any(diff.values()),
        "late_merge_check": hyp,
        "sensitivity_all_dirs": sens,
        "top_folder_pieces": examples,
        "boopesh_m_on_main": on_main,
        "summary": {
            "folders_with_six_plus": sum(1 for r in tw["folders"] if r["n_pieces"] >= 6),
            "folders_with_three_or_fewer": sum(1 for r in tw["folders"] if r["n_pieces"] <= 3),
            "folders_at_max_count": len(full_ish),
            "missing_from_every_top_folder": missing_at_max,
            "merged_prs": tw["merged_prs"],
            "new_work_folders": tw["new_work_folders"],
            "fellows": tw["fellows"],
            "frictional_logs": tw["frictional_logs"],
            "n_pieces": len(PIECES),
            "piece_counts_sorted": [[l, tw["piece_counts"][p]] for p, l, _ in order],
            "most_common": [most[1], tw["piece_counts"][most[0]]],
            "least_common": [least[1], tw["piece_counts"][least[0]]],
            "pieces_hist": {str(k): v for k, v in sorted(hist.items())},
            "median_pieces": median_pieces,
            "max_pieces": by_n[0]["n_pieces"],
            "folders_at_max": full_ish,
            "folders_with_all_pieces": sum(1 for r in tw["folders"] if r["n_pieces"] == len(PIECES)),
            "folders_with_zero_to_two": sum(1 for r in tw["folders"] if r["n_pieces"] <= 2),
        },
    }
    blob = json.dumps(results, indent=2, sort_keys=True)
    (HERE / "results.json").write_text(blob + "\n")
    log(f"results.json sha256 {hashlib.sha256((blob + chr(10)).encode()).hexdigest()}")
    (HERE / "run.log").write_text("\n".join(LOG) + "\n")


if __name__ == "__main__":
    sys.exit(main())
