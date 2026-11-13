/**
 * SqlPlanBeat — two EXPLAIN plans side by side, in the Claude fidelity skin.
 *
 * WHAT      A cream page carrying two mono plan cards (A | B), each with a
 *           heading, a verbatim captured plan body, and a verdict strip. A single
 *           terracotta highlight travels from the left card's SCAN to the right
 *           card's SEARCH, one accent at a time (accent law).
 * WHEN      A beat whose evidence IS captured terminal output and the point is the
 *           CONTRAST between two outputs. Not a general code beat.
 * ADAPTED-FROM
 *           runtime/remotion/src/scenes/ClaudeCodeBeat.tsx — same card grammar,
 *           same spring in, same per-line stagger reveal, same tokens.
 *           Two things made a reel-local scene necessary rather than a props
 *           change (logged in brutalist.art/TEMPLATE-MISSES.md):
 *             1. ClaudeCodeBeat hard-codes its language chip to the literal
 *                string 'python'. This beat is SQL.
 *             2. ClaudeCodeBeat renders ONE card. The whole point of this beat is
 *                two captures next to each other.
 * PROPS     see sqlPlanBeatSchema below.
 *
 * Pure function of the audio clock — no timers, no transitions, no Math.random().
 * Text is positioned from the shared SAFE constant, never by hand-nudged pixels.
 *
 * REEL-LOCAL. Register per remotion-src/REGISTER.md before rendering.
 */
import React from 'react';
import {
  AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate,
} from 'remotion';
import { z } from 'zod';
import { HandleChip } from './ClaudeCodeBeat';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE } from '../tokens/layout';

const planSchema = z.object({
  heading: z.string(),
  /** VERBATIM capture from demo/explain_*.txt. Never retype it by hand. */
  code: z.string(),
  verdict: z.string(),
  tone: z.enum(['good', 'warn']).default('good'),
});

export const sqlPlanBeatSchema = z.object({
  /** Lower-right author handle chip (e.g. "Supriya"). Omitted → no chip. */
  handle: z.string().optional(),
  title: z.string().default('demo/explain_a.txt  →  demo/explain_b.txt'),
  /** Language chip. The reason this scene exists — ClaudeCodeBeat pins 'python'. */
  lang: z.string().default('sql'),
  left: planSchema,
  right: planSchema,
  sparkLine: z.string().default('SCAN means every row.'),
  /** Small provenance line, bottom-left. REBUILD LAW: say where it came from. */
  citation: z.string().default(''),
  /** Substring in left.code that takes the accent first. */
  highlightLeft: z.string().default('SCAN'),
  /** Substring in right.code that takes the accent second. */
  highlightRight: z.string().default('SEARCH'),
});
export type SqlPlanBeatProps = z.infer<typeof sqlPlanBeatSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const MONO = CLAUDE_FONT.mono;
const COMMENT = '#8B8878';
const WARN = '#A44A32';

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

const Spark: React.FC<{ size?: number }> = ({ size = 16 }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" style={{ flexShrink: 0 }}>
    {Array.from({ length: 8 }, (_, i) => (
      <line
        key={i}
        x1={12} y1={12}
        x2={12 + Math.cos((i * Math.PI) / 4) * 9}
        y2={12 + Math.sin((i * Math.PI) / 4) * 9}
        stroke={CLAUDE.SPARK} strokeWidth={2} strokeLinecap="round"
      />
    ))}
  </svg>
);

