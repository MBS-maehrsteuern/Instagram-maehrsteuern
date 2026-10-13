"""Trockenlauf für posten.py – ohne Netz, ohne Instagram, ohne GitHub.

Instagram ist eine Attrappe; git läuft echt, aber gegen ein Wegwerf-Repo (bare „origin“ + zwei Klone: der Lauf und
eine „Claude-Sitzung“, die zwischendurch pusht). Aufruf: python3 -m unittest discover automatik/tests -v
"""
import json, os, shutil, subprocess, sys, tempfile, unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import posten  # noqa: E402

JETZT = datetime(2026, 10, 14, 17, 40, tzinfo=posten.ZONE)
TEXT = "Hinzurechnung nach § 8 GewStG – so rechnest du sie in 30 Sekunden aus."


def sh(cwd, *args):
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def eintrag(eid, typ, uhr, status="freigegeben", **mehr):
    e = {"id": eid, "typ": typ, "zeit": f"2026-10-14 {uhr}", "status": status, "ordner": "posts/x",
         "hinweis": "alt", "bilder": ["bild.png"]}
    if typ != "story":
        e["text"] = "text.txt"
    return {**e, **mehr}


class FakeIG:
    """Attrappe für posten.Instagram – zählt, was veröffentlicht wird."""
    def __init__(self, media=None, beim_posten=None):
        self.user, self.token = "IGUSER", "GEHEIM"
        self.container_n, self.veroeffentlicht, self.media = 0, [], media or []
        self.beim_posten = beim_posten

    def container(self, **daten):
        self.container_n += 1
        return f"c{self.container_n}"

    def veroeffentlichen(self, cid):
        self.veroeffentlicht.append(cid)
        if self.beim_posten:
            self.beim_posten()
        return f"m{len(self.veroeffentlicht)}", f"https://instagram.com/p/m{len(self.veroeffentlicht)}"

    def _get(self, pfad, **params):
        assert pfad == "IGUSER/media", pfad
        return {"data": self.media}


