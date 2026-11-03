import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE916 } from '../tokens/layout';
import { researchCardsSchema } from './ResearchCards';

/**
 * ResearchCards916 — native portrait (1080×1920), NOT a crop.
 * Reflow R4 (serialize): the three side-by-side cards stack vertically as
 * full-width rows, so each idea gets a readable line length on a phone.
 */

export const researchCards916Schema = researchCardsSchema;
export type ResearchCards916Props = z.infer<typeof researchCards916Schema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

export const ResearchCards916: React.FC<ResearchCards916Props> = ({ cards, sparkLine }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));

  const X = 70, W = 940, H = 420, GAP = 48, TOP = 190;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      {cards.map((c, i) => {
        const a = ramp(p, 0.06 + i * 0.2, 0.2 + i * 0.2);
        return (
          <div key={c.name} style={{
            position: 'absolute', left: X, top: TOP + i * (H + GAP), width: W, height: H,
            border: `4px solid ${CLAUDE.INK}`, borderRadius: 18, background: CLAUDE.CARD,
            padding: '40px 44px', boxSizing: 'border-box',
            display: 'flex', flexDirection: 'column', gap: 20,
            opacity: a, transform: `translateY(${(1 - a) * 18}px)`,
          }}>
            <div style={{ fontFamily: SANS, fontSize: 66, lineHeight: 1.1, color: CLAUDE.INK }}>
              {c.name}
            </div>
            <div style={{ fontFamily: SERIF, fontSize: 62, lineHeight: 1.2, color: CLAUDE.INK, flex: 1 }}>
              {c.idea}
            </div>
            <div style={{ fontFamily: SANS, fontSize: 56, color: CLAUDE.INK_SOFT }}>
              {c.cite}
            </div>
          </div>
        );
      })}

      <div style={{
        position: 'absolute', left: SAFE916.x, top: 1680, width: SAFE916.w,
        display: 'flex', alignItems: 'center', gap: 16,
        fontFamily: SERIF, fontSize: 68, color: CLAUDE.INK,
        opacity: ramp(p, 0.04, 0.16),
      }}>
        <span style={{ color: CLAUDE.SPARK, fontSize: 72 }}>✻</span>
        <span>{sparkLine}</span>
      </div>
    </AbsoluteFill>
  );
};
