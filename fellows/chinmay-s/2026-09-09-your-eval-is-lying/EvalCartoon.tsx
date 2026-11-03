import React from 'react';
import { useCurrentFrame, useVideoConfig, interpolate, spring } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { useRise, Eyebrow, SparkLine, Page, Card } from './IndexedOrInvisible';

/**
 * EvalCartoon — character-driven scenes for "Your Eval Is Lying to You".
 *
 * Cartoon BEHAVIOUR inside the Claude fidelity palette: squash-and-stretch,
 * anticipation, overshoot and recoil — but built only from cream, warm ink and
 * the single terracotta accent. No second hue is introduced, so these cut
 * against the diagram scenes without breaking the brand.
 *
 * The cast is one character, the Grader, reused across scenes so the reel
 * reads as a set rather than a pile of one-off gags.
 */

const S = CLAUDE_FONT.serif;
const U = CLAUDE_FONT.ui;
const M = CLAUDE_FONT.mono;

export type Mood = 'neutral' | 'stern' | 'pleased' | 'shifty';

/** One character: head, eyes, brow, body, two arms. Pure SVG, palette-only. */
export const Grader: React.FC<{
  x: number; y: number; scale?: number; mood?: Mood;
  squash?: number;
  armAngle?: number;
  lean?: number;
}> = ({ x, y, scale = 1, mood = 'neutral', squash = 1, armAngle = 0, lean = 0 }) => {
  const sx = squash, sy = 2 - squash;
  const eye = mood === 'stern' ? 3.4 : mood === 'shifty' ? 2.6 : 4.2;
  const browY = mood === 'stern' ? -2.5 : mood === 'pleased' ? -7 : -5;
  const browTilt = mood === 'stern' ? 14 : mood === 'pleased' ? -8 : 0;
  const eyeShift = mood === 'shifty' ? 3.2 : 0;
  return (
    <g transform={`translate(${x} ${y}) scale(${scale}) rotate(${lean})`}>
      <g transform={`scale(${sx} ${sy})`}>
        <path d="M -26 78 Q -30 22 0 20 Q 30 22 26 78 Z" fill={CLAUDE.INK} opacity={0.9} />
        <rect x={-40} y={30} width={13} height={40} rx={6.5} fill={CLAUDE.INK} opacity={0.9} />
        <g transform={`translate(31 34) rotate(${armAngle})`}>
          <rect x={-6.5} y={-6} width={13} height={44} rx={6.5} fill={CLAUDE.INK} opacity={0.9} />
        </g>
        <circle cx={0} cy={-14} r={32} fill={CLAUDE.CARD} stroke={CLAUDE.INK} strokeWidth={4.5} />
        <circle cx={-11 + eyeShift} cy={-16} r={eye} fill={CLAUDE.INK} />
        <circle cx={11 + eyeShift} cy={-16} r={eye} fill={CLAUDE.INK} />
        <line x1={-19} y1={-28 + browY} x2={-5} y2={-28 + browY + browTilt}
          stroke={CLAUDE.INK} strokeWidth={3.4} strokeLinecap="round" />
        <line x1={5} y1={-28 + browY + browTilt} x2={19} y2={-28 + browY}
          stroke={CLAUDE.INK} strokeWidth={3.4} strokeLinecap="round" />
        {mood === 'pleased' ? (
          <path d="M -9 -2 Q 0 6 9 -2" fill="none" stroke={CLAUDE.INK} strokeWidth={3.2} strokeLinecap="round" />
        ) : mood === 'stern' ? (
          <line x1={-9} y1={0} x2={9} y2={0} stroke={CLAUDE.INK} strokeWidth={3.2} strokeLinecap="round" />
        ) : (
          <path d="M -8 2 Q 0 -3 8 2" fill="none" stroke={CLAUDE.INK} strokeWidth={3} strokeLinecap="round" />
        )}
      </g>
    </g>
  );
};

