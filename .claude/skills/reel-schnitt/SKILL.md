---
name: reel-schnitt
description: Reels im neuen Schnitt-Stil von maehrsteuern bauen (Loris 16.11.2026) – echtes Gesicht im Hook, Steuer-Dokument (z. B. Anlage N) wird befüllt, Drohnen-Kamera mit Crash-Zooms und Reißschwenks wie bei den Gerba-Bau-Reels, Zahlen zählen groß am Rand hoch, auf Musik geschnitten (Drop, Schnitt pro Schlag, CTA auf dem Gesangseinsatz), Stimme nur im Hook. Nutzen bei „Reel wie i05“, „wie das Finanzbeamte-Reel“, „Gerba-Stil“, „auf Musik schneiden“, „Beat-Schnitt“, „mit Song“, „neues Reel im neuen Stil“ – auch für andere Marken (z. B. Ehrensaft/TikTok) als Vorlage.
---

# Reel-Schnitt im neuen Stil (Vorlage: i05 „Finanzbeamte setzen das selbst ab“)

Erstes Reel in diesem Stil: i05, 16.11.2026, von Hand gepostet mit „Flower In A Hurricane“ (Justice) aus der Instagram-Musik.
Nach 2 Std.: 372 Aufrufe (ca. 5× ein übliches Reel), 74 % Nicht-Follower, 7× gespeichert, 11 Kommentare, aber Ø 6 s Wiedergabe.
Regeln im Detail: `strategie/22_wissen_schnitt_stil.md`. Diese Datei ist die Bauanleitung.

## Bausteine (alle in `vorlagen/system/premium/`)
| Datei | Zweck |
|---|---|
| `insider_05_beat.html` | **Hauptvorlage** Beat-Schnitt: Hook mit Stimme → Drop → Anlage N im Takt → CTA auf Gesangseinsatz. `window.render(t)` |
| `insider_05_beat_effekte.json` | Crash-Zooms/Reißschwenks je Zeitpunkt `[start, dauer, "zoom"/"whipx"/"whipy", stärke]` |
| `insider_05_gerba.html` (+ `_effekte.json`) | Variante mit Stimme über die ganze Länge (ohne Song-Schnitt) |
| `insider_05_daten.js` | Wortzeiten der Stimme (`WF=[[wort, sek], …]`) – nur für den Hook nötig |
| `takt.py` | Song analysieren: BPM, Raster, Akzente, Drop, grobe Gesangs-Kandidaten |
| `effekte.py` | Unschärfe-Effekte nachträglich auf die Einzelbilder |
| `rendern.mjs` | HTML → Einzelbilder (30 fps); mit Probe-Zeiten nur Vorschau-PNGs |
| `reel_bauen.py` | Rendern + Effekte + Ton für die Variante **mit** Stimme durchgehend |

