// Ehrensaft-Kit: Flasche, Früchte, Siegel, Splash – alles als SVG-Strings + kleine Zeit-Helfer.
// Nutzung: <script src="../kit/kit.js"></script>, dann z. B. el.innerHTML = EK.flasche({fuell:1});
(function () {
  const C = { gelb: "#FFE433", gelbTief: "#F7C600", pink: "#FF2E7E", pinkTief: "#C8104F", neon: "#7CFF3A", tinte: "#1B1220", creme: "#FFF8E1", gold: "#C9A227" };
  let uid = 0;

  // --- Zeit-Helfer (deterministisch, t in Sekunden) ---
  const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  const prog = (t, start, dauer) => clamp((t - start) / dauer);
  const ease = { out: x => 1 - Math.pow(1 - x, 3), inOut: x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2,
    back: x => { const c = 1.70158, d = c + 1; return 1 + d * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); },
    bounce: x => { const n = 7.5625, d = 2.75; if (x < 1 / d) return n * x * x; if (x < 2 / d) return n * (x -= 1.5 / d) * x + .75; if (x < 2.5 / d) return n * (x -= 2.25 / d) * x + .9375; return n * (x -= 2.625 / d) * x + .984375; } };
  const lerp = (a, b, x) => a + (b - a) * x;
  // fester Zufall (gleiches Bild bei jedem Rendern)
  const rnd = seed => { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); };

  // --- Früchte (Draufsicht-Scheiben), Mittelpunkt 0/0, Radius r ---
  function scheibe(r, schale, fleisch, n = 8) {
    let seg = "";
    for (let i = 0; i < n; i++) {
      const a0 = (i / n) * Math.PI * 2 + .06, a1 = ((i + 1) / n) * Math.PI * 2 - .06, ri = r * .8, r0 = r * .1;
      const p = (a, rr) => `${(Math.cos(a) * rr).toFixed(1)},${(Math.sin(a) * rr).toFixed(1)}`;
      seg += `<path d="M${p(a0, r0)} L${p(a0, ri)} A${ri},${ri} 0 0 1 ${p(a1, ri)} L${p(a1, r0)} Z" fill="${fleisch}"/>`;
    }
    return `<g><circle r="${r}" fill="${schale}"/><circle r="${r * .88}" fill="#FFFBE0"/>${seg}<circle r="${r}" fill="none" stroke="${C.tinte}" stroke-width="${Math.max(2, r * .07)}"/></g>`;
  }
  const zitrone = r => scheibe(r, "#FFD400", "#FFEF6B", 8);
  const orange = r => scheibe(r, "#FF8A00", "#FFB347", 10);
  function himbeere(r) {
    let k = ""; const g = rnd(7);
    [[0, -.45], [-.4, -.25], [.4, -.25], [-.2, .05], [.25, .05], [-.45, .2], [.5, .2], [0, .4], [-.25, .55], [.25, .55]].forEach(([x, y]) => {
      k += `<circle cx="${x * r}" cy="${y * r}" r="${r * .3}" fill="${g() > .5 ? C.pink : "#E01B63"}" stroke="${C.tinte}" stroke-width="${Math.max(1.5, r * .05)}"/><circle cx="${x * r - r * .08}" cy="${y * r - r * .1}" r="${r * .07}" fill="#fff" opacity=".7"/>`;
    });
    return `<g>${k}<path d="M${-r * .3},${-r * .7} q${r * .3},${-r * .35} ${r * .6},0 q${-r * .3},${r * .15} ${-r * .6},0Z" fill="#3DBB3D" stroke="${C.tinte}" stroke-width="${Math.max(1.5, r * .05)}"/></g>`;
  }
  const frucht = (art, r) => art === "orange" ? orange(r) : art === "himbeere" ? himbeere(r) : zitrone(r);

  // --- Siegel (Ehrenabzeichen) ---
  function siegel(r = 60, text = "EHREN­WORT", farbe = C.gold) {
    let z = ""; const n = 24;
    for (let i = 0; i < n * 2; i++) { const a = (i / (n * 2)) * Math.PI * 2, rr = i % 2 ? r : r * .88; z += `${i ? "L" : "M"}${(Math.cos(a) * rr).toFixed(1)},${(Math.sin(a) * rr).toFixed(1)}`; }
    return `<g><path d="${z}Z" fill="${farbe}" stroke="${C.tinte}" stroke-width="${r * .05}"/><circle r="${r * .7}" fill="none" stroke="${C.tinte}" stroke-width="${r * .035}" stroke-dasharray="${r * .06} ${r * .06}"/>
      <text text-anchor="middle" y="${r * .13}" font-family="Anton" font-size="${r * .36}" fill="${C.tinte}">${text.replace("­", "")}</text></g>`;
  }

  // --- Flasche: klare 0,5-l-Flasche, Früchte sichtbar, Etikett als Ehrenurkunde. viewBox 0 0 400 1000 ---
  // opts: fuell 0..1 (Füllstand), glow (Neon-Schein), fruechte (Anzahl), etikett (true/false), welle (Phase der Oberfläche)
  function flasche(opts = {}) {
    const o = Object.assign({ fuell: 1, glow: false, fruechte: 9, etikett: true, welle: 0, kronkorken: true }, opts);
    const id = "f" + (++uid), g = rnd(42);
    const koerper = "M150,60 L250,60 L250,205 C250,270 345,300 345,400 L345,910 C345,955 315,975 270,975 L130,975 C85,975 55,955 55,910 L55,400 C55,300 150,270 150,205 Z";
    const oben = 975 - o.fuell * 760; // Flüssigkeitsoberkante
    const w = Math.sin(o.welle) * 10;
    let fr = "";
    for (let i = 0; i < o.fruechte; i++) {
      const art = ["zitrone", "orange", "himbeere"][i % 3], r = art === "himbeere" ? 26 + g() * 8 : 38 + g() * 16;
      const x = 105 + g() * 190, y = Math.max(oben + 50, 380 + g() * 540), rot = g() * 360;
      fr += `<g transform="translate(${x.toFixed(0)},${y.toFixed(0)}) rotate(${rot.toFixed(0)})" opacity=".95">${frucht(art, r)}</g>`;
    }
    let blasen = "";
    for (let i = 0; i < 14; i++) blasen += `<circle cx="${(80 + g() * 240).toFixed(0)}" cy="${(Math.max(oben + 20, 330 + g() * 620)).toFixed(0)}" r="${(3 + g() * 7).toFixed(1)}" fill="#fff" opacity="${(.25 + g() * .4).toFixed(2)}"/>`;
    const etikett = !o.etikett ? "" : `
      <g transform="translate(200,640)">
        <rect x="-140" y="-150" width="280" height="300" rx="10" fill="${C.creme}" stroke="${C.tinte}" stroke-width="6"/>
        <rect x="-126" y="-136" width="252" height="272" rx="4" fill="none" stroke="${C.gold}" stroke-width="3"/>
        <text text-anchor="middle" y="-96" font-family="Inter" font-weight="700" font-size="17" letter-spacing="5" fill="${C.tinte}">EHRENURKUNDE</text>
        <text text-anchor="middle" y="-30" font-family="Bowlby One" font-size="53" fill="${C.pink}" stroke="${C.tinte}" stroke-width="3" paint-order="stroke fill">EHREN</text>
        <text text-anchor="middle" y="26" font-family="Bowlby One" font-size="60" fill="${C.pink}" stroke="${C.tinte}" stroke-width="3" paint-order="stroke fill">SAFT</text>
        <text text-anchor="middle" y="60" font-family="Inter" font-weight="600" font-size="16" letter-spacing="2" fill="${C.tinte}">ZITRONE · HIMBEERE</text>
        <line x1="-90" y1="76" x2="90" y2="76" stroke="${C.tinte}" stroke-width="2"/>
        <text text-anchor="middle" y="108" font-family="Permanent Marker" font-size="22" fill="${C.tinte}">Du weißt Bescheid.</text>
        <g transform="translate(128,-140) rotate(12)">${siegel(40, "EHRE")}</g>
      </g>`;
    return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="-40 -20 480 1040" width="100%" height="100%" style="overflow:visible">
      <defs>
        <clipPath id="${id}c"><path d="${koerper}"/></clipPath>
        <linearGradient id="${id}s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF06A"/><stop offset=".55" stop-color="#FFC93C"/><stop offset="1" stop-color="#FF5E8F"/></linearGradient>
        <linearGradient id="${id}g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset=".18" stop-color="#fff" stop-opacity=".08"/><stop offset=".8" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".12"/></linearGradient>
        <filter id="${id}n" x="-60%" y="-30%" width="220%" height="160%"><feGaussianBlur stdDeviation="26"/></filter>
      </defs>
      ${o.glow ? `<path d="${koerper}" fill="${C.neon}" filter="url(#${id}n)" opacity=".9"/>` : ""}
      <path d="${koerper}" fill="#ffffff" opacity=".28"/>
      <g clip-path="url(#${id}c)">
        <path d="M0,${oben} Q100,${oben - 14 + w} 200,${oben} T400,${oben} L400,1000 L0,1000 Z" fill="url(#${id}s)"/>
        ${fr}${blasen}
        <path d="M0,${oben} Q100,${oben - 14 + w} 200,${oben} T400,${oben}" fill="none" stroke="#fff" stroke-width="5" opacity=".7"/>
      </g>
      ${etikett}
      <path d="${koerper}" fill="url(#${id}g)"/>
      <path d="${koerper}" fill="none" stroke="${o.glow ? C.neon : C.tinte}" stroke-width="9" stroke-linejoin="round"/>
      <path d="M92,420 C84,520 84,760 92,880" fill="none" stroke="#fff" stroke-width="12" stroke-linecap="round" opacity=".75"/>
      ${o.kronkorken ? `<rect x="138" y="14" width="124" height="54" rx="12" fill="${C.pink}" stroke="${C.tinte}" stroke-width="8"/><path d="M150,68 v-40 M172,68 v-40 M194,68 v-40 M216,68 v-40 M238,68 v-40" stroke="${C.tinte}" stroke-width="4" opacity=".5"/>` : ""}
    </svg>`;
  }

  // --- Splash: n Tropfen + Früchte fliegen vom Punkt (0,0) weg. p = Fortschritt 0..1. Gibt SVG-<g> zurück. ---
  function splash(p, opts = {}) {
    const o = Object.assign({ n: 26, kraft: 520, seed: 3, fruechte: 7, farbe: "#FFD23C" }, opts), g = rnd(o.seed);
    let s = "";
    for (let i = 0; i < o.n + o.fruechte; i++) {
      const a = -Math.PI * (.08 + g() * .84), v = o.kraft * (.45 + g() * .75), r = 8 + g() * 22, verz = g() * .12;
      const q = clamp((p - verz) / (1 - verz)); if (q <= 0) continue;
      const x = Math.cos(a) * v * q, y = Math.sin(a) * v * q + 900 * q * q; // Schwerkraft
      const op = clamp(1.25 - q * 1.1);
      if (i < o.n) s += `<ellipse cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" rx="${(r * (1 - q * .4)).toFixed(1)}" ry="${(r * 1.35 * (1 - q * .4)).toFixed(1)}" fill="${g() > .3 ? o.farbe : C.pink}" stroke="${C.tinte}" stroke-width="3" opacity="${op.toFixed(2)}" transform="rotate(${(Math.atan2(Math.sin(a) * v + 1800 * q, Math.cos(a) * v) * 57.3 + 90).toFixed(0)} ${x.toFixed(0)} ${y.toFixed(0)})"/>`;
      else s += `<g transform="translate(${x.toFixed(0)},${y.toFixed(0)}) rotate(${(q * 540 * (g() - .5)).toFixed(0)})" opacity="${op.toFixed(2)}">${frucht(["zitrone", "orange", "himbeere"][i % 3], 34 + g() * 22)}</g>`;
    }
    return `<g>${s}</g>`;
  }

  window.EK = { C, clamp, prog, ease, lerp, rnd, zitrone, orange, himbeere, frucht, siegel, flasche, splash };
})();
