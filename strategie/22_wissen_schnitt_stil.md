# Neuer Reel-Schnitt-Stil (Loris, 16.11.2026) – gilt ab sofort für alle neuen Reels

Vorbild: Bildschirmaufnahme eines englischen „Editor-Timeline“-Reels (Drive, 16.11.). Übertragen auf maehrsteuern, deutsch, Markenfarben.

1. **Sekunde 0–2: echtes Gesicht** (Foto aus `assets/marke/` oder Video), mit Badge „EX-FINANZAMT · DIPLOM-FINANZWIRT“ und Kernsatz – für Vertrauen. Kein KI-Gesicht.
2. **Untertitel oben im Gerba-Look:** max. 2 Wörter, GROSS, kursiv, weiß mit hartem Schatten, Akzentwort grün, jedes Wort knallt rein (Skalierung).
3. **Kamera im Gerba-Stil** (Loris 16.11., Vorbild Bau-Reels @gerba.unternehmensgruppe): Kamera fliegt wie eine Drohne über das Dokument – **Crash-Zooms** mit radialer Unschärfe, **Reißschwenks** mit Bewegungsunschärfe zwischen den Punkten, **schiefe Winkel** (Dutch Angle), Drohnen-Drehung im Überblick, **Speed-Ramps** (schnell rein, langsam weiterdriften), kleine Stöße auf betonten Wörtern. Unschärfe kommt nachträglich per `effekte.py` (`<vorlage>_effekte.json`).
4. **Roter Faden = das Steuer-Dokument selbst** (bei Werbungskosten: **Anlage N**), **fast ohne Wörter**: nur kurze Zeilentitel, sonst Linien. Felder füllen sich, Rahmen und Haken zeichnen sich (Lineouts). **Keine Schallwelle, keine Wort-Spur, kein Editor-Look.**
5. **Titel + Zahl zählen groß am Rand hoch** (unten links, mit Umriss-Echo), z. B. HOMEOFFICE 0 € → 6 € → 1.260 €; rechts ein mitlaufendes Lineal.
6. **CTA am Ende:** „Kommentiere STICHWORT“ – Kommentarfeld tippt das Wort, DM-Blase von maehrsteuern erscheint. Stichwort muss in `automatik/interaktion.json` → `stichwort_antworten` stehen (kommentare.py schickt die DM automatisch, kein ManyChat mehr seit 29.10.).
7. Stimme bleibt Pflicht (Loris' Aufnahme), Wortzeiten aus `aufnahmen/*/woerter.json`.

Baukasten: `vorlagen/system/premium/insider_05_gerba.html` + `insider_05_gerba_effekte.json` (+ `insider_05_daten.js` für die Wortzeiten) → `reel_bauen.py <name> <post> <dauer> <musik>`.
Erstes Reel: i05 „Finanzbeamte setzen das selbst ab“ (16.11.).

Stichwort ABZUG (i05) ist in `automatik/interaktion.json` angelegt.
8. Nur Aufnahmen, die zum Thema passen – keine eingeschobenen Fremd-Sätze (i05: Einschub „Ich war selbst jahrelang im Finanzamt“ entfernt, Loris 16.11.). Original: `ton/stimme_mit_einschub.wav`.

## Offen: neuer Hook (Loris spricht ein)
„Was ist genauso geil wie die Videos von Gerba? Steuern sparen wie ein Diplom-Finanzwirt.“ – kommt als Hook vor das Reel, sobald die Aufnahme in `aufnahmen/` liegt.
