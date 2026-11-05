# 🧭 Lage – maehrsteuern auf Instagram

_Automatisch erzeugt von `automatik/lage.py` – nicht von Hand bearbeiten (Notizen: `automatik/lage_notizen.md`). Stand: letzte Änderung Do 05.11. 10:36 Uhr._

## ⏱️ 30-Sekunden-Briefing

- **Heute online:** 🟡 12:15 📱 Story `54-story-tipp` (pausiert) · 🔴 12:15 📱 Story `i03-story-frage` (Dateien fehlen) · 🟡 17:45 🎬 Reel `i03-reel-insider-einspruch-0euro` (pausiert) · 🟡 17:50 📱 Story `53-story-teaser-karussell` (pausiert) · 🔴 17:50 📱 Story `i03-story-teaser` (Dateien fehlen)
- **Braucht dich:** 39 offen, davon **37 rot** 🔴
- **Letzte 7 Tage:** Reichweite **43470** (29.10.–04.11., +1032 % zur Vorwoche) · Follower **+407** (jetzt 809) · 30 Tage: +470 Follows / −14 entfolgt
- **Testmonat** (Tag 25/28, Soll 7 Feed/Woche, täglich ≥ 1 Reel):
  - 🟡 **KW 45** (02.11.–08.11.) ← jetzt: Feed **6/7** (3 online · 3 geplant) · Reel-Tage (sicher) **4/7** – ohne Reel: Mi 04.11., Do 05.11., So 08.11.
- **Freie Slots nächste 7 Tage** (4):
  - Sa 07.11.: Story 12:15
  - Mo 09.11.: Story 12:15
  - Di 10.11.: Story 12:15
  - Mi 11.11.: Story 12:15

**Als Nächstes online:** 📱 Story `i03-story-frage` am **Do 05.11. 12:15 Uhr** – 🟢 freigegeben (geht automatisch online)

## 📝 Gerade in Arbeit

- **Neue Asset-Quelle 30.10. (Loris):** Runway-Connector in Claude wieder angemeldet (Konto **Pro**, ~2.306 Credits) – KI-Bilder mit **Nano Banana Pro** (~20 Credits/Bild) sind jetzt eine mögliche Quelle neben selbst produzierten Assets und Claudes Animationen. Regeln: `README.md` → „Asset-Quellen“, `strategie/09_reel_regeln.md` → „KI-Bilder“.
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
- 28.10. abends: Memes komplett gestrichen (Loris: „blöd“) – keine Meme-Formate mehr vorschlagen. meme2 lief bereits als Story (verschwindet nach 24 h).
- **29.10.:** Bio **Variante A** gewählt (Loris setzt in der App, `strategie/02_bio_highlights.md`), M1 anpinnen. Karussell K01 „30 KI-Befehle für Steuer-Profis“ gebaut (freigegeben Mi 04.11. 17:45, übrige Karussells je einen Platz später, Mythen → 09.12.), Kommentar-Wort PROMPT → PDF `posts/k01_2026-11-04_ki_befehle/ki_befehle_30.pdf` (ManyChat-Regel legt Loris an).
- **29.10.: Kein ManyChat (Loris).** `kommentare.py` beantwortet Stichwort-Kommentare selbst: PROMPT → DM mit PDF-Link, TOOL → DM mit Demo-Link (Private Reply, 1× je Kommentar, ≤ 7 Tage) + kurze öffentliche Antwort. Texte in `automatik/interaktion.json` → `stichwort_antworten`. Geht die DM nicht (fehlende Berechtigung `instagram_business_manage_messages` oder „Zugriff auf Nachrichten“ aus), meldet das Issue „💬 Kommentare“ den Text zum Selbst-Senden.
- **30.10.: Musik aller 27 geplanten Reels einmalig neu abgemischt** (Loris: Ferrari-Musik „angsteinflößend“). Nur noch Tracks aus der Liste in `musik/README.md` („Musik-Regel ab 30.10.“), düstere gesperrt. Feld `musik` je Eintrag in plan.json. Ferrari (online) bleibt wie es ist.

## 👉 Braucht dich

