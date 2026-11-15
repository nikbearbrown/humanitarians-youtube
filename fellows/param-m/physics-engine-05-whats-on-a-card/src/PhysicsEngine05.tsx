/**
 * PhysicsEngine05.tsx — body scenes for "What's on a Card." (physics engine, 5 of 12).
 *
 * Reel: books/physics-engine/youtube/whats-on-a-card
 * Host: Param Madan · voice Kokoro af_bella
 * Source: github.com/jashshah127/humanitariansai/physics-engine @ 2dc4aa4
 *         (engine/formula_kb.py MECH-ENE-SPRING, WAVE-FROM-EQUATION; COVERAGE.md).
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent marks the
 * card's equation, its stated assumption, the pitfall symbol, and the checks.
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

/** A labeled field row on a formula card. */
const Field: React.FC<{ label: string; o: number; hot?: boolean; children: React.ReactNode }> = ({ label, o, hot = false, children }) => (
  <div style={{
    display: 'flex', alignItems: 'baseline', gap: 30, padding: '14px 0',
    borderTop: `2px solid ${HAIR}`, opacity: o, transform: `translateX(${(1 - o) * -20}px)`,
  }}>
    <div style={{
      width: 360, flexShrink: 0, fontFamily: SANS, fontSize: 28, letterSpacing: 3, whiteSpace: 'nowrap',
      textTransform: 'uppercase', color: hot ? ACCENT : SOFT, fontWeight: hot ? 700 : 500,
    }}>{label}</div>
    <div style={{ fontFamily: MONO, fontSize: 40, color: hot ? ACCENT : INK, fontWeight: hot ? 700 : 500 }}>{children}</div>
  </div>
);

