import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { SHZ, PhoneBaseline, Chip, listening, histBars, fmt } from './shazam/shzKit';

/**
 * ShazamMatch — B04 of "How Shazam Finds a Song."
 *
 * The test, as run: a library of six synthetic songs (and its hash count), the query card (5 s of
 * Song C from 12.0 s, cafe noise as loud as the music, phone band 150-4,000 Hz, and its hash
 * count), then each song's histogram of offset votes on one shared scale. Song C spikes at
 * 12.00 s; the others stay flat. The beat's audio then plays the noisy clip and the original, and
 * the card being heard is lit. Every count is the run's.
 *
 *   built   "So I built one"        frame
 *   six     "six songs from scratch" song cards
 *   indexed "indexed them"          library hash count
 *   took    "five seconds of Song C" query card
 *   buried  "buried it in cafe noise" noise line
 *   votes   "thirty-three votes"    histograms grow, winner lit
 *   next    "The next best song"    runner-up label
 *   listen  (props.listen)          now-playing chip
 */

export const shazamMatchSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('I Built One and Tested It'),
  sparkLine: z.string().default('Thirty-three votes against two.'),
  listen: z.array(z.object({ label: z.string(), from: z.number(), to: z.number() })).optional(),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type ShazamMatchProps = z.infer<typeof shazamMatchSchema>;

