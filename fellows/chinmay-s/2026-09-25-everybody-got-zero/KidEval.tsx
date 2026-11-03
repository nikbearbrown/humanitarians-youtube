import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { useRise, Eyebrow, SparkLine, Page, Card } from './IndexedOrInvisible';
import { Grader } from './EvalCartoon';

/**
 * KidEval — the kid-friendly cut of "the test where everybody got zero".
 *
 * Same subject as EvalHarness/EvalCartoon (a prompt-engineering notebook whose
 * scorer reports 0.0 for everything), retold with two characters and concrete
 * props so a child can follow it. Still Claude-palette only: cream, warm ink,
 * one terracotta. Cartoon BEHAVIOUR, not cartoon colour.
 *
 * Cast: the Grader (reused from EvalCartoon) and Robo, the student.
 */

const S = CLAUDE_FONT.serif;
const U = CLAUDE_FONT.ui;
const M = CLAUDE_FONT.mono;


/** Grader returns an SVG <g>, so it needs an <svg> stage to live in. */
const Stage: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <svg viewBox="0 0 1920 1080" width={1920} height={1080}
    style={{ position: 'absolute', left: 0, top: 0, pointerEvents: 'none' }}>
    {children}
  </svg>
);

const bob = (frame: number, amp = 5, sp = 0.055) => Math.sin(frame * sp) * amp;

/** Robo — a boxy robot student. Antenna wobbles; eyes can sleep. */
export const Robo: React.FC<{
  x: number; y: number; scale?: number; asleep?: boolean; happy?: boolean;
  squash?: number; frame: number;
}> = ({ x, y, scale = 1, asleep, happy, squash = 1, frame }) => {
  const w = 150, h = 140;
  const ant = Math.sin(frame * 0.09) * 9;
  return (
    <div style={{
      position: 'absolute', left: x - (w * scale) / 2, top: y - (h * scale) / 2,
      width: w * scale, height: h * scale,
      transform: `scaleY(${squash}) scaleX(${2 - squash})`, transformOrigin: 'center bottom',
    }}>
      <svg viewBox="0 0 150 140" width={w * scale} height={h * scale}>
        {/* antenna */}
        <line x1={75} y1={26} x2={75 + ant} y2={4} stroke={CLAUDE.INK} strokeWidth={4} strokeLinecap="round" />
        <circle cx={75 + ant} cy={4} r={7} fill={CLAUDE.SPARK} />
        {/* head */}
        <rect x={24} y={24} width={102} height={76} rx={16} fill={CLAUDE.INK} />
        {/* eyes */}
        {asleep ? (
          <>
            <path d="M44 60 q10 8 20 0" stroke={CLAUDE.PAGE} strokeWidth={4} fill="none" strokeLinecap="round" />
            <path d="M86 60 q10 8 20 0" stroke={CLAUDE.PAGE} strokeWidth={4} fill="none" strokeLinecap="round" />
          </>
        ) : (
          <>
            <circle cx={54} cy={58} r={9} fill={CLAUDE.PAGE} />
            <circle cx={96} cy={58} r={9} fill={CLAUDE.PAGE} />
            <circle cx={54} cy={58} r={4} fill={CLAUDE.INK} />
            <circle cx={96} cy={58} r={4} fill={CLAUDE.INK} />
          </>
        )}
        {/* mouth */}
        {happy
          ? <path d="M58 80 q17 14 34 0" stroke={CLAUDE.PAGE} strokeWidth={4} fill="none" strokeLinecap="round" />
          : <rect x={58} y={80} width={34} height={5} rx={2.5} fill={CLAUDE.PAGE} />}
        {/* body */}
        <rect x={40} y={104} width={70} height={34} rx={10} fill={CLAUDE.INK_SOFT} />
      </svg>
    </div>
  );
};

