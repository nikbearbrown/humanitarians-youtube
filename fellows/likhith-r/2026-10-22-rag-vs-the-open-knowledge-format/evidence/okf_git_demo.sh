#!/usr/bin/env bash
# Puts the toy OKF bundle in a throwaway git repo and makes two dated commits to
# metrics/revenue.md, so B06's log + diff are real git output. Fixed author/dates
# make the hashes reproducible. Usage: okf_git_demo.sh <evidence-dir>
set -euo pipefail
E="$1"; W="$(mktemp -d)"
cp -R "$E/okf_bundle/." "$W/"
cd "$W"; git init -q -b main
export GIT_AUTHOR_NAME=likhith GIT_AUTHOR_EMAIL=likhith@example.org GIT_COMMITTER_NAME=likhith GIT_COMMITTER_EMAIL=likhith@example.org
# first version of the metric: no refund rule yet
python3 - <<'PY'
from pathlib import Path
p = Path("metrics/revenue.md"); s = p.read_text()
s = s.replace("Revenue is the sum of `amount` over [orders](../tables/orders.md)\nwith `status = paid`. Refunded orders are excluded; see\n[refunds](../policies/refunds.md).",
              "Revenue is the sum of `amount` over [orders](../tables/orders.md).")
p.write_text(s)
PY
git add -A; GIT_AUTHOR_DATE=2026-10-01T09:00:00-04:00 GIT_COMMITTER_DATE=2026-10-01T09:00:00-04:00 git commit -q -m "Add revenue metric"
cp "$E/okf_bundle/metrics/revenue.md" metrics/revenue.md
git add -A; GIT_AUTHOR_DATE=2026-10-15T09:00:00-04:00 GIT_COMMITTER_DATE=2026-10-15T09:00:00-04:00 git commit -q -m "Exclude refunds from revenue"
echo '$ git log --oneline -- metrics/revenue.md'; git log --oneline -- metrics/revenue.md
echo '$ git diff HEAD~1 -- metrics/revenue.md'; git diff --no-color HEAD~1 -- metrics/revenue.md
git --version
rm -rf "$W"
