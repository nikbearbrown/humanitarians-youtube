/**
 * PhysicsEngine04.tsx — body scenes for "Don't Invent the Mass." (physics engine, 4 of 12).
 *
 * Reel: books/physics-engine/youtube/dont-invent-the-mass
 * Host: Param Madan · voice Kokoro af_bella
 * Source: github.com/jashshah127/humanitariansai/physics-engine @ 2dc4aa4
 *         (engine/parse.py PARSE_PROMPT, variable_glossary.py; PHASE2.md symbolic mode).
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent marks what
 * parse gets right (engine names, SI) and, in B04, the invented values.
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { CLAUDE } from '../tokens/claude';
import { SAFE } from '../tokens/layout';
import { IlluStage, SERIF, SANS, MONO, remap, ease, useP } from '../illustrations/kit';

const INK = CLAUDE.INK;
const SOFT = CLAUDE.INK_SOFT;
const ACCENT = CLAUDE.SPARK;
const HAIR = CLAUDE.BORDER;

/** Small uppercase label that sets the frame's subject. */
const Eyebrow: React.FC<{ text: string; o: number }> = ({ text, o }) => (
  <div style={{
    fontFamily: SANS, fontSize: 34, letterSpacing: 5, color: SOFT,
    textTransform: 'uppercase', opacity: o, textAlign: 'center',
  }}>{text}</div>
);

/** A stat tile: big value over a small caption. */
const Tile: React.FC<{
  value: string; caption: string; o: number; accent?: boolean; w?: number; size?: number;
}> = ({ value, caption, o, accent = false, w = 500, size = 132 }) => (
  <div style={{
    width: w, padding: '34px 28px 30px', background: CLAUDE.CARD,
    border: `2px solid ${accent ? ACCENT : HAIR}`, opacity: o,
    transform: `translateY(${(1 - o) * 26}px)`,
    display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 12,
  }}>
    <div style={{
      fontFamily: SERIF, fontSize: size, lineHeight: 1.08,
      color: accent ? ACCENT : INK, fontWeight: 600,
    }}>{value}</div>
    <div style={{
      fontFamily: SANS, fontSize: 30, letterSpacing: 2.4, lineHeight: 1.3,
      textTransform: 'uppercase', color: SOFT, textAlign: 'center',
    }}>{caption}</div>
  </div>
);

/** The lesson line that lands at the end of a beat, under a terracotta rule. */
const RecordStrip: React.FC<{ text: string; o: number }> = ({ text, o }) => (
  <div style={{
    position: 'absolute', left: SAFE.x, width: SAFE.w, bottom: 96,
    opacity: o, transform: `translateY(${(1 - o) * 18}px)`,
    display: 'flex', justifyContent: 'center',
  }}>
    <div style={{
      borderTop: `3px solid ${ACCENT}`, paddingTop: 20, maxWidth: 1500,
      fontFamily: SERIF, fontSize: 44, lineHeight: 1.25, color: INK, textAlign: 'center',
    }}>{text}</div>
  </div>
);

/** A small mono chip — one value or name. */
const Chip: React.FC<{ text: string; o?: number; hot?: boolean; struck?: boolean; size?: number }> = ({
  text, o = 1, hot = false, struck = false, size = 44,
}) => (
  <span style={{
    display: 'inline-block', padding: '10px 24px', background: CLAUDE.CARD,
    border: `2px solid ${hot ? ACCENT : HAIR}`, opacity: o, whiteSpace: 'nowrap',
    fontFamily: MONO, fontSize: size, fontWeight: 600, color: hot ? ACCENT : struck ? SOFT : INK,
    textDecoration: struck ? 'line-through' : 'none',
  }}>{text}</span>
);

