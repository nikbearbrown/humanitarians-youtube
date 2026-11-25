import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { useRise, Eyebrow, SparkLine, Page, Card } from './IndexedOrInvisible';
import { Grader } from './EvalCartoon';
import { Robo } from './KidEval';

/**
 * KidGPT — the kid-friendly cut of "a tiny GPT, built from nothing".
 *
 * Subject: a from-scratch GPT notebook (NumPy only) with a hand-written autodiff
 * engine, TWO numerical gradient checks, a copy-task sanity check before the real
 * run, and a KV-cache correctness check. This reel TEACHES; it is not a teardown.
 *
 * Every figure is parsed from the notebook's recorded outputs at build time.
 * Claude palette only: cream, warm ink, one terracotta.
 */

const S = CLAUDE_FONT.serif;
const U = CLAUDE_FONT.ui;
const M = CLAUDE_FONT.mono;

const Stage: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <svg viewBox="0 0 1920 1080" width={1920} height={1080}
    style={{ position: 'absolute', left: 0, top: 0, pointerEvents: 'none' }}>
    {children}
  </svg>
);

const bob = (f: number, a = 5, s = 0.055) => Math.sin(f * s) * a;

// ── 1. KidGuessGame — the whole job, in one picture ────────────────────────

export const kidGuessGameSchema = z.object({});

