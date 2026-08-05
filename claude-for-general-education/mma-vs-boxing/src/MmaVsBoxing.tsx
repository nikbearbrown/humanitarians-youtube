/**
 * MmaVsBoxing.tsx — body scenes for "Cage, Rules, Belts." (MMA vs boxing).
 *
 * Reel: books/combat-sports/youtube/mma-vs-boxing
 * Host: Param Madan · voice Kokoro af_bella
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent always
 * marks the side of the comparison the beat is arguing about — the cage in
 * B01, the six MMA weapons in B02, the four sanctioning bodies in B04, the
 * vacant belt in B05. Nothing else competes for it.
 *
 * FACT NOTE: the belt holders on screen are live and expire. They are ledgered
 * with retrieval dates in the reel's SOURCES.md, and the reel says out loud
 * that names change while structure does not. Anything that would need
 * re-verifying to stay true is passed in as a prop, never hardcoded in a scene.
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

/** A stat tile: big value over a small caption. The reel's repeating unit. */
const Tile: React.FC<{
  value: string; caption: string; o: number; accent?: boolean; w?: number; lh?: number;
}> = ({ value, caption, o, accent = false, w = 452, lh = 0.9 }) => (
  <div style={{
    width: w, padding: '34px 28px 30px', background: CLAUDE.CARD,
    border: `2px solid ${accent ? ACCENT : HAIR}`, opacity: o,
    transform: `translateY(${(1 - o) * 26}px)`,
    display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 10,
  }}>
    <div style={{
      fontFamily: SERIF, fontSize: 132, lineHeight: lh,
      color: accent ? ACCENT : INK, fontWeight: 600,
    }}>{value}</div>
    <div style={{
      fontFamily: SANS, fontSize: 30, letterSpacing: 2.4,
      textTransform: 'uppercase', color: SOFT, textAlign: 'center',
    }}>{caption}</div>
  </div>
);

/** The lesson line that lands at the end of a beat, under a terracotta rule. */
const RecordStrip: React.FC<{ text: string; o: number }> = ({ text, o }) => (
  <div style={{
    position: 'absolute', left: SAFE.x, width: SAFE.w, bottom: 118,
    opacity: o, transform: `translateY(${(1 - o) * 18}px)`,
    display: 'flex', justifyContent: 'center',
  }}>
    <div style={{
      borderTop: `3px solid ${ACCENT}`, paddingTop: 20, maxWidth: 1500,
      fontFamily: SERIF, fontSize: 44, lineHeight: 1.25, color: INK, textAlign: 'center',
    }}>{text}</div>
  </div>
);

/* ────────────────────────────────────────────────────────────────────────────
 * B00B — the promise. What this video is and why it is worth watching.
 * ──────────────────────────────────────────────────────────────────────────── */
export const MvbPromise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'Three questions tell the two sports apart.',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.06, 0.22, 0, 1));
  const items = [
    { v: 'Cage', c: 'or ring', hot: true },
    { v: '1', c: 'weapon or six', hot: false },
    { v: '1', c: 'belt or four', hot: false },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 118, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 26,
      }}>
        <Eyebrow text="What this video is" o={remap(p, 0, 0.08, 0, 1)} />
        <div style={{
          fontFamily: SERIF, fontSize: 88, lineHeight: 1.12, color: INK,
          textAlign: 'center', maxWidth: 1580, fontWeight: 600,
          opacity: head, transform: `translateY(${(1 - head) * 30}px)`,
        }}>{headline}</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 360, width: SAFE.w,
        display: 'flex', justifyContent: 'center', gap: 30,
      }}>
        {items.map((n, i) => (
          <Tile key={n.c} value={n.v} caption={n.c} accent={n.hot} lh={1.12}
            o={ease(remap(p, 0.26 + i * 0.13, 0.46 + i * 0.13, 0, 1))} />
        ))}
      </div>
      <RecordStrip
        text="By the end you can tell which sport you are watching in one glance, and say who its champion is. No prior knowledge assumed."
        o={remap(p, 0.72, 0.88, 0, 1)}
      />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B01 — the floor plan. The fastest tell: eight-sided cage or square ring.
 * ──────────────────────────────────────────────────────────────────────────── */
