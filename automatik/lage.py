"""Lagebericht: schreibt LAGE.md – was gerade läuft, was als Nächstes kommt, was du tun musst, und jede Änderung im Repo.

Aufruf:  python automatik/lage.py          – LAGE.md neu schreiben
Läuft automatisch per GitHub Actions (.github/workflows/lage.yml) nach jedem Push und nach jedem Lauf
von Posten, Freigabe, Statistik, Schlüssel und Musik. Quellen: plan.json, Git-Verlauf, statistik/*.csv,
optional der Workflow-Status über die GitHub-API (GH_TOKEN + GITHUB_REPOSITORY).
Handnotizen („gerade in Arbeit“, Entscheidungen) stehen in automatik/lage_notizen.md und werden oben eingebunden.
Schreibt außerdem LAGE.html (automatik/lage_html.py) – dieselbe Lage als grafische Seite (GitHub Pages).
"""
import csv, json, os, re, subprocess
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

WURZEL = Path(__file__).resolve().parent.parent
PLAN = WURZEL / "automatik" / "plan.json"
NOTIZEN = WURZEL / "automatik" / "lage_notizen.md"
INTERAKTION = WURZEL / "automatik" / "interaktion.json"
KONTO = WURZEL / "automatik" / "statistik" / "konto.csv"
ERINNERUNGEN = WURZEL / "automatik" / "erinnerungen.json"
ZIEL = WURZEL / "LAGE.md"
ZONE = ZoneInfo("Europe/Berlin")
NACHHOLEN = timedelta(hours=6)  # wie posten.py: danach wird ein verpasster Eintrag nicht mehr nachgeholt
UEBERFAELLIG = timedelta(minutes=30)  # freigegeben, aber so lange nach der Zeit noch nicht online → rot
RASTER = {"Feed": ("11:45", "17:45"), "Story": ("12:15", "17:50")}  # Slots laut strategie/15_plan_2_pro_tag.md
TEST_START, TEST_ENDE = date(2026, 10, 12), date(2026, 11, 8)  # Testmonat: 14 Feed-Beiträge/Woche, täglich ≥ 1 Reel
FEED_SOLL = 14
REPO = os.environ.get("GITHUB_REPOSITORY", "MBS-maehrsteuern/Instagram-maehrsteuern")
LAGE_COMMIT = "Lage aktualisiert"

TYP = {"karussell": "🖼️ Karussell", "reel": "🎬 Reel", "story": "📱 Story", "bild": "🖼️ Bild"}
STATUS = {
    "freigegeben": "🟢 freigegeben (geht automatisch online)",
    "entwurf": "🟡 Entwurf (wartet auf Freigabe)",
    "manuell": "✋ manuell (postest du in der App)",
    "veroeffentlicht": "✅ veröffentlicht",
    "fehler": "🔴 Fehler",
    "entfaellt": "⚪ entfällt",
}
AUS = ("entfaellt", "pause")  # zählen weder als geplant noch als belegt
WORKFLOWS = [  # Datei, Name, wann
    ("lage.yml", "Lage + Google-Kalender", "alle 15 Min. (LAGE.md, Kalender-Sync, Wächter)"),
    ("posten.yml", "Posten", "alle 15 Min. (postet freigegebene Einträge)"),
    ("freigabe.yml", "Freigabe", "bei neuen Entwürfen / Antwort im Issue"),
    ("statistik.yml", "Statistik", "täglich ca. 08:45"),
    ("token.yml", "Schlüssel verlängern", "am 1. des Monats ca. 06:27"),
    ("radar.yml", "Radar + LinkedIn", "täglich ca. 07:00 (Issue mit Arbeitsliste)"),
    ("kommentare.yml", "Kommentare", "nach jedem Posten-Takt (Vorschläge ins Issue)"),
    ("wochenbericht.yml", "Wochenbericht", "sonntags ca. 18:00 (ein Issue)"),
    ("musik.yml", "Musik holen", "nur von Hand"),
]
WOCHENTAG = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]


def git(*args):
    return subprocess.run(["git", *args], cwd=WURZEL, capture_output=True, text=True).stdout.strip()


def zeit(e):
    return datetime.strptime(e["zeit"], "%Y-%m-%d %H:%M").replace(tzinfo=ZONE)


