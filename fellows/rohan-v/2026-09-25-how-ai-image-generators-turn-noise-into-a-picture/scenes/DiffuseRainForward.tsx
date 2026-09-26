import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, hash, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, SPARK_TEXT, PHONE,
} from '../lib/cueKit';
import { TOY } from './diffusion/toyData';
import { PixelTile, forwardMix, px, ABAR } from './diffusion/diffusionKit';

/**
 * DiffuseRainForward — B02 of "How AI Image Generators Turn Noise Into a Picture."
 *
 * The analogy beat: a photo left out in the rain. The picture on the left is a
 * REAL training picture from the toy model, and the smudging is not an effect —
 * each frame is the forward process computed exactly (x_t = √ᾱ_t·x₀ + √(1−ᾱ_t)·ε
 * with the model's own schedule and its recorded noise draw), so "each drop
 * smudges it a little more" is literally one step of the arithmetic. Rain
 * streaks fall over it only while the narration is in the analogy.
 *
 *   rain        "left out in the rain"   the picture, rain starts, step 0 → 1000
 *   speckle     "grey speckle"           step 1000 reached, rain stops
 *   arithmetic  "simple arithmetic"      the six-panel strip, labelled NO MODEL
 *   backwards   "going backwards"        the spark arrow runs right → left
 *   earlier     "one drop earlier"       SHOWN THIS / GUESS THIS on a pair
 *
 * Portrait: the picture on top, the strip as a 3×2 grid beneath it.
 */

const STRIP = [0, 50, 150, 300, 500, 1000];

