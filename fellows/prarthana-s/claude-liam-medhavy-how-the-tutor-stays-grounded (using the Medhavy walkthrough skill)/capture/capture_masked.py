#!/usr/bin/env python3
"""Reel-local redaction wrapper for brutalist.art's medhavy-walkthrough capture driver.

The toolkit's capture_admin.py is loaded as a module (never edited on disk). Its MASK
JavaScript is extended IN MEMORY with a mask for the term(s) in MW_MASK_TEXT, then the
toolkit's own main() runs unchanged: same plan format, flags, recording and outputs.

  capture_masked.py REEL --run RUN --plan PLAN [capture_admin flags...]   capture
  capture_masked.py --review-sheet REEL --run RUN                          temporary review sheets
  capture_masked.py --purge REEL --run RUN [--plan PLAN]                   delete one run's artifacts
  capture_masked.py --self-test [--workdir DIR] [--keep]                   offline test, dummy term

The mask term is read only from the MW_MASK_TEXT environment variable (comma-separated
for several). It is never printed, logged, or written to any file by this script; all of
this script's output, and the toolkit's, passes through a scrubber that replaces it.
Set it without echo or shell history:   read -rs MW_MASK_TEXT && export MW_MASK_TEXT
"""
import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True   # loading the toolkit module must not write __pycache__ into brutalist.art

HERE =Path(__file__).resolve().parent
TOOLKIT_DRIVER = HERE.parents[4] / 'brutalist.art' / 'skills' / 'make' / 'medhavy-walkthrough' / 'scripts' / 'capture_admin.py'
LABEL = 'Admin account'
MIN_TERM_LEN = 3
LEAK_TOKEN = 'MW_MASK_TERM_LEAK'
SELF_TEST_TERM = 'Testname'

# Appended to the toolkit MASK. __TERMS__/__LABEL__ are filled with JSON literals at runtime
# (browser memory only). Runs as a context init script in every page and popup, and again
# whenever the toolkit re-evaluates MASK after goto/open_textbook; it is idempotent.
EXTRA_JS = r"""
;(() => {
  const TERMS = __TERMS__;
  const LABEL = __LABEL__;
  if (!Array.isArray(TERMS) || !TERMS.length) return;
  const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const RX = new RegExp('(^|[^\\p{L}\\p{N}_])(' + TERMS.map(esc).join('|') + ')(?![\\p{L}\\p{N}_])', 'giu');
  const hit = (s) => { RX.lastIndex = 0; const r = RX.test(String(s || '')); RX.lastIndex = 0; return r; };
  const fix = (s) => { RX.lastIndex = 0; const r = s.replace(RX, (m, pre) => pre + LABEL); RX.lastIndex = 0; return r; };
  const SKIP = new Set(['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEMPLATE']);
  const S = window.__mwTerm || (window.__mwTerm = { installed: false, leak: false, masked: 0 });

  const maskText = (t) => {
    const el = t.parentElement;
    if (el && SKIP.has(el.tagName)) return;
    if (hit(t.nodeValue)) { t.nodeValue = fix(t.nodeValue); S.masked++; }
  };
  const walkAll = (root) => {
    if (!root) return;
    if (root.nodeType === 3) { maskText(root); return; }
    const it = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    let t; while ((t = it.nextNode())) maskText(t);
  };
  // Hub admin header: the <span> right before the "View Analytics" link holds the account's
  // first name (medhavi-hub AdminDashboard.tsx). Replace it whatever it says.
  const header = () => {
    for (const a of document.querySelectorAll('nav a[href="/admin/analytics"]')) {
      const sp = a.previousElementSibling;
      if (sp && sp.tagName === 'SPAN' && sp.textContent !== LABEL) { sp.textContent = LABEL; S.masked++; }
    }
  };
  // Fail closed: the term is visible and could not be masked (e.g. split across elements).
  // Blank the page to a solid canary colour before it can paint; the wrapper scans every
  // recorded video for this colour, and the toolkit's per-step leak check throws.
  const failSafe = () => {
    S.leak = true;
    try { document.documentElement.innerHTML = '<head></head><body style="margin:0;background:#FF00FF;min-height:100vh"></body>'; } catch (e) {}
  };
  const visibleLeak = () => {
    if (!document.body) return false;
    if (hit(document.body.innerText)) return true;
    for (const f of document.querySelectorAll('input, textarea')) {
      if (hit(f.value) || hit(f.placeholder)) return true;
    }
    return false;
  };
  const scan = () => {
    header(); walkAll(document);
    if (visibleLeak()) failSafe();
  };
  // Catches a term split across elements (e.g. "Prar<b>thana</b>") near a mutation, using
  // rendered text (innerText excludes <script>/<style>), so framework payloads don't trip it.
  const localLeak = (n) => {
    let el = n.nodeType === 1 ? n : n.parentElement;
    for (let i = 0; el && i < 3; i++, el = el.parentElement) {
      if (!SKIP.has(el.tagName) && hit(el.innerText)) return true;
    }
    return false;
  };

  if (!S.installed) {
    S.installed = true;
    // childList AND characterData: React often updates an existing text node in place,
    // which a childList-only observer never sees. Callbacks run before the next paint.
    new MutationObserver((recs) => {
      const touched = [];
      for (const r of recs) {
        if (r.type === 'characterData') { maskText(r.target); touched.push(r.target); }
        else for (const n of r.addedNodes) { walkAll(n); touched.push(n); }
      }
      header();
      for (const n of touched) { if (localLeak(n)) { failSafe(); break; } }
    }).observe(document, { childList: true, subtree: true, characterData: true });
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', scan, { once: true });
    setInterval(() => { if (visibleLeak()) failSafe(); }, 1000);
  }
  scan();

  // Extend the toolkit's leak check (it calls this after every plan step): the configured
  // term now counts, and a leak throws so the toolkit's evaluate() raises and the run stops.
  const base = window.__mwLeaks;
  if (typeof base === 'function' && !base.__mwTermWrapped) {
    const wrapped = () => {
      const n = base();
      scan();
      if (S.leak) throw new Error('""" + LEAK_TOKEN + r"""');
      return n;
    };
    wrapped.__mwTermWrapped = true;
    window.__mwLeaks = wrapped;
  }
})();
"""


