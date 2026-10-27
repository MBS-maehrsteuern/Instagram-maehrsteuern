# 🧭 Lage – maehrsteuern auf Instagram

_Automatisch erzeugt von `automatik/lage.py` – nicht von Hand bearbeiten (Notizen: `automatik/lage_notizen.md`). Stand: letzte Änderung Mo 26.10. 09:26 Uhr._

## ⏱️ 30-Sekunden-Briefing

- **Heute online:** 🟡 11:45 🖼️ Karussell `37-karussell-bp-vorbereitung` (pausiert) · 🟡 12:15 📱 Story `37-story-tipp` (pausiert) · 🟡 17:45 🎬 Reel `38-reel-pruefpfad` (pausiert) · 🟡 17:50 📱 Story `38-story-teaser` (pausiert)
- **Braucht dich:** nichts 🎉
- **Letzte 7 Tage:** Reichweite **2149** (20.10.–26.10., +51 % zur Vorwoche) · Follower **+7** (jetzt 368) · 30 Tage: +34 Follows / −11 entfolgt
- **Testmonat** (Tag 16/28, Soll 14 Feed/Woche, täglich ≥ 1 Reel):
  - 🔴 **KW 44** (26.10.–01.11.) ← jetzt: Feed **0/14** (0 online · 0 geplant) · Reel-Tage (sicher) **0/7**
  - 🔴 **KW 45** (02.11.–08.11.): Feed **0/14** (0 online · 0 geplant) · Reel-Tage (sicher) **0/7**
- **Freie Slots nächste 7 Tage** (3):
  - Do 29.10.: Feed 17:45
  - Sa 31.10.: Feed 11:45 · Story 12:15

## 📝 Gerade in Arbeit

- **Stand 21.10. abends (Sitzung mit Loris):**
  - **Online heute:** Reel 42 AfA (manuell ~16:35, Stimme) und Reel 58 Vorsteuer (Autopilot 18:10, Stimme, Link im Plan). Nach 1 h AfA: 80 Aufrufe, Ø 16 s, 30 % geteilt, 18 % bis zum Ende → `strategie/06_auswertung.md`.
  - **Alle anderen Beiträge ab 21.10. sind `pausiert`** (Loris 21.10.; alter Status in `status_vorher`). Grund: Umbau aller Reels auf Loris' Stimme + neues Wissen. Wieder freigeben nur nach Loris' Ansage.
  - **Neues Wissen verbindlich:** `strategie/18_wissen_2026-10-21.md` – großartige Hooks (5-Fragen-Check), Hook ab Frame 1 (Meta Hook Rate = 3 s), Titelbild aus dem Hook, Karussells 1080×1440 (11 kommende neu gerendert), Ablauf nach dem Posten, Meta-Kennzahlen nur als Trend.
  - **Reels jetzt Fachbeiträge 25–30 s** mit Stimme (`09_reel_regeln`). Aufnahme 21.10.: `aufnahmen/2026-10-21/` – 20 Stimmen geschnitten (`geschnitten/stimme_NN.wav`, nur in echten Pausen). Gebaut: 42, 58 (`vorlagen/system/schnitt/p42_…`, `p58_reel_stimme_bauen.py` als Vorlage).
  - **Offen:** übrige 18 Reels nach Muster 58 bauen (Hook ab Frame 1 + Zoom, Titelbild aus Hook) → Loris sichtet → freigeben. 47 Betriebsaufspaltung: Loris nimmt neu auf (Günther-Einstieg raus). 55: Schlussfrage zusätzlich einblenden. 17-reel-kommentare: Thema offen. Titelfolien der Karussells noch mit alten Hooks.
  - **Wissen 22.10. (Abschnitt 6):** Story = eigene Umfrage statt Repost; 48-h-Pause nach Ausreißer (≥ 5× Aufrufe); Hashtags auf ≤ 3; Loris zur Postzeit online. „Von Hand statt planen“ unbelegt → optional A/B-Test.
  - **Autopilot:** Erster Kommentar wird jetzt automatisch gesetzt (`erster_kommentar.txt`, `posten.py`). GitHub-Takt startet Läufe teils ~5–10 Min. später → Puffer einplanen. GWG 11:45 ging nicht raus (Ursache unbekannt, Actions-Protokoll prüfen).
