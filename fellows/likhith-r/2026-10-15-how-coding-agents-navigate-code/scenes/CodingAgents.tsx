/**
 * CodingAgents.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-coding-agents ("How Coding Agents Navigate Code", @HumanitariansAI).
 *
 * Same contract as JevExplainer.tsx / McpProtocol.tsx (whose stage helpers it reuses):
 * each component lays out natively for 16:9 (<Name>) and 9:16 (<Name>916), never a
 * crop, and every motion is a pure function of progress, conformed via `durationSeconds`.
 * Every command, file name, code line and test result on screen is the REAL output of
 * the reel's evidence/agent_loop.py (a toy shop repo; a scripted replay of the agent's
 * tool calls, pytest 8.3.3). Claims: SOURCES.md.
 *
 *   AgentHook     — a bug report vs. a wall of files the agent has never seen
 *   AgentExplore  — find *.py: the real file tree, grouped into code and tests
 *   AgentSearch   — grep 'discount': 3 of 9 files light up, pricing.py opens
 *   AgentEdit     — one exact line replaced, the rest of the file untouched
 *   AgentVerify   — pytest: . . F . → 1 failed, 3 passed, the failure line
 *   AgentIterate  — read the failure → add rounding → 4 passed, no human message
 *   AgentLoop     — explore → edit → verify → iterate, two passes to green
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const GREEN = '#4D7A4A'; // pass marks only; 5.1:1 on white

const Note: React.FC<{ x: number; y: number; w: number; a: number; text: string; align?: 'left' | 'right' | 'center'; size?: number }> = ({ x, y, w, a, text, align = 'left', size = 34 }) => (
  <div style={{ position: 'absolute', left: x, top: y, width: w, textAlign: align, fontFamily: SANS, fontSize: size, color: CLAUDE.INK_SOFT, opacity: a }}>{text}</div>
);

// a tool call as the agent issues it: "$ command"
const Cmd: React.FC<{ x: number; y: number; w: number; a: number; cmd: string; P: boolean; label?: string }> = ({ x, y, w, a, cmd, P, label = 'agent tool call' }) => (
  <Card style={{ left: x, top: y, width: w, padding: P ? '20px 30px' : '22px 34px', opacity: a, transform: `translateY(${(1 - a) * 14}px)` }}>
    <div style={{ fontFamily: SANS, fontSize: P ? 44 : 32, color: CLAUDE.INK_SOFT, marginBottom: 8 }}>{label}</div>
    <div style={{ fontFamily: MONO, fontSize: P ? 50 : 46, color: CLAUDE.INK, whiteSpace: 'pre' }}>
      <span style={{ color: CLAUDE.INK_SOFT }}>$ </span>{cmd}
    </div>
  </Card>
);

// a code line with ink "bars" standing in for an untouched line (portrait context)
const Bar: React.FC<{ w: number; a?: number }> = ({ w, a = 1 }) => (
  <div style={{ height: 22, width: w, borderRadius: 11, background: CLAUDE.GHOST, opacity: a, margin: '19px 0' }} />
);

const Canvas: React.FC<{ P: boolean; children: React.ReactNode }> = ({ P, children }) => (
  <svg width={P ? 1080 : 1920} height={P ? 1920 : 1080} style={{ position: 'absolute', left: 0, top: 0 }}>{children}</svg>
);

// ===========================================================================
// AgentHook — a bug report, and a wall of files the agent has never seen
// ===========================================================================
export const agentHookSchema = z.object({
  title: z.string().default('A bug, in unseen code'),
  label: z.string().default('Bug report'),
  bug: z.string().default('A 10% coupon takes $10 off instead of 10%.'),
  wallLabel: z.string().default('a codebase it has never seen'),
  sparkLine: z.string().default('Where does it look?'),
  durationSeconds: z.number().optional(),
});
export const agentHookMeta = durMeta(4);
export const AgentHook: React.FC<z.infer<typeof agentHookSchema>> = ({ title, label, bug, wallLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cardIn = ease(ramp(t, 0.03, 0.14));
  const q = ease(ramp(t, 0.6, 0.72));
  const card = P ? { x: S.x, y: 290, w: S.w, h: 350 } : { x: S.x, y: 300, w: 620, h: 420 };
  const wall = P ? { x: S.x, y: 690, w: S.w, h: 590 } : { x: S.x + 700, y: 250, w: S.w - 700, h: 620 };
  const cols = P ? 6 : 8, rows = P ? 5 : 6, g = P ? 16 : 18;
  const tw = (wall.w - g * (cols - 1)) / cols, th = (wall.h - 60 - g * (rows - 1)) / rows;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card accent style={{ left: card.x, top: card.y, width: card.w, height: card.h, padding: P ? '30px 40px' : '40px 44px', opacity: cardIn }}>
        <div style={{ fontFamily: SANS, fontSize: P ? 50 : 38, color: CLAUDE.INK_SOFT, marginBottom: P ? 18 : 30 }}>{label}</div>
        <div style={{ fontFamily: SERIF, fontSize: P ? 90 : 66, color: CLAUDE.INK, lineHeight: 1.12 }}>{bug}</div>
      </Card>
      {Array.from({ length: cols * rows }).map((_, i) => {
        const c = i % cols, r = Math.floor(i / cols);
        const a = ease(ramp(t, 0.16 + ((i * 7) % (cols * rows)) * 0.009, 0.24 + ((i * 7) % (cols * rows)) * 0.009));
        return (
          <div key={i} style={{
            position: 'absolute', left: wall.x + c * (tw + g), top: wall.y + r * (th + g), width: tw, height: th,
            background: CLAUDE.CARD, border: `3px solid ${CLAUDE.GHOST}`, borderRadius: 10, boxSizing: 'border-box',
            padding: '14px 12px', opacity: a,
          }}>
            {[0.8, 0.55, 0.7].map((f, k) => (
              <div key={k} style={{ height: 8, width: `${f * 100 - ((i + k) % 3) * 12}%`, background: CLAUDE.GHOST, borderRadius: 4, marginBottom: 9 }} />
            ))}
          </div>
        );
      })}
      <div style={{
        position: 'absolute', left: wall.x, top: wall.y, width: wall.w, height: wall.h - 60,
        display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: q, transform: `scale(${0.8 + 0.2 * q})`,
      }}>
        <div style={{
          width: P ? 280 : 300, height: P ? 280 : 300, borderRadius: 999, background: CLAUDE.CARD, border: `6px solid ${CLAUDE.SPARK}`,
          display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: P ? 220 : 230, color: ACC_TEXT, lineHeight: 1,
        }}>?</div>
      </div>
      <Note x={wall.x} y={wall.y + wall.h - 44} w={wall.w} a={ease(ramp(t, 0.3, 0.4))} align="center" size={P ? 50 : 36} text={wallLabel} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// AgentExplore — find *.py: the real tree grows, then groups into code / tests
// ===========================================================================
export const agentExploreSchema = z.object({
  title: z.string().default('1 · Explore'),
  cmd: z.string().default("find . -name '*.py'"),
  code: z.array(z.string()).default(['cart.py', 'emails.py', 'inventory.py', 'pricing.py', 'shipping.py', 'users.py']),
  tests: z.array(z.string()).default(['test_cart.py', 'test_pricing.py', 'test_shipping.py']),
  caption: z.string().default('real output · toy shop repo'),
  sparkLine: z.string().default('Map first, touch later.'),
  durationSeconds: z.number().optional(),
});
export const agentExploreMeta = durMeta(5);
export const AgentExplore: React.FC<z.infer<typeof agentExploreSchema>> = ({ title, cmd, code, tests, caption, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cmdIn = ease(ramp(t, 0.03, 0.12));
  const lineAt = (i: number) => 0.14 + i * 0.045;
  const group = ease(ramp(t, 0.6, 0.7));
  const top = P ? 520 : 390;
  const colW = P ? (S.w - 30) / 2 : (S.w - 60) / 2;
  const rowH = P ? 86 : 56;
  const Column: React.FC<{ name: string; files: string[]; offset: number; x: number; label: string }> = ({ name, files, offset, x, label }) => (
    <Card style={{ left: x, top, width: colW, height: (P ? 128 : 96) + Math.max(code.length, tests.length) * rowH + (P ? 100 : 80), padding: P ? '22px 28px' : '24px 36px', borderColor: group > 0.5 ? CLAUDE.INK_SOFT : CLAUDE.BORDER, opacity: ease(ramp(t, lineAt(offset) - 0.04, lineAt(offset))) }}>
      <div style={{ fontFamily: MONO, fontSize: P ? 56 : 50, color: CLAUDE.INK, fontWeight: 700, marginBottom: P ? 18 : 14 }}>{name}/</div>
      {files.map((f, i) => (
        <div key={f} style={{ fontFamily: MONO, fontSize: P ? 40 : 42, color: CLAUDE.INK, height: rowH, lineHeight: `${rowH}px`, whiteSpace: 'nowrap', opacity: ease(ramp(t, lineAt(offset + i), lineAt(offset + i) + 0.05)) }}>
          {!P && <span style={{ color: CLAUDE.GHOST }}>├ </span>}{f}
        </div>
      ))}
      <div style={{ fontFamily: SANS, fontSize: P ? 50 : 40, color: ACC_TEXT, marginTop: P ? 14 : 18, opacity: group }}>{label}</div>
    </Card>
  );
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Cmd x={S.x} y={P ? 300 : 230} w={P ? S.w : 900} a={cmdIn} cmd={cmd} P={P} />
      {!P && <Note x={S.x + 940} y={280} w={S.w - 940} a={cmdIn} align="right" text={caption} />}
      <Column name="shop" files={code} offset={0} x={S.x} label={`${code.length} source files`} />
      <Column name="tests" files={tests} offset={code.length} x={S.x + colW + (P ? 30 : 60)} label={`${tests.length} test files`} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// AgentSearch — grep 'discount': 3 of 9 files match; only pricing.py is opened
// ===========================================================================
export const agentSearchSchema = z.object({
  title: z.string().default('2 · Targeted reading'),
  cmd: z.string().default("grep -rn 'discount'"),
  files: z.array(z.object({ name: z.string(), hits: z.number() })).default([
    { name: 'cart.py', hits: 2 }, { name: 'emails.py', hits: 0 }, { name: 'inventory.py', hits: 0 },
    { name: 'pricing.py', hits: 1 }, { name: 'shipping.py', hits: 0 }, { name: 'users.py', hits: 0 },
    { name: 'test_cart.py', hits: 0 }, { name: 'test_pricing.py', hits: 3 }, { name: 'test_shipping.py', hits: 0 },
  ]),
  open: z.string().default('pricing.py'),
  lines: z.array(z.object({ n: z.number(), code: z.string() })).default([
    { n: 4, code: 'def apply_discount(price, percent):' },
    { n: 5, code: '    """Take `percent` % off `price`."""' },
    { n: 6, code: '    return price - percent' },
  ]),
  bugLine: z.number().default(6),
  summary: z.string().default('6 hits · 3 of 9 files'),
  sparkLine: z.string().default('Search, then read.'),
  durationSeconds: z.number().optional(),
});
export const agentSearchMeta = durMeta(5);
export const AgentSearch: React.FC<z.infer<typeof agentSearchSchema>> = ({ title, cmd, files, open, lines, bugLine, summary, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cmdIn = ease(ramp(t, 0.03, 0.12));
  const hit = ease(ramp(t, 0.24, 0.36));
  const opened = ease(ramp(t, 0.56, 0.66));
  const mark = ease(ramp(t, 0.68, 0.76));
  const grid = P ? { x: S.x, y: 530, w: S.w, cols: 3, ch: 100, g: 14 } : { x: S.x, y: 400, w: S.w, cols: 5, ch: 100, g: 18 };
  const cw = (grid.w - grid.g * (grid.cols - 1)) / grid.cols;
  const code = P ? { x: S.x, y: 900, w: S.w } : { x: S.x, y: 650, w: S.w };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Cmd x={S.x} y={P ? 300 : 230} w={P ? S.w : 820} a={cmdIn} cmd={cmd} P={P} label="search for a word from the bug" />
      {files.map((f, i) => {
        const on = f.hits > 0;
        const isOpen = f.name === open;
        return (
          <Card key={f.name} accent={isOpen && opened > 0.5} style={{
            left: grid.x + (i % grid.cols) * (cw + grid.g), top: grid.y + Math.floor(i / grid.cols) * (grid.ch + grid.g),
            width: cw, height: grid.ch, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
            opacity: on ? 1 : 1 - 0.55 * hit, borderColor: on && hit > 0.5 && !(isOpen && opened > 0.5) ? CLAUDE.INK : undefined,
          }}>
            <div style={{ fontFamily: MONO, fontSize: P ? (f.name.length > 12 ? 30 : 36) : (f.name.length > 12 ? 32 : 38), color: CLAUDE.INK, fontWeight: on && hit > 0.5 ? 700 : 400 }}>{f.name}</div>
            {on && <div style={{ fontFamily: SANS, fontSize: P ? 30 : 30, color: CLAUDE.INK_SOFT, opacity: hit }}>{f.hits} {f.hits === 1 ? 'hit' : 'hits'}</div>}
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: P ? grid.x : S.x + 900, top: P ? grid.y - 74 : 280, width: P ? grid.w : S.w - 900, fontFamily: SANS, fontSize: P ? 48 : 44, color: CLAUDE.INK, opacity: hit, textAlign: 'right' }}>{summary}</div>
      <Card style={{ left: code.x, top: code.y, width: code.w, padding: P ? '22px 28px' : '20px 36px', opacity: opened, transform: `translateY(${(1 - opened) * 16}px)` }}>
        <div style={{ fontFamily: SANS, fontSize: P ? 44 : 36, color: CLAUDE.INK_SOFT, marginBottom: 14 }}>opened: shop/{open}</div>
        {lines.map((l) => {
          const bug = l.n === bugLine;
          const txt = P ? l.code.trimStart() : l.code;
          return (
            <div key={l.n} style={{ fontFamily: MONO, fontSize: P ? (txt.length > 30 ? 36 : 44) : 42, color: CLAUDE.INK, whiteSpace: 'pre', lineHeight: 1.35, display: 'flex', gap: 22, position: 'relative' }}>
              <span style={{ color: CLAUDE.GHOST, width: 40, textAlign: 'right' }}>{l.n}</span>
              <span style={{ fontWeight: bug ? 700 : 400, borderBottom: bug ? `5px solid ${mark > 0.5 ? CLAUDE.SPARK : 'transparent'}` : undefined }}>{txt}</span>
            </div>
          );
        })}
        <div style={{ fontFamily: SANS, fontSize: P ? 44 : 36, color: ACC_TEXT, marginTop: 12, opacity: mark }}>subtracts dollars, not percent</div>
      </Card>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// AgentEdit — replace one exact line; the other 9 lines are untouched
// ===========================================================================
export const agentEditSchema = z.object({
  title: z.string().default('3 · Scoped edit'),
  file: z.string().default('shop/pricing.py'),
  lines: z.array(z.string()).default([
    'TAX_RATE = 0.0', '', '', 'def apply_discount(price, percent):', '    """Take `percent` % off `price`."""',
    '    return price - percent', '', '', 'def with_tax(price):', '    return price * (1 + TAX_RATE)',
  ]),
  target: z.number().default(6),
  replacement: z.string().default('    return price * (1 - percent / 100)'),
  badge: z.string().default('1 line changed · 9 untouched'),
  sparkLine: z.string().default('One line, not the file.'),
  durationSeconds: z.number().optional(),
});
export const agentEditMeta = durMeta(4);
export const AgentEdit: React.FC<z.infer<typeof agentEditSchema>> = ({ title, file, lines, target, replacement, badge, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cardIn = ease(ramp(t, 0.03, 0.12));
  const strike = ease(ramp(t, 0.26, 0.38));
  const typed = ramp(t, 0.42, 0.62);
  const badgeIn = ease(ramp(t, 0.68, 0.78));
  const box = P ? { x: S.x, y: 300, w: S.w } : { x: S.x, y: 220, w: 1220 };
  const fs = P ? 40 : 38, lh = P ? 60 : 52;
  const repl = P ? replacement.trimStart() : replacement;
  const shown = repl.slice(0, Math.round(repl.length * typed));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: box.x, top: box.y, width: box.w, padding: P ? '22px 26px' : '26px 36px', opacity: cardIn }}>
        <div style={{ fontFamily: SANS, fontSize: P ? 44 : 36, color: CLAUDE.INK_SOFT, marginBottom: 12 }}>{file}</div>
        {lines.map((l, i) => {
          const n = i + 1;
          if (n === target) {
            const old = P ? l.trimStart() : l;
            return (
              <div key={n}>
                <div style={{ display: 'flex', gap: 22, fontFamily: MONO, fontSize: P ? 46 : fs, height: P ? 72 : lh, lineHeight: `${P ? 72 : lh}px`, whiteSpace: 'pre', color: ACC_TEXT }}>
                  <span style={{ width: 40, textAlign: 'right', color: CLAUDE.GHOST }}>{n}</span>
                  <span style={{ width: 26 }}>{strike > 0.3 ? '-' : ' '}</span>
                  <span>{old.slice(0, old.length - old.trimStart().length)}<span style={{ color: strike > 0.3 ? ACC_TEXT : CLAUDE.INK, textDecoration: strike > 0.3 ? 'line-through' : 'none', textDecorationThickness: 4 }}>{old.trimStart()}</span></span>
                </div>
                <div style={{ display: 'flex', gap: 22, fontFamily: MONO, fontSize: P ? 46 : fs, minHeight: P ? 72 : lh, lineHeight: `${P ? 72 : lh}px`, whiteSpace: 'pre-wrap', color: CLAUDE.INK, background: typed > 0 ? '#F3EEE2' : 'transparent', borderRadius: 8, opacity: typed > 0 ? 1 : 0 }}>
                  <span style={{ width: 40, textAlign: 'right', color: CLAUDE.GHOST }}>{n}</span>
                  <span style={{ width: 26, color: GREEN, fontWeight: 700 }}>+</span>
                  <span style={{ fontWeight: 700, flex: 1 }}>{shown}</span>
                </div>
              </div>
            );
          }
          if (P) return l.trim() ? <div key={n} style={{ display: 'flex', gap: 22, alignItems: 'center' }}><span style={{ width: 40 }} /><Bar w={Math.min(700, 120 + l.trim().length * 18)} /></div> : <div key={n} style={{ height: 26 }} />;
          return (
            <div key={n} style={{ display: 'flex', gap: 22, fontFamily: MONO, fontSize: fs, height: lh, lineHeight: `${lh}px`, whiteSpace: 'pre', color: CLAUDE.INK }}>
              <span style={{ width: 40, textAlign: 'right', color: CLAUDE.GHOST }}>{n}</span>
              <span style={{ width: 26 }} />
              <span>{l}</span>
            </div>
          );
        })}
      </Card>
      <div style={{
        position: 'absolute', ...(P ? { left: S.x, top: 1070, width: S.w, textAlign: 'center' } : { left: box.x + box.w + 60, top: 380, width: S.r - box.x - box.w - 60 }),
        fontFamily: SERIF, fontSize: P ? 84 : 76, color: CLAUDE.INK, lineHeight: 1.1, opacity: badgeIn,
      }}>
        {badge.split(' · ').map((b) => <div key={b} style={{ marginBottom: P ? 10 : 30 }}>{b}</div>)}
      </div>
      {!P && <Note x={box.x + box.w + 60} y={670} w={S.r - box.x - box.w - 60} a={badgeIn} text="replace one exact string, matched once" />}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// AgentVerify — pytest: . . F . → 1 failed, 3 passed, and the failure line
// ===========================================================================
export const agentVerifySchema = z.object({
  title: z.string().default('4 · Verify'),
  cmd: z.string().default('pytest -q'),
  marks: z.string().default('..F.'),
  result: z.string().default('1 failed, 3 passed'),
  failFile: z.string().default('tests/test_pricing.py:5'),
  failAssert: z.string().default('assert 16.9915 == 16.99'),
  sparkLine: z.string().default('Tests are the judge.'),
  durationSeconds: z.number().optional(),
});
export const agentVerifyMeta = durMeta(4);
export const AgentVerify: React.FC<z.infer<typeof agentVerifySchema>> = ({ title, cmd, marks, result, failFile, failAssert, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cmdIn = ease(ramp(t, 0.03, 0.12));
  const res = ease(ramp(t, 0.5, 0.6));
  const fail = ease(ramp(t, 0.64, 0.74));
  const n = marks.length;
  const dot = P ? 190 : 200, dg = P ? 40 : 60;
  const rowW = n * dot + (n - 1) * dg;
  const rowY = P ? 520 : 370;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Cmd x={S.x} y={P ? 300 : 210} w={P ? S.w : 560} a={cmdIn} cmd={cmd} P={P} label="run the existing tests" />
      {marks.split('').map((m, i) => {
        const a = ease(ramp(t, 0.16 + i * 0.07, 0.22 + i * 0.07));
        const bad = m === 'F';
        return (
          <div key={i} style={{
            position: 'absolute', left: (P ? 540 : 960) - rowW / 2 + i * (dot + dg), top: rowY, width: dot, height: dot,
            borderRadius: 24, boxSizing: 'border-box', background: CLAUDE.CARD, border: `5px solid ${bad ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: a, transform: `scale(${0.85 + 0.15 * a})`,
            fontFamily: SANS, fontWeight: 700, fontSize: bad ? 120 : 110, color: bad ? ACC_TEXT : GREEN,
          }}>{bad ? 'F' : '✓'}</div>
        );
      })}
      <div style={{ position: 'absolute', left: S.x, top: rowY + dot + (P ? 50 : 14), width: S.w, textAlign: 'center', fontFamily: SERIF, fontSize: P ? 96 : 84, color: CLAUDE.INK, opacity: res }}>{result}</div>
      <Card accent style={{
        left: P ? S.x : 960 - 600, top: rowY + dot + (P ? 210 : 132), width: P ? S.w : 1200, padding: P ? '24px 30px' : '22px 36px', opacity: fail,
      }}>
        <div style={{ fontFamily: SANS, fontSize: P ? 44 : 34, color: CLAUDE.INK_SOFT, marginBottom: 6 }}>the failure, verbatim</div>
        <div style={{ fontFamily: MONO, fontSize: P ? 44 : 40, color: CLAUDE.INK_SOFT }}>{failFile}</div>
        <div style={{ fontFamily: MONO, fontSize: P ? 56 : 52, color: CLAUDE.INK, fontWeight: 700, marginTop: 4 }}>{failAssert}</div>
      </Card>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// AgentIterate — read the failure → add rounding → rerun → 4 passed
// ===========================================================================
export const agentIterateSchema = z.object({
  title: z.string().default('5 · Iterate'),
  read: z.string().default('16.9915 should be 16.99: round to cents'),
  edit: z.string().default('return round(price * (1 - percent / 100), 2)'),
  editP: z.array(z.string()).default(['return round(', '  price * (1 - percent / 100),', '  2)']),
  rerun: z.string().default('pytest -q'),
  result: z.string().default('4 passed'),
  human: z.string().default('messages from a human: 0'),
  sparkLine: z.string().default('Failure is evidence.'),
  durationSeconds: z.number().optional(),
});
export const agentIterateMeta = durMeta(5);
export const AgentIterate: React.FC<z.infer<typeof agentIterateSchema>> = ({ title, read, edit, editP, rerun, result, human, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const rows = [
    { k: 'read', at: 0.04 }, { k: 'edit', at: 0.24 }, { k: 'run', at: 0.5 },
  ];
  const pass = ease(ramp(t, 0.66, 0.76));
  const humanIn = ease(ramp(t, 0.78, 0.86));
  const top = P ? 290 : 240;
  const rh = P ? [270, 300, 250] : [150, 150, 190];
  const g = P ? 28 : 30;
  const y = (i: number) => top + rh.slice(0, i).reduce((a, b) => a + b + g, 0);
  const label = (i: number, s: string) => (
    <div style={{ fontFamily: SANS, fontSize: P ? 44 : 32, color: CLAUDE.INK_SOFT, marginBottom: 6 }}>{i + 1} · {s}</div>
  );
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {rows.map((r, i) => {
        const a = ease(ramp(t, r.at, r.at + 0.1));
        return (
          <Card key={r.k} accent={i === 2 && pass > 0.5} style={{ left: S.x, top: y(i), width: S.w, height: rh[i], padding: P ? '20px 30px' : '20px 36px', opacity: a, transform: `translateY(${(1 - a) * 14}px)` }}>
            {i === 0 && <>{label(0, 'read the failure')}<div style={{ fontFamily: SERIF, fontSize: P ? 64 : 60, color: CLAUDE.INK }}>{read}</div></>}
            {i === 1 && <>{label(1, 'second scoped edit, shop/pricing.py line 6')}
              <div style={{ fontFamily: MONO, fontSize: P ? 46 : 52, color: CLAUDE.INK, fontWeight: 700, whiteSpace: 'pre' }}>
                <span style={{ color: GREEN }}>+ </span>{P ? editP.join('\n  ') : edit}
              </div></>}
            {i === 2 && <>{label(2, `rerun: $ ${rerun}`)}
              <div style={{ display: 'flex', alignItems: 'center', gap: P ? 24 : 30, marginTop: 6 }}>
                {[0, 1, 2, 3].map((k) => (
                  <div key={k} style={{ width: P ? 110 : 100, height: P ? 110 : 100, borderRadius: 18, border: `4px solid ${CLAUDE.BORDER}`, boxSizing: 'border-box', display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SANS, fontWeight: 700, fontSize: P ? 70 : 60, color: GREEN, opacity: ease(ramp(t, 0.56 + k * 0.03, 0.6 + k * 0.03)) }}>✓</div>
                ))}
                <div style={{ fontFamily: SERIF, fontSize: P ? 90 : 80, color: CLAUDE.INK, marginLeft: P ? 10 : 30, opacity: pass }}>{result}</div>
              </div></>}
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: S.x, top: y(3) + (P ? 0 : -6), width: S.w, textAlign: P ? 'center' : 'right', fontFamily: SANS, fontSize: P ? 52 : 40, color: CLAUDE.INK, opacity: humanIn }}>{human}</div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// AgentLoop — explore → edit → verify → iterate; two passes to green
// ===========================================================================
export const agentLoopSchema = z.object({
  title: z.string().default('The loop'),
  stations: z.array(z.string()).default(['Explore', 'Edit', 'Verify', 'Iterate']),
  passes: z.array(z.object({ label: z.string(), ok: z.boolean() })).default([
    { label: 'pass 1: 1 failed', ok: false }, { label: 'pass 2: 4 passed', ok: true },
  ]),
  sparkLine: z.string().default('Loop until green.'),
  durationSeconds: z.number().optional(),
});
export const agentLoopMeta = durMeta(5);
export const AgentLoop: React.FC<z.infer<typeof agentLoopSchema>> = ({ title, stations, passes, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cx = P ? 540 : 700, cy = P ? 780 : 560, R = P ? 310 : 320;
  const n = stations.length;
  const ang = (i: number) => -Math.PI / 2 + (i / n) * Math.PI * 2;
  const ring = ease(ramp(t, 0.03, 0.16));
  // marker goes around twice: 0.18 → 0.48 (pass 1), 0.5 → 0.8 (pass 2)
  const lap = t < 0.18 ? 0 : t < 0.49 ? (t - 0.18) / 0.31 : t < 0.5 ? 1 : Math.min(2, 1 + (t - 0.5) / 0.3);
  const ma = ang(0) + lap * Math.PI * 2;
  const live = Math.floor(((lap % 1) + 1e-6) * n) % n;
  const p1 = ease(ramp(t, 0.44, 0.5)), p2 = ease(ramp(t, 0.78, 0.84));
  const bw = P ? 290 : 280, bh = P ? 130 : 110;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Canvas P={P}>
        <circle cx={cx} cy={cy} r={R} fill="none" stroke={CLAUDE.BORDER} strokeWidth={10} opacity={ring}
          strokeDasharray={2 * Math.PI * R} strokeDashoffset={(1 - ring) * 2 * Math.PI * R} transform={`rotate(-90 ${cx} ${cy})`} />
        {lap > 0 && lap < 2 && <circle cx={cx + Math.cos(ma) * R} cy={cy + Math.sin(ma) * R} r={P ? 26 : 24} fill={ACC_TEXT} />}
      </Canvas>
      {stations.map((s, i) => {
        const a = ease(ramp(t, 0.06 + i * 0.03, 0.14 + i * 0.03));
        const on = lap > 0 && lap < 2 && live === i;
        return (
          <Card key={s} style={{
            borderColor: on ? ACC_TEXT : CLAUDE.BORDER,
            left: cx + Math.cos(ang(i)) * R - bw / 2, top: cy + Math.sin(ang(i)) * R - bh / 2, width: bw, height: bh, opacity: a,
            display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: P ? 90 : 66, color: CLAUDE.INK,
          }}>{s}</Card>
        );
      })}
      <div style={{ position: 'absolute', left: cx - 200, top: cy - 70, width: 400, textAlign: 'center', fontFamily: SERIF, fontSize: P ? 120 : 110, color: CLAUDE.INK, opacity: ring }}>
        {lap >= 1.5 || t > 0.8 ? '×2' : '×1'}
      </div>
      {passes.map((p, i) => {
        const a = i === 0 ? p1 : p2;
        const pos = P ? { left: S.x, top: 1185, width: S.w } : { left: 1180, top: 400 + i * 180, width: S.r - 1180 };
        if (P && i === 0 && p2 > 0.5) return null;
        return (
          <Card key={i} style={{ ...pos, borderColor: p.ok ? ACC_TEXT : CLAUDE.BORDER, padding: P ? '14px 28px' : '24px 34px', opacity: a, display: 'flex', alignItems: 'center', gap: 24 }}>
            <span style={{ fontFamily: SANS, fontWeight: 700, fontSize: P ? 60 : 64, color: p.ok ? GREEN : ACC_TEXT }}>{p.ok ? '✓' : '✗'}</span>
            <span style={{ fontFamily: MONO, fontSize: P ? 50 : 50, color: CLAUDE.INK }}>{p.label}</span>
          </Card>
        );
      })}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