def tag(d):
    return f"{WOCHENTAG[d.weekday()]} {d:%d.%m.} {d:%H:%M}"


def status(e):
    s = e["status"]
    return STATUS.get(s, "⏳ " + s.replace("_", " ") if s.startswith("wartet") else s)


def issue_link(e):
    return f" · [Freigabe #{e['issue']}](https://github.com/{REPO}/issues/{e['issue']})" if e.get("issue") else ""


def slot_art(e):
    return "Story" if e["typ"] == "story" else "Feed"


def ersatz_text(e):
    """Feld `ersatz_video`: fertiges Notlösungs-Video ohne Stimme, falls die Sprachnachricht nicht kommt."""
    if not e.get("ersatz_video"):
        return ""
    da = (WURZEL / e["ordner"] / e["ersatz_video"]).exists()
    return (f"🎞️ **Ersatz ohne Stimme liegt bereit** (`{e['ersatz_video']}`)" if da
            else f"⚠️ Ersatz ohne Stimme eingetragen, Datei fehlt (`{e['ersatz_video']}`)")


def dateien_fehlen(e):
    namen = list(e.get("bilder", [])) + [e[k] for k in ("video", "titelbild", "text") if e.get(k)]
    return [n for n in namen if not (WURZEL / e["ordner"] / n).exists()]


# Aufforderungen wie „Schreib „TOOL“ per DM“ / „Kommentiere TOOL“ in Bildunterschriften
AUFRUF = re.compile(r"(?i:schreib\w*|kommentier\w*|antworte?\w*|tipp\w*)\s+(?:(?i:mir|uns|einfach|gern|gerne|jetzt|unten)\s+)*"
                    r"[„\"»‚'“]?([A-ZÄÖÜ]{3,})\b")


def stichwort_abgleich(eintraege):
    """ManyChat-Stichwörter stehen nur in automatik/interaktion.json. Fordert ein geplanter Beitrag zu einem
    anderen Wort auf, antwortet weder ManyChat noch passt die Kommentar-Hilfe – das wird hier gemeldet."""
    try:
        bekannt = {w.lower() for w in json.loads(INTERAKTION.read_text())["kommentare"]["manychat_stichwoerter"]}
    except (OSError, KeyError, json.JSONDecodeError):
        return ["🔴 **Stichwörter:** `automatik/interaktion.json` fehlt oder ist kaputt – ManyChat-Abgleich nicht möglich"]
    punkte = []
    for e in eintraege:
        if e["status"] in ("veroeffentlicht", "entfaellt") or not e.get("text"):
            continue
        datei = WURZEL / e["ordner"] / e["text"]
        fremd = sorted({w for w in AUFRUF.findall(datei.read_text()) if w.lower() not in bekannt}) if datei.exists() else []
        if fremd:
            punkte.append(f"⚠️ **Stichwort passt nicht zu ManyChat** `{e['id']}` ({tag(zeit(e))}): "
                          f"{', '.join(f'„{w}“' for w in fremd)} – in ManyChat anlegen und in `automatik/interaktion.json` "
                          "(`manychat_stichwoerter`) eintragen, oder Bildunterschrift auf TOOL ändern")
    return punkte


# ---------- Abschnitte ----------

def erinnerungen():
    """Offene einmalige Erinnerungen aus automatik/erinnerungen.json, mit „start“ als Zeitpunkt (deutsche Zeit)."""
    if not ERINNERUNGEN.exists():
        return []
    aus = []
    for r in json.loads(ERINNERUNGEN.read_text()).get("erinnerungen", []):
        if not r.get("erledigt"):
            aus.append({**r, "start": datetime.fromisoformat(r["wann"]).replace(tzinfo=ZONE)})
    return aus


