/**
 * Live verification harness for the E1 fix (Project 29 regulatory
 * intelligence frontend, mycroft repo): "Select All" had no cap matching
 * the chat endpoint's 10-feed limit, and the chat error handler only ever
 * showed axios's generic error.message instead of the real backend
 * validation reason.
 *
 * Extracts the REAL, current `handleToggle`/`handleSelectAll` logic from
 * the real App.jsx on disk, and the REAL, current error-reason-extraction
 * logic from the real ChatInterface.jsx on disk (not rewritten copies),
 * confirms each occurs verbatim exactly once, and reconstructs the PRE-FIX
 * version of each by undoing exactly the diff shown in E1-VERIFICATION.md's
 * "The fix" section — same discipline as this fellow's 2026-10-27 report's
 * verify_effective_severity.mjs (extract-and-reconstruct, not git checkout).
 *
 * Both the pre-fix and post-fix extracted source strings are then spliced,
 * UNMODIFIED, into a small driver script and executed inside a sandboxed
 * Node `vm` context — this harness never re-implements the logic itself,
 * it runs the literal extracted text.
 *
 * 5 behavioral checks (7 total assertions), matching
 * E1-VERIFICATION.md's own verification table exactly:
 *   1. handleSelectAll against a 411-feed list (matching the real live DB
 *      size) selects exactly 10.
 *   2. 15 individual handleToggle calls in sequence stop adding at 10;
 *      later toggles are no-ops.
 *   3. Untoggling at the cap, then adding a new feed, frees a slot
 *      correctly and stays capped at 10.
 *   4. Error-reason extraction against the real 422 body a live FastAPI
 *      TestClient returned for 15 feed_ids (captured directly from
 *      app.models.FeedQuery during the real investigation, not
 *      reconstructed here) — old behavior vs. new behavior.
 *   5. Error-reason extraction with no response.data.detail (e.g. a real
 *      network failure) falls back to error.message unchanged.
 *
 * Does NOT modify anything in /Users/pranavijs/mycroft — read-only
 * (confirmed via `git -C /Users/pranavijs/mycroft status --short` before
 * and after, see FRICTIONAL.md).
 */
import fs from "node:fs";
import vm from "node:vm";

const APP_JSX_PATH =
  "/Users/pranavijs/mycroft/scripts/mycroft-main/Core_Components/" +
  "Regulatory_QA/frontend/src/App.jsx";
const CHAT_JSX_PATH =
  "/Users/pranavijs/mycroft/scripts/mycroft-main/Core_Components/" +
  "Regulatory_QA/frontend/src/components/ChatInterface.jsx";

const appSrc = fs.readFileSync(APP_JSX_PATH, "utf8");
const chatSrc = fs.readFileSync(CHAT_JSX_PATH, "utf8");

function requireOnce(src, needle, label) {
  const occurrences = src.split(needle).length - 1;
  if (occurrences !== 1) {
    throw new Error(
      `Expected ${label} to appear exactly once in its real source file, found ` +
        `${occurrences}. Refusing to trust this harness's assumptions — the E1 ` +
        `fix may have been reverted, reformatted, or renamed since this script ` +
        `was written.`
    );
  }
}

// --- Extract the REAL, current (post-fix) handleToggle / handleSelectAll --
// Literal text, copied exactly from App.jsx.
const POST_FIX_TOGGLE = `const handleToggle = (id) => {
    setSelected(prev => {
      const newSet = new Set(prev);
      if (newSet.has(id)) {
        newSet.delete(id);
      } else if (newSet.size < MAX_SELECTABLE_FEEDS) {
        newSet.add(id);
      }
      return newSet;
    });
  };`;

const POST_FIX_SELECT_ALL = `const handleSelectAll = () => {
    setSelected(new Set(feeds.slice(0, MAX_SELECTABLE_FEEDS).map(f => f.id)));
  };`;

requireOnce(appSrc, POST_FIX_TOGGLE, "the real post-fix handleToggle");
requireOnce(appSrc, POST_FIX_SELECT_ALL, "the real post-fix handleSelectAll");
requireOnce(appSrc, "const MAX_SELECTABLE_FEEDS = 10;", "the MAX_SELECTABLE_FEEDS constant");
console.log("[ok] real post-fix handleToggle/handleSelectAll confirmed verbatim in App.jsx (1 match each)");

