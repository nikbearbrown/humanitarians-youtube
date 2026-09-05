// claude — the Claude desktop app palette, as a brand token set.
// Used by the `claude` brand (brand_variant.py) and the ClaudeComposerAsk /
// claude-* scenes. This is a FIDELITY palette: the values replicate the real
// Claude app (cream page, warm ink, terracotta spark), so unlike teardown /
// medhavy it should NOT be retinted — if it stops looking like the actual
// product it loses its reason to exist.
//
// Grammar: TERRACOTTA is the ONE accent (the spark, the send button, a
// summoned /skill token, the single focal moment). Everything else is warm
// ink on cream. Same "accent is earned" law as teardown — different hue.
//
// Voice pairing: Kokoro am_onyx (Bear / Liam) — free, local, the default
// for all claude-brand channels.

export const CLAUDE = {
  PAGE: '#FAF9F5',        // ground — the app's cream, never pure white
  CARD: '#FFFFFF',        // composer card / raised surfaces
  BORDER: '#E5E2D9',      // hairline card borders
  FOOTER: '#F1EFE7',      // footer strip / secondary surface
  INK: '#3D3929',         // primary text — warm near-black
  INK_SOFT: '#73705F',    // secondary text, chips
  GHOST: '#A9A491',       // placeholder / disabled text
  SPARK: '#D97757',       // THE accent — the Claude spark terracotta
  SEND: '#C6613F',        // send button / deeper accent step
  PILL: '#EDEBE1',        // pill/toggle track background
} as const;

// Claude type stack. The app pairs a Tiempos-class serif (greetings,
// document headings) with a clean UI sans (everything else). EB Garamond is
// the bundled serif fallback (already shipped in runtime/fonts).
export const CLAUDE_FONT = {
  serif: '"Tiempos Text", "EB Garamond", Georgia, "Times New Roman", serif',
  ui: '-apple-system, "SF Pro Text", "Segoe UI", "Helvetica Neue", sans-serif',
  mono: 'ui-monospace, "SF Mono", Menlo, monospace',
} as const;

export type ClaudeTokens = typeof CLAUDE;