- **Instagram-Regeln Okt. 2026 (20.10., Google-KI-Antwort, ungeprüft):** Zusammenfassung in `strategie/11_wissen_instagram.md` (Saves/Shares, Originalität, 3–5 Hashtags + **Alt-Text**, 3:4-Format). Widerspruch zu „erste Stunde zählt“ → im Testmonat prüfen, Postzeiten nicht ändern. Format 1440 jetzt von zwei Quellen genannt, Randwerte uneinheitlich → `17_karussell_design.md` Abschnitt 2.
- **Karussell-Design (20.10.):** Neue Regeln aus Loris' Screenshots (@fizzaandalgorithm) in `strategie/17_karussell_design.md` – Z-Muster, Kontrast mit Messwerten unserer Marke (Nebentext `#8FA398` nur 4,7 am hellen Verlaufsende), 10-Folien-Raster, Prüfliste und Baustein; Content-Fabrik liest sie über `11_wissen_instagram.md` und `automatik/routinen/content_fabrik.md`. **Offen (Loris):** Format 1080×1440 (3:4) statt 1080×1350 – Angabe der Quelle nicht gegengeprüft, Vorlage bleibt vorerst 1350. Routine-Prompt in den Routine-Einstellungen ggf. um `17_karussell_design.md` in der Leseliste ergänzen.
- **Nachtlauf 14.10. (Loris: „Optimierungen suchen, einbauen, freigeben“)** – Bericht `strategie/16_optimierung_2026-10-14.md`. Kurz: Plan 14.10.–01.11. fast lückenlos (~40 neue Beiträge/Storys aus der gegengelesenen Bibliothek, ohne Stimme, freigegeben, 2× unabhängig geprüft), anstehende Beiträge überarbeitet (Suchbegriff in Zeile 1, „Kommentiere TOOL“, Auswahlfrage, 4 Hashtags), Fachfehler korrigiert (Rückstellung Folie 5, E-Rechnung-Text, Zinsschranke-EBITDA), Ortsangabe im Ampel-Reel überdeckt. Autopilot ohne Doppel-Post-Risiko, Takt-Wächter, Statistik ohne Doppelläufe, Zeitzonen-Fix vor 25.10., Lage mit 30-Sekunden-Briefing. Notlösung 18–22 liegt als `ersatz_video` bereit, Umstellung Do 15.10. 12:05 (geplanter Check). **Braucht Loris:** KI-Label Ampel (Sa) + Mein Weg (Fr) in der App, Bio/Pins/Highlights (`02_bio_highlights.md`), Routine-Prompts übernehmen, ManyChat (TOOL-Kommentare!).
- Neustart läuft: Start-Storys + Vorfreude (30.09.) und Neuvorstellung (Do 01.10. 18:30, von Hand) sind online. Nach 2 h: 26 erreicht, 6× geteilt, 0 neue Follower. Angepinnt ✓ (03.10.). Offen von Hand: Highlight „Start 👋“.
- Wochenrhythmus ab Okt. steht im Prompt der Content-Fabrik (Mo + Do 08:47, max. 4 Beiträge pro Lauf): Di/Do Karussell + Teaser, Mi Begleit-Reel, Fr Wissens-Reel oder Stimm-Reel, So Reel + Teaser, täglich 12:15 Story.
- Content-Fabrik nutzt ab Mo 05.10. die Lernpunkte aus `strategie/wettbewerb.md` (über Abschnitt in `08_hooks.md`): pro Lauf ≥ 1 Hook „konkreter Fall“ oder „Prüfer/Finanzamt“, Lernpunkt im Freigabe-Issue vermerkt. Routine-Prompt selbst unverändert (nur aus ihrer eigenen Sitzung änderbar).
- **So 04.10. umgebaut:** Statt Ampel-Reel geht 19:30 das Community-Reel „5 Sachen, die ich aus Excel rausgeschmissen hab“ online (Loris' Sprachnachricht, 41 s, keine Werbung, CTA: Zahl 1–5 in die Kommentare) + neue Teaser-Story 19:35. Ampel-Reel und alter Teaser stehen auf `pause` – kann später wieder eingeplant werden. Die Kommentar-Antworten (welche Nummer?) sind die Themen für die nächsten Reels.
- **Doppel-Post 04.10. behoben:** Das 5-Dinge-Reel ging zweimal raus (DeFLK53ALSs = im Plan, DeFLSBNFUXy = Duplikat, von Loris am 04.10. gelöscht ✓). Ursache: Ein Lauf startet mit dem Stand vom Startzeitpunkt und hat den Plan nur nach dem Warten neu geladen. `posten.py` holt jetzt direkt vor jedem Posten den neuesten Plan; klappt das nicht, wird nicht gepostet (nächster Lauf holt nach).
- **Di 06.10. 19:30 Reel „Nummer 1: Der Monatsbericht“ (Version 3)** freigegeben (go von Loris im Chat, 06.10.): dritte Aufnahme, Atmer raus, Pausen mit Raumton, 30 s. Karussell Excel-Fehler Mi 07.10., LinkedIn #18 Do 08.10., Split-Reel So 11.10.
- **Testmonat ab Mo 12.10. (bis So 08.11.): 2 Feed-Beiträge pro Tag, **ab 14.10. 11:45 + 17:45, Storys 12:15/17:50** (kurz vor der Follower-Welle 18–21 Uhr laut Insights; vorher 12:15/19:30), täglich ≥ 1 Reel** – Raster und Konflikte in `strategie/15_plan_2_pro_tag.md`. Reels **12–15 s** (13–16 am 11.10. gekürzt, Langfassung reel_lang.mp4). Autopilot postet Reels (bestätigt: KSt-Reel Sa 19:30). Sprechtexte 18–22 (≤ 15 s) warten auf Aufnahme bis Mi 14.10. (Slots Mo 19. – Do 22.10. + Mo 26.10. 17:45); **ohne Aufnahme bis Do 15.10. 12:00 → Reels ohne Stimme** (go 13.10.). **13.10. (go):** Ampel-Reel Sa 17.10. 11:45 (Slot-Test Stimme mittags, Teaser 12:15), Steuersatz-Reel auf Mo 26.10. (KW 44); So 18.10. + Sa 17.10. abends frei für die Fabrik. Mein Weg Fr 16.10.: KI-Label nach dem Posten in der App setzen. Offene Vorschläge zu freigegebenen Beiträgen: `strategie/13_backlog.md` (Umsetzung 11.10.).
- **Stumme Reels behoben (06.10.):** `montage.py` erzeugte bei bestimmten Tonspuren (Atmo/Musik ohne Stimme) eine Tonspur mit kaputten Zeitstempeln → im MP4 stumm. Betroffen: Split-Reel und KSt-Staffel-Reel – beide neu gerendert (−18,5 / −19,7 LUFS). Fix: `asetpts=N/SR/TB` nach `amix` + jede Spur auf volle Länge. Ab jetzt nach jedem Render Lautheit prüfen (sollte ca. −18 LUFS sein, −70 = stumm).
- **Edits-Test (06.10.):** Split-Reel Do 08.10. 19:30 baut Loris selbst in Edits und plant es dort (Status `manuell`, Paket in `posts/02_2026-10-06_excel_fehler/edits_paket/`, Anleitung als Google Doc im Drive). Grund: laut Mosseri (Aug. 2025) kleiner Reichweiten-Bonus für Edits-Reels, nur bei echtem Schnitt in Edits, „nicht für immer“ – aktueller Stand unbelegt, daher Test über 2–3 Reels gegen Autopilot-Reels. Woche dafür verschoben: latente Steuern Fr 09.10., KSt-Reel + „Heute 19:30“-Story Sa 10.10., Rückblick-Story So 11.10.
- Bis 10.10. alles freigegeben: 5-Dinge-Reel (So 04.10.), Excel-Fehler (Di 06.10.), Split-Reel als Begleit-Reel (Mi 07.10., vorgezogen), latente Steuern (Do 08.10.), Wissens-Reel KSt-Staffel (Fr 09.10.). So 11.10. ist frei → Fabrik am Mo 05.10.
- Latente Steuern: Prüfzettel Punkte 1–5 am 05.10. mit Quellen geprüft ✓ – Box Folie 6 präzisiert (kleine KapGes: von § 274 befreit, passive Latenzen ggf. als Rückstellung), fachlich nichts mehr offen (`pruefzettel.md` im Post-Ordner; „Abschluss 2026“ am 05.10. überall auf „spätestens jetzt“ geändert – Folien 1+7, Bildunterschrift, Teaser, LinkedIn-Text + PDF). Änderungen bis Mi 07.10. abends.
- Reel „Mein Weg“: Loris hat Variante B am 08.10. eingesprochen → fertig, Fr 16.10. 17:45 (Autopilot). **15.10.: Karte „Das bin ich heute“ neu** als gerahmter Headshot wie Karte 2 (Loris’ aktuelles Foto, Markenhintergrund, KI-hochskaliert + Augen angeglichen), Hook „Mein Weg. / Rückwärts.“ über den Rahmen gesetzt, Szene 1 ohne Zoom, `reel.mp4` neu gerendert (12,8 s, −18,1 LUFS), KI-Hinweis in der Bildunterschrift ergänzt. **KI-Label beim Posten einschalten** (Karte 2 + 3 KI), Hinweis steht in der Bildunterschrift. Variante-A-Dateien als `*_variante_a.*` im Ordner.
- DM-Strecke läuft über **ManyChat** (Kommentar/Story-Antwort/DM mit Tool/TOOL/tool/tol → DM mit Demo-Link, Follow-up nach 23 h). Stichwörter nur in `automatik/interaktion.json` pflegen – Abweichungen meldet LAGE.md. Die eigenen Skripte schicken nie DMs.
- Interaktion läuft (Radar 50 Konten, Kommentar-Hilfe, LinkedIn-Pakete). **Sprint 1 (03.10.):** Wächter-Issue, Stichwort-Abgleich, Radar-Pflege montags, Erste-Stunde-Checkliste. **Kalender-Sync live (03.10.):** Termine gehen direkt in den Google-Kalender „maehrsteuern Autopilot“ (nur Postzeiten „beschäftigt“ für Reclaim, To-dos/LinkedIn „frei“; Farben + Pop-ups je Art). In Reclaim verbunden ✓, Freigabe nur Dienstkonto (nicht öffentlich, nicht im Hauptkalender) ✓ (Chrome 05.10.). `kalender.ics` entfällt. **Wochenbericht** ab So 04.10. ca. 18:00 als Issue – Demos/ManyChat per Kommentar nachtragen. Demo-Zahlen (entschieden 03.10.): Reclaim-Pflichtfeld „Woher kennst du mich?“ → Apps-Script „maehrsteuern Demo-Kopie“ kopiert Buchungen stündlich ohne Namen nach „maehrsteuern Autopilot“ → Wochenbericht zählt sie; UTM/Webhooks scheiden aus (Starter), `dm_tracking.csv` nicht mehr im Bericht. **Chrome 05.10.:** Pflichtfeld (Dropdown, Pflicht) ✓, Reclaim-Vorlagen weg ✓ (zweiter Link „Demo + Intro Call“ für @maehrtax bleibt, wird nicht gezählt), Apps-Script = GitHub-Stand, 1 Trigger stündlich :40, 0 % Fehler ✓. **Offen:** Testbuchung (loris_jm@gmx.de, Herkunft Instagram → Kopie prüfen → absagen) + Beschreibungsausschnitt an Claude; Puffer: global 10 Min. nach jedem Meeting (gilt auch für @maehrtax, entschieden 05.10.) – setzt Chrome zusammen mit der Testbuchung. ManyChat-Zahlen bleiben von Hand (API nur Pro) – siehe `strategie/13_backlog.md`.
- **Automatik gehärtet (03.10., mit #23 in `claude/instagram`):** kein Doppel-Post bei Push-Konflikt, „stop“ greift auch während des Wartens, kein Schlüssel in Fehlermeldungen, keine verlorenen „go“-Antworten, Schlüssel-Verlängerung mit Reserve-Takt – Details `strategie/13_backlog.md`.
- Externer Takt fürs Posten fiel am 15.10. ab ca. 05:00 aus (Repo-Umzug zu `MBS-maehrsteuern`, alter Schlüssel ohne Zugriff, cron-job.org hat den Job deaktiviert). Neuer Schlüssel `cron-posten` (Org `MBS-maehrsteuern`) nötig, Ablaufdatum beim Anlegen hier eintragen.
- Tax-Calc-Repo: PR #2 (Delta-Plakette beim Tippen) und PR #3 (Reel-Datensatz `?demo=reel`) warten auf Review.
- **Chrome-Claude-Module** (`strategie/14_chrome_module.md`): Erinnerungen im Kalender „maehrsteuern Autopilot“ – So 04.10. 11:00 einmalig A·2·3, jeden So 18:45 Modul 1 (ManyChat → Wochenbericht), 1. Mo im Monat 18:00 Module 4+6, LinkedIn-Upload (Modul 5) automatisch je Karussell am Werktag danach 08:00.
- **Wochenbericht KW 40 ist da ([#29](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/issues/29), So 18:01, Reserve-Lauf 21:26 hat dasselbe Issue nur aktualisiert):** Zahlen geprüft (575 Aufrufe = Zuwachs der 2 neuen Beiträge, Radar 2 Kommentare aus #22, Kalender verbunden – 0 Demos). **Offen: ManyChat-Zeile fehlt** (Chrome Modul 1 lief nicht) → im Issue `manychat x/y` + Zeile `Gesamtstand ManyChat: gesendet X / Klicks Y` kommentieren. Behoben (05.10.): Sonntags-Reels (19:30, nach dem Bericht) zählen jetzt im Bericht der Folgewoche als neu – „neu“ = gepostet So–Sa.
- **Radar-Nachträge (03.10.):** Meta-Drosselung (429/Code 4, 17, 32, 613) → Backoff 30/90/270 s, bei anhaltender Drosselung wird abgebrochen. Gedrosselte oder kurz gestörte Konten landen nicht mehr als 🧹 „nicht abrufbar“ in der Pflege; aufgeräumt werden nur dauerhaft kaputte Konten oder Konten ohne Beitrag seit 30 Tagen (montags, nur abgehakt). Art neuer Konten wird auch aus Wörtern wie „Steuerberaterin“, „Prüfung“, „Akademie“ erkannt; fehlende oder unbekannte Art erscheint als Hinweis im Radar-Issue.
- **Fristen** (`automatik/erinnerungen.json` → „Braucht dich“ + Kalender): LinkedIn #18 Mi 07.10. 08:00 (Termin kommt schon automatisch) · Reel-Vergleich „5 Dinge“/Split → Anzeigen-Start ca. Mo 12.10. (Chrome Modul 2 am 04.10. nur vorbereiten) · **ManyChat-Trial endet Fr 16.10.** → Entscheidung Loris (Erinnerung Mi 14.10.).
- **Meta-App „maehrsteuern Autopilot“** bleibt im Entwicklungsmodus. Die laufenden IG-Schlüssel und die Statistik sind davon nicht betroffen (eigenes Konto mit App-Rolle). Nur die Hashtag-Suche braucht die Freigabe → Checkliste [#26](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/issues/26).
- **Reclaim-Hinweis:** Claudes Reclaim-Zugang (Connector) zeigt auf **Konto B (Outlook, Lite)**, nicht auf das Demo-Konto. Für die Automatik nicht nutzen; Demo-Buchungen kommen nur über das Apps-Script „maehrsteuern Demo-Kopie“.
- **Bibliothek aus dem Brand Kit (Claude Design) gebaut (02.10.):** 365 fertige Bilder in `assets/bibliothek/` (Übersicht `README.md` dort), Texte als Job-Dateien in `vorlagen/system/jobs/bibliothek/`. Neue Vorlagen `zahl.html` + `banner.html`, Highlight-Symbole, Vergleichstabelle/Checkliste im Karussell. Nichts davon ist eingeplant. **Gegengelesen (05.10.):** 10 Fehler korrigiert, 25 Zweifelsfälle mit Loris entschieden und umgesetzt → `assets/bibliothek/PRUEFBERICHT.md`. Offen nur: Zinsschranke-Caption mit Hinweis auf Untergang des Zinsvortrags. **Erste Bibliothek-Beiträge eingeplant (05.10., als Entwurf → Freigabe-Issue):** Rückstellung in 6 Schritten Do 15.10. (Quiz SolZ Mi 14.10., Auflösung Do 15.10. 12:15, Teaser 19:35) · E-Rechnung-Fahrplan Do 22.10. (Umfrage Mi 21.10., Teaser 19:35). Content-Fabrik: diese Slots sind belegt. **Runde 4 ergänzt (05.10.):** +217 Bilder (jetzt 582) – GmbH/Gesellschafter, Bilanz, USt, Lohn, ErbSt/GrESt, Paragraf als Formel, Steuerkalender, GoBD, Mythos/Glossar Teil 2, Einzelposts, Storys, Reel-Titel, Einblendungen, Highlights, Ampeln (`r4_*.json`), nichts eingeplant. 6 Korrekturen vor dem Rendern, 4 Zweifelsfälle + Platzhalter „312 Testfälle“ / § 8c-Quoten 48/62 % offen → Prüfbericht Abschnitt „Runde 4“. **Runde 7 (07.10.):** 14 MBS-Reel-Bilder (10 Titel `reels/mbs_*`, 4 Einblendungen `bausteine/mbs_*`, Abspann „Demo buchen“), `einblendung.html` kann jetzt `chip`/`kicker` im Abspann. **Runden 5+6 (07.10.):** +400 Bilder (jetzt 996) – Kleinunternehmer, Firmenwagen, Gebäude-AfA, USt-Sätze, Minijob/Reisekosten 2026, Grundwerte 2026, Kapitalerträge, Vermietung, AO-Fristen, OSS u. a. 10 Korrekturen, 32 Umbenennungen gegen Überschreiben, Zweifelsfälle → Prüfbericht „Runden 5 und 6“.
- **Lage als Seite (04.10.):** `LAGE.html` mit Kacheln, Kalender, Diagrammen und filterbarem Protokoll, wird mit LAGE.md neu geschrieben und über GitHub Pages veröffentlicht (https://maehrsteuern.github.io/Instagram-maehrsteuern/). Pages eingeschaltet ✓ (04.10.), Seite läuft und aktualisiert sich bei jeder neuen Lage automatisch.
- **Nach jedem Post, innerhalb von 30 Min. (von Hand in der App, Quelle `strategie/18_wissen_2026-10-21.md` Abschnitt 4):** den automatischen ersten Kommentar **anheften** · eigenen Beitrag **liken und speichern** · in der **Story teilen** · **Kommentare unter dem vorigen Beitrag liken** · **jeden Kommentar beantworten**. Den Kommentar setzt `posten.py` selbst, wenn `posts/<ordner>/erster_kommentar.txt` existiert (Feed-Beiträge, nicht Storys; ID als `erster_kommentar_id` im Plan; Fehler = nur Warnung).

## 👉 Braucht dich

- Nichts offen. 🎉

## ⏭️ Nächste 7 Tage

| Wann | Was | Status | Hinweis |
|---|---|---|---|
| Di 27.10. 11:45 | 🖼️ Karussell `37-karussell-bp-vorbereitung` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), karussell/bp_vorbereitung Folien 1–5 unverändert; Folie 6 neu: „Speichern bis zur nächsten Prüfungsanordnung“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p37_bp_vorbereitung.json). Geprüft: §§ 196, 197 AO, § 147 Abs. 6 AO, GoBD, § 200 AO; Bildunterschrift ergänzt um 4/2 Wochen Vorlauf (§ 5 Abs. 4 BpO). Alt-Texte in alt_texte.json. Begleit-Reel 38 am Abend. |
| Di 27.10. 12:15 | 📱 Story `37-story-tipp` | pausiert | 14.10. Nachtlauf: aus Bibliothek Tipp-Story neu (statt frage_pruefung = offene Frage): „Prüfungsanordnung zuerst lesen“, Verlegung des Beginns auf Antrag aus wichtigem Grund (§ 197 Abs. 2 AO), Emoji-Reaktion 👏/😮 (jobs/p37_bp_vorbereitung.json). |
| Di 27.10. 17:45 | 🎬 Reel `38-reel-pruefpfad` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R1/R2 gegengelesen), Begleit-Reel zu Karussell 37, ohne Stimme 13,7 s, −18,0 LUFS, Atmo Uhr im Hook, Musik 09 Lofi-Piano ab der Lösung. Als Betriebsprüfungs-Thema gerahmt („Woher kommt diese Zahl?“, GoBD-Nachvollziehbarkeit), nicht als #BEZUG/Excel-Fehler. Titelbild „Betriebsprüfung – Jede Zahl bis zur Quelle“ und Abspann „Kommentiere TOOL“ neu (jobs/p38_reel_pruefpfad.json); bausteine/haken_pruefpfad, leiste_pruefpfad, haken_ueber_pruefpfad auf Folien 3/4 von bp_vorbereitung (schnitt/p36_40_karten_bauen.py), Schnitt schnitt/p38_reel_pruefpfad.json. |
| Di 27.10. 17:50 | 📱 Story `38-story-teaser` | pausiert | 14.10. Nachtlauf: aus Bibliothek Teaser „Jetzt neu im Profil“ zum Prüfpfad-Reel (Titelbild), jobs/p38_reel_pruefpfad.json. |
| Mi 28.10. 11:45 | 🎬 Reel `39-reel-holding` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R4 gegengelesen), Reel ohne Stimme 13,8 s, −18,0 LUFS, Musik 07 Minimal Tech. Veräußerungsgewinn GmbH an GmbH: 1 Mio. € × 5 % nbBA (§ 8b Abs. 2, 3 KStG) × 29,825 % (Hebesatz 400 %) = 14.913 € = 1,49 % – nachgerechnet. Karten aus karussell/holding Folien 2+3 (schnitt/p36_40_karten_bauen.py); Titelbild „1 Mio. € Gewinn. 1,5 % Steuer.“, Karte „Dividenden erst ab 10 % (§ 8b Abs. 4 KStG)“ und Abspann TOOL neu (jobs/p39_reel_holding.json). Bildunterschrift: Dividenden § 8b Abs. 1/5, 10-%-Grenze Abs. 4, GewSt-Schachtel 15 % (§ 9 Nr. 2a GewStG), Verluste nicht abziehbar (Abs. 3 Satz 3), Ausnahmen Abs. 7/8. Abgrenzung zum Karussell par8b (Dividenden, 01.11.). |
| Mi 28.10. 12:15 | 📱 Story `39-story-quiz` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R4 gegengelesen): quiz_holding als Emoji-Tipp neu gerendert (👏 = rund 1,5 % · 😮 = rund 30 %, richtig: 👏), statt „Antworte in Prozent“; Auflösung im Bild: „Die Antwort steht im neuen Reel“ (Reel 39 lief um 11:45). Keine Auflösungs-Story: Do 29.10. 12:15/17:50 sind von Agent c2 belegt (story_do_tipp Mythen, story_do_teaser AfA). Optional in der App Quiz-Sticker setzen. |
| Mi 28.10. 17:45 | 🎬 Reel `40-reel-formeln` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R2 gegengelesen, $C$12-Satz korrigiert), Reel ohne Stimme 13,7 s, −18,0 LUFS, Atmo Tippen + Fehlerton im Hook, Musik 12 Pop Electronic. Fall „=WENNFEHLER(…; 0): Fehler weg, Steuer auch“ + 2 Lösungen (XVERWEIS statt Festwert, Namen statt $C$12) = 3 Punkte; MAX/ABRUNDEN bewusst weggelassen (stehen schon im Paragraf-Formel-Reel 24.10.). Karten aus karussell/excel_formeln Folien 6, 2, 5 (schnitt/p36_40_karten_bauen.py), Titelbild + Abspann TOOL neu (jobs/p40_reel_formeln.json), Schnitt schnitt/p40_reel_formeln.json. Raster Mi A verlangt Stimme → Abweichung (ohne Aufnahme). |
| Mi 28.10. 17:50 | 📱 Story `40-story-teaser` | pausiert | 14.10. Nachtlauf: aus Bibliothek Teaser „Jetzt neu im Profil“ zum Formel-Reel (Titelbild), jobs/p40_reel_formeln.json. |
| Do 29.10. 11:45 | 🖼️ Karussell `41-karussell-mythen` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), karussell/mythen Folien 1–7 (nicht mythen_3), Folie 8 neu: Speichern + Weiterleiten + TOOL statt offener Kommentarfrage (jobs/p41_mythen.json). Ablaufhemmung § 147 Abs. 3 Satz 5 AO in der Bildunterschrift. alt_texte.json. |
| Do 29.10. 12:15 | 📱 Story `41-story-tipp` | pausiert | 14.10. Nachtlauf: Emoji-Tipp „Gewerbesteuer ist keine Betriebsausgabe“ (§ 4 Abs. 5b EStG) mit Verweis auf das Karussell, 👏/😮, ohne Auflösung nötig (jobs/p41_mythen.json). storys/frage_mythen nicht genutzt (offene Frage). |
| Do 29.10. 17:50 | 📱 Story `42-story-teaser` | pausiert | 14.10. Nachtlauf: Teaser „Jetzt neu im Profil“ zum AfA-Reel (Titelbild), jobs/p42_reel_afa.json. Bibliotheks-Teaser teaser_afa nicht genutzt („zurück“, Dashboard-Zahlen im Bild). |
| Fr 30.10. 11:45 | 🎬 Reel `43-reel-par35` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R5 gegengelesen, „tatsächlich zu zahlende“ GewSt korrigiert), Reel ohne Stimme 14,4 s, −18,1 LUFS (Peak −4,1 dBFS), Musik 06 Lofi ruhig. Titelbild reels/reel_35, Karten aus karussell/par35 Folien 3–5 (schnitt/p41_44_karten_bauen.py), Abspann „Kommentiere TOOL“ neu (jobs/p43_reel_par35.json), Schnitt schnitt/p43_reel_par35.json. Nachgerechnet: 100.000 − 24.500 = 75.500 × 3,5 % = 2.642,50 €; × 400 % = 10.570 € = 4,0 × 2.642,50; bei 450 % 11.891,25 € → 1.321,25 € Rest. Ermäßigungshöchstbetrag und „nur natürliche Personen/Mitunternehmer“ in der Bildunterschrift. |
| Fr 30.10. 12:15 | 📱 Story `43-story-tipp` | pausiert | 14.10. Nachtlauf: Emoji-Tipp „4,0 × Messbetrag“ (§ 35 EStG, Einzel-/Mitunternehmer, höchstens tatsächlich zu zahlende GewSt), 👏/😮 (jobs/p43_reel_par35.json). Statt zdt_35 („angerechnet“, ohne Tipp-Format). |
| Fr 30.10. 17:45 | 🖼️ Karussell `44-karussell-glossar` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen, Einlagekonto und Messbetrag-Box korrigiert), karussell/glossar_1 Folien 1–6, Folie 7 neu: Speichern + Weiterleiten + TOOL statt offener Kommentarfrage (jobs/p44_glossar.json). jahresabschluss_7 nicht genutzt: nur 4 Folien, nur Punkt 01 ausgeführt, Rest doppelt mit KSt-Staffel/Hebesatz/Hinzurechnung/latente Steuern/Rückstellung. Freibetrag/Abrundung und § 8c-Ausnahmen in der Bildunterschrift. alt_texte.json. |
| Fr 30.10. 17:50 | 📱 Story `44-story-teaser` | pausiert | 14.10. Nachtlauf: Teaser „Jetzt neu im Profil“ zum Glossar-Karussell (Folie 1), jobs/p44_glossar.json. |
| Sa 31.10. 17:45 | 🎬 Reel `45-reel-vga` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R2 gegengelesen), Reel ohne Stimme 13,4 s, −18,0 LUFS, Atmo Uhr + Fehlerton im Hook, Musik 06 Lofi ruhig. Titelbild neu als Prüfer-Fall „Darlehen, 0 % Zinsen? vGA.“, Karten aus karussell/vga Folie 2 und Folie 3 mit 3 statt 5 Punkten neu gerendert (Reel-Regel; Folie 04 mit verwaistem „nr 01“ nicht genutzt), Klassiker 4+5 und Rückwirkungsverbot in der Bildunterschrift. jobs/p45_reel_vga.json, Karten schnitt/p45_47_karten_bauen.py, Schnitt schnitt/p45_reel_vga.json. |
| Sa 31.10. 17:50 | 📱 Story `45-story-teaser` | pausiert | 14.10. Nachtlauf: Teaser „Jetzt neu im Profil“ zum vGA-Reel (Titelbild), jobs/p45_reel_vga.json. |
| So 01.11. 11:45 | 🖼️ Karussell `46-karussell-dividenden-8b` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), karussell/par8b Folien 1–5 unverändert; Folie 6 neu: „Speichern für später“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p46_dividenden_8b.json). Bildunterschrift nennt laut Prüfbericht 10-%-Grenze (§ 8b Abs. 4 KStG, Beginn des Kalenderjahres) und 5 % nbBA (§ 8b Abs. 5 KStG); GewSt-Schachtel § 9 Nr. 2a GewStG ab 15 % zu Beginn des EZ, sonst § 8 Nr. 5 GewStG. Nachgerechnet: 5.000 × 15,825 % = 791 €, × 14 % = 700 €, Summe 1.491 €. Alt-Texte in alt_texte.json. Abgrenzung zum Kürzungen-Karussell (18.10.): dort nur Schachtel-Zeile. |
| So 01.11. 12:15 | 📱 Story `46-story-zdt` | pausiert | 14.10. Nachtlauf: Tipp-Story Zahl des Tages storys/zdt_8b (R3 gegengelesen, „ab 10 % Beteiligung“ bereits korrigiert) zum § 8b-Karussell. |
| So 01.11. 17:45 | 🎬 Reel `47-reel-betriebsaufspaltung` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R4 gegengelesen), Reel ohne Stimme 15,0 s, −18,0 LUFS, Atmo Uhr + Fehlerton im Hook, Musik 09 Lofi Piano. Titelbild neu als Fall „Halle an die eigene GmbH. Gewerblich.“, 3 Punkte = karussell/betriebsaufspaltung Folien 2–4 (sachliche + personelle Verflechtung, Folge), Betriebsaufgabe-Risiko in der Bildunterschrift. jobs/p47_reel_betriebsaufspaltung.json, Karten schnitt/p45_47_karten_bauen.py, Schnitt schnitt/p47_reel_betriebsaufspaltung.json. |
| So 01.11. 17:50 | 📱 Story `47-story-teaser` | pausiert | 14.10. Nachtlauf: Teaser „Jetzt neu im Profil“ zum Betriebsaufspaltungs-Reel (Titelbild), jobs/p47_reel_betriebsaufspaltung.json. |
| Mo 02.11. 11:45 | 🎬 Reel `48-reel-firmenwagen` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R5 gegengelesen), Reel ohne Stimme 15,0 s, −17,9 LUFS, Atmo Uhr + Fehlerton im Hook, Musik 10 Spannung. Titelbild neu als Prüfer-Fall „Fahrtenbuch in Excel. Verworfen.“, 3 Punkte = karussell/firmenwagen Folien 5, 2, 3 (Fahrtenbuch zeitnah/geschlossen, 1 %, 0,03 %). Demo 50.000 € BLP, 20 km → 800 €/Monat nachgerechnet; E-Auto 0,25 % bis 100.000 € (Anschaffung ab 1.7.2025) in der Bildunterschrift. jobs/p48_reel_firmenwagen.json, Karten schnitt/p48_50_karten_bauen.py, Schnitt schnitt/p48_reel_firmenwagen.json. |
| Mo 02.11. 12:15 | 📱 Story `48-story-tipp` | pausiert | 14.10. Nachtlauf: Emoji-Tipp-Story „Fahrtenbuch: zeitnah und geschlossen“ (nach storys/tipp_fahrtenbuch, R5) zum Firmenwagen-Reel, jobs/p48_reel_firmenwagen.json. |
| Mo 02.11. 17:45 | 🎬 Reel `49-reel-kleinunternehmer` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R5 gegengelesen), CTA-Reel KW 45 (TOOL-Aufruf im Abspann, eigener TOOL-Absatz in der Bildunterschrift: Grenz-Monitor 100.000 €). Reel ohne Stimme 15,4 s, −18,2 LUFS, Musik 12 Pop Electronic, Abspann zusätzlich groß „Kommentiere „TOOL““. Titelbild neu „100.000 € und raus.“, Karten: Grenz-Folien neu gerendert mit Normbox „§ 19 Abs. 1 UStG“ (ohne Satzangabe – Satzzählung der Neufassung 2025 nicht sicher belegt) + karussell/kleinunternehmer Folie 4. Neugründer-Regel und Verzicht 5 Jahre (§ 19 Abs. 3 UStG) in der Bildunterschrift. jobs/p49_reel_kleinunternehmer.json, Karten schnitt/p48_50_karten_bauen.py, Schnitt schnitt/p49_reel_kleinunternehmer.json. |
| Mo 02.11. 17:50 | 📱 Story `49-story-teaser` | pausiert | 14.10. Nachtlauf: Teaser „Jetzt neu im Profil“ zum Kleinunternehmer-CTA-Reel (Titelbild), jobs/p49_reel_kleinunternehmer.json. |

