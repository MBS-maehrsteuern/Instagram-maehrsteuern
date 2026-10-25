"""Reel 60 „Geld verschenkt“ (15.10.2026): Stimme (3 Takes) + Hook-Foto, Karten, Frist 31.12.2026 (2022) + Abspann.

Reihenfolge:  1) python3 p60_stimme_bauen.py     (Stimme schneiden + transkribieren)
              2) python3 p60_reel_geld_verschenkt_bauen.py   (Hintergründe, Grafiken, Job-JSON, Render mit montage.py, Titelbild, Story)
"""
import json, subprocess, sys
from datetime import date
from pathlib import Path
import numpy as np, imageio_ffmpeg
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
from PIL import Image, ImageDraw, ImageFont

hier = Path(__file__).resolve().parent
SYS = hier.parent
REPO = SYS.parent.parent
P = "posts/60_2026-10-15_reel_geld_verschenkt"
B = REPO / P / "bausteine"; B.mkdir(parents=True, exist_ok=True)
FONT = str(SYS / "schriften/Outfit-Bold.ttf")
W, H = 1080, 1920
VERSATZ = 0.10      # Luft vor dem ersten Wort
ENDKARTE = 1.5
X, BREITE = 465, 820   # Text-Mitte und -Breite: rechts 150 px frei
TAGE = (date(2026, 12, 31) - date(2026, 10, 15)).days
assert TAGE == 77

# ---------- Wörter ----------
w = json.loads((REPO / P / "ton/stimme_schnitt_woerter.json").read_text())
SAETZE = [(0, 10), (11, 20), (21, 28), (29, 31), (32, 44), (45, 50), (51, 59)]
assert len(w) == 60 and w[0][0] == "Im" and w[59][0].startswith("macht") and w[35][0] == "2022" and w[50][0].startswith("weg"), [x[0] for x in w]
t0 = lambda i: w[i][1] + VERSATZ
t1 = lambda i: w[i][2] + VERSATZ
STIMME_ENDE = t1(59)
grenzen = [0.0] + [round((t1(SAETZE[i][1]) + t0(SAETZE[i + 1][0])) / 2, 3) for i in range(6)] + [round(STIMME_ENDE + 0.12, 3)]
GESAMT = round(grenzen[-1] + ENDKARTE, 3)
# Untertitel: wörtlich nach Vorgabe, 2–4 Wörter; je Chunk (Token von, bis, Läufe)
G, WS = "gruen", "weiss"
CHUNKS = [
    (0, 1, [("Im Finanzamt", WS)]), (2, 5, [("hab ich jeden Tag", WS)]), (6, 8, [("gesehen, wie Leute", WS)]), (9, 10, [("Geld", WS), ("verschenken.", G)]),
    (11, 13, [("Nicht, weil sie", WS)]), (14, 15, [("tricksen – sondern", WS)]), (16, 18, [("weil sie gar", WS)]), (19, 20, [("nichts", G), ("abgeben.", WS)]),
    (21, 22, [("Wer keine", WS)]), (23, 24, [("Steuererklärung machen", WS)]), (25, 26, [("muss, darf", WS)]), (27, 28, [("trotzdem", G), ("abgeben.", WS)]),
    (29, 31, [("Vier Jahre", G), ("rückwirkend.", WS)]),
    (32, 35, [("Das heißt: Für", WS), ("2022", G)]), (36, 39, [("hast du nur noch", WS)]), (40, 43, [("bis", WS), ("31. Dezember 2026", G)]), (44, 44, [("Zeit.", WS)]),
    (45, 47, [("Danach ist das", WS)]), (48, 50, [("Geld einfach", WS), ("weg.", G)]),
    (51, 53, [("Schick", G), ("das dem,", WS)]), (54, 56, [("der seit Jahren", WS)]), (57, 59, [("keine Erklärung macht.", WS)]),
]
SPRACHE = " ".join(" ".join(t for t, _ in r) for _, _, r in CHUNKS)


# ---------- Hilfen ----------
def breite_px(txt, g):
    f = ImageFont.truetype(FONT, g); s = round(g * 0.075)
    b = ImageDraw.Draw(Image.new("L", (10, 10))).textbbox((0, 0), txt, font=f, stroke_width=s)
    return b[2] - b[0]


def passend(zeilen, g0, breite=BREITE):
    """Gemeinsame Schriftgröße, bei der die breiteste Zeile in 'breite' passt."""
    return min(g0, int(g0 * breite / max(breite_px(z, g0) for z in zeilen)))


def zeilen_text(zeilen, g0, y0, abstand, farben, ab0, schritt, bis=None, g_max=None):
    g = passend(zeilen, g0)
    out = []
    for i, (z, f) in enumerate(zip(zeilen, farben)):
        e = {"wort": z, "farbe": f, "groesse": g, "y": y0 + i * abstand, "x": X, "breite": BREITE, "ab": round(ab0 + i * schritt, 2)}
        if bis: e["bis"] = bis
        out.append(e)
    return out


