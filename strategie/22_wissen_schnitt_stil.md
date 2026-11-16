# Neuer Reel-Schnitt-Stil (Loris, 16.11.2026) – gilt ab sofort für alle neuen Reels

Vorbild: Bildschirmaufnahme eines englischen „Editor-Timeline“-Reels (Drive, 16.11.). Übertragen auf maehrsteuern, deutsch, Markenfarben.

1. **Sekunde 0–2: echtes Gesicht** (Foto aus `assets/marke/` oder Video), mit Badge „EX-FINANZAMT · DIPLOM-FINANZWIRT“ und Kernsatz – für Vertrauen. Kein KI-Gesicht.
2. **Untertitel oben**, 1–3 Wörter je Einblendung, wortgenau zur Stimme: aktuelles Wort weiß/fett, gesprochene grau, **Schlüsselwörter mit grünem Markier-Rahmen** (mit Anfasser-Punkten).
3. **Kein Standbild:** Bühne in 3D ständig in Bewegung (Neigen, Drehen, Zoom), bei jedem Szenenwechsel kurzer Zoom-Stoß mit Unschärfe. Keine harten Schnitte.
4. **Roter Faden = das Steuer-Dokument selbst** (bei Werbungskosten: **Anlage N**). Es wird im Hintergrund befüllt, die Kamera fährt in 3D zur gerade besprochenen Zeile (Zoom, Neigen, kurze Bewegungsunschärfe), Feld tippt den Wert ein, Haken wird gesetzt. **Keine Schallwelle, keine Wort-Spur, kein Editor-Look** (Loris 16.11.: passt nicht zu Steuern, zu viel).
5. **Zahlen zählen direkt im Formularfeld hoch** (z. B. 6 € / Tag → 1.260 €).
6. **CTA am Ende:** „Kommentiere STICHWORT“ – Kommentarfeld tippt das Wort, DM-Blase von maehrsteuern erscheint. Stichwort muss in `automatik/interaktion.json` → `stichwort_antworten` stehen (kommentare.py schickt die DM automatisch, kein ManyChat mehr seit 29.10.).
7. Stimme bleibt Pflicht (Loris' Aufnahme), Wortzeiten aus `aufnahmen/*/woerter.json`.

Baukasten: `vorlagen/system/premium/insider_05_anlage_n.html` (+ `insider_05_daten.js` für die Wortzeiten) → `reel_bauen.py <name> <post> <dauer> <musik>`.
Erstes Reel: i05 „Finanzbeamte setzen das selbst ab“ (16.11.).

Stichwort ABZUG (i05) ist in `automatik/interaktion.json` angelegt.
8. Nur Aufnahmen, die zum Thema passen – keine eingeschobenen Fremd-Sätze (i05: Einschub „Ich war selbst jahrelang im Finanzamt“ entfernt, Loris 16.11.). Original: `ton/stimme_mit_einschub.wav`.
