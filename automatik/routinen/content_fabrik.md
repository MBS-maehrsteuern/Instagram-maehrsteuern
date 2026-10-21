Content-Fabrik-Lauf (Mo/Mi/Fr 08:47 Berlin) für @maehrsteuern. Stand 14.10.2026. Repo MBS-maehrsteuern/Instagram-maehrsteuern, Zweig claude/instagram.

LAUF OHNE NUTZER – keine Rückfragen. „Heute“ = `TZ=Europe/Berlin date +%F` (der Container läuft in UTC; alle Zeiten im Plan sind deutsche Zeit).

ERLAUBNIS: Diese Routine darf und soll ohne Rückfrage Beiträge bauen, committen und auf claude/instagram pushen. Das ist ausdrücklich angefordert und kein „unangeforderter Commit“.

0. ZUGANG ZUERST (immer, auch wenn schon ein Klon da ist): add_repo(owner "maehrsteuern", repo "Instagram-maehrsteuern", access "push"). Dann im Klon: `git fetch origin claude/instagram && git checkout claude/instagram && git pull --rebase` und SOFORT `git push --dry-run origin HEAD:claude/instagram`.
   Schlägt add_repo oder der Dry-Run fehl: KEINE Arbeit beginnen, nur melden „⛔ Push nicht möglich: <Fehler wörtlich> – Repo in den Routine-Einstellungen als Quelle mit Schreibzugriff eintragen.“ Kein `git clone https://…` als Ersatz – von dort geht nie ein Push durch.
   Werkzeuge prüfen (ToolSearch, z. B. Google Drive): fehlt eins, den Schritt überspringen und am Ende unter „⚠️ Hinweise“ nennen.

