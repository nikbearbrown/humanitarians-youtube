#!/usr/bin/env python3
"""Does a model's adjacent-profession-test verdict track specificity, or length?

The source draft (claude-for-artificial-intelligence/claude-liam-bs-01-pick-and-scope,
beat B07) tells students to paste a role statement into Claude and have it run the
adjacent-profession test. Nobody measured whether a model can run that test. This
measures it.

    claimed cause    the verdict tracks exclusion of adjacent roles
    rival            the verdict tracks word count / density of domain jargon
    isolating arm    `swapped` — matched to `full` on words AND domain terms,
                     but not identifying (see items.py)
    Q3 falsifier     `stripped` — if removing the load-bearing phrase does not
                     flip the verdict, the phrase was not load-bearing
    Q4 guarantee     `full` (expect PASS) and `generic` (expect FAIL) are anchors,
                     so the run cannot silently collect no signal

Ground truth is fixed by construction; the model's opinion is never needed to score.

Usage
    python neighbour_bench.py --dry-run              # no key, no spend, NOT evidence
    python neighbour_bench.py --pilot                # 1 repeat, both models (~$0.07)
    python neighbour_bench.py --repeats 3            # powered run
    python neighbour_bench.py --models claude-haiku-4-5
    python neighbour_bench.py --score results-....json

Credentials: reads ANTHROPIC_API_KEY from the environment, or from a `.env` file
next to this script (KEY=value lines). The key is never printed or logged.
"""

import argparse
import collections
import hashlib
import json
import os
import pathlib
import sys
import time
from datetime import datetime, timezone

import items

HERE = pathlib.Path(__file__).resolve().parent

# Per the claude-api skill's pricing table, 2026-08. Sonnet 5 is on introductory
# pricing ($2/$10) through 2026-08-31; list is $3/$15 after that.
PRICING = {                        # USD per 1M tokens: (input, output)
    "claude-haiku-4-5": (1.00, 5.00),
    "claude-sonnet-5": (2.00, 10.00),
    "claude-opus-5": (5.00, 25.00),
}
DEFAULT_MODELS = ["claude-haiku-4-5", "claude-sonnet-5"]

VERDICT_SCHEMA = {
    "type": "object",
    "properties": {
        "nearest_neighbour": {
            "type": "string",
            "description": "The single profession whose work is most similar to the "
                           "statement's author.",
        },
        "load_bearing_phrase": {
            "type": "string",
            "description": "The exact phrase from the statement that the nearest "
                           "neighbour could not write. Empty string if there is none.",
        },
        "verdict": {
            "type": "string",
            "enum": ["PASS", "FAIL"],
            "description": "PASS if the nearest neighbour could NOT claim the "
                           "statement; FAIL if they could.",
        },
        "reason": {"type": "string", "description": "One sentence."},
    },
    "required": ["nearest_neighbour", "load_bearing_phrase", "verdict", "reason"],
    "additionalProperties": False,
}

# Both prompts are deliberately neutral: they state the test and ask for a verdict
# without hinting that length, jargon, or brevity is relevant either way.

# Arm F — the model picks the neighbour. This is what the source draft's CTA does.
SYSTEM_FREE = (
    "You run the adjacent-profession test on a professional role statement.\n\n"
    "The test: name the single profession whose work is most similar to the "
    "statement's author — their nearest neighbour, not a distant one. Then decide "
    "whether that neighbour could truthfully claim the statement as a description "
    "of their own job.\n\n"
    "If the neighbour could claim it, the statement FAILS. If the statement "
    "excludes the neighbour, it PASSES. Also name the exact phrase doing the "
    "excluding, or an empty string if no phrase does."
)

# Arm P — the neighbour is supplied, so it stops being a free variable. Ground truth
# is only well-defined in this arm.
SYSTEM_PINNED = (
    "You run the adjacent-profession test on a professional role statement, against "
    "a specific neighbouring profession that will be named for you.\n\n"
    "The test: decide whether the named neighbour could truthfully claim the "
    "statement as a description of their own job. Do not substitute a different "
    "neighbour — evaluate against the one you are given.\n\n"
    "If that neighbour could claim it, the statement FAILS. If the statement "
    "excludes them, it PASSES. Also name the exact phrase doing the excluding, or "
    "an empty string if no phrase does. Echo the neighbour you evaluated against."
)


