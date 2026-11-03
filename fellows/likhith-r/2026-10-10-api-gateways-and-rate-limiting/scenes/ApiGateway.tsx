/**
 * ApiGateway.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-api-gateways ("API Gateways and Rate Limiting", @HumanitariansAI).
 *
 * Same contract as KvCache.tsx / JevExplainer.tsx (whose stage helpers it reuses):
 * each component lays out natively for 16:9 (<Name>) and 9:16 (<Name>916) — never
 * a crop — and every motion is a pure function of progress, conformed via
 * `durationSeconds`. Service names, keys, limits and traffic are illustrative and
 * labelled so on screen. The token-bucket and window outcomes are computed in-scene
 * from those toy inputs (deterministic), never hand-placed.
 *
 *   GwHook          — ten services, each stamping its own auth / log / limit (30 copies)
 *   GwFrontDoor     — clients → one gateway → services; the copies merge into it (30 → 3)
 *   GwPipeline      — one request walks authenticate → route → log
 *   GwRateLimit     — one client fires 10 requests at a 5/second cap: 5 pass, 5 get 429
 *   GwTokenBucket   — a 5-token bucket: the burst passes, the steady flood runs dry
 *   GwSlidingWindow — fixed window lets 5 + 5 through at the reset edge; sliding does not
 *   GwAiQuota       — shared model capacity with and without per-user limits
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const Pill: React.FC<{ text: string; size: number; a?: number; accent?: boolean; fill?: string; style?: React.CSSProperties }> = ({ text, size, a = 1, accent, fill, style }) => (
  <span style={{
    display: 'inline-block', padding: `${size * 0.16}px ${size * 0.42}px`, borderRadius: size, boxSizing: 'border-box',
    background: fill ?? (accent ? ACC_TEXT : CLAUDE.INK),
    fontFamily: SANS, fontSize: size, lineHeight: 1.1, color: CLAUDE.CARD, opacity: a, whiteSpace: 'nowrap', ...style,
  }}>{text}</span>
);

const Txt: React.FC<{ text: string; style?: React.CSSProperties }> = ({ text, style }) => (
  <div style={{ position: 'absolute', fontFamily: SANS, fontSize: 36, color: CLAUDE.INK_SOFT, ...style }}>{text}</div>
);

const lerp = (a: number, b: number, p: number) => a + (b - a) * p;
const mmss = (s: number) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;

const SERVICES = ['users', 'orders', 'search', 'cart', 'billing', 'media', 'notify', 'maps', 'reviews', 'ai'];
const CONCERNS = ['auth', 'log', 'limit'];

// ===========================================================================
// GwHook — ten services, each building its own auth, logging and limits
// ===========================================================================
export const gwHookSchema = z.object({
  title: z.string().default('Ten services, ten copies'),
  services: z.array(z.string()).default(SERVICES),
  concerns: z.array(z.string()).default(CONCERNS),
  counterLabel: z.string().default('copies of the same three jobs'),
  counterNote: z.string().default('10 services × auth, log, limit'),
  sparkLine: z.string().default('Ten copies of everything?'),
  durationSeconds: z.number().optional(),
});
export const gwHookMeta = durMeta(6);
export const GwHook: React.FC<z.infer<typeof gwHookSchema>> = ({ title, services, concerns, counterLabel, counterNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cols = P ? 2 : 5;
  const top = P ? 320 : 240;
  const gap = P ? 14 : 24;
  const counterW = P ? 0 : 420;
  const gridW = P ? S.w : S.w - counterW - 60;
  const cw = (gridW - gap * (cols - 1)) / cols;
  const ch = P ? 166 : 330;
  const stampAt = (i: number, k: number) => 0.1 + i * 0.03 + k * 0.01;
  let copies = 0;
  const cards = services.map((name, i) => {
    const x = S.x + (i % cols) * (cw + gap);
    const y = top + Math.floor(i / cols) * (ch + gap);
    const a = ease(ramp(t, 0.03 + i * 0.012, 0.1 + i * 0.012));
    return (
      <Card key={name} style={{
        left: x, top: y, width: cw, height: ch, padding: P ? '14px 22px' : '24px 22px', opacity: a,
        display: 'flex', flexDirection: 'column', gap: P ? 10 : 16, alignItems: 'flex-start',
      }}>
        <Pill text={name} size={P ? 50 : 46} style={{ fontFamily: SERIF, borderRadius: 10 }} />
        <div style={{ display: 'flex', flexDirection: P ? 'row' : 'column', gap: P ? 8 : 14, alignItems: 'flex-start' }}>
          {concerns.map((c, k) => {
            const b = ease(ramp(t, stampAt(i, k), stampAt(i, k) + 0.03));
            if (b > 0.5) copies += 1;
            return <Pill key={c} text={c} size={P ? 48 : 40} a={b} fill={CLAUDE.INK_SOFT} style={{ transform: `scale(${1 + 0.4 * (1 - b)})`, transformOrigin: 'left center' }} />;
          })}
        </div>
      </Card>
    );
  });
  const cIn = ease(ramp(t, 0.1, 0.18));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {cards}
      {P ? (
        <div style={{ position: 'absolute', left: S.x, top: 1226, width: S.w, display: 'flex', alignItems: 'baseline', gap: 20, opacity: cIn }}>
          <span style={{ fontFamily: SERIF, fontSize: 96, lineHeight: 1, color: ACC_TEXT }}>{copies}</span>
          <span style={{ fontFamily: SANS, fontSize: 48, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{counterLabel}</span>
        </div>
      ) : (
        <div style={{ position: 'absolute', left: S.x + gridW + 60, top: top + 60, width: counterW, opacity: cIn }}>
          <div style={{ fontFamily: SERIF, fontSize: 220, lineHeight: 1, color: ACC_TEXT }}>{copies}</div>
          <div style={{ fontFamily: SANS, fontSize: 46, color: CLAUDE.INK, marginTop: 16 }}>{counterLabel}</div>
          <div style={{ fontFamily: SANS, fontSize: 40, color: CLAUDE.INK_SOFT, marginTop: 14 }}>{counterNote}</div>
        </div>
      )}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GwFrontDoor — one gateway in front of every service; the copies merge into it
// ===========================================================================
export const gwFrontDoorSchema = z.object({
  title: z.string().default('One front door'),
  clients: z.array(z.string()).default(['web app', 'mobile', 'partner']),
  services: z.array(z.string()).default(SERVICES),
  gatewayLabel: z.string().default('API gateway'),
  concerns: z.array(z.string()).default(['auth', 'logging', 'rate limits']),
  before: z.string().default('30 copies'),
  after: z.string().default('3, shared'),
  sparkLine: z.string().default('Shared work, done once.'),
  durationSeconds: z.number().optional(),
});
export const gwFrontDoorMeta = durMeta(6);
export const GwFrontDoor: React.FC<z.infer<typeof gwFrontDoorSchema>> = ({ title, clients, services, gatewayLabel, concerns, before, after, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  // geometry — landscape: clients | gateway | services (2 cols); portrait: stacked rows
  const g = P
    ? { x: S.x, y: 520, w: S.w, h: 360 }
    : { x: 690, y: 290, w: 470, h: 600 };
  const cl = clients.map((_, i) => P
    ? { x: S.x + i * ((S.w - 40) / 3 + 20), y: 330, w: (S.w - 40) / 3, h: 104 }
    : { x: S.x, y: 360 + i * 170, w: 300, h: 120 });
  const sv = services.map((_, i) => {
    if (P) {
      const w = (S.w - 3 * 16) / 4;
      return { x: S.x + (i % 4) * (w + 16), y: 960 + Math.floor(i / 4) * 106, w, h: 92 };
    }
    return { x: 1330 + (i % 2) * 254, y: 260 + Math.floor(i / 2) * 130, w: 240, h: 108 };
  });
  const gIn = ease(ramp(t, 0.18, 0.28));
  const wire = ease(ramp(t, 0.22, 0.36));
  const fly = (i: number) => ease(ramp(t, 0.26 + i * 0.008, 0.4 + i * 0.008));
  const pills = (k: number) => ease(ramp(t, 0.34 + k * 0.03, 0.4 + k * 0.03));
  const swap = ease(ramp(t, 0.6, 0.68));
  const gcx = g.x + g.w / 2, gcy = g.y + g.h / 2;
  const lines: Array<[number, number, number, number]> = [];
  cl.forEach((c) => lines.push(P ? [c.x + c.w / 2, c.y + c.h, gcx, g.y] : [c.x + c.w, c.y + c.h / 2, g.x, gcy]));
  sv.forEach((s, i) => {
    if (P ? i < 4 : i % 2 === 0) lines.push(P ? [gcx, g.y + g.h, s.x + s.w / 2, s.y] : [g.x + g.w, gcy, s.x, s.y + s.h / 2]);
  });
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <svg width={P ? 1080 : 1920} height={P ? 1920 : 1080} style={{ position: 'absolute', left: 0, top: 0 }}>
        {lines.map(([x1, y1, x2, y2], i) => {
          const len = Math.hypot(x2 - x1, y2 - y1);
          return <line key={i} x1={x1} y1={y1} x2={x2} y2={y2} stroke={CLAUDE.GHOST} strokeWidth={4}
            strokeDasharray={len} strokeDashoffset={len * (1 - wire)} />;
        })}
      </svg>
      {clients.map((c, i) => (
        <Card key={c} style={{ left: cl[i].x, top: cl[i].y, width: cl[i].w, height: cl[i].h, display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontFamily: SANS, fontSize: P ? 48 : 42, color: CLAUDE.INK, opacity: ease(ramp(t, 0.03 + i * 0.03, 0.1 + i * 0.03)) }}>{c}</Card>
      ))}
      {services.map((s, i) => {
        const r = sv[i];
        return (
          <Card key={s} style={{ left: r.x, top: r.y, width: r.w, height: r.h, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: P ? 4 : 10,
            fontFamily: SANS, fontSize: P ? 48 : 38, color: CLAUDE.INK, opacity: ease(ramp(t, 0.04 + i * 0.01, 0.1 + i * 0.01)) }}>
            <span>{s}</span>
            {/* the service's own auth/log/limit copies — they lift off toward the gateway */}
            <div style={{ display: 'flex', gap: 8, height: P ? 12 : 16 }}>
              {[0, 1, 2].map((k) => <div key={k} style={{ width: P ? 12 : 16, height: P ? 12 : 16, borderRadius: 4, background: CLAUDE.INK_SOFT, opacity: 1 - fly(i) }} />)}
            </div>
          </Card>
        );
      })}
      {services.map((s, i) => {
        const r = sv[i];
        const p = fly(i);
        if (p <= 0 || p >= 1) return null;
        return [0, 1, 2].map((k) => {
          const x = lerp(r.x + r.w / 2 - 28 + k * 24, gcx - 28 + k * 24, p);
          const y = lerp(r.y + r.h - 34, gcy, p);
          return <div key={`${s}${k}`} style={{ position: 'absolute', left: x, top: y, width: 16, height: 16, borderRadius: 4, background: CLAUDE.INK_SOFT, opacity: 1 - ramp(p, 0.75, 1) }} />;
        });
      })}
      <Card accent style={{ left: g.x, top: g.y, width: g.w, height: g.h, opacity: gIn, padding: P ? '24px 36px' : '34px 36px',
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: P ? 18 : 26 }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 88 : 62, lineHeight: 1.05, color: CLAUDE.INK }}>{gatewayLabel}</div>
        <div style={{ display: 'flex', flexDirection: P ? 'row' : 'column', gap: P ? 16 : 18, alignItems: 'center' }}>
          {concerns.map((c, k) => <Pill key={c} text={c} size={P ? 48 : 44} a={pills(k)} />)}
        </div>
        <div style={{ marginTop: 'auto', fontFamily: SANS, fontSize: P ? 50 : 44, color: CLAUDE.INK, opacity: ease(ramp(t, 0.56, 0.62)),
          display: 'flex', flexDirection: P ? 'row' : 'column', gap: P ? 18 : 6, alignItems: 'center', whiteSpace: 'nowrap' }}>
          <span style={{ color: CLAUDE.INK_SOFT, textDecoration: swap > 0.5 ? 'line-through' : 'none' }}>{before}</span>
          <span style={{ opacity: swap, color: ACC_TEXT, fontWeight: 600 }}>→ {after}</span>
        </div>
      </Card>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GwPipeline — one request walks authenticate → route → log
