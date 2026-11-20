// kit3.js — shared three.js helpers for the week-12 HyperFrames films.
// Every frame is drawn from timeline time alone (HyperFrames seeks each frame independently): no clocks, no
// requestAnimationFrame, seeded randomness only.
import * as THREE from "./three.module.min.js";
export { THREE };

export function rng(seed) {            // mulberry32
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lerp = (a, b, t) => a + (b - a) * t;
export const ease = {
  inOut: (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
  out: (t) => 1 - Math.pow(1 - t, 3),
  expo: (t) => (t >= 1 ? 1 : 1 - Math.pow(2, -10 * t)),
  back: (t) => { const c = 1.9; return 1 + (c + 1) * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2); },
};
// progress of an event that starts at t0 and lasts dur, eased
export const prog = (t, t0, dur = 0.8, e = ease.out) => e(clamp((t - t0) / dur));

export function setup(canvas, w, h, opts = {}) {
  const r = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true, alpha: true });
  r.setPixelRatio(1);
  r.setSize(w, h, false);
  r.setClearColor(0x000000, 0);
  r.outputColorSpace = THREE.SRGBColorSpace;
  r.toneMapping = THREE.ACESFilmicToneMapping;
  r.toneMappingExposure = opts.exposure || 1.15;
  const scene = new THREE.Scene();
  if (opts.fog) scene.fog = new THREE.FogExp2(opts.fog, opts.fogDensity || 0.035);
  const cam = new THREE.PerspectiveCamera(opts.fov || 38, w / h, 0.1, 400);
  return { r, scene, cam };
}

// a soft round glow texture for sprites and particles
let _glow = null;
export function glowTex() {
  if (_glow) return _glow;
  const c = document.createElement("canvas"); c.width = c.height = 256;
  const g = c.getContext("2d");
  const grd = g.createRadialGradient(128, 128, 0, 128, 128, 128);
  grd.addColorStop(0, "rgba(255,255,255,1)"); grd.addColorStop(0.2, "rgba(255,255,255,0.75)");
  grd.addColorStop(0.5, "rgba(255,255,255,0.18)"); grd.addColorStop(1, "rgba(255,255,255,0)");
  g.fillStyle = grd; g.fillRect(0, 0, 256, 256);
  _glow = new THREE.CanvasTexture(c); _glow.colorSpace = THREE.SRGBColorSpace;
  return _glow;
}

export function glow(color, size, opacity = 1) {
  const m = new THREE.SpriteMaterial({ map: glowTex(), color, transparent: true, opacity, depthWrite: false,
    blending: THREE.AdditiveBlending });
  const s = new THREE.Sprite(m); s.scale.set(size, size, 1);
  return s;
}

// drifting dust: a seeded point cloud that only depends on t
export function dust(scene, n, radius, color, size, seed = 7) {
  const R = rng(seed), pos = new Float32Array(n * 3), base = [];
  for (let i = 0; i < n; i++) {
    const u = R() * 2 - 1, th = R() * Math.PI * 2, rr = radius * Math.cbrt(R());
    const s = Math.sqrt(1 - u * u);
    base.push([rr * s * Math.cos(th), rr * u, rr * s * Math.sin(th), R() * 6.28]);
  }
  const geo = new THREE.BufferGeometry(); geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const mat = new THREE.PointsMaterial({ map: glowTex(), color, size, transparent: true, opacity: 0.7, depthWrite: false,
    blending: THREE.AdditiveBlending, sizeAttenuation: true });
  const pts = new THREE.Points(geo, mat); scene.add(pts);
  return function update(t) {
    for (let i = 0; i < n; i++) {
      const b = base[i];
      pos[i * 3] = b[0] + Math.sin(t * 0.15 + b[3]) * 0.4;
      pos[i * 3 + 1] = b[1] + Math.cos(t * 0.12 + b[3]) * 0.3;
      pos[i * 3 + 2] = b[2];
    }
    geo.attributes.position.needsUpdate = true;
  };
}