def build_prompt(trial, arm):
    if arm == "pinned":
        return (
            f"Role statement:\n\n{trial['statement']}\n\n"
            f"Nearest neighbouring profession: {trial['nearest_neighbour']}\n\n"
            "Run the adjacent-profession test against that neighbour."
        )
    return (
        f"Role statement:\n\n{trial['statement']}\n\n"
        "Run the adjacent-profession test on it."
    )


def load_env():
    """Populate os.environ from a sibling .env, without printing anything."""
    path = HERE / ".env"
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip("'\""))


def request_kwargs(model, arm="free"):
    """Per-model request config.

    Sonnet 5 runs adaptive thinking when `thinking` is omitted, which would balloon
    output tokens on what is a short classification call — disable it explicitly.
    Haiku 4.5 predates that default and rejects `effort`, so it gets neither field.
    """
    kwargs = {
        "model": model,
        "max_tokens": 400,
        "system": SYSTEM_PINNED if arm == "pinned" else SYSTEM_FREE,
        "output_config": {"format": {"type": "json_schema", "schema": VERDICT_SCHEMA}},
    }
    if model in ("claude-sonnet-5", "claude-opus-5"):
        kwargs["thinking"] = {"type": "disabled"}
    return kwargs


def dry_run_verdict(model, trial, rep, arm="free"):
    """Deterministic stand-in. Proves the harness runs end to end.

    NOT EVIDENCE — canned responses cannot support a finding about model behaviour.
    The verdict is a hash, deliberately uncorrelated with ground truth so a dry run
    can never be mistaken for a result.
    """
    seed = f"{model}|{arm}|{trial['base_id']}|{trial['variant']}|{rep}"
    h = hashlib.sha256(seed.encode()).hexdigest()
    return {
        "nearest_neighbour": "DRY-RUN placeholder neighbour",
        "load_bearing_phrase": "" if int(h[1], 16) % 2 else "DRY-RUN phrase",
        "verdict": "PASS" if int(h[0], 16) % 2 else "FAIL",
        "reason": "DRY RUN — NOT EVIDENCE.",
    }, {"input_tokens": 0, "output_tokens": 0}


def run(models, repeats, dry_run):
    if not dry_run:
        load_env()
        if not os.environ.get("ANTHROPIC_API_KEY"):
            sys.exit(
                "No ANTHROPIC_API_KEY found.\n"
                "  export ANTHROPIC_API_KEY=... in your shell, or write a .env file\n"
                f"  next to this script:  {HERE / '.env'}\n"
                "Re-run with --dry-run to exercise the harness without a key."
            )
        import anthropic
        client = anthropic.Anthropic()

    all_trials = list(items.trials())
    total = len(all_trials) * len(items.ARMS) * repeats * len(models)
    print(f"{'DRY RUN (NOT EVIDENCE)' if dry_run else 'LIVE RUN'} — "
          f"{len(all_trials)} items x {len(items.ARMS)} arms x {repeats} repeat(s) x "
          f"{len(models)} model(s) = {total} calls\n")

    records, done, errors = [], 0, 0
    for model in models:
        for arm in items.ARMS:
            for rep in range(1, repeats + 1):
                for trial in all_trials:
                    done += 1
                    prompt = build_prompt(trial, arm)
                    try:
                        if dry_run:
                            parsed, usage = dry_run_verdict(model, trial, rep, arm)
                        else:
                            kwargs = request_kwargs(model, arm)
                            resp = client.messages.create(
                                messages=[{"role": "user", "content": prompt}], **kwargs
                            )
                            text = next(b.text for b in resp.content if b.type == "text")
                            parsed = json.loads(text)
                            usage = {
                                "input_tokens": resp.usage.input_tokens,
                                "output_tokens": resp.usage.output_tokens,
                            }
                    except Exception as exc:                  # noqa: BLE001
                        errors += 1
                        print(f"  [{done}/{total}] ERROR {model} {arm} "
                              f"{trial['base_id']}/{trial['variant']}: "
                              f"{type(exc).__name__}: {exc}")
                        continue

                    nb = parsed["nearest_neighbour"]
                    # Degenerate free-arm choice: the "neighbour" is the same title as
                    # the subject, so the item fails without testing the statement.
                    degenerate = (arm == "free"
                                  and trial["role_noun"].lower() in nb.lower())
                    records.append({
                        **{k: trial[k] for k in (
                            "base_id", "domain", "variant", "statement", "expected",
                            "nearest_neighbour", "load_bearing", "role_noun",
                            "n_words", "n_domain_terms")},
                        "model": model,
                        "arm": arm,
                        "repeat": rep,
                        "verdict": parsed["verdict"],
                        "model_neighbour": nb,
                        "model_load_bearing": parsed["load_bearing_phrase"],
                        "reason": parsed["reason"],
                        "degenerate_neighbour": degenerate,
                        "correct": parsed["verdict"] == trial["expected"],
                        **usage,
                    })
                    mark = "ok " if parsed["verdict"] == trial["expected"] else "MISS"
                    flag = " [same-title nb]" if degenerate else ""
                    print(f"  [{done}/{total}] {mark} {model:<18} {arm:<7} "
                          f"{trial['base_id']}/{trial['variant']:<9} -> "
                          f"{parsed['verdict']:<5} (exp {trial['expected']}){flag}")
                    if not dry_run:
                        time.sleep(0.15)      # gentle on rate limits

    payload = {
        "meta": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "dry_run": dry_run,
            "evidence": (
                "NOT EVIDENCE — dry-run canned responses cannot support a finding."
                if dry_run else "live model output"
            ),
            "models": models,
            "arms": list(items.ARMS),
            "repeats": repeats,
            "n_items": len(all_trials),
            "calls_attempted": total,
            "calls_recorded": len(records),
            "errors": errors,
            "match_audit": items.match_report(),
        },
        "records": records,
    }
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    name = f"results-{'dryrun-' if dry_run else ''}{stamp}.json"
    (HERE / name).write_text(json.dumps(payload, indent=2))
    print(f"\nwrote {name}")
    score(payload)
    return payload