export const ShazamMatch: React.FC<ShazamMatchProps> = ({ eyebrow, title, sparkLine, listen, cues }) => {
  const { frame, D, width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tSix = at('six', 0.05), tIdx = at('indexed', 0.15), tTook = at('took', 0.24), tBur = at('buried', 0.33);
  const tVotes = at('votes', 0.48), tNext = at('next', 0.58), tListen = at('listen', 0.64);
  const headIn = sp(0);
  const sSix = sp(tSix), sIdx = sp(tIdx), sTook = sp(tTook), sBur = sp(tBur), grow = ramp(tVotes, tVotes + 0.07), sNext = sp(tNext);
  const sparkIn = sp(clamp(tListen, 0, 0.97));
  const now = listening(listen, frame / D);

  const Q = SHZ.query;
  const songs: string[] = SHZ.params.songs;
  const byName: Record<string, any> = {};
  for (const r of SHZ.ranked) byName[r.song] = r;
  const winner = SHZ.ranked[0], runner = SHZ.ranked[1];
  const vmax = Math.max(...(winner.hist as number[]));
  const lbl = portrait ? T.label * 0.78 : 22 * U;

  const songCard = (name: string, i: number, w: number, h: number) => {
    const r = byName[name];
    const win = name === winner.song;
    const k = clamp(op(sSix) * 6 - i, 0, 1);
    const lit = (win && op(grow) > 0.5) || (now?.label === 'ORIGINAL' && win);
    const HH = h * (portrait ? 0.2 : 0.5);
    const bars = r ? histBars(r.hist as number[], w - 28, HH, vmax, grow) : [];
    return (
      <div key={name} style={{ width: w, height: h, boxSizing: 'border-box', background: CLAUDE.CARD, borderRadius: 14, padding: 14,
        border: `${lit ? 5 : 1.5}px solid ${lit ? SPARK_TEXT : CLAUDE.BORDER}`, opacity: k, transform: `translateY(${(1 - k) * 16}px)` }}>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: win && op(grow) > 0.5 ? SPARK_TEXT : CLAUDE.INK }}>{name.toUpperCase()}</div>
        <svg width={w - 28} height={HH} style={{ display: 'block', marginTop: h * (portrait ? 0.04 : 0.06), overflow: 'visible' }}>
          <line x1={0} x2={w - 28} y1={HH} y2={HH} stroke={CLAUDE.BORDER} strokeWidth={2} />
          {bars.map((b, j) => b.h > 0.5 ? <rect key={j} x={b.x} y={HH - b.h} width={b.w} height={b.h} fill={win ? SPARK_TEXT : CLAUDE.INK_SOFT} /> : null)}
        </svg>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, color: win ? SPARK_TEXT : CLAUDE.INK_SOFT, marginTop: 6,
          opacity: op(grow) * (win || name === runner.song ? 1 : 0.85) }}>
          {r ? `${r.score} ${r.score === 1 ? 'VOTE' : 'VOTES'}` : '0 VOTES'}{win && !portrait ? ` · ${winner.offset_s.toFixed(2)} S` : ''}
        </div>
      </div>
    );
  };

  const query = (w: number, size: number) => {
    const lit = now?.label === 'NOISY CLIP';
    return (
      <div style={{ width: w, boxSizing: 'border-box', background: CLAUDE.CARD, borderRadius: 16, padding: `${size * 0.6}px ${size * 0.8}px`,
        border: `${lit ? 5 : 1.5}px solid ${lit ? SPARK_TEXT : CLAUDE.BORDER}`, borderTop: `${lit ? 5 : 6}px solid ${lit ? SPARK_TEXT : CLAUDE.INK}`, opacity: op(sTook) }}>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: size * 0.8, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK_SOFT }}>THE CLIP</div>
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: size * 1.6, fontWeight: 700, color: CLAUDE.INK, marginTop: 6 }}>
          {portrait ? `${Q.dur} s of ${Q.song}` : `${Q.dur} s of ${Q.song}, from ${Q.start.toFixed(1)} s`}</div>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: size * 0.8, fontWeight: 800, letterSpacing: 0.8, color: SPARK_TEXT, marginTop: 10, opacity: op(sBur) }}>
          {portrait ? 'FROM 12.0 S · NOISE AS LOUD' : 'CAFE NOISE AS LOUD AS THE MUSIC · PHONE BAND 150–4,000 HZ'}</div>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: size * 0.8, fontWeight: 800, letterSpacing: 0.8, color: CLAUDE.INK_SOFT, marginTop: 8, opacity: op(sBur) }}>
          {fmt(Q.hashes)} HASHES TO LOOK UP</div>
      </div>
    );
  };
  const libStat = (size: number) => (
    <div style={{ opacity: op(sIdx), fontFamily: HAI_TYPE.sans, fontSize: size, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK_SOFT }}>
      {portrait ? '' : `LIBRARY: 6 SONGS × ${SHZ.params.song_s} S · `}<span style={{ color: CLAUDE.INK }}>{fmt(SHZ.library.hashes)} HASHES{portrait ? ' IN THE LIBRARY' : ''}</span>
    </div>
  );
  const nowChip = now ? <Chip text={`▶ NOW PLAYING: ${now.label}`} size={portrait ? T.label * 0.8 : 24 * U} accent={now.label === 'ORIGINAL'} /> : null;

  if (portrait) {
    const gw = (CW - 24) / 2, gh = height * 0.12;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.2 }}>{query(CW, T.label * 0.8)}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.368 }}>{libStat(T.label * 0.6)}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.395, width: CW, display: 'flex', flexWrap: 'wrap', gap: 14 }}>
          {songs.map((s, i) => songCard(s, i, gw, gh))}
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.825 }}>{nowChip}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn * (now ? 0 : 1)} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  const cw = (CW - 5 * 22 * U) / 6, ch = height * 0.27;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{query(CW * 0.62, 26 * U)}</div>
      <div style={{ position: 'absolute', right: PAD_X, top: height * 0.27, textAlign: 'right' }}>
        <div style={{ opacity: op(sNext), fontFamily: HAI_TYPE.serif, fontSize: 64 * U, fontWeight: 700, color: SPARK_TEXT, lineHeight: 1 }}>
          {winner.score} <span style={{ color: CLAUDE.INK_SOFT }}>vs</span> {runner.score}</div>
        <div style={{ opacity: op(sNext), fontFamily: HAI_TYPE.sans, fontSize: 22 * U, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK_SOFT, marginTop: 10 }}>
          {winner.song.toUpperCase()} VS THE NEXT BEST ({runner.song.toUpperCase()})</div>
      </div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.5 }}>{libStat(22 * U)}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.545, display: 'flex', gap: 22 * U }}>
        {songs.map((s, i) => songCard(s, i, cw, ch))}
      </div>
      {now ? <div style={{ position: 'absolute', right: PAD_X, top: height * 0.455 }}>{nowChip}</div> : null}
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
