import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { KEY, PhoneBaseline, Caps } from './keys/keyKit';

/**
 * KeyChange — B06 of "How Apps Find a Song's Key."
 *
 * A key change (key.py): a C major pop song that moves up a semitone at 10 s. Three lanes over the song's
 * 20 s: what was played (C major, then C sharp major), the single whole-song answer (C minor: wrong for both
 * halves), and the 8-second sliding windows' answers, grouped into runs and labelled where a run is long enough.
 *
 *   second / semitone / one / neither / windows / sharp
 */

export const keyChangeSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('When the Key Changes'),
  sparkLine: z.string().default("One label can't follow a key change."),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type KeyChangeProps = z.infer<typeof keyChangeSchema>;

const SPAN = 20, CHANGE = 10;

export const KeyChange: React.FC<KeyChangeProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tSecond = at('second', 0.0), tSemi = at('semitone', 0.15), tOne = at('one', 0.42), tNeither = at('neither', 0.55);
  const tWin = at('windows', 0.68), tSharp = at('sharp', 0.85);
  const headIn = sp(0);
  const sLane = sp(tSemi), sOne = sp(tOne), sNeither = sp(tNeither), win = ramp(tWin, Math.min(tSharp + 0.05, 0.95));
  const sparkIn = sp(clamp(Math.min(tSharp + 0.03, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;

  const track = KEY.change.track as { t: number; key: string; r: number }[];
  const g = KEY.change.global_key as string;
  // group consecutive windows with the same answer; each window covers its centre +/- 0.5 s of the step
  const runs: { key: string; t0: number; t1: number; n: number }[] = [];
  track.forEach((w, i) => {
    const t0 = i === 0 ? w.t - 0.5 : (track[i - 1].t + w.t) / 2, t1 = i === track.length - 1 ? w.t + 0.5 : (w.t + track[i + 1].t) / 2;
    const last = runs[runs.length - 1];
    if (last && last.key === w.key) { last.t1 = t1; last.n += 1; } else runs.push({ key: w.key, t0, t1, n: 1 });
  });

  const LW = CW, LH = portrait ? 92 : 78 * U;
  const x = (t: number) => (t / SPAN) * LW;
  const laneLabel = (text: string, o: number) => <Caps size={lbl} color={CLAUDE.INK} style={{ marginBottom: 10, opacity: o }}>{text}</Caps>;
  const block = (t0: number, t1: number, text: string, fill: string, ink: string, o: number, key: string | number, strike = false) => (
    <div key={key} style={{ position: 'absolute', left: x(t0), width: Math.max(2, x(t1) - x(t0) - 4), top: 0, height: LH, background: fill, borderRadius: 10,
      opacity: o, display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden' }}>
      <span style={{ fontFamily: HAI_TYPE.sans, fontWeight: 800, fontSize: lbl, color: ink, whiteSpace: 'nowrap', textDecoration: strike ? 'line-through' : 'none' }}>{text}</span>
    </div>
  );
  const gap = portrait ? height * 0.04 : 46 * U;
  const lanes = (
    <div style={{ display: 'flex', flexDirection: 'column', gap }}>
      <div style={{ opacity: op(sLane) }}>
        {laneLabel('WHAT WAS PLAYED', 1)}
        <div style={{ position: 'relative', height: LH }}>
          {block(0, CHANGE, 'C MAJOR', CLAUDE.INK, CLAUDE.CARD, 1, 'a')}
          {block(CHANGE, SPAN, 'C SHARP MAJOR', CLAUDE.INK, CLAUDE.CARD, 1, 'b')}
        </div>
      </div>
      <div style={{ opacity: op(sOne) }}>
        {laneLabel(portrait ? 'ONE ANSWER' : 'ONE ANSWER FOR THE WHOLE SONG', 1)}
        <div style={{ position: 'relative', height: LH }}>
          {block(0, SPAN, g.toUpperCase() + (op(sNeither) > 0.5 ? ' · WRONG FOR BOTH' : ''), CLAUDE.BORDER, SPARK_TEXT, 1, 'g')}
        </div>
      </div>
      <div style={{ opacity: op(sp(tWin)) }}>
        {laneLabel(portrait ? '8-SECOND WINDOWS' : 'LISTENING IN 8-SECOND WINDOWS', 1)}
        <div style={{ position: 'relative', height: LH }}>
          {runs.map((r, i) => {
            const o = clamp(win * SPAN - r.t0, 0, 1);
            const wide = x(r.t1) - x(r.t0) > lbl * 7;
            const ok = (r.key === 'C major' && r.t1 <= CHANGE + 1) || (r.key === 'C# major' && r.t0 >= CHANGE - 1);
            return block(r.t0, r.t1, wide ? r.key.replace('C#', 'C SHARP').toUpperCase() : '', ok ? CLAUDE.INK : CLAUDE.GHOST, CLAUDE.CARD, o, i);
          })}
        </div>
      </div>
      <svg width={LW} height={lbl * 1.6} style={{ overflow: 'visible' }}>
        {[0, 5, 10, 15, 20].map((s) => <text key={s} x={x(s)} y={lbl * 1.2} textAnchor={s === 0 ? 'start' : s === SPAN ? 'end' : 'middle'}
          fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={lbl} fill={CLAUDE.INK_SOFT}>{s} S</text>)}
      </svg>
    </div>
  );
  const changeMark = (top: number, h: number) => (
    <div style={{ position: 'absolute', left: PAD_X + x(CHANGE) - 2, top, width: 4, height: h, background: SPARK_TEXT, opacity: op(sLane) }} />
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.22 }}>{lanes}</div>
        <Caps size={lbl} color={SPARK_TEXT} style={{ position: 'absolute', left: PAD_X, top: height * 0.7, opacity: op(sLane) }}>UP A SEMITONE AT 10 S</Caps>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      {changeMark(height * 0.245, height * 0.6)}
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.26 }}>{lanes}</div>
      <Caps size={lbl} color={SPARK_TEXT} style={{ position: 'absolute', left: PAD_X + x(CHANGE) + 14 * U, top: height * 0.215, opacity: op(sLane) }}>KEY CHANGE AT 10 S: UP A SEMITONE</Caps>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
