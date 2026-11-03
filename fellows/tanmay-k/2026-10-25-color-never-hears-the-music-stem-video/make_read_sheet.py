#!/usr/bin/env python3
"""make_read_sheet.py: the read-aloud sheet is the script's narration and nothing else.

    python3 make_read_sheet.py            # checks READ-ALOUD.md and READ-ALOUD-SHORT.md against the script, line for line
    python3 make_read_sheet.py --write    # writes plain sheets (READ-ALOUD.new.md, READ-ALOUD-SHORT.new.md) from the script

Gate P is signed on the sheet, so a mismatch here means a signed line has changed and needs a fresh read.
"""
import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LONG = HERE / ("BEATS-DRAFT.md" if (HERE / "BEATS-DRAFT.md").exists() else "SCRIPT.md")
SHORT = next(p for p in (HERE / "SHORT-SCRIPT.md", HERE / "short" / "SHORT-SCRIPT.md") if p.exists())


def script_lines(path, prefix):
    text = path.read_text()
    pat = re.compile(r"^(?:\*\*|### )(" + prefix + r"\d\d) · ([^·\n*]+?)(?: · ~\d+ s(?: \+ \d+ s hold)?)?(?:\*\*)?(?: \(tone: [^)]*\))?\s*$", re.M)
    ms = list(pat.finditer(text))
    out = []
    for i, m in enumerate(ms):
        body = text[m.end(): ms[i + 1].start() if i + 1 < len(ms) else len(text)]
        body = re.split(r"\n#{2,3} |\n\*\*(?:Runtime|Notes)", body)[0]
        out.append((m.group(1), m.group(2).strip().rstrip("*"), " ".join(l[2:].strip() for l in body.splitlines() if l.startswith("> "))))
    return out


def sheet_lines(path):
    t = path.read_text()
    return [(m.group(1), m.group(3).strip()) for m in re.finditer(r"^\*\*([BS]\d\d) · ([^*]+?)\*\* \((?:~\d+ s, )?\d+ words\)\n\n(.*?)\n", t, re.M)]


def main():
    ok = True
    for src, sheet, prefix in ((LONG, HERE / "READ-ALOUD.md", "B"), (SHORT, next((p for p in (HERE / "READ-ALOUD-SHORT.md", HERE / "short" / "READ-ALOUD-SHORT.md") if p.exists()), HERE / "READ-ALOUD-SHORT.md"), "S")):
        lines = script_lines(src, prefix)
        if "--write" in sys.argv:
            body = [f"# READ-ALOUD ({src.name})\n", "Narration only, in order, as the voice will say it.\n"]
            body += [f"**{i} · {t}** ({len(n.split())} words)\n\n{n}\n" for i, t, n in lines]
            sheet.with_suffix(".new.md").write_text("\n".join(body))
            continue
        if not sheet.exists():
            print(f"{sheet.name}: missing"); ok = False; continue
        a = {i: n for i, _, n in lines}
        b = dict(sheet_lines(sheet))
        diff = [i for i in a if a[i] != b.get(i)] + [i for i in b if i not in a]
        print(f"{sheet.name}: {len(b)} lines vs {len(a)} in {src.name}; mismatching: {diff or 'none'}")
        ok = ok and not diff
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