/** Impact burst — the cartoon pow ring, terracotta only. */
const Burst: React.FC<{ x: number; y: number; t: number }> = ({ x, y, t }) => {
  if (t <= 0 || t >= 1) return null;
  const r = 14 + t * 66;
  return (
    <g transform={`translate(${x} ${y})`} opacity={1 - t}>
      <circle r={r} fill="none" stroke={CLAUDE.SPARK} strokeWidth={5 * (1 - t)} />
      {Array.from({ length: 8 }, (_, i) => {
        const a = (i * Math.PI) / 4;
        return (
          <line key={i}
            x1={Math.cos(a) * (r + 6)} y1={Math.sin(a) * (r + 6)}
            x2={Math.cos(a) * (r + 20)} y2={Math.sin(a) * (r + 20)}
            stroke={CLAUDE.SPARK} strokeWidth={4 * (1 - t)} strokeLinecap="round" />
        );
      })}
    </g>
  );
};

// ── 1. EvalGraderStamp — a correct answer, stamped WRONG ────────────────────

export const evalGraderStampSchema = z.object({});

export const EvalGraderStamp: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const paper = useRise(4);
  const swing = spring({ frame: frame - 26, fps, config: { damping: 9, stiffness: 190, mass: 0.7 } });
  const arm = interpolate(swing, [0, 0.45, 1], [-58, 24, 6]);
  const impact = frame >= 46;
  const hit = spring({ frame: frame - 46, fps, config: { damping: 7, stiffness: 320, mass: 0.5 } });
  const squash = 1 + (frame >= 44 && frame < 60 ? 0.16 * (1 - hit) : 0);
  const burstT = interpolate(frame, [46, 74], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const stampScale = interpolate(hit, [0, 1], [2.1, 1]);
  const shake = impact ? Math.sin((frame - 46) * 1.5) * 5 * Math.max(0, 1 - (frame - 46) / 18) : 0;

  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the scorer, doing its job" />
      </div>

      <svg width={1920} height={1080} style={{ position: 'absolute', inset: 0 }}>
        <g transform={`translate(${1090 + shake} 470) rotate(-3)`} opacity={paper}>
          <rect x={-330} y={-150} width={660} height={300} rx={14}
            fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={2} />
          <text x={-292} y={-96} style={{ fontFamily: U, fontSize: 21, fill: CLAUDE.INK_SOFT, letterSpacing: 2 }}>
            PREDICTION
          </text>
          <text x={-292} y={-48} style={{ fontFamily: M, fontSize: 27, fill: CLAUDE.INK }}>
            The capital of France is Paris.
          </text>
          <text x={-292} y={16} style={{ fontFamily: U, fontSize: 21, fill: CLAUDE.INK_SOFT, letterSpacing: 2 }}>
            GOLD
          </text>
          <text x={-292} y={62} style={{ fontFamily: M, fontSize: 27, fill: CLAUDE.INK }}>Paris</text>

          {impact ? (
            <g transform={`translate(150 20) rotate(-13) scale(${stampScale})`} opacity={Math.min(1, hit * 1.6)}>
              <rect x={-104} y={-40} width={208} height={80} rx={9}
                fill="none" stroke={CLAUDE.SPARK} strokeWidth={5} />
              <text x={0} y={16} textAnchor="middle"
                style={{ fontFamily: U, fontSize: 44, fontWeight: 700, fill: CLAUDE.SPARK, letterSpacing: 3 }}>
                0.00
              </text>
            </g>
          ) : null}
          <Burst x={150} y={20} t={burstT} />
        </g>

        <Grader x={520} y={430} scale={2.05} mood="stern" squash={squash} armAngle={arm} lean={swing * 4} />
      </svg>

      <SparkLine text="Correct answer. Correct city. Zero on both metrics." delay={80} />
    </Page>
  );
};

// ── 2. EvalSilentCatch — the exception nobody sees ──────────────────────────

export const evalSilentCatchSchema = z.object({});

