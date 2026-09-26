import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, SPARK_TEXT, PHONE,
} from '../lib/cueKit';

/**
 * HaiVerdictSplit — B05 of "Testing AI Video Editors, and a Setup Guide for
 * New Fellows." (HAI weekly progress)
 *
 * What a single test actually showed, and no more. Two columns: what the tool
 * was GOOD AT (ink ticks) and what it did NOT YET do (open terracotta rings),
 * then a dashed PENDING strip for everything not tested at all. The strip is
 * the honesty device: a one-tool test cannot rank four tools, and the frame
 * says so rather than implying a winner.
 *
 *   showed   "what the test showed"     both column frames (shell)
 *   good     "good at packaging"        the good items tick in, staggered
 *   visuals  "didn't add new teaching"  not-yet item 1
 *   fourk    "didn't reach our four K"  not-yet item 2
 *   pending  "other three tools"        the pending strip
 *
 * Portrait stacks the columns, then the strip, inside the safe band.
 */

export const haiVerdictSplitSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · WEEKLY PROGRESS'),
  title: z.string().default('What the Test Showed'),
  goodHeader: z.string().default('GOOD AT'),
  notYetHeader: z.string().default('NOT YET'),
  good: z.array(z.string()).default([]),
  notYet: z.array(z.string()).default([]),
  pendingLabel: z.string().default("NOT TESTED YET"),
  pending: z.string().default(''),
  sparkLine: z.string().default(''),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type HaiVerdictSplitProps = z.infer<typeof haiVerdictSplitSchema>;

