import React from 'react';
import { AbsoluteFill, Img, staticFile, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, CountTo, HAI_TYPE, SPRING_SETTLE, SPARK_TEXT, PHONE,
} from '../lib/cueKit';

/**
 * HaiFootageShowcase — B03 of "Testing AI Video Editors, and a Setup Guide for
 * New Fellows." (HAI weekly progress)
 *
 * The receipt beat. When a progress video reports that a tool was tested, the
 * honest evidence is the tool's actual output, not a rebuilt picture of it — so
 * this plays REAL frames of the agent's render (the fellow's own footage, which
 * the FELLOW'S-WORK carve-out allows) inside a monitor, cross-fading with a slow
 * push-in. What went in and what was asked for sit above the monitor as an
 * input → ask strip, and the measured results count up beside it.
 *
 *   tested    "tested one properly"            monitor + first frame
 *   footage   "finished footage and narration" INPUT chip, second frame
 *   captions  "captions that light up"         ASK chip, the captioned frame
 *   back      "came back with"                 runtime + caption-line counters
 *   overlap   "none of them overlapping"       the 0 lands, in spark
 *
 * Frames are `staticFile` paths under runtime/remotion/public/. Portrait puts
 * the monitor across the width with the stats in a row beneath it.
 */

export const haiFootageShowcaseSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · WEEKLY PROGRESS'),
  title: z.string().default('One Real Test'),
  frames: z.array(z.string()).default([]),
  input: z.string().default('Suno Part 1 — finished footage + narration'),
  ask: z.string().default('word-by-word captions + a new intro'),
  stats: z.array(z.object({ value: z.string(), label: z.string() })).default([]),
  credit: z.string().default(''),
  sparkLine: z.string().default(''),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type HaiFootageShowcaseProps = z.infer<typeof haiFootageShowcaseSchema>;

