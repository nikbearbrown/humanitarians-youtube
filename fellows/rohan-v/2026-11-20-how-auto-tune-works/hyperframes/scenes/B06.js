// B06 · then and now: a voice wave fans out into a stack of seismic traces (the kind of data the maths was first
// used on: echoes from rock layers, drawn as wiggles that line up across traces) and folds back into a voice.
// The seismic traces are an illustration (synthetic wiggles, seeded); the voice is autotune.py's A4 frame.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.15 });
  const c = env.cue, D = env.D, wave = env.data.wave;
  scene.add(K.grid(60, 60, 0x6a4a7a, 0.14, -3.0));
  const dust = K.dust(scene, 320, 16, 0xd8a8ff, 0.06, 61);
  const NT = 16, NP = 260, XL = 12;
  const pk = Math.max(...wave.map(Math.abs));
  const voice = [];
  for (let j = 0; j < NP; j++) {
    const f = j / (NP - 1), idx = f * (wave.length - 1), i = Math.floor(idx), a = idx - i;
    const v = (wave[i] * (1 - a) + wave[Math.min(i + 1, wave.length - 1)] * a) / pk;
    voice.push([(f - 0.5) * XL, v * 1.1]);
  }
  const R = K.rng(1997);
  const refl = [0, 1, 2, 3, 4].map(() => ({ x: -4.5 + R() * 9, dip: (R() - 0.5) * 0.22, A: (R() < 0.5 ? -1 : 1) * (0.35 + R() * 0.4), w: 0.16 + R() * 0.1 }));
  const ricker = (u) => (1 - 2 * u * u) * Math.exp(-u * u);
  const traces = [];
  for (let i = 0; i < NT; i++) {
    const pts = [];
    for (let j = 0; j < NP; j++) {
      const x = (j / (NP - 1) - 0.5) * XL;
      let y = 0;
      refl.forEach((q) => { y += q.A * ricker((x - q.x - q.dip * i * 2.2) / q.w); });
      y += (R() - 0.5) * 0.05;
      pts.push(y);
    }
    const rb = K.ribbon(NP, 0.045, i === 0 ? 0xff6fa8 : 0xb79cff, 0); scene.add(rb);
    traces.push({ rb, pts, z: -i * 0.55, yo: (i - NT / 2) * 0.05 });
  }
  const V = new THREE.Vector3();
  const tmp = Array.from({ length: NP }, () => new THREE.Vector3());
  return function renderAt(t) {
    // 0 = voice, 1 = seismic stack
    const m = K.prog(t, c.oil - 0.5, 1.4, K.ease.inOut) * (1 - K.prog(t, c.today - 0.2, 1.4, K.ease.inOut));
    traces.forEach((tr, i) => {
      for (let j = 0; j < NP; j++) {
        const [vx, vy] = voice[j];
        const sy = tr.pts[j] * 0.8 + tr.yo + 1.0;
        tmp[j].set(vx, K.lerp(vy, sy, m), K.lerp(0, tr.z, m));
      }
      tr.rb.userData.set(tmp);
      const base = K.prog(t, 0.2, 1.0);
      tr.rb.material.opacity = base * (i === 0 ? 1 : 0.75 * m);
      tr.rb.material.color.setHex(m > 0.5 ? 0xb79cff : (i === 0 ? 0xff6fa8 : 0xb79cff));
    });
    const p = K.prog(t, 0, D, K.ease.inOut);
    const ca = K.deg(-30 + 26 * p), cr = (env.portrait ? 13.5 : 12.0) + 2.0 * m;
    cam.position.set(Math.sin(ca) * cr, 2.2 + 2.0 * m, Math.cos(ca) * cr - 2.0 * m);
    V.set(0, 0.2 + 0.3 * m, -3.5 * m);
    cam.lookAt(V);
    dust(t);
    r.render(scene, cam);
  };
}
