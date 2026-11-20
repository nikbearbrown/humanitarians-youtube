// B04 · the buffer: two reservoirs in the earbuds, a 50 ms one and a 200 ms one, filled by arriving packets and drained
// at the playing rate. Their levels are bluetooth.py's own (every 10 ms of the 6 s listening window). During the
// narration the window plays at half speed; during each listening clip, in real time, in step with what you hear.
// When the small one runs dry (the run's own gap times), it flashes red: that is the gap you hear.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.15 });
  K.lights(scene, 0xffffff, 0x224466);
  const c = env.cue, D = env.D, d = env.data;
  scene.add(K.grid(70, 70, 0x2a5a8a, 0.14, -2.4));
  const dust = K.dust(scene, 260, 18, 0x8ac8ff, 0.05, 6);
  const tank = (x, cap, color) => {
    const g = new THREE.Group(); g.position.set(x, 0, 0); scene.add(g);
    const H = 3.4, Rr = 0.9;
    const glass = new THREE.Mesh(new THREE.CylinderGeometry(Rr, Rr, H, 64, 1, true), new THREE.MeshBasicMaterial({ color: 0x9fd0ff,
      transparent: true, opacity: 0.1, side: THREE.DoubleSide, depthWrite: false, blending: THREE.AdditiveBlending }));
    glass.position.y = 0; g.add(glass);
    const rim = K.ring(Rr, 0x9fd0ff, 0.5, 0.02); rim.rotation.x = -Math.PI / 2; rim.position.y = H / 2; g.add(rim);
    const rim2 = K.ring(Rr, 0x9fd0ff, 0.5, 0.02); rim2.rotation.x = -Math.PI / 2; rim2.position.y = -H / 2; g.add(rim2);
    const liq = new THREE.Mesh(new THREE.CylinderGeometry(Rr * 0.94, Rr * 0.94, 1, 64), new THREE.MeshStandardMaterial({ color,
      emissive: color, emissiveIntensity: 0.7, transparent: true, opacity: 0.75, roughness: 0.3 }));
    g.add(liq);
    const top = K.glow(color, 2.6, 0.6); g.add(top);
    const alarm = K.glow(0xff5c6c, 5, 0); alarm.position.y = -H / 2 + 0.2; g.add(alarm);
    return { g, H, cap, liq, top, alarm };
  };
  const S = tank(-1.75, d.small_ms + 14.5, 0xff5c6c), L = tank(1.75, d.large_ms + 14.5, 0x5be49b);
  // packets falling in: a seeded stream that pauses during the run's body-blocking moments
  const drops = []; for (let i = 0; i < 16; i++) { const m = K.glowBox(0.12, 0.12, 0.12, 0x3da9ff, 1.6); scene.add(m); drops.push(m); }
  const at = (arr, wt) => { const i = Math.max(0, Math.min(arr.length - 1, Math.round(wt * 100))); return arr[i]; };
  const blocked = (wt) => d.fades.some(([a, b]) => wt >= a && wt < b);
  const win = d.win, cf = d.clip_from;
  const tA = c.reserve - 0.3;
  return function renderAt(t) {
    // window time: half speed through the narration; real time inside each clip
    let wt, mode = -1;
    win.forEach((w, i) => { if (t >= w.from && t < w.to) { mode = i; wt = cf[i] + (t - w.from); } });
    if (mode < 0) wt = Math.min(5.99, Math.max(0, (t - tA) * 0.5) % 6.0);
    const on = K.prog(t, tA, 0.8);
    const lv = [[S, at(d.small, wt)], [L, at(d.large, wt)]];
    lv.forEach(([T, v], j) => {
      const dim = mode >= 0 && mode !== j ? 0.35 : 1;
      const f = K.clamp(v / T.cap);
      const h = Math.max(0.001, f * T.H);
      T.liq.scale.y = h; T.liq.position.y = -T.H / 2 + h / 2; T.liq.material.opacity = 0.75 * on * dim;
      T.top.position.y = -T.H / 2 + h; T.top.material.opacity = 0.55 * on * dim * (f > 0.01 ? 1 : 0);
      T.g.visible = on > 0.01;
      T.alarm.material.opacity = f < 0.02 && on > 0.5 ? 0.95 * dim * (0.7 + 0.3 * Math.sin(t * 30)) : 0;
    });
    const bl = blocked(wt);
    drops.forEach((m, i) => {
      const ph = ((t * 1.6 + i / 16) % 1);
      const side = i % 2 ? L : S;
      m.position.set(side.g.position.x + Math.sin(i * 2.4) * 0.4, 3.6 - ph * 3.8, Math.cos(i * 2.4) * 0.4);
      m.material.opacity = on * (bl ? 0 : 1) * (1 - ph * 0.3); m.visible = on > 0.01 && !bl;
    });
    K.pin("pl-s", new THREE.Vector3(S.g.position.x, -2.05, 0), cam, env, 0.95 * on);
    K.pin("pl-l", new THREE.Vector3(L.g.position.x, -2.05, 0), cam, env, 0.95 * on);
    const dry = at(d.small, wt) / S.cap < 0.02;
    K.pin("pl-glitch", new THREE.Vector3(S.g.position.x, 2.2, 0), cam, env, dry && on > 0.5 ? 1 : 0);
    const p = K.prog(t, 0, D, K.ease.inOut);
    const ca = K.deg(-16 + 18 * p), cr = env.portrait ? 12.5 : 10.8;
    cam.position.set(Math.sin(ca) * cr, 2.0 - 0.6 * p, Math.cos(ca) * cr);
    cam.lookAt(0, 0.1, 0);
    dust(t);
    r.render(scene, cam);
  };
}
