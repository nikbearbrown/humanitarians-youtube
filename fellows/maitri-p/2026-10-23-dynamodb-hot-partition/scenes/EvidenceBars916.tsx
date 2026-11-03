import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE916 } from '../tokens/layout';
import { evidenceBarsSchema } from './EvidenceBars';

/**
 * EvidenceBars916 — native portrait (1080×1920), NOT a crop.
 * Reflow R4 (serialize): each condition's label sits above its own full-width
 * bar, so labels and values stay large on a phone.
 */

export const evidenceBars916Schema = evidenceBarsSchema;
export type EvidenceBars916Props = z.infer<typeof evidenceBars916Schema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

export const EvidenceBars916: React.FC<EvidenceBars916Props> = ({
  title, note, bars, accentIndex, caption, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));

  const max = Math.max(...bars.map(b => b.value), 1e-9);
  // BAR_MAX leaves ~300px after the longest bar for a value label like "10,000 / s"
  // so it stays inside SAFE916 (right edge 1026).
  const X = 70, BAR_MAX = 600, ROW = 230, TOP = 470;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <div style={{ position: 'absolute', left: SAFE916.x, top: 150, width: SAFE916.w,
        fontFamily: SANS, fontSize: 66, lineHeight: 1.15, color: CLAUDE.INK, opacity: ramp(p, 0.02, 0.1) }}>{title}</div>
      <div style={{ position: 'absolute', left: SAFE916.x, top: 330, width: SAFE916.w,
        fontFamily: SANS, fontSize: 54, color: CLAUDE.INK_SOFT, opacity: ramp(p, 0.04, 0.12) }}>{note}</div>

      {bars.map((b, i) => {
        const a = ramp(p, 0.1 + i * 0.12, 0.26 + i * 0.12);
        const y = TOP + i * ROW;
        const w = (b.value / max) * BAR_MAX * a;
        const accent = i === accentIndex;
        return (
          <React.Fragment key={b.label}>
            <div style={{ position: 'absolute', left: X, top: y, fontFamily: SANS, fontSize: 58,
              color: CLAUDE.INK, opacity: 0.35 + a * 0.65 }}>{b.label}</div>
            <div style={{ position: 'absolute', left: X, top: y + 86, width: w, height: 96,
              borderRadius: 10, background: accent ? CLAUDE.SPARK : CLAUDE.GHOST }} />
            <div style={{ position: 'absolute', left: X + w + 24, top: y + 86, height: 96,
              display: 'flex', alignItems: 'center',
              fontFamily: SANS, fontSize: 62, color: CLAUDE.INK, opacity: a }}>
              {b.display ?? String(b.value)}
            </div>
          </React.Fragment>
        );
      })}

      <div style={{ position: 'absolute', left: SAFE916.x, top: 1420, width: SAFE916.w,
        fontFamily: SANS, fontSize: 52, lineHeight: 1.25, color: CLAUDE.INK_SOFT,
        opacity: ramp(p, 0.64, 0.76) }}>{caption}</div>

      <div style={{ position: 'absolute', left: SAFE916.x, top: 1680, width: SAFE916.w,
        display: 'flex', alignItems: 'center', gap: 16,
        fontFamily: SERIF, fontSize: 68, color: CLAUDE.INK, opacity: ramp(p, 0.04, 0.16) }}>
        <span style={{ color: CLAUDE.SPARK, fontSize: 72 }}>✻</span><span>{sparkLine}</span>
      </div>
    </AbsoluteFill>
  );
};
