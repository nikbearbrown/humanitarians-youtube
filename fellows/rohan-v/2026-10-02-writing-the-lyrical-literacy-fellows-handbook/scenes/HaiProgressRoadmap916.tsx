import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { haiProgressRoadmapSchema } from './HaiProgressRoadmap';
import type { HaiProgressRoadmapProps } from './HaiProgressRoadmap';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * HaiProgressRoadmap916 — portrait 9:16 (1080×1920) version.
 * Same schema, same logic, re-laid-out per THE ONDA CHECK — never a crop.
 *
 * Landscape splits shipped/next left-to-right across a horizontal spine.
 * Portrait rotates the spine vertical: it runs down the left gutter, solid ink
 * through the shipped cards at the top, dashed terracotta through the committed
 * cards below, with the NOW pin dropping on the boundary between them. Reading
 * top-to-bottom is reading forward in time.
 *
 * Safe zone: top 12% / bottom 25% reserved. Active band y 230–1440.
 * With `phoneType` (opt-in, week-06) the PHONE type scale applies and the layout spreads to y 21–80%.
 */

export const haiProgressRoadmap916Schema = haiProgressRoadmapSchema;
export type HaiProgressRoadmap916Props = HaiProgressRoadmapProps;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
const SPRING = { damping: 26, stiffness: 105, mass: 0.9 };