/** One plan card. `accentOn` drives the highlight on `needle` within the body. */
const PlanCard: React.FC<{
  plan: z.infer<typeof planSchema>;
  needle: string;
  accentOn: number;
  lang: string;
  frame: number;
  fps: number;
  delay: number;
  fontSize: number;
}> = ({ plan, needle, accentOn, lang, frame, fps, delay, fontSize }) => {
  const cardIn = spring({
    frame: frame - delay, fps,
    config: { damping: 28, stiffness: 140, mass: 0.8 },
  });
  const lines = plan.code.split('\n');
  const REVEAL_START = 12 + delay;
  const LINE_STRIDE = 2;
  const toneColor = plan.tone === 'warn' ? WARN : CLAUDE.INK;

  // Verdict strip draws in only after the body has finished revealing.
  const verdictAt = REVEAL_START + lines.length * LINE_STRIDE + 6;
  const verdictIn = clamp(interpolate(frame, [verdictAt, verdictAt + 10], [0, 1]), 0, 1);

  return (
    <div style={{
      flex: 1,
      minWidth: 0,                       // lets flex children shrink instead of overflow
      display: 'flex',
      flexDirection: 'column',
      background: CLAUDE.CARD,
      border: `1px solid ${CLAUDE.BORDER}`,
      borderRadius: 14,
      boxShadow: '0 8px 32px rgba(61,57,41,0.10)',
      overflow: 'hidden',
      transform: `translateY(${(1 - clamp(cardIn, 0, 1)) * 18}px)`,
      opacity: clamp(cardIn, 0, 1),
    }}>
      {/* title bar */}
      <div style={{
        display: 'flex', alignItems: 'center', gap: 8,
        padding: '12px 20px',
        background: CLAUDE.PAGE,
        borderBottom: `1px solid ${CLAUDE.BORDER}`,
      }}>
        {[CLAUDE.SPARK, CLAUDE.BORDER, CLAUDE.BORDER].map((c, i) => (
          <div key={i} style={{ width: 11, height: 11, borderRadius: '50%', background: c }} />
        ))}
        <span style={{
          marginLeft: 10, fontFamily: SANS, fontSize: 17, fontWeight: 600,
          color: CLAUDE.INK, letterSpacing: '0.01em',
          overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap',
        }}>
          {plan.heading}
        </span>
        <span style={{
          marginLeft: 'auto', fontFamily: SANS, fontSize: 11, fontWeight: 600,
          color: CLAUDE.SPARK, letterSpacing: 2, textTransform: 'uppercase',
        }}>
          {lang}
        </span>
      </div>

      {/* plan body — verbatim capture */}
      <pre style={{
        margin: 0, padding: '20px 24px', flex: 1,
        fontFamily: MONO, fontSize, lineHeight: 1.6,
        textAlign: 'left', overflow: 'hidden',
        display: 'flex', flexDirection: 'column', justifyContent: 'center',
      }}>
        {lines.map((line, i) => {
          const start = REVEAL_START + i * LINE_STRIDE;
          const op = clamp(interpolate(frame, [start, start + 5], [0, 1]), 0, 1);
          const ty = interpolate(frame, [start, start + 7], [6, 0], {
            extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
          });
          const isComment = line.trimStart().startsWith('--') || line.trimStart().startsWith('#');
          const base = isComment ? COMMENT : CLAUDE.INK;

          // Split the line so `needle` can take the accent without re-laying out.
          const idx = needle ? line.indexOf(needle) : -1;
          const parts = idx >= 0
            ? [line.slice(0, idx), needle, line.slice(idx + needle.length)]
            : [line];

          return (
            <div key={i} style={{
              opacity: op,
              transform: `translateY(${ty}px)`,
              whiteSpace: 'pre',
              color: base,
            }}>
              {idx >= 0 ? (
                <>
                  <span>{parts[0]}</span>
                  <span style={{
                    color: accentOn > 0.02 ? CLAUDE.SPARK : base,
                    fontWeight: accentOn > 0.02 ? 700 : 400,
                    // highlight wash grows under the word as the voice names it
                    background: `rgba(217,119,87,${0.16 * accentOn})`,
                    borderRadius: 3,
                  }}>{parts[1]}</span>
                  <span>{parts[2]}</span>
                </>
              ) : line}
            </div>
          );
        })}
      </pre>

      {/* verdict strip */}
      <div style={{
        borderTop: `1px solid ${CLAUDE.BORDER}`,
        padding: '13px 24px',
        display: 'flex', alignItems: 'center', gap: 12,
        opacity: verdictIn,
      }}>
        <div style={{
          width: 4, height: 22, borderRadius: 2, background: toneColor,
          transform: `scaleY(${verdictIn})`, transformOrigin: 'center',
        }} />
        <span style={{
          fontFamily: SANS, fontSize: 21, fontWeight: 700, color: toneColor,
          overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap',
        }}>
          {plan.verdict}
        </span>
      </div>
    </div>
  );
};

