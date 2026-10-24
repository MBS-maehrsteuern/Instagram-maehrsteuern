"""Autopilot: veröffentlicht fällige, freigegebene Einträge aus plan.json über die Instagram-API.

Aufruf (läuft stündlich per GitHub Actions):
  python automatik/posten.py            – fällige Einträge (nächste 75 Min.) abwarten und posten
  python automatik/posten.py --probe    – nur anzeigen, was passieren würde (kein API-Aufruf, kein Commit)
  python automatik/posten.py --jetzt ID – einen freigegebenen Eintrag sofort posten
  python automatik/posten.py --test ID  – Probelauf: Instagram lädt alles hoch, es wird aber NICHTS veröffentlicht

Umgebung: IG_TOKEN, IG_USER_ID (GitHub-Secrets), GITHUB_REPOSITORY (setzt GitHub automatisch).
Instagram holt die Dateien über öffentliche Links ab; Bilder müssen JPEG sein – das Skript wandelt PNG um,
committet die JPEGs und verlinkt sie über den Commit-Stand (raw.githubusercontent.com/<repo>/<sha>/...).
Schutz vor Doppel-Posts: Status nach dem Posten über status_sichern (frischer Stand, kein Rebase-Konflikt) und vor
jedem Feed-Post der Abgleich mit den letzten Beiträgen des Kontos (schon_online). Teaser-Storys warten auf ihren
Feed-Beitrag (vorgaenger_fehlt). Tests: python3 -m unittest discover automatik/tests
"""
import json, os, subprocess, sys, time
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import requests
from PIL import Image

WURZEL = Path(__file__).resolve().parent.parent
PLAN = WURZEL / "automatik" / "plan.json"
ZONE = ZoneInfo("Europe/Berlin")
API = "https://graph.instagram.com/v23.0"
FENSTER = timedelta(minutes=75)      # so weit voraus wird gewartet
NACHHOLEN = timedelta(hours=6)       # verspätete Läufe holen bis zu 6 h nach


def jetzt():
    return datetime.now(ZONE)


def zeit(e):
    return datetime.strptime(e["zeit"], "%Y-%m-%d %H:%M").replace(tzinfo=ZONE)


def git(*args):
    return subprocess.run(["git", *args], cwd=WURZEL, check=True, capture_output=True, text=True).stdout.strip()


def speichern(plan, nachricht):
    """Committen und pushen – mit Wiederholung: geht der Status „veroeffentlicht“ verloren, würde der nächste
    Lauf denselben Beitrag noch einmal posten."""
    PLAN.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
    git("add", "-A")
    if git("status", "--porcelain"):
        git("commit", "-m", nachricht)
        for versuch in range(6):
            try:
                git("pull", "--rebase", "-q")
                git("push")
                break
            except subprocess.CalledProcessError as fehler:
                subprocess.run(["git", "rebase", "--abort"], cwd=WURZEL, capture_output=True)
                print(f"Push-Versuch {versuch + 1} fehlgeschlagen: {fehler.stderr.strip()[:200]}")
                time.sleep(5 * (versuch + 1))
        else:
            raise RuntimeError(f"plan.json nicht gepusht ({nachricht}) – Beitrag ist ggf. schon online, Plan prüfen!")
    return git("rev-parse", "HEAD")


