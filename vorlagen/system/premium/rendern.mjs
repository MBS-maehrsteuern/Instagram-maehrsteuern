// Premium-Reel rendern: node rendern.mjs <seite.html> <dauer_s> <ausgabe_ordner> [probe-zeiten,…]  → Frames als JPG (30 fps)
// Mit Probe-Zeiten (z. B. 0.05,4,12) nur diese Einzelbilder als PNG – zum Ansehen vor dem vollen Rendern.
import { createRequire } from "module";
import { execSync } from "child_process";
let chromium;  // wie render.mjs: lokal oder global installiertes Playwright
try { ({ chromium } = await import("playwright")); }
catch { ({ chromium } = createRequire(execSync("npm root -g").toString().trim() + "/")("playwright")); }
import { mkdirSync } from "fs";
import { resolve } from "path";
const [seite, dauer, ziel, probe] = process.argv.slice(2);
mkdirSync(ziel, { recursive: true });
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto("file://" + resolve(seite));
await p.evaluate(() => document.fonts.ready);
if (probe) {
  for (const t of probe.split(",")) { await p.evaluate(t => window.render(t), +t); await p.screenshot({ path: `${ziel}/probe_${t}.png` }); }
  await b.close(); process.exit(0);
}
const n = Math.round(+dauer * 30);
for (let i = 0; i < n; i++) {
  await p.evaluate(t => window.render(t), i / 30);
  await p.screenshot({ path: `${ziel}/f${String(i).padStart(5, "0")}.jpg`, type: "jpeg", quality: 92 });
}
await b.close();
console.log("✓", n, "Frames");
