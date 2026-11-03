import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { SHZ, PhoneBaseline, Chip } from './shazam/shzKit';

/**
 * ShazamNoiseSweep — B05 of "How Shazam Finds a Song."
 *
 * Thirty random 5-second queries at each of six noise levels (fingerprint.py's sweep). Each
 * query is one square: filled = named the right song, hollow = said "no match"; a wrong answer
 * would be a struck square, and there are none. Columns fill as the narration reaches them.
 *
 *   how / ran  "How much noise" / "thirty random clips"  grid shells
 *   ten        "ten decibels louder than the noise"      +10 and +5 dB columns
 *   zero       "noise as loud as the music"              0 dB
 *   five       "five decibels louder, twenty-two"        -5 dB
 *   tenl       "Ten decibels louder, nine"               -10 dB
 *   failed     "when it failed"                          -15 dB + no-match legend
 *   never      "It never named"                          zero-wrong chip
 */

export const shazamNoiseSweepSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('How Much Noise It Takes'),
  sparkLine: z.string().default("When it can't tell, it says so."),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type ShazamNoiseSweepProps = z.infer<typeof shazamNoiseSweepSchema>;

const label = (snr: number, short = false) => (snr > 0 ? `MUSIC +${snr}${short ? '' : ' DB'}` : snr === 0 ? 'EQUAL' : `NOISE +${-snr}${short ? '' : ' DB'}`);

export const ShazamNoiseSweep: React.FC<ShazamNoiseSweepProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tRan = at('ran', 0.08), tTen = at('ten', 0.2), tZero = at('zero', 0.42), tFive = at('five', 0.52);
  const tTenl = at('tenl', 0.62), tFail = at('failed', 0.74), tNever = at('never', 0.86);
  const headIn = sp(0);
  const sShell = sp(tRan);
  const fills = [tTen, tTen + 0.04, tZero, tFive, tTenl, tFail].map((t) => ramp(t, t + 0.06));
  const sFail = sp(tFail), sNever = sp(tNever);
  const sparkIn = sp(clamp(tNever + 0.04, 0, 0.97));
  const sweep = SHZ.sweep as { snr: number; correct: number; wrong: number; no_match: number; of: number }[];
  const wrongTotal = sweep.reduce((a, s) => a + s.wrong, 0);
  const total = sweep.reduce((a, s) => a + s.of, 0);
  const lbl = portrait ? T.label * 0.72 : 22 * U;

  const squares = (s: typeof sweep[0], k: number, cols: number, size: number, gap: number) => (
    <div style={{ display: 'grid', gridTemplateColumns: `repeat(${cols}, ${size}px)`, gap }}>
      {Array.from({ length: s.of }, (_, j) => {
        const on = clamp(k * s.of - j, 0, 1);
        const correct = j < s.correct;
        return <div key={j} style={{ width: size, height: size, borderRadius: size * 0.18, boxSizing: 'border-box',
          background: correct && on > 0.5 ? CLAUDE.INK : 'transparent',
          border: `${Math.max(2, size * 0.1)}px solid ${on > 0.5 ? (correct ? CLAUDE.INK : SPARK_TEXT) : CLAUDE.GHOST}`,
          opacity: on > 0.5 ? 1 : 0.6 }} />;
      })}
    </div>
  );
  const legend = (size: number) => (
    <div style={{ display: 'flex', gap: size * 1.4, alignItems: 'center', opacity: op(sShell), fontFamily: HAI_TYPE.sans, fontSize: size, fontWeight: 800, letterSpacing: 1, color: CLAUDE.INK_SOFT }}>
      <span style={{ display: 'flex', alignItems: 'center', gap: 10 }}><span style={{ width: size, height: size, background: CLAUDE.INK, borderRadius: 4, display: 'inline-block' }} />RIGHT SONG</span>
      <span style={{ display: 'flex', alignItems: 'center', gap: 10 }}><span style={{ width: size, height: size, border: `3px solid ${SPARK_TEXT}`, borderRadius: 4, display: 'inline-block', boxSizing: 'border-box' }} />“NO MATCH”</span>
    </div>
  );

  if (portrait) {
    const size = 22, gap = 7;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.205, width: CW, display: 'flex', flexDirection: 'column', gap: height * 0.017, opacity: op(sShell) }}>
          {sweep.map((s, i) => (
            <div key={s.snr} style={{ display: 'flex', alignItems: 'center', gap: 22 }}>
              <div style={{ width: 300, whiteSpace: 'nowrap', fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, color: s.snr < 0 ? SPARK_TEXT : CLAUDE.INK }}>{label(s.snr, true)}</div>
              {squares(s, fills[i], 15, size, gap)}
              <div style={{ fontFamily: HAI_TYPE.serif, fontSize: T.body, fontWeight: 700, color: CLAUDE.INK, opacity: fills[i] }}>{s.correct}</div>
            </div>
          ))}
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.625, opacity: op(sShell), fontFamily: HAI_TYPE.sans, fontSize: lbl * 0.85, fontWeight: 800, letterSpacing: 1, color: CLAUDE.INK_SOFT }}>LEVELS IN DB: HOW MUCH LOUDER</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.66 }}>{legend(lbl * 0.95)}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.71, opacity: op(sNever) }}>
          <Chip text={`${wrongTotal} WRONG SONGS IN ${total}`} size={T.label * 0.85} accent />
        </div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  const colW = CW / 6, size = 30 * U, gap = 9 * U;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.24, width: CW, display: 'flex', opacity: op(sShell) }}>
        {sweep.map((s, i) => (
          <div key={s.snr} style={{ width: colW, display: 'flex', flexDirection: 'column', alignItems: 'flex-start' }}>
            <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1, color: s.snr < 0 ? SPARK_TEXT : CLAUDE.INK, marginBottom: 18 * U }}>{label(s.snr)}</div>
            {squares(s, fills[i], 5, size, gap)}
            <div style={{ fontFamily: HAI_TYPE.serif, fontSize: 56 * U, fontWeight: 700, color: CLAUDE.INK, marginTop: 18 * U, opacity: fills[i] }}>
              {s.correct}<span style={{ fontSize: 44 * U, color: CLAUDE.INK_SOFT }}> / {s.of}</span></div>
          </div>
        ))}
      </div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.8 }}>{legend(22 * U)}</div>
      <div style={{ position: 'absolute', right: PAD_X, top: height * 0.795, opacity: op(sNever) }}>
        <Chip text={`${wrongTotal} WRONG SONGS IN ${total} CLIPS`} size={24 * U} accent />
      </div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
