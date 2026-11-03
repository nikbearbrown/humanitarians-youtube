import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { ANC, PhoneBaseline, Caps, Stat } from './anc/ancKit';

/**
 * AncSystem — B02 of "How Noise-Cancelling Headphones Work."
 *
 * The parts of one ear cup, drawn as a diagram (no head or person: PROFESSOR BEAR LAW not triggered): the
 * outside microphone, the chip, the speaker, the inside (error) microphone, the noise arriving from the left.
 * Then the timing race from the simulation (anc.py's model): the noise takes 83 µs from the outside mic to the
 * ear; the electronics take 125 µs; the gap is what the filter has to predict.
 *
 *   outside / chip / speaker / inside / adjust / rate / noise / elec / predict
 */

export const ancSystemSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Listen, Flip, Check, Adjust'),
  sparkLine: z.string().default('The chip has to stay ahead of the noise.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type AncSystemProps = z.infer<typeof ancSystemSchema>;

export const AncSystem: React.FC<AncSystemProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tOut = at('outside', 0.02), tChip = at('chip', 0.13), tSpk = at('speaker', 0.22), tIn = at('inside', 0.3);
  const tAdj = at('adjust', 0.42), tRate = at('rate', 0.5), tNoise = at('noise', 0.6), tElec = at('elec', 0.72), tPred = at('predict', 0.86);
  const headIn = sp(0);
  const sOut = sp(tOut), sChip = sp(tChip), sSpk = sp(tSpk), sIn = sp(tIn), sAdj = sp(tAdj), sRate = sp(tRate);
  const bNoise = ramp(tNoise, tNoise + 0.06), bElec = ramp(tElec, tElec + 0.06), sPred = sp(Math.min(tPred, 0.88));
  const sparkIn = sp(clamp(Math.min(tPred + 0.03, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const M = ANC.model as { fs: number; d_p: number; d_s: number; taps: number };
  const usP = Math.round(1e6 * M.d_p / M.fs), usS = Math.round(1e6 * M.d_s / M.fs);

  // the diagram, in a box of DW x DH
  const DW = portrait ? CW : CW * 0.55, DH = portrait ? height * 0.28 : height * 0.5;
  const cupX = DW * 0.32, cupW = DW * 0.5, cupY = DH * 0.08, cupH = DH * 0.84;
  const part = (x: number, y: number, w: number, h: number, label: string, o: number, accent = false) => (
    <g opacity={o}>
      <rect x={x} y={y} width={w} height={h} rx={12} fill={accent ? SPARK_TEXT : CLAUDE.CARD} stroke={accent ? SPARK_TEXT : CLAUDE.INK} strokeWidth={3} />
      <text x={x + w / 2} y={y + h / 2 + lbl * 0.36} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl}
        fill={accent ? CLAUDE.CARD : CLAUDE.INK}>{label}</text>
    </g>
  );
  const pw = DW * (portrait ? 0.3 : 0.24), ph = portrait ? 74 : 60 * U;
  const diagram = (
    <svg width={DW} height={DH} style={{ display: 'block', overflow: 'visible' }}>
      {/* noise arriving: three wavy lines on the left */}
      {[0.3, 0.5, 0.7].map((f, i) => (
        <path key={i} d={`M 0 ${DH * f} q ${DW * 0.02} -14 ${DW * 0.04} 0 t ${DW * 0.04} 0`} fill="none" stroke={CLAUDE.GHOST} strokeWidth={4} opacity={op(sOut)} />
      ))}
      <text x={0} y={DH * 0.18} fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={CLAUDE.INK_SOFT} opacity={op(sOut)}>NOISE</text>
      {/* the cup */}
      <rect x={cupX} y={cupY} width={cupW} height={cupH} rx={DW * 0.08} fill={CLAUDE.PAGE} stroke={CLAUDE.INK} strokeWidth={5} />
      {part(cupX - pw * 0.55, DH * 0.42, pw, ph, portrait ? 'MIC OUT' : 'OUTSIDE MIC', op(sOut))}
      {part(cupX + cupW * 0.3, DH * 0.16, pw, ph, 'CHIP', op(sChip), true)}
      {part(cupX + cupW * (portrait ? 0.36 : 0.42), DH * 0.42, pw, ph, 'SPEAKER', op(sSpk))}
      {part(cupX + cupW * (portrait ? 0.36 : 0.42), DH * 0.68, pw, ph, portrait ? 'MIC IN' : 'INSIDE MIC', op(sIn))}
      {/* ear side marker */}
      <text x={cupX + cupW + 14} y={DH * 0.52} fontFamily={HAI_TYPE.sans} fontWeight={800} fontSize={lbl} fill={CLAUDE.INK_SOFT} opacity={op(sSpk)}>EAR</text>
    </svg>
  );
  const TW = portrait ? CW : CW * 0.4, TH = portrait ? 56 : 44 * U;
  const maxUs = 140;
  const race = (label: string, us: number, grow: number, accent: boolean) => (
    <div style={{ opacity: grow > 0 ? 1 : 0.25 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', width: TW, marginBottom: 6 }}>
        <Caps size={lbl} color={accent ? SPARK_TEXT : CLAUDE.INK}>{label}</Caps>
        <Caps size={lbl} color={accent ? SPARK_TEXT : CLAUDE.INK}>{us} µS</Caps>
      </div>
      <div style={{ width: TW, height: TH, background: CLAUDE.BORDER, borderRadius: 8 }}>
        <div style={{ width: (us / maxUs) * TW * grow, height: TH, background: accent ? SPARK_TEXT : CLAUDE.INK, borderRadius: 8 }} />
      </div>
    </div>
  );
  const big = portrait ? T.title * 1.0 : 66 * U;
  const side = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? height * 0.016 : 26 * U }}>
      <div style={{ opacity: op(sAdj) }}><Stat value={(M.fs).toLocaleString('en-US')} label={portrait ? 'FILTER UPDATES A SECOND' : 'FILTER UPDATES A SECOND (MY SIMULATION)'} size={big} opacity={op(sRate)} /></div>
      {race(portrait ? 'NOISE TO THE EAR' : 'NOISE: OUTSIDE MIC TO THE EAR', usP, bNoise, false)}
      {race(portrait ? 'THE ELECTRONICS' : 'ANTI-NOISE: THE ELECTRONICS', usS, bElec, true)}
      <Caps size={lbl} color={SPARK_TEXT} style={{ opacity: op(sPred) }}>{`${usS - usP} µS TO PREDICT`}</Caps>
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.2 }}>{diagram}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.5 }}>{side}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.26 }}>{diagram}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.6, top: height * 0.27 }}>{side}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