def status_sichern(eid, felder, nachricht, versuche=8):
    """Status EINES Eintrags robust ins Repo bringen (nach dem Posten): immer den frischen GitHub-Stand holen und nur
    dessen Felder setzen – ein Rebase-Konflikt (z. B. Claude ändert gerade „hinweis“ daneben) kann so nicht entstehen.
    Lokale, nicht gepushte Commits fallen dabei weg; die JPGs sind zu diesem Zeitpunkt längst gepusht.
    Gibt den neuen Plan zurück."""
    for versuch in range(versuche):
        try:
            git("fetch", "-q")
            git("reset", "-q", "--hard", "@{u}")
            plan = json.loads(PLAN.read_text())
            eintrag = next((x for x in plan["eintraege"] if x["id"] == eid), None)
            if eintrag is None:  # inzwischen umbenannt/gelöscht – nichts zu schreiben, aber laut melden
                print(f"⚠ {eid} steht nicht mehr im Plan – Status {felder.get('status')} NICHT gespeichert")
                return plan
            eintrag.update(felder)
            PLAN.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
            if git("status", "--porcelain", "--", str(PLAN)):
                git("commit", "-q", "-m", nachricht, "--", str(PLAN))
                git("push", "-q")
            return plan
        except subprocess.CalledProcessError as fehler:
            print(f"Status-Versuch {versuch + 1} fehlgeschlagen: {(fehler.stderr or '').strip()[:200]}")
            time.sleep(5 * (versuch + 1))
    raise RuntimeError(f"Status {felder.get('status')} für {eid} nicht gepusht – Beitrag ist ggf. schon online, Plan prüfen!")


def als_jpeg(ordner, namen):
    """PNG → JPEG (Instagram nimmt für Bilder nur JPEG). Gibt die Repo-Pfade der JPEGs zurück."""
    pfade = []
    for n in namen:
        quelle = WURZEL / ordner / n
        ziel = WURZEL / ordner / "_jpg" / (Path(n).stem + ".jpg")
        ziel.parent.mkdir(exist_ok=True)
        if not ziel.exists():
            Image.open(quelle).convert("RGB").save(ziel, "JPEG", quality=92, optimize=True)
        pfade.append(ziel.relative_to(WURZEL).as_posix())
    return pfade


def link(sha, pfad):
    return f"https://raw.githubusercontent.com/{os.environ['GITHUB_REPOSITORY']}/{sha}/{pfad}"


class Instagram:
    def __init__(self):
        self.token = os.environ["IG_TOKEN"]
        self.user = os.environ["IG_USER_ID"]

    def _anfrage(self, methode, pfad, wiederholen=True, **kwargs):
        """Kurze Aussetzer (Verbindung, Zeitüberschreitung, 5xx) bis zu 3× wiederholen – außer bei media_publish:
        dort kann eine Zeitüberschreitung heißen, dass der Beitrag schon online ist."""
        for versuch in range(3 if wiederholen else 1):
            try:
                r = requests.request(methode, f"{API}/{pfad}", **kwargs)
            except (requests.ConnectionError, requests.Timeout):
                if not wiederholen or versuch == 2:
                    raise
            else:
                if r.ok:
                    return r.json()
                if r.status_code < 500 or not wiederholen or versuch == 2:
                    raise RuntimeError(f"{pfad}: {r.status_code} {r.text}")
            time.sleep(10 * (versuch + 1))

    def _post(self, pfad, wiederholen=True, **daten):
        return self._anfrage("POST", pfad, wiederholen, data={**daten, "access_token": self.token}, timeout=120)

    def _get(self, pfad, **params):
        return self._anfrage("GET", pfad, params={**params, "access_token": self.token}, timeout=60)

    def container(self, **daten):
        cid = self._post(f"{self.user}/media", **daten)["id"]
        for _ in range(60):  # Instagram verarbeitet Videos asynchron
            status = self._get(cid, fields="status_code").get("status_code")
            if status == "FINISHED":
                return cid
            if status in ("ERROR", "EXPIRED"):
                raise RuntimeError(f"Container {cid}: {status}")
            time.sleep(10)
        raise RuntimeError(f"Container {cid}: Zeitüberschreitung")

    def veroeffentlichen(self, cid):
        mid = self._post(f"{self.user}/media_publish", wiederholen=False, creation_id=cid)["id"]
        try:  # ab hier ist der Beitrag online – ein fehlender Link darf ihn nicht als „fehler“ markieren
            return mid, self._get(mid, fields="permalink").get("permalink")
        except Exception as fehler:
            print(f"Hinweis: Link zu {mid} nicht abrufbar ({fehler})")
            return mid, None

    def kommentieren(self, mid, text):
        return self._post(f"{mid}/comments", message=text)["id"]