# ---------------------------------------------------------------- helpers

def load_terms():
    raw = os.environ.get('MW_MASK_TEXT', '')
    return [t.strip() for t in raw.split(',') if t.strip()]


def build_extra(terms):
    return EXTRA_JS.replace('__TERMS__', json.dumps(terms)).replace('__LABEL__', json.dumps(LABEL))


def scrub(text, terms):
    s = str(text)
    for t in sorted(terms, key=len, reverse=True):
        s = re.sub(re.escape(t), '[mask term]', s, flags=re.IGNORECASE)
    return s


class Scrubbed:
    """Text stream proxy that replaces the mask term(s) before anything reaches the terminal."""
    def __init__(self, stream, terms):
        self._s, self._t = stream, terms
    def write(self, s):
        return self._s.write(scrub(s, self._t))
    def flush(self):
        return self._s.flush()
    def __getattr__(self, name):
        return getattr(self._s, name)


def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


def load_toolkit(path):
    spec = importlib.util.spec_from_file_location('capture_admin', str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_videos(cap, run):
    pat = re.compile(rf'{re.escape(run)}(-p\d+)?\.mp4')
    return sorted(f for f in cap.iterdir() if f.is_file() and pat.fullmatch(f.name)) if cap.is_dir() else []


def screenshot_names(cap, run, plan_path=None):
    names = set()
    if plan_path and Path(plan_path).is_file():
        try:
            for s in json.loads(Path(plan_path).read_text()).get('steps', []):
                if 'screenshot' in s:
                    names.add(str(s['screenshot']))
        except Exception:
            pass
    acts = cap / f'{run}-actions.jsonl'
    if acts.is_file():
        for line in acts.read_text().splitlines():
            try:
                a = json.loads(line)
            except Exception:
                continue
            if a.get('action') == 'screenshot':
                names.add(str(a.get('selector_or_text')))
    return names


def purge(reel, run, plan_path=None, keep_png=False, reason=None, terms=()):
    """Delete one run's videos, raw recording, screenshots, action log, review sheets and
    redaction records. Names are exact (plan/log-derived), so sibling runs are untouched."""
    cap = Path(reel).resolve() / 'capture'
    removed = []
    raw = cap / f'.{run}-raw'
    if raw.exists():
        shutil.rmtree(raw, ignore_errors=True); removed.append(raw.name + '/')
    for f in run_videos(cap, run):
        f.unlink(); removed.append(f.name)
    if not keep_png:
        for n in screenshot_names(cap, run, plan_path):
            f = cap / f'{run}-{n}.png'
            if f.exists():
                f.unlink(); removed.append(f.name)
    acts = cap / f'{run}-actions.jsonl'
    if acts.exists():
        acts.unlink(); removed.append(acts.name)
    rev = cap / '_review' / run
    if rev.exists():
        shutil.rmtree(rev, ignore_errors=True); removed.append(f'_review/{run}/')
    red = cap / 'redaction.jsonl'
    if red.is_file():
        keep = []
        for line in red.read_text().splitlines():
            try:
                if json.loads(line).get('capture') == run:
                    continue
            except Exception:
                pass
            keep.append(line)
        red.write_text('\n'.join(keep) + ('\n' if keep else ''))
    if reason is not None:
        cap.mkdir(parents=True, exist_ok=True)
        (cap / f'{run}-ABORTED.txt').write_text(scrub(
            f'run: {run}\nreason: {reason}\nscreenshots kept: {"yes (each passed the per-step leak check)" if keep_png else "no"}\n'
            f'removed: {", ".join(removed) or "nothing"}\n', terms))
    return removed


def canary_frames(video, fps=4):
    """Count frames that are mostly the fail-safe canary colour (#FF00FF)."""
    w, h = 64, 36
    p = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(video), '-vf', f'fps={fps},scale={w}:{h}',
                        '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True)
    size, data, bad = w * h * 3, p.stdout, 0
    for i in range(0, len(data) - size + 1, size):
        fr = data[i:i + size]
        mag = sum(1 for r, g, b in zip(fr[0::3], fr[1::3], fr[2::3]) if r > 200 and g < 80 and b > 200)
        if mag > 0.4 * w * h:
            bad += 1
    return bad


def file_has_term(path, terms):
    try:
        data = Path(path).read_bytes().lower()
    except Exception:
        return False
    return any(t.lower().encode() in data for t in terms)


# ---------------------------------------------------------------- capture

def capture(argv, toolkit):
    terms = load_terms()
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument('reel', type=Path)
    ap.add_argument('--run', required=True)
    ap.add_argument('--plan', required=True, type=Path)
    ap.add_argument('--no-session', action='store_true')
    known, _ = ap.parse_known_args(argv)
    signed_in = not known.no_session

    if signed_in and not terms:
        print('REFUSED: MW_MASK_TEXT is not set; a signed-in capture needs a mask term.', file=sys.stderr)
        return 2
    if any(len(t) < MIN_TERM_LEN for t in terms):
        print(f'REFUSED: every mask term must be at least {MIN_TERM_LEN} characters.', file=sys.stderr)
        return 2
    if terms and (any(t.lower() in known.run.lower() for t in terms)
                  or (known.plan.is_file() and file_has_term(known.plan, terms))):
        print('REFUSED: the run name or the plan contains the mask term.', file=sys.stderr)
        return 2
    if not Path(toolkit).is_file():
        print(f'REFUSED: toolkit driver not found at {toolkit}', file=sys.stderr)
        return 2

    reel, run = known.reel.resolve(), known.run
    cap = reel / 'capture'
    before = sha256(toolkit)
    mod = load_toolkit(toolkit)
    if terms:
        mod.MASK = mod.MASK + build_extra(terms)          # in memory only; the file is untouched

    out, err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = Scrubbed(out, terms), Scrubbed(err, terms)
    sys.argv = [str(toolkit)] + list(argv)
    failure = None
    try:
        rc = mod.main()
        if rc not in (0, None):
            failure = f'toolkit exited with status {rc}'
    except SystemExit as e:
        if e.code not in (0, None):
            failure = scrub(e.code, terms)
    except BaseException as e:                            # includes the in-page leak throw
        first = scrub(str(e), terms).strip().splitlines()
        failure = f'{type(e).__name__}: {first[0][:300] if first else ""}'
    finally:
        sys.stdout, sys.stderr = out, err

    if sha256(toolkit) != before:
        print('WARNING: toolkit driver changed on disk during the run (not by this wrapper).', file=sys.stderr)

    if failure is not None:
        leak = LEAK_TOKEN in failure or failure.startswith('LEAK')
        reason = ('mask term (or a toolkit-detected email/code) visible in the active page DOM; fail-closed abort'
                  if leak else f'run failed before completion ({failure})')
        removed = purge(reel, run, known.plan, keep_png=not leak, reason=reason, terms=terms)
        print(scrub(f'ABORTED {run}: {reason}. Removed: {", ".join(removed) or "nothing"}.', terms), file=sys.stderr)
        return 3 if leak else 4

    # Post-run checks: canary colour in ANY recorded tab (the toolkit only checks the active
    # tab), and the term in any text artifact of this run.
    videos = run_videos(cap, run)
    for v in videos:
        n = canary_frames(v)
        if n:
            reason = f'fail-safe canary found in recorded video {v.name} ({n} sampled frames)'
            removed = purge(reel, run, known.plan, reason=reason, terms=terms)
            print(f'ABORTED {run}: {reason}. Removed: {", ".join(removed)}.', file=sys.stderr)
            return 3
    if terms:
        texts = [cap / f'{run}-actions.jsonl', cap / 'redaction.jsonl']
        if any(file_has_term(t, terms) for t in texts if t.exists()):
            reason = 'mask term found in a run log'
            removed = purge(reel, run, known.plan, reason=reason, terms=terms)
            print(f'ABORTED {run}: {reason}. Removed: {", ".join(removed)}.', file=sys.stderr)
            return 3
    print(f'OK {run}: capture finished; DOM leak checks passed on every step; no canary in '
          f'{len(videos)} video(s). Next: --review-sheet for the human frame review.')
    return 0


# ---------------------------------------------------------------- review sheets

def duration(f):
    p = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(f)],
                       capture_output=True, text=True, check=True)
    return float(p.stdout.strip())


