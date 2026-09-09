#!/usr/bin/env python3
"""author_sheets.py — emit BOTH beat sheets for "BLIP: Noisier Data, Better Model?"
from one source of truth.

WHY THIS EXISTS: the reel ships in two orientations. The previous reel in this series
maintained two hand-edited sheets and then verified content parity afterwards with a
diff script. This inverts that: there is ONE authored beat list, and the 9:16 sheet is
a mechanical transform of it (aspect_ratio, the `916` pattern suffix, the slug). Content
divergence between the cuts is therefore impossible by construction, not merely absent.

Run from the reel folder:  python3 author_sheets.py
"""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SIB = HERE.parent / "blip-bootstrap-916"

CITE = "arXiv:2201.12086"
PAPER = "Li, Li, Xiong & Hoi — BLIP, arXiv:2201.12086 (ICML 2022)"

# ─────────────────────────────────────────────────────────────────────────────
# THE BEATS. Spine (ai-explainer): cold open -> executive summary -> body ->
# verdict -> handoff -> title outro. Teaching arc (PROOF): framework BEFORE any
# example (B02), worked example walked live (B04), falsifiability (B05 + B07's
# stated exception), friction the viewer must resolve (B06), scaffolded task (B09).
# ─────────────────────────────────────────────────────────────────────────────
BEATS = [
{
 "beat_id": "B00", "act": "ASK", "motion": "type-on", "est": 7.0,
 "narration": "A model writes its own training captions, then throws a quarter away. "
              "Cleverness, or grading its own homework?",
 "pattern": "ClaudeComposerAsk",
 "show": [
   {"at": "0.00", "event": "cold open on the Claude composer, cream page, spark + 'Merhaba, Ritik'"},
   {"at": "0.20", "event": "the three-part ask types itself into the composer"},
   {"at": "0.70", "event": "send arms terracotta; the answer preview lines land — mechanism, then ablation"},
 ],
 "props": {
   "greeting": "Merhaba, Ritik",
   "topic": "Computational Skepticism",
   "segment": "Bootstrapped Captions",
   "command": "BLIP bootstraps its own training captions: (1) show me the mechanism, "
              "(2) show me the ablation with the bootstrap switched off, and (3) give me one "
              "audit I can run on any paper that trains on data it generated itself.",
   "runningText": f"reading {CITE} (ICML 2022)…",
   "placeholder": "Type / for skills",
   "folderLabel": "@HumanitariansAI",
   "output": [
     "MECHANISM  one model, three functionalities",
     "           captioner writes · filter rejects",
     "ABLATION   14M bootstrapped  80.6 TR@1",
     "           129M raw web      79.6 TR@1",
   ],
 },
},
{
 "beat_id": "B01", "act": "SUMMARY", "motion": "reveal", "est": 11.5,
 "narration": "Web images come with junk captions. BLIP makes two copies of itself: one "
              "writes new captions, one throws out the bad ones. Retrained on the survivors, "
              "fourteen million images beat nine times more raw data.",
 "pattern": "ReelExecSummary",
 "show": [
   {"at": "0.02", "event": "eyebrow, then the title sets in serif — the BLUF, before any specific"},
   {"at": "0.17", "event": "the one-breath thesis reveals as one paragraph"},
   {"at": "0.44", "event": "three numbered cards rise in order: the audit, the mechanism, the receipt"},
 ],
 "props": {
   "spark": "What this is, and why.",
   "eyebrow": "HUMANITARIANS AI · VISION-LANGUAGE",
   "title": "BLIP: Noisier Data, Better Model?",
   "presenter": "with Ritik",
   "thesis": [
     "Web images come with junk captions. BLIP finetunes two copies of itself — one to",
     "write captions, one to reject them — and retrains on whatever survives the cut.",
   ],
   "roadmap": [
     {"label": "The audit", "body": "Four questions for anything trained on data it made itself."},
     {"label": "The mechanism", "body": "One transformer, three jobs: align, match, write."},
     {"label": "The receipt", "body": "14M bootstrapped beats 129M raw — and where it doesn’t."},
   ],
   "source": PAPER,
 },
},
{
 "beat_id": "B02", "act": "FRAMEWORK", "motion": "drawon", "est": 11.5,
 "narration": "Here’s the audit — four questions for anything trained on data it made "
              "itself. Who writes the labels. Is the judge independent. Does the writer take "
              "risks. Is there a run with it switched off.",
 "pattern": "ReelFramework",
 "show": [
   {"at": "0.14", "event": "four numbered axes land one per spoken question, hairline rule above each"},
   {"at": "0.25", "event": "axis 2 (JUDGE) arrives in the terracotta pill — the beat's one accent"},
   {"at": "0.40", "event": "each axis picks up its receipt in mono at the right: the table that proves it"},
   {"at": "0.68", "event": "terracotta rule draws left to right, then the rubric line"},
 ],
 "props": {
   "spark": "Four questions.",
   "heading": "The bootstrap audit",
   "moves": [
     {"label": "GENERATE", "detail": "Who writes the new labels, and with what decoder?", "receipt": "§3.3"},
     {"label": "JUDGE", "detail": "Is the filter a separate copy, or the writer’s twin?", "receipt": "Table 4"},
     {"label": "DIVERSITY", "detail": "Does the writer sample, or play it safe?", "receipt": "Table 2"},
     {"label": "ABLATE", "detail": "Is there a run with the bootstrap switched off?", "receipt": "Table 1"},
   ],
   "accentIndex": 1,
   "keepNote": "Axis 2 is the rubric. A judge that shares weights with the writer rubber-stamps it.",
   "source": f"Receipts are BLIP’s own ablations — {CITE}, Tables 1, 2, 4",
 },
},
{
 "beat_id": "B03", "act": "MECHANISM", "motion": "reveal", "est": 12.0,
 "narration": "One transformer, three jobs: encode text alone, encode it against an image, "
              "or generate it from one. Everything’s shared except the self-attention layers "
              "— so a writer and a judge cost two cheap finetunes.",
 "pattern": "BlipMed",
 "show": [
   {"at": "0.12", "event": "three cards rise in spoken order: unimodal encoder, grounded encoder, grounded decoder"},
   {"at": "0.20", "event": "each card's SA / CA / FFN chips fill in; CA stays dashed on the unimodal card"},
   {"at": "0.55", "event": "each card resolves to its loss — ITC, ITM, LM — and what that loss is for"},
   {"at": "0.78", "event": "the decoder's causal SA chip takes the accent as the sharing rule lands"},
 ],
 "props": {
   "spark": "One model, three hats.",
   "heading": "One transformer, three jobs",
   "hats": [
     {"name": "Unimodal encoder", "loss": "ITC", "lossFull": "image-text contrastive",
      "job": "Align the image and text feature spaces.", "sa": "bi-directional", "ca": False},
     {"name": "Image-grounded encoder", "loss": "ITM", "lossFull": "image-text matching",
      "job": "Judge whether a pair actually matches.", "sa": "bi-directional", "ca": True},
     {"name": "Image-grounded decoder", "loss": "LM", "lossFull": "language modelling",
      "job": "Write a caption for the image.", "sa": "causal", "ca": True},
   ],
   "accentIndex": 2,
   "closing": "Text encoder and decoder share every parameter except the self-attention layers.",
   "source": f"BLIP §3.1–3.2 — {CITE}",
 },
},
{
 "beat_id": "B04", "act": "WORKED-EXAMPLE", "motion": "annotate", "est": 12.0,
 "narration": "Watch it run. This image’s web caption is metadata, not description, so the "
              "filter kills it. The captioner writes a real sentence; that one survives. "
              "Corpus-wide, the filter rejects a quarter of what it’s handed.",
 "pattern": "BlipCapFilt",
 "show": [
   {"at": "0.08", "event": "a drawn web image appears (REBUILD LAW — never a lifted photo)"},
   {"at": "0.16", "event": "its web alt-text lands beneath: Tw, a string of metadata"},
   {"at": "0.28", "event": "the captioner's sentence types in as Ts"},
   {"at": "0.44", "event": "the filter's verdicts land: a terracotta strike draws through Tw, KEEP under Ts"},
   {"at": "0.54", "event": "twenty caption tiles fill the right panel and five strike out — the published 25%"},
   {"at": "0.82", "event": "the closing line: survivors plus the human-annotated pairs become the new set"},
 ],
 "props": {
   "spark": "Write it, then judge it.",
   "heading": "CapFilt, on one image",
   "webText": "IMG_2043 · 1200x800 · stock photo",
   "synthText": "a dog running on the beach near the water",
   "webVerdict": "REJECT — no visual content",
   "synthVerdict": "KEEP",
   "illustrativeNote": "Illustrative: the mechanism and the rate are the paper’s, the two strings are not a paper figure.",
   "rateLabel": "noise ratio",
   "ratePct": 25,
   "rateNote": "the share the filter rejects, nucleus sampling",
   "tiles": 20,
   "closing": "Survivors, plus the human-annotated pairs, become the new pre-training set.",
   "source": f"BLIP §3.3; rate from Table 2, nucleus row — {CITE}",
 },
},
{
 "beat_id": "B05", "act": "EDGE-CASE", "motion": "count-up", "est": 12.5,
 "narration": "Now break it. Let the filter share weights with the captioner and rejection "
              "collapses from twenty-five percent to eight — it stops recognising its twin’s "
              "mistakes. Every downstream number drops. Confirmation bias, measured.",
 "pattern": "BlipIndependence",
 "show": [
   {"at": "0.10", "event": "the shared-weights rejection rate counts up to 8% in ink"},
   {"at": "0.22", "event": "the decoupled rate counts up to 25% in terracotta, beside it for comparison"},
   {"at": "0.40", "event": "four downstream rows land in order, shared column then decoupled column"},
   {"at": "0.70", "event": "the deltas resolve at the right — computed from the two columns, not authored"},
   {"at": "0.82", "event": "the closing line: share the weights and the filter stops seeing its twin"},
 ],
 "props": {
   "spark": "Who filters the filter?",
   "heading": "Let the judge share the writer’s weights",
   "leftLabel": "Shared",
   "rightLabel": "Decoupled",
   "leftNoise": 8,
   "rightNoise": 25,
   "noiseCaption": "of the captioner’s output rejected by the filter",
   "metrics": [
     {"label": "COCO retrieval TR@1", "left": 79.8, "right": 80.6},
     {"label": "COCO retrieval IR@1", "left": 62.2, "right": 63.1},
     {"label": "COCO captioning CIDEr", "left": 129.0, "right": 129.7},
     {"label": "NoCaps zero-shot CIDEr", "left": 103.5, "right": 105.1},
   ],
   "closing": "Share the weights and the filter stops seeing its twin’s mistakes.",
   "source": f"BLIP Table 4 · 14M images, ViT-B/16 — {CITE}",
 },
},
{
 "beat_id": "B06", "act": "FRICTION", "motion": "drawon", "est": 12.5,
 "narration": "Here’s the part that should bother you. Beam search writes safe captions: "
              "nineteen percent rejected. Sampling writes stranger ones: twenty-five percent "
              "rejected. The noisier generator wins — diversity is the payload.",
 "pattern": "BlipDiversity",
 "show": [
   {"at": "0.08", "event": "both axes declare themselves first, including the truncated accuracy floor"},
   {"at": "0.18", "event": "the no-bootstrap row draws: no noise wing, a short accuracy wing"},
   {"at": "0.31", "event": "beam search draws — noise wing 19% left, accuracy wing 79.6 right"},
   {"at": "0.44", "event": "nucleus sampling draws in terracotta: BOTH wings longer. The paradox is the shape"},
   {"at": "0.78", "event": "the closing line: beam writes what's already in the data, sampling writes what isn't"},
 ],
 "props": {
   "spark": "Noisier, and better.",
   "heading": "How the captioner writes",
   "rows": [
     {"label": "No bootstrap", "sub": "web text only", "noise": -1, "score": 78.4},
     {"label": "Beam search", "sub": "deterministic", "noise": 19, "score": 79.6},
     {"label": "Nucleus sampling", "sub": "stochastic, p = 0.9", "noise": 25, "score": 80.6},
   ],
   "accentIndex": 2,
   "noiseMax": 30,
   "scoreFloor": 77,
   "scoreCeil": 81,
   "noiseAxis": "NOISE RATIO — 0 to 30%",
   "scoreAxis": "COCO TR@1 — axis starts at 77",
   "closing": "Beam search writes what is already in the data. Sampling writes what is not.",
   "source": f"BLIP Table 2 · 14M images, ViT-B/16 — {CITE}",
 },
},
{
 "beat_id": "B07", "act": "ABLATION", "motion": "drawon", "est": 13.5,
 "narration": "Axis four. Same images, same backbone. Bootstrap off: 78.4. Filter alone, "
              "captioner alone, then both: 80.6. Nine times the data, unbootstrapped, stops at "
              "79.6 — though on captioning, raw still edges it.",
 "pattern": "BlipLadder",
 "show": [
   {"at": "0.11", "event": "the baseline bar grows to 78.4 and its value counts up with it"},
   {"at": "0.21", "event": "filter-only 79.1, then captioner-only 79.7 — each half of the bootstrap alone"},
   {"at": "0.40", "event": "both together grows to 80.6 in terracotta"},
   {"at": "0.50", "event": "a fifth bar — 129M images, nine times the data, no bootstrap — stops at 79.6"},
   {"at": "0.62", "event": "the dashed reference line draws at 80.6 through every row: the 129M bar falls short"},
   {"at": "0.14", "event": "the axis strip draws with its break glyph and both ticks — this axis starts at 77"},
   {"at": "0.80", "event": "the exception lands beside the claim: on captioning CIDEr the raw 129M edges it"},
 ],
 "props": {
   "spark": "Turn the bootstrap off.",
   "heading": "The ablation",
   "bars": [
     {"label": "No bootstrap", "sub": "14M images", "value": 78.4, "accent": False},
     {"label": "Filter only", "sub": "14M images", "value": 79.1, "accent": False},
     {"label": "Captioner only", "sub": "14M images", "value": 79.7, "accent": False},
     {"label": "Captioner + filter", "sub": "14M images", "value": 80.6, "accent": True},
     {"label": "No bootstrap", "sub": "129M images — 9× the data", "value": 79.6, "accent": False},
   ],
   "refValue": 80.6,
   "floor": 77,
   "ceil": 81.5,
   # kept short on purpose: this renders in a LABEL_W-wide box, which is 350px on
   # the portrait canvas — long enough for this, not for the backbone as well.
   # ViT-B/16 moves to `source`, which wraps and has the room. It is the control
   # variable the ablation rests on, so it has to be legible on BOTH canvases.
   "axisNote": "COCO 5K test · TR@1",
   "exception": "Not everywhere: on COCO captioning the raw 129M edges it — CIDEr 130.1 against 129.7.",
   "source": f"BLIP Table 1 · finetuned COCO 5K test · ViT-B/16 — {CITE}",
 },
},
{
 "beat_id": "B08", "act": "VERDICT", "motion": "reveal", "est": 11.0,
 "narration": "So bootstrapping isn’t self-congratulation. It’s generate-and-judge: "
              "the judge is a separate copy, the writer is allowed to be weird, and someone "
              "published the run with it turned off.",
 "pattern": "ClaudeVerdictArtifact",
 "show": [
   {"at": "0.05", "event": "the Claude artifact page opens — the UI earns this beat, it is the verdict"},
   {"at": "0.15", "event": "four verdict lines set in serif, one per clause of the judgment"},
   {"at": "0.80", "event": "the source note lands under a hairline: the paper and the three tables"},
 ],
 "props": {
   "artifactTitle": "Verdict — BLIP’s CapFilt",
   "artifactHeading": "What the bootstrap earns",
   "artifactLines": [
     "The mechanism is real: one MED runs as encoder, grounded encoder and grounded decoder, sharing all but the self-attention layers.",
     "Independence is load-bearing, not hygiene: share the filter’s weights with the captioner and rejection falls 25% to 8% — every downstream number with it.",
     "Diversity is the captioner’s contribution: nucleus sampling is rejected more often (25% vs 19%) and still wins, 80.6 against 79.6 TR@1.",
     "Bootstrapped 14M beats raw 129M on retrieval — but not on captioning, where 130.1 edges 129.7. Quality beats quantity HERE, not everywhere.",
   ],
   "sourceNote": "Li, Li, Xiong & Hoi — BLIP, ICML 2022. Tables 1, 2 and 4.",
 },
},
{
 "beat_id": "B09", "act": "HANDOFF", "motion": "type-on", "est": 15.0,
 "narration": "Your turn. Paste this into Claude: run the bootstrap audit on a paper that "
              "trains on synthetic data. Quote and grade all four axes, then name the one it "
              "leaves unproven. Most papers ace three and skip one.",
 "pattern": "ClaudeComposerAsk",
 "show": [
   {"at": "0.05", "event": "the composer returns with 'Your turn.' in the greeting slot"},
   {"at": "0.15", "event": "the audit prompt types itself in, read aloud as it lands"},
   {"at": "0.72", "event": "the pass/fail readings appear as output lines — what a good answer looks like"},
 ],
 "props": {
   "greeting": "Your turn.",
   "topic": "Computational Skepticism",
   "segment": "Audit A Bootstrap",
   "command": "Run the bootstrap audit on a paper that trains on data it generated itself. "
              "For each axis, give me the verbatim quote and a PASS or FAIL: (1) GENERATE — who "
              "writes the new labels, with what decoder? (2) JUDGE — is the filter a separate "
              "copy, or does it share weights with the generator? (3) DIVERSITY — sampling or "
              "greedy, and is diversity measured? (4) ABLATE — is there a run with the bootstrap "
              "off, same data, same backbone? Then name the axis the paper leaves unproven.",
   "runningText": "your move…",
   "placeholder": "Type / for skills",
   "folderLabel": "@HumanitariansAI",
   "output": [
     "PASS   a quote per axis · a bootstrap-off run",
     "       · the judge is a separate checkpoint",
     "FAIL   “we filter for quality” with no rate",
     "       · no ablation → the gain is unattributed",
     "WATCH  which axis it skips. Usually axis 2.",
   ],
 },
},
{
 "beat_id": "B10", "act": "OUTRO", "motion": "reveal", "est": 4.5,
 "narration": "Noisier data, better model — if something independent throws the noise out.",
 "pattern": "ClaudeTitleOutro",
 "show": [
   {"at": "0.05", "event": "the episode title restates poster-style in serif with the terracotta period"},
   {"at": "0.45", "event": "the channel handle sets beneath, then the segment subline"},
 ],
 "props": {
   "title": "BLIP: Noisier Data, Better Model?",
   "handle": "@HumanitariansAI",
   "subline": "Computational Skepticism",
 },
},
]

