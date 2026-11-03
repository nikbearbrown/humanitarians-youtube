/**
 * GraphDb.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-graph-databases ("Graph Databases and Cypher", @HumanitariansAI).
 *
 * Same contract as JevExplainer.tsx / McpProtocol.tsx (whose stage helpers it reuses):
 * each component lays out natively for 16:9 (<Name>) and 9:16 (<Name>916) — never a
 * crop — and every motion is a pure function of progress, conformed via `durationSeconds`.
 * The toy network (Ana … Gus), the SQL and the Cypher queries are the REAL inputs and
 * outputs of the reel's evidence/graph_demo.py (Kuzu 0.11.3 + SQLite). Fraud / recs /
 * knowledge panels are illustrative and labelled so on screen. Claims: SOURCES.md.
 *
 * Portrait type follows the MCP reel's GATE T rule (floor scales with frame height):
 * serif labels 90px, sans 52px+, mono 50px+, no arrow glyphs in text.
 *
 *   GraphHook     — a web of who-knows-whom collapses into a table of id pairs
 *   GraphModel    — nodes (things) and edges (relationships) stored directly
 *   GraphJoins    — friends-of-friends-of-friends in SQL: one more join per hop
 *   GraphTraverse — hop-by-hop traversal; most of the table is never touched
 *   GraphCypher   — MATCH (a:Person)-[:FRIENDS_WITH]->(b:Person) drawn as its picture
 *   GraphDepth    — three joins vs. one *3 pattern, same real answer
 *   GraphUses     — fraud rings, recommendations, knowledge graphs
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const Canvas: React.FC<{ P: boolean; children: React.ReactNode }> = ({ P, children }) => (
  <svg width={P ? 1080 : 1920} height={P ? 1920 : 1080} style={{ position: 'absolute', left: 0, top: 0 }}>{children}</svg>
);

const Note: React.FC<{ x: number; y: number; w: number; a: number; text: string; P: boolean; align?: 'left' | 'right' | 'center'; size?: number }> = ({ x, y, w, a, text, P, align = 'left', size }) => (
  <div style={{ position: 'absolute', left: x, top: y, width: w, textAlign: align, fontFamily: SANS, fontSize: size ?? (P ? 46 : 36), color: CLAUDE.INK_SOFT, opacity: a }}>{text}</div>
);

// a line that draws from (x1,y1) to (x2,y2) as d goes 0 → 1, optional arrowhead at the end
const Edge: React.FC<{ x1: number; y1: number; x2: number; y2: number; d: number; color?: string; w?: number; o?: number; dash?: string; head?: boolean; trim?: number }> = ({ x1, y1, x2, y2, d, color = CLAUDE.INK_SOFT, w = 5, o = 1, dash, head, trim = 0 }) => {
  if (d <= 0) return null;
  const L = Math.hypot(x2 - x1, y2 - y1) || 1, ux = (x2 - x1) / L, uy = (y2 - y1) / L;
  const sx = x1 + ux * trim, sy = y1 + uy * trim, ex = x2 - ux * trim, ey = y2 - uy * trim;
  const cx = sx + (ex - sx) * d, cy = sy + (ey - sy) * d;
  const hs = w * 4.2;
  return (
    <g opacity={o}>
      <line x1={sx} y1={sy} x2={cx} y2={cy} stroke={color} strokeWidth={w} strokeDasharray={dash} strokeLinecap="round" />
      {head && d > 0.98 && (
        <polygon fill={color} points={`${ex},${ey} ${ex - ux * hs - uy * hs * 0.6},${ey - uy * hs + ux * hs * 0.6} ${ex - ux * hs + uy * hs * 0.6},${ey - uy * hs - ux * hs * 0.6}`} />
      )}
    </g>
  );
};

// a person node: circle + name, drawn in SVG so edges can trim to its rim
const Node: React.FC<{ x: number; y: number; r: number; a: number; label: string; font: number; hot?: number; dim?: boolean }> = ({ x, y, r, a, label, font, hot = 0, dim }) => (
  <g opacity={a}>
    <circle cx={x} cy={y} r={r} fill={hot > 0.5 ? ACC_TEXT : CLAUDE.CARD} stroke={hot > 0.5 ? ACC_TEXT : dim ? CLAUDE.GHOST : CLAUDE.INK} strokeWidth={4} />
    <text x={x} y={y + font * 0.34} textAnchor="middle" fontFamily={SERIF} fontSize={font} fill={hot > 0.5 ? CLAUDE.CARD : CLAUDE.INK}>{label}</text>
  </g>
);

// the toy network from evidence/graph_demo.py
const PEOPLE = ['Ana', 'Ben', 'Cai', 'Dev', 'Eli', 'Fay', 'Gus'];
const FRIENDS: [string, string][] = [['Ana', 'Ben'], ['Ana', 'Cai'], ['Ben', 'Dev'], ['Cai', 'Eli'], ['Dev', 'Fay'], ['Eli', 'Fay'], ['Fay', 'Gus']];

// ===========================================================================
// GraphHook — who-knows-whom as a web, then squeezed into a table of id pairs
// ===========================================================================
export const graphHookSchema = z.object({
  title: z.string().default('Some data is relationships'),
  tableName: z.string().default('friendships'),
  cols: z.array(z.string()).default(['person_id', 'friend_id']),
  sparkLine: z.string().default('Why force it into rows?'),
  durationSeconds: z.number().optional(),
});
export const graphHookMeta = durMeta(5);
export const GraphHook: React.FC<z.infer<typeof graphHookSchema>> = ({ title, tableName, cols, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const nodesIn = ease(ramp(t, 0.03, 0.12));
  const squash = ease(ramp(t, 0.5, 0.64));
  const tableIn = ease(ramp(t, 0.52, 0.62));
  // web: six people, five 'knows' + one 'paid'
  const names = ['Ana', 'Ben', 'Cai', 'Dev', 'Eli', 'Fay'];
  const links: [number, number, string][] = [[0, 1, 'knows'], [0, 2, 'knows'], [1, 3, 'knows'], [2, 4, 'knows'], [3, 5, 'knows'], [4, 5, 'paid']];
  const W = P ? { x: S.x, y: 290, w: S.w, h: 470 } : { x: S.x, y: 250, w: 900, h: 680 };
  const pts = [[0.12, 0.5], [0.38, 0.15], [0.38, 0.85], [0.66, 0.2], [0.66, 0.8], [0.9, 0.5]].map(([u, v]) => ({ x: W.x + u * W.w, y: W.y + v * W.h }));
  const r = P ? 58 : 62, font = P ? 46 : 46;
  const T = P ? { x: S.x + 90, y: 800, w: S.w - 180 } : { x: S.x + 1000, y: 260, w: S.w - 1000 };
  const rowH = P ? 56 : 82, fontT = P ? 52 : 50;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P={P}>
        {links.map(([i, j, lab], k) => {
          const d = ease(ramp(t, 0.14 + k * 0.05, 0.24 + k * 0.05));
          const paid = lab === 'paid';
          return <Edge key={k} x1={pts[i].x} y1={pts[i].y} x2={pts[j].x} y2={pts[j].y} d={d} trim={r} head
            color={paid ? ACC_TEXT : CLAUDE.INK} w={5} o={1 - squash * 0.75} dash={squash > 0.5 ? '10 14' : undefined} />;
        })}
        {names.map((n, i) => <Node key={n} x={pts[i].x} y={pts[i].y} r={r} a={nodesIn * (1 - squash * 0.55)} label={n} font={font} />)}
        {links.map(([i, j, lab], k) => {
          const d = ease(ramp(t, 0.2 + k * 0.05, 0.28 + k * 0.05));
          // push each label outward from the web's centre so it clears the arrows and circles
          const ex = (pts[i].x + pts[j].x) / 2, ey = (pts[i].y + pts[j].y) / 2;
          const dx = pts[j].x - pts[i].x, dy = pts[j].y - pts[i].y, dl = Math.hypot(dx, dy) || 1;
          let nx = -dy / dl, ny = dx / dl;   // edge normal, flipped to point away from the centre
          if (nx * (ex - (W.x + W.w / 2)) + ny * (ey - (W.y + W.h / 2)) < 0) { nx = -nx; ny = -ny; }
          // clear the line by the label box's extent along the normal (+ a gap)
          const fs = P ? 44 : 42, halfW = lab.length * fs * 0.28, halfH = fs * 0.42;
          const off = halfW * Math.abs(nx) + halfH * Math.abs(ny) + 14;
          const mx = ex + nx * off, my = ey + ny * off + fs * 0.35;
          return <text key={`l${k}`} x={mx} y={my} textAnchor="middle" fontFamily={SANS} fontSize={P ? 44 : 42}
            fill={lab === 'paid' ? ACC_TEXT : CLAUDE.INK_SOFT} opacity={d * (1 - squash)} stroke={CLAUDE.PAGE} strokeWidth={10} paintOrder="stroke">{lab}</text>;
        })}
      </Canvas>
      <Card style={{ left: T.x, top: T.y, width: T.w, padding: P ? '20px 34px' : '26px 40px', opacity: tableIn, transform: `translateY(${(1 - tableIn) * 30}px)` }}>
        <div style={{ fontFamily: MONO, fontSize: fontT, color: CLAUDE.INK, fontWeight: 700, marginBottom: 10 }}>{tableName}</div>
        <div style={{ display: 'flex', fontFamily: MONO, fontSize: P ? 50 : 44, color: CLAUDE.INK_SOFT, borderBottom: `3px solid ${CLAUDE.BORDER}`, paddingBottom: 8 }}>
          {cols.map((c) => <span key={c} style={{ flex: 1 }}>{c}</span>)}
        </div>
        {links.map(([i, j], k) => (
          <div key={k} style={{ display: 'flex', height: rowH, alignItems: 'center', fontFamily: MONO, fontSize: fontT, color: CLAUDE.INK, opacity: ease(ramp(t, 0.56 + k * 0.03, 0.62 + k * 0.03)) }}>
            <span style={{ flex: 1 }}>{i + 1}</span><span style={{ flex: 1 }}>{j + 1}</span>
          </div>
        ))}
      </Card>
      <Spark st={st} text={sparkLine} at={0.8} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GraphModel — node = a thing, edge = a relationship, both stored as data
// ===========================================================================
export const graphModelSchema = z.object({
  title: z.string().default('Nodes and edges, stored'),
  a: z.string().default('Ana'),
  b: z.string().default('Ben'),
  label: z.string().default(':Person'),
  rel: z.string().default('FRIENDS_WITH'),
  keyNode: z.string().default('node: a thing'),
  keyEdge: z.string().default('edge: a relationship, stored as data'),
  sparkLine: z.string().default('Links are data.'),
  durationSeconds: z.number().optional(),
});
export const graphModelMeta = durMeta(5);
export const GraphModel: React.FC<z.infer<typeof graphModelSchema>> = ({ title, a, b, label, rel, keyNode, keyEdge, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const aIn = ease(ramp(t, 0.04, 0.14));
  const bIn = ease(ramp(t, 0.2, 0.3));
  const eIn = ease(ramp(t, 0.36, 0.5));
  const keyIn = ease(ramp(t, 0.56, 0.66));
  const pulse = ramp(t, 0.7, 0.8);
  const R = P ? 140 : 190;
  const A = P ? { x: 540, y: 440 } : { x: S.x + 280, y: 470 };
  const B = P ? { x: 540, y: 890 } : { x: S.r - 280, y: 470 };
  const nf = P ? 90 : 92;
  const relX = (A.x + B.x) / 2, relY = (A.y + B.y) / 2;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P={P}>
        <Edge x1={A.x} y1={A.y} x2={B.x} y2={B.y} d={eIn} trim={R + 6} head color={pulse > 0 ? ACC_TEXT : CLAUDE.INK} w={8} />
        {[{ p: A, n: a, s: aIn }, { p: B, n: b, s: bIn }].map(({ p, n, s }) => (
          <g key={n} opacity={s}>
            <circle cx={p.x} cy={p.y} r={R} fill={CLAUDE.CARD} stroke={CLAUDE.INK} strokeWidth={5} />
            <text x={p.x} y={p.y + 4} textAnchor="middle" fontFamily={SERIF} fontSize={nf} fill={CLAUDE.INK}>{n}</text>
            <text x={p.x} y={p.y + (P ? 80 : 70)} textAnchor="middle" fontFamily={MONO} fontSize={P ? 52 : 44} fill={CLAUDE.INK_SOFT}>{label}</text>
          </g>
        ))}
      </Canvas>
      <div style={{
        position: 'absolute', left: relX - (P ? 300 : 280), width: P ? 600 : 560, top: relY - (P ? 50 : 112), textAlign: 'center', opacity: eIn,
      }}>
        <span style={{ display: 'inline-block', padding: '10px 26px', borderRadius: 999, background: CLAUDE.CARD, border: `3px solid ${ACC_TEXT}`, fontFamily: MONO, fontSize: P ? 54 : 50, color: ACC_TEXT, fontWeight: 700 }}>{rel}</span>
      </div>
      <div style={{ position: 'absolute', left: S.x, width: S.w, top: P ? 1080 : 760, display: 'flex', flexDirection: P ? 'column' : 'row', justifyContent: 'center', alignItems: 'center', gap: P ? 18 : 60, opacity: keyIn }}>
        <Card style={{ position: 'relative', padding: P ? '14px 30px' : '16px 34px', fontFamily: SANS, fontSize: P ? 54 : 54, color: CLAUDE.INK }}>{keyNode}</Card>
        <Card accent style={{ position: 'relative', padding: P ? '14px 30px' : '16px 34px', fontFamily: SANS, fontSize: P ? 54 : 54, color: CLAUDE.INK }}>{keyEdge}</Card>
      </div>
      <Spark st={st} text={sparkLine} at={0.82} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GraphJoins — the SQL for friends-of-friends-of-friends: one more join per hop
// ===========================================================================
export const graphJoinsSchema = z.object({
  title: z.string().default('In SQL, every hop is a join'),
  // the real query from evidence/graph_demo.py (SELECT/WHERE trimmed to the hop lines)
  lines: z.array(z.object({ code: z.string(), on: z.string(), hop: z.string() })).default([
    { code: 'FROM friendships f1', on: '', hop: 'hop 1' },
    { code: 'JOIN friendships f2', on: 'ON f2.person_id = f1.friend_id', hop: 'hop 2' },
    { code: 'JOIN friendships f3', on: 'ON f3.person_id = f2.friend_id', hop: 'hop 3' },
  ]),
  head: z.string().default('SELECT DISTINCT p.name'),
  counterLabel: z.string().default('hops = joins of the same table'),
  note: z.string().default('real query · evidence/graph_demo.py (abridged)'),
  sparkLine: z.string().default('Join, join, join.'),
  durationSeconds: z.number().optional(),
});
export const graphJoinsMeta = durMeta(5);
export const GraphJoins: React.FC<z.infer<typeof graphJoinsSchema>> = ({ title, lines, head, counterLabel, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cardIn = ease(ramp(t, 0.02, 0.1));
  const lineAt = (i: number) => 0.08 + i * 0.16;
  const count = lines.filter((_, i) => t >= lineAt(i) + 0.06).length;
  const C = P ? { x: S.x, y: 290, w: S.w, h: 600 } : { x: S.x, y: 260, w: 1260, h: 620 };
  const K = P ? { x: S.x, y: 925, w: S.w, h: 190 } : { x: S.x + 1310, y: 260, w: S.w - 1310, h: 620 };
  const code = P ? 54 : 54;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: C.x, top: C.y, width: C.w, height: C.h, padding: P ? '28px 32px' : '34px 44px', opacity: cardIn }}>
        <div style={{ fontFamily: MONO, fontSize: code, color: CLAUDE.INK_SOFT, marginBottom: P ? 24 : 22 }}>{head}</div>
        {lines.map((l, i) => {
          const a = ease(ramp(t, lineAt(i), lineAt(i) + 0.08));
          const hot = i === count - 1 && i > 0;
          return (
            <div key={i} style={{ opacity: a, transform: `translateX(${(1 - a) * 30}px)`, marginBottom: P ? 30 : 40, borderLeft: `8px solid ${hot ? CLAUDE.SPARK : CLAUDE.BORDER}`, paddingLeft: 24 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ fontFamily: MONO, fontSize: code, color: CLAUDE.INK, fontWeight: i > 0 ? 700 : 400 }}>{l.code}</span>
                <span style={{ fontFamily: SANS, fontSize: P ? 52 : 40, color: CLAUDE.INK_SOFT, padding: '4px 20px', borderRadius: 999, background: CLAUDE.PILL }}>{l.hop}</span>
              </div>
              {l.on && <div style={{ fontFamily: MONO, fontSize: P ? 46 : 44, color: CLAUDE.INK_SOFT, marginTop: 8 }}>{l.on}</div>}
            </div>
          );
        })}
      </Card>
      <Card accent style={{
        left: K.x, top: K.y, width: K.w, height: K.h, opacity: cardIn, display: 'flex', flexDirection: P ? 'row' : 'column',
        alignItems: 'center', justifyContent: 'center', gap: P ? 30 : 20, textAlign: 'center', padding: '0 24px',
      }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 130 : 200, color: ACC_TEXT, lineHeight: 1 }}>{count}</span>
        <span style={{ fontFamily: SANS, fontSize: P ? 52 : 46, color: CLAUDE.INK, lineHeight: 1.15, maxWidth: P ? 640 : 360 }}>{counterLabel}</span>
      </Card>
      <Note P={P} x={S.x} y={P ? K.y + K.h + 16 : C.y + C.h + 18} w={P ? S.w : C.w} a={cardIn} text={note} />
      <Spark st={st} text={sparkLine} at={0.82} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GraphTraverse — follow stored edges hop by hop; the rest is never touched
// ===========================================================================
export const graphTraverseSchema = z.object({
  title: z.string().default('A graph follows the edges'),
  hopLabel: z.string().default('hop'),
  restLabel: z.string().default('everyone else: never touched'),
  visitedLabel: z.string().default('visited'),
  note: z.string().default('illustrative · toy network from evidence/graph_demo.py'),
  sparkLine: z.string().default('Follow, don’t search.'),
  durationSeconds: z.number().optional(),
});
export const graphTraverseMeta = durMeta(5);
export const GraphTraverse: React.FC<z.infer<typeof graphTraverseSchema>> = ({ title, hopLabel, restLabel, visitedLabel, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const hopOf: Record<string, number> = { Ana: 0, Ben: 1, Cai: 1, Dev: 2, Eli: 2, Fay: 3, Gus: 4 };
  const lane: Record<string, number> = { Ana: 0.5, Ben: 0.22, Cai: 0.78, Dev: 0.22, Eli: 0.78, Fay: 0.5, Gus: 0.5 };
  const hopAt = (h: number) => 0.14 + (h - 1) * 0.16;    // hop h lights at this t
  const inT = ease(ramp(t, 0.02, 0.1));
  const G = P ? { x: S.x, y: 290, w: S.w, h: 560 } : { x: S.x, y: 250, w: 1300, h: 600 };
  const pos = (n: string) => {
    const h = hopOf[n] / 4, l = lane[n];
    return { x: G.x + 80 + h * (G.w - 160), y: G.y + 60 + l * (G.h - 120) };
  };
  const r = P ? 64 : 70;
  const lit = (n: string) => (hopOf[n] === 0 ? (t > 0.08 ? 1 : 0) : hopOf[n] <= 3 && t >= hopAt(hopOf[n]) + 0.06 ? 1 : 0);
  const visited = PEOPLE.filter((n) => lit(n)).length;
  // "the rest of the table": a block of grey dots that never lights
  const restIn = ease(ramp(t, 0.6, 0.7));
  const R = P ? { x: S.x, y: 990, w: S.w, h: 80 } : { x: S.x + 1360, y: 260, w: S.w - 1360, h: 380 };
  const dots = Array.from({ length: P ? 36 : 40 });
  const cols = P ? 18 : 8;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P={P}>
        {FRIENDS.map(([a, b], k) => {
          const p = pos(a), q = pos(b), h = hopOf[b];
          const d = h <= 3 ? ease(ramp(t, hopAt(h) - 0.04, hopAt(h) + 0.06)) : 0;
          return (
            <g key={k}>
              <Edge x1={p.x} y1={p.y} x2={q.x} y2={q.y} d={inT} trim={r} head color={CLAUDE.BORDER} w={5} />
              <Edge x1={p.x} y1={p.y} x2={q.x} y2={q.y} d={d} trim={r} head color={ACC_TEXT} w={7} />
            </g>
          );
        })}
        {PEOPLE.map((n) => { const p = pos(n); return <Node key={n} x={p.x} y={p.y} r={r} a={inT} label={n} font={P ? 54 : 46} hot={lit(n)} dim={hopOf[n] === 4} />; })}
        {[1, 2, 3].map((h) => {
          const p = { x: G.x + 80 + (h / 4) * (G.w - 160), y: G.y + G.h + (P ? 40 : 30) };
          return <text key={h} x={p.x} y={p.y} textAnchor="middle" fontFamily={SANS} fontSize={P ? 52 : 42}
            fill={CLAUDE.INK_SOFT} opacity={ease(ramp(t, hopAt(h), hopAt(h) + 0.06))}>{`${hopLabel} ${h}`}</text>;
        })}
        {dots.map((_, i) => (
          <circle key={i} cx={R.x + 30 + (i % cols) * ((R.w - 60) / (cols - 1))} cy={R.y + 26 + Math.floor(i / cols) * (P ? 56 : 58)}
            r={P ? 14 : 16} fill="none" stroke={CLAUDE.GHOST} strokeWidth={4} opacity={restIn} />
        ))}
      </Canvas>
      <div style={{ position: 'absolute', left: R.x, width: R.w, top: P ? R.y + R.h + 34 : R.y + R.h - 10, textAlign: 'center', fontFamily: SANS, fontSize: P ? 52 : 42, color: CLAUDE.INK_SOFT, opacity: restIn, lineHeight: 1.15 }}>{restLabel}</div>
      <Card accent style={{
        left: P ? S.x : R.x, top: P ? R.y + R.h + 110 : R.y + R.h + 110, width: P ? S.w : R.w, padding: '14px 24px', textAlign: 'center', opacity: restIn,
        fontFamily: SANS, fontSize: P ? 56 : 46, color: CLAUDE.INK,
      }}>{visitedLabel} <span style={{ fontFamily: SERIF, color: ACC_TEXT, fontSize: P ? 80 : 64 }}>{visited}</span> people</Card>
      <Note P={P} x={S.x} y={P ? 905 : 196} w={S.w} a={inT} align={P ? 'center' : 'right'} text={P ? note.split(' from ')[0] : note} />
      <Spark st={st} text={sparkLine} at={0.84} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GraphCypher — the query is a drawing: (node)-[:REL]->(node)
// ===========================================================================
export const graphCypherSchema = z.object({
  title: z.string().default('Cypher draws the pattern'),
  a: z.string().default('(a:Person)'),
  rel: z.string().default('-[:FRIENDS_WITH]->'),
  b: z.string().default('(b:Person)'),
  ret: z.string().default('RETURN b'),
  result: z.array(z.string()).default(['Ben', 'Cai']),
  resultHead: z.string().default("result, for a = Ana"),
  note: z.string().default('real output · Kuzu 0.11.3 · toy network'),
  sparkLine: z.string().default('Draw it, match it.'),
  durationSeconds: z.number().optional(),
});
export const graphCypherMeta = durMeta(5);
export const GraphCypher: React.FC<z.infer<typeof graphCypherSchema>> = ({ title, a, rel, b, ret, result, resultHead, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const qIn = ease(ramp(t, 0.03, 0.12));
  const hiA = ramp(t, 0.22, 0.26) * (1 - ramp(t, 0.4, 0.42));
  const hiR = ramp(t, 0.4, 0.42) * (1 - ramp(t, 0.54, 0.56));
  const hiB = ramp(t, 0.54, 0.56) * (1 - ramp(t, 0.68, 0.7));
  const dA = ease(ramp(t, 0.22, 0.32)), dR = ease(ramp(t, 0.4, 0.52)), dB = ease(ramp(t, 0.54, 0.64));
  const resIn = ease(ramp(t, 0.7, 0.8));
  const code = P ? 60 : 56;
  const tok = (s: string, hi: number) => (
    <span style={{ color: hi > 0.5 ? ACC_TEXT : CLAUDE.INK, borderBottom: `6px solid ${hi > 0.5 ? ACC_TEXT : 'transparent'}` }}>{s}</span>
  );
  // the drawing under the query
  const r = P ? 105 : 110;
  const A = P ? { x: 290, y: 860 } : { x: S.x + 300, y: 640 };
  const B = P ? { x: 790, y: 860 } : { x: S.x + 1020, y: 640 };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: S.x, top: P ? 290 : 250, width: S.w, padding: P ? '22px 34px' : '26px 40px', opacity: qIn, fontFamily: MONO, fontSize: code, lineHeight: P ? 1.3 : 1.35 }}>
        {P ? (
          <>
            <div><span style={{ color: CLAUDE.INK_SOFT }}>MATCH </span>{tok(a, hiA)}</div>
            <div>{tok(rel, hiR)}</div>
            <div>{tok(b, hiB)}</div>
            <div style={{ color: CLAUDE.INK_SOFT }}>{ret}</div>
          </>
        ) : (
          <>
            <div><span style={{ color: CLAUDE.INK_SOFT }}>MATCH </span>{tok(a, hiA)}{tok(rel, hiR)}{tok(b, hiB)}</div>
            <div style={{ color: CLAUDE.INK_SOFT }}>{ret}</div>
          </>
        )}
      </Card>
      <Canvas P={P}>
        <Edge x1={A.x} y1={A.y} x2={B.x} y2={B.y} d={dR} trim={r + 6} head color={hiR > 0.5 ? ACC_TEXT : CLAUDE.INK} w={8} />
        {[{ p: A, d: dA, hi: hiA, n: 'a' }, { p: B, d: dB, hi: hiB, n: 'b' }].map(({ p, d, hi, n }) => (
          <g key={n} opacity={d}>
            <circle cx={p.x} cy={p.y} r={r} fill={CLAUDE.CARD} stroke={hi > 0.5 ? ACC_TEXT : CLAUDE.INK} strokeWidth={6} />
            <text x={p.x} y={p.y + 30} textAnchor="middle" fontFamily={SERIF} fontSize={P ? 96 : 88} fill={CLAUDE.INK}>{n}</text>
          </g>
        ))}
        <text x={(A.x + B.x) / 2} y={A.y - (P ? r + 22 : 34)} textAnchor="middle" fontFamily={MONO} fontSize={P ? 50 : 42} fill={CLAUDE.INK_SOFT} opacity={dR}>FRIENDS_WITH</text>
        <text x={A.x} y={A.y + r + (P ? 66 : 56)} textAnchor="middle" fontFamily={SANS} fontSize={P ? 52 : 42} fill={CLAUDE.INK_SOFT} opacity={dA}>Person</text>
        <text x={B.x} y={B.y + r + (P ? 66 : 56)} textAnchor="middle" fontFamily={SANS} fontSize={P ? 52 : 42} fill={CLAUDE.INK_SOFT} opacity={dB}>Person</text>
      </Canvas>
      <Card accent style={{
        left: P ? S.x : S.x + 1260, top: P ? 1060 : 470, width: P ? S.w : S.w - 1260, padding: P ? '18px 30px' : '26px 34px', opacity: resIn,
      }}>
        <div style={{ fontFamily: SANS, fontSize: P ? 50 : 38, color: CLAUDE.INK_SOFT, marginBottom: 10 }}>{resultHead}</div>
        <div style={{ display: 'flex', flexDirection: P ? 'row' : 'column', gap: P ? 40 : 8 }}>
          {result.map((n) => <div key={n} style={{ fontFamily: MONO, fontSize: P ? 64 : 60, color: CLAUDE.INK, fontWeight: 700 }}>{n}</div>)}
        </div>
      </Card>
      <Note P={P} x={P ? S.x : S.x + 1260} y={P ? 1250 : 800} w={P ? S.w : S.w - 1260} a={resIn} text={note} />
      <Spark st={st} text={sparkLine} at={0.84} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GraphDepth — three joins vs. one variable-length pattern, same real answer
// ===========================================================================
export const graphDepthSchema = z.object({
  title: z.string().default('Three hops, one pattern'),
  sqlHead: z.string().default('SQL'),
  sql: z.array(z.string()).default(['FROM friendships f1', 'JOIN friendships f2 …', 'JOIN friendships f3 …', 'JOIN people p …']),
  cyHead: z.string().default('Cypher'),
  cypher: z.array(z.string()).default(["MATCH (a:Person {name:'Ana'})", '-[:FRIENDS_WITH*3]->', '(c:Person)', 'RETURN DISTINCT c.name']),
  star: z.string().default('*3'),
  answer: z.string().default('Fay'),
  verdict: z.string().default('same answer · 3 joins vs 1 pattern'),
  note: z.string().default('real output · SQLite 3.53 and Kuzu 0.11.3 · same toy data'),
  sparkLine: z.string().default('Depth is a number.'),
  durationSeconds: z.number().optional(),
});
export const graphDepthMeta = durMeta(5);
export const GraphDepth: React.FC<z.infer<typeof graphDepthSchema>> = ({ title, sqlHead, sql, cyHead, cypher, star, answer, verdict, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const lIn = ease(ramp(t, 0.03, 0.12));
  const rIn = ease(ramp(t, 0.28, 0.38));
  const ans = ease(ramp(t, 0.58, 0.66));
  const vIn = ease(ramp(t, 0.68, 0.76));
  const colW = P ? S.w : (S.w - 60) / 2;
  const L = P ? { x: S.x, y: 290, h: 485 } : { x: S.x, y: 250, h: 600 };
  const R = P ? { x: S.x, y: 795, h: 485 } : { x: S.x + colW + 60, y: 250, h: 600 };
  const code = P ? 50 : 46;
  // portrait: the answer sits under the code (no room beside it); the verdict becomes the spark line
  const Ans: React.FC<{ a: number }> = ({ a }) => (
    <div style={{ ...(P ? { marginTop: 6 } : { position: 'absolute', right: 30, bottom: 24 }), opacity: a, display: 'flex', alignItems: 'baseline', gap: 18 }}>
      <span style={{ fontFamily: SANS, fontSize: P ? 52 : 40, color: CLAUDE.INK_SOFT }}>result</span>
      <span style={{ fontFamily: MONO, fontSize: P ? 70 : 64, color: CLAUDE.INK, fontWeight: 700 }}>{answer}</span>
    </div>
  );
  const starred = (l: string) => {
    const i = l.indexOf(star);
    if (i < 0) return l;
    return <>{l.slice(0, i)}<span style={{ color: ACC_TEXT, fontWeight: 700, borderBottom: `6px solid ${CLAUDE.SPARK}` }}>{star}</span>{l.slice(i + star.length)}</>;
  };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: L.x, top: L.y, width: colW, height: L.h, padding: P ? '22px 30px' : '30px 38px', opacity: lIn }}>
        <div style={{ fontFamily: SANS, fontSize: P ? 52 : 40, color: CLAUDE.INK_SOFT, marginBottom: P ? 6 : 14 }}>{sqlHead}{P ? ' · real output' : ''}</div>
        {sql.map((l, i) => (
          <div key={i} style={{ fontFamily: MONO, fontSize: code, color: CLAUDE.INK, lineHeight: P ? 1.3 : 1.5, fontWeight: l.startsWith('JOIN') ? 700 : 400, opacity: ease(ramp(t, 0.05 + i * 0.05, 0.12 + i * 0.05)) }}>{l}</div>
        ))}
        <Ans a={ans} />
      </Card>
      <Card accent={vIn > 0.5} style={{ left: R.x, top: R.y, width: colW, height: R.h, padding: P ? '22px 30px' : '30px 38px', opacity: rIn }}>
        <div style={{ fontFamily: SANS, fontSize: P ? 52 : 40, color: CLAUDE.INK_SOFT, marginBottom: P ? 6 : 14 }}>{cyHead}{P ? ' · real output' : ''}</div>
        {cypher.map((l, i) => (
          <div key={i} style={{ fontFamily: MONO, fontSize: code, color: CLAUDE.INK, lineHeight: P ? 1.3 : 1.5 }}>{starred(l)}</div>
        ))}
        <Ans a={ans} />
      </Card>
      {!P && <div style={{ position: 'absolute', left: S.x, width: S.w, top: 880, textAlign: 'center', fontFamily: SERIF, fontSize: 58, color: CLAUDE.INK, opacity: vIn, lineHeight: 1.15 }}>{verdict}</div>}
      {!P && <Note P={P} x={S.x} y={196} w={S.w} a={lIn} align="right" text={note} />}
      <Spark st={st} text={P ? 'Three joins, one pattern.' : sparkLine} at={P ? 0.7 : 0.86} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GraphUses — fraud rings, recommendations, knowledge graphs (illustrative)
// ===========================================================================
export const graphUsesSchema = z.object({
  title: z.string().default('Where graphs win'),
  labels: z.array(z.string()).default(['Fraud rings', 'Recommendations', 'Knowledge graphs']),
  note: z.string().default('illustrative'),
  sparkLine: z.string().default('Connections are the data.'),
  durationSeconds: z.number().optional(),
});
export const graphUsesMeta = durMeta(5);
export const GraphUses: React.FC<z.infer<typeof graphUsesSchema>> = ({ title, labels, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const gap = P ? 24 : 40;
  const pw = P ? S.w : (S.w - 2 * gap) / 3;
  const ph = P ? 310 : 600;
  const top = P ? 290 : 260;
  const at = [0.04, 0.38, 0.58];
  const panel = (i: number) => (P ? { x: S.x, y: top + i * (ph + gap) } : { x: S.x + i * (pw + gap), y: top });
  const pin = (i: number) => ease(ramp(t, at[i], at[i] + 0.08));
  const lab = P ? 48 : 40, node = P ? 56 : 40;
  // local geometry inside each panel (dx, dy are relative to the panel's drawing box)
  const box = (i: number) => {
    const p = panel(i);
    return P ? { x: p.x + 60, y: p.y + 132, w: pw - 120, h: ph - 160 } : { x: p.x + 20, y: p.y + 110, w: pw - 40, h: ph - 150 };
  };
  const at01 = (i: number, u: number, v: number) => { const b = box(i); return { x: b.x + u * b.w, y: b.y + v * b.h }; };
  // panel 1: four accounts share a phone and a device → the ring closes
  const accts = [[0.15, 0.2], [0.85, 0.2], [0.85, 0.8], [0.15, 0.8]].map(([u, v]) => at01(0, u, v));
  const phone = at01(0, 0.5, 0.2), device = at01(0, 0.5, 0.8);
  const ring = ease(ramp(t, 0.18, 0.32));
  // panel 2: you —bought→ book ←bought— sam —bought→ suggestion
  const you = at01(1, 0.15, 0.25), bookA = at01(1, 0.5, 0.25), sam = at01(1, 0.85, 0.25), bookB = P ? at01(1, 0.62, 0.85) : at01(1, 0.85, 0.85);
  const sug = ease(ramp(t, 0.5, 0.58));
  // panel 3: Curie —DISCOVERED→ Radium, Curie —WON→ Nobel Prize
  const curie = at01(2, 0.2, 0.5), radium = at01(2, 0.8, 0.2), nobel = at01(2, 0.8, 0.8);
  const r = P ? 50 : 46;
  const small = (x: number, y: number, label: string, a: number, hot?: boolean, minW?: number) => {
    const wide = Math.max(minW ?? r, label.length * node * 0.3 + 26);
    return (
    <g opacity={a}>
      <rect x={x - wide} y={y - r * 0.78} width={wide * 2} height={r * 1.56} rx={r * 0.78}
        fill={hot ? ACC_TEXT : CLAUDE.CARD} stroke={hot ? ACC_TEXT : CLAUDE.INK} strokeWidth={4} />
      <text x={x} y={y + node * 0.34} textAnchor="middle" fontFamily={SANS} fontSize={node} fill={hot ? CLAUDE.CARD : CLAUDE.INK}>{label}</text>
    </g>
    );
  };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {[0, 1, 2].map((i) => {
        const p = panel(i);
        return (
          <Card key={i} accent={i === 0 && ring > 0.9} style={{ left: p.x, top: p.y, width: pw, height: ph, opacity: pin(i) }}>
            <div style={{
              position: 'absolute', left: 30, top: P ? 14 : 26, width: pw - 60,
              fontFamily: SERIF, fontSize: P ? 90 : 54, color: CLAUDE.INK, lineHeight: 1.0,
            }}>{labels[i]}</div>
          </Card>
        );
      })}
      <Canvas P={P}>
        <g opacity={pin(0)}>
          {accts.map((a, k) => <Edge key={k} x1={a.x} y1={a.y} x2={k < 2 ? phone.x : device.x} y2={k < 2 ? phone.y : device.y} d={ring} trim={r} color={CLAUDE.SPARK} w={6} />)}
          {accts.map((a, k) => <Edge key={`x${k}`} x1={a.x} y1={a.y} x2={k < 2 ? device.x : phone.x} y2={k < 2 ? device.y : phone.y} d={ease(ramp(t, 0.24, 0.36))} trim={r} color={CLAUDE.SPARK} w={4} dash="10 10" />)}
          {small(phone.x, phone.y, 'phone', 1, ring > 0.9)}
          {small(device.x, device.y, P ? 'PC' : 'device', 1, ring > 0.9, P ? undefined : r * 1.5)}
          {accts.map((a, k) => small(a.x, a.y, `#${k + 1}`, 1))}
        </g>
        <g opacity={pin(1)}>
          <Edge x1={you.x} y1={you.y} x2={bookA.x} y2={bookA.y} d={pin(1)} trim={r} head color={CLAUDE.INK} />
          <Edge x1={sam.x} y1={sam.y} x2={bookA.x} y2={bookA.y} d={pin(1)} trim={r} head color={CLAUDE.INK} />
          <Edge x1={sam.x} y1={sam.y} x2={bookB.x} y2={bookB.y} d={sug} trim={r} head color={CLAUDE.INK} />
          <Edge x1={you.x} y1={you.y} x2={bookB.x} y2={bookB.y} d={sug} trim={r * 1.2} head color={CLAUDE.SPARK} w={6} dash="12 12" />
          {small(you.x, you.y, 'you', 1)}
          {small(sam.x, sam.y, 'Sam', 1)}
          {small(bookA.x, bookA.y, 'book', 1)}
          {small(bookB.x, bookB.y, 'next', sug, true)}
        </g>
        <g opacity={pin(2)}>
          <Edge x1={curie.x} y1={curie.y} x2={radium.x} y2={radium.y} d={ease(ramp(t, 0.62, 0.72))} trim={r * 1.6} head color={CLAUDE.INK} />
          <Edge x1={curie.x} y1={curie.y} x2={nobel.x} y2={nobel.y} d={ease(ramp(t, 0.66, 0.76))} trim={r * 1.6} head color={CLAUDE.INK} />
          {small(curie.x, curie.y, 'Curie', 1, false, r * 1.6)}
          {small(radium.x, radium.y, 'radium', 1, false, r * 1.7)}
          {small(nobel.x, nobel.y, 'Nobel', 1, false, r * 1.6)}
        </g>
      </Canvas>
      <Note P={P} x={S.x} y={P ? top + 3 * (ph + gap) - 10 : top + ph + 14} w={S.w} a={pin(0)} align="right" text={note} size={P ? 60 : undefined} />
      <Spark st={st} text={sparkLine} at={0.84} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