// a glassy sphere with a fresnel rim: the textbook "spherical head" (never a person: a sphere with two ears)
export function rimSphere(radius, color, rimColor) {
  const g = new THREE.Group();
  const core = new THREE.Mesh(new THREE.SphereGeometry(radius, 96, 64),
    new THREE.MeshPhysicalMaterial({ color, roughness: 0.25, metalness: 0.1, clearcoat: 1, clearcoatRoughness: 0.2,
      transparent: true, opacity: 0.92 }));
  const rim = new THREE.Mesh(new THREE.SphereGeometry(radius * 1.04, 96, 64), new THREE.ShaderMaterial({
    uniforms: { c: { value: new THREE.Color(rimColor) }, p: { value: 2.6 }, k: { value: 1.0 } },
    vertexShader: "varying vec3 vN; varying vec3 vV; void main(){ vec4 mv = modelViewMatrix*vec4(position,1.0); vN = normalize(normalMatrix*normal); vV = normalize(-mv.xyz); gl_Position = projectionMatrix*mv; }",
    fragmentShader: "uniform vec3 c; uniform float p; uniform float k; varying vec3 vN; varying vec3 vV; void main(){ float f = pow(1.0-abs(dot(vN,vV)), p)*k; gl_FragColor = vec4(c*f, f); }",
    transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.FrontSide }));
  g.add(core); g.add(rim);
  g.userData = { core, rim };
  return g;
}

// an expanding wavefront shell
export function shell(color, opacity = 0.35) {
  return new THREE.Mesh(new THREE.SphereGeometry(1, 64, 32), new THREE.MeshBasicMaterial({ color, transparent: true,
    opacity, depthWrite: false, blending: THREE.AdditiveBlending, wireframe: false, side: THREE.DoubleSide }));
}

export function ring(radius, color, opacity = 0.5, width = 0.02) {
  return new THREE.Mesh(new THREE.RingGeometry(radius - width, radius + width, 160), new THREE.MeshBasicMaterial({ color,
    transparent: true, opacity, side: THREE.DoubleSide, depthWrite: false, blending: THREE.AdditiveBlending }));
}

export function line(points, color, opacity = 1) {
  const g = new THREE.BufferGeometry().setFromPoints(points.map((p) => new THREE.Vector3(...p)));
  return new THREE.Line(g, new THREE.LineBasicMaterial({ color, transparent: true, opacity, blending: THREE.AdditiveBlending }));
}

export function tube(points, radius, color, opacity = 1) {
  const curve = new THREE.CatmullRomCurve3(points.map((p) => new THREE.Vector3(...p)));
  const m = new THREE.Mesh(new THREE.TubeGeometry(curve, 200, radius, 12, false), new THREE.MeshBasicMaterial({ color,
    transparent: true, opacity, blending: THREE.AdditiveBlending, depthWrite: false }));
  m.userData.curve = curve;
  return m;
}

export function lights(scene, key = 0xffffff, fill = 0x5577aa) {
  scene.add(new THREE.AmbientLight(fill, 0.9));
  const k = new THREE.DirectionalLight(key, 2.2); k.position.set(4, 6, 5); scene.add(k);
  const r = new THREE.DirectionalLight(0x88aaff, 1.2); r.position.set(-5, 2, -4); scene.add(r);
  return k;
}

// hook into HyperFrames' seek protocol
export function drive(renderAt) {
  window.addEventListener("hf-seek", (e) => renderAt(e.detail.time));
  renderAt(0);
}

// ---------------------------------------------------------------- spatial-audio helpers
// azimuth convention (matches spatial.py): theta 0 = straight ahead (-z), +theta = to the right (+x)
export function az(theta, r, y = 0) { return new THREE.Vector3(r * Math.sin(theta), y, -r * Math.cos(theta)); }
export const deg = (d) => (d * Math.PI) / 180;

