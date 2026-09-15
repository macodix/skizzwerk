import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("inventory", ROOT / "tools" / "inventory.py")
inventory = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(inventory)


def valid_data():
    return {
        "schema_version": 1,
        "metadata": {
            "document": "inventory", "process_phase": "swk-02",
            "project": "example", "status": "draft",
            "created": "2026-09-15", "last_updated": "2026-09-15",
            "basis": "idea.md",
        },
        "assignment": "Bestand untersuchen",
        "scope": [{"area": "Plugins", "idea_reference": "idea.md Abschnitt 1", "relevance": "genannt"}],
        "investigation": [{"area": "Plugins", "examined": ["README"], "not_examined": [], "limitations": []}],
        "limitations": [],
        "review": {"precheck_passed": False, "quality_gate_passed": False,
                   "checked_at": None, "checked_by": None,
                   "unmet_criteria": [], "blockage": None},
        "approval": None,
        "findings": [{
            "id": "evd-001", "statement": "README nennt MUC",
            "evidence_status": "DOCUMENTED", "status_reason": "README-Angabe",
            "sources": [{"type": "PROJECT_DOCUMENTATION", "location": "README.md",
                         "version": "Commit abc123", "checked_at": "2026-09-15",
                         "contribution": "Funktionsangabe"}],
            "verification": {"performed": ["README gelesen"], "result": "Angabe vorhanden",
                             "not_performed": ["Funktionstest"], "limitation": "nicht getestet"},
            "idea_reference": {"location": "idea.md Abschnitt 1", "significance": "MUC"},
            "conclusion": "Funktion ist dokumentiert",
        }],
    }


class InventoryTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual([], inventory.validate(valid_data()))

    def test_duplicate_identifier(self):
        data = valid_data()
        data["findings"].append(copy.deepcopy(data["findings"][0]))
        self.assertTrue(any("duplicate" in error for error in inventory.validate(data)))

    def test_verified_may_not_mix_project_documentation(self):
        data = valid_data()
        data["findings"][0]["evidence_status"] = "VERIFIED"
        self.assertTrue(any("may not mix" in error for error in inventory.validate(data)))

    def test_conflict_requires_fields_and_two_sources(self):
        data = valid_data()
        data["findings"][0]["evidence_status"] = "CONFLICT"
        errors = inventory.validate(data)
        self.assertTrue(any("at least two sources" in error for error in errors))
        self.assertTrue(any("conflict: object required" in error for error in errors))

    def test_non_conflict_rejects_conflict_data(self):
        data = valid_data()
        data["findings"][0]["conflict"] = {"statement_1": "a"}
        self.assertTrue(any("allowed only" in error for error in inventory.validate(data)))

    def test_renderer_escapes_table_separator(self):
        data = valid_data()
        data["findings"][0]["statement"] = "A | B"
        self.assertIn("A \\| B", inventory.render(data))

    def test_review_status_requires_successful_review(self):
        data = valid_data()
        data["metadata"]["status"] = "review"
        self.assertTrue(any("passed precheck" in error for error in inventory.validate(data)))

    def test_accepted_requires_human_approval(self):
        data = valid_data()
        data["metadata"]["status"] = "accepted"
        data["review"].update({"precheck_passed": True, "quality_gate_passed": True,
                               "checked_at": "2026-09-15", "checked_by": "validator"})
        self.assertTrue(any("approval: object required" in error for error in inventory.validate(data)))

    def test_cli_detects_manually_changed_markdown(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "inventory.json"
            output = Path(directory) / "inventory.md"
            source.write_text(json.dumps(valid_data()), encoding="utf-8")
            command = [sys.executable, str(ROOT / "tools" / "inventory.py")]
            subprocess.run(command + ["render", str(source), str(output)], check=True)
            subprocess.run(command + ["check", str(source), str(output)], check=True)
            output.write_text(output.read_text(encoding="utf-8") + "manuell\n", encoding="utf-8")
            changed = subprocess.run(command + ["check", str(source), str(output)], check=False)
            self.assertEqual(1, changed.returncode)


if __name__ == "__main__":
    unittest.main()
