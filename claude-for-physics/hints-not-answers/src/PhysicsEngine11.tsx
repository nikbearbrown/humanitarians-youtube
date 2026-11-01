/**
 * PhysicsEngine11.tsx — body scenes for "Hints, Not Answers." (physics engine, 11 of 12).
 *
 * Reel: books/physics-engine/youtube/hints-not-answers
 * Host: Param Madan · voice Kokoro af_bella
 * Source: github.com/jashshah127/humanitariansai/physics-engine @ 2dc4aa4
 *         (engine/physics_mode.py _ROUTE_MAP, _hint_ladder; MEASUREMENT.md; golden MECH-003).
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent marks the
 * verified badge, the labeled fallback, the symbolic rung, and the final rung.
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

/** One rung of the hint ladder. */
const Rung: React.FC<{ n: number; text: React.ReactNode; o: number; hot?: boolean; mono?: boolean }> = ({
  n, text, o, hot = false, mono = false,
}) => (
  <div style={{
    display: 'flex', alignItems: 'center', gap: 30, padding: '18px 34px', background: CLAUDE.CARD,
    border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`, opacity: o,
    transform: `translateX(${(1 - o) * -24}px)`,
  }}>
    <div style={{ fontFamily: SERIF, fontSize: 56, fontWeight: 600, color: hot ? ACCENT : SOFT, width: 50 }}>{n}</div>
    <div style={{ fontFamily: mono ? MONO : SANS, fontSize: mono ? 38 : 38, color: INK, lineHeight: 1.3 }}>{text}</div>
  </div>
);

/* ────────────────────────────────────────────────────────────────────────────
 * B00B — the promise. Three things this video shows.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe11Promise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'The next step, not the answer.',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.04, 0.18, 0, 1));
  const items = [
    { v: 'Badges', c: 'on every answer', hot: false },
    { v: '7 hints', c: 'rung by rung', hot: true },
    { v: 'Better', c: 'once the math went symbolic', hot: false },
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
 * B01 — the three badges.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe11Badges: React.FC<{ spark?: string }> = ({ spark = 'The badge is the product.' }) => {
  const p = useP();
  const rows = [
    { b: 'Verified', d: 'a symbolic solver computed this', at: 0.18, hot: true },
    { b: 'Needs review', d: 'more than one principle fits — here is each result', at: 0.34, hot: false },
    { b: 'Unverified', d: 'nothing in the library covers this — AI reasoning', at: 0.54, hot: false },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 170, width: SAFE.w - 340, top: SAFE.y + 100,
        display: 'flex', flexDirection: 'column', gap: 20,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', opacity: remap(p, 0.04, 0.10, 0, 1) }}>Physics Engine mode: on</div>
        {rows.map((r) => (
          <div key={r.b} style={{
            display: 'flex', alignItems: 'center', gap: 40, padding: '24px 40px', background: CLAUDE.CARD,
            border: `${r.hot ? 3 : 2}px solid ${r.hot ? ACCENT : HAIR}`, opacity: ease(remap(p, r.at, r.at + 0.07, 0, 1)),
          }}>
            <div style={{ width: 360, fontFamily: SERIF, fontSize: 56, fontWeight: 600, color: r.hot ? ACCENT : INK }}>{r.b}</div>
            <div style={{ fontFamily: SANS, fontSize: 38, color: INK, lineHeight: 1.3 }}>{r.d}</div>
          </div>
        ))}
      </div>
      <RecordStrip text="“That visible status IS the product.”" o={remap(p, 0.80, 0.90, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — the floor. Unverified = switch off, labeled.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe11Floor: React.FC<{ spark?: string }> = ({ spark = 'Never worse than off.' }) => {
  const p = useP();
  const a = ease(remap(p, 0.04, 0.16, 0, 1));
  const b = ease(remap(p, 0.20, 0.34, 0, 1));
  const c = ease(remap(p, 0.66, 0.78, 0, 1));
  const Box: React.FC<{ t: string; body: string; o: number; hot?: boolean }> = ({ t, body, o, hot = false }) => (
    <div style={{
      width: 680, padding: '30px 42px', background: CLAUDE.CARD,
      border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`, opacity: o,
      transform: `translateY(${(1 - o) * 22}px)`, display: 'flex', flexDirection: 'column', gap: 12,
    }}>
      <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: hot ? ACCENT : SOFT, textTransform: 'uppercase', fontWeight: hot ? 700 : 500 }}>{t}</div>
      <div style={{ fontFamily: SERIF, fontSize: 48, color: INK, lineHeight: 1.25 }}>{body}</div>
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 110,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 40,
      }}>
        <Box t="Switch off" body="a fluent AI answer, no label" o={a} />
        <div style={{ fontFamily: MONO, fontSize: 60, color: SOFT, opacity: b }}>=</div>
        <Box t="Switch on · unverified path" body="the same AI answer — labeled Unverified" o={b} hot />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 470, textAlign: 'center',
        fontFamily: SERIF, fontSize: 58, fontWeight: 600, color: INK, opacity: c,
      }}>An unverified answer never leaves wearing a verified label.</div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — the ladder, rungs 1–4 (MECH-003).
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe11Rungs1: React.FC<{ spark?: string }> = ({ spark = 'One rung at a time.' }) => {
  const p = useP();
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 130, width: SAFE.w - 260, top: SAFE.y + 96,
        display: 'flex', flexDirection: 'column', gap: 16,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', opacity: remap(p, 0.04, 0.10, 0, 1) }}>Pulley · m1 = 4 kg, m2 = 6 kg</div>
        <Rung n={1} o={ease(remap(p, 0.12, 0.20, 0, 1))} text="Given: m1 = 4, m2 = 6. Find: a, T." />
        <Rung n={2} o={ease(remap(p, 0.28, 0.36, 0, 1))} text="A dynamics problem. Principle: the Atwood machine." />
        <Rung n={3} o={ease(remap(p, 0.46, 0.54, 0, 1))} text="Check first: frictionless massless pulley, string that doesn’t stretch." />
        <Rung n={4} o={ease(remap(p, 0.74, 0.82, 0, 1))} hot mono text="T − g·m1 = a·m1   ·   g·m2 − T = a·m2" />
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — the ladder, rungs 5–7. The answer is last.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe11Rungs2: React.FC<{ spark?: string }> = ({ spark = 'The answer comes last.' }) => {
  const p = useP();
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 130, width: SAFE.w - 260, top: SAFE.y + 96,
        display: 'flex', flexDirection: 'column', gap: 16,
      }}>
        <div style={{ display: 'flex', gap: 14, opacity: 0.55 }}>
          {[1, 2, 3, 4].map((n) => (
            <div key={n} style={{
              padding: '8px 34px', border: `2px solid ${HAIR}`, background: CLAUDE.CARD,
              fontFamily: SANS, fontSize: 28, color: SOFT,
            }}>hint {n} ✓</div>
          ))}
        </div>
        <Rung n={5} o={ease(remap(p, 0.04, 0.12, 0, 1))} text="Avoid: inconsistent signs across the two masses’ equations." />
        <Rung n={6} o={ease(remap(p, 0.30, 0.38, 0, 1))} mono text="a = g·(m2 − m1) / (m1 + m2)" />
        <Rung n={7} o={ease(remap(p, 0.66, 0.74, 0, 1))} hot mono text="a = 1.96 m/s²   ·   T = 47.04 N" />
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — design. From the plan; withheld on purpose.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe11Design: React.FC<{ spark?: string }> = ({ spark = 'Built from the plan.' }) => {
  const p = useP();
  const plan = ease(remap(p, 0.04, 0.16, 0, 1));
  const no = ease(remap(p, 0.30, 0.40, 0, 1));
  const held = ease(remap(p, 0.46, 0.60, 0, 1));
  const parts = ['card', 'conditions', 'equations', 'warning'];
  const hidden = ['the answer', 'the equations', 'the card’s name'];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 110,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 20, opacity: plan,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 30, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', marginRight: 12 }}>The plan holds</div>
        {parts.map((x) => (
          <span key={x} style={{ padding: '10px 26px', border: `2px solid ${HAIR}`, background: CLAUDE.CARD, fontFamily: SERIF, fontSize: 44, color: INK }}>{x}</span>
        ))}
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 230, textAlign: 'center', opacity: no,
        fontFamily: SERIF, fontSize: 60, fontWeight: 600, color: INK,
      }}>No second AI call — <span style={{ color: ACCENT }}>a hint can’t invent a step</span>.</div>
      <div style={{
        position: 'absolute', left: SAFE.x + 260, width: SAFE.w - 520, top: SAFE.y + 380,
        padding: '28px 44px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: held,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Tutor mode holds back</div>
        <div style={{ display: 'flex', gap: 18, marginTop: 16, flexWrap: 'wrap' }}>
          {hidden.map((x) => (
            <span key={x} style={{ padding: '8px 22px', border: `2px solid ${HAIR}`, fontFamily: SANS, fontSize: 38, color: SOFT, textDecoration: 'line-through' }}>{x}</span>
          ))}
        </div>
        <div style={{ fontFamily: SANS, fontSize: 32, color: SOFT, marginTop: 16 }}>The card’s name is hint two.</div>
      </div>
      <RecordStrip text="Each rung reveals strictly less than the next." o={remap(p, 0.84, 0.93, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — evidence. Symbolic hints teach; caching made them faster.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe11Better: React.FC<{ spark?: string }> = ({ spark = 'The unexpected win.' }) => {
  const p = useP();
  const b = ease(remap(p, 0.12, 0.24, 0, 1));
  const a = ease(remap(p, 0.40, 0.52, 0, 1));
  const ms = ease(remap(p, 0.62, 0.74, 0, 1));
  const gap = ease(remap(p, 0.86, 0.94, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 200, width: SAFE.w - 400, top: SAFE.y + 100,
        display: 'flex', flexDirection: 'column', gap: 18,
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 34, padding: '22px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: b }}>
          <div style={{ width: 230, fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Hint 4, before</div>
          <div style={{ fontFamily: MONO, fontSize: 52, color: SOFT, textDecoration: 'line-through' }}>T − 39.2 = 4a</div>
          <div style={{ fontFamily: SANS, fontSize: 30, color: SOFT }}>arithmetic leaked</div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 34, padding: '22px 40px', background: CLAUDE.CARD, border: `3px solid ${ACCENT}`, opacity: a }}>
          <div style={{ width: 230, fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: ACCENT, textTransform: 'uppercase', fontWeight: 700 }}>Hint 4, now</div>
          <div style={{ fontFamily: MONO, fontSize: 52, color: INK, fontWeight: 700 }}>T − g·m1 = a·m1</div>
          <div style={{ fontFamily: SANS, fontSize: 30, color: INK }}>teaches the relationship</div>
        </div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 400,
        display: 'flex', justifyContent: 'center', gap: 34, opacity: ms,
      }}>
        <Tile value="11.04 ms" caption="per problem, before" o={1} w={440} size={84} />
        <Tile value="6.30 ms" caption="with caching" o={1} w={440} size={84} />
      </div>
      <RecordStrip text="Not proven yet: no student has used it." o={gap} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the verdict. Ask for the next step.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe11Verdict: React.FC<{ spark?: string }> = ({ spark = 'One hint at a time.' }) => {
  const p = useP();
  const q = ease(remap(p, 0.06, 0.26, 0, 1));
  const sub = ease(remap(p, 0.46, 0.62, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 190, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 60,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: 100, fontWeight: 600, color: INK, opacity: q, lineHeight: 1.15,
          textAlign: 'center', maxWidth: 1650, transform: `translateY(${(1 - q) * 26}px)`,
        }}>A good tutor gives you<br />the <span style={{ color: ACCENT }}>next step</span>, not the last one.</div>
        <div style={{
          padding: '28px 48px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: sub,
          fontFamily: SANS, fontSize: 46, color: INK, maxWidth: 1400, textAlign: 'center', lineHeight: 1.35,
        }}>Ask for one hint at a time — and try each step before the next.</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Title, terracotta period, host name, credit lines.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe11Outro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = 'Hints, Not Answers.', handle = 'Param Madan', subline = 'Physics Engine · 11 of 12' }) => {
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
