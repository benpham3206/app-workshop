import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tooling" / "scaffold.py"
TROUBLESHOOT = ROOT / "tooling" / "troubleshoot.py"
ICON_PLAN = ROOT / "tooling" / "icon_plan.py"
EXAMPLE = ROOT / "examples" / "neutral-preview" / "project.json"


def invoke(*arguments):
    return subprocess.run(
        [sys.executable, str(TOOL), *map(str, arguments)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


class ScaffoldContracts(unittest.TestCase):
    def test_process_actions_have_stable_unique_ids(self):
        process = json.loads((ROOT / "config" / "process.json").read_text())
        self.assertEqual(process["version"], 2)
        ids = [action["id"] for phase in process["phases"] for action in phase["actions"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(action["text"] for phase in process["phases"] for action in phase["actions"]))

    def test_catalog_choices_have_navigable_sources(self):
        catalog = json.loads((ROOT / "config" / "catalog.json").read_text())
        schema = json.loads((ROOT / "config" / "schema" / "project.schema.json").read_text())
        for item in catalog["identities"]:
            self.assertTrue((ROOT / "design" / "identity" / item / "README.md").is_file(), item)
        for item in catalog["platforms"]:
            self.assertTrue((ROOT / "platforms" / item / "README.md").is_file(), item)
        for item in catalog["modules"]:
            self.assertTrue((ROOT / "modules" / item / "README.md").is_file(), item)
        self.assertEqual(catalog["identities"], schema["properties"]["identity"]["enum"])
        self.assertEqual(catalog["platforms"], schema["properties"]["platforms"]["items"]["enum"])
        self.assertEqual(catalog["modules"], schema["properties"]["modules"]["items"]["enum"])

    def test_neutral_example_generates_selected_structure(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "generated"
            result = invoke("generate", "--config", EXAMPLE, "--output", output)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((output / "AGENTS.md").is_file())
            self.assertTrue((output / "PRINCIPLES.md").is_file())
            self.assertTrue((output / "docs" / "agents" / "NAVIGATION.md").is_file())
            self.assertTrue((output / "docs" / "agents" / "TASK-PACKET.md").is_file())
            navigation = (output / "docs" / "agents" / "NAVIGATION.md").read_text()
            self.assertIn("platforms/ios/PROFILE.md", navigation)
            self.assertIn("platforms/watchos/PROFILE.md", navigation)
            self.assertIn("modules/active-activity/CONTRACT.md", navigation)
            self.assertIn("compatibility/IPHONE-DUO.md", navigation)
            self.assertNotIn("platforms/tvos/PROFILE.md", navigation)
            self.assertNotIn("{{", navigation)
            for destination in re.findall(r"\]\(([^)]+)\)", navigation):
                if not destination.startswith("http"):
                    self.assertTrue((output / "docs" / "agents" / destination).resolve().is_file(), destination)
            self.assertIn("May edit", (output / "docs" / "agents" / "TASK-PACKET.md").read_text())
            self.assertTrue((output / "docs" / "product" / "BRIEF.md").is_file())
            self.assertTrue((output / "docs" / "START-TO-SHIP.md").is_file())
            self.assertTrue((output / "docs" / "BEGINNER-GUIDE.md").is_file())
            self.assertTrue((output / "resources" / "process.json").is_file())
            self.assertTrue((output / "docs" / "OPERATING-SYSTEM.md").is_file())
            self.assertTrue((output / "docs" / "operations" / "WORKBOARD.md").is_file())
            self.assertTrue((output / "docs" / "quality" / "TEST-MATRIX.md").is_file())
            self.assertTrue((output / "docs" / "quality" / "GLASS-AND-PERFORMANCE.md").is_file())
            self.assertTrue((output / "docs" / "engineering" / "SECURE-FAST-DEFAULTS.md").is_file())
            self.assertIn("Liquid Glass", (output / "docs" / "quality" / "GLASS-AND-PERFORMANCE.md").read_text())
            self.assertIn("Representative physical devices", (output / "docs" / "quality" / "TEST-MATRIX.md").read_text())
            self.assertTrue((output / "docs" / "quality" / "AUTOMATION.md").is_file())
            self.assertTrue((output / "docs" / "engineering" / "ECOSYSTEM.md").is_file())
            self.assertTrue((output / "docs" / "release" / "STORE-PAGE.md").is_file())
            self.assertTrue((output / "platforms" / "ios" / "PROFILE.md").is_file())
            self.assertTrue((output / "platforms" / "watchos" / "PROFILE.md").is_file())
            self.assertTrue((output / "modules" / "active-activity" / "CONTRACT.md").is_file())
            self.assertTrue((output / "modules" / "widgets" / "CONTRACT.md").is_file())
            self.assertTrue((output / "docs" / "ux" / "interactions" / "BUTTONS.md").is_file())
            self.assertTrue((output / "docs" / "ux" / "interactions" / "MENUS.md").is_file())
            self.assertTrue((output / "docs" / "ux" / "interactions" / "RENDERING.md").is_file())
            self.assertTrue((output / "docs" / "ux" / "patterns" / "ONBOARDING.md").is_file())
            self.assertTrue((output / "docs" / "ux" / "patterns" / "PERMISSIONS.md").is_file())
            self.assertTrue((output / "docs" / "ux" / "patterns" / "SETTINGS-AND-HELP.md").is_file())
            self.assertTrue((output / "docs" / "design" / "APP-ICON.md").is_file())
            self.assertTrue((output / "docs" / "design" / "NATIVE-REVIEW.md").is_file())
            self.assertTrue((output / "docs" / "compatibility" / "REVIEW.md").is_file())
            self.assertTrue((output / "docs" / "compatibility" / "IPHONE-DUO.md").is_file())
            self.assertIn("current scene or container", (output / "docs" / "compatibility" / "IPHONE-DUO.md").read_text())
            self.assertIn("Adaptive iPhone", (output / "docs" / "quality" / "TEST-MATRIX.md").read_text())
            self.assertTrue((output / "design" / "icon-brief.json").is_file())
            self.assertTrue((output / "tools" / "icon_plan.py").is_file())
            self.assertTrue((output / "tools" / "readiness.py").is_file())
            self.assertTrue((output / "Makefile").is_file())
            self.assertFalse((output / "platforms" / "tvos").exists())
            self.assertFalse((output / "tooling").exists())
            self.assertIn("paired Watch", (output / "modules" / "active-activity" / "CONTRACT.md").read_text())
            self.assertIn("separate module", (output / "modules" / "active-activity" / "CONTRACT.md").read_text())
            manifest = json.loads((output / ".apple-scaffold.json").read_text())
            self.assertEqual(manifest["selection"], json.loads(EXAMPLE.read_text()))
            self.assertEqual(json.loads((output / "design" / "icon-brief.json").read_text())["product_promise"], "")
            guide = (output / "docs" / "TROUBLESHOOTING.md").read_text()
            self.assertIn("Liquid Glass is hard to read", guide)
            self.assertIn("slow or hot on another", guide)
            self.assertIn("Duo opens or closes", guide)
            self.assertIn("Live Activity does not appear", guide)
            self.assertIn("iPhone activity does not look right on Apple Watch", guide)
            self.assertIn("Widget is missing or refreshes later than expected", guide)
            self.assertNotIn("Purchase succeeds", guide)
            self.assertNotIn("Apple TV navigation", guide)

    def test_troubleshooting_cli_filters_for_different_selection(self):
        config = json.loads(EXAMPLE.read_text())
        config["platforms"] = ["macos"]
        config["modules"] = ["commerce"]
        with tempfile.TemporaryDirectory() as directory:
            selection = Path(directory) / "selection.json"
            output = Path(directory) / "guide.md"
            selection.write_text(json.dumps(config))
            result = subprocess.run(
                [sys.executable, str(TROUBLESHOOT), "--config", str(selection), "--output", str(output)],
                cwd=ROOT, capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            guide = output.read_text()
            self.assertIn("Purchase succeeds", guide)
            self.assertNotIn("Live Activity does not appear", guide)
            self.assertNotIn("Duo opens or closes", guide)

    def test_agent_map_only_lists_selected_profiles_and_existing_paths(self):
        config = json.loads(EXAMPLE.read_text())
        config["platforms"] = ["macos"]
        config["modules"] = []
        with tempfile.TemporaryDirectory() as directory:
            selection = Path(directory) / "selection.json"
            output = Path(directory) / "generated"
            selection.write_text(json.dumps(config))
            result = invoke("generate", "--config", selection, "--output", output)
            self.assertEqual(result.returncode, 0, result.stderr)
            navigation = (output / "docs" / "agents" / "NAVIGATION.md").read_text()
            self.assertIn("platforms/macos/PROFILE.md", navigation)
            self.assertIn("None selected; add a capability", navigation)
            self.assertNotIn("platforms/ios/PROFILE.md", navigation)
            self.assertNotIn("modules/widgets/CONTRACT.md", navigation)
            self.assertNotIn("IPHONE-DUO.md", navigation)
            self.assertTrue((output / "platforms" / "macos" / "PROFILE.md").is_file())
            self.assertFalse((output / "docs" / "compatibility" / "IPHONE-DUO.md").exists())
            self.assertNotIn("Adaptive iPhone", (output / "docs" / "quality" / "TEST-MATRIX.md").read_text())

    def test_icon_plan_requires_product_and_generates_concept_directions(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "generated"
            result = invoke("generate", "--config", EXAMPLE, "--output", output)
            self.assertEqual(result.returncode, 0, result.stderr)
            brief = output / "design" / "icon-brief.json"
            plan = output / "docs" / "design" / "ICON-PLAN.md"
            command = [sys.executable, str(output / "tools" / "icon_plan.py"), "--brief", str(brief), "--output", str(plan)]
            result = subprocess.run(command, cwd=output, capture_output=True, text=True, check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(plan.exists())
            data = json.loads(brief.read_text())
            data["product_promise"] = "Help people finish a recurring task"
            data["visual_motifs"] = ["path", "spark"]
            brief.write_text(json.dumps(data))
            result = subprocess.run(command, cwd=output, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            text = plan.read_text()
            self.assertIn("Single symbol", text)
            self.assertIn("Relationship", text)
            self.assertIn("Distinctive geometry", text)
            self.assertIn("not final app assets", text)
            data["identity"] = ["playful-kinetic"]
            brief.write_text(json.dumps(data))
            malformed = subprocess.run(command, cwd=output, capture_output=True, text=True, check=False)
            self.assertEqual(malformed.returncode, 1)
            self.assertIn("Unknown identity", malformed.stderr)
            self.assertNotIn("Traceback", malformed.stderr)

    def test_generated_project_checks_itself(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "generated"
            result = invoke("generate", "--config", EXAMPLE, "--output", output)
            self.assertEqual(result.returncode, 0, result.stderr)
            checker = output / "tools" / "readiness.py"
            result = subprocess.run([sys.executable, str(checker)], cwd=output, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Structure: PASS", result.stdout)
            self.assertIn("Gates: 0 of 8 done", result.stdout)
            self.assertIn("Next: product-brief", result.stdout)
            strict = subprocess.run([sys.executable, str(checker), "--strict"], cwd=output, capture_output=True, text=True)
            self.assertEqual(strict.returncode, 1)
            gates_path = output / "docs" / "quality" / "gates.json"
            gates = json.loads(gates_path.read_text())
            gates["gates"][0]["status"] = "done"
            gates_path.write_text(json.dumps(gates))
            unproven = subprocess.run([sys.executable, str(checker)], cwd=output, capture_output=True, text=True)
            self.assertEqual(unproven.returncode, 2)
            self.assertIn("done needs at least one evidence path", unproven.stdout)
            gates["gates"][0]["evidence"] = ["docs/product/BRIEF.md"]
            gates_path.write_text(json.dumps(gates))
            proven = subprocess.run([sys.executable, str(checker)], cwd=output, capture_output=True, text=True)
            self.assertEqual(proven.returncode, 0, proven.stdout)
            self.assertIn("Gates: 1 of 8 done", proven.stdout)
            (output / "docs" / "ux" / "FLOWS.md").unlink()
            broken = subprocess.run([sys.executable, str(checker)], cwd=output, capture_output=True, text=True)
            self.assertEqual(broken.returncode, 2)
            self.assertIn("Missing docs/ux/FLOWS.md", broken.stdout)

    def test_rejects_invalid_selections(self):
        base = json.loads(EXAMPLE.read_text())
        cases = (
            {**base, "identity": "unknown"},
            {**base, "identity": ["playful-kinetic"]},
            {**base, "platforms": ["ios", "ios"]},
            {**base, "platforms": ["watchos"]},
            {**base, "platforms": ["tvos"], "modules": ["widgets"]},
            {**base, "unexpected": True},
            {**base, "project": {"name": "Neutral Preview", "slug": "../escape"}},
        )
        with tempfile.TemporaryDirectory() as directory:
            for index, config in enumerate(cases):
                with self.subTest(index=index):
                    path = Path(directory) / f"case-{index}.json"
                    path.write_text(json.dumps(config))
                    result = invoke("validate", "--config", path)
                    self.assertNotEqual(result.returncode, 0)

    def test_does_not_overwrite_nonempty_target(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "generated"
            output.mkdir()
            marker = output / "keep.txt"
            marker.write_text("untouched")
            result = invoke("generate", "--config", EXAMPLE, "--output", output)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(), "untouched")

    def test_same_selection_has_deterministic_contents(self):
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first"
            second = Path(directory) / "second"
            for output in (first, second):
                result = invoke("generate", "--config", EXAMPLE, "--output", output)
                self.assertEqual(result.returncode, 0, result.stderr)
            def files(root):
                return {str(path.relative_to(root)): path.read_bytes() for path in root.rglob("*") if path.is_file()}
            self.assertEqual(files(first), files(second))


    def test_ios_starter_renders_a_runnable_project(self):
        config = json.loads(EXAMPLE.read_text())
        config["project"]["name"] = 'Say "Hi"'
        with tempfile.TemporaryDirectory() as directory:
            selection = Path(directory) / "selection.json"
            selection.write_text(json.dumps(config))
            output = Path(directory) / "generated"
            result = invoke("generate", "--config", selection, "--output", output, "--starter", "ios")
            self.assertEqual(result.returncode, 0, result.stderr)
            project = (output / "App.xcodeproj" / "project.pbxproj").read_text()
            self.assertIn("name = NeutralPreview;", project)
            self.assertIn("SWIFT_VERSION = 6.0;", project)
            self.assertIn('TARGETED_DEVICE_FAMILY = "1,2";', project)
            self.assertIn('INFOPLIST_KEY_CFBundleDisplayName = "Say \\"Hi\\"";', project)
            self.assertIn('.navigationTitle("Say \\"Hi\\"")', (output / "App" / "ContentView.swift").read_text())
            self.assertIn("@testable import NeutralPreview", (output / "AppTests" / "FirstTaskTests.swift").read_text())
            self.assertTrue(os.access(output / "scripts" / "simulator.sh", os.X_OK))
            for path in output.rglob("*"):
                if path.is_file() and path.suffix in {".swift", ".pbxproj", ".sh", ".mk"}:
                    self.assertNotIn("{{", path.read_text(), path)
            self.assertEqual(json.loads((output / ".apple-scaffold.json").read_text())["starter"], "ios")
            self.assertTrue((output / ".github" / "workflows" / "app-tests.yml").is_file())
            checker = subprocess.run([sys.executable, str(output / "tools" / "readiness.py")], cwd=output, capture_output=True, text=True)
            self.assertEqual(checker.returncode, 0, checker.stdout)

    def test_ios_starter_needs_an_ios_platform(self):
        config = json.loads(EXAMPLE.read_text())
        config["platforms"] = ["macos"]
        config["modules"] = []
        with tempfile.TemporaryDirectory() as directory:
            selection = Path(directory) / "selection.json"
            selection.write_text(json.dumps(config))
            result = invoke("generate", "--config", selection, "--output", Path(directory) / "out", "--starter", "ios")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("needs iOS or iPadOS", result.stderr)

    @unittest.skipUnless(os.environ.get("APP_WORKSHOP_XCODE") == "1", "set APP_WORKSHOP_XCODE=1 to build and test in Simulator")
    def test_ios_starter_passes_its_tests_in_simulator(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "generated"
            self.assertEqual(invoke("generate", "--config", EXAMPLE, "--output", output, "--starter", "ios").returncode, 0)
            result = subprocess.run(["make", "test"], cwd=output, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_dogfood_matches_the_factory(self):
        # The dogfood app is a committed factory output. Files it owns are listed as "unmanaged" in its manifest.
        result = invoke("update", "--project", ROOT / "dogfood" / "app-workshop")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Would apply 0 change(s); 0 conflict(s)", result.stdout,
                      "dogfood drifted from the factory: run make update PROJECT=dogfood/app-workshop APPLY=1, "
                      "or add a file the app owns to unmanaged in its .apple-scaffold.json\n" + result.stdout)
        self.assertNotRegex(result.stdout, r"(?m)^retired")

    def test_update_replaces_only_unedited_files(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "generated"
            self.assertEqual(invoke("generate", "--config", EXAMPLE, "--output", output).returncode, 0)
            manifest_path = output / ".apple-scaffold.json"
            manifest = json.loads(manifest_path.read_text())
            # An older factory wrote this file and the builder never touched it.
            stale = output / "docs" / "OPERATING-SYSTEM.md"
            stale.write_text("old factory text\n")
            manifest["files"]["docs/OPERATING-SYSTEM.md"] = hashlib.sha256(stale.read_bytes()).hexdigest()
            manifest["files"]["docs/RETIRED.md"] = "0" * 64
            manifest_path.write_text(json.dumps(manifest))
            edited = output / "docs" / "product" / "BRIEF.md"
            edited.write_text("The builder's real brief\n")
            (output / "docs" / "ux" / "STATES.md").unlink()

            dry = invoke("update", "--project", output)
            self.assertEqual(dry.returncode, 0, dry.stderr)
            self.assertIn("update    docs/OPERATING-SYSTEM.md", dry.stdout)
            self.assertIn("conflict  docs/product/BRIEF.md", dry.stdout)
            self.assertIn("add       docs/ux/STATES.md", dry.stdout)
            self.assertIn("retired   docs/RETIRED.md", dry.stdout)
            self.assertEqual(stale.read_text(), "old factory text\n")

            applied = invoke("update", "--project", output, "--apply")
            self.assertEqual(applied.returncode, 0, applied.stderr)
            self.assertNotEqual(stale.read_text(), "old factory text\n")
            self.assertTrue((output / "docs" / "ux" / "STATES.md").is_file())
            self.assertEqual(edited.read_text(), "The builder's real brief\n")
            again = invoke("update", "--project", output)
            self.assertIn("Would apply 0 change(s); 1 conflict(s)", again.stdout)


    def test_check_fails_on_tracked_signing_assets(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "generated"
            self.assertEqual(invoke("generate", "--config", EXAMPLE, "--output", output).returncode, 0)
            self.assertTrue((output / ".github" / "pull_request_template.md").is_file())
            self.assertTrue((output / ".github" / "workflows" / "ci.yml").is_file())
            self.assertFalse((output / ".github" / "workflows" / "app-tests.yml").exists())
            git = lambda *args: subprocess.run(["git", "-C", str(output), *args], capture_output=True, check=True)
            git("init", "-q")
            (output / ".env.example").write_text("TOKEN=\n")
            (output / "AuthKey_TEST.p8").write_text("not a real key\n")
            git("add", "-A")
            git("add", "-f", "AuthKey_TEST.p8")
            checker = [sys.executable, str(output / "tools" / "readiness.py")]
            result = subprocess.run(checker, cwd=output, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2, result.stdout)
            self.assertIn("tracked by Git: AuthKey_TEST.p8", result.stdout)
            self.assertNotIn(".env.example", result.stdout)
            git("rm", "-q", "--cached", "AuthKey_TEST.p8")
            clean = subprocess.run(checker, cwd=output, capture_output=True, text=True)
            self.assertEqual(clean.returncode, 0, clean.stdout)
            pasted = output / "pasted-credentials.txt"
            pasted.write_text("prose mentioning sk_ is harmless\npublic appl_example_key\n")
            git("add", "pasted-credentials.txt")
            self.assertEqual(subprocess.run(checker, cwd=output, capture_output=True, text=True).returncode, 0)
            pasted.write_text("-----BEGIN PRIVATE KEY-----\nfake test fixture\n")
            leaked_pem = subprocess.run(checker, cwd=output, capture_output=True, text=True)
            self.assertEqual(leaked_pem.returncode, 2, leaked_pem.stdout)
            self.assertIn("tracked by Git: pasted-credentials.txt", leaked_pem.stdout)
            pasted.write_text("sk_abcdefghijklmnopqrstuvwxyz123456\n")
            leaked_token = subprocess.run(checker, cwd=output, capture_output=True, text=True)
            self.assertEqual(leaked_token.returncode, 2, leaked_token.stdout)
            self.assertIn("tracked by Git: pasted-credentials.txt", leaked_token.stdout)

    def test_adopt_adds_the_layer_without_touching_the_app(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / "existing"
            (project / "Sources").mkdir(parents=True)
            (project / "Sources" / "main.swift").write_text("print(1)\n")
            (project / "README.md").write_text("# Existing app\n")
            (project / "Makefile").write_text("build:\n\ttrue\n")
            (project / "AGENTS.md").write_text("# Existing rules\nKeep this.\n")
            result = invoke("adopt", "--config", EXAMPLE, "--project", project)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((project / "README.md").read_text(), "# Existing app\n")
            self.assertEqual((project / "Sources" / "main.swift").read_text(), "print(1)\n")
            agents = (project / "AGENTS.md").read_text()
            self.assertTrue(agents.startswith("# Existing rules\nKeep this.\n"))
            self.assertIn("## App Workshop operating layer", agents)
            self.assertTrue((project / "docs" / "product" / "BRIEF.md").is_file())
            self.assertFalse((project / "App.xcodeproj").exists())
            manifest = json.loads((project / ".apple-scaffold.json").read_text())
            self.assertEqual(manifest["unmanaged"], ["AGENTS.md", "Makefile", "README.md"])
            self.assertNotIn("AGENTS.md", manifest["files"])
            update = invoke("update", "--project", project)
            self.assertIn("Would apply 0 change(s); 0 conflict(s)", update.stdout)
            again = invoke("adopt", "--config", EXAMPLE, "--project", project)
            self.assertNotEqual(again.returncode, 0)
            self.assertIn("use update", again.stderr)

    def test_adopt_writes_nothing_on_conflict(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / "existing"
            (project / "docs" / "product").mkdir(parents=True)
            (project / "docs" / "product" / "BRIEF.md").write_text("mine\n")
            result = invoke("adopt", "--config", EXAMPLE, "--project", project)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("docs/product/BRIEF.md", result.stderr)
            self.assertEqual(sorted(path.relative_to(project).as_posix() for path in project.rglob("*") if path.is_file()),
                             ["docs/product/BRIEF.md"])


if __name__ == "__main__":
    unittest.main()
