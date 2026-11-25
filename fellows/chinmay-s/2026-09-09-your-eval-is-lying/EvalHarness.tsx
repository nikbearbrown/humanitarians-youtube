import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { useRise, Eyebrow, SparkLine, Page, Card } from './IndexedOrInvisible';

/**
 * EvalHarness — scene set for "Your Eval Is Lying to You".
 *
 * Subject: an LLM prompt-engineering notebook whose evaluation harness reports
 * 0.0 across the board. Every number rendered here was computed by running the
 * notebook's OWN scoring functions — nothing is illustrative-but-fake.
 *
 * Duration-agnostic like the Idx set: springs settle early, counters clamp.
 */

const S = CLAUDE_FONT.serif;
const U = CLAUDE_FONT.ui;
const M = CLAUDE_FONT.mono;

const RE_LINE = 'text = re.sub(r"[^a-z0-9\\s\\.\\-]", " ", text)';
const FIX_LINE = [
  't = unicodedata.normalize("NFKD", t)',
  '      .encode("ascii", "ignore").decode()',
  't = re.sub(r"[^a-z0-9\\s\\-]", " ", t)',
].join('\n');
const KEEP = /[a-z0-9\s.-]/;

// ── 1. EvalPromptDiff — baseline vs chain-of-thought ────────────────────────

export const evalPromptDiffSchema = z.object({});

export const EvalPromptDiff: React.FC = () => {
  const a = useRise(5);
  const b = useRise(20);
  const box = (title: string, body: string, tag: string, accent: boolean, t: number) => (
    <div style={{ flex: 1, opacity: t, transform: `translateY(${(1 - t) * 18}px)` }}>
      <div style={{
        fontFamily: U, fontSize: 21, fontWeight: 600, letterSpacing: 2,
        color: accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT, marginBottom: 14,
      }}>{title}</div>
      <Card accent={accent} style={{ padding: '26px 28px', height: 300 }}>
        <pre style={{
          margin: 0, fontFamily: M, fontSize: 22, lineHeight: 1.65,
          color: CLAUDE.INK, whiteSpace: 'pre-wrap',
        }}>{body}</pre>
      </Card>
      <div style={{ marginTop: 16, fontFamily: U, fontSize: 23, color: CLAUDE.INK_SOFT }}>{tag}</div>
    </div>
  );
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 78 }}>
        <Eyebrow text="the prompt is the interface" />
      </div>
      <div style={{ position: 'absolute', left: 120, right: 120, top: 182, display: 'flex', gap: 44 }}>
        {box('BASELINE',
          'Answer the following\nquestion in one or\ntwo words.\n\nQuestion: {q}\nAnswer:',
          'answer only — nothing to parse', false, a)}
        {box('CHAIN-OF-THOUGHT',
          'Solve step by step\nand then give the\ncapital.\n\nQuestion: {q}\n\nFinal answer:',
          'reasoning, then a parseable commit line', true, b)}
      </div>
      <SparkLine text="Two interfaces to the same model — and two different parsing problems." delay={40} />
    </Page>
  );
};

// ── 2. EvalPipeline — call → extract → normalize → score ────────────────────

export const evalPipelineSchema = z.object({});

const STAGES: [string, string, boolean][] = [
  ['call_model', 'ask the LLM', false],
  ['extract_final_answer', 'regex the commit line', true],
  ['normalize_text', 'lowercase + strip chars', true],
  ['exact_match / f1', 'compare to gold', true],
];