// the textbook spherical head: a glass sphere, two ears, a small nose so you can see which way it faces
export function headModel(o = {}) {
  const g = new THREE.Group();
  const s = rimSphere(1, o.color || 0x1e2468, o.rim || 0x9aa8ff);
  s.userData.core.material.emissive = new THREE.Color(o.glowc || 0x05072a);
  s.userData.rim.material.uniforms.k.value = 1.7;
  g.add(s);
  const wire = new THREE.Mesh(new THREE.SphereGeometry(1.012, 24, 16), new THREE.MeshBasicMaterial({ color: o.rim || 0x9aa8ff,
    wireframe: true, transparent: true, opacity: 0.07, depthWrite: false, blending: THREE.AdditiveBlending }));
  g.add(wire);
  const earMat = (c) => new THREE.MeshStandardMaterial({ color: c, emissive: c, emissiveIntensity: 0.6, roughness: 0.4 });
  const earL = new THREE.Mesh(new THREE.SphereGeometry(1, 32, 24), earMat(o.left || 0xc39bff));
  const earR = new THREE.Mesh(new THREE.SphereGeometry(1, 32, 24), earMat(o.right || 0x5ce1ff));
  earL.scale.set(0.1, 0.24, 0.16); earR.scale.set(0.1, 0.24, 0.16);
  earL.position.set(-1.02, 0, 0.02); earR.position.set(1.02, 0, 0.02);
  g.add(earL, earR);
  const glowL = glow(o.left || 0xc39bff, 0.9, 0); glowL.position.copy(earL.position);
  const glowR = glow(o.right || 0x5ce1ff, 0.9, 0); glowR.position.copy(earR.position);
  g.add(glowL, glowR);
  const nose = new THREE.Mesh(new THREE.ConeGeometry(0.13, 0.34, 24),
    new THREE.MeshStandardMaterial({ color: o.nose || 0xdfe3ff, emissive: o.nose || 0xdfe3ff, emissiveIntensity: 0.35, roughness: 0.5 }));
  nose.rotation.x = -Math.PI / 2; nose.position.set(0, -0.05, -1.08);
  g.add(nose);
  return { g, wire, sphere: s, earL, earR, glowL, glowR, nose };
}

// floor of concentric rings + spokes every 30 degrees (reads as "directions around you")
export function polarFloor(radius, color, y = -1.25, opacity = 0.22) {
  const g = new THREE.Group();
  const mat = new THREE.LineBasicMaterial({ color, transparent: true, opacity, depthWrite: false });
  for (let k = 1; k <= 4; k++) {
    const r = (radius * k) / 4, pts = [];
    for (let i = 0; i <= 160; i++) { const a = (i / 160) * Math.PI * 2; pts.push(new THREE.Vector3(r * Math.cos(a), y, r * Math.sin(a))); }
    g.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), mat));
  }
  for (let i = 0; i < 12; i++) {
    const a = (i / 12) * Math.PI * 2;
    g.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(Math.cos(a) * 1.3, y, Math.sin(a) * 1.3),
      new THREE.Vector3(Math.cos(a) * radius, y, Math.sin(a) * radius)]), mat));
  }
  return g;
}

// a sound source: bright core + halo (+ optional point light)
export function source(color, size = 0.22, withLight = true) {
  const g = new THREE.Group();
  const core = new THREE.Mesh(new THREE.SphereGeometry(size, 32, 24), new THREE.MeshBasicMaterial({ color }));
  const halo = glow(color, size * 9, 0.85);
  g.add(core, halo);
  let light = null;
  if (withLight) { light = new THREE.PointLight(color, 6, 9, 1.6); g.add(light); }
  g.userData = { core, halo, light };
  return g;
}

// a horizontal ripple ring (scale = radius)
export function ripple(color, opacity = 0.6) {
  const m = new THREE.Mesh(new THREE.RingGeometry(0.985, 1, 192), new THREE.MeshBasicMaterial({ color, transparent: true, opacity,
    side: THREE.DoubleSide, depthWrite: false, blending: THREE.AdditiveBlending }));
  m.rotation.x = -Math.PI / 2;
  return m;
}

