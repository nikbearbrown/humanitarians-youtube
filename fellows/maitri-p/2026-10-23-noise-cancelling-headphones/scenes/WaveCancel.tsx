import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE } from '../tokens/layout';

/**
 * WaveCancel — sound as pressure waves, and destructive interference.
 *
 *   phase "pressure" — one travelling wave with higher/lower pressure labels.
 *   phase "cancel"   — outside noise, the opposite wave, and their computed sum.
 *
 * The sum is real arithmetic, not a drawing: the opposite wave is given a small
 * amplitude/phase mismatch (as real headphones have), so the result is a much
 * smaller wave — never a flat line. Quieter, not silent.
 * Terracotta strokes the opposite wave only (structural); all text is INK.
 */

export const waveCancelSchema = z.object({
  phase: z.enum(['pressure', 'cancel']).default('cancel'),
  noiseLabel: z.string().default('OUTSIDE NOISE'),
  antiLabel: z.string().default('OPPOSITE SOUND'),
  sumLabel: z.string().default('AT YOUR EAR'),
  highLabel: z.string().default('higher pressure'),
  lowLabel: z.string().default('lower pressure'),
  mismatchGain: z.number().default(0.88),   // opposite wave strength vs noise
  mismatchPhase: z.number().default(0.22),  // radians of timing error
  sparkLine: z.string().default(''),
  durationSeconds: z.number().optional(),
});
export type WaveCancelProps = z.infer<typeof waveCancelSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

export const wavePath = (x0: number, x1: number, cy: number, amp: number, k: number,
                         shift: number, f: (t: number) => number) => {
  let d = '';
  for (let x = x0; x <= x1; x += 6) {
    const y = cy - amp * f((x - x0) * k + shift);
    d += (d ? ' L ' : 'M ') + x.toFixed(1) + ' ' + y.toFixed(1);
  }
  return d;
};

export const WaveCancel: React.FC<WaveCancelProps> = ({
  phase, noiseLabel, antiLabel, sumLabel, highLabel, lowLabel, mismatchGain, mismatchPhase, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));
  const shift = frame * 0.07;                 // the wave travels
  const K = 0.0105;                           // ~2.3 cycles across the row
  const noise = (t: number) => Math.sin(t);
  const anti = (t: number) => -mismatchGain * Math.sin(t + mismatchPhase);
  const sum = (t: number) => noise(t) + anti(t);

  const spark = (
    <div style={{ position: 'absolute', left: SAFE.x, top: 930, width: SAFE.w, display: 'flex',
      alignItems: 'center', gap: 14, fontFamily: SERIF, fontSize: 54, color: CLAUDE.INK,
      opacity: ramp(p, 0.04, 0.16) }}>
      <span style={{ color: CLAUDE.SPARK, fontSize: 58 }}>✻</span><span>{sparkLine}</span>
    </div>
  );

  if (phase === 'pressure') {
    const draw = ramp(p, 0.05, 0.35);
    const labels = ramp(p, 0.4, 0.55);
    const X0 = 200, X1 = 1720, CY = 480, A = 190;
    // first crest/trough x positions for the labels
    const crestX = X0 + ((Math.PI / 2 - (shift % (2 * Math.PI)) + 4 * Math.PI) % (2 * Math.PI)) / K;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
        <div style={{ position: 'absolute', left: 140, top: 90, fontFamily: SANS, fontSize: 50,
          letterSpacing: 4, color: CLAUDE.INK, opacity: ramp(p, 0.02, 0.1) }}>SOUND IS AIR PRESSURE CHANGING</div>
        <svg width={1920} height={1080} style={{ position: 'absolute', inset: 0 }}>
          <line x1={X0} y1={CY} x2={X1} y2={CY} stroke={CLAUDE.BORDER} strokeWidth={3} strokeDasharray="10 10" />
          <path d={wavePath(X0, X1, CY, A, K, shift, noise)} fill="none" stroke={CLAUDE.INK} strokeWidth={7}
                pathLength={1} strokeDasharray={1} strokeDashoffset={1 - draw} />
        </svg>
        <div style={{ position: 'absolute', left: Math.min(crestX, X1 - 380) - 20, top: CY - A - 90,
          fontFamily: SANS, fontSize: 46, color: CLAUDE.INK_SOFT, opacity: labels }}>▲ {highLabel}</div>
        <div style={{ position: 'absolute', left: Math.min(crestX + Math.PI / K, X1 - 380) - 20, top: CY + A + 30,
          fontFamily: SANS, fontSize: 46, color: CLAUDE.INK_SOFT, opacity: labels }}>▼ {lowLabel}</div>
        {spark}
      </AbsoluteFill>
    );
  }

  // ── cancel: noise, opposite, computed sum ────────────────────────────────
  const rows = [
    { y: 220, label: noiseLabel, f: noise, stroke: CLAUDE.INK, a: ramp(p, 0.04, 0.24) },
    { y: 470, label: antiLabel, f: anti, stroke: CLAUDE.SPARK, a: ramp(p, 0.28, 0.48) },
    { y: 720, label: sumLabel, f: sum, stroke: CLAUDE.INK, a: ramp(p, 0.55, 0.75) },
  ];
  const X0 = 520, X1 = 1780, A = 95;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <svg width={1920} height={1080} style={{ position: 'absolute', inset: 0 }}>
        {rows.map((r, i) => (
          <g key={i}>
            <line x1={X0} y1={r.y} x2={X1} y2={r.y} stroke={CLAUDE.BORDER} strokeWidth={3} strokeDasharray="10 10" />
            <path d={wavePath(X0, X1, r.y, A, K, shift, r.f)} fill="none" stroke={r.stroke} strokeWidth={6}
                  pathLength={1} strokeDasharray={1} strokeDashoffset={1 - r.a} />
          </g>
        ))}
        {/* plus / equals marks between rows */}
        <text x={X0 - 70} y={350} fontFamily={SANS} fontSize={64} fill={CLAUDE.INK} opacity={rows[1].a}>+</text>
        <text x={X0 - 70} y={600} fontFamily={SANS} fontSize={64} fill={CLAUDE.INK} opacity={rows[2].a}>=</text>
      </svg>
      {rows.map((r, i) => (
        <div key={i} style={{ position: 'absolute', left: 140, top: r.y - 32, width: 300,
          fontFamily: SANS, fontSize: 44, letterSpacing: 2, color: CLAUDE.INK, opacity: 0.3 + r.a * 0.7 }}>{r.label}</div>
      ))}
      {spark}
    </AbsoluteFill>
  );
};
