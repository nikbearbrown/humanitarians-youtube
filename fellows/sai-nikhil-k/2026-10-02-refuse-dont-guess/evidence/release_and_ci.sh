#!/bin/bash
# release_and_ci.sh — measure the week's releases, update manifests and CI from GitHub (not from the README).
#   bash release_and_ci.sh > release_and_ci.out
R=nikhil-kunapareddy/gavia
echo "# release_and_ci — gh api, run $(date -u +%Y-%m-%dT%H:%M:%SZ) · $(gh --version | head -1)"
echo; echo "## release assets (bytes, MiB)"
gh api repos/$R/releases --jq '.[] | select(.tag_name|test("v0.(2.0|3.0|3.1)")) | "\(.tag_name) published \(.published_at) prerelease=\(.prerelease)", (.assets[] | "   \(.name)  \(.size) B  \((.size/1048576*10|round)/10) MiB  uploaded \(.created_at) by \(.uploader.login)")'
echo; echo "## update manifests (latest.json)"
for t in v0.3.0 v0.3.1; do echo "### $t"; gh release download $t -R $R -p latest.json -O - | python3 -c '
import json,sys; d=json.load(sys.stdin)
print("   version", d["version"], "pub_date", d["pub_date"])
for k,v in d["platforms"].items(): print("  ", k, v["url"].split("/")[-1], "signature", len(v["signature"]), "chars")'; done
echo; echo "## updater config (desktop/src-tauri/tauri.conf.json @ v0.3.1)"
gh api "repos/$R/contents/desktop/src-tauri/tauri.conf.json?ref=v0.3.1" --jq .content | base64 -d | python3 -c '
import json,sys; u=json.load(sys.stdin)["plugins"]["updater"]; print("   endpoints", u["endpoints"]); print("   pubkey (minisign, base64)", u["pubkey"][:24]+"…")'
echo; echo "## CI on the two release tags"
for t in v0.3.0 v0.3.1; do id=$(gh run list -R $R --branch $t --limit 1 --json databaseId --jq '.[0].databaseId'); echo "### $t run $id"; gh run view $id -R $R --json jobs --jq '.jobs[] | "   \(.name): \(.conclusion)"'; done
