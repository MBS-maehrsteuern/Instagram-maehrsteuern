# Routinen einrichten – Einstellungen (Stand 14.10.2026)

Diese Datei ist **kein Prompt**. Die Prompts stehen vollständig und ohne Einrichtungs-Text in:
- `automatik/routinen/tagesbericht.md` – „Instagram Tagesbericht 9 Uhr“ (täglich 09:15 Berlin)
- `automatik/routinen/content_fabrik.md` – „Instagram Content-Fabrik“ (Mo/Mi/Fr 08:47 Berlin)

Ins Trigger-Prompt gehört **nur der Inhalt der jeweiligen Datei**, nicht dieser Text (sonst bekommt das Modell
Einrichtungsanweisungen statt einer Aufgabe – so entstanden die 20-Sekunden-Läufe bis 13.10.).
Alle Prompts haben denselben Kopf: Lauf ohne Nutzer, „heute“ in Berliner Zeit, zuerst `add_repo` (access "push") und
`git push --dry-run`, kein https-Clone als Ersatz, Verbote (keine Arbeitgeber-Daten/-Orte, nur Demo-Zahlen, keine
Kontaktnamen), Statuszeile „Status: ✅ | ⚠️ | ⛔ …“ am Ende. Slots: Feed 11:45/17:45, Storys 12:15/17:50.

## Einstellungen je Routine (claude.ai/code → Routinen) – macht Loris
- **Quelle/Repo:** `maehrsteuern/Instagram-maehrsteuern` mit Schreibzugriff eintragen.
- **Neue Sitzung je Lauf** statt fester Sitzung (in einer alten Sitzung greift `add_repo` nicht → Push 403).
- **Modell:** nur auf Loris' Wunsch ändern (Empfehlung der Analyse vom 13.10.: nicht Haiku).
- **Connectors** nur, wo nötig: Tagesbericht → Google Calendar; Content-Fabrik → Google Drive („Maehrsteuern audios“).
- **GitHub:** github.com → Settings → Applications → Claude → Repository access: `Instagram-maehrsteuern` freigeben.
  Das Repo heißt auf GitHub `Instagram-maehrsteuern` (großes I); `instagram-maehrsteuern` wird nur umgeleitet.

## Commit-Regel (alle Routinen, Loris 08.10.2026)
Autor „Loris M. <mkwloris@googlemail.com>“ per `--author`, Committer = signierende Identität aus git config,
Co-Authored-By-Zeile für Claude am Ende. Ältere Trigger-Prompts mit „kein Co-Authored-By, Committer Loris M.“ sind überholt.

Der Monatsbericht-Prompt liegt noch nicht im Repo (nur im Trigger).
