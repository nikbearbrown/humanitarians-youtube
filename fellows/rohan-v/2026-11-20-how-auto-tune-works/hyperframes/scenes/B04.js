// B04 · shifting: the wave cut into single cycles ("grains"). Speeding up squeezes every grain (higher, shorter, the
// vowel moves); the patent's way then repeats whole squeezed cycles to restore the length (vowel still moved);
// PSOLA keeps each grain's shape and only spaces them closer (higher, same length, same vowel).
// The grain is one period of autotune.py's own A4 frame. ratio = 2^(4/12) (up 4 semitones).
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 33, exposure: 1.15 });
  K.lights(scene, 0xffffff, 0x553366);
  const c = env.cue, D = env.D, d = env.data, ratio = d.ratio;
  scene.add(K.grid(60, 60, 0x6a4a7a, 0.14, -3.4));
  const dust = K.dust(scene, 320, 16, 0xd8a8ff, 0.06, 51);
  // one cycle of the real wave, painted once
  const per = Math.round(d.tau_ms / d.step_ms);
  let i0 = 0; for (let i = 0; i < per; i++) if (d.wave[i] < d.wave[i0]) i0 = i;     // start at a trough
  const cyc = d.wave.slice(i0, i0 + per + 1);
  const pk = Math.max(...cyc.map(Math.abs));
  const tex = K.canvasTex(512, 256, (g, w, h) => {
    g.lineCap = "round"; g.lineJoin = "round";
    for (const [lw, a] of [[26, 0.12], [14, 0.25], [6, 1]]) {
      g.strokeStyle = `rgba(255,255,255,${a})`; g.lineWidth = lw; g.beginPath();
      cyc.forEach((v, i) => { const x = 20 + (i / (cyc.length - 1)) * (w - 40), y = h / 2 - (v / pk) * (h * 0.36); i ? g.lineTo(x, y) : g.moveTo(x, y); });
      g.stroke();
    }
  });
  const PW = 1.12, N = 8, L = PW * N, X0 = -L / 2;
  const mk = (color) => { const m = new THREE.Mesh(new THREE.PlaneGeometry(1, 0.95), new THREE.MeshBasicMaterial({ map: tex, color, transparent: true,
    blending: THREE.AdditiveBlending, depthWrite: false, opacity: 0 })); scene.add(m); return m; };
  const rowY = [2.0, 0, -2.0];
  const orig = [], fast = [], extra = [], psola = [];
  for (let k = 0; k < N; k++) { orig.push(mk(0xb79cff)); fast.push(mk(0xff8a5b)); }
  const NX = Math.ceil(N * ratio) - N;
  for (let k = 0; k < NX; k++) extra.push(mk(0xffc857));
  const NP = Math.round(N * ratio);
  for (let k = 0; k < NP; k++) psola.push(mk(0x4fe3d1));
  // length rulers under the rows
  const ruler = (y, color) => { const m = K.slab(1, 0.05, color, 0); m.position.set(0, y - 0.72, 0); scene.add(m); return m; };
  const rO = ruler(rowY[0], 0xb79cff), rF = ruler(rowY[1], 0xff8a5b), rP = ruler(rowY[2], 0x4fe3d1);
  const setRuler = (m, len, o) => { m.scale.x = Math.max(0.001, len); m.position.x = X0 + len / 2; m.material.opacity = o; };
  return function renderAt(t) {
    const a0 = K.prog(t, 0.2, 1.0);
    orig.forEach((m, k) => { m.position.set(X0 + PW * (k + 0.5), rowY[0], 0); m.scale.set(PW, 1, 1); m.material.opacity = 0.95 * K.prog(t, 0.2 + k * 0.08, 0.5); });
    setRuler(rO, L, 0.5 * a0);
    // sped up: appears as a copy, then squeezes on "gets shorter"
    const fOn = K.prog(t, c.speed - 0.2, 0.5), sq = K.prog(t, c.speed + 0.2, Math.max(0.6, c.shorter - c.speed), K.ease.inOut);
    const pwF = K.lerp(PW, PW / ratio, sq);
    fast.forEach((m, k) => { m.position.set(X0 + pwF * (k + 0.5), rowY[1], 0); m.scale.set(pwF, 1, 1); m.material.opacity = 0.95 * fOn; });
    // the patent's way: repeat whole squeezed cycles to fill the original length
    extra.forEach((m, k) => {
      const on = K.prog(t, c.cycles - 0.2 + k * 0.22, 0.4, K.ease.back);
      m.position.set(X0 + pwF * (N + k + 0.5), rowY[1] + (1 - on) * 0.6, 0); m.scale.set(pwF * Math.max(on, 0.001), 1, 1); m.material.opacity = 0.95 * on;
    });
    const fillF = N * pwF + extra.length * pwF * K.prog(t, c.cycles - 0.2, 0.4 + extra.length * 0.22);
    setRuler(rF, fillF, 0.5 * fOn);
    // PSOLA: same grain shape, spaced closer, same length
    const pOn = K.prog(t, c.respace - 0.3, 0.5), sp = K.prog(t, c.respace, 1.2, K.ease.inOut);
    const gap = K.lerp(PW, PW / ratio, sp);
    psola.forEach((m, k) => {
      const show = k < N ? 1 : K.prog(t, c.respace + 0.4 + (k - N) * 0.15, 0.4);
      m.position.set(X0 + PW / 2 + gap * k, rowY[2], 0.002 * k); m.scale.set(PW, 1, 1); m.material.opacity = 0.9 * pOn * show;
    });
    setRuler(rP, Math.min(L, PW + gap * (N - 1 + (NP - N) * K.prog(t, c.respace + 0.4, 0.15 * (NP - N) + 0.4))), 0.5 * pOn);
    K.pin("rl0", new THREE.Vector3(X0, rowY[0] + 0.62, 0), cam, env, 0.9 * a0, 0, 0);
    K.pin("rl1", new THREE.Vector3(X0, rowY[1] + 0.62, 0), cam, env, 0.9 * fOn, 0, 0);
    K.pin("rl2", new THREE.Vector3(X0, rowY[2] + 0.62, 0), cam, env, 0.9 * pOn, 0, 0);
    const p = K.prog(t, 0, D, K.ease.inOut);
    const ca = K.deg(22 - 30 * p), cr = env.portrait ? 14.2 : 12.6;
    cam.position.set(0.9 + Math.sin(ca) * cr, 1.2 + 0.8 * p, Math.cos(ca) * cr);
    cam.lookAt(0.6, 0, 0);
    dust(t);
    r.render(scene, cam);
  };
}
