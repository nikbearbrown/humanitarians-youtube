import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { SHZ, PhoneBaseline, Chip } from './shazam/shzKit';

/**
 * ShazamVersions — B06 of "How Shazam Finds a Song."
 *
 * Song C re-performed four ways (synth.py renders the same song in a new key, at a new speed, or
 * just its melody hummed) and queried at the same easy noise level (+10 dB). Each row is the vote
 * count for Song C in its best offset bin; the line marks the 8 votes fingerprint.py needs to call
 * a match. Only the original recording clears it.
 *
 *   cant / exact  "can't do" / "one exact recording"   frame + the original's row
 *   semitone      "one semitone higher"                row 2
 *   faster        "Six percent faster"                 row 3
 *   hummed        "The melody alone, hummed"           row 4
 *   moved         "every gap has moved"                stamp
 *   apps          "Apps that recognise humming"        footnote
 */

export const shazamVersionsSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('It Matches a Recording, Not a Song'),
  sparkLine: z.string().default('Change the key or the speed, and the codes change.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type ShazamVersionsProps = z.infer<typeof shazamVersionsSchema>;

const ROWS = [
  { key: 'same recording', name: 'THE SAME RECORDING', short: 'SAME RECORDING' },
  { key: 'one semitone higher', name: 'ONE SEMITONE HIGHER', short: 'SEMITONE UP' },
  { key: '6% faster', name: '6% FASTER', short: '6% FASTER' },
  { key: 'melody only, hummed', name: 'THE MELODY, HUMMED', short: 'HUMMED' },
];
const NEED = 8;

export const ShazamVersions: React.FC<ShazamVersionsProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tExact = at('exact', 0.08), tSemi = at('semitone', 0.3), tFast = at('faster', 0.42), tHum = at('hummed', 0.52);
  const tMoved = at('moved', 0.68), tApps = at('apps', 0.8);
  const headIn = sp(0);
  const rowT = [tExact, tSemi, tFast, tHum];
  const grows = rowT.map((t) => ramp(t, t + 0.05));
  const sShell = sp(at('cant', 0.02)), sMoved = sp(tMoved), sApps = sp(tApps);
  const sparkIn = sp(clamp(tApps + 0.06, 0, 0.97));
  const V = SHZ.variants as Record<string, { song_c_votes: number; identified: boolean }>;
  const vmax = Math.max(...ROWS.map((r) => V[r.key].song_c_votes));
  const lbl = portrait ? T.label * 0.8 : 24 * U;

  const rows = (nameW: number, barW: number, rowH: number, gap: number, valSize: number) => (
    <div style={{ position: 'relative', display: 'flex', flexDirection: 'column', gap, opacity: op(sShell) }}>
      {ROWS.map((r, i) => {
        const v = V[r.key];
        const k = grows[i];
        const w = (v.song_c_votes / vmax) * barW * k;
        return (
          <div key={r.key} style={{ display: 'flex', flexWrap: portrait ? 'wrap' : 'nowrap', alignItems: 'center', gap: 20 * (portrait ? 1 : U), height: portrait ? undefined : rowH }}>
            <div style={{ width: nameW, flexBasis: portrait ? '100%' : undefined, fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1, color: CLAUDE.INK, opacity: 0.35 + 0.65 * k }}>
              {portrait ? r.short : r.name}</div>
            <div style={{ position: 'relative', width: barW, flexShrink: 0, height: rowH * 0.62, background: CLAUDE.FOOTER, borderRadius: 8 }}>
              <div style={{ position: 'absolute', left: 0, top: 0, height: '100%', width: Math.max(k > 0 ? 6 : 0, w), borderRadius: 8,
                background: v.identified ? CLAUDE.INK : SPARK_TEXT }} />
              <div style={{ position: 'absolute', left: (NEED / vmax) * barW, top: -rowH * 0.18, width: 3, height: rowH, background: CLAUDE.INK_SOFT }} />
            </div>
            <div style={{ width: valSize * 2.4, flexShrink: 0, fontFamily: HAI_TYPE.serif, fontSize: valSize, fontWeight: 700, color: v.identified ? CLAUDE.INK : SPARK_TEXT, opacity: k }}>
              {Math.round(v.song_c_votes * k)}</div>
            <div style={{ opacity: k, flexShrink: 0 }}><Chip text={v.identified ? 'MATCH' : 'NO MATCH'} size={lbl * (portrait ? 0.7 : 0.85)} accent={!v.identified} /></div>
          </div>
        );
      })}
    </div>
  );
  const needNote = (size: number) => (
    <div style={{ fontFamily: HAI_TYPE.sans, fontSize: size, fontWeight: 800, letterSpacing: 1, color: CLAUDE.INK_SOFT, opacity: op(sShell) }}>
      VOTES FOR SONG C · THE LINE: {NEED} VOTES TO CALL A MATCH</div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.215, width: CW }}>{needNote(T.label * 0.62)}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.27, width: CW }}>{rows(CW, CW - T.body * 2.4 - 330, height * 0.04, height * 0.012, T.body)}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.705, opacity: op(sMoved) }}>
          <Chip text="EVERY FREQUENCY AND GAP MOVED" size={T.label * 0.72} accent />
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.75, width: CW, whiteSpace: 'nowrap', opacity: op(sApps), fontFamily: HAI_TYPE.sans,
          fontSize: T.label * 0.66, fontWeight: 800, letterSpacing: 0.8, color: CLAUDE.INK_SOFT }}>HUM SEARCH: A DIFFERENT FINGERPRINT</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.255 }}>{needNote(22 * U)}</div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.31 }}>{rows(360 * U, CW - 360 * U - 380 * U, 86 * U, 24 * U, 52 * U)}</div>
      <div style={{ position: 'absolute', left: PAD_X + 380 * U, top: height * 0.775, opacity: op(sMoved) }}>
        <Chip text="SAME SONG TO YOU · EVERY FREQUENCY AND GAP MOVED TO THE FINGERPRINT" size={22 * U} accent />
      </div>
      <div style={{ position: 'absolute', right: PAD_X, top: height * 0.255, opacity: op(sApps), fontFamily: HAI_TYPE.sans,
        fontSize: 22 * U, fontWeight: 800, letterSpacing: 1, color: CLAUDE.INK_SOFT }}>HUM SEARCH: A DIFFERENT, MELODY-BASED FINGERPRINT</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