## Ablauf Beat-Schnitt (so wie i05)
1. **Stimme prüfen** (CLAUDE.md: Reels nur mit Loris' Stimme): Hook-Aufnahme in `aufnahmen/`? Sonst Loris fragen. Wortzeiten → `<name>_daten.js`.
2. **Song analysieren:** `python3 takt.py <song.mp3> <ab_s> 90`. Daraus: Schlag `B`, Drop-Zeit, Gesangseinsatz.
   Gesangs-Erkennung ist grob → Einsatz gegenhören bzw. Loris fragen. (i05: Song ab **0:44,04**, 126 BPM, Drop 3,74 s, Gesang 17,54 s.)
3. **Startpunkt wählen:** Song-Start so legen, dass der **Drop direkt nach dem Hook** kommt (Hook ≈ 3–4 s) und der **CTA genau auf dem Gesangseinsatz** liegt.
4. **Vorlage kopieren** (`insider_05_beat.html` → `<thema>_beat.html`) und anpassen:
   - Konstanten `B`, `DROP`, Abschnitte `HO/FA/AM/GR/SP/CTA` als `BEAT(k)` (immer auf Takt; neue Punkte auf 1, 2 oder 4 Takte).
   - `TX` = kurze Texteinblendungen (max. ~4 Wörter, GROSS, ein Akzentwort grün) – sie ersetzen nach dem Hook die Untertitel.
   - Dokument im `#blatt` tauschen (Anlage N → z. B. Anlage KAP, Bescheid, Rechnung): **fast ohne Wörter**, nur kurze Zeilentitel, sonst Linien.
   - `hud(t)`: Titel + Zahl am Rand, die hochzählen (`zahl(von, bis, start, dauer, fmt)`).
   - Kamera-Keyframes `K=[[zeit, ziel-id, zoom, rotX, rotY, rotZ, dauer]]` – schräg (rotZ ±6–12°), Ziel = Zeile, die gerade dran ist.
   - `<name>_effekte.json`: Crash-Zoom (`zoom` 0,3–0,45) auf Drop und Abschnittswechsel, `whipx`/`whipy` (240–300 px) zwischen Zeilen.
5. **Probe ansehen:** `node rendern.mjs <name>.html <dauer> <ordner> 2,4.4,8,…` → Kontaktbogen bauen, prüfen: nichts abgeschnitten, Text nicht verdeckt.
6. **Rendern + Effekte:** `node rendern.mjs <name>.html <dauer> <frames>` und `python3 effekte.py <frames> <name>_effekte.json`.
7. **Ton:** Video nur mit Hook-Stimme speichern (`reel_beat_ohne_song.mp4`, Stimme bis Hook-Ende, danach Stille, `loudnorm=I=-16`).
   Vorschau mit Song nur im Scratchpad mischen (Song bis Hook auf 0,3, dann 1,0; `loudnorm=I=-14`) – **Song nie ins Repo**.
8. **Posten:** Kommerzieller Song → **von Hand in der App** (Instagram-Musik, Start = gewählter Song-Start). In `plan.json` Status `manuell`, `video` auf die Datei ohne Song. Lizenzfreie Musik (`musik/`) → normal automatisch.
9. **CTA-Stichwort** (z. B. ABZUG) in `automatik/interaktion.json` → `stichwort_antworten` + `manychat_stichwoerter`, damit `kommentare.py` die DM schickt. Hinweis in die Bildunterschrift.
10. Commit (deutsch), `lage_notizen.md` + LAGE neu. Änderungen am Live-Zweig `claude/instagram` nur mit Loris' Okay.

## Stilregeln (Kurzform)
- Sek. 0–2 echtes Gesicht (Foto `assets/marke/`), Badge „EX-FINANZAMT · DIPLOM-FINANZWIRT“. Kein KI-Gesicht.
- **Keine** Schallwelle, **keine** Wort-Spur, **kein** Editor-Look, keine fremden eingeschobenen Sätze.
- Kamera immer in Bewegung: Drohnen-Drehung im Überblick, Speed-Ramp (schnell rein, langsam weiterdriften), Stöße auf Schlägen.
- Lineouts: Rahmen um aktive Zeile, Haken und Symbole zeichnen sich als Linie.
- Markenfarben maehrsteuern (Grün `#53C3A2`/`#7FE0C2` auf `#070C0A`), Schrift Outfit, Untertitel kursiv per `skewX(-9deg)`.

## Lernpunkte aus den Zahlen
- i05 erreichte viele Nicht-Follower, aber Ø 6 s von 22 s → **die ersten 3 s müssen noch härter ziehen** (Hook-Satz knapper, Drop früher testen, z. B. Hook 2 s).
- Likes kamen am Anfang und am Ende (CTA) → CTA-Moment funktioniert.

## KI-Shots mit Higgsfield (Ehrensaft-TikTok, 16.11.)
- Connector „Higgsfield“ (voller MCP) kann erzeugen: `generate_video_batch` → `jobs_wait` → Ergebnis-URLs herunterladen. Vorher `get_cost:true` prüfen und bei Kosten Loris fragen.
- Preise (9:16, ohne Ton): Seedance 2.5 1080p 5 s = 80 Credits, Seedance 2.0 Mini 720p 4 s = 4, Grok Lite 720p 3 s = 3.
- Aus wenigen Shots viele Einstellungen machen: `ehrensaft/posts/18_tiktok_higgsfield/schnitt.py` (Ausschnitt, Drehung, Spiegeln, Zeitlupe, Farb-Grade), Grafik-Ebene `overlay.html` + `render_overlay.mjs` + `zusammen.py`, Effekte mit `effekte.py`.
