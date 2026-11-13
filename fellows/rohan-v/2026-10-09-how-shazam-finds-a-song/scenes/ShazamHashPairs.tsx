import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { SHZ, SpecImage, SpecAxes, Stat, PhoneBaseline, useSpec, fmt, HZ_PER_BIN } from './shazam/shzKit';

/**
 * ShazamHashPairs — B02 of "How Shazam Finds a Song."
 *
 * The constellation from B01 (faint), one ANCHOR peak lit, its TARGET ZONE drawn (2-64 columns
 * ahead, within 96 bins: the run's FAN_OUT/ZONE settings), and lines to the peaks it pairs with.
 * The first pair's three numbers (both frequencies and the gap) and the packed hash value are
 * the run's worked example; the per-second rate is the library's.
 *
 *   one     "One point on its own"      constellation, ghosted
 *   anchor  "becomes an anchor"         anchor ring
 *   paired  "paired with a few points"  target zone + pair lines
 *   three   "three numbers"             the numbers card
 *   here    "Here:"                     example pair lit, values fill in
 *   packed  "packed into one code"      packed value
 *   hash    "called a hash"             HASH label
 *   rate    "fifty-seven of them"       rate stat
 */

export const shazamHashPairsSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Pair the Points Into Codes'),
  sparkLine: z.string().default('Two frequencies and a gap: one hash.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type ShazamHashPairsProps = z.infer<typeof shazamHashPairsSchema>;

export const ShazamHashPairs: React.FC<ShazamHashPairsProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tOne = at('one', 0.02), tAnchor = at('anchor', 0.14), tPaired = at('paired', 0.22), tThree = at('three', 0.33);
  const tHere = at('here', 0.45), tPacked = at('packed', 0.7), tHash = at('hash', 0.78), tRate = at('rate', 0.86);
  const headIn = sp(0);
  const sOne = sp(tOne), sAnchor = sp(tAnchor), zone = ramp(tPaired, tPaired + 0.04), lines = ramp(tPaired + 0.02, tPaired + 0.09);
  const sThree = sp(tThree), sHere = sp(tHere), sPacked = sp(tPacked), sHash = sp(tHash), sRate = sp(tRate);
  const sparkIn = sp(clamp(tRate + 0.04, 0, 0.97));

  const LAB = portrait ? 175 : 92 * U;
  const SW = portrait ? CW - LAB : CW * 0.6 - LAB;
  const SH = portrait ? height * 0.225 : height * 0.5;
  const SX = PAD_X + LAB;
  const SY = portrait ? height * 0.255 : height * 0.27;
  const lbl = portrait ? T.label * 0.68 : 22 * U;
  const { x, y } = useSpec(SW, SH);
  const H = SHZ.hash;
  const [at0, af0] = H.anchor as number[];
  const tg = H.targets as number[][];
  const zt0 = x(at0 + SHZ.params.zone_t[0]), zt1 = x(Math.min(SHZ.spec.cols, at0 + SHZ.params.zone_t[1]));
  const zb = SHZ.params.zone_f_hz / HZ_PER_BIN;
  const zy0 = y(Math.min(SHZ.spec.bins, af0 + zb)), zy1 = y(Math.max(0, af0 - zb));
  const R = portrait ? 9 : 7 * U;

  const panel = (
    <>
      <div style={{ position: 'absolute', left: SX, top: SY, width: SW, height: SH, background: CLAUDE.CARD, border: `1.5px solid ${CLAUDE.BORDER}`, opacity: op(sOne) }}>
        <SpecImage w={SW} h={SH} clean={op(sOne) * 0.16} />
      </div>
      <svg width={SW} height={SH} style={{ position: 'absolute', left: SX, top: SY, overflow: 'visible' }}>
        <SpecAxes w={SW} h={SH} size={lbl} opacity={op(sOne)} />
        <rect x={zt0} y={zy0} width={(zt1 - zt0) * zone} height={zy1 - zy0} fill="none" stroke={SPARK_TEXT}
          strokeWidth={3} strokeDasharray="10 8" opacity={zone} />
        {(SHZ.spec.peaks as number[][]).map((p, i) => (
          <circle key={i} cx={x(p[0])} cy={y(p[1])} r={R} fill={CLAUDE.INK_SOFT} opacity={0.45 * op(sOne)} />
        ))}
        {tg.map((p, i) => {
          const first = i === 0;
          const k = clamp(lines * tg.length - i, 0, 1);
          return (
            <g key={i} opacity={k}>
              <line x1={x(at0)} y1={y(af0)} x2={x(at0) + (x(p[0]) - x(at0)) * k} y2={y(af0) + (y(p[1]) - y(af0)) * k}
                stroke={first && op(sHere) > 0.5 ? SPARK_TEXT : CLAUDE.INK} strokeWidth={first && op(sHere) > 0.5 ? 6 : 3} opacity={first ? 1 : 0.75 - 0.35 * op(sHere)} />
              <circle cx={x(p[0])} cy={y(p[1])} r={R * 1.5} fill={first && op(sHere) > 0.5 ? SPARK_TEXT : CLAUDE.INK} />
            </g>
          );
        })}
        <circle cx={x(at0)} cy={y(af0)} r={R * (1.5 + 1.4 * op(sAnchor))} fill="none" stroke={SPARK_TEXT} strokeWidth={5} opacity={op(sAnchor)} />
        <circle cx={x(at0)} cy={y(af0)} r={R * 1.5} fill={SPARK_TEXT} opacity={op(sAnchor)} />
      </svg>
      <div style={{ position: 'absolute', left: SX + x(at0) - 30 * U, top: SY + y(af0) + R * 4, opacity: op(sAnchor),
        fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: SPARK_TEXT }}>ANCHOR</div>
      <div style={{ position: 'absolute', left: SX + zt0, top: SY + zy0 - lbl * 1.5, opacity: zone,
        fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: SPARK_TEXT, whiteSpace: 'nowrap' }}>TARGET ZONE</div>
    </>
  );

  const rows = [
    { k: 'FIRST FREQUENCY', v: `${fmt(H.anchor_hz)} Hz` },
    { k: 'SECOND FREQUENCY', v: `${fmt(H.target_hz)} Hz` },
    { k: 'TIME BETWEEN', v: `${H.dt_s.toFixed(2)} s` },
  ];
  const card = (w: number, size: number) => (
    <div style={{ width: w, background: CLAUDE.CARD, border: `1.5px solid ${CLAUDE.BORDER}`, borderTop: `${6 * (portrait ? 1 : U)}px solid ${CLAUDE.INK}`,
      borderRadius: 16, padding: `${size * 0.6}px ${size * 0.8}px`, boxSizing: 'border-box', opacity: op(sThree) }}>
      <div style={{ fontFamily: HAI_TYPE.sans, fontSize: size * 0.8, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK, marginBottom: size * 0.4 }}>THREE NUMBERS</div>
      {rows.map((r, i) => (
        <div key={i} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', padding: `${size * 0.22}px 0`,
          borderBottom: i < 2 ? `1px solid ${CLAUDE.BORDER}` : 'none' }}>
          <span style={{ fontFamily: HAI_TYPE.sans, fontSize: size * 0.8, fontWeight: 700, color: CLAUDE.INK_SOFT }}>{r.k}</span>
          <span style={{ fontFamily: HAI_TYPE.mono, fontSize: size * 1.05, fontWeight: 700, color: SPARK_TEXT, opacity: op(sHere) }}>{r.v}</span>
        </div>
      ))}
      <div style={{ marginTop: size * 0.7, opacity: op(sPacked) }}>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: size * 0.8, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK_SOFT }}>
          {op(sHash) > 0.5 ? 'ONE HASH' : 'PACKED INTO ONE CODE'}</div>
        <div style={{ fontFamily: HAI_TYPE.mono, fontSize: size * 1.6, fontWeight: 700, color: CLAUDE.INK }}>{fmt(H.packed)}</div>
      </div>
    </div>
  );

  if (portrait) {
    /* Phone: one compact card, every row its own line (the first phone cut stacked the rate stat on
       the card header and ran the hash into the spark line at the end of the beat). */
    const s = T.label * 0.74;
    const line = (k: string, v: React.ReactNode, o: number, last = false) => (
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', padding: `${s * 0.2}px 0`, opacity: o,
        borderBottom: last ? 'none' : `1px solid ${CLAUDE.BORDER}` }}>
        <span style={{ fontFamily: HAI_TYPE.sans, fontSize: s * 0.8, fontWeight: 700, color: CLAUDE.INK_SOFT }}>{k}</span>
        <span style={{ fontFamily: HAI_TYPE.mono, fontSize: s, fontWeight: 700, color: SPARK_TEXT }}>{v}</span>
      </div>
    );
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {panel}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.52, width: CW, boxSizing: 'border-box', background: CLAUDE.CARD,
          border: `1.5px solid ${CLAUDE.BORDER}`, borderTop: `6px solid ${CLAUDE.INK}`, borderRadius: 16, padding: `${s * 0.5}px ${s * 0.7}px`, opacity: op(sThree) }}>
          <div style={{ fontFamily: HAI_TYPE.sans, fontSize: s * 0.8, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK, marginBottom: s * 0.2 }}>THREE NUMBERS</div>
          {rows.map((r) => line(r.k, r.v, op(sHere) * 0.6 + 0.4))}
          {line(op(sHash) > 0.5 ? 'ONE HASH' : 'PACKED INTO ONE CODE', <span style={{ color: CLAUDE.INK }}>{fmt(H.packed)}</span>, op(sPacked))}
          {line('MY VERSION, PER SECOND', `${SHZ.library.hashes_per_s} HASHES`, op(sRate), true)}
        </div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      {panel}
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.64, top: SY }}>{card(CW * 0.36, 26 * U)}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.64, top: SY + SH - 110 * U }}>
        <Stat value={`${SHZ.library.hashes_per_s} hashes`} label="PER SECOND OF MUSIC, IN MY VERSION" size={52 * U} opacity={op(sRate)} accent />
      </div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
