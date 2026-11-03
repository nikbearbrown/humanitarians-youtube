#!/usr/bin/env bash
# Build the 2160x3840 companion for one fantasy reel, end to end.
#
#   PY=<venv python> bash make_vertical_all.sh gdd|walkthrough|gamedev
#
# Order matters: remotion_scenes.py rewrites the vertical beat_sheet.json from the copy
# it loaded, so the B01 edit goes before it and the native portrait cards go after it.
set -euo pipefail
NAME=$1
C="$(cd "$(dirname "$0")" && pwd)"
R="$(dirname "$C")/claude-liam-fantasy-$NAME"
ART=/Users/yeshwanthbalaji/Documents/Brutalist_Updated
PY=${PY:-python3}
export PATH="$(dirname "$PY"):$PATH"

case $NAME in
  gdd)         TEXT=$'Fantasy Survival Crafting\nwas built from its GDD.\nNothing is signed off.' ;;
  walkthrough) TEXT=$'Fantasy Survival Crafting\nis a crafting game.\nSurvive one night.' ;;
  gamedev)     TEXT=$'Fantasy Survival Crafting\nis built from scenes.\nGDScript builds the valley.' ;;
esac

cd "$ART"
./art vertical "$R" 2>&1 | tail -2
"$PY" "$C/make_vertical.py" "$R" 2>&1 | tail -2
B01_TEXT="$TEXT" "$PY" - "$R/vertical/beat_sheet.json" <<'EOF'
import json, os, sys
p = sys.argv[1]; s = json.load(open(p))
b = next(b for b in s['beats'] if b['beat_id'] == 'B01')
pr = b['shot']['remotion']['props']
text = os.environ['B01_TEXT']
assert pr['triggerWords'] in text, (pr['triggerWords'], text)
assert len(text.split()) <= 12
assert len(text.replace(pr['triggerWords'], pr['replacementWords']).split()) <= 12
pr.update(fontSize=150, lineSpacing=1.5, text=text)
json.dump(s, open(p, 'w'), indent=1, ensure_ascii=False)
print('B01 set:', ' / '.join(text.splitlines()))
EOF
"$PY" runtime/scripts/remotion_scenes.py "$R/vertical" 2>&1 | grep "\[remotion\] B" || true
CARDS=$(cd "$C" && "$PY" -c "
import make_vertical_cards as m
jobs = [('gdd', b) for b in m.GDD] + list(m.VERDICTS) + [('gamedev', b) for b in m.TREE_CARDS]
jobs += [('gamedev', b) for b in m.gamedev_code_cards()]
print(' '.join(f'{r}:{b}' for r, b in jobs if r == '$NAME'))")
echo "cards: $CARDS"
"$PY" "$C/make_vertical_cards.py" $CARDS 2>&1 | tail -4
for f in SHOTLIST.md FACTCHECK.md PROMPTS.md SOURCES.md; do [ -f "$R/$f" ] && cp "$R/$f" "$R/vertical/"; done
./art final "$R/vertical" --height 3840 --fps 30 --out "$R/exports/vertical"
