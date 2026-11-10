// Ehrensaft-Karussell-Teile (eigene Zeichnungen für Posts 09–12, ergänzt das Kit, ändert es nicht).
(function () {
  const T = "#1B1220", G = "#FFE433", P = "#FF2E7E", PT = "#C8104F", N = "#7CFF3A", CR = "#FFF8E1", GO = "#C9A227";
  let uid = 0;

  // Kit-Flasche an Position x/y mit Breite/Höhe in ein umgebendes SVG setzen
  const flascheIn = (x, y, w, h, opts = {}) =>
    EK.flasche(opts).replace('width="100%" height="100%"', `x="${x}" y="${y}" width="${w}" height="${h}"`);

  // ganze Früchte (Seitenansicht), Mittelpunkt 0/0
  function ganz(art, r) {
    const sw = Math.max(3, r * .07);
    if (art === "zitrone") return `<g>
      <path d="M${-r * 1.18},0 C${-r * 1.1},${-r * .55} ${-r * .6},${-r * .88} 0,${-r * .88} C${r * .6},${-r * .88} ${r * 1.1},${-r * .55} ${r * 1.18},0 C${r * 1.1},${r * .55} ${r * .6},${r * .88} 0,${r * .88} C${-r * .6},${r * .88} ${-r * 1.1},${r * .55} ${-r * 1.18},0Z" fill="#FFD400" stroke="${T}" stroke-width="${sw}"/>
      <path d="M${-r * 1.18},0 l${-r * .16},${-r * .05} l${r * .02},${r * .12}Z M${r * 1.18},0 l${r * .16},${r * .05} l${-r * .02},${-r * .12}Z" fill="#FFD400" stroke="${T}" stroke-width="${sw * .8}" stroke-linejoin="round"/>
      <ellipse cx="${-r * .35}" cy="${-r * .42}" rx="${r * .38}" ry="${r * .14}" fill="#fff" opacity=".75" transform="rotate(-12 ${-r * .35} ${-r * .42})"/>
      <path d="M${r * .1},${-r * .86} q${r * .45},${-r * .5} ${r * .9},${-r * .25} q${-r * .45},${r * .35} ${-r * .9},${r * .25}Z" fill="#3DBB3D" stroke="${T}" stroke-width="${sw * .8}"/></g>`;
    if (art === "himbeere") return EK.himbeere(r * 1.05);
    if (art === "orange") {
      let d = ""; const g = EK.rnd(11);
      for (let i = 0; i < 18; i++) { const a = g() * 6.28, rr = g() * r * .8; d += `<circle cx="${(Math.cos(a) * rr).toFixed(1)}" cy="${(Math.sin(a) * rr).toFixed(1)}" r="${r * .035}" fill="#D96A00"/>`; }
      return `<g><circle r="${r}" fill="#FF8A00" stroke="${T}" stroke-width="${sw}"/>${d}<ellipse cx="${-r * .35}" cy="${-r * .4}" rx="${r * .3}" ry="${r * .15}" fill="#fff" opacity=".6" transform="rotate(-30 ${-r * .35} ${-r * .4})"/>
      <path d="M0,${-r * .95} q${r * .4},${-r * .45} ${r * .8},${-r * .2} q${-r * .4},${r * .3} ${-r * .8},${r * .2}Z" fill="#3DBB3D" stroke="${T}" stroke-width="${sw * .8}"/></g>`;
    }
    if (art === "kiwi") {
      let k = "";
      for (let i = 0; i < 16; i++) { const a = i / 16 * 6.28; k += `<ellipse cx="${(Math.cos(a) * r * .45).toFixed(1)}" cy="${(Math.sin(a) * r * .45).toFixed(1)}" rx="${r * .05}" ry="${r * .1}" fill="${T}" transform="rotate(${(a * 57.3 + 90).toFixed(0)} ${(Math.cos(a) * r * .45).toFixed(1)} ${(Math.sin(a) * r * .45).toFixed(1)})"/>`; }
      return `<g><circle r="${r}" fill="#8B5A2B" stroke="${T}" stroke-width="${sw}"/><circle r="${r * .86}" fill="#7DC82E"/><circle r="${r * .7}" fill="#9BDB4A"/>${k}<ellipse rx="${r * .25}" ry="${r * .18}" fill="#F4F8D0"/><circle r="${r}" fill="none" stroke="${T}" stroke-width="${sw}"/></g>`;
    }
    if (art === "erdbeere") {
      let s = ""; const g = EK.rnd(5);
      for (let i = 0; i < 14; i++) { const x = (g() - .5) * r * 1.2, y = -r * .3 + g() * r * 1.1 * (1 - Math.abs(x) / r * .6); s += `<ellipse cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" rx="${r * .04}" ry="${r * .07}" fill="#FFE27A"/>`; }
      return `<g><path d="M0,${r} C${-r * .5},${r * .7} ${-r},${r * .1} ${-r * .95},${-r * .35} C${-r * .9},${-r * .75} ${-r * .4},${-r * .8} 0,${-r * .65} C${r * .4},${-r * .8} ${r * .9},${-r * .75} ${r * .95},${-r * .35} C${r},${r * .1} ${r * .5},${r * .7} 0,${r}Z" fill="#E8203A" stroke="${T}" stroke-width="${sw}"/>${s}
      <path d="M${-r * .55},${-r * .7} l${r * .25},${-r * .2} l${r * .3},${r * .1} l${r * .25},${-r * .3} l${r * .25},${r * .3} l${r * .3},${-r * .1} l${r * .2},${r * .25} q${-r * .55},${r * .2} ${-r * 1.1},0Z" fill="#3DBB3D" stroke="${T}" stroke-width="${sw * .8}" stroke-linejoin="round"/></g>`;
    }
    if (art === "kirsche") return `<g><path d="M${-r * .45},${r * .1} Q${-r * .2},${-r * .7} ${r * .25},${-r * 1.0} M${r * .45},${r * .2} Q${r * .4},${-r * .5} ${r * .25},${-r * 1.0}" fill="none" stroke="#3D7A20" stroke-width="${sw}" stroke-linecap="round"/>
      <circle cx="${-r * .45}" cy="${r * .4}" r="${r * .5}" fill="#D2143A" stroke="${T}" stroke-width="${sw}"/><circle cx="${r * .45}" cy="${r * .5}" r="${r * .5}" fill="#E8203A" stroke="${T}" stroke-width="${sw}"/>
      <circle cx="${-r * .6}" cy="${r * .25}" r="${r * .11}" fill="#fff" opacity=".7"/><circle cx="${r * .3}" cy="${r * .35}" r="${r * .11}" fill="#fff" opacity=".7"/></g>`;
    if (art === "melone") return `<g><path d="M${-r * 1.1},${-r * .3} A${r * 1.1},${r * 1.1} 0 0 0 ${r * 1.1},${-r * .3}Z" fill="#2E9E3A" stroke="${T}" stroke-width="${sw}"/><path d="M${-r * .95},${-r * .3} A${r * .95},${r * .95} 0 0 0 ${r * .95},${-r * .3}Z" fill="#F4F8D0"/><path d="M${-r * .85},${-r * .3} A${r * .85},${r * .85} 0 0 0 ${r * .85},${-r * .3}Z" fill="#FF4D6A"/>
      ${[[-.45, .0], [0, .15], [.45, .0], [-.2, .35], [.25, .38]].map(([x, y]) => `<ellipse cx="${x * r}" cy="${y * r}" rx="${r * .05}" ry="${r * .09}" fill="${T}"/>`).join("")}
      <path d="M${-r * 1.1},${-r * .3} H${r * 1.1}" stroke="${T}" stroke-width="${sw}"/></g>`;
    if (art === "mango") return `<g><path d="M${-r * .2},${-r * .95} C${r * .8},${-r * .95} ${r * 1.05},${r * .2} ${r * .55},${r * .7} C${r * .1},${r * 1.1} ${-r * .9},${r * .9} ${-r * .95},${r * .1} C${-r},${-r * .5} ${-r * .7},${-r * .95} ${-r * .2},${-r * .95}Z" fill="#FFB020" stroke="${T}" stroke-width="${sw}"/>
      <path d="M${r * .3},${r * .1} C${r * .55},${r * .4} ${r * .4},${r * .7} ${r * .1},${r * .85} C${r * .5},${r * .85} ${r * .8},${r * .4} ${r * .55},${-r * .2}Z" fill="#FF5E3A" opacity=".55"/>
      <ellipse cx="${-r * .4}" cy="${-r * .45}" rx="${r * .25}" ry="${r * .12}" fill="#fff" opacity=".6" transform="rotate(-35 ${-r * .4} ${-r * .45})"/>
      <path d="M${-r * .2},${-r * .95} q${-r * .2},${-r * .45} ${r * .5},${-r * .5} q${-r * .15},${r * .35} ${-r * .5},${r * .5}Z" fill="#3DBB3D" stroke="${T}" stroke-width="${sw * .8}"/></g>`;
    return EK.frucht(art, r);
  }

  // Sammelfigur „Ehrenfrucht“: Frucht auf Sockel mit Nummernschild. Fußpunkt 0/0 (Unterkante Sockel), Breite ca. 260*s
  function figur(art, nr, opts = {}) {
    const o = Object.assign({ s: 1, glow: false, r: 95 }, opts), id = "fg" + (++uid), s = o.s;
    const glow = o.glow ? `<defs><filter id="${id}" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="22"/></filter></defs>
      <ellipse cx="0" cy="-205" rx="150" ry="140" fill="${N}" opacity=".85" filter="url(#${id})"/>
      <ellipse cx="0" cy="-80" rx="130" ry="30" fill="${N}" opacity=".9" filter="url(#${id})"/>` : "";
    return `<g transform="scale(${s})">${glow}
      <path d="M-120,-78 V-12 A120,26 0 0 0 120,-12 V-78Z" fill="${o.glow ? "#1d1626" : T}" stroke="${o.glow ? N : T}" stroke-width="7"/>
      <ellipse cx="0" cy="-78" rx="120" ry="26" fill="${o.glow ? "#2a2236" : "#3a2c44"}" stroke="${o.glow ? N : T}" stroke-width="7"/>
      <rect x="-62" y="-60" width="124" height="38" rx="6" fill="${GO}" stroke="${T}" stroke-width="4"/>
      <text x="0" y="-31" text-anchor="middle" font-family="Anton" font-size="27" fill="${T}">NR. ${nr}</text>
      <g transform="translate(0,${-90 - o.r})">${o.glow ? `<g opacity=".25">${ganz(art, o.r * 1.06)}</g>` : ""}${ganz(art, o.r)}</g></g>`;
  }

  // Glow-Becher: Mittelpunkt Unterkante 0/0, Höhe ca. 360
  function becher(opts = {}) {
    const o = Object.assign({ glow: true }, opts), id = "bc" + (++uid);
    const k = "M-100,-300 L100,-300 L78,0 L-78,0Z";
    return `<g><defs><filter id="${id}" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="20"/></filter>
      <linearGradient id="${id}f" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF06A"/><stop offset=".6" stop-color="#FFC93C"/><stop offset="1" stop-color="#FF5E8F"/></linearGradient>
      <clipPath id="${id}c"><path d="${k}"/></clipPath></defs>
      ${o.glow ? `<path d="${k}" fill="${N}" filter="url(#${id})" opacity=".95"/>` : ""}
      <path d="M30,-330 L70,-440" stroke="${T}" stroke-width="26" stroke-linecap="round"/><path d="M30,-330 L70,-440" stroke="${P}" stroke-width="14" stroke-linecap="round"/>
      <path d="${k}" fill="#fff" opacity=".35"/>
      <g clip-path="url(#${id}c)"><rect x="-110" y="-215" width="220" height="230" fill="url(#${id}f)"/>
        <g transform="translate(-30,-120) rotate(20)">${EK.frucht("zitrone", 34)}</g><g transform="translate(40,-60)">${EK.frucht("himbeere", 24)}</g>
        <path d="M-110,-215 Q-50,-228 0,-215 T110,-215" fill="none" stroke="#fff" stroke-width="5" opacity=".7"/></g>
      <path d="${k}" fill="none" stroke="${o.glow ? N : T}" stroke-width="10" stroke-linejoin="round"/>
      <path d="M-70,-270 L-56,-30" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".7"/>
      <rect x="-112" y="-338" width="224" height="40" rx="14" fill="${P}" stroke="${T}" stroke-width="8"/>
      <rect x="-40" y="-150" width="80" height="80" rx="40" fill="${CR}" stroke="${T}" stroke-width="5"/>
      <text x="0" y="-100" text-anchor="middle" font-family="Bowlby One" font-size="24" fill="${P}">E</text></g>`;
  }

  // Box (Karton) – Inhalt wird zwischen Rückseite und Vorderseite eingesetzt. viewBox-Koordinaten 0..640 x 0..600
  function box(inhalt = "", opts = {}) {
    const o = Object.assign({ deckel: true, aufschrift: "#EHRENTESTER" }, opts);
    return `<g>
      ${o.deckel ? `<path d="M110,250 L530,250 L505,120 L135,120Z" fill="${PT}" stroke="${T}" stroke-width="10" stroke-linejoin="round"/>` : ""}
      <path d="M110,250 L530,250 L570,292 L70,292Z" fill="#5A0E2C" stroke="${T}" stroke-width="10" stroke-linejoin="round"/>
      ${inhalt}
      <path d="M70,292 L110,250 L28,170 L-8,222Z" fill="${PT}" stroke="${T}" stroke-width="10" stroke-linejoin="round"/>
      <path d="M570,292 L530,250 L612,170 L648,222Z" fill="${PT}" stroke="${T}" stroke-width="10" stroke-linejoin="round"/>
      <rect x="70" y="292" width="500" height="290" rx="8" fill="${P}" stroke="${T}" stroke-width="10"/>
      <path d="M70,330 H570" stroke="${T}" stroke-width="5" opacity=".35"/>
      <rect x="130" y="380" width="380" height="120" rx="12" fill="${CR}" stroke="${T}" stroke-width="7"/>
      <rect x="142" y="392" width="356" height="96" rx="6" fill="none" stroke="${GO}" stroke-width="3"/>
      <text x="320" y="462" text-anchor="middle" font-family="Anton" font-size="56" fill="${T}" letter-spacing="1">${o.aufschrift}</text>
      <g transform="translate(520,540) rotate(-10)">${EK.siegel(56, "EHRE")}</g></g>`;
  }

  // Funkeln/Sterne
  const funkel = (x, y, r, f = "#fff") => `<path transform="translate(${x},${y})" d="M0,${-r} Q${r * .18},${-r * .18} ${r},0 Q${r * .18},${r * .18} 0,${r} Q${-r * .18},${r * .18} ${-r},0 Q${-r * .18},${-r * .18} 0,${-r}Z" fill="${f}" stroke="${T}" stroke-width="${Math.max(2, r * .12)}" stroke-linejoin="round"/>`;

  // verstreute Fruchtscheiben (Deko), Liste [x,y,art,r,rot]
  const deko = liste => liste.map(([x, y, a, r, rot = 0]) => `<g transform="translate(${x},${y}) rotate(${rot})">${a.startsWith("g:") ? ganz(a.slice(2), r) : EK.frucht(a, r)}</g>`).join("");

  window.ET = { T, G, P, PT, N, CR, GO, flascheIn, ganz, figur, becher, box, funkel, deko };
})();
