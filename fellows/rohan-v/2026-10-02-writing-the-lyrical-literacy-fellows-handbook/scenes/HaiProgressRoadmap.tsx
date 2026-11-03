import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * HaiProgressRoadmap — B04 of "Unblocking the Team." (HAI weekly progress)
 *
 * The week as a timeline with a NOW marker: solid ink cards to the left are
 * shipped, dashed terracotta cards to the right are committed-but-not-done,
 * each carrying its own due chip. The spine draws left to right and the NOW
 * pin drops last, so the split reads as a claim about time rather than a list.
 *
 * Reusable as the closing beat of any weekly-progress reel. Duration-agnostic.
 */

export const haiProgressRoadmapSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · WEEKLY PROGRESS'),
  title: z.string().default('Shipped, and What Is Next'),
  shipped: z.array(z.object({ label: z.string(), sub: z.string() })).default([
    { label: 'Suno series, parts 1–3', sub: '10:35 of 4K training material' },
    { label: 'GitHub workshop', sub: 'marketing team unblocked' },
  ]),
  next: z.array(z.object({ label: z.string(), sub: z.string(), due: z.string() })).default([
    { label: 'Midjourney series', sub: 'same approach, interface rebuilt in code', due: 'END OF NEXT WEEK' },
    { label: 'Signup documentation', sub: 'Discord, Suno, Midjourney, Adobe CC', due: 'IN PROGRESS' },
  ]),
  sparkLine: z.string().default('Same approach, pointed at the next tool.'),
  /** Opt-in (portrait only, week-06): the 9:16 type spec's phone scale (title 5.0vh, card
   *  label 4.0vh, small labels >= 2.3vh), eyebrow dropped, layout spread to y 21–76%.
   *  Needs short strings. Absent = the original portrait layout, so earlier reels render unchanged. */
  phoneType: z.boolean().optional(),
});
export type HaiProgressRoadmapProps = z.infer<typeof haiProgressRoadmapSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
const SPRING = { damping: 26, stiffness: 105, mass: 0.9 };

