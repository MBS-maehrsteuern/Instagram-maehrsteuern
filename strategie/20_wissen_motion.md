# 20 · Wissen vom 26.10.2026 – Motion-Vokabular und Premium-Karussell-Muster

Quellen: Karussells @herr_tech („Mach ein schönes Video reicht nicht“ – Motion-Spickzettel; „30 Reels mit Claude in 30 Minuten“),
Screenshots Loris 26.10. Nur **Stil und Muster** übernehmen – Farben, Schrift und Marke bleiben maehrsteuern (Grün auf Dunkel).
Ergänzt `19_wissen_2026-10-24.md`. Baukasten: `vorlagen/system/premium/motion.js` (Reels), `karussell.html` (Karussells).

## 1. Motion-Vokabular (jede Bewegung hat eine Aufgabe)
| Effekt | Wirkung | Bei uns einsetzen für |
|---|---|---|
| **Pop in** (kurzer Größensprung) | „Das ist neu/wichtig“ | Zahl der Pointe, Stempel, Haken |
| **Scale up** | wächst zur Endgröße | große Ergebnis-Zahl im Hook |
| **Stagger** (nacheinander, 0,1–0,15 s) | Liste wird lesbar | Aufzählungen, Checklisten, Tage |
| **Ease in-out** | natürlich, nie ruckartig | Kamerafahrt, Balken, Pfeile |
| **Overshoot** | lebendig, „klickt ein“ | Schalter, Chips, Antwort-Kacheln |
| **Bounce** | verspielt – sparsam! | höchstens Teilen-/Folgen-Symbol am Ende |
| **Typewriter** | „wird gerade geschrieben“ | Einspruchs-Satz, Prompt, Formel |
| **Word reveal** | Stimme und Bild synchron | Untertitel (läuft schon), Schlagzeilen |
| **Text swap** | Gegensatz in einem Wort | „Mensch → Programm“, „05 → 09“, „falsch → richtig“ |
| **Count-up** | Zahl wird spürbar | 12 %, 12.348 €, 1.260 € |
| **Draw-on** | Linie zeichnet sich | Prüfpfad, Geldfluss, Meldeweg Arbeitgeber → Finanzamt |
| **Bar grow** | Verhältnis auf einen Blick | 3 % vs. 5 %, Grenze 100.000 € |
| **Mask reveal / Wipe** | Szenenwechsel ohne Ton-Whoosh | statt harter Schnitte zwischen Panels |
| **Punch zoom** | starker Akzent (1× pro Reel!) | genau die Pointe des Hooks |

Regeln: max. 2 Effekte gleichzeitig; Bounce/Punch-Zoom höchstens 1× pro Reel; Dauer 0,25–0,6 s;
Bewegung startet mit dem gesprochenen Wort (Wortzeiten), nicht vorher. Kein Zirkus.

## 2. Karussell-Muster (herr_tech „30 Reels“)
- **Schritt-Kicker:** „SCHRITT 01 / 05 · VERBINDEN“ – Fortschritt und Ziel sofort klar.
- **„Der alte Weg“-Folie** (früh): Schmerz in 4 Zeilen mit Icon, Schlusszeile „X macht alle vier.“
- **„Ehrlich gesagt“-Folie** (spät): 3 Grenzen/Haken offen nennen → Vertrauen (bei uns: „Ersetzt keine Steuerberatung“, „Demo-Zahlen“, „Excel bleibt erlaubt“).
- **„Vorher · Nachher“-Folie** (vor CTA): zwei Kästen VORHER/JETZT mit je 3 Zeilen.
- **Prompt-/Formel-Box** in Mono-Schrift: konkret kopierbar (bei uns: Formel, Musterformulierung Einspruch).
- **Speichern-Hinweis schon auf Folie 1** („🔖 Speichern für die nächste Erklärung“) und Spickzettel-Rahmen („Dein Steuer-Spickzettel“).

## 3. Umsetzung
- Karussells: neue Panel-Typen `vorher_nachher`, `alter_weg`, `box` (Mono-Box) und Feld `speichern` (Hinweis unten links auf Folie 1) in `karussell.html`.
- Reels: `motion.js` in neue Szenen einbinden; Agenten-Brief verweist darauf.
- Idee Serie: **„Steuer-Spickzettel“**-Karussells (z. B. „Pauschalen 2026 auf einen Blick“, „Fristen-Spickzettel“) – reine Speicher-Formate.