// a polyline trail that can be rewritten each frame
export function trail(n, color, opacity = 0.9) {
  const pos = new Float32Array(n * 3), col = new Float32Array(n * 3);
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  geo.setAttribute("color", new THREE.BufferAttribute(col, 3));
  const c = new THREE.Color(color);
  const ln = new THREE.Line(geo, new THREE.LineBasicMaterial({ vertexColors: true, transparent: true, opacity,
    blending: THREE.AdditiveBlending, depthWrite: false }));
  ln.userData.set = function (pts) {      // pts: array of Vector3, oldest first; fades toward the oldest
    const m = Math.min(n, pts.length);
    for (let i = 0; i < n; i++) {
      const p = pts[Math.min(i, m - 1)] || new THREE.Vector3();
      pos[i * 3] = p.x; pos[i * 3 + 1] = p.y; pos[i * 3 + 2] = p.z;
      const f = m > 1 ? Math.min(i, m - 1) / (m - 1) : 1;
      col[i * 3] = c.r * f; col[i * 3 + 1] = c.g * f; col[i * 3 + 2] = c.b * f;
    }
    geo.setDrawRange(0, m);
    geo.attributes.position.needsUpdate = true; geo.attributes.color.needsUpdate = true;
  };
  return ln;
}

export function setText(id, s) { const e = document.getElementById(id); if (e && e.textContent !== s) e.textContent = s; }
export function setAttr(id, k, v) { const e = document.getElementById(id); if (e) e.setAttribute(k, v); }
export function setStyle(id, k, v) { const e = document.getElementById(id); if (e) e.style[k] = v; }
export function fade(obj, o) { obj.traverse((m) => { if (m.material) { m.material.transparent = true; if (m.userData.o0 === undefined) m.userData.o0 = m.material.opacity; m.material.opacity = m.userData.o0 * o; } }); obj.visible = o > 0.002; }

// a texture from an <img> already in the page (HyperFrames waits for page images before capturing)
export function imgTex(id) {
  const img = document.getElementById(id);
  const tex = new THREE.Texture(img); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
  tex.userData.ready = function () { if (!tex.userData.ok && img && img.complete && img.naturalWidth) { tex.needsUpdate = true; tex.userData.ok = true; } };
  tex.userData.ready();
  return tex;
}

// a dot globe (no coastlines: an abstract sphere of points)
export function dotGlobe(radius, n, color, size = 0.05, opacity = 0.55) {
  const pos = new Float32Array(n * 3);
  for (let i = 0; i < n; i++) {
    const y = 1 - (i + 0.5) / n * 2, rr = Math.sqrt(1 - y * y), ph = i * Math.PI * (3 - Math.sqrt(5));
    pos[i * 3] = Math.cos(ph) * rr * radius; pos[i * 3 + 1] = y * radius; pos[i * 3 + 2] = Math.sin(ph) * rr * radius;
  }
  const geo = new THREE.BufferGeometry(); geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  return new THREE.Points(geo, new THREE.PointsMaterial({ map: glowTex(), color, size, transparent: true, opacity, depthWrite: false,
    blending: THREE.AdditiveBlending }));
}
export function latlon(lat, lon, r) {
  const a = deg(lat), b = deg(lon);
  return new THREE.Vector3(r * Math.cos(a) * Math.cos(b), r * Math.sin(a), -r * Math.cos(a) * Math.sin(b));
}
// a great-circle-ish arc lifted off the sphere
export function arcPts(A, B, r, lift, n = 64) {
  const pts = [];
  for (let i = 0; i <= n; i++) {
    const t = i / n, p = A.clone().normalize().lerp(B.clone().normalize(), t).normalize();
    pts.push(p.multiplyScalar(r + lift * Math.sin(Math.PI * t)));
  }
  return pts;
}

// place an HTML label (by id) over a 3D point; o = opacity
export function pin(id, v3, cam, env, o = 1, dx = 0, dy = 0) {
  const e = document.getElementById(id); if (!e) return;
  cam.updateMatrixWorld(); const p = v3.clone().project(cam);
  e.style.left = (env.X + ((p.x + 1) / 2) * env.W + dx).toFixed(1) + "px";
  e.style.top = (env.Y + ((1 - p.y) / 2) * env.H + dy).toFixed(1) + "px";
  const px = (p.x + 1) / 2, py = (1 - p.y) / 2;
  const inside = px > 0.03 && px < 0.97 && py > 0.03 && py < 0.97;
  e.style.opacity = (p.z < 1 && inside ? o : 0).toFixed(3);
}