def erster_kommentar(ig, e, mid):
    """Direkt nach einem Feed-Beitrag den ersten Kommentar (posts/<ordner>/erster_kommentar.txt) setzen. Gibt die
    Kommentar-ID zurück oder None. Fehler hier verändern den Beitrag nie – nur eine Warnung."""
    if e["typ"] == "story" or not mid or e.get("erster_kommentar_id"):
        return None
    try:
        datei = WURZEL / e["ordner"] / "erster_kommentar.txt"
        text = datei.read_text().strip() if datei.is_file() else ""
        return ig.kommentieren(mid, text) if text else None
    except Exception as fehler:
        print(f"⚠ {e['id']}: erster Kommentar nicht gesetzt ({str(fehler).replace(ig.token, '***')[:200]})")
        return None


def pruefen(e):
    """Gibt einen Grund zurück, warum der Eintrag (noch) nicht gepostet werden darf – oder None."""
    if e["typ"] == "reel":
        if not (WURZEL / e["ordner"] / e["video"]).exists():
            return "Video fehlt"
        if e.get("musik_fehlt"):
            return "Reel ist noch stumm (musik_fehlt) – erst Musik einbauen oder Feld entfernen"
        if e.get("stimme") is not True:  # Loris 24.10.: nie wieder ein Reel ohne seine Stimme
            return "Reel ohne Loris' Stimme (stimme muss true sein) – erst mit Aufnahme neu bauen"
    for n in e.get("bilder", []):
        if not (WURZEL / e["ordner"] / n).exists():
            return f"Bild fehlt: {n}"
    return None


def beitragstext(e):
    return (WURZEL / e["ordner"] / e["text"]).read_text().strip() if e.get("text") else ""


def inhalt(e):
    """Was sich während des Wartens ändern kann (v. a. die Bildunterschrift) – dann wird der Container neu angelegt.
    Die JPGs bleiben wie bisher die vom Vorbereiten."""
    return (e["typ"], e.get("ordner"), e.get("video"), beitragstext(e))


def schon_online(ig, e):
    """Ist der Feed-Beitrag schon auf dem Konto (z. B. Status nach dem Posten nicht gepusht)? Vergleicht den Anfang der
    Bildunterschrift mit den letzten 10 Beiträgen der letzten 3 Tage. Gibt den Treffer (id, permalink, timestamp) oder None.
    Storys haben keine Bildunterschrift – dort greift nur der robuste Status-Push (status_sichern)."""
    kopf = " ".join(beitragstext(e).split())[:80]
    if e["typ"] == "story" or len(kopf) < 20:
        return None
    grenze = min(zeit(e), jetzt()) - timedelta(days=3)
    for m in ig._get(f"{ig.user}/media", fields="id,caption,permalink,timestamp", limit=10).get("data", []):
        try:
            am = datetime.strptime(m["timestamp"], "%Y-%m-%dT%H:%M:%S%z")
        except (KeyError, ValueError):
            continue
        if am >= grenze and " ".join((m.get("caption") or "").split()).startswith(kopf):
            return m
    return None


def vorgaenger_fehlt(e, plan):
    """Teaser-/Folge-Story: gehört zum Feed-Beitrag mit derselben Nummer NN, der am selben Tag früher geplant ist.
    Ist der nicht veröffentlicht (fehler, gestoppt, noch offen), darf die Story nicht raus („Neues Reel ist da“ ohne Reel)."""
    if e["typ"] != "story":
        return None
    nr = e["id"].split("-")[0]
    for x in plan["eintraege"]:
        if (x["typ"] != "story" and x["id"].split("-")[0] == nr and x["zeit"][:10] == e["zeit"][:10]
                and x["zeit"] < e["zeit"] and x["status"] != "veroeffentlicht"):
            return f"Feed-Beitrag {x['id']} ist nicht online (Status {x['status']})"
    return None


