# Triple Hook – Pflicht für jedes Reel (Loris, 22.11.2026)

**Kurz:** Der erste Satz jedes Reels hat ab jetzt drei Teile: Er sagt, **für wen** es ist, macht **neugierig** und dreht dann **die Erwartung um**. Dazu wird dieser erste Satz nicht mehr nur gesprochen, sondern Wort für Wort als bewegter Text auf dunklem Grund gezeigt. Gilt für alle neuen Reels und für alle Reels, die noch nicht online sind.

Vorbild: Bildschirmaufnahme eines englischen Lehr-Reels („The triple hook“), von Loris am 22.11. geschickt. Übernommen wird nur das Prinzip, kein Text und keine Grafik.

## 1. Die Formel (in einem Satz, gesprochen höchstens ~4 Sekunden)

| Teil | Aufgabe | Wie | Beispiel (Kleinunternehmer) |
|---|---|---|---|
| **1 Kontext** | Die richtigen Leute bleiben hängen | Zielgruppe oder Situation nennen – gern am Ende der ersten Satzhälfte, nicht als Einleitung | „Ein einziger Auftrag …“ |
| **2 Neugier** | Sie lehnen sich rein statt wegzuwischen | eine Zahl, die die Aussage stützt · einen Schmerz benennen · etwas Überraschendes sagen | „… kann dich sofort umsatzsteuerpflichtig machen.“ |
| **3 Wendung** | Die Erwartung kippt | „nicht …, sondern …“, „und trotzdem …“, „völlig legal“ | „Nicht erst ab Januar.“ |

Regeln:
- **Sagen, zeigen, schreiben:** Was gesagt wird, steht gleichzeitig als Text im Bild, und ein Symbol zeigt es.
- Kontext nicht vorne breit erklären („Heute geht es um …“) – direkt rein.
- Zahl, Frist oder Paragraf im Hook müssen stimmen und im Rest des Reels belegt werden (Rechtsstand prüfen).
- Kein Clickbait, das das Reel nicht einlöst.
- 2–3 Varianten je Reel schreiben, Loris wählt und spricht ein.

## 2. Der Look (erste 3–5 Sekunden)

- Dunkler Grund (`#070C0A`, weiche Vignette), Text weiß, **Schlüsselwort groß in Markengrün `#53C3A2` mit leichtem Leuchten**; die Wendung („nicht“, „trotzdem“) darf rot `#E07A6B` sein.
- Jedes Wort erscheint genau dann, wenn Loris es sagt (Wortzeiten aus der Transkription), kleiner Schub von unten, ~0,12 s.
- Zeilen stapeln sich oben links, ältere Zeilen werden etwas blasser. Pro Zeile höchstens ein großes Wort.
- Ein schlichtes Strich-Symbol zeichnet sich neben dem Text (Dokument, Kalender, Haus, Auto, Euro, Warnung …).
- Danach blendet der Block in ~0,25 s aus und das Reel läuft normal weiter (Stimme durchgehend).
- Sicherheitszone: Text nur zwischen x 80–1000 und y 220–1500 (unten liegt die Instagram-Leiste).
- Vorlage: `vorlagen/system/premium/hook_triple.html`, Bau: `vorlagen/system/schnitt/hook_triple_bauen.py`.

## 3. Ablauf je Reel

1. Hook-Varianten schreiben → `aufnahmen/<datum>/hooks_einsprechen.md`.
2. Loris spricht die gewählte Variante als Sprachnachricht ein (ruhig, gleiche Stimmlage wie der Rest).
3. Premium-Stimme (Isolator, 10 % Original nur beim Sprechen, Klangformung) → vor den bisherigen Text setzen, alten ersten Satz entfernen.
4. Animierten Hook rendern und vor das Reel setzen.
5. **Ton-Check** (CLAUDE.md): transkribieren, Pausen > 0,5 s kürzen, Schnittstellen prüfen.
6. Titelbild an den neuen Hook anpassen, dann Loris zeigen.
