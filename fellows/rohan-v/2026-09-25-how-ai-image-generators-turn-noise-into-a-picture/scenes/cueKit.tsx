import React from 'react';
import { useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { measureText } from '@remotion/layout-utils';
import { Trail } from '@remotion/motion-blur';
import { AnimatedText, AnimatedCounter } from 'remotion-bits';
import { CLAUDE } from '../tokens/claude';
import { HAI_TYPE } from './haiType';

/**
 * cueKit — shared choreography helpers for word-clock-driven scenes.
 *
 * WHY THIS EXISTS. A scene that drives its reveals off hand-picked fractions of
 * durationInFrames is guessing: the motion lands near the phrase it illustrates
 * but not on it, and the drift is what makes an explainer feel loose. align.py
 * measures when every word is actually spoken and sync_cues.py writes those
 * measured fractions into the beat's props as `cues`. This kit is the consumer
 * side of that contract, plus the motifs the audio reels share so eight new
 * components do not each reinvent a waveform.
 *
 * Every helper is deterministic — no randomness at render time — so a rebuild
 * produces an identical frame and QC sheets stay comparable across builds.
 */

/**
 * Spring feel. An earlier pass used damping 26 / mass 0.9, which is so heavily
 * damped that everything settles dead — technically correct and visually inert.
 * Surveying 81 professionally-built Remotion templates, the convention is
 * damping 12-14, mass 0.5-0.6, stiffness 80-100: a gentle overshoot that reads
 * as fluid rather than mechanical. These are tuned to that.
 */
export const SPRING = { damping: 13, stiffness: 90, mass: 0.55 };
/** For a beat's one decisive moment — snappier, still with a little life. */
export const SPRING_SNAP = { damping: 11, stiffness: 170, mass: 0.5 };
/** Where an overshoot would be wrong (a value landing on a measured number). */
export const SPRING_SETTLE = { damping: 22, stiffness: 120, mass: 0.7 };

export const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
export const op = (v: number) => clamp(v, 0, 1);

export type Cues = Record<string, number> | undefined;

/**
 * The choreography handle. `at` reads a measured cue fraction (falling back to a
 * sensible default so the scene still previews in Studio with no cues wired),
 * `sp` springs at a fraction of the beat, and `ramp` gives a linear 0..1 over a
 * window expressed in fractions.
 */
export function useChoreo(cues: Cues) {
  const frame = useCurrentFrame();
  const { fps, durationInFrames, width, height } = useVideoConfig();
  const D = Math.max(1, durationInFrames);

  const at = (key: string, fallback: number) => {
    const v = cues?.[key];
    return typeof v === 'number' && isFinite(v) ? clamp(v, 0, 1) : fallback;
  };
  /** fraction of the beat -> absolute frame */
  const F = (frac: number) => frac * D;
  /** spring that starts at a fraction of the beat */
  const sp = (frac: number, cfg = SPRING) =>
    op(spring({ frame: frame - F(frac), fps, config: cfg }));
  /** linear 0..1 across [from, to] expressed as fractions of the beat */
  const ramp = (from: number, to: number) =>
    interpolate(frame, [F(from), F(to)], [0, 1], {
      extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
    });
  /** 0..1..0 pulse centred on a fraction — for a moment of emphasis */
  const pulse = (frac: number, wide = 0.06) => {
    const t = (frame / D - frac) / wide;
    return Math.exp(-t * t * 4);
  };

  return { frame, fps, D, width, height, at, F, sp, ramp, pulse };
}

/**
 * EXCLUSIVE EMPHASIS. Given ordered stage values (each 0..1 as it arrives),
 * return the weight each stage should carry so only ONE is ever hot: a stage
 * retires as the next one arrives. Without this every highlight is lit by the
 * end of the beat and the frame reads as several competing emphases rather than
 * a walkthrough.
 */
export function exclusive(stages: number[]): number[] {
  return stages.map((s, i) => (i === stages.length - 1 ? s : s * (1 - stages[i + 1])));
}

/** Deterministic hash in 0..1 — the house noise source. */
export const hash = (x: number, y = 0) => {
  const s = Math.sin(x * 127.1 + y * 311.7) * 43758.5453;
  return s - Math.floor(s);
};

/**
 * Deterministic 4-harmonic waveform path — the channel's waveform language,
 * shared with the stem-separation and loudness reels so every audio reel draws
 * a wave the same way.
 */
export const wavePath = (
  w: number, h: number, seed: number, amp: number,
  n = 120, cycles = 9, phase = 0,
) => {
  let d = '';
  for (let i = 0; i <= n; i++) {
    const t = i / n;
    const s = t * cycles + phase;
    const v =
      (Math.sin(s * 1.0 + seed) * 0.5 +
        Math.sin(s * 2.3 + seed * 1.7) * 0.25 +
        Math.sin(s * 3.7 + seed * 2.3) * 0.15 +
        Math.sin(s * 6.1 + seed * 3.1) * 0.1) * amp;
    d += `${i === 0 ? 'M' : 'L'} ${(t * w).toFixed(2)} ${(h / 2 + v).toFixed(2)} `;
  }
  return d;
};

/** A clean sine path — used where the point is the smooth curve itself. */
export const sinePath = (
  w: number, h: number, amp: number, cycles = 2.2, phase = 0, n = 240,
) => {
  let d = '';
  for (let i = 0; i <= n; i++) {
    const t = i / n;
    const v = Math.sin(t * Math.PI * 2 * cycles + phase) * amp;
    d += `${i === 0 ? 'M' : 'L'} ${(t * w).toFixed(2)} ${(h / 2 - v).toFixed(2)} `;
  }
  return d;
};

/**
 * The same sine, quantised to `levels` rungs — the staircase. Returned as a
 * step path (horizontal run, then vertical riser) so the rounding is visible
 * as steps rather than a smoothed curve.
 */
export const staircasePath = (
  w: number, h: number, amp: number, levels: number,
  cycles = 2.2, phase = 0, n = 96,
) => {
  const step = (2 * amp) / levels;
  const q = (v: number) => Math.round(v / step) * step;
  let d = '';
  let prevY: number | null = null;
  for (let i = 0; i <= n; i++) {
    const t = i / n;
    const x = t * w;
    const y = h / 2 - q(Math.sin(t * Math.PI * 2 * cycles + phase) * amp);
    if (prevY === null) {
      d += `M ${x.toFixed(2)} ${y.toFixed(2)} `;
    } else if (y !== prevY) {
      d += `L ${x.toFixed(2)} ${prevY.toFixed(2)} L ${x.toFixed(2)} ${y.toFixed(2)} `;
    }
    prevY = y;
  }
  d += `L ${w.toFixed(2)} ${(prevY ?? h / 2).toFixed(2)} `;
  return d;
};

/** A jittery low-amplitude trace — what quantisation error looks like. */
export const hissPath = (
  w: number, h: number, amp: number, seed: number, n = 200,
) => {
  let d = '';
  for (let i = 0; i <= n; i++) {
    const t = i / n;
    const v = (hash(i, seed) - 0.5) * 2 * amp;
    d += `${i === 0 ? 'M' : 'L'} ${(t * w).toFixed(2)} ${(h / 2 + v).toFixed(2)} `;
  }
  return d;
};

/**
 * A playhead that sweeps the plot for the whole beat. Its only job is to keep
 * the frame alive — a static graphic held for twenty seconds reads as a
 * screenshot, and this is the cheapest honest way to avoid that.
 */
export const Playhead: React.FC<{
  x: number; y: number; w: number; h: number;
  progress: number; opacity?: number;
}> = ({ x, y, w, h, progress, opacity = 0.5 }) => (
  /* Trail from @remotion/motion-blur leaves a short wake behind the head.
     A 2px hard line crossing a plot reads as a static rule in a still frame;
     with a wake it reads as something travelling. */
  <Trail layers={6} lagInFrames={1.2} trailOpacity={0.55}>
    <div style={{
      position: 'absolute',
      left: x + w * clamp(progress, 0, 1), top: y,
      width: 2, height: h,
      background: CLAUDE.SPARK, opacity,
      boxShadow: `0 0 12px ${CLAUDE.SPARK}`,
    }} />
  </Trail>
);

/**
 * The house eyebrow + serif title block every body beat opens with.
 *
 * The title word-staggers in with a blur lift (`AnimatedText` from
 * remotion-bits) rather than sliding as one block — the single most visible
 * upgrade available, since every beat opens with it.
 *
 * Its font size is MEASURED and stepped down until it fits the safe width.
 * Two of the defects hand-patched in earlier reels were long titles running
 * into the frame edge or wrapping into the graphic beneath; measuring removes
 * that class of bug instead of tuning a magic number per scene.
 */
export const BeatHead: React.FC<{
  eyebrow: string; title: string; inOp: number;
  padX: number; height: number; width?: number; portrait?: boolean;
  startFrame?: number;
  /** Opt-in title size (px). The 9:16 type spec (kerning/reference/type-spec.md
   *  §1) wants titles >= 5.5vh on a phone; the portrait default (3.0vh) predates
   *  it and is kept for earlier reels. Empty `eyebrow` renders nothing. */
  titleSize?: number;
}> = ({ eyebrow, title, inOp, padX, height, width, portrait = false, startFrame = 0, titleSize }) => {
  const maxW = width ? width - padX * 2 : undefined;
  const base = titleSize ?? height * (portrait ? 0.030 : 0.042);

  // step the size down until the measured width fits, then let it wrap
  let size = base;
  if (maxW) {
    for (let i = 0; i < 7; i++) {
      const { width: w } = measureText({
        text: title, fontFamily: HAI_TYPE.serif,
        fontWeight: '600', fontSize: size, letterSpacing: '-0.012em',
      });
      if (w <= maxW * (portrait ? 1.9 : 1.0)) break;
      size *= 0.93;
    }
  }

  return (
    <>
      {eyebrow ? <div style={{
        position: 'absolute', left: padX, top: height * (portrait ? 0.125 : 0.095),
        fontFamily: HAI_TYPE.sans,
        fontSize: height * (portrait ? 0.0135 : 0.0145), fontWeight: 700,
        letterSpacing: 3, textTransform: 'uppercase',
        color: CLAUDE.INK_SOFT, opacity: inOp * 0.8,
      }}>
        {eyebrow}
      </div> : null}
      <div style={{
        position: 'absolute', left: padX, top: height * (portrait ? (eyebrow ? 0.148 : 0.125) : 0.145),
        width: maxW,
      }}>
        <AnimatedText
          transition={{
            split: 'word', splitStagger: 2,
            y: [height * 0.018, 0], opacity: [0, 1], blur: [7, 0],
            frames: [startFrame, startFrame + 20],
            easing: 'easeOutCubic',
          }}
          style={{
            fontFamily: HAI_TYPE.serif, fontSize: size, fontWeight: 600,
            color: CLAUDE.INK, letterSpacing: '-0.012em', lineHeight: 1.1,
          }}
        >
          {title}
        </AnimatedText>
      </div>
    </>
  );
};

/**
 * A number that counts to its value. Replaces the hand-rolled
 * `Math.round(ramp(a,b) * n)` every data beat was carrying.
 */
export const CountTo: React.FC<{
  to: number; fromFrame: number; frames?: number;
  decimals?: number; style?: React.CSSProperties;
  prefix?: React.ReactNode; postfix?: React.ReactNode;
}> = ({ to, fromFrame, frames = 26, decimals = 0, style, prefix, postfix }) => (
  <AnimatedCounter
    transition={{
      values: [0, to],
      frames: [fromFrame, fromFrame + frames],
      easing: 'easeOutQuart',
    }}
    toFixed={decimals}
    prefix={prefix}
    postfix={postfix}
    style={style}
  />
);

/** The house spark line: terracotta rule, serif italic, one compressed claim. */
export const SparkLine: React.FC<{
  text: string; inOp: number; padX: number;
  width: number; height: number; top?: number; portrait?: boolean;
  /** Opt-in font size (px) — the 9:16 spec floor is 3.2vh; default is 2.0vh. */
  fontSize?: number;
}> = ({ text, inOp, padX, width, height, top, portrait = false, fontSize }) => (
  <div style={{
    position: 'absolute', left: padX,
    ...(top !== undefined ? { top } : { bottom: height * 0.075 }),
    width: width - padX * 2,
    display: 'flex', alignItems: portrait ? 'flex-start' : 'center',
    gap: portrait ? 16 : 14, opacity: inOp,
  }}>
    <div style={{
      width: width * (portrait ? 0.085 : 0.055), height: portrait ? 3 : 2,
      background: CLAUDE.SPARK, flexShrink: 0,
      marginTop: portrait ? height * 0.014 : 0,
    }} />
    <span style={{
      fontFamily: HAI_TYPE.serif,
      fontSize: fontSize ?? height * (portrait ? 0.0198 : 0.026),
      fontStyle: 'italic', color: CLAUDE.INK, lineHeight: 1.35,
    }}>
      {text}
    </span>
  </div>
);

/** A MEASURED-badged footnote, for the provenance line under a data beat. */
export const MeasuredNote: React.FC<{
  text: string; inOp: number; padX: number;
  width: number; height: number; top: number;
  label?: string; portrait?: boolean;
}> = ({ text, inOp, padX, width, height, top, label = 'MEASURED', portrait = false }) => (
  <div style={{
    position: 'absolute', left: padX, top, width: width - padX * 2,
    display: 'flex', alignItems: 'flex-start', gap: 14, opacity: inOp,
  }}>
    <div style={{
      fontFamily: HAI_TYPE.sans,
      fontSize: height * (portrait ? 0.0104 : 0.0139), fontWeight: 700,
      letterSpacing: 1.6, color: CLAUDE.SPARK,
      border: `1px solid ${CLAUDE.SPARK}`, borderRadius: 6,
      padding: portrait ? `${height * 0.002}px ${width * 0.014}px` : '4px 11px',
      flexShrink: 0, marginTop: height * 0.003, whiteSpace: 'nowrap',
    }}>
      {label}
    </div>
    <div style={{
      fontFamily: HAI_TYPE.serif,
      fontSize: height * (portrait ? 0.0156 : 0.0194),
      color: CLAUDE.INK_SOFT, lineHeight: 1.45,
    }}>
      {text}
    </div>
  </div>
);

/**
 * SPARK_TEXT — the terracotta for TEXT. The brand spark #D97757 is 2.74:1 on the
 * cream page, under WCAG's 4.5:1, so GATE T (type_check.py §8.3) rightly fails it
 * as a text colour. This deeper step is 5.5:1 on cream and 5.8:1 under white
 * text, and still reads as the same accent. Rule: SPARK for strokes, rules and
 * fills; SPARK_TEXT for any glyph a viewer has to read, and for chips that carry text.
 */
export const SPARK_TEXT = '#A9482B';

/**
 * PHONE — the 9:16 type scale from kerning/reference/type-spec.md §1, as a share
 * of frame height: title 5.5vh, body 4.0vh, label 3.3vh (all-caps, so its cap
 * height clears GATE T's 1.9% run floor), hard floor 3.2vh. Portrait layouts
 * built on it hold LESS text, larger — "if a string can't fit at the floor,
 * that's a content problem (shorten the string)".
 */
export const PHONE = (height: number) => ({
  title: height * 0.050, body: height * 0.040, label: height * 0.033,
  data: height * 0.036, spark: height * 0.034,
});

export { HAI_TYPE } from './haiType';

export const TONE: Record<string, string> = {
  hot: '#C6613F',
  warm: '#D97757',
  ink: '#3D3929',
  soft: '#73705F',
};
