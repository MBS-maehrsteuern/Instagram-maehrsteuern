# 🧭 Lage – maehrsteuern auf Instagram

_Automatisch erzeugt von `automatik/lage.py` – nicht von Hand bearbeiten (Notizen: `automatik/lage_notizen.md`). Stand: letzte Änderung Mo 19.10. 13:52 Uhr._

**Als Nächstes online:** 📱 Story `10-story-umfrage` am **Do 22.10. 12:45 Uhr** – 🟢 freigegeben (geht automatisch online)

## 📝 Gerade in Arbeit

- Neustart läuft: Start-Storys + Vorfreude (30.09.) und Neuvorstellung (Do 01.10. 18:30, von Hand) sind online. Nach 2 h: 26 erreicht, 6× geteilt, 0 neue Follower. Angepinnt ✓ (03.10.). Offen von Hand: Highlight „Start 👋“.
- Wochenrhythmus ab Okt. steht im Prompt der Content-Fabrik (Mo + Do 08:47, max. 4 Beiträge pro Lauf): Di/Do Karussell + Teaser, Mi Begleit-Reel, Fr Wissens-Reel oder Stimm-Reel, So Reel + Teaser, täglich 12:15 Story.
- Content-Fabrik nutzt ab Mo 05.10. die Lernpunkte aus `strategie/wettbewerb.md` (über Abschnitt in `08_hooks.md`): pro Lauf ≥ 1 Hook „konkreter Fall“ oder „Prüfer/Finanzamt“, Lernpunkt im Freigabe-Issue vermerkt. Routine-Prompt selbst unverändert (nur aus ihrer eigenen Sitzung änderbar).
- **So 04.10. umgebaut:** Statt Ampel-Reel geht 19:30 das Community-Reel „5 Sachen, die ich aus Excel rausgeschmissen hab“ online (Loris' Sprachnachricht, 41 s, keine Werbung, CTA: Zahl 1–5 in die Kommentare) + neue Teaser-Story 19:35. Ampel-Reel und alter Teaser stehen auf `pause` – kann später wieder eingeplant werden. Die Kommentar-Antworten (welche Nummer?) sind die Themen für die nächsten Reels.
- **Doppel-Post 04.10. behoben:** Das 5-Dinge-Reel ging zweimal raus (DeFLK53ALSs = im Plan, DeFLSBNFUXy = Duplikat, von Loris am 04.10. gelöscht ✓). Ursache: Ein Lauf startet mit dem Stand vom Startzeitpunkt und hat den Plan nur nach dem Warten neu geladen. `posten.py` holt jetzt direkt vor jedem Posten den neuesten Plan; klappt das nicht, wird nicht gepostet (nächster Lauf holt nach).
- **Di 06.10. 19:30 Reel „Nummer 1: Der Monatsbericht“ (Version 3)** freigegeben (go von Loris im Chat, 06.10.): dritte Aufnahme, Atmer raus, Pausen mit Raumton, 30 s. Karussell Excel-Fehler Mi 07.10., LinkedIn #18 Do 08.10., Split-Reel So 11.10.
- **Testmonat ab Mo 12.10. (bis So 08.11.): 2 Feed-Beiträge pro Tag, 12:15 + 19:30, Storys 12:45/19:35, täglich ≥ 1 Reel** – Raster und Konflikte in `strategie/15_plan_2_pro_tag.md`. Reels **12–15 s** (13–16 am 11.10. gekürzt, Langfassung reel_lang.mp4). Autopilot postet Reels (bestätigt: KSt-Reel Sa 19:30). Sprechtexte 18–22 (≤ 15 s) warten auf Aufnahme bis Mi 14.10. (Slots So 18. – Do 22.10. 19:30). Story Bio-Link Di 13.10. 19:35 (Entwurf). Mein Weg Fr 16.10.: KI-Label nach dem Posten in der App setzen. Offene Vorschläge zu freigegebenen Beiträgen: `strategie/13_backlog.md` (Umsetzung 11.10.).
- **Stumme Reels behoben (06.10.):** `montage.py` erzeugte bei bestimmten Tonspuren (Atmo/Musik ohne Stimme) eine Tonspur mit kaputten Zeitstempeln → im MP4 stumm. Betroffen: Split-Reel und KSt-Staffel-Reel – beide neu gerendert (−18,5 / −19,7 LUFS). Fix: `asetpts=N/SR/TB` nach `amix` + jede Spur auf volle Länge. Ab jetzt nach jedem Render Lautheit prüfen (sollte ca. −18 LUFS sein, −70 = stumm).
- **Edits-Test (06.10.):** Split-Reel Do 08.10. 19:30 baut Loris selbst in Edits und plant es dort (Status `manuell`, Paket in `posts/02_2026-10-06_excel_fehler/edits_paket/`, Anleitung als Google Doc im Drive). Grund: laut Mosseri (Aug. 2025) kleiner Reichweiten-Bonus für Edits-Reels, nur bei echtem Schnitt in Edits, „nicht für immer“ – aktueller Stand unbelegt, daher Test über 2–3 Reels gegen Autopilot-Reels. Woche dafür verschoben: latente Steuern Fr 09.10., KSt-Reel + „Heute 19:30“-Story Sa 10.10., Rückblick-Story So 11.10.
- Bis 10.10. alles freigegeben: 5-Dinge-Reel (So 04.10.), Excel-Fehler (Di 06.10.), Split-Reel als Begleit-Reel (Mi 07.10., vorgezogen), latente Steuern (Do 08.10.), Wissens-Reel KSt-Staffel (Fr 09.10.). So 11.10. ist frei → Fabrik am Mo 05.10.
- Latente Steuern: Prüfzettel Punkte 1–5 am 05.10. mit Quellen geprüft ✓ – Box Folie 6 präzisiert (kleine KapGes: von § 274 befreit, passive Latenzen ggf. als Rückstellung), fachlich nichts mehr offen (`pruefzettel.md` im Post-Ordner; „Abschluss 2026“ am 05.10. überall auf „spätestens jetzt“ geändert – Folien 1+7, Bildunterschrift, Teaser, LinkedIn-Text + PDF). Änderungen bis Mi 07.10. abends.
- Reel „Mein Weg“: Loris hat Variante B am 08.10. eingesprochen → fertig, Fr 16.10. 19:30 (Edits, `manuell`). **KI-Label beim Posten einschalten** (Karte 2 + 3 KI), Hinweis steht in der Bildunterschrift. Variante-A-Dateien als `*_variante_a.*` im Ordner.
- DM-Strecke läuft über **ManyChat** (Kommentar/Story-Antwort/DM mit Tool/TOOL/tool/tol → DM mit Demo-Link, Follow-up nach 23 h). Stichwörter nur in `automatik/interaktion.json` pflegen – Abweichungen meldet LAGE.md. Die eigenen Skripte schicken nie DMs.
- Interaktion läuft (Radar 50 Konten, Kommentar-Hilfe, LinkedIn-Pakete). **Sprint 1 (03.10.):** Wächter-Issue, Stichwort-Abgleich, Radar-Pflege montags, Erste-Stunde-Checkliste. **Kalender-Sync live (03.10.):** Termine gehen direkt in den Google-Kalender „maehrsteuern Autopilot“ (nur Postzeiten „beschäftigt“ für Reclaim, To-dos/LinkedIn „frei“; Farben + Pop-ups je Art). In Reclaim verbunden ✓, Freigabe nur Dienstkonto (nicht öffentlich, nicht im Hauptkalender) ✓ (Chrome 05.10.). `kalender.ics` entfällt. **Wochenbericht** ab So 04.10. ca. 18:00 als Issue – Demos/ManyChat per Kommentar nachtragen. Demo-Zahlen (entschieden 03.10.): Reclaim-Pflichtfeld „Woher kennst du mich?“ → Apps-Script „maehrsteuern Demo-Kopie“ kopiert Buchungen stündlich ohne Namen nach „maehrsteuern Autopilot“ → Wochenbericht zählt sie; UTM/Webhooks scheiden aus (Starter), `dm_tracking.csv` nicht mehr im Bericht. **Chrome 05.10.:** Pflichtfeld (Dropdown, Pflicht) ✓, Reclaim-Vorlagen weg ✓ (zweiter Link „Demo + Intro Call“ für @maehrtax bleibt, wird nicht gezählt), Apps-Script = GitHub-Stand, 1 Trigger stündlich :40, 0 % Fehler ✓. **Offen:** Testbuchung (loris_jm@gmx.de, Herkunft Instagram → Kopie prüfen → absagen) + Beschreibungsausschnitt an Claude; Puffer: global 10 Min. nach jedem Meeting (gilt auch für @maehrtax, entschieden 05.10.) – setzt Chrome zusammen mit der Testbuchung. ManyChat-Zahlen bleiben von Hand (API nur Pro) – siehe `strategie/13_backlog.md`.
- **Automatik gehärtet (03.10., mit #23 in `claude/instagram`):** kein Doppel-Post bei Push-Konflikt, „stop“ greift auch während des Wartens, kein Schlüssel in Fehlermeldungen, keine verlorenen „go“-Antworten, Schlüssel-Verlängerung mit Reserve-Takt – Details `strategie/13_backlog.md`.
- Externer Takt fürs Posten läuft (cron-job.org, alle 15 Min.). Schlüssel `cron-posten` läuft am **29.09.2027** ab → vorher erneuern.
- Tax-Calc-Repo: PR #2 (Delta-Plakette beim Tippen) und PR #3 (Reel-Datensatz `?demo=reel`) warten auf Review.
- **Chrome-Claude-Module** (`strategie/14_chrome_module.md`): Erinnerungen im Kalender „maehrsteuern Autopilot“ – So 04.10. 11:00 einmalig A·2·3, jeden So 18:45 Modul 1 (ManyChat → Wochenbericht), 1. Mo im Monat 18:00 Module 4+6, LinkedIn-Upload (Modul 5) automatisch je Karussell am Werktag danach 08:00.
- **Wochenbericht KW 40 ist da ([#29](https://github.com/maehrsteuern/Instagram-maehrsteuern/issues/29), So 18:01, Reserve-Lauf 21:26 hat dasselbe Issue nur aktualisiert):** Zahlen geprüft (575 Aufrufe = Zuwachs der 2 neuen Beiträge, Radar 2 Kommentare aus #22, Kalender verbunden – 0 Demos). **Offen: ManyChat-Zeile fehlt** (Chrome Modul 1 lief nicht) → im Issue `manychat x/y` + Zeile `Gesamtstand ManyChat: gesendet X / Klicks Y` kommentieren. Behoben (05.10.): Sonntags-Reels (19:30, nach dem Bericht) zählen jetzt im Bericht der Folgewoche als neu – „neu“ = gepostet So–Sa.
- **Radar-Nachträge (03.10.):** Meta-Drosselung (429/Code 4, 17, 32, 613) → Backoff 30/90/270 s, bei anhaltender Drosselung wird abgebrochen. Gedrosselte oder kurz gestörte Konten landen nicht mehr als 🧹 „nicht abrufbar“ in der Pflege; aufgeräumt werden nur dauerhaft kaputte Konten oder Konten ohne Beitrag seit 30 Tagen (montags, nur abgehakt). Art neuer Konten wird auch aus Wörtern wie „Steuerberaterin“, „Prüfung“, „Akademie“ erkannt; fehlende oder unbekannte Art erscheint als Hinweis im Radar-Issue.
- **Fristen** (`automatik/erinnerungen.json` → „Braucht dich“ + Kalender): LinkedIn #18 Mi 07.10. 08:00 (Termin kommt schon automatisch) · Reel-Vergleich „5 Dinge“/Split → Anzeigen-Start ca. Mo 12.10. (Chrome Modul 2 am 04.10. nur vorbereiten) · **ManyChat-Trial endet Fr 16.10.** → Entscheidung Loris (Erinnerung Mi 14.10.).
- **Meta-App „maehrsteuern Autopilot“** bleibt im Entwicklungsmodus. Die laufenden IG-Schlüssel und die Statistik sind davon nicht betroffen (eigenes Konto mit App-Rolle). Nur die Hashtag-Suche braucht die Freigabe → Checkliste [#26](https://github.com/maehrsteuern/Instagram-maehrsteuern/issues/26).
- **Reclaim-Hinweis:** Claudes Reclaim-Zugang (Connector) zeigt auf **Konto B (Outlook, Lite)**, nicht auf das Demo-Konto. Für die Automatik nicht nutzen; Demo-Buchungen kommen nur über das Apps-Script „maehrsteuern Demo-Kopie“.
- **Bibliothek aus dem Brand Kit (Claude Design) gebaut (02.10.):** 365 fertige Bilder in `assets/bibliothek/` (Übersicht `README.md` dort), Texte als Job-Dateien in `vorlagen/system/jobs/bibliothek/`. Neue Vorlagen `zahl.html` + `banner.html`, Highlight-Symbole, Vergleichstabelle/Checkliste im Karussell. Nichts davon ist eingeplant. **Gegengelesen (05.10.):** 10 Fehler korrigiert, 25 Zweifelsfälle mit Loris entschieden und umgesetzt → `assets/bibliothek/PRUEFBERICHT.md`. Offen nur: Zinsschranke-Caption mit Hinweis auf Untergang des Zinsvortrags. **Erste Bibliothek-Beiträge eingeplant (05.10., als Entwurf → Freigabe-Issue):** Rückstellung in 6 Schritten Do 15.10. (Quiz SolZ Mi 14.10., Auflösung Do 15.10. 12:15, Teaser 19:35) · E-Rechnung-Fahrplan Do 22.10. (Umfrage Mi 21.10., Teaser 19:35). Content-Fabrik: diese Slots sind belegt. **Runde 4 ergänzt (05.10.):** +217 Bilder (jetzt 582) – GmbH/Gesellschafter, Bilanz, USt, Lohn, ErbSt/GrESt, Paragraf als Formel, Steuerkalender, GoBD, Mythos/Glossar Teil 2, Einzelposts, Storys, Reel-Titel, Einblendungen, Highlights, Ampeln (`r4_*.json`), nichts eingeplant. 6 Korrekturen vor dem Rendern, 4 Zweifelsfälle + Platzhalter „312 Testfälle“ / § 8c-Quoten 48/62 % offen → Prüfbericht Abschnitt „Runde 4“. **Runde 7 (07.10.):** 14 MBS-Reel-Bilder (10 Titel `reels/mbs_*`, 4 Einblendungen `bausteine/mbs_*`, Abspann „Demo buchen“), `einblendung.html` kann jetzt `chip`/`kicker` im Abspann. **Runden 5+6 (07.10.):** +400 Bilder (jetzt 996) – Kleinunternehmer, Firmenwagen, Gebäude-AfA, USt-Sätze, Minijob/Reisekosten 2026, Grundwerte 2026, Kapitalerträge, Vermietung, AO-Fristen, OSS u. a. 10 Korrekturen, 32 Umbenennungen gegen Überschreiben, Zweifelsfälle → Prüfbericht „Runden 5 und 6“.
- **Lage als Seite (04.10.):** `LAGE.html` mit Kacheln, Kalender, Diagrammen und filterbarem Protokoll, wird mit LAGE.md neu geschrieben und über GitHub Pages veröffentlicht (https://maehrsteuern.github.io/Instagram-maehrsteuern/). Pages eingeschaltet ✓ (04.10.), Seite läuft und aktualisiert sich bei jeder neuen Lage automatisch.

## 👉 Braucht dich

- 🔴 **Verpasst** `08-story-rueckblick` (So 11.10. 12:15): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `13-reel-verknuepfung` (So 11.10. 19:30): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `03-story-quiz` (Mo 12.10. 12:45): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `14-reel-versionen` (Mo 12.10. 19:30): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `03-gewst-hinzurechnung` (Di 13.10. 12:15): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `03-story-teaser` (Di 13.10. 12:45): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `15-reel-rechnungsnummern` (Di 13.10. 19:30): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `09-story-quiz` (Mi 14.10. 12:45): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `07-reel-hinzurechnung` (Mi 14.10. 19:30): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `09-rueckstellung` (Do 15.10. 12:15): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `09-story-teaser` (Do 15.10. 12:45): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `04-story-frage` (Do 15.10. 18:00): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `16-reel-listen` (Do 15.10. 19:30): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `09-story-aufloesung` (Do 15.10. 19:35): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `03-story-aufloesung` (Fr 16.10. 12:45): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `04-reel-mein-weg` (Fr 16.10. 19:30): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `04-story-teaser` (Fr 16.10. 19:35): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `01-reel-ampel` (Sa 17.10. 19:30): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- 🔴 **Verpasst** `01-story-teaser` (Sa 17.10. 19:35): war freigegeben, ist aber nicht online gegangen – Zeit neu setzen oder von Hand posten
- ⏳ **Wartet auf sprachnachricht** `19-reel-verlustvortrag` (Di 20.10. 19:30) – Mindestbesteuerung § 10d Abs. 2 EStG/§ 8 KStG: VZ 2024–2027 70 % über 1 Mio. (ab 2028 wieder 60 %), GewSt § 10a GewStG 60 % – Text vom 08.10. (60 %) korrigiert. Sprechtext in posts/sprechtexte.md (≤ 15 s, Rechtsstand geprüft 11.10.). Loris spricht ein, Claude schneidet (12–15 s, Pointe in den ersten 5 s), danach freigegeben/Autopilot.
- ⏳ **Wartet auf sprachnachricht** `20-reel-erechnung` (Mi 21.10. 19:30) – Begleit-Reel zum Karussell E-Rechnung (Fr 23.10.). § 14 UStG, § 27 Abs. 38 UStG: Empfang ab 2025, Ausstellen ab 2027 (> 800.000 € Vorjahresumsatz), ab 2028 alle. Sprechtext in posts/sprechtexte.md (≤ 15 s, Rechtsstand geprüft 11.10.). Loris spricht ein, Claude schneidet (12–15 s, Pointe in den ersten 5 s), danach freigegeben/Autopilot.
- ⏳ **Wartet auf sprachnachricht** `21-reel-zinsschranke` (Do 22.10. 19:30) – § 4h EStG: 30 % des verrechenbaren EBITDA, Freigrenze Nettozinsaufwand < 3 Mio. €. Sprechtext in posts/sprechtexte.md (≤ 15 s, Rechtsstand geprüft 11.10.). Loris spricht ein, Claude schneidet (12–15 s, Pointe in den ersten 5 s), danach freigegeben/Autopilot.
- ⏳ **Wartet auf sprachnachricht** `17-reel-kommentare` (Sa 24.10. 19:30) – Thema aus den Kommentaren der Serie (wird nach Auswertung bis ca. 20.10. festgelegt). Reel-Takt alle 2 Tage (06.10.). Upload über Edits: Claude baut das Reel komplett fertig (mit Musik, Untertiteln) und schickt es im Chat, Loris lädt es über Edits hoch und plant/postet selbst – der Autopilot postet NICHT (Status nach dem Schnitt: manuell). Sprechtext in posts/sprechtexte.md.

## ⏭️ Nächste 7 Tage

| Wann | Was | Status | Hinweis |
|---|---|---|---|
| Di 20.10. 19:30 | 🎬 Reel `19-reel-verlustvortrag` | ⏳ wartet auf sprachnachricht | Mindestbesteuerung § 10d Abs. 2 EStG/§ 8 KStG: VZ 2024–2027 70 % über 1 Mio. (ab 2028 wieder 60 %), GewSt § 10a GewStG 60 % – Text vom 08.10. (60 %) korrigiert. Sprechtext in posts/sprechtexte.md (≤ 15 s, Rechtsstand geprüft 11.10.). Loris spricht ein, Claude schneidet (12–15 s, Pointe in den ersten 5 s), danach freigegeben/Autopilot. |
| Mi 21.10. 19:30 | 🎬 Reel `20-reel-erechnung` | ⏳ wartet auf sprachnachricht | Begleit-Reel zum Karussell E-Rechnung (Fr 23.10.). § 14 UStG, § 27 Abs. 38 UStG: Empfang ab 2025, Ausstellen ab 2027 (> 800.000 € Vorjahresumsatz), ab 2028 alle. Sprechtext in posts/sprechtexte.md (≤ 15 s, Rechtsstand geprüft 11.10.). Loris spricht ein, Claude schneidet (12–15 s, Pointe in den ersten 5 s), danach freigegeben/Autopilot. |
| Do 22.10. 12:45 | 📱 Story `10-story-umfrage` | 🟢 freigegeben (geht automatisch online) | 11.10.: Testmonat-Raster (Loris: Feed mittags 12:15, Storys 12:45) – Zeit verschoben. · Aus der Bibliothek: Umfrage E-Rechnung als Einstieg · [Freigabe #31](https://github.com/maehrsteuern/Instagram-maehrsteuern/issues/31) |
| Do 22.10. 19:30 | 🎬 Reel `21-reel-zinsschranke` | ⏳ wartet auf sprachnachricht | § 4h EStG: 30 % des verrechenbaren EBITDA, Freigrenze Nettozinsaufwand < 3 Mio. €. Sprechtext in posts/sprechtexte.md (≤ 15 s, Rechtsstand geprüft 11.10.). Loris spricht ein, Claude schneidet (12–15 s, Pointe in den ersten 5 s), danach freigegeben/Autopilot. |
| Fr 23.10. 19:30 | 🖼️ Karussell `10-e-rechnung` | 🟢 freigegeben (geht automatisch online) | Aus der Bibliothek (gegengelesen 05.10., Rechtsstand Okt. 2026: § 27 Abs. 38 UStG) · 06.10.: auf Fr 23.10. geschoben (Reel-Takt alle 2 Tage). · [Freigabe #31](https://github.com/maehrsteuern/Instagram-maehrsteuern/issues/31) |
| Fr 23.10. 19:35 | 📱 Story `10-story-teaser` | 🟢 freigegeben (geht automatisch online) |  · [Freigabe #31](https://github.com/maehrsteuern/Instagram-maehrsteuern/issues/31) |
| Sa 24.10. 19:30 | 🎬 Reel `17-reel-kommentare` | ⏳ wartet auf sprachnachricht | Thema aus den Kommentaren der Serie (wird nach Auswertung bis ca. 20.10. festgelegt). Reel-Takt alle 2 Tage (06.10.). Upload über Edits: Claude baut das Reel komplett fertig (mit Musik, Untertiteln) und schickt es im Chat, Loris lädt es über Edits hoch und plant/postet selbst – der Autopilot postet NICHT (Status nach dem Schnitt: manuell). Sprechtext in posts/sprechtexte.md. |

## ✅ Zuletzt veröffentlicht (Autopilot)

- Sa 10.10. 19:30 · 🎬 Reel `08-reel-kst-staffel` · [ansehen](https://www.instagram.com/reel/DeUn6ezCm7O/) (online 2026-10-10 19:30)
- Sa 10.10. 12:15 · 📱 Story `08-story-heute` · [ansehen](https://www.instagram.com/stories/maehrsteuern/4004782529098566867) (online 2026-10-10 12:15)
- Sa 10.10. 09:30 · 🎬 Reel `12-reel-zeile` · [ansehen](https://www.instagram.com/reel/DeTiK24NyJt/)
- Fr 09.10. 12:35 · 📱 Story `05-story-teaser` · [ansehen](https://www.instagram.com/stories/maehrsteuern/4004067818916764813) (online 2026-10-09 12:35)
- Fr 09.10. 12:30 · 🖼️ Karussell `05-latente-steuern` · [ansehen](https://www.instagram.com/p/DeRTLb4EYwd/) (online 2026-10-09 12:31)
- Do 08.10. 19:35 · 📱 Story `06-story-teaser` · [ansehen](https://www.instagram.com/stories/maehrsteuern/4003554454352185254) (online 2026-10-08 19:35)
- Do 08.10. 19:30 · 🎬 Reel `06-reel-split` · [ansehen](https://www.instagram.com/reel/DePeYymNG2K/)
- Mi 07.10. 19:35 · 📱 Story `02-story-teaser` · [ansehen](https://www.instagram.com/stories/maehrsteuern/4002829658245043420) (online 2026-10-07 19:35)
- Mi 07.10. 19:30 · 🖼️ Karussell `02-excel-fehler` · [ansehen](https://www.instagram.com/p/DeM5u1vGLsR/) (online 2026-10-07 19:32)
- Mi 07.10. 12:15 · 📱 Story `05-story-frage` · [ansehen](https://www.instagram.com/stories/maehrsteuern/4002608197877985940) (online 2026-10-07 12:15)

## 📈 Zahlen (täglich ca. 08:45)

**368 Follower** · 23 Beiträge im Profil (Abruf 2026-10-19) · **+7** seit 2026-10-11
Reichweite pro Tag: 16.10. **146** · 17.10. **214** · 18.10. **196** · 19.10. **1**

| Story (letzte 24 h) | Aufrufe | Erreicht | Antworten | Profilbesuche | Follows |
|---|---|---|---|---|---|
| So 18.10. 13:40 | 66 | 57 | 0 | 0 | 0 |
| So 18.10. 15:50 | 67 | 52 | 0 | 0 | 0 |
| So 18.10. 17:50 | 59 | 46 | 0 | 1 | 0 |

| Beitrag (letzte 14 Tage) | Aufrufe | Erreicht | Likes | Komm. | Gespeichert | Geteilt |
|---|---|---|---|---|---|---|
| So 18.10. 21:10 [Deine Steuererklärung liest im Finanzamt](https://www.instagram.com/reel/DepZflYMPE6/) | 110 | 102 | 2 | 1 | 2 | 0 |
| So 18.10. 17:45 [Organschaft Mindestlaufzeit: Der Gewinna](https://www.instagram.com/reel/Deo8TzBjns_/) | 46 | 31 | 4 | 0 | 4 | 0 |
| So 18.10. 13:39 [Kürzungen Gewerbesteuer nach § 9 GewStG:](https://www.instagram.com/p/DeomJhQG4o8/) | 145 | 66 | 4 | 0 | 4 | 0 |
| Sa 17.10. 18:59 [Plausibilitätsprüfung Jahresabschluss: V](https://www.instagram.com/reel/Deml8DcD_Dx/) | 60 | 49 | 5 | 0 | 4 | 0 |
| Sa 17.10. 12:34 [Steuerrückstellung zwei Tage vor Frist –](https://www.instagram.com/reel/Del54DNE7fz/) | 161 | 132 | 4 | 0 | 4 | 0 |
| Fr 16.10. 19:57 [Diplom-Finanzwirt mit KI-Avatar? Das war](https://www.instagram.com/reel/DekHzHkF7E2/) | 122 | 78 | 10 | 0 | 4 | 0 |
| Fr 16.10. 11:45 [GmbH-Gewinn ausschütten: Von 1 € kommen ](https://www.instagram.com/reel/DejLN1HiY0k/) | 99 | 81 | 4 | 0 | 4 | 0 |
| Do 15.10. 21:15 [Zwei Listen abgleichen in Excel: SVERWEI](https://www.instagram.com/reel/DehnTbyEZ2g/) | 266 | 219 | 6 | 0 | 5 | 0 |
| Do 15.10. 18:25 [Steuererklärung 2022 nachholen – nur noc](https://www.instagram.com/reel/DehYZkyD-sL/) | 253 | 163 | 8 | 0 | 4 | 0 |
| Do 15.10. 11:45 [Steuerrückstellung berechnen – kommst du](https://www.instagram.com/p/DegoIVKluPa/) | 138 | 69 | 1 | 0 | 1 | 0 |
| Mi 14.10. 17:45 [Gewerbesteuer-Hinzurechnung ohne Excel? ](https://www.instagram.com/reel/DeemwStk5mL/) | 249 | 197 | 6 | 0 | 3 | 0 |
| Di 13.10. 19:30 [Eine Rechnungsnummer doppelt. Der Prüfer](https://www.instagram.com/reel/DecWVZwgpOC/) | 296 | 230 | 5 | 2 | 5 | 1 |
| Di 13.10. 12:16 [Werden Mieten voll hinzugerechnet? 🤔](https://www.instagram.com/p/Debkp_3m1WY/) | 131 | 58 | 2 | 0 | 1 | 0 |
| Mo 12.10. 19:30 [final.xlsx · final_final.xlsx · final_fi](https://www.instagram.com/reel/DeZxf9AEy9p/) | 216 | 165 | 7 | 0 | 4 | 0 |
| So 11.10. 19:30 [#BEZUG! – zwei Tage vor Abgabe. Kennst d](https://www.instagram.com/reel/DeXMtEnDn3I/) | 293 | 225 | 8 | 0 | 6 | 1 |
| Sa 10.10. 19:30 [Latente Steuern: Ab 2028 ist ein fester ](https://www.instagram.com/reel/DeUn6ezCm7O/) | 285 (+86) | 221 | 14 | 8 | 7 | 18 |
| Sa 10.10. 09:23 [Jutta hat schon wieder eine Zeile eingef](https://www.instagram.com/reel/DeTiK24NyJt/) | 367 (+91) | 298 | 11 | 0 | 6 | 5 |
| Fr 09.10. 12:31 [Hör auf, 30 % fest einzutippen. 📉](https://www.instagram.com/p/DeRTLb4EYwd/) | 189 (+49) | 69 | 8 | 1 | 6 | 84 |
| Do 08.10. 19:30 [Gleiche Aufgabe, zwei Wege: Hebesatz von](https://www.instagram.com/reel/DePeYymNG2K/) | 314 (+17) | 238 | 8 | 0 | 8 | 25 |
| Mi 07.10. 19:32 [5 Excel-Fehler, die fast jede Steuerrück](https://www.instagram.com/p/DeM5u1vGLsR/) | 225 (+26) | 90 | 6 | 0 | 4 | 0 |
| Di 06.10. 19:30 [Zwei Stunden. Jeden Monat. Nur Copy-Past](https://www.instagram.com/reel/DeKUuvPgA1W/) | 407 (+21) | 306 | 11 | 2 | 10 | 8 |

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

**Mo 19.10.2026**
- 13:52 ✍️ Tagesbericht 19. Oktober: −8% Reichweite, 4/9 Methoden erfolgreich ([`c0930f6`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/c0930f61e0be6c3e0f780c868463410cc17cb4cb))
  - `automatik/berichte`
- 09:37 📈 Statistik 2026-10-19 ([`f4dba84`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/f4dba8488cde74320627a1b8f0261daf46d85ca4))
  - `automatik/statistik`
- 09:32 ✍️ Tagesbericht 18. Oktober: +45% Reichweite, 6/10 Methoden erfolgreich ([`b9e9b96`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/b9e9b961133350182f79aaa2b40ca8dc863b6684))
  - `automatik/berichte`

<details><summary>Älter als 7 Tage</summary>

**So 11.10.2026**
- 09:27 ✅ Freigabe angefragt (1 Beitrag/Beiträge) ([`07a2aec`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/07a2aec36a8a1ef298e471937f113aa249907473))
  - Plan: `23-story-biolink` → Freigabe-Issue #54
- 09:26 ✍️ Testmonat 2 pro Tag, Sprechtexte 18–22, Story-Formate, Auswertung 11.10. ([`1acbd03`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/1acbd030b10692c45c7a9ba058f72024eced1f92))
  - Plan: neu `23-story-biolink` (2026-10-13 19:35, entwurf); neu `22-reel-steuersatz` (2026-10-18 19:30, wartet_auf_sprachnachricht); neu `18-reel-aufbewahrung` (2026-10-19 19:30, wartet_auf_sprachnachricht); neu `19-reel-verlustvortrag` (2026-10-20 19:30, wartet_auf_sprachnachricht); neu `20-reel-erechnung` (2026-10-21 19:30, wartet_auf_sprachnachricht); neu `21-reel-zinsschranke` (2026-10-22 19:30, wartet_auf_sprachnachricht); `03-story-quiz` zeit: 2026-10-12 12:15 → 2026-10-12 12:45; `03-gewst-hinzurechnung` zeit: 2026-10-13 12:30 → 2026-10-13 12:15; `03-story-teaser` zeit: 2026-10-13 12:35 → 2026-10-13 12:45; `09-story-quiz` zeit: 2026-10-14 12:15 → 2026-10-14 12:45; `09-rueckstellung` zeit: 2026-10-15 12:30 → 2026-10-15 12:15; `09-story-teaser` zeit: 2026-10-15 12:35 → 2026-10-15 12:45; `09-story-aufloesung` zeit: 2026-10-15 12:15 → 2026-10-15 19:35; `03-story-aufloesung` zeit: 2026-10-16 12:15 → 2026-10-16 12:45; `10-story-umfrage` zeit: 2026-10-22 12:15 → 2026-10-22 12:45
- 09:19 ✍️ Reels 13–16 auf 12–15 s gekürzt (Pointe in den ersten 5 s) ([`ab29fc7`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/ab29fc72493fa83e4e4f965d6c23cd9d6a1da7a2))
  - Plan: `06-reel-split` status: manuell → veroeffentlicht; `06-reel-split` online: https://www.instagram.com/reel/DePeYymNG2K/
- 09:19 ✍️ Tagesbericht: Reel-Länge, Soll-Ist, Skip-Verlauf, Shares-Hinweis, 1620 px ([`9c2a71c`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/9c2a71c0e06cc283c105633c046f8e264d753f5d))
  - `automatik/berichte`, `automatik/insights_voll.py`, `automatik/tagesbericht.py`
- 08:48 📈 Statistik 2026-10-11 ([`dd8e4a6`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/dd8e4a65d1436f9e3b0bd75cc599956fe798b940))
  - `automatik/statistik`
- 07:04 📡 Radar 2026-10-11: 8 Beiträge, 0 DM-Entwürfe ([`ee909ef`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/ee909efeab6ddaf414905244f8d0806eab3e0b05))
  - `automatik/interaktion`

**Sa 10.10.2026**
- 19:30 🤖 Autopilot: 08-reel-kst-staffel veroeffentlicht ([`041fcea`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/041fceacb928f14ba8df2f9d570f34a8e2edc64c))
  - Plan: `08-reel-kst-staffel` status: freigegeben → veroeffentlicht; `08-reel-kst-staffel` online: https://www.instagram.com/reel/DeUn6ezCm7O/
- 18:15 🤖 Autopilot: Dateien fuer 08-reel-kst-staffel vorbereitet ([`bbd22ff`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/bbd22ff491314c97dec0ea9880c4e3bac0c461a8))
  - `posts/08_2026-10-09_reel_kst_staffel`
- 15:05 📈 Statistik 2026-10-10 ([`57d1b40`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/57d1b404960569c6724f844949ada2ac15ebffe5))
  - `automatik/statistik`
- 13:16 💼 LinkedIn-Pakete: 09-rueckstellung ([`10b1b91`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/10b1b91681b38af05562d6c99af8a85325d7c99e))
  - `posts/09_2026-10-15_rueckstellung`
- 13:15 📡 Radar 2026-10-10: 8 Beiträge, 0 DM-Entwürfe ([`ecdf71d`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/ecdf71d080677edf09128a606ebd01b3323139b5))
  - `automatik/interaktion`
- 12:15 🤖 Autopilot: 08-story-heute veroeffentlicht ([`b09078d`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/b09078d60f4514c2962e5a6ddedfb6400e3659b0))
  - Plan: `08-story-heute` status: freigegeben → veroeffentlicht; `08-story-heute` online: https://www.instagram.com/stories/maehrsteuern/4004782529098566867
- 11:46 🔀 Merge pull request #50 from maehrsteuern/claude/focused-shannon-hrtyy7 ([`fa67d29`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/fa67d290f19e81882a67906341bed9da92828103))
- 11:46 ✍️ Rückstellung-Karussell freigegeben, Ampel-Reel auf Sa 17.10., Link Test-Reel Nr. 2 ([`b4fc245`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/b4fc2454d57236226eb562bfb593be78620711b4))
  - Plan: `12-reel-zeile` online: https://www.instagram.com/reel/DeTiK24NyJt/; `09-story-quiz` status: entwurf → freigegeben; `09-story-aufloesung` status: entwurf → freigegeben; `09-rueckstellung` status: entwurf → freigegeben; `09-story-teaser` status: entwurf → freigegeben; `01-reel-ampel` status: pause → freigegeben; `01-reel-ampel` zeit: 2026-10-04 19:30 → 2026-10-17 19:30; `01-story-teaser` status: pause → freigegeben; `01-story-teaser` zeit: 2026-10-04 19:35 → 2026-10-17 19:35
- 11:01 🤖 Autopilot: Dateien fuer 08-story-heute vorbereitet ([`c6d602e`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/c6d602e6110a14075d724525a984fbb33a6e4053))
  - `posts/08_2026-10-09_reel_kst_staffel`
- 09:32 🔀 Merge pull request #49 from maehrsteuern/claude/focused-shannon-hrtyy7 ([`4ab6262`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/4ab6262832d5f81f384cee0ebf256e8d5713f65d))
- 09:32 ✍️ Reels wieder im Original-Takt und per Autopilot (ab Sa 10.10. Steuersatz) ([`2070594`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/2070594b5722f05e345dae6a175ac839d2590c13))
  - Plan: `12-reel-zeile` status: manuell → veroeffentlicht; `12-reel-zeile` zeit: 2026-10-10 19:30 → 2026-10-10 09:30; `08-story-heute` zeit: 2026-10-11 12:15 → 2026-10-10 12:15; `08-reel-kst-staffel` status: manuell → freigegeben; `08-reel-kst-staffel` zeit: 2026-10-11 19:30 → 2026-10-10 19:30; `08-story-rueckblick` zeit: 2026-10-12 18:00 → 2026-10-11 12:15; `13-reel-verknuepfung` status: manuell → freigegeben; `13-reel-verknuepfung` zeit: 2026-10-12 19:30 → 2026-10-11 19:30; `14-reel-versionen` status: manuell → freigegeben; `14-reel-versionen` zeit: 2026-10-13 19:30 → 2026-10-12 19:30; `15-reel-rechnungsnummern` status: manuell → freigegeben; `15-reel-rechnungsnummern` zeit: 2026-10-14 19:30 → 2026-10-13 19:30; `07-reel-hinzurechnung` zeit: 2026-10-15 19:30 → 2026-10-14 19:30; `04-story-frage` zeit: 2026-10-16 18:00 → 2026-10-15 18:00; `16-reel-listen` status: manuell → freigegeben; `16-reel-listen` zeit: 2026-10-16 19:30 → 2026-10-15 19:30; `04-reel-mein-weg` status: manuell → freigegeben; `04-reel-mein-weg` zeit: 2026-10-17 19:30 → 2026-10-16 19:30; `04-story-teaser` zeit: 2026-10-17 19:35 → 2026-10-16 19:35
- 09:19 🔀 Merge pull request #48 from maehrsteuern/claude/focused-shannon-hrtyy7 ([`5a6d081`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/5a6d08150d964aa7e6bb5e76b3eede7ec4bf49db))
- 09:19 🔀 Merge claude/instagram, Lage neu erzeugt ([`964450c`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/964450c11edb00b8b9c7c38f88299b3dc58d7545))
- 09:10 ✍️ Reel Nr. 2 neu geschnitten (300|Zeilen), heute 19:30 – alle Folge-Reels +1 Tag ([`0ea2834`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/0ea283465021259909da6e7e4b591b1f10eca388))
  - Plan: `12-reel-zeile` zeit: 2026-10-09 19:30 → 2026-10-10 19:30; `08-story-heute` zeit: 2026-10-10 12:15 → 2026-10-11 12:15; `08-reel-kst-staffel` zeit: 2026-10-10 19:30 → 2026-10-11 19:30; `08-story-rueckblick` zeit: 2026-10-11 12:15 → 2026-10-12 18:00; `13-reel-verknuepfung` zeit: 2026-10-11 19:30 → 2026-10-12 19:30; `14-reel-versionen` zeit: 2026-10-12 19:30 → 2026-10-13 19:30; `15-reel-rechnungsnummern` zeit: 2026-10-13 19:30 → 2026-10-14 19:30; `07-reel-hinzurechnung` zeit: 2026-10-14 19:30 → 2026-10-15 19:30; `04-story-frage` zeit: 2026-10-15 18:00 → 2026-10-16 18:00; `16-reel-listen` zeit: 2026-10-15 19:30 → 2026-10-16 19:30; `04-reel-mein-weg` zeit: 2026-10-16 19:30 → 2026-10-17 19:30; `04-story-teaser` zeit: 2026-10-16 19:35 → 2026-10-17 19:35
- 08:49 📈 Statistik 2026-10-10 ([`5fd657b`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/5fd657b3c7b3798ffd911c6e243dc193a231de35))
  - `automatik/statistik`
- 07:04 📡 Radar 2026-10-10: 8 Beiträge, 0 DM-Entwürfe ([`f626328`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/f626328688858f48feed9c8023210206cf3929a6))
  - `automatik/interaktion`

**Fr 09.10.2026**
- 15:47 📈 Statistik 2026-10-09 ([`79346c6`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/79346c66cf32cc4fb3a54b81827749e3e7b01bbe))
  - `automatik/statistik`
- 13:56 📡 Radar 2026-10-09: 8 Beiträge, 0 DM-Entwürfe ([`6837bf4`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/6837bf4cc8cc9607c1938351b4a04f397df157cf))
  - `automatik/interaktion`
- 12:35 🤖 Autopilot: 05-story-teaser veroeffentlicht ([`ff09f34`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/ff09f3462a5439fd1a77b18400d1e643ba27b88f))
  - Plan: `05-story-teaser` status: freigegeben → veroeffentlicht; `05-story-teaser` online: https://www.instagram.com/stories/maehrsteuern/4004067818916764813
- 12:32 🤖 Autopilot: Dateien fuer 05-story-teaser vorbereitet ([`606887a`](https://github.com/maehrsteuern/Instagram-maehrsteuern/commit/606887a622f73b7997e3b21789fe055ca873777f))
  - `posts/05_2026-10-08_latente_steuern`

</details>
