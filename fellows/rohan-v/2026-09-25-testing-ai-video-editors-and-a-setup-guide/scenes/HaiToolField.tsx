import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, exclusive, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, SPARK_TEXT, PHONE,
} from '../lib/cueKit';

/**
 * HaiToolField — B02 of "Testing AI Video Editors, and a Setup Guide for New
 * Fellows." (HAI weekly progress)
 *
 * A survey beat that has to avoid being a logo wall. Four tools, and the point
 * of the beat is that each one has a DIFFERENT idea of what a video is — code,
 * a web page, a timeline, a professional grading suite — so each card carries a
 * small animated drawing of that idea rather than a brand mark (no third-party
 * logos are reproduced). Cards land on their spoken names and the lit card is
 * exclusive; the card named in `testedIndex` receives a TESTED HANDS-ON stamp at
 * the end, which is the hand-off into the next beat.
 *
 *   four        "looked at four tools"      the four card frames (shell)
 *   remotion …  each tool's name            that card fills in and lights
 *   studio      "paid Studio version"       Resolve's caveat line turns spark
 *
 * Portrait re-lays the four cards as a 2×2 grid inside the safe band.
 */

const GLYPHS = ['code', 'html', 'timeline', 'wheel'] as const;

export const haiToolFieldSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · WEEKLY PROGRESS'),
  title: z.string().default('Four Ways to Let an Agent Edit'),
  tools: z.array(z.object({
    name: z.string(), how: z.string(), note: z.string(),
    glyph: z.enum(GLYPHS),
    /** portrait (phone) only: a 1–2 word all-caps tag in place of `how` + `note` */
    tag: z.string().optional(),
    /** portrait only: the tag shown once the `studio` cue lands (the caveat) */
    caveatTag: z.string().optional(),
  })).default([
    { name: 'Remotion', how: 'a video written as code', note: 'what Brutalist is built on', glyph: 'code' },
    { name: 'HyperFrames', how: 'a video written as a web page', note: 'by HeyGen, built for agents', glyph: 'html' },
    { name: 'OpenReel', how: 'an open-source editor in the browser', note: 'desktop app connects to Claude', glyph: 'timeline' },
    { name: 'DaVinci Resolve', how: 'a professional editor, driven by an agent', note: 'community connectors · full scripting needs paid Studio', glyph: 'wheel' },
  ]),
  testedIndex: z.number().default(1),
  stampLabel: z.string().default('TESTED HANDS-ON'),
  sparkLine: z.string().default('Four tools, four ideas of what editing is.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type HaiToolFieldProps = z.infer<typeof haiToolFieldSchema>;

/** The drawing inside each card — its idea of what a video is. */
const Glyph: React.FC<{ kind: typeof GLYPHS[number]; w: number; h: number; t: number; k: number; lit: boolean }> =
({ kind, w, h, t, k, lit }) => {
  const ink = lit ? SPARK_TEXT : CLAUDE.INK;   // also the glyph's text (</>, <video>)
  const soft = CLAUDE.INK_SOFT;
  const stroke = Math.max(2, h * 0.02);
  if (kind === 'code') {
    const lines = [0.62, 0.44, 0.78, 0.36, 0.55];
    const typed = (t * 0.9) % (lines.length + 1.5);
    return (
      <svg width={w} height={h}>
        <text x={w * 0.06} y={h * 0.24} fontFamily={HAI_TYPE.mono} fontSize={h * 0.2}
          fill={ink} fontWeight={700}>{'</>'}</text>
        {lines.map((L, i) => {
          const f = clamp(typed - i, 0, 1) * k;
          return <rect key={i} x={w * (0.06 + (i % 2) * 0.08)} y={h * (0.38 + i * 0.12)}
            width={w * L * f} height={h * 0.05} rx={h * 0.02}
            fill={i === 2 ? ink : soft} opacity={0.75} />;
        })}
      </svg>
    );
  }
  if (kind === 'html') {
    const blink = (Math.sin(t * 5) + 1) / 2;
    return (
      <svg width={w} height={h}>
        <rect x={stroke} y={stroke} width={w - stroke * 2} height={h - stroke * 2} rx={h * 0.06}
          fill="none" stroke={ink} strokeWidth={stroke} />
        <line x1={stroke} y1={h * 0.2} x2={w - stroke} y2={h * 0.2} stroke={ink} strokeWidth={stroke} />
        {[0, 1, 2].map(i => <circle key={i} cx={w * (0.08 + i * 0.06)} cy={h * 0.1} r={h * 0.025} fill={soft} />)}
        <text x={w * 0.08} y={h * 0.42} fontFamily={HAI_TYPE.mono} fontSize={h * 0.12} fill={ink}>{'<video>'}</text>
        <rect x={w * 0.12} y={h * 0.5} width={w * 0.6 * k} height={h * 0.2} rx={h * 0.03}
          fill={ink} opacity={0.18 + 0.2 * blink} />
        <text x={w * 0.08} y={h * 0.88} fontFamily={HAI_TYPE.mono} fontSize={h * 0.12} fill={ink}>{'</video>'}</text>
      </svg>
    );
  }
  if (kind === 'timeline') {
    const play = ((t * 0.22) % 1);
    const tracks = [[0.02, 0.34, 0.4, 0.3], [0.1, 0.45, 0.6, 0.3], [0.0, 0.8]];
    return (
      <svg width={w} height={h}>
        {tracks.map((segs, r) => (
          <g key={r}>
            <rect x={0} y={h * (0.12 + r * 0.28)} width={w} height={h * 0.2} rx={h * 0.03}
              fill={CLAUDE.FOOTER} />
            {Array.from({ length: segs.length / 2 }).map((_, j) => (
              <rect key={j} x={w * segs[j * 2]} y={h * (0.14 + r * 0.28)}
                width={w * segs[j * 2 + 1] * k} height={h * 0.16} rx={h * 0.025}
                fill={r === 1 ? ink : soft} opacity={r === 1 ? 0.85 : 0.55} />
            ))}
          </g>
        ))}
        <line x1={w * play} y1={0} x2={w * play} y2={h} stroke={CLAUDE.SPARK} strokeWidth={stroke * 1.2} />
      </svg>
    );
  }
  // wheel — a grading colour wheel, its puck drifting
  const R = Math.min(w, h) * 0.42;
  const cx = w / 2, cy = h / 2;
  const a = t * 0.8;
  return (
    <svg width={w} height={h}>
      {[0, 1, 2].map(i => {
        const a0 = (i / 3) * Math.PI * 2 - Math.PI / 2;
        const a1 = a0 + (Math.PI * 2) / 3 - 0.1;
        const p = (ang: number) => `${cx + Math.cos(ang) * R} ${cy + Math.sin(ang) * R}`;
        return <path key={i} d={`M ${p(a0)} A ${R} ${R} 0 0 1 ${p(a1)}`} fill="none"
          stroke={[CLAUDE.SPARK, soft, ink][i]} strokeWidth={stroke * 3} strokeLinecap="round"
          opacity={0.35 + 0.65 * k} />;
      })}
      <circle cx={cx} cy={cy} r={R * 0.62} fill="none" stroke={CLAUDE.BORDER} strokeWidth={stroke} />
      <circle cx={cx + Math.cos(a) * R * 0.3} cy={cy + Math.sin(a) * R * 0.3} r={R * 0.1}
        fill={CLAUDE.CARD} stroke={ink} strokeWidth={stroke * 1.2} />
    </svg>
  );
};

export const HaiToolField: React.FC<HaiToolFieldProps> = ({
  eyebrow, title, tools, testedIndex, stampLabel, sparkLine, cues,
}) => {
  const { frame, fps, width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CONTENT_W = width - PAD_X * 2;

  const tFour = at('four', 0.02);
  const keys = ['remotion', 'hyperframes', 'openreel', 'resolve'];
  const defaults = [0.1, 0.3, 0.5, 0.72];
  const tIn = keys.map((k, i) => at(k, defaults[i]));
  const tStudio = at('studio', 0.9);

  const headIn = sp(0);
  const sShell = sp(tFour);
  const sCard = tIn.map(t => sp(t));
  const sStudio = sp(tStudio, SPRING_SNAP);
  const sStamp = sp(clamp(tStudio + 0.05, 0, 0.96), SPRING_SNAP);
  const sparkIn = sp(clamp(tStudio + 0.03, 0, 0.97));
  const hot = exclusive(sCard);

  const COLS = portrait ? 2 : 4;
  const GAP = (portrait ? 26 : 28) * U;
  const TOP = portrait ? height * 0.255 : height * 0.30;
  const CW = (CONTENT_W - GAP * (COLS - 1)) / COLS;
  const CH = portrait ? height * 0.215 : height * 0.52;
  const GW = CW - 52 * U;
  const GH = portrait ? CH * 0.25 : CH * 0.36;

  /* ── PORTRAIT (phone): PHONE type scale — less text, larger. Four full-width rows:
     the drawing on the left, the name and ONE short tag (from the vertical sheet)
     beside it. A 2x2 grid could not hold "HyperFrames" at phone size. The Studio
     caveat replaces Resolve's tag on its cue. */
  if (portrait) {
    const T = PHONE(height);
    const RG = 18, RH = height * 0.098, TOP2 = height * 0.245, GW2 = CONTENT_W * 0.2;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        {tools.slice(0, 4).map((tool, i) => {
          const y = TOP2 + i * (RH + RG);
          const k = op(sCard[i]);
          const lit = hot[i] > 0.3;
          const caveat = i === 3 && op(sStudio) > 0.4 && tool.caveatTag;
          return (
            <div key={i} style={{
              position: 'absolute', left: PAD_X, top: y, width: CONTENT_W, height: RH, boxSizing: 'border-box',
              background: k > 0.05 ? CLAUDE.CARD : CLAUDE.FOOTER, borderRadius: 18,
              border: `${lit ? 4 : 2}px ${k > 0.05 ? 'solid' : 'dashed'} ${lit ? SPARK_TEXT : CLAUDE.GHOST}`,   // spark borders read as accent type at phone size
              padding: '14px 22px', opacity: op(sShell), display: 'flex', alignItems: 'center', gap: 26,
            }}>
              <div style={{ opacity: 0.25 + 0.75 * k, flexShrink: 0 }}>
                <Glyph kind={tool.glyph} w={GW2} h={RH - 40} t={frame / fps} k={k} lit={lit} />
              </div>
              <div style={{ opacity: k }}>
                <div style={{ fontFamily: HAI_TYPE.serif, fontSize: T.body, fontWeight: 700, color: CLAUDE.INK, lineHeight: 1 }}>{tool.name}</div>
                <div style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 0.5,
                  color: caveat ? SPARK_TEXT : CLAUDE.INK_SOFT, marginTop: 6, lineHeight: 1 }}>
                  {caveat ? tool.caveatTag : (tool.tag ?? tool.how)}
                </div>
              </div>
              {i === testedIndex && (
                <div style={{
                  position: 'absolute', right: 20, top: -T.label * 0.55,   // on the row's top edge, clear of the name
                  fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 1,
                  color: CLAUDE.CARD, background: SPARK_TEXT, borderRadius: 10, padding: '0 14px',
                  opacity: op(sStamp), transform: `rotate(-3deg) scale(${0.6 + 0.4 * op(sStamp)})`,
                }}>TESTED</div>
              )}
            </div>
          );
        })}
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
          height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn}
        padX={PAD_X} height={height} width={width} portrait={portrait} />

      {tools.slice(0, 4).map((tool, i) => {
        const col = i % COLS, row = Math.floor(i / COLS);
        const x = PAD_X + col * (CW + GAP);
        const y = TOP + row * (CH + GAP);
        const k = op(sCard[i]);
        const lit = hot[i] > 0.3;
        const isTested = i === testedIndex;
        const caveat = i === 3 && op(sStudio) > 0.4;
        return (
          <div key={i} style={{
            position: 'absolute', left: x, top: y, width: CW, height: CH,
            opacity: op(sShell), boxSizing: 'border-box',
            background: k > 0.05 ? CLAUDE.CARD : CLAUDE.FOOTER, borderRadius: 18 * U,
            border: `${lit ? 3 : 1.5}px ${k > 0.05 ? 'solid' : 'dashed'} ${lit ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            boxShadow: lit ? '0 14px 36px rgba(217,119,87,0.16)' : '0 8px 24px rgba(61,57,41,0.05)',
            padding: `${26 * U}px ${26 * U}px`,
            transform: `translateY(${(1 - k) * 24 * U}px) scale(${lit ? 1.015 : 1})`,
          }}>
            <div style={{ opacity: 0.25 + 0.75 * k }}>
              <Glyph kind={tool.glyph} w={GW} h={GH} t={frame / fps} k={k} lit={lit} />
            </div>
            <div style={{
              fontFamily: HAI_TYPE.serif, fontSize: (portrait ? 38 : 46) * U, fontWeight: 700,
              color: CLAUDE.INK, marginTop: 18 * U, opacity: k, lineHeight: 1.05,
            }}>{tool.name}</div>
            <div style={{
              fontFamily: HAI_TYPE.serif, fontSize: (portrait ? 27 : 31) * U, color: CLAUDE.INK,
              marginTop: 10 * U, lineHeight: 1.25, opacity: k,
            }}>{tool.how}</div>
            <div style={{
              fontFamily: HAI_TYPE.sans, fontSize: (portrait ? 19 : 21) * U, fontWeight: 600,
              letterSpacing: 0.3, color: caveat ? SPARK_TEXT : CLAUDE.INK_SOFT,
              marginTop: 12 * U, lineHeight: 1.35, opacity: k,
            }}>{tool.note}</div>
            {isTested && (
              <div style={{
                position: 'absolute', right: 18 * U, top: -18 * U,
                fontFamily: HAI_TYPE.sans, fontSize: 19 * U, fontWeight: 800, letterSpacing: 2,
                color: CLAUDE.CARD, background: SPARK_TEXT, borderRadius: 8 * U,
                padding: `${8 * U}px ${14 * U}px`,
                opacity: op(sStamp), transform: `rotate(-3deg) scale(${0.6 + 0.4 * op(sStamp)})`,
              }}>{stampLabel}</div>
            )}
          </div>
        );
      })}

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
        height={height} portrait={portrait}
        top={portrait ? TOP + CH * 2 + GAP + 44 * U : undefined} />
    </AbsoluteFill>
  );
};