def verlauf():
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    t = np.clip(np.sqrt(((x - 540) / 780) ** 2 + ((y - 806) / 1100) ** 2), 0, 1)
    c0, c1 = np.array([0x12, 0x30, 0x2A], np.float32), np.array([0x0B, 0x11, 0x0E], np.float32)
    return Image.fromarray((c0 + (c1 - c0) * t[..., None]).astype(np.uint8))


def foto_hintergrund(kopf_y, breite, ziel, unten_dunkel=True):
    bg = verlauf().convert("RGBA")
    # weicher grüner Schein hinter dem Kopf
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    cy = kopf_y + 260
    a = np.clip(1 - np.sqrt(((x - 540) / 520) ** 2 + ((y - cy) / 520) ** 2), 0, 1) ** 1.6 * 0.55
    glow = np.zeros((H, W, 4), np.uint8); glow[..., 0], glow[..., 1], glow[..., 2], glow[..., 3] = 0x2B, 0x8C, 0x74, (a * 255).astype(np.uint8)
    bg.alpha_composite(Image.fromarray(glow, "RGBA"))
    f = Image.open(REPO / "assets/marke/loris_aktuell_freisteller.png").convert("RGBA")
    s = breite / f.width
    f = f.resize((round(f.width * s), round(f.height * s)), Image.LANCZOS)
    bg.alpha_composite(f, (round((W - f.width) / 2), kopf_y - round(10 * s)))
    if unten_dunkel:  # Verlauf für lesbare Untertitel
        d = np.zeros((H, W, 4), np.uint8); yy = np.clip((np.arange(H) - 1150) / 350, 0, 1)
        d[..., 3] = (yy[:, None] * 0.55 * 255).astype(np.uint8)
        bg.alpha_composite(Image.fromarray(d, "RGBA"))
    bg.convert("RGB").save(ziel)


def render(job_name, bilder, ausgabe):
    job = SYS / "jobs" / f"{job_name}.json"
    job.write_text(json.dumps({"ausgabe": ausgabe, "bilder": bilder}, ensure_ascii=False, indent=1))
    subprocess.run(["node", "render.mjs", f"jobs/{job_name}.json"], cwd=SYS, check=True, capture_output=True)


# ---------- Hintergründe ----------
foto_hintergrund(760, 880, B / "bg_foto.png")
verlauf().save(B / "bg_karte.png")

# ---------- Grafiken ----------
YEARS = [("2022", 315, 840), ("2023", 615, 840), ("2024", 315, 985), ("2025", 615, 985)]
UHR_WINKEL = [0, 24, 48, 72, 96, 120]
bilder = [
    {"vorlage": "p60_ebenen", "transparent": True, "datei": "ebene_dokument.png", "typ": "dokument", "x": X, "y": 1020},
    *[{"vorlage": "p60_ebenen", "transparent": True, "datei": f"ebene_jahr_{j}.png", "typ": "jahr", "text": j, "x": x, "y": y, "hell": j == "2022"} for j, x, y in YEARS],
    {"vorlage": "p60_ebenen", "transparent": True, "datei": "ebene_kalender.png", "typ": "kalender", "x": 320, "y": 1000},
    *[{"vorlage": "p60_ebenen", "transparent": True, "datei": f"ebene_uhr_{i}.png", "typ": "uhr", "winkel": a, "x": 620, "y": 1000} for i, a in enumerate(UHR_WINKEL)],
    {"vorlage": "p60_ebenen", "transparent": True, "datei": "ebene_tage.png", "typ": "tage", "text": str(TAGE), "x": X, "y": 1250},
    {"vorlage": "p60_ebenen", "transparent": True, "datei": "ebene_muenze.png", "typ": "muenze", "x": X, "y": 960},
    {"vorlage": "p60_ebenen", "transparent": True, "datei": "ebene_strich.png", "typ": "strich", "x": X, "y": 960},
    {"vorlage": "p60_ebenen", "transparent": True, "datei": "ebene_flieger.png", "typ": "flieger", "x": 420, "y": 1000},
    {"vorlage": "einblendung", "datei": "abspann.png", "typ": "abspann", "kicker": "Steuern × Code", "titel": "Steuerwissen,\ndas *rechnet.*",
     "chip": "@maehrsteuern folgen", "sub": "Kurz erklärt – ohne Fachchinesisch."},
]
render("p60_reel_bausteine", bilder, f"../../{P}/bausteine")

