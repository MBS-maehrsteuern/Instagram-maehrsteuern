# 🧭 Lage – maehrsteuern auf Instagram

_Automatisch erzeugt von `automatik/lage.py` – nicht von Hand bearbeiten (Notizen: `automatik/lage_notizen.md`). Stand: letzte Änderung Mi 28.10. 06:23 Uhr._

## ⏱️ 30-Sekunden-Briefing

- **Heute online:** 🟡 12:15 📱 Story `39-story-quiz` (pausiert) · 🟢 12:15 📱 Story `meme1-story` (läuft automatisch) · 🟢 17:45 🎬 Reel `i14-reel-insider-ferrari` (läuft automatisch) · 🟡 17:50 📱 Story `40-story-teaser` (pausiert)
- **Braucht dich:** nichts 🎉
- **Letzte 7 Tage:** Reichweite **2149** (20.10.–26.10., +51 % zur Vorwoche) · Follower **+9** (jetzt 377) · 30 Tage: +34 Follows / −11 entfolgt
- **Testmonat** (Tag 17/28, Soll 7 Feed/Woche, täglich ≥ 1 Reel):
  - 🟡 **KW 44** (26.10.–01.11.) ← jetzt: Feed **7/7** (2 online · 5 geplant) · Reel-Tage (sicher) **6/7** – ohne Reel: So 01.11.
  - 🟡 **KW 45** (02.11.–08.11.): Feed **7/7** (0 online · 7 geplant) · Reel-Tage (sicher) **5/7** – ohne Reel: Mi 04.11., So 08.11.
- **Freie Slots nächste 7 Tage:** keine

**Als Nächstes online:** 📱 Story `meme1-story` am **Mi 28.10. 12:15 Uhr** – 🟢 freigegeben (geht automatisch online)

## 📝 Gerade in Arbeit

