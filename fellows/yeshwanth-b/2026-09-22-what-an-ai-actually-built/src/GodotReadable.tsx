/**
 * GodotReadable.tsx — reel-local components for claude-liam-godot
 * ("Godot, Readable." — why Godot is the right engine for AI-assisted building).
 *
 * Two beats in that reel had no library hit (GATE L searched: "tree of nodes",
 * "binary vs text diff"), so they are built here as new components rather than
 * slated:
 *
 *   GodotNodeTree      B03 — the scene tree + the GDScript attached to its root.
 *                      The node TYPE is the behaviour, so the type is the label.
 *   GodotTextVsBinary  B05 — the same edit attempted against an opaque binary
 *                      scene and against a .tscn, side by side.
 *
 * House rules honoured: cream stage via IlluStage, one terracotta moment per
 * beat (the `extends` line in B03; the added diff line in B05), everything
 * inside SAFE, motion is a pure function of useP().
 */
import React from 'react';
import { z } from 'zod';
import { IlluStage, useP, remap, ease, SERIF, SANS, MONO } from './illustrations/kit';
import { CLAUDE } from './tokens/claude';
import { SAFE, SAFE916 } from './tokens/layout';

const reveal = (p: number, at: number, span = 0.08) => ease(remap(p, at, at + span, 0, 1));

// ── GodotNodeTree ───────────────────────────────────────────────────────────

export const godotNodeTreeSchema = z.object({
  sparkLine: z.string().default('The type is the behaviour.'),
  rootLabel: z.string().default('Player'),
  rootType: z.string().default('CharacterBody2D'),
  children: z.array(z.object({
    label: z.string(),
    note: z.string().optional(),
  })).default([]),
  scriptName: z.string().default('player.gd'),
  scriptLines: z.array(z.string()).default([]),
});
export type GodotNodeTreeProps = z.infer<typeof godotNodeTreeSchema>;

const TREE_X = 130;
const TREE_W = 700;
const ROOT_Y = 230;
const ROOT_H = 132;
const CHILD_X = TREE_X + 86;
const CHILD_W = TREE_W - 86;
const CHILD_H = 118;
const CHILD_GAP = 34;
const CHILD_Y0 = ROOT_Y + ROOT_H + 74;

