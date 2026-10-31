/**
 * PhysicsEngine02.tsx — body scenes for "A Comma Changed the Answer." (physics engine, 2 of 17).
 *
 * Reel: books/physics-engine/youtube/a-comma-changed-the-answer
 * Host: Param Madan · voice Kokoro af_bella
 * Sources: github.com/jashshah127/humanitariansai/physics-engine @ 2dc4aa4;
 *          Singh & Strouse 2024, arXiv 2402.14903 (GPT-3.5 figures only).
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent always
 * marks the exact side — the calculator in B01, the left-to-right chunks in
 * B02, the comma result in B03, the wrong answers in B04, SymPy in B05.
 *
 * FACT NOTE: the study figures are dated (March 2023 model, published Feb 2024)
 * and are props with an "as of" caption, so updating them is a beat-sheet edit.
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

/** Small mono source line, for dated or external figures. */
const SourceLine: React.FC<{ text: string; o: number; top: number }> = ({ text, o, top }) => (
  <div style={{
    position: 'absolute', left: SAFE.x, width: SAFE.w, top, textAlign: 'center',
    fontFamily: MONO, fontSize: 28, color: SOFT, opacity: o,
  }}>{text}</div>
);

/* ────────────────────────────────────────────────────────────────────────────
 * B00B — the promise. Three things this video shows.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe2Promise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'How an AI sees a number.',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.04, 0.18, 0, 1));
  const items = [
    { v: 'Chunks', c: 'how the model sees numbers', hot: false },
    { v: 'Fragile', c: 'even with no randomness', hot: false },
    { v: 'Exact', c: 'what the engine does instead', hot: true },
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
            o={ease(remap(p, 0.12 + i * 0.22, 0.28 + i * 0.22, 0, 1))} />
        ))}
      </div>
      <RecordStrip text="No math or coding background needed." o={remap(p, 0.84, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B01 — the BLUF. A model predicts; a calculator follows rules.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe2Guess: React.FC<{ spark?: string }> = ({ spark = 'Guess, or rule.' }) => {
  const p = useP();
  const left = ease(remap(p, 0.04, 0.20, 0, 1));
  const right = ease(remap(p, 0.50, 0.66, 0, 1));
  const Col: React.FC<{
    who: string; how: string; verdict: string; o: number; hot?: boolean;
  }> = ({ who, how, verdict, o, hot = false }) => (
    <div style={{
      width: 800, height: 520, padding: '46px 54px', background: CLAUDE.CARD,
      border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`,
      opacity: o, transform: `translateY(${(1 - o) * 28}px)`,
      display: 'flex', flexDirection: 'column', gap: 22,
    }}>
      <div style={{ fontFamily: SERIF, fontSize: 96, fontWeight: 600, color: hot ? ACCENT : INK, lineHeight: 1.05 }}>{who}</div>
      <div style={{ height: 2, background: HAIR }} />
      <div style={{ fontFamily: SANS, fontSize: 46, color: INK, lineHeight: 1.35 }}>{how}</div>
      <div style={{ marginTop: 'auto', fontFamily: SERIF, fontSize: 64, fontWeight: 600, color: hot ? ACCENT : SOFT }}>{verdict}</div>
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 120, width: SAFE.w,
        display: 'flex', justifyContent: 'center', gap: 64,
      }}>
        <Col who="Language model" how="predicts the next piece of text" verdict="usually right" o={left} />
        <Col who="Calculator" how="follows exact rules" verdict="right every time" o={right} hot />
      </div>
      <RecordStrip text="Reading goes to the model. Every calculation goes to the calculator." o={remap(p, 0.84, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — tokens. 8302080 cut left-to-right into 830 | 208 | 0, against
 * place value 8 | 302 | 080.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe2Chunks: React.FC<{ spark?: string; digits?: string }> = ({
  spark = 'Chunks, not digits.', digits = '8302080',
}) => {
  const p = useP();
  const num = ease(remap(p, 0.04, 0.16, 0, 1));
  const l2r = ease(remap(p, 0.44, 0.60, 0, 1));
  const place = ease(remap(p, 0.74, 0.88, 0, 1));
  const D = 150; // one digit cell
  const ds = digits.split('');
  // Left-to-right: chunks of three from the left. Place value: from the right.
  const chunk = (fromRight: boolean) => {
    const out: number[][] = [];
    const idx = ds.map((_, i) => i);
    if (fromRight) {
      for (let e = idx.length; e > 0; e -= 3) out.unshift(idx.slice(Math.max(0, e - 3), e));
    } else {
      for (let s = 0; s < idx.length; s += 3) out.push(idx.slice(s, s + 3));
    }
    return out;
  };
  const Brackets: React.FC<{ groups: number[][]; o: number; hot?: boolean; label: string; y: number }> =
    ({ groups, o, hot = false, label, y }) => (
    <div style={{ position: 'absolute', left: 0, top: y, width: ds.length * D, height: 120, opacity: o }}>
      {groups.map((g, i) => (
        <div key={i} style={{
          position: 'absolute', left: g[0] * D + 10, width: g.length * D - 20, top: 0, height: 26,
          borderLeft: `5px solid ${hot ? ACCENT : SOFT}`, borderRight: `5px solid ${hot ? ACCENT : SOFT}`,
          borderBottom: `5px solid ${hot ? ACCENT : SOFT}`,
        }}>
          <div style={{
            position: 'absolute', top: 38, left: 0, right: 0, textAlign: 'center',
            fontFamily: MONO, fontSize: 46, color: hot ? ACCENT : SOFT, fontWeight: 600,
          }}>{g.map((k) => ds[k]).join('')}</div>
        </div>
      ))}
      <div style={{
        position: 'absolute', left: ds.length * D + 40, top: 20, width: 520, whiteSpace: 'nowrap',
        fontFamily: SANS, fontSize: 30, letterSpacing: 3, textTransform: 'uppercase', color: hot ? ACCENT : SOFT,
      }}>{label}</div>
    </div>
  );
  const W = ds.length * D + 560;
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{ position: 'absolute', left: SAFE.x + (SAFE.w - W) / 2, top: SAFE.y + 150, width: W, height: 640 }}>
        <div style={{ display: 'flex', opacity: num, transform: `translateY(${(1 - num) * 24}px)` }}>
          {ds.map((d, i) => (
            <div key={i} style={{
              width: D - 12, marginRight: 12, height: 200, background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontFamily: SERIF, fontSize: 150, fontWeight: 600, color: INK,
            }}>{d}</div>
          ))}
        </div>
        <Brackets groups={chunk(false)} o={l2r} hot label="How the model reads it" y={232} />
        <Brackets groups={chunk(true)} o={place} label="How place value works" y={400} />
      </div>
      <SourceLine text="GPT-3.5 / GPT-4 tokenizer (cl100k_base) · Singh & Strouse 2024"
        o={remap(p, 0.30, 0.40, 0, 1)} top={SAFE.y + 760} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — the comma experiment. 75.6% → 97.8%.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe2Experiment: React.FC<{
  spark?: string; before?: number; after?: number; source?: string;
}> = ({
  spark = 'Add commas.', before = 75.6, after = 97.8,
  source = 'Singh & Strouse 2024 · GPT-3.5 (Mar 2023) · 7–9 digit addition · 8-shot · temperature 0',
}) => {
  const p = useP();
  const a = ease(remap(p, 0.50, 0.66, 0, 1));
  const b = ease(remap(p, 0.70, 0.86, 0, 1));
  const MAXW = 1040;
  const Row: React.FC<{ form: string; label: string; val: number; t: number; hot?: boolean }> =
    ({ form, label, val, t, hot = false }) => (
    <div style={{ display: 'flex', alignItems: 'center', gap: 40, opacity: 0.2 + 0.8 * Math.min(1, t * 3) }}>
      <div style={{ width: 380, display: 'flex', flexDirection: 'column', gap: 8 }}>
        <div style={{ fontFamily: MONO, fontSize: 60, color: hot ? ACCENT : INK, fontWeight: 600 }}>{form}</div>
        <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, textTransform: 'uppercase', color: SOFT }}>{label}</div>
      </div>
      <div style={{ width: MAXW, height: 120, background: CLAUDE.CARD, border: `2px solid ${HAIR}`, position: 'relative' }}>
        <div style={{ position: 'absolute', left: 0, top: 0, bottom: 0, width: (MAXW * val / 100) * t, background: hot ? ACCENT : SOFT, opacity: hot ? 1 : 0.55 }} />
        <div style={{
          position: 'absolute', right: 26, top: 0, bottom: 0, display: 'flex', alignItems: 'center',
          fontFamily: SERIF, fontSize: 80, fontWeight: 600, color: INK, opacity: t,
        }}>{`${val.toFixed(1)}%`}</div>
      </div>
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 130, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 44,
      }}>
        <Eyebrow text="Same problems · only the formatting changes" o={remap(p, 0.30, 0.42, 0, 1)} />
        <Row form="8302080" label="default chunks" val={before} t={a} />
        <Row form="8,302,080" label="with commas" val={after} t={b} hot />
      </div>
      <SourceLine text={source} o={remap(p, 0.50, 0.60, 0, 1)} top={SAFE.y + 640} />
      <RecordStrip text="Same problems. Different punctuation." o={remap(p, 0.90, 0.97, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — the turn. Randomness was off; 98% right still means 2 wrong per 100.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe2NotRandom: React.FC<{ spark?: string }> = ({ spark = 'Not a coin flip.' }) => {
  const p = useP();
  const off = ease(remap(p, 0.04, 0.16, 0, 1));
  const grid = remap(p, 0.62, 0.80, 0, 1);
  const hot = ease(remap(p, 0.82, 0.90, 0, 1));
  const wrong = new Set([37, 82]);
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 20, top: SAFE.y + 140, width: 860,
        display: 'flex', flexDirection: 'column', gap: 28, opacity: off,
        transform: `translateY(${(1 - off) * 24}px)`,
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 28 }}>
          <div style={{ width: 150, height: 76, borderRadius: 38, background: HAIR, position: 'relative' }}>
            <div style={{ position: 'absolute', left: 8, top: 8, width: 60, height: 60, borderRadius: 30, background: SOFT }} />
          </div>
          <div style={{ fontFamily: SANS, fontSize: 40, letterSpacing: 3, textTransform: 'uppercase', color: SOFT }}>Randomness: off</div>
        </div>
        <div style={{ fontFamily: SERIF, fontSize: 76, fontWeight: 600, color: INK, lineHeight: 1.1 }}>
          The mistakes were<br />built in.
        </div>
        <div style={{ fontFamily: SANS, fontSize: 40, color: INK, lineHeight: 1.4, opacity: ease(remap(p, 0.34, 0.46, 0, 1)) }}>
          The gap shrinks in bigger models.<br />Smaller isn't zero.
        </div>
      </div>
      <div style={{ position: 'absolute', left: SAFE.x + 930, top: SAFE.y + 130, display: 'flex', flexDirection: 'column', gap: 20 }}>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(10, 58px)', gap: 10 }}>
          {Array.from({ length: 100 }, (_, i) => {
            const show = clampN(grid * 100 - i);
            const isWrong = wrong.has(i);
            return (
              <div key={i} style={{
                width: 58, height: 58, opacity: show,
                background: isWrong && hot > 0 ? ACCENT : CLAUDE.CARD,
                border: `2px solid ${isWrong && hot > 0 ? ACCENT : HAIR}`,
              }} />
            );
          })}
        </div>
        <div style={{ fontFamily: SERIF, fontSize: 48, color: INK, fontWeight: 600, opacity: hot }}>
          98% right = <span style={{ color: ACCENT }}>2 wrong</span> in every 100.
        </div>
      </div>
    </IlluStage>
  );
};
const clampN = (v: number) => Math.min(1, Math.max(0, v));

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — the handoff. Model writes knowns; SymPy computes; ten identical runs.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe2Handoff: React.FC<{ spark?: string; result?: string }> = ({
  spark = 'Hand it off.', result = 'a = 1.96 m/s²',
}) => {
  const p = useP();
  const m = ease(remap(p, 0.04, 0.16, 0, 1));
  const k = ease(remap(p, 0.12, 0.26, 0, 1));
  const s = ease(remap(p, 0.30, 0.44, 0, 1));
  const runs = remap(p, 0.74, 0.90, 0, 10);
  const Box: React.FC<{ o: number; hot?: boolean; children: React.ReactNode; w: number }> = ({ o, hot = false, children, w }) => (
    <div style={{
      width: w, padding: '28px 32px', background: CLAUDE.CARD, border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`,
      opacity: o, transform: `translateY(${(1 - o) * 22}px)`, display: 'flex', flexDirection: 'column', gap: 12,
    }}>{children}</div>
  );
  const Arrow: React.FC<{ o: number }> = ({ o }) => (
    <svg width={70} height={40} style={{ opacity: o, flexShrink: 0 }}>
      <line x1={4} y1={20} x2={56} y2={20} stroke={INK} strokeWidth={4} />
      <polygon points="52,8 68,20 52,32" fill={INK} />
    </svg>
  );
  const Lbl: React.FC<{ t: string }> = ({ t }) => (
    <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, textTransform: 'uppercase', color: SOFT }}>{t}</div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 120, width: SAFE.w,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 18,
      }}>
        <Box o={m} w={360}>
          <Lbl t="The model" />
          <div style={{ fontFamily: SERIF, fontSize: 54, fontWeight: 600, color: INK }}>reads</div>
          <div style={{ fontFamily: SANS, fontSize: 32, color: SOFT, lineHeight: 1.3 }}>no numbers computed</div>
        </Box>
        <Arrow o={k} />
        <Box o={k} w={600}>
          <Lbl t="Writes down" />
          <div style={{ fontFamily: MONO, fontSize: 31, color: INK, lineHeight: 1.5, whiteSpace: 'nowrap' }}>
            knowns: m₁=4 kg, m₂=6 kg<br />unknowns: a, T<br />units: SI
          </div>
        </Box>
        <Arrow o={s} />
        <Box o={s} w={420} hot>
          <Lbl t="SymPy" />
          <div style={{ fontFamily: SERIF, fontSize: 54, fontWeight: 600, color: ACCENT }}>computes</div>
          <div style={{ fontFamily: SANS, fontSize: 32, color: SOFT, lineHeight: 1.3 }}>exact, by rule, no randomness</div>
        </Box>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x + 40, top: SAFE.y + 470, width: SAFE.w - 80,
        display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: 14,
      }}>
        {Array.from({ length: 10 }, (_, i) => (
          <div key={i} style={{
            padding: '18px 10px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, textAlign: 'center',
            fontFamily: MONO, fontSize: 30, color: INK, opacity: clampN(runs - i), whiteSpace: 'nowrap',
          }}><span style={{ color: SOFT }}>{`#${i + 1}  `}</span>{result}</div>
        ))}
      </div>
      <RecordStrip text="Same equations, same numbers, same answer — every time." o={remap(p, 0.90, 0.97, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — why exact matters. One reference for every student; symbolic hints.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe2Grading: React.FC<{ spark?: string }> = ({ spark = 'Fair, and teachable.' }) => {
  const p = useP();
  const st = ease(remap(p, 0.04, 0.18, 0, 1));
  const ref = ease(remap(p, 0.16, 0.30, 0, 1));
  const old = ease(remap(p, 0.50, 0.62, 0, 1));
  const strike = remap(p, 0.66, 0.74, 0, 1);
  const neu = ease(remap(p, 0.74, 0.86, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      {/* Left: two students, one reference answer. */}
      <div style={{
        position: 'absolute', left: SAFE.x + 40, top: SAFE.y + 130, width: 760,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 30,
      }}>
        <Eyebrow text="Grading" o={st} />
        <div style={{ display: 'flex', gap: 30, opacity: st }}>
          {['Student A', 'Student B'].map((s) => (
            <div key={s} style={{
              width: 300, padding: '24px 0', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, textAlign: 'center',
              fontFamily: SERIF, fontSize: 52, fontWeight: 600, color: INK,
            }}>{s}</div>
          ))}
        </div>
        <svg width={640} height={90} style={{ opacity: ref }}>
          <line x1={160} y1={0} x2={320} y2={80} stroke={INK} strokeWidth={4} />
          <line x1={480} y1={0} x2={320} y2={80} stroke={INK} strokeWidth={4} />
        </svg>
        <div style={{
          padding: '26px 44px', border: `3px solid ${ACCENT}`, background: CLAUDE.CARD, opacity: ref,
          fontFamily: SERIF, fontSize: 56, fontWeight: 600, color: ACCENT,
        }}>one reference answer</div>
      </div>
      {/* Right: the hint, before and after. */}
      <div style={{
        position: 'absolute', left: SAFE.x + 900, top: SAFE.y + 130, width: 820,
        display: 'flex', flexDirection: 'column', gap: 30,
      }}>
        <Eyebrow text="Tutor hint" o={old} />
        <div style={{ position: 'relative', padding: '30px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: old }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, textTransform: 'uppercase', color: SOFT }}>before · number leaked</div>
          <div style={{ fontFamily: MONO, fontSize: 66, color: SOFT, marginTop: 10 }}>T − 39.2 = 4a</div>
          <div style={{ position: 'absolute', left: 30, right: 30, top: '64%', height: 6, background: INK, transformOrigin: 'left', transform: `scaleX(${strike})` }} />
        </div>
        <div style={{ padding: '30px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: neu, transform: `translateY(${(1 - neu) * 22}px)` }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, textTransform: 'uppercase', color: SOFT }}>after · the relationship</div>
          <div style={{ fontFamily: MONO, fontSize: 66, color: INK, marginTop: 10 }}>T − g·m₁ = a·m₁</div>
        </div>
      </div>
      <RecordStrip text="Exact answers make grading fair, and hints teachable." o={remap(p, 0.90, 0.97, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the verdict. Calculated, or predicted?
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe2Verdict: React.FC<{ spark?: string }> = ({ spark = 'Ask one question.' }) => {
  const p = useP();
  const q = ease(remap(p, 0.06, 0.20, 0, 1));
  const tip = ease(remap(p, 0.30, 0.44, 0, 1));
  const rule = ease(remap(p, 0.76, 0.90, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 140, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 44,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: 120, fontWeight: 600, color: INK, opacity: q,
          transform: `translateY(${(1 - q) * 26}px)`,
        }}>Calculated, or <span style={{ color: ACCENT }}>predicted</span>?</div>
        <div style={{
          padding: '28px 48px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: tip,
          fontFamily: SANS, fontSize: 46, color: INK, maxWidth: 1400, textAlign: 'center', lineHeight: 1.35,
        }}>Need it right? Ask the AI to write the calculation as code — and run it.</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 640, textAlign: 'center',
        fontFamily: SERIF, fontSize: 80, fontWeight: 600, color: INK, opacity: rule,
      }}>Let the model read. <span style={{ color: ACCENT }}>Let a calculator calculate.</span></div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 770, textAlign: 'center',
        fontFamily: SANS, fontSize: 36, color: SOFT, opacity: remap(p, 0.62, 0.74, 0, 1),
      }}>The percentages will change as models change. The rule won't.</div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Title, terracotta period, host name, credit lines.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe2Outro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = 'A Comma Changed the Answer.', handle = 'Param Madan', subline = 'Physics Engine · 2 of 17' }) => {
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
