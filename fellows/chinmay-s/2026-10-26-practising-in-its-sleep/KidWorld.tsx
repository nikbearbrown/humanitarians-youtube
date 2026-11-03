import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { useRise, Eyebrow, SparkLine, Page, Card } from './IndexedOrInvisible';
import { Robo } from './KidEval';

/**
 * KidWorld — the kid-friendly cut of "a machine that practises in its sleep".
 *
 * Subject: a from-scratch World Models notebook (NumPy only): a VAE that squeezes
 * 16x16 frames to 8 numbers, a memory network that predicts the next frame, and a
 * controller evolved ENTIRELY inside the model's dream, which then plays the real
 * game. This reel TEACHES; it is not a teardown.
 *
 * Every figure is parsed from the notebook's recorded outputs at build time.
 * Claude palette only: cream, warm ink, one terracotta.
 */

const U = CLAUDE_FONT.ui;
const M = CLAUDE_FONT.mono;
const S = CLAUDE_FONT.serif;

const bob = (f: number, a = 5, s = 0.055) => Math.sin(f * s) * a;

/** A 16x16 Catch board: ball at (bx, by), paddle of width 3 at px. */
const Board: React.FC<{
  x: number; y: number; cell: number; bx: number; by: number; px: number;
  dim?: boolean; ghost?: boolean;
}> = ({ x, y, cell, bx, by, px, dim, ghost }) => {
  const N = 16;
  const items: React.ReactNode[] = [];
  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      const isBall = r === Math.round(by) && c === Math.round(bx);
      const isPaddle = r === N - 1 && c >= px && c < px + 3;
      const on = isBall || isPaddle;
      items.push(
        <div key={`${r}-${c}`} style={{
          position: 'absolute', left: x + c * cell, top: y + r * cell,
          width: cell - 2, height: cell - 2, borderRadius: 2,
          background: on ? (isBall ? CLAUDE.SPARK : CLAUDE.INK) : CLAUDE.PILL,
          opacity: dim ? 0.35 : ghost && on ? 0.4 : 1,
        }} />,
      );
    }
  }
  return <>{items}</>;
};

// ── 1. KidCatchGame — the whole game in one picture ────────────────────────

export const kidCatchGameSchema = z.object({});

export const KidCatchGame: React.FC = () => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [16, 110], [0, 13], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const bx = 3 + t * 0.62;
  const by = t;
  const px = Math.max(0, Math.min(13, Math.round(3 + t * 0.62) - 1));
  const caught = useRise(118);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="one very small game" />
      </div>
      <Board x={420} y={190} cell={42} bx={bx} by={by} px={px} />
      <div style={{ position: 'absolute', left: 1180, top: 300, right: 130 }}>
        <div style={{ fontFamily: S, fontSize: 50, color: CLAUDE.INK, lineHeight: 1.3 }}>
          A ball falls. A paddle slides. Catch it.
        </div>
        <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT, marginTop: 20, lineHeight: 1.5 }}>
          Sixteen squares across, sixteen down. Three buttons: left, right, stay.
        </div>
        {caught > 0.02 ? (
          <div style={{ marginTop: 30, opacity: caught, fontFamily: M, fontSize: 40, color: CLAUDE.SEND }}>
            caught ✓
          </div>
        ) : null}
      </div>
      <SparkLine text="Small enough to see every pixel. Hard enough to be interesting." delay={126} />
    </Page>
  );
};

// ── 2. KidOneFrame — a snapshot is not a situation ─────────────────────────

export const kidOneFrameSchema = z.object({});