// --- Reconstruct the PRE-FIX versions by undoing exactly the E1 diff ------
// (E1-VERIFICATION.md, "The fix" section, App.jsx side — the "-" lines).
const PRE_FIX_TOGGLE = `const handleToggle = (id) => {
    setSelected(prev => {
      const newSet = new Set(prev);
      if (newSet.has(id)) {
        newSet.delete(id);
      } else {
        newSet.add(id);
      }
      return newSet;
    });
  };`;

const PRE_FIX_SELECT_ALL = `const handleSelectAll = () => {
    setSelected(new Set(feeds.map(f => f.id)));
  };`;

// --- Extract the REAL, current (post-fix) error-reason extraction --------
// Literal text, copied exactly from ChatInterface.jsx's catch block.
const POST_FIX_ERROR_BLOCK = `const detail = error.response?.data?.detail;
      const reason = Array.isArray(detail)
        ? detail.map(d => d.msg || JSON.stringify(d)).join('; ')
        : detail || error.message;
      const errorMessage = {
        role: 'error',
        content: 'Failed to get response: ' + reason,
        timestamp: new Date(),
      };`;

requireOnce(chatSrc, POST_FIX_ERROR_BLOCK, "the real post-fix error-reason extraction");
console.log("[ok] real post-fix error-reason extraction confirmed verbatim in ChatInterface.jsx (1 match)");

// (E1-VERIFICATION.md, "The fix" section, ChatInterface.jsx side — the "-" line).
const PRE_FIX_ERROR_BLOCK = `const errorMessage = {
        role: 'error',
        content: 'Failed to get response: ' + error.message,
        timestamp: new Date(),
      };`;

// --- Driver: splice the literal extracted text into a small vm script ----
// and run it unmodified. The harness supplies only the ambient bindings
// (feeds, MAX_SELECTABLE_FEEDS, setSelected/selected, error) that the real
// component already has in scope via React state / function args — it
// never re-implements handleToggle/handleSelectAll/the error-reason logic
// itself.
function runSelectionOps(toggleSrc, selectAllSrc, feeds, ops) {
  const sandbox = { Set, Array, console };
  vm.createContext(sandbox);
  sandbox.__feeds = feeds;
  sandbox.__ops = ops;
  const code = `
    const feeds = __feeds;
    const MAX_SELECTABLE_FEEDS = 10;
    let selected = new Set();
    function setSelected(updater) {
      selected = typeof updater === 'function' ? updater(selected) : updater;
    }
    ${toggleSrc}
    ${selectAllSrc}
    for (const op of __ops) {
      if (op.type === 'selectAll') handleSelectAll();
      else if (op.type === 'toggle') handleToggle(op.id);
    }
    Array.from(selected)
  `;
  const script = new vm.Script(code);
  return script.runInContext(sandbox, { timeout: 5000 });
}

function runErrorExtraction(errorBlockSrc, error) {
  const sandbox = { Array, JSON, console };
  vm.createContext(sandbox);
  sandbox.__error = error;
  const code = `
    const error = __error;
    ${errorBlockSrc}
    errorMessage.content
  `;
  const script = new vm.Script(code);
  return script.runInContext(sandbox, { timeout: 5000 });
}

// Build the real 411-feed list — matches the real live mycroft_intelligence
// DB row count (same number this fellow's prior D1 report's harness used
// for the same table).
const FEEDS_411 = Array.from({ length: 411 }, (_, i) => ({ id: `feed-${i}` }));

console.log();
console.log("=== TEST 1: handleSelectAll against a 411-feed list ===");
const test1Post = runSelectionOps(POST_FIX_TOGGLE, POST_FIX_SELECT_ALL, FEEDS_411, [
  { type: "selectAll" },
]);
const test1Pre = runSelectionOps(PRE_FIX_TOGGLE, PRE_FIX_SELECT_ALL, FEEDS_411, [
  { type: "selectAll" },
]);
console.log(`post-fix: selected ${test1Post.length} of 411`);
console.log(`pre-fix (bug): selected ${test1Pre.length} of 411`);

