// B02 · loudness: the head casts an acoustic shadow. High sounds (short waves) are blocked, so the far ear hears
// them 14 dB quieter; low sounds (long waves) bend around, only 2.3 dB. The far-side darkening uses those numbers.
export default function (K, canvas, env) {
  const { THREE } = K;
  const { r, scene, cam } = K.setup(canvas, env.W, env.H, { fov: 34, exposure: 1.2 });
  K.lights(scene, 0xffffff, 0x404a99);
  const c = env.cue, D = env.D;
  const head = K.headModel(); scene.add(head.g);
  const dust = K.dust(scene, 300, 14, 0x8a9bff, 0.06, 21);
  const SX = 4.6;
  const src = K.source(0xffb454, 0.2); src.position.set(SX, 0, 0); scene.add(src);
  // the wave field: a plane through the ears, lit by the ripples, darkened in the head's shadow
  const uni = { S: { value: new THREE.Vector2(SX, 0) }, k: { value: 9 }, ph: { value: 0 }, shade: { value: 0.8 }, soft: { value: 0.25 },
    amp: { value: 0 }, warm: { value: new THREE.Color(0xffb454) }, cool: { value: new THREE.Color(0x3a46b8) } };
  const field = new THREE.Mesh(new THREE.PlaneGeometry(22, 22, 1, 1), new THREE.ShaderMaterial({
    uniforms: uni, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide,
    vertexShader: "varying vec2 P; void main(){ vec4 w = modelMatrix*vec4(position,1.0); P = w.xz; gl_Position = projectionMatrix*viewMatrix*w; }",
    fragmentShader: `uniform vec2 S; uniform float k; uniform float ph; uniform float shade; uniform float soft; uniform float amp;
      uniform vec3 warm; uniform vec3 cool; varying vec2 P;
      void main(){
        float r = length(P);
        if (r < 1.0) discard;
        vec2 d = P - S; float dist = length(d); vec2 dir = d / dist;
        vec2 toC = -S; float proj = dot(toC, dir);
        float perp = length(toC - dir * proj);
        float behind = smoothstep(-0.2, 0.6, dist - proj);
        float sh = (1.0 - smoothstep(1.0 - soft * 0.35, 1.0 + soft, perp)) * behind * shade;
        float wv = 0.5 + 0.5 * cos(k * dist - ph);
        wv = pow(wv, 2.2);
        float fall = 1.0 / (1.0 + 0.16 * dist);
        float edge = 1.0 - smoothstep(6.5, 10.5, r);
        float I = wv * fall * (1.0 - sh) * edge * amp;
        vec3 col = mix(cool, warm, 0.35 + 0.65 * (1.0 - sh));
        float base = 0.10 * fall * edge * amp * (1.0 - sh * 0.9);
        gl_FragColor = vec4(col * (I + base), 1.0);
      }` }));
  field.rotation.x = -Math.PI / 2; field.position.y = -0.01; field.renderOrder = -1;
  scene.add(field);
  // a dark "shadow" marker on the floor behind the head
  scene.add(K.polarFloor(6.5, 0x5f6bd6, -1.25, 0.14));

  return function renderAt(t) {
    const tHi = c.high - 0.2, tLo = c.low - 0.1;
    const lo = K.prog(t, tLo, 1.4, K.ease.inOut);
    const hiOn = K.prog(t, c.shadow, 1.2);
    uni.amp.value = hiOn;
    uni.k.value = K.lerp(9.0, 2.0, lo);                       // short waves -> long waves
    uni.shade.value = K.lerp(1 - env.data.hi_far, 1 - env.data.lo_far, lo);   // 0.80 -> 0.23 (from the dB)
    uni.soft.value = K.lerp(0.25, 2.2, lo);                   // long waves bend round: a softer shadow
    uni.ph.value = t * K.lerp(9.0, 3.2, lo);
    // ear glow = level at each ear
    const near = hiOn, far = hiOn * (1 - uni.shade.value);
    head.glowR.material.opacity = 0.9 * near; head.glowR.scale.setScalar(1.1);
    head.glowL.material.opacity = 0.9 * far; head.glowL.scale.setScalar(0.5 + 0.6 * far);
    head.earR.material.emissiveIntensity = 0.5 + 1.6 * near; head.earL.material.emissiveIntensity = 0.5 + 1.6 * far;
    src.userData.halo.material.opacity = 0.7 + 0.15 * Math.sin(t * 6);
    // camera: high three-quarter view so the shadow on the far side reads
    const u = t / D;
    const ca = K.deg(-28 + 18 * u), cr = env.portrait ? 9.4 : 9.6;
    cam.position.set(0.6 + Math.sin(ca) * cr, 7.4 - 0.8 * u, Math.cos(ca) * cr);
    cam.lookAt(0.6, -0.4, -0.2);
    dust(t);
    r.render(scene, cam);
  };
}