/** A paper card that can be stamped. */
const Paper: React.FC<{
  x: number; y: number; w?: number; rot?: number; lines: string[]; stamp?: string;
  stampIn?: number; dim?: boolean;
}> = ({ x, y, w = 430, rot = 0, lines, stamp, stampIn = 0, dim }) => (
  <div style={{
    position: 'absolute', left: x, top: y, width: w,
    transform: `rotate(${rot}deg)`, opacity: dim ? 0.45 : 1,
  }}>
    <Card style={{ padding: '26px 28px', minHeight: 120 }}>
      {lines.map((l, i) => (
        <div key={i} style={{
          fontFamily: i === 0 ? U : M, fontSize: i === 0 ? 20 : 27,
          color: i === 0 ? CLAUDE.INK_SOFT : CLAUDE.INK,
          letterSpacing: i === 0 ? 2 : 0, marginTop: i ? 10 : 0,
        }}>{l}</div>
      ))}
    </Card>
    {stamp && stampIn > 0.01 ? (
      <div style={{
        position: 'absolute', right: -64, top: 30,
        transform: `rotate(-13deg) scale(${1 + (1 - stampIn) * 1.6})`,
        opacity: Math.min(1, stampIn * 1.6),
        border: `4px solid ${CLAUDE.SPARK}`, borderRadius: 10,
        padding: '6px 18px', background: 'rgba(255,255,255,0.86)',
        fontFamily: M, fontSize: 40, color: CLAUDE.SPARK, fontWeight: 700,
      }}>{stamp}</div>
    ) : null}
  </div>
);

// ── 1. KidRobotTest — Robo answers questions ───────────────────────────────

export const kidRobotTestSchema = z.object({});

export const KidRobotTest: React.FC = () => {
  const frame = useCurrentFrame();
  const a = useRise(4);
  const QS = ['What is the capital of France?', 'What is 3 + 4?'];
  const AS = ['Paris', '7'];
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="meet the robot taking the test" />
      </div>
      <Robo x={330} y={470 + bob(frame)} scale={2.1} frame={frame} happy />
      <div style={{ position: 'absolute', left: 620, top: 250, right: 130 }}>
        {QS.map((q, i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(10 + i * 26);
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const r = useRise(22 + i * 26);
          return (
            <div key={q} style={{ marginBottom: 46, opacity: t }}>
              <div style={{ fontFamily: U, fontSize: 30, color: CLAUDE.INK_SOFT }}>{q}</div>
              <div style={{
                display: 'inline-block', marginTop: 12, opacity: r,
                transform: `scale(${0.7 + 0.3 * r})`,
                background: '#FBEEE8', border: `2px solid ${CLAUDE.SPARK}`,
                borderRadius: 14, padding: '10px 26px',
                fontFamily: M, fontSize: 38, color: CLAUDE.SEND,
              }}>{AS[i]}</div>
            </div>
          );
        })}
      </div>
      <SparkLine text="The robot answers. Someone has to mark the answers right or wrong." delay={62} />
    </Page>
  );
};

// ── 2. KidStampRule — the exact-word rule ──────────────────────────────────

export const kidStampRuleSchema = z.object({});

export const KidStampRule: React.FC = () => {
  const frame = useCurrentFrame();
  const swing = interpolate(frame, [34, 44, 52], [0, -52, 8], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const hit = frame >= 50;
  const stampIn = interpolate(frame, [50, 62], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const squash = hit ? 1 - 0.1 * Math.max(0, 1 - (frame - 50) / 12) : 1;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the marking rule" />
      </div>
      <Paper x={300} y={220} lines={['ANSWER', 'Paris']} stamp="✓" stampIn={useRise(10)} />
      <Paper x={300} y={470} w={660} rot={-1.5}
        lines={['ANSWER', 'The capital of France is Paris.']} stamp="✗" stampIn={stampIn} />
      <Stage><Grader x={1430} y={430} scale={2.3} mood="stern" armAngle={swing} squash={squash} /></Stage>
      <div style={{
        position: 'absolute', left: 300, top: 680, right: 500,
        fontFamily: S, fontSize: 48, color: CLAUDE.INK, lineHeight: 1.3,
        opacity: stampIn,
      }}>
        Same city. One tick, one cross.
      </div>
      <SparkLine text="The rule is: say the exact word, and nothing else." delay={68} />
    </Page>
  );
};

// ── 3. KidGumDot — the full stop that sticks ───────────────────────────────

export const kidGumDotSchema = z.object({});

export const KidGumDot: React.FC = () => {
  const frame = useCurrentFrame();
  const a = useRise(5);
  const wob = Math.sin(frame * 0.16) * 7;
  const show = useRise(38);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="why the tick and the cross" />
      </div>
      <div style={{ position: 'absolute', left: 150, top: 260, opacity: a }}>
        <div style={{ fontFamily: U, fontSize: 26, color: CLAUDE.INK_SOFT, marginBottom: 18 }}>
          the marker compares word by word
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 26 }}>
          <div style={{
            background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 12,
            padding: '16px 30px', fontFamily: M, fontSize: 52, color: CLAUDE.INK,
          }}>paris</div>
          <span style={{ fontFamily: U, fontSize: 40, color: CLAUDE.GHOST }}>vs</span>
          <div style={{
            position: 'relative',
            background: '#FBEEE8', border: `2px solid ${CLAUDE.SPARK}`, borderRadius: 12,
            padding: '16px 30px', fontFamily: M, fontSize: 52, color: CLAUDE.SEND,
          }}>
            paris
            <span style={{
              display: 'inline-block',
              transform: `translateY(${wob}px) scale(1.5)`,
              color: CLAUDE.SEND, fontWeight: 700,
            }}>.</span>
          </div>
        </div>
      </div>
      <div style={{ position: 'absolute', left: 150, right: 150, top: 520, opacity: show }}>
        <Card style={{ padding: '30px 34px', background: '#FBEEE8', border: `2px solid ${CLAUDE.SPARK}` }}>
          <div style={{ fontFamily: S, fontSize: 52, color: CLAUDE.INK, lineHeight: 1.3 }}>
            The full stop sticks to the word like chewing gum.
          </div>
          <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT, marginTop: 14 }}>
            So <span style={{ fontFamily: M }}>paris.</span> and <span style={{ fontFamily: M }}>paris</span> are
            different words to the marker — and the score is zero.
          </div>
        </Card>
      </div>
      <SparkLine text="One tiny dot. A completely correct answer, marked wrong." delay={54} />
    </Page>
  );
};

