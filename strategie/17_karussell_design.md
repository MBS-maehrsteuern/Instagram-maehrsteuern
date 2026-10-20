# 17 · Karussell-Design – Do's & Don'ts (Stand 20.10.2026)

Quelle: Instagram-Karussell von @fizzaandalgorithm (Screenshots von Loris, Folien 2–6 von 6, Folie 1 lag nicht vor; Kernsatz:
„Dein Karussell braucht nicht mehr Information, sondern bessere Design-Entscheidungen“). Übernommen ist, was zu
@maehrsteuern passt. Gilt für die Content-Fabrik zusätzlich zu `08_hooks.md`, `09_reel_regeln.md` und
`11_wissen_instagram.md`. Bei Widerspruch gewinnen unsere eigenen Regeln und Zahlen aus `06_auswertung.md`.

## 1. Leseführung (Z-Muster)
- ❌ Überschrift, Text und Zwischenüberschrift ohne erkennbare Reihenfolge.
- ✅ Westliche Leser lesen in einem festen Muster: oben links → rechts → diagonal nach links unten → rechts unten.
  Auf jeder Folie eine klare Hierarchie: **große Überschrift → Zwischenzeile → kleiner Text**.
- Das Wichtigste dahin, wo der Blick zuerst landet (oben). Pro Folie eine Aussage.
- Passt zu `vorlagen/system/karussell.html` (Kicker, Serif-Überschrift, Text); beim Bauen darauf achten, dass die
  Überschrift die Folie führt und nie kleiner wirkt als der Fließtext.

## 2. Format und Sicherheitsrand
- Quelle nennt als **neues Format 1080 × 1440 px (3:4)**; alt: 1080×1080 und 1080×1350. Sicherheitsrand laut Quelle
  **ca. 50 px links/rechts, ca. 180 px oben/unten**. Bei **Anzeigen (Boosting) 1080 × 1350** nehmen.
- ⚠️ **Offene Entscheidung Loris:** Unsere Vorlage `karussell.html` und alle bisherigen Karussells sind **1080×1350 (4:5)**.
  Die Angabe der Quelle ist hier nicht gegengeprüft. Bis Loris entscheidet, bleibt 1350 – und Text/Logo trotzdem
  innerhalb der Ränder (≥ 50 px seitlich, ≥ 180 px oben/unten), damit ein späterer Wechsel auf 3:4 nichts abschneidet.
  Beim Umstellen: Vorlage + Job-Dateien neu rendern, alte Beiträge nicht anfassen.

## 3. Farben und Lesbarkeit
- ❌ Palette mit zu wenig Kontrast – auf kleinen oder gedimmten Displays nicht lesbar.
- ✅ Gut lesbare, markante Farben; Kontrast prüfen (Beispiel der Quelle: #191919 auf #4BC2EA = 8,54, „sehr gut“).
- Unsere Marke (gemessen, WCAG-Kontrast): Text `#EAF1EC` auf `#0B110E` **16,6** · Akzent `#53C3A2` auf `#0B110E` **8,8**
  · Nebentext `#8FA398` auf `#0B110E` **7,1**, aber nur **4,7** am hellen Ende des Verlaufs (`#153A31`) und
  Akzent dort **5,8**.
- Regel: **Kleiner Text (< ca. 28 px) nie in `#8FA398` auf den hellsten Teil des Verlaufs setzen**; dort `#EAF1EC` nehmen.
  Mindestkontrast 4,5 für Text, 3 für große Überschriften. Vor dem Freigeben das Bild auf dem Handy bei niedriger
  Helligkeit ansehen.

## 4. Framework für 10 Folien
| Folie | ❌ Don't | ✅ Do |
|---|---|---|
| 1 | langweiliger Hook | **Scrollen stoppen**, Leser reinholen |
| 2–3 | kein Grund zum Wischen | **Interesse aufbauen mit einem Beispiel** (bei uns: ein konkreter Fall oder eine Zahl mit Norm) |
| 4–5 | verkaufen, bevor Wert geliefert ist | **Aufmerksamkeit halten mit Diagrammen**/Tabelle/Rechenweg |
| 6–9 | zufällige Infos | **praktische, anwendbare Informationen** (Schritte, Checkliste, Prüfpunkte) |
| 10 | schon wieder ein Verkaufs-Pitch | **ein einfacher CTA** (bei uns: „Speichern für später“ + Weiterleiten-Frage; daneben `TOOL`) |

Merksatz: **Erst Wert liefern, dann einladen.** Passt zu `11_wissen_instagram.md` (Karussell = Vertrauen und Anfragen)
und zu „Folie 2 muss allein als Einstieg funktionieren“ (zweite Chance im Feed). Kürzere Karussells dürfen das Raster
straffen (z. B. 7 Folien: 1 Hook · 2–3 Beispiel · 4 Diagramm · 5–6 Praxis · 7 CTA); die **Reihenfolge** bleibt.

## 5. Bildsprache einbinden
- ❌ Flache Bilder: Freisteller wirkt aufgeklebt („wirkt fehl am Platz“).
- ✅ Eingebundene Bilder: Schatten, Licht und Farbstimmung passen zum Hintergrund („wirkt hochwertig“).
- Bei uns: Porträt/Freisteller und App-Screens mit weichem Schatten und Licht passend zum grünen Verlauf; Screens
  `app_9x16.png` nur mit Demo-Daten und leicht gerahmt, nicht als nackte Ausschnitte. Keine Schrift von der KI
  erzeugen lassen (`README.md`, Regeln).

## Prüfliste vor dem Freigeben (Karussell)
- [ ] Z-Muster: Überschrift führt, eine Aussage pro Folie
- [ ] Format wie in der Vorlage (derzeit 1080×1350), Text innerhalb des Sicherheitsrands
- [ ] Kontrast ≥ 4,5 für kleinen Text; Nebentext nicht auf hellem Verlaufsende; auf dem Handy gedimmt geprüft
- [ ] Folie 1 hält an, Folie 2 funktioniert allein, jede Folie gibt einen Grund zum Wischen
- [ ] Wert vor Einladung, letzte Folie genau **ein** CTA
- [ ] Bilder eingebunden (Schatten/Licht), nichts „aufgeklebt“

---

## Baustein für die Content-Fabrik (in Karussell-Aufträge einfügen)
```
KARUSSELL-DESIGN (strategie/17_karussell_design.md): Pro Folie eine Aussage; Überschrift führt (Z-Muster: groß → Zwischenzeile → klein).
Raster: 1 Hook (stoppt das Scrollen) · 2–3 Beispiel/Fall · 4–5 Diagramm/Tabelle/Rechenweg · 6–9 praktische Schritte/Checkliste · letzte Folie genau ein CTA
(„Speichern für später“ + Weiterleiten-Frage), nie Verkauf vor Wert. Folie 2 muss allein funktionieren.
Format wie Vorlage (1080×1350), Text innerhalb 50 px seitlich / 180 px oben und unten. Kontrast ≥ 4,5: kleiner Text nie in #8FA398 auf dem
hellen Verlaufsende (#153A31), dort #EAF1EC. Bilder eingebunden (weicher Schatten, Licht zum grünen Verlauf), keine aufgeklebten Freisteller,
keine KI-Schrift. Vor dem Freigeben Prüfliste am Ende von 17_karussell_design.md abarbeiten.
```