- **Motion-Wissen 26.10.:** `strategie/20_wissen_motion.md` – 14 Effekte mit Einsatzregel, Baukasten `vorlagen/system/premium/motion.js`; Karussell-Vorlage kann jetzt „Der alte Weg“, „Vorher · Nachher“, Mono-Box (Formel/Musterformulierung) und Speichern-Hinweis auf Folie 1. Idee: Serie „Steuer-Spickzettel“.
- **Takt ab 26.10. (Loris 25.10. nach Auswertung):** 1 Feed-Beitrag/Tag um 17:45 – Reel täglich, Karussell statt Reel Mi + So. Grund: an Tagen mit 2–3 Beiträgen Ø ~180 statt ~440 Aufrufe (`19_wissen` Abschnitt 7). Plan steht bis 16.11. (Reels) bzw. 02.12. (Karussells); ab 17.11. braucht es neue Reels (Aufnahmen!).
- **Stand 25.10. (Sitzung mit Loris):**
  - **Premium-Look** (Loris' Design-Screenshots @herr_tech, eigene Markenfarben): Baukasten `vorlagen/system/premium/` (HTML-Animation → `rendern.mjs` → `reel_bauen.py` mit Stimme + `sfx.py` Sounddesign). Erstes Reel: 34 Einspruch v3 (Hook Kalender 05→09 „4 Tage länger“, Szenenwechsel alle 2,5–4 s, CTA „Kommentiere TOOL“). Wartet auf go (Vorschlag So 17:45). Danach alle Reels/Karussells in diesem Look.
  - **17 Reels mit Stimme** neu gebaut (24.10.), alle pausiert. Gläsern-Reel postet Loris So 11:45 selbst.
  - **Sound-Bibliothek:** 111 Musikstücke (12 alt + 39 Runway `musik/runway/` + 60 CC0 `musik/cc0/`), 103 Töne (3 alt + 60 Runway `musik/atmo/runway/` + 40 CC0 `musik/atmo/cc0/`). Quellen/Kataloge: `musik/QUELLEN_*.md`, `musik/katalog_*.json`. CC0-Musik 237–242 auf Vocals anhören; CC0-Töne eher Retro → Runway-Töne bevorzugen. Runway-Stand ~399 Credits.
- **Stand 24.10. vormittags (Sitzung mit Loris, go 1–3):**
  - **Neues Wissen verbindlich:** `strategie/19_wissen_2026-10-24.md` – „Boring Content“: eine Idee pro Beitrag, einfache Wörter, festes Format, Pointe in 2 s, **4-Sekunden-Test vor jeder Freigabe**.
  - **Online:** Reel 36 Bewirtung umgebaut („0 %“ ab Frame 1, Caption kurz) und Sa 24.10. ~11:02 per Sofort-Lauf gepostet (Branch `ccr-8ce2ce66-8i2ful`). Tipp-Story 12:15 wird per Sofort-Lauf nachgeschoben. Paragraf-Formel → Mo 26.10.
  - **Umbau aller pausierten Feed-Beiträge** (32) nach Wissen 24.10. läuft; bleibt `pausiert`, bis Loris die Vorschau freigibt. Danach Branch nach `claude/instagram` übernehmen (Autopilot plant nur von dort).
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
- **Benachrichtigungen repariert (25.10.):** Radar-, Kommentar-, Freigabe-, LinkedIn-, Wächter- und Wochenbericht-Issues erwähnten `@MBS-maehrsteuern` (Organisation → niemand wird benachrichtigt). Jetzt `@maehrsteuern` (änderbar per Env `GH_MELDEN`). Greift ab dem nächsten Lauf; in GitHub unter Settings → Notifications muss „Participating, @mentions“ an sein.
- **Radar-Nachträge (03.10.):** Meta-Drosselung (429/Code 4, 17, 32, 613) → Backoff 30/90/270 s, bei anhaltender Drosselung wird abgebrochen. Gedrosselte oder kurz gestörte Konten landen nicht mehr als 🧹 „nicht abrufbar“ in der Pflege; aufgeräumt werden nur dauerhaft kaputte Konten oder Konten ohne Beitrag seit 30 Tagen (montags, nur abgehakt). Art neuer Konten wird auch aus Wörtern wie „Steuerberaterin“, „Prüfung“, „Akademie“ erkannt; fehlende oder unbekannte Art erscheint als Hinweis im Radar-Issue.
- **Fristen** (`automatik/erinnerungen.json` → „Braucht dich“ + Kalender): LinkedIn #18 Mi 07.10. 08:00 (Termin kommt schon automatisch) · Reel-Vergleich „5 Dinge“/Split → Anzeigen-Start ca. Mo 12.10. (Chrome Modul 2 am 04.10. nur vorbereiten) · **ManyChat-Trial endet Fr 16.10.** → Entscheidung Loris (Erinnerung Mi 14.10.).
- **Meta-App „maehrsteuern Autopilot“** bleibt im Entwicklungsmodus. Die laufenden IG-Schlüssel und die Statistik sind davon nicht betroffen (eigenes Konto mit App-Rolle). Nur die Hashtag-Suche braucht die Freigabe → Checkliste [#26](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/issues/26).
- **Reclaim-Hinweis:** Claudes Reclaim-Zugang (Connector) zeigt auf **Konto B (Outlook, Lite)**, nicht auf das Demo-Konto. Für die Automatik nicht nutzen; Demo-Buchungen kommen nur über das Apps-Script „maehrsteuern Demo-Kopie“.
- **Bibliothek aus dem Brand Kit (Claude Design) gebaut (02.10.):** 365 fertige Bilder in `assets/bibliothek/` (Übersicht `README.md` dort), Texte als Job-Dateien in `vorlagen/system/jobs/bibliothek/`. Neue Vorlagen `zahl.html` + `banner.html`, Highlight-Symbole, Vergleichstabelle/Checkliste im Karussell. Nichts davon ist eingeplant. **Gegengelesen (05.10.):** 10 Fehler korrigiert, 25 Zweifelsfälle mit Loris entschieden und umgesetzt → `assets/bibliothek/PRUEFBERICHT.md`. Offen nur: Zinsschranke-Caption mit Hinweis auf Untergang des Zinsvortrags. **Erste Bibliothek-Beiträge eingeplant (05.10., als Entwurf → Freigabe-Issue):** Rückstellung in 6 Schritten Do 15.10. (Quiz SolZ Mi 14.10., Auflösung Do 15.10. 12:15, Teaser 19:35) · E-Rechnung-Fahrplan Do 22.10. (Umfrage Mi 21.10., Teaser 19:35). Content-Fabrik: diese Slots sind belegt. **Runde 4 ergänzt (05.10.):** +217 Bilder (jetzt 582) – GmbH/Gesellschafter, Bilanz, USt, Lohn, ErbSt/GrESt, Paragraf als Formel, Steuerkalender, GoBD, Mythos/Glossar Teil 2, Einzelposts, Storys, Reel-Titel, Einblendungen, Highlights, Ampeln (`r4_*.json`), nichts eingeplant. 6 Korrekturen vor dem Rendern, 4 Zweifelsfälle + Platzhalter „312 Testfälle“ / § 8c-Quoten 48/62 % offen → Prüfbericht Abschnitt „Runde 4“. **Runde 7 (07.10.):** 14 MBS-Reel-Bilder (10 Titel `reels/mbs_*`, 4 Einblendungen `bausteine/mbs_*`, Abspann „Demo buchen“), `einblendung.html` kann jetzt `chip`/`kicker` im Abspann. **Runden 5+6 (07.10.):** +400 Bilder (jetzt 996) – Kleinunternehmer, Firmenwagen, Gebäude-AfA, USt-Sätze, Minijob/Reisekosten 2026, Grundwerte 2026, Kapitalerträge, Vermietung, AO-Fristen, OSS u. a. 10 Korrekturen, 32 Umbenennungen gegen Überschreiben, Zweifelsfälle → Prüfbericht „Runden 5 und 6“.
- **Lage als Seite (04.10.):** `LAGE.html` mit Kacheln, Kalender, Diagrammen und filterbarem Protokoll, wird mit LAGE.md neu geschrieben und über GitHub Pages veröffentlicht (https://maehrsteuern.github.io/Instagram-maehrsteuern/). Pages eingeschaltet ✓ (04.10.), Seite läuft und aktualisiert sich bei jeder neuen Lage automatisch.
- **Nach jedem Post, innerhalb von 30 Min. (von Hand in der App, Quelle `strategie/18_wissen_2026-10-21.md` Abschnitt 4):** den automatischen ersten Kommentar **anheften** · eigenen Beitrag **liken und speichern** · in der **Story teilen** · **Kommentare unter dem vorigen Beitrag liken** · **jeden Kommentar beantworten**. Den Kommentar setzt `posten.py` selbst, wenn `posts/<ordner>/erster_kommentar.txt` existiert (Feed-Beiträge, nicht Storys; ID als `erster_kommentar_id` im Plan; Fehler = nur Warnung).
- 26.10. abends: Ton aller Stimm-Reels neu (beide Handy-Mikros per Frequenzweiche statt Stereo→Mono – war dumpf; Loris: „perfekt“).
  Wissen 21 (Trichter oben/mitte/unten, Ziel Follower 15/7/8): Reihenfolge ab 27.10. gemischt, Feld `trichter` im Plan.
  Offen: Story-Sprechtexte (Mitte) für Aufnahme 07.11.; GitHub-Zeitplan unzuverlässig → 17:20-Check per Erinnerung.
- 27.10.: Mein Weg #01 (Foto-Montage Diplomierung, 18:00) eskaliert: 1.182 Aufrufe in ~7 h, 91 % Nicht-Follower (Wissen 21 §8).
  Plan: Mi 28.10. Insider #14 Ferrari (statt K41 → 06.12.), Do 29.10. Mein Weg #02 (statt i09 → 05.12.), i05 → 04.12.
  Insider #13 Betriebsprüfung gebaut, noch nicht eingeplant. Offen: Bio-Umbau (Loris), S4 neu einsprechen.

## 👉 Braucht dich

- Nichts offen. 🎉

## ⏭️ Nächste 7 Tage

| Wann | Was | Status | Hinweis |
|---|---|---|---|
| Mi 28.10. 12:15 | 📱 Story `39-story-quiz` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R4 gegengelesen): quiz_holding als Emoji-Tipp neu gerendert (👏 = rund 1,5 % · 😮 = rund 30 %, richtig: 👏), statt „Antworte in Prozent“; Auflösung im Bild: „Die Antwort steht im neuen Reel“ (Reel 39 lief um 11:45). Keine Auflösungs-Story: Do 29.10. 12:15/17:50 sind von Agent c2 belegt (story_do_tipp Mythen, story_do_teaser AfA). Optional in der App Quiz-Sticker setzen. |
| Mi 28.10. 12:15 | 📱 Story `meme1-story` | 🟢 freigegeben (geht automatisch online) | 28.10.: eigenes Steuer-Meme (FINANZAMT – passt zu Insider #14 Ferrari), Story statt Feed (zählt nicht gegen 1 Feed-Beitrag/Tag). Loris: „memes humorvoll als fertige Beiträge“. |
| Mi 28.10. 17:45 | 🎬 Reel `i14-reel-insider-ferrari` | 🟢 freigegeben (geht automatisch online) | 27.10.: Insider #14 (Stimme 27.10.), Thema aus Vorbilder-Radar; ersetzt Karussell 41 am Mi (Loris: „alle Punkte umsetzen“). |
| Mi 28.10. 17:50 | 📱 Story `40-story-teaser` | pausiert | 14.10. Nachtlauf: aus Bibliothek Teaser „Jetzt neu im Profil“ zum Formel-Reel (Titelbild), jobs/p40_reel_formeln.json. |
| Do 29.10. 12:15 | 📱 Story `41-story-tipp` | pausiert | 14.10. Nachtlauf: Emoji-Tipp „Gewerbesteuer ist keine Betriebsausgabe“ (§ 4 Abs. 5b EStG) mit Verweis auf das Karussell, 👏/😮, ohne Auflösung nötig (jobs/p41_mythen.json). storys/frage_mythen nicht genutzt (offene Frage). |
| Do 29.10. 12:15 | 📱 Story `meme2-story` | 🟢 freigegeben (geht automatisch online) | 28.10.: eigenes Steuer-Meme (MEIN WEG – passt zu Mein Weg #02), Story statt Feed (zählt nicht gegen 1 Feed-Beitrag/Tag). Loris: „memes humorvoll als fertige Beiträge“. |
| Do 29.10. 17:45 | 🎬 Reel `m02-reel-mein-weg-haeufigster-fehler` | 🟢 freigegeben (geht automatisch online) | 28.10.: Mein Weg #02 (Stimme 27.10.), Montage wie #01 + Bewegung in Sekunde 1; Welle nach #01 nutzen (Loris: „alle Punkte umsetzen“). |
| Do 29.10. 17:50 | 📱 Story `42-story-teaser` | pausiert | 14.10. Nachtlauf: Teaser „Jetzt neu im Profil“ zum AfA-Reel (Titelbild), jobs/p42_reel_afa.json. Bibliotheks-Teaser teaser_afa nicht genutzt („zurück“, Dashboard-Zahlen im Bild). |
| Fr 30.10. 12:15 | 📱 Story `43-story-tipp` | pausiert | 14.10. Nachtlauf: Emoji-Tipp „4,0 × Messbetrag“ (§ 35 EStG, Einzel-/Mitunternehmer, höchstens tatsächlich zu zahlende GewSt), 👏/😮 (jobs/p43_reel_par35.json). Statt zdt_35 („angerechnet“, ohne Tipp-Format). |
| Fr 30.10. 12:15 | 📱 Story `meme3-story` | 🟢 freigegeben (geht automatisch online) | 28.10.: eigenes Steuer-Meme (EXCEL), Story statt Feed (zählt nicht gegen 1 Feed-Beitrag/Tag). Loris: „memes humorvoll als fertige Beiträge“. |
| Fr 30.10. 17:45 | 🎬 Reel `i01-reel-insider-programm` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-10-30. · 26.10.: Serie Finanzamt-Insider #01 (Aufnahme 26.10., Schnitt aufnahmen/2026-10-26/geschnitten), Premium-Look premium/insider_01.html, 27,5 s, −18 LUFS, Hook „Kein Mensch. Ein Programm.“ ab Frame 1. Freigabe Loris („Freigabe für alles mit Sprachnachricht“, Reihenfolge ab heute). |
| Fr 30.10. 17:50 | 📱 Story `44-story-teaser` | pausiert | 14.10. Nachtlauf: Teaser „Jetzt neu im Profil“ zum Glossar-Karussell (Folie 1), jobs/p44_glossar.json. |
| Sa 31.10. 12:15 | 📱 Story `meme4-story` | 🟢 freigegeben (geht automatisch online) | 28.10.: eigenes Steuer-Meme (BESCHEID), Story statt Feed (zählt nicht gegen 1 Feed-Beitrag/Tag). Loris: „memes humorvoll als fertige Beiträge“. |
| Sa 31.10. 17:45 | 🎬 Reel `52-reel-gobd` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-10-27. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-10-27 17:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-26 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-26 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p52_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf (d2): aus Bibliothek (R4 gegengelesen, karussell/gobd), Reel ohne Stimme 14,0 s, −17,9 LUFS (Peak −3,5 dBFS), Atmo Uhr + Fehlerton im Hook, Musik 11 Future Garage ab 2,4 s. Titelbild neu als Prüfer-Fall „Der Prüfer öffnet deine Excel.“, Karten aus gobd Folien 5/4/6 (3 Punkte: unveränderbar, zeitgerecht, dokumentiert; schnitt/p52_55_karten_bauen.py), Abspann „Kommentiere TOOL“ (jobs/p52_reel_gobd.json), Schnitt schnitt/p52_reel_gobd.json. Geprüft: § 145 Abs. 1, § 146 Abs. 1 und 4, § 147 Abs. 6 AO, 10-Tage-Richtwert GoBD für unbare Vorgänge. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-10-31. |
| Sa 31.10. 17:50 | 📱 Story `45-story-teaser` | pausiert | 14.10. Nachtlauf: Teaser „Jetzt neu im Profil“ zum vGA-Reel (Titelbild), jobs/p45_reel_vga.json. |
| So 01.11. 12:15 | 📱 Story `46-story-zdt` | pausiert | 14.10. Nachtlauf: Tipp-Story Zahl des Tages storys/zdt_8b (R3 gegengelesen, „ab 10 % Beteiligung“ bereits korrigiert) zum § 8b-Karussell. |
| So 01.11. 12:15 | 📱 Story `meme5-story` | 🟢 freigegeben (geht automatisch online) | 28.10.: eigenes Steuer-Meme (BELEGE), Story statt Feed (zählt nicht gegen 1 Feed-Beitrag/Tag). Loris: „memes humorvoll als fertige Beiträge“. |
| So 01.11. 17:45 | 🖼️ Karussell `35-karussell-steuerkalender` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-01. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-01. · 25.10.: Termin 2026-11-01 17:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 25.10.: Slot an Einspruch-Reel abgegeben, neuer Termin beim Umbau auf Premium-Look. · 14.10. Nachtlauf: aus Bibliothek (R4 gegengelesen), Folie 2 präzisiert (Dauerfristverlängerung nur USt, § 46 UStDV), Folie 6 Speichern + Weiterleiten neu (Job p35_steuerkalender.json), Alt-Texte in alt_texte.json. Caption: 15.11.2026 = Sonntag → 16.11. |
| So 01.11. 17:45 | 🎬 Reel `47-reel-betriebsaufspaltung` | pausiert | 14.10. Nachtlauf: aus Bibliothek (R4 gegengelesen), Reel ohne Stimme 15,0 s, −18,0 LUFS, Atmo Uhr + Fehlerton im Hook, Musik 09 Lofi Piano. Titelbild neu als Fall „Halle an die eigene GmbH. Gewerblich.“, 3 Punkte = karussell/betriebsaufspaltung Folien 2–4 (sachliche + personelle Verflechtung, Folge), Betriebsaufgabe-Risiko in der Bildunterschrift. jobs/p47_reel_betriebsaufspaltung.json, Karten schnitt/p45_47_karten_bauen.py, Schnitt schnitt/p47_reel_betriebsaufspaltung.json. |
| So 01.11. 17:50 | 📱 Story `47-story-teaser` | pausiert | 14.10. Nachtlauf: Teaser „Jetzt neu im Profil“ zum Betriebsaufspaltungs-Reel (Titelbild), jobs/p47_reel_betriebsaufspaltung.json. |
| Mo 02.11. 12:15 | 📱 Story `48-story-tipp` | pausiert | 14.10. Nachtlauf: Emoji-Tipp-Story „Fahrtenbuch: zeitnah und geschlossen“ (nach storys/tipp_fahrtenbuch, R5) zum Firmenwagen-Reel, jobs/p48_reel_firmenwagen.json. |
| Mo 02.11. 17:45 | 🎬 Reel `i06-reel-insider-schaetzung` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-10-31. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #06 (Aufnahme 26.10.), Premium-Look premium/insider_06.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-02. |
| Mo 02.11. 17:50 | 📱 Story `49-story-teaser` | pausiert | 14.10. Nachtlauf: Teaser „Jetzt neu im Profil“ zum Kleinunternehmer-CTA-Reel (Titelbild), jobs/p49_reel_kleinunternehmer.json. |
| Di 03.11. 12:15 | 📱 Story `50-story-tipp` | pausiert | 14.10. Nachtlauf: Emoji-Tipp-Story „5 % degressiv für Wohnungsneubau“ (§ 7 Abs. 5a EStG) zum Gebäude-AfA-Reel, jobs/p50_reel_gebaeude_afa.json. |
| Di 03.11. 17:45 | 🎬 Reel `45-reel-vga` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-05. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-10-29 17:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-28 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-27 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p45_reel_stimme_bauen.py, Vorschau vorschau_stimme.png). Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R2 gegengelesen), Reel ohne Stimme 13,4 s, −18,0 LUFS, Atmo Uhr + Fehlerton im Hook, Musik 06 Lofi ruhig. Titelbild neu als Prüfer-Fall „Darlehen, 0 % Zinsen? vGA.“, Karten aus karussell/vga Folie 2 und Folie 3 mit 3 statt 5 Punkten neu gerendert (Reel-Regel; Folie 04 mit verwaistem „nr 01“ nicht genutzt), Klassiker 4+5 und Rückwirkungsverbot in der Bildunterschrift. jobs/p45_reel_vga.json, Karten schnitt/p45_47_karten_bauen.py, Schnitt schnitt/p45_reel_vga.json. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-03. |
| Di 03.11. 17:50 | 📱 Story `51-story-teaser` | pausiert | 14.10. Nachtlauf: Teaser „Jetzt neu im Profil“ zum Kapitalerträge-Karussell (Ausschnitt Folie 1, bausteine/teaser_bild.png), jobs/p51_kapitalertraege.json. |

## 🗓️ Danach

| Wann | Was | Status | Hinweis |
|---|---|---|---|
| Mi 04.11. 12:15 | 📱 Story `52-story-tipp` | pausiert | 14.10. Nachtlauf (d2): Emoji-Tipp „Unbare Vorgänge: als Richtwert 10 Tage“ (GoBD, zeitgerechte Erfassung) mit Verweis aufs Reel, 👏/😮 (jobs/p52_reel_gobd.json). |
| Mi 04.11. 17:45 | 🖼️ Karussell `10-e-rechnung` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-04. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-04. · 25.10.: Termin 2026-10-27 11:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. (Nachtlauf, Loris' Auftrag „optimieren + freigeben“): Bildunterschrift fachlich korrigiert (Papier in der Übergangszeit ohne Zustimmung, § 27 Abs. 38 UStG; Ausnahmen), Folie 6 Speichern + Weiterleiten, Alt-Texte · 13.10.: Zeiten auf die Follower-Welle gelegt (Loris, Insights: aktivste Zeit 18–21 Uhr) – Feed 17:45/11:45, Storys 17:50/12:15. · Aus der Bibliothek (gegengelesen 05.10., Rechtsstand Okt. 2026: § 27 Abs. 38 UStG) · 06.10.: auf Fr 23.10. geschoben (Reel-Takt alle 2 Tage). · [Freigabe #31](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/issues/31) |
| Mi 04.11. 17:50 | 📱 Story `53-story-teaser` | pausiert | 14.10. Nachtlauf (d2): Teaser „Jetzt neu im Profil“ zum IAB-Reel (Titelbild), jobs/p53_iab.json. storys/tipp_iab nicht genutzt (keine Emoji-Reaktion). |
| Do 05.11. 12:15 | 📱 Story `54-story-tipp` | pausiert | 14.10. Nachtlauf (d2): Emoji-Tipp Pflichthinweis „Steuerschuldnerschaft des Leistungsempfängers“ (§ 14a Abs. 5 UStG) mit Verweis aufs Reel, 👏/😮 (jobs/p54_reel_reverse_charge.json). storys/frage_rc nicht genutzt (STICKER-Platzhalter). |
| Do 05.11. 17:45 | 🎬 Reel `i03-reel-insider-einspruch-0euro` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-02. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #03 (Aufnahme 26.10.), Premium-Look premium/insider_03.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-05. |
| Do 05.11. 17:50 | 📱 Story `53-story-teaser-karussell` | pausiert | 14.10. Nachtlauf (d2): Teaser „Jetzt neu im Profil“ zum IAB-Karussell (Folie 1), jobs/p53_iab.json. |
| Fr 06.11. 12:15 | 📱 Story `55-story-tipp` | pausiert | 14.10. Nachtlauf (d2): Emoji-Tipp „28,25 % auf Gewinn, der im Betrieb bleibt“ (§ 34a EStG, zzgl. SolZ, 25 % Nachversteuerung), 👏/😮 (jobs/p55_reel_thesaurierung.json). |
| Fr 06.11. 17:45 | 🎬 Reel `i02-reel-insider-kontenabruf` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-03. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #02 (Aufnahme 26.10.), Premium-Look premium/insider_02.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-06. |
| Fr 06.11. 17:50 | 📱 Story `56-story-teaser` | pausiert | 14.10. Nachtlauf (d2): Teaser „Jetzt neu im Profil“ zum Verjährungs-Karussell (Folie 1), jobs/p56_verjaehrung.json. |
| Sa 07.11. 17:45 | 🎬 Reel `40-reel-formeln` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-03. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-10-28 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-27 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-28 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p40_reel_stimme_bauen.py, Vorschau vorschau_stimme.png). Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R2 gegengelesen, $C$12-Satz korrigiert), Reel ohne Stimme 13,7 s, −18,0 LUFS, Atmo Tippen + Fehlerton im Hook, Musik 12 Pop Electronic. Fall „=WENNFEHLER(…; 0): Fehler weg, Steuer auch“ + 2 Lösungen (XVERWEIS statt Festwert, Namen statt $C$12) = 3 Punkte; MAX/ABRUNDEN bewusst weggelassen (stehen schon im Paragraf-Formel-Reel 24.10.). Karten aus karussell/excel_formeln Folien 6, 2, 5 (schnitt/p36_40_karten_bauen.py), Titelbild + Abspann TOOL neu (jobs/p40_reel_formeln.json), Schnitt schnitt/p40_reel_formeln.json. Raster Mi A verlangt Stimme → Abweichung (ohne Aufnahme). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-07. |
| Sa 07.11. 17:50 | 📱 Story `57-story-teaser` | pausiert | 14.10. Nachtlauf (d3): Teaser „Jetzt neu im Profil“ zum § 8c-Reel (Titelbild), jobs/p57_reel_verlust_8c.json; Karte verkleinert (bausteine/teaser_karte.png, schnitt/p57_58_karten_bauen.py), damit nichts angeschnitten wird. |
| So 08.11. 12:15 | 📱 Story `58-story-tipp` | pausiert | 14.10. Nachtlauf (d3): Tipp-Story mit Emoji-Reaktion „Bis 250 € brutto reicht eine Kleinbetragsrechnung (§ 33 UStDV)“ zum Vorsteuer-Reel, jobs/p58_reel_vorsteuer.json. |
| So 08.11. 17:45 | 🖼️ Karussell `37-karussell-bp-vorbereitung` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-08. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-10-28. · 25.10.: Premium-Look (premium/karussells/p37_bp_vorbereitung.json), go Loris, 2026-10-26 17:45. · 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), karussell/bp_vorbereitung Folien 1–5 unverändert; Folie 6 neu: „Speichern bis zur nächsten Prüfungsanordnung“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p37_bp_vorbereitung.json). Geprüft: §§ 196, 197 AO, § 147 Abs. 6 AO, GoBD, § 200 AO; Bildunterschrift ergänzt um 4/2 Wochen Vorlauf (§ 5 Abs. 4 BpO). Alt-Texte in alt_texte.json. Begleit-Reel 38 am Abend. |
| So 08.11. 17:50 | 📱 Story `59-story-teaser` | pausiert | 14.10. Nachtlauf (d3): Teaser „Jetzt neu im Profil“ zum Pensions-Karussell (Folie 1), jobs/p59_pensionen.json; Karte verkleinert (bausteine/teaser_karte.png, schnitt/p57_58_karten_bauen.py), damit nichts angeschnitten wird. |
| Mo 09.11. 17:45 | 🎬 Reel `i04-reel-insider-saeumnis` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-05. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #04 (Aufnahme 26.10.), Premium-Look premium/insider_04.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-09. |
| Di 10.11. 17:45 | 🎬 Reel `38-reel-pruefpfad` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Loris – Einspruch heute zu speziell, breiteres Thema zuerst → 2026-10-31 17:45. · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-02. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-02 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-27 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-27 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p38_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R1/R2 gegengelesen), Begleit-Reel zu Karussell 37, ohne Stimme 13,7 s, −18,0 LUFS, Atmo Uhr im Hook, Musik 09 Lofi-Piano ab der Lösung. Als Betriebsprüfungs-Thema gerahmt („Woher kommt diese Zahl?“, GoBD-Nachvollziehbarkeit), nicht als #BEZUG/Excel-Fehler. Titelbild „Betriebsprüfung – Jede Zahl bis zur Quelle“ und Abspann „Kommentiere TOOL“ neu (jobs/p38_reel_pruefpfad.json); bausteine/haken_pruefpfad, leiste_pruefpfad, haken_ueber_pruefpfad auf Folien 3/4 von bp_vorbereitung (schnitt/p36_40_karten_bauen.py), Schnitt schnitt/p38_reel_pruefpfad.json. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-10. |
| Mi 11.11. 17:45 | 🖼️ Karussell `31-karussell-zinsschranke` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-11. · 25.10.: Termin 2026-10-28 17:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), Folien 1–5 aus karussell/zinsschranke, Folie 6 neu (Speichern + Weiterleiten, Job jobs/p31_zinsschranke.json). Offener Prüfbericht-Punkt erledigt: Bildunterschrift nennt Untergang des Zinsvortrags bei schädlichem Anteilseignerwechsel (§ 4h Abs. 5 EStG i. V. m. § 8c KStG). Freigrenze < 3 Mio. €, 30 % verrechenbares EBITDA, Stand-alone „keine nahestehende Person“, Escape 2 Prozentpunkte. Begleit-Karussell zum Abend-Reel 21 Zinsschranke |
| Do 12.11. 17:45 | 🎬 Reel `i10-reel-insider-belege` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-06. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #10 (Aufnahme 26.10.), Premium-Look premium/insider_10.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-12. |
| Fr 13.11. 17:45 | 🎬 Reel `39-reel-holding` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-09. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-03 17:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-28 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-28 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p39_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R4 gegengelesen), Reel ohne Stimme 13,8 s, −18,0 LUFS, Musik 07 Minimal Tech. Veräußerungsgewinn GmbH an GmbH: 1 Mio. € × 5 % nbBA (§ 8b Abs. 2, 3 KStG) × 29,825 % (Hebesatz 400 %) = 14.913 € = 1,49 % – nachgerechnet. Karten aus karussell/holding Folien 2+3 (schnitt/p36_40_karten_bauen.py); Titelbild „1 Mio. € Gewinn. 1,5 % Steuer.“, Karte „Dividenden erst ab 10 % (§ 8b Abs. 4 KStG)“ und Abspann TOOL neu (jobs/p39_reel_holding.json). Bildunterschrift: Dividenden § 8b Abs. 1/5, 10-%-Grenze Abs. 4, GewSt-Schachtel 15 % (§ 9 Nr. 2a GewStG), Verluste nicht abziehbar (Abs. 3 Satz 3), Ausnahmen Abs. 7/8. Abgrenzung zum Karussell par8b (Dividenden, 01.11.). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-13. |
| Sa 14.11. 17:45 | 🎬 Reel `i07-reel-insider-kontrollmitteilung` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-07. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #07 (Aufnahme 26.10.), Premium-Look premium/insider_07.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-14. |
| So 15.11. 17:45 | 🖼️ Karussell `53-karussell-iab` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-15. · 25.10.: Termin 2026-10-30 17:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf (d2): aus Bibliothek (R6 gegengelesen), karussell/iab_2 Folien 1–6 unverändert; Folie 7 neu: „Speichern für die Investitionsplanung“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p53_iab.json). Begleit-Reel 53 am Vorabend. Alt-Texte in alt_texte.json. Geprüft: § 7g Abs. 1–6 EStG (50 %, 200.000 €/200.000 €, 3 Jahre, 40 % Sonder-AfA, 90 % betrieblich). |
| Mo 16.11. 17:45 | 🎬 Reel `54-reel-reverse-charge` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-10-29. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-04 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-29 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-29 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p54_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf (d2): aus Bibliothek (R4 gegengelesen, karussell/reverse_charge), Reel ohne Stimme 14,2 s, −18,0 LUFS (Peak −4,4 dBFS), Atmo Uhr + Fehlerton im Hook, Musik 09 Lofi-Piano ab 2,4 s. Titelbild neu als Prüfer-Fall „Mit USt bezahlt. Vorsteuer: 0 €.“, Einblendung Demo-Fall Bau (100.000 € + 19.000 € USt), Karten aus reverse_charge Folien 5/4 (schnitt/p52_55_karten_bauen.py), Abspann TOOL (jobs/p54_reel_reverse_charge.json), Schnitt schnitt/p54_reel_reverse_charge.json. Geprüft: § 13b Abs. 2 Nr. 4 und Abs. 5 UStG, § 14c Abs. 1, § 15 Abs. 1 Satz 1 Nr. 1 und Nr. 4, § 14a Abs. 5 UStG; Bildunterschrift erklärt Saldo (13b-Schuld = Vorsteuer) und Rückforderung über berichtigte Rechnung. Nähe zu d3 (Vorsteuer, So 08.11.) beachtet: hier nur § 13b-Fall. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-16. |
| Di 17.11. 17:45 | 🎬 Reel `i11-reel-insider-anrufen` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-09. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #11 (Aufnahme 26.10.), Premium-Look premium/insider_11.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-17. |
| Mi 18.11. 17:45 | 🖼️ Karussell `56-karussell-verjaehrung` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-18. · 25.10.: Termin 2026-11-02 17:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf (d2): aus Bibliothek (R6 gegengelesen, keine offenen Punkte), karussell/verjaehrung Folien 1–5 unverändert; Folie 6 neu: „Speichern für die nächste Prüfungsanordnung“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p56_verjaehrung.json). Alt-Texte in alt_texte.json. Geprüft: § 169 Abs. 2 Satz 1 Nr. 2 und Satz 2, § 170 Abs. 2 Satz 1 Nr. 1, § 171 AO; Demo Erklärung für 2022, Abgabe 2024 → Ende 31.12.2028. |
| Do 19.11. 17:45 | 🎬 Reel `i12-reel-insider-mbs-excel` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-10. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #12 (Aufnahme 26.10.), Premium-Look premium/insider_12.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-19. |
| Fr 20.11. 17:45 | 🎬 Reel `43-reel-par35` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-10. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-05 17:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-29 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-30 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p43_reel_stimme_bauen.py, Vorschau vorschau_stimme.png). Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R5 gegengelesen, „tatsächlich zu zahlende“ GewSt korrigiert), Reel ohne Stimme 14,4 s, −18,1 LUFS (Peak −4,1 dBFS), Musik 06 Lofi ruhig. Titelbild reels/reel_35, Karten aus karussell/par35 Folien 3–5 (schnitt/p41_44_karten_bauen.py), Abspann „Kommentiere TOOL“ neu (jobs/p43_reel_par35.json), Schnitt schnitt/p43_reel_par35.json. Nachgerechnet: 100.000 − 24.500 = 75.500 × 3,5 % = 2.642,50 €; × 400 % = 10.570 € = 4,0 × 2.642,50; bei 450 % 11.891,25 € → 1.321,25 € Rest. Ermäßigungshöchstbetrag und „nur natürliche Personen/Mitunternehmer“ in der Bildunterschrift. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-20. |
| Sa 21.11. 17:45 | 🎬 Reel `48-reel-firmenwagen` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-10-30. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-10-30 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-30 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-30 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p48_reel_stimme_bauen.py, Vorschau vorschau_stimme.png). Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R5 gegengelesen), Reel ohne Stimme 15,0 s, −17,9 LUFS, Atmo Uhr + Fehlerton im Hook, Musik 10 Spannung. Titelbild neu als Prüfer-Fall „Fahrtenbuch in Excel. Verworfen.“, 3 Punkte = karussell/firmenwagen Folien 5, 2, 3 (Fahrtenbuch zeitnah/geschlossen, 1 %, 0,03 %). Demo 50.000 € BLP, 20 km → 800 €/Monat nachgerechnet; E-Auto 0,25 % bis 100.000 € (Anschaffung ab 1.7.2025) in der Bildunterschrift. jobs/p48_reel_firmenwagen.json, Karten schnitt/p48_50_karten_bauen.py, Schnitt schnitt/p48_reel_firmenwagen.json. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-21. |
| So 22.11. 17:45 | 🖼️ Karussell `44-karussell-glossar` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-22. · 25.10.: Termin 2026-10-31 17:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen, Einlagekonto und Messbetrag-Box korrigiert), karussell/glossar_1 Folien 1–6, Folie 7 neu: Speichern + Weiterleiten + TOOL statt offener Kommentarfrage (jobs/p44_glossar.json). jahresabschluss_7 nicht genutzt: nur 4 Folien, nur Punkt 01 ausgeführt, Rest doppelt mit KSt-Staffel/Hebesatz/Hinzurechnung/latente Steuern/Rückstellung. Freibetrag/Abrundung und § 8c-Ausnahmen in der Bildunterschrift. alt_texte.json. |
| Mo 23.11. 17:45 | 🎬 Reel `55-reel-thesaurierung` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-12. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-07 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-31 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-31 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p55_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf (d2): aus Bibliothek (R4 gegengelesen, karussell/thesaurierung), Reel ohne Stimme 14,0 s, −18,0 LUFS (Peak −4,2 dBFS), Musik 12 Pop Electronic. Titelbild neu „28,25 % statt bis 45 %.“, Karten aus thesaurierung Folien 2/3/4 (Folie 5 Option § 1a KStG bewusst nicht genutzt, Antragsfrist nicht nachgeprüft), Abspann TOOL (jobs/p55_reel_thesaurierung.json), Schnitt schnitt/p55_reel_thesaurierung.json. Geprüft: § 34a Abs. 1 (28,25 % zzgl. SolZ, Antrag, Bilanzierer) und Abs. 4 (25 % Nachversteuerung); Bildunterschrift: Gesamtbelastung bei baldiger Entnahme oft höher. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-23. |
| Di 24.11. 17:45 | 🎬 Reel `49-reel-kleinunternehmer` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Platz für Insider #01 gemacht, Termin vorläufig. · 26.10.: Loris – Einspruch heute zu speziell, breiteres Thema zuerst → 2026-10-26 17:45. · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-10-31. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-10-31 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-31 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-26 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p49_reel_stimme_bauen.py, Vorschau vorschau_stimme.png). Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R5 gegengelesen), CTA-Reel KW 45 (TOOL-Aufruf im Abspann, eigener TOOL-Absatz in der Bildunterschrift: Grenz-Monitor 100.000 €). Reel ohne Stimme 15,4 s, −18,2 LUFS, Musik 12 Pop Electronic, Abspann zusätzlich groß „Kommentiere „TOOL““. Titelbild neu „100.000 € und raus.“, Karten: Grenz-Folien neu gerendert mit Normbox „§ 19 Abs. 1 UStG“ (ohne Satzangabe – Satzzählung der Neufassung 2025 nicht sicher belegt) + karussell/kleinunternehmer Folie 4. Neugründer-Regel und Verzicht 5 Jahre (§ 19 Abs. 3 UStG) in der Bildunterschrift. jobs/p49_reel_kleinunternehmer.json, Karten schnitt/p48_50_karten_bauen.py, Schnitt schnitt/p49_reel_kleinunternehmer.json. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-24. |
| Mi 25.11. 17:45 | 🖼️ Karussell `51-karussell-kapitalertraege` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-25. · 25.10.: Termin 2026-11-03 11:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf: aus Bibliothek (R6 gegengelesen), karussell/kapitalertraege Folien 1–6 unverändert; Folie 7 neu: „Speichern für die Steuererklärung“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p51_kapitalertraege.json). Nachgerechnet: (3.000 − 1.000) × 26,375 % = 527,50 €. Alt-Texte in alt_texte.json. KW 45 ungerade → Karussell abends. |
| Do 26.11. 17:45 | 🎬 Reel `57-reel-verlust-8c` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-13. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-06 17:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-11-01 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-11-01 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p57_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf (d3): aus Bibliothek (R4 gegengelesen), Reel ohne Stimme 13,6 s, −17,8 LUFS, Atmo Uhr + Fehlerton im Hook, Musik 10 Spannung. Titelbild neu als Zahl-Hook „51 % verkauft? Verluste weg.“, Karten aus karussell/par8c Folie 2 (Regel) und 3 (Rettungsanker), ampel_8c_* (Demo-Quoten) bewusst nicht genutzt. Bildunterschrift: § 8c Abs. 1 Satz 1/4/5–8, Abs. 1a, § 8d KStG, § 10a Satz 10 GewStG, Zinsvortrag § 8a Abs. 1 Satz 3 KStG. Sa 11:45 bleibt frei (Stimm-Slot). jobs/p57_reel_verlust_8c.json, Karten schnitt/p57_58_karten_bauen.py, Schnitt schnitt/p57_reel_verlust_8c.json. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-26. |
| Fr 27.11. 17:45 | 🎬 Reel `50-reel-gebaeude-afa` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10.: Loris bestätigt „mehr als doppelt so schnell“ – bleibt so. · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-07. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-01 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-11-01 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-11-02 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p50_reel_stimme_bauen.py, Vorschau vorschau_stimme.png). Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R5 gegengelesen), Reel ohne Stimme 15,0 s, −18,0 LUFS, Musik 08 Chill House. Titelbild = reels/reel_gebaeude (unverändert), 3 Punkte = karussell/gebaeude_afa Folien 3–5 (linear § 7 Abs. 4, degressiv 5 % § 7 Abs. 5a, Sonder-AfA § 7b EStG). Demo 400.000 € → 12.000 € / 20.000 € / 19.000 € nachgerechnet. Grund und Boden + Voraussetzungen Betriebsgebäude in der Bildunterschrift. jobs/p50_reel_gebaeude_afa.json, Karten schnitt/p48_50_karten_bauen.py, Schnitt schnitt/p50_reel_gebaeude_afa.json. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-27. |
| Sa 28.11. 17:45 | 🎬 Reel `53-reel-iab` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-06. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-06 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-30 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-31 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p53_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf (d2): aus Bibliothek (R6 gegengelesen, karussell/iab_2), Begleit-Reel zum Karussell 53 am Do 17:45, ohne Stimme 14,0 s, −18,0 LUFS (Peak −5,6 dBFS), Musik 08 Chill House. Titelbild „Heute abziehen. Später kaufen.“, Karten aus iab_2 Folien 2/3, Einblendung „Nicht investiert? Rückwirkend weg.“ (§ 7g Abs. 3 EStG, § 233a AO) und Abspann TOOL neu (jobs/p53_iab.json), Schnitt schnitt/p53_reel_iab.json. Geprüft: § 7g Abs. 1 (50 %, Gewinngrenze 200.000 €, Höchstbetrag 200.000 €), Abs. 2 (Hinzurechnung/Kürzung im Kaufjahr), Abs. 3; Demo 60.000 € → 30.000 €. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-28. |
| So 29.11. 17:45 | 🖼️ Karussell `46-karussell-dividenden-8b` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-29. · 25.10.: Termin 2026-11-04 17:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), karussell/par8b Folien 1–5 unverändert; Folie 6 neu: „Speichern für später“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p46_dividenden_8b.json). Bildunterschrift nennt laut Prüfbericht 10-%-Grenze (§ 8b Abs. 4 KStG, Beginn des Kalenderjahres) und 5 % nbBA (§ 8b Abs. 5 KStG); GewSt-Schachtel § 9 Nr. 2a GewStG ab 15 % zu Beginn des EZ, sonst § 8 Nr. 5 GewStG. Nachgerechnet: 5.000 × 15,825 % = 791 €, × 14 % = 700 €, Summe 1.491 €. Alt-Texte in alt_texte.json. Abgrenzung zum Kürzungen-Karussell (18.10.): dort nur Schachtel-Zeile. |
| Mo 30.11. 17:45 | 🎬 Reel `32-reel-mindeststeuer` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-14. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-08 17:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-11-02 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-11-02 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p32_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), Reel ohne Stimme 14,6 s (Titelbild reel_mindeststeuer + 3 Karten nach karussell/mindeststeuer + Abspann TOOL), Musik 12_pop_electronic. Schnitt: vorlagen/system/schnitt/p32_reel_mindeststeuer.json |
| Di 01.12. 17:45 | 🎬 Reel `34-reel-einspruch` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Loris – Einspruch heute zu speziell, breiteres Thema zuerst → 2026-11-02 17:45. · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-10-26. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-10-26 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-26 11:45. · 25.10.: go Loris für Premium-Fassung v4 (leisere Töne), So 17:45 per Lauf auf Arbeitsbranch. · 25.10.: Premium-Fassung im Motion-Design-Look (Loris' Design-Screenshots): HTML-Animation vorlagen/system/premium/einspruch.html, Bau premium/reel_bauen.py, 27 s, −18 LUFS, Loris' Stimme, Titelbild = Frame 1; klassische Fassung reel_stimme_klassisch.mp4. Vorschlag So 25.10. 17:45, wartet auf go. · 25.10.: Hook auf Ergebnis umgestellt („Bescheid am 5.10. / Einspruch bis 9.11.“), 26,9 s, −18 LUFS; vorgeschlagen für So 25.10. 17:45 (Autopilot), wartet auf go. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p34_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R6 gegengelesen), Reel ohne Stimme 14,6 s, Fall: zur Post Mo 05.10. → bekannt Fr 09.10. (§ 122 Abs. 2 Nr. 1 AO, 4 Tage seit 2025) → Frist Mo 09.11. (§ 355 AO), § 361 AO. Uhr-Atmo + 07_minimal_tech. Schnitt: vorlagen/system/schnitt/p34_reel_einspruch.json · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-12-01. |
| Di 01.12. 17:50 | 📱 Story `34-story-tipp` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Loris – Einspruch heute zu speziell, breiteres Thema zuerst → 2026-11-02 17:50. · 25.10.: mit dem Einspruch-Reel auf Mo 12:15. · 25.10.: mit dem Reel auf 17:50 (go Loris). · 14.10. Nachtlauf: aus Bibliothek (R6 gegengelesen), Tipp-Story nach tipp_einspruch (korrigierte Fassung: Aufgabe zur Post + 4 Tage) mit Emoji-Reaktion 👏/😮 – kein Quiz, damit keine Auflösung Mo nötig |
| Mi 02.12. 17:45 | 🖼️ Karussell `59-karussell-pensionen` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-12-02. · 25.10.: Termin 2026-11-05 11:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf (d3): aus Bibliothek (R4 gegengelesen, keine offenen Punkte), karussell/pension Folien 1–5 unverändert; Folie 6 neu: „Speichern für die Gutachten-Saison“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p59_pensionen.json). Letzter Testmonat-Tag: Bildunterschrift mit Community-Auswahl „Welches Thema als Nächstes: A) Teilwertabschreibung oder B) Rechnungsabgrenzung?“. Fachlich: § 6a Abs. 1, Abs. 3 Satz 3 EStG (6 %), § 253 Abs. 2 und 6 HGB (10-Jahres-Durchschnitt, Ausschüttungssperre), § 274 HGB (Wahlrecht Aktivüberhang). Alt-Texte in alt_texte.json. |
| Do 03.12. 17:45 | 🎬 Reel `33-reel-paragraf-formel` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-16. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-07 17:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-11-02 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-11-01 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p33_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 24.10.: auf Mo 26.10. getauscht mit Bewirtung (go Loris), Umbau nach Wissen 24.10. offen. · 14.10. Nachtlauf: aus Bibliothek (R4 gegengelesen), Reel ohne Stimme 14,4 s (3 Normen als Formel: § 8 Nr. 1 GewStG, § 4 Abs. 5 S. 1 Nr. 1 EStG, § 8b Abs. 5 KStG; Abspann abspann_paragraf; Titelbild neu mit „Drei Normen“ statt „Fünf“). Raster Sa mittags = Stimme → Abweichung (keine Aufnahme). Schnitt: vorlagen/system/schnitt/p33_reel_paragraf_formel.json · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-12-03. |
| Fr 04.12. 17:45 | 🎬 Reel `i05-reel-insider-finanzbeamte` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-10-27. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #05 (Aufnahme 26.10.), Premium-Look premium/insider_05.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 27.10. 17:35: Platz an Mein Weg #01 abgegeben (Loris), neu 04.12. |
| Sa 05.12. 17:45 | 🎬 Reel `i09-reel-insider-elterngeld` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-10-29. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #09 (Aufnahme 26.10.), Premium-Look premium/insider_09.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 29.10.→05.12. (Platz an Mein Weg #02, Welle nach #01 nutzen). |
| So 06.12. 17:45 | 🖼️ Karussell `41-karussell-mythen` | 🟢 freigegeben (geht automatisch online) | 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-10-28. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-08. · 25.10.: Termin 2026-10-29 11:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), karussell/mythen Folien 1–7 (nicht mythen_3), Folie 8 neu: Speichern + Weiterleiten + TOOL statt offener Kommentarfrage (jobs/p41_mythen.json). Ablaufhemmung § 147 Abs. 3 Satz 5 AO in der Bildunterschrift. alt_texte.json. · 28.10.→06.12. (Platz an Insider #14 Ferrari). |

## ✅ Zuletzt veröffentlicht (Autopilot)

- Di 27.10. 18:00 · 🎬 Reel `m01-reel-mein-weg-scheinsicherheit` · [ansehen](https://www.instagram.com/reel/DfAWBBflLkW/) (online 2026-10-27 18:01)
- Mo 26.10. 17:45 · 🎬 Reel `i08-reel-insider-rente-oma` · [ansehen](https://www.instagram.com/reel/De9tD9vj4EH/) (online 2026-10-26 17:45)
- So 25.10. 17:45 · 🎬 Reel `30-reel-gwg` · [ansehen](https://www.instagram.com/reel/De7JF3cAGrX/) (online 2026-10-25 17:45)
- Sa 24.10. 12:15 · 📱 Story `36-story-tipp` · [ansehen](https://www.instagram.com/stories/maehrsteuern/4014930017247382776) (online 2026-10-24 12:16)
- Sa 24.10. 11:14 · 🎬 Reel `36-reel-bewirtung` · [ansehen](https://www.instagram.com/reel/De3yheAFKBg/) (online 2026-10-24 11:17)
- Do 22.10. 11:50 · 🎬 Reel `62-reel-glaesern` · [ansehen](https://www.instagram.com/reel/DezHdgPt1_0/) (online 2026-10-22)
- Mi 21.10. 18:00 · 🎬 Reel `58-reel-vorsteuer` · [ansehen](https://www.instagram.com/reel/Dewza8JCASO/) (online 2026-10-21 18:10)
- Mi 21.10. 16:35 · 🎬 Reel `42-reel-afa` (online 2026-10-21 16:35)
- Di 20.10. 17:50 · 📱 Story `28-story-aufloesung` · [ansehen](https://www.instagram.com/stories/maehrsteuern/4012196501812014820) (online 2026-10-20 17:50)
- Di 20.10. 17:45 · 🎬 Reel `19-reel-verlustvortrag` · [ansehen](https://www.instagram.com/reel/DeuJJHoDXkl/) (online 2026-10-20 17:45)

## 📈 Zahlen (täglich ca. 08:45)

**377 Follower** · 27 Beiträge im Profil (Abruf 2026-10-27) · **+1** seit 2026-10-26
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

Rohdaten: `automatik/statistik/`, Auswertung: `strategie/06_auswertung.md`

## ⚙️ Automatik

| Ablauf | Wann | Letzter Lauf |
|---|---|---|
| Lage + Google-Kalender | alle 15 Min. (LAGE.md, Kalender-Sync, Wächter) | ✅ ok |
| Posten | alle 15 Min. (postet freigegebene Einträge) | ✅ ok |
| Freigabe | bei neuen Entwürfen / Antwort im Issue | ✅ ok |
| Statistik | täglich ca. 08:45 | ✅ ok |
| Schlüssel verlängern | am 1. des Monats ca. 06:27 | ✅ ok |
| Radar + LinkedIn | täglich ca. 07:00 (Issue mit Arbeitsliste) | ✅ ok |
| Kommentare | nach jedem Posten-Takt (Vorschläge ins Issue) | ✅ ok |
| Wochenbericht | sonntags ca. 18:00 (ein Issue) | ✅ ok |
| Musik holen | nur von Hand | ✅ ok |

## 📜 Protokoll – jede Änderung

🤖 Autopilot · ✅ Freigabe · 📈 Statistik · 🎵 Musik · 🔀 Merge · ✍️ von Hand / Claude

**Mi 28.10.2026**
- 06:23 ✍️ Markenbilder: Übersicht und Einsatzregeln (assets/marke/README.md) ([`572331b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/572331b47745a57a4d64c3728d305df82b8f0d05))
  - `assets/marke/README.md`
- 06:22 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`6596fb7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6596fb7d4c6dffa94d4ffcc11b289d146eba5a57))
- 06:21 ✍️ Markenbilder 28.10.: Portrait Loris (neutral + lächelnd, grüner Hintergrund), MBS-Logo ([`0fdc4ed`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0fdc4ed555675693c3586c44f087e5e62839cac0))
  - `assets/marke/loris_portrait.jpg`, `assets/marke/loris_portrait_laecheln.jpg`, `assets/marke/mbs_logo.jpg`
- 01:15 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`a4dfb19`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a4dfb1982142aed9205359b2c83d346a365c039a))
- 01:15 ✍️ Mein Weg #02: nur noch ein Foto (Selfie), übrige Szenen als Motion-Grafik (Loris: nicht dieselben Bilder wie #01), Excel-Summe sichtbar falsch ([`74576b9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/74576b9b5f6a243d3749a5db2227e452241acf26))
  - `posts/m02_2026-10-29_mein_weg_haeufigster_fehler`, `vorlagen/system/premium/mein_weg_02.html`
- 01:11 ✍️ 5 eigene Steuer-Memes als Storys (12:15, 28.10.–01.11.), Generator memes.py – eigene Texte/Fotos, keine fremden Figuren ([`3e0137a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3e0137ab2aa2bbea1388b607ea6ebce85e0c6f61))
  - Plan: neu `meme1-story` (2026-10-28 12:15, freigegeben); neu `meme2-story` (2026-10-29 12:15, freigegeben); neu `meme3-story` (2026-10-30 12:15, freigegeben); neu `meme4-story` (2026-10-31 12:15, freigegeben); neu `meme5-story` (2026-11-01 12:15, freigegeben)
- 01:02 ✍️ Mein Weg #02 „Der häufigste Fehler war nie Betrug“ gebaut (Montage, Bewegung ab Sekunde 1) und für Do 29.10. 17:45 eingeplant ([`fc6aa4d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fc6aa4d22db9506de614e951dbd17f9742f89a1e))
  - Plan: neu `m02-reel-mein-weg-haeufigster-fehler` (2026-10-29 17:45, freigegeben)
- 00:58 ✍️ Welle nach Mein Weg #01 nutzen: Mi 28.10. Insider #14 Ferrari (Szene „Nicht absetzbar“), Do 29.10. Mein Weg #02; K41 → 06.12., i09 → 05.12.; Wissen 21 §8 (Zahlen #01) ([`b85cf68`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b85cf68044eb4385782de16f9944e53465577fcd))
  - Plan: neu `i14-reel-insider-ferrari` (2026-10-28 17:45, freigegeben); `41-karussell-mythen` zeit: 2026-10-28 17:45 → 2026-12-06 17:45; `i09-reel-insider-elterngeld` zeit: 2026-10-29 17:45 → 2026-12-05 17:45

**Di 27.10.2026**
- 18:03 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`9845b76`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9845b769ca9624230876b449b9f31db18c6526e0))
- 18:03 ✍️ Insider #13 „Brief vom Finanzamt: Betriebsprüfung“ – Zwischenstand (Stimme 27.10.), noch nicht eingeplant ([`1da0d82`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1da0d82554b0a86900a1dc350f2613152cb91229))
  - `posts/i13_2026-10-27_insider_betriebspruefung`, `vorlagen/system/premium/insider_13.html`
- 18:01 🤖 Autopilot: m01-reel-mein-weg-scheinsicherheit veroeffentlicht ([`313c0d5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/313c0d5755ad3c3e8edbcf20cf13d8ac056d9725))
  - Plan: `m01-reel-mein-weg-scheinsicherheit` status: freigegeben → veroeffentlicht; `m01-reel-mein-weg-scheinsicherheit` online: https://www.instagram.com/reel/DfAWBBflLkW/
- 17:59 🤖 Autopilot: Dateien fuer m01-reel-mein-weg-scheinsicherheit vorbereitet ([`7f8b3b8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7f8b3b834d04ac812544f110d15e9525ff475be0))
  - `posts/m01_2026-10-27_mein_weg_scheinsicherheit`
- 17:47 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`6836f0b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6836f0bb2f564041d07b8091192c00b21ea83ca0))
- 17:46 ✍️ Insider #14 „Ferrari über die Firma?“ gebaut (Stimme 27.10., 38,7 s) – noch nicht eingeplant, wartet auf Loris ([`01c23a3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/01c23a33909c6bae8ff5291b048cd3b895ac06a7))
  - `posts/i14_2026-10-27_insider_ferrari`, `vorlagen/system/premium/insider_14.html`
- 17:45 ✍️ Mein Weg #01 „Scheinsicherheit“: Foto-Montage Diplomierung (Loris' Bilder + Stimme 27.10.), heute 18:00 statt Insider #05 (→ 04.12.) ([`db3c6ab`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/db3c6ab953460ca881a44ae13d322ca04826ecb9))
  - Plan: neu `m01-reel-mein-weg-scheinsicherheit` (2026-10-27 18:00, freigegeben); `i05-reel-insider-finanzbeamte` zeit: 2026-10-27 17:45 → 2026-12-04 17:45
- 17:17 🤖 Autopilot: Dateien fuer i05-reel-insider-finanzbeamte vorbereitet ([`9bc3fd3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9bc3fd32defa874216039c8f2ce321bc8d6047ec))
  - `posts/i05_2026-10-26_insider_finanzbeamte`
- 17:17 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`7a81371`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7a813714917f8e1e2b0d9a5ddbc523813c5d2c52))
- 17:17 ✍️ Aufnahme 27.10. geschnitten: I13, I14, M1, M2, S1–S5 (beide Mikros, Wiederholungen raus; I13 ohne unbelegte Wochenangabe) ([`f6786a5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f6786a54d0090dc4e151a7c05ecb5b2f0dc00ab6))
  - `aufnahmen/2026-10-27/geschnitten/schnitt.py`, `aufnahmen/2026-10-27/geschnitten/stimme_I13.wav`, `aufnahmen/2026-10-27/geschnitten/stimme_I14.wav`, `aufnahmen/2026-10-27/geschnitten/stimme_M1.wav`, `aufnahmen/2026-10-27/geschnitten/stimme_M2.wav`, `aufnahmen/2026-10-27/geschnitten/stimme_S1.wav`, `…`
- 17:11 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`087c031`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/087c031a2bfb9e2f761c2bc414b5011245c1a285))
- 17:11 ✍️ Aufnahme 27.10.: Transkript mit Wortzeiten ([`6892def`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6892def20c64973a0f2a9d4525f5de3c165aaf4b))
  - `aufnahmen/2026-10-27/woerter.json`
- 17:10 ✍️ Aufnahme 27.10.: überarbeitete Sprechtexte (I5, I13, I14, M1, M2, S1–S5), roh ([`7c39aab`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7c39aab010f9a0a93fcc0642a2edc8d55d46d7da))
  - `aufnahmen/2026-10-27/alle_reels_roh.mp3`
- 16:55 ✍️ Sprechtexte: alle übrigen Reels überarbeitet (Autoritäts-Satz, CTA nach Trichter) + Korrekturen aus Faktencheck ([`15108dc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/15108dc026e74eb2bfbebe4b3be5d5704b67469f))
  - `posts/sprechtexte.md`
- 16:55 ✍️ Insider #05: Autoritäts-Satz „Ich war selbst jahrelang im Finanzamt.“ eingesprochen (27.10.) und nach dem Hook eingesetzt, 32,1 s ([`8617138`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/86171386a687d86d76fb015197c89cd0d859dc2f))
  - `aufnahmen/2026-10-27/i05_autoritaet_roh.mp3`, `posts/i05_2026-10-26_insider_finanzbeamte`, `vorlagen/system/premium/insider_05.html`
- 16:52 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`ef5079f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ef5079f8ea72ef09153039467d20bfb0ec0cee0f))
- 16:52 ✍️ Sprechtexte 27.10. überarbeitet (Wissen 21), Zahlen gegen Gesetze geprüft ([`692aee8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/692aee8176c631e426833e8805b02a647013245c))
  - `posts/sprechtexte.md`
- 16:43 ✍️ Insider #05: Hook geschärft (Text im Bild „Finanzbeamte setzen das selbst ab.“ statt Wiederholung, Autoritäts-Badge EX-FINANZAMT · DIPLOM-FINANZWIRT ab Frame 0) ([`58b53d8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/58b53d82486e0d2ff59cff14b78bac24f1f950d0))
  - `posts/i05_2026-10-26_insider_finanzbeamte`, `vorlagen/system/premium/insider_05.html`
- 12:48 ✍️ Sprechtexte Insider #13 Betriebsprüfung + #14 Ferrari über die Firma (Ideen Vorbilder-Radar, Normen geprüft) für Aufnahme 07.11. ([`6e69471`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6e69471f0fab05451b5f7443fb6a6c660a775b61))
  - `posts/sprechtexte.md`
- 11:05 ✍️ Vorbilder-Radar: Ausreißer der Woche ([`a8231c0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a8231c07b66ac690d2cdb528d22b608407b97899))
  - `recherche/viral_liste.csv`, `recherche/vorbilder.json`, `recherche/vorbilder_bericht.md`
- 11:03 ✍️ Vorbilder-Radar: robustere Auswahl (≥100 Interaktionen, 12 Monate, max. 3 je Konto), ungültige Konten raus, Probelauf zurückgesetzt ([`8b940a2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8b940a265d93ac4c95e2ae319e89326a61b06679))
  - `automatik/interaktion.json`, `automatik/vorbilder.py`, `recherche/viral_liste.csv`, `recherche/vorbilder.json`
- 11:02 ✍️ Vorbilder-Radar: Ausreißer der Woche ([`a38c368`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a38c3688a226b5fee642d7e1e72094c999f1e924))
  - `recherche/viral_liste.csv`, `recherche/vorbilder.json`, `recherche/vorbilder_bericht.md`
- 10:59 ✍️ Vorbilder-Radar: 30 deutsche Steuer-Accounts (Auswahl Loris), Bericht mit Follower-Übersicht ([`2f12a02`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2f12a0240072e98d702cb6cb7b1fb9de36669ebe))
  - `automatik/interaktion.json`, `automatik/vorbilder.py`, `recherche/vorbilder.json`
- 10:43 ✍️ Vorbilder-Radar: Ausreißer der Woche ([`e4a3613`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e4a3613faf9ccbb2fffa5741a80dd9e0689f94f4))
  - `recherche/viral_liste.csv`, `recherche/vorbilder.json`, `recherche/vorbilder_bericht.md`
- 10:41 🔀 Merge claude/instagram ([`b0010f8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b0010f8e9c19678a3727ac53f5e01bad5979a3d5))
- 10:40 ✍️ Vorbilder-Radar: wöchentlich Ausreißer-Beiträge von Steuer-Accounts sammeln (Start: lauras_taxdiary); Wissen 21 §7 Stufen-Formate + Recherche-Methode ([`a3594a3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a3594a368c0424cdc0775194b38ebac04ac84699))
  - `.github/workflows`, `LAGE.html`, `automatik/interaktion.json`, `automatik/vorbilder.py`, `recherche/viral_liste.csv`, `strategie/21_wissen_trichter.md`
- 10:38 ✍️ Wissen 21 §6: Zeitachse mit Autoritäts-Satz, 4 Story-Vorlagen, Bio-Formel, Nischen-Recherche (Vorlage recherche/) ([`5f6a1fc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5f6a1fc6abac3e163299d17887b10202bc7b982c))
  - `LAGE.html`, `recherche/README.md`, `recherche/viral_liste.csv`, `strategie/21_wissen_trichter.md`
- 10:29 ✍️ Wissen 21 §5: 7 Bausteine viraler Videos, Hook dreifach, Punch-in-Schnitt für Selfie-Reels, Skript-Strukturen; M1 entsprechend ergänzt ([`e98645a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e98645a4c6af2528f9baa9172edb531f50ccb414))
  - `LAGE.html`, `posts/sprechtexte.md`, `strategie/21_wissen_trichter.md`
- 09:20 📈 Statistik 2026-10-27 ([`b08c4bb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b08c4bbc44e80e5e7fe7736cd612d5243fe8eb57))
  - `automatik/statistik`
- 07:15 📡 Radar 2026-10-27: 8 Beiträge, 0 DM-Entwürfe ([`489c3fd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/489c3fd7d7d6de8b0739909371b296cf67a03b2c))
  - `automatik/interaktion`

**Mo 26.10.2026**
- 20:14 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`67a5204`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/67a520452f717f93234143ad7a92907e58611439))
- 20:13 ✍️ Sprechtext M1: 5-Jahres-Bindung von Loris bestätigt, Aufnahme 27.10. ([`0676dbc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0676dbc1fbe3ab599cac21c2c5e0dc43d24fa96b))
  - `posts/sprechtexte.md`
- 20:10 ✍️ Sprechtexte „Mein Weg“: M1 Scheinsicherheit/Rückzahlung Anwärterbezüge (Idee Loris), bisheriges M1 → M2 ([`960abb9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/960abb915e9722e76041209a96bbb89a9db30365))
  - `posts/sprechtexte.md`
