import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE, SAFE916 } from '../tokens/layout';

/**
 * Trilateration — one satellite gives a circle of possible positions, two
 * narrow it to two points, three meet at one point. Geometry is real: each
 * radius is the true distance from its satellite to the receiver, so the
 * circles genuinely intersect at one point. Adapts to 16:9 and 9:16 (the
 * portrait composition re-centres and rescales; it is not a crop).
 * Terracotta marks only the final position.
 */

export const trilaterationSchema = z.object({
  youLabel: z.string().default('YOU ARE HERE'),
  twoLabel: z.string().default('two possible spots'),
  caption: z.string().default(''),
  sparkLine: z.string().default(''),
  durationSeconds: z.number().optional(),
});
export type TrilaterationProps = z.infer<typeof trilaterationSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

// satellite offsets from the receiver, in landscape pixels
const OFF = [[-190, -150], [210, -130], [40, 215]];

export const Trilateration: React.FC<TrilaterationProps> = ({ youLabel, twoLabel, caption, sparkLine }) => {
  const frame = useCurrentFrame();
  const { durationInFrames, width, height } = useVideoConfig();
  const portrait = height > width;
  const p = clamp01(frame / Math.max(1, durationInFrames));
  // scaled so every circle stays inside the title-safe area in both aspects
  const k = portrait ? 0.95 : 0.82;
  const P = portrait ? [540, 800] : [960, 450];
  const sats = OFF.map(([dx, dy]) => [P[0] + dx * k, P[1] + dy * k]);
  const radii = sats.map(([x, y]) => Math.hypot(x - P[0], y - P[1]));

  // the second intersection of circles 1 and 2 (the "other" candidate point)
  const [x1, y1] = sats[0], [x2, y2] = sats[1], r1 = radii[0], r2 = radii[1];
  const d = Math.hypot(x2 - x1, y2 - y1);
  const a = (r1 * r1 - r2 * r2 + d * d) / (2 * d);
  const h = Math.sqrt(Math.max(0, r1 * r1 - a * a));
  const mx = x1 + (a * (x2 - x1)) / d, my = y1 + (a * (y2 - y1)) / d;
  const cand = [[mx + (h * (y2 - y1)) / d, my - (h * (x2 - x1)) / d],
                [mx - (h * (y2 - y1)) / d, my + (h * (x2 - x1)) / d]];
  const other = cand.reduce((b, c) => (Math.hypot(c[0] - P[0], c[1] - P[1]) > Math.hypot(b[0] - P[0], b[1] - P[1]) ? c : b));

  const c1 = ramp(p, 0.05, 0.25), c2 = ramp(p, 0.3, 0.48), two = ramp(p, 0.45, 0.55), c3 = ramp(p, 0.56, 0.72);
  const you = ramp(p, 0.72, 0.8);
  const circ = [c1, c2, c3];
  const fs = portrait ? 1.3 : 1;
  const safe = portrait ? SAFE916 : SAFE;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <svg width={width} height={height} style={{ position: 'absolute', inset: 0 }}>
        {sats.map(([x, y], i) => (
          <g key={i} opacity={circ[i] > 0 ? 1 : 0}>
            <circle cx={x} cy={y} r={radii[i]} fill="none" stroke={CLAUDE.INK} strokeWidth={4 * fs}
                    pathLength={1} strokeDasharray={1} strokeDashoffset={1 - circ[i]} />
            <circle cx={x} cy={y} r={11 * fs} fill={CLAUDE.INK} />
          </g>
        ))}
        {/* two candidate points after two circles */}
        {[P, other].map(([x, y], i) => (
          <circle key={i} cx={x} cy={y} r={14 * fs} fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={4}
                  opacity={two * (1 - you * (i === 1 ? 0.85 : 0))} />
        ))}
        <circle cx={P[0]} cy={P[1]} r={18 * fs * (0.6 + 0.4 * you)} fill={CLAUDE.SPARK} opacity={you} />
      </svg>

      {sats.map(([x, y], i) => (
        <div key={i} style={{ position: 'absolute', left: x - 120 * fs, top: y + (i === 2 ? 18 : -66) * fs, width: 240 * fs,
          textAlign: 'center', fontFamily: SANS, fontSize: 40 * fs, letterSpacing: 2, color: CLAUDE.INK, opacity: circ[i] > 0 ? 1 : 0 }}>
          SAT {i + 1}</div>
      ))}
      <div style={{ position: 'absolute', left: other[0] + 26 * fs, top: other[1] - 24 * fs, fontFamily: SANS,
        fontSize: 40 * fs, color: CLAUDE.INK_SOFT, opacity: two * (1 - you) }}>{twoLabel}</div>
      <div style={{ position: 'absolute', left: P[0] + 30 * fs, top: P[1] - 30 * fs, fontFamily: SANS, fontSize: 44 * fs,
        letterSpacing: 2, color: CLAUDE.INK, opacity: you, background: CLAUDE.PAGE, padding: '2px 10px',
        borderRadius: 6 }}>{youLabel}</div>

      <div style={{ position: 'absolute', left: safe.x, top: portrait ? 1480 : 860, width: safe.w, fontFamily: SANS,
        fontSize: 44 * fs, lineHeight: 1.25, color: CLAUDE.INK_SOFT, opacity: ramp(p, 0.8, 0.9) }}>{caption}</div>
      <div style={{ position: 'absolute', left: safe.x, top: portrait ? 1680 : 930, width: safe.w, display: 'flex',
        alignItems: 'center', gap: 14, fontFamily: SERIF, fontSize: (portrait ? 68 : 54), color: CLAUDE.INK, opacity: ramp(p, 0.04, 0.16) }}>
        <span style={{ color: CLAUDE.SPARK, fontSize: portrait ? 72 : 58 }}>✻</span><span>{sparkLine}</span>
      </div>
    </AbsoluteFill>
  );
};
