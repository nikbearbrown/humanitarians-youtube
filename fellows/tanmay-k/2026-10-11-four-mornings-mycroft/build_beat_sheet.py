#!/usr/bin/env python3
"""Week 26 work video, *Four Mornings*: beat_sheet.json = SCRIPT.md's narration (the source of truth for the
words) + each beat's scene props.

FOUR MORNINGS. Every act opens on the same illustrated dashboard (our verified SAMPLE summary laid out as a
dashboard, labelled as an illustration with invented prices). Under it, a strip of four hand-offs; each morning
lights one. A side panel shows that beat's evidence: a committed file in nikbearbrown/mycroft main @ 5097a8f.

The dashboard's numbers are read from the merged repository itself (`git show 5097a8f:…`, read-only), so the
film cannot show a figure the repository does not hold.

    python3 build_beat_sheet.py            # writes beat_sheet.json (cues on the planning clock until audio exists)

Guards (BEATS.md Part 1): placeholder text, digit years in narration, FACTCHECK drift (W-rows), a cue that is not
in its narration, an evidence beat without a source. Any one fails the build.
"""
import json
import re
from decimal import Decimal, ROUND_HALF_UP
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MYCROFT = HERE.parent.parent / "mycroft"
MERGE = "5097a8f"
VOICE = "am_onyx"
TITLE = "Four Mornings: What a Dashboard Takes on Trust"
SIGNOFF = "Tanmay Kulkarni, in for Humanitarians AI"
WPS = 3.3
MP3 = HERE / "mp3"
MEASURED = json.loads((MP3 / "timings.json").read_text()) if (MP3 / "timings.json").exists() else {}
WORD_TIMES = json.loads((MP3 / "word_times.json").read_text()) if (MP3 / "word_times.json").exists() else {}
sys.path.insert(0, str(Path(__file__).parent))
from cue_align import spoken_at  # noqa: E402  (copied from the topic video: pause-anchored cue clock)

AT_MAIN = f"Mycroft main @ {MERGE}"
ILLUSTRATION = "Illustration: our verified sample summary laid out as a dashboard. Every price is invented."


def show(path: str) -> str:
    """A file as merged into nikbearbrown/mycroft main (read-only)."""
    return subprocess.run(["git", "-C", str(MYCROFT), "show", f"{MERGE}:{path}"],
                          capture_output=True, text=True, check=True).stdout


SUMMARY = json.loads(show("data/verified/portfolio-price-fetcher/clean/portfolio-summary.json"))
VALIDATED = {r["ticker"]: r for r in json.loads(show("data/verified/portfolio-price-fetcher/clean/validated.json"))["records"]}


