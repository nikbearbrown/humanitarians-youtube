import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { TOK, PhoneBaseline, Label, Chip, listening } from './tokens/tokKit';

/**
 * TokCodecQuality — B04 of "How AI Music Generators Turn Text Into Audio."
 *
 * The codec measured on a piece it never heard (codec.py): for 1 to 12 codebooks, how much of the
 * treble (4-12 kHz energy) the decoded audio keeps, in dB, and the overall signal-to-noise ratio.
 * The 1, 4 and 12 points are labelled; the beat's audio then plays those three decodes and the
 * original, and the matching point is lit.
 *
 *   built / never  "So I built one" / "never heard"   chart shells, training note
 *   one / treble   "With one codebook" / "the treble is down"   point 1
 *   four / twelve  "With four, clearer" / "With twelve"           points 4, 12 (line draws)
 *   listen         (props.listen)                                 now playing
 */

export const tokCodecQualitySchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('I Built a Codec and Measured It'),
  sparkLine: z.string().default('More tokens, closer sound. The treble goes first.'),
  listen: z.array(z.object({ label: z.string(), from: z.number(), to: z.number() })).optional(),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type TokCodecQualityProps = z.infer<typeof tokCodecQualitySchema>;

export const TokCodecQuality: React.FC<TokCodecQualityProps> = ({ eyebrow, title, sparkLine, listen, cues }) => {
  const { frame, D, width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tBuilt = at('built', 0.02), tNever = at('never', 0.12), tOne = at('one', 0.24), tTreb = at('treble', 0.3);
  const tFour = at('four', 0.42), tTw = at('twelve', 0.48), tListen = at('listen', 0.58);
  const headIn = sp(0);
  const sBuilt = sp(tBuilt), sNever = sp(tNever), sOne = sp(tOne), sTreb = sp(tTreb), sFour = sp(tFour), sTw = sp(tTw);
  const draw = ramp(tOne, tTw + 0.03);
  const sparkIn = sp(clamp(tListen, 0, 0.97));
  const now = listening(listen, frame / D);
  const lbl = portrait ? T.label * 0.72 : 22 * U;

  const C = TOK.curve as { q: number; snr_db: number; kept_high_db: number }[];
  const nowQ = now ? (now.label.startsWith('12') ? 12 : now.label.startsWith('4') ? 4 : now.label.startsWith('1') ? 1 : 0) : -1;
  const chart = (w: number, h: number, key: 'kept_high_db' | 'snr_db', lo: number, hi: number, name: string, unitTicks: number[], marks: Record<number, number>) => {
    const X = (q: number) => ((q - 1) / 11) * w;
    const Y = (v: number) => h - ((v - lo) / (hi - lo)) * h;
    const m = Math.max(1, Math.round(draw * C.length));
    const d = C.slice(0, m).map((c, i) => `${i ? 'L' : 'M'} ${X(c.q).toFixed(1)} ${Y(c[key]).toFixed(1)}`).join(' ');
    return (
      <div>
        <Label text={name} size={lbl} color={CLAUDE.INK} style={{ marginBottom: lbl * 0.5 }} />
        <svg width={w} height={h} style={{ display: 'block', overflow: 'visible' }}>
          <rect x={0} y={0} width={w} height={h} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
          {unitTicks.map((v) => <g key={v}><line x1={0} x2={w} y1={Y(v)} y2={Y(v)} stroke={CLAUDE.BORDER} />
            <text x={-12} y={Y(v) + lbl * 0.35} textAnchor="end" fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={lbl} fill={CLAUDE.INK_SOFT}>{v}</text></g>)}
          <path d={d} fill="none" stroke={SPARK_TEXT} strokeWidth={4} />
          {C.slice(0, m).map((c) => {
            const lit = c.q === nowQ;
            const show = marks[c.q] !== undefined && op(marks[c.q]) > 0.3;
            return <circle key={c.q} cx={X(c.q)} cy={Y(c[key])} r={lit ? 13 : show ? 9 : 5} fill={lit || show ? SPARK_TEXT : CLAUDE.INK_SOFT} />;
          })}
          {[1, 4, 12].map((q) => {
            const c = C[q - 1];
            const o = op(marks[q] ?? 0);
            return <text key={q} x={X(q) + (q === 1 ? 16 : 0)} y={Y(c[key]) + (q === 1 ? (key === 'kept_high_db' ? -70 : 38) : (q === 4 && portrait && key === 'kept_high_db' ? 44 : -20))} textAnchor={q === 12 ? 'end' : q === 1 ? 'start' : 'middle'} fontFamily={HAI_TYPE.sans} fontWeight={800}
              fontSize={lbl} fill={SPARK_TEXT} opacity={o}>{c[key].toFixed(1)} dB</text>;
          })}
          {[1, 4, 8, 12].map((q) => <text key={q} x={X(q)} y={h + lbl * 1.35} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={lbl} fill={CLAUDE.INK_SOFT}>{q}</text>)}
        </svg>
      </div>
    );
  };
  const marks = { 1: op(sTreb), 4: op(sFour), 12: op(sTw) };
  const note = <Label text={portrait ? 'LEARNED 36 · TESTED 1 NEW' : 'CODEBOOKS LEARNED FROM 36 PIECES · TESTED ON A PIECE IT NEVER HEARD'} size={lbl} opacity={op(sNever)} />;
  const xCap = <Label text="NUMBER OF CODEBOOKS (TOKENS PER FRAME) →" size={lbl} opacity={op(sBuilt)} />;
  const nowChip = now ? <Chip text={`▶ NOW PLAYING: ${now.label}`} size={portrait ? T.label * 0.78 : 24 * U} accent={now.label !== 'ORIGINAL'} /> : null;

  if (portrait) {
    const w = CW - 90, h = height * 0.14;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.2 }}>{note}</div>
        <div style={{ position: 'absolute', left: PAD_X + 90, top: height * 0.245, opacity: op(sBuilt) }}>
          {chart(w, h, 'kept_high_db', -18, 0, 'TREBLE KEPT (DB)', [-15, -10, -5, 0], marks)}</div>
        <div style={{ position: 'absolute', left: PAD_X + 90, top: height * 0.49, opacity: op(sBuilt) }}>
          {chart(w, h, 'snr_db', 0, 14, 'WHOLE SOUND, SNR (DB)', [0, 5, 10], marks)}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.73 }}>{nowChip}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  const w = (CW - 80 * U * 2 - 60 * U) / 2, h = height * 0.36;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.235 }}>{note}</div>
      <div style={{ position: 'absolute', left: PAD_X + 80 * U, top: height * 0.31, display: 'flex', gap: 140 * U, opacity: op(sBuilt) }}>
        {chart(w, h, 'kept_high_db', -18, 0, 'TREBLE KEPT (DB)', [-15, -10, -5, 0], marks)}
        {chart(w, h, 'snr_db', 0, 14, 'WHOLE SOUND, SIGNAL-TO-NOISE (DB)', [0, 5, 10], marks)}
      </div>
      <div style={{ position: 'absolute', left: PAD_X + 80 * U, top: height * 0.31 + h + 90 * U }}>{xCap}</div>
      {now ? <div style={{ position: 'absolute', right: PAD_X, top: height * 0.22 }}>{nowChip}</div> : null}
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
