/**
 * MiniRag.tsx — reel-local Remotion components for claude-liam-minirag
 * ("MiniRAG: The Index Does the Thinking").
 *
 * Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (the ONE accent).
 * All 1920x1080, registered in Root.tsx under the folder "MiniRag".
 *
 * SOURCE CARE: every number these components display arrives as a PROP from
 * beat_sheet.json — no component hardcodes a statistic, so a wrong figure is a
 * beat-sheet fix, never a component fix. Figures trace to Fan, Wang, Ren &
 * Huang, "MiniRAG", arXiv:2501.06713v3 (Tables 1-3); see the reel's FACTCHECK.md.
 *
 * Every scene is a pure function of `frame / durationInFrames`, so each one
 * fills whatever window the measured Kokoro audio assigns it.
 */
import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { z } from 'zod';

// ── Palette ──────────────────────────────────────────────────────────────────
const BG     = '#F2F0E9';
const INK    = '#3D3929';
const ACC    = '#D97757';
const SOFT   = '#73705F';
const GHOST  = '#C6C2B2';
const CARD   = '#FFFFFF';
const BORDER = '#DDD9CC';

// ── Type stack ───────────────────────────────────────────────────────────────
const SERIF = '"EB Garamond", Georgia, "Times New Roman", serif';
const MONO  = '"SF Mono", ui-monospace, Menlo, monospace';

// ── Layout — title-safe inset on a 1920x1080 canvas ──────────────────────────
const CW = 1920;
const CH = 1080;
const SX = 96;   // 5% on the horizontal axis
const SY = 54;   // 5% on the vertical axis

const cl = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const GENTLE = { damping: 30, stiffness: 120, mass: 0.9 };