def offene_punkte(eintraege, n):
    punkte = []
    for e in sorted(eintraege, key=zeit):
        t, s, name = zeit(e), e["status"], f"`{e['id']}` ({tag(zeit(e))})"
        if s == "fehler":
            punkte.append(f"🔴 **Fehler beim Posten** {name}: {e.get('fehler', '')[:200]}")
        elif s == "freigegeben" and t < n - NACHHOLEN:
            punkte.append(f"🔴 **Verpasst** {name}: war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten")
        elif s == "freigegeben" and t < n - UEBERFAELLIG:
            punkte.append(f"🔴 **Überfällig** {name}: freigegeben, seit {(n - t).seconds // 60} Min. über der Zeit und nicht online – "
                          "Posten-Lauf/Wächter in Actions prüfen")
        elif s == "entwurf" and t > n - NACHHOLEN:
            gruppe = [x for x in eintraege if x["id"].split("-")[0] == e["id"].split("-")[0]]
            wartet = next((x["id"] for x in gruppe if x["status"].startswith("wartet")), None)
            wie = (issue_link(e).lstrip(" ·") or (f"Issue kommt, sobald `{wartet}` fertig ist" if wartet
                                                   else "Issue wird automatisch angelegt"))
            punkte.append(f"🟡 **Freigeben** {name} – „go“ oder „stop“ im Issue ({wie})")
        elif s.startswith("wartet") and t > n - NACHHOLEN:
            punkte.append(f"⏳ **{s.replace('_', ' ').capitalize()}** {name}"
                          + (f" – {ersatz}" if (ersatz := ersatz_text(e)) else "")
                          + (f" – {e['hinweis']}" if e.get("hinweis") else ""))
        elif s == "manuell" and t > n - timedelta(days=1):
            punkte.append(f"✋ **Von Hand posten** {name}" + (f" – {e['hinweis']}" if e.get("hinweis") else ""))
        if s in ("freigegeben", "entwurf", "manuell") and t > n and (fehlt := dateien_fehlen(e)):
            punkte.append(f"🔴 **Dateien fehlen** {name}: {', '.join(fehlt)}")
        if e.get("musik_fehlt") and t > n:
            punkte.append(f"🎵 **Musik fehlt** {name}")
        if e.get("danach") and not e.get("danach_erledigt") and (s == "veroeffentlicht" and n - t < timedelta(days=2) or s == "manuell" and t > n - timedelta(days=1)):
            punkte.append(f"👉 **Danach:** {e['danach']} ({name})")
        if s == "veroeffentlicht" and e.get("hinweis", "").startswith("Danach") and n - t < timedelta(days=2):
            punkte.append(f"👉 **{e['hinweis']}** ({name})")
    for r in sorted(erinnerungen(), key=lambda r: r["start"]):
        if r["start"] - timedelta(days=r.get("zeigen_ab_tagen", 3)) <= n <= r["start"] + timedelta(days=1):
            punkte.append(f"⏰ **{r['titel']}** ({tag(r['start'])}) – {r.get('text', '').splitlines()[0]}")
    punkte += stichwort_abgleich(eintraege)
    return punkte or ["Nichts offen. 🎉"]


# ---------- 30-Sekunden-Briefing ----------

def heute_ampel(eintraege, n):
    """[(Ampel, Kurztext, Eintrag)] für alles, was heute online gehen soll."""
    aus = []
    for e in sorted((x for x in eintraege if zeit(x).date() == n.date() and x["status"] not in AUS), key=zeit):
        t, s = zeit(e), e["status"]
        if s == "veroeffentlicht":
            a, txt = "✅", "online"
        elif s == "fehler":
            a, txt = "🔴", "Fehler"
        elif s == "freigegeben" and t < n - UEBERFAELLIG:
            a, txt = "🔴", "überfällig"
        elif s == "freigegeben" and dateien_fehlen(e):
            a, txt = "🔴", "Dateien fehlen"
        elif s == "freigegeben":
            a, txt = "🟢", "läuft automatisch"
        elif s == "manuell":
            a, txt = "✋", "von Hand"
        elif s == "entwurf":
            a, txt = "🟡", "wartet auf go"
        else:
            a, txt = "🟡", s.replace("_", " ")
        aus.append((a, txt, e))
    return aus


