// B06 · scale: about 18,000 Open Connect servers (Dec 2022) light up across the globe in seeded clusters, one per
// country (175); the HUD carries the sourced numbers. Positions are illustrative, not Netflix's real sites.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 32, exposure: 1.1 });
  const c = env.cue, D = env.D;
  const R = 2.6, NS = 18000, NC = 175;
  const globe = new THREE.Group(); scene.add(globe);
  globe.add(K.dotGlobe(R, 4200, 0x8a8a8a, 0.05, 0.6));
  globe.add(new THREE.Mesh(new THREE.SphereGeometry(R * 0.985, 64, 48), new THREE.MeshBasicMaterial({ color: 0x050505 })));
  const rim = K.rimSphere(R * 0.99, 0x050505, 0x7a0a10); rim.userData.core.visible = false; scene.add(rim);
  const dust = K.dust(scene, 220, 18, 0xff3b45, 0.04, 76);
  const Rg = K.rng(18000), cent = [];
  for (let i = 0; i < NC; i++) cent.push([K.lerp(-50, 65, Math.pow(Rg(), 0.9)), K.lerp(-180, 180, Rg()), Rg()]);
  const pos = new Float32Array(NS * 3), col = new Float32Array(NS * 3), born = new Float32Array(NS);
  for (let i = 0; i < NS; i++) {
    const cc = cent[Math.floor(Math.pow(Rg(), 1.6) * NC)];
    const g1 = Rg() + Rg() + Rg() - 1.5, g2 = Rg() + Rg() + Rg() - 1.5;
    const v = K.latlon(cc[0] + g1 * 4.5, cc[1] + g2 * 6, R * 1.004);
    pos[i * 3] = v.x; pos[i * 3 + 1] = v.y; pos[i * 3 + 2] = v.z; born[i] = cc[2] * 0.6 + Rg() * 0.4;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3)); geo.setAttribute("color", new THREE.BufferAttribute(col, 3));
  globe.add(new THREE.Points(geo, new THREE.PointsMaterial({ map: K.glowTex(), size: 0.085, vertexColors: true, transparent: true,
    depthWrite: false, blending: THREE.AdditiveBlending })));
  const red = new THREE.Color(0xe50914), white = new THREE.Color(0xffffff);
  // memberships: a halo ring of light round the globe
  const halo = K.ring(R * 1.35, 0xe50914, 0, 0.012); halo.rotation.x = Math.PI / 2 - 0.3; scene.add(halo);
  const halo2 = K.ring(R * 1.55, 0xffffff, 0, 0.006); halo2.rotation.x = Math.PI / 2 - 0.3; scene.add(halo2);

  return function renderAt(t) {
    const grow = K.clamp((t - c.servers) / 2.4);
    for (let i = 0; i < NS; i++) {
      const a = K.clamp((grow - born[i]) * 6);
      const flash = Math.exp(-Math.pow((grow - born[i]) * 8, 2));
      const k = a * (0.85 + 0.15 * flash);
      const cc = red.clone().lerp(white, flash * 0.8);
      col[i * 3] = cc.r * k; col[i * 3 + 1] = cc.g * k; col[i * 3 + 2] = cc.b * k;
    }
    geo.attributes.color.needsUpdate = true;
    const mv = K.prog(t, c.members - 0.2, 1.2);
    halo.material.opacity = 0.7 * mv; halo2.material.opacity = 0.4 * mv;
    halo.scale.setScalar(0.9 + 0.1 * mv); halo2.scale.setScalar(0.9 + 0.1 * mv);
    halo.rotation.z = t * 0.15; halo2.rotation.z = -t * 0.1;
    globe.rotation.y = K.deg(-20 + 50 * (t / D));
    globe.rotation.x = K.deg(16);
    const pull = K.prog(t, c.av1 - 0.5, 2.5, K.ease.inOut);
    cam.position.set(0, 0.5, (env.portrait ? 9.6 : 9.8) + 1.0 * pull);
    cam.lookAt(0, 0.1, 0);
    dust(t);
    r.render(scene, cam);
  };
}
