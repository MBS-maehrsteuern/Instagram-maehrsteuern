# Routine „Instagram Tagesbericht 9 Uhr“ – Neu anlegen

Anlegen unter https://claude.ai/code → **Routines** → **Neue Routine**.
Danach die alte Routine (trig_01NFxCkqw9NYi4JrF5Xff81e) pausieren oder löschen, sonst laufen zwei.

## Einstellungen

| Feld | Wert |
|---|---|
| Name | Instagram Tagesbericht 9 Uhr |
| Zeitplan | täglich 09:15 (Europe/Berlin) |
| Repository | **MBS-maehrsteuern/Instagram-maehrsteuern** – Zugriff **Schreiben** (nicht den alten Namen `maehrsteuern/…`) |
| Branch | `claude/fervent-newton-ijmv6t` |
| Umgebung | dieselbe wie bisher (Netzwerk: vertrauenswürdig/Standard, Setup-Skript unverändert) |
| Connectors | Google Calendar, (Artifacts sind eingebaut) |
| Modell | Opus |
| Berechtigungsmodus | Auto |

## Prompt (komplett einfügen)

```
Tägliche Routine „Instagram Tagesbericht“ für maehrsteuern. Arbeite im Repo, Branch claude/fervent-newton-ijmv6t. Halte dich an CLAUDE.md und README.md (keine Arbeitgeber-Daten, KI-Label).

1. Frische Zahlen holen: Prüfe auf origin/claude/instagram, ob es unter automatik/statistik/ schon Insights von heute gibt. Wenn nicht: Workflow starten
   gh api -X POST repos/MBS-maehrsteuern/Instagram-maehrsteuern/actions/workflows/statistik.yml/dispatches -f ref=claude/instagram
   und warten, bis der Lauf fertig ist (gh api repos/MBS-maehrsteuern/Instagram-maehrsteuern/actions/runs), dann git fetch. Schlägt der Start fehl (403), mit den neuesten vorhandenen Insights weitermachen und im Bericht „⚠️ Datenstand <Datum Uhrzeit>“ vermerken. Keine Credentials selbst erzeugen, Sperren nicht umgehen.
2. python3 automatik/tagesbericht.py ausführen (optional Datum als Argument), das PNG unter automatik/berichte/ ansehen.
3. Interaktives Dashboard aktualisieren: https://claude.ai/artifact/9epPJLmgBTs2hydM6T6CVZ – Datensätze datasets/{kennzahlen,verlauf,beitraege,methoden,heute} per ArtifactData (batch, mit if_version) auf den neuen Stand bringen. verlauf: Vortag mit reichweite, follower, werbung=false anhängen. Methoden-Status: ✅ greift / ⚠️ knapp / ❌ greift nicht / ⏳ zu früh.
4. PNG per SendUserFile schicken (display render, status proactive), Caption mit Datenstand und Dashboard-Link.
5. Bericht im Chat auf Deutsch:
   a) Konto-Tabelle (Follower, Reichweite, Profilaufrufe, Website-Klicks mit Δ) + Beiträge mit Δ Aufrufe, Skip-Rate, Ø Sehdauer
   b) Greifen unsere Methoden? (Hook, Sehdauer, Teilen, Speichern, Storys, Stichwort-DMs, Profil)
   c) Was wir ändern – NUR vorschlagen, nichts umsetzen ohne Go von Loris
   d) Heute geplant (plan.json auf origin/claude/instagram), Fehler, offene To-dos für Loris
6. Google-Kalender-Termin heute 09:00–09:10 Europe/Berlin, transparency free, keine Erinnerungen (useDefaultReminders false), Titel:
   „📈 Instagram-Tagesbericht: <Follower> Follower (<±Δ>) · <wichtigste Zahl>“, Beschreibung = Kurzfassung des Berichts. Nur belegte Zahlen.
7. Bericht-Dateien committen (Autor: Loris M. <mkwloris@googlemail.com>, deutsche Nachricht) und nach claude/fervent-newton-ijmv6t pushen. Nichts an claude/instagram ändern ohne Freigabe von Loris.
8. PushNotification mit <routine_summary>: erster Satz = wichtigste Erkenntnis, danach Kernzahlen und was Loris entscheiden muss.

NIEMALS automatik/posten.py ausführen (postet live). Kein git reset --hard.
```
