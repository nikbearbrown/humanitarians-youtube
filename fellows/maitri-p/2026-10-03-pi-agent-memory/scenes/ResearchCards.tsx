import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE } from '../tokens/layout';

/**
 * ResearchCards — up to three prior-work cards (name · one-line idea · citation),
 * revealed in narration order. Rebuilt typography, never screenshots of papers.
 * All text INK / INK_SOFT on cream; terracotta only on the spark (§8.3-safe).
 * Type sized for the §8.1 floor (>= 44px design → >= 41px ink at 2160).
 * Every cue lands by ~70% of the beat.
 */

export const researchCardsSchema = z.object({
  cards: z.array(z.object({
    name: z.string(),
    idea: z.string(),
    cite: z.string(),
  })).max(3).default([]),
  sparkLine: z.string().default('Built on prior work.'),
  durationSeconds: z.number().optional(),
});
export type ResearchCardsProps = z.infer<typeof researchCardsSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

export const ResearchCards: React.FC<ResearchCardsProps> = ({ cards, sparkLine }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));

  const W = 520, H = 580, GAP = 64;
  const n = Math.max(1, cards.length);
  const startX = (1920 - (n * W + (n - 1) * GAP)) / 2;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      {cards.map((c, i) => {
        const a = ramp(p, 0.06 + i * 0.2, 0.2 + i * 0.2);
        return (
          <div key={c.name} style={{
            position: 'absolute', left: startX + i * (W + GAP), top: 170, width: W, height: H,
            border: `3px solid ${CLAUDE.INK}`, borderRadius: 16, background: CLAUDE.CARD,
            padding: '44px 40px', boxSizing: 'border-box',
            display: 'flex', flexDirection: 'column', gap: 28,
            opacity: a, transform: `translateY(${(1 - a) * 18}px)`,
          }}>
            <div style={{ fontFamily: SANS, fontSize: 50, lineHeight: 1.12, color: CLAUDE.INK }}>
              {c.name}
            </div>
            <div style={{ fontFamily: SERIF, fontSize: 50, lineHeight: 1.22, color: CLAUDE.INK, flex: 1 }}>
              {c.idea}
            </div>
            <div style={{ fontFamily: SANS, fontSize: 44, color: CLAUDE.INK_SOFT }}>
              {c.cite}
            </div>
          </div>
        );
      })}

      <div style={{
        position: 'absolute', left: SAFE.x, top: 900, width: SAFE.w,
        display: 'flex', alignItems: 'center', gap: 14,
        fontFamily: SERIF, fontSize: 54, color: CLAUDE.INK,
        opacity: ramp(p, 0.04, 0.16),
      }}>
        <span style={{ color: CLAUDE.SPARK, fontSize: 58 }}>✻</span>
        <span>{sparkLine}</span>
      </div>
    </AbsoluteFill>
  );
};
