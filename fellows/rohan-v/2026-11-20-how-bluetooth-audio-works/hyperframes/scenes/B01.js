// B01 · too much data: a wide river of CD-quality data (violet) runs into a narrow Bluetooth link (blue). Before
// "squeezes" it piles up and spills at the mouth; from "squeezes" an SBC ring lights and only 1 in 4.3 particles
// carries on: the same music in under a quarter of the data (bluetooth.py measured 330.7 kbit/s vs 1,411.2).
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.15 });
  K.lights(scene, 0xffffff, 0x224466);
  const c = env.cue, D = env.D, ratio = env.data.ratio;
  scene.add(K.grid(70, 70, 0x2a5a8a, 0.14, -2.6));
  const dust = K.dust(scene, 300, 18, 0x8ac8ff, 0.05, 3);
  // the link: a glass pipe on the right
  const pipe = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.42, 7, 48, 1, true), new THREE.MeshBasicMaterial({ color: 0x3da9ff,
    transparent: true, opacity: 0.12, side: THREE.DoubleSide, depthWrite: false, blending: THREE.AdditiveBlending }));
  pipe.rotation.z = Math.PI / 2; pipe.position.set(4.0, 0, 0); scene.add(pipe);
  const rimA = K.ring(0.42, 0x3da9ff, 0.7, 0.03); rimA.rotation.y = Math.PI / 2; rimA.position.set(0.5, 0, 0); scene.add(rimA);
  const codec = K.ring(1.15, 0x3da9ff, 0, 0.05); codec.rotation.y = Math.PI / 2; codec.position.set(-0.6, 0, 0); scene.add(codec);
  const codecG = K.glow(0x3da9ff, 4.5, 0); codecG.position.set(-0.6, 0, 0); scene.add(codecG);
  // particles: seeded lanes; x advances with t (seek-safe)
  const N = 2600, R = K.rng(1411);
  const base = [];
  for (let i = 0; i < N; i++) {
    const a = R() * Math.PI * 2, rr = Math.sqrt(R());
    base.push({ a, rr, ph: R() * 14, sp: 1.6 + R() * 0.5, keep: R() < 1 / ratio, spill: (R() - 0.5) * 2 });
  }
  const pos = new Float32Array(N * 3), col = new Float32Array(N * 3);
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3)); geo.setAttribute("color", new THREE.BufferAttribute(col, 3));
  const pts = new THREE.Points(geo, new THREE.PointsMaterial({ map: K.glowTex(), size: 0.3, vertexColors: true, transparent: true,
    depthWrite: false, blending: THREE.AdditiveBlending, opacity: 0.95 }));
  pts.frustumCulled = false; scene.add(pts);
  const VIO = new THREE.Color(0xb48cff), BLU = new THREE.Color(0x3da9ff), RED = new THREE.Color(0xff5c6c);
  const X0 = -7.5, LEN = 15;
  return function renderAt(t) {
    const sq = K.prog(t, c.squeeze - 0.2, 1.0, K.ease.inOut);       // 0 = no codec, 1 = SBC on
    codec.material.opacity = 0.85 * sq; codecG.material.opacity = 0.5 * sq * (0.8 + 0.2 * Math.sin(t * 4));
    const on = K.prog(t, 0.1, 1.2);
    for (let i = 0; i < N; i++) {
      const b = base[i];
      let x = X0 + ((b.ph + b.sp * t) % LEN);
      const wide = 1.6 * b.rr;
      let y = Math.sin(b.a) * wide, z = Math.cos(b.a) * wide, cc = VIO, o = on;
      if (x > -0.6) {
        if (sq > 0.5 ? b.keep : false) {          // squeezed: fits the pipe
          const k = K.clamp((x + 0.6) / 1.1);
          y = K.lerp(y, Math.sin(b.a) * 0.32 * b.rr, k); z = K.lerp(z, Math.cos(b.a) * 0.32 * b.rr, k); cc = BLU;
        } else if (sq > 0.5) {
          o = 0;                                  // dropped at the codec: the bits SBC doesn't send
        } else {                                  // no codec: only what fits the mouth gets in; the rest spills
          if (b.rr < 0.26) { cc = VIO; y *= 0.95; z *= 0.95; }
          else { const k = K.clamp((x + 0.6) / 1.2); y += b.spill * k * 2.2 + Math.sin(b.a) * k; z += Math.cos(b.a) * k * 1.4; x = Math.min(x, 0.6 + k * 0.4); cc = RED; o = on * (1 - k); }
        }
      }
      pos[i * 3] = x; pos[i * 3 + 1] = y; pos[i * 3 + 2] = z;
      col[i * 3] = cc.r * o; col[i * 3 + 1] = cc.g * o; col[i * 3 + 2] = cc.b * o;
    }
    geo.attributes.position.needsUpdate = true; geo.attributes.color.needsUpdate = true;
    K.pin("pl-cd", new THREE.Vector3(-5.2, 2.2, 0), cam, env, env.portrait ? 0 : 0.9 * on);   // phone: the stat says CD quality; the label goes (it met "SBC")
    K.pin("pl-link", new THREE.Vector3(4.2, env.portrait ? -0.95 : 1.0, 0), cam, env, 0.9 * K.prog(t, c.more - 0.3, 0.6));
    K.pin("pl-codec", new THREE.Vector3(-0.6, 1.75, 0), cam, env, 0.95 * sq);
    const p = K.prog(t, 0, D, K.ease.inOut);
    const ca = K.deg(-32 + 20 * p), cr = env.portrait ? 15.5 : 13.5;
    cam.position.set(0.4 + Math.sin(ca) * cr, 3.0 - 0.8 * p, Math.cos(ca) * cr);
    cam.lookAt(0.0, -0.1, 0);
    dust(t);
    r.render(scene, cam);
  };
}