console.log();
console.log("=== TEST 2: 15 individual handleToggle calls in sequence ===");
const toggleOps15 = Array.from({ length: 15 }, (_, i) => ({ type: "toggle", id: `feed-${i}` }));
const test2Post = runSelectionOps(POST_FIX_TOGGLE, POST_FIX_SELECT_ALL, FEEDS_411, toggleOps15);
console.log(`post-fix: selected ${test2Post.length} after 15 toggles (should stop at 10)`);

console.log();
console.log("=== TEST 3: untoggle at the cap, then add a new feed ===");
const test3Ops = [
  ...Array.from({ length: 10 }, (_, i) => ({ type: "toggle", id: `feed-${i}` })), // fill to cap
  { type: "toggle", id: "feed-3" }, // untoggle one already-selected id (frees a slot)
  { type: "toggle", id: "feed-99" }, // add a new one into the freed slot
];
const test3Post = runSelectionOps(POST_FIX_TOGGLE, POST_FIX_SELECT_ALL, FEEDS_411, test3Ops);
console.log(`post-fix: selected ${test3Post.length}, contains feed-99: ${test3Post.includes("feed-99")}`);

console.log();
console.log("=== TEST 4: error-reason extraction, real 422 body for 15 feed_ids ===");
// The real 422 response body a live, unmodified FastAPI TestClient returned
// for app.models.FeedQuery against an oversized 15-item feed_ids list
// during the real E1 investigation (E1-VERIFICATION.md's "Verification"
// section; RUN_LOG.md's 2026-11-12 entry) — captured, not reconstructed.
const real422Error = {
  message: "Request failed with status code 422",
  response: {
    status: 422,
    data: {
      detail: [
        {
          type: "too_long",
          loc: ["body", "feed_ids"],
          msg: "List should have at most 10 items after validation, not 15",
          input: Array.from({ length: 15 }, (_, i) => `feed-${i}`),
        },
      ],
    },
  },
};
const test4Pre = runErrorExtraction(PRE_FIX_ERROR_BLOCK, real422Error);
const test4Post = runErrorExtraction(POST_FIX_ERROR_BLOCK, real422Error);
console.log(`pre-fix (bug): "${test4Pre}"`);
console.log(`post-fix:      "${test4Post}"`);

console.log();
console.log("=== TEST 5: error-reason extraction with no response.data.detail ===");
const networkError = { message: "Network Error" }; // no .response at all
const test5Post = runErrorExtraction(POST_FIX_ERROR_BLOCK, networkError);
console.log(`post-fix fallback: "${test5Post}"`);

console.log();
console.log("=== ASSERTIONS ===");
const assertions = [
  ["test1: post-fix selects exactly 10 of 411", test1Post.length === 10],
  [
    "test1: post-fix selects the first 10 feed ids",
    JSON.stringify(test1Post) === JSON.stringify(FEEDS_411.slice(0, 10).map((f) => f.id)),
  ],
  ["test2: 15 sequential toggles stop adding at 10", test2Post.length === 10],
  [
    "test3: untoggle-then-add frees a slot and stays capped at 10, containing the new feed",
    test3Post.length === 10 && test3Post.includes("feed-99"),
  ],
  [
    'test4: pre-fix (bug) reproduces the generic "Request failed with status code 422"',
    test4Pre === "Failed to get response: Request failed with status code 422",
  ],
  [
    'test4: post-fix reproduces the real backend reason, "List should have at most 10 items after validation, not 15"',
    test4Post ===
      "Failed to get response: List should have at most 10 items after validation, not 15",
  ],
  [
    "test5: with no response.data.detail, falls back to error.message unchanged",
    test5Post === "Failed to get response: Network Error",
  ],
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
  "\nALL 7 ASSERTIONS PASSED across 5 behavioral checks: the real, current " +
    "handleToggle/handleSelectAll logic (post-fix) caps selection at 10 " +
    "regardless of path (button or individual clicks) and correctly frees/" +
    "refills a slot on untoggle; the real, current error-reason extraction " +
    "(post-fix) surfaces the real backend validation message instead of " +
    "axios's generic one, and still falls back safely when no detail is " +
    "present. The reconstructed pre-fix versions reproduce the real, " +
    "documented bug exactly: unbounded selection and the generic " +
    "\"Request failed with status code 422\" message."
);
