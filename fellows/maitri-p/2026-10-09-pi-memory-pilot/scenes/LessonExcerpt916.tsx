import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE916 } from '../tokens/layout';
import { lessonExcerptSchema } from './LessonExcerpt';

/**
 * LessonExcerpt916 — native portrait (1080×1920), NOT a crop.
 * Reflow R4 (serialize): each tag sits ABOVE its text, giving the verbatim
 * lesson a full-width line on a phone.
 */

export const lessonExcerpt916Schema = lessonExcerptSchema;
export type LessonExcerpt916Props = z.infer<typeof lessonExcerpt916Schema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

export const LessonExcerpt916: React.FC<LessonExcerpt916Props> = ({ header, subheader, rows, footer, sparkLine }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <div style={{ position: 'absolute', left: SAFE916.x, top: 140, width: SAFE916.w, opacity: ramp(p, 0.02, 0.12) }}>
        <div style={{ fontFamily: SANS, fontSize: 60, letterSpacing: 5, color: CLAUDE.INK }}>{header.toUpperCase()}</div>
        <div style={{ fontFamily: SANS, fontSize: 54, color: CLAUDE.INK_SOFT, marginTop: 10 }}>{subheader}</div>
      </div>

      <div style={{ position: 'absolute', left: SAFE916.x, top: 400, width: SAFE916.w,
        display: 'flex', flexDirection: 'column', gap: 56 }}>
        {rows.map((r, i) => {
          const a = ramp(p, 0.12 + i * 0.2, 0.26 + i * 0.2);
          return (
            <div key={r.tag} style={{
              borderLeft: r.emphasis ? `10px solid ${CLAUDE.SPARK}` : '10px solid transparent',
              paddingLeft: 28, opacity: a, transform: `translateY(${(1 - a) * 14}px)` }}>
              <div style={{ fontFamily: SANS, fontSize: 52, letterSpacing: 3, color: CLAUDE.INK_SOFT }}>{r.tag}</div>
              <div style={{ fontFamily: SERIF, fontSize: 66, lineHeight: 1.22, color: CLAUDE.INK, marginTop: 8 }}>{r.text}</div>
            </div>
          );
        })}
      </div>

      <div style={{ position: 'absolute', left: SAFE916.x, top: 1460, width: SAFE916.w,
        fontFamily: SANS, fontSize: 50, lineHeight: 1.25, color: CLAUDE.INK_SOFT, opacity: ramp(p, 0.72, 0.84) }}>{footer}</div>

      <div style={{ position: 'absolute', left: SAFE916.x, top: 1680, width: SAFE916.w,
        display: 'flex', alignItems: 'center', gap: 16,
        fontFamily: SERIF, fontSize: 68, color: CLAUDE.INK, opacity: ramp(p, 0.04, 0.16) }}>
        <span style={{ color: CLAUDE.SPARK, fontSize: 72 }}>✻</span><span>{sparkLine}</span>
      </div>
    </AbsoluteFill>
  );
};