def _norm_nb(s):
    """Normalise a neighbour string for counting distinct answers."""
    return " ".join("".join(c if c.isalnum() or c.isspace() else " "
                            for c in s.lower()).split())


def reliability(payload):
    """Primary measure as of revision 3.

    Revision 2 established that ground-truth correctness cannot be scored here: three
    of six `full` statements did not in fact exclude their designated neighbour, and the
    models were right to fail them (see ../EXPERIMENT.md). The author's judgment is the
    broken component, so correctness is not measurable with these items.

    Reliability needs no adjudication of who is correct. If the same statement gets
    different verdicts depending on which model you ask, which neighbour got picked, or
    which run it was, then the draft's CTA is unreliable advice regardless.
    """
    records, meta = payload["records"], payload["meta"]
    arms = meta.get("arms", ["free"])
    reps = meta["repeats"]

    print("\n" + "=" * 78)
    print("RELIABILITY — the primary measure (needs no ground truth)")
    if meta["dry_run"]:
        print("DRY RUN — NOT EVIDENCE.")
    print("=" * 78)

    # cell -> list of verdicts across repeats
    cells = collections.defaultdict(list)
    nbs = collections.defaultdict(list)
    for r in records:
        k = (r["model"], r.get("arm", "free"), r["base_id"], r["variant"])
        cells[k].append(r["verdict"])
        nbs[k].append(_norm_nb(r["model_neighbour"]))

    def modal(vs):
        return collections.Counter(vs).most_common(1)[0][0]

    # 1. Within-model verdict stability across repeats.
    if reps > 1:
        print(f"\n1. WITHIN-MODEL STABILITY — same item, same arm, {reps} repeats")
        print(f"   {'model':<20}{'arm':<9}{'items':>7}{'flipped':>9}{'rate':>8}")
        for model in meta["models"]:
            for arm in arms:
                ks = [k for k in cells if k[0] == model and k[1] == arm]
                if not ks:
                    continue
                flips = sum(1 for k in ks if len(set(cells[k])) > 1)
                print(f"   {model:<20}{arm:<9}{len(ks):>7}{flips:>9}"
                      f"{flips / len(ks):>7.0%}")
        print("   A flip means the same statement got both PASS and FAIL from the same")
        print("   model on the same question, with nothing changed but the run.")

    # 2. Cross-model agreement on modal verdicts.
    print("\n2. CROSS-MODEL AGREEMENT — modal verdict, identical items")
    if len(meta["models"]) >= 2:
        a, b = meta["models"][0], meta["models"][1]
        for arm in arms:
            shared = [(k[2], k[3]) for k in cells if k[0] == a and k[1] == arm
                      and (b, arm, k[2], k[3]) in cells]
            if not shared:
                continue
            dis = [s for s in shared
                   if modal(cells[(a, arm, *s)]) != modal(cells[(b, arm, *s)])]
            print(f"   {arm:<9} {len(dis)}/{len(shared)} items disagree "
                  f"= {len(dis) / len(shared):.0%}")
        print(f"   ({a} vs {b})")

    # 3. Arm effect — does pinning the neighbour change the answer?
    if "pinned" in arms and "free" in arms:
        print("\n3. ARM EFFECT — does fixing the neighbour change the verdict?")
        for model in meta["models"]:
            shared = [(k[2], k[3]) for k in cells if k[0] == model and k[1] == "free"
                      and (model, "pinned", k[2], k[3]) in cells]
            if not shared:
                continue
            chg = [s for s in shared
                   if modal(cells[(model, "free", *s)])
                   != modal(cells[(model, "pinned", *s)])]
            print(f"   {model:<20} {len(chg)}/{len(shared)} items changed "
                  f"= {len(chg) / len(shared):.0%}")

    # 4. Free-arm neighbour instability — the variance the draft's CTA inherits.
    if "free" in arms:
        print("\n4. NEIGHBOUR INSTABILITY (free arm) — distinct neighbours named for the")
        print("   same statement across repeats, and degenerate same-title choices")
        for model in meta["models"]:
            ks = [k for k in nbs if k[0] == model and k[1] == "free"]
            if not ks:
                continue
            distinct = [len(set(nbs[k])) for k in ks]
            unstable = sum(1 for d in distinct if d > 1)
            mean_d = sum(distinct) / len(distinct)
            sel = [r for r in records
                   if r["model"] == model and r.get("arm") == "free"]
            deg = sum(1 for r in sel if r.get("degenerate_neighbour"))
            print(f"   {model:<20} mean distinct neighbours/item: {mean_d:.2f}"
                  f"   items with >1: {unstable}/{len(ks)} ({unstable / len(ks):.0%})")
            print(f"   {'':<20} same-title (degenerate) choices: {deg}/{len(sel)} "
                  f"({deg / len(sel):.0%})")

    print("\n" + "-" * 78)
    print("READING THIS: every number above is a disagreement rate. None depends on the")
    print("author being right about which statements pass — which revision 2 showed he")
    print("was not. High numbers mean the draft's CTA hands students an unstable test.")
    print("-" * 78)