// ---------------------------------------------------------------- week-13 helpers
// a tube through many points that can be drawn on progressively (drawTube(m, 0..1))
export function tubeN(points, radius, color, opacity = 1, seg = 400, radial = 10, curveType = "centripetal") {
  const curve = new THREE.CatmullRomCurve3(points.map((p) => (p.isVector3 ? p : new THREE.Vector3(...p))), false, curveType);
  const m = new THREE.Mesh(new THREE.TubeGeometry(curve, seg, radius, radial, false), new THREE.MeshBasicMaterial({ color,
    transparent: true, opacity, blending: THREE.AdditiveBlending, depthWrite: false }));
  m.userData.seg = seg; m.userData.radial = radial; m.userData.curve = curve;
  return m;
}
export function drawTube(m, f) {
  const k = Math.floor(clamp(f) * m.userData.seg);
  m.geometry.setDrawRange(0, k * m.userData.radial * 6);
  m.visible = k > 0;
}
// a polyline tube with straight segments (steps stay sharp): a chain of short tubes merged as one curve path
export function pathTube(points, radius, color, opacity = 1, seg = 600, radial = 8) {
  const path = new THREE.CurvePath();
  const V = points.map((p) => (p.isVector3 ? p : new THREE.Vector3(...p)));
  for (let i = 1; i < V.length; i++) path.add(new THREE.LineCurve3(V[i - 1], V[i]));
  const m = new THREE.Mesh(new THREE.TubeGeometry(path, seg, radius, radial, false), new THREE.MeshBasicMaterial({ color,
    transparent: true, opacity, blending: THREE.AdditiveBlending, depthWrite: false }));
  m.userData.seg = seg; m.userData.radial = radial; m.userData.curve = path;
  return m;
}
// a texture painted with a 2D canvas callback (seek-safe: painted once)
export function canvasTex(w, h, paint) {
  const c = document.createElement("canvas"); c.width = w; c.height = h;
  paint(c.getContext("2d"), w, h);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  return t;
}
// a soft additive plane (for light slabs, bars, beams)
export function slab(w, h, color, opacity = 0.6) {
  const m = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ color, transparent: true, opacity,
    blending: THREE.AdditiveBlending, depthWrite: false, side: THREE.DoubleSide }));
  return m;
}
// a glowing box (packets, bars)
export function glowBox(w, h, d, color, emissive = 1.2) {
  return new THREE.Mesh(new THREE.BoxGeometry(w, h, d), new THREE.MeshStandardMaterial({ color, emissive: color,
    emissiveIntensity: emissive, roughness: 0.35, metalness: 0.1, transparent: true, opacity: 1 }));
}

// a camera-facing-ish flat ribbon through points, rewritable every frame (thick lines; WebGL lines are 1 px)
export function ribbon(n, width, color, opacity = 1) {
  const pos = new Float32Array(n * 2 * 3), idx = [];
  for (let i = 0; i < n - 1; i++) { const a = i * 2; idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3)); geo.setIndex(idx);
  const m = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ color, transparent: true, opacity, side: THREE.DoubleSide,
    blending: THREE.AdditiveBlending, depthWrite: false }));
  m.frustumCulled = false;
  m.userData.set = function (pts) {          // pts: n Vector3; widened in y (the ribbon lies in a vertical plane)
    for (let i = 0; i < n; i++) {
      const p = pts[Math.min(i, pts.length - 1)], q0 = pts[Math.max(i - 1, 0)], q1 = pts[Math.min(i + 1, pts.length - 1)];
      const dx = q1.x - q0.x, dy = q1.y - q0.y, L = Math.hypot(dx, dy) || 1;
      const nx = -dy / L * width / 2, ny = dx / L * width / 2;
      pos.set([p.x + nx, p.y + ny, p.z, p.x - nx, p.y - ny, p.z], i * 6);
    }
    geo.attributes.position.needsUpdate = true;
    geo.computeBoundingSphere();
  };
  return m;
}