// ===========================================================================
export const gwPipelineSchema = z.object({
  title: z.string().default('Every request, three checks'),
  request: z.string().default('GET /orders · key ab12'),
  routes: z.array(z.tuple([z.string(), z.string()])).default([['/users', 'users'], ['/orders', 'orders'], ['/search', 'search']]),
  match: z.number().default(1),
  logLines: z.array(z.string()).default(['12:00:01 user 42', 'GET /orders → 200', '38 ms']),
  toyNote: z.string().default('illustrative request'),
  sparkLine: z.string().default('Check, route, log.'),
  durationSeconds: z.number().optional(),
});
export const gwPipelineMeta = durMeta(5);
export const GwPipeline: React.FC<z.infer<typeof gwPipelineSchema>> = ({ title, request, routes, match, logLines, toyNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const T = [0.1, 0.36, 0.6];                       // each stage goes live
  const stage = t < T[1] ? 0 : t < T[2] ? 1 : 2;
  const gap = P ? 18 : 40;
  const top = P ? 410 : 350;
  const w = P ? S.w : (S.w - 2 * gap) / 3;
  const PH = [240, 300, 306];
  const hOf = (i: number) => P ? PH[i] : 560;
  const box = (i: number) => P ? { x: S.x, y: top + PH.slice(0, i).reduce((a, b) => a + b + gap, 0) } : { x: S.x + i * (w + gap), y: top };
  // packet: landscape travels over the stages; portrait waits above them
  const hop = (i: number) => ease(ramp(t, T[i] - 0.05, T[i]));
  const pk = P ? { x: S.x, y: 314 } : { x: S.x + (w + gap) * (hop(1) + hop(2)) + (w - 520) / 2, y: 238 };
  const head = (n: number, name: string, q: string) => (
    <div style={{ display: 'flex', alignItems: 'baseline', gap: 18, flexWrap: 'wrap' }}>
      <span style={{ fontFamily: SERIF, fontSize: P ? 52 : 56, color: CLAUDE.INK }}>{n}. {name}</span>
      <span style={{ fontFamily: SANS, fontSize: P ? 48 : 36, color: CLAUDE.INK_SOFT }}>{q}</span>
    </div>
  );
  const ok = ease(ramp(t, 0.22, 0.28));
  const hit = ease(ramp(t, 0.44, 0.5));
  const typed = ramp(t, 0.64, 0.8);
  const logText = logLines.join('\n');
  const shown = logText.slice(0, Math.floor(typed * logText.length));
  const mono = P ? 46 : 44;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: pk.x, top: pk.y, width: P ? S.w : 520, height: P ? 76 : 84, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 20,
        fontFamily: MONO, fontSize: P ? 44 : 36, color: CLAUDE.INK, opacity: ease(ramp(t, 0.02, 0.08)) }}>
        <span>{request}</span>
        {P && <span style={{ fontFamily: SANS, fontSize: 48, color: CLAUDE.INK_SOFT }}>· step {stage + 1}</span>}
      </Card>
      {[0, 1, 2].map((i) => {
        const b = box(i);
        const live = ease(ramp(t, T[i], T[i] + 0.06));
        return (
          <Card key={i} style={{ left: b.x, top: b.y, width: w, height: hOf(i), padding: P ? '16px 30px' : '30px 34px',
            border: `${stage === i ? 5 : 3}px solid ${stage === i ? CLAUDE.INK : CLAUDE.BORDER}`,
            opacity: 0.45 + 0.55 * ease(ramp(t, 0.04 + i * 0.03, 0.1 + i * 0.03)) * (0.6 + 0.4 * live),
            display: 'flex', flexDirection: 'column', gap: P ? 8 : 34 }}>
            {i === 0 && <>
              {head(1, 'Authenticate', 'who are you?')}
              <div style={{ fontFamily: MONO, fontSize: mono, color: CLAUDE.INK, opacity: live }}>API key ab12</div>
              <div style={{ fontFamily: SANS, fontSize: P ? 48 : 46, color: CLAUDE.INK, opacity: ok }}>✓ valid · user 42</div>
            </>}
            {i === 1 && <>
              {head(2, 'Route', 'which backend?')}
              <div style={{ display: 'flex', flexDirection: 'column', gap: P ? 2 : 14, opacity: live }}>
                {routes.map(([path, svc], r) => (
                  <div key={path} style={{ fontFamily: MONO, fontSize: mono, padding: P ? '1px 14px' : '4px 14px', borderRadius: 10,
                    color: r === match && hit > 0.5 ? CLAUDE.CARD : CLAUDE.INK, background: r === match && hit > 0.5 ? CLAUDE.INK : 'transparent',
                    opacity: r === match ? 1 : 1 - 0.45 * hit }}>{path} → {svc}</div>
                ))}
              </div>
            </>}
            {i === 2 && <>
              {head(3, 'Log', 'what happened?')}
              <div style={{ fontFamily: MONO, fontSize: mono, lineHeight: 1.35, color: CLAUDE.INK, whiteSpace: 'pre-wrap' }}>{shown}</div>
            </>}
          </Card>
        );
      })}
      {!P && <Txt text={toyNote} style={{ right: 1920 - S.r, top: S.y + 60, fontSize: 32 }} />}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GwRateLimit — 10 requests at a 5-per-second cap: 5 pass, 5 bounce with 429
