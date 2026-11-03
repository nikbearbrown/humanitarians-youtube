// HUMANITARIANS audience palette — muted editorial (Economist / FT-adjacent) on the
// vox cream base. Same ROLE KEYS as tokens/vox.ts, so a scene retints by swapping the
// import.
//
// CVD RESOLUTION: the good/bad semantic pair is split ACROSS warm/cool — petrol teal
// (good) vs burnt orange (bad). Blue-vs-orange survives red-green colorblindness, the
// same principle Okabe-Ito uses, so the one pair that carries meaning stays safe even
// though the full editorial set isn't CVD-guaranteed.
//
// TWO BLUES: petrol (good accent) and navy (structure) are both cool/blue. Keep them
// in clearly different roles + positions — navy as entity-card fills and scaffolding,
// petrol as data marks — so they never read as one dark blue on a small frame.
//
// COLOR LAW (unchanged): position + an explicit label carry meaning; color only
// reinforces. On the cream ground the two lightest — amber and sage — are low-contrast,
// so keep them to fills / large areas with a label, never fine marks or text.
export const HUMANITARIANS = {
  CREAM: '#F3EBDD',   // ground — vox base cream (newsprint ground)
  INK: '#2F2A26',     // text / marks — vox base warm near-black
  TEAL: '#1F4E5F',    // accent A: good / kept / true — petrol teal (cool half of the pair)
  CRIMSON: '#E4572E', // accent B: bad / lost / broken — burnt orange (warm half of the pair)
  SLATE: '#29335C',   // structure — navy (entity cards w/ white text, scaffolding)
  GOLD: '#F3A712',    // highlighter — amber (FILL ONLY, never text)
} as const;

// Soft "human / growth" tertiary accent, OUTSIDE the good/bad semantic pair — for a
// third series, an organic/positive-neutral highlight, human motifs. Not a data accent.
export const HUMANITARIANS_SAGE = '#A8C686';

// Categorical / multi-series set (the five editorial accents), cool -> warm.
export const HUMANITARIANS_CATEGORICAL = [
  '#1F4E5F', // petrol teal
  '#29335C', // navy
  '#A8C686', // sage
  '#F3A712', // amber
  '#E4572E', // burnt orange
] as const;

// Fonts + house spring are audience-neutral; reuse tokens/vox.ts FONT and SPRING_SMOOTH.
