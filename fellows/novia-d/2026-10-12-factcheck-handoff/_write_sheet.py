#!/usr/bin/env python3
"""Handoff sheet — what we added on top of the professor's prompt.

Does not replace chapter14-json-fix or chapter14-second-read.
Source: SOURCE.md (copy of FACTCHECK_HANDOFF.md). Source lives under fellows/novia-d.
"""
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


YOUR_TURN = (
    "Your turn. Open the next empty folder. Check whether a package already exists. "
    "Split the files into three or four batches. Merge them into one JSON. "
    "Run the checks. Generate the four files from that JSON — never the other way around."
)


add(
    beat_id="B00", act="OPEN", lane="BOOKEND", est=14,
    narration_text="Hello Novia. This is Bella. This is the handoff. Not another fact-check of one file. This is what we built on top of the professor's prompt — so the next person can run it.",
    new_visual_element="Handoff cold open",
    shot=remotion("ClaudeComposerAsk", {
        "greeting": "Hello Novia",
        "topic": "HANDOFF · FACT-CHECK PIPELINE",
        "segment": "The Handoff",
        "command": "What did we add on top of the original prompt?",
        "runningText": "opening the handoff…",
        "folderLabel": "@Medhavy",
        "output": [
            "Not a new chapter pass. The extra system.",
            "One chapter at a time. JSON is the record.",
            "Four files. Two safety checks. Then status.",
        ],
    }, "composer ask — handoff frame"),
)

add(
    beat_id="B01", act="I — The frame", lane="REMOTION", est=14,
    narration_text="The original spec asked for one Markdown report from the whole book. What I leave is a pipeline you can rerun: one chapter at a time, JSON as the record, four files generated from it, and two checks that catch silent skips.",
    new_visual_element="BLUF — prompt vs pipeline",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "The handoff, in one breath",
        "artifactHeading": "The prompt asked for a report. We built a pipeline.",
        "artifactLines": [
            "Prompt: one Markdown file. Whole book.",
            "What we ship: one chapter, then the next.",
            "JSON first. Four files generated. Two checks.",
        ],
        "sparkLine": "Everything below is on top of the prompt.",
    }, "BLUF prompt vs pipeline"),
)

add(
    beat_id="B02", act="I — The frame", lane="REMOTION", est=12,
    narration_text="That is the split. Part A is the starting spec. Part B is what we added. Eight additions. Then how one sentence moves. Then what is done.",
    new_visual_element="What this video covers",
    shot=remotion("ClaudeScienceLayerStack", {
        "sparkLine": "Spec first. Then what we added.",
        "layers": [
            {"title": "Part A — the prompt", "sub": "One report. Whole book."},
            {"title": "Part B — eight additions", "sub": "Rules, JSON, four files, two checks", "accent": True},
            {"title": "Then the flow, then status", "sub": "How one sentence moves. What is done."},
        ],
        "caption": "This video is the handoff document, spoken.",
    }, "spec then additions"),
)

add(
    beat_id="B03", act="II — Eight additions", lane="REMOTION", est=13,
    narration_text="First: we do not read the whole book in one pass. Some files have more than one thousand two hundred sentences. Each chapter gets its own folder. Inside it we split the files into three or four batches, run them together, then merge.",
    new_visual_element="One chapter at a time",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "Addition 1",
        "artifactHeading": "One chapter at a time.",
        "artifactLines": [
            "Prompt: one report for the whole book.",
            "Some files: 1,200+ sentences. Too much for one pass.",
            "Split into 3–4 batches. Merge. Then the next folder.",
        ],
        "sparkLine": "A folder per chapter. Not one giant pass.",
    }, "one chapter at a time"),
)

add(
    beat_id="B04", act="II — Eight additions", lane="REMOTION", est=12,
    narration_text="Second: two rules the prompt never stated. Every bullet, including a sub-bullet, is its own sentence. A bold-only header line — like Mechanisms, colon — is skipped. It is not a sentence.",
    new_visual_element="Bullet and header rules",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "Addition 2",
        "artifactHeading": "What counts as a sentence.",
        "artifactLines": [
            "Every bullet is its own sentence. Sub-bullets too.",
            "A bold-only header is skipped.",
            "The prompt never said this. We had to.",
        ],
        "sparkLine": "Count the items. Skip the labels.",
    }, "bullet and header rules"),
)

