/**
 * sqlDeckKit.tsx — shared constants + deterministic helpers for this reel's
 * three forked deck patterns (SqlAttritionChain, SqlScaleComparison,
 * SqlDivergentFates).
 *
 * WHY THIS FILE EXISTS: the originals in `deckPatterns.tsx` keep their palette
 * and helpers MODULE-PRIVATE (only the components and their data types are
 * exported). A reel-local fork therefore cannot import them and must carry its
 * own copy. Values are duplicated VERBATIM from deckPatterns.tsx so the forks
 * are pixel-identical to the library in every respect except the documented
 * fixes.
 *
 * REEL-LOCAL. Copied into runtime/remotion/src/scenes/ at build time.
 * Do NOT edit the shared library to suit this reel.
 */

/* Deterministic helpers — verbatim from deckPatterns.tsx, which mirrors
   deck_anim.js so HTML(D3) and MP4(Remotion) output match. */
export const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
export const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
export const remap = (x: number, x0: number, x1: number, y0: number, y1: number) => {
  if (x1 === x0) return y0;
  return lerp(y0, y1, clamp((x - x0) / (x1 - x0), 0, 1));
};
export const easeOutCubic = (t: number) => 1 - Math.pow(1 - clamp(t, 0, 1), 3);
export const seeded = (i: number) => {
  const x = Math.sin((i + 1) * 127.1 + 311.7) * 43758.5453;
  return x - Math.floor(x);
};

/* Palette — verbatim from deckPatterns.tsx. */
export const BG = '#F2F0E9';
export const INK = '#3D3929';
export const ACCENT = '#D97757';
export const MUTE = '#7A7265';
export const WARN = '#A44A32';
export const GOOD = '#3D3929';
export const FONT = "'JetBrains Mono', ui-monospace, monospace";

/* Cubic bezier point (Remotion cannot measure the DOM). Verbatim. */
export type Pt = {x: number; y: number};
export const cubicPoint = (P0: Pt, P1: Pt, P2: Pt, P3: Pt, t: number): Pt => {
  const mt = 1 - t;
  const a = mt * mt * mt, b = 3 * mt * mt * t, c = 3 * mt * t * t, d = t * t * t;
  return {
    x: a * P0.x + b * P1.x + c * P2.x + d * P3.x,
    y: a * P0.y + b * P1.y + c * P2.y + d * P3.y,
  };
};

/**
 * RESOLUTION SCALE FACTOR — the one structural change these forks make.
 *
 * The library patterns are registered at 1280x720 and mix `useVideoConfig()`
 * proportions with hardcoded 720p pixel constants (padX=70, x0=150,
 * fontSize=14). That is why re-registering the ORIGINALS at 1920x1080 would be
 * wrong: the type would render proportionally smaller (TEMPLATE-MISSES.md #4).
 *
 * The forks multiply every hardcoded pixel constant by `sc(H)`, so the design
 * is identical at 720 and correct at any height. That lets them register at
 * 1920x1080 and render at a true 3840x2160 under the existing global
 * `--scale=2` — no change to remotion_scenes.py required.
 */
export const sc = (H: number) => H / 720;

/**
 * PORTRAIT SCALE FACTOR — the 9:16 counterpart of `sc(H)`.
 *
 * `sc(H) = H / 720` is a LANDSCAPE-HEIGHT basis. Reusing it in portrait would
 * give H/720 = 1920/720 = 2.67x and blow the type up against a 1080-wide frame.
 * Portrait forks scale off WIDTH instead, so 1080x1920 is the design size and
 * 2160x3840 (the --scale=2 render) is proportionally identical.
 */
export const scW = (W: number) => W / 1080;

/** Greedy wrap by character budget — Remotion cannot measure the DOM. */
export const wrapText = (text: string, maxChars: number): string[] => {
  if (maxChars <= 0 || text.length <= maxChars) return [text];
  const words = text.split(' ');
  const lines: string[] = [];
  let cur = '';
  for (const w of words) {
    if (cur && (cur + ' ' + w).length > maxChars) { lines.push(cur); cur = w; }
    else cur = cur ? cur + ' ' + w : w;
  }
  if (cur) lines.push(cur);
  return lines;
};
