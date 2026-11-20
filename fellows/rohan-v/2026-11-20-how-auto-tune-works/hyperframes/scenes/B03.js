// B03 · snap: the same take corrected twice. Gold = retune speed 60 ms (pulled in gently, vibrato kept); cyan = zero
// (instant: flat steps). Both tracks are the pitch MEASURED on autotune.py's corrected audio, not the targets.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.15 });
  K.lights(scene, 0xffffff, 0x553366);
  const c = env.cue, D = env.D, roll = env.data.roll;
  scene.add(K.grid(60, 60, 0x6a4a7a, 0.14, -3.2));
  const dust = K.dust(scene, 340, 16, 0xd8a8ff, 0.06, 31);
  const R = K.pianoRoll(scene, roll, { xs: 2.9 });
  const sung = R.tube("detected", 0xff8a5b, 0.04);
  const gen = R.tube("gentle", 0xffc857, 0.045);
  const hrd = R.tube("hard", 0x4fe3d1, 0.05);
  const hG = K.glow(0xffc857, 1.2, 0), hH = K.glow(0x4fe3d1, 1.3, 0); scene.add(hG, hH);
  const names = { 60: "C4", 62: "D4", 64: "E4", 67: "G4", 69: "A4" };
  // snap flashes where the zero-speed track jumps to the next note
  const flashes = roll.t_starts.slice(1).map((ts) => { const g = K.glow(0x4fe3d1, 1.6, 0); g.position.copy(R.at("hard", ts + 0.01)); scene.add(g); return { g, ts }; });
  const g0 = c.gentle - 0.3, g1 = g0 + 2.4, h0 = c.zero, h1 = h0 + 2.0;
  return function renderAt(t) {
    R.drawTo("detected", R.t1);
    sung.material.opacity = 0.9 - 0.6 * K.prog(t, g0, 0.8);
    const rg = R.t0 + (R.t1 - R.t0) * K.prog(t, g0, g1 - g0, (x) => x);
    R.drawTo("gentle", rg);
    gen.material.opacity = 1 - 0.55 * K.prog(t, h0, 0.8);
    hG.position.copy(R.at("gentle", rg)); hG.material.opacity = t > g0 && t < g1 ? 0.9 : 0;
    const rh = R.t0 + (R.t1 - R.t0) * K.prog(t, h0, h1 - h0, (x) => x);
    R.drawTo("hard", rh);
    hH.position.copy(R.at("hard", rh)); hH.material.opacity = t > h0 && t < h1 ? 1 : 0;
    flashes.forEach(({ g, ts }) => {
      const tf = h0 + (ts - R.t0) / (R.t1 - R.t0) * (h1 - h0);
      const a = Math.max(0, 1 - Math.abs(t - tf) / 0.35);
      g.material.opacity = a; g.scale.setScalar(1 + 2.5 * (1 - a));
    });
    R.notes.forEach((n) => { n.box.material.opacity = 0.08 + 0.12 * K.prog(t, c.nearest, 0.6); });
    for (const m in names) K.pin("pn" + m, new THREE.Vector3(R.X(R.t0 - 0.26), R.Y(+m), 0), cam, env, 0.9 * K.prog(t, 0.3, 0.8));
    const p = K.prog(t, 0, D, K.ease.inOut);
    const ca = K.deg(-26 + 30 * p), cr = env.portrait ? 13.4 : 12.0;
    cam.position.set(0.4 + Math.sin(ca) * cr, 2.0 - 0.6 * p, Math.cos(ca) * cr);
    cam.lookAt(-0.4, 0.2, 0);
    dust(t);
    r.render(scene, cam);
  };
}
