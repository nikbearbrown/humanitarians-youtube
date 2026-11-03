"""Portrait-only props for hai-fourth-week-reverse-engineer/vertical (shorter copy, never smaller type)."""
import json, sys, pathlib
P = {
 "B00": {"largeText": False, "segment": "Reverse Engineer It"}, "B05": {"largeText": False}, "B11": {"largeText": False},
 "B01": {"text": "Every\nvideo\nis built\nfrom\nscratch.", "fontSize": 300, "lineSpacing": 1.3},
 "B02": {"buildLabel": "BUILD", "reverseLabel": "SAVE", "line": "Decide once. Save it.",
         "stages": [{"label": "Idea", "saved": "Brief", "at": 0.29, "savedAt": 0.78}, {"label": "Script", "saved": "Spine", "at": 0.33, "savedAt": 0.73},
                    {"label": "Voice", "saved": "Voice", "at": 0.37, "savedAt": 0.68}, {"label": "Visuals", "saved": "Scenes", "at": 0.4, "savedAt": 0.63},
                    {"label": "Render", "saved": "Checks", "at": 0.46, "savedAt": 0.58}]},
 "B03": {"rows": [{"decision": "Voice", "why": "one steady narrator", "at": 0.14}, {"decision": "Greeting", "why": "fresh each week", "at": 0.22},
                  {"decision": "The handle", "why": "brand on every page", "at": 0.36}], "line": "Next editor, same call."},
 "B04": {"spineLabel": "FIXED", "slotLabel": "SLOTS",
         "slots": [{"label": "TOPIC", "value": "Week 4 playbook", "at": 0.64}, {"label": "EXAMPLES", "value": "Our build log", "at": 0.68},
                   {"label": "PROMPT", "value": "Reverse engineer", "at": 0.73}]},
 "B07": {"rows": [{"fix": "Labels too small", "rule": "Minimum label size", "at": 0.32, "ruleAt": 0.4},
                  {"fix": "Chip on the logo", "rule": "Keep the corner clear", "at": 0.51, "ruleAt": 0.62}],
         "luck": "Once is luck.", "process": "Written down: process."},
 "B08": {"firstLabel": "First video", "nextLabel": "With the playbook",
         "gains": [{"title": "Speed", "why": "no blank page", "at": 0.1}, {"title": "Efficiency", "why": "checks first", "at": 0.31},
                   {"title": "Consistency", "why": "same spine", "at": 0.62}], "caption": "Illustrative"},
 "B09": {"loopLabel": "Keep updating it."},
 "B10": {"artifactTitle": "One page", "artifactHeading": "Build, then reverse",
         "artifactLines": ["Build one video.", "Log every decision.", "Template + playbook.", "Every fix → a rule."],
         "largeText": False, "textScale": 2.0},
 "B12": {"title": "Week 4 Learning:\nBuild It, Then\nReverse\nEngineer It", "scale": 0.8},
}
def apply(sheet_path, rename=False):
    p = pathlib.Path(sheet_path); d = json.loads(p.read_text(encoding="utf-8"))
    for b in d["beats"]:
        r = b["shot"]["remotion"]
        if rename and not r["pattern"].endswith("916"):
            r["pattern"] += "916"
        r["props"].update(P.get(b["beat_id"], {}))
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("portrait props applied:", p)
if __name__ == "__main__":
    apply(sys.argv[1], rename=len(sys.argv) > 2)
