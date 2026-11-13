import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { haiProgressSignupChainSchema } from './HaiProgressSignupChain';
import type { HaiProgressSignupChainProps } from './HaiProgressSignupChain';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * HaiProgressSignupChain916 — portrait 9:16 (1080×1920) version.
 * Same schema, same logic, re-laid-out per THE ONDA CHECK — never a crop.
 *
 * Landscape runs the four tool cards left to right. Portrait stacks them down
 * the frame with the connector running vertically through their hue dots, which
 * reads more naturally as a sequence of steps. The documentation sheet still
 * slides in beneath and wraps the whole chain, stamped IN PROGRESS.
 *
 * Safe zone: top 12% / bottom 25% reserved. Active band y 230–1440.
 */

export const haiProgressSignupChain916Schema = haiProgressSignupChainSchema;
export type HaiProgressSignupChain916Props = HaiProgressSignupChainProps;

/* WCAG: the brand spark is 2.74:1 on cream — too light for TEXT (GATE T §8.3).
   Text and text-bearing chips use this deeper step (5.5:1); rules and borders keep SPARK. */
const SPARK_TEXT = '#A9482B';
const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
const SPRING = { damping: 26, stiffness: 105, mass: 0.9 };

export const HaiProgressSignupChain916: React.FC<HaiProgressSignupChain916Props> = ({
  eyebrow, title, tools, docLabel, docStatus, sparkLine, cues, durationSeconds, phoneType,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height, durationInFrames } = useVideoConfig();

  const PAD_X = width * 0.067;
  const CONTENT_W = width - PAD_X * 2;
  const op = (s: number) => clamp(s, 0, 1);

  const cueAt = (k: string) => (cues && typeof cues[k] === 'number' && durationSeconds)
    ? cues[k] * durationSeconds * fps : null;
  const cardAt = (i: number) => cueAt(`t${i}`) ?? 20 + i * 18;
  const DOC_AT = cueAt('doc') ?? Math.max(120, Math.round(durationInFrames * 0.42));
  const lastCard = cardAt(tools.length - 1);

  const titleIn = spring({ frame, fps, config: SPRING });
  const docIn = spring({ frame: frame - DOC_AT, fps, config: SPRING });
  const sparkIn = spring({ frame: frame - (Math.max(DOC_AT, lastCard) + 56), fps, config: SPRING });

  const CARD_H = height * (phoneType ? 0.094 : 0.092);            // ~177px — keeps the doc sheet clear of the spark line
  const CARD_GAP = height * 0.0104;         // ~20px
  const CARDS_TOP = height * (phoneType ? 0.205 : 0.227);         // ~436
  const cardsH = CARD_H * tools.length + CARD_GAP * (tools.length - 1);

  // Documentation sheet wraps the chain with room for its label lip
  const DOC_PAD = height * (phoneType ? 0.006 : 0.0135);   // phone: the sheet must stay inside the 9:16 title-safe x 54-1026
  const DOC_TOP = CARDS_TOP - DOC_PAD;
  const DOC_H = cardsH + DOC_PAD * 2 + height * (phoneType ? 0.050 : 0.038);

  // More than four tools (week-06: five) push the sheet down; the spark line then follows the
  // sheet instead of sitting at its fixed height. Four or fewer: unchanged, so earlier reels match.
  const SPARK_Y = tools.length > 4
    ? Math.max(height * 0.68, DOC_TOP + DOC_H + height * 0.03)
    : height * (phoneType ? 0.68 : 0.706);

  const DOT = height * 0.0198;              // ~38px hue dot

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>

      {/* Eyebrow */}
      <div style={{
        position: 'absolute', left: PAD_X, top: height * 0.125, display: phoneType ? 'none' : 'block',
        fontFamily: SANS, fontSize: height * 0.0135, fontWeight: 700,
        letterSpacing: 3, textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT, opacity: op(titleIn) * 0.8,
      }}>
        {eyebrow}
      </div>

      {/* Title */}
      <div style={{
        position: 'absolute', left: PAD_X, top: height * (phoneType ? 0.125 : 0.148),
        width: CONTENT_W,
        fontFamily: SERIF, fontSize: height * (phoneType ? 0.050 : 0.032), fontWeight: 600,
        color: CLAUDE.INK, letterSpacing: '-0.015em', lineHeight: 1.1,
        opacity: op(titleIn), transform: `translateY(${(1 - op(titleIn)) * 10}px)`,
      }}>
        {title}
      </div>

      {/* Documentation sheet, beneath the chain */}
      <div style={{
        position: 'absolute',
        left: PAD_X - DOC_PAD, top: DOC_TOP,
        width: CONTENT_W + DOC_PAD * 2, height: DOC_H,
        background: '#FFF8F5',
        border: `2px solid ${CLAUDE.SPARK}`,
        borderRadius: 24,
        opacity: op(docIn) * 0.95,
        transform: `translateY(${(1 - op(docIn)) * 34}px)`,
      }} />

      {/* Doc label + status on the sheet's bottom lip */}
      <div style={{
        position: 'absolute',
        left: PAD_X, top: DOC_TOP + DOC_H - height * (phoneType ? 0.043 : 0.030),
        width: CONTENT_W,
        display: 'flex', alignItems: 'center', gap: width * 0.018,
        opacity: op(docIn),
        transform: `translateY(${(1 - op(docIn)) * 34}px)`,
      }}>
        <div style={{
          fontFamily: SANS, fontSize: height * (phoneType ? 0.033 : 0.0115), fontWeight: 700,
          letterSpacing: phoneType ? 0.5 : 2, color: SPARK_TEXT,
        }}>
          {docLabel}
        </div>
        <div style={{
          fontFamily: SANS, fontSize: height * (phoneType ? 0.033 : 0.0104), fontWeight: 700,
          letterSpacing: phoneType ? 0.5 : 1.8, color: '#FFFFFF', background: SPARK_TEXT,
          borderRadius: 6, padding: `${height * 0.0026}px ${width * 0.014}px`,
        }}>
          {docStatus}
        </div>
      </div>

      {/* Vertical connectors through the hue dots */}
      {tools.slice(0, -1).map((_, i) => {
        const fromY = CARDS_TOP + i * (CARD_H + CARD_GAP) + CARD_H;
        const linkIn = interpolate(
          frame,
          [cardAt(i) + 24, cardAt(i + 1) + 8],
          [0, 1],
          { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' },
        );
        return (
          <div key={i} style={{
            position: 'absolute',
            left: PAD_X + width * 0.028 + DOT / 2 - 1.5,
            top: fromY,
            width: 3, height: CARD_GAP * linkIn,
            background: CLAUDE.INK_SOFT,
            opacity: linkIn * 0.5,
          }} />
        );
      })}

      {/* Tool cards, stacked */}
      {tools.map((t, i) => {
        const cardIn = spring({ frame: frame - cardAt(i), fps, config: SPRING });
        const y = CARDS_TOP + i * (CARD_H + CARD_GAP);

        return (
          <div key={i} style={{
            position: 'absolute',
            left: PAD_X, top: y,
            width: CONTENT_W, height: CARD_H,
            background: CLAUDE.CARD,
            border: `1px solid ${CLAUDE.BORDER}`,
            borderRadius: 18,
            boxShadow: '0 6px 26px rgba(61,57,41,0.08)',
            display: 'flex', alignItems: 'center', gap: width * 0.026,
            padding: `0 ${width * 0.028}px`,
            opacity: op(cardIn),
            transform: `translateY(${(1 - op(cardIn)) * 18}px)`,
          }}>
            {/* Hue dot */}
            <div style={{
              width: DOT, height: DOT, borderRadius: 999,
              background: t.hue, flexShrink: 0,
            }} />

            {/* Step + name + purpose */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: height * 0.003, flex: 1 }}>
              <div style={{
                fontFamily: SANS, fontSize: height * 0.0115, fontWeight: 700,
                letterSpacing: 2.2, color: CLAUDE.GHOST, display: phoneType ? 'none' : 'block',
              }}>
                STEP {i + 1}
              </div>
              <div style={{
                fontFamily: SERIF, fontSize: height * (phoneType ? 0.038 : 0.0245), fontWeight: 600,
                color: CLAUDE.INK, letterSpacing: '-0.01em', lineHeight: 1.15,
              }}>
                {t.name}
              </div>
              <div style={{
                fontFamily: phoneType ? SANS : SERIF, fontSize: height * (phoneType ? 0.033 : 0.0156),
                fontWeight: phoneType ? 700 : 400, color: CLAUDE.INK_SOFT, lineHeight: phoneType ? 1.05 : 1.3,
              }}>
                {t.purpose}
              </div>
            </div>

            {/* Hue rule on the trailing edge */}
            <div style={{
              width: height * 0.0042, height: CARD_H * 0.56 * op(cardIn),
              borderRadius: 3, background: t.hue, opacity: 0.85, flexShrink: 0,
            }} />
          </div>
        );
      })}

      {/* Spark line */}
      <div style={{
        position: 'absolute', left: PAD_X, top: SPARK_Y, width: CONTENT_W,
        display: 'flex', alignItems: 'flex-start', gap: 16,
        opacity: op(sparkIn),
      }}>
        <div style={{
          width: width * 0.085, height: 3, background: CLAUDE.SPARK,
          flexShrink: 0, marginTop: height * 0.014,
        }} />
        <span style={{
          fontFamily: SERIF, fontSize: height * (phoneType ? 0.034 : 0.0198), fontStyle: 'italic',
          color: CLAUDE.INK, lineHeight: 1.35,
        }}>
          {sparkLine}
        </span>
      </div>
    </AbsoluteFill>
  );
};
