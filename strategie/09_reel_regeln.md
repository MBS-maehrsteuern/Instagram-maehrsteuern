# Reel-Regeln aus Feedback (Stand 30.09.2026)

Ergänzt die Formel in `08_demo_reel_formel.md`. Gilt für jedes Reel der Content-Fabrik.
Allgemeines Wissen (Algorithmus, Teilen, Länge, Cover, Suche): `11_wissen_instagram.md`.
Vorlage zum Kopieren: `vorlagen/system/schnitt/p01_reel_ampel_hook.json` (Renderer `vorlagen/system/montage.py`).

## Feedback Loris zum Ampel-Reel `reel_hook.mp4` (30.09.)
- Gut gemacht, aber **zu professionell**: Es wirkt wie ein Produktvideo für eine Website oder Werbung, **nicht wie Instagram**.
- Der Schmerzpunkt im Einstieg funktioniert halbwegs. **Danach wird es generisch**: Screen-Demo mit Lo-Fi-Musik ist ein
  Standard-Muster, das man überall sieht, und hält nicht.
- **Was bei Loris vorher besser lief:** persönlicher Aufhänger, **mehr Drama, mehr Trigger, der Schmerzpunkt
  bleibt länger und wird persönlich erzählt** („mir ist passiert …“) statt neutral gezeigt.
- Folgerungen für die nächsten Reels:
  - Ich-Perspektive, eine echte kleine Geschichte (Situation → Moment, wo es knallt → Wendung), nicht „Problem → Tool-Demo“.
  - Der Schmerz trägt das Reel, das Tool ist nur die Pointe am Ende, nicht der Hauptteil.
  - Text als Gedanke oder Zitat („Ich dachte, die Rückstellung passt.“), nicht als Werbezeile („Alles rechnet neu.“).
  - Keine Hintergrundmusik nach Schema. Lieber Originalton, Stille, Atmo oder einen Trend-Sound aus der Instagram-App (von Hand).
  - Abwägen: professionell/sauber gegen persönlich/roh – auf Instagram gewinnt eher persönlich.

