/**
 * SqlPlanBeat916 — portrait (9:16) variant of B03's two-plan evidence beat.
 *
 * RE-BAND, the canonical case from explainer/SKILL.md: "16:9 lays out SIDE BY
 * SIDE; 9:16 stacks TOP AND BOTTOM." The landscape version puts plan A and plan
 * B in two columns; portrait stacks them, card A above card B, each full width.
 * A portrait column is WIDER in characters than a landscape half-column, so the
 * captured plan text gets MORE horizontal room here, not less.
 *
 * No library `SqlPlanBeat916`; `ClaudeCodeBeat916` exists but renders one card
 * and hardcodes its chip to 'python' (TEMPLATE-MISSES.md #1).
 *
 * Registered 1080x1920; --scale=2 renders 2160x3840 native.
 *
 * REEL-LOCAL. Register per remotion-src/REGISTER.md.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {z} from 'zod';
import { HandleChip } from './ClaudeCodeBeat';
import {clamp, remap, BG, INK, ACCENT, MUTE, WARN, scW} from './sqlDeckKit';

const planSchema = z.object({
  heading: z.string(),
  code: z.string(),
  verdict: z.string(),
  tone: z.enum(['good', 'warn']).default('good'),
});

export const sqlPlanBeat916Schema = z.object({
  /** Lower-right author handle chip (e.g. "Supriya"). Omitted → no chip. */
  handle: z.string().optional(),
  title: z.string().default(''),
  lang: z.string().default('sql'),
  left: planSchema,      // rendered TOP in portrait
  right: planSchema,     // rendered BOTTOM in portrait
  sparkLine: z.string().default('SCAN means every row.'),
  citation: z.string().default(''),
  highlightLeft: z.string().default('SCAN'),
  highlightRight: z.string().default('SEARCH'),
});
export type SqlPlanBeat916Props = z.infer<typeof sqlPlanBeat916Schema>;

const SERIF = "'EB Garamond', Georgia, serif";
const SANS = "system-ui, -apple-system, 'Segoe UI', sans-serif";
const MONO = "'JetBrains Mono', ui-monospace, monospace";
const CARD = '#FFFFFF';
const BORDER = '#E5E2D9';
const GHOST = '#A9A491';
const COMMENT = '#8B8878';

const Spark: React.FC<{size: number}> = ({size}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" style={{flexShrink: 0}}>
    {Array.from({length: 8}, (_, i) => (
      <line key={i} x1={12} y1={12}
        x2={12 + Math.cos((i * Math.PI) / 4) * 9}
        y2={12 + Math.sin((i * Math.PI) / 4) * 9}
        stroke={ACCENT} strokeWidth={2} strokeLinecap="round" />
    ))}
  </svg>
);

const PlanCard: React.FC<{
  plan: z.infer<typeof planSchema>; needle: string; accentOn: number; lang: string;
  frame: number; fps: number; delay: number; S: number; top: number; height: number; W: number;
  fontSize: number;
}> = ({plan, needle, accentOn, lang, frame, fps, delay, S, top, height, W, fontSize}) => {
  const cardIn = spring({frame: frame - delay, fps, config: {damping: 28, stiffness: 140, mass: 0.8}});
  const lines = plan.code.split('\n');
  const REVEAL = 12 + delay;
  const STRIDE = 2;
  const toneColor = plan.tone === 'warn' ? WARN : INK;
  const verdictAt = REVEAL + lines.length * STRIDE + 6;
  const verdictIn = clamp(interpolate(frame, [verdictAt, verdictAt + 10], [0, 1]), 0, 1);

  return (
    <div style={{
      position: 'absolute', left: 52 * S, width: W - 104 * S, top, height,
      display: 'flex', flexDirection: 'column',
      background: CARD, border: `${1 * S}px solid ${BORDER}`, borderRadius: 16 * S,
      boxShadow: '0 8px 32px rgba(61,57,41,0.10)', overflow: 'hidden',
      transform: `translateY(${(1 - clamp(cardIn, 0, 1)) * 18 * S}px)`,
      opacity: clamp(cardIn, 0, 1),
    }}>
      <div style={{
        display: 'flex', alignItems: 'center', gap: 10 * S, padding: `${14 * S}px ${24 * S}px`,
        background: BG, borderBottom: `${1 * S}px solid ${BORDER}`,
      }}>
        {[ACCENT, BORDER, BORDER].map((c, i) => (
          <div key={i} style={{width: 13 * S, height: 13 * S, borderRadius: '50%', background: c}} />
        ))}
        <span style={{
          marginLeft: 12 * S, fontFamily: SANS, fontSize: 24 * S, fontWeight: 600, color: INK,
          overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap',
        }}>{plan.heading}</span>
        <span style={{
          marginLeft: 'auto', fontFamily: SANS, fontSize: 15 * S, fontWeight: 600,
          color: ACCENT, letterSpacing: 2 * S, textTransform: 'uppercase',
        }}>{lang}</span>
      </div>

      <pre style={{
        margin: 0, padding: `${20 * S}px ${24 * S}px`, flex: 1,
        fontFamily: MONO, fontSize, lineHeight: 1.55, textAlign: 'left', overflow: 'hidden',
        display: 'flex', flexDirection: 'column', justifyContent: 'center',
      }}>
        {lines.map((line, i) => {
          const start = REVEAL + i * STRIDE;
          const op = clamp(interpolate(frame, [start, start + 5], [0, 1]), 0, 1);
          const isComment = line.trimStart().startsWith('--') || line.trimStart().startsWith('#');
          const base = isComment ? COMMENT : INK;
          const idx = needle ? line.indexOf(needle) : -1;
          return (
            <div key={i} style={{opacity: op, whiteSpace: 'pre', color: base}}>
              {idx >= 0 ? (
                <>
                  <span>{line.slice(0, idx)}</span>
                  <span style={{
                    color: accentOn > 0.02 ? ACCENT : base,
                    fontWeight: accentOn > 0.02 ? 700 : 400,
                    background: `rgba(217,119,87,${0.16 * accentOn})`,
                    borderRadius: 3 * S,
                  }}>{needle}</span>
                  <span>{line.slice(idx + needle.length)}</span>
                </>
              ) : line}
            </div>
          );
        })}
      </pre>

      <div style={{
        borderTop: `${1 * S}px solid ${BORDER}`, padding: `${15 * S}px ${24 * S}px`,
        display: 'flex', alignItems: 'center', gap: 14 * S, opacity: verdictIn,
      }}>
        <div style={{width: 5 * S, height: 28 * S, borderRadius: 2 * S, background: toneColor}} />
        <span style={{fontFamily: SANS, fontSize: 29 * S, fontWeight: 700, color: toneColor}}>
          {plan.verdict}
        </span>
      </div>
    </div>
  );
};

