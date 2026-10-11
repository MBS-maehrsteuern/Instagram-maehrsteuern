Täglicher Insights-Bericht für @maehrsteuern (Stand 11.10.2026, Lauf 09:15 Berlin). Loris will ihn jeden Morgen hier im Chat UND im Google Kalender – ausführlich, visuell (Bild mit Tabellen) und mit deiner direkten Einschätzung, ob unsere Methoden greifen.

ERLAUBNIS: Diese Routine darf und soll ohne Rückfrage committen und auf den Zweig claude/instagram pushen (Bericht-Dateien, Skript-Reparaturen, Erkenntnisse in strategie/06_auswertung.md). Das ist ausdrücklich angefordert und kein „unangeforderter Commit“.

0. Zugang: add_repo mit owner maehrsteuern, repo Instagram-maehrsteuern, access "push". Fehlt das add_repo-Tool (auch per ToolSearch nicht zu finden): als erste Zeile des Berichts „⚠️ add_repo fehlt – Repo bitte in den Routine-Einstellungen als Quelle eintragen“ und trotzdem weiterarbeiten: vorhandenen Klon nutzen, sonst `git clone https://github.com/maehrsteuern/Instagram-maehrsteuern` (großes I). Zweig claude/instagram, git pull --rebase.

1. Statistik von heute: Der Workflow statistik.yml läuft ca. 08:48 Berlin. Fehlt automatik/statistik/insights_<heute>.json, bis zu 5 Minuten mit einer until-Schleife (alle 30 s git pull) auf den Commit „Statistik <heute>“ warten. Kommt er nicht: Workflow per GitHub-MCP starten (actions_run_trigger, workflow statistik.yml, ref claude/instagram) und nochmals bis 5 Min. warten; ohne GitHub-MCP im Bericht melden und mit dem neuesten Stand arbeiten.

2. `python3 automatik/tagesbericht.py` → automatik/berichte/tagesbericht_<heute>.png/.html/.json. Bild 1620 px breit (Höhe wächst mit, nichts abschneiden). Abschnitte: Kacheln, Reichweite pro Tag, Beiträge (Reels mit Skip · Ø Sehdauer / Länge = Anteil gesehen, Skip-Verlauf mit Alter), Storys, Methoden-Check mit n, Testmonat (Format × Slot × Stimme × Hook), Soll-Ist („geplant, aber nicht erschienen“), Heute geplant. Methoden-Check nur für Beiträge ab 48 h; jüngere ⏳, nie ❌. PNG ansehen (Read): keine „–“ bei Länge und Stimme für Reels, nichts abgeschnitten. Bei Fehlern das Skript reparieren.

3. PNG in den Scratchpad kopieren und mit SendUserFile (display "render", status "proactive") senden.

4. Chat-Bericht (Deutsch, klar gegliedert):
   a) Tabelle Konto (Heute | Vortag | Δ) und alle Beiträge seit 29.09. mit Δ zum Vortag; bei Reels Skip (mit Alter), Ø Sehdauer, Anteil an der Länge.
   b) Greifen unsere Methoden? – jede Zeile mit Status, Ursache in 1–2 Sätzen, Datenlage (n; < 48 h = zu früh). Gruppen (Format, Slot 12:15/19:30, Stimme, Hook fall/zahl) erst ab n ≥ 3. Geteilt > Erreicht ist ⚠️ markiert und zählt nicht in die Teilen-Quote.
   c) Soll-Ist: Steht etwas unter „geplant, aber nicht erschienen“, ganz oben mit 🚨 markieren.
   d) Was wir ändern – 1–3 Maßnahmen mit Bezug auf geplante Beiträge (ID/Datum). Nur vorschlagen; Beiträge mit Status freigegeben/veroeffentlicht nie stillschweigend ändern.
   e) Heute geplant, Einträge mit status "fehler", offene Freigabe-Issues, was Loris heute tun muss.
   Zahlen von 2025 nicht als Maßstab nehmen.

5. Google Kalender (create_event, Primärkalender): heute 09:00–09:10 Europe/Berlin, availability FREE, useDefaultReminders false. Titel „📈 Instagram-Tagesbericht: <Follower> Follower (<±Δ>) · <wichtigste Zahl>“. Beschreibung HTML (Konto, Beiträge, Methoden-Check, Soll-Ist, Was wir ändern, Heute geplant) + Link https://github.com/maehrsteuern/Instagram-maehrsteuern/blob/claude/instagram/automatik/berichte/tagesbericht_<heute>.png . Keine Kontaktnamen. Fehlen die Kalender-Tools (auch per ToolSearch): erste Zeile „⚠️ Kalendereintrag fehlt: Google-Calendar-Connector ist in dieser Routine nicht eingebunden“.

6. automatik/berichte/* (und ggf. automatik/statistik/laengen.json) committen; neue Erkenntnisse knapp in strategie/06_auswertung.md. Commit-Regel (Loris, 08.10.2026): Autor „Loris M. <mkwloris@googlemail.com>“ per --author; Committer bleibt die signierende Identität aus git config (Claude <noreply@anthropic.com>); deutsche Nachricht; am Ende „Co-Authored-By: Claude <noreply@anthropic.com>“. Dann git pull --rebase und git push -u origin claude/instagram. Push-Fehler wörtlich nennen.

Regeln: Nur Demo-Zahlen, Arbeitgeber nie nennen, keine Kontaktnamen im öffentlichen Repo.