def posten(ig, e, sha, veroeffentlichen=True):
    text = beitragstext(e)
    if e["typ"] == "karussell":
        kinder = [ig.container(image_url=link(sha, p), is_carousel_item="true") for p in e["_jpg"]]
        cid = ig.container(media_type="CAROUSEL", children=",".join(kinder), caption=text)
    elif e["typ"] == "bild":
        cid = ig.container(image_url=link(sha, e["_jpg"][0]), caption=text)
    elif e["typ"] == "story":
        cid = ig.container(media_type="STORIES", image_url=link(sha, e["_jpg"][0]))
    elif e["typ"] == "reel":
        daten = dict(media_type="REELS", video_url=link(sha, f"{e['ordner']}/{e['video']}"), caption=text, share_to_feed="true")
        if e.get("_jpg"):
            daten["cover_url"] = link(sha, e["_jpg"][0])
        cid = ig.container(**daten)
    else:
        raise ValueError(f"Unbekannter Typ {e['typ']}")
    if not veroeffentlichen:
        return cid, None
    return ig.veroeffentlichen(cid)


def probelauf(eid):
    """Container anlegen und von Instagram verarbeiten lassen, aber nicht veröffentlichen.
    Nicht veröffentlichte Container verfallen nach 24 Stunden von selbst."""
    plan = json.loads(PLAN.read_text())
    e = next(x for x in plan["eintraege"] if x["id"] == eid)
    grund = pruefen(e)
    if grund and not grund.startswith("Reel ist noch stumm"):
        sys.exit(f"✗ {eid}: {grund}")
    bilder = e.get("bilder") or ([e["titelbild"]] if e.get("titelbild") else [])
    e["_jpg"] = als_jpeg(e["ordner"], bilder)
    sha = speichern(plan_ohne_intern(plan), f"Autopilot: Dateien fuer Probelauf {eid} vorbereitet")
    cid, _ = posten(Instagram(), e, sha, veroeffentlichen=False)
    print(f"✓ Probelauf {eid}: Instagram hat alles angenommen (Container {cid}). Nichts veröffentlicht.")