export const GodotNodeTree: React.FC<GodotNodeTreeProps> = ({
  sparkLine, rootLabel, rootType, children, scriptName, scriptLines,
}) => {
  const p = useP();
  const rootIn = reveal(p, 0.06, 0.1);
  // The script card lands at a third in, not two-thirds: the narration reaches
  // GDScript late, but leaving the right half of SAFE empty until then is an
  // underfill defect (GATE V, first pass). It arrives quiet and the terracotta
  // `extends` line still lands on the spoken word.
  const cardIn = reveal(p, 0.3, 0.1);
  // The one terracotta moment: the line that binds script to node type.
  const extendsIn = reveal(p, 0.72, 0.08);

  const childY = (i: number) => CHILD_Y0 + i * (CHILD_H + CHILD_GAP);
  const lastY = childY(Math.max(0, children.length - 1)) + CHILD_H / 2;

  return (
    <IlluStage spark={sparkLine}>
      {/* ── the scene tree ── */}
      <div style={{
        position: 'absolute', left: TREE_X, top: ROOT_Y - 66, width: TREE_W,
        fontFamily: SANS, fontSize: 26, letterSpacing: 1.6, color: CLAUDE.INK_SOFT,
        opacity: reveal(p, 0.02, 0.08),
      }}>
        SCENE — player.tscn
      </div>

      {/* trunk: drawn top-down as the children land */}
      <div style={{
        position: 'absolute', left: TREE_X + 40, top: ROOT_Y + ROOT_H,
        width: 3, background: CLAUDE.BORDER,
        height: (lastY - (ROOT_Y + ROOT_H)) * reveal(p, 0.2, 0.28),
      }} />

      {/* root node — the type IS the behaviour, so the type is set large */}
      <div style={{
        position: 'absolute', left: TREE_X, top: ROOT_Y, width: TREE_W, height: ROOT_H,
        background: CLAUDE.CARD, border: `3px solid ${CLAUDE.INK}`, borderRadius: 12,
        display: 'flex', flexDirection: 'column', justifyContent: 'center', paddingLeft: 30,
        opacity: rootIn, transform: `translateY(${(1 - rootIn) * 18}px)`,
      }}>
        <div style={{ fontFamily: SERIF, fontSize: 44, color: CLAUDE.INK, lineHeight: 1.1 }}>
          {rootLabel}
        </div>
        <div style={{ fontFamily: MONO, fontSize: 30, color: CLAUDE.INK_SOFT, marginTop: 6 }}>
          {rootType}
        </div>
      </div>

      {/* children */}
      {children.map((c, i) => {
        const o = reveal(p, 0.24 + i * 0.1, 0.09);
        const y = childY(i);
        return (
          <React.Fragment key={c.label}>
            <div style={{
              position: 'absolute', left: TREE_X + 40, top: y + CHILD_H / 2,
              height: 3, width: (CHILD_X - TREE_X - 40) * o, background: CLAUDE.BORDER,
            }} />
            <div style={{
              position: 'absolute', left: CHILD_X, top: y, width: CHILD_W, height: CHILD_H,
              background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 10,
              display: 'flex', flexDirection: 'column', justifyContent: 'center', paddingLeft: 26,
              opacity: o, transform: `translateX(${(1 - o) * 24}px)`,
            }}>
              <div style={{ fontFamily: MONO, fontSize: 32, color: CLAUDE.INK }}>{c.label}</div>
              {c.note ? (
                <div style={{ fontFamily: SANS, fontSize: 25, color: CLAUDE.INK_SOFT, marginTop: 4 }}>
                  {c.note}
                </div>
              ) : null}
            </div>
          </React.Fragment>
        );
      })}

      {/* ── the attached script ── */}
      <div style={{
        position: 'absolute', left: 980, top: 196, width: 810,
        opacity: cardIn, transform: `translateY(${(1 - cardIn) * 20}px)`,
      }}>
        <div style={{
          display: 'inline-block', background: CLAUDE.PILL, borderRadius: '10px 10px 0 0',
          padding: '10px 24px', fontFamily: MONO, fontSize: 27, color: CLAUDE.INK_SOFT,
        }}>
          {scriptName}
        </div>
        <div style={{
          background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: '0 12px 12px 12px',
          padding: '30px 34px', minHeight: 470,
        }}>
          {scriptLines.map((line, i) => {
            const isExtends = line.startsWith('extends');
            return (
              <div key={i} style={{
                fontFamily: MONO, fontSize: 29, lineHeight: '46px',
                whiteSpace: 'pre', color: isExtends ? CLAUDE.SPARK : CLAUDE.INK,
                opacity: isExtends ? extendsIn : reveal(p, 0.34 + i * 0.012, 0.06),
              }}>
                {line || ' '}
              </div>
            );
          })}
        </div>
      </div>
    </IlluStage>
  );
};

// ── GodotFreeChips ──────────────────────────────────────────────────────────
// ClaudeScienceChipGrid was the GATE L hit for B02, but its geometry is baked
// at 1280×720; inside a 1920×1080 composition it renders small and top-left and
// GATE V fails it for underfill (12% of SAFE). Rather than retune a component
// four other reels depend on, B02 gets this one, laid out natively at 1920×1080
// per FILL-THE-CANVAS LAW.

export const godotFreeChipsSchema = z.object({
  sparkLine: z.string().default('Free is not a tier.'),
  items: z.array(z.object({
    label: z.string(),
    accent: z.boolean().optional(),
  })).default([]),
  caption: z.string().optional(),
});
export type GodotFreeChipsProps = z.infer<typeof godotFreeChipsSchema>;

