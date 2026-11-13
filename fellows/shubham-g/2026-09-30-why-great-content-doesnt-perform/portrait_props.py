"""Portrait-only props for why-great-content-doesnt-perform/vertical (shorter copy, never smaller type)."""
import json, sys, pathlib
P = {
 "B00": {"largeText": False},
 "B01": {"text": "Great\ncontent\nalways\nfinds\nits audience.", "fontSize": 280, "lineSpacing": 1.3},
 "B02": {"stallLine": "It stalls.", "caption": ""},
 "B03": {"post": "A budgeting guide", "postTag": "SAME POST", "left": {"label": "Joke scrollers", "verdict": "Skipped", "at": 0.42},
         "right": {"label": "Budget planners", "verdict": "Saved & shared", "at": 0.66}, "line": "Different room."},
 "B04": {"caption": "Illustration"},
 "B05": {"largeText": False},
 "B06": {"chartLabel": "AUDIENCE ONLINE", "axis": [{"h": 0, "label": "12 AM"}, {"h": 12, "label": "12 PM"}, {"h": 24, "label": "12 AM"}],
         "posts": [{"label": "3 AM", "hour": 3, "bar": 0.14, "at": 0.28}, {"label": "7 PM", "hour": 19, "bar": 0.86, "at": 0.59}],
         "barsTitle": "FIRST HOUR", "moreLabel": "→ more people", "caption": "Illustrative"},
 "B07": {"feedLabel": "VIDEO-FIRST FEED", "left": {"title": "Text wall", "verdict": "Skipped", "at": 0.2, "verdictAt": 0.4},
         "right": {"title": "Short video", "verdict": "Watched", "at": 0.55, "verdictAt": 0.92}, "hookLabel": "Point first"},
 "B08": {"strongLabel": "Strong → it grows", "weakLabel": "Weak → it stops", "caption": "Simplified"},
 "B09": {"boostLabel": "Boost", "metricB": "Results", "line": "Paid amplifies fit.",
         "lanes": [{"label": "Wrong audience", "views": 0.9, "results": 0.07, "at": 0.26, "resAt": 0.5},
                   {"label": "Right audience", "views": 0.72, "results": 0.64, "at": 0.73, "resAt": 0.84}]},
 "B10": {"headline": "Sometimes it's the content.",
         "steps": [{"q": "Right people saw it?", "fix": "Fix who sees it", "at": 0.33, "fixAt": 0.45},
                   {"q": "Did they stop?", "fix": "Fix the hook", "at": 0.59, "fixAt": 0.67},
                   {"q": "Did they act?", "fix": "Rework the content", "at": 0.81, "fixAt": 0.88}]},
 "B11": {"artifactTitle": "One page", "artifactHeading": "Quality is one link",
         "artifactLines": ["Quality gets you in.", "Fit: right post, right room.", "Reach them when they're there.",
                           "Hook fast, earn signals.", "Paid amplifies fit."], "largeText": False, "textScale": 2.0},
 "B12": {"largeText": False},
 "B13": {"title": "Why Great\nContent Doesn't\nAlways Perform?", "scale": 0.8},
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