export const KidOneFrame: React.FC = () => {
  const frame = useCurrentFrame();
  const one = useRise(6);
  const split = useRise(40);
  const punch = useRise(90);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="why one picture is never enough" />
      </div>
      <div style={{ opacity: one }}>
        <Board x={170} y={230} cell={26} bx={7} by={5} px={6} />
      </div>
      <div style={{ position: 'absolute', left: 170, top: 680, width: 420, opacity: one }}>
        <div style={{ fontFamily: U, fontSize: 26, color: CLAUDE.INK_SOFT }}>
          here is one frame. which way is the ball going?
        </div>
      </div>

      {split > 0.02 ? (
        <>
          <div style={{ opacity: split }}>
            <Board x={760} y={230} cell={26} bx={4} by={11} px={6} />
            <Board x={1270} y={230} cell={26} bx={10} by={11} px={6} />
          </div>
          <div style={{ position: 'absolute', left: 760, top: 680, width: 400, opacity: split }}>
            <div style={{ fontFamily: U, fontSize: 26, color: CLAUDE.SEND }}>if it came from the right…</div>
          </div>
          <div style={{ position: 'absolute', left: 1270, top: 680, width: 400, opacity: split }}>
            <div style={{ fontFamily: U, fontSize: 26, color: CLAUDE.SEND }}>…and if it came from the left</div>
          </div>
        </>
      ) : null}

      {punch > 0.02 ? (
        <div style={{ position: 'absolute', left: 130, right: 130, top: 790, opacity: punch }}>
          <div style={{ fontFamily: S, fontSize: 52, color: CLAUDE.INK, lineHeight: 1.3 }}>
            Same picture. Opposite endings.
          </div>
        </div>
      ) : null}
      <SparkLine text="You cannot see speed in a photograph. You have to remember." delay={100} />
    </Page>
  );
};

// ── 3. KidSqueeze — 256 pixels into 8 numbers ──────────────────────────────

export const kidSqueezeSchema = z.object({
  pixels: z.string().default('256'),
  numbers: z.string().default('8'),
  ratio: z.string().default('32x'),
  perfect: z.string().default('99.3%'),
});
export type KidSqueezeProps = z.infer<typeof kidSqueezeSchema>;

export const KidSqueeze: React.FC<KidSqueezeProps> = ({ pixels, numbers, ratio, perfect }) => {
  const frame = useCurrentFrame();
  const a = useRise(5);
  const nums = useRise(34);
  const back = useRise(66);
  const score = useRise(96);
  const N = parseInt(numbers, 10) || 8;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="squeeze the picture down" />
      </div>
      <div style={{ opacity: a }}>
        <Board x={150} y={230} cell={22} bx={9} by={6} px={5} />
      </div>
      <div style={{ position: 'absolute', left: 150, top: 620, fontFamily: U, fontSize: 25, color: CLAUDE.INK_SOFT }}>
        {pixels} squares
      </div>

      {/* the 8 numbers */}
      <div style={{
        position: 'absolute', left: 620, top: 330, width: 560, opacity: nums,
        display: 'flex', flexWrap: 'wrap', gap: 12,
      }}>
        {Array.from({ length: N }, (_, i) => (
          <div key={i} style={{
            width: 125, padding: '14px 0', textAlign: 'center',
            background: '#FBEEE8', border: `2px solid ${CLAUDE.SPARK}`, borderRadius: 10,
            fontFamily: M, fontSize: 26, color: CLAUDE.SEND,
          }}>{(Math.sin(i * 2.3 + 1) * 1.7).toFixed(2)}</div>
        ))}
        <div style={{ width: '100%', fontFamily: U, fontSize: 25, color: CLAUDE.INK_SOFT, marginTop: 10 }}>
          just {numbers} numbers — {ratio} smaller
        </div>
      </div>

      {/* rebuilt */}
      <div style={{ opacity: back }}>
        <Board x={1330} y={230} cell={22} bx={9} by={6} px={5} />
      </div>
      <div style={{
        position: 'absolute', left: 1330, top: 620, fontFamily: U, fontSize: 25, color: CLAUDE.INK_SOFT, opacity: back,
      }}>
        built back from those numbers
      </div>

      {score > 0.02 ? (
        <div style={{ position: 'absolute', left: 130, right: 130, top: 740, opacity: score }}>
          <div style={{ fontFamily: S, fontSize: 50, color: CLAUDE.INK, lineHeight: 1.3 }}>
            {perfect} of pictures come back with every single square correct.
          </div>
        </div>
      ) : null}
      <SparkLine text="Throw away almost everything. Keep what actually matters." delay={104} />
    </Page>
  );
};

// ── 4. KidDreaming — the machine plays in its head ─────────────────────────

export const kidDreamingSchema = z.object({});

