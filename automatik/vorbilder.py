"""Vorbilder-Radar (Wissen 21 §6, Loris 27.10.): einmal pro Woche die stärksten Beiträge ausgewählter Steuer-Accounts
sammeln – als Rohstoff für Hooks, Themen und Formate. Nur lesen, nie interagieren.

Die Graph-API (business_discovery) liefert für fremde Konten Likes und Kommentare, aber KEINE Aufrufe. „Ausreißer“
heißt darum: Interaktion (Likes + 3 × Kommentare) mindestens doppelt so hoch wie der Median des Kontos.
Konten: automatik/interaktion.json → "vorbilder". Ergebnis: recherche/vorbilder.json (alle gesehenen Beiträge),
recherche/viral_liste.csv (neue Ausreißer angehängt), recherche/vorbilder_bericht.md (Top der Woche).
  python automatik/vorbilder.py            – normaler Lauf (überspringt, wenn diese Woche schon gelaufen)
  python automatik/vorbilder.py --erzwingen
  python automatik/vorbilder.py --probe    – nur abfragen und Bericht ausgeben, nichts speichern"""
import csv, json, os, statistics, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from radar import api, Gedrosselt, JETZT, WURZEL, kurz

ORDNER = WURZEL / "recherche"
DATEN, LISTE, BERICHT = ORDNER / "vorbilder.json", ORDNER / "viral_liste.csv", ORDNER / "vorbilder_bericht.md"
KONTEN = json.loads((WURZEL / "automatik" / "interaktion.json").read_text()).get("vorbilder", [])
FELDER = "id,caption,permalink,timestamp,like_count,comments_count,media_type,media_product_type"
PROBE = "--probe" in sys.argv
WOCHE = JETZT.strftime("%G-W%V")
FORMATE = {"REELS": "Reel", "FEED": "Beitrag"}


def wert(m):
    return (m.get("like_count") or 0) + 3 * (m.get("comments_count") or 0)


def hook(caption):
    zeile = next((z.strip() for z in (caption or "").splitlines() if z.strip()), "")
    return kurz(zeile, 120)


def main():
    daten = json.loads(DATEN.read_text()) if DATEN.exists() else {"wochen": [], "beitraege": {}}
    if WOCHE in daten["wochen"] and "--erzwingen" not in sys.argv and not PROBE:
        print(f"Vorbilder: {WOCHE} schon erledigt.")
        return
    fehler, neu = [], []
    for name in KONTEN:
        try:
            b = api(os.environ["FB_IG_USER_ID"], fields=f"business_discovery.username({name}){{username,followers_count,"
                                                         f"media.limit(50){{{FELDER}}}}}")["business_discovery"]
        except Gedrosselt as e:
            fehler.append(f"Meta drosselt ({e}) – nächste Woche wieder"); break
        except RuntimeError as e:
            fehler.append(f"@{name}: {e}"); continue
        medien = b.get("media", {}).get("data", [])
        if not medien:
            continue
        median = statistics.median(wert(m) for m in medien) or 1
        for m in medien:
            alt = daten["beitraege"].get(m["id"], {})
            eintrag = {"konto": name, "follower": b.get("followers_count"), "link": m.get("permalink"),
                       "datum": m["timestamp"][:10], "format": FORMATE.get(m.get("media_product_type"), m.get("media_type")),
                       "likes": m.get("like_count"), "kommentare": m.get("comments_count"), "hook": hook(m.get("caption")),
                       "faktor": round(wert(m) / median, 1), "gemeldet": alt.get("gemeldet")}
            daten["beitraege"][m["id"]] = eintrag
            if eintrag["faktor"] >= 2 and not eintrag["gemeldet"]:
                neu.append(eintrag)
        time.sleep(1)
    top = sorted(neu, key=lambda e: -e["faktor"])[:15]
    zeilen = [f"# Vorbilder-Radar {WOCHE} ({JETZT:%d.%m.%Y})", "",
              "Ausreißer = Likes + 3×Kommentare ≥ 2× Median des Kontos (Aufrufe liefert die API für fremde Konten nicht).",
              "Nur Muster übernehmen (Hook, Thema, Format) – Inhalt immer selbst prüfen.", ""]
    zeilen += [f"- **{e['faktor']}×** @{e['konto']} · {e['format']} · {e['datum']} · ❤ {e['likes']} · 💬 {e['kommentare']}"
               f"  \n  „{e['hook']}“ – {e['link']}" for e in top] or ["Keine neuen Ausreißer diese Woche."]
    zeilen += [""] + [f"⚠ {f}" for f in fehler]
    text = "\n".join(zeilen) + "\n"
    print(text)
    if PROBE:
        return
    ORDNER.mkdir(exist_ok=True)
    neue_datei = not LISTE.exists()
    with LISTE.open("a", newline="") as f:
        w = csv.writer(f)
        if neue_datei:
            w.writerow(["hook", "unterthema", "format", "aufrufe", "account", "link", "notiz", "verwendet"])
        for e in top:
            w.writerow([e["hook"], "", e["format"], "", e["konto"], e["link"],
                        f"Radar {WOCHE}: {e['faktor']}× Median, {e['likes']} Likes, {e['kommentare']} Kommentare", ""])
            daten["beitraege"][next(k for k, v in daten["beitraege"].items() if v is e)]["gemeldet"] = WOCHE
    daten["wochen"] = sorted(set(daten["wochen"]) | {WOCHE})
    DATEN.write_text(json.dumps(daten, ensure_ascii=False, indent=1) + "\n")
    BERICHT.write_text(text)


if __name__ == "__main__":
    main()