- 20:07 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`c2fa585`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c2fa58553d3eb7ddc04613e877b40f864e13962e))
- 20:07 ✍️ Sprechtexte: Serie „Mein Weg“ M1 (Selfie + Motion-Overlays, Trichter Mitte) ([`09cc654`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/09cc65441db8a3ede27c2c2df6893a4411a03b3b))
  - `posts/sprechtexte.md`
- 20:05 ✍️ Wissen 21: Content-Trichter (oben/mitte/unten), Ziel Follower – Reihenfolge ab 27.10. gemischt statt in Blöcken ([`2b68a7a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2b68a7abd69410633426d7e40138e5393957729d))
  - Plan: `33-reel-paragraf-formel` zeit: 2026-12-01 17:45 → 2026-12-03 17:45; `34-reel-einspruch` zeit: 2026-12-03 17:45 → 2026-12-01 17:45; `34-story-tipp` zeit: 2026-12-03 17:50 → 2026-12-01 17:50; `38-reel-pruefpfad` zeit: 2026-11-20 17:45 → 2026-11-10 17:45; `39-reel-holding` zeit: 2026-11-21 17:45 → 2026-11-13 17:45; `40-reel-formeln` zeit: 2026-11-13 17:45 → 2026-11-07 17:45; `43-reel-par35` zeit: 2026-11-24 17:45 → 2026-11-20 17:45; `45-reel-vga` zeit: 2026-11-14 17:45 → 2026-11-03 17:45; `48-reel-firmenwagen` zeit: 2026-11-16 17:45 → 2026-11-21 17:45; `49-reel-kleinunternehmer` zeit: 2026-11-17 17:45 → 2026-11-24 17:45; `50-reel-gebaeude-afa` zeit: 2026-11-19 17:45 → 2026-11-27 17:45; `52-reel-gobd` zeit: 2026-11-12 17:45 → 2026-10-31 17:45; `53-reel-iab` zeit: 2026-11-26 17:45 → 2026-11-28 17:45; `54-reel-reverse-charge` zeit: 2026-11-23 17:45 → 2026-11-16 17:45; `55-reel-thesaurierung` zeit: 2026-11-27 17:45 → 2026-11-23 17:45; `57-reel-verlust-8c` zeit: 2026-11-28 17:45 → 2026-11-26 17:45; `i02-reel-insider-kontenabruf` zeit: 2026-11-03 17:45 → 2026-11-06 17:45; `i03-reel-insider-einspruch-0euro` zeit: 2026-11-02 17:45 → 2026-11-05 17:45; `i04-reel-insider-saeumnis` zeit: 2026-11-05 17:45 → 2026-11-09 17:45; `i06-reel-insider-schaetzung` zeit: 2026-10-31 17:45 → 2026-11-02 17:45; `i07-reel-insider-kontrollmitteilung` zeit: 2026-11-07 17:45 → 2026-11-14 17:45; `i10-reel-insider-belege` zeit: 2026-11-06 17:45 → 2026-11-12 17:45; `i11-reel-insider-anrufen` zeit: 2026-11-09 17:45 → 2026-11-17 17:45; `i12-reel-insider-mbs-excel` zeit: 2026-11-10 17:45 → 2026-11-19 17:45
- 19:01 ✍️ Fach-Reels 32/33/39/40/45/48/50/52/54/55: Stimme aus beiden Handy-Mikros (klar), Bild unverändert ([`4777a8d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4777a8da51b89edc3f59a902ecfc8424e867d0be))
  - `LAGE.html`, `posts/32_2026-10-23_reel_mindeststeuer`, `posts/33_2026-10-24_reel_paragraf_formel`, `posts/39_2026-10-28_reel_holding`, `posts/40_2026-10-28_reel_formeln`, `posts/45_2026-10-31_reel_vga`, `…`
- 19:00 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`89b29ca`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/89b29cab14d4529cc3e62f0688d3e30367f2582e))
- 19:00 ✍️ Fach-Reels 34/38/43/49/53/57: Stimme aus beiden Handy-Mikros (Schnitte rekonstruiert, Sicherheitsnetz für unsichere 100-ms-Stellen) ([`883c793`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/883c7933a783435b235041a97021e0df8e4671cf))
  - `aufnahmen/2026-10-21/geschnitten/mikros_neu.py`, `aufnahmen/2026-10-21/geschnitten/stimme_32.wav`, `aufnahmen/2026-10-21/geschnitten/stimme_33.wav`, `aufnahmen/2026-10-21/geschnitten/stimme_34.wav`, `aufnahmen/2026-10-21/geschnitten/stimme_38.wav`, `aufnahmen/2026-10-21/geschnitten/stimme_39.wav`, `…`
- 18:03 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`543c5de`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/543c5de264481a800df383815225cfcdfcde8a03))
- 18:03 ✍️ Reel 34 Einspruch: Stimme aus beiden Handy-Mikros (klar), Schnitte unverändert ([`1236f83`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1236f839ca169007306875234382344c56cd3537))
  - `aufnahmen/2026-10-21/geschnitten/stimme_34.wav`, `posts/34_2026-10-25_reel_einspruch`
- 17:54 ✍️ mikros_neu.py: Normierung per kumulativer Summe (viel schneller); Sicherungsordner alt/ nicht versionieren (Original liegt in der Historie) ([`344f7e9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/344f7e94a4613cc6419a0f25e09a3785c2342e3d))
  - `.gitignore`, `aufnahmen/2026-10-21/geschnitten/mikros_neu.py`
- 17:51 ✍️ mikros_neu.py: Suche erst in der Nähe, normierte Korrelation, 100-ms-Fenster (schneller) ([`b263b1d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b263b1d07e5966a334758e9d32e54ab963c65405))
  - `aufnahmen/2026-10-21/geschnitten/mikros_neu.py`
- 17:45 🤖 Autopilot: i08-reel-insider-rente-oma veroeffentlicht ([`280c91c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/280c91c7930790a8046ba268ee648d17bc43d045))
  - Plan: `i08-reel-insider-rente-oma` status: freigegeben → veroeffentlicht; `i08-reel-insider-rente-oma` online: https://www.instagram.com/reel/De9tD9vj4EH/
- 17:24 ✍️ Werkzeug: Stimmen vom 21.10. mit beiden Handy-Mikros neu aufbauen (Schnitte per Kreuzkorrelation rekonstruiert) ([`c27b562`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c27b5628ca0168c053da111b38f84908776a6dd3))
  - `aufnahmen/2026-10-21/geschnitten/mikros_neu.py`
- 17:22 🤖 Autopilot: Dateien fuer i08-reel-insider-rente-oma vorbereitet ([`aa8badd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/aa8baddb9d5d35975c3b9d62e7c39465fc99c5ee))
  - `posts/i08_2026-10-26_insider_rente_oma`
- 17:09 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`18a26c5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/18a26c51f48ff3e7ed0bdb11abbe8968184c8b87))
- 17:09 ✍️ Insider #02–#12: Stimme mit kombinierten Handy-Mikros neu abgemischt (klar, S-Laute hörbar) ([`dd64107`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/dd641076661370c7e8aae9ac1da357870a37ef59))
  - `posts/i02_2026-10-26_insider_kontenabruf`, `posts/i03_2026-10-26_insider_einspruch_0euro`, `posts/i04_2026-10-26_insider_saeumnis`, `posts/i05_2026-10-26_insider_finanzbeamte`, `posts/i06_2026-10-26_insider_schaetzung`, `posts/i07_2026-10-26_insider_kontrollmitteilung`, `…`
- 17:09 ✍️ Fach-Reels 32–57 zurück auf Originalton (Klangabgleich verworfen), Insider #01 mit kombinierten Mikros ([`82a09f2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/82a09f27d86bef4b9c1a30f19311b153341529b8))
  - `posts/32_2026-10-23_reel_mindeststeuer`, `posts/33_2026-10-24_reel_paragraf_formel`, `posts/34_2026-10-25_reel_einspruch`, `posts/38_2026-10-27_reel_pruefpfad`, `posts/39_2026-10-28_reel_holding`, `posts/40_2026-10-28_reel_formeln`, `…`
- 17:07 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`c903e7c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c903e7c93426a19c53da81cb170e3cd88f8e8bf4))
- 17:07 ✍️ Stimme: beide Handy-Mikros per Frequenzweiche kombiniert (rechts Präsenz, links S-Laute/Höhen ab 7 kHz) – Insider #08 neu ([`edb226d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/edb226d36d8615190f1de83a5aeec7d0ade6f88d))
  - `aufnahmen/2026-10-26/geschnitten/I10_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I11_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I12_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I1_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I2_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I3_roh.wav`, `…`
- 17:02 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`b49f4f4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b49f4f40f6814734f15e52f393410456f7792135))
- 17:02 ✍️ Stimme klingt wieder natürlich: nur Hauptmikro statt Stereo→Mono (Kammfilter um 1–1,5 kHz), keine Entrauschung/De-Esser/EQ – Insider #08 neu ([`1c1a12d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1c1a12ddc3bc2c3794a2b0b7e84f2bfc393bb5f8))
  - `aufnahmen/2026-10-26/geschnitten/I10_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I11_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I12_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I1_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I2_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I3_roh.wav`, `…`
- 16:48 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`02b8737`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/02b87376363065ba03360a0782856730e35d4181))
- 16:48 ✍️ Fach-Reels 32–57: Stimme mit Klangabgleich neu abgemischt (Bild unverändert, −18 LUFS) ([`0411999`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/04119991d85e0b9a355eac89f3f401b66da6598f))
  - `posts/32_2026-10-23_reel_mindeststeuer`, `posts/33_2026-10-24_reel_paragraf_formel`, `posts/34_2026-10-25_reel_einspruch`, `posts/38_2026-10-27_reel_pruefpfad`, `posts/39_2026-10-28_reel_holding`, `posts/40_2026-10-28_reel_formeln`, `…`
- 16:46 ✍️ reel_bauen --nur-ton: Bild-Zwischenkopie im Temp-Ordner statt reel_alt.mp4 (versionierte Sicherungen bleiben erhalten) ([`125c0ab`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/125c0abf883f2ce4cdb069db4aff01b64e7cbb35))
  - `vorlagen/system/premium/reel_bauen.py`
- 16:40 🔀 Merge claude/instagram ([`8141ba6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8141ba63549bc0bb44e5a2ea8feaef56b91b883e))
- 16:40 ✍️ Insider #01–#12: Stimme mit Klangabgleich neu abgemischt (klar statt dumpf), Lage aktualisiert ([`a147798`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a147798754ae475a670d17d33de0c7cdab7fa52b))
  - `LAGE.html`, `posts/i01_2026-10-26_insider_programm`, `posts/i02_2026-10-26_insider_kontenabruf`, `posts/i03_2026-10-26_insider_einspruch_0euro`, `posts/i04_2026-10-26_insider_saeumnis`, `posts/i05_2026-10-26_insider_finanzbeamte`, `…`
- 16:38 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`d6eff0a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d6eff0a694fdaa4a71e4e14d75fbc78323a7806b))
- 16:38 ✍️ Klangabgleich statt festem EQ: Stimme wird pro Aufnahme an eine Sprach-Zielkurve angeglichen (Loch um 1 kHz gefüllt, Bass-Wummern raus) – Insider #08 neu ([`ba85d3f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ba85d3f222e5070e6b54864314d929c2db5f4224))
  - `posts/i08_2026-10-26_insider_rente_oma`, `vorlagen/system/premium/klang.py`, `vorlagen/system/premium/reel_bauen.py`
- 16:33 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`fef40a2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fef40a2b47e6d5a8fa1ef25f52083e1afb3762f7))
- 16:32 ✍️ Insider #01–#12: Stimme mit Klang-EQ neu abgemischt (klarer, weniger dumpf) ([`3e25ff5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3e25ff5db88b7cc31d8e3dcbdbd271b918a14451))
  - `posts/i01_2026-10-26_insider_programm`, `posts/i02_2026-10-26_insider_kontenabruf`, `posts/i03_2026-10-26_insider_einspruch_0euro`, `posts/i04_2026-10-26_insider_saeumnis`, `posts/i05_2026-10-26_insider_finanzbeamte`, `posts/i06_2026-10-26_insider_schaetzung`, `…`
- 16:29 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`ec7d6c6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ec7d6c61655463198fad379657521ff13bffb762))
- 16:29 ✍️ Klang-EQ für Loris' Stimme (weniger Wummern, mehr Präsenz) – Insider #08 neu abgemischt ([`6db3afb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6db3afb62e15a1deecca9c5efe20de593293a962))
  - `posts/i08_2026-10-26_insider_rente_oma`, `vorlagen/system/premium/reel_bauen.py`
- 16:16 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`97d1611`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/97d161192e513c18431f94119dced33f65bd7e74))
- 16:16 ✍️ Insider #08: Pfeilspitze sitzt auf der Linie, Meldung läuft als Datenpaket zum Finanzamt (Bewegung im Hook) ([`07d3b1b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/07d3b1b284aa1f7ce7f3c71a69d6b1e28a6559d8))
  - `posts/i08_2026-10-26_insider_rente_oma`, `vorlagen/system/premium/insider_08.html`
- 16:05 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`73ae8b7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/73ae8b72239b4001b25235c4c4a92b7ed7cef511))
- 16:05 ✍️ Sprechtexte: Serie „Steuer-Spickzettel“ S1–S5 als Reels (Zahlen 2026 geprüft); neue herr_tech-Beispiele kritisch bewertet (20_wissen) ([`fafdcb5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fafdcb56aad68e65628fd4bc372ab9243660506a))
  - `posts/sprechtexte.md`, `strategie/20_wissen_motion.md`
- 15:24 ✍️ Plan: heute 17:45 Insider #08 Oma-Rente (viralstes Thema zuerst), Reihenfolge nach Viral-Potenzial; #08 Zähler 12.348 € rechtzeitig fertig ([`4ca6c15`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4ca6c15e41d972449461fe185ebe379ce7ec6669))
  - Plan: `37-karussell-bp-vorbereitung` zeit: 2026-10-28 17:45 → 2026-11-08 17:45; `41-karussell-mythen` zeit: 2026-11-08 17:45 → 2026-10-28 17:45; `i01-reel-insider-programm` zeit: 2026-10-26 17:45 → 2026-10-30 17:45; `i02-reel-insider-kontenabruf` zeit: 2026-10-30 17:45 → 2026-11-03 17:45; `i04-reel-insider-saeumnis` zeit: 2026-11-03 17:45 → 2026-11-05 17:45; `i06-reel-insider-schaetzung` zeit: 2026-11-05 17:45 → 2026-10-31 17:45; `i07-reel-insider-kontrollmitteilung` zeit: 2026-11-06 17:45 → 2026-11-07 17:45; `i08-reel-insider-rente-oma` zeit: 2026-10-29 17:45 → 2026-10-26 17:45; `i09-reel-insider-elterngeld` zeit: 2026-10-31 17:45 → 2026-10-29 17:45; `i10-reel-insider-belege` zeit: 2026-11-07 17:45 → 2026-11-06 17:45
- 15:20 🔀 Merge claude/instagram ([`c2f3688`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c2f3688f6604299e5f9fb629a87bc13a42afbb8d))
- 15:20 ✍️ Wissen 26.10.: Motion-Vokabular (14 Effekte) + motion.js, Karussell-Vorlage mit „Der alte Weg“, Vorher/Nachher, Mono-Box, Speichern-Hinweis ([`77a9ac2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/77a9ac29ea70e1a8c15deda4d2baa1bbe40af50c))
  - `LAGE.html`, `automatik/lage_notizen.md`, `strategie/20_wissen_motion.md`, `vorlagen/system/premium/karussell.html`, `vorlagen/system/premium/motion.js`
- 14:12 ✍️ Plan: Finanzamt-Insider #01–#12 täglich 17:45 ab 26.10. (Karussells Mi/So), Fach-Reels ab 12.11. – alle Insider-Reels fertig (Premium, Stimme 26.10.) ([`9825e3e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9825e3edc2f27b92b3649414f8cdfd280ef923f2))
  - Plan: neu `i02-reel-insider-kontenabruf` (2026-10-30 17:45, freigegeben); neu `i03-reel-insider-einspruch-0euro` (2026-11-02 17:45, freigegeben); neu `i04-reel-insider-saeumnis` (2026-11-03 17:45, freigegeben); neu `i05-reel-insider-finanzbeamte` (2026-10-27 17:45, freigegeben); neu `i06-reel-insider-schaetzung` (2026-11-05 17:45, freigegeben); neu `i07-reel-insider-kontrollmitteilung` (2026-11-06 17:45, freigegeben); neu `i08-reel-insider-rente-oma` (2026-10-29 17:45, freigegeben); neu `i09-reel-insider-elterngeld` (2026-10-31 17:45, freigegeben); neu `i10-reel-insider-belege` (2026-11-07 17:45, freigegeben); neu `i11-reel-insider-anrufen` (2026-11-09 17:45, freigegeben); neu `i12-reel-insider-mbs-excel` (2026-11-10 17:45, freigegeben); `32-reel-mindeststeuer` zeit: 2026-11-14 17:45 → 2026-11-30 17:45; `33-reel-paragraf-formel` zeit: 2026-11-16 17:45 → 2026-12-01 17:45; `34-reel-einspruch` zeit: 2026-11-02 17:45 → 2026-12-03 17:45; `34-story-tipp` zeit: 2026-11-02 17:50 → 2026-12-03 17:50; `38-reel-pruefpfad` zeit: 2026-10-31 17:45 → 2026-11-20 17:45; `39-reel-holding` zeit: 2026-11-09 17:45 → 2026-11-21 17:45; `40-reel-formeln` zeit: 2026-11-03 17:45 → 2026-11-13 17:45; `43-reel-par35` zeit: 2026-11-10 17:45 → 2026-11-24 17:45; `45-reel-vga` zeit: 2026-11-05 17:45 → 2026-11-14 17:45; `48-reel-firmenwagen` zeit: 2026-10-30 17:45 → 2026-11-16 17:45; `49-reel-kleinunternehmer` zeit: 2026-11-11 17:45 → 2026-11-17 17:45; `50-reel-gebaeude-afa` zeit: 2026-11-07 17:45 → 2026-11-19 17:45; `52-reel-gobd` zeit: 2026-10-27 17:45 → 2026-11-12 17:45; `53-reel-iab` zeit: 2026-11-06 17:45 → 2026-11-26 17:45; `54-reel-reverse-charge` zeit: 2026-10-29 17:45 → 2026-11-23 17:45; `55-reel-thesaurierung` zeit: 2026-11-12 17:45 → 2026-11-27 17:45; `57-reel-verlust-8c` zeit: 2026-11-13 17:45 → 2026-11-28 17:45
