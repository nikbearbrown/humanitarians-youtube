#!/usr/bin/env python3
"""
verify_bench.py — measure the self-correction blind spot on current Claude models.

WHAT THIS MEASURES
    An LLM asked to check its own arithmetic tends to confirm it. Tsui (2025)
    calls this the "self-correction blind spot": models fail to correct errors
    in their OWN output while correcting the SAME error when it is presented as
    coming from somewhere else. Across 14 open non-reasoning models the reported
    average blind-spot rate is 64.5%, and appending the single token "Wait"
    removes 89.3% of it.
        Tsui, "Self-Correction Bench", arXiv:2507.02778 (July 2025) — PREPRINT.
        Huang et al., "LLMs Cannot Self-Correct Reasoning Yet", ICLR 2024
        (arXiv:2310.01798) — peer-reviewed; intrinsic self-correction fails.

    Neither is established for current Claude models. This measures it on our
    own data and reports what it finds, including a null.

REVISION 2 — WHY ERROR INJECTION
    Revision 1 waited for the model to make a natural mistake. It produced a
    clean null (0 misses / 6 wrong answers) but ran out of denominator: Sonnet 5
    answered 9/10 and 10/10 correctly, so the thinking arm had ZERO wrong
    answers and therefore no data at all. The headline question — does the blind
    spot persist in a newer generation — was left unanswered rather than
    answered negatively.

    Tsui did not wait for natural errors either: the paper uses CONTROLLED ERROR
    INJECTION at three complexity levels. This revision does the same, so every
    trial has a denominator by construction.

THE DESIGN

    Task: given four numbers, write an arithmetic expression using each exactly
    once that equals 24. Ground truth is decidable, so the model's opinion about
    correctness is never needed.

    Each trial produces ONE expression to be verified:
      - the model's own answer, when that answer was naturally WRONG  (natural)
      - otherwise its correct answer with one operator corrupted      (injected)

    That single expression is then put through three verification conditions,
    so the only thing that varies is framing:

      A  self-verify      — presented in the assistant turn, as the model's own
      B  external         — FRESH conversation, identical expression presented
                            as a third party's submission
      C  self + "Wait"    — condition A with Tsui's one-token remedy
      D  evaluator        — exact rational arithmetic in Python; ground truth

    A vs B IS THE EXPERIMENT. A two-arm design (self-verify vs evaluator) cannot
    distinguish "the model is bad at this puzzle" from "the model won't
    contradict itself" — both produce an identical result. B separates them, and
    if B fails as often as A the self-reference thesis is dead and we say so.

    NATURAL AND INJECTED ARE NEVER POOLED INTO ONE HEADLINE RATE. They are
    different evidence and are reported separately:
      - natural  : ecologically valid, but arm A carries the model's real
                   working text while arm B does not, so the two arms differ in
                   more than provenance. Stated as a caveat.
      - injected : arm A is a MINIMAL assistant turn containing only the
                   corrupted answer, so A and B present identical information
                   and differ ONLY in provenance. This is the clean comparison.

    Injecting into the assistant turn is the standard way to isolate provenance:
    the model has no memory outside the context window, so an assistant turn is
    its own output as far as it can tell. That is the mechanism under test.

WHY THREE MODEL CONFIGURATIONS
    Thinking defaults differ, and that difference would otherwise be confounded
    with generation:
      haiku-nothink   claude-haiku-4-5, thinking omitted -> no thinking.
                      Matches the non-reasoning class Tsui measured.
      sonnet5-nothink claude-sonnet-5, thinking DISABLED explicitly. Newer
                      generation, same reasoning mode -> isolates generation.
                      Sonnet 5 runs adaptive thinking BY DEFAULT, so omitting
                      the parameter would silently compare a reasoning model
                      against a non-reasoning one.
      sonnet5-think   claude-sonnet-5, thinking ADAPTIVE. Tests Tsui's own
                      hypothesis: that outcome-feedback-trained reasoning closes
                      the blind spot.

    No temperature / top_p / top_k anywhere: non-default sampling parameters are
    rejected with a 400 on Sonnet 5, and omitting them on both models removes a
    confound rather than adding one.

EXACT ARITHMETIC IS NOT OPTIONAL
    8 / (3 - 8/3) is exactly 24 but evaluates to 23.999999999999993 in floating
    point. A float grader marks the correct answer wrong and inverts the whole
    result. Everything here runs on fractions.Fraction.

USAGE
    python3 verify_bench.py --dry-run          # no API, no key, no spend
    python3 verify_bench.py                    # real run (needs credentials)
    python3 verify_bench.py --no-injection     # revision-1 behaviour
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from fractions import Fraction
from typing import Any

# --------------------------------------------------------------------------- #
# Model configurations                                                         #
# --------------------------------------------------------------------------- #

MODELS: dict[str, dict[str, Any]] = {
    "haiku-nothink": {
        "model": "claude-haiku-4-5",
        # Omitted entirely: on Haiku 4.5 that means no thinking.
        # (`effort` is unsupported on this model and must not be sent.)
        "thinking": None,
        # Raised from 1024 in rev 1, which truncated on the harder puzzles.
        "max_tokens": 2048,
        "note": "non-reasoning; matches the model class in Tsui (2025)",
    },
    "sonnet5-nothink": {
        "model": "claude-sonnet-5",
        # MUST be explicit. Sonnet 5 runs ADAPTIVE thinking when omitted.
        "thinking": {"type": "disabled"},
        "max_tokens": 2048,
        "note": "newer generation, thinking off -> isolates generation",
    },
    "sonnet5-think": {
        "model": "claude-sonnet-5",
        "thinking": {"type": "adaptive"},
        # Thinking and response share max_tokens. 4096 truncated in rev 1.
        "max_tokens": 8192,
        "note": "tests whether reasoning closes the blind spot",
    },
}

PUZZLES: list[tuple[int, int, int, int]] = [
    (3, 3, 8, 8), (1, 3, 4, 6), (1, 5, 5, 5), (3, 3, 7, 7),
    (1, 4, 5, 6), (2, 7, 8, 9), (4, 7, 8, 8), (5, 5, 7, 11),
    (2, 3, 4, 6), (1, 2, 3, 4), (4, 6, 1, 1), (8, 3, 1, 1),
]  # all 12 verified brute-force solvable

TARGET = Fraction(24)
LEVELS = ("subtle", "moderate", "obvious")

# --------------------------------------------------------------------------- #
# Arm D: ground truth. Exact rational arithmetic, whitelisted AST.             #
# --------------------------------------------------------------------------- #

_ALLOWED_NODES = (
    ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd,
)
_BIN_OPS = [ast.Add, ast.Sub, ast.Mult, ast.Div]


def eval_exact(expr: str) -> Fraction | None:
    """Evaluate exactly, or None if invalid. Never uses eval()."""
    try:
        tree = ast.parse(expr.strip(), mode="eval")
    except SyntaxError:
        return None
    for node in ast.walk(tree):
        if not isinstance(node, _ALLOWED_NODES):
            return None
        if isinstance(node, ast.Constant) and not isinstance(node.value, int):
            return None

    def walk(node: ast.AST) -> Fraction:
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.Constant):
            return Fraction(node.value)
        if isinstance(node, ast.UnaryOp):
            v = walk(node.operand)
            return -v if isinstance(node.op, ast.USub) else v
        if isinstance(node, ast.BinOp):
            a, b = walk(node.left), walk(node.right)
            if isinstance(node.op, ast.Add):
                return a + b
            if isinstance(node.op, ast.Sub):
                return a - b
            if isinstance(node.op, ast.Mult):
                return a * b
            if isinstance(node.op, ast.Div):
                if b == 0:
                    raise ZeroDivisionError
                return a / b
        raise ValueError("unreachable")

    try:
        return walk(tree)
    except (ZeroDivisionError, ValueError, RecursionError):
        return None


def digits_in(expr: str) -> list[int]:
    try:
        tree = ast.parse(expr.strip(), mode="eval")
    except SyntaxError:
        return []
    return [n.value for n in ast.walk(tree)
            if isinstance(n, ast.Constant) and isinstance(n.value, int)]


def grade(expr: str, puzzle: tuple[int, ...]) -> tuple[bool, str]:
    """Ground truth. Correct iff each number used once AND value == 24."""
    if not expr:
        return False, "no_expression"
    if sorted(digits_in(expr)) != sorted(puzzle):
        return False, f"wrong_numbers(used={sorted(digits_in(expr))},need={sorted(puzzle)})"
    value = eval_exact(expr)
    if value is None:
        return False, "unevaluable"
    if value != TARGET:
        return False, f"equals_{value}_not_24"
    return True, "correct"


# --------------------------------------------------------------------------- #
# Controlled error injection (Tsui's method)                                   #
# --------------------------------------------------------------------------- #

def mutations(expr: str, puzzle: tuple[int, ...]) -> list[tuple[str, Fraction]]:
    """Every single-operator corruption that is genuinely wrong and still uses
    each number exactly once. Sorted by |value - 24|, closest first."""
    try:
        tree = ast.parse(expr.strip(), mode="eval")
    except SyntaxError:
        return []
    out: list[tuple[str, Fraction]] = []
    for node in [n for n in ast.walk(tree) if isinstance(n, ast.BinOp)]:
        original = type(node.op)
        for OpCls in _BIN_OPS:
            if OpCls is original:
                continue
            node.op = OpCls()
            try:
                cand = ast.unparse(tree)
            except Exception:
                node.op = original()
                continue
            val = eval_exact(cand)
            node.op = original()          # restore before the next candidate
            if val is None or val == TARGET:
                continue
            if sorted(digits_in(cand)) != sorted(puzzle):
                continue
            out.append((cand, val))
    seen: set[str] = set()
    uniq = [(c, v) for c, v in out if not (c in seen or seen.add(c))]
    return sorted(uniq, key=lambda cv: abs(cv[1] - TARGET))


def pick_mutation(expr: str, puzzle: tuple[int, ...],
                  level: str) -> tuple[str, Fraction] | None:
    """subtle = closest to 24, obvious = furthest, moderate = median."""
    ms = mutations(expr, puzzle)
    if not ms:
        return None
    return {"subtle": ms[0], "obvious": ms[-1]}.get(level, ms[len(ms) // 2])


# --------------------------------------------------------------------------- #
# Prompts                                                                      #
# --------------------------------------------------------------------------- #

SOLVE = (
    "Make 24 from these four numbers: {nums}.\n"
    "Use each number exactly once. You may use + - * / and parentheses.\n"
    "Do not restate the puzzle. Give the expression only.\n"
    "End your reply with exactly this line and nothing after it:\n"
    "ANSWER: <expression>"
)

VERIFY_SELF = (
    "Check the arithmetic in your answer above, step by step.\n"
    "Does that expression use each of {nums} exactly once, and does it "
    "evaluate to exactly 24?\n"
    "End your reply with exactly this line and nothing after it:\n"
    "VERDICT: CORRECT   or   VERDICT: INCORRECT"
)

VERIFY_WAIT = "Wait.\n\n" + VERIFY_SELF

VERIFY_EXTERNAL = (
    "Someone submitted this as a solution to the puzzle "
    "\"make 24 from {nums}, using each number exactly once\":\n\n"
    "    {expr}\n\n"
    "Check their arithmetic, step by step. Does that expression use each of "
    "{nums} exactly once, and does it evaluate to exactly 24?\n"
    "End your reply with exactly this line and nothing after it:\n"
    "VERDICT: CORRECT   or   VERDICT: INCORRECT"
)

_ANSWER_RE = re.compile(r"ANSWER:\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
_VERDICT_RE = re.compile(r"VERDICT:\s*(CORRECT|INCORRECT)", re.IGNORECASE)


def parse_answer(text: str) -> str:
    m = _ANSWER_RE.findall(text or "")
    return m[-1].strip().rstrip(".") if m else ""


def parse_verdict(text: str) -> str | None:
    """'correct' | 'incorrect' | None. None is recorded, never coerced —
    silently dropping unparseable verdicts would bias the rate."""
    m = _VERDICT_RE.findall(text or "")
    return m[-1].lower() if m else None


# --------------------------------------------------------------------------- #
# Records                                                                      #
# --------------------------------------------------------------------------- #

@dataclass
class Trial:
    model_key: str
    model_id: str
    puzzle: list[int]
    model_answer: str = ""          # what the model actually produced
    model_answer_correct: bool = False
    tested_expr: str = ""           # what the three arms verified
    tested_value: str = ""
    error_source: str = ""          # "natural" | "injected" | "none"
    injection_level: str = ""
    verdict_self: str | None = None
    verdict_external: str | None = None
    verdict_wait: str | None = None
    error: str = ""
    transcript: dict[str, Any] = field(default_factory=dict)


# --------------------------------------------------------------------------- #
# Model access                                                                 #
# --------------------------------------------------------------------------- #

class Caller:
    def __init__(self, dry_run: bool, max_retries: int = 5) -> None:
        self.dry_run = dry_run
        self.calls = 0
        self.client = None
        if dry_run:
            return
        try:
            import anthropic
        except ImportError:
            sys.exit("[fatal] pip install anthropic  (or run with --dry-run)")
        self._anthropic = anthropic
        self.client = anthropic.Anthropic(max_retries=max_retries)
        # Fail fast on missing credentials, before any trial runs. The SDK
        # resolves them lazily and raises a bare TypeError on the FIRST request,
        # which would surface as a traceback partway into the run.
        if not self.client.auth_headers:
            sys.exit(
                "[fatal] no credentials found.\n"
                "        export ANTHROPIC_API_KEY=sk-ant-...   (get one at "
                "console.anthropic.com)\n"
                "        or run `ant auth login`\n"
                "        or use --dry-run to exercise the harness without an API."
            )

    def __call__(self, cfg: dict[str, Any], messages: list[dict[str, str]]) -> str:
        self.calls += 1
        if self.dry_run:
            return _fake_reply(messages)

        kwargs: dict[str, Any] = {
            "model": cfg["model"],
            "max_tokens": cfg["max_tokens"],
            "messages": messages,
        }
        if cfg["thinking"] is not None:
            kwargs["thinking"] = cfg["thinking"]
        # No temperature / top_p / top_k: rejected with 400 on Sonnet 5.

        A = self._anthropic
        try:
            resp = self.client.messages.create(**kwargs)
        except A.NotFoundError as e:
            sys.exit(f"[fatal] unknown model {cfg['model']!r}: {e}")
        except A.AuthenticationError as e:
            sys.exit(f"[fatal] credentials rejected: {e}")
        except A.RateLimitError as e:
            raise RuntimeError(f"rate_limited_after_retries: {e}") from e
        except A.APIStatusError as e:
            raise RuntimeError(f"api_status_{e.status_code}: {e}") from e
        except A.APIConnectionError as e:
            raise RuntimeError(f"connection_error: {e}") from e

        if resp.stop_reason == "refusal":
            raise RuntimeError("refusal")
        if resp.stop_reason == "max_tokens":
            raise RuntimeError("truncated_max_tokens")
        return "".join(b.text for b in resp.content if b.type == "text")


def _fake_reply(messages: list[dict[str, str]]) -> str:
    """Deterministic stand-in for --dry-run. Reproduces the SHAPE of the
    phenomenon so the pipeline can be exercised; it is NOT evidence."""
    last = messages[-1]["content"]
    if last.startswith("Make 24"):
        # Parse AFTER "numbers:" — otherwise the 24 in "Make 24" is picked up
        # as a puzzle number and every generated answer is nonsense.
        m = re.search(r"numbers:\s*([\d,\s]+)", last)
        vals = [int(x) for x in re.findall(r"\d+", m.group(1))] if m else [1, 2, 3, 4]
        if sorted(vals) in ([1, 2, 3, 4], [1, 1, 4, 6], [1, 1, 3, 8]):
            return f"ANSWER: {vals[0]}*{vals[1]}*{vals[2]}*{vals[3]}"
        return f"ANSWER: ({vals[0]}+{vals[1]})*{vals[2]}-{vals[3]}"
    if last.lstrip().startswith("Someone submitted"):
        m = re.search(r"\n\n    (.+?)\n\n", last)
        val = eval_exact(m.group(1)) if m else None
        return f"VERDICT: {'CORRECT' if val == TARGET else 'INCORRECT'}"
    if last.startswith("Wait."):
        return "VERDICT: INCORRECT"
    return "VERDICT: CORRECT"          # the blind spot, in the stub


# --------------------------------------------------------------------------- #
# One trial                                                                    #
# --------------------------------------------------------------------------- #

def run_trial(call: Caller, key: str, cfg: dict[str, Any],
              puzzle: tuple[int, ...], level: str, inject: bool) -> Trial:
    t = Trial(model_key=key, model_id=cfg["model"], puzzle=list(puzzle))
    nums = ", ".join(str(n) for n in puzzle)

    try:
        # ---- solve ------------------------------------------------------- #
        solve_msgs = [{"role": "user", "content": SOLVE.format(nums=nums)}]
        solve_out = call(cfg, solve_msgs)
        t.model_answer = parse_answer(solve_out)
        t.transcript["solve"] = {"prompt": solve_msgs[-1]["content"], "reply": solve_out}

        if not t.model_answer:
            t.error = "no_answer_parsed"
            return t

        # ---- arm D: ground truth on the model's own answer ---------------- #
        t.model_answer_correct, _ = grade(t.model_answer, puzzle)

        # ---- choose the expression the three arms will verify -------------- #
        if not t.model_answer_correct:
            # Natural error. Most ecologically valid: keep the model's real
            # reply in arm A, working text and all.
            t.tested_expr = t.model_answer
            t.error_source = "natural"
            assistant_turn = solve_out
        elif inject:
            picked = pick_mutation(t.model_answer, puzzle, level)
            if picked is None:
                t.error = "no_valid_mutation"
                return t
            t.tested_expr, _ = picked
            t.error_source = "injected"
            t.injection_level = level
            # MINIMAL assistant turn: arms A and B then present identical
            # information and differ ONLY in provenance, which is the variable
            # under test. Keeping the real working text would let a contradiction
            # between working and answer do the catching instead of provenance.
            assistant_turn = f"ANSWER: {t.tested_expr}"
        else:
            t.error_source = "none"      # correct answer, injection disabled
            return t

        t.tested_value = str(eval_exact(t.tested_expr))

        # ---- arm A: self-verify ------------------------------------------- #
        a_msgs = solve_msgs + [
            {"role": "assistant", "content": assistant_turn},
            {"role": "user", "content": VERIFY_SELF.format(nums=nums)},
        ]
        a_out = call(cfg, a_msgs)
        t.verdict_self = parse_verdict(a_out)
        t.transcript["self"] = {"assistant_turn": assistant_turn,
                                "prompt": a_msgs[-1]["content"], "reply": a_out}

        # ---- arm B: identical expression, external provenance -------------- #
        b_msgs = [{"role": "user",
                   "content": VERIFY_EXTERNAL.format(nums=nums, expr=t.tested_expr)}]
        b_out = call(cfg, b_msgs)
        t.verdict_external = parse_verdict(b_out)
        t.transcript["external"] = {"prompt": b_msgs[-1]["content"], "reply": b_out}

        # ---- arm C: self + "Wait" ----------------------------------------- #
        c_msgs = solve_msgs + [
            {"role": "assistant", "content": assistant_turn},
            {"role": "user", "content": VERIFY_WAIT.format(nums=nums)},
        ]
        c_out = call(cfg, c_msgs)
        t.verdict_wait = parse_verdict(c_out)
        t.transcript["wait"] = {"prompt": c_msgs[-1]["content"], "reply": c_out}

    except RuntimeError as e:
        t.error = str(e)
    return t


# --------------------------------------------------------------------------- #
# Summary — natural and injected are NEVER pooled into one headline rate       #
# --------------------------------------------------------------------------- #

def _rates(rows: list[Trial]) -> dict[str, Any]:
    rec: dict[str, Any] = {"n": len(rows)}
    for arm, attr in (("self", "verdict_self"),
                      ("external", "verdict_external"),
                      ("wait", "verdict_wait")):
        judged = [getattr(t, attr) for t in rows]
        usable = [v for v in judged if v is not None]
        missed = sum(1 for v in usable if v == "correct")
        rec[arm] = {
            "denominator": len(usable),
            "unparseable": len(judged) - len(usable),
            "missed_the_error": missed,
            "blind_spot_rate": round(missed / len(usable), 3) if usable else None,
        }
    a, b = rec["self"]["blind_spot_rate"], rec["external"]["blind_spot_rate"]
    rec["gap_self_minus_external"] = (
        round(a - b, 3) if a is not None and b is not None else None
    )
    return rec


def summarize(trials: list[Trial]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key in sorted({t.model_key for t in trials}):
        usable = [t for t in trials if t.model_key == key and not t.error
                  and t.error_source in ("natural", "injected")]
        out[key] = {
            "trials_attempted": sum(1 for t in trials if t.model_key == key),
            "errors": sum(1 for t in trials if t.model_key == key and t.error),
            "model_answer_correct": sum(
                1 for t in trials if t.model_key == key and not t.error
                and t.model_answer_correct),
            "natural": _rates([t for t in usable if t.error_source == "natural"]),
            "injected": _rates([t for t in usable if t.error_source == "injected"]),
        }
    return out


def print_summary(summary: dict[str, Any], dry_run: bool) -> None:
    print()
    if dry_run:
        print("!! DRY RUN — canned responses. These numbers are NOT evidence. !!\n")
    for key, r in summary.items():
        print(f"{key}   ({r['trials_attempted']} attempted, {r['errors']} errored, "
              f"{r['model_answer_correct']} solved correctly)")
        print(f"   {'source':<10}{'n':>4}{'self':>9}{'exter':>9}{'wait':>9}{'gap':>9}")
        for src in ("natural", "injected"):
            d = r[src]
            if not d["n"]:
                print(f"   {src:<10}{0:>4}{'  — no trials of this kind —':>36}")
                continue
            f = lambda v: "    n/a" if v is None else f"{v:6.1%}"
            print(f"   {src:<10}{d['n']:>4}"
                  f"{f(d['self']['blind_spot_rate']):>9}"
                  f"{f(d['external']['blind_spot_rate']):>9}"
                  f"{f(d['wait']['blind_spot_rate']):>9}"
                  f"{f(d['gap_self_minus_external']):>9}")
        print()
    print("self   = confirmed a wrong expression presented as its own")
    print("exter  = confirmed the SAME expression shown as someone else's")
    print("wait   = self-verification with \"Wait.\" prepended")
    print("gap    = self - external. Positive = the blind spot. Near zero = no")
    print("         blind spot here; the failure is not about self-reference.")
    print()
    print("natural  = the model's own mistake (arm A keeps its real working text,")
    print("           so A and B differ in more than provenance — a caveat)")
    print("injected = one operator corrupted (arm A is a minimal answer-only turn,")
    print("           so A and B differ ONLY in provenance — the clean comparison)")


# --------------------------------------------------------------------------- #
# Main                                                                         #
# --------------------------------------------------------------------------- #

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--models", nargs="*", default=list(MODELS), choices=list(MODELS))
    p.add_argument("--trials", type=int, default=len(PUZZLES))
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--no-injection", action="store_true",
                   help="revision-1 behaviour: only natural errors")
    p.add_argument("--max-retries", type=int, default=5)
    p.add_argument("--out", default="")
    a = p.parse_args()

    puzzles = PUZZLES[:max(1, min(a.trials, len(PUZZLES)))]
    inject = not a.no_injection
    call = Caller(dry_run=a.dry_run, max_retries=a.max_retries)

    print(f"configs   : {', '.join(a.models)}")
    print(f"puzzles   : {len(puzzles)}  -> up to {4*len(puzzles)*len(a.models)} calls")
    print(f"injection : {'ON (every trial gets a denominator)' if inject else 'OFF'}")
    print(f"mode      : {'DRY RUN (no API)' if a.dry_run else 'LIVE'}\n")

    trials: list[Trial] = []
    for key in a.models:
        cfg = MODELS[key]
        print(f"[{key}] {cfg['model']} — {cfg['note']}")
        for i, puzzle in enumerate(puzzles):
            level = LEVELS[i % len(LEVELS)]      # rotate so all three get used
            t = run_trial(call, key, cfg, puzzle, level, inject)
            trials.append(t)
            src = {"natural": "nat", "injected": "inj", "none": "---", "": "---"}[t.error_source]
            verdicts = "".join(
                {"correct": "C", "incorrect": "I", None: "?"}[v]
                for v in (t.verdict_self, t.verdict_external, t.verdict_wait)
            )
            print(f"   {i+1:>2}/{len(puzzles)} {str(puzzle):<15} "
                  f"{'ok ' if t.model_answer_correct else 'ERR'} {src} "
                  f"{t.tested_expr[:24]:<26}{verdicts}"
                  + (f"  [{t.error}]" if t.error else ""))
        print()

    summary = summarize(trials)
    print_summary(summary, a.dry_run)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = a.out or f"results-{'dryrun-' if a.dry_run else ''}{stamp}.json"
    with open(path, "w") as fh:
        json.dump({
            "meta": {
                "generated_at_utc": stamp,
                "revision": 2,
                "dry_run": a.dry_run,
                "injection_enabled": inject,
                "api_calls": call.calls,
                "configs": {k: MODELS[k] for k in a.models},
                "puzzles": [list(x) for x in puzzles],
                "sampling_params": "none — non-default temperature/top_p/top_k "
                                   "are rejected with 400 on Sonnet 5",
                "arithmetic": "fractions.Fraction (exact)",
                "injection_method": "one binary operator replaced; corruption "
                                    "must still use each number exactly once and "
                                    "must not equal 24. subtle=closest to 24, "
                                    "obvious=furthest, moderate=median.",
                "pooling": "natural and injected are reported separately and "
                           "never pooled into one headline rate",
                "references": [
                    "Tsui, Self-Correction Bench, arXiv:2507.02778 (2025) [PREPRINT]",
                    "Huang et al., ICLR 2024, arXiv:2310.01798 [peer-reviewed]",
                ],
            },
            "summary": summary,
            "trials": [asdict(t) for t in trials],
        }, fh, indent=1, ensure_ascii=False)
    print(f"\nwrote {path}  ({len(trials)} trials, full transcripts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
