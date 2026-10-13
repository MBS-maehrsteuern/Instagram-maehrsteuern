"""Tagesbericht als Bild:  python3 automatik/tagesbericht.py [JJJJ-MM-TT]

Liest die neueste (bzw. angegebene) und die vorherige automatik/statistik/insights_*.json und schreibt
automatik/berichte/tagesbericht_<datum>.html, .png (1080 breit) und .json (Kennzahlen + Methoden-Check
für die Einschätzung). Bild per Playwright (global installiert, Chromium aus /opt/pw-browsers).
"""
import json, subprocess, sys, html
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ST = ROOT / "automatik/statistik"
OUT = ROOT / "automatik/berichte"
START = "2026-09-29"  # Neustart der Seite; ältere Beiträge zählen nicht als Maßstab

dateien = sorted(ST.glob("insights_*.json"))
if len(sys.argv) > 1:
    dateien = [d for d in dateien if d.stem.split("_")[1] <= sys.argv[1]]
heute_f, vor_f = dateien[-1], (dateien[-2] if len(dateien) > 1 else None)
d = json.loads(heute_f.read_text())
v = json.loads(vor_f.read_text()) if vor_f else {}
# Vortag = Stand des letzten Berichts (Morgen-Schnappschuss), nicht die tagsüber überschriebene insights-Datei
OUT.mkdir(parents=True, exist_ok=True)
basis = sorted(p for p in OUT.glob("basis_*.json") if p.stem.split("_")[1] < d["abgerufen"])
if basis:
    v = json.loads(basis[-1].read_text())
# Läuft der Bericht mehrmals am Tag: aktive Zeiten aus dem früheren Abruf behalten, wenn der neue keine liefert
_bf = OUT / f"basis_{d['abgerufen']}.json"
if _bf.exists() and not any((d.get("online_follower") or {}).values()):
    _alt = json.loads(_bf.read_text()).get("online_follower") or {}
    if any(_alt.values()): d["online_follower"] = _alt
_bf.write_text(json.dumps(d, ensure_ascii=False))
tag = d["abgerufen"]
plan = json.loads((ROOT / "automatik/plan.json").read_text())["eintraege"]

def zahl(x):
    return "–" if x is None else f"{x:,.0f}".replace(",", ".")

def delta(a, b):
    if a is None or b is None or a == b: return ""
    return f'<span class="d {"up" if a > b else "down"}">{"+" if a > b else "−"}{zahl(abs(a - b))}</span>'

def pct(q, n=0):
    return "–" if q is None else f"{q*100:.{n}f} %".replace(".", ",")

def quote(a, b):
    return None if not b or a is None else a / b

k, kv = d["konto"], v.get("konto", {})
fol, fol_v = k["followers_count"], kv.get("followers_count")
tw = d["tageswerte_reichweite"]
tage = sorted(t for t in tw if t < tag)[-14:]  # nur abgeschlossene Tage; ein Abruf am Nachmittag enthält schon den laufenden Tag
gestern = tage[-1] if tage else None
r_gestern = tw.get(gestern)
r_vortag = tw.get(tage[-2]) if len(tage) > 1 else None
m30 = d["konto_verlauf"][0]
nf = m30["reach"]["aufgeteilt"].get("NON_FOLLOWER", 0); ff = m30["reach"]["aufgeteilt"].get("FOLLOWER", 0)
nf_quote = quote(nf, nf + ff)
links = (m30.get("profile_links_taps") or {}).get("gesamt") or 0

# Beiträge seit Neustart
vor_bt = {b["id"]: b for b in v.get("beitraege", [])}
bt = [b for b in d["beitraege"] if b["timestamp"][:10] >= START]
bt.sort(key=lambda b: b["timestamp"], reverse=True)
plan_link = {e.get("link"): e for e in plan if e.get("link")}
BERLIN = ZoneInfo("Europe/Berlin")
FEED = {"REELS": "reel", "CAROUSEL_ALBUM": "karussell", "IMAGE": "bild"}