1. Lesen: README.md, LAGE.md (vor allem „30-Sekunden-Briefing“: Testmonat je KW und „Freie Slots nächste 7 Tage“ = deine Arbeitsliste), strategie/15_plan_2_pro_tag.md (Testmonat, hat Vorrang), strategie/03_redaktionsplan.md, 06_auswertung.md, 08_hooks.md (inkl. Regel 7 und „Lernpunkte aus dem Wettbewerbs-Check“), 08_demo_reel_formel.md, 09_reel_regeln.md, 10_software_reel_konzept.md, 11_wissen_instagram.md, 18_wissen_2026-10-21.md (Hooks, 3:4, Karussell-Aufbau, nach dem Posten – hat Vorrang), 17_karussell_design.md (vor jedem Karussell, inkl. Baustein + Prüfliste), strategie/wettbewerb.md (neuester Monat), posts/sprechtexte.md, automatik/plan.json, neueste automatik/statistik/*.csv + insights_*.json, neuester automatik/berichte/tagesbericht_*.json. Zahlen von 2025 sind verzerrt – nur Werte ab 01.10.2026 als Maßstab.

2. Slots (exakt, bis So 08.11.): Feed NUR 11:45 und 17:45, Storys NUR 12:15 und 17:50. Keine anderen Uhrzeiten (19:30/19:35/12:45 sind abgeschafft). Ein Slot ist belegt, wenn am Datum ein Eintrag gleicher Art (Feed = Reel/Karussell/Bild, Story) genau zu dieser Uhrzeit mit Status ≠ entfaellt/pause steht.
   Fenster: von übermorgen bis heute +7 Tage, HÖCHSTENS 6 Feed-Beiträge pro Lauf (Storys zählen nicht). Vorrang: zuerst Tage ohne Feed-Beitrag, dann Tage ohne Reel (täglich ≥ 1 Reel), dann fehlende Teaser-Storys zu bestehenden Feed-Beiträgen. Welches Format in welchen Slot: Raster in strategie/15_plan_2_pro_tag.md (pro Woche ca. 10 Reels + 4 Karussells, Soll 14 Feed). Lieber ein Slot leer als ein schwacher Beitrag.

3. Inhalt:
   - HOOK-PRÜFUNG (18_wissen Abschnitt 1): Jeder Hook (Folie 1, Reel-Titel, Satz 1 im Sprechtext, Zeile 1 der Bildunterschrift) muss alle 5 Prüffragen mit Ja beantworten – sonst umschreiben. Im Plan-Hinweis „Hook 5/5“ notieren.
   - Format: Karussells und Einzelbilder 1080×1440 (3:4), Reels 9:16. Ab 21.10. sind alle Reels Stimm-Reels (Loris).
   - Pro Feed-Beitrag `erster_kommentar.txt` im Post-Ordner: eine Frage mit Suchbegriff (wird nach dem Posten automatisch kommentiert; Loris heftet an).
   - Reels 12–20 s, Pointe in den ersten 5 s, Hook-Text ab 0,3 s und ohne Ton verständlich, höchstens 3 Punkte, Sprechtext höchstens 35–40 Wörter (09_reel_regeln).
   - Stimm-Reels nur mit Sprachnachricht, sonst status `wartet_auf_sprachnachricht` mit Frist im Hinweis. Dazu gleich das Notlösungs-Video OHNE Stimme bauen (`reel_ohne_stimme.mp4` im Post-Ordner) und im Eintrag `"ersatz_video": "reel_ohne_stimme.mp4"` setzen – Status bleibt `wartet_auf_sprachnachricht`.
   - Ersetzen (Eintrag auf das Ersatz-Video umstellen: `video` = Ersatz, `stimme: false`, status `entwurf`) NUR, wenn die Frist vorbei ist UND Drive „Maehrsteuern audios“ lesbar ist UND dort keine Aufnahme liegt. Ohne Drive-Zugang nie ersetzen, nur melden.
   - Pro Feed-Beitrag im Plan `"stimme": true|false` und `"hook": "fall"|"zahl"`. Mindestens ein fall-Hook pro Lauf (08_hooks); jedes fall-Reel bekommt einen Teilen-Aufruf und eine prüfbare These/Zahl im Hook.
   - Karussells: Aufbau und Design nach strategie/17_karussell_design.md (Hook · Beispiel · Diagramm · praktisch · ein CTA, Kontrast, Sicherheitsrand, eingebundene Bilder). Letzte Folie „Speichern für später“ + Weiterleiten-Frage („Wer in deinem Team braucht das?“). Bibliothek-Karussells vorher fachlich gegenlesen (assets/bibliothek/PRUEFBERICHT.md).
   - Storys nur zum Tippen: Quiz, Umfrage, Ja/Nein, Emoji-Slider, Teaser. Keine offenen Fragesticker.
   - Steuerrecht fachlich korrekt, Rechtsstand prüfen, pruefzettel.md im Post-Ordner. Themen: 03_redaktionsplan.md, dann Themenspeicher, sonst selbst (Zielgruppe Steuerabteilungen/Kanzleien 25–54).
   - Im Plan-Hinweis je Beitrag kurz: „Wer schickt das an wen?“ + Suchbegriff + genutzter Hook-Lernpunkt.

4. Bildunterschrift (bildunterschrift.txt) – für jeden Feed-Beitrag:
   - Zeile 1 = Suchbegriff + Frage/Behauptung, z. B. „Gewerbesteuer-Hinzurechnung: Werden Mieten voll hinzugerechnet? 🤔“. Denselben Begriff auf Folie 1 / im Reel-Titel / im Gesprochenen. Suchbegriffe: Steuerrückstellung · Gewerbesteuer Hinzurechnung · latente Steuern · Körperschaftsteuer 2028 · Jahresabschluss · Steuerabteilung · Tax Compliance / Tax CMS · E-Rechnung 2027 · Verlustvortrag Mindestbesteuerung · Zinsschranke · Aufbewahrungsfristen · Steuererklärung Kapitalgesellschaft · Excel für Steuerberater · DATEV Excel · Steuerfachangestellte · Bilanzbuchhalter · Tax Technology.
   - Absatz 2 wörtlich: „💬 Kommentiere „TOOL“ (oder schreib's mir per DM) – ich schick dir die Demo mit Beispieldaten.“ Einziges Stichwort ist TOOL (automatik/interaktion.json) – kein neues erfinden.
   - Kommentar-Frage als Auswahl, nicht offen: „A oder B?“, „vor oder nach 2028?“, „1 bis 5?“ – mit einem Wort oder einer Zahl beantwortbar, ohne Vorwissen aus früheren Beiträgen.
   - Am Ende genau 4 Hashtags, je nach Zielgruppe ein Set:
     Steuerabteilung `#steuerabteilung #taxtech #jahresabschluss #[thema]` ·
     Kanzlei `#steuerberater #steuerkanzlei #steuerfachangestellte #[thema]` ·
     Excel/Tool `#steuern #excel #automatisierung #[thema]` ([thema] = ein Wort ohne Leerzeichen, z. B. #gewerbesteuer).

5. Bauen: Karussell per Job-Datei (vorlagen/system/jobs/, immer den ganzen Job rendern), Reel per Schnittliste + montage.py/reel.py (Atmo im Hook, Musik erst ab der Lösung, im Wechsel aus musik/). Ordner posts/<NN>_<datum>_<thema>/. Jedes Bild per Kontaktbogen prüfen, Reels per Standbildern (0,3 s, 1,5 s, Mitte, Ende), Lautheit ca. −18 LUFS (−70 = stumm).

6. plan.json: neue Einträge mit status "entwurf"; alle Teile eines Beitrags (auch Teaser-Storys) mit derselben Nummer NN vorn in der ID; Einrückung 2 Leerzeichen, nach "zeit" sortiert, jeder Slot nur einmal. Freigabe-Issues legt freigabe.yml je Beitrag an (kein Sammel-Issue bauen). LAGE.md/LAGE.html und Kalender schreibt die Lage-Action – nicht selbst committen. Bestehende Einträge anderer Sessions nicht überschreiben.

7. Commit (Regel Loris, 08.10.2026): Autor „Loris M. <mkwloris@googlemail.com>“ per --author; Committer bleibt die signierende Identität aus git config; deutsche Nachricht; am Ende die Co-Authored-By-Zeile für Claude. `git pull --rebase`, `git push origin claude/instagram`, kein PR. Push-Fehler wörtlich melden. Danach prüfen, ob freigabe.yml lief und die Issues da sind (`gh issue list --label freigabe` oder GitHub-MCP), sonst melden.

8. Kurz prüfen: Einträge mit status "fehler", Freigabe-Issues älter als 3 Tage, offene Punkte im Issue „🚨 Wächter“.

VERBOTE: nie posten, kommentieren, liken, folgen oder DMs senden; nie status "freigegeben" setzen; Einträge mit freigegeben/veroeffentlicht/manuell nicht ändern oder verschieben; kein force-push; Secrets nie ausgeben oder committen. Keine Arbeitgeber-Daten, -Namen oder -Orte; nur Demo-Zahlen; Repo ist öffentlich: keine Handles oder Namen von Kontakten.

SCHLUSS (immer, auch bei Abbruch), 3–8 Zeilen an Loris, erste Zeile:
„Status: ✅ fertig | ⚠️ teilweise | ⛔ abgebrochen – <Grund>“
Danach: was gebaut wurde (Termine), welcher Hook-Lernpunkt, Testmonat-Stand der KW (x/14), Link https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/issues?q=is%3Aopen+label%3Afreigabe, „⚠️ Hinweise“ (fehlende Werkzeuge, Probleme). Kurz, Deutsch, ohne Jargon.
