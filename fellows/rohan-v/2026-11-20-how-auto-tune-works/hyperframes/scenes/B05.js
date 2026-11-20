// B05 · listen: the three takes play (autotune.py's take / gentle / hard). During each clip a playhead sweeps the
// roll in real time and that take's track lights; the notes glow as the playhead passes them.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.15 });
  K.lights(scene, 0xffffff, 0x553366);
  const D = env.D, roll = env.data.roll, win = env.data.win;
  scene.add(K.grid(60, 60, 0x6a4a7a, 0.14, -3.2));
  const dust = K.dust(scene, 340, 16, 0xd8a8ff, 0.06, 41);
  const R = K.pianoRoll(scene, roll, { xs: 2.9 });
  const cols = [0xff8a5b, 0xffc857, 0x4fe3d1], keys = ["detected", "gentle", "hard"];
  const tubes = keys.map((k, i) => { const m = R.tube(k, cols[i], 0.045); R.drawTo(k, R.t1); m.position.z = 0.02 * i; return m; });
  const ph = K.slab(0.04, 6.4, 0xffffff, 0); scene.add(ph);
  const phG = K.glow(0xffffff, 1.4, 0); scene.add(phG);
  const names = { 60: "C4", 62: "D4", 64: "E4", 67: "G4", 69: "A4" };
  // the take files start 0.12 s before the first note: clip time = roll time
  return function renderAt(t) {
    let active = -1, rt = 0;
    win.forEach((w, i) => { if (t >= w.from && t < w.to) { active = i; rt = t - w.from; } });
    const intro = K.prog(t, 0.2, 1.0);
    tubes.forEach((m, i) => { m.material.opacity = active < 0 ? 0.55 * intro : (active === i ? 1 : 0.16); });
    if (active >= 0) {
      ph.position.set(R.X(Math.min(rt, R.t1 + 0.1)), 0, 0.1); ph.material.opacity = 0.5; phG.material.opacity = 0.9;
      phG.position.copy(R.at(keys[active], rt)); phG.material.color.setHex(cols[active]);
    } else { ph.material.opacity = 0; phG.material.opacity = 0; }
    R.notes.forEach((n) => { const lit = active >= 0 && rt >= n.a && rt < n.b ? 1 : 0; n.box.material.opacity = 0.07 + 0.2 * lit; });
    for (const m in names) K.pin("pn" + m, new THREE.Vector3(R.X(R.t0 - 0.26), R.Y(+m), 0), cam, env, 0.9 * intro);
    const p = K.prog(t, 0, D, K.ease.inOut);
    const ca = K.deg(14 - 22 * p), cr = env.portrait ? 13.2 : 11.8;
    cam.position.set(0.3 + Math.sin(ca) * cr, 1.6 + 0.4 * Math.sin(t * 0.25), Math.cos(ca) * cr);
    cam.lookAt(-0.4, 0.1, 0);
    dust(t);
    r.render(scene, cam);
  };
}