def review_sheet(reel, run):
    """Temporary sheets for the human redaction review: 1 fps across each video, plus every
    frame of the 2 s after each navigation. Deleted by --purge."""
    reel = Path(reel).resolve(); cap = reel / 'capture'
    videos = run_videos(cap, run)
    if not videos:
        print(f'No videos for {run}.', file=sys.stderr); return 2
    for v in videos:
        if canary_frames(v):
            removed = purge(reel, run, reason=f'fail-safe canary found in {v.name} during review', terms=())
            print(f'ABORTED {run}: canary in {v.name}. Removed: {", ".join(removed)}.', file=sys.stderr)
            return 3
    out = cap / '_review' / run
    shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True)
    for v in videos:
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(v), '-vf', 'fps=1,scale=960:540,tile=4x4',
                        str(out / f'{v.stem}-1fps-%03d.png')], check=True)
    acts = []
    af = cap / f'{run}-actions.jsonl'
    if af.is_file():
        acts = [json.loads(l) for l in af.read_text().splitlines() if l.strip()]
    main_v = cap / f'{run}.mp4'
    p2 = cap / f'{run}-p2.mp4'
    offset = duration(main_v) - duration(p2) if p2.exists() else None
    switched, k = False, 0
    for a in acts:
        if a.get('action') not in ('goto', 'open_textbook', 'click_link'):
            continue
        t = a['t_ms'] / 1000.0
        targets = [(p2, max(0.0, t - offset))] if (switched and offset is not None) else [(main_v, t)]
        if a['action'] == 'open_textbook' and offset is not None:
            targets.append((p2, 0.0)); switched = True
        for v, ts in targets:
            k += 1
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{ts:.2f}', '-t', '2', '-i', str(v),
                            '-vf', 'scale=640:360,tile=6x10', '-frames:v', '1',
                            str(out / f'{v.stem}-nav{k:02d}.png')], check=True)
    print(f'Review sheets in {out.relative_to(reel)} (temporary). If the name appears in ANY sheet: '
          f'capture_masked.py --purge {reel} --run {run} --plan <plan>')
    return 0


