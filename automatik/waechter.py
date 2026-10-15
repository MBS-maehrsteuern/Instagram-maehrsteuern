"""Wächter (läuft mit jedem Lage-Lauf): EIN offenes Issue „🚨 Wächter“, das nur bei echten Problemen kommentiert wird.

- Workflow fehlgeschlagen → ein Kommentar, solange er rot bleibt kein weiterer. Wieder grün → nur der Status im
  Issue-Text ändert sich (keine Benachrichtigung).
- Posten-Takt steht: letzter Anstoß von cron-job.org (workflow_dispatch auf posten.yml) älter als 40 Min. → ein
  Kommentar, bis der Takt wieder läuft.
- Schlüssel gilt weniger als 14 Tage (automatik/schluessel_ablauf.json, schreibt token.yml) → ein Kommentar je Ablaufdatum.
Mehrere neue Probleme in einem Lauf landen gebündelt in einem Kommentar. Der Merkzustand steht unsichtbar im Issue-Text,
damit nichts committet werden muss.
Umgebung: GH_TOKEN (issues:write, actions:read), GITHUB_REPOSITORY.
"""
import json, os, re, subprocess, sys
from datetime import date, datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lage import WORKFLOWS
from ablauf import DATEI as ABLAUF

REPO = os.environ.get("GITHUB_REPOSITORY", "MBS-maehrsteuern/Instagram-maehrsteuern")
LABEL = "waechter"
WARNTAGE = 14
TAKT_MINUTEN = 40   # cron-job.org stößt posten.yml alle 15 Min. an – älter als 40 Min. heißt: Takt steht
ZUSTAND = re.compile(r"<!-- zustand (\{.*?\}) -->", re.S)


def gh(*args, eingabe=None):
    return subprocess.run(["gh", *args], input=eingabe, check=True, capture_output=True, text=True).stdout.strip()


def letzter_lauf(datei):
    roh = gh("api", f"repos/{REPO}/actions/workflows/{datei}/runs?status=completed&per_page=100", "--jq",
             '[.workflow_runs[] | select(.conclusion=="success" or .conclusion=="failure")][0]'
             ' | [.conclusion, .html_url, .updated_at] | @tsv')
    return roh.split("\t") if roh else None


def takt_alter():
    """Minuten seit dem letzten Anstoß von posten.yml per workflow_dispatch (= cron-job.org, selten Loris von Hand)."""
    roh = gh("api", f"repos/{REPO}/actions/workflows/posten.yml/runs?event=workflow_dispatch&per_page=1", "--jq",
             ".workflow_runs[0].created_at // empty")
    if not roh:
        return None
    return (datetime.now(timezone.utc) - datetime.fromisoformat(roh.replace("Z", "+00:00"))).total_seconds() / 60


def issue_holen():
    roh = gh("issue", "list", "--repo", REPO, "--label", LABEL, "--state", "open", "--json", "number,body", "--limit", "1")
    offen = json.loads(roh)
    if offen:
        treffer = ZUSTAND.search(offen[0]["body"])
        return offen[0]["number"], json.loads(treffer.group(1)) if treffer else {}
    try:
        gh("label", "create", LABEL, "--repo", REPO, "--color", "D73A4A", "--description", "Fehler und ablaufende Schlüssel")
    except subprocess.CalledProcessError:
        pass
    url = gh("issue", "create", "--repo", REPO, "--title", "🚨 Wächter", "--label", LABEL, "--body", "wird gleich befüllt …")
    return int(url.rstrip("/").split("/")[-1]), {}


