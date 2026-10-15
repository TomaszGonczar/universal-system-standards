#!/usr/bin/env python3
"""
tools/test_validator.py — Test Suite for USS Offline Validator

Zero-dependency Python 3 standard library unit tests verifying:
  - Repository self-validation (positive and negative cases)
  - Consumer adoption validation (positive and negative cases)
  - Anti-fabrication evidence verification (Rule 013-05)
  - Cryptographic signature verification mechanics
"""

import os
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Import the validator module
import sys
sys.path.insert(0, str(Path(__file__).parent))
import importlib
uss_validate = importlib.import_module("uss-validate")


class TestSelfValidation(unittest.TestCase):
    """Tests for Mode 1: Self-Validation of the USS repository."""

    def setUp(self):
        self.repo_root = Path(__file__).parent.parent.resolve()

    def test_current_repo_passes_self_validation(self):
        """The actual USS repository must pass self-validation cleanly."""
        report = uss_validate.run_self_validation(self.repo_root)
        self.assertTrue(report.is_pass, f"Errors: {report.errors}")
        # Verify check names exist
        check_names = [name for name, _, _ in report.results]
        self.assertIn("Rule ID Uniqueness", check_names)
        self.assertIn("Internal Link Integrity", check_names)
        self.assertIn("BCP 14 Keyword Usage", check_names)
        self.assertIn("Template Cleanliness", check_names)

    def test_negative_duplicate_rule_id(self):
        """Duplicate rule IDs across standard files must fail."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            standards_dir = tmp / "standards"
            standards_dir.mkdir()

            (standards_dir / "USS-001-test.md").write_text("1. **001-01** — Rule 1 MUST be active.\n", encoding="utf-8")
            (standards_dir / "USS-002-test.md").write_text("1. **001-01** — Duplicate rule MUST fail.\n", encoding="utf-8")

            report = uss_validate.ValidationReport()
            uss_validate.validate_rule_ids(tmp, report)
            self.assertFalse(report.is_pass)
            self.assertTrue(any("Duplicate rule IDs found" in err for err in report.errors))

    def test_negative_rule_file_prefix_mismatch(self):
        """Rule prefix not matching host filename must fail."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            standards_dir = tmp / "standards"
            standards_dir.mkdir()

            (standards_dir / "USS-001-test.md").write_text("1. **002-05** — Mismatched rule MUST fail.\n", encoding="utf-8")

            report = uss_validate.ValidationReport()
            uss_validate.validate_rule_ids(tmp, report)
            self.assertFalse(report.is_pass)
            self.assertTrue(any("Mismatched rule prefixes" in err for err in report.errors))

    def test_negative_broken_internal_markdown_link(self):
        """Unresolvable local markdown links must fail."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            (tmp / "standards").mkdir()
            (tmp / "patterns").mkdir()
            (tmp / "templates").mkdir()
            (tmp / "governance").mkdir()

            (tmp / "README.md").write_text("See [Broken Link](nonexistent_doc.md) for details.\n", encoding="utf-8")

            report = uss_validate.ValidationReport()
            uss_validate.validate_internal_links(tmp, report)
            self.assertFalse(report.is_pass)
            self.assertTrue(any("broken links found" in err for err in report.errors))

    def test_negative_template_naming_and_secret_leak(self):
        """Templates not named .template.md or containing private keys must fail."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            templates_dir = tmp / "templates"
            templates_dir.mkdir()

            # Bad filename
            (templates_dir / "BAD_NAME.md").write_text("Generic schema\n", encoding="utf-8")
            report = uss_validate.ValidationReport()
            uss_validate.validate_templates_cleanliness(tmp, report)
            self.assertFalse(report.is_pass)
            self.assertTrue(any("must end with '.template.md'" in err for err in report.errors))

            # Secret pattern leak
            (templates_dir / "BAD_NAME.md").unlink()
            (templates_dir / "LEAK.template.md").write_text("Secret: sk-abcdef12345678901234567890123456789012345678\n", encoding="utf-8")
            report2 = uss_validate.ValidationReport()
            uss_validate.validate_templates_cleanliness(tmp, report2)
            self.assertFalse(report2.is_pass)
            self.assertTrue(any("Credential or private key pattern detected" in str(report2.results) for _ in [1]))