# ---------------------------------------------------------------- self-test (offline, dummy term)

PAGES = {
    'clean.html': """<!doctype html><html><body>
<nav><span class="text-sm">Testname</span> <a href="/admin/analytics">View Analytics</a> <span>ADMIN</span></nav>
<h1>Testname's dashboard</h1><button>Hello Testname</button>
<p>Contact jane.doe@university.edu, invite CLS-ABC123</p>
<p id="late">Welcome</p>
<script>setTimeout(function(){ document.getElementById('late').firstChild.nodeValue = 'Welcome back, Testname'; }, 500);</script>
</body></html>""",
    'split.html': """<!doctype html><html><body><p>Hi Test<b>name</b></p></body></html>""",
    'hub.html': """<!doctype html><html><body>
<div class="card"><h3>Cancer textbook</h3><button onclick="window.open('book.html')">Open Textbook</button></div>
<script>document.querySelector('button').addEventListener('click', function(){
  setTimeout(function(){ document.body.insertAdjacentHTML('beforeend', '<p>Test<b>name</b></p>'); }, 1500); });</script>
</body></html>""",
    'book.html': """<!doctype html><html><body><h1>Book page</h1><p>Nothing personal here.</p></body></html>""",
}


def self_test(workdir=None, keep=False, toolkit=TOOLKIT_DRIVER):
    from playwright.sync_api import sync_playwright
    root = Path(tempfile.mkdtemp(prefix='mw-selftest-', dir=workdir))
    site = root / 'site'; site.mkdir()
    for name, html in PAGES.items():
        (site / name).write_text(html)
    state = root / 'empty-state.json'; state.write_text('{"cookies": [], "origins": []}')
    base = 'file://' + str(site)
    toolkit_sha = sha256(toolkit)
    results, logs = [], []

    def record(name, ok, detail=''):
        results.append((name, bool(ok), detail))

    def plan(reel, steps):
        reel.mkdir(parents=True, exist_ok=True)
        p = reel / 'plan.json'
        p.write_text(json.dumps({'base_url': base, 'context': 'admin', 'steps': steps}))
        return p

    def run(reel, run_name, plan_path, env_term, extra=()):
        env = {k: v for k, v in os.environ.items() if k != 'MW_MASK_TEXT'}
        if env_term is not None:
            env['MW_MASK_TEXT'] = env_term
        cmd = [sys.executable, str(Path(__file__).resolve()), str(reel), '--run', run_name, '--plan', str(plan_path),
               '--css-size', '1600x900', '--dpr', '2.4', '--state', str(state), '--toolkit', str(toolkit), *extra]
        p = subprocess.run(cmd, env=env, capture_output=True, text=True)
        logs.append(p.stdout + p.stderr)
        return p

    def run_files(reel, run_name):
        cap = reel / 'capture'
        if not cap.is_dir():
            return []
        return [f.name for f in cap.iterdir() if f.name.startswith(run_name) or f.name == f'.{run_name}-raw']

    # A: signed-in run without MW_MASK_TEXT is refused.
    ra = root / 'reel-a'
    pa = plan(ra, [{'goto': '/clean.html'}])
    p = run(ra, 'run-a', pa, None)
    record('A refuse: MW_MASK_TEXT unset', p.returncode == 2 and not run_files(ra, 'run-a'), f'rc={p.returncode}')

    # B: too-short term is refused.
    p = run(ra, 'run-b', pa, 'Te')
    record('B refuse: term shorter than 3', p.returncode == 2 and not run_files(ra, 'run-b'), f'rc={p.returncode}')

    # C: clean page (header span, button, heading, in-place text update, email, CLS code).
    rc_ = root / 'reel-c'
    pc = plan(rc_, [{'goto': '/clean.html', 'settle_ms': 1500}, {'wait_ms': 1000}, {'screenshot': 'clean'}])
    p = run(rc_, 'run-c', pc, SELF_TEST_TERM)
    capc = rc_ / 'capture'
    red = [json.loads(l) for l in (capc / 'redaction.jsonl').read_text().splitlines()] if (capc / 'redaction.jsonl').exists() else []
    ok = (p.returncode == 0 and (capc / 'run-c.mp4').exists() and (capc / 'run-c-clean.png').exists()
          and red and all(r['raw_emails_or_codes_visible'] == 0 for r in red) and not (capc / 'run-c-ABORTED.txt').exists())
    record('C clean page: run completes, no leaks, outputs kept', ok, f'rc={p.returncode}, redaction steps={len(red)}')

    # C2: review sheets are created, then --purge removes every artifact of the run.
    p2 = subprocess.run([sys.executable, str(Path(__file__).resolve()), '--review-sheet', str(rc_), '--run', 'run-c'],
                        capture_output=True, text=True)
    logs.append(p2.stdout + p2.stderr)
    sheets = list((capc / '_review' / 'run-c').glob('*.png')) if (capc / '_review' / 'run-c').exists() else []
    p3 = subprocess.run([sys.executable, str(Path(__file__).resolve()), '--purge', str(rc_), '--run', 'run-c', '--plan', str(pc)],
                        capture_output=True, text=True)
    logs.append(p3.stdout + p3.stderr)
    left = [f for f in run_files(rc_, 'run-c') if not f.endswith('ABORTED.txt')] + (['_review/run-c'] if (capc / '_review' / 'run-c').exists() else [])
    record('C2 review sheets created, then --purge deletes videos/screenshots/log/sheets',
           p2.returncode == 0 and sheets and p3.returncode == 0 and not left, f'sheets={len(sheets)}, left={left}')

    # D: unmaskable term in the ACTIVE page -> immediate fail-closed abort, everything deleted.
    rd = root / 'reel-d'
    pd = plan(rd, [{'goto': '/split.html', 'settle_ms': 800}, {'wait_ms': 3000}, {'screenshot': 'split'}])
    p = run(rd, 'run-d', pd, SELF_TEST_TERM)
    capd = rd / 'capture'
    left = [f for f in run_files(rd, 'run-d') if not f.endswith('ABORTED.txt')]
    record('D active-page leak: abort at first check; videos/screenshots/log deleted',
           p.returncode == 3 and (capd / 'run-d-ABORTED.txt').exists() and not left, f'rc={p.returncode}, left={left}')

    # E: leak appears in the BACKGROUND tab after a popup opens -> canary found in its video.
    re_ = root / 'reel-e'
    pe = plan(re_, [{'goto': '/hub.html', 'settle_ms': 800}, {'open_textbook': 'Cancer textbook', 'settle_ms': 800},
                    {'wait_ms': 3500}, {'screenshot': 'book'}])
    p = run(re_, 'run-e', pe, SELF_TEST_TERM)
    cape = re_ / 'capture'
    left = [f for f in run_files(re_, 'run-e') if not f.endswith('ABORTED.txt')]
    aborted = (cape / 'run-e-ABORTED.txt').read_text() if (cape / 'run-e-ABORTED.txt').exists() else ''
    record('E background-tab leak: canary detected in recorded video; everything deleted',
           p.returncode == 3 and 'canary' in aborted and not left, f'rc={p.returncode}, left={left}')

    # F: independent DOM verification of the combined mask, sampled across the in-place update.
    mod = load_toolkit(toolkit)
    combined = mod.MASK + build_extra([SELF_TEST_TERM])
    rx = re.compile(r'(?<![A-Za-z0-9_])' + SELF_TEST_TERM + r'(?![A-Za-z0-9_])', re.I)
    with sync_playwright() as pw:
        b = pw.chromium.launch(headless=True)

        def sample(script):
            c = b.new_context(); c.add_init_script(script); pg = c.new_page()
            pg.goto(base + '/clean.html')
            seen, hdr = False, None
            for _ in range(24):
                txt = pg.evaluate('document.body.innerText')
                seen = seen or bool(rx.search(txt))
                pg.wait_for_timeout(50)
            hdr = pg.evaluate('document.querySelector("nav span").textContent')
            final = pg.evaluate('document.body.innerText')
            c.close()
            return seen, hdr, final

        seen, hdr, final = sample(combined)
        record('F1 combined mask: term never visible across 1.2 s incl. in-place update', not seen)
        record('F2 header span replaced with neutral label', hdr == LABEL, f'header={hdr!r}')
        record('F3 toolkit masking preserved (email and CLS code masked)',
               'jane.doe@university.edu' not in final and 'CLS-ABC123' not in final)
        ctrl_seen, _, _ = sample(mod.MASK)
        b.close()
    ctrl = f'toolkit mask alone leaves the single-word term visible: {ctrl_seen} (informational; shows why the wrapper exists)'

    # G: the term never appears in any artifact filename/content or in any process output.
    hits = []
    for reel in root.glob('reel-*'):
        for f in reel.rglob('*'):
            if f.name == 'plan.json':
                continue
            if SELF_TEST_TERM.lower() in f.name.lower() or (f.is_file() and file_has_term(f, [SELF_TEST_TERM])):
                hits.append(str(f.relative_to(root)))
    out_hits = [i for i, l in enumerate(logs) if SELF_TEST_TERM.lower() in l.lower()]
    record('G term absent from artifacts, filenames, logs, ABORTED notes and all output', not hits and not out_hits,
           f'files={hits}, outputs={out_hits}')

    # H: toolkit file unchanged on disk.
    record('H toolkit capture_admin.py unchanged (sha256)', sha256(toolkit) == toolkit_sha)

    width = max(len(n) for n, _, _ in results)
    for name, ok, detail in results:
        print(f'{"PASS" if ok else "FAIL"}  {name.ljust(width)}  {detail}')
    print(f'INFO  {ctrl}')
    all_ok = all(ok for _, ok, _ in results)
    print(f'\nSELF-TEST {"PASSED" if all_ok else "FAILED"}: {sum(ok for _, ok, _ in results)}/{len(results)} checks. '
          f'Base URL was local file:// only; dummy term only.')
    if all_ok and not keep:
        shutil.rmtree(root, ignore_errors=True)
    else:
        print(f'Work dir kept: {root}')
    return 0 if all_ok else 1