export const SqlPlanBeat: React.FC<SqlPlanBeatProps> = ({
  handle,
  title, lang, left, right, sparkLine, citation, highlightLeft, highlightRight,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames, height, width } = useVideoConfig();
  const W = width, H = height;
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);

  // ONE accent at a time: A holds it through the first half, then hands to B.
  const accentA = clamp(interpolate(p, [0.18, 0.28, 0.46, 0.54], [0, 1, 1, 0]), 0, 1);
  const accentB = clamp(interpolate(p, [0.54, 0.64], [0, 1]), 0, 1);

  const sparkIn = spring({ frame: frame - 8, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });
  // FILL-THE-CANVAS without the clipping risk: the plan body uses the largest mono size
  // that fits BOTH the card's inner width (longest captured line, ~0.61em per glyph) and
  // its inner height, capped at 1.5× the original basis. Lines are `whiteSpace: pre` +
  // `overflow: hidden`, so a width overrun would clip silently — this bound prevents it.
  const cardInnerW = (SAFE.w - 30) / 2 - 48 - 2;
  const cardInnerH = (SAFE.h - 46 - 104) - 46 - 50 - 40;
  const maxChars = Math.max(...[left.code, right.code].flatMap((c) => c.split('\n')).map((l) => l.length), 1);
  const maxLines = Math.max(left.code.split('\n').length, right.code.split('\n').length, 1);
  const fontSize = Math.min(height * 0.0205 * 1.5, cardInnerW / (maxChars * 0.61), cardInnerH / (maxLines * 1.6));

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      {/* eyebrow: which files these came from. Inside SAFE. */}
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y,
        maxWidth: SAFE.w,
        fontFamily: MONO, fontSize: 15, color: CLAUDE.INK_SOFT,
        letterSpacing: '0.04em',
        overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap',
        opacity: clamp(interpolate(frame, [0, 12], [0, 1]), 0, 1),
      }}>
        {title}
      </div>

      {/* the two plan cards */}
      <div style={{
        position: 'absolute',
        left: SAFE.x, width: SAFE.w,
        top: SAFE.y + 46,
        height: SAFE.h - 46 - 104,      // leaves room for the spark line + citation
        display: 'flex', gap: 30, alignItems: 'stretch',
      }}>
        <PlanCard plan={left}  needle={highlightLeft}  accentOn={accentA}
                  lang={lang} frame={frame} fps={fps} delay={0}  fontSize={fontSize} />
        <PlanCard plan={right} needle={highlightRight} accentOn={accentB}
                  lang={lang} frame={frame} fps={fps} delay={10} fontSize={fontSize} />
      </div>

      {/* spark line — SPARK-LINE LAW: the spark never stands alone */}
      <div style={{
        position: 'absolute',
        left: SAFE.x, bottom: SAFE.y + 26,
        maxWidth: SAFE.w,
        display: 'flex', alignItems: 'center', gap: 12,
        opacity: clamp(sparkIn, 0, 1),
      }}>
        <Spark size={22} />
        <span style={{
          fontFamily: SERIF, fontSize: 38, color: CLAUDE.INK, lineHeight: 1.1,
        }}>
          {sparkLine}
        </span>
      </div>

      {/* provenance */}
      {citation ? (
        <div style={{
          position: 'absolute', left: SAFE.x, bottom: SAFE.y,
          maxWidth: SAFE.w,
          fontFamily: SANS, fontSize: 14, color: CLAUDE.GHOST,
          opacity: clamp(interpolate(frame, [20, 34], [0, 1]), 0, 1),
        }}>
          {citation}
        </div>
      ) : null}
      <HandleChip handle={handle} fontSize={H * (H > W ? 0.016 : 0.024)} right={W * 0.07}
        bottom={H * (H > W ? 0.06 : 0.055)} opacity={0.9} />
    </AbsoluteFill>
  );
};
