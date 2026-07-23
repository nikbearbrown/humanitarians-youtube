// Lecture.tsx — the assembly. Audio-first: each slide's window is its real spoken
// duration (actual_duration_s) + a tail-padding breath. One slide = one outer
// <Sequence> carrying that slide's narration audio + karaoke captions.
//
// Visual per slide (Bear's rule):
//   visual_mode "live"  (slide has a D3 chart) -> live deck iframe the whole slide.
//   visual_mode "doodle" -> hold the live slide for slide_hold_s, then crossfade to
//                           a bears-doodles Manim clip for the rest.
//   Fallback: a doodle slide with no clip yet just stays live the whole time, so the
//   lecture always renders — doodles fill in over time.
import {
  AbsoluteFill,
  Audio,
  Sequence,
  staticFile,
} from "remotion";
import { DeckBackground } from "./DeckBackground";
import { Captions, CaptionLine } from "./Captions";
import { Doodle, DoodleSpec } from "./Doodle";
import { Bullets, BulletSpec } from "./Bullets";
import { EquationTangent, TangentSpec } from "./EquationTangent";
import { SectionCard, SectionSpec } from "./SectionCard";
import { useOverlayFonts } from "./fonts";
import beats from "./data/beats.json";
import captions from "./data/captions.json";
import doodles from "./data/doodles.json"; // { [beat_id]: { title?, elements: [...] } }
import bulletsData from "./data/bullets.json"; // { [beat_id]: { title?, bullets: [...] } }
import tangentsData from "./data/tangents.json"; // { [beat_id]: TangentSpec }
import sectionsData from "./data/sections.json"; // { [beat_id]: SectionSpec } — native cards
import deckStills from "./data/deck-stills.json"; // number[] — slide indices prerendered to PNG

const fps: number = beats.metadata.fps ?? 30;
const tailPad = Math.round((beats.metadata.tail_padding_s ?? 0.4) * fps);
const fadeIn = Math.round((beats.metadata.crossfade_frames ?? 0) as number);
const holdFrames = Math.round((beats.metadata.slide_hold_s ?? 3.5) * fps);
const XFADE = 10; // frames to crossfade slide -> doodle

type Beat = {
  beat_id: string;
  slide_index?: number;
  visual_mode?: "live" | "doodle" | "bullets" | "equation";
  actual_duration_s?: number;
  audio_file?: string;
};

const doodleSpecs = doodles as Record<string, DoodleSpec>;
const hasDoodle = (bid: string) => (doodleSpecs[bid]?.elements?.length ?? 0) > 0;
const bulletSpecs = bulletsData as Record<string, BulletSpec>;
const hasBullets = (bid: string) => (bulletSpecs[bid]?.bullets?.length ?? 0) > 0;
const tangentSpecs = tangentsData as Record<string, TangentSpec>;
const sectionSpecs = sectionsData as Record<string, SectionSpec>;
const HAS_STILL = new Set<number>(deckStills as number[]); // hold slides use the PNG when prerendered

export function slideFrames(b: Beat): number {
  const d = b.actual_duration_s ?? 0;
  return Math.max(1, Math.round(d * fps) + tailPad);
}

export function totalFrames(): number {
  return (beats.beats as Beat[]).reduce((acc, b) => acc + slideFrames(b), 0);
}

const SlideVisual: React.FC<{ beat: Beat; dur: number; lines: CaptionLine[] }> = ({
  beat,
  dur,
  lines,
}) => {
  const bid = beat.beat_id;

  // title / "Part N" divider / close: render natively (no deck iframe -> no reload
  // hitch at the section boundaries that jittered the export every few minutes)
  if (sectionSpecs[bid]) {
    return <SectionCard spec={sectionSpecs[bid]} />;
  }

  // equation tangent: a standalone generated explainer (no deck slide, no live hold)
  if (beat.visual_mode === "equation" && tangentSpecs[bid]) {
    return (
      <AbsoluteFill style={{ background: "#fff" }}>
        <EquationTangent spec={tangentSpecs[bid]} phaseFrames={dur} />
      </AbsoluteFill>
    );
  }

  const roomForPhase2 = beat.visual_mode === "doodle" && dur > holdFrames + XFADE;
  // tier 2 = authored doodle; tier 3 = auto bullets; else stay live (tier 1 / fallback)
  const phase2: "doodle" | "bullets" | null = !roomForPhase2
    ? null
    : hasDoodle(bid)
    ? "doodle"
    : hasBullets(bid)
    ? "bullets"
    : null;

  if (!phase2) {
    // live (D3) chart slides — kept live so their chart animations play
    return <DeckBackground slideIndex={beat.slide_index ?? 0} fadeInFrames={fadeIn} mode="live" />;
  }
  return (
    <>
      {/* hold the slide, then it unmounts once phase 2 has faded in. Use the
          prerendered still when available (no iframe reload); else fall back live. */}
      <Sequence durationInFrames={holdFrames + XFADE} name={`${bid}-hold`}>
        <DeckBackground
          slideIndex={beat.slide_index ?? 0}
          fadeInFrames={fadeIn}
          mode={HAS_STILL.has(beat.slide_index ?? -1) ? "still" : "live"}
        />
      </Sequence>
      <Sequence from={holdFrames} name={`${bid}-${phase2}`}>
        <AbsoluteFill style={{ background: "#fff" }}>
          {phase2 === "doodle" ? (
            <Doodle spec={doodleSpecs[bid]} lines={lines} holdFrames={holdFrames} phaseFrames={dur - holdFrames} />
          ) : (
            <Bullets spec={bulletSpecs[bid]} lines={lines} holdFrames={holdFrames} phaseFrames={dur - holdFrames} />
          )}
        </AbsoluteFill>
      </Sequence>
    </>
  );
};

export const Lecture: React.FC = () => {
  useOverlayFonts(); // load Inter + JetBrains Mono in render scope (not at module load)
  let start = 0;
  const capSlides =
    (captions as { slides: Record<string, { lines: CaptionLine[] }> }).slides || {};

  return (
    <AbsoluteFill style={{ background: "#000" }}>
      {(beats.beats as Beat[]).map((b) => {
        const dur = slideFrames(b);
        const from = start;
        start += dur;
        const lines = capSlides[b.beat_id]?.lines ?? [];
        return (
          <Sequence key={b.beat_id} from={from} durationInFrames={dur} name={b.beat_id}>
            <SlideVisual beat={b} dur={dur} lines={lines} />
            {b.audio_file ? <Audio src={staticFile(b.audio_file)} /> : null}
            {/* tangents are already text-rich; captions would clash with the panel */}
            {b.visual_mode !== "equation" ? <Captions lines={lines} /> : null}
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
