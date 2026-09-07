#!/usr/bin/env python3
"""Weekly-update sheet for chapter14-json-fix (video 2 — do not replace video 1)."""
import json
from pathlib import Path

REEL = Path(__file__).resolve().parent


def remotion(pattern, props, show):
    return {
        "type": "REMOTION",
        "source": "own",
        "show": show,
        "remotion": {"pattern": pattern, "props": props},
    }


def manim(scene, show):
    return {
        "shot": {"type": "GRAPHIC", "source": "manim", "show": show},
        "graphic": {"manim": scene, "engine": "manim"},
    }


beats = []


def add(**kw):
    b = {
        "voice": "af_bella",
        "engine": "kokoro",
        "classification": kw.pop("classification", "SHOW"),
        "estimated_duration_s": kw.pop("est", 12),
    }
    b.update(kw)
    beats.append(b)


JSON_SNIPPET = """{
  "id": 21,
  "claim": "Warburg effect, historical attribution",
  "overall_verdict": "TRUE",
  "evidence": [
    { "source": "pubmed...21508971", "verdict": "CONFIRMED" },
    { "source": "nature.com/nrc3038", "verdict": "CONFIRMED" },
    { "source": "pubmed...27911732", "verdict": "CONFIRMED" }
  ]
}"""

YOUR_TURN = (
    "Your turn. Put last week's Sites Visited cell next to this week's evidence list. "
    "Which one can a program regenerate the workbook from — and why?"
)


add(
    beat_id="B00", act="OPEN", lane="BOOKEND", est=14,
    narration_text="Hello Novia. This is Bella. Last video showed the fact-check itself. This week is the change: how we store more than one source per claim.",
    new_visual_element="Weekly-update cold open",
    shot=remotion("ClaudeComposerAsk", {
        "greeting": "Hello Novia",
        "topic": "WEEKLY UPDATE · TME METHOD",
        "segment": "One Sentence, Many Sources",
        "command": "Last video was the fact-check. This week: how do you store more than one source per claim?",
        "runningText": "opening this week's change…",
        "folderLabel": "@Medhavy",
        "output": [
            "Video 2 of this file — the record, not the counts.",
            "A row holds one cell. Forty-two claims needed a list.",
            "JSON is the record. Excel is a generated view.",
        ],
    }, "composer ask — weekly frame"),
)

add(
    beat_id="B01", act="I — This week's change", lane="REMOTION", est=13,
    narration_text="The workbook is no longer the record. JSON is. Because a spreadsheet row can hold one Sites Visited cell — and forty-two of forty-six flagged claims needed a list.",
    new_visual_element="BLUF — this week's change",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "This week's change",
        "artifactHeading": "Stop treating the spreadsheet as the record.",
        "artifactLines": [
            "Last video: the fact-check.",
            "This week: the data model.",
            "JSON first. Workbook generated.",
        ],
        "sparkLine": "A fact-check is a workbook, not a vibe.",
    }, "weekly BLUF"),
)

add(
    beat_id="B02", act="I — This week's change", lane="REMOTION", est=11,
    narration_text="Already done: one hundred thirty-eight sentences, forty-six flagged, one hundred fifteen evidence entries, approved sites only. That work stands. This week is how that evidence is stored.",
    new_visual_element="What already stands",
    shot=remotion("ClaudeScienceLayerStack", {
        "sparkLine": "Already done. Then the record.",
        "layers": [
            {"title": "Read + classify", "sub": "138 sentences · six files"},
            {"title": "Verify on approved sites", "sub": "46 flagged · 115 evidence entries", "accent": True},
            {"title": "This week — store it", "sub": "JSON first. Workbook generated from the file"},
        ],
        "caption": "The counts are last week's video. The list is this week's.",
    }, "already done vs this week"),
)

add(
    beat_id="B03", act="II — The row problem", lane="REMOTION", est=10,
    narration_text="So here is the question I had to answer. If one sentence has three independent sources — where do you put them?",
    new_visual_element="Interactive ask — where do three sources go?",
    shot=remotion("ClaudeComposerAsk", {
        "greeting": "Question.",
        "topic": "WEEKLY UPDATE · TME METHOD",
        "segment": "The row problem",
        "command": "If one sentence has three independent sources — where do you put them?",
        "runningText": "waiting on the old workflow…",
        "folderLabel": "@Medhavy",
        "output": [
            "Not a trick. This is the Sites Visited cell.",
        ],
    }, "ask: where do three sources go"),
)

add(
    beat_id="B04", act="II — The row problem", lane="REMOTION", est=13,
    narration_text="In the original workflow: into Markdown, then into Excel. No JSON. One row per assertion. One Sites Visited cell. That worked when each claim had a single source.",
    new_visual_element="Old workflow answer",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "The old answer",
        "artifactHeading": "Markdown + Excel. No JSON.",
        "artifactLines": [
            "One row per assertion.",
            "One Sites Visited cell.",
            "The workbook itself was the record.",
        ],
        "sparkLine": "Fine for one source. Not for a list.",
    }, "old workflow"),
)