## 🗓️ Danach

| Wann | Was | Status | Hinweis |
|---|---|---|---|
| Di 03.11. 11:45 | 🎬 Reel `50-reel-gebaeude-afa` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R5 gegengelesen), Reel ohne Stimme 15,0 s, −18,0 LUFS, Musik 08 Chill House. Titelbild = reels/reel_gebaeude (unverändert), 3 Punkte = karussell/gebaeude_afa Folien 3–5 (linear § 7 Abs. 4, degressiv 5 % § 7 Abs. 5a, Sonder-AfA § 7b EStG). Demo 400.000 € → 12.000 € / 20.000 € / 19.000 € nachgerechnet. Grund und Boden + Voraussetzungen Betriebsgebäude in der Bildunterschrift. jobs/p50_reel_gebaeude_afa.json, Karten schnitt/p48_50_karten_bauen.py, Schnitt schnitt/p50_reel_gebaeude_afa.json. |
| Di 03.11. 12:15 | 📱 Story `50-story-tipp` | pausiert | 14.10. Nachtlauf: Emoji-Tipp-Story „5 % degressiv für Wohnungsneubau“ (§ 7 Abs. 5a EStG) zum Gebäude-AfA-Reel, jobs/p50_reel_gebaeude_afa.json. |
| Di 03.11. 17:45 | 🖼️ Karussell `51-karussell-kapitalertraege` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R6 gegengelesen), karussell/kapitalertraege Folien 1–6 unverändert; Folie 7 neu: „Speichern für die Steuererklärung“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p51_kapitalertraege.json). Nachgerechnet: (3.000 − 1.000) × 26,375 % = 527,50 €. Alt-Texte in alt_texte.json. KW 45 ungerade → Karussell abends. |
| Di 03.11. 17:50 | 📱 Story `51-story-teaser` | pausiert | 14.10. Nachtlauf: Teaser „Jetzt neu im Profil“ zum Kapitalerträge-Karussell (Ausschnitt Folie 1, bausteine/teaser_bild.png), jobs/p51_kapitalertraege.json. |
| Mi 04.11. 11:45 | 🎬 Reel `52-reel-gobd` | pausiert | 14.10. Nachtlauf (d2): aus Bibliothek (R4 gegengelesen, karussell/gobd), Reel ohne Stimme 14,0 s, −17,9 LUFS (Peak −3,5 dBFS), Atmo Uhr + Fehlerton im Hook, Musik 11 Future Garage ab 2,4 s. Titelbild neu als Prüfer-Fall „Der Prüfer öffnet deine Excel.“, Karten aus gobd Folien 5/4/6 (3 Punkte: unveränderbar, zeitgerecht, dokumentiert; schnitt/p52_55_karten_bauen.py), Abspann „Kommentiere TOOL“ (jobs/p52_reel_gobd.json), Schnitt schnitt/p52_reel_gobd.json. Geprüft: § 145 Abs. 1, § 146 Abs. 1 und 4, § 147 Abs. 6 AO, 10-Tage-Richtwert GoBD für unbare Vorgänge. |
| Mi 04.11. 12:15 | 📱 Story `52-story-tipp` | pausiert | 14.10. Nachtlauf (d2): Emoji-Tipp „Unbare Vorgänge: als Richtwert 10 Tage“ (GoBD, zeitgerechte Erfassung) mit Verweis aufs Reel, 👏/😮 (jobs/p52_reel_gobd.json). |
| Mi 04.11. 17:45 | 🎬 Reel `53-reel-iab` | pausiert | 14.10. Nachtlauf (d2): aus Bibliothek (R6 gegengelesen, karussell/iab_2), Begleit-Reel zum Karussell 53 am Do 17:45, ohne Stimme 14,0 s, −18,0 LUFS (Peak −5,6 dBFS), Musik 08 Chill House. Titelbild „Heute abziehen. Später kaufen.“, Karten aus iab_2 Folien 2/3, Einblendung „Nicht investiert? Rückwirkend weg.“ (§ 7g Abs. 3 EStG, § 233a AO) und Abspann TOOL neu (jobs/p53_iab.json), Schnitt schnitt/p53_reel_iab.json. Geprüft: § 7g Abs. 1 (50 %, Gewinngrenze 200.000 €, Höchstbetrag 200.000 €), Abs. 2 (Hinzurechnung/Kürzung im Kaufjahr), Abs. 3; Demo 60.000 € → 30.000 €. |
| Mi 04.11. 17:50 | 📱 Story `53-story-teaser` | pausiert | 14.10. Nachtlauf (d2): Teaser „Jetzt neu im Profil“ zum IAB-Reel (Titelbild), jobs/p53_iab.json. storys/tipp_iab nicht genutzt (keine Emoji-Reaktion). |
| Do 05.11. 11:45 | 🎬 Reel `54-reel-reverse-charge` | pausiert | 14.10. Nachtlauf (d2): aus Bibliothek (R4 gegengelesen, karussell/reverse_charge), Reel ohne Stimme 14,2 s, −18,0 LUFS (Peak −4,4 dBFS), Atmo Uhr + Fehlerton im Hook, Musik 09 Lofi-Piano ab 2,4 s. Titelbild neu als Prüfer-Fall „Mit USt bezahlt. Vorsteuer: 0 €.“, Einblendung Demo-Fall Bau (100.000 € + 19.000 € USt), Karten aus reverse_charge Folien 5/4 (schnitt/p52_55_karten_bauen.py), Abspann TOOL (jobs/p54_reel_reverse_charge.json), Schnitt schnitt/p54_reel_reverse_charge.json. Geprüft: § 13b Abs. 2 Nr. 4 und Abs. 5 UStG, § 14c Abs. 1, § 15 Abs. 1 Satz 1 Nr. 1 und Nr. 4, § 14a Abs. 5 UStG; Bildunterschrift erklärt Saldo (13b-Schuld = Vorsteuer) und Rückforderung über berichtigte Rechnung. Nähe zu d3 (Vorsteuer, So 08.11.) beachtet: hier nur § 13b-Fall. |
| Do 05.11. 12:15 | 📱 Story `54-story-tipp` | pausiert | 14.10. Nachtlauf (d2): Emoji-Tipp Pflichthinweis „Steuerschuldnerschaft des Leistungsempfängers“ (§ 14a Abs. 5 UStG) mit Verweis aufs Reel, 👏/😮 (jobs/p54_reel_reverse_charge.json). storys/frage_rc nicht genutzt (STICKER-Platzhalter). |
| Do 05.11. 17:45 | 🖼️ Karussell `53-karussell-iab` | pausiert | 14.10. Nachtlauf (d2): aus Bibliothek (R6 gegengelesen), karussell/iab_2 Folien 1–6 unverändert; Folie 7 neu: „Speichern für die Investitionsplanung“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p53_iab.json). Begleit-Reel 53 am Vorabend. Alt-Texte in alt_texte.json. Geprüft: § 7g Abs. 1–6 EStG (50 %, 200.000 €/200.000 €, 3 Jahre, 40 % Sonder-AfA, 90 % betrieblich). |
| Do 05.11. 17:50 | 📱 Story `53-story-teaser-karussell` | pausiert | 14.10. Nachtlauf (d2): Teaser „Jetzt neu im Profil“ zum IAB-Karussell (Folie 1), jobs/p53_iab.json. |
| Fr 06.11. 11:45 | 🎬 Reel `55-reel-thesaurierung` | pausiert | 14.10. Nachtlauf (d2): aus Bibliothek (R4 gegengelesen, karussell/thesaurierung), Reel ohne Stimme 14,0 s, −18,0 LUFS (Peak −4,2 dBFS), Musik 12 Pop Electronic. Titelbild neu „28,25 % statt bis 45 %.“, Karten aus thesaurierung Folien 2/3/4 (Folie 5 Option § 1a KStG bewusst nicht genutzt, Antragsfrist nicht nachgeprüft), Abspann TOOL (jobs/p55_reel_thesaurierung.json), Schnitt schnitt/p55_reel_thesaurierung.json. Geprüft: § 34a Abs. 1 (28,25 % zzgl. SolZ, Antrag, Bilanzierer) und Abs. 4 (25 % Nachversteuerung); Bildunterschrift: Gesamtbelastung bei baldiger Entnahme oft höher. |
| Fr 06.11. 12:15 | 📱 Story `55-story-tipp` | pausiert | 14.10. Nachtlauf (d2): Emoji-Tipp „28,25 % auf Gewinn, der im Betrieb bleibt“ (§ 34a EStG, zzgl. SolZ, 25 % Nachversteuerung), 👏/😮 (jobs/p55_reel_thesaurierung.json). |
| Fr 06.11. 17:45 | 🖼️ Karussell `56-karussell-verjaehrung` | pausiert | 14.10. Nachtlauf (d2): aus Bibliothek (R6 gegengelesen, keine offenen Punkte), karussell/verjaehrung Folien 1–5 unverändert; Folie 6 neu: „Speichern für die nächste Prüfungsanordnung“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p56_verjaehrung.json). Alt-Texte in alt_texte.json. Geprüft: § 169 Abs. 2 Satz 1 Nr. 2 und Satz 2, § 170 Abs. 2 Satz 1 Nr. 1, § 171 AO; Demo Erklärung für 2022, Abgabe 2024 → Ende 31.12.2028. |
| Fr 06.11. 17:50 | 📱 Story `56-story-teaser` | pausiert | 14.10. Nachtlauf (d2): Teaser „Jetzt neu im Profil“ zum Verjährungs-Karussell (Folie 1), jobs/p56_verjaehrung.json. |
| Sa 07.11. 17:45 | 🎬 Reel `57-reel-verlust-8c` | pausiert | 14.10. Nachtlauf (d3): aus Bibliothek (R4 gegengelesen), Reel ohne Stimme 13,6 s, −17,8 LUFS, Atmo Uhr + Fehlerton im Hook, Musik 10 Spannung. Titelbild neu als Zahl-Hook „51 % verkauft? Verluste weg.“, Karten aus karussell/par8c Folie 2 (Regel) und 3 (Rettungsanker), ampel_8c_* (Demo-Quoten) bewusst nicht genutzt. Bildunterschrift: § 8c Abs. 1 Satz 1/4/5–8, Abs. 1a, § 8d KStG, § 10a Satz 10 GewStG, Zinsvortrag § 8a Abs. 1 Satz 3 KStG. Sa 11:45 bleibt frei (Stimm-Slot). jobs/p57_reel_verlust_8c.json, Karten schnitt/p57_58_karten_bauen.py, Schnitt schnitt/p57_reel_verlust_8c.json. |
| Sa 07.11. 17:50 | 📱 Story `57-story-teaser` | pausiert | 14.10. Nachtlauf (d3): Teaser „Jetzt neu im Profil“ zum § 8c-Reel (Titelbild), jobs/p57_reel_verlust_8c.json; Karte verkleinert (bausteine/teaser_karte.png, schnitt/p57_58_karten_bauen.py), damit nichts angeschnitten wird. |
| So 08.11. 12:15 | 📱 Story `58-story-tipp` | pausiert | 14.10. Nachtlauf (d3): Tipp-Story mit Emoji-Reaktion „Bis 250 € brutto reicht eine Kleinbetragsrechnung (§ 33 UStDV)“ zum Vorsteuer-Reel, jobs/p58_reel_vorsteuer.json. |
| So 08.11. 17:45 | 🖼️ Karussell `59-karussell-pensionen` | pausiert | 14.10. Nachtlauf (d3): aus Bibliothek (R4 gegengelesen, keine offenen Punkte), karussell/pension Folien 1–5 unverändert; Folie 6 neu: „Speichern für die Gutachten-Saison“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p59_pensionen.json). Letzter Testmonat-Tag: Bildunterschrift mit Community-Auswahl „Welches Thema als Nächstes: A) Teilwertabschreibung oder B) Rechnungsabgrenzung?“. Fachlich: § 6a Abs. 1, Abs. 3 Satz 3 EStG (6 %), § 253 Abs. 2 und 6 HGB (10-Jahres-Durchschnitt, Ausschüttungssperre), § 274 HGB (Wahlrecht Aktivüberhang). Alt-Texte in alt_texte.json. |
| So 08.11. 17:50 | 📱 Story `59-story-teaser` | pausiert | 14.10. Nachtlauf (d3): Teaser „Jetzt neu im Profil“ zum Pensions-Karussell (Folie 1), jobs/p59_pensionen.json; Karte verkleinert (bausteine/teaser_karte.png, schnitt/p57_58_karten_bauen.py), damit nichts angeschnitten wird. |

## ✅ Zuletzt veröffentlicht (Autopilot)