export const KidDreaming: React.FC = () => {
  const frame = useCurrentFrame();
  const t = (frame * 0.09) % 13;
  const bx = 4 + t * 0.55;
  const px = Math.max(0, Math.min(13, Math.round(4 + t * 0.55) - 1));
  const bub = useRise(16);
  const z = (i: number) => {
    const p = ((frame * 0.013) + i * 0.33) % 1;
    return { o: Math.sin(p * Math.PI), y: -p * 80, s: 0.6 + p * 0.8 };
  };
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="now it can play without the game" />
      </div>
      <Robo x={360} y={620} scale={2.4} frame={frame} asleep />
      {[0, 1, 2].map((i) => {
        const { o, y, s } = z(i);
        return (
          <div key={i} style={{
            position: 'absolute', left: 470 + i * 24, top: 470 + y,
            fontFamily: S, fontSize: 38 * s, color: CLAUDE.GHOST, opacity: o * 0.85,
          }}>z</div>
        );
      })}
      {/* thought bubble */}
      <div style={{
        position: 'absolute', left: 740, top: 190, width: 760, height: 560,
        opacity: bub, borderRadius: 60,
        border: `4px dashed ${CLAUDE.BORDER}`, background: CLAUDE.CARD,
      }} />
      <div style={{ opacity: bub }}>
        <Board x={880} y={260} cell={26} bx={bx} by={t} px={px} />
      </div>
      <div style={{
        position: 'absolute', left: 740, right: 130, top: 790, opacity: bub,
      }}>
        <div style={{ fontFamily: S, fontSize: 48, color: CLAUDE.INK, lineHeight: 1.3 }}>
          The game it is playing does not exist.
        </div>
      </div>
      <SparkLine text="No ball, no paddle, no rules. Only its own prediction of what happens next." delay={40} />
    </Page>
  );
};

// ── 5. KidMemoryMatters — the headline result ──────────────────────────────

export const kidMemoryMattersSchema = z.object({
  rows: z.array(z.object({
    label: z.string(), pct: z.string(), val: z.number(), hero: z.boolean(), note: z.string(),
  })).default([]),
});
export type KidMemoryMattersProps = z.infer<typeof kidMemoryMattersSchema>;

export const KidMemoryMatters: React.FC<KidMemoryMattersProps> = ({ rows }) => {
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="same training. one difference." />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 230 }}>
        {rows.map((r, i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(10 + i * 20);
          return (
            <div key={i} style={{ marginBottom: 46, opacity: t }}>
              <div style={{ display: 'flex', alignItems: 'baseline', gap: 16, marginBottom: 12 }}>
                <span style={{
                  fontFamily: U, fontSize: 30,
                  color: r.hero ? CLAUDE.INK : CLAUDE.INK_SOFT,
                  fontWeight: r.hero ? 600 : 400,
                }}>{r.label}</span>
                <span style={{ fontFamily: U, fontSize: 23, color: CLAUDE.GHOST }}>{r.note}</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 24 }}>
                <div style={{ flex: 1, height: 56, background: CLAUDE.PILL, borderRadius: 10, overflow: 'hidden' }}>
                  <div style={{
                    width: `${r.val * 100 * t}%`, height: '100%',
                    background: r.hero ? CLAUDE.SPARK : CLAUDE.GHOST,
                  }} />
                </div>
                <span style={{
                  fontFamily: M, fontSize: 40, width: 150, textAlign: 'right',
                  color: r.hero ? CLAUDE.SEND : CLAUDE.INK,
                }}>{r.pct}</span>
              </div>
            </div>
          );
        })}
      </div>
      <SparkLine text="Remembering beat seeing. That is the whole finding." delay={96} />
    </Page>
  );
};

// ── 6. KidPlanAhead — imagining several futures ────────────────────────────

export const kidPlanAheadSchema = z.object({
  rows: z.array(z.object({ plans: z.string(), pct: z.string(), val: z.number() })).default([]),
});
export type KidPlanAheadProps = z.infer<typeof kidPlanAheadSchema>;

