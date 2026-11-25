#!/usr/bin/env bash
# Snapshot every HyperFrames composition at 35/62/95% of its beat (contact sheet per composition).
cd "$(dirname "$0")/hyperframes" || exit 1
for f in ${ONLY:-B0?-?.html}; do
  n=${f%.html}; b=${n%-?}
  D=$(python -c "import json;print([x['actual_duration_s'] for x in json.load(open('../beat_sheet.json',encoding='utf-8'))['beats'] if x['beat_id']=='$b'][0])")
  AT=$(FR="${FR:-0.35,0.62,0.95}" python -c "import os;d=$D;print(','.join(f'{d*float(x):.2f}' for x in os.environ['FR'].split(',')))")
  cp "$f" index.html
  rm -rf ../_snap/$n
  npx.cmd --no-install hyperframes snapshot --at $AT -o ../_snap/$n --no-end > /dev/null 2>&1 || echo "snapshot failed $n"
done
echo SNAPS-DONE