export const EvalPipeline: React.FC = () => {
  const closer = useRise(56);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 78 }}>
        <Eyebrow text="every prediction walks these four steps" />
      </div>
      <div style={{
        position: 'absolute', left: 96, right: 96, top: 250,
        display: 'flex', alignItems: 'stretch',
      }}>
        {STAGES.map(([fn, sub, isStr], i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(6 + i * 13);
          return (
            <React.Fragment key={fn}>
              <div style={{ flex: 1, opacity: t, transform: `translateY(${(1 - t) * 18}px)` }}>
                <Card accent={isStr} style={{
                  padding: '26px 18px', height: '100%', textAlign: 'center',
                  background: isStr ? '#FBEEE8' : CLAUDE.CARD,
                }}>
                  <div style={{ fontFamily: M, fontSize: 21, color: CLAUDE.INK, wordBreak: 'break-word' }}>{fn}</div>
                  <div style={{ fontFamily: U, fontSize: 19, color: CLAUDE.INK_SOFT, marginTop: 12 }}>{sub}</div>
                  {isStr ? (
                    <div style={{
                      marginTop: 16, fontFamily: U, fontSize: 17, letterSpacing: 1.4,
                      color: CLAUDE.SEND, textTransform: 'uppercase',
                    }}>string handling</div>
                  ) : null}
                </Card>
              </div>
              {i < STAGES.length - 1 ? (
                <div style={{
                  width: 42, display: 'flex', alignItems: 'center', justifyContent: 'center',
                  opacity: t, fontFamily: U, fontSize: 28, color: CLAUDE.GHOST,
                }}>→</div>
              ) : null}
            </React.Fragment>
          );
        })}
      </div>
      <div style={{
        position: 'absolute', left: 96, right: 96, top: 560,
        opacity: closer, transform: `translateY(${(1 - closer) * 12}px)`,
      }}>
        <div style={{ fontFamily: S, fontSize: 46, color: CLAUDE.INK, lineHeight: 1.3 }}>
          Three of the four never touch the model.
        </div>
      </div>
      <SparkLine text="Which means three of the four can fail without the model being wrong." delay={72} />
    </Page>
  );
};

// ── 3. EvalZeroChart — the chart that rendered perfectly ────────────────────

export const evalZeroChartSchema = z.object({});

const BARS = ['A-baseline', 'A-cot', 'B-baseline', 'B-cot'];

export const EvalZeroChart: React.FC = () => {
  const frame = useCurrentFrame();
  const axes = useRise(5);
  const stamp = useRise(64, 20);
  const tick = interpolate(frame, [18, 46], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const H = 330;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="what the notebook actually produced" />
      </div>

      <div style={{ position: 'absolute', left: 150, top: 190, width: 880, opacity: axes }}>
        <div style={{ fontFamily: U, fontSize: 26, color: CLAUDE.INK, marginBottom: 22 }}>
          Prompt Performance on Dataset A vs B
        </div>
        <div style={{
          display: 'flex', gap: 20, alignItems: 'flex-end', height: H,
          borderBottom: `2px solid ${CLAUDE.INK_SOFT}`,
          borderLeft: `2px solid ${CLAUDE.INK_SOFT}`, paddingLeft: 26,
        }}>
          {BARS.map((b) => (
            <div key={b} style={{
              flex: 1, display: 'flex', flexDirection: 'column',
              justifyContent: 'flex-end', height: '100%',
            }}>
              <div style={{
                height: Math.max(2, 2 * tick),
                background: CLAUDE.SPARK, borderRadius: '4px 4px 0 0',
              }} />
            </div>
          ))}
        </div>
        <div style={{ display: 'flex', gap: 20, paddingLeft: 26, marginTop: 12 }}>
          {BARS.map((b) => (
            <div key={b} style={{
              flex: 1, textAlign: 'center', fontFamily: M, fontSize: 19, color: CLAUDE.INK_SOFT,
            }}>{b}</div>
          ))}
        </div>
        <div style={{ marginTop: 18, fontFamily: U, fontSize: 22, color: CLAUDE.GHOST }}>
          y-axis: Average Exact Match (0 – 1.05)
        </div>
      </div>

      <div style={{
        position: 'absolute', right: 130, top: 300, width: 620,
        opacity: stamp, transform: `scale(${0.96 + 0.04 * stamp})`,
      }}>
        <Card accent style={{ padding: '32px 34px', background: '#FBEEE8' }}>
          <div style={{ fontFamily: M, fontSize: 74, color: CLAUDE.SEND, lineHeight: 1 }}>0.00</div>
          <div style={{ fontFamily: U, fontSize: 27, color: CLAUDE.INK, marginTop: 16, lineHeight: 1.45 }}>
            Every bar. Every dataset. Every prompt.
          </div>
          <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 14 }}>
            No error. No warning. It rendered.
          </div>
        </Card>
      </div>

      <SparkLine text="A chart that draws cleanly looks exactly like a chart that means something." delay={82} />
    </Page>
  );
};

