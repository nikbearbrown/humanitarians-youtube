// B06 · LE Audio: one source (a phone or TV) broadcasts; rings of light spread across the floor and each pair of
// earbuds lights as a ring reaches it (Auracast: one to any number). Illustration, seeded; no data.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 36, exposure: 1.15 });
  K.lights(scene, 0xffffff, 0x224466);
  const c = env.cue, D = env.D;
  scene.add(K.polarFloor(9, 0x3da9ff, -1.2, 0.16));
  const dust = K.dust(scene, 300, 20, 0x8ac8ff, 0.05, 8);
  const src = K.source(0x3da9ff, 0.28); src.position.set(0, -0.2, 0); scene.add(src);
  const rings = []; for (let i = 0; i < 6; i++) { const m = K.ripple(0x3da9ff, 0.6); m.position.y = -1.18; scene.add(m); rings.push(m); }
  const R = K.rng(2022), buds = [];
  for (let i = 0; i < 64; i++) {
    const a = R() * 6.283, d = 1.8 + Math.sqrt(R()) * 6.6;
    const g = new THREE.Group(); g.position.set(Math.cos(a) * d, -1.0 + R() * 0.25, Math.sin(a) * d); scene.add(g);
    const l = K.glowBox(0.15, 0.24, 0.15, 0xffd166, 0.4), rr = K.glowBox(0.15, 0.24, 0.15, 0xffd166, 0.4);
    l.position.x = -0.13; rr.position.x = 0.13; g.add(l, rr);
    const gl = K.glow(0xffd166, 0.8, 0); g.add(gl);
    buds.push({ g, l, rr, gl, d, ph: R() });
  }
  const P = 1.6, SPD = 4.2;
  return function renderAt(t) {
    const go = K.prog(t, c.auracast - 1.5, 1.0);
    const on = K.prog(t, 0.1, 1.0);
    src.userData.halo.material.opacity = 0.85 * on;
    rings.forEach((m, i) => {
      const age = ((t - i * P / rings.length * rings.length) % (P * rings.length) + P * rings.length) % (P * rings.length);
      const rad = age * SPD * 0.5;
      m.scale.setScalar(Math.max(0.01, rad)); m.material.opacity = go * Math.max(0, 0.95 * (1 - rad / 11));
    });
    buds.forEach((b) => {
      const fade = K.prog(t, 0.3 + b.ph * 1.2, 0.8);
      let hit = 0;
      for (let i = 0; i < rings.length; i++) {
        const age = ((t - i * P) % (P * rings.length) + P * rings.length) % (P * rings.length);
        hit = Math.max(hit, Math.exp(-Math.pow((age * SPD * 0.5 - b.d) / 0.35, 2)));
      }
      const lit = go * (0.35 + 0.65 * hit);
      b.l.material.opacity = b.rr.material.opacity = fade;
      b.l.material.emissiveIntensity = b.rr.material.emissiveIntensity = 0.3 + 2.6 * lit;
      b.gl.material.opacity = 0.9 * go * hit;
    });
    K.pin("pl-src", new THREE.Vector3(0, env.portrait ? 1.6 : 0.55, 0), cam, env, 0.9 * on);
    const p = K.prog(t, 0, D, K.ease.inOut);
    const ca = K.deg(20 + 40 * p), cr = env.portrait ? 15 : 13;
    cam.position.set(Math.sin(ca) * cr, 5.2 - 1.2 * p, Math.cos(ca) * cr);
    cam.lookAt(0, -0.6, 0);
    dust(t);
    r.render(scene, cam);
  };
}