// ── 4. KidLetterMonster — the machine that eats letters ────────────────────

export const kidLetterMonsterSchema = z.object({});

export const KidLetterMonster: React.FC = () => {
  const frame = useCurrentFrame();
  const a = useRise(4);
  const eat = interpolate(frame, [28, 48], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const out = useRise(56);
  const chomp = 1 + Math.sin(frame * 0.35) * 0.06;
  const WORD = 'Brasília';
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the cleaning machine" />
      </div>

      {/* input word */}
      <div style={{ position: 'absolute', left: 130, top: 330, opacity: a }}>
        <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT, marginBottom: 12 }}>goes in</div>
        <div style={{ display: 'flex', gap: 4 }}>
          {WORD.split('').map((ch, i) => {
            const isAccent = ch === 'í';
            const gone = isAccent && eat > 0.55;
            return (
              <span key={i} style={{
                fontFamily: M, fontSize: 56,
                color: isAccent ? CLAUDE.SPARK : CLAUDE.INK,
                opacity: gone ? 0 : 1,
                transform: isAccent ? `translateY(${-eat * 26}px) scale(${1 - eat * 0.4})` : 'none',
              }}>{ch}</span>
            );
          })}
        </div>
      </div>

      {/* the machine */}
      <div style={{
        position: 'absolute', left: 760, top: 290,
        transform: `scale(${chomp})`, transformOrigin: 'center',
      }}>
        <svg width={260} height={230} viewBox="0 0 260 230">
          <rect x={20} y={40} width={220} height={150} rx={22} fill={CLAUDE.INK} />
          <rect x={52} y={72} width={156} height={54} rx={10} fill={CLAUDE.PAGE} />
          {/* teeth */}
          {Array.from({ length: 7 }, (_, i) => (
            <polygon key={i}
              points={`${60 + i * 22},72 ${71 + i * 22},96 ${82 + i * 22},72`}
              fill={CLAUDE.SPARK} />
          ))}
          <circle cx={78} cy={158} r={12} fill={CLAUDE.SPARK} />
          <rect x={104} y={150} width={90} height={16} rx={8} fill={CLAUDE.INK_SOFT} />
        </svg>
        <div style={{
          fontFamily: U, fontSize: 21, color: CLAUDE.INK_SOFT,
          textAlign: 'center', marginTop: 6,
        }}>keeps only a–z</div>
      </div>

      {/* output */}
      <div style={{ position: 'absolute', right: 130, top: 330, opacity: out, textAlign: 'right' }}>
        <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT, marginBottom: 12 }}>comes out</div>
        <div style={{ fontFamily: M, fontSize: 56, color: CLAUDE.SEND }}>bras lia</div>
      </div>

      <div style={{
        position: 'absolute', left: 130, right: 130, top: 640, opacity: out,
      }}>
        <div style={{ fontFamily: S, fontSize: 50, color: CLAUDE.INK, lineHeight: 1.3 }}>
          It ate the í — and split the city in half.
        </div>
      </div>
      <SparkLine text="Now no spelling of Brasília can ever match. Not even the right one." delay={66} />
    </Page>
  );
};

// ── 5. KidSleepyRobot — nobody plugged the robot in ────────────────────────