export const KidPlanAhead: React.FC<KidPlanAheadProps> = ({ rows }) => {
  const frame = useCurrentFrame();
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="or: think before you move" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 240 }}>
        {rows.map((r, i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(10 + i * 20);
          const n = Math.min(24, parseInt(r.plans, 10) || 8);
          return (
            <div key={i} style={{ marginBottom: 54, opacity: t }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 26 }}>
                <span style={{ fontFamily: U, fontSize: 27, color: CLAUDE.INK_SOFT, width: 290 }}>
                  imagine {r.plans} plans, pick the best
                </span>
                <div style={{ flex: 1, display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                  {Array.from({ length: n }, (_, k) => {
                    const pop = interpolate(frame, [12 + i * 20 + k, 22 + i * 20 + k], [0, 1],
                      { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
                    return (
                      <div key={k} style={{
                        width: 26, height: 26, borderRadius: 13,
                        background: CLAUDE.SPARK, opacity: 0.25 + 0.6 * pop,
                        transform: `scale(${0.4 + 0.6 * pop})`,
                      }} />
                    );
                  })}
                </div>
                <span style={{ fontFamily: M, fontSize: 36, width: 140, textAlign: 'right', color: CLAUDE.INK }}>
                  {r.pct}
                </span>
              </div>
            </div>
          );
        })}
      </div>
      <SparkLine text="More imagining, better play — and it costs only thinking time." delay={86} />
    </Page>
  );
};

// ── 7. KidLoop — play, learn, dream better ─────────────────────────────────

export const kidLoopSchema = z.object({
  oldData: z.string().default('28.1%'),
  newData: z.string().default('63.8%'),
  oldAcc: z.string().default('87.3%'),
  newAcc: z.string().default('92.0%'),
  finalPct: z.string().default('83.5%'),
});
export type KidLoopProps = z.infer<typeof kidLoopSchema>;

export const KidLoop: React.FC<KidLoopProps> = ({ oldData, newData, oldAcc, newAcc, finalPct }) => {
  const steps: [string, string, string][] = [
    ['1', 'play for real', `${oldData} → ${newData} catches`],
    ['2', 'better experience', 'the dream gets more to learn from'],
    ['3', 'improve the dream', `guesses right ${oldAcc} → ${newAcc}`],
    ['4', 'practise again', `now catches ${finalPct}`],
  ];
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="then go round again" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 230 }}>
        {steps.map(([n, title, sub], i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(8 + i * 16);
          return (
            <div key={n} style={{ marginBottom: 22, opacity: t, transform: `translateX(${(1 - t) * 20}px)` }}>
              <Card accent={i === 3} style={{
                padding: '24px 30px', display: 'flex', alignItems: 'center', gap: 28,
                background: i === 3 ? '#FBEEE8' : CLAUDE.CARD,
              }}>
                <div style={{
                  width: 56, height: 56, borderRadius: 28, flexShrink: 0,
                  background: i === 3 ? CLAUDE.SPARK : CLAUDE.PILL,
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontFamily: M, fontSize: 28, color: i === 3 ? CLAUDE.PAGE : CLAUDE.INK_SOFT,
                }}>{n}</div>
                <div style={{ flex: 1 }}>
                  <div style={{ fontFamily: U, fontSize: 32, fontWeight: 600, color: CLAUDE.INK }}>{title}</div>
                  <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 6 }}>{sub}</div>
                </div>
              </Card>
            </div>
          );
        })}
      </div>
      <SparkLine text="A better player makes better memories, which make a better dream." delay={80} />
    </Page>
  );
};

// ── 8. KidFinalBoard — everybody, ranked ───────────────────────────────────

export const kidFinalBoardSchema = z.object({
  rows: z.array(z.object({
    name: z.string(), pct: z.string(), val: z.number(), hero: z.boolean(),
  })).default([]),
});
export type KidFinalBoardProps = z.infer<typeof kidFinalBoardSchema>;

export const KidFinalBoard: React.FC<KidFinalBoardProps> = ({ rows }) => {
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="everyone who played, ranked" />
      </div>
      <div style={{ position: 'absolute', left: 120, right: 120, top: 190 }}>
        {rows.map((r, i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(8 + i * 11);
          return (
            <div key={i} style={{
              display: 'flex', alignItems: 'center', gap: 22, marginBottom: 18, opacity: t,
            }}>
              <span style={{
                width: 420, fontFamily: U, fontSize: 25,
                color: r.hero ? CLAUDE.INK : CLAUDE.INK_SOFT,
                fontWeight: r.hero ? 600 : 400,
              }}>{r.name}</span>
              <div style={{ flex: 1, height: 38, background: CLAUDE.PILL, borderRadius: 8, overflow: 'hidden' }}>
                <div style={{
                  width: `${r.val * 100 * t}%`, height: '100%',
                  background: r.hero ? CLAUDE.SPARK : CLAUDE.GHOST,
                }} />
              </div>
              <span style={{
                width: 130, textAlign: 'right', fontFamily: M, fontSize: 30,
                color: r.hero ? CLAUDE.SEND : CLAUDE.INK,
              }}>{r.pct}</span>
            </div>
          );
        })}
      </div>
      <SparkLine text="The dreamer beat the one that could see the real ball." delay={96} />
    </Page>
  );
};