- Mi 21.10. 18:00 · 🎬 Reel `58-reel-vorsteuer` · [ansehen](https://www.instagram.com/reel/Dewza8JCASO/) (online 2026-10-21 18:10)
- Mi 21.10. 16:35 · 🎬 Reel `42-reel-afa` (online 2026-10-21 16:35)
- Di 20.10. 17:50 · 📱 Story `28-story-aufloesung` · [ansehen](https://www.instagram.com/stories/maehrsteuern/4012196501812014820) (online 2026-10-20 17:50)
- Di 20.10. 17:45 · 🎬 Reel `19-reel-verlustvortrag` · [ansehen](https://www.instagram.com/reel/DeuJJHoDXkl/) (online 2026-10-20 17:45)
- Di 20.10. 12:15 · 📱 Story `29-story-teaser` · [ansehen](https://www.instagram.com/stories/maehrsteuern/4012035073688455220) (online 2026-10-20 12:24)
- Di 20.10. 11:45 · 🖼️ Karussell `29-karussell-verluste` · [ansehen](https://www.instagram.com/p/DetnHd6G82Y/) (online 2026-10-20 12:24)
- Mo 19.10. 17:45 · 🎬 Reel `18-reel-aufbewahrung` · [ansehen](https://www.instagram.com/reel/DeryoWUE_Or/) (online 2026-10-19 19:26)
- Mo 19.10. 12:15 · 📱 Story `28-story-quiz` · [ansehen](https://www.instagram.com/stories/maehrsteuern/4011324194198123089) (online 2026-10-19 12:52)
- Mo 19.10. 11:45 · 🎬 Reel `28-reel-zuschlaege` · [ansehen](https://www.instagram.com/reel/DerFcnnnTMT/) (online 2026-10-19 12:52)
- So 18.10. 17:50 · 📱 Story `27-story-teaser` · [ansehen](https://www.instagram.com/stories/maehrsteuern/4010746920150907932) (online 2026-10-18 17:50)

## 📈 Zahlen (täglich ca. 08:45)

**368 Follower** · 25 Beiträge im Profil (Abruf 2026-10-20) · **+0** seit 2026-10-19
Reichweite pro Tag: 24.10. **201** · 25.10. **584** · 26.10. **347** · 27.10. **1**

| Story (letzte 24 h) | Aufrufe | Erreicht | Antworten | Profilbesuche | Follows |
|---|---|---|---|---|---|
| Mo 26.10. 18:09 | 29 | 18 | 0 | 0 | 0 |

| Beitrag (letzte 14 Tage) | Aufrufe | Erreicht | Likes | Komm. | Gespeichert | Geteilt |
|---|---|---|---|---|---|---|
| Mo 26.10. 17:45 [Die Rente deiner Oma kann steuerpflichti](https://www.instagram.com/reel/De9tD9vj4EH/) | 190 | 142 | 8 | 5 | 7 | 9 |
| So 25.10. 17:45 [Ein einziger Euro entscheidet: 799 € net](https://www.instagram.com/reel/De7JF3cAGrX/) | 849 (+192) | 766 | 11 | 1 | 10 | 68 |
| Sa 24.10. 11:17 [Ohne Anlass auf dem Bewirtungsbeleg: 0 %](https://www.instagram.com/reel/De3yheAFKBg/) | 260 (+9) | 212 | 4 | 1 | 2 | 0 |
| Do 22.10. 15:45 [Finanzamt: Du denkst, es weiß nur, was i](https://www.instagram.com/reel/DezHdgPt1_0/) | 894 (+12) | 749 | 13 | 10 | 12 | 60 |
| Mi 21.10. 18:10 [Vorsteuerabzug: Rechnung bezahlt, Leistu](https://www.instagram.com/reel/Dewza8JCASO/) | 168 (+6) | 140 | 4 | 1 | 2 | 0 |
| Mi 21.10. 15:43 [Degressive AfA 2026: Du kaufst im Dezemb](https://www.instagram.com/reel/DewieoRNf5g/) | 168 (+3) | 119 | 10 | 4 | 7 | 14 |
| Di 20.10. 17:45 [Verlustvortrag 2026: 3 Mio. € Verlust – ](https://www.instagram.com/reel/DeuJJHoDXkl/) | 134 (+3) | 87 | 3 | 0 | 0 | 0 |
| Di 20.10. 12:24 [Verlustvortrag 2026: Gilt die Mindestbes](https://www.instagram.com/p/DetnHd6G82Y/) | 128 (+2) | 43 | 2 | 0 | 1 | 0 |
| So 18.10. 13:39 [Kürzungen Gewerbesteuer nach § 9 GewStG:](https://www.instagram.com/p/DeomJhQG4o8/) | 195 (+3) | 80 | 4 | 0 | 5 | 0 |
| Fr 16.10. 19:57 [Diplom-Finanzwirt mit KI-Avatar? Das war](https://www.instagram.com/reel/DekHzHkF7E2/) | 185 (+2) | 116 | 16 | 0 | 4 | 0 |
| Do 15.10. 21:15 [Zwei Listen abgleichen in Excel: SVERWEI](https://www.instagram.com/reel/DehnTbyEZ2g/) | 279 (+1) | 232 | 7 | 0 | 5 | 0 |
| Do 15.10. 18:25 [Steuererklärung 2022 nachholen – nur noc](https://www.instagram.com/reel/DehYZkyD-sL/) | 286 (+1) | 182 | 11 | 0 | 5 | 0 |
| Do 15.10. 11:45 [Steuerrückstellung berechnen – kommst du](https://www.instagram.com/p/DegoIVKluPa/) | 176 (+3) | 84 | 1 | 0 | 1 | 0 |
| Mi 14.10. 17:45 [Gewerbesteuer-Hinzurechnung ohne Excel? ](https://www.instagram.com/reel/DeemwStk5mL/) | 258 (+1) | 205 | 7 | 0 | 3 | 0 |
| Di 13.10. 19:30 [Eine Rechnungsnummer doppelt. Der Prüfer](https://www.instagram.com/reel/DecWVZwgpOC/) | 304 (+1) | 235 | 6 | 2 | 5 | 1 |
| Di 13.10. 12:16 [Werden Mieten voll hinzugerechnet? 🤔](https://www.instagram.com/p/Debkp_3m1WY/) | 161 (+3) | 70 | 4 | 0 | 2 | 0 |

Rohdaten: `automatik/statistik/`, Auswertung: `strategie/06_auswertung.md`

## ⚙️ Automatik

| Ablauf | Wann | Letzter Lauf |
|---|---|---|
| Lage + Google-Kalender | alle 15 Min. (LAGE.md, Kalender-Sync, Wächter) | – |
| Posten | alle 15 Min. (postet freigegebene Einträge) | – |
| Freigabe | bei neuen Entwürfen / Antwort im Issue | – |
| Statistik | täglich ca. 08:45 | – |
| Schlüssel verlängern | am 1. des Monats ca. 06:27 | – |
| Radar + LinkedIn | täglich ca. 07:00 (Issue mit Arbeitsliste) | – |
| Kommentare | nach jedem Posten-Takt (Vorschläge ins Issue) | – |
| Wochenbericht | sonntags ca. 18:00 (ein Issue) | – |
| Musik holen | nur von Hand | – |

## 📜 Protokoll – jede Änderung

🤖 Autopilot · ✅ Freigabe · 📈 Statistik · 🎵 Musik · 🔀 Merge · ✍️ von Hand / Claude

**Mo 26.10.2026**
- 09:26 ✍️ Tagesbericht 26. Oktober: 376 Follower, 584 Reichweite ([`b0d22f3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b0d22f3928c0e0c8c819bddedc8dd02068c8eb60))
  - `LAGE.html`, `automatik/berichte`, `automatik/statistik`

**So 25.10.2026**
- 09:26 ✍️ Basis-Daten für Tagesbericht 25. Oktober ([`7cf6b83`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7cf6b83947bb71186d8b4dea6b5e25a0cf5900c5))
  - `automatik/berichte`
- 09:26 ✍️ Tagesbericht 25. Oktober: 374 Follower, 201 Reichweite ([`a0a8d7c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a0a8d7cb9b36b0df2088cf6bc037ba65f9bf81b1))
  - `automatik/berichte`, `automatik/statistik`

**Sa 24.10.2026**
- 10:31 🔀 Merge remote changes into local branch ([`f6e3a95`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f6e3a95631b3da26d886dd9b8ec0f73e9c787e7d))
- 10:31 ✍️ Tagesberichte 21.–24. Oktober: Berichte als interaktive Artifacts veröffentlicht ([`5fa6971`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5fa69713efdb9e09bfc465fff9a91d8303f73edd))
  - `automatik/berichte`
- 09:15 📈 Statistik 2026-10-24 ([`0b46019`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0b46019484dc3aa186b6b29fce3232fe35d9e7a1))
  - `automatik/statistik`
- 09:14 📡 Radar 2026-10-24: 8 Beiträge, 0 DM-Entwürfe ([`b3e08cd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b3e08cdec554f5e2996078aca2d99b76bce63286))
  - `automatik/interaktion`

**Fr 23.10.2026**
- 09:18 ✍️ LAGE aktualisiert: Zeitstempel und Protokoll auf Änderungen vom 20.10. synchronisiert ([`84eda02`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/84eda022c29de98683916b4b6cccfbb4b6b52df8))
  - `LAGE.html`
- 09:27 📡 Radar 2026-10-23: 8 Beiträge, 0 DM-Entwürfe ([`ef3db1a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ef3db1ad9587cd7df5b292e285d00d8888acf4d9))
  - `automatik/interaktion`
- 09:22 📈 Statistik 2026-10-23 ([`9e117e4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9e117e4cfff38e4fb0352d6ced16d06aeba65fce))
  - `automatik/statistik`
- 09:18 ✍️ LAGE aktualisiert: Zeitstempel und Protokoll auf Änderungen vom 20.10. synchronisiert ([`5566708`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/556670807f12b3283077b9cf5e1384b8093334a5))
  - `LAGE.html`

**Do 22.10.2026**
- 14:29 📈 Statistik 2026-10-22 ([`c74205e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c74205e5dde717a3640ca91decd1d3459219f140))
  - `automatik/statistik`
- 11:50 ✍️ Reel 62: Loris postet von Hand – aus dem Autopiloten genommen ([`7573cda`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7573cda15e15e73bcc21e3e30943869f7ba82558))
  - Plan: `62-reel-glaesern` status: freigegeben → manuell; `62-reel-glaesern` zeit: 2026-10-22 17:45 → 2026-10-22 11:50
- 11:45 ✍️ Reel 62 „Das Finanzamt weiß es schon“ mit Stimme, heute 17:45 ([`c28b879`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c28b87953f97d961207dbfb4cf5b9f71a00b40ab))
  - Plan: neu `62-reel-glaesern` (2026-10-22 17:45, freigegeben)
- 08:43 📡 Radar 2026-10-22: 8 Beiträge, 0 DM-Entwürfe ([`99f651e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/99f651e0434bc7b43c40927bc127aefb52c2c68b))
  - `automatik/interaktion`
- 06:08 ✍️ Sprechtext 62 „3 Dinge, die das Finanzamt längst weiß“ (Idee Loris 22.10.) ([`c420547`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c420547619d7148e7d17fa782d754b62f0aed41d))
  - `posts/sprechtexte.md`
- 03:59 ✍️ Wissen 22.10.: Postzeiten-Routine (Story-Umfrage statt Repost, 48-h-Pause, ≤ 3 Hashtags) ([`c865e1b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c865e1b5014a1c6079e1cd823da7a9a8b161ff88))
  - `LAGE.html`, `automatik/lage_notizen.md`, `automatik/routinen`, `strategie/18_wissen_2026-10-21.md`

**Mi 21.10.2026**
- 20:03 ✍️ Stand 21.10. abends: AfA-Reel online (manuell), Notizen und Lage aktualisiert ([`2b1f882`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2b1f8825bdf1495df1aa3e2ea1e26d9ecef90475))
  - Plan: `42-reel-afa` status: pausiert → veroeffentlicht; `42-reel-afa` zeit: 2026-10-29 17:45 → 2026-10-21 16:35
- 18:10 🤖 Autopilot: 58-reel-vorsteuer veroeffentlicht ([`ec5614b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ec5614b9bdae1f4eb87a0af046e06368dd6afe4a))
  - Plan: `58-reel-vorsteuer` status: freigegeben → veroeffentlicht; `58-reel-vorsteuer` online: https://www.instagram.com/reel/Dewza8JCASO/
- 18:08 🤖 Autopilot: Dateien fuer 58-reel-vorsteuer vorbereitet ([`8be6fd4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8be6fd4877629f55a22b6a55602e46b1912a40fc))
  - `posts/58_2026-11-08_reel_vorsteuer`
- 17:52 ✍️ Reel 58 umgebaut (Hook ab Frame 1, neues Titelbild), Autopilot 18:00 ([`22a87a2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/22a87a2d61d97ad13069ddcfa9597435cdb03c9d))
  - Plan: `58-reel-vorsteuer` status: pausiert → freigegeben
- 17:42 ✍️ Reel 58 angehalten (Umbau, neu 18:00) ([`f4dd096`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f4dd0960c39fb7a9bfb769c259905f126872bfac))
  - Plan: `58-reel-vorsteuer` status: freigegeben → pausiert; `58-reel-vorsteuer` zeit: 2026-10-21 17:45 → 2026-10-21 18:00
- 17:38 ✍️ Auswertung: erstes Stimm-Fach-Reel (AfA) nach 1 h ([`f37dadc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f37dadc570822d4a307b8491d14a13c7c1ffcd15))
  - `strategie/06_auswertung.md`
- 16:42 ✍️ Reel 58 (Vorsteuer) mit Stimme, Autopilot heute 17:45 ([`fd702af`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fd702afc1456427f044a99abac6a00784c2d3f48))
  - Plan: `58-reel-vorsteuer` status: pausiert → freigegeben; `58-reel-vorsteuer` zeit: 2026-11-08 11:45 → 2026-10-21 17:45
- 16:34 ✍️ Wissen 21.10.: Meta-Kennzahlen (Hook Rate = 3 s, geschätzte Werte nur als Trend) ([`2238d53`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2238d5384316896999a2ec218333705d1e0233bf))
  - `strategie/18_wissen_2026-10-21.md`
- 15:31 ✍️ Reel 42 (AfA) mit Stimme 21.10.; Stimmen neu geschnitten nur in echten Pausen ([`907fde5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/907fde5b0c6c77871c040a950a8f49032c619266))
  - `aufnahmen/2026-10-21/geschnitten/schnitt.py`, `aufnahmen/2026-10-21/geschnitten/stimme_30.wav`, `aufnahmen/2026-10-21/geschnitten/stimme_32.wav`, `aufnahmen/2026-10-21/geschnitten/stimme_33.wav`, `aufnahmen/2026-10-21/geschnitten/stimme_34.wav`, `aufnahmen/2026-10-21/geschnitten/stimme_36.wav`, `…`
- 14:31 ✍️ Aufnahme 21.10.: Fachbeitrags-Sprechtexte, beste Takes je Reel geschnitten (21 Stimmen, −18 LUFS) ([`487cdc1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/487cdc13507c54c7bb502807953deb44dbc97423))
  - `aufnahmen/2026-10-21/geschnitten/info.json`, `aufnahmen/2026-10-21/geschnitten/schnitt.py`, `aufnahmen/2026-10-21/geschnitten/stimme_30.wav`, `aufnahmen/2026-10-21/geschnitten/stimme_32.wav`, `aufnahmen/2026-10-21/geschnitten/stimme_33.wav`, `aufnahmen/2026-10-21/geschnitten/stimme_34.wav`, `…`
- 13:52 ✍️ Sprechtexte als Fachbeiträge 25–30 s (Loris 21.10.); Reel-Regel und Content-Fabrik angepasst ([`2553eb2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2553eb251ef95617b1782f6df72b4d3ca232d3b5))
  - `automatik/routinen`, `posts/sprechtexte.md`, `strategie/09_reel_regeln.md`
- 12:16 ✍️ Karussells auf 3:4 (1080×1440): Vorlagen umgestellt, 11 kommende Karussells neu gerendert ([`eec6c7b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/eec6c7bdf3a250a718e921dd5dde790da1f00c29))
  - `posts/10_2026-10-22_e_rechnung`, `posts/31_2026-10-22_zinsschranke`, `posts/35_2026-10-25_steuerkalender`, `posts/37_2026-10-27_bp_vorbereitung`, `posts/41_2026-10-29_mythen`, `posts/44_2026-10-30_glossar`, `…`
- 12:06 ✍️ Alle geplanten Beiträge pausiert (Loris 21.10.); Bildunterschriften mit großartigen Hooks, erster Kommentar automatisch nach dem Posten ([`0725ab0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0725ab046c6c6422e3ef8daf5439c67a16c8c230))
  - Plan: `30-reel-gwg` status: freigegeben → pausiert; `30-story-quiz` status: freigegeben → pausiert; `20-reel-erechnung` status: freigegeben → pausiert; `31-karussell-zinsschranke` status: freigegeben → pausiert; `10-story-umfrage` status: freigegeben → pausiert; `21-reel-zinsschranke` status: freigegeben → pausiert; `30-story-aufloesung` status: freigegeben → pausiert; `32-reel-mindeststeuer` status: freigegeben → pausiert; `32-story-zahl` status: freigegeben → pausiert; `10-e-rechnung` status: freigegeben → pausiert; `10-story-teaser` status: freigegeben → pausiert; `33-reel-paragraf-formel` status: freigegeben → pausiert; `33-story-teaser` status: freigegeben → pausiert; `34-reel-einspruch` status: freigegeben → pausiert; `34-story-tipp` status: freigegeben → pausiert; `35-karussell-steuerkalender` status: freigegeben → pausiert; `35-story-teaser` status: freigegeben → pausiert; `36-reel-bewirtung` status: freigegeben → pausiert; `36-story-tipp` status: freigegeben → pausiert; `22-reel-steuersatz` status: freigegeben → pausiert; `37-karussell-bp-vorbereitung` status: freigegeben → pausiert; `37-story-tipp` status: freigegeben → pausiert; `38-reel-pruefpfad` status: freigegeben → pausiert; `38-story-teaser` status: freigegeben → pausiert; `39-reel-holding` status: freigegeben → pausiert; `39-story-quiz` status: freigegeben → pausiert; `40-reel-formeln` status: freigegeben → pausiert; `40-story-teaser` status: freigegeben → pausiert; `41-karussell-mythen` status: freigegeben → pausiert; `41-story-tipp` status: freigegeben → pausiert; `42-reel-afa` status: freigegeben → pausiert; `42-story-teaser` status: freigegeben → pausiert; `43-reel-par35` status: freigegeben → pausiert; `43-story-tipp` status: freigegeben → pausiert; `44-karussell-glossar` status: freigegeben → pausiert; `44-story-teaser` status: freigegeben → pausiert; `45-reel-vga` status: freigegeben → pausiert; `45-story-teaser` status: freigegeben → pausiert; `46-karussell-dividenden-8b` status: freigegeben → pausiert; `46-story-zdt` status: freigegeben → pausiert; `47-reel-betriebsaufspaltung` status: freigegeben → pausiert; `47-story-teaser` status: freigegeben → pausiert; `48-reel-firmenwagen` status: freigegeben → pausiert; `48-story-tipp` status: freigegeben → pausiert; `49-reel-kleinunternehmer` status: freigegeben → pausiert; `49-story-teaser` status: freigegeben → pausiert; `50-reel-gebaeude-afa` status: freigegeben → pausiert; `50-story-tipp` status: freigegeben → pausiert; `51-karussell-kapitalertraege` status: freigegeben → pausiert; `51-story-teaser` status: freigegeben → pausiert; `52-reel-gobd` status: freigegeben → pausiert; `52-story-tipp` status: freigegeben → pausiert; `53-reel-iab` status: freigegeben → pausiert; `53-story-teaser` status: freigegeben → pausiert; `54-reel-reverse-charge` status: freigegeben → pausiert; `54-story-tipp` status: freigegeben → pausiert; `53-karussell-iab` status: freigegeben → pausiert; `53-story-teaser-karussell` status: freigegeben → pausiert; `55-reel-thesaurierung` status: freigegeben → pausiert; `55-story-tipp` status: freigegeben → pausiert; `56-karussell-verjaehrung` status: freigegeben → pausiert; `56-story-teaser` status: freigegeben → pausiert; `57-reel-verlust-8c` status: freigegeben → pausiert; `57-story-teaser` status: freigegeben → pausiert; `58-reel-vorsteuer` status: freigegeben → pausiert; `58-story-tipp` status: freigegeben → pausiert; `59-karussell-pensionen` status: freigegeben → pausiert; `59-story-teaser` status: freigegeben → pausiert
- 11:59 ✍️ Wissen 21.10.: großartige Hooks, Format 3:4, Karussell-Aufbau, Routine nach dem Posten; Sprechtexte mit neuen Hooks ([`4752ff5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4752ff57357b3e20d60a85c672ebc23b46b8872a))
  - `automatik/routinen`, `posts/sprechtexte.md`, `strategie/08_hooks.md`, `strategie/17_karussell_design.md`, `strategie/18_wissen_2026-10-21.md`
- 10:54 ✍️ Sprechtexte 21.10.: Stimm-Fassung für alle 21 Reels ab heute ([`9f9630b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9f9630be2b8c54ec7237d590aeb8892c2c294a06))
  - `posts/sprechtexte.md`
- 09:22 📈 Statistik 2026-10-21 ([`f404f3e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f404f3e639597c30fe30c8ae4a0e7fbab9927786))
  - `automatik/statistik`
- 08:00 📡 Radar 2026-10-21: 8 Beiträge, 0 DM-Entwürfe ([`55c2c36`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/55c2c360a480fbbde486b749d04d7df1922b11e9))
  - `automatik/interaktion`

<details><summary>Älter als 7 Tage</summary>

**Di 20.10.2026**
- 14:54 ✍️ Tagesbericht 20. Oktober: −41% Reichweite, 3/9 Methoden erfolgreich ([`3dcec7d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3dcec7ddc7c3b92e32560559e7a104fa03b11602))
  - `LAGE.html`, `automatik/berichte`
- 09:34 📈 Statistik 2026-10-20 ([`8e4923c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8e4923c2dd1f03f41321b685fda75f144d9b9d6d))
  - `automatik/statistik`
- 17:50 🤖 Autopilot: 28-story-aufloesung veroeffentlicht ([`73152cc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/73152cc6473f5066c434511b2e849c18052fcc76))
  - Plan: `28-story-aufloesung` status: freigegeben → veroeffentlicht; `28-story-aufloesung` online: https://www.instagram.com/stories/maehrsteuern/4012196501812014820
- 17:45 🤖 Autopilot: Dateien fuer 28-story-aufloesung vorbereitet ([`3d041f1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3d041f1b9caf1eaa1e927f77471795a02dd6e969))
  - `posts/28_2026-10-19_reel_zuschlaege`
- 17:45 🤖 Autopilot: 19-reel-verlustvortrag veroeffentlicht ([`b32dff7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b32dff711058e72d12d412fe18d8293d030b57b5))
  - Plan: `19-reel-verlustvortrag` status: freigegeben → veroeffentlicht; `19-reel-verlustvortrag` online: https://www.instagram.com/reel/DeuJJHoDXkl/
- 17:21 🤖 Autopilot: Dateien fuer 19-reel-verlustvortrag vorbereitet ([`f717de0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f717de06fdd80b8c3c7f3c72c0700c079efa4cb5))
  - `posts/19_2026-10-20_reel_verlustvortrag`
- 14:54 ✍️ Tagesbericht 20. Oktober: −41% Reichweite, 3/9 Methoden erfolgreich ([`909d652`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/909d652ca03f873dd90e02d86649eb639bdf26d9))
  - `LAGE.html`, `automatik/berichte`
- 14:14 📈 Statistik 2026-10-20 ([`0a8e3fd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0a8e3fdb074d97ccebd331113e3d34641b23c482))
  - `automatik/statistik`
- 13:28 ✍️ Instagram-Regeln Oktober 2026 (Google-KI-Antwort) als ungeprüftes Wissen eingetragen ([`a86b9c2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a86b9c2e5d175ad7ff1a90bf2dd6d0535023142b))
  - `automatik/lage_notizen.md`, `strategie/11_wissen_instagram.md`, `strategie/17_karussell_design.md`
- 13:27 ✍️ Karussell-Design-Regeln und Baustein für die Content-Fabrik ([`b127d80`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b127d80d3af2e0f704a081424dd448f8c3ef7226))
  - `README.md`, `automatik/lage_notizen.md`, `automatik/routinen`, `strategie/11_wissen_instagram.md`, `strategie/17_karussell_design.md`
- 12:24 🤖 Autopilot: 29-story-teaser veroeffentlicht ([`cfbfc3e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/cfbfc3e83bc85afe583bf3d79351fe7101aa240a))
  - Plan: `29-story-teaser` status: freigegeben → veroeffentlicht; `29-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4012035073688455220
- 12:24 🤖 Autopilot: Dateien fuer 29-story-teaser vorbereitet ([`a6501f5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a6501f551887c0ba3ec0ca327c0c1072eb2f688b))
  - `posts/29_2026-10-20_verluste_70`
- 12:24 🤖 Autopilot: 29-karussell-verluste veroeffentlicht ([`597d886`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/597d886deb95ec66fea1cfa637bb8529243d7271))
  - Plan: `29-karussell-verluste` status: freigegeben → veroeffentlicht; `29-karussell-verluste` online: https://www.instagram.com/p/DetnHd6G82Y/
- 12:22 🤖 Autopilot: Dateien fuer 29-karussell-verluste vorbereitet ([`943b6c7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/943b6c7349a0d25cc1b9f86576a1d7e4b90714b7))
  - `posts/29_2026-10-20_verluste_70`
- 09:34 📈 Statistik 2026-10-20 ([`38195d0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/38195d0a4eb07058603979585415860e17a35024))
  - `automatik/statistik`
- 07:28 📡 Radar 2026-10-20: 8 Beiträge, 0 DM-Entwürfe ([`aba45c8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/aba45c8dfd569198a5c5929be3f2b8668d6aa705))
  - `automatik/interaktion`

**Mo 19.10.2026**
- 13:52 ✍️ Tagesbericht 19. Oktober: −8% Reichweite, 4/9 Methoden erfolgreich ([`5baa649`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5baa64958f3d4ad8993b6fa8dc224d39e655bb43))
  - `automatik/berichte`
- 09:37 📈 Statistik 2026-10-19 ([`01128a3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/01128a3003147d1e087424a8a7853a713225c955))
  - `automatik/statistik`
- 09:32 ✍️ Tagesbericht 18. Oktober: +45% Reichweite, 6/10 Methoden erfolgreich ([`f7e2739`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f7e27390004fcc264c0996138b6644d388dd1e60))
  - `automatik/berichte`
- 19:26 🤖 Autopilot: 18-reel-aufbewahrung veroeffentlicht ([`0e93a0d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0e93a0d136d815e4bb611d9ef14e9513d3fb00e6))
  - Plan: `18-reel-aufbewahrung` status: freigegeben → veroeffentlicht; `18-reel-aufbewahrung` online: https://www.instagram.com/reel/DeryoWUE_Or/
- 19:25 🤖 Autopilot: Dateien fuer 18-reel-aufbewahrung vorbereitet ([`6eae2ca`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6eae2ca71f2a557899258f763c3a7ef8a10fbbe5))
  - `posts/18_2026-10-19_reel_aufbewahrung`
- 16:02 📈 Statistik 2026-10-19 ([`9665ae7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9665ae7c4dee9510e80f9ff4f131dccb3103a02e))
  - `automatik/statistik`
- 13:52 ✍️ Tagesbericht 19. Oktober: −8% Reichweite, 4/9 Methoden erfolgreich ([`c0930f6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c0930f61e0be6c3e0f780c868463410cc17cb4cb))
  - `automatik/berichte`
- 12:52 🤖 Autopilot: 28-story-quiz veroeffentlicht ([`763f070`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/763f070c7bcc9dba81c81f1079675e9c43910469))
  - Plan: `28-story-quiz` status: freigegeben → veroeffentlicht; `28-story-quiz` online: https://www.instagram.com/stories/maehrsteuern/4011324194198123089
- 12:52 🤖 Autopilot: Dateien fuer 28-story-quiz vorbereitet ([`c5c60d2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c5c60d2a27160e56fd6e0891709216b39f5f2ee9))
  - `posts/28_2026-10-19_reel_zuschlaege`
- 12:52 🤖 Autopilot: 28-reel-zuschlaege veroeffentlicht ([`4bc0642`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4bc0642194080491d56295e23dcedbef22847669))
  - Plan: `28-reel-zuschlaege` status: freigegeben → veroeffentlicht; `28-reel-zuschlaege` online: https://www.instagram.com/reel/DerFcnnnTMT/
- 12:51 🤖 Autopilot: Dateien fuer 28-reel-zuschlaege vorbereitet ([`be13455`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/be134558a4708e9b7b578b6c16ba66e3da812a1d))
  - `posts/28_2026-10-19_reel_zuschlaege`
- 09:37 📈 Statistik 2026-10-19 ([`f4dba84`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f4dba8488cde74320627a1b8f0261daf46d85ca4))
  - `automatik/statistik`
- 09:32 ✍️ Tagesbericht 18. Oktober: +45% Reichweite, 6/10 Methoden erfolgreich ([`b9e9b96`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b9e9b961133350182f79aaa2b40ca8dc863b6684))
  - `automatik/berichte`
- 07:15 📡 Radar 2026-10-19: 8 Beiträge, 0 DM-Entwürfe ([`f24b172`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f24b17280244cdb352b99cc0ea9ef3757ad69b91))
  - `automatik/interaktion`

**So 18.10.2026**
- 20:18 ✍️ Reel 61: Version mit Loris' Stimme (30 s, beste Takes, Untertitel Wort für Wort) – von Hand über Edits ([`d5ea58a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d5ea58a3621dbf603ff331527a0623c8e02bef9f))
  - `posts/61_2026-10-18_reel_rms_finanzamt`, `vorlagen/system/schnitt/p61_reel_stimme_bauen.py`
- 19:54 ✍️ Reel 61: Status manuell – Loris postet von Hand über Edits ([`24a5e56`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/24a5e562283e604b68b9dfc01ef89b218851fff5))
  - Plan: `61-reel-rms-finanzamt` status: freigegeben → manuell
- 19:43 ✍️ Wochenbericht KW 2026-42 ([`6c25e1f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6c25e1fa7071bec4f01f0a2c16e67b982f7e01b4))
  - `automatik/statistik`
- 19:42 ✍️ Reel 61: Einzelbild „Deine Steuererklärung liest zuerst kein Mensch“ (RMS, § 88 Abs. 5 AO) – freigegeben für 18.10. 19:45 ([`0879258`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/087925802a0db2a86b2c22a07854115e7cce0f9b))
  - Plan: neu `61-reel-rms-finanzamt` (2026-10-18 19:45, freigegeben)
- 17:50 🤖 Autopilot: 27-story-teaser veroeffentlicht ([`e978ebf`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e978ebfe1aa136bf28c8101a52d06a8b985ad57e))
  - Plan: `27-story-teaser` status: freigegeben → veroeffentlicht; `27-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4010746920150907932
- 17:45 🤖 Autopilot: Dateien fuer 27-story-teaser vorbereitet ([`e04eead`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e04eeadec7a2fbfd4af56d71716b3f47fe1a2af1))
  - `posts/27_2026-10-18_reel_organschaft`
- 17:45 🤖 Autopilot: 27-reel-organschaft veroeffentlicht ([`e2d8d24`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e2d8d24817a798061e1d1f88a17cb5998e63d58c))
  - Plan: `27-reel-organschaft` status: freigegeben → veroeffentlicht; `27-reel-organschaft` online: https://www.instagram.com/reel/Deo8TzBjns_/
- 16:52 🤖 Autopilot: Dateien fuer 27-reel-organschaft vorbereitet ([`6a26e95`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6a26e95384354d18262467d446375bf9bd29f00a))
  - `posts/27_2026-10-18_reel_organschaft`
- 13:40 🤖 Autopilot: 26-story-tipp veroeffentlicht ([`38b0bcf`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/38b0bcf4e5fc6d6674f75828899230c14c58ad57))
  - Plan: `26-story-tipp` status: freigegeben → veroeffentlicht; `26-story-tipp` online: https://www.instagram.com/stories/maehrsteuern/4010623450268543057
- 13:39 🤖 Autopilot: Dateien fuer 26-story-tipp vorbereitet ([`59e23b8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/59e23b85485ddc921b157614598e9a5d9c3580ca))
  - `posts/26_2026-10-18_kuerzungen`
- 13:39 🤖 Autopilot: 26-karussell-kuerzungen veroeffentlicht ([`ae5fe9f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ae5fe9fc1d09c46c7f2a3dc4656e6163cee41506))
  - Plan: `26-karussell-kuerzungen` status: freigegeben → veroeffentlicht; `26-karussell-kuerzungen` online: https://www.instagram.com/p/DeomJhQG4o8/
- 13:37 🤖 Autopilot: Dateien fuer 26-karussell-kuerzungen vorbereitet ([`d6441d5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d6441d5352955936cdf8cfa7922f6ceee770ff2a))
  - `posts/26_2026-10-18_kuerzungen`
- 09:19 📈 Statistik 2026-10-18 ([`ce42aa3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ce42aa33224a40f452d8a22456da1f8160215aa0))
  - `automatik/statistik`
- 08:34 📡 Radar 2026-10-18: 8 Beiträge, 0 DM-Entwürfe ([`202a9d5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/202a9d53176496be4e01f10cff5a482fdc7f08f6))
  - `automatik/interaktion`

**Sa 17.10.2026**
- 19:00 🤖 Autopilot: 25-story-teaser veroeffentlicht ([`68449e0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/68449e01da676d7b4c74238f4f307aa4c69f36d8))
  - Plan: `25-story-teaser` status: freigegeben → veroeffentlicht; `25-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4010059715828907470
- 18:59 🤖 Autopilot: Dateien fuer 25-story-teaser vorbereitet ([`b59d9d2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b59d9d2bcd3af77c14aef956a1787c2631393efe))
  - `posts/25_2026-10-17_reel_plausi`
- 18:59 🤖 Autopilot: 25-reel-plausi veroeffentlicht ([`ddd63a5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ddd63a5fec029bd0435535ff2858c070185566cb))
  - Plan: `25-reel-plausi` status: freigegeben → veroeffentlicht; `25-reel-plausi` online: https://www.instagram.com/reel/Deml8DcD_Dx/
- 18:58 🤖 Autopilot: Dateien fuer 25-reel-plausi vorbereitet ([`21e8942`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/21e89429a9649ceb3ee3bee868bce16991f8f485))
  - `posts/25_2026-10-17_reel_plausi`
- 12:35 🤖 Autopilot: 01-story-teaser veroeffentlicht ([`6af7ed2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6af7ed21274cdca2a697a5e5cf794149a0c9cda4))
  - Plan: `01-story-teaser` status: freigegeben → veroeffentlicht; `01-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4009865918985715708
- 12:34 🤖 Autopilot: Dateien fuer 01-story-teaser vorbereitet ([`fc129bc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fc129bc6662ebbdb4ce514f80dfb839ff4a56bc9))
  - `posts/01_2026-10-04_reel_ampel`
- 12:34 🤖 Autopilot: 01-reel-ampel veroeffentlicht ([`5909755`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/59097558a84ca99e01a56912c3abc5dd6cd6075a))
  - Plan: `01-reel-ampel` status: freigegeben → veroeffentlicht; `01-reel-ampel` online: https://www.instagram.com/reel/Del54DNE7fz/
- 12:33 🤖 Autopilot: Dateien fuer 01-reel-ampel vorbereitet ([`4cd7e78`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4cd7e7894c312be99e8760e2fab886f27cb72f44))
  - `posts/01_2026-10-04_reel_ampel`
- 10:01 ✍️ Stimm-Reels 18–22 aus Loris' Aufnahme vom 17.10. geschnitten und freigegeben ([`c638676`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c638676a697d861ae5839c5e3a4d298d53f0aaca))
  - `LAGE.html`, `automatik/plan.json`, `posts/18_2026-10-19_reel_aufbewahrung`, `posts/19_2026-10-20_reel_verlustvortrag`, `posts/20_2026-10-21_reel_erechnung`, `posts/21_2026-10-22_reel_zinsschranke`, `…`
- 09:29 ✍️ Tagesbericht 17. Oktober: 368 Follower (+3), Reichweite 146, 6 Methoden ✅ ([`a7a4844`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a7a4844048864095fe6a2eb56a43ba8567519881))
  - `automatik/berichte`
- 09:19 ✍️ Aufnahme 17.10. (alle Sprechtexte 18–22) + Anweisungen daraus: Kalender-Erinnerung, Zinsschranke-Serie ([`642f5be`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/642f5beeeeb7e239ffb3e65b0c6bc0860560ec18))
  - `LAGE.html`, `aufnahmen/2026-10-17_sprechtexte.mp3`, `aufnahmen/2026-10-17_sprechtexte_woerter.json`, `automatik/erinnerungen.json`, `strategie/13_backlog.md`
- 09:19 📈 Statistik 2026-10-17 ([`c02ca73`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c02ca73d8393e09b81e59486376632abe40b4b36))
  - `automatik/statistik`
- 08:08 📡 Radar 2026-10-17: 8 Beiträge, 0 DM-Entwürfe ([`dcd9eeb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/dcd9eeb97bf8a423c39a31d289c16e84a047d6ec))
  - `automatik/interaktion`

**Fr 16.10.2026**
- 19:58 🤖 Autopilot: 04-story-teaser veroeffentlicht ([`97bc986`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/97bc986ff205d3055248653a6db5d4120049963c))
  - Plan: `04-story-teaser` status: freigegeben → veroeffentlicht; `04-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4009364203832588698
- 19:57 🤖 Autopilot: Dateien fuer 04-story-teaser vorbereitet ([`891e4c6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/891e4c6965890a6c2e3d8ae78f062a25f7cc2065))
  - `posts/04_2026-10-20_reel_mein_weg`
- 19:57 🤖 Autopilot: 04-reel-mein-weg veroeffentlicht ([`702317b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/702317b7456085a7b612d168cfcc34a160b4412c))
  - Plan: `04-reel-mein-weg` status: freigegeben → veroeffentlicht; `04-reel-mein-weg` online: https://www.instagram.com/reel/DekHzHkF7E2/
- 19:56 🤖 Autopilot: Dateien fuer 04-reel-mein-weg vorbereitet ([`c84f980`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c84f9801c22dbb45f5cd8ac9b1199fd76fc93d6c))
  - `posts/04_2026-10-20_reel_mein_weg`
- 13:59 📈 Statistik 2026-10-16 ([`03a7062`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/03a706239d18de19226340ec07406a881b71d4a5))
  - `automatik/statistik`
- 12:15 🤖 Autopilot: 03-story-aufloesung veroeffentlicht ([`3f7f444`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3f7f444bdaf540ba9e23576159d05dfdde8bbec7))
  - Plan: `03-story-aufloesung` status: freigegeben → veroeffentlicht; `03-story-aufloesung` online: https://www.instagram.com/stories/maehrsteuern/4009116186525268251
- 11:48 📡 Radar 2026-10-16: 8 Beiträge, 0 DM-Entwürfe ([`3b1c3e0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3b1c3e068baa3dd731c9a75c829476a2faf85923))
  - `automatik/interaktion`
- 11:45 🤖 Autopilot: Dateien fuer 03-story-aufloesung vorbereitet ([`5368e91`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5368e918d254122c64cd7fd714b2eb14d365336e))
  - `posts/03_2026-10-13_gewst_hinzurechnung`
- 11:45 🤖 Autopilot: 24-reel-ein-euro veroeffentlicht ([`4ba5f80`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4ba5f80bf7f6181d263d14534cea7ee5aa168f9d))
  - Plan: `24-reel-ein-euro` status: freigegeben → veroeffentlicht; `24-reel-ein-euro` online: https://www.instagram.com/reel/DejLN1HiY0k/
- 11:07 🤖 Autopilot: Dateien fuer 24-reel-ein-euro vorbereitet ([`2355cc2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2355cc2d7bd1049034095519026869fae3d12634))
  - `posts/24_2026-10-16_reel_ein_euro`
- 10:26 ✍️ LAGE regeneriert nach Tagesbericht 15. Oktober ([`acd61f7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/acd61f748d97205ccb7dcd9b14733dd8001ea3db))
  - `LAGE.html`
- 10:26 ✍️ Tagesbericht 15. Oktober: 365 Follower (+1), Reichweite 195, 6 Methoden ✅ ([`9cb1f72`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9cb1f72e22fa2474046a3b45d4822f9fc5255d8d))
  - `automatik/berichte`

**Do 15.10.2026**
- 21:57 ✍️ Sprechtexte: Aufnahme-Doc für Fr 16.10. im Drive, Steuersatz-Reel auf 26.10. + „Kommentiere TOOL“ ([`d5b5672`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d5b5672beab5adc7ab6900b05441cb2f6b8d9c0f))
  - `LAGE.html`, `posts/sprechtexte.md`
- 21:15 🤖 Autopilot: 16-reel-listen veroeffentlicht ([`d4a5adc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d4a5adcc4c5d7da91adbfa6e447448603b3c8fdf))
  - Plan: `16-reel-listen` status: freigegeben → veroeffentlicht; `16-reel-listen` online: https://www.instagram.com/reel/DehnTbyEZ2g/
- 20:34 🤖 Autopilot: Dateien fuer 16-reel-listen vorbereitet ([`aebfbf3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/aebfbf3ceae88a1bea51ff379b6ccb48b4be91b9))
  - `posts/16_2026-10-15_reel_listen`
- 19:47 💼 LinkedIn-Bild mit aktuellem Headshot (15.10.) ([`d20616f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d20616f7798c3b8fc7685c2e914e850fdfa7bce1))
  - `assets/marke/loris_headshot_1.jpg`, `assets/marke/loris_headshot_2.jpg`, `posts/60_2026-10-15_reel_geld_verschenkt`, `vorlagen/system/linkedin_bild.html`
- 19:46 💼 LinkedIn-Paket zum Follower-Reel (Bild + Text); Fallbeispiele korrigiert (Lohnersatzleistungen = Pflichtveranlagung) ([`a0b1ce1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a0b1ce16d92337e72251b909d86b3d5c344cb6e9))
  - `LAGE.html`, `posts/60_2026-10-15_reel_geld_verschenkt`, `vorlagen/system/linkedin_bild.html`
- 18:32 ✍️ SVERWEIS-Reel auf 21:15 verschoben (17:45 ausgefallen, Vorsprung fürs Follower-Reel) ([`6316cba`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6316cbab0429c6dfd1e563a5428a8d4bddc776bc))
  - Plan: `16-reel-listen` zeit: 2026-10-15 17:45 → 2026-10-15 21:15
- 18:31 🤖 Autopilot: 04-story-frage veroeffentlicht ([`72fa99c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/72fa99c40ff9dce61b221deb13d0da756bd2bc76))
  - Plan: `04-story-frage` status: freigegeben → veroeffentlicht; `04-story-frage` online: https://www.instagram.com/stories/maehrsteuern/4008595900159636869
- 18:31 🤖 Autopilot: Dateien fuer 04-story-frage vorbereitet ([`777bc73`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/777bc730b4169336ee6d2d6170eff5b8bf2d2d69))
  - `posts/04_2026-10-20_reel_mein_weg`
- 18:29 🤖 Autopilot: 09-story-aufloesung veroeffentlicht ([`6cf9da8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6cf9da80e0d1adfe0b19ab0086d89f90e06321a3))
  - Plan: `09-story-aufloesung` status: freigegeben → veroeffentlicht; `09-story-aufloesung` online: https://www.instagram.com/stories/maehrsteuern/4008594677285168406
- 18:28 🤖 Autopilot: Dateien fuer 09-story-aufloesung vorbereitet ([`20be58b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/20be58b07a26643b2fd46656d6c480ce6ca5123f))
  - `posts/09_2026-10-15_rueckstellung`
- 18:27 🤖 Autopilot: 60-story-teaser veroeffentlicht ([`a202edd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a202edd151c60751dd494b3b5f747038cebe5181))
  - Plan: `60-story-teaser` status: freigegeben → veroeffentlicht; `60-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4008593645150536384
- 18:26 🤖 Autopilot: Dateien fuer 60-story-teaser vorbereitet ([`e3b7217`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e3b721705b09b57236e3b34c6238228c4db528ad))
  - `posts/60_2026-10-15_reel_geld_verschenkt`
- 18:25 🤖 Autopilot: 60-reel-geld-verschenkt veroeffentlicht ([`2083bfd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2083bfdf03e9e39f5a1dd210b2d8e30e50740b51))
  - Plan: `60-reel-geld-verschenkt` status: freigegeben → veroeffentlicht; `60-reel-geld-verschenkt` online: https://www.instagram.com/reel/DehYZkyD-sL/
- 18:24 🤖 Autopilot: Dateien fuer 60-reel-geld-verschenkt vorbereitet ([`98adca1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/98adca1f708d53aee02bb2131ba4fa3c27e74d09))
  - `posts/60_2026-10-15_reel_geld_verschenkt`
- 18:22 ✍️ Neues Follower-Reel „Geld verschenkt“ (Antragsveranlagung 2022 bis 31.12.2026) + Story, sofort freigegeben ([`f116413`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f116413d3f3419f857f6528cca694bd190a7c31a))
  - Plan: neu `60-reel-geld-verschenkt` (2026-10-15 18:35, freigegeben); neu `60-story-teaser` (2026-10-15 18:45, freigegeben)
- 17:38 ✍️ Sprechtext Follower-Reel „Geld, das Leute verschenken“ (Antragsveranlagung 2022 bis 31.12.) ([`0d1d4e0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0d1d4e0846308fb270d43028ea9a8de54400e1df))
  - `LAGE.html`, `posts/sprechtexte.md`
- 16:53 ✍️ Repo-Umzug zu MBS-maehrsteuern: Verweise, Takt-Anleitung und Wächter-Hinweis angepasst ([`b9a7fee`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b9a7feec735db7e10505320d72cc66745b18b2ff))
  - `EINRICHTUNG.md`, `automatik/freigabe.py`, `automatik/kalender.py`, `automatik/kommentare.py`, `automatik/lage.py`, `automatik/lage_notizen.md`, `…`
- 14:10 📈 Statistik 2026-10-15 ([`7f4b181`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7f4b18167dd8f61b06e189d0c897c0dd9d812359))
  - `automatik/statistik`
- 12:15 🤖 Autopilot: 09-story-teaser veroeffentlicht ([`43ead3b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/43ead3bc2ceaeab431fc196449077d1f150142e9))
  - Plan: `09-story-teaser` status: freigegeben → veroeffentlicht; `09-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4008391387481799579
- 12:07 ✍️ Plan: Stimm-Reels 18–22 auf Fassung ohne Stimme umgestellt (Notlösung, keine Aufnahme bis 15.10. 12:00) ([`57d175c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/57d175cde86a211435f4fbf7baae2470a284fae3))
  - Plan: `18-reel-aufbewahrung` status: wartet_auf_sprachnachricht → freigegeben; `19-reel-verlustvortrag` status: wartet_auf_sprachnachricht → freigegeben; `20-reel-erechnung` status: wartet_auf_sprachnachricht → freigegeben; `21-reel-zinsschranke` status: wartet_auf_sprachnachricht → freigegeben; `22-reel-steuersatz` status: wartet_auf_sprachnachricht → freigegeben
- 11:57 📡 Radar 2026-10-15: 8 Beiträge, 0 DM-Entwürfe ([`f11d92f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f11d92f88f7e1bba6923e66fa2413dae12b65211))
  - `automatik/interaktion`
- 11:45 🤖 Autopilot: Dateien fuer 09-story-teaser vorbereitet ([`339d132`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/339d1325aa0374adb8d787ffd363e1cfcea5f9c0))
  - `posts/09_2026-10-15_rueckstellung`
- 11:45 🤖 Autopilot: 09-rueckstellung veroeffentlicht ([`1e392cc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1e392ccbd73bb58a3cf7cd32a1d085f352e20946))
  - Plan: `09-rueckstellung` status: freigegeben → veroeffentlicht; `09-rueckstellung` online: https://www.instagram.com/p/DegoIVKluPa/
- 11:34 ✍️ Mein-Weg-Reel: Karte 1 als gerahmter Headshot statt Ganzkörper, Hook über den Rahmen ([`166a7d4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/166a7d4aa90facd5ec786ec561c07a818842f593))
  - `LAGE.html`, `assets/marke/karte_1_aktuell_9x16.png`, `assets/marke/loris_aktuell_freisteller_2026-10.png`, `automatik/lage_notizen.md`, `posts/04_2026-10-20_reel_mein_weg`, `vorlagen/system/schnitt/p04_reel_mein_weg_0810.json`
- 11:21 🤖 Autopilot: Dateien fuer 09-rueckstellung vorbereitet ([`d47306d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d47306d5bcb560788f0bf7ee5656027a1248295e))
  - `posts/09_2026-10-15_rueckstellung`
- 11:09 ✍️ Mein-Weg-Reel: Karte „Das bin ich heute“ mit aktuellem Foto (Bild 1) neu, Reel neu gerendert, KI-Hinweis ergänzt ([`593413e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/593413ee94912455090257e55e162c4475ac6afa))
  - `assets/marke/karte_1_aktuell_9x16.png`, `assets/marke/loris_aktuell_freisteller_2026-10.png`, `automatik/lage_notizen.md`, `posts/04_2026-10-20_reel_mein_weg`

**Mi 14.10.2026**
- 17:45 🤖 Autopilot: 07-reel-hinzurechnung veroeffentlicht ([`2cda127`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2cda127419002dbc77fc067d6ffd383412b79111))
  - Plan: `07-reel-hinzurechnung` status: freigegeben → veroeffentlicht; `07-reel-hinzurechnung` online: https://www.instagram.com/reel/DeemwStk5mL/
- 16:31 🤖 Autopilot: Dateien fuer 07-reel-hinzurechnung vorbereitet ([`af88a97`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/af88a97b3fbb92a2475cc8e9767d72a903148bc6))
  - `posts/03_2026-10-13_gewst_hinzurechnung`
- 12:15 🤖 Autopilot: 09-story-quiz veroeffentlicht ([`fe70178`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fe70178e388d8239e9cbc25805be3ecd28ebfe2d))
  - Plan: `09-story-quiz` status: freigegeben → veroeffentlicht; `09-story-quiz` online: https://www.instagram.com/stories/maehrsteuern/4007644771296937300
- 11:01 🤖 Autopilot: Dateien fuer 09-story-quiz vorbereitet ([`234f46f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/234f46f0714bdcb992442dc9992e649ac7b41778))
  - `posts/09_2026-10-15_rueckstellung`
- 09:39 ✍️ LAGE aktualisiert nach Tagesbericht 14. Oktober ([`95dd5d1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/95dd5d12f0e9300ea13d4217d07ec65374f411c9))
  - `LAGE.html`
- 09:38 ✍️ Tagesbericht 14. Oktober: Reichweite +23%, Website-Klicks x 9, Sehdauer grün ([`ca4022b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ca4022b41a97b229d5a3748ec0303f06cd1c75ed))
  - `automatik/berichte`
- 08:50 📈 Statistik 2026-10-14 ([`79e1d05`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/79e1d058cbada9781211ffa612dac1888cd2cf2e))
  - `automatik/statistik`
- 07:10 💼 LinkedIn-Pakete: 26-karussell-kuerzungen, 29-karussell-verluste, 31-karussell-zinsschranke, 35-karussell-steuerkalender, 37-karussell-bp-vorbereitung, 41-karussell-mythen, 44-karussell-glossar, 46-karussell-dividenden-8b, 51-karussell-kapitalertraege, 53-karussell-iab, 56-karussell-verjaehrung, 59-karussell-pensionen ([`faf26c5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/faf26c55651209ab7dbcb4f72bac877727909c02))
  - `posts/26_2026-10-18_kuerzungen`, `posts/29_2026-10-20_verluste_70`, `posts/31_2026-10-22_zinsschranke`, `posts/35_2026-10-25_steuerkalender`, `posts/37_2026-10-27_bp_vorbereitung`, `posts/41_2026-10-29_mythen`, `…`
- 07:05 📡 Radar 2026-10-14: 8 Beiträge, 0 DM-Entwürfe ([`e5cac03`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e5cac037e3f8f772fca6abbd6abdb3cf69c31ff0))
  - `automatik/interaktion`
- 06:51 ✍️ Bericht Nachtlauf 14.10. finalisiert (Morgen-Check, Radar-Fix) ([`015a26d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/015a26d56b96743b265a9b20ceaceae399f474a8))
  - `LAGE.html`, `strategie/16_optimierung_2026-10-14.md`
- 05:29 📡 Radar: gleicher Beitrag nicht mehr mehrfach vorschlagen ([`0311da4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0311da48b02b229d0a8927e2ecda9d3734c46e16))
  - `automatik/radar.py`
- 01:46 ✍️ QA KW 45: Fahrtenbuch-Normen, InvStG, § 171 AO, § 8c, § 34a ab 2028; Teaser ([`234e53f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/234e53f1ba57e2d4430bee2cc2ba4d38864bcfdc))
  - `LAGE.html`, `posts/48_2026-11-02_reel_firmenwagen`, `posts/51_2026-11-03_kapitalertraege`, `posts/52_2026-11-04_reel_gobd`, `posts/53_2026-11-04_iab`, `posts/55_2026-11-06_reel_thesaurierung`, `…`
- 01:19 ✍️ Bericht Nachtlauf 14.10.: Instagram-Optimierungen (Entwurf, QA KW 45 folgt) ([`92c6434`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/92c6434c40788e36757e3e60dbc089f8c466713c))
  - `LAGE.html`, `strategie/16_optimierung_2026-10-14.md`
- 01:18 ✍️ Plan: 04.–06.11. gefüllt (4 Reels, 2 Karussells, 6 Storys, freigegeben) ([`d79428e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d79428ee2f5f237886dfe0d0441a37f38afdb6e4))
  - Plan: neu `52-reel-gobd` (2026-11-04 11:45, freigegeben); neu `52-story-tipp` (2026-11-04 12:15, freigegeben); neu `53-reel-iab` (2026-11-04 17:45, freigegeben); neu `53-story-teaser` (2026-11-04 17:50, freigegeben); neu `54-reel-reverse-charge` (2026-11-05 11:45, freigegeben); neu `54-story-tipp` (2026-11-05 12:15, freigegeben); neu `53-karussell-iab` (2026-11-05 17:45, freigegeben); neu `53-story-teaser-karussell` (2026-11-05 17:50, freigegeben); neu `55-reel-thesaurierung` (2026-11-06 11:45, freigegeben); neu `55-story-tipp` (2026-11-06 12:15, freigegeben); neu `56-karussell-verjaehrung` (2026-11-06 17:45, freigegeben); neu `56-story-teaser` (2026-11-06 17:50, freigegeben)
- 01:13 ✍️ Plan: 02./03.11. gefüllt (3 Reels, 1 Karussell, 4 Storys, freigegeben) ([`d107c25`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d107c252e79f77215ffa99c550ccd9e1d494b904))
  - Plan: neu `48-reel-firmenwagen` (2026-11-02 11:45, freigegeben); neu `48-story-tipp` (2026-11-02 12:15, freigegeben); neu `49-reel-kleinunternehmer` (2026-11-02 17:45, freigegeben); neu `49-story-teaser` (2026-11-02 17:50, freigegeben); neu `50-reel-gebaeude-afa` (2026-11-03 11:45, freigegeben); neu `50-story-tipp` (2026-11-03 12:15, freigegeben); neu `51-karussell-kapitalertraege` (2026-11-03 17:45, freigegeben); neu `51-story-teaser` (2026-11-03 17:50, freigegeben)
- 01:13 ✍️ QA KW 44: ApO statt BpO, § 35 als Ermäßigung, Teaser nicht mehr angeschnitten ([`440024c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/440024c11e345604c848b57a1dea392d2ef539fc))
  - `LAGE.html`, `posts/37_2026-10-27_bp_vorbereitung`, `posts/38_2026-10-27_reel_pruefpfad`, `posts/39_2026-10-28_reel_holding`, `posts/40_2026-10-28_reel_formeln`, `posts/42_2026-10-29_reel_afa`, `…`
- 01:07 ✍️ Plan: 07./08.11. gefüllt (2 Reels, 1 Karussell, 3 Storys, freigegeben) ([`d3fc1ce`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d3fc1cebc4a7919a3aa2f5cef7577b1561a4fc22))
  - Plan: neu `57-reel-verlust-8c` (2026-11-07 17:45, freigegeben); neu `57-story-teaser` (2026-11-07 17:50, freigegeben); neu `58-reel-vorsteuer` (2026-11-08 11:45, freigegeben); neu `58-story-tipp` (2026-11-08 12:15, freigegeben); neu `59-karussell-pensionen` (2026-11-08 17:45, freigegeben); neu `59-story-teaser` (2026-11-08 17:50, freigegeben)
- 00:53 ✍️ Lage-Notizen: Nachtlauf 14.10. zusammengefasst ([`f47a927`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f47a927ab6a462ee8f3f67a07e8fdc713747acb3))
  - `LAGE.html`, `automatik/lage_notizen.md`
- 00:51 ✍️ QA-Korrekturen: Hashtag-Fallen, Zinsschranke-EBITDA, Organschaft, Zuschläge, Lesbarkeit ([`5323eec`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5323eecc3acb8cc88acaaf7b405e53f40890ef65))
  - `LAGE.html`, `posts/01_2026-10-04_reel_ampel`, `posts/16_2026-10-15_reel_listen`, `posts/20_2026-10-21_reel_erechnung`, `posts/21_2026-10-22_reel_zinsschranke`, `posts/27_2026-10-18_reel_organschaft`, `…`
- 00:31 ✍️ Plan: 29./30.10. gefüllt (2 Reels, 2 Karussells, 4 Storys, freigegeben) ([`e6fa956`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e6fa956f3640ad15c1a3433b72790b86b93c7496))
  - Plan: neu `41-karussell-mythen` (2026-10-29 11:45, freigegeben); neu `41-story-tipp` (2026-10-29 12:15, freigegeben); neu `42-reel-afa` (2026-10-29 17:45, freigegeben); neu `42-story-teaser` (2026-10-29 17:50, freigegeben); neu `43-reel-par35` (2026-10-30 11:45, freigegeben); neu `43-story-tipp` (2026-10-30 12:15, freigegeben); neu `44-karussell-glossar` (2026-10-30 17:45, freigegeben); neu `44-story-teaser` (2026-10-30 17:50, freigegeben)
- 00:31 ✍️ Plan: 26.–28.10. gefüllt (4 Reels, 1 Karussell, 5 Storys, freigegeben) ([`b5fdc39`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b5fdc399b015da0e3b17a8e88866df2094cf1999))
  - Plan: neu `36-reel-bewirtung` (2026-10-26 11:45, freigegeben); neu `36-story-tipp` (2026-10-26 12:15, freigegeben); neu `37-karussell-bp-vorbereitung` (2026-10-27 11:45, freigegeben); neu `37-story-tipp` (2026-10-27 12:15, freigegeben); neu `38-reel-pruefpfad` (2026-10-27 17:45, freigegeben); neu `38-story-teaser` (2026-10-27 17:50, freigegeben); neu `39-reel-holding` (2026-10-28 11:45, freigegeben); neu `39-story-quiz` (2026-10-28 12:15, freigegeben); neu `40-reel-formeln` (2026-10-28 17:45, freigegeben); neu `40-story-teaser` (2026-10-28 17:50, freigegeben)
- 00:26 ✍️ Plan: 31.10./01.11. gefüllt (2 Reels, 1 Karussell, 3 Storys, freigegeben) ([`3f27fe0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3f27fe0533bc8d9d3bd8b0b34e9e294d9bb2a320))
  - Plan: neu `45-reel-vga` (2026-10-31 17:45, freigegeben); neu `45-story-teaser` (2026-10-31 17:50, freigegeben); neu `46-karussell-dividenden-8b` (2026-11-01 11:45, freigegeben); neu `46-story-zdt` (2026-11-01 12:15, freigegeben); neu `47-reel-betriebsaufspaltung` (2026-11-01 17:45, freigegeben); neu `47-story-teaser` (2026-11-01 17:50, freigegeben)
- 00:13 ✍️ Notlösung bereit: 5 Reels ohne Stimme für 18–22 (Aufbewahrung … Steuersatz) ([`68bdddf`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/68bdddf43ab89f34e405a8fe02f55c3a268ff4bd))
  - `LAGE.html`, `automatik/plan.json`, `posts/18_2026-10-19_reel_aufbewahrung`, `posts/19_2026-10-20_reel_verlustvortrag`, `posts/20_2026-10-21_reel_erechnung`, `posts/21_2026-10-22_reel_zinsschranke`, `…`

**Di 13.10.2026**
- 23:44 ✍️ Plan: Lücken 16.–18.10. gefüllt (3 Reels, 1 Karussell, 3 Storys, freigegeben) ([`0d15697`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0d15697e1a0cf25025af67bc82391c0e8b2a6a83))
  - Plan: neu `24-reel-ein-euro` (2026-10-16 11:45, freigegeben); neu `25-reel-plausi` (2026-10-17 17:45, freigegeben); neu `25-story-teaser` (2026-10-17 17:50, freigegeben); neu `26-karussell-kuerzungen` (2026-10-18 11:45, freigegeben); neu `26-story-tipp` (2026-10-18 12:15, freigegeben); neu `27-reel-organschaft` (2026-10-18 17:45, freigegeben); neu `27-story-teaser` (2026-10-18 17:50, freigegeben)
- 23:42 ✍️ Plan: Lücken 23.–25.10. gefüllt (3 Reels, 1 Karussell, 4 Storys, freigegeben) ([`30e75c2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/30e75c2dc4abe4558981365f4f123fbcb182cb80))
  - Plan: neu `32-reel-mindeststeuer` (2026-10-23 11:45, freigegeben); neu `32-story-zahl` (2026-10-23 12:15, freigegeben); neu `33-reel-paragraf-formel` (2026-10-24 11:45, freigegeben); neu `33-story-teaser` (2026-10-24 12:15, freigegeben); neu `34-reel-einspruch` (2026-10-25 11:45, freigegeben); neu `34-story-tipp` (2026-10-25 12:15, freigegeben); neu `35-karussell-steuerkalender` (2026-10-25 17:45, freigegeben); neu `35-story-teaser` (2026-10-25 17:50, freigegeben)
- 23:38 ✍️ Plan: Lücken 19.–22.10. mittags gefüllt (4 Beiträge + 5 Storys, freigegeben) ([`c51436c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c51436c692282d1790af1cd8a1e7beb48de61bb6))
  - Plan: neu `28-reel-zuschlaege` (2026-10-19 11:45, freigegeben); neu `28-story-quiz` (2026-10-19 12:15, freigegeben); neu `29-karussell-verluste` (2026-10-20 11:45, freigegeben); neu `29-story-teaser` (2026-10-20 12:15, freigegeben); neu `28-story-aufloesung` (2026-10-20 17:50, freigegeben); neu `30-reel-gwg` (2026-10-21 11:45, freigegeben); neu `30-story-quiz` (2026-10-21 12:15, freigegeben); neu `31-karussell-zinsschranke` (2026-10-22 11:45, freigegeben); neu `30-story-aufloesung` (2026-10-22 17:50, freigegeben)
- 23:35 📈 Statistik: keine Doppelläufe mehr, Zeitzonen sicher, neue Kennzahlen + Wochenziele ([`7e21f3e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7e21f3e46681926d58cd731c6c11b820c861e84e))
  - `.github/workflows`, `automatik/insights_voll.py`, `automatik/radar.py`, `automatik/tagesbericht.py`, `automatik/wochenbericht.py`
- 23:35 ✍️ Lage: 30-Sekunden-Briefing, 7-Tage-Kachel, Testmonat je KW, freie Slots; Routine-Prompts neu ([`40e4b81`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/40e4b81b9cf066267004de35296f613cb000b22b))
  - `.claude/skills/lage/SKILL.md`, `automatik/lage.py`, `automatik/lage_html.py`, `automatik/routinen`
- 23:34 🤖 Autopilot: kein Doppel-Post mehr, Teaser nur nach Feed-Beitrag, Takt-Wächter ([`18b7d14`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/18b7d1481b4a7fc60e3b5ef71b1337feeacf6d31))
  - `automatik/posten.py`, `automatik/tests`, `automatik/waechter.py`
- 23:26 ✍️ Bio-/Profil-Vorschlag 14.10.: Nutzen-Bio, Namensfeld, Pins, Highlights (braucht Loris in der App) ([`0a8f9f2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0a8f9f217615061add684e67a775935ba5896007))
  - `strategie/02_bio_highlights.md`
- 23:24 ✍️ Nachtlauf 1: anstehende Beiträge optimiert (Texte, Titelbilder, Fachkorrekturen) ([`f0009be`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f0009bea8b43bbb09695fbefabfe592304948e3e))
  - `LAGE.html`, `automatik/plan.json`, `posts/01_2026-10-04_reel_ampel`, `posts/03_2026-10-13_gewst_hinzurechnung`, `posts/04_2026-10-20_reel_mein_weg`, `posts/09_2026-10-15_rueckstellung`, `…`
- 23:09 ✍️ Lage nach Rebase neu erzeugt ([`41f3298`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/41f3298f33034864fee374590869ad749ae08a19))
  - `LAGE.html`
- 23:08 ✍️ Postzeiten vor die Follower-Welle gelegt: Feed 11:45/17:45, Storys 12:15/17:50 ([`52a273d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/52a273d4fc78d6c90705f304a38708e1aebd92ac))
  - Plan: `09-story-quiz` zeit: 2026-10-14 12:45 → 2026-10-14 12:15; `07-reel-hinzurechnung` zeit: 2026-10-14 19:30 → 2026-10-14 17:45; `09-rueckstellung` zeit: 2026-10-15 12:15 → 2026-10-15 11:45; `09-story-teaser` zeit: 2026-10-15 12:45 → 2026-10-15 12:15; `16-reel-listen` zeit: 2026-10-15 19:30 → 2026-10-15 17:45; `09-story-aufloesung` zeit: 2026-10-15 19:35 → 2026-10-15 17:50; `03-story-aufloesung` zeit: 2026-10-16 12:45 → 2026-10-16 12:15; `04-reel-mein-weg` zeit: 2026-10-16 19:30 → 2026-10-16 17:45; `04-story-teaser` zeit: 2026-10-16 19:35 → 2026-10-16 17:50; `01-reel-ampel` zeit: 2026-10-17 12:15 → 2026-10-17 11:45; `01-story-teaser` zeit: 2026-10-17 12:45 → 2026-10-17 12:15; `18-reel-aufbewahrung` zeit: 2026-10-19 19:30 → 2026-10-19 17:45; `19-reel-verlustvortrag` zeit: 2026-10-20 19:30 → 2026-10-20 17:45; `20-reel-erechnung` zeit: 2026-10-21 19:30 → 2026-10-21 17:45; `10-story-umfrage` zeit: 2026-10-22 12:45 → 2026-10-22 12:15; `21-reel-zinsschranke` zeit: 2026-10-22 19:30 → 2026-10-22 17:45; `10-e-rechnung` zeit: 2026-10-23 19:30 → 2026-10-23 17:45; `10-story-teaser` zeit: 2026-10-23 19:35 → 2026-10-23 17:50; `17-reel-kommentare` zeit: 2026-10-24 19:30 → 2026-10-24 17:45; `22-reel-steuersatz` zeit: 2026-10-26 19:30 → 2026-10-26 17:45
- 23:00 ✍️ Lage nach Rebase neu erzeugt ([`0e1e645`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0e1e645cca01cbf14e1ea428881e8a819c976b5e))
  - `LAGE.html`
- 23:00 ✍️ Konflikte Testmonat entschieden: Ampel mittags, Steuersatz KW 44, Notlösung ohne Stimme ([`c3eca9c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c3eca9cf94b92f497e19a71aafa60a91a82a18c2))
  - Plan: `01-reel-ampel` zeit: 2026-10-17 19:30 → 2026-10-17 12:15; `01-story-teaser` zeit: 2026-10-17 19:35 → 2026-10-17 12:45; `22-reel-steuersatz` zeit: 2026-10-18 19:30 → 2026-10-26 19:30
- 19:35 🤖 Autopilot: 23-story-biolink veroeffentlicht ([`204f1d7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/204f1d70261c50bc2559a49982e0fef940b4383d))
  - Plan: `23-story-biolink` status: freigegeben → veroeffentlicht; `23-story-biolink` online: https://www.instagram.com/stories/maehrsteuern/4007178310619152901
- 19:31 🤖 Autopilot: Dateien fuer 23-story-biolink vorbereitet ([`2b08c21`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2b08c218c4d03a69acf66d9f578689214574d60d))
  - `posts/23_2026-10-13_story_biolink`
- 19:31 🤖 Autopilot: 15-reel-rechnungsnummern veroeffentlicht ([`36bff2a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/36bff2afc1ace31d7a1c1b785d5bd05c0bab19b2))
  - Plan: `15-reel-rechnungsnummern` status: freigegeben → veroeffentlicht; `15-reel-rechnungsnummern` online: https://www.instagram.com/reel/DecWVZwgpOC/
- 18:15 🤖 Autopilot: Dateien fuer 15-reel-rechnungsnummern vorbereitet ([`a2c8f67`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a2c8f676db4a7c63146be7aa5d0ecbe0996ea667))
  - `posts/15_2026-10-13_reel_rechnungsnummern`
- 16:37 📈 Statistik 2026-10-13 ([`389b189`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/389b189ccd95b7d8d5d483276d6acc1ad993ebc1))
  - `automatik/statistik`
- 14:45 📡 Radar 2026-10-13: 8 Beiträge, 0 DM-Entwürfe ([`4c4f55c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4c4f55cbd80075d4604bb0c366ef30300e6083ca))
  - `automatik/interaktion`
- 12:45 🤖 Autopilot: 03-story-teaser veroeffentlicht ([`aa973e5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/aa973e51d0cd18c5ff91da89325a0375abcd464b))
  - Plan: `03-story-teaser` status: freigegeben → veroeffentlicht; `03-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4006971953613492167
- 12:17 🤖 Autopilot: Dateien fuer 03-story-teaser vorbereitet ([`eca6cff`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/eca6cff46d2077fc3d774e3ff295a2c4c09db417))
  - `posts/03_2026-10-13_gewst_hinzurechnung`
- 12:16 🤖 Autopilot: 03-gewst-hinzurechnung veroeffentlicht ([`dfac075`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/dfac0756f1bd1514cea26f14c6acd201ac3f7dcf))
  - Plan: `03-gewst-hinzurechnung` status: freigegeben → veroeffentlicht; `03-gewst-hinzurechnung` online: https://www.instagram.com/p/Debkp_3m1WY/
- 11:01 🤖 Autopilot: Dateien fuer 03-gewst-hinzurechnung vorbereitet ([`609c5b4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/609c5b4784405e3c49790c800bf081fd3e025a0d))
  - `posts/03_2026-10-13_gewst_hinzurechnung`
- 10:55 ✍️ LAGE aktualisiert nach Tagesbericht 13. Oktober ([`326e3e4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/326e3e4f5061f5c8d1797cd06df9001ff8bb4520))
  - `LAGE.html`
- 10:55 ✍️ Tagesbericht 13. Oktober: Hook-Rate zu hoch, Videos zu lang, Bio-Link schläft ([`f0dbf0a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f0dbf0a3e06801145ff36869a21138e92dfc134b))
  - `automatik/berichte`
- 08:48 📈 Statistik 2026-10-13 ([`f6f52ee`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f6f52eed533bd742bf7888e67ff524d93cd9ec57))
  - `automatik/statistik`
- 07:07 📡 Radar 2026-10-13: 8 Beiträge, 0 DM-Entwürfe ([`84b20f9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/84b20f9b44b56d10b2287d315441083a7b7827f7))
  - `automatik/interaktion`

**Mo 12.10.2026**
- 19:30 🤖 Autopilot: 14-reel-versionen veroeffentlicht ([`b6160e3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b6160e35e81e4273979114637d5437be4d307840))
  - Plan: `14-reel-versionen` status: freigegeben → veroeffentlicht; `14-reel-versionen` online: https://www.instagram.com/reel/DeZxf9AEy9p/
- 18:15 🤖 Autopilot: Dateien fuer 14-reel-versionen vorbereitet ([`69246e2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/69246e2f709d1285c3b4f1315b6d9497b1b591b3))
  - `posts/14_2026-10-12_reel_versionen`
- 18:08 📈 Statistik 2026-10-12 ([`c4d1931`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c4d19313a4ec1c09b38b20f0fd5afd83d3ed048d))
  - `automatik/statistik`
- 15:12 📡 Radar 2026-10-12: 8 Beiträge, 0 DM-Entwürfe ([`e4b3e32`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e4b3e32cec354f1fbee284a61436f147b380f5f4))
  - `automatik/interaktion`
- 12:45 🤖 Autopilot: 03-story-quiz veroeffentlicht ([`020ed0c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/020ed0ca6c3d1267b189f6a86ae608aa4a0d0022))
  - Plan: `03-story-quiz` status: freigegeben → veroeffentlicht; `03-story-quiz` online: https://www.instagram.com/stories/maehrsteuern/4006247183418785188
- 11:40 ✍️ Lage nach Autopilot-Lauf neu erzeugt ([`1d27acd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1d27acd2dd0e8baf2508c8c9b79be9c0ab35e4bb))
  - `LAGE.html`
- 11:40 ✍️ Ampel-Reel auf 15 s gekürzt, Frage-Story als Tipp-Version ([`5e5c68d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5e5c68d880d4ea6772bdc169f44f7c96ec1de03f))
  - `LAGE.html`, `automatik/plan.json`, `posts/01_2026-10-04_reel_ampel`, `strategie/13_backlog.md`, `vorlagen/system/schnitt/p01_reel_ampel_kurz.json`, `vorlagen/system/schnitt/p01_reel_ampel_kurz_bauen.py`
- 11:30 🤖 Autopilot: Dateien fuer 03-story-quiz vorbereitet ([`2c882cc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2c882ccfdc84da6a62fa05142789937cd0ee3196))
  - `posts/03_2026-10-13_gewst_hinzurechnung`
- 09:42 ✍️ Tagesbericht 12.10. (Ersatz für den Routine-Lauf) ([`c80bb3d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c80bb3daa188cb22fd652e164a28eda92f7e2df0))
  - `automatik/berichte`, `automatik/statistik`
- 08:49 📈 Statistik 2026-10-12 ([`409095e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/409095efb20fab0777eca83916c58751c4f9e414))
  - `automatik/statistik`
- 07:04 📡 Radar 2026-10-12: 8 Beiträge, 0 DM-Entwürfe ([`4502ea7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4502ea74317a7d152fe9bbec006880bb2f53a623))
  - `automatik/interaktion`

**So 11.10.2026**
- 19:30 🤖 Autopilot: 13-reel-verknuepfung veroeffentlicht ([`6574fbf`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6574fbf8cdb937ab8dfe8d92eb5651957108939b))
  - Plan: `13-reel-verknuepfung` status: freigegeben → veroeffentlicht; `13-reel-verknuepfung` online: https://www.instagram.com/reel/DeXMtEnDn3I/
- 18:15 🤖 Autopilot: Dateien fuer 13-reel-verknuepfung vorbereitet ([`e614761`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e614761f9a5cb84ed2431b4048bbaf70c2d23795))
  - `posts/13_2026-10-11_reel_verknuepfung`
- 18:02 ✍️ Wochenbericht KW 2026-41 ([`36fba34`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/36fba34b680db5d5a8e921a37b9940ec8b256e6b))
  - `automatik/statistik`
- 15:33 📈 Statistik 2026-10-11 ([`47f6bbd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/47f6bbd047525bd94869e79ea3c6a0ef58f1ddd7))
  - `automatik/statistik`
- 13:25 📡 Radar 2026-10-11: 8 Beiträge, 0 DM-Entwürfe ([`38b03af`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/38b03af8ea3a9247fa4a55c0a401933958834c09))
  - `automatik/interaktion`
- 12:15 🤖 Autopilot: 08-story-rueckblick veroeffentlicht ([`13ef768`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/13ef768c61c88308d4738e7b9ec5e92b53765591))
  - Plan: `08-story-rueckblick` status: freigegeben → veroeffentlicht; `08-story-rueckblick` online: https://www.instagram.com/stories/maehrsteuern/4005507302220849298
- 11:01 🤖 Autopilot: Dateien fuer 08-story-rueckblick vorbereitet ([`a937cc1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a937cc1d7924d3f46a81914363925b5b086ea9b6))
  - `posts/08_2026-10-09_reel_kst_staffel`
- 10:41 ✍️ LAGE.md aktualisiert nach Tagesbericht 11.10. ([`7d7cc99`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7d7cc9924497d99ce774a2197d09db91ed9ffc07))
  - `LAGE.html`
- 10:40 ✍️ Tagesbericht 11. Oktober: 361 Follower, Reichweite +159 %, Hook-Quote über Ziel ([`480fc40`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/480fc40b12a8bf1a93238664474b3e015e31a5d3))
  - `automatik/berichte`
- 10:12 ✅ Freigabe #54: go ([`a926d0d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a926d0d27a345a16f6987409129b085fcf620733))
  - Plan: `23-story-biolink` status: entwurf → freigegeben
- 09:27 ✅ Freigabe angefragt (1 Beitrag/Beiträge) ([`07a2aec`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/07a2aec36a8a1ef298e471937f113aa249907473))
  - Plan: `23-story-biolink` → Freigabe-Issue #54
- 09:26 ✍️ Testmonat 2 pro Tag, Sprechtexte 18–22, Story-Formate, Auswertung 11.10. ([`1acbd03`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1acbd030b10692c45c7a9ba058f72024eced1f92))
  - Plan: neu `23-story-biolink` (2026-10-13 19:35, entwurf); neu `22-reel-steuersatz` (2026-10-18 19:30, wartet_auf_sprachnachricht); neu `18-reel-aufbewahrung` (2026-10-19 19:30, wartet_auf_sprachnachricht); neu `19-reel-verlustvortrag` (2026-10-20 19:30, wartet_auf_sprachnachricht); neu `20-reel-erechnung` (2026-10-21 19:30, wartet_auf_sprachnachricht); neu `21-reel-zinsschranke` (2026-10-22 19:30, wartet_auf_sprachnachricht); `03-story-quiz` zeit: 2026-10-12 12:15 → 2026-10-12 12:45; `03-gewst-hinzurechnung` zeit: 2026-10-13 12:30 → 2026-10-13 12:15; `03-story-teaser` zeit: 2026-10-13 12:35 → 2026-10-13 12:45; `09-story-quiz` zeit: 2026-10-14 12:15 → 2026-10-14 12:45; `09-rueckstellung` zeit: 2026-10-15 12:30 → 2026-10-15 12:15; `09-story-teaser` zeit: 2026-10-15 12:35 → 2026-10-15 12:45; `09-story-aufloesung` zeit: 2026-10-15 12:15 → 2026-10-15 19:35; `03-story-aufloesung` zeit: 2026-10-16 12:15 → 2026-10-16 12:45; `10-story-umfrage` zeit: 2026-10-22 12:15 → 2026-10-22 12:45
- 09:19 ✍️ Reels 13–16 auf 12–15 s gekürzt (Pointe in den ersten 5 s) ([`ab29fc7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ab29fc72493fa83e4e4f965d6c23cd9d6a1da7a2))
  - Plan: `06-reel-split` status: manuell → veroeffentlicht; `06-reel-split` online: https://www.instagram.com/reel/DePeYymNG2K/
- 09:19 ✍️ Tagesbericht: Reel-Länge, Soll-Ist, Skip-Verlauf, Shares-Hinweis, 1620 px ([`9c2a71c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9c2a71c0e06cc283c105633c046f8e264d753f5d))
  - `automatik/berichte`, `automatik/insights_voll.py`, `automatik/tagesbericht.py`
- 08:48 📈 Statistik 2026-10-11 ([`dd8e4a6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/dd8e4a65d1436f9e3b0bd75cc599956fe798b940))
  - `automatik/statistik`
- 07:04 📡 Radar 2026-10-11: 8 Beiträge, 0 DM-Entwürfe ([`ee909ef`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ee909efeab6ddaf414905244f8d0806eab3e0b05))
  - `automatik/interaktion`

**Sa 10.10.2026**
- 19:30 🤖 Autopilot: 08-reel-kst-staffel veroeffentlicht ([`041fcea`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/041fceacb928f14ba8df2f9d570f34a8e2edc64c))
  - Plan: `08-reel-kst-staffel` status: freigegeben → veroeffentlicht; `08-reel-kst-staffel` online: https://www.instagram.com/reel/DeUn6ezCm7O/
- 18:15 🤖 Autopilot: Dateien fuer 08-reel-kst-staffel vorbereitet ([`bbd22ff`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/bbd22ff491314c97dec0ea9880c4e3bac0c461a8))
  - `posts/08_2026-10-09_reel_kst_staffel`
- 15:05 📈 Statistik 2026-10-10 ([`57d1b40`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/57d1b404960569c6724f844949ada2ac15ebffe5))
  - `automatik/statistik`
- 13:16 💼 LinkedIn-Pakete: 09-rueckstellung ([`10b1b91`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/10b1b91681b38af05562d6c99af8a85325d7c99e))
  - `posts/09_2026-10-15_rueckstellung`
- 13:15 📡 Radar 2026-10-10: 8 Beiträge, 0 DM-Entwürfe ([`ecdf71d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ecdf71d080677edf09128a606ebd01b3323139b5))
  - `automatik/interaktion`
- 12:15 🤖 Autopilot: 08-story-heute veroeffentlicht ([`b09078d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b09078d60f4514c2962e5a6ddedfb6400e3659b0))
  - Plan: `08-story-heute` status: freigegeben → veroeffentlicht; `08-story-heute` online: https://www.instagram.com/stories/maehrsteuern/4004782529098566867
- 11:46 🔀 Merge pull request #50 from maehrsteuern/claude/focused-shannon-hrtyy7 ([`fa67d29`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fa67d290f19e81882a67906341bed9da92828103))
- 11:46 ✍️ Rückstellung-Karussell freigegeben, Ampel-Reel auf Sa 17.10., Link Test-Reel Nr. 2 ([`b4fc245`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b4fc2454d57236226eb562bfb593be78620711b4))
  - Plan: `12-reel-zeile` online: https://www.instagram.com/reel/DeTiK24NyJt/; `09-story-quiz` status: entwurf → freigegeben; `09-story-aufloesung` status: entwurf → freigegeben; `09-rueckstellung` status: entwurf → freigegeben; `09-story-teaser` status: entwurf → freigegeben; `01-reel-ampel` status: pause → freigegeben; `01-reel-ampel` zeit: 2026-10-04 19:30 → 2026-10-17 19:30; `01-story-teaser` status: pause → freigegeben; `01-story-teaser` zeit: 2026-10-04 19:35 → 2026-10-17 19:35
- 11:01 🤖 Autopilot: Dateien fuer 08-story-heute vorbereitet ([`c6d602e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c6d602e6110a14075d724525a984fbb33a6e4053))
  - `posts/08_2026-10-09_reel_kst_staffel`
- 09:32 🔀 Merge pull request #49 from maehrsteuern/claude/focused-shannon-hrtyy7 ([`4ab6262`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4ab6262832d5f81f384cee0ebf256e8d5713f65d))
- 09:32 ✍️ Reels wieder im Original-Takt und per Autopilot (ab Sa 10.10. Steuersatz) ([`2070594`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2070594b5722f05e345dae6a175ac839d2590c13))
  - Plan: `12-reel-zeile` status: manuell → veroeffentlicht; `12-reel-zeile` zeit: 2026-10-10 19:30 → 2026-10-10 09:30; `08-story-heute` zeit: 2026-10-11 12:15 → 2026-10-10 12:15; `08-reel-kst-staffel` status: manuell → freigegeben; `08-reel-kst-staffel` zeit: 2026-10-11 19:30 → 2026-10-10 19:30; `08-story-rueckblick` zeit: 2026-10-12 18:00 → 2026-10-11 12:15; `13-reel-verknuepfung` status: manuell → freigegeben; `13-reel-verknuepfung` zeit: 2026-10-12 19:30 → 2026-10-11 19:30; `14-reel-versionen` status: manuell → freigegeben; `14-reel-versionen` zeit: 2026-10-13 19:30 → 2026-10-12 19:30; `15-reel-rechnungsnummern` status: manuell → freigegeben; `15-reel-rechnungsnummern` zeit: 2026-10-14 19:30 → 2026-10-13 19:30; `07-reel-hinzurechnung` zeit: 2026-10-15 19:30 → 2026-10-14 19:30; `04-story-frage` zeit: 2026-10-16 18:00 → 2026-10-15 18:00; `16-reel-listen` status: manuell → freigegeben; `16-reel-listen` zeit: 2026-10-16 19:30 → 2026-10-15 19:30; `04-reel-mein-weg` status: manuell → freigegeben; `04-reel-mein-weg` zeit: 2026-10-17 19:30 → 2026-10-16 19:30; `04-story-teaser` zeit: 2026-10-17 19:35 → 2026-10-16 19:35
- 09:19 🔀 Merge pull request #48 from maehrsteuern/claude/focused-shannon-hrtyy7 ([`5a6d081`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5a6d08150d964aa7e6bb5e76b3eede7ec4bf49db))
- 09:19 🔀 Merge claude/instagram, Lage neu erzeugt ([`964450c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/964450c11edb00b8b9c7c38f88299b3dc58d7545))
- 09:10 ✍️ Reel Nr. 2 neu geschnitten (300|Zeilen), heute 19:30 – alle Folge-Reels +1 Tag ([`0ea2834`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0ea283465021259909da6e7e4b591b1f10eca388))
  - Plan: `12-reel-zeile` zeit: 2026-10-09 19:30 → 2026-10-10 19:30; `08-story-heute` zeit: 2026-10-10 12:15 → 2026-10-11 12:15; `08-reel-kst-staffel` zeit: 2026-10-10 19:30 → 2026-10-11 19:30; `08-story-rueckblick` zeit: 2026-10-11 12:15 → 2026-10-12 18:00; `13-reel-verknuepfung` zeit: 2026-10-11 19:30 → 2026-10-12 19:30; `14-reel-versionen` zeit: 2026-10-12 19:30 → 2026-10-13 19:30; `15-reel-rechnungsnummern` zeit: 2026-10-13 19:30 → 2026-10-14 19:30; `07-reel-hinzurechnung` zeit: 2026-10-14 19:30 → 2026-10-15 19:30; `04-story-frage` zeit: 2026-10-15 18:00 → 2026-10-16 18:00; `16-reel-listen` zeit: 2026-10-15 19:30 → 2026-10-16 19:30; `04-reel-mein-weg` zeit: 2026-10-16 19:30 → 2026-10-17 19:30; `04-story-teaser` zeit: 2026-10-16 19:35 → 2026-10-17 19:35
- 08:49 📈 Statistik 2026-10-10 ([`5fd657b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5fd657b3c7b3798ffd911c6e243dc193a231de35))
  - `automatik/statistik`
- 07:04 📡 Radar 2026-10-10: 8 Beiträge, 0 DM-Entwürfe ([`f626328`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f626328688858f48feed9c8023210206cf3929a6))
  - `automatik/interaktion`

**Fr 09.10.2026**
- 15:47 📈 Statistik 2026-10-09 ([`79346c6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/79346c66cf32cc4fb3a54b81827749e3e7b01bbe))
  - `automatik/statistik`
- 13:56 📡 Radar 2026-10-09: 8 Beiträge, 0 DM-Entwürfe ([`6837bf4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6837bf4cc8cc9607c1938351b4a04f397df157cf))
  - `automatik/interaktion`
- 12:35 🤖 Autopilot: 05-story-teaser veroeffentlicht ([`ff09f34`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ff09f3462a5439fd1a77b18400d1e643ba27b88f))
  - Plan: `05-story-teaser` status: freigegeben → veroeffentlicht; `05-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4004067818916764813
- 12:32 🤖 Autopilot: Dateien fuer 05-story-teaser vorbereitet ([`606887a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/606887a622f73b7997e3b21789fe055ca873777f))
  - `posts/05_2026-10-08_latente_steuern`

</details>