def _rate(records, model, variant, arm=None):
    sel = [r for r in records
           if r["model"] == model and r["variant"] == variant
           and (arm is None or r.get("arm", "free") == arm)]
    if not sel:
        return None, 0
    passes = sum(1 for r in sel if r["verdict"] == "PASS")
    return passes / len(sel), len(sel)


def score(payload):
    records = payload["records"]
    meta = payload["meta"]
    if not records:
        print("\nNo records to score.")
        return
    arms = meta.get("arms", ["free"])

    reliability(payload)

    print("\n" + "=" * 78)
    print("SECONDARY — correctness against author ground truth.")
    print("NOT RELIABLE: revision 2 showed 3 of 6 `full` statements do not exclude their")
    print("designated neighbour, and the models were right to fail them. Shown for the")
    print("`generic` anchor only, which has held across all revisions. Not for screen.")
    print("=" * 78)
    if meta["dry_run"]:
        print("DRY RUN — NOT EVIDENCE. Numbers below are hashes, not measurements.")

    for arm in arms:
        label = ("ARM P — neighbour PINNED (ground truth well-defined here)"
                 if arm == "pinned" else
                 "ARM F — neighbour FREE (what the draft's CTA does)")
        print(f"\n{label}")
        print("PASS rate by variant (truth: full=PASS, swapped/stripped/generic=FAIL)\n")
        header = f"{'model':<20}" + "".join(f"{v:>11}" for v in items.VARIANTS)
        print(header)
        print("-" * len(header))
        for model in meta["models"]:
            row = f"{model:<20}"
            for variant in items.VARIANTS:
                rate, _ = _rate(records, model, variant, arm)
                row += "          -" if rate is None else f"{rate:>10.0%} "
            print(row)

        for model in meta["models"]:
            full, _ = _rate(records, model, "full", arm)
            gen, _ = _rate(records, model, "generic", arm)
            swap, n_swap = _rate(records, model, "swapped", arm)
            strip, n_strip = _rate(records, model, "stripped", arm)
            if full is None or gen is None:
                continue
            sep = full - gen
            print(f"\n  {model}")
            print(f"    anchor separation (full − generic)   : {sep:+.0%}"
                  f"   {'OK' if sep > 0.5 else 'weak'}")
            print(f"    length/jargon confound (swapped PASS): {swap:.0%} of {n_swap}"
                  f"   {'← verdict reading length' if swap > 0.5 else ''}")
            print(f"    load-bearing held (stripped PASS)    : {strip:.0%} of {n_strip}"
                  f"   {'← phrase NOT load-bearing' if strip > 0.5 else ''}")

    # Free-arm neighbour behaviour — the revision-1 finding, now measured on purpose.
    if "free" in arms:
        print("\n" + "-" * 78)
        print("FREE-ARM NEIGHBOUR CHOICE (why revision 1 failed)")
        for model in meta["models"]:
            sel = [r for r in records
                   if r["model"] == model and r.get("arm") == "free"]
            if not sel:
                continue
            deg = sum(1 for r in sel if r.get("degenerate_neighbour"))
            print(f"\n  {model}")
            print(f"    same-title 'neighbour' picked: {deg}/{len(sel)} "
                  f"({deg / len(sel):.0%}) — not an adjacent profession, so the item")
            print(f"      fails without testing the statement")
            # Verdict divergence between arms on identical items.
            flips = 0
            paired = 0
            for r in sel:
                match = [q for q in records
                         if q["model"] == model and q.get("arm") == "pinned"
                         and q["base_id"] == r["base_id"]
                         and q["variant"] == r["variant"]
                         and q["repeat"] == r["repeat"]]
                if match:
                    paired += 1
                    if match[0]["verdict"] != r["verdict"]:
                        flips += 1
            if paired:
                print(f"    verdict changed when the neighbour was pinned: "
                      f"{flips}/{paired} ({flips / paired:.0%})")

    # Stability, only meaningful with repeats.
    if meta["repeats"] > 1:
        print("\nVerdict stability across repeats")
        for model in meta["models"]:
            for arm in arms:
                groups = collections.defaultdict(set)
                for r in records:
                    if r["model"] == model and r.get("arm", "free") == arm:
                        groups[(r["base_id"], r["variant"])].add(r["verdict"])
                if not groups:
                    continue
                flips = sum(1 for v in groups.values() if len(v) > 1)
                print(f"  {model:<20} {arm:<7} {flips}/{len(groups)} items flipped "
                      f"across {meta['repeats']} repeats")

    # Cost.
    print("\nCost")
    grand = 0.0
    for model in meta["models"]:
        sel = [r for r in records if r["model"] == model]
        if not sel:
            continue
        tin = sum(r["input_tokens"] for r in sel)
        tout = sum(r["output_tokens"] for r in sel)
        pin, pout = PRICING.get(model, (0, 0))
        cost = tin / 1e6 * pin + tout / 1e6 * pout
        grand += cost
        print(f"  {model:<20} {len(sel):>4} calls  {tin:>7,} in  {tout:>7,} out  "
              f"${cost:.4f}")
    print(f"  {'TOTAL':<20} {len(records):>4} calls"
          f"{'':>32}${grand:.4f}")
    if meta["errors"]:
        print(f"\n  {meta['errors']} call(s) errored and are absent from the above.")

    # Revision 3 replaces the correctness gate. The question is no longer "do the
    # anchors separate" (unanswerable — see the SECONDARY banner) but "did we collect
    # enough repeats to estimate a disagreement rate at all".
    gate_arm = "pinned" if "pinned" in arms else "free"
    print("\n" + "-" * 78)
    print("DATA-SUFFICIENCY CHECK")
    gen, n_gen = _rate(records, meta["models"][0], "generic", gate_arm)
    if meta["repeats"] < 3:
        print(f"  THIN   {meta['repeats']} repeat(s) — within-model stability needs >=3 "
              "to mean anything.")
    else:
        print(f"  OK     {meta['repeats']} repeats per cell; stability is estimable.")
    if gen is not None and gen > 0.2:
        print(f"  WATCH  `generic` PASSes {gen:.0%} of the time in the {gate_arm} arm — "
              "the one\n         anchor that should never pass. Inspect those trials.")
    else:
        print(f"  OK     `generic` anchor holds ({gen:.0%} PASS, {gate_arm} arm).")
    print("-" * 78)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="canned deterministic responses; no key, no spend, NOT evidence")
    ap.add_argument("--pilot", action="store_true", help="1 repeat, both default models")
    ap.add_argument("--repeats", type=int, default=1)
    ap.add_argument("--models", nargs="+", default=None)
    ap.add_argument("--score", metavar="RESULTS.json",
                    help="re-score an existing results file")
    args = ap.parse_args()

    if args.score:
        score(json.loads(pathlib.Path(args.score).read_text()))
        return

    models = args.models or DEFAULT_MODELS
    repeats = 1 if args.pilot else args.repeats
    run(models, repeats, args.dry_run)


if __name__ == "__main__":
    main()