add(
    beat_id="B05", act="II — The row problem", lane="REMOTION", est=14,
    narration_text="Then the standard became two to four sources per claim — sometimes disagreeing. A row holds one value per column. Everything flattened into that one cell. You could not tell which source produced which verdict.",
    new_visual_element="Why the cell fails",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "Why the cell fails",
        "artifactHeading": "A row holds one value per column.",
        "artifactLines": [
            "Two to four sources in one cell.",
            "Sometimes the sources disagree.",
            "You cannot tell which source produced which verdict.",
        ],
        "sparkLine": "A limit of the format — not a sloppy row.",
    }, "why the cell fails"),
)

add(
    beat_id="B06", act="II — The row problem", lane="MANIM", est=14,
    narration_text="That is not one broken row. Four claims had one source. Eighteen had two. Twenty-one had three. Three had four. Forty-two of forty-six flagged assertions hit the same wall.",
    new_visual_element="Manim: why other rows",
    **manim("B06_OtherRows", "4 · 18 · 21 · 3 — 42 of 46"),
)

add(
    beat_id="B07", act="II — The row problem", lane="REMOTION", est=10,
    narration_text="Could we just keep the Markdown report? It already lists sources under a sentence. Why add a file?",
    new_visual_element="Interactive ask — is Markdown enough?",
    shot=remotion("ClaudeComposerAsk", {
        "greeting": "Question.",
        "topic": "WEEKLY UPDATE · TME METHOD",
        "segment": "The row problem",
        "command": "Markdown already lists sources under a sentence. Why add a file?",
        "runningText": "waiting on the hand-off…",
        "folderLabel": "@Medhavy",
        "output": [
            "Looks organized. Isn't data.",
        ],
    }, "ask: is Markdown enough"),
)

add(
    beat_id="B08", act="II — The row problem", lane="REMOTION", est=12,
    narration_text="Because Markdown looks organized to a person. To a program it is unlabeled text. Hand-retyping into Excel is where the list became a string.",
    new_visual_element="Markdown is not data",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "Why Markdown was not enough",
        "artifactHeading": "Looks organized. Isn't data.",
        "artifactLines": [
            "A person can read a numbered list.",
            "A program cannot trust it.",
            "The hand-off into Excel flattened the sources.",
        ],
        "sparkLine": "JSON removes that hand-off.",
    }, "markdown handoff"),
)

add(
    beat_id="B09", act="II — The row problem", lane="MANIM", est=11,
    narration_text="One cell cannot hold a list. One sentence needs many independent sources, each with its own verdict. That is the Sites Visited problem, on screen.",
    new_visual_element="Manim: one cell vs three sources",
    **manim("B09_OneToMany", "Sites Visited flattened → source cards"),
)

add(
    beat_id="B10", act="III — The JSON fix", lane="REMOTION", est=12,
    narration_text="JSON holds a list inside an object. One assertion, many evidence entries. The sentence is stored once. Each source keeps its own URL and its own verdict.",
    new_visual_element="The fix named",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "This week's fix",
        "artifactHeading": "One assertion. Many evidence entries.",
        "artifactLines": [
            "Nested list — not a text cell.",
            "Sentence and overall verdict stored once.",
            "Each source: URL, verdict, explanation.",
        ],
        "sparkLine": "The data model matches the relationship.",
    }, "JSON one-to-many"),
)

add(
    beat_id="B11", act="III — The JSON fix", lane="REMOTION", est=11,
    narration_text="Assertion twenty-one. The Warburg sentence. Three confirmed sources, stored as a list, not a cell. Overall verdict: true.",
    new_visual_element="ClaudeCodeBeat schema ID 21",
    shot=remotion("ClaudeCodeBeat", {
        "title": "factcheck.json — assertion 21",
        "code": JSON_SNIPPET,
        "sparkLine": "One sentence. A list.",
    }, "JSON evidence list"),
)

add(
    beat_id="B12", act="III — The JSON fix", lane="MANIM", est=10,
    narration_text="Three confirmed sources sit under a true verdict. PubMed, Nature, PubMed again. The list stays visible. Nothing is flattened.",
    new_visual_element="Manim: ID 21 three CONFIRMED",
    **manim("B12_WarburgThree", "TRUE above three CONFIRMED"),
)

add(
    beat_id="B13", act="III — The JSON fix", lane="REMOTION", est=12,
    narration_text="That is this week's fix. JSON is the record. The workbook is generated from it. Fix a verdict once. Regenerate. Rows are a view, not storage.",
    new_visual_element="JSON first, Excel is a view",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "Source of truth",
        "artifactHeading": "JSON stores. Excel displays.",
        "artifactLines": [
            "Workbook generated from the file.",
            "One evidence row in the view — not in storage.",
            "Correct once. Regenerate.",
        ],
        "sparkLine": "Do not treat rows as storage.",
    }, "JSON is the record"),
)

