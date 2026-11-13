import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { KEY, NOTES, PhoneBaseline, Caps, Stat } from './keys/keyKit';

/**
 * KeyGrid — B04 of "How Apps Find a Song's Key."
 *
 * The whole test set (key.py): 5 Western styles x 12 tonics, one square per song. Ink = right; terracotta =
 * the relative major/minor (same seven notes); grey = anything else (there is none in this run, but the legend
 * keeps the scale honest). Rows fill on the style names; then the total.
 *
 *   built / sixty / styles / fifty / every
 */

export const keyGridSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Sixty Songs, Fifty Right'),
  sparkLine: z.string().default('Pop, rock and blues: all right.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type KeyGridProps = z.infer<typeof keyGridSchema>;

const ORDER = ['pop', 'rock', 'blues', 'harmonic', 'minor'];
const NAME: Record<string, string> = { pop: 'POP', rock: 'ROCK (FLAT 7TH)', blues: '12-BAR BLUES', harmonic: 'MINOR, RAISED 7TH', minor: 'MINOR BALLAD' };
const SHORT: Record<string, string> = { pop: 'POP', rock: 'ROCK', blues: 'BLUES', harmonic: 'MINOR, RAISED 7', minor: 'MINOR BALLAD' };

export const KeyGrid: React.FC<KeyGridProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tBuilt = at('built', 0.0), tSixty = at('sixty', 0.1), tStyles = at('styles', 0.25), tFifty = at('fifty', 0.6), tEvery = at('every', 0.85);
  const headIn = sp(0);
  const sGrid = sp(tSixty), fill = ramp(tStyles, Math.min(tFifty, tStyles + 0.3)), sFifty = sp(tFifty), sEvery = sp(tEvery);
  const sparkIn = sp(clamp(Math.min(tEvery + 0.04, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const rows = KEY.rows as any[];
  const all = KEY.all as Record<string, number>;
  const right = all.right ?? 0;
  const prb = rows.filter((r) => ['pop', 'rock', 'blues'].includes(r.style));
  const prbRight = prb.filter((r) => r.relation === 'right').length;

  const size = portrait ? 54 : 54 * U, gap = portrait ? 9 : 9 * U, nameW = portrait ? 0 : 330 * U;
  const square = (r: any, on: number) => {
    const c = r.relation as string, lit = on > 0.5;
    return <div key={r.tonic} style={{ width: size, height: size, borderRadius: size * 0.16, boxSizing: 'border-box',
      background: !lit ? CLAUDE.BORDER : c === 'right' ? CLAUDE.INK : c === 'relative' ? SPARK_TEXT : CLAUDE.BORDER,
      border: `${Math.max(3, size * 0.08)}px solid ${!lit ? CLAUDE.BORDER : c === 'right' ? CLAUDE.INK : c === 'relative' ? SPARK_TEXT : CLAUDE.GHOST}`,
      transform: `scale(${0.85 + 0.15 * on})` }} />;
  };
  const grid = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 26 : 18 * U, opacity: op(sGrid) }}>
      {!portrait ? (
        <div style={{ display: 'flex', alignItems: 'center', gap: gap * 2 }}>
          <div style={{ width: nameW }} />
          <div style={{ display: 'flex', gap }}>{NOTES.map((n) => <div key={n} style={{ width: size, textAlign: 'center', fontFamily: HAI_TYPE.sans, fontWeight: 800, fontSize: lbl * 0.85, color: CLAUDE.INK_SOFT }}>{n}</div>)}</div>
        </div>) : null}
      {ORDER.map((s, si) => {
        const on = clamp(fill * ORDER.length - si, 0, 1);
        const rs = rows.filter((r) => r.style === s).sort((a, b) => a.tonic - b.tonic);
        const ok = rs.filter((r) => r.relation === 'right').length;
        return (
          <div key={s} style={{ display: 'flex', flexDirection: portrait ? 'column' : 'row', alignItems: portrait ? 'flex-start' : 'center', gap: portrait ? 8 : gap * 2 }}>
            <Caps size={lbl} color={s === 'minor' && on > 0.5 ? SPARK_TEXT : CLAUDE.INK} style={{ width: portrait ? undefined : nameW }}>
              {portrait ? `${SHORT[s]} · ${ok}/12` : NAME[s]}</Caps>
            <div style={{ display: 'flex', gap: portrait ? 6 : gap }}>{rs.map((r) => square(r, on))}</div>
            {!portrait ? <Caps size={lbl} color={s === 'minor' ? SPARK_TEXT : CLAUDE.INK_SOFT} style={{ opacity: on }}>{ok} / 12</Caps> : null}
          </div>
        );
      })}
    </div>
  );
  const legend = (
    <div style={{ display: 'flex', gap: lbl * 1.3, opacity: op(sGrid), fontFamily: HAI_TYPE.sans, fontSize: lbl * 0.9, fontWeight: 800, letterSpacing: 1, color: CLAUDE.INK_SOFT }}>
      {[['RIGHT KEY', CLAUDE.INK, CLAUDE.INK], [portrait ? 'OTHER HOME' : 'SAME NOTES, OTHER HOME', SPARK_TEXT, SPARK_TEXT]].map(([l, bg, bd]) => (
        <span key={l} style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <span style={{ width: lbl, height: lbl, background: bg, border: `3px solid ${bd}`, boxSizing: 'border-box', borderRadius: 4, display: 'inline-block' }} />{l}</span>
      ))}
    </div>
  );
  const big = portrait ? T.title * 1.1 : 84 * U;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.2 }}>{grid}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.59 }}>{legend}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.645 }}>
          <Stat value={`${right} / ${rows.length}`} label="RIGHT KEY" size={big} opacity={op(sFifty)} accent />
        </div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.26 }}>{grid}</div>
      <div style={{ position: 'absolute', left: PAD_X + nameW + gap * 2, top: height * 0.75 }}>{legend}</div>
      <div style={{ position: 'absolute', right: PAD_X, top: height * 0.3, opacity: 0.3 + 0.7 * op(sFifty) }}>
        <Stat value={`${right} / ${rows.length}`} label="RIGHT KEY" size={big} opacity={1} accent />
      </div>
      <div style={{ position: 'absolute', right: PAD_X, top: height * 0.5, opacity: 0.3 + 0.7 * op(sEvery) }}>
        <Stat value={`${prbRight} / ${prb.length}`} label="POP, ROCK, BLUES" size={big * 0.75} opacity={1} />
      </div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
