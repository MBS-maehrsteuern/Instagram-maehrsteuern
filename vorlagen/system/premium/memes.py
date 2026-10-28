"""Memes als Story-Bilder (1080×1920) im maehrsteuern-Look – eigene Texte und eigene Fotos, keine fremden Figuren
(Loris 28.10.: „humorvoll als fertige Beiträge“). python3 vorlagen/system/premium/memes.py → posts/memes_2026-10/meme_N.png"""
import subprocess, tempfile
from pathlib import Path
HIER = Path(__file__).resolve().parent; REPO = HIER.parent.parent.parent; ZIEL = REPO / "posts/memes_2026-10"
KOPF = """<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../../schriften.css"><style>
@font-face{font-family:"Outfit";src:url(../schriften/Outfit-Bold.ttf);font-weight:700}
*{box-sizing:border-box;margin:0}html,body{width:1080px;height:1920px;overflow:hidden;background:#070C0A;color:#EEF4F0;font-family:"IBM Plex Sans",sans-serif}
#bg{position:absolute;inset:0;background:radial-gradient(900px 700px at 30% 22%,rgba(83,195,162,.18),transparent 70%),radial-gradient(700px 600px at 85% 85%,rgba(83,195,162,.08),transparent 70%)}
.k{position:absolute;left:80px;top:170px;font-family:"IBM Plex Mono",monospace;font-size:30px;letter-spacing:.22em;color:#B9C9C0;display:flex;gap:16px;align-items:center}
.k i{width:16px;height:16px;border-radius:50%;background:#53C3A2;box-shadow:0 0 18px #53C3A2}
.karte{position:absolute;left:70px;right:70px;top:50%;transform:translateY(-50%);background:#0D1613;border:1px solid #1E3A31;border-radius:36px;padding:56px 50px;box-shadow:0 0 70px rgba(83,195,162,.14)}
h1{font-family:"Outfit";font-weight:700;font-size:64px;line-height:1.1;letter-spacing:-.02em}
.g{color:#7FE0C2}.r{color:#E07A6B}.y{color:#E8B04A}
.zwei{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:40px}
.p{border-radius:24px;overflow:hidden;background:#111d19;border:1px solid #1E3A31}
.p .t{position:relative;z-index:2;background:#111d19;font-family:"Outfit";font-weight:700;font-size:40px;padding:22px 22px 16px;line-height:1.1}
.p img{width:100%;height:560px;position:relative;object-fit:cover;display:block}
.datei{font-family:"IBM Plex Mono",monospace;font-size:40px;padding:22px 26px;border:1px solid #1E3A31;border-radius:18px;margin-top:22px;background:#0a1210;display:flex;gap:18px;align-items:center}
.datei b{color:#53C3A2}.zeile{font-family:"Outfit";font-weight:700;font-size:54px;line-height:1.15;margin-top:34px}
.mono{font-family:"IBM Plex Mono",monospace;font-size:34px;color:#B9C9C0}
.fuss{position:absolute;left:80px;right:80px;bottom:150px;display:flex;justify-content:space-between;align-items:center;font-family:"IBM Plex Mono",monospace;font-size:32px;color:#B9C9C0}
.fuss span{display:flex;gap:14px;align-items:center}.fuss i{width:20px;height:20px;border-radius:50%;background:#53C3A2;box-shadow:0 0 18px #53C3A2}
</style></head><body><div id="bg"></div><div class="k"><i></i>STEUER-MEME · {KICK}</div><div class="karte">{INHALT}</div>
<div class="fuss"><span><i></i>@maehrsteuern</span><span>Schick's jemandem ↗</span></div>
<script>window.render=()=>{}</script></body></html>"""
B = "../../../posts/memes_2026-10/"
MEMES = [
 ("FINANZAMT", '<h1>Ich: „Das setz ich einfach ab.“</h1><div class="zeile">Das Finanzamt:</div>'
  '<div style="margin-top:40px;text-align:center"><span style="display:inline-block;transform:rotate(-6deg);border:6px solid #E07A6B;color:#E07A6B;border-radius:18px;padding:18px 40px;font-family:Outfit;font-weight:700;font-size:96px;letter-spacing:.04em">ANGEMESSEN?</span></div>'
  '<div class="zeile" style="font-size:44px;color:#B9C9C0;margin-top:50px">Jeder Ausgabe ihr Moment der Wahrheit.</div>'),
 ("MEIN WEG", '<h1>Frisch geprüft im Finanzamt</h1><div class="zwei"><div class="p"><div class="t">Tag der Diplomierung</div><img src="%s1_urkunde.jpg" style="object-position:58%% 12%%"></div>'
  '<div class="p"><div class="t">Zwei Jahre später, <span class="y">Plan B</span></div><div style="height:560px;overflow:hidden"><img src="%s6_maske.jpg" style="object-position:50%% 50%%;transform:scale(1.5)"></div></div></div>' % (B, B)),
 ("EXCEL", '<h1>Die Steuer-Datei im Laufe des Jahres</h1>'
  '<div class="datei">📄 <span>Steuer<b>.xlsx</b></span></div><div class="datei">📄 <span>Steuer_final<b>.xlsx</b></span></div>'
  '<div class="datei">📄 <span>Steuer_final_v2<b>.xlsx</b></span></div><div class="datei">📄 <span>Steuer_final_WIRKLICH<b>.xlsx</b></span></div>'
  '<div class="datei" style="border-color:#E07A6B">📄 <span class="r">Steuer_final_v7_NEU(2)<b>.xlsx</b></span></div>'
  '<div class="zeile" style="font-size:44px;color:#B9C9C0">Und der Prüfer fragt: „Welche gilt?“</div>'),
 ("BESCHEID", '<h1>Der Steuerbescheid liegt seit 5 Wochen ungeöffnet in der Schublade.</h1>'
  '<div class="zeile">Die Einspruchsfrist:</div><div style="font-size:220px;text-align:center;margin-top:30px">👋</div>'
  '<div class="mono" style="margin-top:20px;text-align:center">1 Monat ab Bekanntgabe · § 355 AO</div>'),
 ("BELEGE", '<h1>Belege sortieren</h1><div class="zwei">'
  '<div class="p" style="padding:30px"><div class="t" style="padding:0 0 20px">Im Januar</div><div class="mono">„Dieses Jahr mach ich alles sofort digital.“</div><div style="font-size:150px;text-align:center;margin-top:40px">🗂️</div></div>'
  '<div class="p" style="padding:30px"><div class="t" style="padding:0 0 20px"><span class="y">Im Juli</span></div><div class="mono">Ein Schuhkarton. Drei Tankquittungen. Ein Kassenzettel vom Bäcker.</div><div style="font-size:150px;text-align:center;margin-top:40px">📦</div></div></div>'),
]
for n, (kick, inhalt) in enumerate(MEMES, 1):
    h = HIER / f"_meme_{n}.html"; h.write_text(KOPF.replace("{KICK}", kick).replace("{INHALT}", inhalt))
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["node", "rendern.mjs", h.name, "1", tmp, "0.03"], cwd=HIER, check=True, capture_output=True)
        png = next(Path(tmp).glob("*.png")); subprocess.run(["cp", png, ZIEL / f"meme_{n}.png"], check=True)
    h.unlink(); print("✓", ZIEL / f"meme_{n}.png")
