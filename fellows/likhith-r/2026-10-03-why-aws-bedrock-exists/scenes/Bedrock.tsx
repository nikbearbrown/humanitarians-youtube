/**
 * Bedrock.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-aws-bedrock ("Why AWS Bedrock Exists", @HumanitariansAI).
 *
 * Same contract as McpProtocol.tsx / JevExplainer.tsx (whose stage helpers it reuses):
 * each component lays out natively for 16:9 (<Name>) and 9:16 (<Name>916) — never a
 * crop — and every motion is a pure function of progress, conformed via `durationSeconds`.
 * Provider request bodies, the model pairing and task labels are illustrative and
 * labelled so on screen; the API names in BedrockCapabilities and the converse() call in
 * BedrockSwap come from the reel's evidence/converse_shape.py (botocore service models,
 * offline). Claims: SOURCES.md.
 *
 *   BedrockHook         — your app wants a model; who runs the GPUs underneath?
 *   BedrockSilos        — Claude / Llama / Titan: own request body, own hosting → 3 integrations
 *   BedrockUnified      — 3 direct wires collapse into one Bedrock API to many providers
 *   BedrockManaged      — the infra moves from "you handle" to "AWS handles"
 *   BedrockCapabilities — guardrails, fine-tuning, agents on the same platform (real API names)
 *   BedrockSwap         — one converse() call; only the modelId string changes
 *   BedrockCombine      — a small model sorts, a stronger one replies, one integration
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const Canvas: React.FC<{ P: boolean; children: React.ReactNode }> = ({ P, children }) => (
  <svg width={P ? 1080 : 1920} height={P ? 1920 : 1080} style={{ position: 'absolute', left: 0, top: 0 }}>{children}</svg>
);

// a line that draws from (x1,y1) to (x2,y2) as d goes 0 → 1
const DrawLine: React.FC<{ x1: number; y1: number; x2: number; y2: number; d: number; color?: string; w?: number; o?: number; dash?: string }> = ({ x1, y1, x2, y2, d, color = CLAUDE.INK_SOFT, w = 4, o = 1, dash }) =>
  d <= 0 ? null : <line x1={x1} y1={y1} x2={x1 + (x2 - x1) * d} y2={y1 + (y2 - y1) * d} stroke={color} strokeWidth={w} opacity={o} strokeDasharray={dash} strokeLinecap="round" />;

const Note: React.FC<{ x: number; y: number; w: number; a: number; text: string; P: boolean; align?: 'left' | 'right' | 'center' }> = ({ x, y, w, a, text, P, align = 'left' }) => (
  <div style={{ position: 'absolute', left: x, top: y, width: w, textAlign: align, fontFamily: SANS, fontSize: P ? 48 : 36, color: CLAUDE.INK_SOFT, opacity: a, lineHeight: 1.2 }}>{text}</div>
);

// the Bedrock hub: darker terracotta fill (white label 5.5:1, GATE T §8.3)
const Hub: React.FC<{ x: number; y: number; w: number; h: number; a: number; grow: 'x' | 'y'; children: React.ReactNode }> = ({ x, y, w, h, a, grow, children }) => (
  <div style={{
    position: 'absolute', left: x, top: y, width: w, height: h, borderRadius: 18, background: ACC_TEXT, opacity: a,
    transform: grow === 'x' ? `scaleX(${0.3 + 0.7 * a})` : `scaleY(${0.3 + 0.7 * a})`,
    display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', color: CLAUDE.CARD, textAlign: 'center',
  }}>{children}</div>
);

// ===========================================================================
// BedrockHook — your app wants a model; the infrastructure stack piles up under it
// ===========================================================================
export const bedrockHookSchema = z.object({
  title: z.string().default('AI in your app?'),
  app: z.string().default('Your app'),
  model: z.string().default('AI model'),
  infra: z.array(z.string()).default(['GPU servers', 'scaling', 'patching & security', 'uptime & on-call']),
  ask: z.string().default('yours to run?'),
  sparkLine: z.string().default('Do you run the GPUs?'),
  durationSeconds: z.number().optional(),
});
export const bedrockHookMeta = durMeta(5);
export const BedrockHook: React.FC<z.infer<typeof bedrockHookSchema>> = ({ title, app, model, infra, ask, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const appIn = ease(ramp(t, 0.03, 0.12));
  const link = ease(ramp(t, 0.1, 0.22));
  const modelIn = ease(ramp(t, 0.16, 0.26));
  const barAt = (i: number) => 0.3 + i * 0.08;
  const q = ease(ramp(t, 0.68, 0.76));
  const app$ = P ? { x: S.x, y: 300, w: S.w, h: 140 } : { x: S.x, y: 400, w: 440, h: 220 };
  const mod$ = P ? { x: S.x, y: 500, w: S.w, h: 140 } : { x: 760, y: 250, w: S.r - 760, h: 150 };
  const barTop = P ? 680 : 430, barH = P ? 112 : 110, barGap = P ? 22 : 20;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P={P}>
        {P
          ? <DrawLine x1={540} y1={app$.y + app$.h + 6} x2={540} y2={mod$.y - 6} d={link} color={CLAUDE.INK} w={6} />
          : <DrawLine x1={app$.x + app$.w + 10} y1={app$.y + app$.h / 2} x2={mod$.x - 10} y2={mod$.y + mod$.h / 2} d={link} color={CLAUDE.INK} w={6} />}
      </Canvas>
      <Card style={{ left: app$.x, top: app$.y, width: app$.w, height: app$.h, opacity: appIn, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: P ? 90 : 68, color: CLAUDE.INK }}>{app}</Card>
      <Card style={{ left: mod$.x, top: mod$.y, width: mod$.w, height: mod$.h, opacity: modelIn, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: P ? 90 : 68, color: CLAUDE.INK }}>{model}</Card>
      {infra.map((label, i) => {
        const a = ease(ramp(t, barAt(i), barAt(i) + 0.08));
        return (
          <Card key={label} style={{
            left: mod$.x, top: barTop + i * (barH + barGap), width: mod$.w, height: barH, opacity: a,
            transform: `translateY(${(1 - a) * 30}px)`, border: `3px dashed ${CLAUDE.GHOST}`, background: CLAUDE.FOOTER,
            display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: P ? '0 36px' : '0 40px',
            fontFamily: SANS, fontSize: P ? 60 : 50, color: CLAUDE.INK,
          }}>
            <span>{label}</span>
            <span style={{ fontFamily: SERIF, fontSize: P ? 90 : 72, color: ACC_TEXT, opacity: q, lineHeight: 1 }}>?</span>
          </Card>
        );
      })}
      {!P && (
        <div style={{
          position: 'absolute', left: S.x, top: app$.y + app$.h + 60, width: app$.w + 160,
          fontFamily: SERIF, fontSize: 76, color: ACC_TEXT, opacity: q, lineHeight: 1.05,
        }}>{ask}</div>
      )}
      <Spark st={st} text={sparkLine} at={0.8} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// BedrockSilos — each model brings its own request body and its own hosting
// ===========================================================================
const siloSchema = z.object({ name: z.string(), maker: z.string(), body: z.string(), runs: z.string() });
export const bedrockSilosSchema = z.object({
  title: z.string().default('Every model, its own setup'),
  models: z.array(siloSchema).default([
    { name: 'Claude', maker: 'Anthropic', body: '"messages"', runs: 'Anthropic' },
    { name: 'Llama', maker: 'Meta', body: '"prompt"', runs: 'you host it' },
    { name: 'Titan', maker: 'Amazon', body: '"inputText"', runs: 'Amazon' },
  ]),
  bodyLabel: z.string().default('request body'),
  runsLabel: z.string().default('runs on'),
  counter: z.string().default('3 models ='),
  counterHit: z.string().default('3 integrations'),
  note: z.string().default('illustrative: each model integrated on its own'),
  sparkLine: z.string().default('Three models, three setups.'),
  durationSeconds: z.number().optional(),
});
export const bedrockSilosMeta = durMeta(6);
export const BedrockSilos: React.FC<z.infer<typeof bedrockSilosSchema>> = ({ title, models, bodyLabel, runsLabel, counter, counterHit, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = models.length;
  const colAt = (i: number) => 0.06 + i * 0.13;
  const cnt = ease(ramp(t, 0.58, 0.68));
  if (P) {
    const top = 300, rowH = 290, gap = 18;
    const countY = top + n * (rowH + gap) - 2;
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
        <Title st={st} text={title} />
        {models.map((m, i) => {
          const a = ease(ramp(t, colAt(i), colAt(i) + 0.08));
          return (
            <Card key={m.name} style={{ left: S.x, top: top + i * (rowH + gap), width: S.w, height: rowH, padding: '18px 34px', opacity: a, transform: `translateX(${(1 - a) * 30}px)` }}>
              <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between' }}>
                <span style={{ fontFamily: SERIF, fontSize: 90, color: CLAUDE.INK, lineHeight: 1 }}>{m.name}</span>
                <span style={{ fontFamily: SANS, fontSize: 52, color: CLAUDE.INK_SOFT }}>{m.maker}</span>
              </div>
              <div style={{ fontFamily: MONO, fontSize: 52, color: CLAUDE.INK, marginTop: 14 }}>{m.body}</div>
              <div style={{ fontFamily: SANS, fontSize: 56, color: CLAUDE.INK, marginTop: 8 }}>
                <span style={{ color: CLAUDE.INK_SOFT }}>{runsLabel}: </span>{m.runs}
              </div>
            </Card>
          );
        })}
        <div style={{ position: 'absolute', left: S.x, top: countY, width: S.w, textAlign: 'center', fontFamily: SERIF, fontSize: 76, color: CLAUDE.INK, opacity: cnt, lineHeight: 1.1 }}>
          {counter} <span style={{ color: ACC_TEXT }}>{counterHit}</span>
        </div>
        <Spark st={st} text={sparkLine} at={0.84} />
        <Bug st={st} />
      </AbsoluteFill>
    );
  }
  const gap = 44, cw = (S.w - gap * (n - 1)) / n, top = 250, ch = 560;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {models.map((m, i) => {
        const a = ease(ramp(t, colAt(i), colAt(i) + 0.08));
        const rowA = (k: number) => ease(ramp(t, colAt(i) + 0.04 + k * 0.03, colAt(i) + 0.1 + k * 0.03));
        return (
          <Card key={m.name} style={{ left: S.x + i * (cw + gap), top, width: cw, height: ch, padding: '34px 40px', opacity: a, transform: `translateY(${(1 - a) * 24}px)` }}>
            <div style={{ fontFamily: SERIF, fontSize: 84, color: CLAUDE.INK, lineHeight: 1 }}>{m.name}</div>
            <div style={{ fontFamily: SANS, fontSize: 42, color: CLAUDE.INK_SOFT, marginTop: 10 }}>{m.maker}</div>
            <div style={{ height: 3, background: CLAUDE.BORDER, margin: '30px 0' }} />
            <div style={{ opacity: rowA(0) }}>
              <div style={{ fontFamily: SANS, fontSize: 40, color: CLAUDE.INK_SOFT }}>{bodyLabel}</div>
              <div style={{ fontFamily: MONO, fontSize: 52, color: CLAUDE.INK, marginTop: 8 }}>{m.body}</div>
            </div>
            <div style={{ opacity: rowA(1), marginTop: 34 }}>
              <div style={{ fontFamily: SANS, fontSize: 40, color: CLAUDE.INK_SOFT }}>{runsLabel}</div>
              <div style={{ fontFamily: SANS, fontSize: 54, color: CLAUDE.INK, marginTop: 8 }}>{m.runs}</div>
            </div>
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: S.x, top: top + ch + 30, width: S.w, textAlign: 'center', fontFamily: SERIF, fontSize: 72, color: CLAUDE.INK, opacity: cnt }}>
        {counter} <span style={{ color: ACC_TEXT }}>{counterHit}</span>
      </div>
      <Note P={P} x={S.x} y={top - 52} w={S.w} a={ease(ramp(t, 0.06, 0.14))} align="right" text={note} />
      <Spark st={st} text={sparkLine} at={0.84} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// BedrockUnified — three direct integrations collapse into one Bedrock API
// ===========================================================================
export const bedrockUnifiedSchema = z.object({
  title: z.string().default('One API, many providers'),
  app: z.string().default('Your app'),
  hub: z.string().default('Bedrock'),
  hubSub: z.string().default('one API'),
  models: z.array(z.string()).default(['Claude', 'Llama', 'Titan', '+ more providers']),
  before: z.string().default('3 integrations'),
  after: z.string().default('1 integration'),
  sparkLine: z.string().default('One API, many models.'),
  durationSeconds: z.number().optional(),
});
export const bedrockUnifiedMeta = durMeta(5);
export const BedrockUnified: React.FC<z.infer<typeof bedrockUnifiedSchema>> = ({ title, app, hub, hubSub, models, before, after, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const nodes = ease(ramp(t, 0.02, 0.1));
  const direct = ease(ramp(t, 0.08, 0.26));
  const fade = ease(ramp(t, 0.34, 0.44));
  const hubA = ease(ramp(t, 0.38, 0.5));
  const spokes = ease(ramp(t, 0.5, 0.64));
  const direct3 = models.slice(0, 3);
  const countTxt = fade < 0.5 ? before : after;
  const countA = fade < 0.5 ? ease(ramp(t, 0.18, 0.26)) * (1 - ease(ramp(t, 0.3, 0.36))) : ease(ramp(t, 0.58, 0.66));
  type B = { x: number; y: number; w: number; h: number };
  let A: B, H: B, M: B[], countPos: B;
  if (P) {
    A = { x: S.x, y: 300, w: S.w, h: 130 };
    H = { x: S.x, y: 510, w: S.w, h: 160 };
    M = models.map((_, i) => ({ x: S.x + 110, y: 740 + i * 112, w: S.w - 110, h: 96 }));
    countPos = { x: S.x, y: 1180, w: S.w, h: 80 };
  } else {
    A = { x: S.x, y: 410, w: 380, h: 200 };
    H = { x: 830, y: 270, w: 340, h: 580 };
    M = models.map((_, i) => ({ x: S.r - 440, y: 270 + i * 156, w: 440, h: 112 }));
    countPos = { x: S.x, y: 650, w: 600, h: 80 };
  }
  const aOut = P ? { x: A.x + A.w / 2, y: A.y + A.h } : { x: A.x + A.w, y: A.y + A.h / 2 };
  const mIn = (b: B) => ({ x: b.x, y: b.y + b.h / 2 });
  const busX = S.x + 30;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P={P}>
        {direct3.map((_, i) => {
          const q = mIn(M[i]);
          const sx = P ? S.x + 24 + i * 30 : aOut.x;
          return <DrawLine key={`d${i}`} x1={sx} y1={aOut.y} x2={P ? q.x - 8 : q.x} y2={q.y} d={ease(ramp(direct, i * 0.2, i * 0.2 + 0.6))} o={1 - fade} w={4} dash="16 12" />;
        })}
        {P ? (
          <>
            <DrawLine x1={540} y1={A.y + A.h + 6} x2={540} y2={H.y - 6} d={spokes} color={CLAUDE.INK} w={6} />
            <DrawLine x1={busX} y1={H.y + H.h} x2={busX} y2={mIn(M[M.length - 1]).y} d={spokes} color={CLAUDE.INK} w={6} />
            {M.map((b, i) => <DrawLine key={`s${i}`} x1={busX} y1={mIn(b).y} x2={b.x} y2={mIn(b).y} d={spokes} color={CLAUDE.INK} w={6} />)}
          </>
        ) : (
          <>
            <DrawLine x1={aOut.x + 6} y1={aOut.y} x2={H.x - 6} y2={aOut.y} d={spokes} color={CLAUDE.INK} w={6} />
            {M.map((b, i) => <DrawLine key={`s${i}`} x1={H.x + H.w + 6} y1={mIn(b).y} x2={b.x - 6} y2={mIn(b).y} d={spokes} color={CLAUDE.INK} w={6} />)}
          </>
        )}
      </Canvas>
      <Card style={{ left: A.x, top: A.y, width: A.w, height: A.h, opacity: nodes, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: P ? 90 : 66, color: CLAUDE.INK }}>{app}</Card>
      {M.map((b, i) => {
        const more = i >= 3;
        return (
          <Card key={models[i]} style={{
            left: b.x, top: b.y, width: b.w, height: b.h, opacity: more ? spokes : nodes,
            border: more ? `3px dashed ${CLAUDE.GHOST}` : undefined,
            display: 'flex', alignItems: 'center', padding: P ? '0 34px' : '0 36px',
            fontFamily: more ? SANS : SERIF, fontSize: more ? (P ? 56 : 44) : (P ? 90 : 60), color: more ? CLAUDE.INK_SOFT : CLAUDE.INK,
          }}>{models[i]}</Card>
        );
      })}
      <Hub x={H.x} y={H.y} w={H.w} h={H.h} a={hubA} grow={P ? 'x' : 'y'}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 100 : 80, lineHeight: 1 }}>{hub}</span>
        <span style={{ fontFamily: SANS, fontSize: P ? 56 : 46, marginTop: P ? 6 : 18 }}>{hubSub}</span>
      </Hub>
      <div style={{
        position: 'absolute', left: countPos.x, top: countPos.y, width: countPos.w, textAlign: 'center',
        fontFamily: SERIF, fontSize: P ? 80 : 64, color: fade < 0.5 ? CLAUDE.INK : ACC_TEXT, opacity: countA,
      }}>{countTxt}</div>
      <Spark st={st} text={sparkLine} at={0.82} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// BedrockManaged — the infrastructure moves from "you handle" to "AWS handles"
// ===========================================================================
export const bedrockManagedSchema = z.object({
  title: z.string().default('No servers to manage'),
  youHead: z.string().default('you handle'),
  awsHead: z.string().default('AWS handles'),
  yours: z.array(z.string()).default(['your app', 'your prompts']),
  infra: z.array(z.string()).default(['GPU servers', 'scaling', 'patching', 'uptime']),
  badge: z.string().default('fully managed'),
  youLeft: z.string().default('you just send requests'),
  sparkLine: z.string().default('Nothing to provision.'),
  durationSeconds: z.number().optional(),
});
export const bedrockManagedMeta = durMeta(5);
export const BedrockManaged: React.FC<z.infer<typeof bedrockManagedSchema>> = ({ title, youHead, awsHead, yours, infra, badge, youLeft, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cardsIn = ease(ramp(t, 0.02, 0.1));
  const moveAt = (i: number) => 0.3 + i * 0.06;
  const done = ease(ramp(t, 0.62, 0.7));
  const gap = P ? 30 : 88;
  const cw = (S.w - gap) / 2;
  const top = P ? 290 : 250, ch = P ? 1000 : 700;
  const headH = P ? 140 : 90, barH = P ? 112 : 84, barGap = P ? 20 : 14, pad = P ? 22 : 30;
  const Lx = S.x, Rx = S.x + cw + gap;
  const slotY = (k: number) => top + headH + k * (barH + barGap);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: Lx, top, width: cw, height: ch, opacity: cardsIn }} />
      <Card accent={done > 0.5} style={{ left: Rx, top, width: cw, height: ch, opacity: cardsIn, background: CLAUDE.FOOTER }} />
      {[youHead, awsHead].map((h, c) => (
        <div key={h} style={{
          position: 'absolute', left: (c ? Rx : Lx) + pad, top: top + (P ? 24 : 22), width: cw - 2 * pad,
          fontFamily: SERIF, fontSize: P ? 72 : 56, color: CLAUDE.INK, opacity: cardsIn, lineHeight: 1, whiteSpace: 'nowrap',
        }}>{h}</div>
      ))}
      {yours.map((y, k) => (
        <Card key={y} style={{
          left: Lx + pad, top: slotY(k), width: cw - 2 * pad, height: barH, opacity: cardsIn,
          display: 'flex', alignItems: 'center', padding: '0 28px', fontFamily: SANS, fontSize: P ? 58 : 46, color: CLAUDE.INK,
        }}>{y}</Card>
      ))}
      {infra.map((label, i) => {
        const m = ease(ramp(t, moveAt(i), moveAt(i) + 0.12));
        const x0 = Lx + pad, y0 = slotY(yours.length + i);
        const x1 = Rx + pad, y1 = slotY(i);
        return (
          <Card key={label} style={{
            left: x0 + (x1 - x0) * m, top: y0 + (y1 - y0) * m, width: cw - 2 * pad, height: barH, opacity: cardsIn,
            border: `3px dashed ${m > 0.99 ? CLAUDE.BORDER : CLAUDE.GHOST}`,
            display: 'flex', alignItems: 'center', padding: '0 28px', fontFamily: SANS, fontSize: P ? 58 : 46, color: CLAUDE.INK,
          }}>{label}</Card>
        );
      })}
      <div style={{
        position: 'absolute', left: Rx + pad, top: slotY(infra.length) + (P ? 20 : 16), width: cw - 2 * pad, textAlign: 'center',
        opacity: done, fontFamily: SANS, fontSize: P ? 58 : 46, color: ACC_TEXT, fontWeight: 600,
      }}>✓ {badge}</div>
      <div style={{
        position: 'absolute', left: Lx + pad, top: slotY(yours.length) + (P ? 40 : 60), width: cw - 2 * pad, textAlign: 'center',
        opacity: done, fontFamily: SERIF, fontSize: P ? 90 : 64, color: CLAUDE.INK, lineHeight: 1.1,
      }}>{youLeft}</div>
      <Spark st={st} text={sparkLine} at={0.82} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// BedrockCapabilities — guardrails, fine-tuning and agents on the same platform
// ===========================================================================
const capSchema = z.object({ name: z.string(), what: z.string(), api: z.string() });
export const bedrockCapabilitiesSchema = z.object({
  title: z.string().default('Built into the same platform'),
  caps: z.array(capSchema).default([
    { name: 'Guardrails', what: 'filter harmful content, block topics, mask PII', api: 'guardrailConfig' },
    { name: 'Fine-tuning', what: 'customize a model on your own data', api: 'CreateModelCustomizationJob' },
    { name: 'Agents', what: 'multi-step tasks that call your APIs', api: 'InvokeAgent' },
  ]),
  base: z.string().default('all through Bedrock'),
  note: z.string().default('API names: boto3 service models · fine-tuning: supported models'),
  sparkLine: z.string().default('Safety, tuning, agents.'),
  durationSeconds: z.number().optional(),
});
export const bedrockCapabilitiesMeta = durMeta(5);

// shield / tuning sliders / agent steps, drawn in one stroke weight
const CapGlyph: React.FC<{ kind: number; s: number; color: string }> = ({ kind, s, color }) => {
  const w = 6;
  if (kind === 0) return (
    <g stroke={color} strokeWidth={w} fill="none" strokeLinejoin="round">
      <path d={`M0 ${-s * 0.46} L${s * 0.38} ${-s * 0.3} L${s * 0.34} ${s * 0.12} Q0 ${s * 0.46} 0 ${s * 0.46} Q0 ${s * 0.46} ${-s * 0.34} ${s * 0.12} L${-s * 0.38} ${-s * 0.3} Z`} />
      <path d={`M${-s * 0.16} 0 L${-s * 0.03} ${s * 0.13} L${s * 0.18} ${-s * 0.12}`} strokeLinecap="round" />
    </g>
  );
  if (kind === 1) return (
    <g stroke={color} strokeWidth={w} fill="none" strokeLinecap="round">
      {[-0.26, 0, 0.26].map((x, i) => (
        <React.Fragment key={i}>
          <line x1={s * x} y1={-s * 0.4} x2={s * x} y2={s * 0.4} />
          <rect x={s * x - s * 0.08} y={s * [0.1, -0.24, 0.2][i] - s * 0.06} width={s * 0.16} height={s * 0.12} rx={4} fill={CLAUDE.CARD} />
        </React.Fragment>
      ))}
    </g>
  );
  return (
    <g stroke={color} strokeWidth={w} fill="none" strokeLinecap="round">
      <circle cx={-s * 0.3} cy={s * 0.24} r={s * 0.12} />
      <circle cx={0} cy={-s * 0.24} r={s * 0.12} />
      <circle cx={s * 0.3} cy={s * 0.24} r={s * 0.12} />
      <line x1={-s * 0.22} y1={s * 0.14} x2={-s * 0.08} y2={-s * 0.14} />
      <line x1={s * 0.08} y1={-s * 0.14} x2={s * 0.22} y2={s * 0.14} />
    </g>
  );
};

export const BedrockCapabilities: React.FC<z.infer<typeof bedrockCapabilitiesSchema>> = ({ title, caps, base, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const capAt = (i: number) => 0.06 + i * 0.18;
  const baseA = ease(ramp(t, 0.62, 0.72));
  const top = P ? 290 : 240, rowH = P ? 280 : 172, gap = P ? 16 : 22;
  const icon = P ? 150 : 140;
  const baseY = top + caps.length * (rowH + gap) + (P ? 4 : 0);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {caps.map((c, i) => {
        const a = ease(ramp(t, capAt(i), capAt(i) + 0.08));
        const on = t >= capAt(i) && t < capAt(i + 1) + 0.02 && baseA < 0.5;
        const y = top + i * (rowH + gap);
        return (
          <Card key={c.name} accent={on} style={{
            left: S.x, top: y, width: S.w, height: rowH, opacity: a, transform: `translateX(${(1 - a) * 30}px)`,
            display: 'flex', alignItems: 'center', gap: P ? 26 : 34, padding: P ? '0 30px' : '0 40px',
          }}>
            <svg width={icon} height={icon} style={{ flex: 'none' }}>
              <g transform={`translate(${icon / 2} ${icon / 2})`}><CapGlyph kind={i} s={icon * 0.86} color={on ? CLAUDE.SPARK : CLAUDE.INK} /></g>
            </svg>
            {P ? (
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ fontFamily: SERIF, fontSize: 92, color: CLAUDE.INK, lineHeight: 1 }}>{c.name}</div>
                <div style={{ fontFamily: SANS, fontSize: 52, color: CLAUDE.INK, marginTop: 12, lineHeight: 1.15 }}>{c.what}</div>
                <div style={{ fontFamily: MONO, fontSize: 40, color: CLAUDE.INK_SOFT, marginTop: 12, whiteSpace: 'nowrap' }}>{c.api}</div>
              </div>
            ) : (
              <>
                <div style={{ width: 640, flex: 'none' }}>
                  <div style={{ fontFamily: SERIF, fontSize: 64, color: CLAUDE.INK, lineHeight: 1 }}>{c.name}</div>
                  <div style={{ fontFamily: MONO, fontSize: 38, color: CLAUDE.INK_SOFT, marginTop: 14, whiteSpace: 'nowrap' }}>{c.api}</div>
                </div>
                <div style={{ flex: 1, fontFamily: SANS, fontSize: 46, color: CLAUDE.INK, lineHeight: 1.15 }}>{c.what}</div>
              </>
            )}
          </Card>
        );
      })}
      <Hub x={S.x} y={baseY} w={S.w} h={P ? 110 : 96} a={baseA} grow="x">
        <span style={{ fontFamily: SERIF, fontSize: P ? 76 : 56 }}>{base}</span>
      </Hub>
      {!P && <Note P={P} x={S.x} y={top - 50} w={S.w} a={ease(ramp(t, 0.06, 0.14))} align="right" text={note} />}
      <Spark st={st} text={sparkLine} at={0.84} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// BedrockSwap — one converse() call; only the modelId string changes
// ===========================================================================
export const bedrockSwapSchema = z.object({
  title: z.string().default('Switch with one string'),
  modelIds: z.array(z.string()).default([
    'anthropic.claude-3-haiku-20240307-v1:0',
    'meta.llama3-8b-instruct-v1:0',
    'amazon.titan-text-express-v1',
  ]),
  names: z.array(z.string()).default(['Claude', 'Llama', 'Titan']),
  ok: z.string().default('same call ✓'),
  unchanged: z.string().default('everything else: unchanged'),
  caption: z.string().default('request shape validated offline against botocore · no AWS call · evidence/converse_shape.py'),
  sparkLine: z.string().default('Change the ID, keep the code.'),
  durationSeconds: z.number().optional(),
});
export const bedrockSwapMeta = durMeta(5);
export const BedrockSwap: React.FC<z.infer<typeof bedrockSwapSchema>> = ({ title, modelIds, names, ok, unchanged, caption, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = modelIds.length;
  const codeIn = ease(ramp(t, 0.02, 0.1));
  // each id holds for a slot; the next one types over it
  const slot0 = 0.1, slotW = 0.2;
  const idx = Math.max(0, Math.min(n - 1, Math.floor((t - slot0) / slotW)));
  const typeP = idx === 0 ? 1 : ease(ramp(t, slot0 + idx * slotW, slot0 + idx * slotW + 0.07));
  const id = modelIds[idx];
  const shown = id.slice(0, Math.round(id.length * typeP));
  const unA = ease(ramp(t, 0.7, 0.78));
  const fs = P ? 44 : 48;
  const lineH = fs * 1.55;
  const Hi: React.FC<{ children: React.ReactNode }> = ({ children }) => (
    <div style={{ borderLeft: `8px solid ${CLAUDE.SPARK}`, marginLeft: -28, paddingLeft: 20, background: '#FBF1EC' }}>{children}</div>
  );
  const dot = shown.indexOf('.');
  const idLines = P ? (dot >= 0 ? [shown.slice(0, dot + 1), shown.slice(dot + 1)] : [shown, '']) : [shown];
  const code = (
    <div style={{ fontFamily: MONO, fontSize: fs, lineHeight: `${lineH}px`, color: CLAUDE.INK, whiteSpace: 'pre' }}>
      <div>{'response = client.converse('}</div>
      <Hi>
        {P ? (
          <>
            <div>{'  modelId='}</div>
            <div>{'    "'}{idLines[0]}</div>
            <div>{'    '}{idLines[1]}{typeP >= 1 ? '",' : ''}</div>
          </>
        ) : (
          <div>{'    modelId="'}{shown}{typeP >= 1 ? '",' : ''}</div>
        )}
      </Hi>
      <div>{P ? '  messages=messages,' : '    messages=messages,'}</div>
      <div>{')'}</div>
    </div>
  );
  const cardB = P ? { x: S.x, y: 290, w: S.w, h: 6 * lineH + 70 } : { x: S.x, y: 250, w: S.w, h: 4 * lineH + 80 };
  const chipTop = cardB.y + cardB.h + (P ? 30 : 28);
  const chipH = P ? 104 : 120, chipGap = P ? 16 : 40;
  const chipW = P ? S.w : (S.w - chipGap * (n - 1)) / n;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: cardB.x, top: cardB.y, width: cardB.w, height: cardB.h, padding: P ? '34px 32px' : '40px 48px', opacity: codeIn }}>{code}</Card>
      {names.map((nm, i) => {
        const a = ease(ramp(t, slot0 + i * slotW + (i === 0 ? 0.04 : 0.08), slot0 + i * slotW + (i === 0 ? 0.1 : 0.14)));
        const pos = P ? { x: S.x, y: chipTop + i * (chipH + chipGap) } : { x: S.x + i * (chipW + chipGap), y: chipTop };
        return (
          <Card key={nm} accent={i === idx && unA < 0.5} style={{
            left: pos.x, top: pos.y, width: chipW, height: chipH, opacity: a,
            display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: P ? '0 34px' : '0 36px',
          }}>
            <span style={{ fontFamily: SERIF, fontSize: P ? 90 : 60, color: CLAUDE.INK }}>{nm}</span>
            <span style={{ fontFamily: SANS, fontSize: P ? 56 : 44, color: CLAUDE.INK_SOFT }}>{ok}</span>
          </Card>
        );
      })}
      <div style={{
        position: 'absolute', left: S.x, width: S.w, textAlign: 'center',
        top: P ? chipTop + n * (chipH + chipGap) + 4 : chipTop + chipH + 18,
        fontFamily: SERIF, fontSize: P ? 76 : 58, color: ACC_TEXT, opacity: unA,
      }}>{unchanged}</div>
      {!P && <Note P={P} x={S.x} y={chipTop + chipH + 96} w={S.w} a={unA} align="center" text={caption} />}
      <Spark st={st} text={sparkLine} at={0.86} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// BedrockCombine — a small model sorts, a stronger one replies, one integration
// ===========================================================================
const stepSchema = z.object({ task: z.string(), model: z.string() });
export const bedrockCombineSchema = z.object({
  title: z.string().default('Or combine them'),
  input: z.string().default('support ticket'),
  steps: z.array(stepSchema).default([
    { task: 'sort it', model: 'small, fast model' },
    { task: 'write the reply', model: 'stronger model' },
  ]),
  output: z.string().default('reply draft'),
  hub: z.string().default('one Bedrock integration'),
  note: z.string().default('illustrative pairing'),
  sparkLine: z.string().default('Mix models, one integration.'),
  durationSeconds: z.number().optional(),
});
export const bedrockCombineMeta = durMeta(5);
export const BedrockCombine: React.FC<z.infer<typeof bedrockCombineSchema>> = ({ title, input, steps, output, hub, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const at = [0.04, 0.16, 0.32, 0.48];   // input, step 1, step 2, output
  const A = at.map((a) => ease(ramp(t, a, a + 0.08)));
  const hubA = ease(ramp(t, 0.58, 0.68));
  type B = { x: number; y: number; w: number; h: number };
  let boxes: B[], H: B;
  if (P) {
    boxes = [
      { x: S.x, y: 290, w: S.w, h: 100 },
      { x: S.x, y: 420, w: S.w, h: 250 },
      { x: S.x, y: 700, w: S.w, h: 250 },
      { x: S.x, y: 980, w: S.w, h: 100 },
    ];
    H = { x: S.x, y: 1105, w: S.w, h: 100 };
  } else {
    const g = 64, ew = 300, sw = (S.w - 2 * ew - 3 * g) / 2;
    const y = 300, h = 270;
    boxes = [
      { x: S.x, y: y + 35, w: ew, h: h - 70 },
      { x: S.x + ew + g, y, w: sw, h },
      { x: S.x + ew + g + sw + g, y, w: sw, h },
      { x: S.r - ew, y: y + 35, w: ew, h: h - 70 },
    ];
    H = { x: boxes[1].x, y: 700, w: boxes[2].x + sw - boxes[1].x, h: 120 };
  }
  const ends = [input, '', '', output];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P={P}>
        {[0, 1, 2].map((k) => {
          const a = boxes[k], b = boxes[k + 1];
          const d = ease(ramp(t, at[k + 1] - 0.05, at[k + 1] + 0.03));
          return P
            ? <DrawLine key={k} x1={540} y1={a.y + a.h + 6} x2={540} y2={b.y - 6} d={d} color={CLAUDE.INK} w={6} />
            : <DrawLine key={k} x1={a.x + a.w + 8} y1={a.y + a.h / 2} x2={b.x - 8} y2={b.y + b.h / 2} d={d} color={CLAUDE.INK} w={6} />;
        })}
        {!P && [1, 2].map((k) => (
          <DrawLine key={`h${k}`} x1={boxes[k].x + boxes[k].w / 2} y1={boxes[k].y + boxes[k].h + 6} x2={boxes[k].x + boxes[k].w / 2} y2={H.y - 6} d={hubA} color={CLAUDE.SPARK} w={6} />
        ))}
      </Canvas>
      {boxes.map((b, i) => {
        const isStep = i === 1 || i === 2;
        const s = steps[i - 1];
        return (
          <Card key={i} accent={isStep && hubA > 0.5} style={{
            left: b.x, top: b.y, width: b.w, height: b.h, opacity: A[i], transform: `translateY(${(1 - A[i]) * 16}px)`,
            display: 'flex', flexDirection: 'column', alignItems: isStep ? 'flex-start' : 'center', justifyContent: 'center',
            padding: P ? '0 34px' : '0 36px', background: isStep ? CLAUDE.CARD : CLAUDE.FOOTER,
          }}>
            {isStep ? (
              <>
                <div style={{ fontFamily: SANS, fontSize: P ? 52 : 40, color: CLAUDE.INK_SOFT }}>step {i}</div>
                <div style={{ fontFamily: SERIF, fontSize: P ? 92 : 64, color: CLAUDE.INK, lineHeight: 1.05, marginTop: 6 }}>{s.task}</div>
                <div style={{ fontFamily: SANS, fontSize: P ? 56 : 44, color: CLAUDE.INK, marginTop: 12 }}>{s.model}</div>
              </>
            ) : (
              <div style={{ fontFamily: SANS, fontSize: P ? 60 : 46, color: CLAUDE.INK, textAlign: 'center', lineHeight: 1.15 }}>{ends[i]}</div>
            )}
          </Card>
        );
      })}
      <Hub x={H.x} y={H.y} w={H.w} h={H.h} a={hubA} grow="x">
        <span style={{ fontFamily: SERIF, fontSize: P ? 72 : 60 }}>{hub}</span>
      </Hub>
      <Note P={P} x={P ? S.x : S.x} y={P ? H.y + H.h + 12 : H.y + H.h + 22} w={P ? S.w : H.x + H.w - S.x} a={hubA} align="right" text={note} />
      <Spark st={st} text={sparkLine} at={0.84} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