export const EvalSilentCatch: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const code = useRise(4);
  const fall = interpolate(frame, [22, 46], [-230, 250], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const caught = frame >= 46;
  const stuff = spring({ frame: frame - 52, fps, config: { damping: 14, stiffness: 150, mass: 0.8 } });
  const fadeIn = interpolate(frame, [20, 26], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const errOpacity = caught ? Math.max(0, 1 - stuff * 1.5) : fadeIn;
  const errY = caught ? 250 + stuff * 96 : fall;
  const flagIn = useRise(74);
  const squash = caught && frame < 60 ? 1.12 : 1;

  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="why every score was zero" />
      </div>

      <svg width={1920} height={1080} style={{ position: 'absolute', inset: 0 }}>
        <g opacity={code}>
          <rect x={110} y={200} width={720} height={210} rx={13}
            fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={2} />
          <text x={146} y={252} style={{ fontFamily: M, fontSize: 25, fill: CLAUDE.INK_SOFT }}>try:</text>
          <text x={146} y={292} style={{ fontFamily: M, fontSize: 25, fill: CLAUDE.INK_SOFT }}>    client = OpenAI()</text>
          <text x={146} y={332} style={{ fontFamily: M, fontSize: 25, fill: CLAUDE.SPARK }}>except Exception:</text>
          <text x={146} y={372} style={{ fontFamily: M, fontSize: 25, fill: CLAUDE.SPARK }}>    OPENAI_AVAILABLE = False</text>
        </g>

        <g transform={`translate(1230 ${errY})`} opacity={errOpacity}>
          <rect x={-250} y={-38} width={500} height={76} rx={10}
            fill="#FBEEE8" stroke={CLAUDE.SPARK} strokeWidth={2.5} />
          <text x={0} y={8} textAnchor="middle" style={{ fontFamily: M, fontSize: 23, fill: CLAUDE.SEND }}>
            AuthenticationError: no api_key
          </text>
        </g>

        <g transform="translate(1230 640)">
          <path d="M -96 -46 L 96 -46 L 78 96 L -78 96 Z"
            fill={CLAUDE.PILL} stroke={CLAUDE.INK} strokeWidth={3.5} />
          <rect x={-112} y={-64} width={224} height={22} rx={11} fill={CLAUDE.INK} opacity={0.9} />
          <text x={0} y={150} textAnchor="middle"
            style={{ fontFamily: U, fontSize: 22, fill: CLAUDE.INK_SOFT, letterSpacing: 1.6 }}>
            swallowed, no message
          </text>
        </g>

        <Grader x={880} y={620} scale={1.75} mood="shifty" squash={squash} lean={-4} />
      </svg>

      <div style={{
        position: 'absolute', left: 110, top: 470, opacity: flagIn,
        transform: `translateY(${(1 - flagIn) * 14}px)`,
      }}>
        <Card style={{ padding: '24px 30px', width: 720, background: '#FBEEE8', border: `1px solid ${CLAUDE.SPARK}` }}>
          <div style={{ fontFamily: S, fontSize: 40, color: CLAUDE.INK, lineHeight: 1.28 }}>
            The notebook ran. Nothing called a model.
          </div>
        </Card>
      </div>

      <SparkLine text="A bare except turns a missing key into a silent mock." delay={96} />
    </Page>
  );
};

// ── 3. EvalTwinZeros — blank and wrong score identically ────────────────────

export const evalTwinZerosSchema = z.object({});

