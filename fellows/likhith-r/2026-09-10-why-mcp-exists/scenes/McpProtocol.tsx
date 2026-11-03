/**
 * McpProtocol.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-mcp-protocol ("Why MCP Exists", @HumanitariansAI).
 *
 * Same contract as JevExplainer.tsx (whose stage helpers it reuses): each component
 * lays out natively for 16:9 (<Name>) and 9:16 (<Name>916) — never a crop — and
 * every motion is a pure function of progress, conformed via `durationSeconds`.
 * Tool names, auth schemes and call arguments are illustrative and labelled so on
 * screen; the tools/list payloads in McpDiscovery / McpRuntime are the REAL output of
 * the reel's evidence/mcp_discovery.py (MCP Python SDK 2.2.0). Claims: SOURCES.md.
 *
 *   McpHook      — app ↔ API works; an agent facing many tools is the open question
 *   McpBespoke   — every API brings its own auth, format and docs → custom code each
 *   McpStandard  — 3 agents × 4 tools = 12 integrations collapse to 3 + 4 via MCP
 *   McpDiscovery — tools/list: the agent asks the server what it can do (real output)
 *   McpRuntime   — hardcoded endpoints vs. a tool list that grows at runtime
 *   McpCompose   — an agent chains three tools with one call shape
 *   McpTerminal  — analogy: each store's own checkout vs. one universal terminal
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const Note: React.FC<{ x: number; y: number; w: number; a: number; text: string; align?: 'left' | 'right' }> = ({ x, y, w, a, text, align = 'left' }) => (
  <div style={{ position: 'absolute', left: x, top: y, width: w, textAlign: align, fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT, opacity: a }}>{text}</div>
);

const Box: React.FC<{ x: number; y: number; w: number; h: number; a: number; accent?: boolean; children?: React.ReactNode; font?: number }> = ({ x, y, w, h, a, accent, children, font = 48 }) => (
  <Card accent={accent} style={{
    left: x, top: y, width: w, height: h, opacity: a, display: 'flex', flexDirection: 'column',
    alignItems: 'center', justifyContent: 'center', textAlign: 'center', fontFamily: SERIF, fontSize: font, color: CLAUDE.INK, lineHeight: 1.1,
  }}>{children}</Card>
);

const Canvas: React.FC<{ P: boolean; children: React.ReactNode }> = ({ P, children }) => (
  <svg width={P ? 1080 : 1920} height={P ? 1920 : 1080} style={{ position: 'absolute', left: 0, top: 0 }}>{children}</svg>
);

// a line that draws from (x1,y1) to (x2,y2) as d goes 0 → 1
const DrawLine: React.FC<{ x1: number; y1: number; x2: number; y2: number; d: number; color?: string; w?: number; o?: number; dash?: string }> = ({ x1, y1, x2, y2, d, color = CLAUDE.INK_SOFT, w = 4, o = 1, dash }) =>
  d <= 0 ? null : <line x1={x1} y1={y1} x2={x1 + (x2 - x1) * d} y2={y1 + (y2 - y1) * d} stroke={color} strokeWidth={w} opacity={o} strokeDasharray={dash} strokeLinecap="round" />;

// ===========================================================================
// McpHook — an app talking to one API works; an agent facing many tools is the question
// ===========================================================================
export const mcpHookSchema = z.object({
  title: z.string().default('APIs already connect software'),
  app: z.string().default('App'),
  api: z.string().default('Calendar API'),
  call: z.string().default('GET /events → 200 OK'),
  agent: z.string().default('AI agent'),
  tools: z.array(z.string()).default(['Calendar', 'Email', 'Files', 'CRM', 'Maps', 'Docs']),
  sparkLine: z.string().default('So why a new protocol?'),
  durationSeconds: z.number().optional(),
});
export const mcpHookMeta = durMeta(5);
export const McpHook: React.FC<z.infer<typeof mcpHookSchema>> = ({ title, app, api, call, agent, tools, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const pairIn = ease(ramp(t, 0.04, 0.14));
  const link = ease(ramp(t, 0.12, 0.26));
  const ok = ease(ramp(t, 0.24, 0.32));
  const agentIn = ease(ramp(t, 0.42, 0.52));
  // pair geometry
  const bw = P ? 380 : 330, bh = 170;
  const py = P ? 360 : 495;
  const ax = S.x, sx = P ? S.r - bw : S.x + 480 + 30;
  const pairR = sx + bw;
  // agent + tool ring geometry
  const cx = P ? 540 : (pairR + S.r) / 2 + 20, cy = P ? 1000 : 580;
  const R = P ? 260 : 300, rAgent = P ? 120 : 115;
  const chipW = P ? 230 : 230, chipH = 84;
  if (P) return <McpHookPortrait {...{ title, app, api, call, agent, tools, sparkLine }} />;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P={P}>
        <DrawLine x1={ax + bw} y1={py + bh / 2} x2={sx} y2={py + bh / 2} d={link} w={6} color={CLAUDE.INK} />
        {tools.map((tool, i) => {
          const a = -Math.PI / 2 + (i / tools.length) * Math.PI * 2;
          const d = ease(ramp(t, 0.5 + i * 0.04, 0.6 + i * 0.04));
          return <DrawLine key={tool} x1={cx + Math.cos(a) * rAgent} y1={cy + Math.sin(a) * rAgent}
            x2={cx + Math.cos(a) * (R - chipH / 2)} y2={cy + Math.sin(a) * (R - chipH / 2)} d={d} dash="14 12" />;
        })}
        <circle cx={cx} cy={cy} r={rAgent} fill={CLAUDE.CARD} stroke={CLAUDE.INK} strokeWidth={4} opacity={agentIn} />
      </Canvas>
      <Box x={ax} y={py} w={bw} h={bh} a={pairIn}>{app}</Box>
      <Box x={sx} y={py} w={bw} h={bh} a={pairIn}>{api}</Box>
      <div style={{
        position: 'absolute', left: ax, top: py + bh + 40, width: pairR - ax, textAlign: 'center',
        fontFamily: MONO, fontSize: P ? 44 : 40, color: CLAUDE.INK, opacity: ok,
      }}>{call} <span style={{ fontFamily: SANS, color: CLAUDE.INK_SOFT }}>✓</span></div>
      <div style={{
        position: 'absolute', left: ax, top: py + bh + 110, width: pairR - ax, textAlign: 'center',
        fontFamily: SANS, fontSize: 36, color: CLAUDE.INK_SOFT, opacity: ok,
      }}>one app, one API: solved</div>
      <div style={{
        position: 'absolute', left: cx - rAgent, top: cy - 36, width: rAgent * 2, textAlign: 'center',
        fontFamily: SERIF, fontSize: P ? 50 : 48, color: CLAUDE.INK, opacity: agentIn, lineHeight: 1,
      }}>{agent}</div>
      {tools.map((tool, i) => {
        const a = -Math.PI / 2 + (i / tools.length) * Math.PI * 2;
        const d = ease(ramp(t, 0.52 + i * 0.04, 0.62 + i * 0.04));
        const q = ease(ramp(t, 0.72, 0.8));
        return (
          <Card key={tool} style={{
            left: cx + Math.cos(a) * R - chipW / 2, top: cy + Math.sin(a) * R - chipH / 2, width: chipW, height: chipH,
            display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 14, opacity: d,
            fontFamily: SANS, fontSize: 38, color: CLAUDE.INK,
          }}>
            {tool}<span style={{ color: CLAUDE.SPARK, fontWeight: 700, opacity: q }}>?</span>
          </Card>
        );
      })}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};


// Portrait (9:16) layout: GATE T's floor scales with frame HEIGHT (72px at 3840), so every
// touching-glyph cluster must stand >= 36 logical px — serif labels 90px, sans labels 56px+,
// no arrow glyphs. Tools become a 2 × 3 grid instead of a ring so the type can stay large.
const McpHookPortrait: React.FC<z.infer<typeof mcpHookSchema>> = ({ title, app, api, call, agent, tools, sparkLine }) => {
  const st = useStage(); const { t, S } = st;
  const pairIn = ease(ramp(t, 0.04, 0.14));
  const link = ease(ramp(t, 0.12, 0.26));
  const ok = ease(ramp(t, 0.24, 0.32));
  const agentIn = ease(ramp(t, 0.42, 0.52));
  const q = ease(ramp(t, 0.72, 0.8));
  const bw = 440, bh = 150, py = 300;
  const aw = 520, ah = 140, ay = 700, ax = 540 - aw / 2;
  const cw = (S.w - 24) / 2, ch = 104, gy = 890, gg = 18;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P>
        <DrawLine x1={S.x + bw} y1={py + bh / 2} x2={S.r - bw} y2={py + bh / 2} d={link} w={6} color={CLAUDE.INK} />
        {[0, 1].map((c) => (
          <DrawLine key={c} x1={540} y1={ay + ah} x2={S.x + c * (cw + 24) + cw / 2} y2={gy}
            d={ease(ramp(t, 0.5, 0.6))} dash="14 12" />
        ))}
      </Canvas>
      <Card style={{ left: S.x, top: py, width: bw, height: bh, opacity: pairIn, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SANS, fontSize: 64, color: CLAUDE.INK }}>{app}</Card>
      <Card style={{ left: S.r - bw, top: py, width: bw, height: bh, opacity: pairIn, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SANS, fontSize: 60, color: CLAUDE.INK }}>{api}</Card>
      <div style={{ position: 'absolute', left: S.x, top: py + bh + 36, width: S.w, textAlign: 'center', fontFamily: MONO, fontSize: 60, color: CLAUDE.INK, opacity: ok }}>
        {call} <span style={{ fontFamily: SANS, color: CLAUDE.INK_SOFT }}>✓</span>
      </div>
      <div style={{ position: 'absolute', left: S.x, top: py + bh + 124, width: S.w, textAlign: 'center', fontFamily: SANS, fontSize: 56, color: CLAUDE.INK_SOFT, opacity: ok }}>
        one app, one API: solved
      </div>
      <Card style={{ left: ax, top: ay, width: aw, height: ah, borderRadius: 999, borderColor: CLAUDE.INK, opacity: agentIn, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: 90, color: CLAUDE.INK }}>{agent}</Card>
      {tools.map((tool, i) => {
        const d = ease(ramp(t, 0.52 + i * 0.04, 0.62 + i * 0.04));
        return (
          <Card key={tool} style={{
            left: S.x + (i % 2) * (cw + 24), top: gy + Math.floor(i / 2) * (ch + gg), width: cw, height: ch,
            border: `3px dashed ${CLAUDE.GHOST}`, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 18,
            opacity: d, fontFamily: SANS, fontSize: 60, color: CLAUDE.INK,
          }}>
            {tool}<span style={{ color: CLAUDE.SPARK, fontWeight: 700, opacity: q }}>?</span>
          </Card>
        );
      })}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// McpBespoke — every API has its own auth, request format and docs
// ===========================================================================
export const mcpBespokeSchema = z.object({
  title: z.string().default('Every API is different'),
  agent: z.string().default('AI agent'),
  rows: z.array(z.object({ tool: z.string(), auth: z.string(), format: z.string(), docs: z.string() })).default([
    { tool: 'Calendar', auth: 'OAuth 2.0', format: 'REST + JSON', docs: 'REST reference' },
    { tool: 'Email', auth: 'API key', format: 'GraphQL', docs: 'GraphQL schema' },
    { tool: 'Files', auth: 'bearer token', format: 'SOAP + XML', docs: 'WSDL file' },
    { tool: 'CRM', auth: 'basic auth', format: 'REST + form', docs: 'PDF manual' },
  ]),
  counterLabel: z.string().default('custom integrations'),
  note: z.string().default('illustrative tools'),
  sparkLine: z.string().default('One integration per tool.'),
  durationSeconds: z.number().optional(),
});
export const mcpBespokeMeta = durMeta(6);
export const McpBespoke: React.FC<z.infer<typeof mcpBespokeSchema>> = ({ title, agent, rows, counterLabel, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = rows.length;
  const agentIn = ease(ramp(t, 0.02, 0.1));
  const rowAt = (i: number) => 0.1 + i * 0.13;
  const count = rows.filter((_, i) => t >= rowAt(i) + 0.08).length;
  // columns: auth / format / docs land in narration order across each row
  const colA = (i: number, c: number) => ease(ramp(t, rowAt(i) + 0.02 + c * 0.025, rowAt(i) + 0.08 + c * 0.025));
  if (P) {
    // Portrait: GATE T floor is 72px at 3840 → serif names 90px, chips 50px sans (short
    // labels via the vertical sheet), the counter sentence on its own card.
    const cTop = 318, cH = 150;
    const top = cTop + cH + 26, rowH = 180, gap = 14;
    const chipW = (S.w - 40 - 2 * 12) / 3;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
        <Title st={st} text={title} />
        <Card style={{ left: S.x, top: cTop, width: S.w, height: cH, opacity: agentIn, display: 'flex', alignItems: 'center', gap: 28, padding: '0 32px' }}>
          <span style={{ fontFamily: SERIF, fontSize: 130, color: CLAUDE.SPARK, lineHeight: 1 }}>{count}</span>
          <span style={{ fontFamily: SANS, fontSize: 60, color: CLAUDE.INK, lineHeight: 1.05 }}>{counterLabel}</span>
        </Card>
        {rows.map((r, i) => {
          const a = ease(ramp(t, rowAt(i), rowAt(i) + 0.06));
          return (
            <Card key={r.tool} style={{ left: S.x, top: top + i * (rowH + gap), width: S.w, height: rowH, padding: '8px 20px', opacity: a }}>
              <div style={{ fontFamily: SERIF, fontSize: 90, color: CLAUDE.INK, lineHeight: 0.95 }}>{r.tool}</div>
              <div style={{ display: 'flex', gap: 12, marginTop: 6 }}>
                {[r.auth, r.format, r.docs].map((v, c) => (
                  <div key={c} style={{
                    width: chipW, padding: '2px 0', borderRadius: 999, background: CLAUDE.PILL, textAlign: 'center',
                    fontFamily: SANS, fontSize: 50, color: CLAUDE.INK, opacity: colA(i, c), whiteSpace: 'nowrap',
                  }}>{v}</div>
                ))}
              </div>
            </Card>
          );
        })}
        <Note x={S.x} y={top + rows.length * (rowH + gap) - 6} w={S.w} a={agentIn} align="right" text={note} />
        <Spark st={st} text={sparkLine} />
        <Bug st={st} />
      </AbsoluteFill>
    );
  }
  const aX = S.x, aW = 300, top = 290, rowH = 128, gap = 24;
  const aH = n * rowH + (n - 1) * gap;
  const rX = aX + aW + 110, rW = S.r - rX;
  const nameW = 250, chipW = (rW - nameW - 48 - 3 * 20) / 3;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P={P}>
        {rows.map((r, i) => (
          <DrawLine key={r.tool} x1={aX + aW} y1={top + aH / 2} x2={rX} y2={top + i * (rowH + gap) + rowH / 2}
            d={ease(ramp(t, rowAt(i), rowAt(i) + 0.06))} />
        ))}
      </Canvas>
      <Card style={{
        left: aX, top, width: aW, height: aH, opacity: agentIn, display: 'flex', flexDirection: 'column',
        alignItems: 'center', justifyContent: 'center', gap: 30, textAlign: 'center',
      }}>
        <span style={{ fontFamily: SERIF, fontSize: 56, color: CLAUDE.INK }}>{agent}</span>
        <span style={{ fontFamily: SERIF, fontSize: 150, color: CLAUDE.SPARK, lineHeight: 1 }}>{count}</span>
        <span style={{ fontFamily: SANS, fontSize: 36, color: CLAUDE.INK_SOFT, width: 240, lineHeight: 1.15 }}>{counterLabel}</span>
      </Card>
      {['auth', 'request format', 'docs'].map((h, c) => (
        <div key={h} style={{
          position: 'absolute', left: rX + 24 + nameW + c * (chipW + 20), top: top - 58, width: chipW, textAlign: 'center',
          fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT, opacity: agentIn,
        }}>{h}</div>
      ))}
      {rows.map((r, i) => {
        const a = ease(ramp(t, rowAt(i), rowAt(i) + 0.06));
        return (
          <Card key={r.tool} style={{
            left: rX, top: top + i * (rowH + gap), width: rW, height: rowH, padding: '0 24px', opacity: a,
            display: 'flex', alignItems: 'center', gap: 20,
          }}>
            <span style={{ width: nameW - 20, fontFamily: SERIF, fontSize: 52, color: CLAUDE.INK }}>{r.tool}</span>
            {[r.auth, r.format, r.docs].map((v, c) => (
              <span key={c} style={{
                width: chipW, padding: '14px 0', borderRadius: 999, background: CLAUDE.PILL, textAlign: 'center',
                fontFamily: SANS, fontSize: 38, color: CLAUDE.INK, opacity: colA(i, c), whiteSpace: 'nowrap',
              }}>{v}</span>
            ))}
          </Card>
        );
      })}
      <Note x={rX} y={top + aH + 18} w={rW} a={agentIn} align="right" text={note} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// McpStandard — N × M custom integrations collapse to N + M through one protocol
// ===========================================================================
export const mcpStandardSchema = z.object({
  title: z.string().default('One protocol in the middle'),
  agents: z.array(z.string()).default(['Agent A', 'Agent B', 'Agent C']),
  tools: z.array(z.string()).default(['Calendar', 'Email', 'Files', 'CRM']),
  protocol: z.string().default('MCP'),
  serverTag: z.string().default('MCP server'),
  sparkLine: z.string().default('Build once. Reuse everywhere.'),
  durationSeconds: z.number().optional(),
});
export const mcpStandardMeta = durMeta(6);
export const McpStandard: React.FC<z.infer<typeof mcpStandardSchema>> = ({ title, agents, tools, protocol, serverTag, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const nA = agents.length, nT = tools.length;
  const nodesIn = ease(ramp(t, 0.02, 0.1));
  const mesh = ease(ramp(t, 0.08, 0.3));
  const fade = ease(ramp(t, 0.38, 0.48));
  const bar = ease(ramp(t, 0.42, 0.54));
  const spokes = ease(ramp(t, 0.52, 0.66));
  const tag = ease(ramp(t, 0.6, 0.7));
  // node boxes in canvas coordinates
  type B = { x: number; y: number; w: number; h: number };
  let A: B[], T: B[], barB: B;
  if (P) {
    const aw = 296, ag = (S.w - nA * aw) / Math.max(1, nA - 1);
    // portrait: tools stack as full-width rows off a vertical bus, so names can be 90px
    // serif (GATE T's floor is 72px at 3840 tall)
    A = agents.map((_, i) => ({ x: S.x + i * (aw + ag), y: 340, w: aw, h: 120 }));
    T = tools.map((_, i) => ({ x: S.x + 64, y: 790 + i * 124, w: S.w - 64, h: 110 }));
    barB = { x: S.x, y: 560, w: S.w, h: 120 };
  } else {
    const aw = 330, ah = 130, ag = 60, aTop = 300 + ((4 * 110 + 3 * 40) - (nA * ah + (nA - 1) * ag)) / 2;
    A = agents.map((_, i) => ({ x: S.x, y: aTop + i * (ah + ag), w: aw, h: ah }));
    T = tools.map((_, i) => ({ x: S.r - 330, y: 290 + i * 150, w: 330, h: 124 }));
    barB = { x: 960 - 90, y: 290, w: 180, h: 580 };
  }
  const aPort = (b: B) => (P ? { x: b.x + b.w / 2, y: b.y + b.h } : { x: b.x + b.w, y: b.y + b.h / 2 });
  const tPort = (b: B) => ({ x: b.x, y: b.y + b.h / 2 });
  const busX = S.x + 24;
  const count = fade < 0.5 ? `${nA} × ${nT} = ${nA * nT} custom integrations` : `${nA} + ${nT} = ${nA + nT}, each built once`;
  const countA = fade < 0.5 ? ease(ramp(t, 0.22, 0.3)) * (1 - ease(ramp(t, 0.36, 0.42))) : ease(ramp(t, 0.6, 0.68));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P={P}>
        {!P && A.map((a, i) => T.map((b, j) => {
          const p = aPort(a), q = tPort(b);
          return <DrawLine key={`${i}-${j}`} x1={p.x} y1={p.y} x2={q.x} y2={q.y} d={ease(ramp(mesh, (i * nT + j) / (nA * nT) * 0.6, (i * nT + j) / (nA * nT) * 0.6 + 0.4))} o={1 - fade} w={3} />;
        }))}
        {A.map((a, i) => {
          const p = aPort(a);
          return <DrawLine key={`a${i}`} x1={p.x} y1={p.y} x2={P ? p.x : barB.x} y2={P ? barB.y : p.y} d={spokes} color={CLAUDE.INK} w={5} />;
        })}
        {T.map((b, j) => {
          const q = tPort(b);
          return <DrawLine key={`t${j}`} x1={P ? busX : barB.x + barB.w} y1={q.y} x2={q.x} y2={q.y} d={spokes} color={CLAUDE.INK} w={5} />;
        })}
        {P && <DrawLine x1={busX} y1={barB.y + barB.h} x2={busX} y2={tPort(T[T.length - 1]).y} d={spokes} color={CLAUDE.INK} w={5} />}
      </Canvas>
      {A.map((a, i) => <Box key={agents[i]} x={a.x} y={a.y} w={a.w} h={a.h} a={nodesIn} font={P ? 46 : 50}>{agents[i]}</Box>)}
      {P && T.map((b, j) => (
        <Card key={tools[j]} style={{
          left: b.x, top: b.y, width: b.w, height: b.h, opacity: nodesIn, padding: '0 28px',
          display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        }}>
          <span style={{ fontFamily: SERIF, fontSize: 90, color: CLAUDE.INK, lineHeight: 1 }}>{tools[j]}</span>
          <span style={{ fontFamily: SANS, fontSize: 50, color: CLAUDE.INK_SOFT, opacity: tag }}>{serverTag}</span>
        </Card>
      ))}
      {!P && T.map((b, j) => (
        <Box key={tools[j]} x={b.x} y={b.y} w={b.w} h={b.h} a={nodesIn} font={P ? 42 : 54}>
          {tools[j]}
          <span style={{ fontFamily: SANS, fontSize: P ? 40 : 46, color: CLAUDE.INK_SOFT, marginTop: 4, opacity: tag, height: tag > 0 ? 'auto' : 0 }}>{serverTag}</span>
        </Box>
      ))}
      {P && (
        // portrait: the tangle draws OVER the tool rows — behind them it only showed as stubs
        <Canvas P>
          {A.map((a, i) => T.map((b, j) => {
            const p = aPort(a), q = { x: b.x + 180 + j * 120, y: b.y + b.h / 2 };
            return <DrawLine key={`m${i}-${j}`} x1={p.x} y1={p.y} x2={q.x} y2={q.y} d={ease(ramp(mesh, (i * nT + j) / (nA * nT) * 0.6, (i * nT + j) / (nA * nT) * 0.6 + 0.4))} o={0.7 * (1 - fade)} w={3} />;
          }))}
        </Canvas>
      )}
      <div style={{
        position: 'absolute', left: barB.x, top: barB.y, width: barB.w, height: barB.h, borderRadius: 18, background: ACC_TEXT,   // darker terracotta: white label 5.5:1, GATE T §8.3
        opacity: bar, transform: P ? `scaleX(${0.3 + 0.7 * bar})` : `scaleY(${0.3 + 0.7 * bar})`,
        display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: P ? 76 : 64, color: CLAUDE.CARD,
      }}>{protocol}</div>
      <div style={{
        position: 'absolute', left: S.x, width: S.w, textAlign: 'center', top: P ? 262 : 188,
        fontFamily: P ? SANS : SERIF, fontSize: P ? 48 : 52, color: CLAUDE.INK, opacity: countA,
      }}>{count}</div>
      <Spark st={st} text={sparkLine} at={0.84} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// McpDiscovery — the agent asks the server what tools exist (REAL tools/list output)
// ===========================================================================
const toolSchema = z.object({ name: z.string(), description: z.string(), required: z.array(z.string()) });
const V1_TOOLS = [
  { name: 'list_events', description: 'List events on a date.', required: ['date'] },
  { name: 'create_event', description: 'Create a calendar event.', required: ['title', 'date'] },
];
export const mcpDiscoverySchema = z.object({
  title: z.string().default('The agent asks at runtime'),
  method: z.string().default('tools/list'),
  tools: z.array(toolSchema).default(V1_TOOLS),
  caption: z.string().default('real output · toy calendar server · MCP Python SDK 2.2.0'),
  sparkLine: z.string().default('What can you do?'),
  durationSeconds: z.number().optional(),
});
export const mcpDiscoveryMeta = durMeta(5);
const ToolRow: React.FC<{ tool: z.infer<typeof toolSchema>; a: number; P: boolean; accent?: boolean }> = ({ tool, a, P, accent }) => (
  <div style={{ opacity: a, transform: `translateY(${(1 - a) * 14}px)`, borderLeft: `6px solid ${accent ? CLAUDE.SPARK : CLAUDE.BORDER}`, paddingLeft: 22, marginBottom: P ? 30 : 34 }}>
    <div style={{ fontFamily: MONO, fontSize: P ? 44 : 48, color: CLAUDE.INK, fontWeight: 600 }}>{tool.name}</div>
    <div style={{ fontFamily: SANS, fontSize: P ? 36 : 38, color: CLAUDE.INK, marginTop: 6 }}>{tool.description}</div>
    <div style={{ fontFamily: MONO, fontSize: P ? 32 : 34, color: CLAUDE.INK_SOFT, marginTop: 6 }}>needs: {tool.required.join(', ')}</div>
  </div>
);
export const McpDiscovery: React.FC<z.infer<typeof mcpDiscoverySchema>> = ({ title, method, tools, caption, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const ask = ease(ramp(t, 0.04, 0.14));
  const arrow = ease(ramp(t, 0.16, 0.28));
  const answer = ease(ramp(t, 0.26, 0.36));
  const reqB = P ? { x: S.x, y: 330, w: S.w, h: 250 } : { x: S.x, y: 290, w: 720, h: 270 };
  const resB = P ? { x: S.x, y: 660, w: S.w, h: 540 } : { x: S.x + 830, y: 290, w: S.w - 830, h: 560 };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: reqB.x, top: reqB.y, width: reqB.w, height: reqB.h, padding: P ? '26px 34px' : '30px 38px', opacity: ask }}>
        <div style={{ fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT, marginBottom: 18 }}>agent → server</div>
        <div style={{ fontFamily: MONO, fontSize: P ? 42 : 40, color: CLAUDE.INK, lineHeight: 1.45, whiteSpace: 'pre' }}>
          {'{ "jsonrpc": "2.0",'}<br />
          {'  "method": '}<span style={{ color: CLAUDE.SPARK, fontWeight: 700 }}>"{method}"</span>{' }'}
        </div>
      </Card>
      <Canvas P={P}>
        {P
          ? <DrawLine x1={540} y1={reqB.y + reqB.h + 8} x2={540} y2={resB.y - 12} d={arrow} color={CLAUDE.INK} w={6} />
          : <DrawLine x1={reqB.x + reqB.w + 16} y1={reqB.y + reqB.h / 2} x2={resB.x - 18} y2={reqB.y + reqB.h / 2} d={arrow} color={CLAUDE.INK} w={6} />}
      </Canvas>
      <Card style={{ left: resB.x, top: resB.y, width: resB.w, height: resB.h, padding: P ? '26px 34px' : '30px 40px', opacity: answer }}>
        <div style={{ fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT, marginBottom: 26 }}>server → agent: its tools</div>
        {tools.map((tool, i) => <ToolRow key={tool.name} tool={tool} P={P} a={ease(ramp(t, 0.36 + i * 0.12, 0.46 + i * 0.12))} />)}
      </Card>
      <Note x={P ? S.x : reqB.x} y={P ? resB.y + resB.h + 16 : reqB.y + reqB.h + 30} w={P ? S.w : reqB.w} a={answer} text={caption} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// McpRuntime — hardcoded endpoints vs. a tool list that grows, client unchanged
// ===========================================================================
export const mcpRuntimeSchema = z.object({
  title: z.string().default('Nothing hardcoded'),
  apiHead: z.string().default('plain API client'),
  apiLines: z.array(z.string()).default(['POST /v1/events', 'GET  /v1/events?date=', '# new endpoint?', '# → edit the client']),
  mcpHead: z.string().default('MCP client'),
  mcpCall: z.string().default('tools = session.list_tools()'),
  tools: z.array(z.string()).default(['list_events', 'create_event']),
  added: z.string().default('cancel_event'),
  addedTag: z.string().default('added to the server'),
  unchanged: z.string().default('client code: unchanged'),
  caption: z.string().default('tool lists: real output (v1 → v2 server)'),
  sparkLine: z.string().default('Found, not hardcoded.'),
  durationSeconds: z.number().optional(),
});
export const mcpRuntimeMeta = durMeta(6);
export const McpRuntime: React.FC<z.infer<typeof mcpRuntimeSchema>> = ({ title, apiHead, apiLines, mcpHead, mcpCall, tools, added, addedTag, unchanged, caption, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const leftIn = ease(ramp(t, 0.03, 0.12));
  const rightIn = ease(ramp(t, 0.3, 0.4));
  const add = ease(ramp(t, 0.5, 0.6));
  const badge = ease(ramp(t, 0.66, 0.74));
  const colW = P ? S.w : (S.w - 60) / 2;
  const L = P ? { x: S.x, y: 320, h: 350 } : { x: S.x, y: 280, h: 560 };
  const R = P ? { x: S.x, y: 700, h: 540 } : { x: S.x + colW + 60, y: 280, h: 560 };
  const code = P ? 38 : 42;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: L.x, top: L.y, width: colW, height: L.h, padding: P ? '24px 32px' : '32px 40px', opacity: leftIn }}>
        <div style={{ fontFamily: SANS, fontSize: 36, color: CLAUDE.INK_SOFT, marginBottom: 20 }}>{apiHead}</div>
        {apiLines.map((l, i) => (
          <div key={i} style={{
            fontFamily: MONO, fontSize: code, lineHeight: 1.55, color: l.startsWith('#') ? CLAUDE.INK_SOFT : CLAUDE.INK,
            opacity: ease(ramp(t, 0.06 + i * 0.05, 0.14 + i * 0.05)), whiteSpace: 'pre',
          }}>{l}</div>
        ))}
      </Card>
      <Card accent={badge > 0.5} style={{ left: R.x, top: R.y, width: colW, height: R.h, padding: P ? '24px 32px' : '32px 40px', opacity: rightIn }}>
        <div style={{ fontFamily: SANS, fontSize: 36, color: CLAUDE.INK_SOFT, marginBottom: 20 }}>{mcpHead}</div>
        <div style={{ fontFamily: MONO, fontSize: code, color: CLAUDE.INK, marginBottom: 30 }}>{mcpCall}</div>
        {tools.map((n) => (
          <div key={n} style={{ fontFamily: MONO, fontSize: code + 2, color: CLAUDE.INK, lineHeight: 1.6, paddingLeft: 20, borderLeft: `6px solid ${CLAUDE.BORDER}` }}>{n}</div>
        ))}
        <div style={{
          display: 'flex', alignItems: 'baseline', gap: 22, paddingLeft: 20, borderLeft: `6px solid ${CLAUDE.SPARK}`,
          opacity: add, transform: `translateX(${(1 - add) * 40}px)`, lineHeight: 1.6,
        }}>
          <span style={{ fontFamily: MONO, fontSize: code + 2, color: CLAUDE.INK, fontWeight: 700 }}>{added}</span>
          <span style={{ fontFamily: SANS, fontSize: 32, color: CLAUDE.SPARK }}>+ {addedTag}</span>
        </div>
        <div style={{
          marginTop: 34, display: 'inline-block', padding: '10px 26px', borderRadius: 999, background: CLAUDE.PILL,
          fontFamily: SANS, fontSize: 36, color: CLAUDE.INK, opacity: badge,
        }}>✓ {unchanged}</div>
      </Card>
      <Note x={P ? S.x : R.x} y={R.y + R.h + 16} w={colW} a={rightIn} text={caption} />
      <Spark st={st} text={sparkLine} at={0.82} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// McpCompose — the agent chains tools on the fly, one call shape for all of them
// ===========================================================================
export const mcpComposeSchema = z.object({
  title: z.string().default('Agents chain tools'),
  steps: z.array(z.object({ server: z.string(), tool: z.string(), args: z.string() })).default([
    { server: 'email', tool: 'search_email', args: '{"from": "Ana"}' },
    { server: 'calendar', tool: 'list_events', args: '{"date": "Fri"}' },
    { server: 'rooms', tool: 'book_room', args: '{"at": "Fri 2pm"}' },
  ]),
  method: z.string().default('tools/call'),
  shared: z.string().default('one call shape for every tool'),
  note: z.string().default('illustrative tools'),
  sparkLine: z.string().default('One interface, not three.'),
  durationSeconds: z.number().optional(),
});
export const mcpComposeMeta = durMeta(5);
export const McpCompose: React.FC<z.infer<typeof mcpComposeSchema>> = ({ title, steps, method, shared, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = steps.length;
  const gap = P ? 36 : 90;
  const cw = P ? S.w : (S.w - gap * (n - 1)) / n;
  const ch = P ? 260 : 440;
  const top = P ? 340 : 300;
  const stepAt = (i: number) => 0.06 + i * 0.16;
  const brace = ease(ramp(t, 0.62, 0.74));
  const pos = (i: number) => (P ? { x: S.x, y: top + i * (ch + gap) } : { x: S.x + i * (cw + gap), y: top });
  const braceY = P ? 0 : top + ch + 44;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P={P}>
        {steps.slice(1).map((_, k) => {
          const a = pos(k), b = pos(k + 1);
          const d = ease(ramp(t, stepAt(k + 1) - 0.04, stepAt(k + 1) + 0.04));
          return P
            ? <DrawLine key={k} x1={540} y1={a.y + ch + 6} x2={540} y2={b.y - 6} d={d} color={CLAUDE.INK} w={6} />
            : <DrawLine key={k} x1={a.x + cw + 12} y1={top + ch / 2} x2={b.x - 12} y2={top + ch / 2} d={d} color={CLAUDE.INK} w={6} />;
        })}
        {!P && brace > 0 && (
          <path d={`M${S.x} ${braceY - 24} L${S.x} ${braceY} L${S.r} ${braceY} L${S.r} ${braceY - 24}`} fill="none"
            stroke={CLAUDE.SPARK} strokeWidth={6} strokeLinecap="round" opacity={brace} />
        )}
      </Canvas>
      {steps.map((s, i) => {
        const a = ease(ramp(t, stepAt(i), stepAt(i) + 0.08));
        const p = pos(i);
        return (
          <Card key={s.tool} style={{
            left: p.x, top: p.y, width: cw, height: ch, padding: P ? '22px 30px' : '30px 34px', opacity: a,
            transform: `translateY(${(1 - a) * 16}px)`,
          }}>
            <div style={{ fontFamily: SANS, fontSize: P ? 34 : 40, color: CLAUDE.INK_SOFT }}>{i + 1} · {s.server} server</div>
            <div style={{ fontFamily: MONO, fontSize: P ? 40 : 46, color: brace > 0.5 ? CLAUDE.SPARK : CLAUDE.INK, marginTop: P ? 14 : 44, fontWeight: 700 }}>{method}</div>
            <div style={{ fontFamily: MONO, fontSize: P ? 42 : 50, color: CLAUDE.INK, marginTop: P ? 8 : 22 }}>{s.tool}</div>
            <div style={{ fontFamily: MONO, fontSize: P ? 34 : 38, color: CLAUDE.INK_SOFT, marginTop: P ? 8 : 22 }}>{s.args}</div>
          </Card>
        );
      })}
      <div style={{
        position: 'absolute', left: S.x, width: S.w, textAlign: 'center', top: P ? top + n * (ch + gap) - 20 : braceY + 18,
        fontFamily: SERIF, fontSize: P ? 50 : 50, color: CLAUDE.INK, opacity: brace,
      }}>{shared}</div>
      <Note x={S.x} y={P ? top + n * (ch + gap) + 50 : braceY + 18} w={S.w} a={brace} align="right" text={P ? note : ''} />
      {!P && <Note x={S.x} y={top - 56} w={S.w} a={ease(ramp(t, 0.06, 0.14))} align="right" text={note} />}
      <Spark st={st} text={sparkLine} at={0.84} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// McpTerminal — analogy: each store's own checkout vs. one universal payment terminal
// ===========================================================================
export const mcpTerminalSchema = z.object({
  title: z.string().default('An analogy: checkout'),
  stores: z.array(z.object({ name: z.string(), checkout: z.string() })).default([
    { name: 'Bakery', checkout: 'cash drawer' },
    { name: 'Books', checkout: 'card swipe' },
    { name: 'Café', checkout: 'scan a code' },
  ]),
  terminal: z.string().default('one terminal'),
  beforeLine: z.string().default('APIs: every store runs its own checkout'),
  afterLine: z.string().default('MCP: one terminal every store plugs into'),
  sparkLine: z.string().default('Plug in once.'),
  durationSeconds: z.number().optional(),
});
export const mcpTerminalMeta = durMeta(5);

// three different checkout glyphs, then the same terminal glyph for all
const Glyph: React.FC<{ kind: number; s: number; color: string }> = ({ kind, s, color }) => {
  const w = 5;
  if (kind === 0) return ( // cash drawer
    <g stroke={color} strokeWidth={w} fill="none">
      <rect x={-s * 0.5} y={-s * 0.18} width={s} height={s * 0.42} rx={8} />
      <line x1={-s * 0.14} y1={s * 0.03} x2={s * 0.14} y2={s * 0.03} />
      <rect x={-s * 0.36} y={-s * 0.5} width={s * 0.72} height={s * 0.28} rx={6} />
    </g>
  );
  if (kind === 1) return ( // card + swipe slot
    <g stroke={color} strokeWidth={w} fill="none">
      <rect x={-s * 0.46} y={-s * 0.28} width={s * 0.92} height={s * 0.56} rx={12} />
      <line x1={-s * 0.46} y1={-s * 0.1} x2={s * 0.46} y2={-s * 0.1} strokeWidth={w * 3} />
    </g>
  );
  if (kind === 2) return ( // QR-ish grid
    <g stroke={color} strokeWidth={w} fill="none">
      <rect x={-s * 0.34} y={-s * 0.34} width={s * 0.68} height={s * 0.68} rx={6} />
      {[[-0.22, -0.22], [0.06, -0.22], [-0.22, 0.06], [0.1, 0.1]].map(([x, y], i) => (
        <rect key={i} x={s * x} y={s * y} width={s * 0.14} height={s * 0.14} fill={color} />
      ))}
    </g>
  );
  return ( // universal terminal: screen + keypad
    <g stroke={color} strokeWidth={w} fill="none">
      <rect x={-s * 0.3} y={-s * 0.44} width={s * 0.6} height={s * 0.88} rx={16} />
      <rect x={-s * 0.2} y={-s * 0.34} width={s * 0.4} height={s * 0.26} rx={6} />
      {[0, 1, 2].map((r) => [0, 1, 2].map((c) => (
        <circle key={`${r}${c}`} cx={s * (-0.13 + c * 0.13)} cy={s * (0.04 + r * 0.12)} r={s * 0.035} fill={color} />
      )))}
    </g>
  );
};
export const McpTerminal: React.FC<z.infer<typeof mcpTerminalSchema>> = ({ title, stores, terminal, beforeLine, afterLine, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = stores.length;
  const gap = P ? 36 : 110;
  const inset = 12;   // keeps awning strokes inside SAFE
  const sw = (S.w - 2 * inset - gap * (n - 1)) / n;
  const top = P ? 350 : 280;
  const shopH = P ? 250 : 250;
  const devTop = top + shopH + (P ? 40 : 36);
  const devH = P ? 300 : 250;
  const swap = ease(ramp(t, 0.5, 0.62));
  const lineY = devTop + devH + (P ? 50 : 40);
  if (P) return <McpTerminalPortrait {...{ title, stores, terminal, beforeLine, afterLine, sparkLine }} />;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P={P}>
        {stores.map((s, i) => {
          const x = S.x + inset + i * (sw + gap);
          const a = ease(ramp(t, 0.04 + i * 0.07, 0.14 + i * 0.07));
          const stripes = 6;
          return (
            <g key={s.name} opacity={a}>
              {Array.from({ length: stripes }).map((_, k) => (
                <rect key={k} x={x + (k * sw) / stripes} y={top} width={sw / stripes} height={56}
                  fill={k % 2 ? CLAUDE.CARD : CLAUDE.PILL} stroke={CLAUDE.INK} strokeWidth={3} />
              ))}
              <rect x={x + 12} y={top + 56} width={sw - 24} height={shopH - 56} fill={CLAUDE.CARD} stroke={CLAUDE.INK} strokeWidth={4} />
            </g>
          );
        })}
        {stores.map((s, i) => {
          const cx = S.x + inset + i * (sw + gap) + sw / 2, cy = devTop + devH * 0.42;
          const a = ease(ramp(t, 0.16 + i * 0.07, 0.26 + i * 0.07));
          const g = P ? 170 : 190;
          return (
            <g key={`d${i}`} transform={`translate(${cx} ${cy})`}>
              <g opacity={a * (1 - swap)}><Glyph kind={i} s={g} color={CLAUDE.INK} /></g>
              <g opacity={swap}><Glyph kind={3} s={g * 1.05} color={CLAUDE.SPARK} /></g>
            </g>
          );
        })}
      </Canvas>
      {stores.map((s, i) => {
        const x = S.x + inset + i * (sw + gap);
        const a = ease(ramp(t, 0.04 + i * 0.07, 0.14 + i * 0.07));
        const da = ease(ramp(t, 0.16 + i * 0.07, 0.26 + i * 0.07));
        return (
          <React.Fragment key={s.name}>
            <div style={{
              position: 'absolute', left: x, top: top + 56, width: sw, height: shopH - 56, display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontFamily: SERIF, fontSize: P ? 56 : 60, color: CLAUDE.INK, opacity: a,
            }}>{s.name}</div>
            <div style={{
              position: 'absolute', left: x, top: devTop + devH * 0.8, width: sw, textAlign: 'center',
              fontFamily: SANS, fontSize: P ? 34 : 38, color: swap > 0.5 ? CLAUDE.SPARK : CLAUDE.INK_SOFT, opacity: swap > 0.5 ? swap : da * (1 - swap * 2),
            }}>{swap > 0.5 ? terminal : s.checkout}</div>
          </React.Fragment>
        );
      })}
      <div style={{
        position: 'absolute', left: S.x, top: lineY, width: S.w, textAlign: 'center',
        fontFamily: SERIF, fontSize: P ? 50 : 54, color: CLAUDE.INK, lineHeight: 1.15,
        opacity: swap > 0.5 ? swap : ease(ramp(t, 0.3, 0.38)) * (1 - swap * 2),
      }}>{swap > 0.5 ? afterLine : beforeLine}</div>
      <Spark st={st} text={sparkLine} at={0.84} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// Portrait (9:16): stores stack as rows — store left, checkout right — so the store names
// can be 90px serif and the labels 52px sans (GATE T's floor is 72px at 3840 tall).
const McpTerminalPortrait: React.FC<z.infer<typeof mcpTerminalSchema>> = ({ title, stores, terminal, beforeLine, afterLine, sparkLine }) => {
  const st = useStage(); const { t, S } = st;
  const swap = ease(ramp(t, 0.5, 0.62));
  const inset = 12, shopW = 440, awn = 50, rowH = 220, rowGap = 30, top = 310;
  const devCx = S.x + shopW + (S.w - shopW) / 2;
  const lineY = top + stores.length * (rowH + rowGap) + 10;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P>
        {stores.map((s, i) => {
          const y = top + i * (rowH + rowGap), x = S.x + inset;
          const a = ease(ramp(t, 0.04 + i * 0.07, 0.14 + i * 0.07));
          const da = ease(ramp(t, 0.16 + i * 0.07, 0.26 + i * 0.07));
          const stripes = 6;
          return (
            <g key={s.name}>
              <g opacity={a}>
                {Array.from({ length: stripes }).map((_, k) => (
                  <rect key={k} x={x + (k * shopW) / stripes} y={y} width={shopW / stripes} height={awn}
                    fill={k % 2 ? CLAUDE.CARD : CLAUDE.PILL} stroke={CLAUDE.INK} strokeWidth={3} />
                ))}
                <rect x={x + 12} y={y + awn} width={shopW - 24} height={rowH - awn} fill={CLAUDE.CARD} stroke={CLAUDE.INK} strokeWidth={4} />
              </g>
              <g transform={`translate(${devCx} ${y + 76})`}>
                <g opacity={da * (1 - swap)}><Glyph kind={i} s={140} color={CLAUDE.INK} /></g>
                <g opacity={swap}><Glyph kind={3} s={150} color={CLAUDE.SPARK} /></g>
              </g>
            </g>
          );
        })}
      </Canvas>
      {stores.map((s, i) => {
        const y = top + i * (rowH + rowGap);
        const a = ease(ramp(t, 0.04 + i * 0.07, 0.14 + i * 0.07));
        const da = ease(ramp(t, 0.16 + i * 0.07, 0.26 + i * 0.07));
        return (
          <React.Fragment key={s.name}>
            <div style={{
              position: 'absolute', left: S.x + inset, top: y + awn, width: shopW, height: rowH - awn,
              display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: 90, color: CLAUDE.INK, opacity: a,
            }}>{s.name}</div>
            <div style={{
              position: 'absolute', left: S.x + shopW, top: y + 150, width: S.w - shopW, textAlign: 'center',
              fontFamily: SANS, fontSize: 52, color: swap > 0.5 ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
              opacity: swap > 0.5 ? swap : da * (1 - swap * 2),
            }}>{swap > 0.5 ? terminal : s.checkout}</div>
          </React.Fragment>
        );
      })}
      <div style={{
        position: 'absolute', left: S.x, top: lineY, width: S.w, textAlign: 'center',
        fontFamily: SERIF, fontSize: 90, color: CLAUDE.INK, lineHeight: 1.1,
        opacity: swap > 0.5 ? swap : ease(ramp(t, 0.3, 0.38)) * (1 - swap * 2),
      }}>{swap > 0.5 ? afterLine : beforeLine}</div>
      <Spark st={st} text={sparkLine} at={0.84} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
