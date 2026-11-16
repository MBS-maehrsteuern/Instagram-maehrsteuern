// Frames rendern: node render.mjs <seite.html> <dauer_s> <ordner> [probe-zeiten,…]
// Ruft window.zeichne(t) auf (nicht render). Ohne Probe-Zeiten: f00000.jpg … mit 30 fps; mit Probe-Zeiten nur PNG-Einzelbilder.
import { createRequire } from "module";
import { execSync } from "child_process";
let chromium;
try { ({ chromium } = await import("playwright")); }
catch { ({ chromium } = createRequire(execSync("npm root -g").toString().trim() + "/")("playwright")); }
import { mkdirSync } from "fs";
import { resolve } from "path";
const [seite, dauer, ziel, probe] = process.argv.slice(2);
mkdirSync(ziel, { recursive: true });
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });  // transparente PNGs fürs Überlagern
await p.goto("file://" + resolve(seite));
await p.evaluate(async () => {
  await Promise.all(['100px Anton', '100px "Bowlby One"', '100px "Permanent Marker"', '100px Inter'].map(f => document.fonts.load(f, "AÄÖÜß…")));
  await document.fonts.ready;
});
await p.evaluate(() => { window.zeichne(0); });
if (probe) {
  for (const t of probe.split(",")) { await p.evaluate(t => window.zeichne(t), +t); await p.screenshot({ path: `${ziel}/probe_${t}.png`, omitBackground: true }); }
  await b.close(); process.exit(0);
}
const n = Math.round(+dauer * 30);
for (let i = 0; i < n; i++) {
  await p.evaluate(t => window.zeichne(t), i / 30);
  await p.screenshot({ path: `${ziel}/o${String(i).padStart(5, "0")}.png`, omitBackground: true });
}
await b.close();
console.log("fertig", n, "Frames");