# ---------- Szenen ----------
def sub_eintraege(sa, sb, szene_start, szene_ende):
    """Untertitel-Chunks einer Szene (Zeiten relativ zum Szenenanfang)."""
    out = []
    chunks = [c for c in CHUNKS if sa <= c[0] <= sb]
    for k, (a, b, runs) in enumerate(chunks):
        ab = t0(a)
        nxt = t0(chunks[k + 1][0]) if k + 1 < len(chunks) else None
        bis = nxt if nxt is not None and nxt - t1(b) < 0.5 else min(t1(b) + 0.3, szene_ende)
        bis = min(bis, szene_ende)
        out.append({"teile": [[t, f] for t, f in runs], "groesse": 72, "y": 1385, "x": X, "breite": 800,
                    "ab": round(max(ab - 0.04 - szene_start, 0), 2), "bis": round(bis - szene_start, 2)})
    return out


S = grenzen
dau = lambda i: round(S[i + 1] - S[i], 3)
rel = lambda i: (lambda tok: round(t0(tok) - S[i], 2))   # Wortstart relativ zur Szene i
foto = "../../" + P + "/bausteine/bg_foto.png"; karte = "../../" + P + "/bausteine/bg_karte.png"
eb = lambda n: f"../../{P}/bausteine/{n}.png"
szenen = []

# a: Hook auf dem Foto, langsamer Push-in
hook = zeilen_text(["Im Finanzamt", "hab ich gesehen,", "wie Leute", "Geld verschenken."], 112, 300, 112, [WS, WS, WS, G], 0.3, 0.3, bis=dau(0))
szenen.append({"karte": foto, "dauer": dau(0), "von": [540, 960, 1080], "nach": [540, 1010, 1000], "text": hook + sub_eintraege(0, 10, S[0], S[1])})
# b: dunkler, Textkarte
b_txt = zeilen_text(["Nicht tricksen.", "Nichts abgeben."], 140, 360, 140, [WS, G], 0.1, 0.45, bis=dau(1))
szenen.append({"karte": foto, "dauer": dau(1), "von": [540, 1010, 1000], "nach": [540, 1040, 940], "abdunkeln": 0.35, "text": b_txt + sub_eintraege(11, 20, S[1], S[2])})
# c: Keine Pflicht? Trotzdem abgeben.
c_txt = zeilen_text(["Keine Pflicht?"], 150, 340, 0, [WS], 0.15, 0, bis=dau(2)) + \
        [{**e, "ab": rel(2)(26) - 0.1 + k * 0.35} for k, e in enumerate(zeilen_text(["Trotzdem", "abgeben."], 190, 530, 175, [G, G], 0, 0, bis=dau(2)))]
szenen.append({"karte": karte, "dauer": dau(2), "text": c_txt + sub_eintraege(21, 28, S[2], S[3]),
               "ebenen": [{"datei": eb("ebene_dokument"), "ab": rel(2)(27), "pop": True, "pivot": [X, 1020]}]})
# d: 4 Jahre rückwirkend + Jahreszahlen
d_txt = zeilen_text(["4 Jahre"], 240, 390, 0, [G], 0.05, 0, bis=dau(3)) + zeilen_text(["rückwirkend"], 120, 575, 0, [WS], 0.3, 0, bis=dau(3))
d_eb = [{"datei": eb(f"ebene_jahr_{j}"), "ab": round(0.2 + k * 0.17, 2), "pop": True, "pivot": [x, y]} for k, (j, x, y) in enumerate(YEARS)]
szenen.append({"karte": karte, "dauer": dau(3), "text": d_txt + sub_eintraege(29, 31, S[3], S[4]), "ebenen": d_eb})
# e: Held 2022 + Frist + Uhr
e0 = S[4]
tick = [round(0.45 + k, 2) for k in range(6)]  # Ticks der Uhr-Atmo (jeweils eine Sekunde)
uhr_ab = rel(4)(40) + 0.05
uhr_eb = []
for i, a in enumerate(UHR_WINKEL):
    start = next(x for x in tick if x >= uhr_ab) + i  # Zeiger springt mit jedem Tick
    uhr_eb.append({"datei": eb(f"ebene_uhr_{i}"), "ab": round(start if i else uhr_ab, 2), "bis": round(start + 1, 2) if i < len(UHR_WINKEL) - 1 else dau(4),
                   "pop": i == 0, "pivot": [620, 1000]})
# Uhr-Layer 0 läuft bis zum ersten Sprung
uhr_eb[0]["bis"] = uhr_eb[1]["ab"]
e_txt = zeilen_text(["2022"], 380, 480, 0, [G], 0.0, 0, bis=dau(4))
e_txt[0]["ab"] = rel(4)(35) - 0.05
e_txt += [{"teile": [["bis", WS], ["31.12.2026", G]], "groesse": 120, "y": 770, "x": X, "breite": BREITE, "ab": rel(4)(40) - 0.05, "bis": dau(4)}]
szenen.append({"karte": karte, "dauer": dau(4), "text": e_txt + sub_eintraege(32, 44, S[4], S[5]),
               "ebenen": [{"datei": eb("ebene_kalender"), "ab": rel(4)(41), "pop": True, "pivot": [320, 1000]}, *uhr_eb,
                          {"datei": eb("ebene_tage"), "ab": rel(4)(42) + 0.1, "pop": True, "pivot": [X, 1250]}]})