export const diffuseRainForwardSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AI CONCEPTS'),
  title: z.string().default('Ruining a Picture Is Easy'),
  stripLabel: z.string().default('EXACT ARITHMETIC · NO MODEL INVOLVED'),
  jobLabel: z.string().default('THE MODEL’S JOB: GO BACKWARDS'),
  sparkLine: z.string().default('The model learns to undo one drop at a time.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type DiffuseRainForwardProps = z.infer<typeof diffuseRainForwardSchema>;

export const DiffuseRainForward: React.FC<DiffuseRainForwardProps> = ({
  eyebrow, title, stripLabel, jobLabel, sparkLine, cues,
}) => {
  const { frame, width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CONTENT_W = width - PAD_X * 2;

  const tRain = at('rain', 0.05);
  const tSpeck = at('speckle', 0.24);
  const tArith = at('arithmetic', 0.44);
  const tBack = at('backwards', 0.62);
  const tEarly = at('earlier', 0.86);

  const headIn = sp(0);
  const sPic = sp(Math.max(0, tRain - 0.04));
  const sStrip = STRIP.map((_, i) => sp(clamp(tArith + i * 0.025, 0, 0.97)));
  /* SHELL: the strip's frame arrives with the picture so the right half of the
     frame is never empty at a Gate V sample; its panels still wait for
     "simple arithmetic". */
  const sShell = sp(Math.max(0, tRain - 0.02));
  const sBack = sp(tBack);
  const sEarly = sp(tEarly, SPRING_SNAP);
  const sparkIn = sp(clamp(tEarly + 0.04, 0, 0.97));

  // step ramps 0 → 1000 across the analogy; squared so the first drops are visible
  const r = ramp(tRain, tSpeck);
  const step = Math.round(1000 * r * r);
  const x0 = px(TOY.x0);
  const eps = TOY.eps as unknown as number[];
  const live = forwardMix(x0, eps, step);
  const pic = Math.sqrt(ABAR[step]);
  const noi = Math.sqrt(1 - ABAR[step]);
  const raining = op(sPic) * (1 - ramp(tSpeck, tSpeck + 0.05));

  // ── layout ──────────────────────────────────────────────────────────
  const BIG = portrait ? CONTENT_W * 0.42 : height * 0.43;
  const BIG_X = portrait ? PAD_X + (CONTENT_W - BIG) / 2 : PAD_X;
  const BIG_Y = portrait ? height * 0.235 : height * 0.29;
  const BARS_Y = BIG_Y + BIG + 22 * U;

  const S_X = portrait ? PAD_X : PAD_X + BIG + CONTENT_W * 0.06;
  const S_W = portrait ? CONTENT_W : CONTENT_W - BIG - CONTENT_W * 0.06;
  const S_Y = portrait ? BARS_Y + 170 * U : BIG_Y + BIG / 2 - 150 * U;
  const COLS = 6;
  const GAP = (portrait ? 12 : 16) * U;
  const TW = (S_W - GAP * (COLS - 1)) / COLS;

  const bar = (label: string, v: number, colour: string, i: number) => (
    <div key={label} style={{ marginTop: i ? 12 * U : 0 }}>
      <div style={{
        display: 'flex', justifyContent: 'space-between',
        fontFamily: HAI_TYPE.sans, fontSize: 18 * U, fontWeight: 700, letterSpacing: 1.6,
        color: CLAUDE.INK_SOFT, marginBottom: 5 * U,
      }}>
        <span>{label}</span><span style={{ color: colour, fontFamily: HAI_TYPE.mono }}>× {v.toFixed(v < 0.1 ? 4 : 2)}</span>
      </div>
      <div style={{ height: 12 * U, background: CLAUDE.FOOTER, borderRadius: 6 * U }}>
        <div style={{ width: `${v * 100}%`, height: '100%', background: colour, borderRadius: 6 * U }} />
      </div>
    </div>
  );

  const panel = (t: number, i: number) => {
    const col = i % COLS, row = Math.floor(i / COLS);
    const x = S_X + col * (TW + GAP);
    const y = S_Y + row * (TW + 64 * U);
    const k = op(sStrip[i]);
    const shown = i === 4, guess = i === 3;            // the pair: 500 shown, 300 guessed
    const e = op(sEarly);
    const ring = (shown || guess) && e > 0.2;
    return (
      <div key={t} style={{ position: 'absolute', left: x, top: y, width: TW }}>
        <div style={{
          width: TW, height: TW, borderRadius: 10 * U, background: CLAUDE.FOOTER,
          border: `1.5px dashed ${CLAUDE.BORDER}`, boxSizing: 'border-box', opacity: op(sShell),
          position: 'absolute',
        }} />
        <div style={{ opacity: k, transform: `scale(${0.9 + 0.1 * k})` }}>
          <PixelTile a={forwardMix(x0, eps, t)} size={TW} radius={10 * U}
            frameWidth={ring ? 5 * U : 0} frameColor={guess ? CLAUDE.SPARK : CLAUDE.INK} />
        </div>
        <div style={{
          fontFamily: HAI_TYPE.mono, fontSize: 19 * U, fontWeight: 700, textAlign: 'center',
          color: CLAUDE.INK_SOFT, marginTop: 8 * U, opacity: k,
        }}>step {t}</div>
        {ring && (
          <div style={{
            fontFamily: HAI_TYPE.sans, fontSize: 16 * U, fontWeight: 800, letterSpacing: 1.4,
            textAlign: 'center', marginTop: 4 * U, opacity: e,
            color: guess ? SPARK_TEXT : CLAUDE.INK,
          }}>{guess ? 'GUESS THIS' : 'SHOWN THIS'}</div>
        )}
      </div>
    );
  };

  // the backwards arrow, under the strip, running right → left
  const rows = 1;
  const ARROW_Y = S_Y + rows * (TW + 64 * U) + (portrait ? 14 : 40) * U;
  const kb = op(sBack);
  const aL = S_X + TW * 0.2;
  const aR = S_X + S_W - TW * 0.2;
  const head = aR - (aR - aL) * kb;

  /* ── PORTRAIT (phone): PHONE type scale — less text, larger. The six-panel strip
     becomes the ONE pair the beat is about (step 500 shown, step 300 guessed),
     with the backwards arrow between them. */
  if (portrait) {
    const T = PHONE(height);
    const pBIG = CONTENT_W * 0.5, pY = height * 0.245;
    const RX = PAD_X + pBIG + CONTENT_W * 0.05, RW = CONTENT_W - pBIG - CONTENT_W * 0.05;
    const PT = CONTENT_W * 0.36, PGAP = CONTENT_W * 0.12;
    const PX0 = PAD_X + (CONTENT_W - (PT * 2 + PGAP)) / 2;
    const PY = pY + pBIG + height * 0.028;
    const e = op(sEarly), kb = op(sBack), kp = op(sStrip[0]);
    const readout = (label: string, v: number, colour: string) => (
      <div style={{ marginBottom: height * 0.012 }}>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 700,
          letterSpacing: 1, color: CLAUDE.INK_SOFT, lineHeight: 1 }}>{label}</div>
        <div style={{ fontFamily: HAI_TYPE.mono, fontSize: T.data, fontWeight: 700,
          color: colour, lineHeight: 1.15 }}>× {v.toFixed(v < 0.1 ? 4 : 2)}</div>
        <div style={{ height: 14, background: CLAUDE.FOOTER, borderRadius: 7, marginTop: 6 }}>
          <div style={{ width: `${v * 100}%`, height: '100%', background: colour === SPARK_TEXT ? CLAUDE.SPARK : colour, borderRadius: 7 }} />
        </div>
      </div>
    );
    const pairTile = (t: number, i: number) => (
      <div key={t} style={{ position: 'absolute', left: PX0 + i * (PT + PGAP), top: PY, width: PT }}>
        {/* SHELL: the pair's slots hold their place (Gate V fill) until 'simple arithmetic' */}
        <div style={{ position: 'absolute', left: 0, top: 0, width: PT, height: PT, borderRadius: 10, boxSizing: 'border-box',
          border: `3px dashed ${CLAUDE.GHOST}`, background: CLAUDE.FOOTER, opacity: op(sShell) * (1 - kp) }} />
        <div style={{ opacity: kp }}>
        <PixelTile a={forwardMix(x0, eps, t)} size={PT} radius={10}
          frameWidth={e > 0.2 ? 6 : 0} frameColor={i === 1 ? CLAUDE.SPARK : CLAUDE.INK} />
        <div style={{ textAlign: 'center', marginTop: 10, fontFamily: e > 0.5 ? HAI_TYPE.sans : HAI_TYPE.mono,
          fontSize: T.label, fontWeight: 800, letterSpacing: e > 0.5 ? 1 : 0,
          color: e > 0.5 && i === 1 ? SPARK_TEXT : CLAUDE.INK }}>
          {e > 0.5 ? (i === 0 ? 'SHOWN' : 'GUESS') : String(t)}
        </div>
        </div>
      </div>
    );
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: pY, opacity: op(sPic),
          boxShadow: '0 18px 44px rgba(61,57,41,0.24)', borderRadius: 14 }}>
          <PixelTile a={live} size={pBIG} radius={14} frameWidth={8} frameColor={CLAUDE.CARD} />
          {raining > 0.01 && (
            <svg width={pBIG} height={pBIG} style={{ position: 'absolute', left: 0, top: 0, opacity: raining }}>
              {Array.from({ length: 22 }).map((_, i) => {
                const sx = hash(i, 3.3) * pBIG;
                const speed = 0.6 + hash(i, 9.1) * 0.8;
                const y = ((frame * 14 * speed + hash(i, 1.7) * pBIG * 2) % (pBIG * 1.3)) - pBIG * 0.15;
                return <line key={i} x1={sx} y1={y} x2={sx - 6} y2={y + 34}
                  stroke="#BFD3DC" strokeWidth={3} strokeLinecap="round" opacity={0.8} />;
              })}
            </svg>
          )}
        </div>
        <div style={{ position: 'absolute', left: RX, top: pY, width: RW, opacity: op(sPic) }}>
          {readout('PICTURE', pic, CLAUDE.INK)}
          {readout('NOISE', noi, SPARK_TEXT)}
        </div>
        {pairTile(500, 0)}
        {pairTile(300, 1)}
        <svg width={PGAP} height={60} style={{ position: 'absolute', left: PX0 + PT, top: PY + PT / 2 - 30, opacity: kb }}>
          <path d={`M 14 30 L ${PGAP - 14} 30 M ${PGAP - 34} 12 L ${PGAP - 14} 30 L ${PGAP - 34} 48`}
            fill="none" stroke={CLAUDE.SPARK} strokeWidth={8} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
          height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn}
        padX={PAD_X} height={height} width={width} portrait={portrait} />

      {/* ══ the photo in the rain ════════════════════════════════════ */}
      <div style={{
        position: 'absolute', left: BIG_X, top: BIG_Y, opacity: op(sPic),
        transform: `rotate(${-1.5 * op(sPic)}deg)`,
        boxShadow: '0 18px 44px rgba(61,57,41,0.24)', borderRadius: 14 * U,
      }}>
        <PixelTile a={live} size={BIG} radius={14 * U} frameWidth={8 * U} frameColor={CLAUDE.CARD} />
        {raining > 0.01 && (
          <svg width={BIG} height={BIG} style={{ position: 'absolute', left: 0, top: 0, opacity: raining }}>
            {Array.from({ length: 28 }).map((_, i) => {
              const sx = hash(i, 3.3) * BIG;
              const speed = 0.6 + hash(i, 9.1) * 0.8;
              const y = ((frame * 14 * U * speed + hash(i, 1.7) * BIG * 2) % (BIG * 1.3)) - BIG * 0.15;
              return <line key={i} x1={sx} y1={y} x2={sx - 6 * U} y2={y + 34 * U}
                stroke="#BFD3DC" strokeWidth={3 * U} strokeLinecap="round" opacity={0.8} />;
            })}
          </svg>
        )}
      </div>
      <div style={{
        position: 'absolute', left: BIG_X, top: BARS_Y, width: BIG, opacity: op(sPic),
      }}>
        <div style={{
          fontFamily: HAI_TYPE.mono, fontSize: 22 * U, fontWeight: 700, color: CLAUDE.INK,
          marginBottom: 10 * U,
        }}>step {step} / 1000</div>
        {bar('HOW MUCH PICTURE', pic, CLAUDE.INK, 0)}
        {bar('HOW MUCH NOISE', noi, SPARK_TEXT, 1)}
      </div>

      {/* ══ the strip ════════════════════════════════════════════════ */}
      <div style={{
        position: 'absolute', left: S_X, top: S_Y - 44 * U,
        fontFamily: HAI_TYPE.sans, fontSize: 20 * U, fontWeight: 800, letterSpacing: 2.4,
        color: CLAUDE.INK_SOFT, opacity: op(sStrip[0]),
      }}>{stripLabel}</div>
      {STRIP.map(panel)}

      <svg width={width} height={80 * U} style={{
        position: 'absolute', left: 0, top: ARROW_Y, opacity: kb, overflow: 'visible',
      }}>
        <line x1={aR} y1={20 * U} x2={head} y2={20 * U} stroke={CLAUDE.SPARK}
          strokeWidth={6 * U} strokeLinecap="round" />
        <path d={`M ${head + 20 * U} ${6 * U} L ${head} ${20 * U} L ${head + 20 * U} ${34 * U}`}
          fill="none" stroke={CLAUDE.SPARK} strokeWidth={6 * U} strokeLinecap="round" strokeLinejoin="round" />
      </svg>
      <div style={{
        position: 'absolute', left: S_X, top: ARROW_Y + 44 * U, width: S_W, textAlign: 'center',
        fontFamily: HAI_TYPE.sans, fontSize: 21 * U, fontWeight: 800, letterSpacing: 2.2,
        color: SPARK_TEXT, opacity: kb,
      }}>{jobLabel}</div>

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
        height={height} portrait={portrait}
        top={portrait ? height * 0.722 : undefined} />
    </AbsoluteFill>
  );
};