export const HaiFootageShowcase: React.FC<HaiFootageShowcaseProps> = ({
  eyebrow, title, frames, input, ask, stats, credit, sparkLine, cues,
}) => {
  const { frame, D, width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CONTENT_W = width - PAD_X * 2;

  const tTest = at('tested', 0.02);
  const tFoot = at('footage', 0.2);
  const tCap = at('captions', 0.42);
  const tBack = at('back', 0.66);
  const tOver = at('overlap', 0.86);

  const headIn = sp(0);
  const sMon = sp(tTest);
  const sInput = sp(tFoot);
  const sAsk = sp(tCap);
  const sBack = sp(tBack, SPRING_SETTLE);
  const sOver = sp(tOver, SPRING_SETTLE);
  const sparkIn = sp(clamp(tOver + 0.04, 0, 0.97));

  // which frame is up, cross-faded on the spoken cues
  const switches = [tTest, tFoot, tCap, tBack].slice(0, Math.max(1, frames.length));
  const fr = frame / D;

  // ── layout ──────────────────────────────────────────────────────────
  const STRIP_Y = portrait ? height * 0.235 : height * 0.265;
  const MON_Y = portrait ? height * 0.305 : height * 0.345;
  const MON_W = portrait ? CONTENT_W : CONTENT_W * 0.55;
  const MON_H = MON_W * 9 / 16;
  const SIDE_X = PAD_X + MON_W + CONTENT_W * 0.04;
  const SIDE_W = CONTENT_W - MON_W - CONTENT_W * 0.04;

  const chip = (label: string, text: string, k: number, hotChip: boolean) => (
    <div style={{
      display: 'flex', alignItems: 'baseline', gap: 12 * U, opacity: k,
      transform: `translateX(${(1 - k) * 20 * U}px)`,
    }}>
      <span style={{
        fontFamily: HAI_TYPE.sans, fontSize: 19 * U, fontWeight: 800, letterSpacing: 2,
        color: CLAUDE.CARD, background: hotChip ? SPARK_TEXT : CLAUDE.INK,
        borderRadius: 6 * U, padding: `${5 * U}px ${10 * U}px`, whiteSpace: 'nowrap',
      }}>{label}</span>
      <span style={{
        fontFamily: HAI_TYPE.serif, fontSize: (portrait ? 30 : 32) * U, color: CLAUDE.INK,
      }}>{text}</span>
    </div>
  );

  const statTiles = stats.map((s, i) => {
    const isZero = i === stats.length - 1;
    const k = op(isZero ? sOver : sBack);
    const num = parseFloat(s.value.replace(':', '.'));
    const counts = !s.value.includes(':') && isFinite(num) && num > 0;
    return (
      <div key={i} style={{
        flex: portrait ? 1 : undefined,
        /* SHELL: an empty dashed tile holds the slot from the first frame, so the
           results column is never blank at a Gate V sample; the value waits. */
        background: k > 0.05 ? CLAUDE.CARD : CLAUDE.FOOTER,
        border: `${isZero && k > 0.5 ? 3 : 1.5}px ${k > 0.05 ? 'solid' : 'dashed'} ${isZero && k > 0.5 ? CLAUDE.SPARK : CLAUDE.BORDER}`,
        borderRadius: 14 * U, padding: `${18 * U}px ${22 * U}px`,
        opacity: Math.max(k, op(sMon) * 0.7),
      }}>
        <div style={{ opacity: k, transform: `translateY(${(1 - k) * 16 * U}px)` }}>
        <div style={{
          fontFamily: HAI_TYPE.serif, fontSize: (portrait ? 76 : 84) * U, fontWeight: 700,
          lineHeight: 1, color: isZero ? SPARK_TEXT : CLAUDE.INK,
        }}>
          {counts
            ? <CountTo to={num} fromFrame={D * (isZero ? tOver : tBack)} frames={26}
                style={{ display: 'inline-block' }} />
            : s.value}
        </div>
        <div style={{
          fontFamily: HAI_TYPE.sans, fontSize: 19 * U, fontWeight: 700, letterSpacing: 2,
          color: CLAUDE.INK_SOFT, marginTop: 8 * U,
        }}>{s.label}</div>
        </div>
      </div>
    );
  });

  /* ── PORTRAIT (phone): PHONE type scale — less text, larger. Two short caps rows
     (INPUT / ASK, strings from the vertical sheet), the monitor full width, and the
     results as one row of big numbers. The credit line is landscape-only. */
  if (portrait) {
    const T = PHONE(height);
    const R1 = height * 0.19, R2 = R1 + T.label * 1.3;
    const pMON_Y = R2 + T.label * 1.45, pMON_W = CONTENT_W, pMON_H = pMON_W * 9 / 16;
    const ST_Y = pMON_Y + pMON_H + height * 0.018;
    const capsRow = (label: string, text: string, y: number, k: number, hotChip: boolean) => (
      <div style={{ position: 'absolute', left: PAD_X, top: y, display: 'flex', gap: 16, alignItems: 'center',
        opacity: k, whiteSpace: 'nowrap', transform: `translateX(${(1 - k) * 20}px)` }}>
        <span style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label * 0.98, fontWeight: 800, letterSpacing: 0.5,
          color: CLAUDE.CARD, background: hotChip ? SPARK_TEXT : CLAUDE.INK, borderRadius: 8, padding: '0 12px' }}>{label}</span>
        <span style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 700, letterSpacing: 0.5, color: CLAUDE.INK }}>{text}</span>
      </div>
    );
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        {capsRow('INPUT', input, R1, op(sInput), false)}
        {capsRow('ASK', ask, R2, op(sAsk), true)}
        <div style={{
          position: 'absolute', left: PAD_X, top: pMON_Y, width: pMON_W, height: pMON_H,
          borderRadius: 16, overflow: 'hidden', background: '#10131F',
          border: `8px solid ${CLAUDE.INK}`, boxSizing: 'border-box',
          boxShadow: '0 22px 50px rgba(61,57,41,0.22)', opacity: op(sMon),
        }}>
          {frames.map((f, i) => {
            const start = switches[i] ?? 1, next = switches[i + 1] ?? 2;
            const vis = (i === 0 ? 1 : clamp((fr - start) / 0.035, 0, 1)) * (1 - clamp((fr - next) / 0.035, 0, 1));
            if (vis <= 0) return null;
            const push = interpolate(fr, [start, Math.min(1, next + 0.05)], [1.0, 1.06], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
            return <Img key={i} src={staticFile(f)} style={{ position: 'absolute', inset: 0, width: '100%', height: '100%',
              objectFit: 'cover', opacity: vis, transform: `scale(${push})` }} />;
          })}
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: ST_Y, width: CONTENT_W, display: 'flex', gap: 18 }}>
          {stats.map((s, i) => {
            const isZero = i === stats.length - 1;
            const k = op(isZero ? sOver : sBack);
            return (
              <div key={i} style={{ flex: 1, opacity: Math.max(k, op(sMon) * 0.9),
                borderTop: `6px ${k > 0.05 ? 'solid' : 'dashed'} ${isZero && k > 0.5 ? CLAUDE.SPARK : CLAUDE.GHOST}`, paddingTop: 10 }}>
                {/* the value counts in on its cue; the label names the slot from the start */}
                <div style={{ opacity: k, fontFamily: HAI_TYPE.serif, fontSize: T.title, fontWeight: 700, lineHeight: 1,
                  color: isZero ? SPARK_TEXT : CLAUDE.INK }}>{s.value}</div>
                <div style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: -0.5,
                  color: CLAUDE.INK_SOFT, marginTop: 6 }}>{s.label}</div>
              </div>
            );
          })}
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

      {/* ══ what went in, what was asked ═════════════════════════════ */}
      <div style={{
        position: 'absolute', left: PAD_X, top: STRIP_Y, width: CONTENT_W,
        display: 'flex', flexDirection: portrait ? 'column' : 'row',
        gap: portrait ? 10 * U : 40 * U,
      }}>
        {chip('INPUT', input, op(sInput), false)}
        {chip('ASK', ask, op(sAsk), true)}
      </div>

      {/* ══ the monitor ══════════════════════════════════════════════ */}
      <div style={{
        position: 'absolute', left: PAD_X, top: MON_Y, width: MON_W, height: MON_H,
        borderRadius: 16 * U, overflow: 'hidden', background: '#10131F',
        border: `${6 * U}px solid ${CLAUDE.INK}`, boxSizing: 'border-box',
        boxShadow: '0 22px 50px rgba(61,57,41,0.22)',
        opacity: op(sMon), transform: `scale(${0.94 + 0.06 * op(sMon)})`,
      }}>
        {frames.map((f, i) => {
          const start = switches[i] ?? 1;
          const next = switches[i + 1] ?? 2;
          const fadeIn = i === 0 ? 1 : clamp((fr - start) / 0.035, 0, 1);
          const fadeOut = clamp((fr - next) / 0.035, 0, 1);
          const vis = fadeIn * (1 - fadeOut);
          if (vis <= 0) return null;
          const push = interpolate(fr, [start, Math.min(1, next + 0.05)], [1.0, 1.06],
            { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
          return (
            <Img key={i} src={staticFile(f)} style={{
              position: 'absolute', inset: 0, width: '100%', height: '100%',
              objectFit: 'cover', opacity: vis, transform: `scale(${push})`,
            }} />
          );
        })}
        {/* the live-render badge */}
        <div style={{
          position: 'absolute', left: 16 * U, top: 14 * U,
          fontFamily: HAI_TYPE.sans, fontSize: 16 * U, fontWeight: 800, letterSpacing: 2,
          color: '#fff', background: 'rgba(16,19,31,0.72)', borderRadius: 6 * U,
          padding: `${5 * U}px ${10 * U}px`,
        }}>AGENT OUTPUT · 1920 × 1080</div>
      </div>
      <div style={{
        position: 'absolute', left: PAD_X, top: MON_Y + MON_H + 14 * U, width: MON_W,
        fontFamily: HAI_TYPE.serif, fontStyle: 'italic', fontSize: 22 * U,
        color: CLAUDE.INK_SOFT, opacity: op(sMon),
      }}>{credit}</div>

      {/* ══ the results ══════════════════════════════════════════════ */}
      <div style={{
        position: 'absolute',
        left: portrait ? PAD_X : SIDE_X,
        top: portrait ? MON_Y + MON_H + 70 * U : MON_Y,
        width: portrait ? CONTENT_W : SIDE_W,
        display: 'flex', flexDirection: portrait ? 'row' : 'column',
        gap: 20 * U,
      }}>
        {statTiles}
      </div>

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
        height={height} portrait={portrait}
        top={portrait ? height * 0.715 : undefined} />
    </AbsoluteFill>
  );
};
