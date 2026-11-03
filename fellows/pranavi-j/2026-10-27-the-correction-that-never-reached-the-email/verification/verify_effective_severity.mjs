/**
 * Live verification harness for the C3 fix (Generate Email node,
 * workflow.dev.json, Project 29 regulatory intelligence pipeline).
 *
 * Extracts the REAL, current jsCode from the "Generate Email" node in the
 * real workflow.dev.json on disk (not a rewritten copy) and runs it in a
 * sandboxed Node vm against a 3-item synthetic batch covering every real
 * case this node sees, with $("High Priority Filter").all() shimmed to
 * return that batch (same shimming approach this week's own investigation
 * used, per RUN_LOG.md's 2026-10-27 entry and C3-VERIFICATION.md).
 *
 * Then reconstructs the PRE-FIX version of the same real code by undoing
 * exactly the diff shown in C3-VERIFICATION.md (string-substituting the
 * `effectiveImpact()` block back to the original two-line
 * `impact_level`-only bucketing), confirmed to match that diff's context
 * before trusting it as a faithful "before" baseline — same discipline as
 * this fellow's 2026-10-20 report's verify_source_feed.py (reconstruct the
 * pre-fix signature instead of `git checkout`-ing the real repo).
 *
 * Does NOT modify anything in /Users/pranavijs/mycroft — read-only.
 */
import fs from "node:fs";
import vm from "node:vm";

const WORKFLOW_PATH =
  "/Users/pranavijs/mycroft/scripts/regulatory-intel/workflow.dev.json";

const workflow = JSON.parse(fs.readFileSync(WORKFLOW_PATH, "utf8"));
const node = workflow.nodes.find((n) => n.name === "Generate Email");
if (!node) {
  throw new Error('Node "Generate Email" not found in workflow.dev.json');
}
const postFixCode = node.parameters.jsCode;
if (!postFixCode.includes("effectiveImpact")) {
  throw new Error(
    "Real jsCode no longer contains effectiveImpact() — C3 fix may have " +
      "been reverted or renamed; harness assumptions are stale."
  );
}

// --- Reconstruct the PRE-FIX version by undoing exactly the C3 diff -------
// (C3-VERIFICATION.md, "The fix" section). Confirmed below that the needle
// occurs exactly once before trusting the substitution.
const POST_FIX_BLOCK = `const effectiveImpact = (item) => (item.json.llm_reviewed && item.json.llm_corrected_impact_level)
  ? item.json.llm_corrected_impact_level
  : item.json.impact_level;

const criticalItems = newItems.filter(i => effectiveImpact(i) === 'Critical');
const highItems = newItems.filter(i => effectiveImpact(i) === 'High');`;

const PRE_FIX_BLOCK = `const criticalItems = newItems.filter(i => i.json.impact_level === 'Critical');
const highItems = newItems.filter(i => i.json.impact_level === 'High');`;

const occurrences = postFixCode.split(POST_FIX_BLOCK).length - 1;
if (occurrences !== 1) {
  throw new Error(
    `Expected the post-fix block to appear exactly once in the real jsCode, found ${occurrences}. ` +
      "Refusing to build an untrustworthy pre-fix reconstruction."
  );
}
const preFixCode = postFixCode.split(POST_FIX_BLOCK).join(PRE_FIX_BLOCK);

// --- The 3-item batch: every real case Generate Email sees ----------------
// Mirrors C3-VERIFICATION.md's verification table exactly.
function item(json) {
  return { json };
}

const BATCH = [
  // 1 — confirmed, recategorized: keyword scorer said Critical, Layer 2
  // reviewed it, confirmed it's real, but corrected the label to High.
  item({
    id: "item-1",
    title: "SEC proposes amendment to Rule 15c3-5",
    source_feed: "SEC Press Releases",
    link: "https://example.gov/item-1",
    urgency_score: 8,
    impact_level: "Critical",
    llm_reviewed: true,
    llm_verdict: "confirm",
    llm_corrected_impact_level: "High",
    llm_reasoning: "Substantive new rule, not an enforcement action.",
    llm_downgrade: false,
  }),
  // 2 — confirmed, no change: Layer 2 reviewed it and agreed with the
  // original label.
  item({
    id: "item-2",
    title: "FINRA enforcement action against broker-dealer",
    source_feed: "FINRA Enforcement News",
    link: "https://example.gov/item-2",
    urgency_score: 7,
    impact_level: "High",
    llm_reviewed: true,
    llm_verdict: "confirm",
    llm_corrected_impact_level: "High",
    llm_reasoning: "Correctly scored as High, no correction needed.",
    llm_downgrade: false,
  }),
  // 3 — never reviewed: below the urgency_score > 6 review threshold, so
  // Layer 2 never ran on it; behaves exactly as before this fix either way.
  item({
    id: "item-3",
    title: "CFTC routine procedural filing",
    source_feed: "CFTC Regulations",
    link: "https://example.gov/item-3",
    urgency_score: 5,
    impact_level: "Critical",
    llm_reviewed: false,
    llm_downgrade: false,
  }),
];

function runGenerateEmail(code, items) {
  const sandbox = {
    $: (nodeName) => {
      if (nodeName !== "High Priority Filter") {
        throw new Error(`Unexpected node lookup: ${nodeName}`);
      }
      return { all: () => items };
    },
    console,
    Date,
  };
  vm.createContext(sandbox);
  const script = new vm.Script(`(function(){\n${code}\n})()`);
  const result = script.runInContext(sandbox, { timeout: 5000 });
  const out = result[0].json;
  return {
    total_new: out.total_new,
    critical_count: out.critical_count,
    high_count: out.high_count,
    item_ids: out.item_ids,
  };
}

const pre = runGenerateEmail(preFixCode, BATCH);
const post = runGenerateEmail(postFixCode, BATCH);

console.log("=== PRE-FIX (reconstructed: original impact_level-only bucketing) ===");
console.log(pre);
console.log();
console.log("=== POST-FIX (real, current jsCode from workflow.dev.json on disk) ===");
console.log(post);
console.log();
console.log("=== Per-item bucket (post-fix, effectiveImpact) ===");
for (const it of BATCH) {
  const j = it.json;
  const eff = j.llm_reviewed && j.llm_corrected_impact_level ? j.llm_corrected_impact_level : j.impact_level;
  console.log(`${j.id}: impact_level=${j.impact_level} llm_reviewed=${j.llm_reviewed} llm_corrected_impact_level=${j.llm_corrected_impact_level ?? "(none)"} -> effective=${eff}`);
}

console.log();
console.log("=== ASSERTIONS ===");
const assertions = [
  ["pre.critical_count === 2", pre.critical_count === 2],
  ["pre.high_count === 1", pre.high_count === 1],
  ["post.critical_count === 1", post.critical_count === 1],
  ["post.high_count === 2", post.high_count === 2],
  ["post.total_new === pre.total_new (3)", post.total_new === pre.total_new && post.total_new === 3],
];
let failed = false;
for (const [label, ok] of assertions) {
  console.log(`${ok ? "PASS" : "FAIL"} — ${label}`);
  if (!ok) failed = true;
}
if (failed) {
  console.error("\nONE OR MORE ASSERTIONS FAILED.");
  process.exit(1);
}
console.log(
  "\nALL ASSERTIONS PASSED: item-1 (confirmed, recategorized Critical -> High) " +
    "was counted Critical before the fix (bug) and High after (fixed). " +
    "item-2 and item-3 are unchanged in both versions (no regression)."
);
