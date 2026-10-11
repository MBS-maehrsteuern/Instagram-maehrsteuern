# 15 · Testmonat: 2 Beiträge pro Tag (Mo 12.10. – So 08.11.2026)

Stand 11.10.2026. Grundlage: Auswertung in `06_auswertung.md` (Abschnitt „Stand 11.10.“) und Loris' Entscheidungen vom 11.10.

## Warum
- **Reels bringen die Reichweite:** 90 % Nicht-Follower (30 Tage). Der Tag ohne Reel (Fr 09.10.) erreichte **66** Konten,
  der Tag mit zwei Reels (Sa 10.10.) **362**.
- **Karussells werden geteilt und gespeichert** (Neuvorstellung 17×, latente Steuern 84× geteilt; 2,9 % gespeichert),
  erreichen aber nur 54–135 Konten.
- Bisher lief fast alles um 19:30. Ob 12:15 genauso gut oder besser ist, wissen wir nicht.

## Raster (pro Woche 14 Feed-Beiträge: ~10 Reels, 4 Karussells)
Feed **12:15** und **19:30**, Storys **12:45** (Frage zum Tippen / Teaser zum Mittagsbeitrag) und **19:35** (Teaser).
Täglich mindestens ein Reel.

| Tag | 12:15 | 19:30 |
|---|---|---|
| Mo | Reel · ohne Stimme · Hook *fall* | Reel · Stimme · Hook *zahl* |
| Di | Karussell | Reel · **Begleit-Reel** zum Karussell |
| Mi | Reel · ohne Stimme | Reel · Stimme |
| Do | Karussell | Reel · Einzel-Reel |
| Fr | Reel · Hook *zahl* | Karussell |
| Sa | Reel · Stimme | Reel · ohne Stimme |
| So | Karussell | Reel · Hook *fall* |

**Wochen wechseln:** In geraden Wochen (KW 42, 44) wie oben (Karussells 3× mittags, 1× abends), in ungeraden (KW 43, 45)
Karussell und Reel am Di/Do/So tauschen (Karussells 3× abends). So hat jede Zelle Format × Slot nach 4 Wochen n ≥ 3.

Reel-Regeln (`09_reel_regeln.md`): **12–15 s**, Pointe in den ersten 5 s, Hook-Text ab 0,3 s, höchstens 3 Punkte.
Karussells: letzte Folie „Speichern für später“ + Weiterleiten-Frage („Wer in deinem Team braucht das?“).
Pro Woche mindestens **1 Beitrag mit klarem Aufruf** („Schreib TOOL in die Kommentare“).

## Testfaktoren (im Plan je Beitrag)
| Faktor | Feld in `plan.json` | Werte |
|---|---|---|
| Format | `typ` | reel · karussell |
| Slot | `zeit` | 12:15 · 19:30 |
| Stimme | `stimme` | true · false |
| Hook-Art | `hook` | fall · zahl (Prüfer zählt als *fall*) |
| Begleit- vs. Einzel-Reel | `begleit` | true · false (nur Reels) |

## Bewertung
- Jeder Beitrag nach **48 h** (frühe Werte wandern noch, siehe Skip-Drift in `06_auswertung.md`).
- Zellen erst ab **n ≥ 3** beurteilen (Tagesbericht, Tabelle „Testmonat“).
- Kennzahlen: Ø Erreicht, Nicht-Follower-Anteil (nur Konto, je Beitrag liefert die API ihn nicht), Gespeichert ÷ Erreicht,
  Geteilt ÷ Erreicht (ohne Geteilt > Erreicht), Median-Skip und Ø gesehen bei Reels, Follows ÷ Profilbesuche bei Karussells.
- **Zwischenstand Mo 26.10.** (Tagesbericht + kurze Notiz hier), **Entscheidung Mo 09.11.** (bleibt es bei 2 pro Tag, welcher Slot, welches Format?).

## Zusammengeführt mit dem bestehenden Plan (Stand 11.10.)
Der Plan wurde vorher an anderer Stelle umgebaut (Reels meist 19:30, Karussells 12:30). Zusammengeführt, nichts überschrieben:

