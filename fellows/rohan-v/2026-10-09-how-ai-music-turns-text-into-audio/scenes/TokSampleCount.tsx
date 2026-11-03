import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { TOK, Stat, PhoneBaseline, Chip, Label, fmt } from './tokens/tokKit';

/**
 * TokSampleCount — B01 of "How AI Music Generators Turn Text Into Audio."
 *
 * Four milliseconds of the codec's test piece, as the numbers it really is: each sample a stem and
 * a dot (96 of them at 24 kHz), with the first values printed. Then the counts: a CD's 44,100
 * numbers per second per ear (verified rate), and the 15,876,000 numbers of a three-minute stereo
 * song (computed in export_tok_data.py). The squeeze arrow points at the next beat.
 *
 *   problem  "Here's the problem"       panel
 *   list     "long list of numbers"     stems draw, values print
 *   cd       "A CD stores"              per-second stat
 *   song     "A three-minute song"      song stat
 *   many     "far too many"             chip
 *   squeezed "squeezed into a much shorter list"  arrow
 */

export const tokSampleCountSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Audio Is a Lot of Numbers'),
  sparkLine: z.string().default('Sixteen million numbers is too many to predict.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type TokSampleCountProps = z.infer<typeof tokSampleCountSchema>;

export const TokSampleCount: React.FC<TokSampleCountProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tProb = at('problem', 0.02), tList = at('list', 0.1), tCd = at('cd', 0.27), tSong = at('song', 0.5);
  const tMany = at('many', 0.66), tSq = at('squeezed', 0.82);
  const headIn = sp(0);
  const sPanel = sp(tProb), draw = ramp(tList, tList + 0.12), sCd = sp(tCd), sSong = sp(tSong), sMany = sp(tMany), sSq = sp(tSq);
  const sparkIn = sp(clamp(tSq + 0.06, 0, 0.97));

  const s: number[] = TOK.wave.samples;
  const amax = Math.max(...s.map(Math.abs)) * 1.1;
  const PW = portrait ? CW : CW * 0.58, PH = portrait ? height * 0.2 : height * 0.36;
  const PX = PAD_X, PY = portrait ? height * 0.23 : height * 0.3;
  const lbl = portrait ? T.label * 0.72 : 22 * U;
  const n = s.length;
  const shown = Math.round(draw * n);
  const R = portrait ? 6 : 5 * U;

  const panel = (
    <>
      <svg width={PW} height={PH} style={{ position: 'absolute', left: PX, top: PY, overflow: 'visible', opacity: op(sPanel) }}>
        <rect x={0} y={0} width={PW} height={PH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
        <line x1={0} x2={PW} y1={PH / 2} y2={PH / 2} stroke={CLAUDE.GHOST} strokeWidth={2} />
        {s.slice(0, shown).map((v, i) => {
          const x = ((i + 0.5) / n) * PW, y = PH / 2 - (v / amax) * (PH / 2);
          return <g key={i}><line x1={x} x2={x} y1={PH / 2} y2={y} stroke={CLAUDE.INK_SOFT} strokeWidth={2} />
            <circle cx={x} cy={y} r={R} fill={SPARK_TEXT} /></g>;
        })}
      </svg>
      <Label text={portrait ? '4 MS OF MUSIC · 96 NUMBERS' : '4 MILLISECONDS OF MY TEST MUSIC · 96 NUMBERS'} size={lbl} opacity={op(sPanel)}
        style={{ position: 'absolute', left: PX, top: PY - lbl * 1.7 }} />
      <div style={{ position: 'absolute', left: PX, top: PY + PH + lbl * 0.9, display: 'flex', gap: lbl * 0.8, flexWrap: 'wrap', width: PW,
        fontFamily: HAI_TYPE.mono, fontSize: lbl * 1.05, fontWeight: 700, color: CLAUDE.INK, opacity: op(sPanel) }}>
        {s.slice(0, portrait ? 6 : 8).map((v, i) => <span key={i} style={{ opacity: clamp(draw * n - i, 0, 1) }}>{v.toFixed(3)}</span>)}
        <span style={{ opacity: draw, color: CLAUDE.INK_SOFT }}>…</span>
      </div>
    </>
  );
  const stats = (size: number, gap: number) => (
    <div style={{ display: 'flex', flexDirection: 'column', gap }}>
      <Stat value={fmt(44100)} label={portrait ? 'PER SECOND, PER EAR (CD)' : 'NUMBERS PER SECOND, FOR EACH EAR, ON A CD'} size={size} opacity={op(sCd)} />
      <Stat value={fmt(TOK.derived.songSamples)} label={portrait ? 'IN A 3-MINUTE SONG' : 'NUMBERS IN A THREE-MINUTE STEREO SONG'} size={size} opacity={op(sSong)} accent />
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {panel}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.53 }}>{stats(T.title * 1.0, 30)}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.715, opacity: op(sMany) }}>
          <Chip text={op(sSq) > 0.5 ? 'SQUEEZE IT FIRST →' : 'TOO MANY TO PREDICT'} size={T.label * 0.8} accent />
        </div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      {panel}
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.64, top: PY }}>{stats(60 * U, 34 * U)}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.64, top: PY + PH + 30 * U, opacity: op(sMany) }}>
        <Chip text="TOO MANY TO PREDICT ONE BY ONE" size={22 * U} accent />
      </div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.64, top: PY + PH + 100 * U, opacity: op(sSq),
        fontFamily: HAI_TYPE.sans, fontSize: 26 * U, fontWeight: 800, letterSpacing: 1.2, color: SPARK_TEXT }}>→ SQUEEZE IT INTO A SHORTER LIST</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