def main():
    if "--test" in sys.argv:
        return probelauf(sys.argv[sys.argv.index("--test") + 1])
    probe = "--probe" in sys.argv
    sofort = sys.argv[sys.argv.index("--jetzt") + 1] if "--jetzt" in sys.argv else None
    plan = json.loads(PLAN.read_text())
    n = jetzt()
    faellig = [e for e in plan["eintraege"] if e["status"] == "freigegeben" and
               (e["id"] == sofort if sofort else n - NACHHOLEN <= zeit(e) <= n + FENSTER)]
    if not faellig:
        print("Nichts fällig.", n.strftime("%d.%m. %H:%M"))
        return
    ig = None if probe else Instagram()
    fehlgeschlagen = []
    for e in sorted(faellig, key=zeit):
        # immer den Eintrag aus dem aktuellen Plan nehmen (der Plan wird nach dem Warten neu gelesen)
        e = next((x for x in plan["eintraege"] if x["id"] == e["id"]), None)
        if not e or e["status"] != "freigegeben":
            continue
        grund = pruefen(e)
        if grund:
            print(f"✗ {e['id']}: {grund}")
            continue
        # Teaser ohne Feed-Beitrag: schon hier aussteigen (spart Commit und Container); geprüft wird direkt vor dem
        # Posten noch einmal mit dem frischen Plan
        grund = vorgaenger_fehlt(e, plan)
        if grund:
            print(f"↷ {e['id']}: {grund} – Story übersprungen (holt ein späterer Lauf nach, sobald er online ist)")
            continue
        bilder = e.get("bilder") or ([e["titelbild"]] if e.get("titelbild") else [])
        if probe:
            print(f"• {e['id']} ({e['typ']}) um {e['zeit']}: {len(bilder)} Bild(er)", e.get("video", ""))
            continue
        # Vorbereiten: JPGs committen, dann Container anlegen (Upload + Verarbeitung) – schon VOR dem Warten,
        # damit um die geplante Minute nur noch media_publish läuft (Container gelten 24 h). Ein Fehler hier trifft
        # nur diesen Eintrag, nicht den ganzen Lauf.
        try:
            e["_jpg"] = als_jpeg(e["ordner"], bilder)
            sha = speichern(plan_ohne_intern(plan), f"Autopilot: Dateien fuer {e['id']} vorbereitet")
            vorbereitet = inhalt(e)
            cid, _ = posten(ig, e, sha, veroeffentlichen=False)
        except Exception as fehler:
            plan = fehler_sichern(ig, e["id"], fehler, fehlgeschlagen, "Vorbereitung") or plan
            continue
        warten = (zeit(e) - jetzt()).total_seconds()
        if warten > 0 and not sofort:
            print(f"… warte {int(warten // 60)} Min. bis {e['zeit']} für {e['id']} (Container {cid} liegt bereit)")
            time.sleep(warten)
        # Direkt vor dem Posten IMMER den neuesten Plan holen – nicht nur nach dem Warten: Ein Lauf startet mit dem
        # Stand vom Start-Zeitpunkt; hat ein früherer Lauf den Beitrag inzwischen gepostet, steht das nur auf GitHub
        # (04.10.: Reel doppelt online). Auch „stop“, eine neue Zeit oder „entfaellt“ während des Wartens greifen so.
        try:
            git("pull", "--rebase", "-q")
            plan = json.loads(PLAN.read_text())
        except subprocess.CalledProcessError as fehler:
            subprocess.run(["git", "rebase", "--abort"], cwd=WURZEL, capture_output=True)
            print(f"✗ {e['id']}: Plan nicht neu geladen ({fehler.stderr.strip()[:200]}) – nicht gepostet, nächster Lauf versucht es erneut")
            continue
        aktuell = next((x for x in plan["eintraege"] if x["id"] == e["id"]), None)
        if not aktuell or aktuell["status"] != "freigegeben" or aktuell["zeit"] != e["zeit"]:
            print(f"↷ {e['id']}: Plan hat sich geändert (schon gepostet, gestoppt oder verschoben) – übersprungen")
            continue
        grund = vorgaenger_fehlt(aktuell, plan)
        if grund:
            print(f"↷ {e['id']}: {grund} – Story übersprungen (holt ein späterer Lauf nach, sobald er online ist)")
            continue
        aktuell["_jpg"], e = e["_jpg"], aktuell
        try:
            treffer = schon_online_sicher(ig, e)
            if treffer:  # früherer Lauf hat gepostet, der Status ging verloren → nur nachtragen, NICHT erneut posten
                am = datetime.strptime(treffer["timestamp"], "%Y-%m-%dT%H:%M:%S%z").astimezone(ZONE)
                felder = dict(status="veroeffentlicht", media_id=treffer["id"], link=treffer.get("permalink"),
                              veroeffentlicht_am=am.strftime("%Y-%m-%d %H:%M"))
                print(f"↷ {e['id']} war schon online ({treffer.get('permalink')}) – Doppel-Post verhindert, Status nachgetragen")
            else:
                if inhalt(e) != vorbereitet:  # Text/Dateien während des Wartens geändert → frischer Container
                    print(f"… {e['id']}: Inhalt geändert – Container wird neu angelegt")
                    cid, _ = posten(ig, e, sha, veroeffentlichen=False)
                mid, permalink = ig.veroeffentlichen(cid)
                felder = dict(status="veroeffentlicht", media_id=mid, link=permalink,
                              veroeffentlicht_am=jetzt().strftime("%Y-%m-%d %H:%M"))
                print(f"✓ {e['id']} online: {permalink}")
                kid = erster_kommentar(ig, e, mid)
                if kid:
                    felder["erster_kommentar_id"] = kid
                erste_stunde({**e, **felder})
        except Exception as fehler:
            plan = fehler_sichern(ig, e["id"], fehler, fehlgeschlagen) or plan
            continue
        try:
            plan = status_sichern(e["id"], felder, f"Autopilot: {e['id']} veroeffentlicht")
        except Exception as fehler:  # Beitrag ist online; der nächste Lauf erkennt ihn über schon_online()
            print(f"✗ {e['id']}: {fehler}")
            fehlgeschlagen.append(e["id"])
    if fehlgeschlagen:
        sys.exit(1)