class TestConsumerValidation(unittest.TestCase):
    """Tests for Mode 2: Consumer Adoption Validation & Anti-Fabrication."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.consumer_root = Path(self.tmpdir)

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def create_valid_consumer_repo(self):
        # Create root AGENTS.md
        agents_content = """# Agent Instructions
## Mission
Execute tasks within bounded domain scope.
## Execution Boundaries
Enforce least privilege and deterministic state reporting.
## Stop Conditions
Halt when encountering L4 risk.
## Reporting Format
Report changed files and verification evidence.
"""
        (self.consumer_root / "AGENTS.md").write_text(agents_content, encoding="utf-8")

        # Create verifiable evidence file
        tests_dir = self.consumer_root / "tests"
        tests_dir.mkdir(parents=True, exist_ok=True)
        evidence_file = tests_dir / "test_verification.py"
        evidence_file.write_text("# Passing unit test\nassert True\n", encoding="utf-8")

        # Create SYSTEM_ADOPTION.md
        adoption_content = f"""# System Adoption Record
System ID: test-system
Adopted USS Release: v0.1.0
Status: COMPLIANT

## 3. Compliance Evidence
| Rule ID | Status | Local Evidence Path |
|---|---|---|
| `001-01` | `COMPLIANT` | tests/test_verification.py |
"""
        (self.consumer_root / "SYSTEM_ADOPTION.md").write_text(adoption_content, encoding="utf-8")

    def test_positive_consumer_adoption(self):
        """A properly structured adopting repository passes validation."""
        self.create_valid_consumer_repo()
        report = uss_validate.run_consumer_validation(self.consumer_root)
        self.assertTrue(report.is_pass, f"Errors: {report.errors}")

    def test_negative_missing_agents_file(self):
        """Missing root AGENTS.md must fail."""
        self.create_valid_consumer_repo()
        (self.consumer_root / "AGENTS.md").unlink()

        report = uss_validate.run_consumer_validation(self.consumer_root)
        self.assertFalse(report.is_pass)
        self.assertTrue(any("Missing root AGENTS.md file" in err for err in report.errors))

    def test_negative_agents_missing_required_scaffolding(self):
        """AGENTS.md without required sections must fail."""
        self.create_valid_consumer_repo()
        (self.consumer_root / "AGENTS.md").write_text("# Agent Instructions\nJust some text.\n", encoding="utf-8")

        report = uss_validate.run_consumer_validation(self.consumer_root)
        self.assertFalse(report.is_pass)
        self.assertTrue(any("Missing required sections" in err for err in report.errors))

    def test_negative_missing_system_adoption(self):
        """Missing SYSTEM_ADOPTION.md must fail."""
        self.create_valid_consumer_repo()
        (self.consumer_root / "SYSTEM_ADOPTION.md").unlink()

        report = uss_validate.run_consumer_validation(self.consumer_root)
        self.assertFalse(report.is_pass)
        self.assertTrue(any("Missing SYSTEM_ADOPTION.md" in err for err in report.errors))

    def test_negative_unpinned_uss_version(self):
        """Unpinned USS release version must fail."""
        self.create_valid_consumer_repo()
        bad_adoption = (self.consumer_root / "SYSTEM_ADOPTION.md").read_text(encoding="utf-8").replace("v0.1.0", "NONE")
        (self.consumer_root / "SYSTEM_ADOPTION.md").write_text(bad_adoption, encoding="utf-8")

        report = uss_validate.run_consumer_validation(self.consumer_root)
        self.assertFalse(report.is_pass)
        self.assertTrue(any("lacks an explicit, adopted USS release version" in err for err in report.errors))

    def test_negative_invalid_compliance_status_enum(self):
        """Invalid compliance status enum must fail."""
        self.create_valid_consumer_repo()
        bad_adoption = (self.consumer_root / "SYSTEM_ADOPTION.md").read_text(encoding="utf-8").replace("COMPLIANT", "ALMOST_DONE")
        (self.consumer_root / "SYSTEM_ADOPTION.md").write_text(bad_adoption, encoding="utf-8")

        report = uss_validate.run_consumer_validation(self.consumer_root)
        self.assertFalse(report.is_pass)
        self.assertTrue(any("Invalid status" in err for err in report.errors))

    def test_negative_anti_fabrication_nonexistent_evidence(self):
        """Rule 013-05: Claiming COMPLIANT with nonexistent evidence files must fail."""
        self.create_valid_consumer_repo()
        bad_adoption = (self.consumer_root / "SYSTEM_ADOPTION.md").read_text(encoding="utf-8").replace(
            "tests/test_verification.py", "tests/imaginary_proof.py"
        )
        (self.consumer_root / "SYSTEM_ADOPTION.md").write_text(bad_adoption, encoding="utf-8")

        report = uss_validate.run_consumer_validation(self.consumer_root)
        self.assertFalse(report.is_pass)
        self.assertTrue(any("Referenced local evidence files do not exist" in err for err in report.errors))

    def test_negative_anti_fabrication_zero_evidence_provided(self):
        """Rule 013-05: Claiming COMPLIANT without providing any local evidence must fail."""
        self.create_valid_consumer_repo()
        bad_adoption = """# System Adoption Record