export const MvbFloorPlan: React.FC<{ spark?: string }> = ({ spark = 'Look at the floor.' }) => {
  const p = useP();
  const cage = ease(remap(p, 0.06, 0.30, 0, 1));
  const ring = ease(remap(p, 0.38, 0.62, 0, 1));
  // An octagon inscribed in a 380-radius circle, drawn flat-topped.
  const oct = Array.from({ length: 8 }, (_, i) => {
    const a = (Math.PI / 4) * i + Math.PI / 8;
    return `${420 + 380 * Math.cos(a)},${420 + 380 * Math.sin(a)}`;
  }).join(' ');
  const Panel: React.FC<{
    sport: string; label: string; o: number; hot?: boolean; children: React.ReactNode;
  }> = ({ sport, label, o, hot = false, children }) => (
    <div style={{
      display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 22,
      opacity: o, transform: `translateY(${(1 - o) * 30}px)`,
    }}>
      <svg width={420} height={420} viewBox="0 0 840 840">{children}</svg>
      <div style={{
        fontFamily: SERIF, fontSize: 76, color: hot ? ACCENT : INK, fontWeight: 600,
      }}>{sport}</div>
      <div style={{
        fontFamily: SANS, fontSize: 32, letterSpacing: 3.4, textTransform: 'uppercase', color: SOFT,
      }}>{label}</div>
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 108, width: SAFE.w,
        display: 'flex', justifyContent: 'center', gap: 200,
      }}>
        <Panel sport="MMA" label="eight-sided cage" o={cage} hot>
          <polygon points={oct} fill="none" stroke={ACCENT} strokeWidth={14} />
          <polygon points={oct} fill={ACCENT} opacity={0.07} />
        </Panel>
        <Panel sport="Boxing" label="square ring, ropes" o={ring}>
          <rect x={60} y={60} width={720} height={720} fill="none" stroke={INK} strokeWidth={14} />
          {[0, 1, 2].map((i) => (
            <React.Fragment key={i}>
              <line x1={60} y1={190 + i * 200} x2={780} y2={190 + i * 200} stroke={SOFT} strokeWidth={7} />
            </React.Fragment>
          ))}
        </Panel>
      </div>
      <RecordStrip
        text="Cage means MMA. Ropes mean boxing. That glance never lies."
        o={remap(p, 0.74, 0.90, 0, 1)}
      />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — the rules. One legal weapon against six.
 * ──────────────────────────────────────────────────────────────────────────── */
export const MvbWeapons: React.FC<{ spark?: string }> = ({ spark = 'One tool, or six.' }) => {
  const p = useP();
  const mma = ['punches', 'kicks', 'knees', 'elbows', 'takedowns', 'submissions'];
  const boxO = ease(remap(p, 0.05, 0.24, 0, 1));
  const Chip: React.FC<{ text: string; o: number; hot?: boolean }> = ({ text, o, hot = false }) => (
    <div style={{
      padding: '26px 38px', border: `2px solid ${hot ? ACCENT : HAIR}`, background: CLAUDE.CARD,
      fontFamily: SANS, fontSize: 46, letterSpacing: 1.6, color: hot ? ACCENT : INK,
      opacity: o, transform: `translateY(${(1 - o) * 20}px)`, whiteSpace: 'nowrap',
    }}>{text}</div>
  );
  const Label: React.FC<{ text: string; o: number; hot?: boolean }> = ({ text, o, hot = false }) => (
    <div style={{
      width: 260, textAlign: 'right', fontFamily: SANS, fontSize: 44,
      letterSpacing: 2.4, textTransform: 'uppercase',
      color: hot ? INK : SOFT, fontWeight: hot ? 600 : 400, opacity: o,
    }}>{text}</div>
  );
  const Count: React.FC<{ n: string; o: number; hot?: boolean }> = ({ n, o, hot = false }) => (
    <div style={{
      width: 150, textAlign: 'center', fontFamily: SERIF, fontSize: 190, lineHeight: 1,
      color: hot ? ACCENT : INK, fontWeight: 600, opacity: o,
    }}>{n}</div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      {/* Two rows sized to occupy the full band between the spark line and the
          lesson strip — the one-versus-six gap has to be visible as area, not
          just as a numeral (FILL-THE-CANVAS LAW). */}
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 120, width: SAFE.w, height: 590,
        display: 'flex', flexDirection: 'column', justifyContent: 'space-between',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 44, opacity: boxO }}>
          <Label text="Boxing" o={1} />
          <Chip text="punches, above the belt" o={1} />
          <div style={{ flex: 1, height: 3, background: HAIR }} />
          <Count n="1" o={1} />
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 44 }}>
          <Label text="MMA" hot o={ease(remap(p, 0.26, 0.40, 0, 1))} />
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 20, width: 980 }}>
            {mma.map((w, i) => (
              <Chip key={w} text={w} hot
                o={ease(remap(p, 0.30 + i * 0.065, 0.42 + i * 0.065, 0, 1))} />
            ))}
          </div>
          <div style={{ flex: 1, height: 3, background: HAIR }} />
          <Count n="6" hot o={ease(remap(p, 0.66, 0.78, 0, 1))} />
        </div>
      </div>
      <RecordStrip
        text="In boxing a fighter who goes down is stopped. In MMA the fight has only moved to the floor."
        o={remap(p, 0.80, 0.93, 0, 1)}
      />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — MMA's answer. One organization, one ladder, twelve divisions.
 * ──────────────────────────────────────────────────────────────────────────── */