# f: Danach: Geld weg.
f_txt = zeilen_text(["Danach:"], 140, 330, 0, [WS], 0.1, 0, bis=dau(5)) + zeilen_text(["Geld weg."], 210, 510, 0, [G], rel(5)(48) - 0.05, 0, bis=dau(5))
szenen.append({"karte": karte, "dauer": dau(5), "text": f_txt + sub_eintraege(45, 50, S[5], S[6]),
               "ebenen": [{"datei": eb("ebene_muenze"), "ab": 0.1, "pop": True, "pivot": [X, 960], "verblassen": [rel(5)(48), rel(5)(50) + 0.25, 0.12]},
                          {"datei": eb("ebene_strich"), "ab": rel(5)(50) - 0.05, "pop": True, "pivot": [X, 960]}]})
# g: Teilen
g_txt = zeilen_text(["Schick das"], 180, 340, 0, [G], 0.1, 0, bis=dau(6)) + \
        zeilen_text(["dem, der seit Jahren", "keine Erklärung macht."], 100, 505, 105, [WS, WS], 0.45, 0.35, bis=dau(6))
szenen.append({"karte": karte, "dauer": dau(6), "text": g_txt + sub_eintraege(51, 59, S[6], S[7]),
               "ebenen": [{"datei": eb("ebene_flieger"), "ab": 0.5, "pop": True, "pivot": [420, 1000], "drift": [170, -110, 1.7]}]})
# Abspann
szenen.append({"karte": eb("abspann"), "dauer": round(GESAMT - S[7], 3)})

ton = [{"datei": f"../../{P}/ton/stimme_schnitt.wav", "ab": VERSATZ, "lautstaerke": 1.0, "ein": 0.01, "aus": 0.3},
       {"datei": "../../musik/07_runway_minimal_tech.mp3", "ab": round(S[2], 2), "start": 0.4, "lautstaerke": 0.12, "ein": 0.8, "aus": 0.8},
       {"datei": "../../musik/atmo/uhr_ticken.mp3", "ab": round(e0, 2), "start": 0, "dauer": 4.0, "lautstaerke": 0.22, "ein": 0.05, "aus": 0.1},
       {"datei": "../../musik/atmo/uhr_ticken.mp3", "ab": round(e0 + 4.0, 2), "start": 0, "dauer": round(dau(4) - 4.0, 2), "lautstaerke": 0.22, "ein": 0.02, "aus": 0.3}]
cfg = {"ausgabe": f"../../{P}/reel.mp4", "fps": 30, "quellen": {}, "szenen": szenen, "ton": ton}
(hier / "p60_reel_geld_verschenkt.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=1))
print("Sprache:", SPRACHE)
print("Szenen:", [round(x, 2) for x in S], "Gesamt", GESAMT)
if "nur_job" in sys.argv: sys.exit()
subprocess.run([sys.executable, str(SYS / "montage.py"), str(hier / "p60_reel_geld_verschenkt.json")], check=True, cwd=SYS)

# ---------- Titelbild + Story ----------
foto_hintergrund(930, 900, B / "bg_titel.png", unten_dunkel=False)
render("p60_titelbild", [{"vorlage": "reel_titel", "datei": "titelbild.png", "kicker": "Steuern × Code", "titel": "Geld *verschenkt* –\nnur weil du\nnichts abgibst?",
                          "bild": f"../../{P}/bausteine/bg_titel.png", "scharf": True, "oben": 300, "chip": False, "groesse": 92}], f"../../{P}")
subprocess.run([FFMPEG, "-loglevel", "error", "-y", "-ss", "14.0", "-i", str(REPO / P / "reel.mp4"), "-frames:v", "1", str(B / "frame_2022.png")], check=True)
Image.open(B / "frame_2022.png").convert("RGB").crop((0, 300, 1080, 1068)).resize((900, 640)).save(B / "story_karte.png")  # Standbild „2022“ als Vorschau
render("p60_story", [{"vorlage": "story", "typ": "teaser", "datei": "story_reel_teaser.png", "kicker": "Neues Reel 🔥", "titel": "Für *2022* läuft die Frist ab – bis 31.12.2026",
                      "bild": f"../../{P}/bausteine/story_karte.png", "hint": "Jetzt im Feed ansehen"}], f"../../{P}")
print("fertig")