System ID: test-system
Adopted USS Release: v0.1.0
Status: COMPLIANT
"""
        (self.consumer_root / "SYSTEM_ADOPTION.md").write_text(bad_adoption, encoding="utf-8")

        report = uss_validate.run_consumer_validation(self.consumer_root)
        self.assertFalse(report.is_pass)
        self.assertTrue(any("COMPLIANT status declared but zero local evidence file paths found" in err for err in report.errors))

    def test_positive_partial_status_bypasses_anti_fabrication(self):
        """A system marked PARTIAL is not required to have all evidence in place."""
        self.create_valid_consumer_repo()
        partial_adoption = """# System Adoption Record
System ID: test-system
Adopted USS Release: v0.1.0
Status: PARTIAL
"""
        (self.consumer_root / "SYSTEM_ADOPTION.md").write_text(partial_adoption, encoding="utf-8")

        report = uss_validate.run_consumer_validation(self.consumer_root)
        self.assertTrue(report.is_pass)


class TestCryptographicVerificationMechanics(unittest.TestCase):
    """Tests for tag signature verification logic."""

    @patch("subprocess.run")
    def test_valid_signed_tag_passes(self, mock_run):
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="Good signature from Operator <operator@system.local>\n",
            stderr=""
        )
        report = uss_validate.ValidationReport()
        uss_validate.validate_tag_signatures(Path("."), report, target_tag="v0.1.0", trusted_signer="operator@system.local")
        self.assertTrue(report.is_pass)

    @patch("subprocess.run")
    def test_unsigned_or_bad_tag_fails(self, mock_run):
        mock_run.return_value = MagicMock(
            returncode=1,
            stdout="",
            stderr="error: no signature found\n"
        )
        report = uss_validate.ValidationReport()
        uss_validate.validate_tag_signatures(Path("."), report, target_tag="v0.1.0")
        self.assertFalse(report.is_pass)
        self.assertTrue(any("invalid or missing signature" in err for err in report.errors))

    @patch("subprocess.run")
    def test_mismatched_signer_fails(self, mock_run):
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="Good signature from Impostor <impostor@rogue.local>\n",
            stderr=""
        )
        report = uss_validate.ValidationReport()
        uss_validate.validate_tag_signatures(Path("."), report, target_tag="v0.1.0", trusted_signer="operator@system.local")
        self.assertFalse(report.is_pass)
        self.assertTrue(any("signed by unrecognized key" in err for err in report.errors))


if __name__ == "__main__":
    unittest.main()