# ─────────────────────────────────────────────────────────────────────────────
META = {
 "title": "BLIP: Noisier Data, Better Model?",
 "slug": "blip-bootstrap",
 "topic": "Computational Skepticism",
 "register": "Teardown",
 "audience": "Claude",
 "brand": "claude",
 "voice": "HumanitariansAI",
 "folderLabel": "@HumanitariansAI",
 "engine": "kokoro",
 "voice_kokoro": "am_onyx",
 "palette": "claude",
 "style_preset": "claude",
 "ground": "#FAF9F5",
 "aspect_ratio": "16:9",
 "fit": "crop",
 "greeting": "Merhaba, Ritik",
 "greeting_note": "hello lexicon: Turkish (rotating off Hindi 'Namaste' from 2026-09-06-vqa-blind, "
                  "which rotated off Zulu 'Sawubona'). Persona is the presenter named in B01 (Ritik); "
                  "channel is @HumanitariansAI. Wagwan is Bear's alone and never applies here.",
 "color_semantics": "Claude fidelity skin throughout. Terracotta marks exactly one thing per beat: "
                    "the JUDGE axis (B02), the decoder's causal self-attention (B03), rejection "
                    "(B04), the decoupled design (B05), nucleus sampling (B06), captioner+filter "
                    "(B07). CLAUDE.SEND is annotation only — B07's reference line and its exception "
                    "rule — never a second subject accent. Everything else is warm ink on cream.",
 "note": "ILLUSTRATE LAW: the Claude UI appears at B00 (ask), B08 (verdict), B09 (handoff), B10 "
         "(outro) only. B01–B07 are concept illustrations — ONE responsive component per beat, "
         "registered at both 1920×1080 and 1080×1920, so the 9:16 twin is the same content and "
         "the same measured audio, never a re-edit. Both sheets are emitted by author_sheets.py "
         "from one beat list, so content divergence is impossible by construction. Every published "
         "number on screen carries its citation in the same frame (the Stage source slot). B04's "
         "two caption strings are illustrative and say so on screen; its 25% rate is published.",
 "companion_reel": "blip-bootstrap-916",
 "playlist": "Fellows Research",
 "tags": ["BLIP", "vision-language pre-training", "CapFilt", "synthetic data", "data filtering",
          "nucleus sampling", "confirmation bias", "ablation", "image-text retrieval",
          "multimodal transformers", "Humanitarians AI"],
}