## Learnings Stimme und Ton (Loris, 30.09.)
- **Eigene Stimme trägt das Reel** (Sprachnachricht vom Handy reicht). Text vorher grob überlegen, locker sprechen.
- **Untertitel bilden das Gesprochene genau ab** – Wort für Wort, damit das Reel auch ohne Ton verständlich ist.
  Alle eingeblendeten Texte folgen dieser Logik (Schlagworte wie „#BEZUG!“ nur als Verstärkung des Gesagten).
  Zeitmarken per Spracherkennung (faster-whisper, Modell „small“), Wortlaut am Ende von Hand gegenlesen.
- **Sprache hat Vorrang:** Musik höchstens ganz leise im Hintergrund, Geräusche (Uhr, Fehlerton, Tippen) ebenfalls leise.
  Richtwerte: Stimme ca. −18 LUFS, Musik ~0,13, Atmo 0,2–0,3.
- Aufnahme: Abstand zum Handy-Mikro halten (sonst klingt es kratzig/übersteuert), ruhiger Raum.

## Länge: 12–20 s (Auswertung 11.10., angepasst 13.10.)
- Ø gesehen nur **20–24 % der Länge**, egal ob 23 s oder 41 s; Skip 62–82 %. Die Zuschauer gehen nach ca. 5–7 s – die Länge
  ist also nicht das Problem, sondern alles nach dem Einstieg.
- **Regel ab 13.10.:** Reels **12–20 s**, **Pointe in den ersten 5 s**, Hook-Text ab 0,3 s und ohne Ton verständlich, höchstens 3 Punkte, Sprechtexte höchstens 35–40 Wörter. Nicht mehr nachträglich unter 15 s schneiden, wenn dabei Inhalt (Zahl, Ergebnis) wegfällt. Zusätzliche Kennzahl: **Ø Sehdauer in Sekunden** (Ziel ≥ 6 s) neben „gesehen %“ – kurze Reels heben den Prozentwert rechnerisch, nicht die Sehzeit (13.10.: 13–15 s → Ø 4,8 s, 30–41 s → Ø 8,5 s; n = 2 je Gruppe, Hinweis).
- Bereits aufgenommene Sprachnachrichten werden nicht verworfen, sondern per Schnitt gekürzt (13–16 am 11.10.: 22–26 s → 13–15 s).
- Täglich mindestens ein Reel: Der Tag ohne Reel (09.10.) erreichte 66 Konten, der Tag mit zwei Reels (10.10.) 362.
- **Reichweite steht nach ~13 h zu 80–90 % fest** (5 Reels, 13.10.). Wer nach 24 h unter 150 Erreichten liegt, wird nicht mehr „entdeckt“ – Folgeformat sofort anpassen, nicht 48 h warten. Überspringrate weiter erst ab 48 h werten.

## Listen-Reels: höchstens 3 Punkte (Entscheidung Loris, 04.10.)
- Reel „5 Dinge mit Code statt Excel“ (41 s): Einstieg stark (46 % weitergewischt statt 66 %), aber Ø Sehdauer nur 7,6 s = 19 % der Länge – die meisten steigen nach Punkt 5/4 aus.
- **Regel:** Listen-/Countdown-Reels mit **maximal 3 Punkten**, Ziel **unter 20 s**. Mehr Punkte → als Karussell oder als Serie (Teil 1, 2 …).
- Countdown beibehalten (3 → 1), stärkster Punkt zuletzt, damit man bis zum Ende schaut.
- Folge-Reels einer Serie müssen allein funktionieren: kein „Nummer X aus meinem …“ im Hook oder in der Frage; Serien-Hinweis höchstens als letzte Zeile vor den Hashtags („Teil 4 meiner Excel-Serie – alle Teile im Profil“).

## Hook (0–3 s)
- **Kein Dauerfeuer.** Im Hook 2 Einstellungen, nicht 4–5 Achtel-Schnitte. Jede Einstellung darf 1,4–2 s stehen.
- **Text ab 0,3 s**, groß mit schwarzer Outline, Wort für Wort bzw. Zeile für Zeile. Der Hook muss **ohne Ton** funktionieren.
- **Fehler-Callout** passt für @maehrsteuern: echter Schmerz („#BEZUG! – 2 Tage vor Abgabe. Kennst du?“), dann Auflösung.
- Hook-Formulierungen: Sammlung unter „Inspiration“ unten. Keine Behauptungen, die das Reel nicht einlöst.

## KI-Clips (Runway)
- **Nur einen Ausschnitt nutzen.** KI-Gesichter übertreiben die Mimik (Schreien, Hände an den Kopf). Das wirkt unecht, die Leute mögen es nicht.
- Gut: der **stille, angespannte Moment** (Blick in den roten Bildschirm, Stirnrunzeln), langsame Kamerafahrt.
- Clip auf `"tempo": 0.8` verlangsamen, keine Glitch- oder Shake-Effekte drauf.
- Beim Prompt ruhige Mimik verlangen („subtle, restrained expression“) statt „shock“ oder „disbelief“.

## Ton
- **Die Musik muss zur Emotion passen.** Schmerz-Moment ≠ Deep House.
- Im Hook **keine Musik, sondern Atmo**: Tippen → Fehlerton (Text poppt darauf auf) → Uhr-Ticken.
- **Musik setzt erst mit der Lösung ein** (Schnitt aufs Tool). Der Kontrast Stille → Musik trägt die Erleichterung.
- Musik für die Lösung: ruhig, souverän (Lo-Fi, Minimal), kein Party-Drop. Beat ab Sekunde 0.
- Atmo liegt unter `musik/atmo/`, Titel unter `musik/` (Quellen in `musik/QUELLEN.md`).

## Schnitt und Effekte
- Effekte **sparsam und gezielt**: ein sauberer Whip-Pan beim Wechsel Schmerz → Lösung reicht.
- Flash, Glitch, Zoom-Punch und Shake (Bau-Montage-Stil) fallen auf, sind aber schnell zu viel und im Feed gesättigt.
  Höchstens einzeln einsetzen, nie alle gleichzeitig.
- **Bau-Montagen (Gerba-Stil) funktionieren im Handwerk, nicht für Software.** Dort zeigt jeder Schnitt echten Fortschritt,
  bei Software wirkt dasselbe Tempo nur hektisch. Unser eigenes Konzept: `10_software_reel_konzept.md`.
- Unruhige Screens hinter Text abdunkeln (`"abdunkeln": 0.35`).

## Text und Safe-Zone (1080×1920)
- Nichts über **y ≈ 1500** (Bildunterschrift und Buttons von Instagram) und nichts unter **y ≈ 200** (Kopfzeile).
- Rechts ca. 150 px frei lassen (Like-, Kommentar- und Teilen-Buttons).
- Text nie übers Gesicht legen. Beim KI-Clip steht der Text auf Brust bzw. Hemd.
- Farben: Rot = Fehler/Schmerz, Gelb = Frage, Grün = Lösung, Weiß = Rest.

## Inspiration für Hooks (Fehler/Problem, auf Steuern übertragen)
- „Diesen Fehler macht jeder bei der Steuerrückstellung – hier ist die Lösung.“
- „Hör auf, das hier zu tun – es hält dich nur auf.“ (Excel-Verknüpfungen)
- „Kennst du das, wenn … ?“ (#BEZUG! kurz vor Abgabe)
- „3 Fehler, die du bestimmt machst, wenn du die GewSt-Hinzurechnung rechnest.“
- „Das hat mir Stunden gespart – und es ist lächerlich einfach.“
- „Früher habe ich immer diesen Fehler gemacht.“

Quellen: kontentino.com/de/blog/100-hook-ideen-instagram-reels, speekly.de/blog/100-ugc-hook-beispiele