/* ────────────────────────────────────────────────────────────────────────────
 * B00B — the promise. Three things this video shows.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe5Promise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'The physics the engine trusts.',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.04, 0.18, 0, 1));
  const items = [
    { v: 'One card', c: 'a real one, field by field', hot: false },
    { v: 'Warnings', c: 'conditions and pitfalls', hot: false },
    { v: 'Built', c: 'against real problems', hot: true },
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
 * B01 — the BLUF. A card is a small, checked package.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe5Package: React.FC<{ spark?: string }> = ({ spark = 'A checked package.' }) => {
  const p = useP();
  const card = ease(remap(p, 0.04, 0.12, 0, 1));
  const rows = [
    { l: 'Equations', v: 'what to solve', at: 0.10 },
    { l: 'When it applies', v: 'the conditions', at: 0.16 },
    { l: 'Knowns needed', v: 'what you must be given', at: 0.22 },
    { l: 'Common mistakes', v: 'the usual slip', at: 0.28 },
  ];
  const stamp = ease(remap(p, 0.74, 0.84, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 230, width: SAFE.w - 460, top: SAFE.y + 90,
        padding: '34px 50px 20px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: card,
      }}>
        <div style={{ fontFamily: SERIF, fontSize: 60, fontWeight: 600, color: INK, marginBottom: 14 }}>A formula card</div>
        {rows.map((r) => (
          <Field key={r.l} label={r.l} o={ease(remap(p, r.at, r.at + 0.06, 0, 1))}>
            <span style={{ fontFamily: SANS }}>{r.v}</span>
          </Field>
        ))}
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 660,
        display: 'flex', justifyContent: 'center', gap: 40, alignItems: 'center',
        opacity: ease(remap(p, 0.44, 0.56, 0, 1)),
      }}>
        <div style={{ fontFamily: SANS, fontSize: 40, color: INK }}>The engine can only solve what its cards cover.</div>
        <span style={{
          padding: '12px 30px', border: `3px solid ${ACCENT}`, background: CLAUDE.CARD, opacity: stamp,
          fontFamily: MONO, fontSize: 36, fontWeight: 700, color: ACCENT, whiteSpace: 'nowrap',
        }}>checked against known answers</span>
      </div>
      <RecordStrip text="That’s a limit — and the guarantee: every answer traces back to a card."
        o={remap(p, 0.86, 0.95, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — anatomy. The spring card, field by field.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe5Anatomy: React.FC<{ spark?: string }> = ({ spark = 'One real card.' }) => {
  const p = useP();
  const card = ease(remap(p, 0.02, 0.10, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 170, width: SAFE.w - 340, top: SAFE.y + 96,
        padding: '30px 50px 18px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: card,
      }}>
        <div style={{ fontFamily: MONO, fontSize: 28, color: SOFT, letterSpacing: 1 }}>MECH-ENE-SPRING</div>
        <div style={{ fontFamily: SERIF, fontSize: 60, fontWeight: 600, color: INK, marginBottom: 14 }}>Spring energy to kinetic energy</div>
        <Field label="Needs" o={ease(remap(p, 0.12, 0.18, 0, 1))}>m · k · x</Field>
        <Field label="Solves for" o={ease(remap(p, 0.34, 0.40, 0, 1))}>v</Field>
        <Field label="Equation" o={ease(remap(p, 0.46, 0.54, 0, 1))} hot>½·k·x² = ½·m·v²</Field>
        <Field label="Units" o={ease(remap(p, 0.76, 0.82, 0, 1))}>v in m/s</Field>
        <Field label="Must be" o={ease(remap(p, 0.86, 0.92, 0, 1))}>v &gt; 0</Field>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — conditions. Applicability becomes the solution's stated assumption.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe5Assume: React.FC<{ spark?: string }> = ({ spark = 'What had to be true.' }) => {
  const p = useP();
  const cond = ease(remap(p, 0.04, 0.14, 0, 1));
  const sol = ease(remap(p, 0.30, 0.42, 0, 1));
  const nums = ease(remap(p, 0.62, 0.74, 0, 1));
  const ans = ease(remap(p, 0.84, 0.92, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 40,
      }}>
        <div style={{
          width: 700, padding: '30px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: cond,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', marginBottom: 12 }}>The card says it applies to</div>
          <div style={{ fontFamily: SERIF, fontSize: 44, color: INK, lineHeight: 1.35 }}>an ideal spring, a frictionless surface, all stored energy turned into motion</div>
        </div>
        <div style={{ fontFamily: MONO, fontSize: 60, color: SOFT, opacity: sol }}>→</div>
        <div style={{
          width: 700, padding: '30px 40px', background: CLAUDE.CARD, border: `3px solid ${ACCENT}`, opacity: sol,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: ACCENT, textTransform: 'uppercase', fontWeight: 700, marginBottom: 12 }}>The solution states</div>
          <div style={{ fontFamily: MONO, fontSize: 38, color: INK, lineHeight: 1.45 }}>assumptions:<br />ideal spring, frictionless,<br />all PE → KE</div>
        </div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 520,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 28,
      }}>
        <div style={{ fontFamily: MONO, fontSize: 46, color: INK, opacity: nums, whiteSpace: 'nowrap' }}>m = 2 kg · k = 500 N/m · x = 0.15 m</div>
        <div style={{ fontFamily: MONO, fontSize: 54, color: SOFT, opacity: ans }}>→</div>
        <div style={{ fontFamily: MONO, fontSize: 64, fontWeight: 700, color: INK, opacity: ans, whiteSpace: 'nowrap' }}>v ≈ 2.37 m/s</div>
      </div>
      <RecordStrip text="Not just the answer — what had to be true for it to hold."
        o={remap(p, 0.42, 0.52, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — pitfalls. The usual mistake travels with the formula.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe5Pitfalls: React.FC<{ spark?: string }> = ({ spark = 'The usual slip.' }) => {
  const p = useP();
  const w = ease(remap(p, 0.12, 0.24, 0, 1));
  const fix = ease(remap(p, 0.40, 0.50, 0, 1));
  const k = ease(remap(p, 0.62, 0.74, 0, 1));
  const Card: React.FC<{ id: string; o: number; children: React.ReactNode }> = ({ id, o, children }) => (
    <div style={{
      width: 790, height: 470, padding: '32px 42px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
      opacity: o, transform: `translateY(${(1 - o) * 24}px)`, display: 'flex', flexDirection: 'column', gap: 20,
    }}>
      <div style={{ fontFamily: MONO, fontSize: 28, color: SOFT }}>{id}</div>
      {children}
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', gap: 48,
      }}>
        <Card id="WAVE-FROM-EQUATION · pitfall" o={w}>
          <div style={{ fontFamily: MONO, fontSize: 50, color: INK, whiteSpace: 'nowrap' }}>
            y = A sin(<span style={{ color: ACCENT, fontWeight: 700 }}>k</span>·x − ω·t)
          </div>
          <div style={{ fontFamily: SANS, fontSize: 40, color: INK, lineHeight: 1.3 }}>
            <span style={{ color: ACCENT, fontWeight: 700 }}>k</span> is the wave <b>number</b> — not the wavelength.
          </div>
          <div style={{ marginTop: 'auto', fontFamily: MONO, fontSize: 48, fontWeight: 700, color: INK, opacity: fix }}>λ = 2π / k</div>
        </Card>
        <Card id="MECH-KIN-1D · pitfall" o={k}>
          <div style={{ fontFamily: SERIF, fontSize: 50, color: INK }}>“starts from rest”</div>
          <div style={{ fontFamily: SANS, fontSize: 40, color: INK, lineHeight: 1.3 }}>Forgetting it means a starting speed of zero.</div>
          <div style={{ marginTop: 'auto', fontFamily: MONO, fontSize: 48, fontWeight: 700, color: INK }}>v0 = 0</div>
        </Card>
      </div>
      <RecordStrip text="The warning sits right next to the formula it’s about."
        o={remap(p, 0.86, 0.95, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — evidence. Zero cards to eight, each checked against published answers.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe5Built: React.FC<{ spark?: string }> = ({ spark = 'Built against real answers.' }) => {
  const p = useP();
  const gap = ease(remap(p, 0.10, 0.22, 0, 1));
  const eight = ease(remap(p, 0.34, 0.44, 0, 1));
  const checks = [
    { q: 'Wavelength', v: '4 cm', at: 0.56 },
    { q: 'Wave speed', v: '60 cm/s', at: 0.64 },
    { q: 'Moon escape velocity', v: '2.37 km/s', at: 0.74 },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 40,
      }}>
        <Tile value="179" caption="vibrations & waves problems" o={gap} w={460} size={110} />
        <Tile value={eight > 0.5 ? '8' : '0'} caption={eight > 0.5 ? 'cards built' : 'cards'} o={gap} w={460} size={110} accent={eight > 0.5} />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x + 270, width: SAFE.w - 540, top: SAFE.y + 400,
        display: 'flex', flexDirection: 'column', gap: 12,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', opacity: remap(p, 0.50, 0.56, 0, 1) }}>Checked against the benchmark’s published answers</div>
        {checks.map((c) => {
          const o = ease(remap(p, c.at, c.at + 0.05, 0, 1));
          return (
            <div key={c.q} style={{
              display: 'flex', alignItems: 'center', padding: '14px 30px', background: CLAUDE.CARD,
              border: `2px solid ${HAIR}`, opacity: o,
            }}>
              <div style={{ flex: 1, fontFamily: SERIF, fontSize: 42, color: INK }}>{c.q}</div>
              <div style={{ width: 300, fontFamily: MONO, fontSize: 40, fontWeight: 600, color: INK }}>{c.v}</div>
              <div style={{ fontFamily: MONO, fontSize: 36, fontWeight: 700, color: ACCENT }}>✓ match</div>
            </div>
          );
        })}
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — honest. Footholds, not depth; one symbol, two meanings.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe5Thin: React.FC<{ spark?: string }> = ({ spark = 'Footholds, not depth.' }) => {
  const p = useP();
  const t = ease(remap(p, 0.10, 0.22, 0, 1));
  const col = ease(remap(p, 0.40, 0.52, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 230,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 60,
      }}>
        <Tile value="180 : 1" caption="rigid-body problems : cards" o={t} w={620} size={120} />
        <div style={{
          width: 900, padding: '30px 44px', background: CLAUDE.CARD, border: `3px solid ${ACCENT}`, opacity: col,
          transform: `translateY(${(1 - col) * 20}px)`, display: 'flex', flexDirection: 'column', gap: 16,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: ACCENT, textTransform: 'uppercase', fontWeight: 700 }}>One symbol, two meanings</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 34 }}>
            <div style={{ fontFamily: MONO, fontSize: 120, fontWeight: 700, color: ACCENT }}>T</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
              <div style={{ fontFamily: SANS, fontSize: 40, color: INK }}>tension — on the pulley card</div>
              <div style={{ fontFamily: SANS, fontSize: 40, color: INK }}>period — on two other cards</div>
            </div>
          </div>
        </div>
      </div>
      <RecordStrip text="Today the right card still wins. At scale, the team warns, it eventually won’t."
        o={remap(p, 0.72, 0.82, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the verdict. A formula comes with its conditions.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe5Verdict: React.FC<{ spark?: string }> = ({ spark = 'Ask for the conditions.' }) => {
  const p = useP();
  const q = ease(remap(p, 0.06, 0.24, 0, 1));
  const ask = ease(remap(p, 0.40, 0.56, 0, 1));
  const qs = ['When does it apply?', 'What’s the usual mistake?'];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 200, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 64,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: 100, fontWeight: 600, color: INK, opacity: q, lineHeight: 1.15,
          textAlign: 'center', maxWidth: 1600, transform: `translateY(${(1 - q) * 26}px)`,
        }}>A formula is only as good as<br />its <span style={{ color: ACCENT }}>conditions</span>.</div>
        <div style={{ display: 'flex', gap: 34, opacity: ask, transform: `translateY(${(1 - ask) * 20}px)` }}>
          {qs.map((t) => (
            <div key={t} style={{
              padding: '18px 36px', border: `2px solid ${ACCENT}`, background: CLAUDE.CARD,
              fontFamily: SERIF, fontSize: 52, fontWeight: 600, color: INK, whiteSpace: 'nowrap',
            }}>{t}</div>
          ))}
        </div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Title, terracotta period, host name, credit lines.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe5Outro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = "What's on a Card.", handle = 'Param Madan', subline = 'Physics Engine · 5 of 12' }) => {
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