/** Progress-window helper: 0 before `from`, 1 after `to`. */
const win = (t: number, from: number, to: number) =>
  cl(interpolate(t, [from, to], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

/** Spark + one short serif line. SPARK-LINE LAW on illustration beats. */
const SparkLine: React.FC<{ line: string; t: number; bottom?: boolean }> = ({ line, t, bottom }) => {
  if (!line) return null;
  const o = win(t, 0.02, 0.10);
  return (
    <div style={{
      position: 'absolute', left: SX, [bottom ? 'bottom' : 'top']: SY,
      display: 'flex', alignItems: 'baseline', gap: 14, opacity: o,
      transform: `translateY(${(1 - o) * 8}px)`,
    }}>
      <span style={{ color: ACC, fontFamily: SERIF, fontSize: 40, lineHeight: 1 }}>✳</span>
      <span style={{ color: INK, fontFamily: SERIF, fontSize: 40, fontStyle: 'italic', letterSpacing: '-0.01em' }}>
        {line}
      </span>
    </div>
  );
};

/** Small provenance line, bottom-right. REBUILD LAW: cite the redraw, once, small. */
const Credit: React.FC<{ text: string; t: number }> = ({ text, t }) => {
  if (!text) return null;
  return (
    <div style={{
      position: 'absolute', right: SX, bottom: SY, maxWidth: 900, textAlign: 'right',
      color: SOFT, fontFamily: SERIF, fontSize: 24, opacity: win(t, 0.80, 0.92) * 0.9,
    }}>
      {text}
    </div>
  );
};

// ═════════════════════════════════════════════════════════════════════════════
// 1. MiniRagStackToday — B02. Three stages, one dependency underneath them all.
// ═════════════════════════════════════════════════════════════════════════════
export const miniRagStackTodaySchema = z.object({
  spark: z.string().default(''),
  stages: z.array(z.string()).min(2).max(4).default(['INDEX', 'RETRIEVE', 'GENERATE']),
  stageSubs: z.array(z.string()).default([]),
  bandLabel: z.string().default('LARGE LANGUAGE MODEL'),
  caption: z.string().default(''),
});
export type MiniRagStackTodayProps = z.infer<typeof miniRagStackTodaySchema>;

export const MiniRagStackToday: React.FC<MiniRagStackTodayProps> = ({
  spark, stages, stageSubs, bandLabel, caption,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;

  const n = stages.length;
  const gap = 56;
  const totalW = CW - SX * 2;
  const boxW = (totalW - gap * (n - 1)) / n;
  // FILL-THE-CANVAS: sized so stages + band + caption span the safe area.
  const boxH = 380;
  const boxY = 232;

  const bandIn = win(t, 0.58, 0.72);
  const capIn = win(t, 0.82, 0.92);

  return (
    <AbsoluteFill style={{ backgroundColor: BG }}>
      <SparkLine line={spark} t={t} />

      {stages.map((s, i) => {
        const app = win(t, 0.08 + i * 0.13, 0.20 + i * 0.13);
        const x = SX + i * (boxW + gap);
        const lit = bandIn;
        return (
          <React.Fragment key={s}>
            {i > 0 && (
              <div style={{
                position: 'absolute', left: x - gap + 8, top: boxY + boxH / 2 - 1,
                width: (gap - 16) * app, height: 2, backgroundColor: GHOST,
              }} />
            )}
            <div style={{
              position: 'absolute', left: x, top: boxY, width: boxW, height: boxH,
              background: CARD, border: `2px solid ${lit > 0.5 ? ACC : BORDER}`,
              borderRadius: 14, opacity: app,
              transform: `translateY(${(1 - app) * 20}px)`,
              display: 'flex', flexDirection: 'column',
              alignItems: 'center', justifyContent: 'center', gap: 20, padding: 32,
            }}>
              <div style={{
                fontFamily: SERIF, fontSize: 76, fontWeight: 700, color: INK,
                letterSpacing: '-0.01em', textAlign: 'center',
              }}>{s}</div>
              {stageSubs[i] ? (
                <div style={{
                  fontFamily: SERIF, fontSize: 34, color: SOFT,
                  textAlign: 'center', lineHeight: 1.3, maxWidth: boxW - 64,
                }}>{stageSubs[i]}</div>
              ) : null}
            </div>
          </React.Fragment>
        );
      })}

      {/* The band: one dependency under every stage — the beat's whole argument. */}
      <div style={{
        position: 'absolute', left: SX, top: boxY + boxH + 74,
        width: (CW - SX * 2) * bandIn, height: 136,
        background: ACC, borderRadius: 12,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        overflow: 'hidden',
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: 58, fontWeight: 700, color: '#FFFFFF',
          letterSpacing: '0.06em', whiteSpace: 'nowrap', opacity: win(t, 0.66, 0.76),
        }}>{bandLabel}</div>
      </div>

      {/* Ties from each stage down into the band. */}
      {stages.map((s, i) => {
        const x = SX + i * (boxW + gap) + boxW / 2;
        return (
          <div key={`tie-${s}`} style={{
            position: 'absolute', left: x - 1, top: boxY + boxH,
            width: 2, height: 74 * bandIn, backgroundColor: ACC, opacity: 0.75,
          }} />
        );
      })}

      {caption ? (
        <div style={{
          position: 'absolute', left: SX, right: SX, top: boxY + boxH + 250,
          textAlign: 'center', fontFamily: SERIF, fontSize: 48, fontStyle: 'italic',
          color: INK, opacity: capIn,
        }}>{caption}</div>
      ) : null}
    </AbsoluteFill>
  );
};

// ═════════════════════════════════════════════════════════════════════════════
// 2. MiniRagPipeline — B06. Figure 1, rebuilt (REBUILD LAW).
// ═════════════════════════════════════════════════════════════════════════════
export const miniRagPipelineSchema = z.object({
  spark: z.string().default(''),
  panels: z.array(z.object({ title: z.string(), sub: z.string().default('') })).min(2).max(3),
  credit: z.string().default(''),
});
export type MiniRagPipelineProps = z.infer<typeof miniRagPipelineSchema>;

export const MiniRagPipeline: React.FC<MiniRagPipelineProps> = ({ spark, panels, credit }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;

  const n = panels.length;
  const gap = 44;
  const totalW = CW - SX * 2;
  const pw = (totalW - gap * (n - 1)) / n;
  const py = 214;
  const ph = 700;

  return (
    <AbsoluteFill style={{ backgroundColor: BG }}>
      <SparkLine line={spark} t={t} />

      {panels.map((p, i) => {
        const app = win(t, 0.06 + i * 0.22, 0.20 + i * 0.22);
        const x = SX + i * (pw + gap);
        const inner = win(t, 0.14 + i * 0.22, 0.34 + i * 0.22);
        return (
          <React.Fragment key={p.title}>
            {i > 0 && (
              <div style={{
                position: 'absolute', left: x - gap + 6, top: py + ph / 2 - 12,
                fontFamily: SERIF, fontSize: 34, color: GHOST, opacity: app,
              }}>→</div>
            )}
            <div style={{
              position: 'absolute', left: x, top: py, width: pw, height: ph,
              background: CARD, border: `2px solid ${BORDER}`, borderRadius: 16,
              opacity: app, transform: `translateY(${(1 - app) * 18}px)`,
              padding: 34, display: 'flex', flexDirection: 'column', gap: 18,
            }}>
              <div style={{
                fontFamily: SERIF, fontSize: 50, fontWeight: 700, color: INK,
                lineHeight: 1.12, letterSpacing: '-0.01em',
              }}>{p.title}</div>
              <div style={{ height: 2, width: 74, background: ACC, opacity: inner }} />
              <div style={{
                fontFamily: SERIF, fontSize: 31, color: SOFT, lineHeight: 1.38, opacity: inner,
              }}>{p.sub}</div>

              {/* Panel-specific mechanism sketch, drawn inside the card. */}
              <div style={{ position: 'relative', flex: 1, marginTop: 8 }}>
                {i === 0 && <SketchCollapse t={inner} w={pw - 68} />}
                {i === 1 && <SketchWalk t={inner} w={pw - 68} pulse={win(t, 0.48, 0.72)} />}
                {i === 2 && <SketchAnswer t={inner} w={pw - 68} />}
              </div>
            </div>
          </React.Fragment>
        );
      })}

      <Credit text={credit} t={t} />
    </AbsoluteFill>
  );
};

/** Panel 1: loose text lines collapsing into a compact graph. */
const SketchCollapse: React.FC<{ t: number; w: number }> = ({ t, w }) => {
  const pull = cl(t);
  return (
    <div style={{ position: 'absolute', inset: 0 }}>
      {[0, 1, 2, 3].map((i) => (
        <div key={i} style={{
          position: 'absolute', left: 0, top: 12 + i * 34,
          width: (w * 0.62) * (1 - pull * 0.55), height: 12,
          background: GHOST, borderRadius: 6, opacity: 1 - pull * 0.5,
        }} />
      ))}
      {[[0.62, 0.30], [0.80, 0.52], [0.60, 0.74], [0.86, 0.86]].map(([fx, fy], i) => (
        <div key={`n${i}`} style={{
          position: 'absolute', left: w * fx * pull, top: 160 * fy,
          width: 20, height: 20, borderRadius: 10,
          background: i === 1 ? ACC : INK, opacity: pull,
        }} />
      ))}
    </div>
  );
};

/** Panel 2: two labelled steps, a pulse riding the discovered path. */
const SketchWalk: React.FC<{ t: number; w: number; pulse: number }> = ({ t, w, pulse }) => {
  const pts = [[0.06, 0.80], [0.34, 0.34], [0.64, 0.66], [0.94, 0.22]];
  return (
    <div style={{ position: 'absolute', inset: 0 }}>
      {['STEP 1', 'STEP 2'].map((s, i) => (
        <div key={s} style={{
          position: 'absolute', left: i * (w * 0.5), top: 0,
          fontFamily: MONO, fontSize: 20, letterSpacing: '0.08em',
          color: i === 1 && pulse > 0.2 ? ACC : SOFT, opacity: cl(t),
        }}>{s}</div>
      ))}
      {pts.slice(0, -1).map((p, i) => {
        const q = pts[i + 1];
        const x1 = w * p[0], y1 = 46 + 130 * p[1];
        const x2 = w * q[0], y2 = 46 + 130 * q[1];
        const len = Math.hypot(x2 - x1, y2 - y1);
        const ang = (Math.atan2(y2 - y1, x2 - x1) * 180) / Math.PI;
        const grow = cl((t - i * 0.12) * 2.2);
        return (
          <div key={`e${i}`} style={{
            position: 'absolute', left: x1, top: y1,
            width: len * grow, height: 2, background: pulse > 0.3 ? ACC : GHOST,
            transformOrigin: '0 50%', transform: `rotate(${ang}deg)`,
          }} />
        );
      })}
      {pts.map((p, i) => (
        <div key={`p${i}`} style={{
          position: 'absolute', left: w * p[0] - 11, top: 46 + 130 * p[1] - 11,
          width: 22, height: 22, borderRadius: 11,
          background: pulse > 0.3 && i === pts.length - 1 ? ACC : INK,
          opacity: cl(t * 1.4 - i * 0.1),
        }} />
      ))}
    </div>
  );
};

/** Panel 3: evidence entering a small model, an answer leaving it. */
const SketchAnswer: React.FC<{ t: number; w: number }> = ({ t, w }) => (
  <div style={{ position: 'absolute', inset: 0 }}>
    {[0, 1, 2].map((i) => (
      <div key={i} style={{
        position: 'absolute', left: 0, top: 16 + i * 30,
        width: (w * 0.38) * cl(t * 1.4 - i * 0.15), height: 10,
        background: GHOST, borderRadius: 5,
      }} />
    ))}
    <div style={{
      position: 'absolute', left: w * 0.44, top: 24,
      width: w * 0.30, height: 78, borderRadius: 10,
      border: `2px solid ${INK}`, opacity: cl(t * 1.2),
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      fontFamily: MONO, fontSize: 18, color: INK, letterSpacing: '0.04em',
    }}>SLM</div>
    <div style={{
      position: 'absolute', left: 0, top: 132,
      width: w * cl(t * 1.6 - 0.4), height: 14,
      background: ACC, borderRadius: 7,
    }} />
  </div>
);

// ═════════════════════════════════════════════════════════════════════════════
// 3. MiniRagHeteroGraph — B07. Two node types, two edge families.
// ═════════════════════════════════════════════════════════════════════════════
export const miniRagHeteroGraphSchema = z.object({
  spark: z.string().default(''),
  chunkLabel: z.string().default('TEXT CHUNK'),
  entityLabel: z.string().default('ENTITY'),
  edgeAB: z.string().default('entity ↔ entity'),
  edgeBC: z.string().default('entity ↔ chunk'),
  edgeNote: z.string().default(''),
  credit: z.string().default(''),
});
export type MiniRagHeteroGraphProps = z.infer<typeof miniRagHeteroGraphSchema>;

export const MiniRagHeteroGraph: React.FC<MiniRagHeteroGraphProps> = ({
  spark, chunkLabel, entityLabel, edgeAB, edgeBC, edgeNote, credit,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;

  const chunks = [0, 1, 2, 3].map((i) => ({ x: 250 + i * 400, y: 810 }));
  const ents = [
    { x: 400, y: 430, c: 0 }, { x: 700, y: 330, c: 0 },
    { x: 1030, y: 440, c: 1 }, { x: 1330, y: 330, c: 2 }, { x: 1560, y: 470, c: 3 },
  ];
  const ee: [number, number][] = [[0, 1], [1, 2], [2, 3], [3, 4]];

  const chunkIn = (i: number) => cl(spring({ frame: frame - i * 4, fps, config: GENTLE }));
  const entIn = win(t, 0.24, 0.42);
  const eeIn = win(t, 0.44, 0.60);
  const ecIn = win(t, 0.60, 0.74);
  const noteIn = win(t, 0.78, 0.90);

  const Edge = ({ x1, y1, x2, y2, grow, color, dashed }:
    { x1: number; y1: number; x2: number; y2: number; grow: number; color: string; dashed?: boolean }) => {
    const len = Math.hypot(x2 - x1, y2 - y1);
    const ang = (Math.atan2(y2 - y1, x2 - x1) * 180) / Math.PI;
    return (
      <div style={{
        position: 'absolute', left: x1, top: y1, width: len * grow, height: dashed ? 0 : 3,
        borderTop: dashed ? `3px dashed ${color}` : undefined,
        background: dashed ? undefined : color,
        transformOrigin: '0 50%', transform: `rotate(${ang}deg)`, opacity: 0.85,
      }} />
    );
  };

  return (
    <AbsoluteFill style={{ backgroundColor: BG }}>
      <SparkLine line={spark} t={t} />

      {/* entity ↔ chunk (terracotta, dashed) */}
      {ents.map((e, i) => (
        <Edge key={`ec${i}`} x1={e.x} y1={e.y} x2={chunks[e.c].x} y2={chunks[e.c].y}
          grow={ecIn} color={ACC} dashed />
      ))}
      {/* entity ↔ entity (ink, solid) */}
      {ee.map(([a, b], i) => (
        <Edge key={`ee${i}`} x1={ents[a].x} y1={ents[a].y} x2={ents[b].x} y2={ents[b].y}
          grow={cl(eeIn * 1.6 - i * 0.15)} color={INK} />
      ))}

      {/* chunk nodes */}
      {chunks.map((c, i) => (
        <div key={`c${i}`} style={{
          position: 'absolute', left: c.x - 150, top: c.y - 52,
          width: 300, height: 104, background: CARD,
          border: `2px solid ${BORDER}`, borderRadius: 10,
          opacity: chunkIn(i), transform: `translateY(${(1 - chunkIn(i)) * 14}px)`,
          display: 'flex', flexDirection: 'column', gap: 9,
          alignItems: 'center', justifyContent: 'center',
        }}>
          {[0.72, 0.52].map((wf, k) => (
            <div key={k} style={{ width: 300 * wf * 0.7, height: 8, background: GHOST, borderRadius: 4 }} />
          ))}
        </div>
      ))}

      {/* entity nodes */}
      {ents.map((e, i) => {
        const o = cl(entIn * 1.8 - i * 0.12);
        return (
          <div key={`e${i}`} style={{
            position: 'absolute', left: e.x - 34, top: e.y - 34,
            width: 68, height: 68, borderRadius: 34,
            background: INK, opacity: o, transform: `scale(${0.6 + o * 0.4})`,
          }} />
        );
      })}

      {/* legend */}
      <div style={{ position: 'absolute', right: SX, top: SY + 4, display: 'flex', flexDirection: 'column', gap: 20, opacity: win(t, 0.30, 0.44) }}>
        {[
          { swatch: <div style={{ width: 40, height: 22, background: CARD, border: `2px solid ${BORDER}`, borderRadius: 5 }} />, label: chunkLabel },
          { swatch: <div style={{ width: 26, height: 26, borderRadius: 13, background: INK }} />, label: entityLabel },
          { swatch: <div style={{ width: 40, height: 3, background: INK }} />, label: edgeAB },
          { swatch: <div style={{ width: 40, height: 0, borderTop: `3px dashed ${ACC}` }} />, label: edgeBC },
        ].map((r, i) => (
          <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 16, justifyContent: 'flex-end' }}>
            <span style={{ fontFamily: SERIF, fontSize: 28, color: INK }}>{r.label}</span>
            <span style={{ width: 44, display: 'flex', justifyContent: 'center' }}>{r.swatch}</span>
          </div>
        ))}
      </div>

      {edgeNote ? (
        <div style={{
          position: 'absolute', left: SX, bottom: SY + 74, maxWidth: 1100,
          fontFamily: SERIF, fontSize: 32, fontStyle: 'italic', color: INK,
          opacity: noteIn, transform: `translateY(${(1 - noteIn) * 10}px)`,
        }}>{edgeNote}</div>
      ) : null}

      <Credit text={credit} t={t} />
    </AbsoluteFill>
  );
};

// ═════════════════════════════════════════════════════════════════════════════
// 4. MiniRagWorkedQuery — B08. One query, two systems, ground truth last.
// ═════════════════════════════════════════════════════════════════════════════
const sideSchema = z.object({
  system: z.string(),
  steps: z.array(z.string()).default([]),
  answer: z.string().default(''),
  ok: z.boolean().default(false),
});

export const miniRagWorkedQuerySchema = z.object({
  spark: z.string().default(''),
  query: z.string(),
  truth: z.string().default(''),
  left: sideSchema,
  right: sideSchema,
  credit: z.string().default(''),
});
export type MiniRagWorkedQueryProps = z.infer<typeof miniRagWorkedQuerySchema>;

export const MiniRagWorkedQuery: React.FC<MiniRagWorkedQueryProps> = ({
  spark, query, truth, left, right, credit,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;

  const colW = (CW - SX * 2 - 48) / 2;
  const colY = 396;
  const colH = 520;
  const qIn = win(t, 0.02, 0.12);
  const truthIn = win(t, 0.84, 0.94);

  const Column: React.FC<{ side: z.infer<typeof sideSchema>; x: number; from: number }> =
    ({ side, x, from }) => {
      const app = win(t, from, from + 0.10);
      const ansIn = win(t, from + 0.16, from + 0.24);
      return (
        <div style={{
          position: 'absolute', left: x, top: colY, width: colW, height: colH,
          background: CARD, borderRadius: 16,
          border: `2px solid ${side.ok && ansIn > 0.4 ? ACC : BORDER}`,
          opacity: app, transform: `translateY(${(1 - app) * 16}px)`,
          padding: 30, display: 'flex', flexDirection: 'column', gap: 16,
        }}>
          <div style={{
            fontFamily: MONO, fontSize: 24, letterSpacing: '0.08em',
            color: side.ok ? ACC : SOFT,
          }}>{side.system.toUpperCase()}</div>

          {side.steps.map((s, i) => (
            <div key={i} style={{
              display: 'flex', gap: 12, alignItems: 'flex-start',
              opacity: win(t, from + 0.06 + i * 0.04, from + 0.14 + i * 0.04),
            }}>
              <span style={{ fontFamily: MONO, fontSize: 22, color: GHOST, marginTop: 4 }}>{i + 1}</span>
              <span style={{ fontFamily: SERIF, fontSize: 28, color: SOFT, lineHeight: 1.3 }}>{s}</span>
            </div>
          ))}

          <div style={{ flex: 1 }} />
          <div style={{ height: 2, background: BORDER, opacity: ansIn }} />
          <div style={{
            fontFamily: SERIF, fontSize: side.ok ? 42 : 32,
            fontWeight: side.ok ? 700 : 400,
            color: side.ok ? ACC : SOFT,
            textDecoration: side.ok ? 'none' : 'line-through',
            textDecorationColor: GHOST,
            lineHeight: 1.2, opacity: ansIn,
          }}>{side.answer}</div>
        </div>
      );
    };

  return (
    <AbsoluteFill style={{ backgroundColor: BG }}>
      <SparkLine line={spark} t={t} />

      <div style={{
        position: 'absolute', left: SX, right: SX, top: SY + 92,
        fontFamily: SERIF, fontSize: 40, color: INK, lineHeight: 1.28,
        opacity: qIn, transform: `translateY(${(1 - qIn) * 10}px)`,
      }}>
        <span style={{ color: SOFT, fontFamily: MONO, fontSize: 22, letterSpacing: '0.08em' }}>QUERY&nbsp;&nbsp;</span>
        “{query}”
      </div>

      <Column side={left} x={SX} from={0.22} />
      <Column side={right} x={SX + colW + 48} from={0.50} />

      {truth ? (
        <div style={{
          position: 'absolute', left: SX, bottom: SY + 4,
          display: 'flex', alignItems: 'baseline', gap: 16, opacity: truthIn,
        }}>
          <span style={{ fontFamily: MONO, fontSize: 22, color: SOFT, letterSpacing: '0.08em' }}>GROUND TRUTH</span>
          <span style={{ fontFamily: SERIF, fontSize: 38, fontWeight: 700, color: INK }}>{truth}</span>
        </div>
      ) : null}

      <Credit text={credit} t={t} />
    </AbsoluteFill>
  );
};

// ═════════════════════════════════════════════════════════════════════════════
// 5. MiniRagAblationDrop — B10. Strip a layer, watch the number fall.
// ═════════════════════════════════════════════════════════════════════════════
export const miniRagAblationDropSchema = z.object({
  spark: z.string().default(''),
  baselineLabel: z.string().default('MiniRAG'),
  baseline: z.number(),
  steps: z.array(z.object({ label: z.string(), value: z.number() })).min(1).max(4),
  unit: z.string().default('%'),
  credit: z.string().default(''),
});
export type MiniRagAblationDropProps = z.infer<typeof miniRagAblationDropSchema>;

export const MiniRagAblationDrop: React.FC<MiniRagAblationDropProps> = ({
  spark, baselineLabel, baseline, steps, unit, credit,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;

  const stages = [{ label: baselineLabel, value: baseline }, ...steps];
  const segStart = 0.10;
  const segEnd = 0.80;
  const segLen = (segEnd - segStart) / stages.length;

  // Which stage are we in, and the eased value between it and the previous one.
  let idx = 0;
  for (let i = 0; i < stages.length; i += 1) {
    if (t >= segStart + segLen * i) idx = i;
  }
  const localT = win(t, segStart + segLen * idx, segStart + segLen * (idx + 0.7));
  const prev = idx === 0 ? baseline : stages[idx - 1].value;
  const shown = prev + (stages[idx].value - prev) * (idx === 0 ? 1 : localT);
  const isFinal = idx === stages.length - 1;

  // Structure remaining, 1 → 0 across the ablation.
  const intact = 1 - idx / Math.max(1, stages.length - 1);

  const nodes = [
    { x: 300, y: 430 }, { x: 520, y: 330 }, { x: 720, y: 470 }, { x: 470, y: 610 },
  ];
  const chunkY = 790;

  return (
    <AbsoluteFill style={{ backgroundColor: BG }}>
      <SparkLine line={spark} t={t} />

      {/* Left: the structure, losing a layer per step. */}
      <div style={{ position: 'absolute', left: 0, top: 0, width: CW * 0.52, height: CH }}>
        {/* entity↔chunk edges — first to go */}
        {nodes.map((n, i) => {
          const alive = cl(intact * 3 - 0.0);
          const x2 = 300 + i * 130;
          const len = Math.hypot(x2 - n.x, chunkY - n.y);
          const ang = (Math.atan2(chunkY - n.y, x2 - n.x) * 180) / Math.PI;
          return (
            <div key={`ec${i}`} style={{
              position: 'absolute', left: n.x, top: n.y, width: len, height: 0,
              borderTop: `3px dashed ${ACC}`, opacity: cl(alive - 1) * 0.9,
              transformOrigin: '0 50%', transform: `rotate(${ang}deg)`,
            }} />
          );
        })}
        {/* chunk nodes — second to go */}
        {[0, 1, 2, 3].map((i) => (
          <div key={`ch${i}`} style={{
            position: 'absolute', left: 240 + i * 130, top: chunkY - 32,
            width: 116, height: 64, background: CARD,
            border: `2px solid ${BORDER}`, borderRadius: 8,
            opacity: cl(intact * 3 - 1),
          }} />
        ))}
        {/* entity↔entity edges + nodes — last to go */}
        {[[0, 1], [1, 2], [2, 3], [3, 0]].map(([a, b], i) => {
          const len = Math.hypot(nodes[b].x - nodes[a].x, nodes[b].y - nodes[a].y);
          const ang = (Math.atan2(nodes[b].y - nodes[a].y, nodes[b].x - nodes[a].x) * 180) / Math.PI;
          return (
            <div key={`ee${i}`} style={{
              position: 'absolute', left: nodes[a].x, top: nodes[a].y,
              width: len, height: 3, background: INK, opacity: cl(intact * 3 - 2),
              transformOrigin: '0 50%', transform: `rotate(${ang}deg)`,
            }} />
          );
        })}
        {nodes.map((n, i) => (
          <div key={`n${i}`} style={{
            position: 'absolute', left: n.x - 30, top: n.y - 30,
            width: 60, height: 60, borderRadius: 30, background: INK,
            opacity: cl(intact * 3 - 2),
          }} />
        ))}
        {/* what's left when the structure is gone: a flat list */}
        {isFinal && [0, 1, 2, 3, 4].map((i) => (
          <div key={`flat${i}`} style={{
            position: 'absolute', left: 300, top: 420 + i * 54,
            width: 420 * localT, height: 16, background: GHOST, borderRadius: 8,
          }} />
        ))}
      </div>

      {/* Right: the counter and the ladder of steps. */}
      <div style={{ position: 'absolute', right: SX, top: 250, width: CW * 0.40, textAlign: 'right' }}>
        <div style={{
          fontFamily: SERIF, fontSize: 190, fontWeight: 700, lineHeight: 0.95,
          color: isFinal ? ACC : INK, letterSpacing: '-0.03em',
        }}>
          {shown.toFixed(2)}<span style={{ fontSize: 96 }}>{unit}</span>
        </div>
        <div style={{
          fontFamily: MONO, fontSize: 30, color: SOFT,
          letterSpacing: '0.06em', marginTop: 10, minHeight: 40,
        }}>{stages[idx].label}</div>

        <div style={{ marginTop: 52, display: 'flex', flexDirection: 'column', gap: 18, alignItems: 'flex-end' }}>
          {stages.slice(1).map((s, i) => (
            <div key={s.label} style={{
              fontFamily: SERIF, fontSize: 32,
              color: i + 1 === idx ? ACC : (i + 1 < idx ? SOFT : GHOST),
              opacity: i + 1 <= idx ? 1 : 0.45,
            }}>
              {s.label} → {s.value.toFixed(2)}{unit}
            </div>
          ))}
        </div>

        {isFinal ? (
          <div style={{
            marginTop: 44, fontFamily: SERIF, fontSize: 38, fontStyle: 'italic',
            color: INK, opacity: win(t, 0.86, 0.95),
          }}>
            {baseline.toFixed(2)}{unit} → {stages[stages.length - 1].value.toFixed(2)}{unit}
          </div>
        ) : null}
      </div>

      <Credit text={credit} t={t} />
    </AbsoluteFill>
  );
};

// ═════════════════════════════════════════════════════════════════════════════
// 6. MiniRagPoints — B04 / B12. An enumerated card that FILLS the safe area.
//    Replaces FormACard on this reel: the shared card centres a short stack and
//    leaves the lower half empty, which Gate V correctly flags as underfill.
// ═════════════════════════════════════════════════════════════════════════════
export const miniRagPointsSchema = z.object({
  spark: z.string().default(''),
  heading: z.string().default(''),
  points: z.array(z.string()).min(2).max(4),
  labels: z.array(z.string()).default([]),
  credit: z.string().default(''),
});
export type MiniRagPointsProps = z.infer<typeof miniRagPointsSchema>;

export const MiniRagPoints: React.FC<MiniRagPointsProps> = ({
  spark, heading, points, labels, credit,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;

  const headIn = win(t, 0.04, 0.14);
  const top = heading ? 262 : 196;
  const bottom = CH - SY - 34;
  const rowH = (bottom - top) / points.length;
  const bodySize = points.length <= 3 ? 72 : 58;

  return (
    <AbsoluteFill style={{ backgroundColor: BG }}>
      <SparkLine line={spark} t={t} />

      {heading ? (
        <div style={{
          position: 'absolute', left: SX, right: SX, top: 152,
          fontFamily: SERIF, fontSize: 86, fontWeight: 700, color: INK,
          letterSpacing: '-0.015em', opacity: headIn,
          transform: `translateY(${(1 - headIn) * 12}px)`,
        }}>{heading}</div>
      ) : null}

      {points.map((p, i) => {
        const o = win(t, 0.18 + i * 0.20, 0.32 + i * 0.20);
        const y = top + i * rowH;
        return (
          <React.Fragment key={i}>
            <div style={{
              position: 'absolute', left: SX, top: y + 6,
              width: 4, height: rowH - 46, background: ACC, opacity: o * 0.85,
            }} />
            {labels[i] ? (
              <div style={{
                position: 'absolute', left: SX + 34, top: y,
                fontFamily: MONO, fontSize: 30, letterSpacing: '0.10em',
                color: ACC, opacity: o,
              }}>{labels[i]}</div>
            ) : null}
            <div style={{
              position: 'absolute', left: SX + 34, right: SX,
              top: y + (labels[i] ? 52 : 0),
              fontFamily: SERIF, fontSize: bodySize, color: INK,
              lineHeight: 1.24, opacity: o,
              transform: `translateY(${(1 - o) * 10}px)`,
            }}>{p}</div>
          </React.Fragment>
        );
      })}

      <Credit text={credit} t={t} />
    </AbsoluteFill>
  );
};
