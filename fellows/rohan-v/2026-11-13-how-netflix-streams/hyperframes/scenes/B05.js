// B05 · close by: a far origin server vs an Open Connect box inside your provider. Overnight, popular shows are
// copied out to the boxes; then one chunk's trip, timed at stream.py's model: 1.50 s far, 0.49 s near (real time).
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 32, exposure: 1.1 });
  const c = env.cue, D = env.D, FAR = env.data.far, NEAR = env.data.near;
  const R = 2.6;
  const globe = new THREE.Group(); scene.add(globe);
  globe.add(K.dotGlobe(R, 5200, 0xb3b3b3, 0.06, 0.75));
  const core = new THREE.Mesh(new THREE.SphereGeometry(R * 0.985, 64, 48), new THREE.MeshBasicMaterial({ color: 0x050505 }));
  globe.add(core);
  const rim = K.rimSphere(R * 0.99, 0x050505, 0x7a0a10); rim.userData.core.visible = false; scene.add(rim);
  const dust = K.dust(scene, 220, 18, 0xff3b45, 0.04, 75);
  const home = K.latlon(38, 10, R), origin = K.latlon(30, -95, R);
  const node = (p, color, size) => { const g = K.glow(color, size, 0); g.position.copy(p); globe.add(g); return g; };
  const gHome = node(home, 0xffffff, 0.7), gOrigin = node(origin, 0xb3b3b3, 1.0);
  const isp = K.latlon(45, 17, R * 1.002), gIsp = node(isp, 0xe50914, 0.9);
  // the other provider boxes around the world (seeded)
  const Rg = K.rng(5), boxes = [];
  for (let i = 0; i < 26; i++) { const p = K.latlon(K.lerp(-40, 60, Rg()), K.lerp(-180, 180, Rg()), R * 1.002); boxes.push({ p, g: node(p, 0xe50914, 0.5), d: Rg() }); }
  const mkArc = (A, B, lift, color) => { const pts = K.arcPts(A, B, R, lift, 80); const tb = K.tube(pts.map((v) => [v.x, v.y, v.z]), 0.012, color, 0); globe.add(tb); return { tb, pts }; };
  const farArc = mkArc(origin, home, 1.3, 0xb3b3b3), nearArc = mkArc(isp, home, 0.25, 0xe50914);
  const fill = boxes.map((b) => mkArc(origin, b.p, 0.9 + b.d * 0.6, 0xe50914));
  const pkF = K.glow(0xffffff, 0.5, 0), pkN = K.glow(0xff4a52, 0.5, 0); globe.add(pkF, pkN);
  const draw = (a, p) => a.tb.geometry.setDrawRange(0, Math.floor((a.tb.geometry.index.count * K.clamp(p)) / 3) * 3);

  return function renderAt(t) {
    gHome.material.opacity = K.prog(t, 0.2, 0.8); gOrigin.material.opacity = 0.9 * K.prog(t, 0.6, 0.8);
    gIsp.material.opacity = K.prog(t, c.inside - 0.2, 0.6) * (0.8 + 0.2 * Math.sin(t * 4));
    boxes.forEach((b) => { b.g.material.opacity = 0.8 * K.prog(t, c.open + b.d * 1.4, 0.5); });
    // overnight fill: copies travel from the origin to every box
    fill.forEach((a, i) => { const p = K.prog(t, c.overnight + boxes[i].d * 1.6, 1.0, K.ease.inOut); draw(a, p);
      a.tb.material.opacity = 0.55 * p * (1 - K.prog(t, c.far - 0.6, 0.8)); });
    // the timed trips (real seconds)
    const fp = K.clamp((t - c.far) / FAR), np = K.clamp((t - c.near) / NEAR);
    draw(farArc, Math.max(fp, t > c.far ? 0.001 : 0)); farArc.tb.material.opacity = t > c.far - 0.3 ? 0.8 : 0;
    draw(nearArc, np); nearArc.tb.material.opacity = t > c.near - 0.3 ? 0.95 : 0;
    const fi = Math.min(80, Math.floor(fp * 80)), ni = Math.min(80, Math.floor(np * 80));
    pkF.position.copy(farArc.pts[fi]); pkF.material.opacity = t > c.far && fp < 1 ? 1 : 0;
    pkN.position.copy(nearArc.pts[ni]); pkN.material.opacity = t > c.near && np < 1 ? 1 : 0;
    K.setText("far-n", (t > c.far ? Math.min(FAR, t - c.far) : 0).toFixed(2));
    K.setText("near-n", (t > c.near ? Math.min(NEAR, t - c.near) : 0).toFixed(2));
    // slow spin; the home side turns toward the camera for the trips
    globe.rotation.y = K.deg(-40 + 30 * K.ease.inOut(t / D));
    globe.rotation.x = K.deg(18);
    cam.position.set(0, 0.6, env.portrait ? 9.4 : 9.6);
    cam.lookAt(0, 0.2, 0);
    globe.updateMatrixWorld();
    const W = (v) => v.clone().applyMatrix4(globe.matrixWorld).multiplyScalar(1.08);
    K.pin("pyou", W(home), cam, env, K.prog(t, 0.4, 0.8), 0, 46);
    K.pin("pfar", W(origin), cam, env, K.prog(t, 0.8, 0.8), 0, -36);
    K.pin("pisp", W(isp), cam, env, K.prog(t, c.inside, 0.6), 0, -46);
    dust(t);
    r.render(scene, cam);
  };
}
