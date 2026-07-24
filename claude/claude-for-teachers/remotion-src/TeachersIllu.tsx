import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from 'remotion';
import { CLAUDE, CLAUDE_FONT } from '../runtime/tokens/claude';
import { ClaudeWindow } from '../onda/registry/components/claude-window/ClaudeWindow';
import { claudeWindowSchema } from '../onda/registry/components/claude-window/schema';
import { ClaudeCallout } from '../onda/registry/components/claude-callout/ClaudeCallout';
import { claudeCalloutSchema } from '../onda/registry/components/claude-callout/schema';

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const MONO = 'ui-monospace, "SF Mono", Menlo, monospace';
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
const remap = (x: number, x0: number, x1: number, y0: number, y1: number) => {
  const t = clamp((x - x0) / (x1 - x0 || 1), 0, 1);
  return y0 + (y1 - y0) * t;
};
const ease = (t: number) => 1 - Math.pow(1 - clamp(t, 0, 1), 3);
const useP = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  return clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
};

/* Three layers stack up: tier → skills → connectors. Then the comparison line. */
export const TeachersLayerStack: React.FC = () => {
  const p = useP();
  const LAYERS = [
    { title: 'a free tier', sub: 'premium Claude · verified US K-12 educators' },
    { title: 'a skills library', sub: 'teaching skills — open-source, on GitHub' },
    { title: 'connectors', sub: 'state standards + nine classroom tools (MCP)' },
  ];
  return (
    <>
      {LAYERS.map((l, i) => {
        const t0 = 0.08 + i * 0.16;
        const lp = ease(remap(p, t0, t0 + 0.12, 0, 1));
        if (lp <= 0) return null;
        return (
          <div key={i} style={{
            position: 'absolute', left: 320, width: 640, top: 150 + i * 130 + (1 - lp) * 40,
            opacity: lp, background: '#FFFFFF', border: `1px solid ${CLAUDE.BORDER}`,
            borderLeft: `10px solid ${i === 2 ? CLAUDE.SPARK : CLAUDE.INK}`,
            borderRadius: 14, padding: '20px 28px', boxShadow: '0 8px 24px rgba(61,57,41,0.10)',
          }}>
            <div style={{ fontFamily: SERIF, fontSize: 34, color: CLAUDE.INK }}>{l.title}</div>
            <div style={{ fontFamily: SANS, fontSize: 19, color: CLAUDE.INK_SOFT, marginTop: 4 }}>{l.sub}</div>
          </div>
        );
      })}
      <div style={{ position: 'absolute', bottom: 96, left: 0, right: 0, textAlign: 'center', fontFamily: SANS, fontSize: 24, color: CLAUDE.INK_SOFT, opacity: remap(p, 0.72, 0.82, 0, 1) }}>
        not Claude&nbsp;Design (a product you go to) — the Figma/Canva&nbsp;MCP pattern (plumbing into the Claude you use)
      </div>
    </>
  );
};

/* Standards fly from the Learning Commons server into a Cowork lesson plan. */
const FEEDS = [
  { label: '50-state standards', tint: CLAUDE.SPARK },
  { label: 'competencies, in order', tint: '#8A7B57' },
  { label: 'OpenSciEd', tint: '#5E7D7A' },
  { label: 'Illustrative Mathematics', tint: '#7A6C8F' },
];
export const StandardsToCowork: React.FC = () => {
  const p = useP();
  const W = 1280, H = 720;
  const srvX = 140, srvY = 250, srvW = 220, srvH = 290;
  const winX = 790, winY = 235, winW = 360, winH = 330;
  const plugP = remap(p, 0.05, 0.16, 0, 1);
  const startX = srvX + srvW, endX = winX;
  return (
    <>
      <div style={{ position: 'absolute', left: srvX, top: srvY, width: srvW, height: srvH, background: CLAUDE.INK, borderRadius: 14, padding: 16, boxShadow: '0 10px 30px rgba(61,57,41,0.25)' }}>
        {Array.from({ length: 5 }, (_, i) => (
          <div key={i} style={{ height: 40, borderRadius: 8, background: '#4A4535', marginBottom: 9, display: 'flex', alignItems: 'center', padding: '0 12px', gap: 8 }}>
            <div style={{ width: 9, height: 9, borderRadius: 5, background: (p * 6 + i) % 1.4 < 0.7 ? CLAUDE.SPARK : '#6B6350' }} />
            <div style={{ flex: 1, height: 5, borderRadius: 3, background: '#5C5545' }} />
          </div>
        ))}
        <div style={{ position: 'absolute', bottom: -40, left: 0, right: 0, textAlign: 'center', fontFamily: MONO, fontSize: 16, color: CLAUDE.INK_SOFT }}>
          Learning Commons
        </div>
      </div>
      <svg width={W} height={H} style={{ position: 'absolute', inset: 0 }}>
        <path
          d={`M ${startX + 10} ${srvY + srvH / 2} C ${startX + 180} ${srvY + srvH / 2 - 60}, ${endX - 180} ${winY + winH / 2 - 60}, ${endX - 8} ${winY + winH / 2}`}
          stroke={CLAUDE.SPARK} strokeWidth={4} fill="none" strokeLinecap="round"
          strokeDasharray={600} strokeDashoffset={600 * (1 - ease(plugP))}
        />
      </svg>
      <div style={{ position: 'absolute', left: (startX + endX) / 2 - 90, top: srvY - 46, fontFamily: MONO, fontSize: 17, color: CLAUDE.SPARK, opacity: remap(p, 0.12, 0.18, 0, 1) }}>
        served as data, not prose
      </div>
      {FEEDS.map((b, i) => {
        const t0 = 0.18 + i * 0.15;
        const bp = ease(remap(p, t0, t0 + 0.17, 0, 1));
        if (bp <= 0 || bp >= 1) return null;
        const bx = remap(bp, 0, 1, startX - 30, endX + 20);
        const by = srvY + 40 + i * 52 + Math.sin(bp * Math.PI) * -70 + bp * (winY + 70 + i * 40 - (srvY + 40 + i * 52));
        return (
          <div key={i} style={{
            position: 'absolute', left: bx, top: by, padding: '7px 12px',
            background: CLAUDE.PAGE, border: `2px solid ${b.tint}`, borderLeftWidth: 8,
            borderRadius: 6, fontFamily: SANS, fontSize: 15, color: CLAUDE.INK,
            boxShadow: '0 4px 12px rgba(61,57,41,0.15)',
            transform: `rotate(${Math.sin(bp * 7 + i) * 6}deg)`,
          }}>
            {b.label}
          </div>
        );
      })}
      <div style={{ position: 'absolute', left: winX, top: winY, width: winW, height: winH, background: '#FAF9F5', borderRadius: 14, border: `1px solid ${CLAUDE.BORDER}`, boxShadow: '0 10px 30px rgba(61,57,41,0.12)', padding: 16 }}>
        <div style={{ display: 'flex', gap: 6, marginBottom: 12 }}>
          {['#EC6A5E', '#F4BF4F', '#61C554'].map((c) => (
            <div key={c} style={{ width: 10, height: 10, borderRadius: 5, background: c }} />
          ))}
          <div style={{ marginLeft: 12, fontFamily: SANS, fontSize: 14, color: CLAUDE.INK_SOFT }}>Cowork</div>
        </div>
        <div style={{ fontFamily: SERIF, fontSize: 20, color: CLAUDE.INK, marginBottom: 10 }}>
          <span style={{ color: CLAUDE.SPARK }}>✳</span> plan Monday's lesson
        </div>
        <div style={{ fontFamily: MONO, fontSize: 14, color: CLAUDE.INK_SOFT, lineHeight: 1.95 }}>
          {FEEDS.map((b, i) => {
            const landed = p > 0.18 + i * 0.15 + 0.17;
            return <div key={i} style={{ opacity: landed ? 1 : 0.18 }}>{landed ? '✓' : '·'} {b.label}</div>;
          })}
          <div style={{ color: CLAUDE.SPARK, opacity: remap(p, 0.88, 0.95, 0, 1) }}>✳ scaffolded to your state…</div>
        </div>
      </div>
    </>
  );
};

