# 16 · Nachtlauf 14.10.2026 – Instagram-Optimierungen

Auftrag Loris (13.10., 23:10): Über Insights, LAGE.md und Lage-Skill alle Optimierungen suchen, automatisch einbauen,
freigeben, morgens berichten. Gearbeitet mit 5 Analyse-, 13 Bau-, 3 Prüf- und 5 Umsetzungs-Agenten; jede Änderung
einzeln committet (Protokoll in LAGE.md).

## Auf einen Blick
- **Plan bis zum Testmonat-Ende voll:** 37 neue Feed-Beiträge (28 Reels, 9 Karussells) + 37 Storys, alle
  `freigegeben`, aus der gegengelesenen Bibliothek, ohne Stimme. Stand Testmonat: KW 42 12/14 · KW 43 9/14 (+5 Notlösung
  → 14/14) · KW 44 12/14 (+1 Notlösung) · KW 45 13/14 · jeden Tag ≥ 1 Reel. Frei bleiben nur Stimm-Slots (Sa mittags).
- **Dreimal unabhängig geprüft** (je Zeitraum: 14.–26.10., KW 44, KW 45; fachlich an Primärquellen + Regeln + Technik). Gefunden und behoben: 5 Fachfehler/-ungenauigkeiten,
  1 Arbeitgeber-Ortsbezug, 1 Platzhalter-Story, Hashtag-Fallen, Überlappungen.
- **Autopilot sicherer:** kein Doppel-Post mehr bei Push-Konflikt, Teaser nur wenn der Beitrag online ist, Wächter
  meldet ausgefallenen Takt (cron-job.org), Container vor dem Warten → pünktlicher.
- **Statistik/Lage besser:** Zeitzonen-Fehler ab 25.10. behoben, keine Doppelläufe, neue Kennzahlen (Ø Sehdauer in s,
  Reichweite nach 24 h, Follows/Entfolgungen, Wochenziele mit Ampel), LAGE mit 30-Sekunden-Briefing.

**Morgen-Check 14.10. 06:50:** alles gepusht, Automatik ✅ (alle Abläufe ok), heute online: 12:15 Quiz-Story Rückstellung, 17:45 Hinzurechnungs-Reel (neues Titelbild, neuer Text).

## 1 · Was die Daten sagen (Insights 30.09.–13.10.)
| Erkenntnis | Beleg | Konsequenz (eingebaut) |
|---|---|---|
| Reichweite steht nach ~13 h zu 80–90 % fest | 5 Reels, 79–93 % des Endwerts am 1. Morgen | Reichweite nach 24 h werten (09_reel_regeln, Tagesbericht-Spalte) |
| Kürzere Reels (13–15 s) heben „gesehen %“, nicht die Sekunden | Ø 4,8 s vs. 8,5 s bei 30–41 s, Skip gleich | Regel 12–20 s, Ziel Ø Sehdauer ≥ 6 s (neue Kennzahl) |
| Hook „Zahl/These“ wird ~4× öfter geteilt als „Fall/Ich-Geschichte“ | 5,1 % vs. 0,8 % geteilt ÷ erreicht (n 4/3) | Fall-Reels bekommen These + Teilen-Aufruf (08_hooks) |
| Kommentare kommen nur auf Auswahlfragen | 10 und 8 Kommentare vs. 0–2 bei offenen Fragen | Überall Auswahlfrage (A oder B?) |
| Serien-Folgen verlieren (298 → 141 erreicht) | 91 % Nicht-Follower kennen „Nummer X“ nicht | Folgen müssen allein funktionieren |
| Karussells: viel Speichern, wenig Reichweite | 4,9–9,8 % gespeichert, 61–146 erreicht | Schlussfolie Speichern + „Wer in deinem Team braucht das?“ |
| Storys: 8–16 % der Follower, 0 Antworten auf offene Fragen | 25 Storys seit 03.10. | Nur Tipp-Storys (👏/😮), Quiz, Teaser |
| Follower am aktivsten 18–21 Uhr | App + API (17:45 = 92–95 % der Spitze) | Zeiten 11:45/17:45 bleiben im Testmonat; ab 09.11. 19:30 dagegen testen (Vorschlag) |
| Nur 2 von 7 Reels mit TOOL-Aufruf, Bio-Link-Metrik zählt nur Kontakt-Buttons | 2 Demos KW 41 trotz „0 Klicks“ | „💬 Kommentiere „TOOL““ als 2. Absatz jeder Bildunterschrift + im Abspann; Messung umbenannt, website_clicks abgefragt |
| Wachstum +7–10/Woche, 8–13 Entfolgungen/Monat, Folgt-Zahl 253 → 292 | konto.csv | Wochenziele (≥ +15 netto), Folgt-Zahl < 200 (braucht dich) |

## 2 · Eingebaut und freigegeben
**Anstehende Beiträge überarbeitet** (01 Ampel, 07 Hinzurechnung, 16 Listen, 04 Mein Weg, 09 Rückstellung, 10 E-Rechnung):
Bildunterschriften neu (Suchbegriff in Zeile 1, Kommentiere TOOL, Auswahlfrage, genau 4 Hashtags, keine #-Fallen im
Text), Titelbilder Ampel + Hinzurechnung, Alt-Texte für Karussells (Datei `alt_texte.json`, posten.py setzt sie noch nicht).

