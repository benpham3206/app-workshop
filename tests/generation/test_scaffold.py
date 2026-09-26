import json
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
            self.assertIn("Planning decisions still pending", result.stdout)
            strict = subprocess.run([sys.executable, str(checker), "--strict"], cwd=output, capture_output=True, text=True)
            self.assertEqual(strict.returncode, 1)
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


if __name__ == "__main__":
    unittest.main()
