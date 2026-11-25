// B03 · codecs: one glass pipe per codec, its flow of light proportional to its data rate (SBC, AAC, aptX measured
// by bluetooth.py with ffmpeg's encoders; LDAC's 990 is Sony's top setting, drawn dashed-thin as "up to").
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.15 });
  K.lights(scene, 0xffffff, 0x224466);
  const c = env.cue, D = env.D, rows = env.data.rows;
  scene.add(K.grid(70, 70, 0x2a5a8a, 0.14, -2.8));
  const dust = K.dust(scene, 260, 18, 0x8ac8ff, 0.05, 5);
  const COL = [0x3da9ff, 0xe8eef5, 0xffd166, 0xb48cff];
  const CUE = [c.sbc, c.aac, c.aptx, c.ldac];
  const L = 9, X0 = -4.5;
  const lanes = rows.map(([name, kbps], i) => {
    const y = 1.65 - i * 1.1;
    const rad = 0.12 + 0.3 * Math.sqrt(kbps / 990);
    const pipe = new THREE.Mesh(new THREE.CylinderGeometry(rad, rad, L, 48, 1, true), new THREE.MeshBasicMaterial({ color: COL[i],
      transparent: true, opacity: 0, side: THREE.DoubleSide, depthWrite: false, blending: THREE.AdditiveBlending }));
    pipe.rotation.z = Math.PI / 2; pipe.position.set(0, y, -i * 0.3); scene.add(pipe);
    const n = Math.round(kbps / 5), R = K.rng(100 + i), base = [];
    for (let k = 0; k < n; k++) base.push({ a: R() * 6.283, rr: Math.sqrt(R()) * rad * 0.8, ph: R() * L, sp: 1.2 + R() * 0.4 });
    const pos = new Float32Array(n * 3);
    const geo = new THREE.BufferGeometry(); geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    const pts = new THREE.Points(geo, new THREE.PointsMaterial({ map: K.glowTex(), color: COL[i], size: 0.12, transparent: true, opacity: 0,
      depthWrite: false, blending: THREE.AdditiveBlending }));
    pts.frustumCulled = false; scene.add(pts);
    return { y, z: -i * 0.3, rad, pipe, pts, pos, geo, base, n, name };
  });
  return function renderAt(t) {
    lanes.forEach((ln, i) => {
      const on = K.prog(t, CUE[i] - 0.3, 0.7);
      ln.pipe.material.opacity = 0.13 * on; ln.pts.material.opacity = 0.95 * on;
      for (let k = 0; k < ln.n; k++) {
        const b = ln.base[k], x = X0 + ((b.ph + b.sp * t) % L);
        ln.pos[k * 3] = x; ln.pos[k * 3 + 1] = ln.y + Math.sin(b.a) * b.rr; ln.pos[k * 3 + 2] = ln.z + Math.cos(b.a) * b.rr;
      }
      ln.geo.attributes.position.needsUpdate = true;
      K.pin("pl-" + ln.name.toLowerCase(), new THREE.Vector3(X0 + 1.0, ln.y + ln.rad + 0.22, ln.z), cam, env, 0.95 * on);
    });
    const p = K.prog(t, 0, D, K.ease.inOut);
    const ca = K.deg(-24 + 20 * p), cr = env.portrait ? 13.5 : 11.6;
    cam.position.set(1.0 + Math.sin(ca) * cr, 1.8 - 0.4 * p, Math.cos(ca) * cr);
    cam.lookAt(0.6, 0.1, -0.4);
    dust(t);
    r.render(scene, cam);
  };
}