def schon_online_sicher(ig, e):
    """schon_online(), aber ein Fehler bei der Abfrage verhindert das Posten nicht (Verhalten wie bisher)."""
    try:
        return schon_online(ig, e)
    except Exception as fehler:
        print(f"Hinweis: Prüfung „schon online?“ für {e['id']} nicht möglich ({str(fehler).replace(ig.token, '***')[:200]})")
        return None


def fehler_sichern(ig, eid, fehler, fehlgeschlagen, schritt="Posten"):
    """Fehler im Plan vermerken, damit er im Repo sichtbar ist – nur für diesen Eintrag. Gibt den neuen Plan zurück
    (oder None, wenn auch das nicht ging)."""
    # Verbindungsfehler enthalten die URL samt access_token – nie ins öffentliche Repo schreiben
    meldung = f"{schritt}: {fehler}".replace(ig.token, "***")
    fehlgeschlagen.append(eid)
    print(f"✗ {eid}: {meldung}")
    try:
        return status_sichern(eid, dict(status="fehler", fehler=meldung[:500]), f"Autopilot: {eid} fehler")
    except Exception as weiterer:
        print(f"✗ {eid}: Fehler-Status nicht gespeichert ({weiterer})")
        return None


def erste_stunde(e):
    """Nach einem Feed-Beitrag: Checkliste als Kommentar ins bestehende Freigabe-Issue (kein neues Issue).
    Fehler hier stoppen das Posten nie."""
    if e["typ"] not in ("karussell", "reel", "bild") or not e.get("issue") or not os.environ.get("GH_TOKEN"):
        return
    repo = os.environ["GITHUB_REPOSITORY"]
    suche = f"https://github.com/{repo}/issues?q=is%3Aopen+label%3A"
    zeilen = [f"Moin, `{e['id']}` ist online 🚀 [Beitrag ansehen]({e.get('link')})", "",
              "Die erste Stunde zählt doppelt – wie Fristverlängerung, nur ohne Antrag:", "",
              "- [ ] In die Story teilen (Papierflieger → „Zu deiner Story hinzufügen“), mit Sticker oder kurzer Frage",
              f"- [ ] Kommentare zügig beantworten → [💬 Kommentare]({suche}kommentare) (`K12 ok` reicht)",
              f"- [ ] 2–3 Beiträge aus dem [📡 Radar]({suche}radar) kommentieren – bringt Gegenbesuch"]
    if e["typ"] == "karussell":
        zeilen.append(f"- [ ] LinkedIn-Paket steht bereit → [💼 LinkedIn]({suche}linkedin)")
    try:
        subprocess.run(["gh", "issue", "comment", str(e["issue"]), "--repo", repo, "--body", "\n".join(zeilen)],
                       check=True, capture_output=True, text=True, timeout=60)
    except Exception as fehler:
        print(f"Hinweis: Erste-Stunde-Checkliste nicht gepostet ({fehler})")


def plan_ohne_intern(plan):
    return {**plan, "eintraege": [{k: v for k, v in e.items() if not k.startswith("_")} for e in plan["eintraege"]]}


if __name__ == "__main__":
    main()