- 14:12 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`c339dd9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c339dd9b7b0cb7b5110cde9ddc71853e6d6f8f21))
- 14:09 ✍️ Finanzamt-Insider: Zwischenstand Gruppe A ([`612fcc5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/612fcc5593e9ce03408f43cb80b9d3d9cb7a66aa))
  - `posts/i05_2026-10-26_insider_finanzbeamte`, `posts/i08_2026-10-26_insider_rente_oma`
- 14:05 ✍️ Finanzamt-Insider #07/#10/#11/#12 fertig (Premium) ([`d67cc9c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d67cc9ceae232c0d60539507813935dea67f866e))
  - `posts/i12_2026-10-26_insider_mbs_excel`
- 14:05 ✍️ Finanzamt-Insider: Zwischenstand (in Arbeit) ([`99a498d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/99a498d66d2a4e4b9ecdfe1e4053b6d762b789f7))
  - `posts/i02_2026-10-26_insider_kontenabruf`, `posts/i05_2026-10-26_insider_finanzbeamte`, `posts/i07_2026-10-26_insider_kontrollmitteilung`, `posts/i08_2026-10-26_insider_rente_oma`, `posts/i10_2026-10-26_insider_belege`, `posts/i11_2026-10-26_insider_anrufen`, `…`
- 14:01 ✍️ Finanzamt-Insider #03/#04/#06/#09 + Zwischenstand übrige (Premium, pausiert bis Einplanung) ([`7bebcfc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7bebcfc059a633f3b4c8b780d3480eb5037513e4))
  - `posts/i02_2026-10-26_insider_kontenabruf`, `posts/i03_2026-10-26_insider_einspruch_0euro`, `posts/i04_2026-10-26_insider_saeumnis`, `posts/i05_2026-10-26_insider_finanzbeamte`, `posts/i06_2026-10-26_insider_schaetzung`, `posts/i07_2026-10-26_insider_kontrollmitteilung`, `…`
- 14:01 ✍️ Plan: Finanzamt-Insider #01 heute 17:45 (Premium, Stimme 26.10.), Kleinunternehmer verschoben ([`fa6a66c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fa6a66cfeaf27e1fd2f381896a2d5abe337148b5))
  - Plan: neu `i01-reel-insider-programm` (2026-10-26 17:45, freigegeben); `49-reel-kleinunternehmer` zeit: 2026-10-26 17:45 → 2026-11-11 17:45
- 14:01 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`c61f5f8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c61f5f88a22ea1182c4cddc33786b8d30b0d5b33))
- 13:45 ✍️ Aufnahme 26.10. geschnitten: 12 Insider-Stimmen (nur vollständige Anläufe, Atmer gedämpft, −16 LUFS), Post-Ordner i01–i12 angelegt ([`6e989b9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6e989b9dc90b454777ba8ac883ce6a7423ba7a70))
  - `aufnahmen/2026-10-26/chunks.json`, `aufnahmen/2026-10-26/geschnitten/I10_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I11_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I12_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I1_roh.wav`, `aufnahmen/2026-10-26/geschnitten/I2_roh.wav`, `…`
- 13:30 ✍️ Aufnahme 26.10.: Finanzamt-Insider I1–I12 (Rohdatei) ([`9358fc0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9358fc0998ffdfb99a0759c33cd9a768b7075584))
  - `aufnahmen/2026-10-26/insider_roh.mp3`
- 08:48 📈 Statistik 2026-10-26 ([`d7efd2a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d7efd2a4a3aefe3291f2506eb1891091b50dea3e))
  - `automatik/statistik`
- 08:43 📡 Radar 2026-10-26: 8 Beiträge, 0 DM-Entwürfe ([`ac086f8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ac086f8093203858f0fc334d76adc99653e36ed8))
  - `automatik/interaktion`
- 08:38 ✍️ Plan: heute 17:45 Kleinunternehmer statt Einspruch (breiteres Publikum), Einspruch auf Mo 02.11., Prüfpfad auf Sa 31.10. (Platzhalter für Insider-Reel) ([`c4a35ae`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c4a35aece96fe6724e1ebe5f8e6ba75a0d834732))
  - Plan: `34-reel-einspruch` zeit: 2026-10-26 17:45 → 2026-11-02 17:45; `34-story-tipp` zeit: 2026-10-26 17:50 → 2026-11-02 17:50; `38-reel-pruefpfad` zeit: 2026-11-02 17:45 → 2026-10-31 17:45; `49-reel-kleinunternehmer` zeit: 2026-10-31 17:45 → 2026-10-26 17:45
- 08:38 ✍️ Sprechtexte: Serie „Finanzamt-Insider“ I1–I12 (breites Publikum, Teilen-CTA, Normen geprüft 26.10.) für Aufnahme heute ([`e66c71e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e66c71eb4c1fe717ef7e64d8bd1b1d22b774d7fa))
  - `posts/sprechtexte.md`
- 03:54 ✍️ Plan: Gläsern-Reel als veröffentlicht nachgetragen (online seit 22.10., Link von Loris) ([`f4a6fa7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f4a6fa72b7bed214dee8ebac0997bf9a0bbadf4c))
  - Plan: `62-reel-glaesern` status: manuell → veroeffentlicht; `62-reel-glaesern` zeit: 2026-10-25 11:45 → 2026-10-22 11:50; `62-reel-glaesern` online: https://www.instagram.com/reel/DezHdgPt1_0/

**So 25.10.2026**
- 19:52 ✍️ Wochenbericht KW 2026-43 ([`1c85f7c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1c85f7cbe983760378f83fe49f650c88bc79905e))
  - `automatik/statistik`
- 17:45 🤖 Autopilot: 30-reel-gwg veroeffentlicht ([`18985ac`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/18985acdcd47117f5cca25aefec87eca830f46b5))
  - Plan: `30-reel-gwg` status: freigegeben → veroeffentlicht; `30-reel-gwg` online: https://www.instagram.com/reel/De7JF3cAGrX/
- 17:30 🤖 Autopilot: Dateien fuer 30-reel-gwg vorbereitet ([`eca3899`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/eca3899de9103af4b9552d9cb9588972f44436b4))
  - `posts/30_2026-10-21_reel_gwg`
- 13:00 🔀 Merge pull request #87 from MBS-maehrsteuern/claude/instagram-radar-fix-27vc78 ([`72804de`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/72804de651e3402354f1745c3ef092444654bbfa))
- 12:59 ✍️ LAGE: Stand von claude/instagram übernehmen (volle Historie) ([`447f7b4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/447f7b4d0a5a298f811f93f3cf8bc94924c270aa))
  - `LAGE.html`
- 12:59 🔀 Merge claude/instagram in Radar-Fix ([`06b8d49`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/06b8d495682517b58a54b0584b984f60028517a9))
- 12:59 🔀 Merge claude/instagram in Radar-Fix ([`62be6f9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/62be6f94a125008672de04c70ac59e2c55aad059))
- 12:57 🔀 Merge claude/instagram ([`b7a4354`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b7a4354cee3f1a01623665fbb8264ac06583240b))
- 12:57 ✍️ Benachrichtigungen: Issues erwähnen @maehrsteuern statt der Organisation ([`4081a21`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4081a219cafdf06f930625a5deddc319d844a76b))
  - `LAGE.html`, `automatik/freigabe.py`, `automatik/kommentare.py`, `automatik/lage_notizen.md`, `automatik/linkedin.py`, `automatik/radar.py`, `…`
- 12:57 ✍️ Erinnerung: Reel-Aufnahme Sa 07.11. 10:00 (Kalender), Sprechtexte bis Do 05.11.; Reel 50 von Loris bestätigt ([`de2f0ee`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/de2f0ee2565658be04791374f5bf71b6f34abae6))
  - `LAGE.html`, `automatik/erinnerungen.json`, `automatik/plan.json`
- 12:47 🔀 Merge claude/instagram ([`d04efe7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d04efe7b1e6f8d159253839b51fccac96c731b6d))
- 12:47 ✍️ Takt: 1 Feed-Beitrag pro Tag um 17:45 (Reel täglich, Karussell Mi + So) nach Auswertung – Plan bis 02.12. umgestellt, Lage-Raster/Soll angepasst ([`72b7045`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/72b70450d61630c532767223de16e6087f39127b))
  - Plan: `31-karussell-zinsschranke` zeit: 2026-10-28 17:45 → 2026-11-11 17:45; `32-reel-mindeststeuer` zeit: 2026-11-08 17:45 → 2026-11-14 17:45; `10-e-rechnung` zeit: 2026-10-27 11:45 → 2026-11-04 17:45; `33-reel-paragraf-formel` zeit: 2026-11-07 17:45 → 2026-11-16 17:45; `34-reel-einspruch` zeit: 2026-10-26 11:45 → 2026-10-26 17:45; `34-story-tipp` zeit: 2026-10-26 12:15 → 2026-10-26 17:50; `37-karussell-bp-vorbereitung` zeit: 2026-10-26 17:45 → 2026-10-28 17:45; `38-reel-pruefpfad` zeit: 2026-11-02 11:45 → 2026-11-02 17:45; `39-reel-holding` zeit: 2026-11-03 17:45 → 2026-11-09 17:45; `40-reel-formeln` zeit: 2026-10-28 11:45 → 2026-11-03 17:45; `41-karussell-mythen` zeit: 2026-10-29 11:45 → 2026-11-08 17:45; `43-reel-par35` zeit: 2026-11-05 17:45 → 2026-11-10 17:45; `44-karussell-glossar` zeit: 2026-10-31 17:45 → 2026-11-22 17:45; `45-reel-vga` zeit: 2026-10-29 17:45 → 2026-11-05 17:45; `46-karussell-dividenden-8b` zeit: 2026-11-04 17:45 → 2026-11-29 17:45; `48-reel-firmenwagen` zeit: 2026-10-30 11:45 → 2026-10-30 17:45; `49-reel-kleinunternehmer` zeit: 2026-10-31 11:45 → 2026-10-31 17:45; `50-reel-gebaeude-afa` zeit: 2026-11-01 11:45 → 2026-11-07 17:45; `51-karussell-kapitalertraege` zeit: 2026-11-03 11:45 → 2026-11-25 17:45; `53-reel-iab` zeit: 2026-11-06 11:45 → 2026-11-06 17:45; `54-reel-reverse-charge` zeit: 2026-11-04 11:45 → 2026-10-29 17:45; `53-karussell-iab` zeit: 2026-10-30 17:45 → 2026-11-15 17:45; `55-reel-thesaurierung` zeit: 2026-11-07 11:45 → 2026-11-12 17:45; `56-karussell-verjaehrung` zeit: 2026-11-02 17:45 → 2026-11-18 17:45; `57-reel-verlust-8c` zeit: 2026-11-06 17:45 → 2026-11-13 17:45; `59-karussell-pensionen` zeit: 2026-11-05 11:45 → 2026-12-02 17:45
- 12:31 ✍️ Plan: alle 11 Premium-Karussells freigegeben (go Loris) – bis 08.11. täglich 1 Reel + 1 Karussell ([`0a6d403`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0a6d403798675fee3f9a9f824a84f9b973420de4))
  - Plan: `31-karussell-zinsschranke` status: pausiert → freigegeben; `10-e-rechnung` status: pausiert → freigegeben; `35-karussell-steuerkalender` status: pausiert → freigegeben; `41-karussell-mythen` status: pausiert → freigegeben; `44-karussell-glossar` status: pausiert → freigegeben; `46-karussell-dividenden-8b` status: pausiert → freigegeben; `51-karussell-kapitalertraege` status: pausiert → freigegeben; `53-karussell-iab` status: pausiert → freigegeben; `56-karussell-verjaehrung` status: pausiert → freigegeben; `59-karussell-pensionen` status: pausiert → freigegeben
- 12:30 ✍️ Premium-Karussells 41/44/46/51: Zwischenstand (in Arbeit, pausiert) ([`25b794f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/25b794fc22544e7e45011d5c7ad0db682aad0236))
  - `posts/41_2026-10-29_mythen`, `posts/44_2026-10-30_glossar`, `posts/46_2026-11-01_dividenden_8b`, `posts/51_2026-11-03_kapitalertraege`, `vorlagen/system/premium/karussells/p46_dividenden_8b.json`, `vorlagen/system/premium/karussells/p51_kapitalertraege.json`
- 12:30 ✍️ Premium-Karussells 10, 31, 35, 53, 56, 59 umgebaut (Inhalte unverändert, alte Folien als *_alt.png) ([`c75f013`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c75f0136f7da294b8fdf2a87bfe9b5a86f2dab0d))
  - `posts/10_2026-10-22_e_rechnung`, `posts/31_2026-10-22_zinsschranke`, `posts/35_2026-10-25_steuerkalender`, `posts/53_2026-11-04_iab`, `posts/56_2026-11-06_verjaehrung`, `posts/59_2026-11-08_pensionen`, `…`
- 12:29 🔀 Merge claude/instagram ([`38eed99`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/38eed9909465b96720334765ca00b9987354da9b))
- 12:29 ✍️ Plan: ab 26.10. täglich 1 Reel + 1 Karussell bis 08.11.; Karussell 37 (Premium) Mo 26.10. 17:45 freigegeben, übrige Karussell-Termine reserviert ([`acbb62e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/acbb62e825d65040adf8bbc4f16e1770c4973b8e))
  - Plan: `31-karussell-zinsschranke` zeit: 2026-10-22 11:45 → 2026-10-28 17:45; `32-reel-mindeststeuer` zeit: 2026-11-02 11:45 → 2026-11-08 17:45; `10-e-rechnung` zeit: 2026-10-23 17:45 → 2026-10-27 11:45; `33-reel-paragraf-formel` zeit: 2026-11-02 17:45 → 2026-11-07 17:45; `35-karussell-steuerkalender` zeit: 2026-10-25 17:45 → 2026-11-01 17:45; `37-karussell-bp-vorbereitung` status: pausiert → freigegeben; `37-karussell-bp-vorbereitung` zeit: 2026-10-27 11:45 → 2026-10-26 17:45; `38-reel-pruefpfad` zeit: 2026-10-27 17:45 → 2026-11-02 11:45; `39-reel-holding` zeit: 2026-10-28 17:45 → 2026-11-03 17:45; `40-reel-formeln` zeit: 2026-10-27 11:45 → 2026-10-28 11:45; `43-reel-par35` zeit: 2026-10-29 17:45 → 2026-11-05 17:45; `44-karussell-glossar` zeit: 2026-10-30 17:45 → 2026-10-31 17:45; `45-reel-vga` zeit: 2026-10-28 11:45 → 2026-10-29 17:45; `46-karussell-dividenden-8b` zeit: 2026-11-01 11:45 → 2026-11-04 17:45; `51-karussell-kapitalertraege` zeit: 2026-11-03 17:45 → 2026-11-03 11:45; `52-reel-gobd` zeit: 2026-10-26 17:45 → 2026-10-27 17:45; `53-reel-iab` zeit: 2026-10-30 17:45 → 2026-11-06 11:45; `54-reel-reverse-charge` zeit: 2026-10-29 11:45 → 2026-11-04 11:45; `53-karussell-iab` zeit: 2026-11-05 17:45 → 2026-10-30 17:45; `55-reel-thesaurierung` zeit: 2026-10-31 17:45 → 2026-11-07 11:45; `56-karussell-verjaehrung` zeit: 2026-11-06 17:45 → 2026-11-02 17:45; `57-reel-verlust-8c` zeit: 2026-11-01 17:45 → 2026-11-06 17:45; `59-karussell-pensionen` zeit: 2026-11-08 17:45 → 2026-11-05 11:45
- 12:28 ✍️ Premium-Karussell: Vorlage + Renderer (vorlagen/system/premium/karussell.*), erstes Karussell 37 Betriebsprüfung umgebaut ([`b201b83`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b201b83d9971896363cee7e1051403915f87b1d4))
  - `posts/37_2026-10-27_bp_vorbereitung`, `vorlagen/system/premium/karussell.html`, `vorlagen/system/premium/karussell.mjs`, `vorlagen/system/premium/karussells/p37_bp_vorbereitung.json`
- 12:25 🔀 Merge claude/instagram ([`c228a9c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c228a9cc9db23f8650c4f5758af4031ba2cc3aff))
- 12:25 ✍️ Premium: erstes Bild von 43, 50, 52 nachgebessert (Ergebnis ab Frame 0, Titelbild neu) ([`f789a7f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f789a7f3c598900d737137bbf8cb877bae400f52))
  - `posts/52_2026-11-04_reel_gobd`
- 12:24 ✍️ Premium: Nachbesserung 52 (Zwischenstand, in Arbeit) ([`a114097`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a114097c0e863e7915ccd30c72a0cb50a7378e74))
  - `posts/43_2026-10-30_reel_par35`, `posts/50_2026-11-03_reel_gebaeude_afa`, `posts/52_2026-11-04_reel_gobd`
- 12:23 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`ba48ed9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ba48ed9978cdb66ce740c0fec19a4164d42f4a5f))
- 12:23 ✍️ Plan: Reihenfolge nach Wochentag neu – So 25.10. 17:45 GWG (Wochenende + Montag), Einspruch Mo 11:45, alle Reels bis Mo 02.11. umgestellt ([`6c06a02`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6c06a02bb38da31c4dce23976d6c4058243485bf))
  - Plan: `30-reel-gwg` zeit: 2026-10-29 11:45 → 2026-10-25 17:45; `33-reel-paragraf-formel` zeit: 2026-11-01 11:45 → 2026-11-02 17:45; `34-reel-einspruch` zeit: 2026-10-25 17:45 → 2026-10-26 11:45; `34-story-tipp` zeit: 2026-10-25 17:50 → 2026-10-26 12:15; `38-reel-pruefpfad` zeit: 2026-10-27 11:45 → 2026-10-27 17:45; `40-reel-formeln` zeit: 2026-10-28 11:45 → 2026-10-27 11:45; `43-reel-par35` zeit: 2026-10-30 17:45 → 2026-10-29 17:45; `45-reel-vga` zeit: 2026-10-27 17:45 → 2026-10-28 11:45; `49-reel-kleinunternehmer` zeit: 2026-10-26 17:45 → 2026-10-31 11:45; `50-reel-gebaeude-afa` zeit: 2026-11-02 17:45 → 2026-11-01 11:45; `52-reel-gobd` zeit: 2026-10-26 11:45 → 2026-10-26 17:45; `53-reel-iab` zeit: 2026-10-31 11:45 → 2026-10-30 17:45; `54-reel-reverse-charge` zeit: 2026-10-29 17:45 → 2026-10-29 11:45
- 12:19 ✍️ Premium: Nachbesserung 43/50/52 (Zwischenstand, in Arbeit) ([`e0c5f3b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e0c5f3b8d215dee2a239f452b853dd0d91b9c501))
  - `posts/50_2026-11-03_reel_gebaeude_afa`
- 12:18 ✍️ Premium: Nachbesserung erstes Bild 43/50/52 (Zwischenstand, in Arbeit) ([`11c0d3c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/11c0d3cddbb3e4e25a34011778a9eefe82235675))
  - `vorlagen/system/premium/gebaeude.html`, `vorlagen/system/premium/gobd.html`, `vorlagen/system/premium/par35.html`
- 12:18 🔀 Merge claude/instagram (Statistik/Radar 25.10.) in Arbeitsbranch ([`11faab8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/11faab8463f8ee081977d35d95f029b2d5b6077f))
- 12:15 ✍️ Plan: 16 Premium-Reels mit Stimme freigegeben (volle Freigabe Loris), Mo 26.10.–Mo 02.11. je 11:45 + 17:45 ([`393c2f8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/393c2f89767457a12faceda2d361f892f803ff12))
  - Plan: `30-reel-gwg` status: pausiert → freigegeben; `30-reel-gwg` zeit: 2026-10-21 11:45 → 2026-10-29 11:45; `32-reel-mindeststeuer` status: pausiert → freigegeben; `32-reel-mindeststeuer` zeit: 2026-10-23 11:45 → 2026-11-02 11:45; `33-reel-paragraf-formel` status: pausiert → freigegeben; `33-reel-paragraf-formel` zeit: 2026-10-26 11:45 → 2026-11-01 11:45; `38-reel-pruefpfad` status: pausiert → freigegeben; `38-reel-pruefpfad` zeit: 2026-10-27 17:45 → 2026-10-27 11:45; `39-reel-holding` status: pausiert → freigegeben; `39-reel-holding` zeit: 2026-10-28 11:45 → 2026-10-28 17:45; `40-reel-formeln` status: pausiert → freigegeben; `40-reel-formeln` zeit: 2026-10-28 17:45 → 2026-10-28 11:45; `43-reel-par35` status: pausiert → freigegeben; `43-reel-par35` zeit: 2026-10-30 11:45 → 2026-10-30 17:45; `45-reel-vga` status: pausiert → freigegeben; `45-reel-vga` zeit: 2026-10-31 17:45 → 2026-10-27 17:45; `48-reel-firmenwagen` status: pausiert → freigegeben; `48-reel-firmenwagen` zeit: 2026-11-02 11:45 → 2026-10-30 11:45; `49-reel-kleinunternehmer` status: pausiert → freigegeben; `49-reel-kleinunternehmer` zeit: 2026-11-02 17:45 → 2026-10-26 17:45; `50-reel-gebaeude-afa` status: pausiert → freigegeben; `50-reel-gebaeude-afa` zeit: 2026-11-03 11:45 → 2026-11-02 17:45; `52-reel-gobd` status: pausiert → freigegeben; `52-reel-gobd` zeit: 2026-11-04 11:45 → 2026-10-26 11:45; `53-reel-iab` status: pausiert → freigegeben; `53-reel-iab` zeit: 2026-11-04 17:45 → 2026-10-31 11:45; `54-reel-reverse-charge` status: pausiert → freigegeben; `54-reel-reverse-charge` zeit: 2026-11-05 11:45 → 2026-10-29 17:45; `55-reel-thesaurierung` status: pausiert → freigegeben; `55-reel-thesaurierung` zeit: 2026-11-06 11:45 → 2026-10-31 17:45; `57-reel-verlust-8c` status: pausiert → freigegeben; `57-reel-verlust-8c` zeit: 2026-11-07 17:45 → 2026-11-01 17:45
- 11:50 ✍️ Premium-Look: Reels 30, 32, 33, 38, 39 umgebaut – alle 16 Reels im Premium-Look, pausiert bis go ([`55b43d8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/55b43d8ecf438155fcd0ada381ed75770615b1cd))
  - `posts/30_2026-10-21_reel_gwg`, `posts/33_2026-10-24_reel_paragraf_formel`, `posts/38_2026-10-27_reel_pruefpfad`, `posts/39_2026-10-28_reel_holding`
- 11:45 ✍️ Premium-Look: Zwischenstand Gruppe A (in Arbeit, pausiert) ([`1627072`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/16270729b802eb635b1ee15ff09a149267a78d5d))
  - `posts/30_2026-10-21_reel_gwg`, `posts/33_2026-10-24_reel_paragraf_formel`, `posts/38_2026-10-27_reel_pruefpfad`
- 11:44 ✍️ Premium-Look: Reels 52, 53, 54, 55, 57 umgebaut, weiter pausiert ([`af89878`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/af898784e0253c495babff89296c229926d1c140))
  - `posts/52_2026-11-04_reel_gobd`, `posts/53_2026-11-04_iab`, `posts/54_2026-11-05_reel_reverse_charge`, `posts/55_2026-11-06_reel_thesaurierung`, `posts/57_2026-11-07_reel_verlust_8c`
- 11:40 ✍️ Premium-Look: Zwischenstand Gruppen A/C (in Arbeit, pausiert) ([`fa8ae2b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fa8ae2be78130d78faa7cf12de924b5a055b9a5b))
  - `posts/30_2026-10-21_reel_gwg`, `posts/32_2026-10-23_reel_mindeststeuer`, `posts/33_2026-10-24_reel_paragraf_formel`, `posts/52_2026-11-04_reel_gobd`, `posts/53_2026-11-04_iab`, `posts/54_2026-11-05_reel_reverse_charge`, `…`
- 11:39 ✍️ Premium-Look: Reels 40, 43, 45, 48, 49, 50 umgebaut (Hook-Animation, Takt 2,5–4 s, leise Töne, CTA TOOL), weiter pausiert ([`eecb5b6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/eecb5b6c7c850d25d597d0dd1e152f48831cf6dc))
  - `posts/40_2026-10-28_reel_formeln`, `posts/43_2026-10-30_reel_par35`, `posts/45_2026-10-31_reel_vga`, `posts/48_2026-11-02_reel_firmenwagen`, `posts/49_2026-11-02_reel_kleinunternehmer`, `posts/50_2026-11-03_reel_gebaeude_afa`, `…`
- 11:17 ✍️ Plan: Reel Einspruch (Premium) So 25.10. 17:45 + Tipp-Story 17:50 freigegeben (go Loris), Steuerkalender-Karussell verschoben ([`4543583`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/45435838d1f908d33cc76dbef19219a882473efc))
  - Plan: `34-reel-einspruch` status: pausiert → freigegeben; `34-reel-einspruch` zeit: 2026-10-25 11:45 → 2026-10-25 17:45; `34-story-tipp` status: pausiert → freigegeben; `34-story-tipp` zeit: 2026-10-25 12:15 → 2026-10-25 17:50
- 11:15 ✍️ Reel Einspruch: Töne leiser, Übergang jetzt dezenter Karten-Swipe aus der Bibliothek statt Whoosh (Loris) ([`cca0c91`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/cca0c9125947b156680e9bb9474e28578d1add3c))
  - `LAGE.html`, `posts/34_2026-10-25_reel_einspruch`, `vorlagen/system/premium/reel_bauen.py`, `vorlagen/system/premium/sfx.py`
- 10:59 ✍️ Sound-Bibliothek komplett: 39 Runway-Musikstücke + 60 Runway-Töne, Notizen + Lage aktualisiert ([`ca63919`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ca6391985ccb455b2843b8aaf5d12e6579de97ab))
  - `LAGE.html`, `automatik/lage_notizen.md`
- 10:59 ✍️ Sound-Bibliothek: Runway-Zwischenstand ([`86f0b19`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/86f0b19494fe09259dcb2a7968ca688ee506fd56))
  - `musik/QUELLEN_runway.md`, `musik/katalog_runway.json`
- 10:58 ✍️ Sound-Bibliothek: 60 Musikstücke + 40 Töne CC0 aus dem Internet Archive (Lizenz je Item geprüft, Quellen + Katalog) ([`1bf0b71`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1bf0b711206e1594380eca0d24a6b18775d928ca))
  - `musik/QUELLEN_cc0.md`, `musik/atmo/cc0/201_button_klick1.mp3`, `musik/atmo/cc0/202_button_klick2.mp3`, `musik/atmo/cc0/203_button_klick3.mp3`, `musik/atmo/cc0/204_button_klick4.mp3`, `musik/atmo/cc0/205_menue_move1.mp3`, `…`
- 10:54 ✍️ Sound-Bibliothek: Zwischenstand (Runway + CC0, noch in Arbeit) ([`e5c7c37`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e5c7c3718c76f93a509c000a47a965b1b606f6e2))
  - `musik/cc0/201_komiku_balance.mp3`, `musik/cc0/202_komiku_chillout.mp3`, `musik/cc0/203_komiku_time.mp3`, `musik/cc0/204_komiku_river.mp3`, `musik/cc0/205_komiku_frozen_jungle.mp3`, `musik/cc0/206_komiku_dreaming.mp3`, `…`
- 10:54 ✍️ Reel Einspruch: schnellerer Takt (Szenenwechsel alle 2,5–4 s, 8 statt 7 Szenen, schnellere Einblendungen, Kamerafahrt in jeder Szene, Übergangs-Sounds) ([`8c61c4e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8c61c4ebb47f8272e5c8beef3faacb83fafb21ba))
  - `LAGE.html`, `posts/34_2026-10-25_reel_einspruch`, `vorlagen/system/premium/einspruch.html`
- 10:48 ✍️ Reel Einspruch: stärkerer Hook (Kalender 05→09, „4 Tage länger“, Sounddesign) und deutlicher CTA „Kommentiere TOOL“ ([`44a8848`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/44a8848a4a32564de74604e8d373bdb3fe7f3b5e))
  - `LAGE.html`, `posts/34_2026-10-25_reel_einspruch`, `vorlagen/system/premium/einspruch.html`, `vorlagen/system/premium/reel_bauen.py`, `vorlagen/system/premium/sfx.py`