def main():
    nummer, zustand = issue_holen()
    alt = json.dumps(zustand, sort_keys=True)
    zustand.setdefault("rot", {})
    zustand.setdefault("gewarnt", {})
    neu, zeilen = [], []
    for datei, name, _ in WORKFLOWS:
        try:
            lauf = letzter_lauf(datei)
        except subprocess.CalledProcessError:
            lauf = None
        if not lauf:
            zeilen.append(f"| {name} | – |")
            continue
        ergebnis, url, wann = lauf
        if ergebnis == "failure":
            if zustand["rot"].get(datei) is None:
                neu.append(f"🔴 **{name}** ist fehlgeschlagen – [Lauf ansehen]({url})")
            zustand["rot"][datei] = url
            zeilen.append(f"| {name} | 🔴 [fehlgeschlagen]({url}) |")
        else:
            zustand["rot"].pop(datei, None)
            zeilen.append(f"| {name} | ✅ |")
    # Takt: cron-job.org stößt posten.yml alle 15 Min. per workflow_dispatch an. Fällt er aus, bleibt jeder Lauf grün,
    # aber Beiträge gehen nur noch mit GitHubs eigenem Zeitplan raus (real alle 4–7 h). Gezählt wird der Anstoß
    # (created_at, egal ob erfolgreich, abgebrochen oder wartend): Ein Lauf, der bis 17:45 schläft, lässt die
    # folgenden Anstöße als „cancelled“ enden – die Erfolgszeit wäre dann bis 75 Min. alt, ohne dass etwas kaputt ist.
    try:
        alter = takt_alter()
    except (subprocess.CalledProcessError, ValueError):
        alter = None
    if alter is None:
        zeilen.append("| Posten-Takt (cron-job.org) | – |")
    elif alter > TAKT_MINUTEN:
        if not zustand.get("takt"):
            neu.append(f"⏱️ **Posten-Takt steht** – letzter Anstoß von cron-job.org vor {alter:.0f} Min. (Soll: alle 15 Min.). "
                       "Beiträge gehen jetzt nur noch mit GitHubs eigenem Zeitplan raus (alle paar Stunden, ggf. gar nicht). "
                       "Bitte prüfen: ① cron-job.org einloggen → ist der Job für posten.yml aktiv? Steht er auf „deaktiviert wegen zu vieler Fehler“, erst Ursache beheben, dann wieder einschalten (Enable job). ② Verlauf dort: 401/403 = GitHub-Schlüssel "
                       "`cron-posten` abgelaufen/ungültig → neuen (Actions: write) anlegen und im Job eintragen; 404/422 = "
                       "Workflow- oder Branch-Name geändert; 404 kann auch heißen: Repo umgezogen (URL und Resource owner des Schlüssels müssen `MBS-maehrsteuern` sein). ③ Bis dahin fällige Beiträge von Hand: Actions → *Instagram posten* "
                       "→ *Run workflow*.")
        zustand["takt"] = "rot"
        zeilen.append(f"| Posten-Takt (cron-job.org) | 🔴 letzter Anstoß vor {alter:.0f} Min. |")
    else:
        zustand.pop("takt", None)
        zeilen.append("| Posten-Takt (cron-job.org) | ✅ |")
    ablauf = json.loads(ABLAUF.read_text()) if ABLAUF.exists() else {}
    heute = date.today()
    schluessel = []
    for name, datum in sorted(ablauf.items()):
        tage = (date.fromisoformat(datum) - heute).days
        warnung = tage < WARNTAGE
        schluessel.append(f"| {name} | {datum} | {'⚠️ ' if warnung else ''}noch {tage} Tage |")
        if warnung and zustand["gewarnt"].get(name) != datum:
            neu.append(f"🔑 **{name}** gilt nur noch {tage} Tage (bis {datum}) – Actions → *Instagram-Schlüssel verlängern* "
                       "→ *Run workflow*, oder von Hand erneuern (EINRICHTUNG.md)")
            zustand["gewarnt"][name] = datum
    if neu:
        gh("issue", "comment", str(nummer), "--repo", REPO, "--body", "Moin, hier hakt was:\n\n" + "\n".join(f"- {z}" for z in neu))
        print(f"✓ {len(neu)} neue Probleme gemeldet")
    if neu or json.dumps(zustand, sort_keys=True) != alt or not alt.strip("{}"):
        stand = datetime.now(ZoneInfo("Europe/Berlin")).strftime("%d.%m. %H:%M")
        text = (f"@{REPO.split('/')[0]} Dieses Issue bleibt offen. Es meldet sich **nur bei echten Problemen** "
                f"(Workflow rot, Posten-Takt steht, Schlüssel < {WARNTAGE} Tage) – bei Grün ist Funkstille, wie bei einer Steuererklärung ohne Rückfragen. "
                "Bitte nicht schließen.\n\n"
                f"**Stand {stand}**\n\n| Ablauf | Letzter Lauf |\n|---|---|\n" + "\n".join(zeilen) +
                "\n\n| Schlüssel | gültig bis | |\n|---|---|---|\n" + ("\n".join(schluessel) or "| – | – | – |") +
                f"\n\n<!-- zustand {json.dumps(zustand, sort_keys=True)} -->")
        gh("issue", "edit", str(nummer), "--repo", REPO, "--body", text)
    print("Wächter: alles ruhig." if not neu else "Wächter: gemeldet.")


if __name__ == "__main__":
    main()