| Woche 42 | 12:15 | 19:30 |
|---|---|---|
| Mo 12.10. | *frei → Fabrik* | 14 Nr. 3 final_final_v3 (Reel, Stimme, fall) |
| Di 13.10. | 03 GewSt-Hinzurechnung (Karussell, 12:30 → 12:15) | 15 Nr. 4 Rechnungsnummern (Reel, Stimme, fall) |
| Mi 14.10. | *frei → Fabrik* | 07 Hinzurechnung (Begleit-Reel, ohne Stimme) |
| Do 15.10. | 09 Rückstellung (Karussell, 12:30 → 12:15) | 16 Nr. 5 Listen (Reel, Stimme) |
| Fr 16.10. | *frei → Fabrik* | 04 Mein Weg (Reel, Stimme, KI-Label von Hand) |
| Sa 17.10. | *frei → Fabrik* | 01 Ampel (Reel, Stimme) |
| So 18.10. | *frei → Fabrik* | 22 Steuersatz (Reel, Stimme, **CTA TOOL**) – wartet auf Sprachnachricht |

| Woche 43 | 12:15 | 19:30 |
|---|---|---|
| Mo 19.10. | *frei* | 18 Aufbewahrung – wartet auf Sprachnachricht |
| Di 20.10. | *frei* | 19 Verlustvortrag – wartet auf Sprachnachricht |
| Mi 21.10. | *frei* | 20 E-Rechnung (Begleit-Reel) – wartet auf Sprachnachricht |
| Do 22.10. | *frei* | 21 Zinsschranke – wartet auf Sprachnachricht |
| Fr 23.10. | *frei* | 10 E-Rechnung (Karussell) |
| Sa 24.10. | *frei* | 17 Thema aus den Kommentaren – wartet auf Sprachnachricht |

Storys: alle Mittags-Storys von 12:15 auf **12:45** (Quiz, Auflösungen, Umfrage, Teaser); 09-Auflösung auf Do 19:35.

### Konflikte – Loris entscheidet
1. **Woche 42 ist reel-lastig abends, mittags leer.** Die Fabrik (Mo/Mi/Fr) füllt ab Mo 12.10. die Mittags-Slots ab übermorgen.
   Mo 12.10. 12:15 bleibt deshalb wahrscheinlich leer (zu kurzfristig) – ok so?
2. **Alle Stimm-Reels liegen auf 19:30.** Für den Slot-Test „Stimme mittags“ müssten 1–2 davon auf 12:15 (z. B. Ampel Sa 17.10. 12:15). Vorschlag, nicht umgesetzt.
3. **Themen-Dopplung:** 22 Steuersatz (So 18.10.) wiederholt das KSt-Staffel-Reel vom 10.10. Vorschlag: auf KW 44 schieben und dafür
   ein anderes CTA-Reel vorziehen – oder bewusst als „Teil 2 mit TOOL-Aufruf“ laufen lassen.
4. **Wartet-auf-Sprachnachricht-Slots 18.–24.10.:** Ohne Aufnahme bis Mi 14.10. bleiben fünf Abend-Slots leer. Notlösung: Fabrik baut
   dort Reels ohne Stimme (dann Faktor Stimme = false).

## Content-Fabrik (3.3a)
- Läuft seit 08.10. **Mo, Mi, Fr 08:47** (3 Läufe), bis zu **6 Feed-Beiträge pro Lauf** → 18 Plätze für 14 Beiträge.
- Neuer Prompt liegt in `automatik/routinen/content_fabrik.md` (Raster dieser Datei, 12–15 s, Hook-Kürzel, Commit-Regel, ausdrückliche Commit-Erlaubnis).
  Übernehmen geht nur aus dem Chat der Routine (siehe `13_backlog.md`).
- **Sammel-Freigabe:** ein Issue pro Woche (Montag 19:00) statt je Beitrag – Vorschlag im Backlog, Workflow `freigabe.py` noch nicht umgebaut.
