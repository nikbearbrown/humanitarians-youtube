import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { KEY, ProfileBars, PhoneBaseline, Caps, Stat, Chip } from './keys/keyKit';

/**
 * KeyRelative — B05 of "How Apps Find a Song's Key."
 *
 * The catch (key.py): the A minor ballad's note profile, and its two closest keys as a near tie: C major
 * 0.891 against A minor 0.886 (the run's values). Then the counts: 10 of 12 natural-minor ballads came out as
 * the relative major; 12 of 12 with the raised seventh came out right; and the MIREX scoring's partial credit
 * (0.3) for a relative-key answer.
 *
 *   misses / natural / ten / amin / cmaj / raise / credit
 */

export const keyRelativeSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Same Notes, Wrong Home'),
  sparkLine: z.string().default('A minor and C major share every note.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type KeyRelativeProps = z.infer<typeof keyRelativeSchema>;

export const KeyRelative: React.FC<KeyRelativeProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tMiss = at('misses', 0.0), tNat = at('natural', 0.12), tTen = at('ten', 0.25), tAm = at('amin', 0.37);
  const tCm = at('cmaj', 0.48), tRaise = at('raise', 0.62), tCredit = at('credit', 0.85);
  const headIn = sp(0);
  const sProf = sp(tNat), sTen = sp(tTen), sAm = sp(tAm), sCm = sp(tCm), sRaise = sp(tRaise), sCredit = sp(Math.min(tCredit, 0.88));
  const sparkIn = sp(clamp(Math.min(tCredit + 0.03, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;

  const rm = KEY.minor.r as number[];
  const am = rm[21], cm = rm[0];
  const summ = KEY.summary as any;
  const relN = summ.minor.counts.relative ?? 0;
  const harmRight = summ.harmonic.counts.right ?? 0;

  // the near tie, drawn on a zoomed axis so the gap is visible, with the axis range printed
  const LO = 0.86, HI = 0.9;
  const BW = portrait ? CW : CW * 0.5, BH = portrait ? 64 : 62 * U;
  const bar = (label: string, v: number, o: number, accent: boolean) => (
    <div style={{ opacity: o }}>
      <Caps size={lbl} color={accent ? SPARK_TEXT : CLAUDE.INK} style={{ marginBottom: 8 }}>{label}</Caps>
      <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 20 : 20 * U }}>
        <div style={{ width: BW * 0.78, height: BH, background: CLAUDE.BORDER, borderRadius: 8, overflow: 'hidden' }}>
          <div style={{ width: `${clamp((v - LO) / (HI - LO), 0, 1) * 100}%`, height: '100%', background: accent ? SPARK_TEXT : CLAUDE.INK }} />
        </div>
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body : 46 * U, fontWeight: 700, color: accent ? SPARK_TEXT : CLAUDE.INK }}>{v.toFixed(3)}</div>
      </div>
    </div>
  );
  const PW = portrait ? CW : CW * 0.4, PH = portrait ? height * 0.1 : height * 0.22;
  const prof = (
    <div style={{ opacity: op(sProf) }}>
      <Caps size={lbl} color={CLAUDE.INK} style={{ marginBottom: 10 }}>{portrait ? 'A MINOR BALLAD' : 'MY A MINOR BALLAD: ITS NOTE PROFILE'}</Caps>
      <ProfileBars values={KEY.minor.profile as number[]} w={PW} h={PH} size={portrait ? lbl * 0.9 : lbl} />
    </div>
  );
  const big = portrait ? T.title * 1.0 : 66 * U;
  const counts = (dir: 'row' | 'column') => (
    <div style={{ display: 'flex', flexDirection: dir, gap: dir === 'row' ? 0 : 26 * U, justifyContent: 'space-between', width: dir === 'row' ? CW : undefined }}>
      <Stat value={`${relN} / 12`} label={portrait ? 'BALLADS: RELATIVE MAJOR' : 'MINOR BALLADS CALLED THE RELATIVE MAJOR'} size={big} opacity={op(sTen)} accent />
      <Stat value={`${harmRight} / 12`} label={portrait ? 'RAISED 7TH: RIGHT' : 'WITH THE SEVENTH RAISED: RIGHT'} size={big} opacity={op(sRaise)} />
    </div>
  );
  const credit = <div style={{ opacity: op(sCredit) }}><Chip text={portrait ? 'STANDARD TEST: 0.3 CREDIT' : 'MIREX TEST: A RELATIVE KEY EARNS 0.3'} size={portrait ? T.label * 0.74 : 22 * U} /></div>;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.2 }}>{prof}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.39, display: 'flex', flexDirection: 'column', gap: 22 }}>
          {bar('C MAJOR', cm, op(sCm), true)}
          {bar('A MINOR (RIGHT)', am, op(sAm), false)}
        </div>
        <Caps size={lbl * 0.85} style={{ position: 'absolute', left: PAD_X, top: height * 0.588, opacity: op(sCm) }}>{`AXIS ${LO.toFixed(2)} TO ${HI.toFixed(2)}`}</Caps>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.625 }}>{counts('row')}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.735 }}>{credit}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{prof}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.58, display: 'flex', flexDirection: 'column', gap: 22 * U }}>
        {bar('C MAJOR (CHOSEN)', cm, op(sCm), true)}
        {bar('A MINOR (THE RIGHT KEY)', am, op(sAm), false)}
        <Caps size={lbl * 0.85} style={{ opacity: op(sCm) }}>{`AXIS ${LO.toFixed(2)} TO ${HI.toFixed(2)}`}</Caps>
      </div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.58, top: height * 0.27 }}>{counts('column')}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.58, top: height * 0.68 }}>{credit}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
