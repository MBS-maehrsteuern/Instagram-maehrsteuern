# maehrsteuern – Instagram

- Zu Beginn jeder Sitzung Skill `lage` nutzen: `python3 automatik/lage.py`, dann `LAGE.md` lesen und Loris sagen, was als Nächstes online geht und was offen ist.
- Nach jeder Änderung: aussagekräftige deutsche Commit-Nachricht, ggf. `automatik/lage_notizen.md` anpassen, `LAGE.md` + `LAGE.html` neu erzeugen und mit committen.
- Übersicht über das Repo: `README.md`. Regeln (keine Arbeitgeber-Daten, KI-Label) dort beachten.
- **Reels nur mit Loris' Stimme** – nie ohne. Vor dem Bau `aufnahmen/` prüfen, fehlt die Aufnahme: Loris fragen. Neue Regeln: `strategie/19_wissen_2026-10-24.md`.
- **Ton-Check nach jedem Schnitt (Loris 30.10., ausnahmslos):** Endfassung transkribieren, Pausen in der Stimme > 0,5 s kürzen, jede Schnittstelle auf angeschnittene Wörter prüfen (Pegelverlauf vor/nach dem Schnitt, Wort vollständig im Transkript, Luft am Ende). Erst danach Loris zeigen oder einplanen. Werkzeug: `vorlagen/system/schnitt/feld_fertig_v5.py` (ruft `feld_schnitt_v5.py`) (Pausen-Kürzung + Zeit-Mapping für Overlays + Premium-Stimme).
- **Premium-Stimme (Loris 30.10.):** Außenaufnahmen erst durch den ElevenLabs-Stimmisolator, dann 10 % Original-Ton nur während des Sprechens dazumischen (Gate; sonst verschluckt der Isolator Wörter bei Windstößen – mehr Original bringt Wind zurück, Loris 31.10.) und leichte Klangformung (−2,5 dB bei 250 Hz, +3 dB bei 3,5 kHz). Kein starkes Entrauschen mehr – das klingt dumpf.
