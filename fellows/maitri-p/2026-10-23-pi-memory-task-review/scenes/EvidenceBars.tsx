import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE } from '../tokens/layout';

/**
 * EvidenceBars — recorded results as horizontal bars that grow to their value
 * in narration order. Built for honest small-sample evidence: a required
 * caption carries the sample size, and an axis note says which direction is
 * better. Only numbers from the source appear (REBUILD LAW).
 * Text is INK/INK_SOFT; terracotta fills the single accent bar only (§8.3-safe).
 */

export const evidenceBarsSchema = z.object({
  title:   z.string().default(''),
  note:    z.string().default(''),
  bars:    z.array(z.object({ label: z.string(), value: z.number(), display: z.string().optional() }))
             .min(1).max(6).default([]),
  accentIndex: z.number().int().default(-1),
  caption: z.string().default(''),
  sparkLine: z.string().default(''),
  durationSeconds: z.number().optional(),
});
export type EvidenceBarsProps = z.infer<typeof evidenceBarsSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

export const EvidenceBars: React.FC<EvidenceBarsProps> = ({
  title, note, bars, accentIndex, caption, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));

  const max = Math.max(...bars.map(b => b.value), 1e-9);
  const LABEL_W = 430, BAR_X = 140 + LABEL_W, BAR_MAX = 1000;
  const ROW_H = 104, ROW_GAP = 40, TOP = 260;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <div style={{ position: 'absolute', left: 140, top: 90, width: 1640,
        fontFamily: SANS, fontSize: 56, color: CLAUDE.INK, opacity: ramp(p, 0.02, 0.1) }}>{title}</div>
      <div style={{ position: 'absolute', left: 140, top: 170, width: 1640,
        fontFamily: SANS, fontSize: 44, color: CLAUDE.INK_SOFT, opacity: ramp(p, 0.04, 0.12) }}>{note}</div>

      {bars.map((b, i) => {
        const a = ramp(p, 0.1 + i * 0.12, 0.26 + i * 0.12);
        const y = TOP + i * (ROW_H + ROW_GAP);
        const w = (b.value / max) * BAR_MAX * a;
        const accent = i === accentIndex;
        return (
          <React.Fragment key={b.label}>
            <div style={{ position: 'absolute', left: 140, top: y, width: LABEL_W - 30, height: ROW_H,
              display: 'flex', alignItems: 'center',
              fontFamily: SANS, fontSize: 48, color: CLAUDE.INK, opacity: 0.35 + a * 0.65 }}>{b.label}</div>
            <div style={{ position: 'absolute', left: BAR_X, top: y + 14, width: w, height: ROW_H - 28,
              borderRadius: 8, background: accent ? CLAUDE.SPARK : CLAUDE.GHOST }} />
            <div style={{ position: 'absolute', left: BAR_X + w + 22, top: y, height: ROW_H,
              display: 'flex', alignItems: 'center',
              fontFamily: SANS, fontSize: 52, color: CLAUDE.INK, opacity: a }}>
              {b.display ?? String(b.value)}
            </div>
          </React.Fragment>
        );
      })}

      <div style={{ position: 'absolute', left: 140, top: 830, width: 1640,
        fontFamily: SANS, fontSize: 44, color: CLAUDE.INK_SOFT, opacity: ramp(p, 0.64, 0.76) }}>{caption}</div>

      <div style={{ position: 'absolute', left: SAFE.x, top: 920, width: SAFE.w,
        display: 'flex', alignItems: 'center', gap: 14,
        fontFamily: SERIF, fontSize: 54, color: CLAUDE.INK, opacity: ramp(p, 0.04, 0.16) }}>
        <span style={{ color: CLAUDE.SPARK, fontSize: 58 }}>✻</span><span>{sparkLine}</span>
      </div>
    </AbsoluteFill>
  );
};
