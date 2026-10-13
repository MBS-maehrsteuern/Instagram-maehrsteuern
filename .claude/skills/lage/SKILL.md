---
name: lage
description: Überblick über den Instagram-Content-Plan von maehrsteuern – was gerade läuft, was als Nächstes online geht, was von Hand zu tun ist und was zuletzt passiert ist. IMMER zu Beginn jeder Sitzung in diesem Repo nutzen und nach jeder Änderung an plan.json, posts/, strategie/ oder automatik/. Auch bei „Lage“, „Überblick“, „Stand“, „was läuft gerade“, „was kommt als Nächstes“, „was ist passiert“.
---

# Lage – der laufende Überblick

`LAGE.md` im Repo-Wurzelordner ist die eine Seite, auf der Loris jederzeit sieht, was auf Instagram passiert.
Sie wird von `automatik/lage.py` erzeugt und von `.github/workflows/lage.yml` nach **jedem Push**, nach **jedem Lauf**
von Posten/Freigabe/Statistik/Schlüssel/Musik und jeden Morgen neu geschrieben. Das Protokoll darin kommt aus dem
Git-Verlauf – jeder Commit (Autopilot und von Hand) steht dort automatisch, inkl. der Änderungen an `plan.json`.
Dasselbe Skript schreibt `LAGE.html` (grafische Seite, `automatik/lage_html.py`); die Lage-Action veröffentlicht sie auf
GitHub Pages: https://maehrsteuern.github.io/Instagram-maehrsteuern/ – neue Abschnitte in LAGE.md auch dort ergänzen.

## Zu Beginn jeder Sitzung
1. `git pull` auf `claude/instagram` bzw. den Arbeitsbranch, dann `python3 automatik/lage.py`.
2. `LAGE.md` lesen – zuerst das **30-Sekunden-Briefing** ganz oben, dann **Braucht dich**, **Nächste 7 Tage** und
   **Automatik** (rote Einträge = Fehler).
3. Loris kurz sagen, was als Nächstes online geht und was offen ist, bevor anderes gemacht wird – das Briefing knapp
   zusammenfassen, Rotes zuerst (überfällig, Fehler, Testmonat-Wochen mit 🔴, ganz leere Tage).

## 30-Sekunden-Briefing (oben in LAGE.md und LAGE.html)
- **Heute online:** jeder Eintrag von heute mit Ampel – ✅ online · 🟢 läuft automatisch · 🟡 wartet auf go / wartet_* ·
  ✋ von Hand · 🔴 Fehler, Dateien fehlen oder **überfällig** (freigegeben, aber > 30 Min. über der Zeit nicht online →
  Posten-Lauf in Actions prüfen; erscheint dann auch rot unter „Braucht dich“, nach 6 h als „Verpasst“).
- **Letzte 7 Tage:** Reichweite der letzten 7 *abgeschlossenen* Tage (der laufende Tag zählt nicht, er ist unvollständig)
  mit Vergleich zur Vorwoche, Follower ± seit 7 Tagen (`automatik/statistik/konto.csv`), Follows/Entfolgungen der letzten
  30 Tage (API, `insights_*.json`).
- **Testmonat** (12.10.–08.11.) je KW: Feed-Beiträge *sicher* (online + geplant) gegen Soll 14, „wartet“ zählt nicht mit;
  Reel-Tage = Tage mit mindestens einem Reel (Soll: jeder Tag). 🔴 = unter 7 sicher.
- **Freie Slots nächste 7 Tage:** Raster Feed 11:45/17:45, Storys 12:15/17:50 (`RASTER` in `automatik/lage.py`); ein Slot
  ist belegt, wenn ein Eintrag gleicher Art genau zu dieser Uhrzeit steht (außer `entfaellt`/`pause`). Das ist die
  Arbeitsliste für die Content-Fabrik.

## Notlösung ohne Stimme (`ersatz_video`)
Ein Reel mit `wartet_auf_sprachnachricht` kann im Plan das Feld `"ersatz_video": "<datei>.mp4"` (im Post-Ordner) haben:
das fertige Notlösungs-Video **ohne Stimme**, falls die Sprachnachricht bis zur Frist nicht kommt. „Braucht dich“ zeigt dann
„🎞️ Ersatz ohne Stimme liegt bereit“ (oder ⚠️, wenn die Datei fehlt). `posten.py` nutzt das Feld nicht: Kommt bis zur
Frist keine Aufnahme, wird der Eintrag umgestellt (`video` = Ersatz, `stimme: false`, Status `entwurf` → Freigabe-Issue).

## Nach jeder Änderung
- Commit-Nachricht auf Deutsch und so, dass sie im Protokoll allein verständlich ist
  (z. B. „Plan: Reel Ampel auf Mo 17:45 verschoben (Feiertag)“). Das Protokoll zeigt nur Nachricht + Plan-Änderungen.
- Ändert sich, woran gerade gearbeitet wird oder wurde etwas entschieden: `automatik/lage_notizen.md` anpassen
  (kurze Stichpunkte, Veraltetes löschen). Das erscheint oben in LAGE.md unter „Gerade in Arbeit“.
- `python3 automatik/lage.py` ausführen und `LAGE.md` + `LAGE.html` mit committen. (Die Action macht es sonst ohnehin nach dem Push.)
- `LAGE.md`/`LAGE.html` nie von Hand bearbeiten – wird überschrieben. Fehlt dort etwas, `automatik/lage.py` erweitern.

## Status in plan.json (Bedeutung)
`entwurf` → Freigabe-Issue, „go“ → `freigegeben` → Autopilot postet → `veroeffentlicht` (mit Link).
`manuell` = Loris postet in der App · `wartet_*` = blockiert (z. B. Clips fehlen) · `fehler` = Posten fehlgeschlagen · `entfaellt` · `pause`.
