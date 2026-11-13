#!/usr/bin/env python3
"""
chapters.py — emit a YouTube chapter list from a beat sheet, and refuse to
emit an invalid one.

WHY THIS EXISTS
  A beat is not a chapter. This reel's B00 (the spoken sign-in) measures
  7.98 s, and YouTube requires every chapter to be at least 10 seconds. One
  short chapter does not shorten the list — it disables the whole list, so
  the video ships with no chapters at all and nothing warns you.

  So short beats must be MERGED FORWARD into the following chapter rather
  than published as their own. That is what this script does, and it exits
  non-zero if the result still breaks a rule.

YOUTUBE'S RULES (all enforced below)
  1. the first timestamp must be 00:00
  2. at least 3 chapters
  3. every chapter at least 10 seconds long
  4. timestamps in ascending order

USAGE
  python3 chapters.py                        # this reel
  python3 chapters.py --sheet path/to/beat_sheet.json
  python3 chapters.py --min-seconds 10       # override the floor
  python3 chapters.py --names "Intro,Two tables,..."   # custom labels

Durations come from actual_duration_s (measured audio), never from estimates,
so the timestamps match the rendered master exactly.
"""
import argparse, json, sys
from pathlib import Path

MIN_DEFAULT = 10.0        # YouTube's per-chapter minimum, in seconds
MIN_CHAPTERS = 3


def mmss(t: float) -> str:
    t = int(t)                      # floor: a chapter must not start early
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def build(beats, min_s):
    """Merge any beat shorter than min_s forward into the next chapter."""
    chapters, pending = [], []
    for bid, name, dur in beats:
        pending.append((bid, name, dur))
        total = sum(d for _, _, d in pending)
        if total >= min_s:
            label = " + ".join(n for _, n, _ in pending)
            ids = [b for b, _, _ in pending]
            chapters.append({"ids": ids, "name": label, "seconds": total})
            pending = []
    if pending:
        # tail too short to stand alone — fold it back into the last chapter
        if chapters:
            chapters[-1]["ids"] += [b for b, _, _ in pending]
            chapters[-1]["name"] += " + " + " + ".join(n for _, n, _ in pending)
            chapters[-1]["seconds"] += sum(d for _, _, d in pending)
        else:
            chapters.append({"ids": [b for b, _, _ in pending],
                             "name": " + ".join(n for _, n, _ in pending),
                             "seconds": sum(d for _, _, d in pending)})
    start = 0.0
    for c in chapters:
        c["start"] = start
        c["ts"] = mmss(start)
        start += c["seconds"]
    return chapters


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", default=None)
    ap.add_argument("--min-seconds", type=float, default=MIN_DEFAULT)
    ap.add_argument("--names", default=None, help="comma-separated chapter labels")
    a = ap.parse_args()

    sheet_path = Path(a.sheet) if a.sheet else Path(__file__).parent / "beat_sheet.json"
    sheet = json.loads(sheet_path.read_text())

    beats = []
    for b in sheet["beats"]:
        dur = b.get("actual_duration_s")
        if dur is None:
            sys.exit(f"[chapters] {b['beat_id']} has no actual_duration_s — "
                     f"generate audio first; estimates must not drive timestamps")
        act = (b.get("act") or b["beat_id"]).split("—")[-1].strip()
        beats.append((b["beat_id"], act, float(dur)))

    total = sum(d for _, _, d in beats)
    chapters = build(beats, a.min_seconds)

    if a.names:
        labels = [x.strip() for x in a.names.split(",")]
        if len(labels) != len(chapters):
            sys.exit(f"[chapters] got {len(labels)} names for {len(chapters)} chapters")
        for c, n in zip(chapters, labels):
            c["name"] = n

    print("# paste into the YouTube description\n")
    for c in chapters:
        print(f"{c['ts']} {c['name']}")

    print("\n# audit")
    for c in chapters:
        print(f"  {c['ts']:>7}  {c['seconds']:6.2f}s  {','.join(c['ids']):<12} {c['name']}")
    print(f"  total {sum(c['seconds'] for c in chapters):.2f}s "
          f"(reel {total:.2f}s)")

    lens = [c["seconds"] for c in chapters]
    checks = {
        "first chapter starts at 00:00": chapters[0]["ts"] in ("0:00", "0:00:00"),
        f"at least {MIN_CHAPTERS} chapters": len(chapters) >= MIN_CHAPTERS,
        f"every chapter >= {a.min_seconds:g}s": all(x >= a.min_seconds for x in lens),
        "timestamps ascending": all(chapters[i]["start"] < chapters[i + 1]["start"]
                                    for i in range(len(chapters) - 1)),
        "chapter total == reel length": abs(sum(lens) - total) < 0.01,
        "no two chapters share a timestamp": len({c["ts"] for c in chapters}) == len(chapters),
    }
    print()
    bad = [k for k, v in checks.items() if not v]
    for k, v in checks.items():
        print(f"  [{'ok' if v else 'FAIL'}] {k}")
    if bad:
        sys.exit(f"\n[chapters] REFUSING to emit — {len(bad)} rule(s) broken. "
                 f"A single bad chapter disables the entire list on YouTube.")
    print(f"\n[chapters] {len(chapters)} chapters, shortest {min(lens):.2f}s — valid.")


if __name__ == "__main__":
    main()
