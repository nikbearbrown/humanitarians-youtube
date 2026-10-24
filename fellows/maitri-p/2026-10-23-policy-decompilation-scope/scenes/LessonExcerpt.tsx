import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE } from '../tokens/layout';

/**
 * LessonExcerpt — a stored memory shown in its own structure (e.g. WHEN / DO /
 * INSTEAD OF), revealed row by row. Text must be verbatim fragments of the
 * source lesson; the header labels it as an excerpt. A terracotta left rule
 * marks the one emphasised row (structural, not text colour — §8.3-safe).
 */

export const lessonExcerptSchema = z.object({
  header:    z.string().default('Lesson excerpt'),
  subheader: z.string().default(''),
  rows: z.array(z.object({ tag: z.string(), text: z.string(), emphasis: z.boolean().optional() }))
          .max(4).default([]),
  footer:    z.string().default(''),
  sparkLine: z.string().default(''),
  durationSeconds: z.number().optional(),
});
export type LessonExcerptProps = z.infer<typeof lessonExcerptSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

export const LessonExcerpt: React.FC<LessonExcerptProps> = ({ header, subheader, rows, footer, sparkLine }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <div style={{ position: 'absolute', left: 140, top: 90, display: 'flex', gap: 22, alignItems: 'baseline',
        opacity: ramp(p, 0.02, 0.12) }}>
        <span style={{ fontFamily: SANS, fontSize: 50, letterSpacing: 4, color: CLAUDE.INK }}>{header.toUpperCase()}</span>
        <span style={{ fontFamily: SANS, fontSize: 46, color: CLAUDE.INK_SOFT }}>{subheader}</span>
      </div>

      <div style={{ position: 'absolute', left: 140, top: 220, width: 1640,
        display: 'flex', flexDirection: 'column', gap: 52 }}>
        {rows.map((r, i) => {
          const a = ramp(p, 0.12 + i * 0.2, 0.26 + i * 0.2);
          return (
            <div key={r.tag} style={{ display: 'flex', gap: 40, alignItems: 'baseline',
              borderLeft: r.emphasis ? `8px solid ${CLAUDE.SPARK}` : '8px solid transparent',
              paddingLeft: 28, opacity: a, transform: `translateY(${(1 - a) * 14}px)` }}>
              <div style={{ width: 380, flexShrink: 0, fontFamily: SANS, fontSize: 46,
                letterSpacing: 3, color: CLAUDE.INK_SOFT }}>{r.tag}</div>
              <div style={{ fontFamily: SERIF, fontSize: 58, lineHeight: 1.25, color: CLAUDE.INK }}>{r.text}</div>
            </div>
          );
        })}
      </div>

      <div style={{ position: 'absolute', left: 140, top: 820, width: 1640,
        fontFamily: SANS, fontSize: 44, color: CLAUDE.INK_SOFT, opacity: ramp(p, 0.72, 0.84) }}>{footer}</div>

      <div style={{ position: 'absolute', left: SAFE.x, top: 920, width: SAFE.w,
        display: 'flex', alignItems: 'center', gap: 14,
        fontFamily: SERIF, fontSize: 54, color: CLAUDE.INK, opacity: ramp(p, 0.04, 0.16) }}>
        <span style={{ color: CLAUDE.SPARK, fontSize: 58 }}>✻</span><span>{sparkLine}</span>
      </div>
    </AbsoluteFill>
  );
};
