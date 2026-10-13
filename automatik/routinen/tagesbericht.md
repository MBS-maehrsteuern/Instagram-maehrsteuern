Täglicher Insights-Bericht für @maehrsteuern (Stand 14.10.2026, Lauf 09:15 Berlin). Loris will ihn jeden Morgen hier im Chat UND im Google Kalender – ausführlich, visuell (Bild mit Tabellen) und mit deiner direkten Einschätzung, ob unsere Methoden greifen.

LAUF OHNE NUTZER – keine Rückfragen. „Heute“ = `TZ=Europe/Berlin date +%F` (der Container läuft in UTC; alle Zeiten sind deutsche Zeit).

ERLAUBNIS: Diese Routine darf und soll ohne Rückfrage committen und auf den Zweig claude/instagram pushen (Bericht-Dateien, Erkenntnisse in strategie/06_auswertung.md). Das ist ausdrücklich angefordert und kein „unangeforderter Commit“.

0. ZUGANG ZUERST (immer, auch wenn schon ein Klon da ist): add_repo(owner "maehrsteuern", repo "Instagram-maehrsteuern", access "push"). Dann im Klon: `git fetch origin claude/instagram && git checkout claude/instagram && git pull --rebase` und SOFORT `git push --dry-run origin HEAD:claude/instagram`.
   Schlägt add_repo oder der Dry-Run fehl: KEINE Arbeit beginnen, nur melden „⛔ Push nicht möglich: <Fehler wörtlich> – Repo in den Routine-Einstellungen als Quelle mit Schreibzugriff eintragen.“ Kein `git clone https://…` als Ersatz – von dort geht nie ein Push durch.
   Werkzeuge prüfen (ToolSearch: Google Calendar, SendUserFile, GitHub-MCP) und Umgebung: `ls /opt/pw-browsers/chromium-*`, `which ffprobe node`. Fehlt etwas, den Schritt überspringen bzw. den Ersatzweg unten nehmen und am Ende unter „⚠️ Hinweise“ nennen.

1. Statistik von heute: statistik.yml läuft ca. 08:48 Berlin. Fehlt automatik/statistik/insights_<heute>.json: bis zu 5 Min. mit einer until-Schleife (alle 30 s `git pull`) auf den Commit „Statistik <heute>“ warten. Kommt er nicht: `gh workflow run statistik.yml --ref claude/instagram` (wenn gh angemeldet ist), sonst per GitHub-MCP (actions_run_trigger), und nochmals bis 5 Min. warten. Geht beides nicht: mit dem neuesten Stand arbeiten und das melden.

2. `python3 automatik/tagesbericht.py` → automatik/berichte/tagesbericht_<heute>.png/.html/.json. Bild 1620 px breit (Höhe wächst mit, nichts abschneiden). Abschnitte: Kacheln, Reichweite pro Tag, Beiträge (Reels mit Skip · Ø Sehdauer / Länge = Anteil gesehen, Skip-Verlauf mit Alter), Storys, Methoden-Check mit n, Testmonat (Format × Slot × Stimme × Hook), Soll-Ist („geplant, aber nicht erschienen“), Heute geplant. Methoden-Check nur für Beiträge ab 48 h; jüngere ⏳, nie ❌. PNG ansehen (Read): keine „–“ bei Länge und Stimme für Reels, nichts abgeschnitten.
   Fehlt Chromium: nur HTML + JSON erzeugen und den Link senden. Fehlt ffprobe: Längen aus dem Cache `automatik/statistik/laengen.json`, fehlende als „–“ lassen und melden. Das Skript nur bei echtem Fehler reparieren, nicht „verbessern“.

3. PNG in den Scratchpad kopieren und mit SendUserFile (display "render", status "proactive") senden. Fehlt SendUserFile: PNG-Link im Text.