**Fachkorrekturen:** Rückstellung Folie 5 (Vorauszahlungen je Steuer, kein Saldieren über Steuerarten) · E-Rechnung-Text
(Papier in der Übergangszeit ohne Zustimmung) · Zinsschranke (verrechenbares EBITDA = 30 % des steuerlichen; § 8a Abs. 1
S. 3 KStG) · Organschaft (Aufhebung aus wichtigem Grund) · Säumniszuschlag-Formulierung · Betriebsprüfung nach neuer
**Außenprüfungsordnung (ersetzt BpO 2000 seit 10.09.2026)** · § 35 EStG als Ermäßigung statt „zurück“.
KW 45: Fahrtenbuch mit Arbeitnehmer-Normen (§ 8 Abs. 2 S. 2–4 EStG, BMF 03.03.2022) · InvStG „mehr als 50 %“ · § 171 AO als Ablaufhemmung · § 8c Abs. 1 Sätze 4–8 · § 34a-Satz sinkt ab 2028 ergänzt.
Geprüft und **nicht** geändert: Verlustrücktrag-Folie ist richtig (10 Mio. € nur 2022/2023, seit 2024 1 Mio. €).

**Arbeitgeber-Bezug entfernt:** Im Ampel-Reel stand in der Programm-Aufnahme ein Hebesatz-Hinweis mit Stadtname (~10–12 s)
→ überdeckt, Stammdaten-Seite herausgeschnitten.

**Neue Beiträge 16.10.–08.11.** (je mit Tipp-/Quiz-Story oder Teaser): 1 € Gewinn → 52 Cent · Plausi-Checks · Kürzungen
§ 9 GewStG · Organschaft 5 Zeitjahre · Säumniszuschlag · Verluste 70 % · GWG · Zinsschranke · Mindeststeuer · Paragraf als
Formel · Einspruch · Steuerkalender · Bewirtung · Betriebsprüfung · Prüfpfad · Holding · WENNFEHLER · 6 Irrtümer ·
Degressive AfA · § 35 EStG · Glossar · vGA · Dividenden § 8b · Betriebsaufspaltung · Fahrtenbuch · Kleinunternehmer
(CTA-Reel KW 45) · Gebäude-AfA · Kapitalerträge · GoBD · IAB (Reel + Karussell) · Reverse-Charge · § 34a · Verjährung ·
§ 8c · Vorsteuer · Pensionsrückstellung (mit Community-Frage zum Testmonat-Ende).

**Notlösung Stimm-Reels 18–22:** Fassungen ohne Stimme liegen als `ersatz_video` bereit. Do 15.10. 12:05 prüft Claude
automatisch, ob Aufnahmen da sind, und stellt sonst um (video → Ersatz, stimme false, freigegeben).

## 3 · Automatik
- `posten.py`: Status-Sicherung ohne Rebase-Konflikt (8 Versuche), „schon online?“-Abgleich vor jedem Feed-Post, Teaser
  warten auf ihren Feed-Beitrag, Fehler beim Vorbereiten trifft nur den einen Eintrag, Container vor dem Warten.
  14 Unit-Tests (`automatik/tests/test_posten.py`).
- `waechter.py`: 🔴 wenn der externe Posten-Takt > 40 Min. steht.
- `radar.py` (14.10. früh, Loris' Hinweis): derselbe Beitrag erscheint nur noch einmal (nach ID + Textanfang).
- Statistik/Radar: Reserve-Läufe überschreiben den Morgenstand nicht mehr; Radar schließt das Morgen-Issue nicht.
- `tagesbericht.py`: Pacific→Berlin je Datum (Zeitumstellung 25.10./01.11.), neue Kennzahlen; `wochenbericht.py`:
  Kennzahlen + Ziele + Ampel.
- LAGE.md/LAGE.html: 30-Sekunden-Briefing (heute, überfällig, 7 Tage, Testmonat je KW, freie Slots).
- Routine-Prompts (Content-Fabrik, Tagesbericht) neu geschrieben – **übernehmen musst du im Chat der Routine**.

## 4 · Braucht dich (nach Dringlichkeit)
1. **Heute Mi 14.10.:** ManyChat-Entscheidung (Trial endet Fr 16.10.). Empfehlung: bis 08.11. behalten – alle neuen
   Beiträge rufen zu „Kommentiere TOOL“ auf; ohne ManyChat musst du diese Kommentare selbst beantworten.
2. **Bis Do 15.10. 12:00:** Sprachnachrichten 18–22 (sonst laufen die Fassungen ohne Stimme).
3. **Fr 16.10. 17:45 / Sa 17.10. 11:45:** KI-Label in der App bei „Mein Weg“ und beim Ampel-Reel (geht nicht per API).
4. **Profil in der App:** Bio, Namensfeld, Pins, Highlights „Start 👋“/„Demo ⚙️“ – fertige Texte in `02_bio_highlights.md`.
5. **Routinen:** Repo als Quelle bei Tagesbericht + Content-Fabrik, neue Prompts aus `automatik/routinen/` einfügen.
6. **Radar:** 5 Kommentare/Werktag, 10 Konten aus Steuerabteilungen ergänzen; Folgt-Liste ausdünnen (292 → < 200).
7. **Wissen solltest du:** Ältere Reels (Split, KSt) zeigen in der Programm-Aufnahme evtl. denselben Ortsnamen – sind schon
   online; die Original-Aufnahme liegt weiter im (öffentlichen) Repo bzw. in der Git-Historie.

## 5 · Bewusst nicht gemacht
- Bibliothek-Vorlage `jobs/bibliothek/r4_06_par8c.json` nennt noch „§ 8c Abs. 1 Sätze 4–9“ (richtig 4–8) – im Beitrag 57 korrigiert, Bibliothek selbst unverändert.
- Postzeit 17:45 nicht geändert (deine Entscheidung; Daten zeigen 19:30 minimal höher → Test ab 09.11. vorgeschlagen).
- Keine Stimm-Reels erfunden, keine Inhalte aus nicht gegengelesenen Bibliothek-Teilen (mbs_*, Platzhalter).
- Keine Routine-Prompts per API getauscht, kein Modellwechsel.
