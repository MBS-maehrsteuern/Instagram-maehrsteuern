// Premium-Karussell rendern: node karussell.mjs karussells/<name>.json  → PNGs 1080×1440 in "ausgabe" (relativ zur Job-Datei)
// Job: { "ausgabe": "../../../../posts/<ordner>", "folien": [ { "datei": "folie_01.png", "kicker", "h1", "h2", "sub", "panel": {…}, "norm" }, … ] }
import { readFileSync } from "fs";
import { resolve, dirname } from "path";
import { createRequire } from "module";
import { execSync } from "child_process";
let chromium;
try { ({ chromium } = await import("playwright")); }
catch { ({ chromium } = createRequire(execSync("npm root -g").toString().trim() + "/")("playwright")); }
const jobPfad = resolve(process.argv[2]);
const job = JSON.parse(readFileSync(jobPfad, "utf8"));
const ziel = resolve(dirname(jobPfad), job.ausgabe);
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1080, height: 1440 } });
await p.goto("file://" + resolve(dirname(new URL(import.meta.url).pathname), "karussell.html"));
await p.evaluate(() => document.fonts.ready);
let fehler = 0;
for (const [i, f] of job.folien.entries()) {
  const r = await p.evaluate(([f, n, g]) => window.zeichne(f, n, g), [f, i + 1, job.folien.length]);
  await p.screenshot({ path: `${ziel}/${f.datei}` });
  if (r !== "ok") { fehler++; console.log("⚠", f.datei, r); }
}
await b.close();
console.log(fehler ? `✗ ${fehler} Folie(n) zu hoch` : `✓ ${job.folien.length} Folien → ${ziel}`);