add(
    beat_id="B14", act="III — The JSON fix", lane="REMOTION", est=9,
    narration_text="Last question. What if the sources disagree? Do you average them? Do you pick the first?",
    new_visual_element="Interactive ask — disagreement",
    shot=remotion("ClaudeComposerAsk", {
        "greeting": "Question.",
        "topic": "WEEKLY UPDATE · TME METHOD",
        "segment": "Judgment, not a vote",
        "command": "What if the sources disagree? Do you average them? Do you pick the first?",
        "runningText": "waiting on the overall verdict…",
        "folderLabel": "@Medhavy",
        "output": [
            "Neither. Overall verdict is a judgment.",
        ],
    }, "ask: what if they disagree"),
)

add(
    beat_id="B15", act="III — The JSON fix", lane="REMOTION", est=13,
    narration_text="No. Overall verdict is a judgment, not a vote. Assertion one twenty-nine: one source confirmed, one outdated. Overall: flagged. A flattened cell would hide that split.",
    new_visual_element="ID 129 — why the list earns the verdict",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "Why the list matters",
        "artifactHeading": "Overall verdict is not a vote.",
        "artifactLines": [
            "ID 129: CONFIRMED + OUTDATED.",
            "Overall: FLAGGED — a split claim.",
            "A flattened cell would hide the split.",
        ],
        "sparkLine": "The list is what makes the judgment visible.",
    }, "judgment not a vote"),
)

add(
    beat_id="B16", act="IV — The count", lane="REMOTION", est=11,
    narration_text="Twenty-five true. Nine false. Twelve flagged. Same one-to-many for every file. The row problem is not unique to this one.",
    new_visual_element="Closing counts",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "The count",
        "artifactHeading": "46 flagged assertions.",
        "artifactLines": [
            "TRUE 25 · FALSE 9 · FLAGGED 12.",
            "115 evidence entries. 24 need expert review.",
            "Same template for the rest of the book.",
        ],
        "sparkLine": "JSON first. Then the view.",
    }, "closing counts"),
)

add(
    beat_id="B17", act="CLOSE", lane="BOOKEND", est=13,
    narration_text="Let's recap with Claude. This week we stopped treating rows as storage. Forty-two of forty-six flagged claims needed a list. JSON stores one assertion, many sources. Excel is a generated view.",
    new_visual_element="Verdict artifact",
    shot=remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "This week's change",
        "artifactHeading": "The row is a view. JSON is the record.",
        "artifactLines": [
            "Last video: the fact-check.",
            "This week: one assertion, many evidence entries.",
            "Forty-two of forty-six flagged claims needed a list.",
            "The workbook is generated. Fix once.",
        ],
    }, "verdict recap"),
)

add(
    beat_id="B18", act="CLOSE", lane="BOOKEND", est=14,
    narration_text=YOUR_TURN,
    new_visual_element="Your turn prompt",
    shot=remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": "WEEKLY UPDATE · TME METHOD",
        "segment": "One Sentence, Many Sources",
        "command": YOUR_TURN,
        "runningText": "handoff…",
        "folderLabel": "@Medhavy",
        "output": [
            "Cell versus list.",
            "Which one regenerates the workbook?",
        ],
    }, "your-turn composer"),
)

add(
    beat_id="B19", act="CLOSE", lane="BOOKEND", est=5,
    narration_text="One Sentence, Many Sources.",
    new_visual_element="Title restate",
    shot=remotion("ClaudeTitleOutro", {
        "title": "One Sentence, Many Sources.",
        "handle": "@Medhavy",
        "subline": "Weekly update · the record, not the counts",
    }, "title outro"),
)


body = [b for b in beats if b.get("lane") != "BOOKEND"]
hist = {"VOX": 0, "MANIM": 0, "REMOTION": 0, "CARD": 0}
for b in body:
    hist[b["lane"]] = hist.get(b["lane"], 0) + 1
n = len(body)

sheet = {
    "metadata": {
        "title": "One Sentence, Many Sources.",
        "slug": "chapter14-json-fix",
        "topic": "WEEKLY UPDATE · TME METHOD",
        "purpose": "Video 2 — weekly update: row problem, why other rows, JSON evidence list. Does not replace chapter14-second-read.",
        "skill": "ai-explainer",
        "register": "Teardown",
        "brand": "claude-bella-novia",
        "channel": "@Medhavy",
        "persona": "Bella (in for Novia)",
        "engine": "kokoro",
        "voice_kokoro": "af_bella",
        "palette": "claude",
        "style_preset": "claude",
        "style": "cli",
        "hello": "Hello Novia",
        "aspect": "16:9",
        "date": "2026-09-04",
        "clock": "narration",
        "source": "youtube/chapter14-json-fix/SOURCE.md (14_factcheck_methodology_report.md)",
        "acts": [
            "I — This week's change",
            "II — The row problem",
            "III — The JSON fix",
            "IV — The count",
        ],
        "lane_histogram_plan": {
            "vox": hist["VOX"],
            "manim": hist["MANIM"],
            "remotion": hist["REMOTION"],
            "card": hist["CARD"],
            "body_total": n,
            "vox_share": round(hist["VOX"] / n, 3) if n else 0,
        },
        "note": "VIDEO 2. Does not replace chapter14-second-read. Bella / af_bella. Hello Novia. Clock 3:00–3:20. No VOX.",
    },
    "beats": beats,
}

out = REEL / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {out}  beats={len(beats)} body={n} hist={hist}")