// a faint floor grid
export function grid(size, div, color, opacity = 0.18, y = -2) {
  const g = new THREE.GridHelper(size, div, color, color);
  g.material.transparent = true; g.material.opacity = opacity; g.material.depthWrite = false;
  g.position.y = y;
  return g;
}

// the 3D piano roll (Auto-Tune film): lanes for MIDI 59-72 (C major lanes lit), the sung notes as soft boxes,
// pitch tracks as tubes. roll = {t_starts, t_end, tune, names, tracks:{name:[[t, midi], ...]}}
export function pianoRoll(scene, roll, o = {}) {
  const XS = o.xs || 3.0, YS = o.ys || 0.42, T0 = o.t0 !== undefined ? o.t0 : 1.88, M0 = o.m0 !== undefined ? o.m0 : 65;
  const X = (t) => (t - T0) * XS, Y = (m) => (m - M0) * YS;
  const g = new THREE.Group(); scene.add(g);
  const key = new Set([0, 2, 4, 5, 7, 9, 11]);
  const t0 = roll.t_starts[0] - 0.2, t1 = roll.t_end + 0.2;
  const lanes = {};
  for (let m = 59; m <= 72; m++) {
    const inKey = key.has(m % 12);
    const lane = slab((t1 - t0) * XS, inKey ? 0.03 : 0.012, inKey ? 0xb79cff : 0x6a5878, inKey ? 0.5 : 0.22);
    lane.position.set(X((t0 + t1) / 2), Y(m), 0); g.add(lane); lanes[m] = lane;
  }
  const notes = [];
  roll.tune.forEach((m, i) => {
    const a = roll.t_starts[i], b = i + 1 < roll.tune.length ? roll.t_starts[i + 1] : roll.t_end;
    const box = slab((b - a) * XS - 0.08, YS * 0.7, 0xb79cff, 0.1); box.position.set(X((a + b) / 2), Y(m), -0.03);
    g.add(box); notes.push({ box, a, b, m });
  });
  const tubes = {};
  const tube = (name, color, r = 0.04) => {
    const pts = roll.tracks[name].map(([t, m]) => new THREE.Vector3(X(t), Y(m), 0.06));
    const mm = tubeN(pts, r, color, 1, Math.max(200, pts.length * 3), 10, "centripetal");
    mm.material.blending = THREE.NormalBlending;
    mm.userData.t0 = roll.tracks[name][0][0]; mm.userData.t1 = roll.tracks[name][roll.tracks[name].length - 1][0];
    g.add(mm); tubes[name] = mm; return mm;
  };
  // the point on a track at roll time t (for glows that ride the draw head)
  const at = (name, t) => {
    const tr = roll.tracks[name]; let lo = 0, hi = tr.length - 1;
    if (t <= tr[0][0]) return new THREE.Vector3(X(tr[0][0]), Y(tr[0][1]), 0.08);
    if (t >= tr[hi][0]) return new THREE.Vector3(X(tr[hi][0]), Y(tr[hi][1]), 0.08);
    while (hi - lo > 1) { const mid = (lo + hi) >> 1; if (tr[mid][0] <= t) lo = mid; else hi = mid; }
    const f = (t - tr[lo][0]) / (tr[hi][0] - tr[lo][0]);
    return new THREE.Vector3(X(tr[lo][0] + f * (tr[hi][0] - tr[lo][0])), Y(tr[lo][1] + f * (tr[hi][1] - tr[lo][1])), 0.08);
  };
  // draw a track up to roll time t
  const drawTo = (name, t) => { const m = tubes[name]; drawTube(m, (t - m.userData.t0) / (m.userData.t1 - m.userData.t0)); };
  return { g, X, Y, notes, lanes, tube, tubes, at, drawTo, t0: roll.t_starts[0], t1: roll.t_end };
}
