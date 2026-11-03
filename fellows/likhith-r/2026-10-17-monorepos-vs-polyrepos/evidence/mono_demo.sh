#!/usr/bin/env bash
# Toy monorepo evidence for claude-hai-monorepos-polyrepos.
# Builds a throwaway repo under $TMPDIR, makes ONE atomic commit across three
# projects, then clones it with a sparse checkout and counts what lands on disk.
set -euo pipefail
W="$(mktemp -d)"; trap 'rm -rf "$W"' EXIT
export GIT_AUTHOR_NAME=demo GIT_AUTHOR_EMAIL=demo@example.com GIT_COMMITTER_NAME=demo GIT_COMMITTER_EMAIL=demo@example.com
export GIT_AUTHOR_DATE="2026-10-21T12:00:00Z" GIT_COMMITTER_DATE="2026-10-21T12:00:00Z"
cd "$W"; git init -q -b main mono; cd mono
projects="apps/web apps/mobile services/billing services/search services/ads libs/auth libs/ui tools/ci"
for p in $projects; do mkdir -p "$p"; for i in $(seq -w 1 50); do echo "// $p file $i" > "$p/f$i.ts"; done; done
echo 'export const login = (u) => check(u);' > libs/auth/index.ts
echo 'import { login } from "libs/auth";'  > apps/web/main.ts
echo 'import { login } from "libs/auth";'  > apps/mobile/main.ts
git config uploadpack.allowFilter true; git config uploadpack.allowAnySHA1InWant true
git add -A; git commit -q -m "initial import"
echo "== atomic change: rename login -> signIn in the library AND every caller =="
sed -i.bak 's/login/signIn/g' libs/auth/index.ts apps/web/main.ts apps/mobile/main.ts; rm -f */*/*.bak
git commit -qam "auth: rename login to signIn (library + callers)"
git show --stat --format='commit %h  %s' HEAD | sed '/^$/d'
total=$(git ls-files | wc -l | tr -d ' ')
echo "== sparse checkout: clone, then materialise only apps/web + libs/auth =="
cd "$W"; git clone -q --no-checkout --filter=blob:none "file://$W/mono" sparse; cd sparse
git sparse-checkout set apps/web libs/auth
git checkout -q main
ondisk=$(git ls-files -t | grep -c "^H" || true); ondisk=$(find . -path ./.git -prune -o -type f -print | wc -l | tr -d " ")
echo "files in repo:    $total"
echo "files on disk:    $ondisk"
echo "dirs on disk:     $(ls -d */* | tr '\n' ' ')"