def sieben_tage(n):
    """Letzte 7 abgeschlossene Tage: Reichweite (Summe, Vorwoche), Follower ±, Follows/Entfolgt (30 Tage, API)."""
    zeilen = list(csv.DictReader(KONTO.open())) if KONTO.exists() else []
    dateien = insights_dateien()
    w = {}
    if dateien:
        d = json.loads(dateien[-1].read_text())
        # Tag des Abrufs (und später) ist noch nicht vorbei → nicht mitzählen
        grenze = min(n.strftime("%Y-%m-%d"), d.get("abgerufen", "9999")[:10])
        fertig = [(t, v) for t, v in sorted((d.get("tageswerte_reichweite") or {}).items()) if t < grenze]
        if fertig:
            w.update(von=fertig[-7:][0][0], bis=fertig[-1][0], reichweite=sum(v for _, v in fertig[-7:]),
                     tage=len(fertig[-7:]))
            if len(fertig) >= 14:
                w["vorwoche"] = sum(v for _, v in fertig[-14:-7])
        fu = ((d.get("konto_verlauf") or [{}])[0].get("follows_and_unfollows") or {}).get("aufgeteilt") or {}
        if fu:  # laut API: FOLLOWER = neue Follows, NON_FOLLOWER = Entfolgungen (30 Tage)
            w.update(follows30=fu.get("FOLLOWER"), entfolgt30=fu.get("NON_FOLLOWER"))
    if zeilen:
        letzte = zeilen[-1]
        stichtag = (datetime.strptime(letzte["datum"], "%Y-%m-%d") - timedelta(days=7)).strftime("%Y-%m-%d")
        vorher = next((z for z in reversed(zeilen) if z["datum"] <= stichtag), None)
        if vorher:
            w.update(follower=int(letzte["followers_count"]),
                     follower_diff=int(letzte["followers_count"]) - int(vorher["followers_count"]),
                     follower_seit=vorher["datum"])
    return w


def vorwoche_prozent(w):
    return f"{round(100 * (w['reichweite'] - w['vorwoche']) / max(w['vorwoche'], 1)):+d} %"


def sieben_tage_text(w):
    if not w:
        return "noch keine Statistik"
    teile = []
    if "reichweite" in w:
        vw = f", {vorwoche_prozent(w)} zur Vorwoche" if "vorwoche" in w else ""
        teile.append(f"Reichweite **{w['reichweite']}** ({w['von'][8:10]}.{w['von'][5:7]}.–{w['bis'][8:10]}.{w['bis'][5:7]}.{vw})")
    if "follower_diff" in w:
        teile.append(f"Follower **{w['follower_diff']:+d}** (jetzt {w['follower']})" + (" ⚠️" if w["follower_diff"] < 0 else ""))
    if w.get("follows30") is not None:
        teile.append(f"30 Tage: +{w['follows30']} Follows / −{w.get('entfolgt30', '–')} entfolgt")
    return " · ".join(teile)


def testmonat(eintraege, n):
    """Je Kalenderwoche des Testmonats: Feed-Beiträge (online/geplant/wartet) gegen Soll 14 und Tage mit Reel."""
    if n.date() > TEST_ENDE + timedelta(days=7):
        return []
    aus = []
    start = TEST_START - timedelta(days=TEST_START.weekday())
    while start <= TEST_ENDE:
        tage = [start + timedelta(days=i) for i in range(7)]
        woche = [e for e in eintraege if e["status"] not in AUS and zeit(e).date() in tage]
        feed = [e for e in woche if e["typ"] != "story"]
        online = sum(e["status"] == "veroeffentlicht" for e in feed)
        geplant = sum(e["status"] in ("freigegeben", "manuell", "entwurf") for e in feed)
        wartet = sum(e["status"].startswith("wartet") for e in feed)
        fehler = sum(e["status"] == "fehler" for e in feed)
        # Reel-Tag zählt, wenn ein Reel online oder sicher geplant ist (wartet_* zählt nicht)
        reel_tage = {zeit(e).date() for e in feed if e["typ"] == "reel" and e["status"] in ("veroeffentlicht", "freigegeben", "manuell", "entwurf")}
        im_test = [d for d in tage if TEST_START <= d <= TEST_ENDE]
        ohne_reel = [d for d in im_test if d not in reel_tage]
        aus.append({"kw": start.isocalendar()[1], "von": start, "bis": start + timedelta(days=6), "online": online,
                    "geplant": geplant, "wartet": wartet, "fehler": fehler, "summe": online + geplant + wartet + fehler,
                    "reel_tage": len(im_test) - len(ohne_reel), "test_tage": len(im_test), "ohne_reel": ohne_reel, "aktuell": start <= n.date() <= start + timedelta(days=6),
                    "vorbei": start + timedelta(days=6) < n.date()})
        start += timedelta(days=7)
    return aus