export const EvalTwinZeros: React.FC = () => {
  const frame = useCurrentFrame();
  const a = useRise(6);
  const b = useRise(18);
  const verdict = useRise(46);
  const bob = Math.sin(frame / 11) * 5;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="two failures, one score" />
      </div>

      <svg width={1920} height={1080} style={{ position: 'absolute', inset: 0 }}>
        <g opacity={a}>
          <Grader x={430} y={410 + bob} scale={1.6} mood="neutral" />
          <rect x={300} y={560} width={260} height={92} rx={11}
            fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={2} strokeDasharray="7 6" />
          <text x={430} y={615} textAnchor="middle" style={{ fontFamily: M, fontSize: 26, fill: CLAUDE.GHOST }}>
            &quot;&quot; (empty)
          </text>
          <text x={430} y={700} textAnchor="middle" style={{ fontFamily: U, fontSize: 23, fill: CLAUDE.INK_SOFT }}>
            the API call failed
          </text>
        </g>

        <g opacity={b}>
          <Grader x={1130} y={410 - bob} scale={1.6} mood="neutral" />
          <rect x={1000} y={560} width={260} height={92} rx={11}
            fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={2} />
          <text x={1130} y={615} textAnchor="middle" style={{ fontFamily: M, fontSize: 26, fill: CLAUDE.INK }}>
            &quot;Berlin&quot;
          </text>
          <text x={1130} y={700} textAnchor="middle" style={{ fontFamily: U, fontSize: 23, fill: CLAUDE.INK_SOFT }}>
            the model was wrong
          </text>
        </g>

        <g opacity={verdict}>
          <text x={1560} y={400} textAnchor="middle"
            style={{ fontFamily: M, fontSize: 84, fill: CLAUDE.SPARK }}>0.0</text>
          <text x={1560} y={452} textAnchor="middle"
            style={{ fontFamily: U, fontSize: 23, fill: CLAUDE.INK_SOFT, letterSpacing: 2 }}>EXACT MATCH</text>
          <text x={1560} y={560} textAnchor="middle"
            style={{ fontFamily: M, fontSize: 84, fill: CLAUDE.SPARK }}>0.0</text>
          <text x={1560} y={612} textAnchor="middle"
            style={{ fontFamily: U, fontSize: 23, fill: CLAUDE.INK_SOFT, letterSpacing: 2 }}>F1</text>
        </g>
      </svg>

      <SparkLine text="An outage and a wrong answer are indistinguishable in the results table." delay={70} />
    </Page>
  );
};

// ── 4. EvalRegexMiss — the fallback that swallows the essay ─────────────────

export const evalRegexMissSchema = z.object({});

const REASONING = [
  'First, France is a country in Europe.',
  'Its seat of government is in the north.',
  'That city is Paris.',
];

export const EvalRegexMiss: React.FC = () => {
  const frame = useCurrentFrame();
  const code = useRise(4);
  const sweep = interpolate(frame, [26, 66], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const grab = useRise(70);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the bug that has not fired yet" />
      </div>

      <svg width={1920} height={1080} style={{ position: 'absolute', inset: 0 }}>
        <g opacity={code}>
          <rect x={110} y={186} width={880} height={106} rx={12}
            fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={2} />
          <text x={146} y={232} style={{ fontFamily: M, fontSize: 22, fill: CLAUDE.INK_SOFT }}>
            m = re.search(r&quot;final answer\s*:\s*(.*)&quot;, text)
          </text>
          <text x={146} y={270} style={{ fontFamily: M, fontSize: 22, fill: CLAUDE.SPARK }}>
            return m.group(1) if m else text.strip()
          </text>
        </g>

        <g>
          <rect x={110} y={340} width={880} height={230} rx={12}
            fill={grab > 0.2 ? '#FBEEE8' : CLAUDE.CARD}
            stroke={grab > 0.2 ? CLAUDE.SPARK : CLAUDE.BORDER} strokeWidth={grab > 0.2 ? 3 : 2} />
          {REASONING.map((l, i) => (
            <text key={i} x={146} y={392 + i * 46}
              style={{ fontFamily: M, fontSize: 24, fill: CLAUDE.INK }}>{l}</text>
          ))}
          <text x={146} y={530}
            style={{ fontFamily: M, fontSize: 24, fill: CLAUDE.GHOST }}>
            (no &quot;Final answer:&quot; anywhere)
          </text>
        </g>

        {sweep > 0 && sweep < 1 ? (
          <line x1={130 + sweep * 840} y1={340} x2={130 + sweep * 840} y2={570}
            stroke={CLAUDE.SPARK} strokeWidth={3} opacity={0.65} />
        ) : null}

        <g opacity={grab}>
          <Grader x={1330} y={430} scale={1.85} mood="pleased" armAngle={-30}
            squash={1 + 0.08 * Math.sin(frame / 6)} />
          <rect x={1140} y={620} width={620} height={92} rx={11}
            fill="#FBEEE8" stroke={CLAUDE.SPARK} strokeWidth={2.5} />
          <text x={1450} y={676} textAnchor="middle"
            style={{ fontFamily: U, fontSize: 25, fill: CLAUDE.SEND }}>
            the entire essay becomes the answer
          </text>
        </g>
      </svg>

      <SparkLine text="It never fired here — because the mock never wrote a sentence." delay={96} />
    </Page>
  );
};

