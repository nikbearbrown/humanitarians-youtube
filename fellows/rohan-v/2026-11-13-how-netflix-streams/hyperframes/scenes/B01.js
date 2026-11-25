// B01 · the ladder: one show stored six times. Each pane is a real frame of stream.py's encode at that rung
// (evidence/rungs/*.png), sized by its resolution; the stack rises from 235 kbit/s to 5,800 kbit/s.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 30, exposure: 1.05 });
  scene.add(new THREE.AmbientLight(0xffffff, 1.0));
  const c = env.cue, D = env.D, rungs = env.data.rungs, lad = env.data.ladder.simple;
  const dust = K.dust(scene, 300, 16, 0xff3b45, 0.05, 71);
  const panes = rungs.map((kb, i) => {
    const w = 1.3 + 2.2 * (lad[i].w / 1920), h = w * 9 / 16;
    const tA = K.imgTex(`rung-simple-${kb}`), tB = K.imgTex(`rung-busy-${kb}`);
    const mA = new THREE.MeshBasicMaterial({ map: tA, transparent: true, opacity: 0, toneMapped: false });
    const mB = new THREE.MeshBasicMaterial({ map: tB, transparent: true, opacity: 0, toneMapped: false });
    const g = new THREE.Group();
    const a = new THREE.Mesh(new THREE.PlaneGeometry(w, h), mA), b = new THREE.Mesh(new THREE.PlaneGeometry(w, h), mB);
    b.position.z = 0.002;
    const edge = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.PlaneGeometry(w * 1.02, h * 1.03)),
      new THREE.LineBasicMaterial({ color: i === 5 ? 0xe50914 : 0xffffff, transparent: true, opacity: 0 }));
    const glow = K.glow(0xe50914, w * 1.6, 0); glow.position.z = -0.05;
    g.add(glow, a, b, edge);
    // a staircase: each rung higher, further back and to the right
    g.position.set(-3.4 + i * 1.3, -1.7 + i * 0.66, -i * 1.5);
    g.rotation.y = -0.38;
    scene.add(g);
    return { g, mA, mB, edge, glow, tA, tB, w, i };
  });
  // the rail that joins the rungs
  const rail = K.tube(panes.map((p) => [p.g.position.x - p.w * 0.5, p.g.position.y - p.w * 0.29, p.g.position.z]), 0.012, 0xe50914, 0);
  scene.add(rail);

  return function renderAt(t) {
    const busy = K.prog(t, c.grainy - 0.1, 0.8, K.ease.inOut);
    panes.forEach((p) => {
      p.tA.userData.ready(); p.tB.userData.ready();
      const on = K.prog(t, c.stored + p.i * 0.32, 0.9, K.ease.expo);
      p.mA.opacity = on * (1 - busy); p.mB.opacity = on * busy;
      const hi = Math.exp(-Math.pow((t - (c.ladder + 0.5 + p.i * 0.35)) / 0.35, 2));    // a pulse climbs the ladder
      const six = Math.exp(-Math.pow((t - c.six - 0.2) / 0.4, 2));
      p.edge.material.opacity = on * (0.35 + 0.65 * Math.max(hi, six));
      p.glow.material.opacity = (p.i === 5 ? 0.35 * on : 0) + 0.5 * Math.max(hi, six) * on;
      p.g.position.y = -1.7 + p.i * 0.66 + (1 - on) * -0.6;
    });
    rail.material.opacity = 0.7 * K.prog(t, c.ladder, 1.2);
    const u = t / D;
    cam.position.set(-1.6 + 2.4 * u, 1.0 + 0.5 * u, (env.portrait ? 11.8 : 12.4) - 1.4 * u);
    cam.lookAt(0.0, 0.2, -3.6);
    dust(t);
    r.render(scene, cam);
  };
}