def money(x) -> str:
    """Two decimals the way the workflow's JavaScript shows them (toFixed: exact binary value, ties away from
    zero). Python's default formatting would show NVDA's 25,228.125 as .12; the dashboard must not round
    differently from the system it illustrates (caught in the first stills review)."""
    d = Decimal(float(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"{d:,.2f}"


def rows(tag=None, extra=None):
    """Dashboard rows from the merged summary; `tag` = {ticker: (state, note)}."""
    out = []
    for s in SUMMARY["stocks"]:
        state, note = (tag or {}).get(s["ticker"], ("normal", ""))
        out.append({"ticker": s["ticker"], "shares": str(s["shares"]), "price": money(s["currentPrice"]),
                    "value": money(s["currentValue"]), "pct": f"{s['gainLossPct']}%", "state": state, "note": note})
    return out + (extra or [])


TOTAL = {"label": "Total value", "value": money(SUMMARY["summary"]["totalCurrentValue"]),
         "pct": f"+{SUMMARY['summary']['totalReturn']}%"}
HANDOFF_LABELS = ["a missing price", "a stock not in the portfolio", "a list written twice", "a call by name"]


def handoffs(states, lit=None, lit_cue=None):
    """states: list of 4 of idle | recorded | stops. lit: index of the hand-off this beat lights, at lit_cue."""
    out = [{"label": l, "state": s} for l, s in zip(HANDOFF_LABELS, states)]
    if lit is not None:
        out[lit]["atCue"] = lit_cue
    return out


def morning(heading, morning_label, row_list, hand, evidence_title, evidence_lines, source, evidence_cue=None,
            compare=None, open_items=None, dim=False, question=None):
    return {"type": "GRAPHIC", "status": "PROPS SET (component planned)", "motion": "illustrate",
            "remotion": {"pattern": "MorningDashboard", "props": {
                "heading": heading, "morningLabel": morning_label, "illustrationNote": ILLUSTRATION,
                "rows": row_list, "total": TOTAL, "handoffs": hand,
                "evidenceTitle": evidence_title, "evidenceLines": evidence_lines, "source": source,
                "evidenceAtCue": evidence_cue,
                "compare": compare or [], "openItems": open_items or [], "dim": dim,
                "question": question or {"text": "", "good": "", "weak": ""}}}}


def card(title, heading, lines, source):
    return {"type": "GRAPHIC", "status": "PROPS SET", "motion": "illustrate", "remotion": {
        "pattern": "ClaudeArtifactCardFull",
        "props": {"chrome": "artifact", "artifactTitle": title, "artifactHeading": heading,
                  "artifactLines": lines, "sparkLine": source}}}


IDLE4 = ["idle"] * 4
META = VALIDATED["META"]

SHOTS = {
    "B01": (morning("A portfolio dashboard, over coffee", "Any morning", rows(), handoffs(IDLE4),
                    "Sample summary", [f"{SUMMARY['summary']['totalStocks']} holdings · total {TOTAL['value']} · return {TOTAL['pct']}"],
                    f"data/verified/portfolio-price-fetcher/clean/portfolio-summary.json · {AT_MAIN}",
                    evidence_cue="One total"), ["W4"]),
    "B02": (card("Mycroft · PR #64, merged", "“both a book and a working agentic repository”",
                 ["Portfolio Dashboard → calls → Portfolio Price Fetcher",
                  "PR #64: checks for both recipes, and the math step rebuilt to run on test data",
                  "Every price in this video is invented"],
                 f"Mycroft README · PR #64, merged 2026-10-11 ({MERGE})"), ["W1", "W2", "W3"]),
    "B03": (morning("Morning one: a price of zero", "Morning 1",
                    rows({"META": ("flagged", "previous close"), "GOOGL": ("flagged", "previous close")}), handoffs(["recorded", "idle", "idle", "idle"], 0, "What changed is the record"),
                    "What the record says now",
                    [f"META · regularMarketPrice: {META['regularMarketPrice']} · previousClose: {META['previousClose']:g}",
                     f"price_source: {META['price_source']}",
                     "The workflow reads: regularMarketPrice || previousClose"],
                    f"data/verified/portfolio-price-fetcher/clean/validated.json · recipe “Notes from porting” · {AT_MAIN}",
                    evidence_cue="zero counts as missing"), ["W5", "W6", "W7", "W8"]),
    "B04": (morning("Morning two: a stock the portfolio doesn't hold", "Morning 2",
                    rows(extra=[{"ticker": "ZZZZ", "shares": "–", "price": "–", "value": "–", "pct": "–",
                                 "state": "rejected", "note": "set aside at step 3"}]),
                    handoffs(["recorded", "stops", "idle", "idle"], 1, "Now the check before it"), "What stops it now",
                    ["The original: const myStock = portfolio[ticker]; const shares = myStock.shares;",
                     "Step 3: “meta.symbol 'ZZZZ' is not in the workflow's portfolio”",
                     "Step 5: refuses to run on rejected data (exit 1), writes nothing"],
                    f"declared workflow, Calculate Metrics · defective/validated.json · self-test C · {AT_MAIN}",
                    evidence_cue="In the original"), ["W9", "W10"]),
    "B05": (morning("Morning three: one list, written twice", "Morning 3", rows(),
                    handoffs(["recorded", "stops", "stops", "idle"], 2, "So the first step now"), "What stops it now",
                    ["Step 1 compares both copies: portfolio_consistent",
                     "Self-test A: “the two portfolio definitions disagree (NVDA shares 50 vs 55): exit 1”"],
                    f"logs/portfolio-price-fetcher-provenance-2026-10-10.json · self-test results · {AT_MAIN}",
                    evidence_cue="So the first step",
                    compare=[{"label": "Define Portfolio · NVDA shares", "value": "50 → 55", "struck": False,
                              "atCue": "Edit the shares in the first", "struckAtCue": None},
                             {"label": "Calculate Metrics · NVDA shares", "value": "50", "struck": False,
                              "atCue": "Edit the shares in the first", "struckAtCue": None}]),
            ["W11", "W12", "W13"]),
    "B06": (morning("Morning four: the call by name", "Morning 4", rows(),
                    handoffs(["recorded", "stops", "stops", "stops"], 3, "So the dashboard's first step"), "What stops it now",
                    ["Call Portfolio Price Fetcher → “Portfolio Price Fetcher” (by name)",
                     "Workflow id: YOUR_WORKFLOW_1_ID (a placeholder)",
                     "Self-test A: “dashboard calls a different workflow by name: exit 1”"],
                    f"logs/portfolio-dashboard-provenance-2026-10-10.json · self-test results · {AT_MAIN}",
                    evidence_cue="So the dashboard's first step"), ["W14", "W15"]),
    "B07": (morning("The morning it was my own check", "Morning 5", rows(),
                    handoffs(["recorded", "stops", "stops", "stops"]), "My own test",
                    ["Self-test comment: “a first version of this check passed against the good summary left in a copied folder”",
                     "Self-test D: “broken port ran: True”, then caught"],
                    f"scripts/tools/portfolio-price-fetcher-self-test.py · self-test results · {AT_MAIN}",
                    evidence_cue="But the broken version",
                    compare=[{"label": "First version of the test", "value": "pass", "struck": True,
                              "atCue": "It passed", "struckAtCue": "But the broken version"},
                             {"label": "Now", "value": "broken version ran · 11,298.13 vs 11,298.12 · caught", "struck": False,
                              "atCue": "Now the test", "struckAtCue": None}]),
            ["W16", "W17"]),
    "B08": (morning("The same dashboard, any morning", "Any morning", rows(),
                    handoffs(["recorded", "stops", "stops", "stops"]), "Both recipes still say DRAFT",
                    ["Both recipes: status DRAFT · todos_open 4 and 7"],
                    f"recipes/portfolio-price-fetcher.md, recipes/portfolio-dashboard.md · logs/RUN_LOG.md · {AT_MAIN}",
                    evidence_cue="And some that still run on trust",
                    open_items=["live prices", "price fetcher steps 2, 4, 6", "dashboard steps 2–6"]), ["W18", "W19"]),
    "B09": (morning("Your number", "Tomorrow morning", rows(), handoffs(["recorded", "stops", "stops", "stops"]),
                    "", [], "", dim=True,
                    question={"text": "What is it quietly taking on trust? And what would tell you if that slipped?",
                              "good": "Good answer: names the hand-off, and the thing that would say so",
                              "weak": "Not an answer: “it's always been right”"}), []),
    "B10": ({"type": "GRAPHIC", "status": "PROPS SET", "motion": "fade", "remotion": {
        "pattern": "ClaudeTitleOutroFull",
        "props": {"title": "Four mornings, one dashboard.", "handle": "@HumanitariansAI", "subline": SIGNOFF}}}, []),
}

PLACEHOLDER = re.compile(r"\b(PLACEHOLDER|TODO|TBD|TK|XXX|lorem)\b")
DIGIT_YEAR = re.compile(r"\b1[0-9]{3}\b|\b20[0-9]{2}\b")


def strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from strings(v)


def main():
    script = (HERE / "SCRIPT.md").read_text()
    beats_src = re.findall(r"^### (B\d\d) · (.+?)\n> (.+?)\n", script, re.M | re.S)
    rows_fc = set(re.findall(r"^\| (W\d+) \|", (HERE / "FACTCHECK.md").read_text(), re.M))
    errors, beats = [], []
    if [b for b, _, _ in beats_src] != list(SHOTS):
        errors.append(f"SCRIPT beats {[b for b, _, _ in beats_src]} != shot table {list(SHOTS)}")
    for bid, title, text in beats_src:
        shot, refs = SHOTS.get(bid, (None, []))
        if shot is None:
            continue
        for r in refs:
            if r not in rows_fc:
                errors.append(f"{bid}: FACTCHECK row {r} missing")
        for s in [text, *strings(shot)]:
            if PLACEHOLDER.search(s.replace("YOUR_WORKFLOW_1_ID", "")):
                errors.append(f"{bid}: placeholder text: {s[:60]!r}")
        if DIGIT_YEAR.search(text):
            errors.append(f"{bid}: digit year in narration: {DIGIT_YEAR.search(text).group()}")
        props = shot["remotion"]["props"]
        if refs and not (props.get("source") or props.get("sparkLine")):
            errors.append(f"{bid}: cites {refs} but shows no source")
        words = len(text.split())
        est = MEASURED.get(bid, round(words / WPS, 1))
        shot["remotion"]["pattern"] += "OFL"
        def resolve(d):
            # "<key>Cue": narration phrase -> "<key>": seconds; reaches into nested items (compare panel)
            if isinstance(d, dict):
                for k in [k for k in d if k.endswith("Cue")]:
                    cue = d.pop(k)
                    if cue is None:
                        d[k[:-3]] = None
                    elif cue not in text:
                        errors.append(f"{bid}: cue not in narration: {cue!r}")
                    else:
                        mp3 = MP3 / f"beat-{bid}.mp3"
                        k_word = len(text[:text.index(cue)].split())
                        if WORD_TIMES.get(bid) and WORD_TIMES[bid][k_word] is not None:
                            d[k[:-3]] = WORD_TIMES[bid][k_word]   # measured: Whisper's start for the cue's first word
                        elif bid in MEASURED and mp3.exists():
                            d[k[:-3]] = spoken_at(text, str(mp3), cue)   # measured: pause-anchored fallback
                        else:
                            d[k[:-3]] = round(len(text[:text.index(cue)].split()) / WPS, 2)   # planning clock
                for v in d.values():
                    resolve(v)
            elif isinstance(d, list):
                for v in d:
                    resolve(v)
        resolve(props)
        props["durationSeconds"] = round(est + 0.1, 2)
        beats.append({"beat_id": bid, "act": title.split(",")[0].strip(), "narration_text": text, "shot": shot,
                      "estimated_duration_s": est, "word_count": words, "audio_file": f"mp3/beat-{bid}.mp3",
                      "engine": "kokoro", "voice": VOICE,
                      "factcheck_ref": [f"FACTCHECK.md {r}" for r in refs] or None})
    if errors:
        sys.exit("BUILD FAILED\n  " + "\n  ".join(errors))
    sheet = {"metadata": {
        "title": TITLE, "title_status": "WORKING", "structure": "FOUR MORNINGS", "slug": "four-mornings",
        "topic": "MYCROFT CONTRIBUTION (PR #64)", "register": "Pragmatist", "audience": "hai",
        "brand": "claude-liam", "channel": "hai", "chip": "@HumanitariansAI",
        "voice": VOICE, "engine": "kokoro", "voice_kokoro": VOICE, "palette": "claude", "style_preset": "claude",
        "ground": "#FAF9F5", "source_commit": f"nikbearbrown/mycroft@{MERGE}",
        "thesis": ("A dashboard is only as honest as the quiet hand-offs behind it. PR #64 puts a check at four of them "
                   "(a missing price, a stock not in the portfolio, a list written twice, a call by name), and my own "
                   "test once passed when it should have failed."),
        "note": "DRAFT (FOUR MORNINGS). Generated by build_beat_sheet.py from SCRIPT.md. MorningDashboard is a planned component.",
    }, "beats": beats}
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
    est = sum(b["estimated_duration_s"] for b in beats)
    print(f"{len(beats)} beats · {sum(b['word_count'] for b in beats)} words · ~{int(est // 60)}:{int(est % 60):02d}")
    for b in beats:
        print(f"  {b['beat_id']} {b['act']:38} {b['word_count']:3}w ~{b['estimated_duration_s']:5}s "
              f"{b['shot']['remotion']['pattern']}")


if __name__ == "__main__":
    main()