# ---------------------------------------------------------------- entry

def main():
    argv = sys.argv[1:]
    toolkit = TOOLKIT_DRIVER
    if '--toolkit' in argv:
        i = argv.index('--toolkit'); toolkit = Path(argv[i + 1]).resolve(); del argv[i:i + 2]
    if '--self-test' in argv:
        ap = argparse.ArgumentParser()
        ap.add_argument('--self-test', action='store_true'); ap.add_argument('--workdir'); ap.add_argument('--keep', action='store_true')
        a = ap.parse_args(argv)
        return self_test(a.workdir, a.keep, toolkit)
    if '--review-sheet' in argv or '--purge' in argv:
        ap = argparse.ArgumentParser()
        ap.add_argument('--review-sheet', dest='review', metavar='REEL'); ap.add_argument('--purge', metavar='REEL')
        ap.add_argument('--run', required=True); ap.add_argument('--plan')
        a = ap.parse_args(argv)
        if a.review:
            return review_sheet(a.review, a.run)
        removed = purge(a.purge, a.run, a.plan, reason='purged by request after human review', terms=load_terms())
        print(f'PURGED {a.run}: {", ".join(removed) or "nothing"}.')
        return 0
    return capture(argv, toolkit)


if __name__ == '__main__':
    sys.exit(main())
