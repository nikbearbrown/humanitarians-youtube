// B06 · your ears: three outer ears, each a different shape (seeded point clouds: rim, inner fold, bowl, lobe);
// then a phone's depth camera sweeps one ear and builds its point cloud (Personalized Spatial Audio, iOS 16).
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 32, exposure: 1.2 });
  K.lights(scene, 0xffffff, 0x404a99);
  const c = env.cue, D = env.D;
  const dust = K.dust(scene, 260, 14, 0x8a9bff, 0.05, 61);

  function ear(seed, p) {     // an outer ear as ~3200 points in a local frame (y up, z toward the viewer)
    const R = K.rng(seed), out = [];
    const add = (x, y, z, k) => out.push([x, y, z, k]);
    for (let i = 0; i < 1300; i++) {          // the rim (helix): a C from the top round the back to the lobe
      const a = K.lerp(-0.35, 3.75, R()), w = p.rimW * (0.6 + 0.4 * R());
      const rx = p.w * (1 + 0.08 * Math.sin(a * 2 + p.ph)), ry = p.h;
      const x = Math.cos(a + Math.PI / 2) * rx * -1, y = Math.sin(a + Math.PI / 2) * ry;
      const nx = x / rx, ny = y / ry, tt = (R() - 0.5) * 2;
      add(x + nx * w * tt * 0.5, y + ny * w * tt * 0.5, 0.18 + (R() - 0.5) * 0.14, 0);
    }
    for (let i = 0; i < 700; i++) {           // the inner fold (antihelix)
      const a = K.lerp(0.2, 2.6, R());
      const x = -Math.cos(a + Math.PI / 2) * p.w * 0.62 + 0.05, y = Math.sin(a + Math.PI / 2) * p.h * 0.6 + 0.1;
      add(x + (R() - 0.5) * 0.08, y + (R() - 0.5) * 0.08, 0.12 + (R() - 0.5) * 0.1, 1);
    }
    for (let i = 0; i < 800; i++) {           // the bowl (concha)
      const a = R() * Math.PI * 2, rr = Math.sqrt(R());
      const x = Math.cos(a) * rr * p.cw + 0.12, y = Math.sin(a) * rr * p.cw * 1.15 - 0.05;
      add(x, y, -0.22 * (1 - rr * rr), 2);
    }
    for (let i = 0; i < 420; i++) {           // the lobe
      const a = R() * Math.PI * 2, rr = Math.sqrt(R());
      add(Math.cos(a) * rr * p.lobe * 0.8 - 0.05, -p.h * 0.92 + Math.sin(a) * rr * p.lobe, 0.12 + (R() - 0.5) * 0.08, 3);
    }
    return out;
  }
  const SH = [{ w: 0.62, h: 1.0, rimW: 0.2, cw: 0.26, lobe: 0.26, ph: 0.3 }, { w: 0.7, h: 1.08, rimW: 0.26, cw: 0.32, lobe: 0.18, ph: 1.6 },
    { w: 0.56, h: 0.94, rimW: 0.16, cw: 0.24, lobe: 0.32, ph: 2.6 }];
  const COL = [new THREE.Color(0xc39bff), new THREE.Color(0x5ce1ff), new THREE.Color(0xffb454)];
  const clouds = SH.map((p, k) => {
    const e = ear(100 + k * 17, p), n = e.length;
    const pos = new Float32Array(n * 3), col = new Float32Array(n * 3);
    e.forEach((q, i) => { pos[i * 3] = q[0]; pos[i * 3 + 1] = q[1]; pos[i * 3 + 2] = q[2]; });
    const geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.BufferAttribute(pos, 3)); geo.setAttribute("color", new THREE.BufferAttribute(col, 3));
    const m = new THREE.Points(geo, new THREE.PointsMaterial({ map: K.glowTex(), size: 0.07, vertexColors: true, transparent: true,
      depthWrite: false, blending: THREE.AdditiveBlending }));
    const g = new THREE.Group(); g.add(m); scene.add(g);
    return { g, geo, col, e, n };
  });
  // the phone: a dark rounded slab with a camera notch, facing the centre ear
  const phone = new THREE.Group();
  const body = new THREE.Mesh(new THREE.BoxGeometry(1.0, 2.05, 0.08), new THREE.MeshPhysicalMaterial({ color: 0x23263f, metalness: 0.5,
    roughness: 0.3, clearcoat: 1, emissive: 0x0b0d22 }));
  const rim = new THREE.Mesh(new THREE.BoxGeometry(1.05, 2.1, 0.06), new THREE.MeshStandardMaterial({ color: 0xc4c9e8, metalness: 0.8, roughness: 0.25,
    emissive: 0x4a4f78, emissiveIntensity: 0.8 }));
  const lens = K.glow(0x5ce1ff, 0.5, 0.9); lens.position.set(0, 0.93, -0.08);
  phone.add(lens);
  const notch = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.07, 0.01), new THREE.MeshBasicMaterial({ color: 0x000000 }));
  notch.position.set(0, 0.93, -0.046);
  phone.add(rim, body, notch); scene.add(phone);
  // the scan plane (a sheet of dots sweeping across the ear)
  const scanPlane = new THREE.Mesh(new THREE.PlaneGeometry(0.02, 2.8), new THREE.MeshBasicMaterial({ color: 0x5ce1ff, transparent: true,
    opacity: 0, blending: THREE.AdditiveBlending, depthWrite: false }));
  scene.add(scanPlane);
  const scanGlow = K.glow(0x5ce1ff, 2.4, 0); scene.add(scanGlow);
  const white = new THREE.Color(0xffffff), dim = new THREE.Color(0x2b3380);

  return function renderAt(t) {
    const u = t / D;
    const solo = K.prog(t, c.mixup + 0.6, 1.6, K.ease.inOut);       // side ears leave; the centre ear comes forward
    const scanning = K.clamp((t - c.scan) / 2.8);                    // 0..1 sweep across the ear (left -> right)
    clouds.forEach((cl, k) => {
      const side = k - 1;
      cl.g.position.set(side * K.lerp(2.3, 4.2, solo), 0, side === 0 ? K.lerp(0, 0.9, solo) : 0);
      cl.g.rotation.y = side * 0.25 + Math.sin(t * 0.5 + k) * 0.18 + (side === 0 ? K.lerp(0, -0.25, solo) : 0);
      const vis = side === 0 ? 1 : 1 - solo;
      const born = K.prog(t, 0.2 + k * 0.35, 1.0);
      for (let i = 0; i < cl.n; i++) {
        const q = cl.e[i];
        let cc;
        if (side === 0 && t > c.scan) {
          const xs = K.lerp(-0.9, 0.9, scanning);
          const got = q[0] < xs ? 1 : 0, edge = Math.exp(-Math.pow((q[0] - xs) / 0.05, 2));
          cc = dim.clone().lerp(COL[1], got * 0.85).lerp(white, edge);
        } else {
          cc = COL[k].clone();
        }
        cc.multiplyScalar(vis * born);
        cl.col[i * 3] = cc.r; cl.col[i * 3 + 1] = cc.g; cl.col[i * 3 + 2] = cc.b;
      }
      cl.geo.attributes.color.needsUpdate = true;
      cl.g.visible = vis > 0.01;
    });
    // phone slides in at "scans", scanning plane sweeps
    const ph = K.prog(t, c.scan - 1.0, 1.0, K.ease.inOut);
    phone.position.set(K.lerp(4.2, 1.75, ph), 0.15, 1.6); phone.rotation.set(0, 0.5, 0.05);
    phone.visible = ph > 0.001;
    const sv = t > c.scan && scanning < 1 ? 1 : 0;
    const center = clouds[1].g;
    const xs = K.lerp(-0.9, 0.9, scanning);
    const sp = new THREE.Vector3(xs, 0, 0.1).applyMatrix4(center.matrixWorld);
    scanPlane.position.copy(sp); scanPlane.rotation.y = center.rotation.y; scanPlane.material.opacity = 0.7 * sv;
    scanGlow.position.copy(sp); scanGlow.material.opacity = 0.5 * sv;
    cam.position.set(Math.sin(K.deg(-8 + 10 * u)) * 7.2, 0.6 - 0.3 * u, Math.cos(K.deg(-8 + 10 * u)) * K.lerp(7.6, 5.6, solo));
    cam.lookAt(0, -0.05, 0);
    scene.updateMatrixWorld();
    dust(t);
    r.render(scene, cam);
  };
}