def testmonat_text(w):
    ampel = "✅" if w["online"] + w["geplant"] >= FEED_SOLL and not w["ohne_reel"] else ("🔴" if w["online"] + w["geplant"] < FEED_SOLL / 2 else "🟡")
    t = (f"{ampel} **KW {w['kw']}** ({w['von']:%d.%m.}–{w['bis']:%d.%m.}){' ← jetzt' if w['aktuell'] else ''}: "
         f"Feed **{w['online'] + w['geplant']}/{FEED_SOLL}** ({w['online']} online · {w['geplant']} geplant"
         + (f" · {w['wartet']} wartet" if w["wartet"] else "") + (f" · {w['fehler']} Fehler" if w["fehler"] else "") + ")"
         + f" · Reel-Tage (sicher) **{w['reel_tage']}/{w['test_tage']}**")
    if w["ohne_reel"] and not w["vorbei"] and len(w["ohne_reel"]) <= 3:
        t += " – ohne Reel: " + ", ".join(f"{WOCHENTAG[d.weekday()]} {d:%d.%m.}" for d in w["ohne_reel"])
    return t


def freie_slots(eintraege, n, tage=7):
    """{Datum: [„Feed 11:45“, …]} – Raster-Slots von jetzt bis +7 Tage, an denen nichts gleicher Art steht."""
    belegt = {(zeit(e).date(), slot_art(e), e["zeit"][11:]) for e in eintraege if e["status"] not in AUS}
    frei = {}
    for i in range(tage + 1):
        d = (n + timedelta(days=i)).date()
        for art, zeiten in RASTER.items():
            for z in zeiten:
                beginn = datetime.strptime(f"{d} {z}", "%Y-%m-%d %H:%M").replace(tzinfo=ZONE)
                if n < beginn <= n + timedelta(days=tage) and (d, art, z) not in belegt:
                    frei.setdefault(d, []).append(f"{art} {z}")
    return frei


def briefing(eintraege, n, punkte):
    """Kurzblock ganz oben in LAGE.md – was der Lage-Skill Loris zuerst sagt."""
    heute = heute_ampel(eintraege, n)
    zeilen = ["## ⏱️ 30-Sekunden-Briefing", ""]
    zeilen.append("- **Heute online:** " + (" · ".join(f"{a} {zeit(e):%H:%M} {TYP.get(e['typ'], e['typ'])} `{e['id']}` ({t})"
                                                        for a, t, e in heute) or "nichts geplant"))
    offen = [p for p in punkte if not p.startswith("Nichts")]
    rot = sum(p.startswith("🔴") for p in offen)
    zeilen.append(f"- **Braucht dich:** {len(offen)} offen" + (f", davon **{rot} rot** 🔴" if rot else "") if offen else "- **Braucht dich:** nichts 🎉")
    zeilen.append(f"- **Letzte 7 Tage:** {sieben_tage_text(sieben_tage(n))}")
    wochen = [w for w in testmonat(eintraege, n) if not w["vorbei"] or w["aktuell"]]
    if wochen:
        zeilen.append(f"- **Testmonat** (Tag {max(0, min((n.date() - TEST_START).days + 1, 28))}/28, Soll {FEED_SOLL} Feed/Woche, täglich ≥ 1 Reel):")
        zeilen += [f"  - {testmonat_text(w)}" for w in wochen]
    frei = freie_slots(eintraege, n)
    if frei:
        zeilen.append(f"- **Freie Slots nächste 7 Tage** ({sum(map(len, frei.values()))}):")
        zeilen += [f"  - {WOCHENTAG[d.weekday()]} {d:%d.%m.}: {' · '.join(s)}" + (" – **ganzer Tag leer**" if len(s) == 4 else "")
                   for d, s in sorted(frei.items())]
    else:
        zeilen.append("- **Freie Slots nächste 7 Tage:** keine")
    return zeilen + [""]


def tabelle(eintraege, mit_status=True):
    zeilen = ["| Wann | Was | Status | Hinweis |", "|---|---|---|---|"]
    for e in sorted(eintraege, key=zeit):
        hinweis = (e.get("hinweis", "") + issue_link(e)).replace("|", "/")
        zeilen.append(f"| {tag(zeit(e))} | {TYP.get(e['typ'], e['typ'])} `{e['id']}` | {status(e)} | {hinweis} |")
    return zeilen


