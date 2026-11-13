// B04 · the player: 150 four-second chunks (ten minutes) over stream.py's sagging, dropping connection.
// Three lanes = three players; each block's height is the rung that player chose; red blocks = a stall.
// The ribbon above is the connection speed (Mbit/s), placed at the chunk being fetched at that moment.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.1 });
  scene.add(new THREE.AmbientLight(0xffffff, 0.55));
  const key = new THREE.DirectionalLight(0xffffff, 1.8); key.position.set(-3, 8, 6); scene.add(key);
  const c = env.cue, D = env.D, Q = env.data.q, BW = env.data.bw, ST = env.data.stalls;
  const N = Q.highest.length, DX = 0.2;
  const dust = K.dust(scene, 240, 18, 0xff3b45, 0.05, 74);
  const LANES = [["highest", 0xe50914, -1.3], ["buffer", 0xf5f5f1, 0], ["throughput", 0x8a8a8a, 1.3]];
  const box = new THREE.BoxGeometry(DX * 0.82, 1, 0.7);
  const lanes = LANES.map(([k, color, z]) => {
    const mat = new THREE.MeshStandardMaterial({ color, emissive: color, emissiveIntensity: 0.25, roughness: 0.35, transparent: true });
    const stallMat = new THREE.MeshStandardMaterial({ color: 0xff2030, emissive: 0xff2030, emissiveIntensity: 1.4, transparent: true });
    const stalls = new Set(ST[k]);
    const blocks = Q[k].map((q, i) => {
      const m = new THREE.Mesh(box, stalls.has(i) ? stallMat : mat);
      const h = 0.18 + q * 0.2; m.userData = { h, q, stall: stalls.has(i) };
      m.position.set(i * DX, h / 2, z); m.scale.y = h; scene.add(m); return m;
    });
    const glows = ST[k].map((i) => { const g = K.glow(0xff2030, 1.4, 0); g.position.set(i * DX, 0.6, z); scene.add(g); return g; });
    return { k, mat, stallMat, blocks, glows, z };
  });
  // connection speed ribbon (Mbit/s), behind the lanes
  const ribbonPts = BW.map(([x, b]) => [x * DX, 1.9 + b * 0.16, -2.6]);     // x = chunk position, b = Mbit/s
  const ribbon = K.tube(ribbonPts, 0.03, 0xffffff, 0.8); scene.add(ribbon);
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(80, 12), new THREE.MeshStandardMaterial({ color: 0x080808, roughness: 0.4, metalness: 0.5 }));
  floor.rotation.x = -Math.PI / 2; floor.position.set(15, 0, 0); scene.add(floor);
  const head = K.glow(0xffffff, 2.4, 0); scene.add(head);
  const ribIdx = ribbon.geometry.index.count;

  return function renderAt(t) {
    // the playhead: chunk index reached by time t (fills ten minutes of chunks between "I streamed" and "Always picking")
    const fill = K.clamp((t - c.streamed) / (c.best - c.streamed + 1.2));
    const pre = K.prog(t, c.chunks, 1.2);                                    // chunks split apart at the start
    const n = Math.floor(N * fill);
    const focus = t >= c.speed - 0.3 ? "throughput" : t >= c.buffer - 0.2 ? "buffer" : t >= c.best - 0.2 ? "highest" : null;
    lanes.forEach((L) => {
      const dimmed = focus && focus !== L.k ? 0.22 : 1;
      L.mat.opacity = dimmed; L.stallMat.opacity = dimmed;
      L.blocks.forEach((m, i) => {
        // before streaming: the first 24 chunks sit as one bar that splits; their height shows "picks a rung"
        let vis = i < n ? 1 : 0, h = m.userData.h;
        if (i < 24 && t < c.streamed) { vis = pre; h = K.lerp(0.5, m.userData.h, K.prog(t, c.picks + i * 0.03, 0.4)); }
        if (i < 24 && t >= c.streamed) vis = 1;
        m.visible = vis > 0.01;
        m.scale.set(1 - 0.18 * (1 - pre), Math.max(0.001, h * vis), 1);
        m.position.y = (h * vis) / 2;
      });
      L.glows.forEach((g, j) => { const i = ST[L.k][j]; g.material.opacity = L.k === "highest" && focus === "highest" && i < n ? 0.75 + 0.25 * Math.sin(t * 7) : 0; });
    });
    ribbon.geometry.setDrawRange(0, Math.floor((ribIdx * Math.max(fill, t < c.streamed ? 0.16 * pre : 0)) / 3) * 3);
    const px = Math.max(24, n) * DX;
    head.position.set(px, 0.6, 0); head.material.opacity = fill > 0 && fill < 1 ? 0.6 : 0;
    // camera: trucks along with the playhead, then pulls back to see all ten minutes
    const back = K.prog(t, c.best - 0.4, 1.8, K.ease.inOut);
    const follow = Math.min(px, 22);
    const cx = K.lerp(follow - 1.5, 14.8, back), cz = K.lerp(8.2, 19.5, back), cy = K.lerp(3.6, 7.2, back);
    cam.position.set(cx - K.lerp(3, 0, back), cy, cz);
    cam.lookAt(K.lerp(follow, 14.8, back), K.lerp(0.8, 0.6, back), -0.3);
    dust(t);
    r.render(scene, cam);
  };
}
