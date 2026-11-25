import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { Caps, PhoneBaseline, LandBaseline, SpotifyTag, Tiles } from './recs/recsKit';

/**
 * RecsSignals — B01 of "How Spotify Picks Songs."
 *
 * What Spotify says it learns from (facts-recs.md §1): your taste profile, built from what you search, play, skip
 * and save; no star ratings; and the habits of people with similar taste (collaborative filtering). The four
 * signals are drawn as shapes; the two listener rows show the idea of "similar taste": they share four songs,
 * so the song only one of them played becomes the other's recommendation. The rows are an illustration.
 *
 *   profile / search / skip / stars / similar / cf
 */

export const recsSignalsSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · TECH CONCEPTS'),
  title: z.string().default('It Learns From What You Do'),
  sparkLine: z.string().default('No ratings. Just plays, skips and saves.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type RecsSignalsProps = z.infer<typeof recsSignalsSchema>;

const Icon: React.FC<{ kind: 'search' | 'play' | 'skip' | 'save'; size: number; color: string }> = ({ kind, size, color }) => {
  const s = size;
  return (
    <svg width={s} height={s} viewBox="0 0 100 100" style={{ display: 'block' }}>
      {kind === 'search' && <><circle cx="42" cy="42" r="24" fill="none" stroke={color} strokeWidth="10" /><line x1="60" y1="60" x2="82" y2="82" stroke={color} strokeWidth="12" strokeLinecap="round" /></>}
      {kind === 'play' && <path d="M32 20 L80 50 L32 80 Z" fill={color} />}
      {kind === 'skip' && <><path d="M22 22 L62 50 L22 78 Z" fill={color} /><rect x="66" y="22" width="12" height="56" rx="3" fill={color} /></>}
      {kind === 'save' && <path d="M50 84 C 20 62 12 46 12 34 C 12 22 22 14 32 14 C 40 14 46 18 50 26 C 54 18 60 14 68 14 C 78 14 88 22 88 34 C 88 46 80 62 50 84 Z" fill={color} />}
    </svg>
  );
};

export const RecsSignals: React.FC<RecsSignalsProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tProf = at('profile', 0.02), tSearch = at('search', 0.12), tSkip = at('skip', 0.2), tStars = at('stars', 0.35);
  const tSim = at('similar', 0.58), tCf = at('cf', 0.8);
  const headIn = sp(0);
  const sProf = sp(tProf), sStars = sp(tStars), sSim = sp(tSim), sRec = sp(Math.min(tSim + 0.08, 0.9)), sCf = sp(tCf);
  const sig = [sp(tSearch), sp(tSearch + 0.03), sp(tSkip), sp(tSkip + 0.03)];
  const sparkIn = sp(clamp(Math.min(tCf + 0.05, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const ic = portrait ? 120 : 92 * U;

  const kinds: ['search' | 'play' | 'skip' | 'save', string][] = [['search', 'SEARCH'], ['play', 'PLAY'], ['skip', 'SKIP'], ['save', 'SAVE']];
  const signals = (
    <div style={{ display: 'flex', gap: portrait ? 34 : 40 * U }}>
      {kinds.map(([k, l], i) => (
        <div key={k} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: portrait ? 14 : 12 * U, opacity: 0.25 + 0.75 * op(sig[i]),
          transform: `translateY(${(1 - op(sig[i])) * 14}px)` }}>
          <div style={{ width: ic * 1.5, height: ic * 1.5, borderRadius: ic * 0.4, background: CLAUDE.CARD, border: `1.5px solid ${CLAUDE.BORDER}`,
            display: 'flex', alignItems: 'center', justifyContent: 'center' }}><Icon kind={k} size={ic} color={k === 'skip' ? SPARK_TEXT : CLAUDE.INK} /></div>
          <Caps size={lbl} color={CLAUDE.INK}>{l}</Caps>
        </div>
      ))}
    </div>
  );
  const st = portrait ? 64 : 52 * U;
  const stars = (
    <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 24 : 22 * U, opacity: 0.25 + 0.75 * op(sStars) }}>
      <div style={{ position: 'relative' }}>
        <svg width={st * 5.6} height={st} viewBox="0 0 560 100">
          {Array.from({ length: 5 }, (_, i) => (
            <path key={i} transform={`translate(${i * 112} 0)`} d="M50 6 L62 38 L96 38 L68 58 L79 92 L50 72 L21 92 L32 58 L4 38 L38 38 Z" fill={CLAUDE.GHOST} />
          ))}
          <line x1="0" y1="54" x2={560 * op(sStars)} y2="46" stroke={SPARK_TEXT} strokeWidth="10" strokeLinecap="round" />
        </svg>
      </div>
      <Caps size={lbl} color={SPARK_TEXT}>NO STAR RATINGS</Caps>
    </div>
  );
  const tile = portrait ? 66 : 54 * U, gap = portrait ? 12 : 10 * U;
  const listeners = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 22 : 20 * U, opacity: 0.25 + 0.75 * op(sSim) }}>
      <Caps size={lbl} color={CLAUDE.INK}>PEOPLE WITH SIMILAR TASTE</Caps>
      {[0, 1].map((r) => (
        <div key={r} style={{ display: 'flex', alignItems: 'center', gap: portrait ? 20 : 20 * U }}>
          <Caps size={lbl} style={{ width: portrait ? 340 : 200 * U }}>{r === 0 ? 'LISTENER A' : 'LISTENER B'}</Caps>
          <Tiles n={6} size={tile} gap={gap} hidden={r === 0 ? [5] : []} accent={r === 1 && op(sRec) > 0.5 ? [5] : []} />
          {r === 0 && !portrait ? <div style={{ opacity: op(sRec) }}><Caps size={lbl} color={SPARK_TEXT}>RECOMMEND TO A</Caps></div> : null}
        </div>
      ))}
      {portrait ? <div style={{ opacity: op(sRec) }}><Caps size={lbl} color={SPARK_TEXT}>B'S SONG GOES TO A</Caps></div> : null}
    </div>
  );
  const cf = (
    <div style={{ opacity: op(sCf), fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.body * 1.02 : 46 * U, color: CLAUDE.INK }}>
      collaborative filtering
    </div>
  );
  const tag = <div style={{ opacity: 0.3 + 0.7 * op(sProf) }}><SpotifyTag size={lbl} label={portrait ? 'SPOTIFY: TASTE PROFILE' : 'SPOTIFY SAYS: YOUR TASTE PROFILE'} /></div>;

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.178, width: CW, height: height * 0.667, display: 'flex', flexDirection: 'column', justifyContent: 'space-evenly' }}>
          <div>{tag}</div>
          <div>{signals}</div>
          <div>{stars}</div>
          <div>{listeners}</div>
          <div>{cf}</div>
        </div>
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{tag}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.32 }}>{signals}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.62 }}>{stars}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.52, top: height * 0.32 }}>{listeners}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.52, top: height * 0.62 }}>{cf}</div>
      <LandBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
