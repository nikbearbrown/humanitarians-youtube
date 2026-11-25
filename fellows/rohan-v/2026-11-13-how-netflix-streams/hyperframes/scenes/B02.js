// B02 · VMAF: the six rungs' scores as columns, clean test card in front (white), grainy zoom behind (red).
// Heights are stream.py's measured VMAF (libvmaf against the 1080p original).
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 32, exposure: 1.1 });
  scene.add(new THREE.AmbientLight(0xffffff, 0.5));
  const key = new THREE.DirectionalLight(0xffffff, 2.0); key.position.set(4, 8, 6); scene.add(key);
  const c = env.cue, D = env.D, L = env.data.ladder;
  const dust = K.dust(scene, 260, 16, 0xff3b45, 0.05, 72);
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(30, 30), new THREE.MeshStandardMaterial({ color: 0x0a0a0a, roughness: 0.35, metalness: 0.6 }));
  floor.rotation.x = -Math.PI / 2; scene.add(floor);
  const H = 4.2;    // 100 points
  // the 0-100 scale: grid planes at 25/50/75/100
  for (const v of [25, 50, 75, 100]) {
    const ln = K.line([[-3.9, (v / 100) * H, -1.6], [3.9, (v / 100) * H, -1.6]], 0xffffff, v === 100 ? 0.35 : 0.12); scene.add(ln);
  }
  const mk = (clip, z, color, emissive) => L[clip].map((row, i) => {
    const m = new THREE.Mesh(new THREE.BoxGeometry(0.44, 1, 0.44), new THREE.MeshStandardMaterial({ color, emissive, emissiveIntensity: 0.55,
      roughness: 0.3, metalness: 0.1 }));
    m.position.set(-3.1 + i * 1.24, 0, z); scene.add(m);
    const cap = K.glow(emissive, 1.2, 0); scene.add(cap);
    return { m, cap, v: row.vmaf, i };
  });
  const card = mk("simple", 0.6, 0xf5f5f1, 0x6e6e6e), busy = mk("busy", -0.6, 0xe50914, 0xb0060f);
  const setBar = (b, f) => { b.m.visible = f > 0.002; const h = Math.max(0.001, (b.v / 100) * H * f); b.m.scale.y = h; b.m.position.y = h / 2; b.cap.position.set(b.m.position.x, h + 0.05, b.m.position.z); };

  return function renderAt(t) {
    card.forEach((b) => { const t0 = b.i === 0 ? c.lowest - 0.3 : c.lowest + 0.6 + b.i * 0.28; setBar(b, K.prog(t, b.i === 5 ? Math.min(t0, c.top - 0.2) : t0, 0.9, K.ease.expo));
      b.cap.material.opacity = (b.i === 0 || b.i === 5) ? 0.6 * Math.exp(-Math.pow((t - (b.i === 0 ? c.lowest : c.top)) / 0.6, 2)) : 0; });
    busy.forEach((b) => { setBar(b, K.prog(t, c.grain - 0.6 + b.i * 0.12, 0.9, K.ease.expo));
      b.cap.material.opacity = b.i === 5 ? 0.7 * Math.exp(-Math.pow((t - c.grain - 0.6) / 0.6, 2)) : 0; });
    // before the bars: the empty 0-100 scale, the camera sweeping in
    const u = t / D;
    const ca = K.deg(-24 + 30 * K.ease.inOut(u)), cr = (env.portrait ? 13.6 : 14.2) - 1.2 * u;
    cam.position.set(Math.sin(ca) * cr, 3.6 + 0.6 * u, Math.cos(ca) * cr);
    cam.lookAt(0, 1.9, 0);
    const lab = K.prog(t, c.range - 0.2, 0.8);
    card.forEach((b) => K.pin(`pk${b.i}`, new THREE.Vector3(b.m.position.x, -0.05, 1.25), cam, env, lab, 0, 30));
    K.pin("p100", new THREE.Vector3(-4.3, H, -1.6), cam, env, lab);
    K.pin("p50", new THREE.Vector3(-4.3, H / 2, -1.6), cam, env, lab);
    dust(t);
    r.render(scene, cam);
  };
}