add(
    beat_id="B05", act="II — Eight additions", lane="REMOTION", est=14,
    narration_text="Third: six categories. Each has an approved list of sites. Only those sites. If none confirm the claim, the answer is unverified. Do not wander. We approve the whole domain — pages move — and we added a couple of extra domains where the same source publishes in more than one place.",
    new_visual_element="Approved sites only",
    shot=remotion("ClaudeScienceChipGrid", {
        "sparkLine": "Approved sites only.",
        "items": [
            "STAT",
            "GUIDELINE",
            "APPROVAL",
            "EVIDENCE",
            "SPECIALIST",
            "CURRENT",
        ],
        "cols": 3,
        "caption": "If none confirm it: unverified. Do not look elsewhere.",
    }, "six locked categories"),
)

add(
    beat_id="B06", act="II — Eight additions", lane="REMOTION", est=13,
    narration_text="Fourth: the prompt asked for one Markdown file. We save JSON first. The Excel workbook and both Markdown reports are generated from that file. Fix a verdict once. Regenerate. A spreadsheet cell holds one value. A sentence can need a list.",
    new_visual_element="JSON is the record",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "Addition 4",
        "artifactHeading": "JSON is the record.",
        "artifactLines": [
            "Prompt: one Markdown file.",
            "We store JSON first. Excel is generated.",
            "A cell holds one value. A sentence can need a list.",
        ],
        "sparkLine": "Fix once. Regenerate the rest.",
    }, "JSON first"),
)

add(
    beat_id="B07", act="II — Eight additions", lane="REMOTION", est=14,
    narration_text="Fifth: one sentence, many sources. Each source keeps its own link and its own verdict — confirmed, outdated, unverified, or contradicted. On top of that list we added one overall verdict for the whole sentence: true, false, or flagged. False or flagged always means expert review is yes.",
    new_visual_element="One sentence, many sources",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "Addition 5",
        "artifactHeading": "One sentence. A list of sources.",
        "artifactLines": [
            "Each source: link + verdict + detail.",
            "Overall: TRUE / FALSE / FLAGGED.",
            "FALSE or FLAGGED → Expert Review = Yes.",
        ],
        "sparkLine": "Overall verdict is a judgment, not a vote.",
    }, "evidence list + overall"),
)

add(
    beat_id="B08", act="II — Eight additions", lane="REMOTION", est=13,
    narration_text="Sixth: four files instead of one. JSON is the data. An Excel workbook with four sheets — and a place on every sheet for a reviewer's decision. Two Markdown reports: one for flagged sentences, one for AI-only, editorial, and the hallucination check.",
    new_visual_element="Four files from JSON",
    shot=remotion("ClaudeScienceLayerStack", {
        "sparkLine": "Four files. One record.",
        "layers": [
            {"title": "JSON", "sub": "The real data. Fix it here.", "accent": True},
            {"title": "Excel · four sheets", "sub": "Summary · flagged · AI-Only · editorial"},
            {"title": "Two Markdown reports", "sub": "Flagged/verified · AI-Only + editorial + check"},
        ],
        "caption": "Every Excel sheet has a reviewer decision column. The prompt did not.",
    }, "four files"),
)

add(
    beat_id="B09", act="II — Eight additions", lane="MANIM", est=14,
    narration_text="Seventh: the AI-only second read is required, not optional. A zero is not automatically safe. This already went wrong once. A chapter reported zero issues out of one thousand five hundred ninety-nine sentences. A real re-check found twenty-six genuine problems.",
    new_visual_element="Manim: zero is not safe",
    **manim("B09_ZeroNotSafe", "0 of 1599, then 26"),
)

add(
    beat_id="B10", act="II — Eight additions", lane="REMOTION", est=13,
    narration_text="Eighth: two extra safety checks, every time. Completeness: did we actually capture every sentence? A batch once said done and had secretly skipped most of a file. And classification-bypass: no AI-only sentence may be marked true from memory. If a category name like Evidence shows up inside an AI-only tag, that is a warning.",
    new_visual_element="Two safety checks",
    shot=remotion("ClaudeWindow", {
        "view": "artifact",
        "artifactTitle": "Addition 8",
        "artifactHeading": "Two checks. Every package. Every time.",
        "artifactLines": [
            "Completeness: every sentence captured.",
            "A batch once said done — and skipped most of a file.",
            "Bypass: no AI-Only tag may hide an EVIDENCE decision.",
        ],
        "sparkLine": "Green checks are not enough. Run both.",
    }, "completeness + bypass"),
)

