import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, SPARK_TEXT, PHONE,
} from '../lib/cueKit';
import { TOY } from './diffusion/toyData';
import { PixelTile, StaticField, snapshotAt, px, SCREEN_DARK } from './diffusion/diffusionKit';

/**
 * DiffuseSeedStatic — B01 of "How AI Image Generators Turn Noise Into a Picture."
 *
 * The background beat: where every image starts. A television fills the left of
 * the frame with static while Midjourney's own documentation is quoted beside
 * it. When the narration names the SEED, the full-screen static coarsens into
 * one specific 16×16 field — the actual starting noise of the toy model's seed-7
 * run — and from "removes a little of the noise" that exact field is walked back
 * through its recorded steps until the picture is left.
 *
 *   guide   "own guide says it plainly"       quote card
 *   tv      "static on an old TV"             the quote's key phrase lights
 *   seed    "called a seed"                   --seed chip; static -> the seed's field
 *   remove  "removes a little of the noise"   the loop starts; the step counter runs
 *   left    "a picture is left"               step 0, the picture framed in spark
 *
 * HONESTY: the TV's opening static is decorative house noise. From `seed` on,
 * every pixel is the toy model's recorded run (toyData.ts), labelled as a toy.
 * Portrait: the TV spans the width, the quote and loop sit beneath it.
 */