def _utc(ts):
    return datetime.strptime(ts[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)

def _plan_zeit(e):
    return datetime.strptime(str(e["zeit"])[:16].replace("T", " "), "%Y-%m-%d %H:%M").replace(tzinfo=BERLIN)

def _erste_zeile(e):
    f = ROOT / e.get("ordner", "") / e.get("text", "")
    try: return f.read_text().strip().split("\n")[0][:40] if e.get("text") and f.is_file() else ""
    except OSError: return ""

def plan_eintrag(b):
    """Plan-Eintrag zu einem Beitrag: per Link, sonst (von Hand gepostet) gleicher Typ ±90 Min. um die Planzeit
    oder gleiche erste Zeile der Bildunterschrift."""
    e = plan_link.get(b.get("permalink"))
    if e: return e
    typ = "reel" if b.get("media_product_type") == "REELS" else FEED.get(b.get("media_type"))
    kand = [x for x in plan if x.get("typ") == typ and not x.get("link") and x.get("zeit")]
    t = _utc(b["timestamp"])
    nah = [x for x in kand if abs((_plan_zeit(x) - t).total_seconds()) <= 5400]
    if nah: return min(nah, key=lambda x: abs((_plan_zeit(x) - t).total_seconds()))
    z1 = (b.get("caption") or "").strip().split("\n")[0][:40]
    return next((x for x in kand if z1 and _erste_zeile(x) == z1), None)

def name(b):
    e = plan_eintrag(b)
    if e: return e["id"]
    return (b.get("caption") or "").split("\n")[0][:34]

# Bezugszeit für das Alter der Beiträge: jetzt, wenn der Bericht für heute läuft, sonst 09:00 Ortszeit des Berichtstags
REIF_H = 48  # erst ab diesem Alter werden Beiträge im Methoden-Check bewertet (frühe Werte wandern noch)
_jetzt = datetime.now(timezone.utc)
_bezug_tag = datetime.strptime(tag, "%Y-%m-%d").replace(hour=7, tzinfo=timezone.utc)  # 09:00 MESZ
bezug = _jetzt if (_jetzt + timedelta(hours=2)).strftime("%Y-%m-%d") == tag else _bezug_tag

def alter_h(ts):
    t = datetime.strptime(ts[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
    return max(0.0, (bezug - t).total_seconds() / 3600)

def nf_anteil(b):
    """Nicht-Follower-Anteil an der Reichweite eines Beitrags, falls Instagram die Aufteilung liefert."""
    r = b.get("reach_aufgeteilt") or {}
    a = r.get("aufgeteilt") if isinstance(r, dict) else None
    if not a: return None
    nf_, f_ = a.get("NON_FOLLOWER", 0), a.get("FOLLOWER", 0)
    return nf_ / (nf_ + f_) if nf_ + f_ else None

LAENGEN = ST / "laengen.json"  # Cache: Reel-Länge je Media-ID (aus Videodatei oder media_url)
_laengen = json.loads(LAENGEN.read_text()) if LAENGEN.exists() else {}

def _ffprobe(quelle):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(quelle)],
                             capture_output=True, text=True, timeout=60).stdout.strip()
        return round(float(out), 1) if out else None
    except (OSError, ValueError, subprocess.SubprocessError):
        return None

def laenge_s(b):
    """Reel-Länge in s: 'laenge_s' im Plan, sonst Video im Beitragsordner (auch von Hand gepostete Reels über
    plan_eintrag), sonst Cache, sonst ffprobe auf die media_url aus der API (wird in laengen.json gemerkt)."""
    e = plan_eintrag(b)
    if e and e.get("laenge_s"): return float(e["laenge_s"])
    if e and e.get("video") and (ROOT / e["ordner"] / e["video"]).exists():
        return _ffprobe(ROOT / e["ordner"] / e["video"])
    if b["id"] in _laengen: return _laengen[b["id"]]
    if b.get("media_url"):
        l = _ffprobe(b["media_url"])
        if l:
            _laengen[b["id"]] = l
            LAENGEN.write_text(json.dumps(_laengen, indent=1))
        return l
    return None

def ortszeit(ts):
    t = _utc(ts).astimezone(BERLIN)  # Sommer-/Winterzeit richtig (vorher fest +2 h)
    return t.strftime("%a %d.%m. %H:%M").replace("Mon","Mo").replace("Tue","Di").replace("Wed","Mi").replace("Thu","Do").replace("Fri","Fr").replace("Sat","Sa").replace("Sun","So")

# Skip-Verlauf je Reel aus den Morgen-Schnappschüssen (frühe Werte steigen mit der Reichweite – Alter mit anzeigen)
skip_verlauf = {}
for f in sorted(OUT.glob("basis_*.json")):
    try: snap = json.loads(f.read_text())
    except (OSError, ValueError): continue
    snap_t = datetime.strptime(snap["abgerufen"], "%Y-%m-%d").replace(hour=7, tzinfo=timezone.utc)
    for sb in snap.get("beitraege", []):
        if sb.get("reels_skip_rate") is None: continue
        h = (snap_t - _utc(sb["timestamp"])).total_seconds() / 3600
        if h > 0: skip_verlauf.setdefault(sb["id"], []).append((round(h), sb["reels_skip_rate"]))

zeilen = []
for b in bt:
    p = vor_bt.get(b["id"], {})
    typ = "Reel" if b["media_product_type"] == "REELS" else ("Karussell" if b["media_type"] == "CAROUSEL_ALBUM" else "Bild")
    zeilen.append(dict(name=name(b), typ=typ, zeit=ortszeit(b["timestamp"]), link=b["permalink"],
        views=b.get("views"), reach=b.get("reach"), likes=b.get("likes"), comments=b.get("comments"),
        saved=b.get("saved"), shares=b.get("shares"), profil=b.get("profile_visits"), follows=b.get("follows"),
        sehdauer=(b.get("ig_reels_avg_watch_time") or 0) / 1000 or None, skip=b.get("reels_skip_rate"),
        alter_h=round(alter_h(b["timestamp"]), 1), laenge=laenge_s(b) if typ == "Reel" else None,
        stimme=(plan_eintrag(b) or {}).get("stimme"), hook=(plan_eintrag(b) or {}).get("hook"),
        teilen_ueber=bool(b.get("shares") and b.get("reach") and b["shares"] > b["reach"]),
        skip_verlauf=sorted(set(skip_verlauf.get(b["id"], [])))[-3:],
        slot="mittags" if int(ortszeit(b["timestamp"])[-5:-3]) < 15 else "abends", nf_reach=nf_anteil(b),
        v_views=p.get("views"), v_reach=p.get("reach"), v_saved=p.get("saved"), v_shares=p.get("shares"), v_comments=p.get("comments")))

storys = [s for s in d.get("storys_aktiv", []) if s.get("views") is not None]

# Testmonat: Format × Slot × Stimme (nur Beiträge ab REIF_H; Urteil erst ab n ≥ 3)
MIN_N = 3
def _ja(x): return "ja" if x is True else ("nein" if x is False else "?")
def gruppen_tabelle():
    gr = {}
    for z in zeilen:
        if z["alter_h"] < 48 or z["typ"] not in ("Reel", "Karussell"): continue
        gr.setdefault((z["typ"], z["slot"], _ja(z["stimme"]), z["hook"] or "?"), []).append(z)
    alle = [z for l in gr.values() for z in l]
    schnitt = (sum(z["reach"] or 0 for z in alle) / len(alle)) if alle else None
    out = []
    for (typ, slot, st_, hk), l in sorted(gr.items()):
        n = len(l); r = summe(l, "reach")
        skips = [z["skip"] for z in l if z["skip"] is not None]
        prof = summe(l, "profil")
        zeile = dict(format=typ, slot=slot, stimme=st_, hook=hk, n=n,
            reichweite=r / n if n else None,
            speichern=quote(summe(l, "saved"), r),
            teilen=quote(summe([z for z in l if not z["teilen_ueber"]], "shares"), summe([z for z in l if not z["teilen_ueber"]], "reach")),
            skip=sum(skips) / len(skips) if skips else None,
            follows_profil=quote(summe(l, "follows"), prof) if prof else None)
        if n < MIN_N or not schnitt:
            zeile["urteil"] = "zu wenig Daten"
        else:
            v = zeile["reichweite"] / schnitt
            zeile["urteil"] = "über Schnitt" if v >= 1.15 else ("unter Schnitt" if v <= .85 else "im Schnitt")
        out.append(zeile)
    return out

# Methoden-Check: (Methode, Kennzahl, Wert-Text, Ziel, Status)
def st(wert, ziel, knapp=None):
    if wert is None: return "⏳"
    if wert >= ziel: return "✅"
    if knapp is not None and wert >= knapp: return "⚠️"
    return "❌"

for z in zeilen:
    z["anteil"] = quote(z["sehdauer"], z["laenge"])
reif = [z for z in zeilen if z["alter_h"] >= REIF_H]
jung = [z for z in zeilen if z["alter_h"] < REIF_H]

def zu_frueh(typen):
    """Hinweis auf noch zu junge Beiträge der Typen, z. B. 'Karussell 13 h'."""
    j = [z for z in jung if z["typ"] in typen]
    return ", ".join(f'{z["typ"]} {int(z["alter_h"])} h' for z in j)

def check(methode, kennzahl, typen, wert_f, fmt, ziel_txt, bewerte, braucht=None):
    """Bewertet nur reife Beiträge (≥ REIF_H) der Typen; wert_f(liste) -> Quote. Liefert (Methode, Kennzahl, Ist, Ziel, Status, n)."""
    pool = [z for z in reif if z["typ"] in typen and (braucht is None or z.get(braucht) is not None)]
    jf = zu_frueh(typen)
    unter = kennzahl + (f" · zu früh: {jf}" if jf and pool else "")
    if not pool:
        return (methode, unter, f"zu früh ({jf})" if jf else "–", ziel_txt, "⏳", 0)
    w = wert_f(pool)
    return (methode, unter, fmt(w) if w is not None else "–", ziel_txt, bewerte(w), len(pool))

def summe(liste, feld):
    return sum(z[feld] or 0 for z in liste)

def median(werte):
    w = sorted(werte); n = len(w)
    return None if not n else (w[n // 2] if n % 2 else (w[n // 2 - 1] + w[n // 2]) / 2)

testmonat = gruppen_tabelle()
s_reach = max((s.get("reach") or 0 for s in storys), default=None)
s_repl = sum(s.get("replies") or 0 for s in storys) if storys else None
profil = sum(z["profil"] or 0 for z in zeilen); follows = sum(z["follows"] or 0 for z in zeilen)
# Aktive Zeiten: Instagram liefert sie nicht bei jedem Abruf – dann den letzten Abruf mit Werten nehmen
on = {}
for f in [None] + sorted(OUT.glob("basis_*.json"), reverse=True):
    online = d.get("online_follower", {}) if f is None else json.loads(f.read_text()).get("online_follower", {})
    on = next((online[t] for t in sorted(online, reverse=True) if online[t]), {})
    if on: break
on_cest = {(int(h) + 9) % 24: n for h, n in on.items()}
on_abend = quote(on_cest.get(18), max(on_cest.values())) if on_cest else None  # gepostet wird 17:45, kurz vor der Welle

methoden = [
    ("Reels bringen Nicht-Follower", "Anteil Nicht-Follower an der Reichweite (30 Tage)",
     pct(nf_quote) if nf_quote is not None else "–", "≥ 50 %", st(nf_quote, .5, .35), None),
    check("Hook in den ersten 1,5 s", f"Median Überspringrate Reels ab {REIF_H} h (Ziel s. 06_auswertung)", {"Reel"},
          lambda l: median([z["skip"] for z in l]), lambda w: f"{w:.0f} %", "< 65 %",
          lambda w: "✅" if w < 65 else ("⚠️" if w < 75 else "❌"), braucht="skip"),
    check("Ø Sehdauer ÷ Länge", f"Anteil gesehen, Reels ab {REIF_H} h", {"Reel"},
          lambda l: sum(z["anteil"] for z in l) / len(l), lambda w: pct(w), "≥ 40 %",
          lambda w: st(w, .40, .25), braucht="anteil"),
    check("„Wer schickt das an wen?“", f"Geteilt ÷ Erreicht, Karussells + Reels ab {REIF_H} h, ohne Geteilt > Erreicht", {"Karussell", "Reel"},
          lambda l: quote(summe([z for z in l if not z["teilen_ueber"]], "shares"), summe([z for z in l if not z["teilen_ueber"]], "reach")),
          lambda w: pct(w, 1), "≥ 3 %", lambda w: st(w, .03, .015)),
    check("Speicherbare Inhalte", f"Gespeichert ÷ Erreicht, Karussells ab {REIF_H} h", {"Karussell"},
          lambda l: quote(summe(l, "saved"), summe(l, "reach")), lambda w: pct(w, 1), "≥ 2 %",
          lambda w: st(w, .02, .01)),
    ("Mittags-Story mit Frage", "Story-Reichweite ÷ Follower · Antworten (letzte 24 h)",
     f"{pct(s_reach/fol)} · {s_repl} Antw." if s_reach else "–", "≥ 15 % · ≥ 1",
     "⏳" if not s_reach else ("✅" if s_reach / fol >= .15 and s_repl else "⚠️"), len(storys)),
    check("Profil verwandelt Besucher", f"Follows ÷ Profilbesuche, Karussells ab {REIF_H} h (für Reels liefert die API nichts)", {"Karussell", "Bild"},
          lambda l: quote(summe(l, "follows"), summe(l, "profil")),
          lambda w: f"{pct(w)}", "≥ 10 %", lambda w: st(w, .10, .05), braucht="profil"),
    ("TOOL-Aufruf / Bio-Link", "Link-Klicks in der Bio (30 Tage)", str(links), "≥ 1 pro Woche", "✅" if links else "❌", None),
    ("Posten um 17:45", "Follower online 18–19 Uhr ÷ Spitzenstunde", pct(on_abend) if on_abend else "–", "≥ 85 %", st(on_abend, .85, .7), None),
]
# Profil-Zeile: absolute Zahlen mit anzeigen (z. B. „0 / 7“), weil die Quote bei kleinen Zahlen wenig sagt
_p = [z for z in reif if z["profil"] is not None]
if _p and summe(_p, "profil"):
    i = next(i for i, m in enumerate(methoden) if m[0] == "Profil verwandelt Besucher")
    m = list(methoden[i]); m[2] = f'{summe(_p, "follows")} / {summe(_p, "profil")} · {m[2]}'; methoden[i] = tuple(m)

# Heute geplant: alle Einträge des Tages außer entfallen/pausiert, mit Hinweis je Status. Früher nur
# freigegeben/manuell – dadurch war die Liste leer, wenn morgens noch etwas auf Freigabe oder Sprachnachricht wartete.
STATUS_TXT = {"freigegeben": "geht automatisch online", "manuell": "von Hand posten", "veroeffentlicht": "ist online",
              "wartet_auf_sprachnachricht": "wartet auf Sprachnachricht", "entwurf": "Entwurf – noch nicht freigegeben",
              "fehler": "Fehler beim Posten – prüfen"}
def _zeit(e):
    return str(e.get("zeit", "")).strip().replace("T", " ")[:16]
heute_online = sorted((e for e in plan if _zeit(e)[:10] == tag and e.get("status") not in ("entfaellt", "pause")), key=_zeit)
fehler = [e["id"] for e in plan if e["status"] == "fehler"]

# Soll-Ist: Feed-Einträge der letzten 48 h (vor dem Bezugszeitpunkt), die nicht als Beitrag erschienen sind
_gefunden = {plan_eintrag(b)["id"] for b in d["beitraege"] if plan_eintrag(b)}
nicht_erschienen = [e for e in plan if e.get("typ") in ("reel", "karussell", "bild") and e.get("zeit")
                    and e.get("status") not in ("entfaellt", "pause")
                    and bezug - timedelta(hours=48) <= _plan_zeit(e) <= bezug - timedelta(minutes=30)
                    and e["id"] not in _gefunden and not e.get("link")]

# --- HTML ---
def balken():
    w, h, pad = 960, 220, 30
    mx = max([tw[t] for t in tage] + [1])
    bw = (w - 2 * pad) / len(tage)
    gepostet = {z["zeit"][3:9].strip() for z in zeilen}
    out = [f'<svg viewBox="0 0 {w} {h+46}" width="{w}" height="{h+46}">',
           f'<line x1="{pad}" y1="{h}" x2="{w-pad}" y2="{h}" stroke="#2a3a33" stroke-width="1"/>']
    for i, t in enumerate(tage):
        val = tw[t]; bh = max(3, (h - 20) * val / mx); x = pad + i * bw + 4
        tt = f"{t[8:10]}.{t[5:7]}."
        farbe = "#53C3A2" if tt in gepostet else "#2E6B5B"
        out.append(f'<rect x="{x:.1f}" y="{h-bh:.1f}" width="{bw-8:.1f}" height="{bh:.1f}" rx="4" fill="{farbe}"/>')
        out.append(f'<text x="{x+(bw-8)/2:.1f}" y="{h-bh-6:.1f}" text-anchor="middle" class="bv">{val}</text>')
        out.append(f'<text x="{x+(bw-8)/2:.1f}" y="{h+20}" text-anchor="middle" class="bl">{tt}</text>')
    out.append(f'<text x="{pad}" y="{h+42}" class="bl">hell = Tag mit neuem Beitrag</text></svg>')
    return "".join(out)

def kachel(titel, wert, d_html="", unter=""):
    return f'<div class="kachel"><div class="kt">{titel}</div><div class="kw">{wert}{d_html}</div><div class="ku">{unter}</div></div>'

def komma(x, n=1):
    return f"{x:.{n}f}".replace(".", ",")

def reel_zelle(z):
    """Skip · Ø Sehdauer / Länge = Anteil (nur Reels)."""
    if z["skip"] is None and z["sehdauer"] is None: return "–"
    teile = [f'{z["skip"]:.0f} %' if z["skip"] is not None else "–"]
    seh = f'{komma(z["sehdauer"])} s' if z["sehdauer"] else "–"
    if z["laenge"]:
        seh += f' / {z["laenge"]:.0f} s'
    teile.append(seh)
    zelle = " · ".join(teile)
    if z["anteil"] is not None:
        zelle += f'<br><span class="m">= {pct(z["anteil"])} gesehen</span>'
    if z["skip_verlauf"]:  # frühere Skip-Werte mit Alter, damit die Drift sichtbar ist
        zelle += '<br><span class="m">Skip: ' + " → ".join(f"{w:.0f} % ({h} h)" for h, w in z["skip_verlauf"]) + "</span>"
    return zelle

reihen = "".join(
    f'<tr><td><b>{html.escape(z["name"])}</b><br><span class="m">{z["typ"]} · {z["zeit"]} · {int(z["alter_h"])} h</span></td>'
    f'<td>{zahl(z["views"])}{delta(z["views"], z["v_views"])}</td><td>{zahl(z["reach"])}{delta(z["reach"], z["v_reach"])}</td>'
    f'<td>{zahl(z["likes"])}</td><td>{zahl(z["comments"])}{delta(z["comments"], z["v_comments"])}</td>'
    f'<td>{zahl(z["saved"])}{delta(z["saved"], z["v_saved"])}</td><td>{zahl(z["shares"])}{delta(z["shares"], z["v_shares"])}{" ⚠️" if z["teilen_ueber"] else ""}</td>'
    f'<td>{"n. v." if z["typ"] == "Reel" else zahl(z["profil"])}</td>'
    f'<td>{reel_zelle(z)}</td></tr>'
    for z in zeilen)
s_reihen = "".join(
    f'<tr><td>Story {ortszeit(s["zeit"])}</td><td>{zahl(s.get("views"))}</td><td>{zahl(s.get("reach"))}</td>'
    f'<td>{zahl(s.get("replies"))}</td><td>{zahl(s.get("navigation"))}</td><td>{zahl(s.get("profile_visits"))}</td></tr>'
    for s in storys) or '<tr><td colspan="6" class="m">keine Story in den letzten 24 h</td></tr>'
m_reihen = "".join(
    f'<tr><td class="st">{s}</td><td><b>{html.escape(a)}</b><br><span class="m">{html.escape(b)}</span></td><td class="w">{html.escape(c)}</td><td class="m">{html.escape(z)}</td><td class="m">{"" if n is None else n}</td></tr>'
    for a, b, c, z, s, n in methoden)
def _p(x, n=0): return "–" if x is None else pct(x, n)
t_reihen = "".join(
    f'<tr><td><b>{t["format"]}</b></td><td>{t["slot"]}</td><td>{t["stimme"]}</td><td>{t["hook"]}</td><td>{t["n"]}</td>'
    f'<td>{zahl(t["reichweite"])}</td><td>{_p(t["speichern"],1)}</td><td>{_p(t["teilen"],1)}</td>'
    f'<td>{"–" if t["skip"] is None else f"{t[chr(115)+chr(107)+chr(105)+chr(112)]:.0f} %"}</td><td>{_p(t["follows_profil"])}</td>'
    f'<td class="{"m" if t["urteil"] == "zu wenig Daten" else "w"}">{t["urteil"]}</td></tr>'
    for t in testmonat) or '<tr><td colspan="11" class="m">noch keine Beiträge ab 48 h</td></tr>'
n_reihen = "".join(
    f'<tr><td class="w">{_zeit(e)[8:10]}.{_zeit(e)[5:7]}. {_zeit(e)[11:]}</td><td>{html.escape(e["typ"])}</td><td><b>{html.escape(e["id"])}</b></td>'
    f'<td class="warn">{STATUS_TXT.get(e["status"], e["status"])} – nicht erschienen</td></tr>'
    for e in nicht_erschienen) or '<tr><td colspan="4" class="m">alles Geplante ist erschienen</td></tr>'
h_reihen = "".join(
    f'<tr><td class="w">{_zeit(e)[11:]}</td><td>{html.escape(e["typ"])}</td><td><b>{html.escape(e["id"])}</b></td>'
    f'<td class="{"warn" if e["status"] != "freigegeben" and e["status"] != "veroeffentlicht" else "m"}">{STATUS_TXT.get(e["status"], e["status"])}</td></tr>'
    for e in heute_online) or '<tr><td colspan="4" class="m">heute nichts geplant</td></tr>'
wt = datetime.strptime(tag, "%Y-%m-%d")
titel_tag = ["Mo","Di","Mi","Do","Fr","Sa","So"][wt.weekday()] + wt.strftime(" %d.%m.%Y")

seite = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@import url("../../vorlagen/schriften.css");
*{{box-sizing:border-box}}
body{{margin:0;width:1080px;background:#0B110E;color:#EAF1EC;font-family:"IBM Plex Sans",sans-serif;padding:44px 50px}}
h1{{font-family:"IBM Plex Serif",serif;font-weight:600;font-size:46px;margin:0 0 4px}}
.kick{{font-family:"IBM Plex Mono",monospace;letter-spacing:.25em;text-transform:uppercase;color:#53C3A2;font-size:16px;font-weight:600}}
h2{{font-family:"IBM Plex Mono",monospace;letter-spacing:.18em;text-transform:uppercase;color:#53C3A2;font-size:15px;margin:34px 0 12px}}
.kacheln{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:26px}}
.kachel{{background:#12201B;border:1px solid #1f3a31;border-radius:16px;padding:16px 18px}}
.kt{{font-size:15px;color:#8FA398}} .kw{{font-size:40px;font-weight:600;margin-top:4px}} .ku{{font-size:14px;color:#8FA398;margin-top:2px}}
.d{{font-size:16px;font-weight:600;margin-left:8px;vertical-align:middle}} .up{{color:#53C3A2}} .down{{color:#E07A6B}}
table{{width:100%;border-collapse:collapse;font-size:17px}}
th{{text-align:left;color:#8FA398;font-weight:500;font-size:14px;padding:8px 8px;border-bottom:1px solid #2a3a33}}
td{{padding:10px 8px;border-bottom:1px solid #18261f;vertical-align:top}}
td .d{{font-size:13px;margin-left:5px}}
.m{{color:#8FA398;font-size:14px}} .st{{font-size:24px;width:40px}} .w{{font-weight:600;white-space:nowrap}}
.bv{{fill:#C9D6CE;font-size:14px;font-family:"IBM Plex Mono",monospace}} .bl{{fill:#8FA398;font-size:13px;font-family:"IBM Plex Sans",sans-serif}}
.leg{{color:#8FA398;font-size:14px;margin-top:10px}} .warn{{color:#E8C468;font-size:14px}} table.klein{{font-size:15px}} table.klein td,table.klein th{{padding:8px 6px}}
</style></head><body>
<div class="kick">@maehrsteuern · Tagesbericht</div><h1>{titel_tag}</h1>
<div class="kacheln">
{kachel("Follower", zahl(fol), delta(fol, fol_v), f"du folgst {k['follows_count']}")}
{kachel("Reichweite gestern", zahl(r_gestern), delta(r_gestern, r_vortag), "erreichte Konten")}
{kachel("Nicht-Follower (30 T.)", pct(nf_quote) if nf_quote is not None else "–", "", f"{nf} von {nf+ff} Konten")}
{kachel("Bio-Link-Klicks", str(links), "", f"30 Tage · {m30.get('replies',0)} Story-Antworten")}
</div>
<h2>Reichweite pro Tag</h2>{balken()}
<h2>Beiträge seit Neustart (Δ zum Vortag)</h2>
<table><tr><th>Beitrag</th><th>Aufrufe</th><th>Erreicht</th><th>Likes</th><th>Komm.</th><th>Gespeich.</th><th>Geteilt</th><th>Profil</th><th>Skip · Ø Seh. / Länge</th></tr>{reihen}</table>
<div class="leg">⚠️ bei Geteilt: mehr Weiterleitungen als erreichte Konten (Instagram zählt jedes Senden, auch mehrfach an Chats/Gruppen; Reichweite = eindeutige Konten) – fließt nicht in die Teilen-Quote ein · Profil n. v. = liefert die API für Reels nicht</div>
<h2>Storys (letzte 24 h)</h2>
<table><tr><th>Story</th><th>Aufrufe</th><th>Erreicht</th><th>Antworten</th><th>Tipps</th><th>Profil</th></tr>{s_reihen}</table>
<h2>Greifen unsere Methoden?</h2>
<table><tr><th></th><th>Methode · Kennzahl</th><th>Ist</th><th>Ziel</th><th>n</th></tr>{m_reihen}</table>
<div class="leg">✅ greift · ⚠️ knapp · ❌ greift (noch) nicht · ⏳ zu früh / keine Daten · bewertet werden nur Beiträge ab {REIF_H} h, n = Anzahl Beiträge</div>
<h2>Testmonat: Format × Slot × Stimme</h2>
<table class="klein"><tr><th>Format</th><th>Slot</th><th>Stimme</th><th>Hook</th><th>n</th><th>Ø Erreicht</th><th>Speich.÷Err.</th><th>Teilen÷Err.</th><th>Skip</th><th>Follows÷Profil</th><th>Urteil</th></tr>{t_reihen}</table>
<div class="leg">nur Beiträge ab 48 h · Urteil (Ø Erreicht gegen Schnitt aller Gruppen) erst ab n ≥ {MIN_N} · Stimme/Hook ? = nicht im Plan · Nicht-Follower je Beitrag liefert die API nicht (nur fürs ganze Konto, Kachel oben) · Teilen÷Erreicht ohne Beiträge mit Geteilt &gt; Erreicht</div>
<h2>Soll-Ist: geplant, aber nicht erschienen (48 h)</h2>
<table><tr><th>Geplant</th><th>Art</th><th>Beitrag</th><th>Status im Plan</th></tr>{n_reihen}</table>
<h2>Heute geplant</h2>
<table><tr><th>Zeit</th><th>Art</th><th>Beitrag</th><th>Status</th></tr>{h_reihen}</table>
</body></html>"""

OUT.mkdir(parents=True, exist_ok=True)
html_f = OUT / f"tagesbericht_{tag}.html"; png_f = OUT / f"tagesbericht_{tag}.png"
html_f.write_text(seite)
(OUT / f"tagesbericht_{tag}.json").write_text(json.dumps(dict(
    tag=tag, follower=fol, follower_vortag=fol_v, reichweite_gestern=r_gestern, reichweite_vortag=r_vortag,
    nicht_follower_quote=nf_quote, link_klicks=links, beitraege=zeilen, storys=storys,
    methoden=[dict(methode=a, kennzahl=b, ist=c, ziel=z, status=s, n=n) for a, b, c, z, s, n in methoden],
    heute_online=[f'{_zeit(e)[11:]} {e["typ"]} {e["id"]} – {STATUS_TXT.get(e["status"], e["status"])}' for e in heute_online],
    fehler=fehler, reif_ab_h=REIF_H, testmonat=testmonat,
    nicht_erschienen=[f'{_zeit(e)} {e["typ"]} {e["id"]} ({e["status"]})' for e in nicht_erschienen]),
    ensure_ascii=False, indent=1, default=str))

js = f"""const {{createRequire}}=require('module');const {{execSync}}=require('child_process');
const {{chromium}}=createRequire(execSync('npm root -g').toString().trim()+'/')('playwright');
(async()=>{{const b=await chromium.launch({{executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'}});
const p=await b.newPage({{viewport:{{width:1080,height:800}},deviceScaleFactor:1.5}});
await p.goto('file://{html_f}');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({{path:'{png_f}',fullPage:true}});await b.close();}})();"""
subprocess.run(["node", "-e", js], check=True)
print(png_f)