// ===========================================================================
export const gwRateLimitSchema = z.object({
  title: z.string().default('Rate limiting'),
  requests: z.number().default(10),
  limit: z.number().default(5),
  limitLabel: z.string().default('limit: 5 requests per second'),
  rejectLabel: z.string().default('429 Too Many Requests'),
  toyNote: z.string().default('illustrative limit'),
  sparkLine: z.string().default('A cap per client.'),
  durationSeconds: z.number().optional(),
});
export const gwRateLimitMeta = durMeta(6);
export const GwRateLimit: React.FC<z.infer<typeof gwRateLimitSchema>> = ({ title, requests, limit, limitLabel, rejectLabel, toyNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const launch = (i: number) => 0.08 + i * 0.045;
  const leg = 0.07;
  // landscape: left → right; portrait: top → bottom. Positions along the main axis.
  const client = P ? { x: S.x, y: 350, w: 520, h: 160 } : { x: S.x, y: 470, w: 340, h: 150 };
  const gate = P ? 780 : 900;                       // gate position on the main axis
  const backend = P ? { x: S.x, y: 920, w: S.w, h: 310 } : { x: S.r - 460, y: 400, w: 460, h: 300 };
  const start = P ? client.y + client.h : client.x + client.w;
  const end = P ? backend.y : backend.x;
  const lane = P ? S.x + 160 : 545;                 // cross-axis lane centre
  let passed = 0; let seen = 0;
  const dots: React.ReactNode[] = [];
  const chips: React.ReactNode[] = [];
  for (let i = 0; i < requests; i++) {
    const t0 = launch(i);
    if (t < t0) continue;
    const ok = i < limit;
    const p1 = ease(ramp(t, t0, t0 + leg));
    const arrived = t >= t0 + leg;
    if (arrived) { seen += 1; if (ok) passed += 1; }
    const jitter = ((i % 3) - 1) * (P ? 30 : 40);
    if (!arrived || ok) {
      const p2 = ok ? ease(ramp(t, t0 + leg, t0 + 2 * leg)) : 0;
      const along = p2 > 0 ? lerp(gate, end, p2) : lerp(start, gate, p1);
      const fade = 1 - ramp(p2, 0.8, 1);
      if (fade > 0) {
        const r = 22;
        dots.push(<div key={i} style={{ position: 'absolute', width: 2 * r, height: 2 * r, borderRadius: r, background: CLAUDE.INK, opacity: fade,
          left: (P ? lane + jitter : along) - r, top: (P ? along : lane + jitter) - r }} />);
      }
    } else {
      // rejected: becomes a 429 chip and settles into the pile before the gate
      const k = i - limit;
      const s = ease(ramp(t, t0 + leg, t0 + leg + 0.06));
      const px = P ? S.x + 330 + k * 128 : gate - 150 - (requests - limit - 1 - k) * 128;
      const py = P ? 580 : 730;
      const fromX = P ? lane + jitter : gate - 40, fromY = P ? gate - 40 : lane + jitter;
      chips.push(<div key={i} style={{ position: 'absolute', left: lerp(fromX, px, s), top: lerp(fromY, py, s), width: 116, height: P ? 72 : 64, borderRadius: 12,
        border: `3px dashed ${CLAUDE.GHOST}`, boxSizing: 'border-box', display: 'flex', alignItems: 'center', justifyContent: 'center',
        fontFamily: MONO, fontSize: P ? 48 : 36, color: ACC_TEXT, background: CLAUDE.CARD }}>429</div>);
    }
  }
  const window = Math.min(seen, requests);
  const load = passed / limit;
  const lbl = ease(ramp(t, 0.5, 0.58));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: client.x, top: client.y, width: client.w, height: client.h, padding: '18px 26px', display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: 8,
        opacity: ease(ramp(t, 0.02, 0.08)) }}>
        <div style={{ fontFamily: SERIF, fontSize: 52, color: CLAUDE.INK }}>one client</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 48 : 36, color: CLAUDE.INK_SOFT, whiteSpace: 'nowrap' }}>{requests} requests, fast</div>
      </Card>
      <div style={{ position: 'absolute', opacity: ease(ramp(t, 0.05, 0.12)),
        ...(P ? { left: S.x + 560, top: 350, width: S.w - 560 } : { left: gate - 260, top: 236, width: 560, textAlign: 'center' as const }) }}>
        <div style={{ fontFamily: MONO, fontSize: P ? 84 : 96, lineHeight: 1, color: CLAUDE.INK }}>{Math.min(passed, limit)} / {limit}</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 48 : 36, color: CLAUDE.INK_SOFT, marginTop: 10 }}>{limitLabel}</div>
      </div>
      {dots}
      {chips}
      {/* the gate: a thin solid accent bar across the lane */}
      <div style={{ position: 'absolute', background: CLAUDE.SPARK, borderRadius: 12, opacity: ease(ramp(t, 0.03, 0.1)),
        ...(P ? { left: S.x, top: gate - 12, width: S.w, height: 24 } : { left: gate - 12, top: 420, width: 24, height: 480 }) }} />
      <Txt text={rejectLabel} style={{ opacity: lbl, fontSize: P ? 48 : 42, color: ACC_TEXT, fontWeight: 600,
        ...(P ? { left: S.x + 330, top: 668, whiteSpace: 'nowrap' as const } : { left: gate - 150 - 4 * 128, top: 820 }) }} />
      <Card style={{ left: backend.x, top: backend.y, width: backend.w, height: backend.h, padding: '24px 30px', display: 'flex', flexDirection: 'column', gap: 16,
        opacity: ease(ramp(t, 0.04, 0.1)) }}>
        <div style={{ fontFamily: SERIF, fontSize: 52, color: CLAUDE.INK }}>backend</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 48 : 36, color: CLAUDE.INK_SOFT }}>load</div>
        <div style={{ position: 'relative', flexShrink: 0, height: 40, borderRadius: 20, border: `3px solid ${CLAUDE.BORDER}`, boxSizing: 'border-box' }}>
          <div style={{ position: 'absolute', left: 4, top: 4, bottom: 4, width: `calc(${60 * load}% - 8px)`, minWidth: 0, borderRadius: 16, background: CLAUDE.INK_SOFT }} />
        </div>
        <div style={{ fontFamily: SANS, fontSize: P ? 48 : 36, color: CLAUDE.INK, opacity: lbl, whiteSpace: 'nowrap' }}>steady: {passed} of {window} passed</div>
      </Card>
      <Txt text={toyNote} style={P ? { right: 1080 - S.r, top: 1252, fontSize: 48 } : { right: 1920 - S.r, top: 730, fontSize: 32 }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GwTokenBucket — a 5-token bucket refilling one token per tick
// ===========================================================================
type BucketEvent = { at: number; kind: 'refill' | 'req'; group: 0 | 1 };
const bucketEvents = (cap: number, refillEvery: number, burst: number[], flood: number[]) => {
  const ev: BucketEvent[] = [];
  for (let u = refillEvery; u <= 100; u += refillEvery) ev.push({ at: u, kind: 'refill', group: 0 });
  burst.forEach((u) => ev.push({ at: u, kind: 'req', group: 0 }));
  flood.forEach((u) => ev.push({ at: u, kind: 'req', group: 1 }));
  // refills land before a request at the same instant
  ev.sort((a, b) => a.at - b.at || (a.kind === 'refill' ? -1 : 1));
  let tokens = cap;
  const out: Array<BucketEvent & { ok: boolean; tokensAfter: number }> = [];
  ev.forEach((e) => {
    let ok = true;
    if (e.kind === 'refill') tokens = Math.min(cap, tokens + 1);
    else if (tokens >= 1) tokens -= 1;
    else ok = false;
    out.push({ ...e, ok, tokensAfter: tokens });
  });
  return out;
};
export const gwTokenBucketSchema = z.object({
  title: z.string().default('Token bucket'),
  capacity: z.number().default(5),
  refillEvery: z.number().default(10),                                   // in hundredths of the beat
  burst: z.array(z.number()).default([14, 16, 18, 20]),
  flood: z.array(z.number()).default([46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76]),
  refillLabel: z.string().default('+1 token every tick'),
  toyNote: z.string().default('illustrative: 5 tokens, +1 per tick'),
  sparkLine: z.string().default('Bursts yes, floods no.'),
  durationSeconds: z.number().optional(),
});
export const gwTokenBucketMeta = durMeta(6);
export const GwTokenBucket: React.FC<z.infer<typeof gwTokenBucketSchema>> = ({ title, capacity, refillEvery, burst, flood, refillLabel, toyNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const u = t * 100;
  const all = bucketEvents(capacity, refillEvery, burst, flood);
  const past = all.filter((e) => e.at <= u);
  const tokens = past.length ? past[past.length - 1].tokensAfter : capacity;
  const reqs = all.filter((e) => e.kind === 'req');
  const lastRefill = [...past].reverse().find((e) => e.kind === 'refill');
  const drip = lastRefill ? 1 - ramp(u, lastRefill.at, lastRefill.at + 3) : 0;
  const passed = reqs.filter((e) => e.at <= u && e.ok).length;
  const rejected = reqs.filter((e) => e.at <= u && !e.ok).length;
  // bucket geometry
  const bw = P ? 380 : 460, bh = P ? 320 : 440;
  const bx = P ? S.x + 20 : S.x + 40, by = P ? 360 : 330;
  const r = P ? 36 : 40;
  const slots = [[0.3, 0.8], [0.5, 0.8], [0.7, 0.8], [0.4, 0.52], [0.6, 0.52]].slice(0, capacity);
  // request log geometry
  const lx = P ? S.x : S.x + 640, lw = P ? S.w : S.r - (S.x + 640);
  const chipW = P ? 140 : 88, chipH = P ? 90 : 92, cg = P ? 14 : 12;
  const perRow = P ? 6 : 11;
  const rowY = (g: number, k: number) => (P ? 930 : 330) + (g === 0 ? 0 : (P ? 150 : 200) + Math.floor(k / perRow) * (chipH + cg + 6));
  const groupIdx = [0, 0];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <svg width={bw} height={bh} style={{ position: 'absolute', left: bx, top: by, overflow: 'visible', opacity: ease(ramp(t, 0.02, 0.08)) }}>
        <path d={`M 0 ${bh * 0.25} L ${bw * 0.1} ${bh} L ${bw * 0.9} ${bh} L ${bw} ${bh * 0.25}`} fill={CLAUDE.CARD} stroke={CLAUDE.GHOST} strokeWidth={8} strokeLinejoin="round" />
        {slots.map(([sx, sy], i) => (
          <circle key={i} cx={bw * sx} cy={bh * sy} r={r} fill={i < tokens ? CLAUDE.INK : 'none'}
            stroke={i < tokens ? CLAUDE.INK : CLAUDE.GHOST} strokeWidth={4} strokeDasharray={i < tokens ? undefined : '10 8'} />
        ))}
        {drip > 0 && <circle cx={bw * 0.5} cy={lerp(10, bh * 0.4, 1 - drip)} r={r * 0.6} fill={CLAUDE.INK} opacity={drip} />}
      </svg>
      <div style={{ position: 'absolute', left: bx, top: by + bh + 24, width: bw, textAlign: 'center' }}>
        <div style={{ fontFamily: MONO, fontSize: P ? 64 : 72, color: CLAUDE.INK }}>{tokens} / {capacity} <span style={{ fontFamily: SANS, fontSize: P ? 48 : 36, color: CLAUDE.INK_SOFT }}>tokens</span></div>
        <div style={{ fontFamily: SANS, fontSize: P ? 48 : 36, color: CLAUDE.INK_SOFT, marginTop: 6, whiteSpace: 'nowrap' }}>{refillLabel}</div>
      </div>
      {P && <div style={{ position: 'absolute', left: bx + bw + 40, top: by + 40, width: S.r - (bx + bw + 40) }}>
        <div style={{ fontFamily: SANS, fontSize: 52, color: CLAUDE.INK }}>passed {passed}</div>
        <div style={{ fontFamily: SANS, fontSize: 52, color: ACC_TEXT, marginTop: 16 }}>rejected {rejected}</div>
      </div>}
      {[0, 1].map((g) => (
        <Txt key={g} text={g === 0 ? 'a burst of 4' : 'then a steady flood'} style={{ left: lx, top: rowY(g, 0) - (P ? 62 : 52), fontSize: P ? 48 : 38, color: CLAUDE.INK,
          opacity: ease(ramp(u, (g === 0 ? burst[0] : flood[0]) - 4, g === 0 ? burst[0] : flood[0])) }} />
      ))}
      {reqs.map((e, i) => {
        const k = groupIdx[e.group]++;
        const a = ease(ramp(u, e.at, e.at + 3));
        if (a <= 0) return null;
        return (
          <div key={i} style={{ position: 'absolute', left: lx + (k % perRow) * (chipW + cg), top: rowY(e.group, k), width: chipW, height: chipH,
            borderRadius: 14, boxSizing: 'border-box', background: e.ok ? CLAUDE.CARD : CLAUDE.PAGE,
            border: e.ok ? `3px solid ${CLAUDE.INK_SOFT}` : `3px dashed ${CLAUDE.GHOST}`,
            display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: a, transform: `translateY(${(1 - a) * -30}px)`,
            fontFamily: SANS, fontSize: 48, color: e.ok ? CLAUDE.INK : ACC_TEXT }}>{e.ok ? '✓' : '✕'}</div>
        );
      })}
      {!P && <div style={{ position: 'absolute', left: lx, top: 760, display: 'flex', gap: 48, fontFamily: SANS, fontSize: 42 }}>
        <span style={{ color: CLAUDE.INK }}>passed {passed}</span>
        <span style={{ color: ACC_TEXT }}>rejected {rejected}</span>
      </div>}
      <Txt text={toyNote} style={P ? { left: S.x, top: 266, fontSize: 48, whiteSpace: 'nowrap' } : { left: lx, top: 840, width: lw, fontSize: 32 }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GwSlidingWindow — the reset edge: fixed window lets 5 + 5 through; sliding does not
// ===========================================================================
export const gwSlidingWindowSchema = z.object({
  title: z.string().default('Fixed vs. sliding window'),
  limit: z.number().default(5),
  windowS: z.number().default(60),
  axisS: z.number().default(75),
  hits: z.array(z.number()).default([55, 56, 57, 58, 59, 60, 61, 62, 63, 64]),
  sweep: z.tuple([z.number(), z.number()]).default([50, 68]),
  fixedNote: z.string().default('5 + 5 in ten seconds: double the limit'),
  slidingNote: z.string().default('the second 5 rejected'),
  toyNote: z.string().default('illustrative: limit 5 per minute'),
  sparkLine: z.string().default('No edge to game.'),
  durationSeconds: z.number().optional(),
});
export const gwSlidingWindowMeta = durMeta(6);
export const GwSlidingWindow: React.FC<z.infer<typeof gwSlidingWindowSchema>> = ({ title, limit, windowS, axisS, hits, sweep, fixedNote, slidingNote, toyNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const now = lerp(sweep[0], sweep[1], ease(ramp(t, 0.1, 0.6)));
  const ax = S.x, aw = S.w;
  const X = (s: number) => ax + (s / axisS) * aw;
  // outcomes, computed from the hits
  const fixedOk = hits.map((s, i) => hits.slice(0, i).filter((p) => Math.floor(p / windowS) === Math.floor(s / windowS)).length < limit);
  const slideOk: boolean[] = [];
  hits.forEach((s, i) => { slideOk.push(hits.slice(0, i).filter((p, j) => slideOk[j] && p > s - windowS).length < limit); });
  const laneH = P ? 450 : 330;
  const laneTop = (l: number) => (P ? 350 : 236) + l * (laneH + (P ? 30 : 24));
  const trackY = (l: number) => laneTop(l) + (P ? 130 : 110);
  const tickH = P ? 120 : 100, tickW = P ? 9 : 14;
  const inSlide = hits.filter((s, i) => slideOk[i] && s <= now && s > now - windowS).length;
  const lane = (l: 0 | 1) => {
    const ok = l === 0 ? fixedOk : slideOk;
    const ty = trackY(l);
    const noteA = ease(ramp(t, l === 0 ? 0.62 : 0.7, l === 0 ? 0.7 : 0.78));
    const passedN = hits.filter((s, i) => s <= now && ok[i]).length;
    return (
      <React.Fragment key={l}>
        <div style={{ position: 'absolute', left: S.x, top: laneTop(l), width: S.w, display: 'flex', alignItems: 'baseline', gap: 22, flexWrap: 'wrap',
          opacity: ease(ramp(t, 0.03 + l * 0.04, 0.1 + l * 0.04)) }}>
          <Pill text={l === 0 ? 'Fixed window · resets at 1:00' : 'Sliding window · always the last 60 s'} size={P ? 46 : 42} />
        </div>
        {/* track */}
        <div style={{ position: 'absolute', left: ax, top: ty + tickH, width: aw, height: 4, background: CLAUDE.BORDER }} />
        {l === 0 && [0, windowS].map((s) => (
          <React.Fragment key={s}>
            <div style={{ position: 'absolute', left: X(s) - 2, top: ty - 20, width: 4, height: tickH + 44, background: s ? CLAUDE.INK : CLAUDE.BORDER }} />
          </React.Fragment>
        ))}
        {l === 1 && (() => {
          const a = Math.max(0, now - windowS), b = now;
          return <div style={{ position: 'absolute', left: X(a), top: ty - 22, width: X(b) - X(a), height: tickH + 30, borderRadius: 12,
            background: 'rgba(217, 119, 87, 0.16)', opacity: ease(ramp(t, 0.08, 0.14)) }} />;
        })()}
        {hits.map((s, i) => {
          if (s > now) return null;
          return <div key={i} style={{ position: 'absolute', left: X(s) - tickW / 2, top: ty, width: tickW, height: tickH, borderRadius: 4, boxSizing: 'border-box',
            background: ok[i] ? CLAUDE.INK : 'transparent', border: ok[i] ? 'none' : `3px dashed ${CLAUDE.GHOST}` }} />;
        })}
        {[0, 30, 60].map((s) => (
          <Txt key={s} text={mmss(s)} style={{ left: X(s) - (s ? (P ? 56 : 40) : 0), top: ty + tickH + 22, fontSize: P ? 48 : 32 }} />
        ))}
        <div style={{ position: 'absolute', left: S.x, top: ty + tickH + (P ? 92 : 62), width: S.w, display: 'flex', columnGap: 28, alignItems: 'baseline', flexWrap: 'wrap' }}>
          <span style={{ fontFamily: SANS, fontSize: P ? 48 : 38, color: CLAUDE.INK }}>
            {l === 0 ? `${passedN} passed` : `last 60 s: ${inSlide} / ${limit}`}
          </span>
          <span style={{ fontFamily: SANS, fontSize: P ? 48 : 38, fontWeight: 600, color: ACC_TEXT, opacity: noteA }}>{l === 0 ? fixedNote : slidingNote}</span>
        </div>
      </React.Fragment>
    );
  };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {lane(0)}
      {lane(1)}
      {/* "now" cursor through both lanes */}
      <div style={{ position: 'absolute', left: X(now) - 1, top: trackY(0) - 30, width: 3, height: trackY(1) + tickH - trackY(0) + 40, background: CLAUDE.INK_SOFT, opacity: 0.6 }} />
      <Txt text={`now ${mmss(now)}`} style={{ ...(X(now) + (P ? 240 : 190) > S.r ? { right: (P ? 1080 : 1920) - X(now) + 14 } : { left: X(now) + 14 }), top: trackY(0) - (P ? 64 : 74), fontSize: P ? 48 : 32, color: CLAUDE.INK, whiteSpace: 'nowrap' }} />
      <Txt text={toyNote} style={P ? { left: S.x, top: 266, fontSize: 48, whiteSpace: 'nowrap' } : { right: 1920 - S.r, top: S.y + 60, fontSize: 32 }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GwAiQuota — shared model capacity, without and with per-user limits
// ===========================================================================
const fillOrder = (cells: number, order: string[]) => Array.from({ length: cells }, (_, i) => order[i % order.length]);
export const gwAiQuotaSchema = z.object({
  title: z.string().default('Sharing an expensive model'),
  cells: z.number().default(24),
  // arrival order with no limits: A keeps sending, B and C get one slot each
  greedy: z.array(z.string()).default(['A', 'A', 'B', 'A', 'C', ...Array(19).fill('A')]),
  fair: z.array(z.string()).default(['A', 'B', 'C']),
  caption: z.string().default('Real limits count requests and model tokens per minute, per user or key.'),
  toyNote: z.string().default('illustrative: 24 slots of shared capacity'),
  sparkLine: z.string().default('A fair share each.'),
  durationSeconds: z.number().optional(),
});
export const gwAiQuotaMeta = durMeta(6);
export const GwAiQuota: React.FC<z.infer<typeof gwAiQuotaSchema>> = ({ title, cells, greedy, fair, caption, toyNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const tint: Record<string, { bg: string; border: string }> = {
    A: { bg: CLAUDE.SPARK, border: CLAUDE.SPARK },
    B: { bg: CLAUDE.INK_SOFT, border: CLAUDE.INK_SOFT },
    C: { bg: CLAUDE.PILL, border: CLAUDE.INK_SOFT },
  };
  const perRow = P ? 12 : cells;
  const gap = 8;
  const cw = (S.w - gap * (perRow - 1)) / perRow;
  const chh = P ? 70 : 120;
  const rowsN = Math.ceil(cells / perRow);
  const barH = rowsN * chh + (rowsN - 1) * gap;
  const blockH = P ? 420 : 310;
  const blockTop = (b: number) => (P ? 352 : 236) + b * blockH;
  const fairSeq = fillOrder(cells, fair);
  const count = (seq: string[], n: number, who: string) => seq.slice(0, n).filter((x) => x === who).length;
  const block = (b: 0 | 1) => {
    const seq = b === 0 ? greedy.slice(0, cells) : fairSeq;
    const [t0, t1] = b === 0 ? [0.1, 0.4] : [0.5, 0.72];
    const n = Math.floor(ramp(t, t0, t1) * cells + (t >= t1 ? 0 : 0));
    const top = blockTop(b);
    const appear = ease(ramp(t, t0 - 0.06, t0));
    const statusA = ease(ramp(t, t1, t1 + 0.06));
    const counts = ['A', 'B', 'C'].map((w) => `${w} ${count(seq, n, w)}`).join(' · ');
    return (
      <React.Fragment key={b}>
        <div style={{ position: 'absolute', left: S.x, top, opacity: appear }}>
          <Pill text={b === 0 ? 'No per-user limits' : 'Per-user limits: 8 slots each'} size={P ? 44 : 40} />
        </div>
        {Array.from({ length: cells }, (_, i) => {
          const who = seq[i];
          const on = i < n;
          return <div key={i} style={{ position: 'absolute', left: S.x + (i % perRow) * (cw + gap), top: top + 76 + Math.floor(i / perRow) * (chh + gap),
            width: cw, height: chh, borderRadius: 8, boxSizing: 'border-box', opacity: appear,
            background: on ? tint[who].bg : CLAUDE.CARD, border: `3px solid ${on ? tint[who].border : CLAUDE.BORDER}` }} />;
        })}
        <div style={{ position: 'absolute', left: S.x, top: top + 76 + barH + 18, width: S.w, display: 'flex', gap: 28, flexWrap: 'wrap', alignItems: 'baseline', opacity: appear }}>
          <span style={{ fontFamily: MONO, fontSize: P ? 48 : 38, color: CLAUDE.INK }}>{counts}</span>
          <span style={{ fontFamily: SANS, fontSize: P ? 48 : 38, fontWeight: 600, color: b === 0 ? ACC_TEXT : CLAUDE.INK, opacity: statusA }}>
            {b === 0 ? 'B and C wait: capacity full' : P ? 'A capped; B and C served' : 'A gets 429 past its share; B and C are served'}
          </span>
        </div>
      </React.Fragment>
    );
  };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', top: P ? 262 : 128, display: 'flex', gap: 26, alignItems: 'center', opacity: ease(ramp(t, 0.03, 0.09)),
        ...(P ? { left: S.x } : { right: 1920 - S.r }) }}>
        {['A', 'B', 'C'].map((w) => (
          <span key={w} style={{ display: 'flex', alignItems: 'center', gap: 10, fontFamily: SANS, fontSize: P ? 48 : 38, color: CLAUDE.INK }}>
            <span style={{ width: 34, height: 34, borderRadius: 6, boxSizing: 'border-box', background: tint[w].bg, border: `3px solid ${tint[w].border}` }} />user {w}
          </span>
        ))}
      </div>
      {block(0)}
      {block(1)}
      <div style={{ position: 'absolute', left: S.x, top: P ? 1180 : 870, width: P ? S.w : S.w - 520, opacity: ease(ramp(t, 0.76, 0.84)),
        fontFamily: SANS, fontSize: P ? 48 : 36, lineHeight: 1.2, color: CLAUDE.INK }}>{caption}</div>
      {!P && <Txt text={toyNote} style={{ right: 1920 - S.r, top: 876, fontSize: 32 }} />}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