export const kidSleepyRobotSchema = z.object({});

export const KidSleepyRobot: React.FC = () => {
  const frame = useCurrentFrame();
  const a = useRise(4);
  const reveal = useRise(46);
  const z = (i: number) => {
    const p = ((frame * 0.014) + i * 0.33) % 1;
    return { o: Math.sin(p * Math.PI), y: -p * 90, s: 0.6 + p * 0.9 };
  };
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="but here is the thing" />
      </div>
      <Robo x={420} y={430} scale={2.6} frame={frame} asleep />
      {[0, 1, 2].map((i) => {
        const { o, y, s } = z(i);
        return (
          <div key={i} style={{
            position: 'absolute', left: 530 + i * 26, top: 300 + y,
            fontFamily: S, fontSize: 40 * s, color: CLAUDE.GHOST, opacity: o * 0.9,
          }}>z</div>
        );
      })}
      <div style={{ position: 'absolute', left: 820, top: 300, right: 130, opacity: a }}>
        <Card style={{ padding: '30px 34px' }}>
          <div style={{ fontFamily: U, fontSize: 26, color: CLAUDE.INK_SOFT }}>
            every single answer the robot gave
          </div>
          <div style={{ fontFamily: M, fontSize: 52, color: CLAUDE.SEND, marginTop: 16 }}>
            MOCK_OUTPUT
          </div>
        </Card>
        {reveal > 0.02 ? (
          <div style={{ marginTop: 34, opacity: reveal }}>
            <div style={{ fontFamily: S, fontSize: 50, color: CLAUDE.INK, lineHeight: 1.3 }}>
              The robot was never switched on.
            </div>
            <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT, marginTop: 14 }}>
              It said the same two words ten times, and the test carried on regardless.
            </div>
          </div>
        ) : null}
      </div>
      <SparkLine text="Nothing in the test noticed. Nothing in the test could." delay={74} />
    </Page>
  );
};

// ── 6. KidZeroParade — everybody gets zero ─────────────────────────────────

export const kidZeroParadeSchema = z.object({});

export const KidZeroParade: React.FC = () => {
  const frame = useCurrentFrame();
  const chart = useRise(58);
  const N = 10;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="ten questions, ten results" />
      </div>
      <div style={{
        position: 'absolute', left: 130, right: 130, top: 190,
        display: 'flex', flexWrap: 'wrap', gap: 18,
      }}>
        {Array.from({ length: N }, (_, i) => {
          const t = interpolate(frame, [6 + i * 4, 18 + i * 4], [0, 1],
            { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
          return (
            <div key={i} style={{
              width: 300, opacity: t, transform: `translateY(${(1 - t) * 20}px) rotate(${(i % 3 - 1) * 1.2}deg)`,
            }}>
              <Card style={{ padding: '18px 20px', display: 'flex', alignItems: 'center', gap: 16 }}>
                <span style={{ fontFamily: M, fontSize: 19, color: CLAUDE.GHOST }}>Q{i + 1}</span>
                <span style={{ flex: 1, fontFamily: M, fontSize: 19, color: CLAUDE.INK_SOFT }}>MOCK_OUTPUT</span>
                <span style={{ fontFamily: M, fontSize: 30, color: CLAUDE.SPARK, fontWeight: 700 }}>0</span>
              </Card>
            </div>
          );
        })}
      </div>
      {chart > 0.02 ? (
        <div style={{
          position: 'absolute', left: 130, right: 130, top: 640, opacity: chart,
          display: 'flex', alignItems: 'flex-end', gap: 60, height: 150,
        }}>
          {['A-baseline', 'A-cot', 'B-baseline', 'B-cot'].map((l) => (
            <div key={l} style={{ flex: 1, textAlign: 'center' }}>
              <div style={{ height: 4, background: CLAUDE.SPARK, borderRadius: 2 }} />
              <div style={{ fontFamily: M, fontSize: 19, color: CLAUDE.INK_SOFT, marginTop: 10 }}>{l}</div>
            </div>
          ))}
          <div style={{
            position: 'absolute', right: 0, top: -40,
            fontFamily: S, fontSize: 40, color: CLAUDE.INK,
          }}>…and the chart drew itself anyway.</div>
        </div>
      ) : null}
      <SparkLine text="A picture of nothing still looks like a picture of something." delay={80} />
    </Page>
  );
};

// ── 7. KidTestTheTeacher — check the marker first ──────────────────────────

export const kidTestTheTeacherSchema = z.object({});

export const KidTestTheTeacher: React.FC = () => {
  const frame = useCurrentFrame();
  const a = useRise(6);
  const fail = useRise(40);
  const shake = fail > 0.1 ? Math.sin(frame * 1.3) * 4 * Math.max(0, 1 - (frame - 40) / 30) : 0;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the fix — mark the marker" />
      </div>
      <Stage><Grader x={330} y={440} scale={2.4} mood={fail > 0.5 ? 'shifty' : 'neutral'} lean={shake * 0.4} /></Stage>
      <div style={{ position: 'absolute', left: 640, top: 240, right: 130, opacity: a }}>
        <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT, marginBottom: 20 }}>
          Give the marker an answer you already know is right.
        </div>
        {[['Paris', 'Paris', true], ['Paris.', 'Paris', false], ['Brasilia', 'Brasília', false]].map(
          ([p, g, ok], i) => {
            // eslint-disable-next-line react-hooks/rules-of-hooks
            const t = useRise(14 + i * 12);
            const shown = fail > 0.4;
            return (
              <div key={i} style={{
                display: 'flex', alignItems: 'center', gap: 20, marginBottom: 16,
                opacity: t, transform: `translateX(${shake * (ok ? 0 : 1)}px)`,
              }}>
                <span style={{ fontFamily: M, fontSize: 28, color: CLAUDE.INK, width: 190 }}>{p as string}</span>
                <span style={{ fontFamily: U, fontSize: 22, color: CLAUDE.GHOST }}>should be</span>
                <span style={{ fontFamily: M, fontSize: 28, color: CLAUDE.INK, width: 190 }}>{g as string}</span>
                {shown ? (
                  <span style={{
                    fontFamily: M, fontSize: 28, fontWeight: 700,
                    color: ok ? CLAUDE.INK_SOFT : CLAUDE.SPARK,
                  }}>{ok ? 'ok' : 'MARKER IS WRONG'}</span>
                ) : null}
              </div>
            );
          },
        )}
      </div>
      <div style={{
        position: 'absolute', left: 640, right: 130, top: 640, opacity: fail,
      }}>
        <div style={{ fontFamily: S, fontSize: 48, color: CLAUDE.INK, lineHeight: 1.3 }}>
          Two of the three fail. Now you know it is the test, not the robot.
        </div>
      </div>
      <SparkLine text="Check the ruler before you measure anything with it." delay={74} />
    </Page>
  );
};