def veroeffentlicht(eintraege):
    fertig = sorted((e for e in eintraege if e["status"] == "veroeffentlicht"), key=zeit, reverse=True)[:10]
    if not fertig:
        return ["Über den Autopiloten noch nichts veröffentlicht."]
    return [f"- {tag(zeit(e))} · {TYP.get(e['typ'], e['typ'])} `{e['id']}`"
            + (f" · [ansehen]({e['link']})" if e.get("link") else "")
            + (f" (online {e['veroeffentlicht_am']})" if e.get("veroeffentlicht_am") else "") for e in fertig]


def insights_dateien():
    return sorted((WURZEL / "automatik" / "statistik").glob("insights_*.json"))


def lokal(zeitstempel):
    return datetime.strptime(zeitstempel, "%Y-%m-%dT%H:%M:%S%z").astimezone(ZONE)


def zahlen(n):
    """Tagesbericht aus konto.csv und der neuesten insights_*.json (Abruf täglich ca. 08:45)."""
    zeilen = list(csv.DictReader(KONTO.open())) if KONTO.exists() else []
    dateien = insights_dateien()
    if not zeilen and not dateien:
        return ["Noch keine Statistik."]
    aus = []
    if zeilen:
        letzte = zeilen[-1]
        text = f"**{letzte['followers_count']} Follower** · {letzte['media_count']} Beiträge im Profil (Abruf {letzte['datum']})"
        frueher = [z for z in zeilen if z["datum"] < letzte["datum"]]
        if frueher:
            diff = int(letzte["followers_count"]) - int(frueher[-1]["followers_count"])
            text += f" · **{diff:+d}** seit {frueher[-1]['datum']}" + (" ⚠️" if diff < 0 else "")
        aus.append(text)
    if dateien:
        d = json.loads(dateien[-1].read_text())
        alt = {b["id"]: b for b in json.loads(dateien[-2].read_text()).get("beitraege", [])} if len(dateien) > 1 else {}
        tage = sorted((d.get("tageswerte_reichweite") or {}).items())[-4:]
        if tage:
            aus.append("Reichweite pro Tag: " + " · ".join(f"{t[8:10]}.{t[5:7]}. **{v}**" for t, v in tage))
        storys = sorted(d.get("storys_aktiv") or [], key=lambda x: x.get("zeit") or "")
        if storys:
            aus += ["", "| Story (letzte 24 h) | Aufrufe | Erreicht | Antworten | Profilbesuche | Follows |", "|---|---|---|---|---|---|"]
            aus += [f"| {tag(lokal(s['zeit']))} | {s.get('views', '–')} | {s.get('reach', '–')} | {s.get('replies', '–')} | "
                    f"{s.get('profile_visits', '–')} | {s.get('follows', '–')} |" for s in storys if s.get("zeit")]
        neu = [b for b in d.get("beitraege", []) if b.get("timestamp") and n - lokal(b["timestamp"]) < timedelta(days=14)]
        if neu:
            aus += ["", "| Beitrag (letzte 14 Tage) | Aufrufe | Erreicht | Likes | Komm. | Gespeichert | Geteilt |", "|---|---|---|---|---|---|---|"]
            for b in sorted(neu, key=lambda x: x["timestamp"], reverse=True):
                plus = f" (+{b['views'] - alt[b['id']]['views']})" if isinstance(alt.get(b["id"], {}).get("views"), int) and isinstance(b.get("views"), int) else ""
                name = (b.get("caption") or "").split("\n")[0][:40].replace("|", "/")
                aus.append(f"| {tag(lokal(b['timestamp']))} [{name}]({b.get('permalink', '')}) | {b.get('views', '–')}{plus} | "
                           f"{b.get('reach', '–')} | {b.get('likes', '–')} | {b.get('comments', '–')} | {b.get('saved', '–')} | {b.get('shares', '–')} |")
    return aus + ["", "Rohdaten: `automatik/statistik/`, Auswertung: `strategie/06_auswertung.md`"]