export const KidGuessGame: React.FC = () => {
  const frame = useCurrentFrame();
  const TEXT = '    def area(self';
  const shown = Math.min(TEXT.length, Math.floor(interpolate(frame, [8, 70], [0, TEXT.length],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' })));
  const guess = useRise(78);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the entire job, start to finish" />
      </div>
      <div style={{ position: 'absolute', left: 130, top: 300, right: 130 }}>
        <Card style={{ padding: '34px 38px' }}>
          <span style={{ fontFamily: M, fontSize: 56, color: CLAUDE.INK, whiteSpace: 'pre' }}>
            {TEXT.slice(0, shown)}
          </span>
          <span style={{
            fontFamily: M, fontSize: 56, color: CLAUDE.SPARK,
            opacity: Math.sin(frame * 0.3) > 0 ? 1 : 0.2,
          }}>▌</span>
        </Card>
        {guess > 0.02 ? (
          <div style={{ marginTop: 40, opacity: guess, display: 'flex', alignItems: 'center', gap: 30 }}>
            <span style={{ fontFamily: S, fontSize: 46, color: CLAUDE.INK }}>what comes next?</span>
            <div style={{
              background: '#FBEEE8', border: `3px solid ${CLAUDE.SPARK}`, borderRadius: 14,
              padding: '10px 32px', fontFamily: M, fontSize: 56, color: CLAUDE.SEND,
              transform: `scale(${0.8 + 0.2 * guess})`,
            }}>,</div>
          </div>
        ) : null}
      </div>
      <Robo x={1560} y={760 + bob(frame)} scale={2.0} frame={frame} happy={guess > 0.5} />
      <SparkLine text="Guess the next character. That is the whole job. Nothing else." delay={86} />
    </Page>
  );
};

// ── 2. KidAlphabetShrink — 96 choices down to about 5 ──────────────────────

export const kidAlphabetShrinkSchema = z.object({
  stages: z.array(z.object({ label: z.string(), choices: z.number(), hero: z.boolean() })).default([]),
});
export type KidAlphabetShrinkProps = z.infer<typeof kidAlphabetShrinkSchema>;

export const KidAlphabetShrink: React.FC<KidAlphabetShrinkProps> = ({ stages }) => {
  const frame = useCurrentFrame();
  const idx = Math.min(stages.length - 1,
    Math.floor(interpolate(frame, [20, 140], [0, stages.length],
      { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' })));
  const cur = stages[Math.max(0, idx)] || { label: '', choices: 96, hero: false };
  const MAXN = stages.length ? stages[0].choices : 96;
  const lit = Math.round(cur.choices);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="how many letters is it still choosing between?" />
      </div>
      <div style={{
        position: 'absolute', left: 130, top: 200, width: 1080,
        display: 'grid', gridTemplateColumns: 'repeat(12, 1fr)', gap: 10,
      }}>
        {Array.from({ length: MAXN }, (_, i) => {
          const on = i < lit;
          return (
            <div key={i} style={{
              aspectRatio: '1 / 1', borderRadius: 8,
              background: on ? CLAUDE.SPARK : CLAUDE.PILL,
              opacity: on ? 0.9 : 1,
            }} />
          );
        })}
      </div>
      <div style={{ position: 'absolute', right: 130, top: 300, width: 530 }}>
        <div style={{ fontFamily: U, fontSize: 30, color: CLAUDE.INK_SOFT }}>{cur.label}</div>
        <div style={{ fontFamily: M, fontSize: 130, color: cur.hero ? CLAUDE.SEND : CLAUDE.INK, lineHeight: 1.05 }}>
          {lit}
        </div>
        <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT }}>
          letters still in the running
        </div>
      </div>
      <SparkLine text="From the whole alphabet down to a small handful." delay={150} />
    </Page>
  );
};

// ── 3. KidShortcuts — BPE glues common pieces together ─────────────────────

export const kidShortcutsSchema = z.object({
  merges: z.array(z.string()).default([]),
  charsPerToken: z.string().default('2.38'),
});
export type KidShortcutsProps = z.infer<typeof kidShortcutsSchema>;

export const KidShortcuts: React.FC<KidShortcutsProps> = ({ merges, charsPerToken }) => {
  const frame = useCurrentFrame();
  const tail = useRise(96);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="it invents its own shortcuts" />
      </div>
      <div style={{
        position: 'absolute', left: 130, right: 130, top: 220,
        display: 'flex', flexWrap: 'wrap', gap: 16,
      }}>
        {merges.map((m, i) => {
          const t = interpolate(frame, [8 + i * 7, 22 + i * 7], [0, 1],
            { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
          const isSpace = m.trim() === '' && !m.includes('\\n');
          return (
            <div key={i} style={{
              opacity: t, transform: `scale(${0.6 + 0.4 * t})`,
              background: isSpace ? CLAUDE.PILL : '#FBEEE8',
              border: `2px solid ${isSpace ? CLAUDE.BORDER : CLAUDE.SPARK}`,
              borderRadius: 12, padding: '14px 22px',
              fontFamily: M, fontSize: 34,
              color: isSpace ? CLAUDE.GHOST : CLAUDE.SEND, whiteSpace: 'pre',
            }}>{isSpace
              ? `·${'·'.repeat(Math.min(7, m.length - 1))}`
              : m.replace(/\\n/g, '↵').replace(/ /g, '·')}</div>
          );
        })}
      </div>
      {tail > 0.02 ? (
        <div style={{ position: 'absolute', left: 130, right: 130, top: 660, opacity: tail }}>
          <div style={{ fontFamily: S, fontSize: 46, color: CLAUDE.INK, lineHeight: 1.3 }}>
            The commonest thing in Python code is empty space.
          </div>
          <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT, marginTop: 14 }}>
            After that it glues together bits of real words — and then whole ones.
            Each shortcut now covers {charsPerToken} letters on average.
          </div>
        </div>
      ) : null}
      <SparkLine text="Nobody told it about Python. It found the patterns by counting." delay={104} />
    </Page>
  );
};

// ── 4. KidLookBack — attention as a spotlight ──────────────────────────────

export const kidLookBackSchema = z.object({});

export const KidLookBack: React.FC = () => {
  const frame = useCurrentFrame();
  const CH = ['s', 'e', 'l', 'f', '.', 'a', 'r', 'e', 'a'];
  const focus = Math.min(CH.length - 1, Math.floor(interpolate(frame, [20, 130], [4, CH.length],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' })));
  const X0 = 300, GAP = 136, Y = 420;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="every letter looks back at the ones before it" />
      </div>
      <Stage>
        {CH.map((_, i) => {
          if (i >= focus) return null;
          const w = 1 - (focus - i) / (focus + 1);
          const xf = X0 + focus * GAP + 34;
          const xi = X0 + i * GAP + 34;
          // arc height grows with distance so overlapping links stay readable
          const lift = 46 + (focus - i) * 26;
          return (
            <path key={i}
              d={`M ${xf} ${Y - 16} Q ${(xf + xi) / 2} ${Y - 16 - lift} ${xi} ${Y - 16}`}
              fill="none"
              stroke={CLAUDE.SPARK} strokeWidth={2 + w * 8}
              opacity={0.2 + w * 0.62} strokeLinecap="round" />
          );
        })}
      </Stage>
      <div style={{ position: 'absolute', left: X0, top: Y, display: 'flex', gap: GAP - 68 }}>
        {CH.map((c, i) => {
          const isFocus = i === focus;
          const past = i < focus;
          return (
            <div key={i} style={{
              width: 68, height: 68, borderRadius: 12,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              background: isFocus ? CLAUDE.SPARK : past ? '#FBEEE8' : CLAUDE.PILL,
              border: `2px solid ${isFocus ? CLAUDE.SEND : past ? CLAUDE.SPARK : CLAUDE.BORDER}`,
              fontFamily: M, fontSize: 36,
              color: isFocus ? CLAUDE.PAGE : past ? CLAUDE.SEND : CLAUDE.GHOST,
              transform: isFocus ? 'scale(1.16)' : 'none',
            }}>{c === ' ' ? '·' : c}</div>
          );
        })}
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 640 }}>
        <div style={{ fontFamily: S, fontSize: 48, color: CLAUDE.INK, lineHeight: 1.3 }}>
          Thicker line, more attention paid.
        </div>
        <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT, marginTop: 14 }}>
          It can only look backwards. Peeking ahead would be cheating — the answer is there.
        </div>
      </div>
      <SparkLine text="That looking-back is the trick the whole thing is built on." delay={140} />
    </Page>
  );
};