- 10:40 ✍️ Reel Einspruch als Premium-Fassung (Motion-Design-Look, HTML-Animation mit Loris' Stimme), Baukasten vorlagen/system/premium ([`15668cb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/15668cb013bac86f7140cefac215b60540b9023c))
  - `LAGE.html`, `automatik/plan.json`, `posts/34_2026-10-25_reel_einspruch`, `vorlagen/system/premium/einspruch.html`, `vorlagen/system/premium/reel_bauen.py`, `vorlagen/system/premium/rendern.mjs`
- 10:24 ✍️ Reel Einspruch: Hook auf Ergebnis (Einspruch bis 9.11.), Gläsern-Test So 25.10. 11:45 von Hand ([`03ff980`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/03ff980bfb5d8beb99fe7a26fb17c888001624d9))
  - Plan: `62-reel-glaesern` zeit: 2026-10-22 11:50 → 2026-10-25 11:45
- 09:22 📈 Statistik 2026-10-25 ([`fd47a39`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fd47a392825d31c5c791658ec71bad319ba7434f))
  - `automatik/statistik`
- 07:47 📡 Radar 2026-10-25: 8 Beiträge, 0 DM-Entwürfe ([`0997767`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0997767e1fd6edd8a6f028f3e893148e891e6b2d))
  - `automatik/interaktion`

**Sa 24.10.2026**
- 12:16 🤖 Autopilot: 36-story-tipp veroeffentlicht ([`d016057`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d016057e025c11484907b76f7b767d8a6e3c9476))
  - Plan: `36-story-tipp` status: freigegeben → veroeffentlicht; `36-story-tipp` online: https://www.instagram.com/stories/maehrsteuern/4014930017247382776
- 12:15 🤖 Autopilot: Dateien fuer 36-story-tipp vorbereitet ([`db5c340`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/db5c3406d351ba97edaa13c60282141ca4129824))
  - `posts/36_2026-10-26_reel_bewirtung`
- 12:11 ✍️ Reels 40, 43, 45, 48, 49, 50 mit Loris' Stimme neu gebaut – alle 18 Stimm-Reels fertig, pausiert bis go ([`1da326d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1da326df5edcaefd12e158b39ecb8ec9845e4073))
  - `LAGE.html`, `automatik/plan.json`, `posts/43_2026-10-30_reel_par35`, `posts/45_2026-10-31_reel_vga`, `posts/50_2026-11-03_reel_gebaeude_afa`
- 11:59 ✍️ Stimm-Reels Gruppe B: Zwischenstand (in Arbeit, alles pausiert) ([`eb94cf3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/eb94cf3734c515a1c23baa98099a55b87b4245db))
  - `posts/45_2026-10-31_reel_vga`, `posts/50_2026-11-03_reel_gebaeude_afa`
- 11:58 ✍️ Reels 30, 32, 33, 34, 38, 39 mit Loris' Stimme neu gebaut, weiter pausiert bis go ([`686d4f8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/686d4f882099196d84b99505116488de75406d14))
  - `automatik/plan.json`, `posts/38_2026-10-27_reel_pruefpfad`
- 11:54 ✍️ Stimm-Reels Gruppe A/B: Zwischenstand (in Arbeit, alles pausiert) ([`0598bfb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0598bfbed19c47aa1ea91bb4e2d340677e0a9067))
  - `posts/30_2026-10-21_reel_gwg`, `posts/32_2026-10-23_reel_mindeststeuer`, `posts/33_2026-10-24_reel_paragraf_formel`, `posts/34_2026-10-25_reel_einspruch`, `posts/38_2026-10-27_reel_pruefpfad`, `posts/39_2026-10-28_reel_holding`, `…`
- 11:54 ✍️ Reels 52–57 mit Loris' Stimme neu gebaut (Hook ab Frame 1), weiter pausiert bis go ([`47fac4e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/47fac4e732011fd22596ddbb2f1cac9af3a35c61))
  - `automatik/plan.json`, `posts/50_2026-11-03_reel_gebaeude_afa`, `posts/52_2026-11-04_reel_gobd`, `posts/53_2026-11-04_iab`, `posts/54_2026-11-05_reel_reverse_charge`, `posts/55_2026-11-06_reel_thesaurierung`, `…`
- 11:17 🤖 Autopilot: 36-reel-bewirtung veroeffentlicht ([`b15cf6e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b15cf6ee396a8decb48252e83a0327dda15325f0))
  - Plan: `36-reel-bewirtung` status: freigegeben → veroeffentlicht; `36-reel-bewirtung` online: https://www.instagram.com/reel/De3yheAFKBg/
- 11:14 ✍️ Plan: Reel Bewirtung mit Stimme freigegeben, sofort posten (go Loris), Tipp-Story 12:15 ([`880a5e9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/880a5e9f9be7796036c0293f972e5db377f7a645))
  - Plan: `36-reel-bewirtung` status: pausiert → freigegeben; `36-reel-bewirtung` zeit: 2026-10-24 11:00 → 2026-10-24 11:14; `36-story-tipp` status: pausiert → freigegeben
- 11:14 ✍️ Regel: Reels nur mit Loris' Stimme – posten.py blockiert Reels ohne stimme:true, CLAUDE.md + Wissen 24.10. ergänzt ([`48477e3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/48477e3c9675cf1a9fc75a2b6e30728bff0923a1))
  - `CLAUDE.md`, `LAGE.html`, `automatik/posten.py`, `strategie/19_wissen_2026-10-24.md`
- 11:13 ✍️ Umbau Gruppe B: Bildunterschriften 38–49 nach Wissen 24.10., Schnitt-Hooks vorbereitet (Reels werden mit Stimme neu gebaut), Lage aktualisiert ([`fd54a02`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fd54a022ddc7ad71f63cea67946eb28e7184e45a))
  - `LAGE.html`
- 11:13 ✍️ Reel Bewirtung mit Loris' Stimme neu gebaut (Fassung ohne Stimme archiviert), wartet auf go; Umbau Gruppe A+C: Bildunterschriften und Karussell-Folie 1 nach Wissen 24.10. ([`e1bd79b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e1bd79bccd1667a5325d85f47ccfaed1e8518c0f))
  - Plan: `36-reel-bewirtung` status: veroeffentlicht → pausiert; `36-story-tipp` status: freigegeben → pausiert
- 11:04 ✍️ Umbau nach Wissen 24.10. (Zwischenstand): Bildunterschriften gekürzt, Reel-Hooks ab Frame 1 – alle Beiträge weiter pausiert ([`8f8f635`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8f8f635682a66b95ff08d16520d6f57e4f653f15))
  - `posts/10_2026-10-22_e_rechnung`, `posts/20_2026-10-21_reel_erechnung`, `posts/21_2026-10-22_reel_zinsschranke`, `posts/22_2026-10-18_reel_steuersatz`, `posts/30_2026-10-21_reel_gwg`, `posts/31_2026-10-22_zinsschranke`, `…`
- 11:03 ✍️ Wissen 24.10.: Boring Content + 4-Sekunden-Test verbindlich, Notizen zum Umbau ([`caaed72`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/caaed72da49937c4ab4ea555b3a0756d8add8708))
  - `automatik/lage_notizen.md`, `strategie/19_wissen_2026-10-24.md`
- 11:03 🤖 Autopilot: 36-reel-bewirtung veroeffentlicht ([`e9ecd92`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e9ecd92f34f54c2b7b9b19c0bd0fa705f6b7385a))
  - Plan: `36-reel-bewirtung` status: freigegeben → veroeffentlicht; `36-reel-bewirtung` online: https://www.instagram.com/reel/De3w_gsoISU/
- 11:02 🤖 Autopilot: Dateien fuer 36-reel-bewirtung vorbereitet ([`966f27a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/966f27adf3d0c976219b0c482b3304284f3e7a7e))
  - `posts/36_2026-10-26_reel_bewirtung`
- 11:01 ✍️ Plan: Reel Bewirtung auf Sa 24.10. sofort vorgezogen und umgebaut (Hook 0 % ab Frame 1, kürzere Bildunterschrift), Paragraf-Formel auf Mo 26.10. ([`643e7bc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/643e7bcba24fbf475e82d5d0257eee3af17f0a01))
  - Plan: `33-reel-paragraf-formel` zeit: 2026-10-24 11:45 → 2026-10-26 11:45; `33-story-teaser` zeit: 2026-10-24 12:15 → 2026-10-26 12:15; `36-reel-bewirtung` status: pausiert → freigegeben; `36-reel-bewirtung` zeit: 2026-10-26 11:45 → 2026-10-24 11:00; `36-story-tipp` status: pausiert → freigegeben; `36-story-tipp` zeit: 2026-10-26 12:15 → 2026-10-24 12:15
- 09:15 📈 Statistik 2026-10-24 ([`0b46019`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0b46019484dc3aa186b6b29fce3232fe35d9e7a1))
  - `automatik/statistik`
- 09:14 📡 Radar 2026-10-24: 8 Beiträge, 0 DM-Entwürfe ([`b3e08cd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b3e08cdec554f5e2996078aca2d99b76bce63286))
  - `automatik/interaktion`

**Fr 23.10.2026**
- 09:27 📡 Radar 2026-10-23: 8 Beiträge, 0 DM-Entwürfe ([`ef3db1a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ef3db1ad9587cd7df5b292e285d00d8888acf4d9))
  - `automatik/interaktion`
- 09:22 📈 Statistik 2026-10-23 ([`9e117e4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9e117e4cfff38e4fb0352d6ced16d06aeba65fce))
  - `automatik/statistik`

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

<details><summary>Älter als 7 Tage</summary>

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

**Di 20.10.2026**
- 17:50 🤖 Autopilot: 28-story-aufloesung veroeffentlicht ([`73152cc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/73152cc6473f5066c434511b2e849c18052fcc76))
  - Plan: `28-story-aufloesung` status: freigegeben → veroeffentlicht; `28-story-aufloesung` online: https://www.instagram.com/stories/maehrsteuern/4012196501812014820
- 17:45 🤖 Autopilot: Dateien fuer 28-story-aufloesung vorbereitet ([`3d041f1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3d041f1b9caf1eaa1e927f77471795a02dd6e969))
  - `posts/28_2026-10-19_reel_zuschlaege`
- 17:45 🤖 Autopilot: 19-reel-verlustvortrag veroeffentlicht ([`b32dff7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b32dff711058e72d12d412fe18d8293d030b57b5))
  - Plan: `19-reel-verlustvortrag` status: freigegeben → veroeffentlicht; `19-reel-verlustvortrag` online: https://www.instagram.com/reel/DeuJJHoDXkl/
- 17:21 🤖 Autopilot: Dateien fuer 19-reel-verlustvortrag vorbereitet ([`f717de0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f717de06fdd80b8c3c7f3c72c0700c079efa4cb5))
  - `posts/19_2026-10-20_reel_verlustvortrag`
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
- 07:28 📡 Radar 2026-10-20: 8 Beiträge, 0 DM-Entwürfe ([`aba45c8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/aba45c8dfd569198a5c5929be3f2b8668d6aa705))
  - `automatik/interaktion`

**Mo 19.10.2026**
- 19:26 🤖 Autopilot: 18-reel-aufbewahrung veroeffentlicht ([`0e93a0d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0e93a0d136d815e4bb611d9ef14e9513d3fb00e6))
  - Plan: `18-reel-aufbewahrung` status: freigegeben → veroeffentlicht; `18-reel-aufbewahrung` online: https://www.instagram.com/reel/DeryoWUE_Or/
- 19:25 🤖 Autopilot: Dateien fuer 18-reel-aufbewahrung vorbereitet ([`6eae2ca`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6eae2ca71f2a557899258f763c3a7ef8a10fbbe5))
  - `posts/18_2026-10-19_reel_aufbewahrung`
- 16:02 📈 Statistik 2026-10-19 ([`9665ae7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9665ae7c4dee9510e80f9ff4f131dccb3103a02e))
  - `automatik/statistik`
- 12:52 🤖 Autopilot: 28-story-quiz veroeffentlicht ([`763f070`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/763f070c7bcc9dba81c81f1079675e9c43910469))
  - Plan: `28-story-quiz` status: freigegeben → veroeffentlicht; `28-story-quiz` online: https://www.instagram.com/stories/maehrsteuern/4011324194198123089
- 12:52 🤖 Autopilot: Dateien fuer 28-story-quiz vorbereitet ([`c5c60d2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c5c60d2a27160e56fd6e0891709216b39f5f2ee9))
  - `posts/28_2026-10-19_reel_zuschlaege`
- 12:52 🤖 Autopilot: 28-reel-zuschlaege veroeffentlicht ([`4bc0642`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4bc0642194080491d56295e23dcedbef22847669))
  - Plan: `28-reel-zuschlaege` status: freigegeben → veroeffentlicht; `28-reel-zuschlaege` online: https://www.instagram.com/reel/DerFcnnnTMT/
- 12:51 🤖 Autopilot: Dateien fuer 28-reel-zuschlaege vorbereitet ([`be13455`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/be134558a4708e9b7b578b6c16ba66e3da812a1d))
  - `posts/28_2026-10-19_reel_zuschlaege`
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
- 12:31 🤖 Autopilot: 05-latente-steuern veroeffentlicht ([`afefee6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/afefee6abd0848ee8dd8f942b12ce1abb8428d36))
  - Plan: `05-latente-steuern` status: freigegeben → veroeffentlicht; `05-latente-steuern` online: https://www.instagram.com/p/DeRTLb4EYwd/
- 11:15 🤖 Autopilot: Dateien fuer 05-latente-steuern vorbereitet ([`7e99d1f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7e99d1f35b6ee4e5bace79c97ba157adf8023f33))
  - `posts/05_2026-10-08_latente_steuern`
- 08:48 📈 Statistik 2026-10-09 ([`177eda4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/177eda42043631c50f2998d39d777203aafded82))
  - `automatik/statistik`
- 07:05 📡 Radar 2026-10-09: 8 Beiträge, 0 DM-Entwürfe ([`0c9c6fc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0c9c6fc3bc9e991c600d222579b7668cf1aba5c4))
  - `automatik/interaktion`

**Do 08.10.2026**
- 19:35 🤖 Autopilot: 06-story-teaser veroeffentlicht ([`7cfed5a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7cfed5abd434681ce018f0a123c80eb0491cf57b))
  - Plan: `06-story-teaser` status: freigegeben → veroeffentlicht; `06-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4003554454352185254
- 19:08 ✍️ Testmonat-Auswertung im Tagesbericht, plan.json mit stimme/hook, Fabrik 3× pro Woche ([`6dcd8c7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6dcd8c7968a14def4aa8cfc32248471bac62075b))
  - `LAGE.html`, `automatik/berichte`, `automatik/insights_voll.py`, `automatik/plan.json`, `automatik/tagesbericht.py`, `strategie/06_auswertung.md`, `…`
- 19:05 ✍️ Story-Quiz zum Antippen, Bio-Vorschlag mit Nutzen-Satz, Highlight „Start“ ([`582aabb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/582aabb34e1bf44982ef8bd91f90189188ed7e89))
  - `LAGE.html`, `automatik/plan.json`, `posts/09_2026-10-15_rueckstellung`, `strategie/02_bio_highlights.md`, `vorlagen/system/jobs/p09_story_quiz_tippen.json`
- 19:03 ✍️ Routine Tagesbericht: neues Prompt mit Zugangsschritt, Kalender-Hinweis und Commit-Regel ([`ae0777f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ae0777fc08b87f56cdd5028499638a2259597158))
  - `automatik/routinen`
- 18:40 ✅ Freigabe #44: go ([`390a66d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/390a66d43e28766dca308d7cc17a1895ec1b215e))
  - Plan: `04-story-frage` status: entwurf → freigegeben; `04-story-teaser` status: entwurf → freigegeben
- 18:31 🤖 Autopilot: Dateien fuer 06-story-teaser vorbereitet ([`6385791`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/63857917ff22592ef62b18671eddd2ec800ab2cb))
  - `posts/02_2026-10-06_excel_fehler`
- 16:05 📈 Statistik 2026-10-08 ([`55edf34`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/55edf34f548269184f9d3f6591adc15b0fa278db))
  - `automatik/statistik`
- 15:51 ✅ Freigabe angefragt (1 Beitrag/Beiträge) ([`16ff123`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/16ff12330f13313cdcc95c89bc9c5e1678a73dc5))
  - Plan: `04-story-frage` → Freigabe-Issue #44; `04-story-teaser` → Freigabe-Issue #44
- 15:50 ✍️ Tagesbericht: Methoden-Check erst ab 48 h, Reel-Länge, Heute-geplant-Liste ([`66cd01e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/66cd01eeed24ffb7d1e20811b6ed4e75635cdb1d))
  - `automatik/berichte`, `automatik/tagesbericht.py`
- 15:49 🔀 Merge pull request #43 from maehrsteuern/claude/focused-shannon-hrtyy7 ([`776c97e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/776c97e9409d714980d146efb4985e72337dd4f3))
- 15:41 🔀 Merge claude/instagram (Radar 08.10.), Lage neu erzeugt ([`79694ed`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/79694edad1b8dd49d7dd25953fabff045db1f649))
- 14:55 ✍️ Split-Reel in Edits geplant (Do 08.10. 19:30) ([`c90e7bb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c90e7bb0f50dfe1d7d148cb9fe5f45e83073ea1f))
  - `LAGE.html`, `automatik/plan.json`
- 14:30 ✍️ Reel Nr. 2 Zeile: Einstieg „Jutta hat schon wieder …“ wieder drin ([`a41e46c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a41e46c5119a4b5bbd1b7de8d949e786cd365b45))
  - `LAGE.html`, `automatik/plan.json`, `posts/12_2026-10-09_reel_zeile`, `vorlagen/system/schnitt/p12_reel_zeile_0810.json`, `vorlagen/system/schnitt/reels_0810_bauen.py`
- 14:03 📡 Radar 2026-10-08: 8 Beiträge, 0 DM-Entwürfe ([`a059875`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a059875b857f4f56170661b32248ffd76e3404a9))
  - `automatik/interaktion`
- 11:20 ✍️ Reels mit Loris' Stimme fertig: 8 Reels, ab heute täglich 19:30 (Edits, manuell) ([`eadde9e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/eadde9ec7f24e21028ced687f424ad20eedf2851))
  - Plan: `05-latente-steuern` zeit: 2026-10-09 19:30 → 2026-10-09 12:30; `05-story-teaser` zeit: 2026-10-09 19:35 → 2026-10-09 12:35; `12-reel-zeile` status: wartet_auf_sprachnachricht → manuell; `12-reel-zeile` zeit: 2026-10-12 19:30 → 2026-10-09 19:30; `08-reel-kst-staffel` status: freigegeben → manuell; `13-reel-verknuepfung` status: wartet_auf_sprachnachricht → manuell; `13-reel-verknuepfung` zeit: 2026-10-16 19:30 → 2026-10-11 19:30; `14-reel-versionen` status: wartet_auf_sprachnachricht → manuell; `14-reel-versionen` zeit: 2026-10-18 19:30 → 2026-10-12 19:30; `03-gewst-hinzurechnung` zeit: 2026-10-13 19:30 → 2026-10-13 12:30; `03-story-teaser` zeit: 2026-10-13 19:35 → 2026-10-13 12:35; `15-reel-rechnungsnummern` status: wartet_auf_sprachnachricht → manuell; `15-reel-rechnungsnummern` zeit: 2026-10-20 19:30 → 2026-10-13 19:30; `09-rueckstellung` zeit: 2026-10-15 19:30 → 2026-10-15 12:30; `09-story-teaser` zeit: 2026-10-15 19:35 → 2026-10-15 12:35; `04-story-frage` zeit: 2026-10-26 12:15 → 2026-10-15 18:00; `16-reel-listen` status: wartet_auf_sprachnachricht → manuell; `16-reel-listen` zeit: 2026-10-22 19:30 → 2026-10-15 19:30; `04-reel-mein-weg` status: wartet_auf_sprachnachricht → manuell; `04-reel-mein-weg` zeit: 2026-10-27 19:30 → 2026-10-16 19:30; `04-story-teaser` zeit: 2026-10-27 19:35 → 2026-10-16 19:35
- 10:53 ✍️ Add files via upload ([`57a5004`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/57a5004dc3b20c04644e78bcb86e3b07fd2ff393))
  - `08.10.2026 10.38.mp3`, `08.10.2026 10.39.mp3`, `08.10.2026 10.41.mp3`, `08.10.2026 10.42(2).mp3`, `08.10.2026 10.42.mp3`, `08.10.2026 10.43(2).mp3`, `…`
- 10:51 ✍️ Lage neu erzeugt (Sitzungsstart 08.10.) ([`9baf27e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9baf27eb474eb8da24c86eda1ebd0a45fdec6343))
  - `LAGE.html`
- 08:48 📈 Statistik 2026-10-08 ([`7abdbc6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7abdbc6f628d3ff57b68e0630f6c833f8da9bff0))
  - `automatik/statistik`
- 07:05 📡 Radar 2026-10-08: 8 Beiträge, 0 DM-Entwürfe ([`24a5a4f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/24a5a4ffd0c8dc898c67f078a9bce7f64a4ba470))
  - `automatik/interaktion`

**Mi 07.10.2026**
- 19:35 🤖 Autopilot: 02-story-teaser veroeffentlicht ([`e476372`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e476372f52ceb6d0bc4bee2debcd9b34867e3ac9))
  - Plan: `02-story-teaser` status: freigegeben → veroeffentlicht; `02-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4002829658245043420
- 19:32 🤖 Autopilot: Dateien fuer 02-story-teaser vorbereitet ([`abc4d88`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/abc4d88f198aa0cf7fba3cb751486cb4235ce6ab))
  - `posts/02_2026-10-06_excel_fehler`
- 19:32 🤖 Autopilot: 02-excel-fehler veroeffentlicht ([`1e9ba27`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1e9ba27479847ba2022ae3b4cd03e91954f8155a))
  - Plan: `02-excel-fehler` status: freigegeben → veroeffentlicht; `02-excel-fehler` online: https://www.instagram.com/p/DeM5u1vGLsR/
- 16:34 ✍️ Bibliothek Runden 5 und 6: 400 Assets (jetzt 996) ([`722b914`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/722b9140f6ff0cbcc8fce8cb4eec2087cdad236f))
  - `LAGE.html`, `README.md`, `assets/bibliothek/PRUEFBERICHT.md`, `assets/bibliothek/README.md`, `assets/bibliothek/bausteine/abspann_frist.png`, `assets/bibliothek/bausteine/abspann_plausi.png`, `…`
- 16:02 ✍️ Bibliothek Runde 7: MBS-Reels (10 Titel, 4 Einblendungen) ([`070fd3b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/070fd3b4a71c53a5b19c0cdf439b18642f30e189))
  - `LAGE.html`, `README.md`, `assets/bibliothek/README.md`, `assets/bibliothek/bausteine/mbs_abspann_demo.png`, `assets/bibliothek/bausteine/mbs_haken_baum.png`, `assets/bibliothek/bausteine/mbs_haken_ueber_ampel.png`, `…`
- 15:57 📈 Statistik 2026-10-07 ([`4a88e46`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4a88e46e8170ddfc9874c707f10498163fa293fa))
  - `automatik/statistik`
- 13:48 📡 Radar 2026-10-07: 8 Beiträge, 0 DM-Entwürfe ([`60f7657`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/60f76576125ce2bb92dcf47d8139fbd84f33690b))
  - `automatik/interaktion`
- 12:15 🤖 Autopilot: 05-story-frage veroeffentlicht ([`9709ca9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9709ca9674c2c5decabc5e417c2cabe3ec52fed2))
  - Plan: `05-story-frage` status: freigegeben → veroeffentlicht; `05-story-frage` online: https://www.instagram.com/stories/maehrsteuern/4002608197877985940
- 11:00 🤖 Autopilot: Dateien fuer 05-story-frage vorbereitet ([`a8342f2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a8342f2bcef7afa73ebcde2c8b2e0e4b17cf81ec))
  - `posts/05_2026-10-08_latente_steuern`
- 08:47 📈 Statistik 2026-10-07 ([`281779f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/281779f62c7d99ba9a9f36191ffec48836d91250))
  - `automatik/statistik`
- 07:05 📡 Radar 2026-10-07: 8 Beiträge, 0 DM-Entwürfe ([`b4bb83c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b4bb83c7f8f93671ce6847808a8dc4b36ec6b407))
  - `automatik/interaktion`

**Di 06.10.2026**
- 21:10 ✍️ Titelbild-Vorlage „Excel vs. Code“ (titel_split.html) für das Split-Reel – Varianten zur Auswahl ([`45579b6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/45579b6ad03fb20a6d2c3452a98444a2a89f3800))
  - `posts/02_2026-10-06_excel_fehler`, `vorlagen/system/render.mjs`, `vorlagen/system/titel_split.html`
- 21:07 ✍️ montage.py: stumme Tonspur behoben – Split- und KSt-Reel mit Ton neu gerendert ([`1413df2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1413df2f4329f7f252b56cdf8ce5d3f77e9f012b))
  - `LAGE.html`, `automatik/lage_notizen.md`, `posts/02_2026-10-06_excel_fehler`, `posts/08_2026-10-09_reel_kst_staffel`, `vorlagen/system/montage.py`
- 20:50 ✍️ Reel-Serie: komplett fertig liefern (inkl. Musik), Loris lädt über Edits hoch ([`e490c8d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e490c8d24f38c8e94696626468fed05fcd5c2718))
  - `LAGE.html`, `automatik/lage_notizen.md`, `automatik/plan.json`
- 20:49 ✍️ Stand claude/instagram übernommen ([`a1fda23`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a1fda236acc2b7523259e14a26b6d07a183bf706))
- 20:49 ✍️ Reel-Takt alle 2 Tage bis 24.10.: 6 neue Reel-Slots + 5 Sprechtexte (Serie Nummer 2–5 + Verknüpfung) ([`ac88455`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ac884553c77ec5411a0e2dc8ce4ee97ac4ed083f))
  - Plan: neu `12-reel-zeile` (2026-10-12 19:30, wartet_auf_sprachnachricht); neu `13-reel-verknuepfung` (2026-10-16 19:30, wartet_auf_sprachnachricht); neu `14-reel-versionen` (2026-10-18 19:30, wartet_auf_sprachnachricht); neu `15-reel-rechnungsnummern` (2026-10-20 19:30, wartet_auf_sprachnachricht); neu `16-reel-listen` (2026-10-22 19:30, wartet_auf_sprachnachricht); neu `17-reel-kommentare` (2026-10-24 19:30, wartet_auf_sprachnachricht); `10-story-umfrage` zeit: 2026-10-21 12:15 → 2026-10-22 12:15; `10-e-rechnung` zeit: 2026-10-22 19:30 → 2026-10-23 19:30; `10-story-teaser` zeit: 2026-10-22 19:35 → 2026-10-23 19:35; `04-story-frage` zeit: 2026-10-19 12:15 → 2026-10-26 12:15; `04-reel-mein-weg` zeit: 2026-10-20 19:30 → 2026-10-27 19:30; `04-story-teaser` zeit: 2026-10-20 19:35 → 2026-10-27 19:35
- 20:45 📈 Statistik: Schnellabruf einzelner Beiträge (nur Protokoll, keine Dateien) ([`a028389`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a028389fd39fec8aeefb0d76ec5acecd5ee5fb2c))
  - `.github/workflows`, `automatik/beitrag_jetzt.py`
- 20:44 ✍️ Edits-Test: Split-Reel Do 08.10. von Loris in Edits (manuell), Woche verschoben ([`ea2ce8f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ea2ce8fa74a159a7beb35cbfcc8accc9c6499de3))
  - Plan: `06-reel-split` status: freigegeben → manuell; `06-reel-split` zeit: 2026-10-11 19:30 → 2026-10-08 19:30; `06-story-teaser` zeit: 2026-10-11 19:35 → 2026-10-08 19:35; `05-latente-steuern` zeit: 2026-10-08 19:30 → 2026-10-09 19:30; `05-story-teaser` zeit: 2026-10-08 19:35 → 2026-10-09 19:35; `08-story-heute` zeit: 2026-10-09 12:15 → 2026-10-10 12:15; `08-reel-kst-staffel` zeit: 2026-10-09 19:30 → 2026-10-10 19:30; `08-story-rueckblick` zeit: 2026-10-10 12:15 → 2026-10-11 12:15
- 19:35 🤖 Autopilot: 11-story-teaser veroeffentlicht ([`461142e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/461142eef2e2d6b5a0a87e5afc8355fe1aef4e4d))
  - Plan: `11-story-teaser` status: freigegeben → veroeffentlicht; `11-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4002104878277412503
- 19:33 🤖 Autopilot: Dateien fuer 11-story-teaser vorbereitet ([`ee11a38`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ee11a38228eba20470b2a90f856cc2ef92c0ad70))
  - `posts/11_2026-10-07_reel_monatsbericht`
- 19:30 🤖 Autopilot: 11-reel-monatsbericht veroeffentlicht ([`cc1c6cd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/cc1c6cdf9569ac208f740249a8bce31a07f9392e))
  - Plan: `11-reel-monatsbericht` status: freigegeben → veroeffentlicht; `11-reel-monatsbericht` online: https://www.instagram.com/reel/DeKUuvPgA1W/
