import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { ANC, PhoneBaseline, Caps, Chip, listening } from './anc/ancKit';

/**
 * AncTypes — B04 of "How Noise-Cancelling Headphones Work."
 *
 * Four kinds of synthetic noise through the simulated headphone (anc.py): the change at the ear with ANC on
 * vs off, in dB, as bars from a zero line (left = quieter, right = louder). Engine hum −25.5, low rumble
 * −31.4, voices −11.2, clatter +0.9. Ends with the hum itself, off then on (props.listen, one clip).
 *
 *   four / engine / rumble / voices / clatter / steady / sudden / listen
 */

export const ancTypesSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default("What It Cancels, and What It Can't"),
  sparkLine: z.string().default('Steady and low: gone. Sudden: still there.'),
  listen: z.array(z.object({ label: z.string(), from: z.number(), to: z.number() })).optional(),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type AncTypesProps = z.infer<typeof ancTypesSchema>;

const ORDER = [
  { k: 'engine', name: 'ENGINE HUM', cue: 'engine' },
  { k: 'rumble', name: 'LOW RUMBLE', cue: 'rumble' },
  { k: 'voices', name: 'VOICES', cue: 'voices' },
  { k: 'clatter', name: 'CLATTER', cue: 'clatter' },
];
const LO = -35, HI = 5;

export const AncTypes: React.FC<AncTypesProps> = ({ eyebrow, title, sparkLine, listen, cues }) => {
  const { width, height, frame, D, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tFour = at('four', 0.0), tSteady = at('steady', 0.58), tSudden = at('sudden', 0.68), tListen = at('listen', 0.76);
  const headIn = sp(0);
  const sChart = sp(tFour), sSteady = sp(tSteady), sSudden = sp(tSudden);
  const now = listening(listen, frame / D);
  const sparkIn = sp(clamp(Math.min(tListen - 0.03, 0.88), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const types = ANC.types as Record<string, number>;

  const AW = portrait ? CW : CW * 0.62, BH = portrait ? 66 : 76 * U, rowGap = portrait ? 34 : 34 * U;
  const x = (db: number) => ((db - LO) / (HI - LO)) * AW;
  const chart = (
    <div style={{ position: 'relative', width: AW, opacity: op(sChart) }}>
      {ORDER.map((o, i) => {
        const g = ramp(at(o.cue, 0.1 + i * 0.1), at(o.cue, 0.1 + i * 0.1) + 0.06);
        const v = types[o.k];
        const x0 = x(0), x1 = x(v * g);
        const quiet = v < 0;
        return (
          <div key={o.k} style={{ marginBottom: rowGap }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', width: AW, marginBottom: 8 }}>
              <Caps size={lbl} color={CLAUDE.INK}>{o.name}</Caps>
              <Caps size={lbl} color={quiet ? CLAUDE.INK : SPARK_TEXT} style={{ opacity: g }}>{`${v > 0 ? '+' : ''}${v.toFixed(1)} DB`}</Caps>
            </div>
            <div style={{ position: 'relative', width: AW, height: BH, background: CLAUDE.BORDER, borderRadius: 8 }}>
              <div style={{ position: 'absolute', left: Math.min(x0, x1), width: Math.abs(x1 - x0), top: 0, height: BH,
                background: quiet ? (v < -20 ? CLAUDE.INK : CLAUDE.INK_SOFT) : SPARK_TEXT, borderRadius: 6 }} />
              <div style={{ position: 'absolute', left: x0 - 2, top: -8, width: 4, height: BH + 16, background: CLAUDE.INK }} />
            </div>
          </div>
        );
      })}
      <div style={{ display: 'flex', justifyContent: 'space-between', width: AW }}>
        <Caps size={lbl * 0.9}>QUIETER</Caps><Caps size={lbl * 0.9}>LOUDER</Caps>
      </div>
    </div>
  );
  const notes = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 18 : 18 * U, alignItems: 'flex-start' }}>
      <div style={{ opacity: portrait ? op(sSteady) : 0.35 + 0.65 * op(sSteady) }}><Chip text={portrait ? 'STEADY, LOW: PREDICTABLE' : 'STEADY AND LOW: PREDICTABLE'} size={portrait ? T.label * 0.74 : 22 * U} /></div>
      <div style={{ opacity: portrait ? op(sSudden) : 0.35 + 0.65 * op(sSudden) }}><Chip text={portrait ? "SUDDEN: CAN'T PREDICT" : "SUDDEN: CAN'T BE PREDICTED"} size={portrait ? T.label * 0.74 : 22 * U} accent /></div>
      <div style={{ opacity: now ? 1 : 0 }}><Chip text={now ? `▶ HUM: ANC ${now.progress < 0.5 ? 'OFF' : 'ON'}` : '▶'} size={portrait ? T.label * 0.8 : 26 * U} accent /></div>
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.21 }}>{chart}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.6 }}>{notes}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25 }}>{chart}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.66, top: height * 0.3 }}>{notes}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