// ── 5. KidTwoChecks — both gradient checks ─────────────────────────────────

export const kidTwoChecksSchema = z.object({
  engineErr: z.string().default('4.81e-07'),
  modelErr: z.string().default('7.98e-06'),
});
export type KidTwoChecksProps = z.infer<typeof kidTwoChecksSchema>;

export const KidTwoChecks: React.FC<KidTwoChecksProps> = ({ engineErr, modelErr }) => {
  const frame = useCurrentFrame();
  const a = useRise(8);
  const b = useRise(34);
  const badge = (t: number, title: string, sub: string, err: string) => (
    <div style={{ flex: 1, opacity: t, transform: `translateY(${(1 - t) * 20}px)` }}>
      <Card accent style={{ padding: '32px 34px', background: '#FBEEE8', height: '100%' }}>
        <div style={{ fontFamily: U, fontSize: 22, letterSpacing: 2.2, color: CLAUDE.SEND }}>{title}</div>
        <div style={{ fontFamily: S, fontSize: 42, color: CLAUDE.INK, marginTop: 14, lineHeight: 1.25 }}>{sub}</div>
        <div style={{ marginTop: 22, display: 'flex', alignItems: 'baseline', gap: 14 }}>
          <span style={{ fontFamily: M, fontSize: 34, color: CLAUDE.SEND }}>{err}</span>
          <span style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT }}>difference</span>
        </div>
      </Card>
    </div>
  );
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="they checked their working — twice" />
      </div>
      <Stage><Grader x={960} y={300} scale={1.7} mood="pleased" /></Stage>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 430, display: 'flex', gap: 40 }}>
        {badge(a, 'CHECK ONE', 'The maths engine itself.', engineErr)}
        {badge(b, 'CHECK TWO', 'Then the whole machine.', modelErr)}
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 760 }}>
        <div style={{ fontFamily: U, fontSize: 30, color: CLAUDE.INK_SOFT }}>
          Both worked out by hand, then counted a second way. Both agreed.
        </div>
      </div>
      <SparkLine text="Check the small thing first. Then check the big thing." delay={56} />
    </Page>
  );
};

// ── 6. KidCopyTest — the easy exam before the hard one ─────────────────────

export const kidCopyTestSchema = z.object({
  accuracy: z.string().default('100.0%'),
  seconds: z.string().default('5.5s'),
});
export type KidCopyTestProps = z.infer<typeof kidCopyTestSchema>;