def automatik_daten():
    """[(Name, wann, letzter Lauf als Markdown)] – Workflow-Status über die GitHub-API (nur mit GH_TOKEN)."""
    aus = []
    token = os.environ.get("GH_TOKEN")
    for datei, name, wann in WORKFLOWS:
        letzter = "–"
        if token:
            try:
                roh = subprocess.run(
                    ["gh", "api", f"repos/{REPO}/actions/workflows/{datei}/runs?status=completed&per_page=20",
                     "--jq", '[.workflow_runs[] | select(.conclusion=="success" or .conclusion=="failure")][0]'
                             ' | [.conclusion, .updated_at, .html_url] | @tsv'],
                    capture_output=True, text=True, timeout=30).stdout.strip()
                if roh:
                    ergebnis, wann_lief, url = roh.split("\t")
                    t = datetime.fromisoformat(wann_lief.replace("Z", "+00:00")).astimezone(ZONE)
                    # erfolgreiche Läufe ohne Zeit, damit LAGE.md nicht bei jedem Posten-Lauf neu committet wird
                    letzter = "✅ ok" if ergebnis == "success" else f"🔴 [fehlgeschlagen]({url}) {tag(t)}"
            except Exception:
                pass
        aus.append((name, wann, letzter))
    return aus


def automatik(daten):
    return ["| Ablauf | Wann | Letzter Lauf |", "|---|---|---|"] + [f"| {n} | {w} | {l} |" for n, w, l in daten]


# ---------- Protokoll ----------

def art(nachricht):
    for anfang, symbol in (("Autopilot", "🤖"), ("Freigabe", "✅"), ("Statistik", "📈"), ("Musik", "🎵"),
                           ("Schlüssel", "🔑"), ("Merge", "🔀"),
                           ("Radar", "📡"), ("Kommentare", "💬"), ("LinkedIn", "💼")):
        if nachricht.startswith(anfang):
            return symbol
    return "✍️"


def plan_von(sha):
    try:
        return {e["id"]: e for e in json.loads(git("show", f"{sha}:automatik/plan.json") or "{}").get("eintraege", [])}
    except json.JSONDecodeError:
        return {}


def plan_aenderungen(sha):
    """Was sich an plan.json in diesem Commit geändert hat (neu, gelöscht, Status, Zeit)."""
    if not git("diff-tree", "--no-commit-id", "-r", "--name-only", "--root", sha, "--", "automatik/plan.json"):
        return []
    eltern = git("rev-parse", "-q", "--verify", f"{sha}^")
    alt, neu = plan_von(eltern) if eltern else {}, plan_von(sha)
    teile = [f"neu `{i}` ({neu[i]['zeit']}, {neu[i]['status']})" for i in neu if i not in alt]
    teile += [f"entfernt `{i}`" for i in alt if i not in neu]
    for i in neu:
        if i in alt:
            for feld in ("status", "zeit"):
                if alt[i].get(feld) != neu[i].get(feld):
                    teile.append(f"`{i}` {feld}: {alt[i].get(feld)} → {neu[i].get(feld)}")
            if neu[i].get("issue") and not alt[i].get("issue"):
                teile.append(f"`{i}` → Freigabe-Issue #{neu[i]['issue']}")
            if neu[i].get("fehler") and neu[i].get("fehler") != alt[i].get("fehler"):
                teile.append(f"`{i}` Fehler: {neu[i]['fehler'][:120]}")
            if neu[i].get("link") and not alt[i].get("link"):
                teile.append(f"`{i}` online: {neu[i]['link']}")
    return teile


def bereiche(sha):
    pfade = git("diff-tree", "--no-commit-id", "-r", "--name-only", "--root", sha).splitlines()
    b = []
    for p in pfade:
        teile = p.split("/")
        x = "/".join(teile[:2]) if teile[0] in ("posts", "strategie", "automatik", ".github") and len(teile) > 2 else p
        if x not in b and x != "LAGE.md":
            b.append(x)
    return b[:6] + (["…"] if len(b) > 6 else [])


def protokoll_daten():
    """Alle Commits (ohne Lage-Commits) als Dicts, neueste zuerst."""
    aus = []
    for zeile in git("log", "--format=%H%x09%aI%x09%s").splitlines():
        sha, datum, nachricht = zeile.split("\t", 2)
        if nachricht.startswith(LAGE_COMMIT):
            continue
        aend = plan_aenderungen(sha)
        aus.append({"sha": sha, "zeit": datetime.fromisoformat(datum).astimezone(ZONE), "nachricht": nachricht,
                    "art": art(nachricht), "plan": aend, "bereiche": [] if aend else bereiche(sha)})
    return aus