// ── 4. EvalNormalizer — watch the accent get deleted ────────────────────────

export const evalNormalizerSchema = z.object({});

export const EvalNormalizer: React.FC = () => {
  const frame = useCurrentFrame();
  const head = useRise(4);
  const verdict = useRise(70);
  const src = 'Brasília';
  const upto = interpolate(frame, [24, 78], [0, src.length], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const lower = src.toLowerCase();
  const killed = lower.split('').map((ch) => !KEEP.test(ch));
  const out = lower.split('').map((ch, i) => (i >= upto ? null : (KEEP.test(ch) ? ch : ' ')));

  const cellStyle = (accent: boolean, filled: boolean): React.CSSProperties => ({
    width: 62, height: 78, borderRadius: 10,
    border: `2px solid ${accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
    background: filled ? '#FBEEE8' : CLAUDE.CARD,
    display: 'flex', alignItems: 'center', justifyContent: 'center',
    fontFamily: M, fontSize: 34, color: CLAUDE.INK,
  });

  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="normalize_text(), one character at a time" />
      </div>

      <div style={{ position: 'absolute', left: 130, right: 130, top: 172, opacity: head }}>
        <Card style={{ padding: '22px 26px' }}>
          <pre style={{
            margin: 0, fontFamily: M, fontSize: 23, color: CLAUDE.INK_SOFT, lineHeight: 1.6,
          }}>{RE_LINE}</pre>
        </Card>

        <div style={{
          marginTop: 42, fontFamily: U, fontSize: 22, letterSpacing: 2, color: CLAUDE.INK_SOFT,
        }}>INPUT</div>
        <div style={{ display: 'flex', gap: 10, marginTop: 14 }}>
          {src.split('').map((ch, i) => (
            <div key={i} style={cellStyle(killed[i], killed[i])}>{ch}</div>
          ))}
        </div>

        <div style={{
          marginTop: 32, fontFamily: U, fontSize: 22, letterSpacing: 2, color: CLAUDE.SPARK,
        }}>OUTPUT</div>
        <div style={{ display: 'flex', gap: 10, marginTop: 14 }}>
          {out.map((ch, i) => (
            <div key={i} style={cellStyle(ch === ' ', false)}>
              {ch === null ? '' : (ch === ' ' ? '␣' : ch)}
            </div>
          ))}
        </div>
      </div>

      <div style={{
        position: 'absolute', left: 130, right: 130, top: 726,
        opacity: verdict, transform: `translateY(${(1 - verdict) * 12}px)`,
      }}>
        <div style={{ fontFamily: S, fontSize: 48, color: CLAUDE.INK }}>
          “Brasília” becomes <span style={{ fontFamily: M, color: CLAUDE.SEND }}>“bras lia”</span> — two tokens.
        </div>
      </div>

      <SparkLine text="The gold answer is mangled before the model is ever compared to it." delay={86} />
    </Page>
  );
};

// ── 5. EvalScoreboard — live EM / F1 on real pairs ──────────────────────────

export const evalScoreboardSchema = z.object({
  rows: z.array(z.object({
    pred: z.string(), gold: z.string(), em: z.number(), f1: z.number(),
  })).default([]),
  eyebrow: z.string().default('scored by the notebook’s own functions'),
  sparkLine: z.string().default(''),
});
export type EvalScoreboardProps = z.infer<typeof evalScoreboardSchema>;

export const EvalScoreboard: React.FC<EvalScoreboardProps> = ({ rows, eyebrow, sparkLine }) => {
  const frame = useCurrentFrame();
  const card = useRise(4);
  const shown = interpolate(frame, [16, 16 + Math.max(1, rows.length) * 16], [0, rows.length], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const cell = (v: number) => (v >= 1 ? CLAUDE.INK : CLAUDE.SEND);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 78 }}>
        <Eyebrow text={eyebrow} />
      </div>
      <div style={{ position: 'absolute', left: 120, right: 120, top: 186, opacity: card }}>
        <Card style={{ padding: '10px 30px 20px' }}>
          <div style={{
            display: 'flex', padding: '18px 0', borderBottom: `2px solid ${CLAUDE.BORDER}`,
            fontFamily: U, fontSize: 20, letterSpacing: 2, color: CLAUDE.INK_SOFT,
          }}>
            <span style={{ flex: 2.4 }}>PREDICTION</span>
            <span style={{ flex: 1.1 }}>GOLD</span>
            <span style={{ width: 110, textAlign: 'right' }}>EM</span>
            <span style={{ width: 130, textAlign: 'right' }}>F1</span>
          </div>
          {rows.map((r, i) => {
            const on = i < shown;
            return (
              <div key={i} style={{
                display: 'flex', alignItems: 'center', padding: '18px 0',
                borderBottom: i < rows.length - 1 ? `1px solid ${CLAUDE.BORDER}` : 'none',
                opacity: on ? 1 : 0.15,
              }}>
                <span style={{ flex: 2.4, fontFamily: M, fontSize: 23, color: CLAUDE.INK }}>{r.pred}</span>
                <span style={{ flex: 1.1, fontFamily: M, fontSize: 23, color: CLAUDE.INK_SOFT }}>{r.gold}</span>
                <span style={{
                  width: 110, textAlign: 'right', fontFamily: M, fontSize: 27, color: cell(r.em),
                }}>{on ? r.em.toFixed(0) : '·'}</span>
                <span style={{
                  width: 130, textAlign: 'right', fontFamily: M, fontSize: 27, color: cell(r.f1),
                }}>{on ? r.f1.toFixed(2) : '·'}</span>
              </div>
            );
          })}
        </Card>
      </div>
      <SparkLine text={sparkLine} delay={16 + Math.max(1, rows.length) * 16 + 10} />
    </Page>
  );
};

// ── 6. EvalTokenOverlap — what F1 actually measures ─────────────────────────

export const evalTokenOverlapSchema = z.object({});

const Chip: React.FC<{ text: string; on: boolean }> = ({ text, on }) => (
  <div style={{
    padding: '12px 22px', borderRadius: 10,
    background: on ? '#FBEEE8' : CLAUDE.PILL,
    border: `2px solid ${on ? CLAUDE.SPARK : 'transparent'}`,
    fontFamily: M, fontSize: 27, color: on ? CLAUDE.SEND : CLAUDE.INK_SOFT,
  }}>{text}</div>
);

export const EvalTokenOverlap: React.FC = () => {
  const l = useRise(6);
  const r = useRise(16);
  const hit = useRise(38);
  const score = useRise(56);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 78 }}>
        <Eyebrow text="f1 = token overlap, not string equality" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 214 }}>
        <div style={{ opacity: l }}>
          <div style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT, letterSpacing: 2 }}>PREDICTION</div>
          <div style={{ display: 'flex', gap: 14, marginTop: 14 }}>
            <Chip text="delhi" on />
          </div>
        </div>
        <div style={{ marginTop: 34, opacity: r }}>
          <div style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT, letterSpacing: 2 }}>GOLD</div>
          <div style={{ display: 'flex', gap: 14, marginTop: 14 }}>
            <Chip text="new" on={false} />
            <Chip text="delhi" on />
          </div>
        </div>
        <div style={{ marginTop: 48, opacity: hit, display: 'flex', gap: 58, alignItems: 'baseline' }}>
          <div>
            <div style={{ fontFamily: M, fontSize: 40, color: CLAUDE.INK }}>1 / 1</div>
            <div style={{ fontFamily: U, fontSize: 21, color: CLAUDE.INK_SOFT, marginTop: 6 }}>precision</div>
          </div>
          <div>
            <div style={{ fontFamily: M, fontSize: 40, color: CLAUDE.INK }}>1 / 2</div>
            <div style={{ fontFamily: U, fontSize: 21, color: CLAUDE.INK_SOFT, marginTop: 6 }}>recall</div>
          </div>
          <div style={{ opacity: score }}>
            <div style={{ fontFamily: M, fontSize: 52, color: CLAUDE.SEND }}>0.67</div>
            <div style={{ fontFamily: U, fontSize: 21, color: CLAUDE.INK_SOFT, marginTop: 6 }}>F1 — partial credit</div>
          </div>
          <div style={{ opacity: score }}>
            <div style={{ fontFamily: M, fontSize: 52, color: CLAUDE.INK_SOFT }}>0</div>
            <div style={{ fontFamily: U, fontSize: 21, color: CLAUDE.INK_SOFT, marginTop: 6 }}>exact match</div>
          </div>
        </div>
      </div>
      <SparkLine text="F1 is the forgiving metric — until a full stop lands on the token." delay={70} />
    </Page>
  );
};

// ── 7. EvalBeforeAfter — the four-line fix, measured ────────────────────────

export const evalBeforeAfterSchema = z.object({
  before: z.number().default(0.6),
  after: z.number().default(1.0),
});
export type EvalBeforeAfterProps = z.infer<typeof evalBeforeAfterSchema>;

export const EvalBeforeAfter: React.FC<EvalBeforeAfterProps> = ({ before, after }) => {
  const frame = useCurrentFrame();
  const fix = useRise(4);
  const grow = interpolate(frame, [30, 92], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const H = 300;
  const bar = (label: string, val: number, accent: boolean) => (
    <div style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <div style={{
        fontFamily: M, fontSize: 40, color: accent ? CLAUDE.SEND : CLAUDE.INK_SOFT, marginBottom: 14,
      }}>{val.toFixed(2)}</div>
      <div style={{
        width: 150, height: H * val,
        background: accent ? CLAUDE.SPARK : CLAUDE.PILL,
        borderRadius: '8px 8px 0 0',
      }} />
      <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.INK, marginTop: 16 }}>{label}</div>
    </div>
  );
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="same predictions · same gold · same metrics" />
      </div>

      <div style={{ position: 'absolute', left: 120, top: 210, width: 840, opacity: fix }}>
        <Card style={{ padding: '24px 28px' }}>
          <pre style={{
            margin: 0, fontFamily: M, fontSize: 21, lineHeight: 1.7, color: CLAUDE.INK_SOFT,
          }}>{FIX_LINE}</pre>
          <div style={{ marginTop: 16, fontFamily: U, fontSize: 22, color: CLAUDE.SPARK }}>
            fold the accent · drop the full stop
          </div>
        </Card>
      </div>

      <div style={{
        position: 'absolute', right: 150, top: 200, width: 600,
        display: 'flex', gap: 60, alignItems: 'flex-end', height: H + 100,
      }}>
        {bar('broken', before * Math.min(1, grow * 1.6), false)}
        {bar('fixed', before + (after - before) * grow, true)}
      </div>

      <SparkLine text="Nothing about the model changed. Forty percent of the score was the harness." delay={100} />
    </Page>
  );
};