export const MvbOneOrg: React.FC<{
  spark?: string; champion?: string; note?: string;
}> = ({
  spark = 'One ladder.',
  champion = 'Tom Aspinall',
  note = 'Heavyweight also has an interim champion, Ciryl Gane — a stand-in while the champion is out, not a rival organization.',
}) => {
  const p = useP();
  const orgO = ease(remap(p, 0.04, 0.22, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 62, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 20,
      }}>
        <Eyebrow text="Mixed martial arts" o={remap(p, 0, 0.10, 0, 1)} />
        <div style={{
          padding: '20px 66px', border: `3px solid ${ACCENT}`, background: CLAUDE.CARD,
          fontFamily: SERIF, fontSize: 86, color: ACCENT, fontWeight: 600,
          opacity: orgO, transform: `translateY(${(1 - orgO) * 26}px)`,
        }}>UFC</div>
        <div style={{
          fontFamily: SANS, fontSize: 34, letterSpacing: 4, textTransform: 'uppercase',
          color: SOFT, opacity: orgO,
        }}>one organization</div>
        <div style={{ display: 'flex', gap: 30 }}>
          <Tile value="12" caption="weight divisions" o={ease(remap(p, 0.30, 0.48, 0, 1))} />
          <Tile value="1" caption="champion each" o={ease(remap(p, 0.42, 0.60, 0, 1))} />
        </div>
        <div style={{
          fontFamily: SERIF, fontSize: 54, color: INK,
          opacity: ease(remap(p, 0.58, 0.72, 0, 1)),
        }}>
          Heavyweight: <span style={{ color: ACCENT, fontWeight: 600 }}>{champion}</span>
        </div>
      </div>
      <RecordStrip text={note} o={remap(p, 0.78, 0.92, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — the turn. Boxing has no single league; four bodies award four titles.
 * ──────────────────────────────────────────────────────────────────────────── */
export const MvbFourOrgs: React.FC<{ spark?: string }> = ({ spark = 'Four, not one.' }) => {
  const p = useP();
  const orgs = [
    { abbr: 'WBC', name: 'World Boxing Council' },
    { abbr: 'WBA', name: 'World Boxing Association' },
    { abbr: 'IBF', name: 'International Boxing Federation' },
    { abbr: 'WBO', name: 'World Boxing Organization' },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 118, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 40,
      }}>
        <Eyebrow text="Boxing — no single league" o={remap(p, 0, 0.10, 0, 1)} />
        <div style={{ display: 'flex', gap: 24 }}>
          {orgs.map((o, i) => {
            const t = ease(remap(p, 0.14 + i * 0.12, 0.34 + i * 0.12, 0, 1));
            return (
              <div key={o.abbr} style={{
                width: 396, padding: '34px 22px', background: CLAUDE.CARD,
                border: `2px solid ${ACCENT}`, opacity: t,
                transform: `translateY(${(1 - t) * 26}px)`,
                display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 14,
              }}>
                <div style={{ fontFamily: SERIF, fontSize: 104, lineHeight: 1, color: ACCENT, fontWeight: 600 }}>{o.abbr}</div>
                <div style={{
                  fontFamily: SANS, fontSize: 26, letterSpacing: 1.2, color: SOFT,
                  textAlign: 'center', lineHeight: 1.35,
                }}>{o.name}</div>
              </div>
            );
          })}
        </div>
        <div style={{
          fontFamily: SERIF, fontSize: 62, color: INK, textAlign: 'center', maxWidth: 1480,
          opacity: ease(remap(p, 0.62, 0.76, 0, 1)),
        }}>Each one awards its own world title — so a single weight class can hold four champions at once.</div>
      </div>
      <RecordStrip
        text="Win all four in one division and you are called undisputed."
        o={remap(p, 0.82, 0.94, 0, 1)}
      />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — the proof. Boxing's heavyweight belts, split four ways.
 *
 * Every holder is a prop: these expire, and the reel says so out loud.
 * ──────────────────────────────────────────────────────────────────────────── */
export const MvbSplitBelts: React.FC<{
  spark?: string; asOf?: string; rows?: { belt: string; holder: string; vacant?: boolean }[];
}> = ({
  spark = 'Four belts, three names.',
  asOf = 'as of 3 August 2026',
  rows = [
    { belt: 'WBC', holder: 'Agit Kabayel' },
    { belt: 'WBA', holder: 'Murat Gassiev' },
    { belt: 'WBO', holder: 'Daniel Dubois' },
    { belt: 'IBF', holder: 'vacant', vacant: true },
  ],
}) => {
  const p = useP();
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 66, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 14,
      }}>
        <Eyebrow text={`Boxing heavyweight · ${asOf}`} o={remap(p, 0, 0.10, 0, 1)} />
        <div style={{ width: SAFE.w - 180, marginTop: 6 }}>
          {rows.map((r, i) => {
            const t = ease(remap(p, 0.12 + i * 0.11, 0.30 + i * 0.11, 0, 1));
            return (
              <div key={r.belt} style={{
                display: 'flex', alignItems: 'baseline', gap: 40, padding: '18px 0',
                borderBottom: `2px solid ${HAIR}`, opacity: t,
                transform: `translateY(${(1 - t) * 18}px)`,
              }}>
                <div style={{
                  width: 230, fontFamily: MONO, fontSize: 62, letterSpacing: 3,
                  color: r.vacant ? ACCENT : SOFT,
                }}>{r.belt}</div>
                <div style={{
                  flex: 1, fontFamily: SERIF, fontSize: 76, fontWeight: 600,
                  color: r.vacant ? ACCENT : INK,
                  fontStyle: r.vacant ? 'italic' : 'normal',
                }}>{r.holder}</div>
              </div>
            );
          })}
        </div>
        <div style={{
          fontFamily: SERIF, fontSize: 54, color: INK, marginTop: 10, textAlign: 'center',
          opacity: ease(remap(p, 0.62, 0.76, 0, 1)),
        }}>Four belts. Three champions. One empty seat.</div>
      </div>
      <RecordStrip
        text="The same weight class where MMA has one name."
        o={remap(p, 0.82, 0.94, 0, 1)}
      />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — the payoff. Undisputed is rare: one man's name across all four.
 * ──────────────────────────────────────────────────────────────────────────── */
export const MvbUndisputed: React.FC<{
  spark?: string; name?: string; division?: string;
}> = ({ spark = 'Rare on purpose.', name = 'Naoya Inoue', division = 'super bantamweight' }) => {
  const p = useP();
  const nameO = ease(remap(p, 0.30, 0.50, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 130, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 34,
      }}>
        <Eyebrow text="All four belts, one division" o={remap(p, 0, 0.10, 0, 1)} />
        <div style={{ display: 'flex', gap: 20 }}>
          {['WBC', 'WBA', 'IBF', 'WBO'].map((b, i) => (
            <div key={b} style={{
              padding: '18px 40px', border: `2px solid ${ACCENT}`, background: CLAUDE.CARD,
              fontFamily: MONO, fontSize: 48, letterSpacing: 3, color: ACCENT,
              opacity: ease(remap(p, 0.10 + i * 0.05, 0.24 + i * 0.05, 0, 1)),
            }}>{b}</div>
          ))}
        </div>
        <div style={{
          fontFamily: SERIF, fontSize: 152, lineHeight: 1.05, color: INK, fontWeight: 600,
          opacity: nameO, transform: `translateY(${(1 - nameO) * 30}px)`, textAlign: 'center',
        }}>{name}</div>
        <div style={{
          fontFamily: SANS, fontSize: 38, letterSpacing: 4, textTransform: 'uppercase', color: SOFT,
          opacity: ease(remap(p, 0.46, 0.62, 0, 1)),
        }}>{division}</div>
      </div>
      <RecordStrip
        text="In men's boxing today, exactly one fighter holds all four in his division. In the UFC, that is simply what champion means."
        o={remap(p, 0.74, 0.90, 0, 1)}
      />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the verdict. Three questions the viewer can now answer.
 * ──────────────────────────────────────────────────────────────────────────── */
export const MvbTest: React.FC<{ spark?: string }> = ({ spark = 'Your three questions.' }) => {
  const p = useP();
  const rows = [
    { q: 'What is the floor?', a: 'Cage → MMA · Ring → boxing' },
    { q: 'What is legal?', a: 'Fists only → boxing · Six weapons → MMA' },
    { q: 'How many belts?', a: 'One per division → MMA · Up to four → boxing' },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 66, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 20,
      }}>
        {rows.map((r, i) => {
          const t = ease(remap(p, 0.06 + i * 0.16, 0.28 + i * 0.16, 0, 1));
          return (
            <div key={r.q} style={{
              width: SAFE.w - 140, padding: '22px 44px', background: CLAUDE.CARD,
              border: `2px solid ${i === 0 ? ACCENT : HAIR}`, opacity: t,
              transform: `translateY(${(1 - t) * 24}px)`,
              display: 'flex', flexDirection: 'column', gap: 8,
            }}>
              <div style={{
                fontFamily: SANS, fontSize: 26, letterSpacing: 3.4, textTransform: 'uppercase',
                color: SOFT,
              }}>{`Question ${i + 1}`}</div>
              <div style={{ fontFamily: SERIF, fontSize: 58, color: INK, fontWeight: 600 }}>{r.q}</div>
              <div style={{ fontFamily: SANS, fontSize: 36, color: SOFT }}>{r.a}</div>
            </div>
          );
        })}
      </div>
      <RecordStrip
        text="The names on the belts change every few months. The structure does not."
        o={remap(p, 0.78, 0.92, 0, 1)}
      />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Same poster-scale card as the football reel: title restate,
 * terracotta period, host name beneath. See WorldCup2026.tsx for why the
 * shipped ClaudeTitleOutro is not used (it fails FILL-THE-CANVAS at this size).
 * ──────────────────────────────────────────────────────────────────────────── */
export const MvbOutro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = 'Cage, Rules, Belts.', handle = 'Param Madan', subline = 'MMA vs Boxing' }) => {
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
        fontFamily: SERIF, fontSize: 196, lineHeight: 1.02, fontWeight: 600, color: INK,
        maxWidth: SAFE.w, textAlign: 'center',
        opacity: rise, transform: `translateY(${(1 - rise) * 40}px)`,
      }}>
        {stem}{hasDot && <span style={{ color: ACCENT }}>.</span>}
      </div>
      <div style={{
        fontFamily: SERIF, fontSize: 86, color: INK, opacity: nameO,
        transform: `translateY(${(1 - ease(nameO)) * 22}px)`,
      }}>{handle}</div>
      <div style={{
        fontFamily: SANS, fontSize: 40, letterSpacing: 5, textTransform: 'uppercase',
        color: SOFT, opacity: subO,
      }}>{subline}</div>
    </AbsoluteFill>
  );
};