// ── 5. EvalGoldenTest — grade the grader ────────────────────────────────────

export const evalGoldenTestSchema = z.object({});

const ASSERTS: [string, boolean][] = [
  ['assert em("Paris.",   "Paris")    == 1', false],
  ['assert em("Brasilia", "Brasília") == 1', false],
  ['assert em("paris",    "Paris")    == 1', true],
  ['assert f1("Delhi", "New Delhi")    > 0.5', true],
];

export const EvalGoldenTest: React.FC = () => {
  const frame = useCurrentFrame();
  const card = useRise(5);
  const revealed = interpolate(frame, [24, 96], [0, ASSERTS.length], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const closer = useRise(104);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the test the notebook never wrote" />
      </div>

      <div style={{ position: 'absolute', left: 130, top: 190, width: 1180, opacity: card }}>
        <Card style={{ padding: '30px 34px' }}>
          {ASSERTS.map(([src, pass], i) => {
            const shown = i < revealed;
            return (
              <div key={src} style={{
                display: 'flex', alignItems: 'center', gap: 20, padding: '18px 0',
                borderBottom: i < ASSERTS.length - 1 ? `1px solid ${CLAUDE.BORDER}` : 'none',
                opacity: shown ? 1 : 0.18,
              }}>
                <div style={{
                  width: 30, height: 30, borderRadius: 15, flexShrink: 0,
                  border: `2.5px solid ${shown ? (pass ? CLAUDE.GHOST : CLAUDE.SPARK) : CLAUDE.PILL}`,
                  background: shown && !pass ? '#FBEEE8' : 'transparent',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontFamily: U, fontSize: 18, fontWeight: 700,
                  color: pass ? CLAUDE.GHOST : CLAUDE.SEND,
                }}>{shown ? (pass ? '✓' : '✕') : ''}</div>
                <span style={{ flex: 1, fontFamily: M, fontSize: 25, color: CLAUDE.INK }}>{src}</span>
                <span style={{
                  fontFamily: U, fontSize: 20, letterSpacing: 1.6, textTransform: 'uppercase',
                  color: shown ? (pass ? CLAUDE.GHOST : CLAUDE.SPARK) : 'transparent',
                }}>{pass ? 'passes' : 'FAILS'}</span>
              </div>
            );
          })}
        </Card>
      </div>

      <svg width={1920} height={1080} style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}>
        <g opacity={closer}>
          <Grader x={1600} y={700} scale={1.45} mood="stern" lean={3} />
        </g>
      </svg>

      <div style={{ position: 'absolute', left: 130, top: 620, width: 900, opacity: closer }}>
        <div style={{ fontFamily: S, fontSize: 46, color: CLAUDE.INK, lineHeight: 1.26 }}>
          Four lines would have caught all of it.
        </div>
      </div>

      <SparkLine text="If the scorer is untested, every number downstream is a guess." delay={116} />
    </Page>
  );
};