export const diffuseSeedStaticSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AI CONCEPTS'),
  title: z.string().default('Every Image Starts as Static'),
  quote: z.string().default('the random noise you see on a TV screen'),
  quoteSource: z.string().default('Midjourney documentation, “Seeds”'),
  seedLabel: z.string().default('--seed 7'),
  runIndex: z.number().default(0),
  toyLabel: z.string().default('TOY MODEL · trained from scratch on a laptop · not Midjourney'),
  sparkLine: z.string().default('The picture is found in the noise, one step at a time.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type DiffuseSeedStaticProps = z.infer<typeof diffuseSeedStaticSchema>;

export const DiffuseSeedStatic: React.FC<DiffuseSeedStaticProps> = ({
  eyebrow, title, quote, quoteSource, seedLabel, runIndex, toyLabel, sparkLine, cues,
}) => {
  const { frame, width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CONTENT_W = width - PAD_X * 2;
  const run = TOY.runs[runIndex] ?? TOY.runs[0];

  const tGuide = at('guide', 0.02);
  const tTv = at('tv', 0.2);
  const tSeed = at('seed', 0.36);
  const tRemove = at('remove', 0.62);
  const tLeft = at('left', 0.88);

  const headIn = sp(0);
  const sTv = sp(0.0);
  const sQuote = sp(tGuide);
  const sPhrase = sp(tTv);
  const sSeed = sp(tSeed, SPRING_SNAP);
  const sLoop = sp(tRemove);
  const sDone = sp(tLeft, SPRING_SNAP);
  const sparkIn = sp(clamp(tLeft + 0.05, 0, 0.97));

  // the reverse walk: step 1000 at `remove`, step 0 at `left`
  const walk = ramp(tRemove, tLeft);
  const eased = 1 - Math.pow(1 - walk, 1.6);
  const step = Math.round(1000 * (1 - eased));
  const snap = snapshotAt(run.frames, step, TOY.keepEvery);

  // ── layout ──────────────────────────────────────────────────────────
  const TV_W = portrait ? CONTENT_W * 0.8 : CONTENT_W * 0.46;
  const TV_H = TV_W * 0.75;
  const TV_X = portrait ? PAD_X + (CONTENT_W - TV_W) / 2 : PAD_X;
  const TV_Y = portrait ? height * 0.235 : height * 0.285;
  const SCR_PAD = TV_W * 0.045;
  const SCR_W = TV_W - SCR_PAD * 2;
  const SCR_H = TV_H - SCR_PAD * 2;
  const TILE = Math.min(SCR_W, SCR_H) * 0.8;

  const R_X = portrait ? PAD_X : TV_X + TV_W + CONTENT_W * 0.05;
  const R_W = portrait ? CONTENT_W : CONTENT_W - (R_X - PAD_X);
  const R_Y = portrait ? TV_Y + TV_H + 56 * U : TV_Y;

  const kStatic = 1 - op(sSeed);          // full-screen static gives way to the seed's field
  const kField = op(sSeed);

  // quote with its key phrase lit
  const key = 'TV screen';
  const qi = quote.indexOf(key);
  const Q = (portrait ? 40 : 50) * U;

  /* ── PORTRAIT (phone): the 9:16 type spec's scale (PHONE) — less text, larger.
     title · the TV with a TOY MODEL sticker · one readout row · the quote · spark.
     The loop sentence is dropped here; the narration carries it. */
  if (portrait) {
    const T = PHONE(height);
    const pTV_W = CONTENT_W * 0.8, pTV_H = pTV_W * 0.75;   // Gate V: the 9:16 safe box is y 96-1824; fill it
    const pTV_X = PAD_X, pTV_Y = height * 0.245;
    const pPad = pTV_W * 0.045, pSW = pTV_W - pPad * 2, pSH = pTV_H - pPad * 2;
    const pTile = Math.min(pSW, pSH) * 0.86;
    const ROW_Y = pTV_Y + pTV_H + height * 0.012;
    const Q_Y = ROW_Y + T.data * 1.45;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        <div style={{
          position: 'absolute', left: pTV_X, top: pTV_Y, width: pTV_W, height: pTV_H,
          background: CLAUDE.INK, borderRadius: 24, opacity: op(sTv),
          boxShadow: '0 20px 50px rgba(61,57,41,0.28)',
        }}>
          <div style={{
            position: 'absolute', left: pPad, top: pPad, width: pSW, height: pSH,
            borderRadius: 16, overflow: 'hidden', background: SCREEN_DARK,
          }}>
            {kStatic > 0.01 && (
              <div style={{ position: 'absolute', inset: 0, opacity: kStatic }}>
                <StaticField cols={40} rows={30} w={pSW} h={pSH} frame={frame} />
              </div>
            )}
            <div style={{
              position: 'absolute', left: (pSW - pTile) / 2, top: (pSH - pTile) / 2,
              opacity: kField, transform: `scale(${0.85 + 0.15 * kField})`,
            }}>
              <PixelTile a={step >= 1000 ? px(run.frames[0]) : snap.a}
                b={step >= 1000 ? undefined : snap.b} mix={snap.mix} size={pTile} radius={8}
                frameWidth={op(sDone) > 0.3 ? 6 : 0} frameColor={CLAUDE.SPARK} />
            </div>
          </div>
          <div style={{
            position: 'absolute', right: -PAD_X * 0.4, top: -T.label * 0.55,
            fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 1,
            color: CLAUDE.CARD, background: CLAUDE.INK, border: `4px solid ${CLAUDE.CARD}`,
            borderRadius: 12, padding: '2px 18px', transform: 'rotate(3deg)', opacity: kField,
          }}>TOY MODEL</div>
        </div>
        <div style={{
          position: 'absolute', left: PAD_X, top: ROW_Y, width: CONTENT_W,
          fontFamily: HAI_TYPE.mono, fontSize: T.data, fontWeight: 700, whiteSpace: 'nowrap',
          color: op(sDone) > 0.5 ? SPARK_TEXT : CLAUDE.INK, opacity: kField,
        }}>{seedLabel}{op(sLoop) > 0.05 ? ` · step ${step}` : ''}</div>
        <div style={{
          position: 'absolute', left: PAD_X, top: Q_Y, width: CONTENT_W,
          fontFamily: HAI_TYPE.serif, fontSize: T.body, lineHeight: 1.12, color: CLAUDE.INK,
          opacity: op(sQuote), transform: `translateY(${(1 - op(sQuote)) * 20}px)`,
        }}>
          <span style={{ color: SPARK_TEXT }}>“</span>
          {qi >= 0 ? (
            <>
              {quote.slice(0, qi)}
              <span style={{ color: op(sPhrase) > 0.5 ? SPARK_TEXT : CLAUDE.INK }}>{key}</span>
              {quote.slice(qi + key.length)}
            </>
          ) : quote}
          <span style={{ color: SPARK_TEXT }}>”</span>
          <div style={{
            fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 700, letterSpacing: 1,
            color: CLAUDE.INK_SOFT, marginTop: 14,
          }}>— MIDJOURNEY DOCS</div>
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

      {/* ══ the television ═══════════════════════════════════════════ */}
      <div style={{
        position: 'absolute', left: TV_X, top: TV_Y, width: TV_W, height: TV_H,
        background: CLAUDE.INK, borderRadius: 28 * U, opacity: op(sTv),
        boxShadow: '0 24px 60px rgba(61,57,41,0.28)',
      }}>
        <div style={{
          position: 'absolute', left: SCR_PAD, top: SCR_PAD, width: SCR_W, height: SCR_H,
          borderRadius: 18 * U, overflow: 'hidden', background: SCREEN_DARK,
        }}>
          {kStatic > 0.01 && (
            <div style={{ position: 'absolute', inset: 0, opacity: kStatic }}>
              <StaticField cols={64} rows={48} w={SCR_W} h={SCR_H} frame={frame} />
            </div>
          )}
          <div style={{
            position: 'absolute', left: (SCR_W - TILE) / 2, top: (SCR_H - TILE) / 2,
            opacity: kField, transform: `scale(${0.85 + 0.15 * kField})`,
          }}>
            <PixelTile a={step >= 1000 ? px(run.frames[0]) : snap.a}
              b={step >= 1000 ? undefined : snap.b} mix={snap.mix} size={TILE} radius={8 * U}
              frameWidth={op(sDone) > 0.3 ? 6 * U : 0} frameColor={CLAUDE.SPARK} />
          </div>
          {/* the step counter, on the screen */}
          <div style={{
            position: 'absolute', right: 14 * U, bottom: 12 * U,
            fontFamily: HAI_TYPE.mono, fontSize: 24 * U, fontWeight: 700,
            /* on the DARK screen the deep text-terracotta would be too dark (2.7:1);
               a light terracotta tint keeps the accent and reads at >8:1 */
            color: op(sDone) > 0.5 ? '#F4B49A' : '#EDE6D6',
            background: 'rgba(34,31,26,0.78)', borderRadius: 6 * U,
            padding: `${4 * U}px ${10 * U}px`, opacity: op(sLoop),
          }}>step {step}</div>
          <div style={{
            position: 'absolute', left: 14 * U, top: 12 * U,
            fontFamily: HAI_TYPE.mono, fontSize: 24 * U, fontWeight: 700, color: '#EDE6D6',
            background: 'rgba(34,31,26,0.78)', borderRadius: 6 * U,
            padding: `${4 * U}px ${10 * U}px`, opacity: kField,
          }}>{seedLabel}</div>
        </div>
      </div>
      <div style={{
        position: 'absolute', left: TV_X, top: TV_Y + TV_H + 12 * U, width: TV_W,
        fontFamily: HAI_TYPE.sans, fontSize: 17 * U, fontWeight: 700, letterSpacing: 1.4,
        color: CLAUDE.INK_SOFT, opacity: kField, textAlign: portrait ? 'center' : 'left',
      }}>{toyLabel}</div>

      {/* ══ the quote ════════════════════════════════════════════════ */}
      <div style={{
        position: 'absolute', left: R_X, top: R_Y, width: R_W,
        opacity: op(sQuote), transform: `translateY(${(1 - op(sQuote)) * 20 * U}px)`,
      }}>
        <div style={{
          fontFamily: HAI_TYPE.serif, fontSize: Q * 2.2, lineHeight: 0.6,
          color: SPARK_TEXT, height: Q * 0.9,
        }}>“</div>
        <div style={{ fontFamily: HAI_TYPE.serif, fontSize: Q, lineHeight: 1.22, color: CLAUDE.INK }}>
          {qi >= 0 ? (
            <>
              {quote.slice(0, qi)}
              <span style={{
                color: op(sPhrase) > 0.5 ? SPARK_TEXT : CLAUDE.INK,
                backgroundImage: `linear-gradient(${CLAUDE.SPARK}33, ${CLAUDE.SPARK}33)`,
                backgroundSize: `${op(sPhrase) * 100}% 38%`, backgroundRepeat: 'no-repeat',
                backgroundPosition: '0 88%',
              }}>{key}</span>
              {quote.slice(qi + key.length)}
            </>
          ) : quote}
        </div>
        <div style={{
          fontFamily: HAI_TYPE.sans, fontSize: 20 * U, fontWeight: 600, letterSpacing: 0.4,
          color: CLAUDE.INK_SOFT, marginTop: 16 * U,
        }}>— {quoteSource}</div>
      </div>

      {/* ══ the loop: look, remove a little, repeat ══════════════════ */}
      <div style={{
        position: 'absolute', left: R_X,
        top: portrait ? R_Y + 150 * U : R_Y + TV_H * 0.56, width: R_W,
        display: 'flex', alignItems: 'center', gap: 22 * U, opacity: op(sLoop),
      }}>
        <svg width={92 * U} height={92 * U} style={{ flexShrink: 0 }}>
          <g transform={`translate(${46 * U} ${46 * U}) rotate(${frame * 6 * (1 - op(sDone))})`}>
            <circle r={36 * U} fill="none" stroke={CLAUDE.BORDER} strokeWidth={6 * U} />
            <path d={`M ${36 * U} 0 A ${36 * U} ${36 * U} 0 1 1 0 ${-36 * U}`} fill="none"
              stroke={CLAUDE.SPARK} strokeWidth={6 * U} strokeLinecap="round" />
            <path d={`M ${-9 * U} ${-46 * U} L ${3 * U} ${-36 * U} L ${-9 * U} ${-26 * U}`}
              fill="none" stroke={CLAUDE.SPARK} strokeWidth={6 * U} strokeLinecap="round" strokeLinejoin="round" />
          </g>
        </svg>
        <div>
          <div style={{
            fontFamily: HAI_TYPE.serif, fontSize: (portrait ? 36 : 40) * U, fontWeight: 600,
            color: CLAUDE.INK, lineHeight: 1.2,
          }}>Look at the static. Remove a little noise. Repeat.</div>
          <div style={{
            fontFamily: HAI_TYPE.sans, fontSize: 20 * U, fontWeight: 700, letterSpacing: 1.6,
            color: CLAUDE.INK_SOFT, marginTop: 8 * U,
          }}>1,000 TIMES IN THIS TOY</div>
        </div>
      </div>

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
        height={height} portrait={portrait}
        top={portrait ? height * 0.72 : undefined} />
    </AbsoluteFill>
  );
};
