import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { TMP, Chip, PhoneBaseline, Caps, Stat } from './tempo/tmpKit';

/**
 * TempoGrid — B05 of "How Apps Find a Song's Tempo."
 *
 * The whole test set with the 120 preference on (tempo.py): 8 Western styles x 5 tempos, one
 * square per groove. Ink = right (within 4%), terracotta fill = exactly half, terracotta outline =
 * exactly double, grey = another repeat altogether. The rows the narration names fill first
 * (ballads double, drum and bass half, funk other), then the rest; then the totals, and the
 * librosa cross-check (same verdict on 34 of 40), with librosa's own mark (LOGO LAW).
 *
 *   cuts / ballad / dnb / funk / all / octave / librosa / name / tests
 */

export const tempoGridSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Right, Double or Half'),
  sparkLine: z.string().default('Off by exactly double or half: an octave error.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type TempoGridProps = z.infer<typeof tempoGridSchema>;

const ORDER = ['rock', 'funk', 'house', 'hiphop', 'ballad', 'dnb', 'waltz', 'swing'];
const NAME: Record<string, string> = { rock: 'ROCK', funk: 'FUNK', house: 'HOUSE', hiphop: 'HIP HOP', ballad: 'SLOW BALLAD',
  dnb: 'DRUM AND BASS', waltz: 'WALTZ (3/4)', swing: 'JAZZ SWING' };

export const TempoGrid: React.FC<TempoGridProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tCuts = at('cuts', 0.0), tBallad = at('ballad', 0.08), tDnb = at('dnb', 0.2), tFunk = at('funk', 0.33), tAll = at('all', 0.45);
  const tOct = at('octave', 0.55), tLib = at('librosa', 0.7), tName = at('name', 0.82), tTests = at('tests', 0.92);
  const headIn = sp(0);
  const sGrid = sp(tCuts);
  const fillAt: Record<string, number> = { ballad: tBallad, dnb: tDnb, funk: tFunk };
  const sAll = sp(tAll), sOct = sp(tOct), sLib = sp(tLib), sName = sp(tName), sTests = sp(tTests);
  const sparkIn = sp(clamp(tTests + 0.03, 0, 0.97));
  const lbl = portrait ? T.label * 0.7 : 22 * U;

  const rows = TMP.rows as any[];
  const S = TMP.summary as any;
  const note: Record<string, string> = { ballad: 'ALL DOUBLE', dnb: 'ALL HALF', funk: 'ANOTHER REPEAT' };

  const square = (r: any, on: number, size: number) => {
    const c = r.prior_class as string;
    const lit = on > 0.5;
    const right = c === 'right', half = c === 'half', dbl = c === 'double';
    return <div key={r.bpm} style={{ width: size, height: size, borderRadius: size * 0.18, boxSizing: 'border-box',
      background: !lit ? 'transparent' : right ? CLAUDE.INK : half ? SPARK_TEXT : dbl ? 'transparent' : CLAUDE.BORDER,
      border: `${Math.max(3, size * 0.12)}px solid ${!lit ? CLAUDE.BORDER : right ? CLAUDE.INK : half || dbl ? SPARK_TEXT : CLAUDE.GHOST}`,
      transform: `scale(${0.85 + 0.15 * on})` }} />;
  };
  const grid = (size: number, gap: number, nameW: number, rowGap: number, noteSize: number) => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: rowGap, opacity: op(sGrid) }}>
      {ORDER.map((s) => {
        const t = fillAt[s];
        const on = t !== undefined ? ramp(t, t + 0.04) : ramp(tAll, tAll + 0.05);
        const rs = rows.filter((r) => r.style === s);
        return (
          <div key={s} style={{ display: 'flex', alignItems: 'center', gap: gap * 2 }}>
            <Caps size={portrait ? T.label * 0.62 : lbl} color={t !== undefined && on > 0.5 ? SPARK_TEXT : CLAUDE.INK} style={{ width: nameW, lineHeight: 1.15 }}>{NAME[s]}</Caps>
            <div style={{ display: 'flex', gap }}>{rs.map((r) => square(r, on, size))}</div>
            {note[s] && !portrait ? <Caps size={noteSize} color={SPARK_TEXT} style={{ opacity: on }}>{note[s]}</Caps> : null}
          </div>
        );
      })}
    </div>
  );
  const legend = (size: number) => (
    <div style={{ display: 'flex', gap: size * 1.2, flexWrap: 'wrap', opacity: op(sGrid), fontFamily: HAI_TYPE.sans, fontSize: size, fontWeight: 800, letterSpacing: 1, color: CLAUDE.INK_SOFT }}>
      {[['RIGHT', CLAUDE.INK, CLAUDE.INK], ['HALF', SPARK_TEXT, SPARK_TEXT], ['DOUBLE', 'transparent', SPARK_TEXT], ['OTHER', CLAUDE.BORDER, CLAUDE.GHOST]].map(([l, bg, bd]) => (
        <span key={l} style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <span style={{ width: size, height: size, background: bg, border: `3px solid ${bd}`, boxSizing: 'border-box', borderRadius: 4, display: 'inline-block' }} />{l}</span>
      ))}
    </div>
  );
  const big = portrait ? T.title * 1.2 : 72 * U;
  const ag = S.agreement;
  const totals = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? height * 0.016 : 26 * U }}>
      <Stat value={`${S.prior.acc1} / ${S.prior.n}`} label="EXACTLY RIGHT" size={big} opacity={op(sAll)} />
      <Stat value={`${S.prior.acc2} / ${S.prior.n}`} label={portrait ? 'RIGHT, DOUBLE OR HALF' : 'RIGHT, OR EXACTLY DOUBLE OR HALF'} size={big} opacity={op(sOct)} accent />
      <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 18 : 16 * U, opacity: op(sLib) }}>
        <Img src={staticFile(TMP.logo.librosa)} style={{ height: 230 * U, width: 230 * U, margin: `${-70 * U}px ${-24 * U}px` }} />
        <Stat value={`${ag.same_class} / ${ag.n}`} label="SAME VERDICT FROM LIBROSA" size={big * 0.8} opacity={1} />
      </div>
    </div>
  );
  const chips = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 18 : 14 * U, alignItems: 'flex-start' }}>
      <div style={{ opacity: op(sName) }}><Chip text="THE OCTAVE ERROR" size={portrait ? T.label * 0.8 : 26 * U} accent /></div>
      <div style={{ opacity: op(sTests) }}><Chip text={portrait ? 'TESTS SCORE IT SEPARATELY' : 'STANDARD TESTS SCORE IT SEPARATELY'} size={portrait ? T.label * 0.66 : 22 * U} /></div>
    </div>
  );

  if (portrait) {
    const pb = T.title * 0.95;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.2 }}>{grid(36, 9, 470, 6, T.label * 0.62)}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.448 }}>{legend(lbl * 0.85)}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.49, width: CW, display: 'flex', justifyContent: 'space-between' }}>
          <Stat value={`${S.prior.acc1} / ${S.prior.n}`} label="EXACTLY RIGHT" size={pb} opacity={op(sAll)} />
          <Stat value={`${S.prior.acc2} / ${S.prior.n}`} label="RIGHT, DOUBLE OR HALF" size={pb} opacity={op(sOct)} accent />
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.595, display: 'flex', alignItems: 'center', gap: 22, opacity: op(sLib) }}>
          <Img src={staticFile(TMP.logo.librosa)} style={{ height: 270, width: 270, margin: '-85px -30px' }} />
          <Stat value={`${ag.same_class} / ${ag.n}`} label="SAME VERDICT, LIBROSA" size={pb} opacity={1} />
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.69 }}>{chips}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.255 }}>{grid(40 * U, 10 * U, 250 * U, 14 * U, 20 * U)}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.8 }}>{legend(20 * U)}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.6, top: height * 0.255 }}>{totals}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.6, top: height * 0.74 }}>{chips}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