export const SqlPlanBeat916: React.FC<SqlPlanBeat916Props> = ({
  handle,
  title, lang, left, right, sparkLine, citation, highlightLeft, highlightRight,
}) => {
  const frame = useCurrentFrame();
  const {fps, width: W, height: H, durationInFrames} = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
  const S = scW(W);

  const accentA = clamp(interpolate(p, [0.18, 0.28, 0.46, 0.54], [0, 1, 1, 0]), 0, 1);
  const accentB = clamp(remap(p, 0.54, 0.64, 0, 1), 0, 1);
  const sparkIn = spring({frame: frame - 8, fps, config: {damping: 28, stiffness: 140, mass: 0.8}});

  // TOP AND BOTTOM: card A above, card B below.
  const topY = 192 * S;
  const gap = 34 * S;
  const bottomReserve = 250 * S;           // spark line + citation band
  const cardH = (H - topY - bottomReserve - gap) / 2;
  // v2: one shared mono size for both cards — the largest that fits the inner width
  // (longest captured line, ~0.61em/glyph; `pre` + overflow hidden would clip silently)
  // and inner height, capped at 1.5x the original 25*S. Body is centred vertically.
  const innerW = W - 104 * S - 48 * S - 2;
  const innerH = cardH - 52 * S - 56 * S - 40 * S;
  const allLines = [left.code, right.code].flatMap((c) => c.split('\n'));
  const maxChars = Math.max(...allLines.map((l) => l.length), 1);
  const maxLines = Math.max(left.code.split('\n').length, right.code.split('\n').length, 1);
  const planFont = Math.min(25 * S * 1.5, innerW / (maxChars * 0.61), innerH / (maxLines * 1.55));

  return (
    <AbsoluteFill style={{background: BG}}>
      <div style={{
        position: 'absolute', left: 52 * S, top: 100 * S, right: 52 * S,
        fontFamily: MONO, fontSize: 21 * S, color: MUTE, letterSpacing: '0.03em',
        whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis',
        opacity: clamp(interpolate(frame, [0, 12], [0, 1]), 0, 1),
      }}>{title}</div>

      <PlanCard plan={left} needle={highlightLeft} accentOn={accentA} lang={lang}
        frame={frame} fps={fps} delay={0} S={S} top={topY} height={cardH} W={W} fontSize={planFont} />
      <PlanCard plan={right} needle={highlightRight} accentOn={accentB} lang={lang}
        frame={frame} fps={fps} delay={10} S={S} top={topY + cardH + gap} height={cardH} W={W} fontSize={planFont} />

      <div style={{
        position: 'absolute', left: 52 * S, right: 52 * S, bottom: 108 * S,
        display: 'flex', alignItems: 'center', gap: 16 * S, opacity: clamp(sparkIn, 0, 1),
      }}>
        <Spark size={30 * S} />
        <span style={{fontFamily: SERIF, fontSize: 52 * S, color: INK, lineHeight: 1.1}}>
          {sparkLine}
        </span>
      </div>

      {citation ? (
        <div style={{
          position: 'absolute', left: 52 * S, right: 52 * S, bottom: 58 * S,
          fontFamily: SANS, fontSize: 20 * S, color: GHOST,
          opacity: clamp(interpolate(frame, [20, 34], [0, 1]), 0, 1),
        }}>{citation}</div>
      ) : null}
      <HandleChip handle={handle} fontSize={H * (H > W ? 0.016 : 0.024)} right={W * 0.07}
        bottom={H * (H > W ? 0.06 : 0.055)} opacity={0.9} />
    </AbsoluteFill>
  );
};
