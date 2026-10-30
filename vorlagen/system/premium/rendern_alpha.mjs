// Overlay rendern mit transparentem Hintergrund: node rendern_alpha.mjs <seite.html> <dauer_s> <ziel> [probe-zeiten | mapping.json]
// mapping.json {zeiten:[…]} = je Frame die Overlay-Zeit (nach Pausen-Kürzung im Schnitt bleiben Karten/Untertitel synchron)
import { createRequire } from "module"; import { execSync } from "child_process";
let chromium; try { ({ chromium } = await import("playwright")); }
catch { ({ chromium } = createRequire(execSync("npm root -g").toString().trim() + "/")("playwright")); }
import { mkdirSync, readFileSync } from "fs"; import { resolve } from "path";
const [seite, dauer, ziel, probe] = process.argv.slice(2);
mkdirSync(ziel, { recursive: true });
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto("file://" + resolve(seite)); await p.evaluate(() => document.fonts.ready);
const shot = (t, pfad) => p.evaluate(t => window.render(t), t).then(() => p.screenshot({ path: pfad, omitBackground: true }));
const karte = probe && probe.endsWith(".json") ? JSON.parse(readFileSync(probe)).zeiten : null;
if (probe && !karte) { for (const t of probe.split(",")) await shot(+t, `${ziel}/probe_${t}.png`); await b.close(); process.exit(0); }
const n = karte ? karte.length : Math.round(+dauer * 30);
for (let i = 0; i < n; i++) await shot(karte ? karte[i] : i / 30, `${ziel}/f${String(i).padStart(5, "0")}.png`);
await b.close(); console.log("✓", n, "Frames");