/* ────────────────────────────────────────────────────────────────────────────
 * B00B — the promise. Three things this video shows.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe4Promise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'The one step a model touches.',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.04, 0.18, 0, 1));
  const items = [
    { v: 'Allowed', c: 'what parse may do', hot: false },
    { v: 'Rules', c: 'that keep it honest', hot: false },
    { v: 'The bug', c: 'made-up numbers, fixed', hot: true },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 110, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 26,
      }}>
        <Eyebrow text="What this video is" o={remap(p, 0, 0.08, 0, 1)} />
        <div style={{
          fontFamily: SERIF, fontSize: 92, lineHeight: 1.12, color: INK,
          textAlign: 'center', maxWidth: 1600, fontWeight: 600,
          opacity: head, transform: `translateY(${(1 - head) * 30}px)`,
        }}>{headline}</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 370, width: SAFE.w, height: 360,
        display: 'flex', justifyContent: 'center', gap: 34,
      }}>
        {items.map((n, i) => (
          <Tile key={n.v} value={n.v} caption={n.c} accent={n.hot} w={520} size={120}
            o={ease(remap(p, 0.14 + i * 0.2, 0.30 + i * 0.2, 0, 1))} />
        ))}
      </div>
      <RecordStrip text="No physics or coding background needed." o={remap(p, 0.84, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B01 — the BLUF. Read, don't solve; a misread number survives every check.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe4OneJob: React.FC<{ spark?: string }> = ({ spark = 'Reading only.' }) => {
  const p = useP();
  const yes = ease(remap(p, 0.06, 0.18, 0, 1));
  const no = ease(remap(p, 0.26, 0.38, 0, 1));
  const flow = ease(remap(p, 0.66, 0.80, 0, 1));
  const Col: React.FC<{ title: string; items: string[]; o: number; bad?: boolean }> = ({ title, items, o, bad = false }) => (
    <div style={{
      width: 720, padding: '36px 48px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
      opacity: o, transform: `translateY(${(1 - o) * 24}px)`,
      display: 'flex', flexDirection: 'column', gap: 18,
    }}>
      <div style={{ fontFamily: SERIF, fontSize: 64, fontWeight: 600, color: INK }}>{title}</div>
      <div style={{ height: 2, background: HAIR }} />
      {items.map((t) => (
        <div key={t} style={{
          fontFamily: SANS, fontSize: 42, color: bad ? SOFT : INK, lineHeight: 1.25,
          textDecoration: bad ? 'line-through' : 'none',
        }}>{bad ? '✕ ' : '✓ '}{t}</div>
      ))}
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 110, width: SAFE.w,
        display: 'flex', justifyContent: 'center', gap: 60,
      }}>
        <Col title="Parse may" o={yes} items={['pull out stated quantities', 'name what is asked', 'quote where each came from']} />
        <Col title="Parse may not" o={no} bad items={['solve anything', 'rearrange a formula', 'pick a value']} />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 590,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 30, opacity: flow,
        transform: `translateY(${(1 - flow) * 20}px)`,
      }}>
        <Chip text="wrong number in" hot size={38} />
        <div style={{ fontFamily: MONO, fontSize: 48, color: SOFT }}>→</div>
        <Chip text="4 fixed-rule steps" size={38} />
        <div style={{ fontFamily: MONO, fontSize: 48, color: SOFT }}>→</div>
        <Chip text="checked wrong answer" hot size={38} />
      </div>
      <RecordStrip text="A reading mistake is the one mistake the later steps can’t catch."
        o={remap(p, 0.86, 0.95, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — rule one. The model's names are translated into the engine's names.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe4Vocab: React.FC<{ spark?: string }> = ({ spark = 'Use the engine’s words.' }) => {
  const p = useP();
  const pairs = [
    { from: 'initial_velocity', to: 'v0', at: 0.20 },
    { from: 'mass_1', to: 'm1', at: 0.30 },
    { from: 'initial_speed', to: 'v0', at: 0.38 },
  ];
  const before = ease(remap(p, 0.58, 0.68, 0, 1));
  const after = ease(remap(p, 0.74, 0.84, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 96,
        display: 'flex', justifyContent: 'center', gap: 200,
        fontFamily: SANS, fontSize: 30, letterSpacing: 3, color: SOFT, textTransform: 'uppercase',
        opacity: remap(p, 0.06, 0.14, 0, 1),
      }}>
        <div style={{ width: 520, textAlign: 'right' }}>The model writes</div>
        <div style={{ width: 520 }}>The engine reads</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 156,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 20,
      }}>
        {pairs.map((r) => {
          const o = ease(remap(p, r.at, r.at + 0.06, 0, 1));
          return (
            <div key={r.from} style={{ display: 'flex', alignItems: 'center', gap: 40, opacity: o }}>
              <div style={{ width: 520, textAlign: 'right' }}><Chip text={r.from} struck /></div>
              <div style={{ width: 120, textAlign: 'center', fontFamily: MONO, fontSize: 54, color: SOFT }}>→</div>
              <div style={{ width: 520 }}><Chip text={r.to} hot /></div>
            </div>
          );
        })}
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x + 150, width: SAFE.w - 300, top: SAFE.y + 500,
        display: 'flex', flexDirection: 'column', gap: 16,
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 30, opacity: before }}>
          <div style={{ width: 300, fontFamily: SANS, fontSize: 30, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', whiteSpace: 'nowrap' }}>Before the fix</div>
          <div style={{ fontFamily: MONO, fontSize: 40, color: SOFT, whiteSpace: 'nowrap' }}>a = 9.8*(-mass_1 + mass_2)/(mass_1 + mass_2)</div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 30, opacity: after }}>
          <div style={{ width: 300, fontFamily: SANS, fontSize: 30, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', whiteSpace: 'nowrap' }}>After</div>
          <div style={{ fontFamily: MONO, fontSize: 40, color: INK, fontWeight: 600, whiteSpace: 'nowrap' }}>a = 9.8*(m2 - m1)/(m1 + m2)</div>
        </div>
      </div>
      <RecordStrip text="Same algebra — but only one version a student or an answer key can use."
        o={remap(p, 0.86, 0.95, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — rules two and three. SI units; no constants; "from rest" means zero.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe4Rules: React.FC<{ spark?: string }> = ({ spark = 'Standard units.' }) => {
  const p = useP();
  const Card: React.FC<{ title: string; o: number; hot?: boolean; children: React.ReactNode }> = ({ title, o, hot = false, children }) => (
    <div style={{
      width: 530, height: 500, padding: '34px 38px', background: CLAUDE.CARD,
      border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`,
      opacity: o, transform: `translateY(${(1 - o) * 24}px)`,
      display: 'flex', flexDirection: 'column', gap: 20,
    }}>
      <div style={{ fontFamily: SERIF, fontSize: 52, fontWeight: 600, color: INK, lineHeight: 1.1 }}>{title}</div>
      <div style={{ height: 2, background: HAIR }} />
      {children}
    </div>
  );
  const line = { fontFamily: MONO, fontSize: 36, color: INK, lineHeight: 1.4, whiteSpace: 'nowrap' as const };
  const note = { fontFamily: SANS, fontSize: 32, color: SOFT, lineHeight: 1.3 };
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 110,
        display: 'flex', justifyContent: 'center', gap: 40,
      }}>
        <Card title="Convert to SI" o={ease(remap(p, 0.04, 0.14, 0, 1))} hot>
          <div style={line}>25 km  → 25000 m</div>
          <div style={{ ...line, opacity: remap(p, 0.18, 0.24, 0, 1) }}>100 µF → 0.0001 F</div>
          <div style={{ ...note, marginTop: 'auto', opacity: remap(p, 0.34, 0.40, 0, 1) }}>Exception: angles stay in degrees.</div>
        </Card>
        <Card title="No constants" o={ease(remap(p, 0.46, 0.56, 0, 1))}>
          <div style={line}>g · G · k_e · ε₀ · μ₀</div>
          <div style={{ ...note, marginTop: 'auto' }}>Not reported. The engine adds them itself.</div>
        </Card>
        <Card title="Rest means zero" o={ease(remap(p, 0.72, 0.82, 0, 1))}>
          <div style={{ ...note, color: INK }}>“starts from rest”</div>
          <div style={line}>→ v0 = 0</div>
          <div style={{ ...note, marginTop: 'auto' }}>Written down, never left implied.</div>
        </Card>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — the turn. A problem with no numbers; a parse with numbers in it.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe4Invented: React.FC<{ spark?: string }> = ({ spark = 'Numbers from nowhere.' }) => {
  const p = useP();
  const stat = ease(remap(p, 0.06, 0.18, 0, 1));
  const prob = ease(remap(p, 0.26, 0.36, 0, 1));
  const fake = ease(remap(p, 0.46, 0.58, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', alignItems: 'baseline', gap: 26, opacity: stat,
      }}>
        <div style={{ fontFamily: SERIF, fontSize: 84, fontWeight: 600, color: INK }}>734 of 1,226</div>
        <div style={{ fontFamily: SANS, fontSize: 34, color: SOFT, maxWidth: 560, lineHeight: 1.3 }}>UGPhysics problems have answers written in symbols, not numbers</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 290,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 50,
      }}>
        <div style={{
          width: 700, padding: '30px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
          opacity: prob, fontFamily: SERIF, fontSize: 48, lineHeight: 1.35, color: INK,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', marginBottom: 12 }}>The problem says</div>
          “A particle of mass <i>m</i>, with charge <i>q</i> …”
        </div>
        <div style={{ fontFamily: MONO, fontSize: 60, color: SOFT, opacity: fake }}>→</div>
        <div style={{
          width: 560, padding: '30px 40px', background: CLAUDE.CARD, border: `3px solid ${ACCENT}`,
          opacity: fake, display: 'flex', flexDirection: 'column', gap: 14,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>The old parser wrote</div>
          <div style={{ fontFamily: MONO, fontSize: 54, fontWeight: 700, color: ACCENT }}>m = 1.0</div>
          <div style={{ fontFamily: MONO, fontSize: 54, fontWeight: 700, color: ACCENT }}>q = 1.0</div>
        </div>
      </div>
      <RecordStrip text="No numbers in the problem — numbers in the parse."
        o={remap(p, 0.80, 0.90, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — the payoff. Letters stay letters; SymPy solves with them.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe4Symbolic: React.FC<{ spark?: string }> = ({ spark = 'A letter stays a letter.' }) => {
  const p = useP();
  const parse = ease(remap(p, 0.04, 0.16, 0, 1));
  const ans = ease(remap(p, 0.36, 0.50, 0, 1));
  const chk = ease(remap(p, 0.68, 0.80, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 110,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 24, opacity: parse,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 30, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', marginRight: 16 }}>Parse</div>
        <Chip text='m1: {"symbolic": true}' size={38} />
        <Chip text='m2: {"symbolic": true}' size={38} />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 260,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 18, opacity: ans,
        transform: `translateY(${(1 - ans) * 24}px)`,
      }}>
        <Eyebrow text="SymPy solves with letters" o={1} />
        <div style={{ fontFamily: MONO, fontSize: 84, fontWeight: 700, color: ACCENT, whiteSpace: 'nowrap' }}>a = g·(m2 − m1) / (m1 + m2)</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x + 200, width: SAFE.w - 400, top: SAFE.y + 530,
        padding: '28px 44px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: chk,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12,
      }}>
        <div style={{ fontFamily: MONO, fontSize: 44, color: INK, whiteSpace: 'nowrap' }}>verify: T − g·m1 = a·m1  →  simplifies to 0</div>
        <div style={{ fontFamily: SANS, fontSize: 34, color: SOFT }}>holds for every value of m1 and m2 — a stronger check than one number</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — safeguards, and what is not proven yet.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe4Honest: React.FC<{ spark?: string }> = ({ spark = 'What’s not proven.' }) => {
  const p = useP();
  const a = ease(remap(p, 0.04, 0.14, 0, 1));
  const b = ease(remap(p, 0.20, 0.30, 0, 1));
  const gap = ease(remap(p, 0.44, 0.56, 0, 1));
  const Card: React.FC<{ title: string; o: number; children: React.ReactNode }> = ({ title, o, children }) => (
    <div style={{
      width: 790, height: 250, padding: '28px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
      opacity: o, transform: `translateY(${(1 - o) * 20}px)`, display: 'flex', flexDirection: 'column', gap: 16,
    }}>
      <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Safeguard</div>
      <div style={{ fontFamily: SERIF, fontSize: 50, fontWeight: 600, color: INK }}>{title}</div>
      {children}
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', gap: 48,
      }}>
        <Card title="Every value is traceable" o={a}>
          <div style={{ fontFamily: MONO, fontSize: 36, color: INK, whiteSpace: 'nowrap' }}>a = 2.5  ← “accelerates at 2.5 m/s²”</div>
        </Card>
        <Card title="Errors kept separate" o={b}>
          <div style={{ fontFamily: MONO, fontSize: 36, color: INK, whiteSpace: 'nowrap' }}>parse error  ≠  not covered</div>
        </Card>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x + 70, width: SAFE.w - 140, top: SAFE.y + 400,
        padding: '30px 48px', background: CLAUDE.CARD, border: `3px solid ${ACCENT}`, opacity: gap,
        transform: `translateY(${(1 - gap) * 20}px)`, display: 'flex', flexDirection: 'column', gap: 18,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 30, letterSpacing: 3, color: ACCENT, textTransform: 'uppercase', fontWeight: 700 }}>Not proven yet</div>
        <div style={{ fontFamily: SANS, fontSize: 42, color: INK, lineHeight: 1.3 }}>Parse quality hasn’t been measured against a real model beyond spot checks.</div>
        <div style={{ fontFamily: SANS, fontSize: 42, color: INK, lineHeight: 1.3, opacity: remap(p, 0.74, 0.82, 0, 1) }}>Newer Claude models take no randomness setting — so this one step can vary between runs.</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the verdict. Check what it read before what it got.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe4Verdict: React.FC<{ spark?: string }> = ({ spark = 'Check the reading.' }) => {
  const p = useP();
  const q = ease(remap(p, 0.06, 0.24, 0, 1));
  const sub = ease(remap(p, 0.44, 0.60, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 200, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 60,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: 104, fontWeight: 600, color: INK, opacity: q, lineHeight: 1.15,
          textAlign: 'center', maxWidth: 1600, transform: `translateY(${(1 - q) * 26}px)`,
        }}>Check what it <span style={{ color: ACCENT }}>read</span><br />before you check what it got.</div>
        <div style={{
          padding: '28px 48px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: sub,
          fontFamily: SANS, fontSize: 46, color: INK, maxWidth: 1400, textAlign: 'center', lineHeight: 1.35,
        }}>A number that wasn’t in the problem is a guess — and everything built on it is wrong.</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Title, terracotta period, host name, credit lines.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe4Outro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = "Don't Invent the Mass.", handle = 'Param Madan', subline = 'Physics Engine · 4 of 12' }) => {
  const p = useP();
  const rise = ease(remap(p, 0.02, 0.30, 0, 1));
  const nameO = remap(p, 0.24, 0.48, 0, 1);
  const subO = remap(p, 0.44, 0.66, 0, 1);
  const hasDot = title.trim().endsWith('.');
  const stem = hasDot ? title.trim().slice(0, -1) : title.trim();
  return (
    <AbsoluteFill style={{
      background: CLAUDE.PAGE, display: 'flex', flexDirection: 'column',
      alignItems: 'center', justifyContent: 'center', gap: 30,
    }}>
      <div style={{
        fontFamily: SERIF, fontSize: 160, lineHeight: 1.04, fontWeight: 600, color: INK,
        maxWidth: SAFE.w, textAlign: 'center',
        opacity: rise, transform: `translateY(${(1 - rise) * 40}px)`,
      }}>
        {stem}{hasDot && <span style={{ color: ACCENT }}>.</span>}
      </div>
      <div style={{
        fontFamily: SERIF, fontSize: 86, color: INK, opacity: nameO,
        transform: `translateY(${(1 - ease(nameO)) * 22}px)`,
      }}>{handle}</div>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12, opacity: subO }}>
        {subline.split(' · ').map((line) => (
          <div key={line} style={{
            fontFamily: SANS, fontSize: 36, letterSpacing: 3, textTransform: 'uppercase',
            color: SOFT, textAlign: 'center', whiteSpace: 'nowrap',
          }}>{line}</div>
        ))}
      </div>
    </AbsoluteFill>
  );
};