// ── 8. KidFixedScores — the real marks appear ──────────────────────────────

export const kidFixedScoresSchema = z.object({
  before: z.number().default(0.60),
  after: z.number().default(1.0),
});
export type KidFixedScoresProps = z.infer<typeof kidFixedScoresSchema>;

export const KidFixedScores: React.FC<KidFixedScoresProps> = ({ before, after }) => {
  const frame = useCurrentFrame();
  const g1 = interpolate(frame, [12, 44], [0, before], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const g2 = interpolate(frame, [58, 96], [0, after], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const cheer = useRise(98);
  const W = 780;
  const bar = (v: number, label: string, accent: boolean) => (
    <div style={{ marginBottom: 46 }}>
      <div style={{ fontFamily: U, fontSize: 26, color: CLAUDE.INK_SOFT, marginBottom: 12 }}>{label}</div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 24 }}>
        <div style={{
          width: W * v, height: 62, borderRadius: 10,
          background: accent ? CLAUDE.SPARK : CLAUDE.PILL,
          border: accent ? 'none' : `1px solid ${CLAUDE.BORDER}`,
        }} />
        <span style={{ fontFamily: M, fontSize: 36, color: CLAUDE.INK }}>{(v * 100).toFixed(0)}%</span>
      </div>
    </div>
  );
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="mend the marker, mark again" />
      </div>
      <div style={{ position: 'absolute', left: 130, top: 250, width: 1000 }}>
        {bar(g1, 'with the broken marker', false)}
        {bar(g2, 'with the mended marker', true)}
      </div>
      <Robo x={1560} y={430 + bob(frame, 7)} scale={2.3} frame={frame} happy={cheer > 0.4} />
      {cheer > 0.02 ? (
        <div style={{
          position: 'absolute', left: 130, right: 130, top: 640, opacity: cheer,
        }}>
          <div style={{ fontFamily: S, fontSize: 50, color: CLAUDE.INK, lineHeight: 1.3 }}>
            The answers never changed. Only the marking did.
          </div>
        </div>
      ) : null}
      <SparkLine text="Same robot. Same answers. A completely different score." delay={104} />
    </Page>
  );
};