def build(portrait: bool) -> dict:
    meta = dict(META)
    if portrait:
        meta["slug"] = "blip-bootstrap-916"
        meta["aspect_ratio"] = "9:16"
        meta["companion_reel"] = "blip-bootstrap"
    beats = []
    for b in BEATS:
        pattern = b["pattern"] + ("916" if portrait else "")
        beats.append({
            "beat_id": b["beat_id"],
            "act": b["act"],
            "narration": b["narration"],
            "narration_text": b["narration"],
            "shot": {
                "type": "GRAPHIC",
                "source": "remotion",
                "motion": b["motion"],
                "show": b["show"],
                "remotion": {
                    "pattern": pattern,
                    "props": json.loads(json.dumps(b["props"])),
                    "rendered": {"out": f"media/{b['beat_id']}.mp4", "at": ""},
                },
            },
            "estimated_duration_s": b["est"],
            "audio_file": f"mp3/beat-{b['beat_id']}.mp3",
        })
    return {"metadata": meta, "beats": beats}


if __name__ == "__main__":
    for folder, portrait in ((HERE, False), (SIB, True)):
        folder.mkdir(parents=True, exist_ok=True)
        sheet = build(portrait)
        (folder / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n")
        print(f"wrote {folder.name}/beat_sheet.json  ({len(sheet['beats'])} beats)")
    words = sum(len(re.findall(r"[\w’'-]+", b["narration"])) for b in BEATS)
    est = sum(b["est"] for b in BEATS)
    print(f"narration: {words} words · estimated {est:.1f}s ({est/60:.2f} min)")
    from collections import Counter
    hist = Counter(b["motion"] for b in BEATS)
    n = len(BEATS)
    print("motion:", ", ".join(f"{k}:{v} ({v/n:.0%})" for k, v in hist.most_common()))