class Trockenlauf(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        origin, self.lauf, self.claude = self.tmp / "origin.git", self.tmp / "lauf", self.tmp / "claude"
        sh(self.tmp, "git", "init", "-q", "--bare", "-b", "claude/instagram", str(origin))
        start = self.tmp / "start"
        sh(self.tmp, "git", "clone", "-q", str(origin), str(start))
        (start / "automatik").mkdir()
        (start / "posts/x").mkdir(parents=True)
        (start / "posts/x/text.txt").write_text(TEXT + "\n")
        (start / "posts/x/video.mp4").write_bytes(b"video")
        from PIL import Image
        Image.new("RGB", (8, 8), "green").save(start / "posts/x/bild.png")
        (start / "posts/x/kaputt.png").write_bytes(b"kein bild")
        self.start = start
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        for repo in (start,):
            sh(repo, "git", "config", "user.name", "Test"); sh(repo, "git", "config", "user.email", "t@t")

    def plan_anlegen(self, eintraege):
        (self.start / "automatik/plan.json").write_text(json.dumps({"eintraege": eintraege}, ensure_ascii=False, indent=2) + "\n")
        sh(self.start, "git", "checkout", "-q", "-b", "claude/instagram")
        sh(self.start, "git", "add", "-A"); sh(self.start, "git", "commit", "-q", "-m", "start")
        sh(self.start, "git", "push", "-q", "-u", "origin", "claude/instagram")
        for repo in (self.lauf, self.claude):
            sh(self.tmp, "git", "clone", "-q", "-b", "claude/instagram", str(self.tmp / "origin.git"), str(repo))
            sh(repo, "git", "config", "user.name", "Test"); sh(repo, "git", "config", "user.email", "t@t")

    def remote_plan(self):
        sh(self.claude, "git", "pull", "-q", "--rebase")
        return {e["id"]: e for e in json.loads((self.claude / "automatik/plan.json").read_text())["eintraege"]}

    def claude_aendert(self, eid, **felder):
        """Eine Claude-Sitzung ändert genau den Eintrag (Zeile neben „status“) und pusht – der klassische Konflikt."""
        sh(self.claude, "git", "pull", "-q", "--rebase")
        datei = self.claude / "automatik/plan.json"
        plan = json.loads(datei.read_text())
        next(x for x in plan["eintraege"] if x["id"] == eid).update(felder)
        datei.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
        sh(self.claude, "git", "commit", "-q", "-am", "Claude: Hinweis")
        sh(self.claude, "git", "push", "-q")

    def lauf_starten(self, ig, argv=("posten.py",), schlafen=lambda s: None):
        with mock.patch.object(posten, "WURZEL", self.lauf), \
             mock.patch.object(posten, "PLAN", self.lauf / "automatik/plan.json"), \
             mock.patch.object(posten, "Instagram", lambda: ig), \
             mock.patch.object(posten, "jetzt", lambda: JETZT), \
             mock.patch.object(posten.time, "sleep", schlafen), \
             mock.patch.object(sys, "argv", list(argv)), \
             mock.patch.dict(os.environ, {"GITHUB_REPOSITORY": "test/repo"}), \
             mock.patch("requests.request", side_effect=AssertionError("kein echter API-Aufruf!")):
            os.environ.pop("GH_TOKEN", None)
            try:
                posten.main()
                return 0
            except SystemExit as ende:
                return ende.code

    # 1 ── normaler Post
    def test_normaler_post(self):
        self.plan_anlegen([eintrag("07-reel-hinzurechnung", "reel", "17:45", video="video.mp4", bilder=[], titelbild="bild.png")])
        ig = FakeIG()
        self.assertEqual(self.lauf_starten(ig), 0)
        self.assertEqual(ig.veroeffentlicht, ["c1"])
        e = self.remote_plan()["07-reel-hinzurechnung"]
        self.assertEqual((e["status"], e["media_id"], e["link"]), ("veroeffentlicht", "m1", "https://instagram.com/p/m1"))
        self.assertTrue((self.claude / "posts/x/_jpg/bild.jpg").exists(), "JPG muss gepusht sein")

    # 2 ── Push-Konflikt direkt nach dem Posten → Status kommt trotzdem an, kein zweiter Post
    def test_push_konflikt_nach_post(self):
        eid = "09-rueckstellung"
        self.plan_anlegen([eintrag(eid, "karussell", "17:45")])
        ig = FakeIG(beim_posten=lambda: self.claude_aendert(eid, hinweis="neu von Claude", zeit_hinweis="x"))
        echtes_git, gescheitert = posten.git, []

        def git_mit_absage(*args):  # erster Status-Push wird zusätzlich abgewiesen (Wettlauf mit weiterem Push)
            if args[0] == "push" and not gescheitert and ig.veroeffentlicht:
                gescheitert.append(1)
                raise subprocess.CalledProcessError(1, "git push", stderr="! [rejected] (fetch first)")
            return echtes_git(*args)

        with mock.patch.object(posten, "git", git_mit_absage):
            self.assertEqual(self.lauf_starten(ig), 0)
        self.assertEqual(len(ig.veroeffentlicht), 1)
        e = self.remote_plan()[eid]
        self.assertEqual(e["status"], "veroeffentlicht")
        self.assertEqual(e["hinweis"], "neu von Claude", "Claudes Änderung darf nicht verloren gehen")
        # nächster Lauf 15 Min. später: nichts mehr fällig, kein zweiter Post
        ig2 = FakeIG(media=[{"id": "m1", "caption": TEXT, "timestamp": "2026-10-14T15:45:03+0000"}])
        self.assertEqual(self.lauf_starten(ig2), 0)
        self.assertEqual(ig2.veroeffentlicht, [])

    # 3 ── Status ging verloren, Beitrag ist aber schon online → nur nachtragen
    def test_schon_online_erkannt(self):
        eid = "09-rueckstellung"
        self.plan_anlegen([eintrag(eid, "karussell", "17:45")])
        ig = FakeIG(media=[{"id": "m77", "caption": "  " + TEXT.replace(" ", "\n", 1) + "\n#steuern",
                            "permalink": "https://instagram.com/p/m77", "timestamp": "2026-10-14T15:45:20+0000"}])
        self.assertEqual(self.lauf_starten(ig), 0)
        self.assertEqual(ig.veroeffentlicht, [], "darf NICHT erneut posten")
        e = self.remote_plan()[eid]
        self.assertEqual((e["status"], e["media_id"], e["veroeffentlicht_am"]), ("veroeffentlicht", "m77", "2026-10-14 17:45"))

    def test_alter_beitrag_mit_gleichem_text_blockiert_nicht(self):
        eid = "09-rueckstellung"
        self.plan_anlegen([eintrag(eid, "karussell", "17:45")])
        ig = FakeIG(media=[{"id": "m1", "caption": TEXT, "timestamp": "2026-09-01T10:00:00+0000"}])
        self.lauf_starten(ig)
        self.assertEqual(len(ig.veroeffentlicht), 1)

    def test_pruefung_scheitert_postet_trotzdem(self):
        self.plan_anlegen([eintrag("09-rueckstellung", "karussell", "17:45")])
        ig = FakeIG()
        ig._get = mock.Mock(side_effect=RuntimeError("IGUSER/media: 500 GEHEIM"))
        self.assertEqual(self.lauf_starten(ig), 0)
        self.assertEqual(len(ig.veroeffentlicht), 1)

    # 4 ── Teaser-Story, deren Feed-Beitrag gescheitert ist
    def test_teaser_bei_gescheitertem_feed(self):
        self.plan_anlegen([eintrag("09-rueckstellung", "karussell", "11:45", status="fehler"),
                           eintrag("09-story-aufloesung", "story", "17:50")])
        ig = FakeIG()
        self.assertEqual(self.lauf_starten(ig), 0)
        self.assertEqual(ig.veroeffentlicht, [])
        self.assertEqual(ig.container_n, 0, "kein Container für die Story")
        self.assertEqual(self.remote_plan()["09-story-aufloesung"]["status"], "freigegeben")

    def test_teaser_wenn_feed_im_selben_lauf_scheitert(self):
        self.plan_anlegen([eintrag("09-rueckstellung", "karussell", "17:41", bilder=["kaputt.png"]),
                           eintrag("09-story-aufloesung", "story", "17:50")])
        ig = FakeIG()
        self.assertEqual(self.lauf_starten(ig), 1)
        self.assertEqual(ig.veroeffentlicht, [])
        p = self.remote_plan()
        self.assertEqual((p["09-rueckstellung"]["status"], p["09-story-aufloesung"]["status"]), ("fehler", "freigegeben"))

    def test_teaser_nach_veroeffentlichtem_feed(self):
        self.plan_anlegen([eintrag("09-rueckstellung", "karussell", "11:45", status="veroeffentlicht"),
                           eintrag("09-story-aufloesung", "story", "17:50"),
                           eintrag("04-story-frage", "story", "17:42")])   # andere Nummer: unabhängig
        ig = FakeIG()
        self.assertEqual(self.lauf_starten(ig), 0)
        self.assertEqual(len(ig.veroeffentlicht), 2)

    # 5 ── Vorbereitungsfehler trifft nur diesen Eintrag
    def test_vorbereitungsfehler(self):
        self.plan_anlegen([eintrag("05-kaputt", "karussell", "17:41", bilder=["kaputt.png"]),
                           eintrag("07-reel-hinzurechnung", "reel", "17:45", video="video.mp4", bilder=[])])
        ig = FakeIG()
        self.assertEqual(self.lauf_starten(ig), 1)   # Lauf rot, damit der Wächter meldet
        self.assertEqual(len(ig.veroeffentlicht), 1)
        p = self.remote_plan()
        self.assertEqual(p["05-kaputt"]["status"], "fehler")
        self.assertIn("Vorbereitung", p["05-kaputt"]["fehler"])
        self.assertEqual(p["07-reel-hinzurechnung"]["status"], "veroeffentlicht")

    def test_token_landet_nie_im_plan(self):
        self.plan_anlegen([eintrag("09-rueckstellung", "karussell", "17:45")])
        ig = FakeIG()
        ig.veroeffentlichen = mock.Mock(side_effect=RuntimeError("media_publish?access_token=GEHEIM: 400"))
        self.assertEqual(self.lauf_starten(ig), 1)
        e = self.remote_plan()["09-rueckstellung"]
        self.assertEqual(e["status"], "fehler")
        self.assertNotIn("GEHEIM", e["fehler"])

    def test_text_waehrend_warten_geaendert(self):
        eid = "09-rueckstellung"
        self.plan_anlegen([eintrag(eid, "karussell", "17:45")])
        ig = FakeIG()

        def schlafen(_):  # Claude korrigiert die Bildunterschrift, während der Lauf schläft
            sh(self.claude, "git", "pull", "-q", "--rebase")
            (self.claude / "posts/x/text.txt").write_text("Korrigiert: " + TEXT)
            sh(self.claude, "git", "commit", "-q", "-am", "Text"); sh(self.claude, "git", "push", "-q")

        self.assertEqual(self.lauf_starten(ig, schlafen=schlafen), 0)
        self.assertEqual(ig.veroeffentlicht, ["c4"], "neuer Container (c1/c2 = Kind/Karussell alt, c3/c4 = neu)")


class Waechter(unittest.TestCase):
    def setUp(self):
        import waechter
        self.w = waechter

    def test_takt_alter(self):
        from datetime import timezone
        utc = (datetime.now(timezone.utc) - timedelta(minutes=55)).strftime("%Y-%m-%dT%H:%M:%SZ")
        with mock.patch.object(self.w, "gh", return_value=utc):
            self.assertAlmostEqual(self.w.takt_alter(), 55, delta=1)
        with mock.patch.object(self.w, "gh", return_value=""):
            self.assertIsNone(self.w.takt_alter())

    def lauf(self, alter, zustand):
        aufrufe = []

        def gh(*args, eingabe=None):
            aufrufe.append(args)
            if args[0] == "issue" and args[1] == "list":
                return json.dumps([{"number": 7, "body": f"<!-- zustand {json.dumps(zustand)} -->"}])
            if args[0] == "api":
                return "success\thttps://x\t2026-10-14T10:00:00Z"
            return ""

        with mock.patch.object(self.w, "gh", gh), mock.patch.object(self.w, "takt_alter", return_value=alter):
            self.w.main()
        return [a for a in aufrufe if a[:2] == ("issue", "comment")], [a for a in aufrufe if a[:2] == ("issue", "edit")]

    def test_takt_rot_meldet_einmal(self):
        kommentare, edits = self.lauf(55, {"rot": {}, "gewarnt": {}})
        self.assertEqual(len(kommentare), 1)
        self.assertIn("Posten-Takt steht", kommentare[0][-1])
        self.assertIn('"takt": "rot"', edits[0][-1])
        kommentare, _ = self.lauf(70, {"rot": {}, "gewarnt": {}, "takt": "rot"})
        self.assertEqual(kommentare, [], "kein zweiter Kommentar, solange rot")

    def test_takt_ok(self):
        kommentare, edits = self.lauf(12, {"rot": {}, "gewarnt": {}, "takt": "rot"})
        self.assertEqual(kommentare, [])
        self.assertNotIn('"takt"', edits[0][-1])


if __name__ == "__main__":
    unittest.main()
