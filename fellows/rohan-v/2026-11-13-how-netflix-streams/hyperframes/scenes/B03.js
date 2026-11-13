// B03 · per title: score vs bitrate for both clips (stream.py's six measured points each), with the VMAF-93 target
// as a glass plane. The clean card crosses it at ~3.9 Mbit/s; the grainy clip never does.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 32, exposure: 1.1 });
  scene.add(new THREE.AmbientLight(0xffffff, 0.8));
  const c = env.cue, D = env.D, L = env.data.ladder, need = env.data.need, target = env.data.target;
  const dust = K.dust(scene, 260, 16, 0xff3b45, 0.05, 73);
  const X = (kb) => -4 + (kb / 6000) * 8, Y = (v) => -2 + (v / 100) * 4.4;
  // axes + grid
  scene.add(K.line([[-4, -2, 0], [4.2, -2, 0]], 0xffffff, 0.35), K.line([[-4, -2, 0], [-4, 2.6, 0]], 0xffffff, 0.35));
  for (const kb of [1000, 2000, 3000, 4000, 5000, 6000]) scene.add(K.line([[X(kb), -2, 0], [X(kb), 2.4, 0]], 0xffffff, 0.06));
  for (const v of [25, 50, 75, 100]) scene.add(K.line([[-4, Y(v), 0], [4.2, Y(v), 0]], 0xffffff, 0.1));
  // the target plane at 93
  const plane = new THREE.Mesh(new THREE.PlaneGeometry(8.4, 2.4), new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0,
    side: THREE.DoubleSide, depthWrite: false }));
  plane.rotation.x = -Math.PI / 2; plane.position.set(0.1, Y(target), 0); scene.add(plane);
  const tline = K.line([[-4, Y(target), 0], [4.2, Y(target), 0]], 0xffffff, 0); scene.add(tline);
  const curve = (clip, color) => {
    const pts = L[clip].map((p) => [X(p.kbps), Y(p.vmaf), 0]);
    const tb = K.tube(pts, 0.035, color, 0); scene.add(tb);
    const dots = pts.map((p) => { const d = K.glow(color, 0.45, 0); d.position.set(...p); scene.add(d); return d; });
    return { tb, dots };
  };
  const A = curve("simple", 0xf5f5f1), B = curve("busy", 0xe50914);
  const hit = K.glow(0xffffff, 1.0, 0); hit.position.set(X(need), Y(target), 0); scene.add(hit);
  const drop = K.line([[X(need), Y(target), 0], [X(need), -2, 0]], 0xffffff, 0); scene.add(drop);
  const miss = K.glow(0xe50914, 1.1, 0); miss.position.set(X(5800), Y(L.busy[5].vmaf), 0); scene.add(miss);
  const reveal = (o, t0) => {
    const g = o.tb.geometry, n = g.index ? g.index.count : 0, p = K.prog(t, t0, 1.6, K.ease.inOut);
    return p;
  };
  let t = 0;

  return function renderAt(tt) {
    t = tt;
    const pa = K.prog(t, c.fit, 1.4, K.ease.inOut), pb = K.prog(t, c.fit + 0.8, 1.4, K.ease.inOut);
    A.tb.material.opacity = pa; B.tb.material.opacity = pb;
    A.tb.geometry.setDrawRange(0, Math.floor(A.tb.geometry.index.count * pa / 3) * 3);
    B.tb.geometry.setDrawRange(0, Math.floor(B.tb.geometry.index.count * pb / 3) * 3);
    A.dots.forEach((d, i) => { d.material.opacity = 0.9 * K.prog(t, c.fit + i * 0.22, 0.4); });
    B.dots.forEach((d, i) => { d.material.opacity = 0.9 * K.prog(t, c.fit + 0.8 + i * 0.22, 0.4); });
    const tg = K.prog(t, c.card - 0.4, 0.8);
    plane.material.opacity = 0.07 * tg; tline.material.opacity = 0.6 * tg;
    hit.material.opacity = K.prog(t, c.card + 0.4, 0.6) * (0.75 + 0.25 * Math.sin(t * 5));
    drop.material.opacity = 0.6 * K.prog(t, c.card + 0.5, 0.6);
    miss.material.opacity = K.prog(t, c.never, 0.6) * (0.7 + 0.3 * Math.sin(t * 5));
    // "since 2015": each title gets its own ladder: rungs light along each curve
    const u = t / D;
    const ca = K.deg(-16 + 26 * K.ease.inOut(u));
    cam.position.set(Math.sin(ca) * 11.5, 1.6 - 0.8 * u, Math.cos(ca) * 11.5);
    cam.lookAt(0, 0.2, 0);
    K.pin("pt", new THREE.Vector3(-2.0, Y(target) + 0.32, 0), cam, env, tg);
    K.pin("pa", new THREE.Vector3(X(4800), Y(L.simple[5].vmaf) + 0.42, 0), cam, env, K.prog(t, c.fit + 1.2, 0.6));   // inside the stage, above the curve
    K.pin("pb", new THREE.Vector3(X(4800), Y(L.busy[5].vmaf) - 0.42, 0), cam, env, K.prog(t, c.fit + 2.0, 0.6));    // below the curve
    K.pin("px", new THREE.Vector3(3.2, -2.35, 0), cam, env, K.prog(t, c.fit, 0.6));
    K.pin("py", new THREE.Vector3(-4.0, 2.85, 0), cam, env, K.prog(t, c.fit, 0.6));
    dust(t);
    r.render(scene, cam);
  };
}