/* Nine day-one connector chips snap into a grid. */
const TOOLS = ['Canva Education', 'MagicSchool', 'Diffit', 'ASSISTments', 'Brisk', 'Coteach', 'Eedi', 'Snorkl', 'TeachFX'];
export const ConnectorGrid: React.FC = () => {
  const p = useP();
  const cols = 3, cw = 300, ch = 96, gapX = 46, gapY = 42;
  const gridW = cols * cw + (cols - 1) * gapX;
  const x0 = (1280 - gridW) / 2, y0 = 168;
  return (
    <>
      {TOOLS.map((t, i) => {
        const t0 = 0.07 + i * 0.075;
        const tp = ease(remap(p, t0, t0 + 0.09, 0, 1));
        if (tp <= 0) return null;
        const cx = x0 + (i % cols) * (cw + gapX);
        const cy = y0 + Math.floor(i / cols) * (ch + gapY);
        return (
          <div key={t} style={{
            position: 'absolute', left: cx, top: cy + (1 - tp) * 26, width: cw, height: ch,
            opacity: tp, background: '#FFFFFF', border: `1px solid ${CLAUDE.BORDER}`,
            borderRadius: 14, boxShadow: '0 8px 22px rgba(61,57,41,0.09)',
            display: 'flex', alignItems: 'center', gap: 14, padding: '0 20px',
          }}>
            <div style={{ width: 12, height: 12, borderRadius: 7, background: tp >= 1 ? CLAUDE.SPARK : CLAUDE.BORDER }} />
            <div style={{ fontFamily: SANS, fontSize: 22, fontWeight: 600, color: CLAUDE.INK }}>{t}</div>
          </div>
        );
      })}
      <div style={{ position: 'absolute', bottom: 92, left: 0, right: 0, textAlign: 'center', fontFamily: SANS, fontSize: 24, color: CLAUDE.INK_SOFT, opacity: remap(p, 0.78, 0.88, 0, 1) }}>
        the Figma/Canva pattern, for the classroom — your tools become things Claude can drive
      </div>
    </>
  );
};

/* B04 — the one UI-legal inner beat: Cowork IS the subject (the 4pm routine). */
export const CoworkScheduleBeat: React.FC<{ sparkLine: string }> = ({ sparkLine }) => (
  <AbsoluteFill style={{ background: '#F2F0E9' }}>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <ClaudeWindow {...claudeWindowSchema.parse({
        view: 'composer', width: 640, height: 460, fontSize: 13,
        greeting: sparkLine, folderLabel: '@HumanitariansAI',
        command: '4pm daily: review exit tickets, adapt tomorrow’s plan',
        delay: 0, typeSpeed: 1,
      })} />
    </AbsoluteFill>
    <ClaudeCallout {...claudeCalloutSchema.parse({
      items: [
        { title: 'a folder, not a form', body: 'roster + diagnostics +\nyour notes — Claude maps\nwhere every student is.', x: 0.22, y: 0.42, targetX: 0.34, targetY: 0.52, bend: 0.2, delay: 8 },
        { title: 'the 4pm routine', body: 'hand it off once.\nit runs every school day.\n“Claude works while\nyou drive home.”', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 40 },
      ], increment: 0, titleSize: 26, bodySize: 17, maxWidth: 270,
    })} />
  </AbsoluteFill>
);
