import React from 'react';
import { AbsoluteFill, Img } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { KEY, NOTES, ProfileBars, PhoneBaseline, Caps, Stat, keyName } from './keys/keyKit';

/**
 * KeyProfiles — B03 of "How Apps Find a Song's Key."
 *
 * Step two: the song's note profile beside the Krumhansl–Kessler (1982) C major profile (the template's
 * shape), then all 24 correlations from key.py (12 major, 12 minor) as bars; the winner (C major, r = 0.98)
 * and the runner-up (G major, 0.72) are marked. Pearson correlation is typeset (typeset_math.py).
 *
 *   two / template / listeners / shape / slides / corr / cmaj / rival
 */

export const keyProfilesSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default("Step Two: Match a Key's Shape"),
  sparkLine: z.string().default('The closest shape names the key.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type KeyProfilesProps = z.infer<typeof keyProfilesSchema>;

export const KeyProfiles: React.FC<KeyProfilesProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tTwo = at('two', 0.0), tTemp = at('template', 0.08), tShape = at('shape', 0.3), tSlides = at('slides', 0.45);
  const tCorr = at('corr', 0.6), tCmaj = at('cmaj', 0.72), tRival = at('rival', 0.85);
  const headIn = sp(0);
  const sSong = sp(tTwo), sTemp = sp(tTemp), sShape = sp(tShape), grow = ramp(tSlides, tSlides + 0.12), sCorr = sp(tCorr);
  const sCmaj = sp(tCmaj), sRival = sp(tRival);
  const sparkIn = sp(clamp(Math.min(tRival + 0.05, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;

  const r = KEY.pop.r as number[];
  const kkMaj = KEY.kk.major as number[];
  const order = r.map((v, i) => [v, i]).sort((a, b) => b[0] - a[0]).map((x) => x[1]);
  const best = order[0], rival = order[1];   // the run's winner and runner-up (C major, G major)

  const PW = portrait ? (CW - 40) / 2 : CW * 0.26, PH = portrait ? height * 0.085 : height * 0.17;
  const profiles = (
    <div style={{ display: 'flex', gap: portrait ? 40 : 40 * U }}>
      <div style={{ opacity: op(sSong) }}>
        <Caps size={lbl} color={CLAUDE.INK} style={{ marginBottom: 10 }}>THE SONG</Caps>
        <ProfileBars values={KEY.pop.profile as number[]} w={PW} h={PH} size={lbl * 0.62} labels={!portrait} />
      </div>
      <div style={{ opacity: op(sTemp) }}>
        <Caps size={lbl} color={CLAUDE.INK} style={{ marginBottom: 10 }}>{portrait ? 'C MAJOR SHAPE' : 'C MAJOR TEMPLATE (1982)'}</Caps>
        <ProfileBars values={kkMaj} w={PW} h={PH} size={lbl * 0.62} labels={!portrait} color={CLAUDE.GHOST} />
      </div>
    </div>
  );
  const CWID = portrait ? CW : CW * 0.6, CH = portrait ? height * 0.14 : height * 0.28;
  const bw = CWID / 24;
  const corr = (
    <svg width={CWID} height={CH + lbl * 2} style={{ overflow: 'visible', display: 'block', opacity: 0.5 + 0.5 * op(sShape) }}>
      <line x1={0} x2={CWID} y1={CH} y2={CH} stroke={CLAUDE.INK_SOFT} strokeWidth={2} />
      {r.map((v, i) => {
        const k = clamp(grow * 24 - i, 0, 1);
        const bh = Math.max(0, v) * CH * k;
        const isBest = i === best && op(sCmaj) > 0.5, isRival = i === rival && op(sRival) > 0.5;
        return <React.Fragment key={i}><rect x={i * bw + bw * 0.15} y={CH - Math.max(0, v) * CH} width={bw * 0.7} height={Math.max(0, v) * CH} fill={CLAUDE.BORDER} />
          <rect x={i * bw + bw * 0.15} y={CH - bh} width={bw * 0.7} height={bh}
          fill={isBest ? SPARK_TEXT : isRival ? CLAUDE.INK : CLAUDE.GHOST} opacity={i === best || i === rival ? 1 : 0.7} /></React.Fragment>;
      })}
      <text x={0} y={CH + lbl * 1.4} fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={CLAUDE.INK_SOFT}>12 MAJOR KEYS</text>
      <text x={CWID} y={CH + lbl * 1.4} textAnchor="end" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={CLAUDE.INK_SOFT}>12 MINOR KEYS</text>
    </svg>
  );
  const big = portrait ? T.title * 1.0 : 72 * U;
  const stats = (dir: 'row' | 'column') => (
    <div style={{ display: 'flex', flexDirection: dir, gap: dir === 'row' ? 0 : 30 * U, justifyContent: 'space-between', width: dir === 'row' ? CW : undefined }}>
      <Stat value={r[best].toFixed(2)} label={keyName(best).toUpperCase()} size={big} opacity={(dir === 'row' ? 0 : 0.25) + (dir === 'row' ? 1 : 0.75) * op(sCmaj)} accent />
      <Stat value={r[rival].toFixed(2)} label={`${keyName(rival).toUpperCase()}, NEXT BEST`} size={big} opacity={(dir === 'row' ? 0 : 0.25) + (dir === 'row' ? 1 : 0.75) * op(sRival)} />
    </div>
  );
  const eq = KEY.eq.corr as { src: string; aspect: number };

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.205 }}>{profiles}</div>
        <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: height * 0.375, opacity: op(sShape) }}>MATCH WITH ALL 24 KEYS</Caps>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.41 }}>{corr}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.62 }}>{stats('row')}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{profiles}</div>
      <Caps size={lbl} color={CLAUDE.INK} style={{ position: 'absolute', left: PAD_X, top: height * 0.52, opacity: op(sShape) }}>HOW WELL THE SONG MATCHES EACH OF THE 24 KEYS</Caps>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.56 }}>{corr}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.66, top: height * 0.25, display: 'flex', flexDirection: 'column', gap: 34 * U }}>
        <div style={{ opacity: 0.35 + 0.65 * op(sCorr) }}>
          <Caps size={lbl} style={{ marginBottom: 10 * U }}>CORRELATION</Caps>
          <Img src={eq.src} style={{ height: 96 * U, width: Math.min(CW * 0.34, 96 * U * eq.aspect), objectFit: 'contain', objectPosition: 'left' }} />
        </div>
        {stats('column')}
      </div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