export const KidCopyTest: React.FC<KidCopyTestProps> = ({ accuracy, seconds }) => {
  const frame = useCurrentFrame();
  const SRC = ['k', 'q', 'm', 'a', 'z', 'r', 'b', 'w'];
  const copied = Math.min(SRC.length, Math.floor(interpolate(frame, [24, 110], [0, SRC.length],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' })));
  const done = useRise(118);
  const cell = (c: string, on: boolean, hero: boolean) => (
    <div style={{
      width: 74, height: 74, borderRadius: 12,
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      background: on ? (hero ? CLAUDE.SPARK : '#FBEEE8') : CLAUDE.PILL,
      border: `2px solid ${on ? CLAUDE.SPARK : CLAUDE.BORDER}`,
      fontFamily: M, fontSize: 34, color: on ? (hero ? CLAUDE.PAGE : CLAUDE.SEND) : CLAUDE.GHOST,
    }}>{on ? c : '?'}</div>
  );
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="an easy exam first" />
      </div>
      <div style={{ position: 'absolute', left: 200, top: 300 }}>
        <div style={{ fontFamily: U, fontSize: 26, color: CLAUDE.INK_SOFT, marginBottom: 16 }}>
          here is a jumble — now say it back
        </div>
        <div style={{ display: 'flex', gap: 14 }}>{SRC.map((c, i) => <div key={i}>{cell(c, true, false)}</div>)}</div>
        <div style={{ height: 40 }} />
        <div style={{ display: 'flex', gap: 14 }}>
          {SRC.map((c, i) => <div key={i}>{cell(c, i < copied, true)}</div>)}
        </div>
      </div>
      <Robo x={1520} y={430 + bob(frame, 7)} scale={2.1} frame={frame} happy={done > 0.4} />
      {done > 0.02 ? (
        <div style={{ position: 'absolute', left: 200, right: 130, top: 640, opacity: done }}>
          <div style={{ fontFamily: S, fontSize: 50, color: CLAUDE.INK, lineHeight: 1.3 }}>
            {accuracy} right, in {seconds}.
          </div>
          <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT, marginTop: 14 }}>
            If it had failed this, nothing after it would have been worth trying.
          </div>
        </div>
      ) : null}
      <SparkLine text="Prove the machine works on something easy before you trust it on something hard." delay={126} />
    </Page>
  );
};

// ── 7. KidFinishWord — the probes ──────────────────────────────────────────

export const kidFinishWordSchema = z.object({
  probes: z.array(z.object({ prompt: z.string(), next: z.string(), pct: z.string() })).default([]),
});
export type KidFinishWordProps = z.infer<typeof kidFinishWordSchema>;

export const KidFinishWord: React.FC<KidFinishWordProps> = ({ probes }) => {
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="what did it actually learn?" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 210 }}>
        {probes.map((p, i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(8 + i * 20);
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const r = useRise(18 + i * 20);
          return (
            <div key={i} style={{ marginBottom: 34, opacity: t }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 20 }}>
                <Card style={{ padding: '20px 26px' }}>
                  <span style={{ fontFamily: M, fontSize: 36, color: CLAUDE.INK, whiteSpace: 'pre' }}>
                    {p.prompt}
                  </span>
                </Card>
                <span style={{ fontFamily: U, fontSize: 30, color: CLAUDE.GHOST }}>→</span>
                <div style={{
                  opacity: r, transform: `scale(${0.7 + 0.3 * r})`,
                  background: CLAUDE.SPARK, borderRadius: 12, padding: '18px 30px',
                  fontFamily: M, fontSize: 40, color: CLAUDE.PAGE, fontWeight: 700,
                }}>{p.next}</div>
                <span style={{ fontFamily: M, fontSize: 34, color: CLAUDE.SEND, opacity: r }}>{p.pct}</span>
              </div>
            </div>
          );
        })}
      </div>
      <SparkLine text="Nobody taught it the word “self”. It worked that out from the code." delay={80} />
    </Page>
  );
};

