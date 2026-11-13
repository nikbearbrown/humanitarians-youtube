import React from 'react';
import { AbsoluteFill, Img, staticFile, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE,
} from '../lib/cueKit';

/**
 * HaiDocPages — B01 of "Writing the Lyrical Literacy Fellows Handbook." (HAI weekly progress)
 *
 * A fellow's written deliverable, shown as itself. Each `pages` entry is a CROP of the
 * real document (rendered from its PDF at 300 dpi), cut tight enough that its body type
 * stays above the GATE T floor when shown — a whole page at video size would be
 * unreadable. The crop is laid on a sheet with two blank sheets behind it (the document's
 * thickness, with no unreadable thumbnails), and each new crop slides in on its cue word.
 * The right column carries the document's own facts as designed type: page count,
 * sections, version, and who drafted and who reviewed it.
 *
 * cues: one per page (`pages[i].cue`), plus `drafted` / `reviewed` for the credit line.
 * Portrait: the sheet runs full width and the crop is shown 2.2× larger, panning slowly
 * with the crop's LEFT edge pinned (no pan: a pan clipped the start of each line), so a wide
 * crop stays readable at the phone type floor and every line starts in view.
 */

export const haiDocPagesSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · WEEKLY PROGRESS'),
  title: z.string().default('The Document'),
  pages: z.array(z.object({ src: z.string(), label: z.string(), cue: z.string() })).default([]),
  stats: z.array(z.object({ value: z.string(), label: z.string() })).default([]),
  credit: z.string().default(''),
  sparkLine: z.string().default(''),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type HaiDocPagesProps = z.infer<typeof haiDocPagesSchema>;

export const HaiDocPages: React.FC<HaiDocPagesProps> = ({ eyebrow, title, pages, stats, credit, sparkLine, cues }) => {
  const { frame, width, height, at, sp, F } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const starts = pages.map((p, i) => at(p.cue, (i / Math.max(1, pages.length)) * 0.9));
  let cur = 0;
  starts.forEach((s, i) => { if (frame >= F(s)) cur = i; });
  const sIn = (i: number) => sp(starts[i] ?? 0);
  const tDrafted = at('drafted', 0.18), tReviewed = at('reviewed', 0.38);
  const lastStart = starts[starts.length - 1] ?? 0.9;

  const headIn = sp(0);
  const sStats = sp(Math.min(0.12, (starts[1] ?? 0.05)));
  const sCredit = sp(tDrafted);
  const sRev = sp(tReviewed);
  const sparkIn = sp(clamp(lastStart + 0.02, 0, 0.97));

  // sheet geometry
  const SX = PAD_X;
  const SY = portrait ? height * 0.215 : height * 0.27;
  // portrait: narrower by the two-sheet stack offset, so the back sheets end inside the title-safe edge
  const SW = portrait ? CW - 28 * U : CW * 0.6;
  const SH = portrait ? height * 0.42 : height * 0.56;
  const INNER = 34 * U;
  const lbl = portrait ? T.label * 0.85 : 22 * U;

  const crop = (i: number) => {
    const p = pages[i];
    if (!p) return null;
    const k = op(sIn(i));
    const next = op(sIn(i + 1));
    // portrait: show larger and pan across the crop while it is current
    const zoom = portrait ? 2.2 : 1;
    const segEnd = starts[i + 1] ?? 1;
    const pan = portrait ? interpolate(frame, [F(starts[i] ?? 0), F(segEnd)], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }) : 0;
    const imgW = (SW - INNER * 2) * zoom;
    return (
      <div key={i} style={{
        position: 'absolute', left: SX, top: SY, width: SW, height: SH,
        background: CLAUDE.CARD, borderRadius: 14 * U, border: `1px solid ${CLAUDE.BORDER}`,
        boxShadow: '0 18px 40px rgba(61,57,41,0.12)', overflow: 'hidden',
        opacity: k * (1 - (i < pages.length - 1 ? next : 0)),
        transform: `translateY(${(1 - k) * 40 * U}px) rotate(${(1 - k) * -1.5}deg)`,
      }}>
        <div style={{ position: 'absolute', left: INNER - pan * 0 * (imgW - (SW - INNER * 2)), top: INNER, width: imgW }}>
          <Img src={staticFile(p.src)} style={{ width: imgW, display: 'block' }} />
        </div>
      </div>
    );
  };

  const statBlock = (s: { value: string; label: string }, i: number) => (
    <div key={i} style={{ opacity: op(sStats), transform: `translateY(${(1 - op(sStats)) * (14 + i * 6)}px)`,
      marginBottom: portrait ? 0 : 26 * U, flex: portrait ? 1 : undefined }}>
      <div style={{ fontFamily: HAI_TYPE.serif, fontSize: portrait ? T.title * 1.05 : 70 * U, fontWeight: 700, color: CLAUDE.INK, lineHeight: 1 }}>{s.value}</div>
      <div style={{ fontFamily: HAI_TYPE.sans, fontSize: portrait ? T.label * 0.7 : 20 * U, fontWeight: 700, letterSpacing: 1.2, color: CLAUDE.INK_SOFT, marginTop: 6 * U }}>{s.label}</div>
    </div>
  );

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={portrait ? '' : eyebrow} title={title} inOp={headIn}
        padX={PAD_X} height={height} width={width} portrait={portrait}
        titleSize={portrait ? T.title : undefined} />

      {/* the document's thickness: two blank sheets behind the current crop */}
      {[2, 1].map((d) => (
        <div key={d} style={{
          position: 'absolute', left: SX + d * 14 * U, top: SY + d * 14 * U, width: SW, height: SH,
          background: CLAUDE.CARD, borderRadius: 14 * U, border: `1px solid ${CLAUDE.BORDER}`, opacity: op(headIn) * 0.9,
        }} />
      ))}
      {pages.map((_, i) => crop(i))}

      {/* the current crop's section label, under the sheet */}
      <div style={{ position: 'absolute', left: SX, top: SY + SH + (portrait ? 30 : 34) * U, opacity: op(sIn(cur)),
        fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1, color: SPARK_TEXT }}>
        {(pages[cur]?.label ?? '').toUpperCase()}
      </div>

      {/* the document's facts */}
      <div style={{
        position: 'absolute', left: portrait ? PAD_X : PAD_X + SW + CW * 0.06,
        top: portrait ? height * 0.70 : SY, width: portrait ? CW : CW * 0.34,
        display: portrait ? 'flex' : 'block', gap: 30 * U,
      }}>
        {stats.map(statBlock)}
      </div>
      {!portrait && credit ? (
        <div style={{ position: 'absolute', left: PAD_X + SW + CW * 0.06, top: SY + SH - 110 * U, width: CW * 0.34 }}>
          <div style={{ fontFamily: HAI_TYPE.serif, fontSize: 25 * U, color: CLAUDE.INK, lineHeight: 1.4, opacity: op(sCredit) }}>
            {credit.split(' · ')[0]}
          </div>
          <div style={{ fontFamily: HAI_TYPE.serif, fontSize: 25 * U, color: SPARK_TEXT, lineHeight: 1.4, opacity: op(sRev), marginTop: 6 * U }}>
            {credit.split(' · ')[1] ?? ''}
          </div>
        </div>
      ) : null}

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height}
        portrait={portrait} top={portrait ? height * 0.8 : undefined} fontSize={portrait ? T.spark : undefined} />
    </AbsoluteFill>
  );
};
