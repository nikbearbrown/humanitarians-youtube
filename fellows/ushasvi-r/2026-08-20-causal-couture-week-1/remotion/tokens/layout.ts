/**
 * layout.ts — shared safe-area and canvas constants for all Remotion scenes.
 *
 * QC RULE: every scene lays essential text, logos, and chips INSIDE SAFE.
 * Nothing that must be readable may live outside SAFE. Decorative backgrounds
 * and full-bleed fills are the only exceptions.
 *
 * FILL RULE: also USE the safe area — do not cluster content in the top
 * third over a small font while the rest of SAFE sits empty. Scale the
 * composition and its type up to occupy SAFE's vertical and horizontal
 * span; the ~24px legibility floor is a floor, not a target. Dead space
 * under undersized content is a defect (FILL-THE-CANVAS LAW, claude-explainer).
 *
 * Text boxes that hold variable-length copy MUST use maxWidth + wrap or
 * auto-shrink (CSS overflow:hidden + text-overflow:ellipsis), never a bare
 * fixed width that silently clips when content is longer than assumed.
 *
 * Usage:
 *   import { CANVAS, SAFE, safeX, safeY } from '../tokens/layout';
 *   style={{ left: safeX(0), top: safeY(0), maxWidth: SAFE.w }}
 */

/** Full canvas — 1920×1080 16:9 30fps */
export const CANVAS = { w: 1920, h: 1080 } as const;

/**
 * 5% title-safe inset: x 96–1824, y 54–1026.
 * Any essential element (text, logo, chip) must sit inside this box.
 */
export const SAFE = {
  x: 96,
  y: 54,
  w: 1728,   // 1920 - 2*96
  h: 972,    // 1080 - 2*54
  r: 1824,   // right edge: SAFE.x + SAFE.w
  b: 1026,   // bottom edge: SAFE.y + SAFE.h
} as const;

/**
 * Convert a relative-safe offset to an absolute canvas coordinate.
 * safeX(0)    → left edge of safe area  (96px)
 * safeX(SAFE.w) → right edge           (1824px)
 */
export const safeX = (offsetFromLeft: number): number => SAFE.x + offsetFromLeft;
export const safeY = (offsetFromTop: number): number  => SAFE.y + offsetFromTop;

/**
 * Shorthand: centered inside the safe area.
 * left: safeX((SAFE.w - myWidth) / 2)
 */
export const safeCenterX = (elementW: number): number =>
  SAFE.x + (SAFE.w - elementW) / 2;
export const safeCenterY = (elementH: number): number =>
  SAFE.y + (SAFE.h - elementH) / 2;

/**
 * fitToSafe — the POSITIVE canvas-fill driver (hardening rule 8).
 *
 * The FILL RULE above is a rule with no enforcer: scenes render content at a
 * fixed size wherever, so a small block sits in the middle over a sea of empty
 * safe area (the negative-space defect). fitToSafe computes the scale that
 * grows a content box of natural size (contentW × contentH) until it occupies
 * `target` (default 0.92) of the safe area on its tighter axis — then caps at
 * `max` so a two-word beat doesn't become billboard type.
 *
 * Usage — wrap a scene's content group:
 *   const s = fitToSafe(measuredW, measuredH);
 *   <div style={{ transform: `scale(${s})`, transformOrigin: 'center' }}> … </div>
 * Center it with safeCenterX/Y on the scaled dimensions. Gate V
 * (qc/final_frame_check.py) fails any beat whose rendered ink still covers
 * < 55% of SAFE, so this driver and that gate are two sides of one rule.
 */
export const fitToSafe = (
  contentW: number,
  contentH: number,
  target = 0.92,
  max = 2.4,
  safe: { w: number; h: number } = SAFE,
): number => {
  if (contentW <= 0 || contentH <= 0) return 1;
  const s = Math.min((safe.w * target) / contentW, (safe.h * target) / contentH);
  return Math.min(Math.max(s, 0.1), max);
};

/** Portrait 9:16 canvas — 1080×1920 */
export const CANVAS916 = { w: 1080, h: 1920 } as const;

/**
 * 5% title-safe inset for 9:16: x 54–1026, y 96–1824.
 * Essential elements (text, logo, chip) must sit inside this box.
 * Note: YouTube Shorts UI occupies roughly the bottom 25% and right ~11%
 * of the frame at runtime — keep critical content above y ~1440 and left of x ~960.
 */
export const SAFE916 = {
  x: 54,
  y: 96,
  w: 972,   // 1080 - 2*54
  h: 1728,  // 1920 - 2*96
  r: 1026,  // SAFE916.x + SAFE916.w
  b: 1824,  // SAFE916.y + SAFE916.h
} as const;

export const safeX916 = (offsetFromLeft: number): number => SAFE916.x + offsetFromLeft;
export const safeY916 = (offsetFromTop: number): number  => SAFE916.y + offsetFromTop;
export const safeCenterX916 = (elementW: number): number =>
  SAFE916.x + (SAFE916.w - elementW) / 2;
export const safeCenterY916 = (elementH: number): number =>
  SAFE916.y + (SAFE916.h - elementH) / 2;
