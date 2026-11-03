import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, CountTo, SPARK_TEXT, PHONE,
} from '../lib/cueKit';
import { TOY } from './diffusion/toyData';
import { PixelTile, snapshotAt, px } from './diffusion/diffusionKit';

/**
 * DiffuseReverseRun — B04 of "How AI Image Generators Turn Noise Into a Picture."
 *
 * The measured beat: the toy model actually generating. LEFT is the receipt for
 * what it learned from — sixteen of the real 12,000 training pictures (rebuilt
 * from the same seeded draws) and the run's own numbers. RIGHT is the reverse
 * process itself: the seed's static walked back through its recorded snapshots
 * (every 20 of the 1,000 steps, cross-faded), with the model's running guess of
 * the clean picture underneath — the thing "at first it's only guessing" means.
 *
 *   trained   "trained one myself"            TOY MODEL badge
 *   laptop    "no graphics card"              the hardware stat
 *   pictures  "Twelve thousand little…"       the training mosaic + counts
 *   static    "gave it pure static"           the run tile at step 1000
 *   guessing  "only guessing"                 the guess tile
 *   heart     "there's a heart"               step 0, framed in spark
 *
 * Portrait: the run on top, the training receipt beneath it.
 */

export const diffuseReverseRunSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AI CONCEPTS'),
  title: z.string().default('I Trained One on My Laptop'),
  runIndex: z.number().default(0),
  toyLabel: z.string().default('TOY MODEL · plain numpy · no pretrained weights'),
  hardware: z.string().default('CPU only — no graphics card'),
  sparkLine: z.string().default('A thousand small steps, from static to a heart.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type DiffuseReverseRunProps = z.infer<typeof diffuseReverseRunSchema>;

export const DiffuseReverseRun: React.FC<DiffuseReverseRunProps> = ({
  eyebrow, title, runIndex, toyLabel, hardware, sparkLine, cues,
}) => {
  const { D, width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CONTENT_W = width - PAD_X * 2;
  const run = TOY.runs[runIndex] ?? TOY.runs[0];

  const tTrained = at('trained', 0.02);
  const tLaptop = at('laptop', 0.1);
  const tPics = at('pictures', 0.2);
  const tStatic = at('static', 0.5);
  const tGuess = at('guessing', 0.78);
  const tHeart = at('heart', 0.9);

  const headIn = sp(0);
  const sBadge = sp(tTrained);
  const sHw = sp(tLaptop);
  const sPics = sp(tPics);
  const sRun = sp(Math.max(0, tStatic - 0.03));
  const sGuess = sp(tGuess);
  const sHeart = sp(tHeart, SPRING_SNAP);
  const sparkIn = sp(clamp(tHeart + 0.04, 0, 0.97));
  /* SHELL: the run's frame is up from the first stat so the right column is
     never empty at a Gate V sample; the static inside it waits for its phrase. */
  const sShell = sp(tTrained);

  const walk = ramp(tStatic + 0.02, tHeart);
  const eased = 1 - Math.pow(1 - walk, 1.5);
  const step = Math.round(1000 * (1 - eased));
  const snap = snapshotAt(run.frames, step, TOY.keepEvery);
  const gsnap = snapshotAt(run.guesses, Math.max(step, 20), TOY.keepEvery);

  const mins = Math.round(TOY.trainSeconds / 60);

  // ── layout ──────────────────────────────────────────────────────────
  const L_W = portrait ? CONTENT_W : CONTENT_W * 0.44;
  const RUN = portrait ? CONTENT_W * 0.44 : height * 0.46;
  const RUN_X = portrait ? PAD_X : PAD_X + CONTENT_W - RUN - (CONTENT_W * 0.56 - RUN) * 0.35;
  const RUN_Y = portrait ? height * 0.24 : height * 0.285;
  const GUESS = RUN * 0.42;
  const L_Y = portrait ? RUN_Y + RUN + 100 * U : height * 0.285;

  const MOS_COLS = portrait ? 16 : 8;
  const MOS_GAP = (portrait ? 6 : 8) * U;
  const MT = (L_W - MOS_GAP * (MOS_COLS - 1)) / MOS_COLS;

  const stat = (value: React.ReactNode, label: string, k: number) => (
    <div style={{ opacity: k, transform: `translateY(${(1 - k) * 14 * U}px)` }}>
      <div style={{
        fontFamily: HAI_TYPE.serif, fontSize: (portrait ? 52 : 58) * U, fontWeight: 700,
        color: CLAUDE.INK, lineHeight: 1,
      }}>{value}</div>
      <div style={{
        fontFamily: HAI_TYPE.sans, fontSize: 17 * U, fontWeight: 700, letterSpacing: 1.6,
        color: CLAUDE.INK_SOFT, marginTop: 6 * U,
      }}>{label}</div>
    </div>
  );

  /* ── PORTRAIT (phone): PHONE type scale — less text, larger. Badge · the run with
     the model's guess beside it · the step readout · two headline stats. The
     training mosaic and the parameter count are landscape-only. */
  if (portrait) {
    const T = PHONE(height);
    const B_Y = height * 0.245;
    const R_Y = B_Y + T.label * 1.55;
    const pRUN = CONTENT_W * 0.46, pGUESS = CONTENT_W * 0.3;
    const G_X = PAD_X + pRUN + CONTENT_W * 0.05;
    const STEP_Y = R_Y + pRUN + 16;
    const STAT_Y = STEP_Y + T.data * 1.4;
    const stat = (value: string, label: string) => (
      <div style={{ flex: 1, opacity: op(sPics) }}>
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: T.data * 1.3, fontWeight: 700, color: CLAUDE.INK, lineHeight: 1 }}>{value}</div>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 700, letterSpacing: 0.5, color: CLAUDE.INK_SOFT, marginTop: 4 }}>{label}</div>
      </div>
    );
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: B_Y, opacity: op(sBadge),
          fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 1,
          color: CLAUDE.CARD, background: CLAUDE.INK, borderRadius: 10, padding: '0 16px' }}>
          TOY MODEL{op(sHw) > 0.5 ? ' · CPU ONLY' : ''}
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: R_Y, width: pRUN, height: pRUN,
          borderRadius: 14, border: `3px dashed ${CLAUDE.GHOST}`, boxSizing: 'border-box',
          opacity: op(sShell) * (1 - op(sRun)) }} />
        <div style={{ position: 'absolute', left: PAD_X, top: R_Y, opacity: op(sRun) }}>
          <PixelTile a={step >= 1000 ? px(run.frames[0]) : snap.a} b={step >= 1000 ? undefined : snap.b}
            mix={snap.mix} size={pRUN} radius={14}
            frameWidth={op(sHeart) > 0.3 ? 8 : 0} frameColor={CLAUDE.SPARK} />
        </div>
        <div style={{ position: 'absolute', left: G_X, top: R_Y, width: CONTENT_W - pRUN - CONTENT_W * 0.05, opacity: op(sGuess) }}>
          <PixelTile a={gsnap.a} b={gsnap.b} mix={gsnap.mix} size={pGUESS} radius={8} />
          <div style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 1,
            color: CLAUDE.INK_SOFT, marginTop: 10, lineHeight: 1.1 }}>ITS GUESS</div>
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: STEP_Y, width: CONTENT_W, opacity: op(sRun),
          fontFamily: HAI_TYPE.mono, fontSize: T.data, fontWeight: 700, whiteSpace: 'nowrap',
          color: op(sHeart) > 0.5 ? SPARK_TEXT : CLAUDE.INK }}>
          step {step} · “{run.prompt}”
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: STAT_Y, width: CONTENT_W, display: 'flex', gap: 30 }}>
          {stat(TOY.trainPictures.toLocaleString('en-US'), 'PICTURES')}
          {stat(`${mins} min`, 'TRAINING')}
        </div>
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
          height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn}
        padX={PAD_X} height={height} width={width} portrait={portrait} />

      {/* ══ the receipt: what it learned from ════════════════════════ */}
      <div style={{ position: 'absolute', left: PAD_X, top: L_Y, width: L_W }}>
        <div style={{ display: 'flex', gap: 12 * U, flexWrap: 'wrap', opacity: op(sBadge) }}>
          <span style={{
            fontFamily: HAI_TYPE.sans, fontSize: 17 * U, fontWeight: 800, letterSpacing: 1.8,
            color: CLAUDE.CARD, background: CLAUDE.INK, borderRadius: 6 * U,
            padding: `${6 * U}px ${12 * U}px`,
          }}>{toyLabel}</span>
          <span style={{
            fontFamily: HAI_TYPE.sans, fontSize: 17 * U, fontWeight: 800, letterSpacing: 1.8,
            color: SPARK_TEXT, border: `2px solid ${SPARK_TEXT}`, borderRadius: 6 * U,   // an outline around TEXT reads as accent type (GATE T §8.3)
            padding: `${4 * U}px ${10 * U}px`, opacity: op(sHw),
          }}>{hardware.toUpperCase()}</span>
        </div>

        <div style={{
          fontFamily: HAI_TYPE.sans, fontSize: 17 * U, fontWeight: 700, letterSpacing: 1.8,
          color: CLAUDE.INK_SOFT, marginTop: 26 * U, marginBottom: 10 * U, opacity: op(sPics),
        }}>16 OF THE REAL TRAINING PICTURES</div>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: MOS_GAP, width: L_W }}>
          {TOY.trainSamples.map((h, i) => {
            const k = clamp(op(sPics) * 20 - i, 0, 1);
            return (
              <div key={i} style={{
                width: MT, height: MT, borderRadius: 5 * U, position: 'relative',
                background: CLAUDE.FOOTER, opacity: op(sShell),
              }}>
                <div style={{ position: 'absolute', inset: 0, opacity: k, transform: `scale(${0.8 + 0.2 * k})` }}>
                  <PixelTile a={px(h)} size={MT} radius={5 * U} />
                </div>
              </div>
            );
          })}
        </div>

        <div style={{ display: 'flex', gap: 40 * U, marginTop: 26 * U }}>
          {stat(TOY.trainPictures.toLocaleString('en-US'), 'TRAINING PICTURES', op(sPics))}
          {stat(`${mins} min`, 'OF TRAINING', op(sPics))}
          {stat(`${(TOY.params / 1e6).toFixed(1)}M`, 'NUMBERS IN THE MODEL', op(sPics))}
        </div>
      </div>

      {/* ══ the run ══════════════════════════════════════════════════ */}
      <div style={{
        position: 'absolute', left: RUN_X, top: RUN_Y, width: RUN, height: RUN,
        borderRadius: 14 * U, border: `2px dashed ${CLAUDE.BORDER}`, boxSizing: 'border-box',
        opacity: op(sShell) * (1 - op(sRun)),
      }} />
      <div style={{ position: 'absolute', left: RUN_X, top: RUN_Y, opacity: op(sRun) }}>
        <PixelTile a={step >= 1000 ? px(run.frames[0]) : snap.a} b={step >= 1000 ? undefined : snap.b}
          mix={snap.mix} size={RUN} radius={14 * U}
          frameWidth={op(sHeart) > 0.3 ? 8 * U : 0} frameColor={CLAUDE.SPARK} />
        {/* progress through the thousand steps */}
        <div style={{ marginTop: 14 * U, width: RUN }}>
          <div style={{
            display: 'flex', justifyContent: 'space-between',
            fontFamily: HAI_TYPE.mono, fontSize: 21 * U, fontWeight: 700,
            color: op(sHeart) > 0.5 ? SPARK_TEXT : CLAUDE.INK,
          }}>
            <span>step {step}</span>
            <span>{op(sHeart) > 0.5 ? `“${run.prompt}” · seed ${run.seed}` : `prompt: “${run.prompt}”`}</span>
          </div>
          <div style={{ height: 10 * U, background: CLAUDE.FOOTER, borderRadius: 5 * U, marginTop: 8 * U }}>
            <div style={{ width: `${(1 - step / 1000) * 100}%`, height: '100%',
              background: CLAUDE.SPARK, borderRadius: 5 * U }} />
          </div>
        </div>
      </div>

      {/* the model's running guess of the clean picture */}
      <div style={{
        position: 'absolute',
        left: portrait ? RUN_X + RUN + 40 * U : RUN_X - GUESS - 36 * U,
        top: portrait ? RUN_Y + RUN * 0.18 : RUN_Y + RUN - GUESS,
        width: portrait ? CONTENT_W - RUN - 40 * U : GUESS,
        opacity: op(sGuess),
      }}>
        <PixelTile a={gsnap.a} b={gsnap.b} mix={gsnap.mix} size={GUESS} radius={8 * U}
          style={{ opacity: 0.92 }} />
        <div style={{
          fontFamily: HAI_TYPE.sans, fontSize: 16 * U, fontWeight: 800, letterSpacing: 1.6,
          color: CLAUDE.INK_SOFT, marginTop: 10 * U, lineHeight: 1.35,
        }}>ITS GUESS OF WHAT'S UNDERNEATH</div>
      </div>

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
        height={height} portrait={portrait}
        top={portrait ? height * 0.722 : undefined} />
    </AbsoluteFill>
  );
};