def protokoll(n, daten):
    tage = {}
    for c in daten:
        t, sha = c["zeit"], c["sha"]
        text = f"- {t:%H:%M} {c['art']} {c['nachricht']} ([`{sha[:7]}`](https://github.com/{REPO}/commit/{sha}))"
        if c["plan"]:
            text += "\n  - Plan: " + "; ".join(c["plan"])
        elif c["bereiche"]:
            text += "\n  - " + ", ".join(f"`{x}`" for x in c["bereiche"])
        tage.setdefault(t.date(), []).append(text)
    zeilen, alt = [], []
    for d, eintraege in tage.items():
        block = [f"**{WOCHENTAG[d.weekday()]} {d:%d.%m.%Y}**", *eintraege, ""]
        (zeilen if (n.date() - d).days < 7 else alt).extend(block)
    if alt:
        zeilen += ["<details><summary>Älter als 7 Tage</summary>", "", *alt, "</details>"]
    return zeilen


# ---------- Zusammenbau ----------

def main():
    n = datetime.now(ZONE)
    eintraege = json.loads(PLAN.read_text())["eintraege"]
    aktiv = [e for e in eintraege if e["status"] not in ("veroeffentlicht", "entfaellt")]
    kommend = [e for e in aktiv if zeit(e) >= n - NACHHOLEN]
    naechster = next((e for e in sorted(kommend, key=zeit) if e["status"] in ("freigegeben", "manuell")), None)
    # ohne eigene Lage-Commits, sonst ändert jeder Lauf den Stand und erzeugt den nächsten Commit
    stand = datetime.fromisoformat(git("log", "-1", "--format=%aI", "--invert-grep", f"--grep=^{LAGE_COMMIT}")).astimezone(ZONE)

    teile = [
        "# 🧭 Lage – maehrsteuern auf Instagram",
        "",
        f"_Automatisch erzeugt von `automatik/lage.py` – nicht von Hand bearbeiten (Notizen: `automatik/lage_notizen.md`). "
        f"Stand: letzte Änderung {tag(stand)} Uhr._",
        "",
    ]
    punkte = offene_punkte(eintraege, n)
    teile += briefing(eintraege, n, punkte)
    if naechster:
        teile += [f"**Als Nächstes online:** {TYP.get(naechster['typ'])} `{naechster['id']}` am **{tag(zeit(naechster))} Uhr** "
                  f"– {status(naechster)}"
                  + (" – 🔴 **überfällig**" if naechster["status"] == "freigegeben" and zeit(naechster) < n - UEBERFAELLIG else ""), ""]
    if NOTIZEN.exists() and (notiz := NOTIZEN.read_text().strip()):
        teile += ["## 📝 Gerade in Arbeit", "", notiz, ""]
    teile += ["## 👉 Braucht dich", "", *[f"- {p}" for p in punkte], ""]
    woche = [e for e in kommend if zeit(e) <= n + timedelta(days=7)]
    spaeter = [e for e in kommend if zeit(e) > n + timedelta(days=7)]
    teile += ["## ⏭️ Nächste 7 Tage", "", *(tabelle(woche) if woche else ["Nichts geplant."]), ""]
    if spaeter:
        teile += ["## 🗓️ Danach", "", *tabelle(spaeter), ""]
    teile += ["## ✅ Zuletzt veröffentlicht (Autopilot)", "", *veroeffentlicht(eintraege), ""]
    teile += ["## 📈 Zahlen (täglich ca. 08:45)", "", *zahlen(n), ""]
    ablaeufe, commits = automatik_daten(), protokoll_daten()
    teile += ["## ⚙️ Automatik", "", *automatik(ablaeufe), ""]
    teile += ["## 📜 Protokoll – jede Änderung", "",
              "🤖 Autopilot · ✅ Freigabe · 📈 Statistik · 🎵 Musik · 🔀 Merge · ✍️ von Hand / Claude", "",
              *protokoll(n, commits)]
    ZIEL.write_text("\n".join(teile).rstrip() + "\n")
    print(f"✓ {ZIEL.relative_to(WURZEL)} geschrieben")

    import lage_html  # gleiche Daten als grafische Seite (LAGE.html)
    lage_html.schreiben(n=n, stand=stand, eintraege=eintraege, kommend=kommend, naechster=naechster,
                        punkte=punkte, ablaeufe=ablaeufe, commits=commits)


if __name__ == "__main__":
    main()
