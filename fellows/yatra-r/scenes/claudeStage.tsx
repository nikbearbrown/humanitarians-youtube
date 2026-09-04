/**
 * claudeStage.tsx — shared stage furniture for claude-brand illustration beats.
 *
 * Content-free on purpose: ground, safe-area mapping, the LOGO LAW corner bug, and the
 * eyebrow+title block. Every claude illustration scene needs these and they are pure
 * layout, so they belong in one place rather than being re-typed per reel.
 *
 * NOTE ON DUPLICATION: `scenes/BottleneckMoved.tsx` carries its own private copies of
 * these helpers. That reel is already built, QC'd and delivered, so it was left alone
 * rather than refactored underneath a verified master. Folding it onto this module is a
 * safe follow-up, not something to do mid-flight.
 */
import React from 'react';
import {AbsoluteFill} from 'remotion';
import {CANVAS, SAFE} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';

/** The claude illustration ground — matches deckPatterns' own BG constant. */
export const STAGE = '#F2F0E9';
export const RULE = '#D8D4C8';
export const MUTE = '#7A7265';

export const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
/** eased, clamped progress within a [a,b] window of the beat */
export const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));

/**
 * LOGO LAW — small, low-opacity corner bug, lower-right, INSIDE the title-safe inset,
 * never covering content. No logo file ships for @NikBearBrown in this tree, so the
 * law's stated fallback applies: the handle as a clean wordmark in the Claude serif.
 */
export const LogoBug: React.FC<{handle?: string}> = ({handle = '@Yatra'}) => (
  <div
    style={{
      position: 'absolute',
      right: CANVAS.w - SAFE.r,
      bottom: CANVAS.h - SAFE.b,
      fontFamily: CLAUDE_FONT.serif,
      fontSize: 26,
      color: CLAUDE.INK,
      opacity: 0.3,
      letterSpacing: '.04em',
      pointerEvents: 'none',
    }}
  >
    {handle}
  </div>
);

/**
 * SafeStage — for REUSED deckPatterns scenes only.
 *
 * Those components lay out against useVideoConfig() and place end-of-track label boxes
 * hard against the canvas edge; at 1920×1080 that lands past SAFE.r in the 4K render.
 * They are shared with other reels, so instead of widening their internal margins the
 * whole composition is mapped onto the safe box. The inset is a uniform 5%, so
 * SAFE.w/CANVAS.w === SAFE.h/CANVAS.h === 0.9 exactly — isotropic, no distortion, and
 * ink coverage as a fraction of SAFE is unchanged.
 */
const SAFE_SCALE = SAFE.w / CANVAS.w;

export const SafeStage: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{backgroundColor: STAGE}}>
    <div
      style={{
        position: 'absolute',
        left: SAFE.x,
        top: SAFE.y,
        width: CANVAS.w,
        height: CANVAS.h,
        transform: `scale(${SAFE_SCALE})`,
        transformOrigin: 'top left',
      }}
    >
      {children}
    </div>
    <LogoBug />
  </AbsoluteFill>
);

/** Plain stage — for scenes authored at safe-box coordinates directly. */
export const PlainStage: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{backgroundColor: STAGE}}>
    {children}
    <LogoBug />
  </AbsoluteFill>
);

/** Shared eyebrow + title block, authored at safe-box coordinates. */
export const Head: React.FC<{meta: string; title: string}> = ({meta, title}) => (
  <>
    <div
      style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 6,
        fontFamily: CLAUDE_FONT.ui, fontSize: 22, letterSpacing: '.18em',
        color: MUTE, fontWeight: 600,
      }}
    >
      {meta.toUpperCase()}
    </div>
    <div
      style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 62,
        fontFamily: CLAUDE_FONT.serif, fontSize: 78, color: CLAUDE.INK,
        lineHeight: 1.05, maxWidth: SAFE.w,
      }}
    >
      {title}
    </div>
  </>
);