- 18:15 🤖 Autopilot: Dateien fuer 11-reel-monatsbericht vorbereitet ([`1ffae8c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1ffae8c0517ab28cf932f749de5a62628339f0f3))
  - `posts/11_2026-10-07_reel_monatsbericht`
- 15:39 📈 Statistik 2026-10-06 ([`7b45a11`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7b45a114620537823b44d3d9103db877910dbc23))
  - `automatik/statistik`
- 14:03 📡 Radar 2026-10-06: 8 Beiträge, 0 DM-Entwürfe ([`53d5ace`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/53d5acee2585587251978ea768430868550bbc18))
  - `automatik/interaktion`
- 09:28 ✅ Freigabe #36: go (Loris im Chat) – Monatsbericht-Reel + Teaser heute 19:30/19:35 ([`e6f5338`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e6f533880a1a424a48be4f029b68285e534eaa66))
  - Plan: `11-reel-monatsbericht` status: entwurf → freigegeben; `11-story-teaser` status: entwurf → freigegeben
- 09:22 ✍️ Monatsbericht-Reel: Pausen mit Raumton statt digitaler Stille, feste Verstärkung statt loudnorm ([`5652c08`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5652c08b40452b44bdb9c362759387ba44985cd7))
  - `posts/11_2026-10-07_reel_monatsbericht`, `vorlagen/system/schnitt/p11_reel_monatsbericht.json`, `vorlagen/system/schnitt/p11_reel_monatsbericht_bauen.py`
- 09:12 ✍️ Monatsbericht-Reel Version 3: dritte Aufnahme (09:02), Atmer stumm – zur Freigabe für heute 19:30 ([`3d9f5d9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3d9f5d977c9e214072fc5a846127b73ff315dee4))
  - Plan: `11-reel-monatsbericht` status: wartet_auf_sprachnachricht → entwurf
- 08:59 ✍️ Monatsbericht-Reel: wartet wieder auf Sprachnachricht (dritte Aufnahme) ([`d3176b8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d3176b8cc85a301be61b969d890f34d927c78f00))
  - Plan: `11-reel-monatsbericht` status: entwurf → wartet_auf_sprachnachricht
- 08:57 ✍️ Monatsbericht-Reel: Atmer zwischen den Sätzen stummgeschaltet ([`79237c6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/79237c6f549d8b3e182f581a210face1009b783a))
  - `posts/11_2026-10-07_reel_monatsbericht`
- 08:43 📈 Statistik 2026-10-06 ([`368b30b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/368b30bd09a7ab618ce159a6ad38de68edf1876e))
  - `automatik/statistik`
- 08:41 ✍️ Rohaufnahme Monatsbericht v2 aus dem Repo genommen (nur fertiger Schnitt bleibt öffentlich) ([`2dd3db2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2dd3db2e541627df46c62c3e8b4f7973e918e953))
  - `posts/11_2026-10-07_reel_monatsbericht`
- 08:40 ✍️ Monatsbericht-Reel Version 2: neue Aufnahme, neuer Hook, heute Di 06.10. – Karussell Excel-Fehler auf Mi 07.10. ([`2985d86`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2985d86376a25f5ed42a02296819c73dbb53acda))
  - Plan: `11-reel-monatsbericht` status: wartet_auf_sprachnachricht → entwurf; `11-reel-monatsbericht` zeit: 2026-10-07 19:30 → 2026-10-06 19:30; `11-story-teaser` zeit: 2026-10-07 19:35 → 2026-10-06 19:35; `02-excel-fehler` zeit: 2026-10-06 19:30 → 2026-10-07 19:30; `02-story-teaser` zeit: 2026-10-06 19:35 → 2026-10-07 19:35
- 08:14 ✍️ Stand claude/instagram übernommen ([`f4e5a6f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f4e5a6fc5b878181908df23ed69461eac79acc43))
- 08:14 ✍️ Sprechtext Monatsbericht neu: kürzer, lockerer, stärkerer Hook („Zwei Stunden. Jeden Monat.“) ([`61689c3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/61689c353aae2043cd1da047291a9c13bf2e045c))
  - `LAGE.html`, `posts/sprechtexte.md`
- 08:13 ✍️ Monatsbericht-Reel: wartet wieder auf Sprachnachricht (Loris nimmt neu auf) ([`843b8d1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/843b8d10aa19018cedbfc94c5c2a5b19f0e254fa))
  - Plan: `11-reel-monatsbericht` status: entwurf → wartet_auf_sprachnachricht
- 07:05 📡 Radar 2026-10-06: 8 Beiträge, 0 DM-Entwürfe ([`ffe8206`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ffe8206f9e4374e897b90f4e3832155b384c2bca))
  - `automatik/interaktion`

**Mo 05.10.2026**
- 21:39 ✍️ Monatsbericht-Reel auf Mi 07.10. vorgezogen (Follow-up zum 5-Dinge-Reel), Split-Reel auf So 11.10. ([`4f65efd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4f65efdd295d4130154d8206b85409f2f38b638f))
  - Plan: `11-reel-monatsbericht` zeit: 2026-10-11 19:30 → 2026-10-07 19:30; `11-story-teaser` zeit: 2026-10-11 19:35 → 2026-10-07 19:35; `06-reel-split` zeit: 2026-10-07 19:30 → 2026-10-11 19:30; `06-story-teaser` zeit: 2026-10-07 19:35 → 2026-10-11 19:35
- 18:20 ✅ Freigabe angefragt (1 Beitrag/Beiträge) ([`c745b43`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c745b43fac15981b8c5d90711dbc29ab11892ee6))
  - Plan: `11-reel-monatsbericht` → Freigabe-Issue #36; `11-story-teaser` → Freigabe-Issue #36
- 18:18 ✍️ Reel Monatsbericht auf Nummer 11 umbenannt (Kollision mit Fabrik-Beitrag 09 Rückstellung) ([`b194a17`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b194a1754ae37fc1833ba4e73594092788ae09c5))
  - Plan: neu `11-reel-monatsbericht` (2026-10-11 19:30, entwurf); neu `11-story-teaser` (2026-10-11 19:35, entwurf); entfernt `09-reel-monatsbericht`
- 18:17 ✅ Freigabe angefragt (1 Beitrag/Beiträge) ([`87c407c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/87c407cb4ceffb24ce06dc0d79472937e95f0d0f))
  - Plan: `09-reel-monatsbericht` → Freigabe-Issue #35; `09-story-teaser` → Freigabe-Issue #35; `09-story-quiz` → Freigabe-Issue #35; `09-story-aufloesung` → Freigabe-Issue #35; `09-rueckstellung` → Freigabe-Issue #35
- 18:17 ✍️ Reel 11.10. „Nummer 1: Der Monatsbericht“ geschnitten – zur Freigabe ([`cfc83cc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/cfc83cc2a55c097f6dfddf72a7ea2dfade7cf107))
  - Plan: `09-reel-monatsbericht` status: wartet_auf_sprachnachricht → entwurf
- 17:17 📈 Statistik 2026-10-05 ([`a785838`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a785838ecb2a55609596407a52204986a168b3e9))
  - `automatik/statistik`
- 14:17 💼 LinkedIn-Pakete: 10-e-rechnung ([`6ff6d3c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6ff6d3c82581dc188f2ad622cf6dd6b52bd0269d))
  - `posts/10_2026-10-22_e_rechnung`
- 14:17 📡 Radar 2026-10-05: 8 Beiträge, 0 DM-Entwürfe ([`6f78e52`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6f78e52ac0bae4745576201e56a4ba4e376a8ede))
  - `automatik/interaktion`
- 12:15 🤖 Autopilot: 02-story-umfrage veroeffentlicht ([`61dad15`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/61dad15cd99d4e4ee1f15b5a3ae17cacec13c781))
  - Plan: `02-story-umfrage` status: freigegeben → veroeffentlicht; `02-story-umfrage` online: https://www.instagram.com/stories/maehrsteuern/4001158648931891388
- 11:00 🤖 Autopilot: Dateien fuer 02-story-umfrage vorbereitet ([`dc7f4d4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/dc7f4d46478243f426a7bdc2245de6512b8cfdb2))
  - `posts/02_2026-10-06_excel_fehler`
- 10:10 🔀 Merge pull request #32 from maehrsteuern/claude/sweet-newton-56icda ([`4aef643`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4aef643f42aeae8410a34b2be6074cbcb9f67031))
- 10:04 ✍️ Lage-Seite: Pages-Paket je Versuch eindeutig benennen ([`b0d954d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b0d954dd50ff5ac191e0c5bc363850805a183eb3))
  - `.github/workflows`
- 09:15 ✍️ Bibliothek Runde 4: 217 neue Assets aus dem Brand Kit (jetzt 582) ([`6f7ccb5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6f7ccb559d09ff18e0cb292e44c7694c6178ad33))
  - `LAGE.html`, `README.md`, `assets/bibliothek/PRUEFBERICHT.md`, `assets/bibliothek/README.md`, `assets/bibliothek/bausteine/abspann_getestet.png`, `assets/bibliothek/bausteine/abspann_paragraf.png`, `…`
- 09:13 ✅ Freigabe #31: go ([`fc33faf`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fc33faf70167f966ac3f31f801fbb370ec70f21e))
  - Plan: `10-story-umfrage` status: entwurf → freigegeben; `10-e-rechnung` status: entwurf → freigegeben; `10-story-teaser` status: entwurf → freigegeben
- 09:06 ✍️ Stand claude/instagram übernommen ([`53b4eaf`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/53b4eaf085e3b802e2b0e1698a2b6d6a4eedf704))
- 09:06 ✍️ Reel 11.10. Monatsbericht: Bilder (3 Schritte), Titelbild, Teaser, Bildunterschrift, Drehbuch ([`b197f71`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b197f7113caee3b60e3dc3c002797a50e42b5b7c))
  - `LAGE.html`, `posts/09_2026-10-11_reel_monatsbericht`, `posts/sprechtexte.md`, `vorlagen/system/fuenf_dinge.html`, `vorlagen/system/jobs/p09_reel_monatsbericht.json`
- 09:05 ✅ Freigabe angefragt (1 Beitrag/Beiträge) ([`8ca2ae2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8ca2ae236f636b31dfadd9054c658953f92cc3a4))
  - Plan: `10-story-umfrage` → Freigabe-Issue #31; `10-e-rechnung` → Freigabe-Issue #31; `10-story-teaser` → Freigabe-Issue #31
- 09:05 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-e6f8d1b2-zd8pzn ([`c77b202`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c77b2029d7d18815b0e9539038a26353f2166d13))
- 09:05 ✍️ Erste Bibliothek-Beiträge eingeplant: Rückstellung (15.10.) und E-Rechnung (22.10.) ([`14efa48`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/14efa482bd2af59d6966f30dc6ae35c5eca2a9f1))
  - Plan: neu `09-story-quiz` (2026-10-14 12:15, entwurf); neu `09-story-aufloesung` (2026-10-15 12:15, entwurf); neu `09-rueckstellung` (2026-10-15 19:30, entwurf); neu `09-story-teaser` (2026-10-15 19:35, entwurf); neu `10-story-umfrage` (2026-10-21 12:15, entwurf); neu `10-e-rechnung` (2026-10-22 19:30, entwurf); neu `10-story-teaser` (2026-10-22 19:35, entwurf)
- 09:03 ✍️ Reel So 11.10. eingeplant: „Nummer 1: Der Monatsbericht“ (wartet auf Sprachnachricht) ([`dc36957`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/dc369579b6a2ad1835017ac59cf1e0fe1137e099))
  - Plan: neu `09-reel-monatsbericht` (2026-10-11 19:30, wartet_auf_sprachnachricht); neu `09-story-teaser` (2026-10-11 19:35, entwurf)
- 09:03 ✍️ Lage-Notiz: globaler Reclaim-Puffer 10 Min. entschieden ([`384fa87`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/384fa8755b9dfe73c4f34ad54f00d77a0846f180))
  - `LAGE.html`, `automatik/lage_notizen.md`
- 09:02 🔀 Merge remote-tracking branch 'origin/claude/instagram' into claude/instagram ([`ff02a11`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ff02a11e25af47725737b0578a24172525306ca7))
- 09:02 ✍️ Lage-Notiz: Chrome-Check Sprint 2 eingetragen – nur Testbuchung und Puffer offen ([`4afac31`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4afac31f1821607173ab39a0fc86320728a251c1))
  - `LAGE.html`, `automatik/lage_notizen.md`
- 09:02 🔀 Merge remote-tracking branch 'origin/claude/instagram' into claude/instagram ([`322e9a0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/322e9a0f68abb1e6c8cfc94fd5c361e53fe38a23))
- 09:02 💼 LinkedIn Excel-Fehler: Punkt 1 um KSt-Senkung ab 2028 ergänzt ([`e2566fb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e2566fb480b207cb97497a659f0e616290ba79e0))
  - `LAGE.html`, `posts/02_2026-10-06_excel_fehler`
- 09:01 🔀 Merge remote-tracking branch 'origin/claude/instagram' into instagram-merge ([`93ebbbf`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/93ebbbfad07e8fe0dd9864ffd9c6151db587c386))
- 09:01 ✍️ Bibliothek: 25 Zweifelsfälle entschieden und umgesetzt ([`9c2dcd6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9c2dcd64d6c93ec74e5adb0491d2ef39c2f32014))
  - `LAGE.html`, `assets/bibliothek/PRUEFBERICHT.md`, `assets/bibliothek/bausteine/haken_8b.png`, `assets/bibliothek/karussell/bewirtung/folie_05.png`, `assets/bibliothek/karussell/e_rechnung/folie_03.png`, `assets/bibliothek/karussell/examen/folie_01.png`, `…`
- 08:56 ✍️ Latente Steuern Folie 6: Hinweis zu kleinen Kapitalgesellschaften präzisiert ([`e0329b6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e0329b680ce9146b3c3876400c272a2511656c16))
  - `LAGE.html`, `automatik/lage_notizen.md`, `posts/05_2026-10-08_latente_steuern`, `vorlagen/system/jobs/p05_latente_steuern.json`
- 08:54 ✍️ Prüfzettel latente Steuern: Punkte 4–5 geprüft, Box Folie 6 zur Entscheidung ([`f92e962`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f92e96267a45ac4725e3f0247683590b002cd476))
  - `LAGE.html`, `automatik/lage_notizen.md`, `posts/05_2026-10-08_latente_steuern`
- 08:51 ✍️ Prüfzettel latente Steuern: Punkte 1–3 mit Quellen geprüft ([`ac252f8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ac252f80ce0dc6a0d87aa1d8b5c975bd4fa4a80a))
  - `LAGE.html`, `automatik/lage_notizen.md`, `posts/05_2026-10-08_latente_steuern`
- 08:47 📈 Statistik 2026-10-05 ([`db0069d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/db0069da35cb6b2d766db3757f07a80d67c9001c))
  - `automatik/statistik`
- 08:47 🔀 Merge: Bibliothek gegengelesen (10 Korrekturen, Prüfbericht) ([`686ac1b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/686ac1bfb2362e5b9bf0745eb19ff13b6ac1c796))
- 08:39 ✍️ Bibliothek gegengelesen: 10 Korrekturen, 25 Zweifelsfälle im Prüfbericht ([`d3ee26f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d3ee26f6780915231a438dacbce0b5cddb704709))
  - `LAGE.html`, `assets/bibliothek/PRUEFBERICHT.md`, `assets/bibliothek/einzelposts/zahl_zinsen.png`, `assets/bibliothek/karussell/e_rechnung/folie_03.png`, `assets/bibliothek/karussell/forschungszulage/folie_03.png`, `assets/bibliothek/karussell/gewst_zahlen/folie_04.png`, `…`
- 08:31 ✍️ Lage-Notiz: latente Steuern auf „spätestens jetzt“ umgestellt ([`fde2ac9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fde2ac984d3a7f1056f4f3cbec8c577b76ac6f81))
  - `LAGE.html`, `automatik/lage_notizen.md`
- 08:29 🔀 Merge remote-tracking branch 'origin/claude/instagram' into claude/instagram ([`a465237`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a4652376cdd635f24d23f9d1da551b6e32c8da58))
- 08:29 💼 LinkedIn-Paket latente Steuern: „Abschluss 2026“ → „spätestens jetzt“ ([`f3959e2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f3959e2020519cf14d0f0930ddac914db5066b55))
  - `LAGE.html`, `posts/05_2026-10-08_latente_steuern`
- 08:29 ✍️ Lage-Notiz: Puffer 10 Min. am Demo-Link als offener Chrome-Schritt ([`b444ec7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b444ec7b5dcc7c5b647219ede693ccc5b9bf8f35))
  - `LAGE.html`, `automatik/lage_notizen.md`
- 08:29 🔀 Merge remote-tracking branch 'origin/claude/instagram' into claude/instagram ([`c364a4e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c364a4eacdad154f62e5d7b8663483c242213f4f))
- 08:28 🔀 Merge branch 'claude/instagram' of https://github.com/maehrsteuern/Instagram-maehrsteuern into claude/instagram ([`85a1dfd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/85a1dfd6974909865ccd70e2981a3796672f54a3))
- 08:27 ✍️ Wochenbericht: Demo-Zahlen aus Reclaim-Pflichtfeld + Kalender, dm_tracking nicht mehr angezeigt ([`714b0eb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/714b0eb0b4c9cc35d73cb7f9a5ac3d874d340d3b))
  - `LAGE.html`, `automatik/lage_notizen.md`, `automatik/wochenbericht.py`
- 08:28 🔀 Merge branch 'claude/instagram' of https://github.com/maehrsteuern/Instagram-maehrsteuern into claude/instagram ([`34127cc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/34127ccd7ac5d0ba8fc5e8a126eef22d65c9de45))
- 08:28 🔀 Merge remote-tracking branch 'origin/claude/instagram' into claude/instagram ([`ee6e233`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ee6e2334b3f6301f88ebcc09a627054c16554281))
- 08:28 🔀 Merge remote-tracking branch 'origin/claude/instagram' into claude/instagram ([`99bf365`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/99bf3657a014fa18a807313182eea9e1e49e5385))
- 08:28 ✍️ Lage-Notiz: GitHub Pages eingeschaltet, Lage-Seite läuft (erledigt) ([`be6765d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/be6765d918528c33a51ad1a07e4a9caab5ad19ff))
  - `LAGE.html`, `automatik/lage_notizen.md`
- 08:28 ✍️ Latente Steuern: „Abschluss 2026“ → „spätestens jetzt“ ([`f8fda58`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f8fda5850ec94d37c8b92b989248f2e4360936d7))
  - `LAGE.html`, `posts/05_2026-10-08_latente_steuern`, `vorlagen/system/jobs/p05_latente_steuern.json`
- 08:28 ✍️ Wochenbericht: Sonntags-Reels zählen in der Folgewoche als neu; Reel-Vergleich auf „5 Dinge“ vs. Split ([`3cb33fe`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3cb33fe0780585282727634cb1951bc61d819ce7))
  - `LAGE.html`, `automatik/erinnerungen.json`, `automatik/lage_notizen.md`, `automatik/wochenbericht.py`
- 08:27 🔀 Merge pull request #16 from maehrsteuern/claude/upbeat-goodall-huo6u7 ([`262ed48`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/262ed487ed9b2c5f9a63c5e7d9950047851bda2d))
- 08:27 🔀 Merge claude/instagram in Bibliothek-Branch: Konflikte gelöst ([`0581783`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/058178316c96c700026777ee6023c075a8d81354))
- 08:27 🔀 Merge: Lage-Notizen Kalender-Prüfung – Autopilot-Kalender in Reclaim verbunden, Freigabe/Auslöser noch gegenprüfen ([`0deb532`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0deb532118e3e94d8151e674981da7063d1b4099))
- 08:26 ✍️ Lage: Duplikat des 5-Dinge-Reels gelöscht ([`c09d6c5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c09d6c5fa749cc10f86e3b418b0f06e4964b98fe))
  - `LAGE.html`, `automatik/lage_notizen.md`
- 07:03 📡 Radar 2026-10-05: 8 Beiträge, 0 DM-Entwürfe ([`c7af627`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c7af627103cd7673c90dbc18c53d97522c1b2062))
  - `automatik/interaktion`

**So 04.10.2026**
- 21:28 📈 Statistik 2026-10-04 ([`1e9ea9e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1e9ea9ea7c92280cb4d24c0b8a6636c28d6fa5fb))
  - `automatik/statistik`
- 21:04 ✍️ Reel-Regeln: Listen-Reels hoechstens 3 Punkte, unter 20 s (Erkenntnis 5-Dinge-Reel) ([`4878531`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/48785317faa85863a94d49e61e1aab4b027e1cbe))
  - `strategie/09_reel_regeln.md`
- 20:38 📈 Statistik 2026-10-04 ([`1096968`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1096968c6b9b9a9b9156e5f097d3f95312fba9bb))
  - `automatik/statistik`
- 19:48 🤖 Autopilot: vor jedem Posten neuesten Plan holen – verhindert Doppel-Posts ([`5738537`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5738537125e7e824964b436914029f8446af3573))
  - `LAGE.html`, `automatik/lage_notizen.md`, `automatik/posten.py`
- 19:46 🤖 Autopilot: 01-story-teaser-5dinge veroeffentlicht ([`a850704`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a850704aa2a081fcd149efb9a8f2a15bbd8df45a))
  - Plan: `01-story-teaser-5dinge` status: freigegeben → veroeffentlicht; `01-story-teaser-5dinge` online: https://www.instagram.com/stories/maehrsteuern/4000661016565086455
- 19:46 🤖 Autopilot: Dateien fuer 01-story-teaser-5dinge vorbereitet ([`3b9e1ab`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3b9e1ab11b4c811de1de4d0d4e98ed69cfa2910c))
  - `posts/01_2026-10-04_reel_5dinge`
- 19:30 🤖 Autopilot: 01-reel-5dinge veroeffentlicht ([`f6ad3ab`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f6ad3ab088f3b8f0749e5dc1831c69714e06b3b3))
  - Plan: `01-reel-5dinge` status: freigegeben → veroeffentlicht; `01-reel-5dinge` online: https://www.instagram.com/reel/DeFLK53ALSs/
- 18:01 ✍️ Wochenbericht KW 2026-40 ([`3c6a4f2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3c6a4f232ad9525921acc222113685ad90c9eb41))
  - `automatik/statistik`
- 16:15 🤖 Autopilot: Dateien fuer Probelauf 01-reel-5dinge vorbereitet ([`2657c66`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2657c66bd11cb4207c840b9cb22841fdc37cee8b))
  - `posts/01_2026-10-04_reel_5dinge`
- 16:14 ✍️ Stand claude/instagram übernommen ([`3a8d366`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3a8d36658bc954aed59859eee9526d6a1d691129))
- 16:14 ✍️ Reel 04.10. umgebaut: „5 Sachen, die ich aus Excel rausgeschmissen hab“ (Community statt Werbung) ([`353300b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/353300b53859ce2859db10a565744c53c84c2d74))
  - Plan: neu `01-reel-5dinge` (2026-10-04 19:30, freigegeben); neu `01-story-teaser-5dinge` (2026-10-04 19:35, freigegeben)
- 15:54 ✍️ Ampel-Reel und Teaser 04.10. pausiert: Go zurückgenommen, wird durch Reel „5 Dinge mit Code statt Excel“ ersetzt ([`ca552b3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ca552b33fbf7c6500de59b076c41b3ff7e916f09))
  - Plan: `01-reel-ampel` status: freigegeben → pause; `01-story-teaser` status: freigegeben → pause
- 14:52 📈 Statistik 2026-10-04 ([`e5a407c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e5a407c19b52d51642910375205b1c48b17183e1))
  - `automatik/statistik`
- 13:07 📡 Radar 2026-10-04: 8 Beiträge, 0 DM-Entwürfe ([`996fe74`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/996fe74d4dbf888d86c5d28492b53f48b2ec0864))
  - `automatik/interaktion`
- 08:59 ✍️ Tagesbericht 04.10.; Vortagsvergleich jetzt Morgen gegen Morgen (Schnappschuss je Bericht) ([`4d41c01`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4d41c016723ad265a0331f9ab1350a2f5acbda92))
  - `automatik/berichte`, `automatik/tagesbericht.py`
- 08:47 📈 Statistik 2026-10-04 ([`91fa33b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/91fa33b5962d62e23d7996789d41c1b65de38ed2))
  - `automatik/statistik`
- 07:02 📡 Radar 2026-10-04: 8 Beiträge, 0 DM-Entwürfe ([`9ee31d0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9ee31d0805fd2abb5e1444972821876d9f5f3dd8))
  - `automatik/interaktion`
- 01:03 ✍️ Lage-Seite: Veröffentlichung darf scheitern, ohne die Lage rot zu färben ([`015c30e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/015c30e3dbcf0bef7616834ed5c397900c529435))
  - `.github/workflows`
- 01:03 ✍️ Lage als Seite: LAGE.html mit Kacheln, Kalender, Diagrammen und Protokoll, Veröffentlichung über GitHub Pages ([`110b299`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/110b29958834522e6296662811988d45acc5aa14))
  - `.claude/skills/lage/SKILL.md`, `.github/workflows`, `CLAUDE.md`, `LAGE.html`, `README.md`, `automatik/lage.py`, `…`
- 00:13 ✍️ LAGE.md vom Ziel-Branch übernommen (wird nach dem Merge automatisch neu erzeugt) ([`5c7f63c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5c7f63cd3015f373ddca653ec4c90f4b63605c28))
- 00:13 🔀 Merge claude/instagram in Bibliothek-Branch: Konflikte gelöst ([`978f730`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/978f730edd04156b2f0426f0b2e68001f153f180))

**Sa 03.10.2026**
- 19:52 🔀 Merge: Radar drosselfest, Wochenbericht geprüft, Fristen in Lage + Kalender ([`01b05e7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/01b05e73e2d2ae3c6aef2f8e5390e6d4ea2defbe))
- 16:35 📡 Radar drosselfest, Wochenbericht geprüft, Fristen in Lage + Kalender ([`2598e31`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2598e310de3f079372f545e40dbf050c5415fe85))
  - `automatik/erinnerungen.json`, `automatik/kalender.py`, `automatik/kalender_sync.py`, `automatik/lage.py`, `automatik/lage_notizen.md`, `automatik/radar.py`, `…`
- 14:02 📈 Statistik 2026-10-03 ([`4e9a81f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4e9a81f04f6335ce3440326acfdef106dd264738))
  - `automatik/statistik`
- 12:25 📡 Radar 2026-10-03: 8 Beiträge, 0 DM-Entwürfe, Konten −0/+10 (abgehakt) ([`d9cc42b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d9cc42b16e0f8541602b616f118d6075f54a3430))
  - `automatik/interaktion.json`, `automatik/interaktion`
- 12:15 🤖 Autopilot: 08-story-tipp veroeffentlicht ([`e36ea97`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e36ea9729d02b9bcd9389c289c388ee439254b91))
  - Plan: `08-story-tipp` status: freigegeben → veroeffentlicht; `08-story-tipp` online: https://www.instagram.com/stories/maehrsteuern/3999709094836161880