add(
    beat_id="B11", act="III — How a sentence moves", lane="REMOTION", est=14,
    narration_text="How one sentence moves. Does it match one of the six categories? No: AI-only path. Re-read with no website. Record whether it sounds right. Yes: search only the approved sites. One evidence entry per source. Then one overall verdict. False or flagged means expert review.",
    new_visual_element="Sentence split: AI-only or flagged",
    shot=remotion("ClaudeScienceSourceFlow", {
        "sparkLine": "One sentence. Two paths.",
        "sourceLabel": "Sentence from the file",
        "feeds": [
            {"label": "No → AI-ONLY"},
            {"label": "Yes → approved sites only"},
        ],
        "destApp": "Four-file package",
        "destTitle": "JSON first. Then the views.",
        "arcCaption": "Six categories decide the path. Unverified if the approved list cannot confirm it.",
        "settleLine": "FALSE or FLAGGED → expert review.",
    }, "sentence flow"),
)

add(
    beat_id="B12", act="IV — Status", lane="MANIM", est=12,
    narration_text="Status as of October twelfth, twenty twenty-six. Thirty-six packages are done — all on the current format.",
    new_visual_element="Manim: what is done",
    **manim("B12_WhatIsDone", "36 current format as of 2026-10-12"),
)

add(
    beat_id="B13", act="CLOSE", lane="BOOKEND", est=14,
    narration_text="Let's recap with Claude. The prompt asked for one report. We built a chapter pipeline. JSON is the record. Four files are generated from it. The AI-only second read is required. Two checks run every time. That is the handoff.",
    new_visual_element="Verdict artifact",
    shot=remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "The handoff",
        "artifactHeading": "On top of the prompt: a pipeline you can rerun.",
        "artifactLines": [
            "One chapter at a time. Approved sites only.",
            "JSON first. Four files generated.",
            "AI-Only second read is required. Zero is not safe.",
            "Completeness + bypass. Then the next folder.",
        ],
    }, "verdict recap"),
)

add(
    beat_id="B14", act="CLOSE", lane="BOOKEND", est=16,
    narration_text=(
        YOUR_TURN
        + " That prompt is the start of the next package. Look for a missing file, or a check that was skipped. The JSON is the thing you trust."
    ),
    new_visual_element="Your turn prompt",
    shot=remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.",
        "topic": "HANDOFF · FACT-CHECK PIPELINE",
        "segment": "The Handoff",
        "command": YOUR_TURN,
        "runningText": "handoff…",
        "folderLabel": "@Medhavy",
        "output": [
            "Check the folder first. Do not overwrite a package.",
            "JSON first. Generate the four files from it.",
        ],
    }, "your-turn composer"),
)

add(
    beat_id="B15", act="CLOSE", lane="BOOKEND", est=5,
    narration_text="The Handoff. On top of the prompt.",
    new_visual_element="Title restate",
    shot=remotion("ClaudeTitleOutro", {
        "title": "The Handoff.",
        "handle": "@Medhavy",
        "subline": "On top of the prompt · the pipeline, not one report",
    }, "title outro"),
)


body = [b for b in beats if b.get("lane") != "BOOKEND"]
hist = {"VOX": 0, "MANIM": 0, "REMOTION": 0, "CARD": 0}
for b in body:
    hist[b["lane"]] = hist.get(b["lane"], 0) + 1
n = len(body)

sheet = {
    "metadata": {
        "title": "The Handoff.",
        "slug": "factcheck-handoff",
        "topic": "HANDOFF · FACT-CHECK PIPELINE",
        "purpose": "Handoff reel — what we added on top of the professor's prompt. Does not replace chapter14 videos.",
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
        "date": "2026-10-11",
        "clock": "narration",
        "source": "youtube/factcheck-handoff/SOURCE.md (FACTCHECK_HANDOFF.md)",
        "acts": [
            "I — The frame",
            "II — Eight additions",
            "III — How a sentence moves",
            "IV — Status",
        ],
        "lane_histogram_plan": {
            "vox": hist["VOX"],
            "manim": hist["MANIM"],
            "remotion": hist["REMOTION"],
            "card": hist["CARD"],
            "body_total": n,
            "vox_share": round(hist["VOX"] / n, 3) if n else 0,
        },
        "note": "HANDOFF. Local only. Do not push. Bella / af_bella. Hello Novia. No VOX. No GitHub.",
    },
    "beats": beats,
}

out = REEL / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {out}  beats={len(beats)} body={n} hist={hist}")