export const HaiVerdictSplit: React.FC<HaiVerdictSplitProps> = ({
  eyebrow, title, goodHeader, notYetHeader, good, notYet, pendingLabel, pending, sparkLine, cues,
}) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CONTENT_W = width - PAD_X * 2;

  const tShow = at('showed', 0.03);
  const tGood = at('good', 0.16);
  const tVis = at('visuals', 0.46);
  const tFour = at('fourk', 0.7);
  const tPend = at('pending', 0.85);

  const headIn = sp(0);
  const sShell = sp(tShow);
  const sGood = good.map((_, i) => sp(clamp(tGood + i * 0.05, 0, 0.97), SPRING_SNAP));
  const sNot = notYet.map((_, i) => sp(i === 0 ? tVis : tFour, SPRING_SNAP));
  const sPend = sp(tPend);
  const sparkIn = sp(clamp(tPend + 0.06, 0, 0.97));

  const GAP = (portrait ? 22 : 36) * U;
  const COL_W = portrait ? CONTENT_W : (CONTENT_W - GAP) / 2;
  const TOP = portrait ? height * 0.235 : height * 0.29;
  const COL_H = portrait ? height * 0.17 : height * 0.43;
  const TXT = (portrait ? 42 : 44) * U;   // GATE T §8.1: x-height of short words must clear 41px at 4K

  const column = (i: number, header: string, items: string[], springs: number[], positive: boolean) => {
    const x = portrait ? PAD_X : PAD_X + i * (COL_W + GAP);
    const y = portrait ? TOP + i * (COL_H + GAP) : TOP;
    const accent = positive ? CLAUDE.INK : SPARK_TEXT;   // header text + top rule
    return (
      <div style={{
        position: 'absolute', left: x, top: y, width: COL_W, height: COL_H,
        boxSizing: 'border-box', background: CLAUDE.CARD, borderRadius: 18 * U,
        border: `1.5px solid ${CLAUDE.BORDER}`, borderTop: `${6 * U}px solid ${accent}`,
        padding: `${26 * U}px ${32 * U}px`, opacity: op(sShell),
        boxShadow: '0 10px 30px rgba(61,57,41,0.06)',
      }}>
        <div style={{
          fontFamily: HAI_TYPE.sans, fontSize: 23 * U, fontWeight: 800,
          letterSpacing: 3, color: accent, marginBottom: 16 * U,
        }}>{header}</div>
        {items.map((it, j) => {
          const k = op(springs[j] ?? 0);
          return (
            <div key={j} style={{
              display: 'flex', alignItems: 'flex-start', gap: 18 * U,
              marginBottom: (portrait ? 12 : 20) * U, opacity: k,
              transform: `translateX(${(1 - k) * 22 * U}px)`,
            }}>
              <svg width={TXT * 0.95} height={TXT * 0.95} style={{ flexShrink: 0, marginTop: TXT * 0.12 }}>
                {positive ? (
                  <>
                    <circle cx={TXT * 0.475} cy={TXT * 0.475} r={TXT * 0.44} fill={CLAUDE.INK} />
                    <path d={`M ${TXT * 0.26} ${TXT * 0.5} L ${TXT * 0.42} ${TXT * 0.66} L ${TXT * 0.7} ${TXT * 0.32}`}
                      stroke={CLAUDE.CARD} strokeWidth={TXT * 0.1} fill="none"
                      strokeLinecap="round" strokeLinejoin="round"
                      strokeDasharray={TXT} strokeDashoffset={TXT * (1 - k)} />
                  </>
                ) : (
                  <circle cx={TXT * 0.475} cy={TXT * 0.475} r={TXT * 0.38} fill="none"
                    stroke={CLAUDE.SPARK} strokeWidth={TXT * 0.1}
                    strokeDasharray={TXT * 2.4} strokeDashoffset={TXT * 2.4 * (1 - k)} />
                )}
              </svg>
              <div style={{
                fontFamily: HAI_TYPE.serif, fontSize: TXT, lineHeight: 1.25, color: CLAUDE.INK,
              }}>{it}</div>
            </div>
          );
        })}
      </div>
    );
  };

  const PEND_Y = portrait ? TOP + COL_H * 2 + GAP * 2 : TOP + COL_H + GAP;
  const kp = op(sPend);
  /* ── PORTRAIT (phone): PHONE type scale — less text, larger. One-line items (short
     strings from the vertical sheet), the two cards stacked, the pending strip as two
     caps lines. Title must be one line (the vertical sheet shortens it). */
  if (portrait) {
    const T = PHONE(height);
    const TOPp = height * 0.19, GAPp = 16;
    const item = (it: string, k: number, positive: boolean, j: number) => (
      <div key={j} style={{ display: 'flex', alignItems: 'center', gap: 18, opacity: k,
        transform: `translateX(${(1 - k) * 22}px)`, marginTop: 6 }}>
        <svg width={T.body * 0.75} height={T.body * 0.75} style={{ flexShrink: 0 }}>
          {positive ? (
            <>
              <circle cx={T.body * 0.375} cy={T.body * 0.375} r={T.body * 0.35} fill={CLAUDE.INK} />
              <path d={`M ${T.body * 0.2} ${T.body * 0.39} L ${T.body * 0.33} ${T.body * 0.52} L ${T.body * 0.55} ${T.body * 0.25}`}
                stroke={CLAUDE.CARD} strokeWidth={T.body * 0.08} fill="none" strokeLinecap="round" strokeLinejoin="round" />
            </>
          ) : (
            <circle cx={T.body * 0.375} cy={T.body * 0.375} r={T.body * 0.3} fill="none" stroke={CLAUDE.SPARK} strokeWidth={T.body * 0.08} />
          )}
        </svg>
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: T.body, lineHeight: 1.1, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{it}</div>
      </div>
    );
    const cardp = (header: string, items: string[], springs: number[], positive: boolean) => (
      <div style={{ boxSizing: 'border-box', background: CLAUDE.CARD, borderRadius: 18, width: CONTENT_W,
        border: `2px solid ${CLAUDE.BORDER}`, borderTop: `8px solid ${positive ? CLAUDE.INK : CLAUDE.SPARK}`,
        padding: '16px 28px 20px', opacity: op(sShell), marginBottom: GAPp }}>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 1,
          color: positive ? CLAUDE.INK : SPARK_TEXT }}>{header}</div>
        {items.map((it, j) => item(it, op(springs[j] ?? 0), positive, j))}
      </div>
    );
    const kp = op(sPend);
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: TOPp }}>
          {cardp(goodHeader, good, sGood, true)}
          {cardp(notYetHeader, notYet, sNot, false)}
          <div style={{ boxSizing: 'border-box', width: CONTENT_W, borderRadius: 14, background: CLAUDE.FOOTER,
            border: `3px dashed ${kp > 0.5 ? CLAUDE.SPARK : CLAUDE.GHOST}`, padding: '12px 24px',
            opacity: 0.45 + 0.55 * kp }}>
            <span style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 0.5,
              color: CLAUDE.CARD, background: SPARK_TEXT, borderRadius: 8, padding: '0 12px', opacity: kp }}>{pendingLabel}</span>
            <div style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 0.5,
              color: CLAUDE.INK, marginTop: 8, opacity: kp }}>{pending}</div>
          </div>
        </div>
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
          height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn}
        padX={PAD_X} height={height} width={width} portrait={portrait} />
      {column(0, goodHeader, good, sGood, true)}
      {column(1, notYetHeader, notYet, sNot, false)}

      <div style={{
        position: 'absolute', left: PAD_X, top: PEND_Y, width: CONTENT_W,
        boxSizing: 'border-box', borderRadius: 14 * U,
        border: `2px dashed ${kp > 0.5 ? CLAUDE.SPARK : CLAUDE.BORDER}`,
        background: CLAUDE.FOOTER, padding: `${16 * U}px ${26 * U}px`,
        display: 'flex', flexDirection: portrait ? 'column' : 'row',
        alignItems: portrait ? 'flex-start' : 'center', gap: (portrait ? 8 : 22) * U,
        opacity: 0.35 + 0.65 * kp,
      }}>
        <span style={{
          fontFamily: HAI_TYPE.sans, fontSize: 22 * U, fontWeight: 800, letterSpacing: 2,
          color: CLAUDE.CARD, background: SPARK_TEXT, borderRadius: 6 * U,
          padding: `${5 * U}px ${10 * U}px`, whiteSpace: 'nowrap', opacity: kp,
        }}>{pendingLabel}</span>
        <span style={{
          fontFamily: HAI_TYPE.serif, fontSize: (portrait ? 28 : 31) * U, color: CLAUDE.INK, opacity: kp,
        }}>{pending}</span>
      </div>

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
        height={height} portrait={portrait}
        top={portrait ? PEND_Y + 150 * U : undefined} />
    </AbsoluteFill>
  );
};
