// tokens.ts — the lecture-video design tokens (see unreal-reels/brutalist/DESIGN.md).
// One red, warm ink, grays as the only neutrals — no blue. Three typefaces:
// Lato (live deck), Inter (overlays, loaded in fonts.ts), JetBrains Mono (numbers).
import { Easing } from "remotion";
import { OVERLAY_FONT, MONO_FONT } from "./fonts";

export const COLORS = {
  white: "#FFFFFF",
  ink: "#2a1a0e", // warm near-black — body, headings, marks
  red: "#C8102E", // the one accent: brand, emphasis, primary data series
  secondary: "#545454", // captions, dimmed/earlier bullets, axis labels
  border: "#D4D4D4", // hairlines only
  ochre: "#C8860E", // decorative accent only (underlines/rules), never body text
};

export const FONTS = { overlay: OVERLAY_FONT, mono: MONO_FONT };

// Motion: ease-out-quart. No bounce, no overshoot, no scale-on-mount.
export const EASE = Easing.bezier(0.2, 0.8, 0.2, 1);
export const ENTER = 10; // frames (~320ms @30fps) — element entrance
export const DRAW = 16; // frames — a stroke drawing on

// numeric tokens to set in mono: 60%, 0.8, 0.6/0.3, 2016, 40 (non-global: safe for
// both String.split with the capture group AND RegExp.test without lastIndex state)
export const NUM_RE = /(\d[\d.,]*\s*%?|\d+\s*\/\s*\d+)/;