export const HaiProgressRoadmap916: React.FC<HaiProgressRoadmap916Props> = ({
  eyebrow, title, shipped, next, sparkLine, phoneType,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const PAD_X = width * 0.067;
  const op = (s: number) => clamp(s, 0, 1);

  const titleIn = spring({ frame, fps, config: SPRING });
  const pinIn = spring({ frame: frame - 88, fps, config: SPRING });
  const sparkIn = spring({ frame: frame - 126, fps, config: SPRING });

  // Spine runs down a left gutter; cards sit to its right
  const SPINE_X = PAD_X + width * 0.026;
  const CARD_X = SPINE_X + width * 0.055;
  const CARD_W = width - CARD_X - PAD_X;
  // phoneType: kerning/reference/type-spec.md §1 as numbers (cueKit PHONE), spread to fill.
  const PH = phoneType;
  const fTitle = PH ? height * 0.050 : height * 0.032;
  const fLabel = PH ? height * 0.042 : height * 0.0208;
  const fSub = PH ? height * 0.042 : height * 0.0146;
  const fSmall = PH ? height * 0.031 : height * 0.0125;
  const fDue = PH ? height * 0.031 : height * 0.0094;
  const CARD_H = PH ? height * 0.098 : height * 0.0885;           // ~170px
  const NEXT_CARD_H = PH ? height * 0.105 : CARD_H;
  const CARD_GAP = height * 0.0115;         // ~22px

  const SHIP_LABEL_Y = PH ? height * 0.195 : height * 0.203;      // ~390
  const SHIP_TOP = PH ? height * 0.232 : height * 0.222;          // ~426
  const shipH = CARD_H * shipped.length + CARD_GAP * (shipped.length - 1);

  const PIN_Y = SHIP_TOP + shipH + height * (PH ? 0.024 : 0.026);
  const NEXT_LABEL_Y = PIN_Y + height * (PH ? 0.026 : 0.020);
  const NEXT_TOP = PIN_Y + height * (PH ? 0.072 : 0.043);
  const nextH = NEXT_CARD_H * next.length + CARD_GAP * (next.length - 1);

  const SPINE_TOP = SHIP_TOP - height * 0.014;
  const SPINE_BOT = NEXT_TOP + nextH + height * 0.010;

  const SPARK_Y = PH ? height * 0.79 : height * 0.706;

  const spine = interpolate(frame, [14, 76], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>

      {/* Eyebrow */}
      <div style={{
        position: 'absolute', left: PAD_X, top: height * 0.125,
        fontFamily: SANS, fontSize: height * 0.0135, fontWeight: 700,
        letterSpacing: 3, textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT, opacity: op(titleIn) * 0.8,
        display: PH ? 'none' : 'block',
      }}>
        {eyebrow}
      </div>

      {/* Title */}
      <div style={{
        position: 'absolute', left: PAD_X, top: PH ? height * 0.125 : height * 0.148,
        width: width - PAD_X * 2,
        fontFamily: SERIF, fontSize: fTitle, fontWeight: 600,
        color: CLAUDE.INK, letterSpacing: '-0.015em', lineHeight: 1.1,
        opacity: op(titleIn), transform: `translateY(${(1 - op(titleIn)) * 10}px)`,
      }}>
        {title}
      </div>

      {/* Spine — solid down to the pin */}
      <div style={{
        position: 'absolute',
        left: SPINE_X - 1.5, top: SPINE_TOP,
        width: 3,
        height: (PIN_Y - SPINE_TOP) * clamp(spine / 0.5, 0, 1),
        background: CLAUDE.INK, opacity: 0.85,
      }} />

      {/* Spine — dashed past the pin */}
      <div style={{
        position: 'absolute',
        left: SPINE_X - 1.5, top: PIN_Y,
        width: 3,
        height: (SPINE_BOT - PIN_Y) * clamp((spine - 0.5) / 0.5, 0, 1),
        borderLeft: `3px dashed ${CLAUDE.SPARK}`,
        opacity: 0.9,
      }} />

      {/* NOW pin */}
      <div style={{
        position: 'absolute',
        left: SPINE_X - height * 0.0057, top: PIN_Y - height * 0.0057,
        width: height * 0.0114, height: height * 0.0114, borderRadius: 999,
        background: CLAUDE.SPARK,
        boxShadow: `0 0 0 ${height * 0.0042}px ${CLAUDE.PAGE}, 0 0 0 ${height * 0.0057}px ${CLAUDE.SPARK}40`,
        opacity: op(pinIn), transform: `scale(${0.6 + op(pinIn) * 0.4})`,
      }} />
      <div style={{
        position: 'absolute',
        left: CARD_X, top: PIN_Y - height * 0.011,
        fontFamily: SANS, fontSize: PH ? fSmall : height * 0.0146, fontWeight: 700,
        letterSpacing: 3.4, color: CLAUDE.SPARK, opacity: op(pinIn),
      }}>
        NOW
      </div>

      {/* Column labels */}
      <div style={{
        position: 'absolute', left: CARD_X, top: SHIP_LABEL_Y,
        fontFamily: SANS, fontSize: fSmall, fontWeight: 700,
        letterSpacing: 2.5, textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT,
        opacity: op(spring({ frame: frame - 26, fps, config: SPRING })) * 0.95,
      }}>
        SHIPPED THIS WEEK
      </div>
      <div style={{
        position: 'absolute', left: CARD_X, top: NEXT_LABEL_Y,
        fontFamily: SANS, fontSize: fSmall, fontWeight: 700,
        letterSpacing: 2.5, textTransform: 'uppercase' as const,
        color: CLAUDE.SPARK,
        opacity: op(spring({ frame: frame - 96, fps, config: SPRING })) * 0.95,
      }}>
        COMMITTED NEXT
      </div>

      {/* Shipped cards — solid */}
      {shipped.map((s, i) => {
        const cardIn = spring({ frame: frame - (32 + i * 16), fps, config: SPRING });
        return (
          <div key={`s${i}`} style={{
            position: 'absolute',
            left: CARD_X, top: SHIP_TOP + i * (CARD_H + CARD_GAP),
            width: CARD_W, height: CARD_H,
            background: CLAUDE.CARD,
            border: `1px solid ${CLAUDE.BORDER}`,
            borderRadius: 18,
            boxShadow: '0 6px 24px rgba(61,57,41,0.07)',
            display: 'flex', alignItems: 'center', gap: width * 0.024,
            padding: `0 ${width * 0.026}px`,
            opacity: op(cardIn),
            transform: `translateX(${(1 - op(cardIn)) * -18}px)`,
          }}>
            <div style={{
              width: height * 0.0245, height: height * 0.0245, borderRadius: 999,
              background: CLAUDE.INK, flexShrink: 0,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
            }}>
              <svg width={height * 0.0135} height={height * 0.0135} viewBox="0 0 18 18">
                <path
                  d="M3.5 9.5 L7 13 L14.5 5"
                  fill="none" stroke="#FFFFFF"
                  strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round"
                />
              </svg>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: height * 0.0037 }}>
              <div style={{
                fontFamily: SERIF, fontSize: fLabel, fontWeight: 600,
                color: CLAUDE.INK, letterSpacing: '-0.01em', lineHeight: 1.15, whiteSpace: PH ? 'nowrap' : undefined,
              }}>
                {s.label}
              </div>
              <div style={{
                fontFamily: SERIF, fontSize: fSub, color: CLAUDE.INK_SOFT,
              }}>
                {s.sub}
              </div>
            </div>
          </div>
        );
      })}

      {/* Next cards — dashed */}
      {next.map((n, i) => {
        const cardIn = spring({ frame: frame - (102 + i * 16), fps, config: SPRING });
        return (
          <div key={`n${i}`} style={{
            position: 'absolute',
            left: CARD_X, top: NEXT_TOP + i * (NEXT_CARD_H + CARD_GAP),
            width: CARD_W, height: NEXT_CARD_H,
            background: '#FFF8F5',
            border: `2px dashed ${CLAUDE.SPARK}`,
            borderRadius: 18,
            display: 'flex', flexDirection: 'column', justifyContent: 'center',
            gap: height * 0.0032,
            padding: `0 ${width * 0.026}px`,
            opacity: op(cardIn),
            transform: `translateX(${(1 - op(cardIn)) * 18}px)`,
          }}>
            <div style={{
              fontFamily: SERIF, fontSize: fLabel, fontWeight: 600,
              color: CLAUDE.INK, letterSpacing: '-0.01em', lineHeight: 1.15,
            }}>
              {n.label}
            </div>
            {PH ? null : (
              <div style={{
                fontFamily: SERIF, fontSize: fSub, color: CLAUDE.INK_SOFT,
                lineHeight: 1.3,
              }}>
                {n.sub}
              </div>
            )}
            <div style={{
              fontFamily: SANS, fontSize: fDue, fontWeight: 700,
              letterSpacing: 1.8, color: CLAUDE.SPARK,
              border: `1px solid ${CLAUDE.SPARK}`, borderRadius: 5,
              padding: `${height * 0.0021}px ${width * 0.011}px`,
              alignSelf: 'flex-start' as const, marginTop: height * 0.002,
            }}>
              {n.due}
            </div>
          </div>
        );
      })}

      {/* Spark line */}
      <div style={{
        position: 'absolute', left: PAD_X, top: SPARK_Y, width: width - PAD_X * 2,
        display: 'flex', alignItems: 'flex-start', gap: 16,
        opacity: op(sparkIn),
      }}>
        <div style={{
          width: width * 0.085, height: 3, background: CLAUDE.SPARK,
          flexShrink: 0, marginTop: height * 0.014,
        }} />
        <span style={{
          fontFamily: SERIF, fontSize: PH ? height * 0.034 : height * 0.0198, fontStyle: 'italic',
          color: CLAUDE.INK, lineHeight: 1.35,
        }}>
          {sparkLine}
        </span>
      </div>
    </AbsoluteFill>
  );
};