// ── 8. KidTempDial — adventurousness ───────────────────────────────────────

export const kidTempDialSchema = z.object({
  rows: z.array(z.object({ temp: z.string(), sample: z.string(), note: z.string() })).default([]),
});
export type KidTempDialProps = z.infer<typeof kidTempDialSchema>;

export const KidTempDial: React.FC<KidTempDialProps> = ({ rows }) => {
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="how adventurous should it be?" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 190 }}>
        {rows.map((r, i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(8 + i * 16);
          return (
            <div key={i} style={{
              marginBottom: 24, opacity: t, display: 'flex', alignItems: 'center', gap: 26,
            }}>
              <div style={{
                width: 132, flexShrink: 0, textAlign: 'center',
                background: '#FBEEE8', border: `2px solid ${CLAUDE.SPARK}`, borderRadius: 12,
                padding: '12px 0', fontFamily: M, fontSize: 30, color: CLAUDE.SEND,
              }}>{r.temp}</div>
              <Card style={{ flex: 1, padding: '18px 24px', overflow: 'hidden' }}>
                <span style={{
                  fontFamily: M, fontSize: 24, color: CLAUDE.INK_SOFT,
                  whiteSpace: 'nowrap', display: 'block', overflow: 'hidden', textOverflow: 'ellipsis',
                }}>{r.sample}</span>
              </Card>
              <span style={{
                width: 230, fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT,
              }}>{r.note}</span>
            </div>
          );
        })}
      </div>
      <SparkLine text="Too careful and it repeats itself. Too wild and it is nonsense." delay={80} />
    </Page>
  );
};

// ── 9. KidMemoryTrick — the KV cache ───────────────────────────────────────

export const kidMemoryTrickSchema = z.object({
  without: z.string().default('2,016'),
  with_: z.string().default('63'),
  speedup: z.string().default('32x'),
  msWithout: z.string().default('47 ms'),
  msWith: z.string().default('22 ms'),
});
export type KidMemoryTrickProps = z.infer<typeof kidMemoryTrickSchema>;

export const KidMemoryTrick: React.FC<KidMemoryTrickProps> = ({
  without, with_, speedup, msWithout, msWith,
}) => {
  const frame = useCurrentFrame();
  const a = useRise(6);
  const b = useRise(30);
  const punch = useRise(58);
  const side = (t: number, title: string, pages: number, cnt: string, ms: string, hero: boolean) => (
    <div style={{ flex: 1, opacity: t }}>
      <div style={{ fontFamily: U, fontSize: 25, letterSpacing: 2, color: hero ? CLAUDE.SEND : CLAUDE.INK_SOFT, marginBottom: 18 }}>
        {title}
      </div>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 7, minHeight: 190, alignContent: 'flex-start' }}>
        {Array.from({ length: pages }, (_, i) => (
          <div key={i} style={{
            width: 22, height: 28, borderRadius: 3,
            background: hero ? CLAUDE.SPARK : CLAUDE.PILL,
            border: `1px solid ${hero ? CLAUDE.SEND : CLAUDE.BORDER}`,
            opacity: hero ? 0.9 : 0.75,
          }} />
        ))}
      </div>
      <div style={{ fontFamily: M, fontSize: 52, color: CLAUDE.INK, marginTop: 20 }}>{cnt}</div>
      <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT }}>pages re-read · {ms}</div>
    </div>
  );
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="one more trick — stop re-reading" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 200, display: 'flex', gap: 70 }}>
        {side(a, 'READING IT ALL AGAIN, EVERY TIME', 48, without, msWithout, false)}
        {side(b, 'REMEMBERING WHAT IT READ', 6, with_, msWith, true)}
      </div>
      {punch > 0.02 ? (
        <div style={{ position: 'absolute', left: 130, right: 130, top: 700, opacity: punch }}>
          <div style={{ fontFamily: S, fontSize: 54, color: CLAUDE.INK, lineHeight: 1.25 }}>
            {speedup} less work — and exactly the same answer.
          </div>
        </div>
      ) : null}
      <SparkLine text="They checked both ways agree before trusting the fast one." delay={66} />
    </Page>
  );
};
