import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE916 } from '../tokens/layout';
import { waveCancelSchema, wavePath } from './WaveCancel';

/**
 * WaveCancel916 — native portrait (1080×1920), NOT a crop.
 * Reflow R4 (serialize): each wave gets a full-width row with its label above;
 * the computed sum keeps the same small mismatch as the landscape scene.
 */

export const waveCancel916Schema = waveCancelSchema;
export type WaveCancel916Props = z.infer<typeof waveCancel916Schema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

export const WaveCancel916: React.FC<WaveCancel916Props> = ({
  phase, noiseLabel, antiLabel, sumLabel, highLabel, lowLabel, mismatchGain, mismatchPhase, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));
  const shift = frame * 0.07, K = 0.0125;
  const noise = (t: number) => Math.sin(t);
  const anti = (t: number) => -mismatchGain * Math.sin(t + mismatchPhase);
  const sum = (t: number) => noise(t) + anti(t);
  const X0 = 90, X1 = 990;

  const spark = (
    <div style={{ position: 'absolute', left: SAFE916.x, top: 1680, width: SAFE916.w, display: 'flex',
      alignItems: 'center', gap: 16, fontFamily: SERIF, fontSize: 68, color: CLAUDE.INK, opacity: ramp(p, 0.04, 0.16) }}>
      <span style={{ color: CLAUDE.SPARK, fontSize: 72 }}>✻</span><span>{sparkLine}</span>
    </div>
  );

  if (phase === 'pressure') {
    const draw = ramp(p, 0.05, 0.35), labels = ramp(p, 0.4, 0.55), CY = 860, A = 230;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
        <div style={{ position: 'absolute', left: SAFE916.x, top: 180, width: SAFE916.w, fontFamily: SANS,
          fontSize: 62, lineHeight: 1.2, letterSpacing: 3, color: CLAUDE.INK, opacity: ramp(p, 0.02, 0.1) }}>
          SOUND IS AIR PRESSURE CHANGING</div>
        <div style={{ position: 'absolute', left: SAFE916.x, top: CY - A - 150, fontFamily: SANS, fontSize: 58,
          color: CLAUDE.INK_SOFT, opacity: labels }}>▲ {highLabel}</div>
        <svg width={1080} height={1920} style={{ position: 'absolute', inset: 0 }}>
          <line x1={X0} y1={CY} x2={X1} y2={CY} stroke={CLAUDE.BORDER} strokeWidth={4} strokeDasharray="12 12" />
          <path d={wavePath(X0, X1, CY, A, K, shift, noise)} fill="none" stroke={CLAUDE.INK} strokeWidth={9}
                pathLength={1} strokeDasharray={1} strokeDashoffset={1 - draw} />
        </svg>
        <div style={{ position: 'absolute', left: SAFE916.x, top: CY + A + 80, fontFamily: SANS, fontSize: 58,
          color: CLAUDE.INK_SOFT, opacity: labels }}>▼ {lowLabel}</div>
        {spark}
      </AbsoluteFill>
    );
  }

  const rows = [
    { y: 420, label: noiseLabel, f: noise, stroke: CLAUDE.INK, a: ramp(p, 0.04, 0.24) },
    { y: 860, label: antiLabel, f: anti, stroke: CLAUDE.SPARK, a: ramp(p, 0.28, 0.48) },
    { y: 1300, label: sumLabel, f: sum, stroke: CLAUDE.INK, a: ramp(p, 0.55, 0.75) },
  ];
  const A = 120;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      {rows.map((r, i) => (
        <div key={i} style={{ position: 'absolute', left: SAFE916.x, top: r.y - A - 110, fontFamily: SANS,
          fontSize: 58, letterSpacing: 2, color: CLAUDE.INK, opacity: 0.3 + r.a * 0.7 }}>
          {i === 1 ? '+ ' : i === 2 ? '= ' : ''}{r.label}</div>
      ))}
      <svg width={1080} height={1920} style={{ position: 'absolute', inset: 0 }}>
        {rows.map((r, i) => (
          <g key={i}>
            <line x1={X0} y1={r.y} x2={X1} y2={r.y} stroke={CLAUDE.BORDER} strokeWidth={4} strokeDasharray="12 12" />
            <path d={wavePath(X0, X1, r.y, A, K, shift, r.f)} fill="none" stroke={r.stroke} strokeWidth={8}
                  pathLength={1} strokeDasharray={1} strokeDashoffset={1 - r.a} />
          </g>
        ))}
      </svg>
      {spark}
    </AbsoluteFill>
  );
};