export const HaiProgressRoadmap: React.FC<HaiProgressRoadmapProps> = ({
  eyebrow, title, shipped, next, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const PAD_X = width * 0.065;
  const op = (s: number) => clamp(s, 0, 1);

  const titleIn = spring({ frame, fps, config: SPRING });
  const pinIn = spring({ frame: frame - 92, fps, config: SPRING });
  const sparkIn = spring({ frame: frame - 132, fps, config: SPRING });

  const CONTENT_W = width - PAD_X * 2;
  const MID = width * 0.5;

  // Spine
  const SPINE_Y = height * 0.335;
  const spine = interpolate(frame, [14, 78], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });

  // Two columns, split at the NOW pin
  const COL_GAP = 74;
  const COL_W = (CONTENT_W - COL_GAP) / 2;
  const CARD_H = 152;
  const CARD_GAP = 26;
  const CARDS_TOP = height * 0.435;

  const colHead = (label: string, x: number, tint: string, delay: number) => (
    <div style={{
      position: 'absolute', left: x, top: height * 0.375, width: COL_W,
      fontFamily: SANS, fontSize: height * 0.0135, fontWeight: 700,
      letterSpacing: 2.5, textTransform: 'uppercase' as const,
      color: tint,
      opacity: op(spring({ frame: frame - delay, fps, config: SPRING })) * 0.95,
    }}>
      {label}
    </div>
  );

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>

      {/* Eyebrow */}
      <div style={{
        position: 'absolute', left: PAD_X, top: height * 0.095,
        fontFamily: SANS, fontSize: height * 0.0145, fontWeight: 700,
        letterSpacing: 3, textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT, opacity: op(titleIn) * 0.8,
      }}>
        {eyebrow}
      </div>

      {/* Title */}
      <div style={{
        position: 'absolute', left: PAD_X, top: height * 0.145,
        fontFamily: SERIF, fontSize: height * 0.042, fontWeight: 600,
        color: CLAUDE.INK, letterSpacing: '-0.01em',
        opacity: op(titleIn), transform: `translateY(${(1 - op(titleIn)) * 10}px)`,
      }}>
        {title}
      </div>

      {/* Spine — solid to the pin, dashed past it */}
      <div style={{
        position: 'absolute',
        left: PAD_X, top: SPINE_Y - 1.5,
        width: (MID - PAD_X) * clamp(spine / 0.5, 0, 1), height: 3,
        background: CLAUDE.INK, opacity: 0.85,
      }} />
      <div style={{
        position: 'absolute',
        left: MID, top: SPINE_Y - 1.5,
        width: (width - PAD_X - MID) * clamp((spine - 0.5) / 0.5, 0, 1), height: 3,
        borderTop: `3px dashed ${CLAUDE.SPARK}`,
        opacity: 0.9,
      }} />

      {/* NOW pin */}
      <div style={{
        position: 'absolute',
        left: MID - 9, top: SPINE_Y - 9,
        width: 18, height: 18, borderRadius: 999,
        background: CLAUDE.SPARK,
        boxShadow: `0 0 0 7px ${CLAUDE.PAGE}, 0 0 0 9px ${CLAUDE.SPARK}40`,
        opacity: op(pinIn), transform: `scale(${0.6 + op(pinIn) * 0.4})`,
      }} />
      <div style={{
        position: 'absolute',
        left: MID - 60, top: SPINE_Y - 52,
        width: 120, textAlign: 'center' as const,
        fontFamily: SANS, fontSize: 16, fontWeight: 700, letterSpacing: 3,
        color: CLAUDE.SPARK, opacity: op(pinIn),
      }}>
        NOW
      </div>

      {colHead('SHIPPED THIS WEEK', PAD_X, CLAUDE.INK_SOFT, 30)}
      {colHead('COMMITTED NEXT', MID + COL_GAP / 2, CLAUDE.SPARK, 100)}

      {/* Shipped cards — solid */}
      {shipped.map((s, i) => {
        const cardIn = spring({ frame: frame - (34 + i * 18), fps, config: SPRING });
        return (
          <div key={i} style={{
            position: 'absolute',
            left: PAD_X, top: CARDS_TOP + i * (CARD_H + CARD_GAP),
            width: COL_W, height: CARD_H,
            background: CLAUDE.CARD,
            border: `1px solid ${CLAUDE.BORDER}`,
            borderRadius: 16,
            boxShadow: '0 6px 24px rgba(61,57,41,0.07)',
            display: 'flex', alignItems: 'center', gap: 20,
            padding: '0 26px',
            opacity: op(cardIn),
            transform: `translateX(${(1 - op(cardIn)) * -22}px)`,
          }}>
            <div style={{
              width: 40, height: 40, borderRadius: 999,
              background: CLAUDE.INK, flexShrink: 0,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
            }}>
              <svg width="20" height="20" viewBox="0 0 18 18">
                <path
                  d="M3.5 9.5 L7 13 L14.5 5"
                  fill="none" stroke="#FFFFFF"
                  strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round"
                />
              </svg>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
              <div style={{
                fontFamily: SERIF, fontSize: 26, fontWeight: 600, color: CLAUDE.INK,
                letterSpacing: '-0.01em', lineHeight: 1.2,
              }}>
                {s.label}
              </div>
              <div style={{ fontFamily: SERIF, fontSize: 19, color: CLAUDE.INK_SOFT }}>
                {s.sub}
              </div>
            </div>
          </div>
        );
      })}

      {/* Next cards — dashed */}
      {next.map((n, i) => {
        const cardIn = spring({ frame: frame - (106 + i * 18), fps, config: SPRING });
        return (
          <div key={i} style={{
            position: 'absolute',
            left: MID + COL_GAP / 2, top: CARDS_TOP + i * (CARD_H + CARD_GAP),
            width: COL_W, height: CARD_H,
            background: '#FFF8F5',
            border: `2px dashed ${CLAUDE.SPARK}`,
            borderRadius: 16,
            display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: 8,
            padding: '0 26px',
            opacity: op(cardIn),
            transform: `translateX(${(1 - op(cardIn)) * 22}px)`,
          }}>
            <div style={{
              fontFamily: SERIF, fontSize: 26, fontWeight: 600, color: CLAUDE.INK,
              letterSpacing: '-0.01em', lineHeight: 1.2,
            }}>
              {n.label}
            </div>
            <div style={{ fontFamily: SERIF, fontSize: 19, color: CLAUDE.INK_SOFT }}>
              {n.sub}
            </div>
            <div style={{
              fontFamily: SANS, fontSize: 13, fontWeight: 700, letterSpacing: 1.8,
              color: CLAUDE.SPARK, border: `1px solid ${CLAUDE.SPARK}`,
              borderRadius: 5, padding: '4px 9px', alignSelf: 'flex-start' as const,
              marginTop: 2,
            }}>
              {n.due}
            </div>
          </div>
        );
      })}

      {/* Spark line */}
      <div style={{
        position: 'absolute', left: PAD_X, right: PAD_X, bottom: height * 0.075,
        display: 'flex', alignItems: 'center', gap: 14,
        opacity: op(sparkIn),
      }}>
        <div style={{ width: width * 0.055, height: 2, background: CLAUDE.SPARK, flexShrink: 0 }} />
        <span style={{
          fontFamily: SERIF, fontSize: height * 0.026, fontStyle: 'italic', color: CLAUDE.INK,
        }}>
          {sparkLine}
        </span>
      </div>
    </AbsoluteFill>
  );
};
