// Motion-Baukasten für Premium-Reels (Wissen 26.10., strategie/20_wissen_motion.md).
// Alle Funktionen sind zeitgesteuert: render(t) ruft sie mit der aktuellen Sekunde t auf – kein CSS-Transition,
// damit jedes Frame beim Rendern exakt reproduzierbar ist.  Einbinden: <script src="motion.js"></script>
const M = (() => {
  const cl = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  const p = (t, t0, d) => cl((t - t0) / d);                          // Fortschritt 0…1
  const ease = {
    out: x => 1 - Math.pow(1 - x, 3),                                // Standard: schnell rein, sanft aus
    inOut: x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2,  // langsam – schneller – bremst ab
    overshoot: x => { const c = 1.70158, c3 = c + 1; return 1 + c3 * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2) },  // kurz übers Ziel
    bounce: x => { const n = 7.5625, d = 2.75; if (x < 1 / d) return n * x * x; if (x < 2 / d) return n * (x -= 1.5 / d) * x + .75;
      if (x < 2.5 / d) return n * (x -= 2.25 / d) * x + .9375; return n * (x -= 2.625 / d) * x + .984375 },          // federt nach
  };
  const $ = e => typeof e === "string" ? document.getElementById(e) : e;
  return {
    cl, p, ease,
    // Einblenden
    popIn(el, t, t0, d = .35) { const x = ease.overshoot(p(t, t0, d)); el = $(el); el.style.opacity = cl(x * 1.4); el.style.transform = `scale(${.6 + .4 * x})` },
    scaleUp(el, t, t0, d = .6) { const x = ease.out(p(t, t0, d)); el = $(el); el.style.opacity = cl(x * 2); el.style.transform = `scale(${.2 + .8 * x})` },
    stagger(els, t, t0, gap = .12, d = .35) { [...els].forEach((e, i) => { const x = ease.out(p(t, t0 + i * gap, d)); e.style.opacity = x; e.style.transform = `translateY(${(1 - x) * 40}px)` }) },
    slideIn(el, t, t0, d = .4, dx = -120) { const x = ease.out(p(t, t0, d)); el = $(el); el.style.opacity = x; el.style.transform = `translateX(${(1 - x) * dx}px)` },
    // Text in Bewegung
    typewriter(el, text, t, t0, cps = 22) { el = $(el); const n = Math.floor(cl((t - t0) * cps, 0, text.length)); el.textContent = text.slice(0, n) + (n < text.length && t >= t0 ? "▍" : "") },
    wordReveal(el, words, t, zeiten) { el = $(el); el.innerHTML = words.map((w, i) => `<span style="opacity:${t >= zeiten[i] ? 1 : .12}">${w}</span>`).join(" ") },
    textSwap(el, a, b, t, t0, d = .3) { el = $(el); const x = p(t, t0, d); el.textContent = x < .5 ? a : b; el.style.transform = `rotateX(${(x < .5 ? x : 1 - x) * 180}deg)` },
    countUp(el, von, bis, t, t0, d = 1, fmt = v => Math.round(v).toLocaleString("de-DE")) { $(el).textContent = fmt(von + (bis - von) * ease.out(p(t, t0, d))) },
    // Formen
    drawOn(path, t, t0, d = .8) { path = $(path); const L = path.getTotalLength(); path.style.strokeDasharray = L; path.style.strokeDashoffset = L * (1 - ease.inOut(p(t, t0, d))) },
    barGrow(el, ziel, t, t0, d = .8) { $(el).style.width = (ziel * ease.out(p(t, t0, d))) + "%" },
    // Übergänge zwischen Szenen
    maskReveal(el, t, t0, d = .45) { const x = ease.inOut(p(t, t0, d)); $(el).style.clipPath = `inset(${50 * (1 - x)}% 0 ${50 * (1 - x)}% 0)` },
    wipe(el, t, t0, d = .45) { const x = ease.inOut(p(t, t0, d)); $(el).style.clipPath = `inset(0 ${100 * (1 - x)}% 0 0)` },
    punchZoom(el, t, t0, d = .25, staerke = .12) { const x = p(t, t0, d); $(el).style.transform = `scale(${1 + staerke * Math.sin(Math.PI * x)})` },
  };
})();