- 12:01 ✍️ Kalender-Sync optimiert + Automatik gehärtet (#23) ([`c918b6b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c918b6b08d85b6e622d80fee6e6125368bdb0ba1))
- 11:18 🔀 Merge: Neuvorstellung angepinnt, Mein Weg umkonzipieren ([`a53f609`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a53f6092c90496057f06f91c320ef6a2118c9b4d))
- 11:18 ✍️ Neuvorstellung angepinnt (erledigt), Reel „Mein Weg“: Konzept baut Loris um – keine Sprachnachricht anfordern ([`c4e6cbc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c4e6cbc75b479ad12d03f38c4afbbb5e35327d41))
  - `automatik/lage.py`, `automatik/lage_notizen.md`, `automatik/plan.json`
- 11:00 🤖 Autopilot: Dateien fuer 08-story-tipp vorbereitet ([`568830e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/568830e81361f28c724dd67e42f296ad2615006a))
  - `posts/08_2026-10-09_reel_kst_staffel`
- 10:59 🔀 Merge claude/instagram (LAGE.md vom Ziel-Branch übernommen) ([`cec8375`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/cec837549e12513f9d9faa1a0c53032f068c0896))
- 10:58 ✍️ Lage-Notizen: Autopilot-Kalender in Reclaim noch nicht verbunden, Freigabe/Auslöser gegenprüfen ([`072d0e8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/072d0e80655779c70ac91964e7ce2c09ec1f3949))
  - `automatik/lage_notizen.md`
- 10:58 ✍️ Latente Steuern: Bildunterschrift „Spätestens im Abschluss 2026“ ([`517eed6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/517eed626f47d00007d4a1c63450ed845d5c2dda))
  - `automatik/lage_notizen.md`, `posts/05_2026-10-08_latente_steuern`
- 10:55 🔀 Merge claude/instagram ([`f4b8248`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f4b82489c0731ed02aebcf2960f65a244732385f))
- 10:55 ✍️ Automatik gehärtet: kein Doppel-Post, kein Schlüssel im Repo, keine verlorenen Antworten ([`b90716b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b90716bb466a8a9e959e81d505c6e17df9ad7b83))
  - `.github/workflows`, `automatik/fb_schluessel_verlaengern.py`, `automatik/freigabe.py`, `automatik/kommentare.py`, `automatik/lage_notizen.md`, `automatik/linkedin.py`, `…`
- 10:47 ✍️ Kalender-Sync optimiert: nur Postzeiten blocken Reclaim, Farben + Pop-ups je Art ([`0ed7b42`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0ed7b42725646e2f4bf95e63dd5f29f15e9d8128))
  - `.github/workflows`, `EINRICHTUNG.md`, `README.md`, `automatik/kalender.py`, `automatik/kalender_sync.py`, `automatik/lage_notizen.md`, `…`
- 10:44 ✍️ Content-Fabrik: Lernpunkte aus dem Wettbewerbs-Check in die Hook-Regeln ([`639b98d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/639b98dbb2ca0cba0b13f2f590e63e5e6f6d4424))
  - `automatik/lage_notizen.md`, `strategie/08_hooks.md`, `strategie/wettbewerb.md`
- 10:35 📡 Radar: Art neuer Konten aus der Vorschlagszeile übernehmen ([`e76ef09`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e76ef095f26b45caeeec04de1ed23659919c17d2))
  - `automatik/radar.py`
- 10:32 ✍️ Wettbewerbs-Check Oktober 2026 ([`fb00717`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fb007179e4cbbc084bed1e937fc0b81b877835ed))
  - `strategie/wettbewerb.md`
- 10:00 ✍️ Chrome-Module: Gesamtprompt im Repo + LinkedIn-Erinnerungen im Kalender ([`4eccdd2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4eccdd2bec52c33150e9a7bfdceb5f5db7fa4660))
  - `README.md`, `automatik/kalender.py`, `automatik/lage_notizen.md`, `strategie/14_chrome_module.md`
- 09:58 🔀 Merge branch 'claude/instagram' of https://github.com/maehrsteuern/Instagram-maehrsteuern into claude/instagram ([`7e9ecfe`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7e9ecfebcc3690be006282adb22a8b468546884e))
- 09:58 ✍️ Reel-Entwurf „Mein Weg rückwärts“ zum Review und Prüfzettel latente Steuern ([`ab5fc1f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ab5fc1f8fdd6db7b591e13a8e384c84a61bb1139))
  - `posts/04_2026-10-20_reel_mein_weg`, `posts/05_2026-10-08_latente_steuern`, `vorlagen/system/schnitt/p04_reel_markenweg_entwurf.json`
- 09:52 ✍️ Tagesbericht als Bild: Kennzahlen, Reichweite pro Tag, Beitraege mit Vortagsvergleich und Methoden-Check ([`ad5c8ad`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ad5c8ad64e3d0c9902b294a4dbe229ef86a858c2))
  - `automatik/berichte`, `automatik/tagesbericht.py`
- 09:51 📡 Radar: Häkchen auch in eigenen Kommentaren im Radar-Issue zählen ([`72d79a5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/72d79a53ba0cec60f21f1c2491f1eca24c2d22c5))
  - `automatik/radar.py`
- 08:59 ✍️ Auswertung: eigene Frage-Story schlaegt geteilte Story, Karussell waechst ueber 2 Tage ([`f9d3771`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f9d37710e292a1875e55d1d3b1c104ef8db8276d))
  - `strategie/06_auswertung.md`
- 08:37 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-9d4fa6dd-1kqi9l ([`09d9a7f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/09d9a7f09ee103b9151cea0c4b72ec7d7027113e))
- 08:37 ✍️ Reel „Mein Weg“: Variante B über den Autopiloten, KI-Hinweis in der Bildunterschrift ([`7eca616`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7eca6167f7e62a3493798598751f7d944ef20585))
  - `automatik/lage_notizen.md`, `automatik/plan.json`, `posts/04_2026-10-20_reel_mein_weg`
- 08:34 ✍️ Zwischenstand: Reel „Mein Weg“ auf Variante B (Markenweg) umgestellt ([`36f5416`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/36f54165c1e7c0e94aca36a544501e686645dad7))
  - Plan: `04-reel-mein-weg` status: wartet_auf_clips → wartet_auf_sprachnachricht
- 08:32 ✍️ Demo-Kopie: Echttest bestanden, Doku nachgezogen ([`cc33a15`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/cc33a15b97d6a74a8e99ba1aabddd15415b8a537))
  - `automatik/lage_notizen.md`, `strategie/13_backlog.md`
- 08:24 ✍️ Marken-Assets und Drehbuch-Variante B für Reel „Mein Weg“ ([`104945c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/104945c07cee0c65eb3a533c23dff933dc699350))
  - `README.md`, `assets/marke/karte_1_aktuell_9x16.png`, `assets/marke/karte_2_ki_portrait_9x16.png`, `assets/marke/karte_3_ki_avatar_2025_9x16.png`, `assets/marke/loris_aktuell_freisteller.png`, `assets/marke/loris_ki_avatar_2025.jpg`, `…`
- 08:00 ✍️ Demo-Kopie: Herkunft robuster erkennen ([`40f0db5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/40f0db5b44fba06a7906b2f7624a4443c9d48d94))
  - `automatik/apps_script`
- 07:52 ✍️ Demo-Buchungen: Apps-Script kopiert sie anonymisiert in den Autopilot-Kalender ([`eb930d7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/eb930d7d8a6bfb81c9d69653fd01373ce2cfccea))
  - `EINRICHTUNG.md`, `README.md`, `automatik/apps_script`, `automatik/lage_notizen.md`, `automatik/wochenbericht.py`, `strategie/13_backlog.md`
- 07:20 ✍️ Wochenbericht: Demo-Buchungen und Herkunft automatisch aus dem Autopilot-Kalender ([`65d201b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/65d201b9befc3f700f2d9c5b9d5508b5e0f3dd17))
  - `.github/workflows`, `automatik/lage_notizen.md`, `automatik/wochenbericht.py`, `strategie/13_backlog.md`
- 07:05 ✍️ Wochenbericht sonntags + kalender.ics entfernt ([`c91f227`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c91f2275870664f901ed455c62e3a9a6de699df2))
  - `.github/workflows`, `EINRICHTUNG.md`, `README.md`, `automatik/kalender.py`, `automatik/kalender_sync.py`, `automatik/lage.py`, `…`
- 07:02 📡 Radar 2026-10-03: 8 Beiträge, 0 DM-Entwürfe ([`a9e2318`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a9e23183c84d6febc68ee8e5269b4f0f61f183f8))
  - `automatik/interaktion`
- 07:01 ✍️ Kalender-Sync: Plan-Termine direkt in den Google-Kalender „maehrsteuern Autopilot“ ([`b471b14`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b471b147904d2f8b5c3b2a9fd65a6330ff54d788))
  - `.github/workflows`, `EINRICHTUNG.md`, `README.md`, `automatik/kalender.py`, `automatik/kalender_sync.py`, `automatik/lage.py`, `…`
- 06:42 🔑 Schlüssel: Ablaufdaten aktualisiert ([`e739f8b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e739f8ba33ac734584bedc573df49d77e48e7a95))
  - `automatik/schluessel_ablauf.json`
- 06:41 ✍️ Sprint 1: Wächter, Stichwort-Abgleich, Radar-Pflege, Erste-Stunde-Checkliste ([`76f93ad`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/76f93adf3889d22af2feb576cca9c6ef36037ec8))
  - `.github/workflows`, `README.md`, `automatik/ablauf.py`, `automatik/fb_schluessel_verlaengern.py`, `automatik/lage.py`, `automatik/lage_notizen.md`, `…`
- 06:35 📈 Statistik 2026-10-03 ([`c02d4c7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c02d4c7c62bf7bdb390785debd9726ef23a832fe))
  - `automatik/statistik`
- 06:33 ✍️ Abläufe: Actions auf Node 24 (checkout@v7, setup-python@v7), Runner fest auf ubuntu-24.04 ([`c31d663`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c31d663ae51d08bb5c2ec6ac6332a84bce42b15f))
  - `.github/workflows`
- 00:41 📡 Radar: TaxTech-Konten ergänzt, ManyChat-Stichwörter angeglichen ([`399ed14`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/399ed142cfa2d8e65c476fae102f690bada38347))
  - `automatik/interaktion.json`
- 00:29 📡 Radar: Excel/DATEV-Konten ergänzt ([`c824346`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c824346653277cd05bbe1e04ac265fe73417cfd1))
  - `automatik/interaktion.json`

**Fr 02.10.2026**
- 21:05 💼 LinkedIn-Pakete: 02-excel-fehler, 05-latente-steuern, 03-gewst-hinzurechnung ([`5214c46`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5214c460db8ac7cc9206d8649a67b97413765715))
  - `posts/02_2026-10-06_excel_fehler`, `posts/03_2026-10-13_gewst_hinzurechnung`, `posts/05_2026-10-08_latente_steuern`
- 21:04 📡 Radar 2026-10-02: 8 Beiträge, 0 DM-Entwürfe ([`8955b76`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8955b76d24593880e98cf6b3035a561c81c4a749))
  - `automatik/interaktion`
- 20:55 📡 Radar: Konten eingetragen ([`0e7b547`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0e7b5474da4cf4a29873d372c46e6adc6e14859f))
  - `automatik/interaktion.json`
- 17:40 ✍️ Lage: Neuvorstellung angepinnt (erledigt), ManyChat läuft ([`433d9dd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/433d9ddfa08f42fc6450fc6ac72b4538d5d8fbc0))
  - `automatik/lage_notizen.md`, `automatik/plan.json`
- 16:36 🔀 Merge remote-tracking branch 'origin/claude/instagram' into claude/upbeat-goodall-huo6u7 ([`9f1937f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9f1937f8cacd4c46086ac72ebc469ad709bc8d3b))
- 16:31 ✍️ Bibliothek aus dem Brand Kit (Claude Design): 365 fertige Assets ([`1f6ffc4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1f6ffc4940575300f26391be0fb53ec83b501a21))
  - `README.md`, `assets/bibliothek/README.md`, `assets/bibliothek/bausteine/abspann_copy_paste.png`, `assets/bibliothek/bausteine/abspann_mehr_abschluss.png`, `assets/bibliothek/bausteine/abspann_pruefpfad.png`, `assets/bibliothek/bausteine/abspann_quote.png`, `…`
- 16:12 ✍️ Auswertung: aktive Zeiten der ganzen Woche (auf deutsche Zeit umgerechnet) – 19:30 passt, Sonntag stärkster Abend ([`a2f31a3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a2f31a30f1fd371ecc9e4895d59dac6e254bc376))
  - `strategie/06_auswertung.md`
- 15:11 📈 Statistik 2026-10-02 ([`c3f893b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c3f893b5c2d3bb9f56c0b7b3646ae9679ac7990b))
  - `automatik/statistik`
- 13:18 ✍️ Lage-Notizen: Interaktion gemergt, offen sind Secrets und Kontenliste ([`a54983d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a54983d43696c5264401b31bfd0d104f40971bbb))
  - `automatik/lage_notizen.md`
- 13:18 🔀 Merge: Zweite Säule Interaktion (Radar, Kommentar-Hilfe, LinkedIn-Pakete) ([`47638f3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/47638f3a174a1652349a3026025805e6a6024553))
- 13:14 ✍️ Zweite Säule Interaktion: Radar, Kommentar-Hilfe, LinkedIn-Pakete ([`cbe6029`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/cbe6029322456f13146cef5c89d2ece58c5b28fb))
  - `.github/workflows`, `EINRICHTUNG.md`, `README.md`, `automatik/fb_schluessel_verlaengern.py`, `automatik/interaktion.json`, `automatik/ki.py`, `…`
- 12:15 🤖 Autopilot: 01-story-frage veroeffentlicht ([`3b2259f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3b2259fe3586af7149a5ff06981c0f95d9e2190c))
  - Plan: `01-story-frage` status: freigegeben → veroeffentlicht; `01-story-frage` online: https://www.instagram.com/stories/maehrsteuern/3998984318181825905
- 11:00 🤖 Autopilot: Dateien fuer 01-story-frage vorbereitet ([`7789e51`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7789e5125a87885287c3cc34acbce3910159a8c6))
  - `posts/01_2026-10-04_reel_ampel`
- 08:47 📈 Statistik 2026-10-02 ([`60c4aa6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/60c4aa67f643e11d4d6ef46ef453c4a2c18202b3))
  - `automatik/statistik`

**Do 01.10.2026**
- 23:56 ✍️ Lage: Neuvorstellung als veroeffentlicht eingetragen, Notizen auf Stand 01.10. abends ([`805d54b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/805d54b688b007b543fe592ea32cf008054844a9))
  - Plan: `00-neuvorstellung` status: manuell → veroeffentlicht; `00-neuvorstellung` online: https://www.instagram.com/p/Dd9V5HAAhcL/
- 23:42 ✅ Freigabe 08: go – Wissens-Reel KSt-Staffel Fr 09.10. 19:30 (Einstieg neu mit 30-%-Tabelle) und Storys 03./09./10.10. ([`408aec1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/408aec19b17bf969055638edeb99707edf4cb3b2))
  - `posts/08_2026-10-09_reel_kst_staffel`, `vorlagen/system/aufnahmen/tabelle_30prozent.html`, `vorlagen/system/schnitt/p08_reel_kst_staffel.json`
- 23:33 ✍️ DM-Strecke: ManyChat erst ab mehr DMs (Schwelle festgehalten) ([`a24df07`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a24df07835a8e97cc929e291aac789076cad780e))
  - `strategie/04_dm_strecke.md`
- 23:31 ✍️ Redaktionsplan: Regel fuer Hinter-dem-Code-Beitraege (kein Jargon, immer Aha im Kanzleialltag) ([`1c5285f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1c5285f0548874863ba8d4ae67e3c3f90dc23fb6))
  - `strategie/03_redaktionsplan.md`
- 22:55 ✍️ Split-Reel als Begleit-Reel auf Mi 07.10. 19:30 vorgezogen (Teaser 19:35), Bildunterschrift oben/unten korrigiert ([`9c487b5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9c487b500d1fbec910db609568aa549348dfb7e1))
  - Plan: `06-reel-split` zeit: 2026-10-11 19:30 → 2026-10-07 19:30; `06-story-teaser` zeit: 2026-10-11 19:35 → 2026-10-07 19:35
- 21:39 ✅ Freigabe #15: go ([`a1c37f2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a1c37f287f46c60263bc0763f2c74dac956146fe))
  - Plan: `08-story-tipp` status: entwurf → freigegeben; `08-story-heute` status: entwurf → freigegeben; `08-reel-kst-staffel` status: entwurf → freigegeben; `08-story-rueckblick` status: entwurf → freigegeben
- 20:53 ✅ Freigabe angefragt (1 Beitrag/Beiträge) ([`c9bc6a3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c9bc6a3ea3cace2cbeeaf1eba8b7b2a70df90e0f))
  - Plan: `08-story-tipp` → Freigabe-Issue #15; `08-story-heute` → Freigabe-Issue #15; `08-reel-kst-staffel` → Freigabe-Issue #15; `08-story-rueckblick` → Freigabe-Issue #15
- 20:53 ✍️ Content-Fabrik: Wissens-Reel KSt-Staffel (Fr 09.10.) und Mittags-Storys 03./09./10.10. als Entwurf ([`57cc299`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/57cc299dca2fa36a99febde1189bac5ab0d85e5b))
  - Plan: neu `08-story-tipp` (2026-10-03 12:15, entwurf); neu `08-story-heute` (2026-10-09 12:15, entwurf); neu `08-reel-kst-staffel` (2026-10-09 19:30, entwurf); neu `08-story-rueckblick` (2026-10-10 12:15, entwurf)
- 20:49 📈 Statistik 2026-10-01 ([`03c29c8`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/03c29c89d0c80c5955295b2a456dd03d72540461))
  - `automatik/statistik`
- 18:32 ✍️ Kalender: Drehbuch-Link im To-do für fehlende Clips ([`e66ed4c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e66ed4c28a0945cbba3b786ace32c49667f66a4f))
  - `automatik/kalender.py`, `kalender.ics`
- 18:02 🔀 Merge branch 'claude/busy-shannon-s341nd' into claude/instagram ([`1edc40b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1edc40b064d9335d593884fadc7d23edf2da9b8e))
- 18:01 ✍️ Kalender-Feed: kalender.ics aus plan.json (Beiträge, Freigaben, fehlende Clips/Musik), wird mit der Lage automatisch neu geschrieben ([`41c3f6e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/41c3f6e6046a45f36542b9dece14a75f99015307))
  - `.github/workflows`, `EINRICHTUNG.md`, `README.md`, `automatik/kalender.py`, `automatik/lage_notizen.md`, `kalender.ics`
- 15:55 📈 Statistik 2026-10-01 ([`9d77f59`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9d77f59e10b8afeba9e3c83383dceaae114eedc1))
  - `automatik/statistik`
- 15:11 ✅ Freigabe #14: go ([`5e2e5d0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5e2e5d0c889aa1954b0ec25064e0c9edca349afa))
  - Plan: `07-reel-hinzurechnung` status: entwurf → freigegeben
- 10:22 ✅ Freigabe angefragt (1 Beitrag/Beiträge) ([`fa3bf2a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fa3bf2a24cefa9c9f35c72b95661646f609a3e39))
  - Plan: `07-reel-hinzurechnung` → Freigabe-Issue #14
- 10:21 ✍️ Strategie: Karussell vs. Reel am Abend ergänzt; Neuvorstellung bleibt Karussell ([`a4d5abd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a4d5abd328a414c99dee685d50a5df6cc87fe857))
  - `strategie/11_wissen_instagram.md`
- 10:11 ✍️ Plan: 3 Reels pro Woche (Mi/Fr/So) – Begleit-Reel Hinzurechnung Mi 14.10. als Entwurf, Sprechtexte für Fr 09.10. und 16.10. ([`b74ebc3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b74ebc3d4ec29d7655f46b313b584b65ffa66508))
  - Plan: neu `07-reel-hinzurechnung` (2026-10-14 19:30, entwurf)
- 10:01 ✍️ Strategie: Video Sebiforce (Verkaufen ohne Kaltakquise) eingearbeitet, Entscheidungen 2–3 Reels/Woche und Werbebudget nur für laufende Beiträge ([`f1b05cc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f1b05ccb0128933da2ecf6638ff3722b84122e9e))
  - `automatik/lage_notizen.md`, `strategie/11_wissen_instagram.md`
- 09:48 ✍️ Strategie: Instagram-Wissen aus 5 Artikeln gesammelt (Algorithmus, Teilen/Speichern, Suche, Serien, Saison) und in Redaktionsplan/Reel-Regeln verlinkt ([`6398d4e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6398d4e1a4a781a0e285577dacb8d842ebc3313a))
  - `README.md`, `automatik/lage_notizen.md`, `strategie/03_redaktionsplan.md`, `strategie/09_reel_regeln.md`, `strategie/11_wissen_instagram.md`
- 09:43 ✍️ Lage-Notizen aktualisiert: Ampel-Reel freigegeben, Content-Fabrik 01.10. ergänzt, Neustart-Schritte für heute ([`14ea872`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/14ea8723269b97ca7c0353ad85c3a6985f47e3bd))
  - `automatik/lage_notizen.md`
- 09:38 ✅ Freigabe #12: go ([`af139c9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/af139c9b3518ba304516edbb193f44d9d6e376ec))
  - Plan: `05-story-frage` status: entwurf → freigegeben; `05-latente-steuern` status: entwurf → freigegeben; `05-story-teaser` status: entwurf → freigegeben
- 09:37 ✅ Freigabe #13: go ([`3768a94`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3768a9419c370c50ecd16a89a879e98556b0138d))
  - Plan: `06-reel-split` status: entwurf → freigegeben; `06-story-teaser` status: entwurf → freigegeben
- 09:29 ✅ Freigabe angefragt (2 Beitrag/Beiträge) ([`260979f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/260979f24133388d2d7cc77b878d811d9a21e817))
  - Plan: `05-story-frage` → Freigabe-Issue #12; `05-latente-steuern` → Freigabe-Issue #12; `05-story-teaser` → Freigabe-Issue #12; `06-reel-split` → Freigabe-Issue #13; `06-story-teaser` → Freigabe-Issue #13
- 09:29 ✅ Freigabe #7: go – Reel Ampel (Stimme) So 04.10. 19:30 ([`349ebba`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/349ebbacc7d52731a96720c7d7538bb4a75e6fb4))
  - Plan: `01-reel-ampel` status: entwurf → freigegeben
- 09:13 🔀 Merge: Freigabe robust gegen fehlgeschlagenes Speichern ([`559aec1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/559aec18abc324cf8b1f9488de5654154fade0e7))
- 09:12 ✅ Freigabe: push mit Wiederholung, go/stop findet Beiträge auch ohne gespeicherte Issue-Nummer (über den Titel) ([`3070a04`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3070a04173765d6ea35cef39ea0e9c998d095b39))
  - `automatik/freigabe.py`
- 08:56 ✍️ Content-Fabrik 01.10.: Karussell latente Steuern (08.10.) mit Storys, Split-Reel Excel gegen Tool (11.10.) als Entwuerfe ([`4646f25`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4646f252f71029dfe7526ee2119864032710affe))
  - Plan: neu `05-story-frage` (2026-10-07 12:15, entwurf); neu `05-latente-steuern` (2026-10-08 19:30, entwurf); neu `05-story-teaser` (2026-10-08 19:35, entwurf); neu `06-reel-split` (2026-10-11 19:30, entwurf); neu `06-story-teaser` (2026-10-11 19:35, entwurf)
- 08:21 📈 Statistik 2026-10-01 ([`431db3b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/431db3b1b6bbe22e73c56dd1258a827b7ec2d175))
  - `automatik/statistik`
- 08:18 ✍️ Schluessel verlaengern: Workflow neu anmelden (war bei GitHub nicht registriert) ([`94eb587`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/94eb5875c40243fdacc3da6695390902f39d463d))
  - `.github/workflows`

**Mi 30.09.2026**
- 19:45 🔀 Merge: Statistik täglich ca. 08:45 + Tagesbericht ([`b427de9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b427de99d250726c8bfffe750bfd24e6b15513cf))
- 19:45 📈 Statistik täglich ca. 08:45 (Anstoß über Lage-Lauf, Reserve-Zeitplan) + Tagesbericht in LAGE.md ([`6f3a270`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6f3a2708cc7ab144af63059f669c7d49bc5f164a))
  - `.github/workflows`, `EINRICHTUNG.md`, `README.md`, `automatik/lage.py`, `automatik/statistik.py`
- 18:49 ✅ Freigabe: eigene Warteschlange, damit der 15-Min.-Posten-Takt wartende Freigabe-Läufe nicht mehr verdrängt ([`4372d22`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4372d220840705e09262ad0782074a1e59e464f5))
  - `.github/workflows`
- 18:38 ✅ Freigabe angefragt (1 Beitrag/Beiträge) ([`0d81948`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0d819486c988f0b002726307f089a428466b688b))
  - Plan: `01-reel-ampel` → Freigabe-Issue #7
- 18:37 🤖 Autopilot: 00-vorfreude veroeffentlicht ([`2ec2f9d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2ec2f9d4eaaccbdc37a9e3f5a93d7f7cf920d167))
  - Plan: `00-vorfreude` status: freigegeben → veroeffentlicht; `00-vorfreude` online: https://www.instagram.com/stories/maehrsteuern/3997727075650058524
- 18:24 ✍️ Bildunterschrift Reel Ampel an die Fassung mit Loris' Stimme angepasst (Excel-Fehler, Code, lokal) ([`c371f6f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c371f6fef6723840031efba88ec160c88d9c50f0))
  - `posts/01_2026-10-04_reel_ampel`
- 18:22 ✍️ Plan: Reel Ampel (Fassung mit Stimme) neu zur Freigabe – Status entwurf, neues Freigabe-Issue ([`9aeceb2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9aeceb2bd9fcd106c0524d3f6fbd161305dae4c9))
  - Plan: `01-reel-ampel` status: pause → entwurf
- 18:19 🔀 Merge: Reel Ampel testet die Fassung mit Loris' Stimme (reel_stimme.mp4), Status pause bleibt ([`8106eb9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8106eb9823c4d5e707f40c833010ee30c6050ef1))
- 18:18 ✍️ Plan: Reel Ampel (04.10.) testet die Fassung mit Loris' Stimme (reel_stimme.mp4) ([`080e966`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/080e96623844e913c20ed71c112e26e1338f4c08))
  - `automatik/plan.json`
- 18:15 🤖 Autopilot: Dateien fuer 00-vorfreude vorbereitet ([`de366fa`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/de366fa96f1339ddeac43467097ab50bc0c008a3))
  - `posts/extra_2026-09-30_vorfreude`
- 17:47 ✍️ Ampel-Reel mit neuer Sprachaufnahme: Untertitel wörtlich, Stimme vorn, Musik und Atmo leise; Learnings in den Reel-Regeln ([`2bff54b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2bff54b9897e26d4431e642caa8fc8b21e191132))
  - `posts/01_2026-10-04_reel_ampel`, `strategie/09_reel_regeln.md`, `vorlagen/system/schnitt/p01_reel_ampel_stimme.json`
- 17:31 ✍️ Ampel-Reel: neue Fassung mit Loris' Stimme (Ich-Geschichte, wörtliche Untertitel, keine Lo-Fi-Musik) ([`8860eac`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8860eac08352f9cfdf258950a3df20d914dd378c))
  - `posts/01_2026-10-04_reel_ampel`, `vorlagen/system/montage.py`, `vorlagen/system/schnitt/p01_reel_ampel_stimme.json`
- 17:16 ✍️ Reel-Regeln: Feedback zum Ampel-Reel – zu professionell/generisch, mehr persönliches Drama statt Screen-Demo mit Lo-Fi ([`b10373c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b10373c626e2f520c314bd668296b2b28f2292bf))
  - `strategie/09_reel_regeln.md`
- 16:09 🔀 Merge remote-tracking branch 'origin/claude/instagram' into claude/instagram ([`befde8f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/befde8f42c6c366748595166c8106b10ae22702e))
- 16:08 🔀 Merge: Reels aus echten Programm-Aufnahmen, Hook-Bibliothek, Reel-Ampel auf reel_hook.mp4 (Status pause bleibt) ([`e048af2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e048af2954e4154ba3bb16ffef04852f9271bf51))
- 16:07 🔀 Merge: Lage ohne Dauer-Commits ([`e7e5dfa`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e7e5dfabe79cba20f5164613645778ece0cb96ba))
- 16:07 🔀 Merge remote-tracking branch 'origin/claude/instagram' into claude/admiring-ramanujan-2dwc7k ([`12606f7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/12606f7ff905a81186369517ecdc71cf31772ae8))
- 15:28 📈 Statistik 2026-09-30 ([`a4bab94`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a4bab94532ab349b4f2d5f23572b90447d272c10))
  - `automatik/statistik`
- 15:26 ✍️ Lage: Stand ohne eigene Lage-Commits (verhindert Commit alle 15 Minuten) ([`5c69bdd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5c69bddf24fc338217ec0736bfd5f418bb681b7e))
  - `automatik/lage.py`
- 15:26 ✍️ Plan: Ampel-Reel postet die Hook-Version mit echter Programm-Aufnahme (reel_hook.mp4) ([`4242076`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4242076191ff34c4c5839600bf9c6c6abcde79bd))
  - `automatik/plan.json`
- 13:28 ✍️ Hook-Bibliothek: zehn fertige Reel-Einstiege (1,8-2,8 s) mit Bauskript ([`cbfc192`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/cbfc1920d55787b310d0bd61918e87fcd7e8b446))
  - `musik/QUELLEN.md`, `vorlagen/hooks/README.md`, `vorlagen/hooks/bausteine/karte_oben_tabelle.mp4`, `vorlagen/hooks/bausteine/karte_unten_tool.mp4`, `vorlagen/hooks/bausteine/ki_buero_abend.mp4`, `vorlagen/hooks/bausteine/ki_taschenrechner.mp4`, `…`
- 13:01 ✍️ Post 02: untere Hälfte mit echter Delta-Plakette (+87.500) neu aufgenommen ([`defb906`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/defb9069e7cdf692414b87e0945704638c52ffa9))
  - `posts/02_2026-10-06_excel_fehler`, `strategie/10_software_reel_konzept.md`, `vorlagen/system/aufnahmen/split_excel_tool.mjs`
- 12:50 ✅ Freigabe #2: stop ([`6f673c3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6f673c3f8ae35d0bfbcd75cbed1e447959f9d73b))
  - Plan: `01-reel-ampel` status: entwurf → pause
- 12:47 🔀 Merge: externer Posten-Takt eingerichtet ([`00f0756`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/00f07568055445b6a012dc4c6e97a299c7798495))
- 12:47 ✍️ Externer Posten-Takt eingerichtet (cron-job.org, Test 204), Ablaufdaten notiert ([`258f5fd`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/258f5fd049079208bf84903c532f607ba19bc945))
  - `EINRICHTUNG.md`, `automatik/lage_notizen.md`
- 12:38 ✍️ Post 02: Split-Screen-Reel Tabelle gegen Tool (Hebesatz 400 -> 450) ([`ec1c4df`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ec1c4dff3fb411294c9838cec27393e04e110ea1))
  - `posts/02_2026-10-06_excel_fehler`, `strategie/10_software_reel_konzept.md`, `vorlagen/system/aufnahmen/excel_attrappe.html`, `vorlagen/system/aufnahmen/rekorder.mjs`, `vorlagen/system/aufnahmen/split_excel_tool.mjs`, `vorlagen/system/schnitt/p02_reel_split.json`
- 12:37 🔀 Merge: externer Takt fürs Posten (EINRICHTUNG Schritt 5) ([`16bec95`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/16bec95ba152bf98778aca0645155f06b09868f9))
- 12:37 ✍️ Einrichtung: externer 15-Min.-Takt fürs Posten über cron-job.org (GitHub-Zeitplan fällt aus) ([`3c4f377`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3c4f377564522f803a179e379deef606bd14b87d))
  - `EINRICHTUNG.md`, `automatik/lage_notizen.md`
- 12:35 🤖 Autopilot: 00-start-3 veroeffentlicht ([`aab43f3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/aab43f30e4bf740fabc2c30ae765cafa24f8d674))
  - Plan: `00-start-3` status: freigegeben → veroeffentlicht; `00-start-3` online: https://www.instagram.com/stories/maehrsteuern/3997545080966344429
- 12:35 🤖 Autopilot: Dateien fuer 00-start-3 vorbereitet ([`cc6bd34`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/cc6bd342f9607e5d0f875ed3a36cc0a940918a3b))
  - `assets/storys/start/_jpg/start_3.jpg`
- 12:35 🤖 Autopilot: 00-start-2 veroeffentlicht ([`2cda9a5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2cda9a5ac7a96d23f9f4cf211043e4a30dc300b7))
  - Plan: `00-start-2` status: freigegeben → veroeffentlicht; `00-start-2` online: https://www.instagram.com/stories/maehrsteuern/3997544897742372327
- 12:35 🤖 Autopilot: Dateien fuer 00-start-2 vorbereitet ([`18a5f5d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/18a5f5d5d793d2c6bdae93462eceb706bd347425))
  - `assets/storys/start/_jpg/start_2.jpg`
- 12:35 🤖 Autopilot: 00-start-1 veroeffentlicht ([`c104979`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c104979ca545a77571a71aebff738a648c936600))
  - Plan: `00-start-1` status: freigegeben → veroeffentlicht; `00-start-1` online: https://www.instagram.com/stories/maehrsteuern/3997544707312529712
- 12:34 🤖 Autopilot: Dateien fuer 00-start-1 vorbereitet ([`422d822`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/422d8223d998e79f7ed7d26cece1437a1029bc4f))
  - `assets/storys/start/_jpg/start_1.jpg`
- 11:55 ✍️ Post 03: Begleit-Reel GewSt-Hinzurechnung aus echter Programm-Aufnahme ([`c457e10`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c457e10cbc35bac47e0f62590f78929d62552c39))
  - `posts/03_2026-10-13_gewst_hinzurechnung`, `strategie/10_software_reel_konzept.md`, `vorlagen/system/aufnahmen/ampel_gelb_gruen.mjs`, `vorlagen/system/aufnahmen/gewst_hinzurechnung.mjs`, `vorlagen/system/aufnahmen/rekorder.mjs`, `vorlagen/system/schnitt/p03_reel_hinzurechnung.json`
- 11:55 ✍️ Beitrag 03: Hook „Werden Mieten voll hinzugerechnet?“ ([`f4d49f4`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f4d49f446f5ca2dff902da7c8efcee75258c7ad3))
  - `posts/03_2026-10-13_gewst_hinzurechnung`, `strategie/03_redaktionsplan.md`, `strategie/08_hooks.md`, `vorlagen/system/jobs/p03_gewst.json`
- 11:54 🔀 Merge remote-tracking branch 'origin/claude/instagram' into claude/focused-darwin-3hmeil ([`79b6d5c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/79b6d5c558810a5a458075d41f3d0834c2a09617))
- 11:54 ✍️ Hook-Sammlung: strategie/08_hooks.md ([`ab7ce12`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ab7ce12bc907b5474012662116e864122e104ef6))
  - `README.md`, `strategie/03_redaktionsplan.md`, `strategie/08_hooks.md`
- 11:54 🔀 Merge: Lage – laufender Überblick LAGE.md + Skill ([`1a0cc59`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1a0cc5962a47730a3061b5144954ba4d7ebf0e92))
- 11:01 ✍️ Ampel-Reel: echte Programm-Aufnahme Gelb -> Grün statt Standbilder ([`e5d6794`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e5d67948e33f5623a7c741bd68b7ac1f0bbbe4d3))
  - `posts/01_2026-10-04_reel_ampel`, `strategie/10_software_reel_konzept.md`, `vorlagen/system/aufnahmen/ampel_gelb_gruen.mjs`, `vorlagen/system/montage.py`, `vorlagen/system/schnitt/p01_reel_ampel_hook.json`
- 10:55 ✍️ Lage: laufender Überblick LAGE.md (Plan, offene Punkte, Automatik, Protokoll jeder Änderung) + Skill ([`ce1dfd3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ce1dfd370f6ad1e09c2cc8145d38945ddc49219e))
  - `.claude/skills/lage/SKILL.md`, `.github/workflows`, `CLAUDE.md`, `README.md`, `automatik/lage.py`, `automatik/lage_notizen.md`
- 10:50 ✍️ Start-Story 1: Hook „Wir müssen ehrlich über Excel reden.“ ([`d5290d5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d5290d549c6f4af12c5828ce371869601b0313a1))
  - `assets/storys/start/start_1.png`, `vorlagen/system/jobs/start_storys.json`
- 10:37 ✍️ Strategie: eigenes Reel-Konzept für Software (Split-Screen, Satisfying Software, Gesicht + Screen) ([`457cf54`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/457cf541e93c8ed58913cd587bdd30923cacbed4))
  - `strategie/09_reel_regeln.md`, `strategie/10_software_reel_konzept.md`
- 10:34 ✍️ Ampel-Reel: ruhiger Hook mit Atmo statt Musik, Lo-Fi erst ab der Lösung ([`11d8e74`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/11d8e748f39d0af80e9343520d879aa9412326c1))
  - `musik/06_runway_lofi_ruhig.mp3`, `musik/QUELLEN.md`, `musik/atmo/fehlerton.mp3`, `musik/atmo/tippen_fehlerton.mp3`, `musik/atmo/uhr_ticken.mp3`, `posts/01_2026-10-04_reel_ampel`, `…`
- 10:26 ✍️ Ampel-Reel: schnelle Hook-Montage mit KI-Clip, Effekten und Outline-Texten ([`74d38e3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/74d38e3c39a438a8b7252a1e4dfa177011827a18))
  - `posts/01_2026-10-04_reel_ampel`, `vorlagen/system/montage.py`, `vorlagen/system/schnitt/p01_reel_ampel_hook.json`, `vorlagen/system/schriften/Outfit-Bold.ttf`, `vorlagen/system/schriften/Outfit-OFL.txt`
- 10:09 ✍️ Ampel-Reel: Runway-Deep-House-Titel, Drop auf Schnitt bei 1,3 s ([`ce63bcc`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ce63bcc13f7291956e4c402a24d492784d23ae22))
  - `musik/05_runway_deephouse.mp3`, `musik/QUELLEN.md`, `posts/01_2026-10-04_reel_ampel`, `vorlagen/system/schnitt/p01_reel_ampel_musik.json`
- 10:02 ✍️ reel.py: Option musik_start (Titel versetzt starten); ungenutzten Workflow entfernt ([`8a81bdb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8a81bdbb98e89d73aba0c5196c9e917f64034dc3))
  - `.github/workflows`, `vorlagen/system/reel.py`
- 09:54 ✍️ Workflow „Musik von URL“; Reel Ampel zurück auf Autopilot ([`177435b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/177435bad3a8aab05af82d211ca5c56b1735985b))
  - Plan: `01-reel-ampel` status: manuell → entwurf
- 09:50 ✍️ Reel Ampel: manuell mit Instagram-Musik statt eingebauter Musik ([`48dd8a7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/48dd8a7987a9e8dc62150305b141ef42e41cdd75))
  - Plan: `01-reel-ampel` status: entwurf → manuell
- 09:49 ✍️ Reel Ampel: Hinweis „läuft lokal“ in Aufruf-Leiste und Bildunterschrift ([`bc4b807`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/bc4b8073c68cbcc79851ff51be5eb62e847d958a))
  - `posts/01_2026-10-04_reel_ampel`, `vorlagen/system/jobs/p01_reel_ampel.json`
- 09:47 ✍️ Reel Ampel: neuer Einstieg #BEZUG!, Ampel Rot→Gelb→Grün, 11 s ohne Abspann ([`d96a6c1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d96a6c176dfac57d3660a520479e0567574c2a13))
  - `README.md`, `automatik/plan.json`, `posts/01_2026-10-04_reel_ampel`, `strategie/03_redaktionsplan.md`, `strategie/08_demo_reel_formel.md`, `vorlagen/system/ampel.html`, `…`
- 08:56 📈 Statistik 2026-09-30 ([`068d3fb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/068d3fb9dc3d508d04ffcd6340aee0e4432052db))
  - `automatik/statistik`
- 07:31 ✅ Freigabe #1: go ([`32bac43`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/32bac432abd6a15141b6d74da0e5516a09bab628))
  - Plan: `00-vorfreude` status: entwurf → freigegeben
- 06:03 ✅ Freigabe angefragt (2 Beitrag/Beiträge) ([`1cd5370`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1cd53708b890f895560b4078d677fbbfd1c9fa28))
  - Plan: `00-vorfreude` → Freigabe-Issue #1; `01-reel-ampel` → Freigabe-Issue #2
- 06:02 ✍️ Entwuerfe: Vorfreude-Story heute 19:30, Ampel-Reel automatisch mit Musik ([`4e4d043`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4e4d0435e8360c7b138a9d9d40c1925db82c0a1e))
  - Plan: neu `00-vorfreude` (2026-09-30 19:30, entwurf); `01-reel-ampel` status: manuell → entwurf
- 05:58 ✍️ Plan: 3 Start-Storys heute 12:30-12:32 automatisch ([`dfd885f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/dfd885f00d09730777291bbe33a07c29ec27d975))
  - Plan: neu `00-start-1` (2026-09-30 12:30, freigegeben); neu `00-start-2` (2026-09-30 12:31, freigegeben); neu `00-start-3` (2026-09-30 12:32, freigegeben)
- 05:49 ✍️ DM-Strecke: Stand 30.09. abends (nur Sofortantwort, tool2 Berechnungen, Tests) ([`7922a53`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7922a53fdbd2b00e3ab36e9edb3c577b51202dd7))
  - `strategie/04_dm_strecke.md`
- 05:41 ✍️ Reel Ampel: neuer Einstieg mit Excel-Chaos und hartem Schnitt aufs Dashboard ([`b0da689`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b0da689efbda5be42c868dba08db25a6cb375326))
  - `posts/01_2026-10-04_reel_ampel`, `vorlagen/system/excel_chaos.html`, `vorlagen/system/jobs/p01_reel_ampel.json`, `vorlagen/system/render.mjs`, `vorlagen/system/schnitt/p01_reel_ampel.json`
- 05:27 ✍️ DM-Strecke: Schnellantworten nach Gruppe (tool1-5, termin), Automatik TOOL in der App ([`c5199cb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c5199cb514c03c9b31a2e6c46b00d77f64ac9bac))
  - `strategie/04_dm_strecke.md`
- 05:23 ✍️ DM-Strecke: Sofortantwort aktiv, danach manuell ([`a01471c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a01471c265dbc3227415f2aeac8e758d7c4d4d37))
  - `strategie/04_dm_strecke.md`
- 04:49 ✍️ Neuvorstellung: alle App-Einstellungen zum Neu-Einplanen ([`bac74a7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/bac74a7ff1a17d4331c563a901c8be2e84656a81))
  - `posts/00_2026-10-01_neuvorstellung`
- 04:48 ✍️ Neuvorstellung: flexible Folie 6 und Bildunterschrift zum Neu-Einplanen ([`2ae0cd9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2ae0cd9a8714fba93c24a61aed295b775757662c))
  - `posts/00_2026-10-01_neuvorstellung`, `vorlagen/system/jobs/p00_neuvorstellung.json`
- 04:43 ✍️ Neustart: Examens-Community als Zielgruppe, Bildunterschrift Neuvorstellung, Themenspeicher, Demo-Drehbuch, DM-Tracking anonymisiert ([`a1b4eee`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a1b4eee53141dbd066c7bb3cbe7d4e0e01856efd))
  - `posts/00_2026-10-01_neuvorstellung`, `strategie/01_positionierung.md`, `strategie/03_redaktionsplan.md`, `strategie/04_dm_strecke.md`, `strategie/06_auswertung.md`, `strategie/07_demo_video.md`, `…`
- 04:38 ✍️ Auswertung: Ausgangswert 352 echte Follower ([`f8214ec`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f8214ec5af15642d577522b92b10e7d17fea6aab))
  - `strategie/06_auswertung.md`
- 04:32 📈 Statistik 2026-09-30 ([`8a0d526`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8a0d5264729060fb801fbce85e9113d261c0337d))
  - `automatik/statistik`
- 04:28 ✍️ Neuvorstellung: alte Folie 6 bleibt (so geplant in der App) ([`5e4450e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5e4450e0eac5740d3214da11770e3eaaeab34d1f))
  - `posts/00_2026-10-01_neuvorstellung`, `vorlagen/system/jobs/p00_neuvorstellung.json`
- 04:24 ✍️ Neuvorstellung: flexibel mindestens 1-2 Beitraege pro Woche, meist 19:30 ([`e392ff5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e392ff53af778cb1bf0814c98e1e9b27db2a0474))
  - `posts/00_2026-10-01_neuvorstellung`, `vorlagen/system/jobs/p00_neuvorstellung.json`
- 04:24 ✍️ Neuvorstellung: Folie 6 und Text auf mindestens 3 Beitraege, Di/Do/So 19:30 ([`3144e0e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3144e0ec45e16ce041383d70c387c4ebdde97b62))
  - `posts/00_2026-10-01_neuvorstellung`, `vorlagen/system/jobs/p00_neuvorstellung.json`
- 04:22 ✍️ Postingzeit ab 04.10. auf 19:30 (Follower-Hoch um 20 Uhr laut Statistik) ([`d0a9d62`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d0a9d6244436b98f00617641479df6c135b7cd37))
  - Plan: `01-reel-ampel` zeit: 2026-10-04 18:30 → 2026-10-04 19:30; `01-story-teaser` zeit: 2026-10-04 18:35 → 2026-10-04 19:35; `02-excel-fehler` zeit: 2026-10-06 18:30 → 2026-10-06 19:30; `02-story-teaser` zeit: 2026-10-06 18:35 → 2026-10-06 19:35; `03-gewst-hinzurechnung` zeit: 2026-10-13 18:30 → 2026-10-13 19:30; `03-story-teaser` zeit: 2026-10-13 18:35 → 2026-10-13 19:35; `04-reel-mein-weg` zeit: 2026-10-20 18:30 → 2026-10-20 19:30; `04-story-teaser` zeit: 2026-10-20 18:35 → 2026-10-20 19:35
- 04:19 ✍️ Auswertung: Eigen-Push und gekaufte Reichweite 2025 beruecksichtigt ([`a6cd5e2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a6cd5e22dc694e0eda7108dc4602c91f77a96219))
  - `strategie/06_auswertung.md`
- 04:15 ✍️ Auswertung Instagram-Insights 30.09.2026 ([`f5d676a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/f5d676a42f0b8d3f8df334d7df6bd7e28aa99995))
  - `automatik/insights_voll.py`, `strategie/06_auswertung.md`
- 04:13 ✍️ Insights: Verlauf nur bis Kontostart Mai 2025 ([`fb262b9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fb262b902e9305ddb9c4fae891de40fc5f8f2123))
  - `automatik/insights_voll.py`
- 04:12 📈 Statistik 2026-09-30 ([`d66b955`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d66b9557b86ab3fabc3ff0706cc873590c0bb324))
  - `automatik/statistik`
- 04:08 ✍️ Insights: leere Aufschluesselungen abfangen ([`4cb094b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4cb094b730ef5c3734f8ddd941a70921209e45aa))
  - `automatik/insights_voll.py`
- 04:00 📈 Statistik: doppelter Lauf am selben Tag endet ohne Fehler ([`73e74fe`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/73e74fe01cfaa7251a923d2ec19ccd636674599a))
  - `automatik/statistik.py`
- 04:00 📈 Statistik: vollstaendige Insights (Zielgruppe, Verlauf, Reel-Kennzahlen, Kommentare) ([`ed7753b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ed7753bcbfda194568f15946ec8c61e162337bc0))
  - `.github/workflows`, `automatik/insights_voll.py`, `automatik/statistik.py`
- 03:48 🎵 Musik: Rausch-Titel entfernt, Reihenfolge nach Eignung ([`10a183e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/10a183ed4f746845c8e109cdf9e6af6b45e5113b))
  - `musik/05_gt577noisesurfer_rainteardrops_01_noises.mp3`, `musik/QUELLEN.md`, `musik/README.md`
- 03:48 🎵 Musik: gemeinfreie Titel (CC0) aus dem Internet Archive ([`69e6aa2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/69e6aa23790d3c8a0a25157ef9557f30ae34992c))
  - `musik/01_productionloopsandsamplesvol12009_2011_0.mp3`, `musik/02_variousartists_tastersvinegar3_03_a_n_k.mp3`, `musik/03_plantasia_garfield_park_conservatory_02.mp3`, `musik/04_tomorrows_harbest_raw_wav_a1_gemini.mp3`, `musik/05_gt577noisesurfer_rainteardrops_01_noises.mp3`, `musik/QUELLEN.md`
- 03:44 🎵 Musik holen: Laengenangaben im Format mm:ss verstehen ([`810338b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/810338b846468e63c4afb2678ad839485b9780ba))
  - `automatik/musik_holen.py`
- 03:42 🎵 Musik holen: einfachere Suchabfragen ([`e10ff49`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e10ff494ae8c9267e32a3b3ca1225d32832ab617))
  - `automatik/musik_holen.py`
- 03:41 🎵 Musik holen: Quelle Internet Archive (CC0), FreePD ist geschlossen ([`a9c3d69`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/a9c3d6928e349b17d9b7b3e8120fc4d6fbd244d8))
  - `.github/workflows`, `automatik/musik_holen.py`
- 03:41 🎵 Musik holen: breitere Suche und Protokoll ([`fb67903`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fb67903ec9316d97452f0ccf07400359891c0e40))
  - `automatik/musik_holen.py`
- 03:40 🎵 Musik holen: gemeinfreie Titel (CC0) von FreePD per Workflow ([`cbfb80a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/cbfb80ade71abbdc926a8dbe5d4a4db5af43d0fc))
  - `.github/workflows`, `automatik/musik_holen.py`
- 03:34 🤖 Autopilot: Dateien fuer Probelauf 02-excel-fehler vorbereitet ([`dead862`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/dead862461ca2f7721903e10621d07c584ffd98a))
  - `posts/02_2026-10-06_excel_fehler`
- 03:33 ✍️ Posting-Lauf alle 15 Minuten statt stuendlich (ausgefallene GitHub-Zeitplaene abfangen) ([`2be796f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2be796fd90418a2852c5d1b9839316d07644ab4c))
  - `.github/workflows`
- 03:32 ✍️ Vollautomatik: Freigabe per Issue (go/stop), Storys ohne Sticker, Reels mit eingebauter Musik, 3 Beitraege pro Woche ([`4093d29`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4093d29d4662bbe896a68d8b9cb98f4e93985ca6))
  - Plan: neu `01-story-frage` (2026-10-02 12:15, freigegeben); neu `02-story-umfrage` (2026-10-05 12:15, freigegeben); neu `03-story-quiz` (2026-10-12 12:15, freigegeben); neu `04-story-frage` (2026-10-19 12:15, entwurf)
- 03:27 🤖 Autopilot: Probelauf-Modus (hochladen ohne Veroeffentlichen) und Freigabe 04.10.-16.10. ([`892f85e`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/892f85e0414e1c0acf8ac1cda780a4a993ca0514))
  - Plan: `01-story-teaser` status: entwurf → freigegeben; `02-excel-fehler` status: entwurf → freigegeben; `02-story-teaser` status: entwurf → freigegeben; `03-gewst-hinzurechnung` status: entwurf → freigegeben; `03-story-teaser` status: entwurf → freigegeben; `03-story-aufloesung` status: entwurf → freigegeben
- 03:22 📈 Statistik 2026-09-30 ([`7a0815d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7a0815da20aac7c4641e29249d87e04aab9977db))
  - `automatik/statistik`
- 03:21 ✍️ Modify comment for workflow trigger clarity ([`9e128d1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9e128d175328a4f9d7fb9122d109e6f4da1e3048))
  - `.github/workflows`

**Di 29.09.2026**
- 22:47 ✍️ Neuvorstellung manuell in der App geplant, Teaser-Story entfaellt ([`eef8768`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/eef87684b6c812c3da006927c0da28b9dc21df85))
  - Plan: `00-neuvorstellung` status: entwurf → manuell; `00-story-teaser` status: entwurf → entfaellt
- 20:23 ✍️ Reel Ampel neu geschnitten: Haken ab dem ersten Bild ueber laufendem Dashboard, 14 s ([`0984d52`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0984d527f5bee77f31947e246846f634d800ea80))
  - `posts/01_2026-10-04_reel_ampel`, `vorlagen/system/einblendung.html`, `vorlagen/system/jobs/p01_reel_ampel.json`, `vorlagen/system/reel.py`, `vorlagen/system/schnitt/p01_reel_ampel.json`
- 20:17 ✍️ DM-Tracking: erster Kontakt aus Kaltakquise ([`5c91e80`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5c91e800c012ebf7a717dfa4727c7897b5089554))
  - `strategie/dm_tracking.csv`
- 20:14 ✍️ Leitspruch bleibt Steuern x Code, KI als Qualifikation; Bio, Terminlink und Start-Storys aktualisiert ([`42abd34`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/42abd3437316350355126e2dbff9d7b921c10a7b))
  - `README.md`, `assets/storys/start/start_1.png`, `posts/00_2026-10-01_neuvorstellung`, `posts/01_2026-10-04_reel_ampel`, `posts/02_2026-10-06_excel_fehler`, `posts/04_2026-10-20_reel_mein_weg`, `…`
- 20:09 ✍️ Leitspruch Steuern x KI: Vorlagen, Storys, Bio und Strategie angepasst ([`e4a6372`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e4a63728fbf080782131ff9752f50986244794e0))
  - `README.md`, `assets/storys/start/start_1.png`, `posts/01_2026-10-04_reel_ampel`, `posts/02_2026-10-06_excel_fehler`, `posts/04_2026-10-20_reel_mein_weg`, `posts/extra_2026-09-29_countdown`, `…`
- 20:06 ✍️ Neuvorstellung: Werdegang (Diplom-Finanzwirt, IHK KI-Transformation) und Ausrichtung KI x Steuern ([`12420d2`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/12420d28e25d1407338d432540da8e7dd145fcbb))
  - `posts/00_2026-10-01_neuvorstellung`, `vorlagen/system/jobs/p00_neuvorstellung.json`
- 19:25 ✍️ Startwoche vorgezogen: Neuvorstellung Do 01.10., Reel So 04.10., danach dienstags ([`1e942af`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1e942aff6edf7d31fd9e61cef194e3b942b163a6))
  - Plan: `00-neuvorstellung` zeit: 2026-10-04 18:30 → 2026-10-01 18:30; `00-story-teaser` zeit: 2026-10-04 18:35 → 2026-10-01 18:35; `01-reel-ampel` status: entwurf → manuell; `01-reel-ampel` zeit: 2026-10-06 18:30 → 2026-10-04 18:30; `01-story-teaser` zeit: 2026-10-06 18:35 → 2026-10-04 18:35; `02-excel-fehler` zeit: 2026-10-13 18:30 → 2026-10-06 18:30; `02-story-teaser` zeit: 2026-10-13 18:35 → 2026-10-06 18:35; `03-gewst-hinzurechnung` zeit: 2026-10-20 18:30 → 2026-10-13 18:30; `03-story-teaser` zeit: 2026-10-20 18:35 → 2026-10-13 18:35; `03-story-aufloesung` zeit: 2026-10-23 12:15 → 2026-10-16 12:15; `04-reel-mein-weg` zeit: 2026-10-27 18:30 → 2026-10-20 18:30; `04-story-teaser` zeit: 2026-10-27 18:35 → 2026-10-20 18:35
- 19:22 ✍️ Countdown-Story fuer den Neustart ([`77eb295`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/77eb29502816e4b10ba4de995b5b1bc4945601c5))
  - `posts/extra_2026-09-29_countdown`, `vorlagen/system/jobs/extra_countdown.json`
- 19:21 ✍️ Repo-Name Instagram-maehrsteuern eingetragen ([`8390edf`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8390edf95db04982e136d36a618472e858c702ea))
  - `EINRICHTUNG.md`
- 19:17 ✍️ Instagram-Autopilot: Vorlagen, Beitraege Okt. 2026 und automatisches Posten ([`d04f975`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d04f97515051945cf5190af915df1281805d2b44))
  - Plan: neu `00-neuvorstellung` (2026-10-04 18:30, entwurf); neu `00-story-teaser` (2026-10-04 18:35, entwurf); neu `01-reel-ampel` (2026-10-06 18:30, entwurf); neu `01-story-teaser` (2026-10-06 18:35, entwurf); neu `02-excel-fehler` (2026-10-13 18:30, entwurf); neu `02-story-teaser` (2026-10-13 18:35, entwurf); neu `03-gewst-hinzurechnung` (2026-10-20 18:30, entwurf); neu `03-story-teaser` (2026-10-20 18:35, entwurf); neu `03-story-aufloesung` (2026-10-23 12:15, entwurf); neu `04-reel-mein-weg` (2026-10-27 18:30, wartet_auf_clips); neu `04-story-teaser` (2026-10-27 18:35, entwurf)

</details>