const CHIP_W = 830;
const CHIP_H = 296;
const CHIP_GAP_X = 56;
const CHIP_GAP_Y = 56;
const GRID_X = (1920 - (CHIP_W * 2 + CHIP_GAP_X)) / 2;
const GRID_Y = 200;

export const GodotFreeChips: React.FC<GodotFreeChipsProps> = ({ sparkLine, items, caption }) => {
  const p = useP();
  return (
    <IlluStage spark={sparkLine}>
      {items.slice(0, 4).map((it, i) => {
        const o = reveal(p, 0.12 + i * 0.16, 0.1);
        const col = i % 2;
        const row = Math.floor(i / 2);
        return (
          <div key={it.label} style={{
            position: 'absolute',
            left: GRID_X + col * (CHIP_W + CHIP_GAP_X),
            top: GRID_Y + row * (CHIP_H + CHIP_GAP_Y),
            width: CHIP_W, height: CHIP_H,
            background: CLAUDE.CARD,
            border: `${it.accent ? 3 : 2}px solid ${it.accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            borderRadius: 16,
            display: 'flex', alignItems: 'center', gap: 26, padding: '0 44px',
            opacity: o, transform: `translateY(${(1 - o) * 22}px)`,
          }}>
            <div style={{
              width: 22, height: 22, borderRadius: '50%', flexShrink: 0,
              background: it.accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
            }} />
            <div style={{
              fontFamily: SANS, fontSize: 50, fontWeight: 600, lineHeight: 1.15,
              color: it.accent ? CLAUDE.SPARK : CLAUDE.INK,
              maxWidth: CHIP_W - 130,
            }}>
              {it.label}
            </div>
          </div>
        );
      })}
      {caption ? (
        <div style={{
          position: 'absolute', left: GRID_X, top: GRID_Y + 2 * CHIP_H + CHIP_GAP_Y + 44,
          width: CHIP_W * 2 + CHIP_GAP_X, textAlign: 'center',
          fontFamily: SERIF, fontSize: 38, fontStyle: 'italic', color: CLAUDE.INK_SOFT,
          opacity: reveal(p, 0.76, 0.1),
        }}>
          {caption}
        </div>
      ) : null}
    </IlluStage>
  );
};

// ── GodotTextVsBinary ───────────────────────────────────────────────────────

export const godotTextVsBinarySchema = z.object({
  sparkLine: z.string().default('A diff you can read.'),
  leftTitle: z.string().default('Unity · scene (binary)'),
  leftNote: z.string().default('GUID references — breaks silently'),
  rightTitle: z.string().default('Godot · player.tscn (text)'),
  rightNote: z.string().default('Every change is a reviewable diff'),
  diffLines: z.array(z.object({
    kind: z.enum(['context', 'add', 'remove']),
    text: z.string(),
  })).default([]),
});
export type GodotTextVsBinaryProps = z.infer<typeof godotTextVsBinarySchema>;

const PANEL_Y = 194;
const PANEL_H = 660;
const PANEL_W = 800;
const LEFT_X = SAFE.x + 24;         // 120
const RIGHT_X = SAFE.r - PANEL_W - 24; // 1000

/** Deterministic pseudo-hex so the binary panel is unreadable but stable. */
const hexRow = (row: number, cols: number) => {
  let s = '';
  let v = (row + 7) * 2654435761 % 4294967296;
  for (let i = 0; i < cols; i++) {
    v = (v * 1664525 + 1013904223) % 4294967296;
    s += ((v >> 8) & 0xff).toString(16).padStart(2, '0') + ' ';
  }
  return s.trim();
};

export const GodotTextVsBinary: React.FC<GodotTextVsBinaryProps> = ({
  sparkLine, leftTitle, leftNote, rightTitle, rightNote, diffLines,
}) => {
  const p = useP();
  const panelsIn = reveal(p, 0.04, 0.1);
  const breakIn = reveal(p, 0.54, 0.08);
  const stampIn = reveal(p, 0.84, 0.08);

  const panelBase: React.CSSProperties = {
    position: 'absolute', top: PANEL_Y, width: PANEL_W, height: PANEL_H,
    background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 14,
    padding: '26px 30px', opacity: panelsIn,
  };
  const titleStyle: React.CSSProperties = {
    fontFamily: SANS, fontSize: 30, color: CLAUDE.INK, marginBottom: 20,
    maxWidth: PANEL_W - 60, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap',
  };
  const noteStyle = (o: number): React.CSSProperties => ({
    position: 'absolute', top: PANEL_Y + PANEL_H + 26, width: PANEL_W,
    fontFamily: SANS, fontSize: 27, color: CLAUDE.INK_SOFT, opacity: o,
    maxWidth: PANEL_W, overflow: 'hidden',
  });

  return (
    <IlluStage spark={sparkLine} sparkPos="top">
      {/* ── left: the opaque binary ── */}
      <div style={{ ...panelBase, left: LEFT_X }}>
        <div style={titleStyle}>{leftTitle}</div>
        {Array.from({ length: 9 }).map((_, i) => (
          <div key={i} style={{
            fontFamily: MONO, fontSize: 25, lineHeight: '40px', color: CLAUDE.GHOST,
            whiteSpace: 'pre', opacity: reveal(p, 0.18 + i * 0.014, 0.06),
          }}>
            {hexRow(i, 16)}
          </div>
        ))}
        <div style={{
          marginTop: 22, fontFamily: MONO, fontSize: 25, color: CLAUDE.INK_SOFT,
          opacity: reveal(p, 0.34, 0.08),
        }}>
          guid: 9f2c1ab74e0d…
        </div>
        {/* the edit lands and nothing legible changes */}
        <div style={{
          position: 'absolute', left: 30, right: 30, top: PANEL_H - 118,
          border: `2px dashed ${CLAUDE.INK_SOFT}`, borderRadius: 10, padding: '14px 18px',
          fontFamily: SANS, fontSize: 26, color: CLAUDE.INK_SOFT, opacity: breakIn,
        }}>
          edit applied → reference broken, no visible change
        </div>
      </div>
      <div style={{ ...noteStyle(panelsIn), left: LEFT_X }}>{leftNote}</div>

      {/* ── right: the readable diff ── */}
      <div style={{ ...panelBase, left: RIGHT_X }}>
        <div style={titleStyle}>{rightTitle}</div>
        {diffLines.map((d, i) => {
          const isAdd = d.kind === 'add';
          const isRemove = d.kind === 'remove';
          // context lines settle early; the changed pair lands on the spoken edit
          const o = isAdd || isRemove
            ? reveal(p, 0.56 + (isAdd ? 0.08 : 0), 0.08)
            : reveal(p, 0.28 + i * 0.03, 0.07);
          const color = isAdd ? CLAUDE.SPARK : isRemove ? CLAUDE.GHOST : CLAUDE.INK;
          return (
            <div key={i} style={{
              display: 'flex', gap: 16, alignItems: 'baseline', opacity: o,
              background: isAdd ? '#FBEFE9' : 'transparent', borderRadius: 8,
              padding: isAdd ? '6px 10px' : '6px 10px', marginLeft: isAdd ? -10 : -10,
            }}>
              <div style={{ fontFamily: MONO, fontSize: 27, color, width: 22 }}>
                {isAdd ? '+' : isRemove ? '−' : ' '}
              </div>
              <div style={{
                fontFamily: MONO, fontSize: 26, lineHeight: '40px', color,
                textDecoration: isRemove ? 'line-through' : 'none',
                maxWidth: PANEL_W - 110, overflow: 'hidden', textOverflow: 'ellipsis',
                whiteSpace: 'nowrap',
              }}>
                {d.text}
              </div>
            </div>
          );
        })}
        <div style={{
          position: 'absolute', left: 30, top: PANEL_H - 118,
          border: `2px solid ${CLAUDE.INK}`, borderRadius: 10, padding: '14px 22px',
          fontFamily: SANS, fontSize: 26, color: CLAUDE.INK, opacity: stampIn,
        }}>
          reviewable — line by line
        </div>
      </div>
      <div style={{ ...noteStyle(panelsIn), left: RIGHT_X }}>{rightNote}</div>
    </IlluStage>
  );
};

// ── GodotTitleOutro ─────────────────────────────────────────────────────────
// OUTRO-LOCK.md scopes the @NikBearBrown card to claude-liam reels ONLY and
// says other channels "have their OWN outros and NEVER get this card, handle,
// or mascot." This reel is @HumanitariansAI, so it gets its own card rather
// than a modified copy of the locked one — the handle is a prop here because
// the lock's reason for hardcoding (one channel, one handle) does not apply.

export const godotTitleOutroSchema = z.object({
  title: z.string().default('What is Godot?'),
  handle: z.string().default('@HumanitariansAI'),
  kicker: z.string().default(''),
  subline: z.string().default(''),
});
export type GodotTitleOutroProps = z.infer<typeof godotTitleOutroSchema>;

/** Title with its final punctuation mark set in terracotta. */
const TitleWithAccent: React.FC<{ text: string; size: number }> = ({ text, size }) => {
  const m = text.match(/^(.*?)([.?!]?)$/);
  const body = m ? m[1] : text;
  const mark = m ? m[2] : '';
  return (
    <span style={{ fontFamily: SERIF, fontSize: size, color: CLAUDE.INK, lineHeight: 1.08 }}>
      {body}
      {mark ? <span style={{ color: CLAUDE.SPARK }}>{mark}</span> : null}
    </span>
  );
};

const OutroCard: React.FC<GodotTitleOutroProps & { portrait?: boolean }> = ({
  title, handle, kicker, subline, portrait,
}) => {
  const p = useP();
  // Laid out at fixed fractions of SAFE rather than flex-centred, so the ink
  // bounding box spans the frame deliberately. final_frame_check measures
  // bbox/SAFE (needs >=55%) AND each axis (>=50%); a centred stack of small
  // type fails both, which is what blocked the first master.
  const S = portrait ? SAFE916 : SAFE;
  // The band layout places handle and subline at fixed rows, so it assumes a
  // SINGLE-LINE title. "It Passed Every Test." at the flat 240 wrapped to two
  // lines and pushed the handle and subline off the card entirely — the fill
  // metric read that as underfill, but the real defect was a missing handle.
  // Size down by title length so one line always fits inside SAFE.
  const titleBase = portrait ? 140 : 240;
  const titleFit = (S.w * 0.94) / Math.max(1, title.length * 0.44);
  const titleSize = Math.min(titleBase, titleFit);
  const kickSize  = portrait ? 64 : 70;
  const handleSize = portrait ? 76 : 78;
  const subSize   = portrait ? 60 : 64;
  const row = (f: number) => S.y + S.h * f;

  const band: React.CSSProperties = {
    position: 'absolute', left: S.x, width: S.w, textAlign: 'center',
  };

  return (
    <IlluStage spark="" sparkPos="top">
      <div style={{
        ...band, top: row(0.08), fontFamily: SANS, fontSize: kickSize,
        color: CLAUDE.INK_SOFT, lineHeight: 1.3,
        opacity: reveal(p, 0.02, 0.06),
        transform: `translateY(${(1 - reveal(p, 0.02, 0.06)) * 14}px)`,
      }}>
        {kicker}
      </div>

      <div style={{
        ...band, top: row(portrait ? 0.3 : 0.28),
        opacity: reveal(p, 0.1, 0.08),
        transform: `translateY(${(1 - reveal(p, 0.1, 0.08)) * 16}px)`,
      }}>
        <TitleWithAccent text={title} size={titleSize} />
      </div>

      <div style={{
        ...band, top: row(portrait ? 0.54 : 0.56), fontFamily: SANS,
        fontSize: handleSize, color: CLAUDE.INK, letterSpacing: 0.5,
        opacity: reveal(p, 0.2, 0.08),
      }}>
        {handle}
      </div>

      <div style={{
        ...band, top: row(portrait ? 0.80 : 0.80), fontFamily: SERIF,
        fontSize: subSize, fontStyle: 'italic', color: CLAUDE.INK_SOFT,
        lineHeight: 1.45,
        opacity: reveal(p, 0.28, 0.08),
      }}>
        {subline}
      </div>
    </IlluStage>
  );
};

export const GodotTitleOutro: React.FC<GodotTitleOutroProps> = (props) => <OutroCard {...props} />;
export const GodotTitleOutro916: React.FC<GodotTitleOutroProps> = (props) => <OutroCard {...props} portrait />;

/** Portrait spark line. IlluStage puts its own at y=44, which is above
 *  SAFE916.y (96) — legal in 16:9 (SAFE.y 54) but a title-safe BLOCKER in
 *  portrait. The 916 components below pass spark="" and use this instead. */
const PortraitSpark: React.FC<{ text: string }> = ({ text }) => {
  const p = useP();
  return (
    <div style={{
      position: 'absolute', top: SAFE916.y + 26, left: SAFE916.x, width: SAFE916.w,
      textAlign: 'center', fontFamily: SERIF, fontSize: 44, color: CLAUDE.INK,
      opacity: remap(p, 0, 0.06, 0, 1),
    }}>
      {text}
    </div>
  );
};

// ── Portrait 9:16 variants ──────────────────────────────────────────────────
// `./art vertical` rewires each beat to <pattern>916 when one is registered,
// so these are what make the vertical cut portrait-NATIVE instead of a crop.
// Same zod schema as their landscape twins (shorts.py standing rule #4) —
// only the layout changes: side-by-side becomes stacked.

const P_X = SAFE916.x + 20;     // 74
const P_W = SAFE916.w - 40;     // 932

export const GodotFreeChips916: React.FC<GodotFreeChipsProps> = ({ sparkLine, items, caption }) => {
  const p = useP();
  const H = 300;
  const GAP = 40;
  const top = 330;
  return (
    <IlluStage spark="">
      <PortraitSpark text={sparkLine} />
      {items.slice(0, 4).map((it, i) => {
        const o = reveal(p, 0.12 + i * 0.16, 0.1);
        return (
          <div key={it.label} style={{
            position: 'absolute', left: P_X, top: top + i * (H + GAP), width: P_W, height: H,
            background: CLAUDE.CARD,
            border: `${it.accent ? 3 : 2}px solid ${it.accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            borderRadius: 18, display: 'flex', alignItems: 'center', gap: 28, padding: '0 46px',
            opacity: o, transform: `translateY(${(1 - o) * 24}px)`,
          }}>
            <div style={{
              width: 24, height: 24, borderRadius: '50%', flexShrink: 0,
              background: it.accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
            }} />
            <div style={{
              fontFamily: SANS, fontSize: 54, fontWeight: 600, lineHeight: 1.18,
              color: it.accent ? CLAUDE.SPARK : CLAUDE.INK, maxWidth: P_W - 130,
            }}>
              {it.label}
            </div>
          </div>
        );
      })}
      {caption ? (
        <div style={{
          position: 'absolute', left: P_X, top: top + 4 * (H + GAP) + 26, width: P_W,
          textAlign: 'center', fontFamily: SERIF, fontSize: 40, fontStyle: 'italic',
          color: CLAUDE.INK_SOFT, opacity: reveal(p, 0.76, 0.1),
        }}>
          {caption}
        </div>
      ) : null}
    </IlluStage>
  );
};

export const GodotNodeTree916: React.FC<GodotNodeTreeProps> = ({
  sparkLine, rootLabel, rootType, children, scriptName, scriptLines,
}) => {
  const p = useP();
  const rootIn = reveal(p, 0.06, 0.1);
  const cardIn = reveal(p, 0.3, 0.1);
  const extendsIn = reveal(p, 0.72, 0.08);

  const ROOT_Y = 250;
  const ROOT_H = 156;
  const CH_H = 138;
  const CH_GAP = 30;
  const CH_X = P_X + 70;
  const CH_Y0 = ROOT_Y + ROOT_H + 70;
  const childY = (i: number) => CH_Y0 + i * (CH_H + CH_GAP);
  const lastY = childY(Math.max(0, children.length - 1)) + CH_H / 2;

  return (
    <IlluStage spark="">
      <PortraitSpark text={sparkLine} />
      <div style={{
        position: 'absolute', left: P_X, top: ROOT_Y - 62, width: P_W,
        fontFamily: SANS, fontSize: 30, letterSpacing: 1.8, color: CLAUDE.INK_SOFT,
        opacity: reveal(p, 0.02, 0.08),
      }}>
        SCENE — player.tscn
      </div>

      <div style={{
        position: 'absolute', left: P_X + 34, top: ROOT_Y + ROOT_H, width: 3,
        background: CLAUDE.BORDER, height: (lastY - (ROOT_Y + ROOT_H)) * reveal(p, 0.2, 0.28),
      }} />

      <div style={{
        position: 'absolute', left: P_X, top: ROOT_Y, width: P_W, height: ROOT_H,
        background: CLAUDE.CARD, border: `3px solid ${CLAUDE.INK}`, borderRadius: 14,
        display: 'flex', flexDirection: 'column', justifyContent: 'center', paddingLeft: 34,
        opacity: rootIn, transform: `translateY(${(1 - rootIn) * 18}px)`,
      }}>
        <div style={{ fontFamily: SERIF, fontSize: 54, color: CLAUDE.INK, lineHeight: 1.1 }}>{rootLabel}</div>
        <div style={{ fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT, marginTop: 8 }}>{rootType}</div>
      </div>

      {children.map((c, i) => {
        const o = reveal(p, 0.24 + i * 0.1, 0.09);
        const y = childY(i);
        return (
          <React.Fragment key={c.label}>
            <div style={{
              position: 'absolute', left: P_X + 34, top: y + CH_H / 2, height: 3,
              width: (CH_X - P_X - 34) * o, background: CLAUDE.BORDER,
            }} />
            <div style={{
              position: 'absolute', left: CH_X, top: y, width: P_W - 70, height: CH_H,
              background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 12,
              display: 'flex', flexDirection: 'column', justifyContent: 'center', paddingLeft: 30,
              opacity: o, transform: `translateX(${(1 - o) * 20}px)`,
            }}>
              <div style={{ fontFamily: MONO, fontSize: 36, color: CLAUDE.INK }}>{c.label}</div>
              {c.note ? (
                <div style={{ fontFamily: SANS, fontSize: 29, color: CLAUDE.INK_SOFT, marginTop: 6 }}>{c.note}</div>
              ) : null}
            </div>
          </React.Fragment>
        );
      })}

      <div style={{
        position: 'absolute', left: P_X, top: lastY + 130, width: P_W,
        opacity: cardIn, transform: `translateY(${(1 - cardIn) * 20}px)`,
      }}>
        <div style={{
          display: 'inline-block', background: CLAUDE.PILL, borderRadius: '12px 12px 0 0',
          padding: '12px 28px', fontFamily: MONO, fontSize: 30, color: CLAUDE.INK_SOFT,
        }}>
          {scriptName}
        </div>
        <div style={{
          background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`,
          borderRadius: '0 14px 14px 14px', padding: '30px 34px', minHeight: 300,
        }}>
          {scriptLines.map((line, i) => {
            const isExtends = line.startsWith('extends');
            return (
              <div key={i} style={{
                fontFamily: MONO, fontSize: 31, lineHeight: '48px', whiteSpace: 'pre',
                color: isExtends ? CLAUDE.SPARK : CLAUDE.INK,
                opacity: isExtends ? extendsIn : reveal(p, 0.34 + i * 0.012, 0.06),
              }}>
                {line || ' '}
              </div>
            );
          })}
        </div>
      </div>
    </IlluStage>
  );
};

export const GodotTextVsBinary916: React.FC<GodotTextVsBinaryProps> = ({
  sparkLine, leftTitle, leftNote, rightTitle, rightNote, diffLines,
}) => {
  const p = useP();
  const panelsIn = reveal(p, 0.04, 0.1);
  const breakIn = reveal(p, 0.54, 0.08);
  const stampIn = reveal(p, 0.84, 0.08);

  const PH = 620;
  const TOP_Y = 250;
  const BOT_Y = TOP_Y + PH + 150;

  const panel = (top: number): React.CSSProperties => ({
    position: 'absolute', left: P_X, top, width: P_W, height: PH,
    background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 16,
    padding: '28px 32px', opacity: panelsIn,
  });
  const title: React.CSSProperties = {
    fontFamily: SANS, fontSize: 34, color: CLAUDE.INK, marginBottom: 22,
    maxWidth: P_W - 64, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap',
  };
  const note = (top: number): React.CSSProperties => ({
    position: 'absolute', left: P_X, top, width: P_W,
    fontFamily: SANS, fontSize: 30, color: CLAUDE.INK_SOFT, opacity: panelsIn,
  });

  return (
    <IlluStage spark="">
      <PortraitSpark text={sparkLine} />
      <div style={panel(TOP_Y)}>
        <div style={title}>{leftTitle}</div>
        {Array.from({ length: 7 }).map((_, i) => (
          <div key={i} style={{
            fontFamily: MONO, fontSize: 26, lineHeight: '42px', color: CLAUDE.GHOST,
            whiteSpace: 'pre', opacity: reveal(p, 0.18 + i * 0.014, 0.06),
          }}>
            {hexRow(i, 13)}
          </div>
        ))}
        <div style={{
          position: 'absolute', left: 32, right: 32, top: PH - 116,
          border: `2px dashed ${CLAUDE.INK_SOFT}`, borderRadius: 12, padding: '16px 20px',
          fontFamily: SANS, fontSize: 28, color: CLAUDE.INK_SOFT, opacity: breakIn,
        }}>
          something changed — you can't see what
        </div>
      </div>
      <div style={note(TOP_Y + PH + 24)}>{leftNote}</div>

      <div style={panel(BOT_Y)}>
        <div style={title}>{rightTitle}</div>
        {diffLines.map((d, i) => {
          const isAdd = d.kind === 'add';
          const isRemove = d.kind === 'remove';
          const o = isAdd || isRemove
            ? reveal(p, 0.56 + (isAdd ? 0.08 : 0), 0.08)
            : reveal(p, 0.28 + i * 0.03, 0.07);
          const color = isAdd ? CLAUDE.SPARK : isRemove ? CLAUDE.GHOST : CLAUDE.INK;
          return (
            <div key={i} style={{
              display: 'flex', gap: 16, alignItems: 'baseline', opacity: o,
              background: isAdd ? '#FBEFE9' : 'transparent', borderRadius: 8,
              padding: '8px 10px', marginLeft: -10,
            }}>
              <div style={{ fontFamily: MONO, fontSize: 30, color, width: 24 }}>
                {isAdd ? '+' : isRemove ? '−' : ' '}
              </div>
              <div style={{
                fontFamily: MONO, fontSize: 29, lineHeight: '46px', color,
                textDecoration: isRemove ? 'line-through' : 'none',
                maxWidth: P_W - 120, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap',
              }}>
                {d.text}
              </div>
            </div>
          );
        })}
        <div style={{
          position: 'absolute', left: 32, top: PH - 116,
          border: `2px solid ${CLAUDE.INK}`, borderRadius: 12, padding: '16px 24px',
          fontFamily: SANS, fontSize: 28, color: CLAUDE.INK, opacity: stampIn,
        }}>
          you see exactly what changed
        </div>
      </div>
      <div style={note(BOT_Y + PH + 24)}>{rightNote}</div>
    </IlluStage>
  );
};
