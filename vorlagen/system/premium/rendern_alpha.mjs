// Overlay rendern mit transparentem Hintergrund: node rendern_alpha.mjs <seite.html> <dauer_s> <ziel> [probe-zeiten]
import { createRequire } from "module"; import { execSync } from "child_process";
let chromium; try { ({ chromium } = await import("playwright")); }
catch { ({ chromium } = createRequire(execSync("npm root -g").toString().trim() + "/")("playwright")); }
import { mkdirSync } from "fs"; import { resolve } from "path";
const [seite, dauer, ziel, probe] = process.argv.slice(2);
mkdirSync(ziel, { recursive: true });
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto("file://" + resolve(seite)); await p.evaluate(() => document.fonts.ready);
const shot = (t, pfad) => p.evaluate(t => window.render(t), t).then(() => p.screenshot({ path: pfad, omitBackground: true }));
if (probe) { for (const t of probe.split(",")) await shot(+t, `${ziel}/probe_${t}.png`); await b.close(); process.exit(0); }
const n = Math.round(+dauer * 30);
for (let i = 0; i < n; i++) await shot(i / 30, `${ziel}/f${String(i).padStart(5, "0")}.png`);
await b.close(); console.log("✓", n, "Frames");