4. Chat-Bericht (Deutsch, klar gegliedert):
   a) Tabelle Konto (Heute | Vortag | Δ) und alle Beiträge seit 29.09. mit Δ zum Vortag; bei Reels Skip (mit Alter), Ø Sehdauer, Anteil an der Länge.
   b) Greifen unsere Methoden? – jede Zeile mit Status, Ursache in 1–2 Sätzen, Datenlage (n; < 48 h = zu früh). Gruppen (Format, Slot mittags 11:45 / abends 17:45 – bis 13.10. waren es 12:15/19:30, Stimme, Hook fall/zahl) erst ab n ≥ 3. Geteilt > Erreicht ist ⚠️ markiert und zählt nicht in die Teilen-Quote.
   c) Soll-Ist: Steht etwas unter „geplant, aber nicht erschienen“, ganz oben mit 🚨 markieren.
   d) Was wir ändern – 1–3 Maßnahmen mit Bezug auf geplante Beiträge (ID/Datum). Nur vorschlagen. Maßstab für neue Beiträge: Reels 12–20 s, Pointe in den ersten 5 s; Bildunterschrift Zeile 1 = Suchbegriff, Absatz 2 „💬 Kommentiere „TOOL“ (oder schreib's mir per DM) – ich schick dir die Demo mit Beispieldaten.“, Auswahlfrage statt offener Frage, genau 4 Hashtags nach Set (Steuerabteilung `#steuerabteilung #taxtech #jahresabschluss #[thema]`, Kanzlei `#steuerberater #steuerkanzlei #steuerfachangestellte #[thema]`, Excel/Tool `#steuern #excel #automatisierung #[thema]`); Karussell-Schlussfolie Speichern + Weiterleiten-Frage; Storys nur zum Tippen.
   e) Heute geplant (Slots Feed 11:45/17:45, Storys 12:15/17:50), Einträge mit status "fehler", offene Freigabe-Issues, was Loris heute tun muss (inkl. Reels mit `wartet_auf_sprachnachricht` und Frist; liegt ein `ersatz_video` bereit, das nennen).
   Zahlen von 2025 nicht als Maßstab nehmen.

5. Google Kalender (create_event, Primärkalender): heute 09:00–09:10 Europe/Berlin, availability FREE, useDefaultReminders false. Titel „📈 Instagram-Tagesbericht: <Follower> Follower (<±Δ>) · <wichtigste Zahl>“. Beschreibung HTML (Konto, Beiträge, Methoden-Check, Soll-Ist, Was wir ändern, Heute geplant) + Link https://github.com/maehrsteuern/Instagram-maehrsteuern/blob/claude/instagram/automatik/berichte/tagesbericht_<heute>.png . Fehlen die Kalender-Tools (auch per ToolSearch): unter „⚠️ Hinweise“ „Kalendereintrag fehlt: Google-Calendar-Connector ist in dieser Routine nicht eingebunden“.

6. Nur automatik/berichte/*, automatik/statistik/laengen.json und strategie/06_auswertung.md committen – nie plan.json, nie LAGE.md/LAGE.html (macht die Lage-Action). Neue Erkenntnisse knapp in 06_auswertung.md. Commit (Regel Loris, 08.10.2026): Autor „Loris M. <mkwloris@googlemail.com>“ per --author; Committer bleibt die signierende Identität aus git config; deutsche Nachricht; am Ende die Co-Authored-By-Zeile für Claude. `git pull --rebase`, `git push origin claude/instagram`. Push-Fehler wörtlich nennen.

VERBOTE: nie posten, kommentieren, liken, folgen oder DMs senden; nie status "freigegeben" setzen; Einträge im Plan nicht ändern; kein force-push; Secrets nie ausgeben. Keine Arbeitgeber-Daten, -Namen oder -Orte; nur Demo-Zahlen; Repo und Kalender-Text ohne Handles oder Namen von Kontakten.

SCHLUSS (immer, auch bei Abbruch) – erste Zeile des Chat-Berichts:
„Status: ✅ fertig | ⚠️ teilweise | ⛔ abgebrochen – <Grund>“
Dann der Bericht aus Schritt 4 und am Ende „⚠️ Hinweise“ (fehlende Werkzeuge, Wartezeiten, Push-Fehler).