- 🔴 **Dateien fehlen** `i03-story-frage` (Do 05.11. 12:15): story_do_frage.png
- 🔴 **Dateien fehlen** `i03-story-teaser` (Do 05.11. 17:50): story_do_teaser.png
- 🔴 **Dateien fehlen** `i06-story-frage` (Fr 06.11. 12:15): story_fr_frage.png
- 🔴 **Dateien fehlen** `i06-reel-insider-schaetzung` (Fr 06.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `i06-story-teaser` (Fr 06.11. 17:50): story_fr_teaser.png
- 🔴 **Dateien fehlen** `40-reel-formeln` (Sa 07.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `10-e-rechnung` (So 08.11. 17:45): folie_01.png, folie_02.png, folie_03.png, folie_04.png, folie_05.png, folie_06.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `i04-reel-insider-saeumnis` (Mo 09.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `38-reel-pruefpfad` (Di 10.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `37-karussell-bp-vorbereitung` (Mi 11.11. 17:45): folie_01.png, folie_02.png, folie_03.png, folie_04.png, folie_05.png, folie_06.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `i10-reel-insider-belege` (Do 12.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `39-reel-holding` (Fr 13.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `i07-reel-insider-kontrollmitteilung` (Sa 14.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `31-karussell-zinsschranke` (So 15.11. 17:45): folie_01.png, folie_02.png, folie_03.png, folie_04.png, folie_05.png, folie_06.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `54-reel-reverse-charge` (Mo 16.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `i11-reel-insider-anrufen` (Di 17.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `53-karussell-iab` (Mi 18.11. 17:45): folie_01.png, folie_02.png, folie_03.png, folie_04.png, folie_05.png, folie_06.png, folie_07.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `i12-reel-insider-mbs-excel` (Do 19.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `43-reel-par35` (Fr 20.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `48-reel-firmenwagen` (Sa 21.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `56-karussell-verjaehrung` (So 22.11. 17:45): folie_01.png, folie_02.png, folie_03.png, folie_04.png, folie_05.png, folie_06.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `55-reel-thesaurierung` (Mo 23.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `49-reel-kleinunternehmer` (Di 24.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `44-karussell-glossar` (Mi 25.11. 17:45): folie_01.png, folie_02.png, folie_03.png, folie_04.png, folie_05.png, folie_06.png, folie_07.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `57-reel-verlust-8c` (Do 26.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `50-reel-gebaeude-afa` (Fr 27.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `53-reel-iab` (Sa 28.11. 17:45): reel.mp4, titelbild.png, bildunterschrift_reel.txt
- 🔴 **Dateien fehlen** `51-karussell-kapitalertraege` (So 29.11. 17:45): folie_01.png, folie_02.png, folie_03.png, folie_04.png, folie_05.png, folie_06.png, folie_07.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `32-reel-mindeststeuer` (Mo 30.11. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `34-reel-einspruch` (Di 01.12. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `34-story-tipp` (Di 01.12. 17:50): story_so_tipp.png
- 🔴 **Dateien fehlen** `46-karussell-dividenden-8b` (Mi 02.12. 17:45): folie_01.png, folie_02.png, folie_03.png, folie_04.png, folie_05.png, folie_06.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `33-reel-paragraf-formel` (Do 03.12. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `i05-reel-insider-finanzbeamte` (Fr 04.12. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `i09-reel-insider-elterngeld` (Sa 05.12. 17:45): reel.mp4, titelbild.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `59-karussell-pensionen` (So 06.12. 17:45): folie_01.png, folie_02.png, folie_03.png, folie_04.png, folie_05.png, folie_06.png, bildunterschrift.txt
- 🔴 **Dateien fehlen** `41-karussell-mythen` (Mi 09.12. 17:45): folie_01.png, folie_02.png, folie_03.png, folie_04.png, folie_05.png, folie_06.png, folie_07.png, folie_08.png, bildunterschrift.txt
- ⏰ **✍️ Claude: Sprechtexte für Aufnahme Sa 07.11. vorbereiten** (Do 05.11. 09:00) – 15–20 neue Reel-Sprechtexte nach 19_wissen (Boring Content, Hook mit Ergebnis) in posts/sprechtexte.md, Themen aus Auswertung + Kommentaren.
- ⏰ **🎙️ Neue Reel-Aufnahmen einsprechen (Reels ab 17.11.)** (Sa 07.11. 10:00) – Ca. 1 h. Sprechtexte (je 25–30 s, Hook im ersten Satz, Schlussfrage) legt Claude bis Do 05.11. in posts/sprechtexte.md bereit. Ruhiger Raum, Handy nah, wie Aufnahme 21.10. Danach die Datei(en) an Claude geben → Premium-Reels bauen. Ohne neue Aufnahme gehen ab 17.11. keine Reels mehr raus (nur Karussells Mi + So).

## ⏭️ Nächste 7 Tage

| Wann | Was | Status | Hinweis |
|---|---|---|---|
| Do 05.11. 12:15 | 📱 Story `54-story-tipp` | pausiert | 14.10. Nachtlauf (d2): Emoji-Tipp Pflichthinweis „Steuerschuldnerschaft des Leistungsempfängers“ (§ 14a Abs. 5 UStG) mit Verweis aufs Reel, 👏/😮 (jobs/p54_reel_reverse_charge.json). storys/frage_rc nicht genutzt (STICKER-Platzhalter). |
| Do 05.11. 12:15 | 📱 Story `i03-story-frage` | 🟢 freigegeben (geht automatisch online) | 05.11.: Story-Slots wieder an (Loris: „Ja Story Slots wieder einschalten“) – neue Story passend zum Reel des Tages, alte Storys der verschobenen Beiträge bleiben pausiert. Job vorlagen/system/jobs/p_storys_2026-11-05_06.json. Frage-Story vor i03 (Emoji antippen, kein Sticker) |
| Do 05.11. 17:45 | 🎬 Reel `i03-reel-insider-einspruch-0euro` | pausiert | 05.11. 11:10: pausiert (Loris: Gesicht einbauen – Hook mit eigener Aufnahme im Büro-Look, Mitte Blur + Präsentation als Pop-up, Schluss Büro-CTA). Wieder freigeben, sobald die neue Fassung steht. · 30.10.: Musik neu (102_deep_house_ruhig, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-02. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #03 (Aufnahme 26.10.), Premium-Look premium/insider_03.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-05. |
| Do 05.11. 17:50 | 📱 Story `53-story-teaser-karussell` | pausiert | 14.10. Nachtlauf (d2): Teaser „Jetzt neu im Profil“ zum IAB-Karussell (Folie 1), jobs/p53_iab.json. |
| Do 05.11. 17:50 | 📱 Story `i03-story-teaser` | 🟢 freigegeben (geht automatisch online) | 05.11.: Story-Slots wieder an (Loris: „Ja Story Slots wieder einschalten“) – neue Story passend zum Reel des Tages, alte Storys der verschobenen Beiträge bleiben pausiert. Job vorlagen/system/jobs/p_storys_2026-11-05_06.json. Teaser „Neues Reel“ zu i03, wartet bis i03 online ist |
| Fr 06.11. 12:15 | 📱 Story `55-story-tipp` | pausiert | 14.10. Nachtlauf (d2): Emoji-Tipp „28,25 % auf Gewinn, der im Betrieb bleibt“ (§ 34a EStG, zzgl. SolZ, 25 % Nachversteuerung), 👏/😮 (jobs/p55_reel_thesaurierung.json). |
| Fr 06.11. 12:15 | 📱 Story `i06-story-frage` | 🟢 freigegeben (geht automatisch online) | 05.11.: Story-Slots wieder an (Loris: „Ja Story Slots wieder einschalten“) – neue Story passend zum Reel des Tages, alte Storys der verschobenen Beiträge bleiben pausiert. Job vorlagen/system/jobs/p_storys_2026-11-05_06.json. Frage-Story vor i06 (Emoji antippen, kein Sticker) |
| Fr 06.11. 17:45 | 🎬 Reel `i06-reel-insider-schaetzung` | 🟢 freigegeben (geht automatisch online) | 02.11.: mit i06 getauscht (Loris: „i02 heute“) – Hook-Muster „Finanzamt sieht/weiß etwas über dich“ = bisher meistgeteilte Insider-Reels. · 30.10.: Musik neu (113_organic_house, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-10-31. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #06 (Aufnahme 26.10.), Premium-Look premium/insider_06.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-02. |
| Fr 06.11. 17:50 | 📱 Story `56-story-teaser` | pausiert | 14.10. Nachtlauf (d2): Teaser „Jetzt neu im Profil“ zum Verjährungs-Karussell (Folie 1), jobs/p56_verjaehrung.json. |
| Fr 06.11. 17:50 | 📱 Story `i06-story-teaser` | 🟢 freigegeben (geht automatisch online) | 05.11.: Story-Slots wieder an (Loris: „Ja Story Slots wieder einschalten“) – neue Story passend zum Reel des Tages, alte Storys der verschobenen Beiträge bleiben pausiert. Job vorlagen/system/jobs/p_storys_2026-11-05_06.json. Teaser „Neues Reel“ zu i06, wartet bis i06 online ist |
| Sa 07.11. 17:45 | 🎬 Reel `40-reel-formeln` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (136_modern_jazz_leicht, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-03. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-10-28 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-27 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-28 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p40_reel_stimme_bauen.py, Vorschau vorschau_stimme.png). Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R2 gegengelesen, $C$12-Satz korrigiert), Reel ohne Stimme 13,7 s, −18,0 LUFS, Atmo Tippen + Fehlerton im Hook, Musik 12 Pop Electronic. Fall „=WENNFEHLER(…; 0): Fehler weg, Steuer auch“ + 2 Lösungen (XVERWEIS statt Festwert, Namen statt $C$12) = 3 Punkte; MAX/ABRUNDEN bewusst weggelassen (stehen schon im Paragraf-Formel-Reel 24.10.). Karten aus karussell/excel_formeln Folien 6, 2, 5 (schnitt/p36_40_karten_bauen.py), Titelbild + Abspann TOOL neu (jobs/p40_reel_formeln.json), Schnitt schnitt/p40_reel_formeln.json. Raster Mi A verlangt Stimme → Abweichung (ohne Aufnahme). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-07. |
| Sa 07.11. 17:50 | 📱 Story `57-story-teaser` | pausiert | 14.10. Nachtlauf (d3): Teaser „Jetzt neu im Profil“ zum § 8c-Reel (Titelbild), jobs/p57_reel_verlust_8c.json; Karte verkleinert (bausteine/teaser_karte.png, schnitt/p57_58_karten_bauen.py), damit nichts angeschnitten wird. |
| So 08.11. 12:15 | 📱 Story `58-story-tipp` | pausiert | 14.10. Nachtlauf (d3): Tipp-Story mit Emoji-Reaktion „Bis 250 € brutto reicht eine Kleinbetragsrechnung (§ 33 UStDV)“ zum Vorsteuer-Reel, jobs/p58_reel_vorsteuer.json. |
| So 08.11. 17:45 | 🖼️ Karussell `10-e-rechnung` | 🟢 freigegeben (geht automatisch online) | 29.10.: verschoben 2026-11-04 → 2026-11-08 (K01 KI-Befehle am 04.11., Loris go). · 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-04. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-04. · 25.10.: Termin 2026-10-27 11:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. (Nachtlauf, Loris' Auftrag „optimieren + freigeben“): Bildunterschrift fachlich korrigiert (Papier in der Übergangszeit ohne Zustimmung, § 27 Abs. 38 UStG; Ausnahmen), Folie 6 Speichern + Weiterleiten, Alt-Texte · 13.10.: Zeiten auf die Follower-Welle gelegt (Loris, Insights: aktivste Zeit 18–21 Uhr) – Feed 17:45/11:45, Storys 17:50/12:15. · Aus der Bibliothek (gegengelesen 05.10., Rechtsstand Okt. 2026: § 27 Abs. 38 UStG) · 06.10.: auf Fr 23.10. geschoben (Reel-Takt alle 2 Tage). · [Freigabe #31](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/issues/31) |
| So 08.11. 17:50 | 📱 Story `59-story-teaser` | pausiert | 14.10. Nachtlauf (d3): Teaser „Jetzt neu im Profil“ zum Pensions-Karussell (Folie 1), jobs/p59_pensionen.json; Karte verkleinert (bausteine/teaser_karte.png, schnitt/p57_58_karten_bauen.py), damit nichts angeschnitten wird. |
| Mo 09.11. 17:45 | 🎬 Reel `i04-reel-insider-saeumnis` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (121_minimal_house, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-05. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #04 (Aufnahme 26.10.), Premium-Look premium/insider_04.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-09. |
| Di 10.11. 17:45 | 🎬 Reel `38-reel-pruefpfad` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (122_lofi_hiphop, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Loris – Einspruch heute zu speziell, breiteres Thema zuerst → 2026-10-31 17:45. · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-02. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-02 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-27 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-27 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p38_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R1/R2 gegengelesen), Begleit-Reel zu Karussell 37, ohne Stimme 13,7 s, −18,0 LUFS, Atmo Uhr im Hook, Musik 09 Lofi-Piano ab der Lösung. Als Betriebsprüfungs-Thema gerahmt („Woher kommt diese Zahl?“, GoBD-Nachvollziehbarkeit), nicht als #BEZUG/Excel-Fehler. Titelbild „Betriebsprüfung – Jede Zahl bis zur Quelle“ und Abspann „Kommentiere TOOL“ neu (jobs/p38_reel_pruefpfad.json); bausteine/haken_pruefpfad, leiste_pruefpfad, haken_ueber_pruefpfad auf Folien 3/4 von bp_vorbereitung (schnitt/p36_40_karten_bauen.py), Schnitt schnitt/p38_reel_pruefpfad.json. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-10. |
| Mi 11.11. 17:45 | 🖼️ Karussell `37-karussell-bp-vorbereitung` | 🟢 freigegeben (geht automatisch online) | 29.10.: verschoben 2026-11-08 → 2026-11-11 (K01 KI-Befehle am 04.11., Loris go). · 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-08. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-10-28. · 25.10.: Premium-Look (premium/karussells/p37_bp_vorbereitung.json), go Loris, 2026-10-26 17:45. · 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), karussell/bp_vorbereitung Folien 1–5 unverändert; Folie 6 neu: „Speichern bis zur nächsten Prüfungsanordnung“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p37_bp_vorbereitung.json). Geprüft: §§ 196, 197 AO, § 147 Abs. 6 AO, GoBD, § 200 AO; Bildunterschrift ergänzt um 4/2 Wochen Vorlauf (§ 5 Abs. 4 BpO). Alt-Texte in alt_texte.json. Begleit-Reel 38 am Abend. |

## 🗓️ Danach

| Wann | Was | Status | Hinweis |
|---|---|---|---|
| Do 12.11. 17:45 | 🎬 Reel `i10-reel-insider-belege` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (127_tech_groove, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-06. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #10 (Aufnahme 26.10.), Premium-Look premium/insider_10.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-12. |
| Fr 13.11. 17:45 | 🎬 Reel `39-reel-holding` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (130_pop_electronic_clean, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-09. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-03 17:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-28 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-28 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p39_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R4 gegengelesen), Reel ohne Stimme 13,8 s, −18,0 LUFS, Musik 07 Minimal Tech. Veräußerungsgewinn GmbH an GmbH: 1 Mio. € × 5 % nbBA (§ 8b Abs. 2, 3 KStG) × 29,825 % (Hebesatz 400 %) = 14.913 € = 1,49 % – nachgerechnet. Karten aus karussell/holding Folien 2+3 (schnitt/p36_40_karten_bauen.py); Titelbild „1 Mio. € Gewinn. 1,5 % Steuer.“, Karte „Dividenden erst ab 10 % (§ 8b Abs. 4 KStG)“ und Abspann TOOL neu (jobs/p39_reel_holding.json). Bildunterschrift: Dividenden § 8b Abs. 1/5, 10-%-Grenze Abs. 4, GewSt-Schachtel 15 % (§ 9 Nr. 2a GewStG), Verluste nicht abziehbar (Abs. 3 Satz 3), Ausnahmen Abs. 7/8. Abgrenzung zum Karussell par8b (Dividenden, 01.11.). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-13. |
| Sa 14.11. 17:45 | 🎬 Reel `i07-reel-insider-kontrollmitteilung` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (113_organic_house, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-07. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #07 (Aufnahme 26.10.), Premium-Look premium/insider_07.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-14. |
| So 15.11. 17:45 | 🖼️ Karussell `31-karussell-zinsschranke` | 🟢 freigegeben (geht automatisch online) | 29.10.: verschoben 2026-11-11 → 2026-11-15 (K01 KI-Befehle am 04.11., Loris go). · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-11. · 25.10.: Termin 2026-10-28 17:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), Folien 1–5 aus karussell/zinsschranke, Folie 6 neu (Speichern + Weiterleiten, Job jobs/p31_zinsschranke.json). Offener Prüfbericht-Punkt erledigt: Bildunterschrift nennt Untergang des Zinsvortrags bei schädlichem Anteilseignerwechsel (§ 4h Abs. 5 EStG i. V. m. § 8c KStG). Freigrenze < 3 Mio. €, 30 % verrechenbares EBITDA, Stand-alone „keine nahestehende Person“, Escape 2 Prozentpunkte. Begleit-Karussell zum Abend-Reel 21 Zinsschranke |
| Mo 16.11. 17:45 | 🎬 Reel `54-reel-reverse-charge` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (115_marimba_corporate, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-10-29. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-04 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-29 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-29 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p54_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf (d2): aus Bibliothek (R4 gegengelesen, karussell/reverse_charge), Reel ohne Stimme 14,2 s, −18,0 LUFS (Peak −4,4 dBFS), Atmo Uhr + Fehlerton im Hook, Musik 09 Lofi-Piano ab 2,4 s. Titelbild neu als Prüfer-Fall „Mit USt bezahlt. Vorsteuer: 0 €.“, Einblendung Demo-Fall Bau (100.000 € + 19.000 € USt), Karten aus reverse_charge Folien 5/4 (schnitt/p52_55_karten_bauen.py), Abspann TOOL (jobs/p54_reel_reverse_charge.json), Schnitt schnitt/p54_reel_reverse_charge.json. Geprüft: § 13b Abs. 2 Nr. 4 und Abs. 5 UStG, § 14c Abs. 1, § 15 Abs. 1 Satz 1 Nr. 1 und Nr. 4, § 14a Abs. 5 UStG; Bildunterschrift erklärt Saldo (13b-Schuld = Vorsteuer) und Rückforderung über berichtigte Rechnung. Nähe zu d3 (Vorsteuer, So 08.11.) beachtet: hier nur § 13b-Fall. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-16. |
| Di 17.11. 17:45 | 🎬 Reel `i11-reel-insider-anrufen` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (102_deep_house_ruhig, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-09. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #11 (Aufnahme 26.10.), Premium-Look premium/insider_11.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-17. |
| Mi 18.11. 17:45 | 🖼️ Karussell `53-karussell-iab` | 🟢 freigegeben (geht automatisch online) | 29.10.: verschoben 2026-11-15 → 2026-11-18 (K01 KI-Befehle am 04.11., Loris go). · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-15. · 25.10.: Termin 2026-10-30 17:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf (d2): aus Bibliothek (R6 gegengelesen), karussell/iab_2 Folien 1–6 unverändert; Folie 7 neu: „Speichern für die Investitionsplanung“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p53_iab.json). Begleit-Reel 53 am Vorabend. Alt-Texte in alt_texte.json. Geprüft: § 7g Abs. 1–6 EStG (50 %, 200.000 €/200.000 €, 3 Jahre, 40 % Sonder-AfA, 90 % betrieblich). |
| Do 19.11. 17:45 | 🎬 Reel `i12-reel-insider-mbs-excel` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (129_breaks_lounge, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-11-10. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #12 (Aufnahme 26.10.), Premium-Look premium/insider_12.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-19. |
| Fr 20.11. 17:45 | 🎬 Reel `43-reel-par35` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (112_jazzhop, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-10. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-05 17:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-29 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-30 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p43_reel_stimme_bauen.py, Vorschau vorschau_stimme.png). Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R5 gegengelesen, „tatsächlich zu zahlende“ GewSt korrigiert), Reel ohne Stimme 14,4 s, −18,1 LUFS (Peak −4,1 dBFS), Musik 06 Lofi ruhig. Titelbild reels/reel_35, Karten aus karussell/par35 Folien 3–5 (schnitt/p41_44_karten_bauen.py), Abspann „Kommentiere TOOL“ neu (jobs/p43_reel_par35.json), Schnitt schnitt/p43_reel_par35.json. Nachgerechnet: 100.000 − 24.500 = 75.500 × 3,5 % = 2.642,50 €; × 400 % = 10.570 € = 4,0 × 2.642,50; bei 450 % 11.891,25 € → 1.321,25 € Rest. Ermäßigungshöchstbetrag und „nur natürliche Personen/Mitunternehmer“ in der Bildunterschrift. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-20. |
| Sa 21.11. 17:45 | 🎬 Reel `48-reel-firmenwagen` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (136_modern_jazz_leicht, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-10-30. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-10-30 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-30 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-30 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p48_reel_stimme_bauen.py, Vorschau vorschau_stimme.png). Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R5 gegengelesen), Reel ohne Stimme 15,0 s, −17,9 LUFS, Atmo Uhr + Fehlerton im Hook, Musik 10 Spannung. Titelbild neu als Prüfer-Fall „Fahrtenbuch in Excel. Verworfen.“, 3 Punkte = karussell/firmenwagen Folien 5, 2, 3 (Fahrtenbuch zeitnah/geschlossen, 1 %, 0,03 %). Demo 50.000 € BLP, 20 km → 800 €/Monat nachgerechnet; E-Auto 0,25 % bis 100.000 € (Anschaffung ab 1.7.2025) in der Bildunterschrift. jobs/p48_reel_firmenwagen.json, Karten schnitt/p48_50_karten_bauen.py, Schnitt schnitt/p48_reel_firmenwagen.json. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-21. |
| So 22.11. 17:45 | 🖼️ Karussell `56-karussell-verjaehrung` | 🟢 freigegeben (geht automatisch online) | 29.10.: verschoben 2026-11-18 → 2026-11-22 (K01 KI-Befehle am 04.11., Loris go). · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-18. · 25.10.: Termin 2026-11-02 17:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf (d2): aus Bibliothek (R6 gegengelesen, keine offenen Punkte), karussell/verjaehrung Folien 1–5 unverändert; Folie 6 neu: „Speichern für die nächste Prüfungsanordnung“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p56_verjaehrung.json). Alt-Texte in alt_texte.json. Geprüft: § 169 Abs. 2 Satz 1 Nr. 2 und Satz 2, § 170 Abs. 2 Satz 1 Nr. 1, § 171 AO; Demo Erklärung für 2022, Abgabe 2024 → Ende 31.12.2028. |
| Mo 23.11. 17:45 | 🎬 Reel `55-reel-thesaurierung` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (122_lofi_hiphop, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-12. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-07 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-31 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-31 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p55_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf (d2): aus Bibliothek (R4 gegengelesen, karussell/thesaurierung), Reel ohne Stimme 14,0 s, −18,0 LUFS (Peak −4,2 dBFS), Musik 12 Pop Electronic. Titelbild neu „28,25 % statt bis 45 %.“, Karten aus thesaurierung Folien 2/3/4 (Folie 5 Option § 1a KStG bewusst nicht genutzt, Antragsfrist nicht nachgeprüft), Abspann TOOL (jobs/p55_reel_thesaurierung.json), Schnitt schnitt/p55_reel_thesaurierung.json. Geprüft: § 34a Abs. 1 (28,25 % zzgl. SolZ, Antrag, Bilanzierer) und Abs. 4 (25 % Nachversteuerung); Bildunterschrift: Gesamtbelastung bei baldiger Entnahme oft höher. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-23. |
| Di 24.11. 17:45 | 🎬 Reel `49-reel-kleinunternehmer` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (130_pop_electronic_clean, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Platz für Insider #01 gemacht, Termin vorläufig. · 26.10.: Loris – Einspruch heute zu speziell, breiteres Thema zuerst → 2026-10-26 17:45. · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-10-31. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-10-31 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-31 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-26 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p49_reel_stimme_bauen.py, Vorschau vorschau_stimme.png). Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R5 gegengelesen), CTA-Reel KW 45 (TOOL-Aufruf im Abspann, eigener TOOL-Absatz in der Bildunterschrift: Grenz-Monitor 100.000 €). Reel ohne Stimme 15,4 s, −18,2 LUFS, Musik 12 Pop Electronic, Abspann zusätzlich groß „Kommentiere „TOOL““. Titelbild neu „100.000 € und raus.“, Karten: Grenz-Folien neu gerendert mit Normbox „§ 19 Abs. 1 UStG“ (ohne Satzangabe – Satzzählung der Neufassung 2025 nicht sicher belegt) + karussell/kleinunternehmer Folie 4. Neugründer-Regel und Verzicht 5 Jahre (§ 19 Abs. 3 UStG) in der Bildunterschrift. jobs/p49_reel_kleinunternehmer.json, Karten schnitt/p48_50_karten_bauen.py, Schnitt schnitt/p49_reel_kleinunternehmer.json. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-24. |
| Mi 25.11. 17:45 | 🖼️ Karussell `44-karussell-glossar` | 🟢 freigegeben (geht automatisch online) | 29.10.: verschoben 2026-11-22 → 2026-11-25 (K01 KI-Befehle am 04.11., Loris go). · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-22. · 25.10.: Termin 2026-10-31 17:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen, Einlagekonto und Messbetrag-Box korrigiert), karussell/glossar_1 Folien 1–6, Folie 7 neu: Speichern + Weiterleiten + TOOL statt offener Kommentarfrage (jobs/p44_glossar.json). jahresabschluss_7 nicht genutzt: nur 4 Folien, nur Punkt 01 ausgeführt, Rest doppelt mit KSt-Staffel/Hebesatz/Hinzurechnung/latente Steuern/Rückstellung. Freibetrag/Abrundung und § 8c-Ausnahmen in der Bildunterschrift. alt_texte.json. |
| Do 26.11. 17:45 | 🎬 Reel `57-reel-verlust-8c` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (115_marimba_corporate, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-13. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-06 17:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-11-01 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-11-01 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p57_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf (d3): aus Bibliothek (R4 gegengelesen), Reel ohne Stimme 13,6 s, −17,8 LUFS, Atmo Uhr + Fehlerton im Hook, Musik 10 Spannung. Titelbild neu als Zahl-Hook „51 % verkauft? Verluste weg.“, Karten aus karussell/par8c Folie 2 (Regel) und 3 (Rettungsanker), ampel_8c_* (Demo-Quoten) bewusst nicht genutzt. Bildunterschrift: § 8c Abs. 1 Satz 1/4/5–8, Abs. 1a, § 8d KStG, § 10a Satz 10 GewStG, Zinsvortrag § 8a Abs. 1 Satz 3 KStG. Sa 11:45 bleibt frei (Stimm-Slot). jobs/p57_reel_verlust_8c.json, Karten schnitt/p57_58_karten_bauen.py, Schnitt schnitt/p57_reel_verlust_8c.json. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-26. |
| Fr 27.11. 17:45 | 🎬 Reel `50-reel-gebaeude-afa` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (112_jazzhop, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10.: Loris bestätigt „mehr als doppelt so schnell“ – bleibt so. · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-07. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-01 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-11-01 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-11-02 17:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p50_reel_stimme_bauen.py, Vorschau vorschau_stimme.png). Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R5 gegengelesen), Reel ohne Stimme 15,0 s, −18,0 LUFS, Musik 08 Chill House. Titelbild = reels/reel_gebaeude (unverändert), 3 Punkte = karussell/gebaeude_afa Folien 3–5 (linear § 7 Abs. 4, degressiv 5 % § 7 Abs. 5a, Sonder-AfA § 7b EStG). Demo 400.000 € → 12.000 € / 20.000 € / 19.000 € nachgerechnet. Grund und Boden + Voraussetzungen Betriebsgebäude in der Bildunterschrift. jobs/p50_reel_gebaeude_afa.json, Karten schnitt/p48_50_karten_bauen.py, Schnitt schnitt/p50_reel_gebaeude_afa.json. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-27. |
| Sa 28.11. 17:45 | 🎬 Reel `53-reel-iab` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (136_modern_jazz_leicht, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-06. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-06 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-30 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-10-31 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p53_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf (d2): aus Bibliothek (R6 gegengelesen, karussell/iab_2), Begleit-Reel zum Karussell 53 am Do 17:45, ohne Stimme 14,0 s, −18,0 LUFS (Peak −5,6 dBFS), Musik 08 Chill House. Titelbild „Heute abziehen. Später kaufen.“, Karten aus iab_2 Folien 2/3, Einblendung „Nicht investiert? Rückwirkend weg.“ (§ 7g Abs. 3 EStG, § 233a AO) und Abspann TOOL neu (jobs/p53_iab.json), Schnitt schnitt/p53_reel_iab.json. Geprüft: § 7g Abs. 1 (50 %, Gewinngrenze 200.000 €, Höchstbetrag 200.000 €), Abs. 2 (Hinzurechnung/Kürzung im Kaufjahr), Abs. 3; Demo 60.000 € → 30.000 €. · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-11-28. |
| So 29.11. 17:45 | 🖼️ Karussell `51-karussell-kapitalertraege` | 🟢 freigegeben (geht automatisch online) | 29.10.: verschoben 2026-11-25 → 2026-11-29 (K01 KI-Befehle am 04.11., Loris go). · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-25. · 25.10.: Termin 2026-11-03 11:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf: aus Bibliothek (R6 gegengelesen), karussell/kapitalertraege Folien 1–6 unverändert; Folie 7 neu: „Speichern für die Steuererklärung“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p51_kapitalertraege.json). Nachgerechnet: (3.000 − 1.000) × 26,375 % = 527,50 €. Alt-Texte in alt_texte.json. KW 45 ungerade → Karussell abends. |
| Mo 30.11. 17:45 | 🎬 Reel `32-reel-mindeststeuer` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (122_lofi_hiphop, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-14. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-08 17:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-11-02 11:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-11-02 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p32_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), Reel ohne Stimme 14,6 s (Titelbild reel_mindeststeuer + 3 Karten nach karussell/mindeststeuer + Abspann TOOL), Musik 12_pop_electronic. Schnitt: vorlagen/system/schnitt/p32_reel_mindeststeuer.json |
| Di 01.12. 17:45 | 🎬 Reel `34-reel-einspruch` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (130_pop_electronic_clean, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Loris – Einspruch heute zu speziell, breiteres Thema zuerst → 2026-11-02 17:45. · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-10-26. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-10-26 11:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-10-26 11:45. · 25.10.: go Loris für Premium-Fassung v4 (leisere Töne), So 17:45 per Lauf auf Arbeitsbranch. · 25.10.: Premium-Fassung im Motion-Design-Look (Loris' Design-Screenshots): HTML-Animation vorlagen/system/premium/einspruch.html, Bau premium/reel_bauen.py, 27 s, −18 LUFS, Loris' Stimme, Titelbild = Frame 1; klassische Fassung reel_stimme_klassisch.mp4. Vorschlag So 25.10. 17:45, wartet auf go. · 25.10.: Hook auf Ergebnis umgestellt („Bescheid am 5.10. / Einspruch bis 9.11.“), 26,9 s, −18 LUFS; vorgeschlagen für So 25.10. 17:45 (Autopilot), wartet auf go. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p34_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 14.10. Nachtlauf: aus Bibliothek (R6 gegengelesen), Reel ohne Stimme 14,6 s, Fall: zur Post Mo 05.10. → bekannt Fr 09.10. (§ 122 Abs. 2 Nr. 1 AO, 4 Tage seit 2025) → Frist Mo 09.11. (§ 355 AO), § 361 AO. Uhr-Atmo + 07_minimal_tech. Schnitt: vorlagen/system/schnitt/p34_reel_einspruch.json · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-12-01. |
| Di 01.12. 17:50 | 📱 Story `34-story-tipp` | 🟢 freigegeben (geht automatisch online) | 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Loris – Einspruch heute zu speziell, breiteres Thema zuerst → 2026-11-02 17:50. · 25.10.: mit dem Einspruch-Reel auf Mo 12:15. · 25.10.: mit dem Reel auf 17:50 (go Loris). · 14.10. Nachtlauf: aus Bibliothek (R6 gegengelesen), Tipp-Story nach tipp_einspruch (korrigierte Fassung: Aufgabe zur Post + 4 Tage) mit Emoji-Reaktion 👏/😮 – kein Quiz, damit keine Auflösung Mo nötig |
| Mi 02.12. 17:45 | 🖼️ Karussell `46-karussell-dividenden-8b` | 🟢 freigegeben (geht automatisch online) | 29.10.: verschoben 2026-11-29 → 2026-12-02 (K01 KI-Befehle am 04.11., Loris go). · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-29. · 25.10.: Termin 2026-11-04 17:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), karussell/par8b Folien 1–5 unverändert; Folie 6 neu: „Speichern für später“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p46_dividenden_8b.json). Bildunterschrift nennt laut Prüfbericht 10-%-Grenze (§ 8b Abs. 4 KStG, Beginn des Kalenderjahres) und 5 % nbBA (§ 8b Abs. 5 KStG); GewSt-Schachtel § 9 Nr. 2a GewStG ab 15 % zu Beginn des EZ, sonst § 8 Nr. 5 GewStG. Nachgerechnet: 5.000 × 15,825 % = 791 €, × 14 % = 700 €, Summe 1.491 €. Alt-Texte in alt_texte.json. Abgrenzung zum Kürzungen-Karussell (18.10.): dort nur Schachtel-Zeile. |
| Do 03.12. 17:45 | 🎬 Reel `33-reel-paragraf-formel` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (115_marimba_corporate, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-16. · 25.10. nachm.: 1 Reel + 1 Karussell pro Tag bis 08.11. (Loris), jetzt 2026-11-07 17:45. · 25.10. ~12:30: Reihenfolge nach Wochentag/Stimmung neu (Loris), jetzt 2026-11-02 17:45. · 25.10.: volle Freigabe Loris (Premium-Look mit Stimme), Raster 2026-11-01 11:45. · 24.10.: mit Loris' Stimme (Aufnahme 21.10.) neu gebaut nach Wissen 24.10. (Hook ab Frame 1, Bau schnitt/p33_reel_stimme_bauen.py, Vorschau vorschau_stimme.png), alte Fassung reel_ohne_stimme.mp4. Wartet auf go. · 24.10.: auf Mo 26.10. getauscht mit Bewirtung (go Loris), Umbau nach Wissen 24.10. offen. · 14.10. Nachtlauf: aus Bibliothek (R4 gegengelesen), Reel ohne Stimme 14,4 s (3 Normen als Formel: § 8 Nr. 1 GewStG, § 4 Abs. 5 S. 1 Nr. 1 EStG, § 8b Abs. 5 KStG; Abspann abspann_paragraf; Titelbild neu mit „Drei Normen“ statt „Fünf“). Raster Sa mittags = Stimme → Abweichung (keine Aufnahme). Schnitt: vorlagen/system/schnitt/p33_reel_paragraf_formel.json · 26.10. abends: Trichter-Mix (Wissen 21, Ziel Follower) → 2026-12-03. |
| Fr 04.12. 17:45 | 🎬 Reel `i05-reel-insider-finanzbeamte` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (121_minimal_house, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-10-27. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #05 (Aufnahme 26.10.), Premium-Look premium/insider_05.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 27.10. 17:35: Platz an Mein Weg #01 abgegeben (Loris), neu 04.12. |
| Sa 05.12. 17:45 | 🎬 Reel `i09-reel-insider-elterngeld` | 🟢 freigegeben (geht automatisch online) | 30.10.: Musik neu (127_tech_groove, hell/rhythmisch – Loris: keine düstere Musik), einmalig neu abgemischt. · 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-10-29. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 26.10.: Serie Finanzamt-Insider #09 (Aufnahme 26.10.), Premium-Look premium/insider_09.html. Freigabe Loris („Freigabe für alles mit Sprachnachricht“). · 29.10.→05.12. (Platz an Mein Weg #02, Welle nach #01 nutzen). |
| So 06.12. 17:45 | 🖼️ Karussell `59-karussell-pensionen` | 🟢 freigegeben (geht automatisch online) | 29.10.: verschoben 2026-12-02 → 2026-12-06 (K01 KI-Befehle am 04.11., Loris go). · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-12-02. · 25.10.: Termin 2026-11-05 11:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf (d3): aus Bibliothek (R4 gegengelesen, keine offenen Punkte), karussell/pension Folien 1–5 unverändert; Folie 6 neu: „Speichern für die Gutachten-Saison“ + „Wer in deinem Team braucht das?“ + TOOL (jobs/p59_pensionen.json). Letzter Testmonat-Tag: Bildunterschrift mit Community-Auswahl „Welches Thema als Nächstes: A) Teilwertabschreibung oder B) Rechnungsabgrenzung?“. Fachlich: § 6a Abs. 1, Abs. 3 Satz 3 EStG (6 %), § 253 Abs. 2 und 6 HGB (10-Jahres-Durchschnitt, Ausschüttungssperre), § 274 HGB (Wahlrecht Aktivüberhang). Alt-Texte in alt_texte.json. |
| Mi 09.12. 17:45 | 🖼️ Karussell `41-karussell-mythen` | 🟢 freigegeben (geht automatisch online) | 29.10.: verschoben 2026-12-06 → 2026-12-09 (K01 KI-Befehle am 04.11., Loris go). · 26.10. 15:30: Reihenfolge nach Viral-Potenzial (Loris: „das virale als erstes“) → 2026-10-28. · 26.10. abends: Reihenfolge Insider-Serie zuerst (Loris). · 25.10. nachm.: Takt 1 Beitrag/Tag 17:45, Reels täglich, Karussell Mi+So (Loris nach Auswertung), jetzt 2026-11-08. · 25.10.: Termin 2026-10-29 11:45 reserviert, Premium-Look fertig, freigegeben (go Loris). · 14.10. Nachtlauf: aus Bibliothek (R3 gegengelesen), karussell/mythen Folien 1–7 (nicht mythen_3), Folie 8 neu: Speichern + Weiterleiten + TOOL statt offener Kommentarfrage (jobs/p41_mythen.json). Ablaufhemmung § 147 Abs. 3 Satz 5 AO in der Bildunterschrift. alt_texte.json. · 28.10.→06.12. (Platz an Insider #14 Ferrari). |

## ✅ Zuletzt veröffentlicht (Autopilot)

- Mi 04.11. 17:45 · 🖼️ Karussell `k01-karussell-ki-befehle` · [ansehen](https://www.instagram.com/p/DfUzoUhoMFD/) (online 2026-11-04 17:45)
- Di 03.11. 17:45 · 🎬 Reel `45-reel-vga` · [ansehen](https://www.instagram.com/reel/DfSO9Gagk8j/) (online 2026-11-03 17:45)
- Mo 02.11. 17:45 · 🎬 Reel `i02-reel-insider-kontenabruf` · [ansehen](https://www.instagram.com/reel/DfPwiKDkcWo/) (online 2026-11-02 17:45)
- So 01.11. 17:45 · 🖼️ Karussell `mbs-karussell-launch` · [ansehen](https://www.instagram.com/p/DfNdBsEmmdN/) (online 2026-11-01 20:11)
- So 01.11. 17:45 · 🖼️ Karussell `35-karussell-steuerkalender` · [ansehen](https://www.instagram.com/p/DfNFAr9lLsn/) (online 2026-11-01 17:45)
- Sa 31.10. 17:45 · 🎬 Reel `52-reel-gobd` · [ansehen](https://www.instagram.com/reel/DfKgI-ZEb9C/) (online 2026-10-31 17:45)
- Fr 30.10. 17:45 · 🎬 Reel `i01-reel-insider-programm` · [ansehen](https://www.instagram.com/reel/DfILcg8DfQm/) (online 2026-10-30 19:02)
- Do 29.10. 17:45 · 🎬 Reel `i14-reel-insider-ferrari` · [ansehen](https://www.instagram.com/reel/DfFcLcFk7yt/) (online 2026-10-29 17:45)
- Mi 28.10. 17:45 · 🎬 Reel `m02-reel-mein-weg-haeufigster-fehler` · [ansehen](https://www.instagram.com/reel/DfC3UzMCo4m/) (online 2026-10-28 17:45)
- Mi 28.10. 12:15 · 📱 Story `meme2-story` · [ansehen](https://www.instagram.com/stories/maehrsteuern/4017955438842916913) (online 2026-10-28 15:27)

## 📈 Zahlen (täglich ca. 08:45)

**809 Follower** · 35 Beiträge im Profil (Abruf 2026-11-05) · **-4** seit 2026-11-04 ⚠️
Reichweite pro Tag: 02.11. **30025** · 03.11. **165** · 04.11. **49** · 05.11. **0**

| Beitrag (letzte 14 Tage) | Aufrufe | Erreicht | Likes | Komm. | Gespeichert | Geteilt |
|---|---|---|---|---|---|---|
| Mi 04.11. 17:45 [30 KI-Befehle für Steuer-Profis – ohne G](https://www.instagram.com/p/DfUzoUhoMFD/) | 53 | 23 | 0 | 0 | 1 | 0 |
| Di 03.11. 17:45 [Ein Darlehen an dich selbst – und für de](https://www.instagram.com/reel/DfSO9Gagk8j/) | 160 (+12) | 137 | 1 | 1 | 0 | 0 |
| Mo 02.11. 17:45 [Das Finanzamt sieht deine Bankkonten – a](https://www.instagram.com/reel/DfPwiKDkcWo/) | 204 (+10) | 165 | 2 | 1 | 0 | 0 |
| So 01.11. 20:11 [Ich bin aus dem Finanzamt raus. Heute ge](https://www.instagram.com/p/DfNdBsEmmdN/) | 562 (+7) | 346 | 4 | 1 | 4 | 0 |
| So 01.11. 17:45 [GewSt-Vorauszahlung am 15.11.: Gezahlt w](https://www.instagram.com/p/DfNFAr9lLsn/) | 428 (+6) | 265 | 2 | 1 | 2 | 0 |
| Fr 30.10. 19:02 [Deine Steuererklärung liest zuerst kein ](https://www.instagram.com/reel/DfILcg8DfQm/) | 573 (+0) | 471 | 14 | 1 | 5 | 4 |
| Do 29.10. 17:45 [Ferrari über die Firma? Beim Finanzamt e](https://www.instagram.com/reel/DfFcLcFk7yt/) | 635 (+0) | 525 | 5 | 1 | 2 | 1 |
| Mi 28.10. 17:45 [Der häufigste Fehler, den ich im Finanza](https://www.instagram.com/reel/DfC3UzMCo4m/) | 909 (+11) | 714 | 8 | 1 | 6 | 6 |
| Di 27.10. 18:01 [Ich hab gezahlt, um aus dem sichersten J](https://www.instagram.com/reel/DfAWBBflLkW/) | 2552 (+7) | 1961 | 25 | 1 | 12 | 46 |
| Mo 26.10. 17:45 [Die Rente deiner Oma kann steuerpflichti](https://www.instagram.com/reel/De9tD9vj4EH/) | 599 (+1) | 478 | 9 | 5 | 10 | 9 |
| So 25.10. 17:45 [Ein einziger Euro entscheidet: 799 € net](https://www.instagram.com/reel/De7JF3cAGrX/) | 1221 (+2) | 1079 | 15 | 1 | 12 | 70 |
| Sa 24.10. 11:17 [Ohne Anlass auf dem Bewirtungsbeleg: 0 %](https://www.instagram.com/reel/De3yheAFKBg/) | 546 (+0) | 451 | 6 | 1 | 3 | 3 |
| Do 22.10. 15:45 [Finanzamt: Du denkst, es weiß nur, was i](https://www.instagram.com/reel/DezHdgPt1_0/) | 1364 (+0) | 1091 | 19 | 10 | 17 | 62 |

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

**Do 05.11.2026**
- 10:36 ✍️ Story-Slots wieder an: Frage + Teaser zu i03 (heute) und i06 (morgen) ([`1b3a31b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/1b3a31ba1ac2f5d82e4cabf56a9cc09f8d4e3598))
  - Plan: neu `i03-story-frage` (2026-11-05 12:15, freigegeben); neu `i03-story-teaser` (2026-11-05 17:50, freigegeben); neu `i06-story-frage` (2026-11-06 12:15, freigegeben); neu `i06-story-teaser` (2026-11-06 17:50, freigegeben)
- 09:31 📡 Radar 2026-11-05: 8 Beiträge, 0 DM-Entwürfe ([`b727aee`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b727aee407caa7bf950e2172dd034c5c9053ea6d))
  - `automatik/interaktion`
- 09:24 📈 Statistik 2026-11-05 ([`8b5d1c6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8b5d1c6b0323df8d17cf115292bae7c74ffb6b7d))
  - `automatik/statistik`

**Mi 04.11.2026**
- 17:45 🤖 Autopilot: k01-karussell-ki-befehle veroeffentlicht ([`cb07761`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/cb07761beda1dc02b1b48215da88e61db98685ba))
  - Plan: `k01-karussell-ki-befehle` status: freigegeben → veroeffentlicht; `k01-karussell-ki-befehle` online: https://www.instagram.com/p/DfUzoUhoMFD/
- 16:40 🤖 Autopilot: Dateien fuer k01-karussell-ki-befehle vorbereitet ([`cf07583`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/cf075835eae629341cbee83daa81bf19a90e5b26))
  - `posts/k01_2026-11-04_ki_befehle`
- 09:29 📡 Radar 2026-11-04: 8 Beiträge, 0 DM-Entwürfe ([`c592489`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c592489f7d3fadeef9a707f174d5bc4c9000aa18))
  - `automatik/interaktion`
- 09:21 📈 Statistik 2026-11-04 ([`e4eb3d5`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e4eb3d5afa4db2872fd225a01a6921e6a38dfc64))
  - `automatik/statistik`

**Di 03.11.2026**
- 17:45 🤖 Autopilot: 45-reel-vga veroeffentlicht ([`5d7cd04`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5d7cd048dff6b0d13bdfc0b299a1add000f2ff22))
  - Plan: `45-reel-vga` status: freigegeben → veroeffentlicht; `45-reel-vga` online: https://www.instagram.com/reel/DfSO9Gagk8j/
- 16:41 🤖 Autopilot: Dateien fuer 45-reel-vga vorbereitet ([`69ac547`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/69ac54752b4589c299c86f934b0cdda36ac4c769))
  - `posts/45_2026-10-31_reel_vga`
- 12:58 📈 Statistik 2026-11-03 ([`8892859`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8892859d0dbd881c87fa87e7f59fb9a226d70ce0))
  - `automatik/statistik`
- 09:29 📡 Radar 2026-11-03: 8 Beiträge, 0 DM-Entwürfe ([`dac1011`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/dac1011f4dca82dfbda7191da3e9c745d601980f))
  - `automatik/interaktion`
- 09:21 📈 Statistik 2026-11-03 ([`5460242`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5460242505006811a66437f8e6d05e8ab2c9bdfc))
  - `automatik/statistik`

**Mo 02.11.2026**
- 17:45 🤖 Autopilot: i02-reel-insider-kontenabruf veroeffentlicht ([`8639359`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/86393595b8afbaef110909459fbc001dda2f121a))
  - Plan: `i02-reel-insider-kontenabruf` status: freigegeben → veroeffentlicht; `i02-reel-insider-kontenabruf` online: https://www.instagram.com/reel/DfPwiKDkcWo/
- 17:38 🤖 Autopilot: Dateien fuer i02-reel-insider-kontenabruf vorbereitet ([`0d480d9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0d480d9d35d42a187b9f31f4977ceffc465ea219))
  - `posts/i02_2026-10-26_insider_kontenabruf`
- 11:05 ✍️ Plan: i02 Kontenabruf heute 17:45, i06 Schätzung auf Fr 06.11. getauscht ([`8642a7c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8642a7c08f4f88a23f33ae7acb96771a9076b643))
  - Plan: `i02-reel-insider-kontenabruf` zeit: 2026-11-06 17:45 → 2026-11-02 17:45; `i06-reel-insider-schaetzung` zeit: 2026-11-02 17:45 → 2026-11-06 17:45
- 09:46 ✍️ Vorbilder-Radar: Ausreißer der Woche ([`94fe6e0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/94fe6e0eddc52fa2c055a881a8e94c035be087e7))
  - `recherche/viral_liste.csv`, `recherche/vorbilder.json`, `recherche/vorbilder_bericht.md`
- 09:44 📡 Radar 2026-11-02: 8 Beiträge, 0 DM-Entwürfe ([`2ae9848`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2ae9848e4c7c21a333189869ed3b83a62b36a644))
  - `automatik/interaktion`
- 09:37 📈 Statistik 2026-11-02 ([`5c60f4a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/5c60f4a9c592c52e31af95ed472bcbee31645e01))
  - `automatik/statistik`

**So 01.11.2026**
- 20:15 ✍️ Wochenbericht KW 2026-44 ([`e068e28`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e068e28f47704b5fa346f681b83526565eb2d376))
  - `automatik/statistik`
- 20:12 🤖 Autopilot: mbs-karussell-launch veroeffentlicht ([`b8b3d63`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b8b3d638f7660a8945ea5aa44007ab30efabdc09))
  - Plan: `mbs-karussell-launch` status: freigegeben → veroeffentlicht; `mbs-karussell-launch` online: https://www.instagram.com/p/DfNdBsEmmdN/
- 20:08 🤖 Autopilot: Dateien fuer mbs-karussell-launch vorbereitet ([`c9de85b`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c9de85bcc9cfe0cb649c12977f97966e94bb582a))
  - `posts/mbs_2026-11-01_launch`
- 17:45 🤖 Autopilot: 35-karussell-steuerkalender veroeffentlicht ([`7b8ee50`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7b8ee502cae80384c32cb19c2a661097ce59efb7))
  - Plan: `35-karussell-steuerkalender` status: freigegeben → veroeffentlicht; `35-karussell-steuerkalender` online: https://www.instagram.com/p/DfNFAr9lLsn/
- 16:47 ✍️ MBS-Launch-Karussell für So 01.11. 17:45 freigegeben (go Loris) ([`ebdb799`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ebdb799fa8635801751b38f32e65afb6673c3f1e))
  - Plan: `mbs-karussell-launch` status: entwurf → freigegeben; `mbs-karussell-launch` zeit: 2026-11-01 13:45 → 2026-11-01 17:45
- 11:46 ✍️ MBS-Launch-Karussell 01.11.: 9 Folien Premium-Look, Bildunterschrift, Alt-Texte, LinkedIn-PDF und -Text, Plan-Eintrag 13:45 (Entwurf) ([`b05a2e7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b05a2e746b7ad5cc0b19f96ce3c4e15ca6424295))
  - Plan: neu `mbs-karussell-launch` (2026-11-01 13:45, entwurf)
- 16:39 🤖 Autopilot: Dateien fuer 35-karussell-steuerkalender vorbereitet ([`23faf63`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/23faf632c861c7b2bfcdb701437e826dfd64eee4))
  - `posts/35_2026-10-25_steuerkalender`
- 09:22 📈 Statistik 2026-11-01 ([`8352e13`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/8352e13e2ba75bcebd19a205a731bee365b4a460))
  - `automatik/statistik`
- 09:08 📡 Radar 2026-11-01: 8 Beiträge, 0 DM-Entwürfe ([`4030dff`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4030dff8bc62e6979270a4350ca9e6ce5f3aaec3))
  - `automatik/interaktion`
- 09:07 📈 Statistik 2026-11-01 ([`6516a7d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6516a7da922c15c665a7706cc67a549893e23db4))
  - `automatik/statistik`

**Sa 31.10.2026**
- 17:45 🤖 Autopilot: 52-reel-gobd veroeffentlicht ([`6b8e212`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6b8e2120700b8385b401cc6246303e7993bb814a))
  - Plan: `52-reel-gobd` status: freigegeben → veroeffentlicht; `52-reel-gobd` online: https://www.instagram.com/reel/DfKgI-ZEb9C/
- 16:39 🤖 Autopilot: Dateien fuer 52-reel-gobd vorbereitet ([`d6b1650`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d6b165079eeb060f6e2f291635273e423cfa05d4))
  - `posts/52_2026-11-04_reel_gobd`
- 09:27 📡 Radar 2026-10-31: 8 Beiträge, 0 DM-Entwürfe ([`6dc1100`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6dc1100c9fdf09ca8031fd7f9fa3de4e39f30651))
  - `automatik/interaktion`
- 09:20 📈 Statistik 2026-10-31 ([`b8b8dba`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b8b8dba1e584e1c9a7286f8b24176b03ed9eb586))
  - `automatik/statistik`

**Fr 30.10.2026**
- 19:02 🤖 Autopilot: i01-reel-insider-programm veroeffentlicht ([`b742235`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b7422353ad44ff7cf2208bc57f1d1fa7b9b905c2))
  - Plan: `i01-reel-insider-programm` status: freigegeben → veroeffentlicht; `i01-reel-insider-programm` online: https://www.instagram.com/reel/DfILcg8DfQm/
- 19:00 🤖 Autopilot: Dateien fuer i01-reel-insider-programm vorbereitet ([`d375fa3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d375fa338b46d4f1c5d0dda6b07651bf7d3ed062))
  - `automatik/plan.json`, `posts/i01_2026-10-26_insider_programm`
- 16:57 ✍️ Neue Asset-Quelle: KI-Bilder über Runway-Connector (Nano Banana Pro) neben eigenen Assets und Claude-Animationen ([`ef71737`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ef71737c139349c0ca174d3e23f3a97bb4495e74))
  - `README.md`, `automatik/lage_notizen.md`, `strategie/09_reel_regeln.md`
- 11:37 🎵 Musik aller 27 geplanten Reels einmalig neu abgemischt (hell/rhythmisch), düstere Tracks gesperrt ([`b226194`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/b22619480cabf2642a93411ca823b1317a18e06f))
  - `LAGE.html`, `automatik/lage_notizen.md`, `automatik/plan.json`, `musik/README.md`, `posts/32_2026-10-23_reel_mindeststeuer`, `posts/33_2026-10-24_reel_paragraf_formel`, `…`
- 09:36 📈 Statistik 2026-10-30 ([`306d2f3`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/306d2f3df37992e1b8318614542af84b120eaef6))
  - `automatik/statistik`
- 08:24 📡 Radar 2026-10-30: 8 Beiträge, 0 DM-Entwürfe ([`7f8a129`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/7f8a12946273379606ee28fd117c888dd4db3dc3))
  - `automatik/interaktion`

<details><summary>Älter als 7 Tage</summary>

**Do 29.10.2026**
- 17:45 🤖 Autopilot: i14-reel-insider-ferrari veroeffentlicht ([`9b35784`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9b35784f38ace125a99febdc95872e67bc7ef5cc))
  - Plan: `i14-reel-insider-ferrari` status: freigegeben → veroeffentlicht; `i14-reel-insider-ferrari` online: https://www.instagram.com/reel/DfFcLcFk7yt/
- 17:28 🤖 Autopilot: Dateien fuer i14-reel-insider-ferrari vorbereitet ([`43f09d0`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/43f09d0332a8728d97f40ff3f426cdd2b51347b9))
  - `posts/i14_2026-10-27_insider_ferrari`
- 13:27 ✍️ Ferrari-Reel: kopierte M1-Felder wirklich entfernt ([`ad27664`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ad276642f838607e45ce681eedfbf20a10035df5))
  - `LAGE.html`, `automatik/plan.json`
- 13:26 ✍️ Ferrari-Reel: versehentlich kopierte media_id/veroeffentlicht_am von M1 entfernt (Hinweis Nebensitzung) ([`bfdca97`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/bfdca97a03afd658d2e3a4f428035a9eaa514f98))
  - `LAGE.html`
- 09:30 💼 LinkedIn-Pakete: k01-karussell-ki-befehle ([`3c996e6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/3c996e68f57472327a5efe32e7c79b3b5f99aac0))
  - `posts/k01_2026-11-04_ki_befehle`
- 09:28 📡 Radar 2026-10-29: 8 Beiträge, 0 DM-Entwürfe ([`d232b9f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d232b9fd93357448173465a87d0d654618f7a841))
  - `automatik/interaktion`
- 09:22 📈 Statistik 2026-10-29 ([`75377c6`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/75377c61651c368497a960009de6381415b1cd4e))
  - `automatik/statistik`
- 05:32 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`38b836d`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/38b836d7707747d070704a3c013b4f4024c00e8d))
- 05:32 💼 LinkedIn-Bild Mein Weg: ganzes Diplomtag-Foto (Loris' Wahl) ([`2f0e1ff`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2f0e1ffaf3f21b7908f6f81e8ce9c5aaae9b3190))
  - `vorlagen/system/linkedin_mein_weg.html`
- 05:27 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`c818835`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/c818835d161dd69eee821f8ace2b2ecaf4d2584d))
- 05:27 💼 LinkedIn-Bild-Vorlage Mein Weg #01 (Split: Hook + Eckdaten + Foto) ([`00205e9`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/00205e95ada46f9e63ac4d73c6cb845d509bc4be))
  - `vorlagen/system/linkedin_mein_weg.html`
- 03:17 🔀 Merge claude/instagram ([`4bce94c`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/4bce94c6b3821e99cd0d23a6303e69fb450b7a92))
- 03:17 ✍️ Wissen §10: Storytelling-Reels in 6 Schritten, Abgleich M1/M2 ([`6a44b00`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/6a44b001ad19dcad1f23d3aa1d70adee69945144))
  - `LAGE.html`, `strategie/21_wissen_trichter.md`
- 02:44 🔀 Merge claude/instagram ([`fabfb5f`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/fabfb5f35205ff2b9e7851fcc0fb531976817384))
- 02:43 ✍️ Stichwort-Antworten ohne ManyChat: PROMPT/TOOL bekommen automatisch DM + öffentliche Antwort ([`2fe7701`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/2fe77013f3d9e9ee373c246d3348372cd5caff16))
  - `.github/workflows`, `LAGE.html`, `automatik/interaktion.json`, `automatik/kommentare.py`, `automatik/lage_notizen.md`
- 02:42 🔀 Merge claude/instagram ([`d739e16`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/d739e1619c7e55084f6329c641102285f2a9105f))
- 02:41 ✍️ K01 KI-Befehle für Mi 04.11. freigegeben, Karussell-Reihe um einen Platz verschoben ([`834bc02`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/834bc02b4cab49e0f6572f8e34403b99fc36d726))
  - Plan: `31-karussell-zinsschranke` zeit: 2026-11-11 17:45 → 2026-11-15 17:45; `10-e-rechnung` zeit: 2026-11-04 17:45 → 2026-11-08 17:45; `37-karussell-bp-vorbereitung` zeit: 2026-11-08 17:45 → 2026-11-11 17:45; `41-karussell-mythen` zeit: 2026-12-06 17:45 → 2026-12-09 17:45; `44-karussell-glossar` zeit: 2026-11-22 17:45 → 2026-11-25 17:45; `46-karussell-dividenden-8b` zeit: 2026-11-29 17:45 → 2026-12-02 17:45; `51-karussell-kapitalertraege` zeit: 2026-11-25 17:45 → 2026-11-29 17:45; `53-karussell-iab` zeit: 2026-11-15 17:45 → 2026-11-18 17:45; `56-karussell-verjaehrung` zeit: 2026-11-18 17:45 → 2026-11-22 17:45; `59-karussell-pensionen` zeit: 2026-12-02 17:45 → 2026-12-06 17:45; `k01-karussell-ki-befehle` status: entwurf → freigegeben
- 02:29 ✅ Freigabe angefragt (1 Beitrag/Beiträge) ([`abc2a38`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/abc2a38e10bbfcdb5dbae027b5fa568cd092c574))
  - Plan: `k01-karussell-ki-befehle` → Freigabe-Issue #93
- 02:27 🔀 Merge claude/instagram ([`248cdfb`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/248cdfbd9f63ed27498f49f52ad7b15af3699480))
- 02:27 ✍️ Karussell K01 „30 KI-Befehle für Steuer-Profis“ als Entwurf, Bio A notiert ([`9689932`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/96899329395943fac5fceae784d7da4961aa85ae))
  - Plan: neu `k01-karussell-ki-befehle` (2026-11-04 17:45, entwurf)
- 02:20 🔀 Merge claude/instagram ([`0495009`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0495009736a3f1db2fbce6d99d6d470f5cff842b))
- 02:19 ✍️ Bio-Varianten A/B und Wissen §9 Spickzettel-Karussell (herr_tech) ergänzt ([`54e5c47`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/54e5c476ed12e512c917e366e48fc76194431270))
  - `LAGE.html`, `strategie/02_bio_highlights.md`, `strategie/21_wissen_trichter.md`

**Mi 28.10.2026**
- 22:31 🔀 Merge claude/instagram ([`ebce622`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ebce62239bf56ad60fe18369ed186ef23af03401))
- 22:31 ✍️ Auswertung Mein Weg #01 nach 28 h ergänzt (Wissen 21 §8) ([`abeef1a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/abeef1a679b58ba5b89ca95229f62cbf2bf03aca))
  - `LAGE.html`, `strategie/21_wissen_trichter.md`
- 22:28 ✍️ Memes gestrichen (Loris), restliche Meme-Storys nicht mehr posten ([`9ace857`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9ace85793f13ff6124916a9d59eaef16f1449fb3))
  - Plan: `meme1-story` status: freigegeben → gestrichen; `meme3-story` status: freigegeben → gestrichen; `meme4-story` status: freigegeben → gestrichen; `meme5-story` status: freigegeben → gestrichen
- 17:45 🤖 Autopilot: m02-reel-mein-weg-haeufigster-fehler veroeffentlicht ([`61c8fff`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/61c8fff6efb00abd3eaaf16e311f3d065a7d8995))
  - Plan: `m02-reel-mein-weg-haeufigster-fehler` status: freigegeben → veroeffentlicht; `m02-reel-mein-weg-haeufigster-fehler` online: https://www.instagram.com/reel/DfC3UzMCo4m/
- 17:24 🤖 Autopilot: Dateien fuer m02-reel-mein-weg-haeufigster-fehler vorbereitet ([`ff226ef`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/ff226ef943803b96ae9270f4fb87170888e704b2))
  - `posts/m02_2026-10-29_mein_weg_haeufigster_fehler`
- 15:27 🤖 Autopilot: meme2-story veroeffentlicht ([`9de7cf1`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/9de7cf10a1896806a09342ae97ea0d7df36d9274))
  - Plan: `meme2-story` status: freigegeben → veroeffentlicht; `meme2-story` online: https://www.instagram.com/stories/maehrsteuern/4017955438842916913
- 15:25 🤖 Autopilot: Dateien fuer meme2-story vorbereitet ([`de27104`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/de271041e776205f8a39c4394bba02190a826a5b))
  - `posts/memes_2026-10`
- 09:20 📈 Statistik 2026-10-28 ([`e091915`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/e0919153d163f380bcbed9acd9e993b82db71101))
  - `automatik/statistik`
- 08:36 📡 Radar 2026-10-28: 8 Beiträge, 0 DM-Entwürfe ([`0b56bc7`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/0b56bc7b328ddc500b55139801b9f16eb97f26c5))
  - `automatik/interaktion`
- 08:34 ✍️ Tausch: Mein Weg #02 heute Mi 28.10. 17:45, Ferrari Do 29.10.; Meme-Storys passend getauscht (Loris: ja) ([`483fd51`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/483fd5170f0ffd27151f1138738702ad2283f6f6))
  - Plan: `i14-reel-insider-ferrari` zeit: 2026-10-28 17:45 → 2026-10-29 17:45; `m02-reel-mein-weg-haeufigster-fehler` zeit: 2026-10-29 17:45 → 2026-10-28 17:45; `meme1-story` zeit: 2026-10-28 12:15 → 2026-10-29 12:15; `meme2-story` zeit: 2026-10-29 12:15 → 2026-10-28 12:15
- 06:26 🔀 Merge remote-tracking branch 'origin/claude/instagram' into ccr-8ce2ce66-8i2ful ([`34cde22`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/34cde225374d741ef45bed7ed4e988f6ef889aac))
- 06:26 ✍️ Mein Weg #02: Fotos Selfie + Lehrgang + Markenportrait (lächelnd), MBS-Logo in der Tool-Szene ([`37bb51a`](https://github.com/MBS-maehrsteuern/Instagram-maehrsteuern/commit/37bb51a339afa3795901d03da5b82466c166e09c))
  - `posts/m02_2026-10-29_mein_weg_haeufigster_fehler`, `vorlagen/system/premium/mein_weg_02.html`
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

</details>
