import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, SPARK_TEXT, PHONE,
} from '../lib/cueKit';
import { TOY } from './diffusion/toyData';
import { PixelTile, snapshotAt, px } from './diffusion/diffusionKit';

/**
 * DiffuseSeedPrompt — B05 of "How AI Image Generators Turn Noise Into a Picture."
 *
 * The two controls, separated. LEFT: one seed's static forks under two prompts —
 * the toy model's seed-7 runs for "heart" and "music note", which start from
 * the identical field. RIGHT: one prompt under four seeds — four real runs that
 * resolve side by side into four different hearts, framed as the grid of four a
 * Midjourney user already knows. Every tile is a recorded run (toyData.ts).
 *
 *   same    "Keep the same static"          the shared seed-7 field, both forks
 *   note    "becomes a note"                the note fork resolves
 *   change  "change the seed"               four fresh fields appear
 *   every   "different heart every time"    all four resolve
 *   four    "four different starting…"      the grid frame + label
 *
 * Portrait: the fork on top, the grid of four beneath it.
 */

export const diffuseSeedPromptSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AI CONCEPTS'),
  title: z.string().default('What the Seed Decides'),
  leftHeader: z.string().default('SAME STATIC · DIFFERENT PROMPT'),
  rightHeader: z.string().default('SAME PROMPT · FOUR SEEDS'),
  gridLabel: z.string().default('one prompt, four starting points — like your grid of four'),
  sparkLine: z.string().default('The prompt steers. The seed sets where you start.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type DiffuseSeedPromptProps = z.infer<typeof diffuseSeedPromptSchema>;

export const DiffuseSeedPrompt: React.FC<DiffuseSeedPromptProps> = ({
  eyebrow, title, leftHeader, rightHeader, gridLabel, sparkLine, cues,
}) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CONTENT_W = width - PAD_X * 2;

  const tSame = at('same', 0.08);
  const tNote = at('note', 0.36);
  const tChange = at('change', 0.5);
  const tEvery = at('every', 0.6);
  const tFour = at('four', 0.9);

  const headIn = sp(0);
  const sLeft = sp(Math.max(0, tSame - 0.04));
  const sRight = sp(Math.max(0, tSame - 0.02));           // shell for the grid
  const sFour = sp(tFour, SPRING_SNAP);
  const sparkIn = sp(clamp(tFour + 0.04, 0, 0.97));

  /* The fork uses the seed scan_seeds.py chose by its logged rule (TOY.forkSeed);
     the grid is the four fixed training-time seeds. Looked up by prompt + seed,
     never by position. */
  const find = (prompt: string, seed: number) =>
    TOY.runs.find(r => r.prompt === prompt && r.seed === seed) ?? TOY.runs[0];
  const heart7 = find('heart', TOY.forkSeed);
  const note7 = find('music note', TOY.forkSeed);
  const grid = [101, 202, 303, 404].map(s => find('heart', s));

  // both forks resolve from `same` to `note`; the grid from `change` to past `every`
  const forkStep = Math.round(1000 * (1 - ramp(tSame + 0.03, tNote)));
  const gridStep = Math.round(1000 * (1 - ramp(tChange, Math.min(0.96, tEvery + 0.14))));
  const kGrid = op(sp(Math.max(0, tChange - 0.03)));

  const tile = (frames: readonly string[], step: number, size: number, frameColor?: string) => {
    const s = snapshotAt(frames, step, TOY.keepEvery);
    return <PixelTile a={step >= 1000 ? px(frames[0]) : s.a} b={step >= 1000 ? undefined : s.b}
      mix={s.mix} size={size} radius={10 * U} frameWidth={frameColor ? 5 * U : 0} frameColor={frameColor} />;
  };
  const label = (text: string, colour: string = CLAUDE.INK_SOFT) => (
    <div style={{
      fontFamily: HAI_TYPE.sans, fontSize: 17 * U, fontWeight: 800, letterSpacing: 1.6,
      color: colour, marginTop: 8 * U, textAlign: 'center',
    }}>{text}</div>
  );
  const header = (text: string, k: number) => (
    <div style={{
      fontFamily: HAI_TYPE.sans, fontSize: 21 * U, fontWeight: 800, letterSpacing: 2.4,
      color: SPARK_TEXT, marginBottom: 18 * U, opacity: k,
    }}>{text}</div>
  );

  // ── layout ──────────────────────────────────────────────────────────
  const T = portrait ? 206 * U : 240 * U;          // fork tiles
  const G = portrait ? 206 * U : 210 * U;          // grid tiles
  const GG = 18 * U;
  const TOP = portrait ? height * 0.235 : height * 0.29;
  const LEFT_W = portrait ? CONTENT_W : CONTENT_W * 0.5;
  const GRID_W = G * 2 + GG + 28 * U + 8 * U;
  const R_X = portrait ? PAD_X : PAD_X + CONTENT_W - GRID_W;   // pinned right: the frame is used edge to edge
  const R_Y = portrait ? TOP + T * 2 + 100 * U : TOP;
  const ARROW_W = portrait ? 150 * U : 170 * U;

  const kl = op(sLeft);
  /* ── PORTRAIT (phone): PHONE type scale — less text, larger. The fork's labels
     sit beside its outputs; the four seeds run as one row with the seed number
     on each tile; the grid caption is landscape-only (the spark line says it). */
  if (portrait) {
    const T = PHONE(height);
    const H1_Y = height * 0.245;
    const F_Y = H1_Y + T.label * 1.35;
    const OUT = CONTENT_W * 0.2, OG = 20, START = CONTENT_W * 0.26, AR = CONTENT_W * 0.12;
    const forkH = OUT * 2 + OG;
    const S_Y = F_Y + (forkH - START) / 2;
    const H2_Y = F_Y + forkH + height * 0.012;
    const G_Y = H2_Y + T.label * 1.35;
    const GT = (CONTENT_W - 18 * 3) / 4;
    const hdr = (t: string, y: number, k: number) => (
      <div style={{ position: 'absolute', left: PAD_X, top: y, opacity: k, whiteSpace: 'nowrap',
        fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 1, color: SPARK_TEXT }}>{t}</div>
    );
    const snapTile = (frames: readonly string[], st: number, size: number, frameColor?: string) => {
      const s2 = snapshotAt(frames, st, TOY.keepEvery);
      return <PixelTile a={st >= 1000 ? px(frames[0]) : s2.a} b={st >= 1000 ? undefined : s2.b}
        mix={s2.mix} size={size} radius={10} frameWidth={frameColor ? 6 : 0} frameColor={frameColor} />;
    };
    const outLabel = (t: string, y: number, colour: string) => (
      <div style={{ position: 'absolute', left: PAD_X + START + AR + OUT + 22, top: y + OUT / 2 - T.label * 0.6,
        fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 1, color: colour, opacity: op(sLeft) }}>{t}</div>
    );
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        {hdr(leftHeader, H1_Y, op(sLeft))}
        <div style={{ position: 'absolute', left: PAD_X, top: S_Y, opacity: op(sLeft) }}>
          {snapTile(heart7.frames, 1000, START)}
          <div style={{ fontFamily: HAI_TYPE.mono, fontSize: T.label, fontWeight: 700, color: CLAUDE.INK, marginTop: 8 }}>seed {heart7.seed}</div>
        </div>
        <svg width={AR} height={forkH} style={{ position: 'absolute', left: PAD_X + START, top: F_Y, opacity: op(sLeft) }}>
          {[0, 1].map(i => {
            const y1 = forkH / 2, y2 = i === 0 ? OUT / 2 : OUT * 1.5 + OG;
            return <path key={i} d={`M 6 ${y1} C ${AR * 0.5} ${y1}, ${AR * 0.5} ${y2}, ${AR - 8} ${y2}`}
              fill="none" stroke={i === 0 ? CLAUDE.INK : CLAUDE.SPARK} strokeWidth={6} strokeLinecap="round" />;
          })}
        </svg>
        <div style={{ position: 'absolute', left: PAD_X + START + AR, top: F_Y, opacity: op(sLeft) }}>
          {snapTile(heart7.frames, forkStep, OUT)}
          <div style={{ height: OG }} />
          {snapTile(note7.frames, forkStep, OUT)}
        </div>
        {outLabel('HEART', F_Y, CLAUDE.INK)}
        {outLabel('NOTE', F_Y + OUT + OG, SPARK_TEXT)}
        {hdr(rightHeader, H2_Y, op(sRight))}
        <div style={{ position: 'absolute', left: PAD_X, top: G_Y, display: 'flex', gap: 18, opacity: op(sRight) }}>
          {grid.map((r, i) => (
            <div key={i} style={{ position: 'relative', width: GT, height: GT, borderRadius: 10,
              background: CLAUDE.FOOTER, border: kGrid > 0.05 ? 'none' : `3px dashed ${CLAUDE.GHOST}`, boxSizing: 'border-box' }}>
              <div style={{ position: 'absolute', inset: 0, opacity: kGrid }}>
                {snapTile(r.frames, gridStep, GT, op(sFour) > 0.3 ? CLAUDE.SPARK : undefined)}
              </div>
              <div style={{ position: 'absolute', left: 8, top: 8, opacity: kGrid,
                fontFamily: HAI_TYPE.mono, fontSize: T.label * 0.98, fontWeight: 700, color: '#F6F0E3',
                background: 'rgba(34,31,26,0.82)', borderRadius: 8, padding: '0 10px' }}>{r.seed}</div>
            </div>
          ))}
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

      {/* ══ one static, two prompts ══════════════════════════════════ */}
      <div style={{ position: 'absolute', left: PAD_X, top: TOP, width: LEFT_W }}>
        {header(leftHeader, kl)}
        <div style={{ display: 'flex', alignItems: 'center', opacity: kl }}>
          <div>
            {tile(heart7.frames, 1000, T)}
            {label(`SEED ${heart7.seed}`)}
          </div>
          <svg width={ARROW_W} height={T * 2 + 40 * U} style={{ flexShrink: 0 }}>
            {[0, 1].map(i => {
              const y1 = T * 2 * 0.5 + 20 * U;
              const y2 = i === 0 ? T * 0.5 : T * 1.5 + 40 * U;
              return <path key={i} d={`M ${10 * U} ${y1} C ${ARROW_W * 0.5} ${y1}, ${ARROW_W * 0.5} ${y2}, ${ARROW_W - 16 * U} ${y2}`}
                fill="none" stroke={i === 0 ? CLAUDE.INK : CLAUDE.SPARK} strokeWidth={4 * U} strokeLinecap="round" />;
            })}
          </svg>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 40 * U - 25 * U }}>
            <div>
              {tile(heart7.frames, forkStep, T * 0.9)}
              {label('“HEART”', CLAUDE.INK)}
            </div>
            <div>
              {tile(note7.frames, forkStep, T * 0.9)}
              {label('“MUSIC NOTE”', SPARK_TEXT)}
            </div>
          </div>
        </div>
      </div>

      {/* ══ one prompt, four seeds ═══════════════════════════════════ */}
      <div style={{ position: 'absolute', left: R_X, top: R_Y }}>
        {header(rightHeader, op(sRight))}
        <div style={{
          display: 'grid', gridTemplateColumns: `repeat(${portrait ? 4 : 2}, ${G}px)`, gap: GG,
          padding: 14 * U, borderRadius: 16 * U,
          border: `${op(sFour) > 0.3 ? 4 : 1.5}px ${kGrid > 0.05 ? 'solid' : 'dashed'} ${op(sFour) > 0.3 ? CLAUDE.SPARK : CLAUDE.BORDER}`,
          background: CLAUDE.CARD, opacity: op(sRight),
        }}>
          {grid.map((r, i) => (
            <div key={i} style={{ opacity: kGrid }}>
              {tile(r.frames, gridStep, portrait ? (CONTENT_W - 28 * U - GG * 3) / 4 : G)}
              {label(`SEED ${r.seed}`)}
            </div>
          ))}
        </div>
        {portrait && (
          <div style={{
            fontFamily: HAI_TYPE.serif, fontStyle: 'italic', fontSize: 28 * U,
            color: CLAUDE.INK, marginTop: 14 * U, opacity: op(sFour), width: CONTENT_W,
          }}>{gridLabel}</div>
        )}
      </div>
      {!portrait && (
        <div style={{
          position: 'absolute', left: PAD_X, top: height * 0.80, width: CONTENT_W - GRID_W - 40 * U,
          fontFamily: HAI_TYPE.serif, fontStyle: 'italic', fontSize: 34 * U,
          color: CLAUDE.INK, opacity: op(sFour),
        }}>
          <span style={{ color: SPARK_TEXT }}>→ </span>{gridLabel}
        </div>
      )}

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
        height={height} portrait={portrait}
        top={portrait ? height * 0.722 : undefined} />
    </AbsoluteFill>
  );
};
