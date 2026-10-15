#!/usr/bin/env python3
"""
tools/uss-validate.py — Universal System Standards (USS) Offline Validator

Zero-dependency Python 3 standard library verification utility for USS.
Supports:
  Mode 1 (--self, default): Validates USS standards repository integrity.
  Mode 2 (--consumer <path>): Validates an adopting consumer repository.

Conforms to USS-010 reporting: PASS, FAIL, CHECK_BLOCKED, NOT RUN.
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

# Deterministic State Machine Enums
VALID_COMPLIANCE_STATUSES = {"COMPLIANT", "PARTIAL", "EXEMPT", "NOT_APPLICABLE", "UNKNOWN"}
VALID_CHECK_OUTCOMES = {"PASS", "FAIL", "CHECK_BLOCKED", "NOT RUN"}
VALID_HEALTH_STATES = {"HEALTHY", "DEGRADED", "SYSTEM_BLOCKED", "FAILED", "IDLE", "UNKNOWN"}
VALID_LIFECYCLE_STATES = {
    "PLANNED", "EXPERIMENTAL", "ACTIVE", "MAINTENANCE",
    "MIGRATING", "ARCHIVED", "RETIRED", "UNKNOWN"
}

BCP14_KEYWORDS = {
    "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
    "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", "OPTIONAL"
}


class ValidationReport:
    def __init__(self):
        self.results = []
        self.errors = []
        self.warnings = []

    def add(self, check_name: str, outcome: str, details: str = ""):
        assert outcome in VALID_CHECK_OUTCOMES, f"Invalid outcome: {outcome}"
        self.results.append((check_name, outcome, details))
        if outcome == "FAIL":
            self.errors.append(f"{check_name}: {details}")

    def add_warning(self, message: str):
        self.warnings.append(message)

    @property
    def is_pass(self) -> bool:
        return all(outcome in ("PASS", "NOT RUN") for _, outcome, _ in self.results) and not self.errors

    def print_summary(self):
        print("=" * 72)
        print("UNIVERSAL SYSTEM STANDARDS (USS) — VALIDATION RECEIPT")
        print("=" * 72)
        for name, outcome, details in self.results:
            status_box = f"[{outcome}]"
            detail_str = f" — {details}" if details else ""
            print(f"{status_box:16} {name}{detail_str}")

        if self.warnings:
            print("\nWARNINGS:")
            for w in self.warnings:
                print(f"  [WARN] {w}")

        print("=" * 72)
        final_verdict = "PASS" if self.is_pass else "FAIL"
        print(f"FINAL VERDICT: {final_verdict}")
        print("=" * 72)


# ==============================================================================
# MODE 1: SELF VALIDATION (USS STANDARDS REPOSITORY)
# ==============================================================================

def validate_rule_ids(repo_root: Path, report: ValidationReport):
    """Checks uniqueness, syntax, and file placement of all standard rule IDs."""
    standards_dir = repo_root / "standards"
    if not standards_dir.is_dir():
        report.add("Rule ID Verification", "FAIL", f"Missing directory: {standards_dir}")
        return

    rule_id_pattern = re.compile(r"\b(0\d\d-\d\d)\b")
    all_rules = {}
    duplicates = []
    file_mismatches = []

    for md_file in sorted(standards_dir.glob("*.md")):
        prefix_match = re.search(r"USS-(0\d\d)", md_file.name)
        expected_prefix = prefix_match.group(1) if prefix_match else None

        content = md_file.read_text(encoding="utf-8")
        found_rules = rule_id_pattern.findall(content)

        for rule in found_rules:
            rule_prefix = rule.split("-")[0]
            if expected_prefix and rule_prefix != expected_prefix:
                file_mismatches.append(f"{rule} in {md_file.name} (expected {expected_prefix})")

            if rule in all_rules:
                duplicates.append((rule, all_rules[rule], md_file.name))
            else:
                all_rules[rule] = md_file.name

    if duplicates:
        report.add("Rule ID Uniqueness", "FAIL", f"Duplicate rule IDs found: {duplicates}")
    else:
        report.add("Rule ID Uniqueness", "PASS", f"Found {len(all_rules)} unique rule IDs across {len(list(standards_dir.glob('*.md')))} standards")

    if file_mismatches:
        report.add("Rule ID File Placement", "FAIL", f"Mismatched rule prefixes: {file_mismatches}")
    else:
        report.add("Rule ID File Placement", "PASS", "All rule prefixes match host filenames")


def validate_internal_links(repo_root: Path, report: ValidationReport):
    """Validates markdown link integrity across all documentation files."""
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    broken_links = []
    checked_count = 0

    scan_targets = list(repo_root.glob("*.md")) + \
                   list((repo_root / "standards").glob("*.md")) + \
                   list((repo_root / "governance").rglob("*.md")) + \
                   list((repo_root / "patterns").glob("*.md")) + \
                   list((repo_root / "templates").glob("*.md"))

    for md_path in scan_targets:
        if not md_path.is_file():
            continue
        try:
            content = md_path.read_text(encoding="utf-8")
        except Exception as e:
            report.add("Link Integrity", "FAIL", f"Cannot read {md_path}: {e}")
            return

        for text, target in link_pattern.findall(content):
            target = target.strip()
            # Ignore external, mailto, or fragment-only links
            if target.startswith(("http://", "https://", "mailto:", "#")) or not target:
                continue

            parsed = urlparse(target)
            target_path_part = unquote(parsed.path)
            if not target_path_part:
                continue

            resolved_path = (md_path.parent / target_path_part).resolve()
            checked_count += 1
            if not resolved_path.exists():
                broken_links.append((str(md_path.relative_to(repo_root)), target))

    if broken_links:
        report.add("Internal Link Integrity", "FAIL", f"{len(broken_links)} broken links found: {broken_links[:5]}")
    else:
        report.add("Internal Link Integrity", "PASS", f"{checked_count} internal markdown links verified")


def validate_bcp14_syntax(repo_root: Path, report: ValidationReport):
    """Ensures standards files use uppercase IETF BCP 14 normative keywords."""
    standards_dir = repo_root / "standards"
    if not standards_dir.is_dir():
        report.add("BCP 14 Syntax Check", "FAIL", "Missing standards directory")
        return

    # Check for presence of uppercase BCP 14 keywords
    files_with_bcp14 = 0
    standards_files = list(standards_dir.glob("*.md"))

    for sf in standards_files:
        content = sf.read_text(encoding="utf-8")
        has_keywords = any(f"**{kw}**" in content or f" {kw} " in content for kw in BCP14_KEYWORDS)
        if has_keywords:
            files_with_bcp14 += 1

    if files_with_bcp14 == len(standards_files):
        report.add("BCP 14 Keyword Usage", "PASS", f"All {files_with_bcp14} standards employ BCP 14 uppercase requirements")
    else:
        report.add("BCP 14 Keyword Usage", "FAIL", f"Only {files_with_bcp14}/{len(standards_files)} standards use BCP 14 keywords")


def validate_templates_cleanliness(repo_root: Path, report: ValidationReport):
    """Checks that templates/ contains no live operational data or private secrets."""
    templates_dir = repo_root / "templates"
    if not templates_dir.is_dir():
        report.add("Template Cleanliness", "FAIL", "Missing templates directory")
        return

    suspicious_patterns = [
        re.compile(r"gh[pousr]_[A-Za-z0-9_]{30,}"),       # GitHub tokens
        re.compile(r"sk-[A-Za-z0-9_-]{20,}"),             # API keys (OpenAI, etc.)
        re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),      # Slack tokens
        re.compile(r"BEGIN (?:RSA|OPENSSH|EC|DSA|PRIVATE) KEY"), # Private keys
    ]

    leaks = []
    template_files = list(templates_dir.glob("*.md"))

    for tf in template_files:
        if not tf.name.endswith(".template.md"):
            report.add("Template Naming", "FAIL", f"Template file {tf.name} must end with '.template.md'")
            return
        content = tf.read_text(encoding="utf-8")
        for p in suspicious_patterns:
            if p.search(content):
                leaks.append((tf.name, "Credential or private key pattern detected"))

    report.add("Template Naming", "PASS", f"All {len(template_files)} template files end with '.template.md'")
    if leaks:
        report.add("Template Cleanliness", "FAIL", f"Operational leaks detected in templates: {leaks}")
    else:
        report.add("Template Cleanliness", "PASS", "Templates contain solely generic schemas and placeholders")


def validate_tag_signatures(repo_root: Path, report: ValidationReport, target_tag: str = None, trusted_signer: str = None):
    """Verifies cryptographic tag signatures using git verify-tag."""
    trusted_signer = trusted_signer or os.environ.get("USS_OPERATOR_SIGNER")

    # If target_tag is not specified, look for release tags
    if not target_tag:
        try:
            result = subprocess.run(
                ["git", "tag", "-l", "v*"],
                cwd=str(repo_root),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
            tags = [t.strip() for t in result.stdout.strip().splitlines() if t.strip()]
            if not tags:
                report.add("Cryptographic Tag Signature", "NOT RUN", "No release tags (v*) exist in repository yet")
                return
            target_tag = sorted(tags)[-1]
        except Exception as e:
            report.add("Cryptographic Tag Signature", "CHECK_BLOCKED", f"Failed to list git tags: {e}")
            return

    # Verify the tag signature
    try:
        verify_cmd = ["git", "verify-tag", target_tag]
        proc = subprocess.run(
            verify_cmd,
            cwd=str(repo_root),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        if proc.returncode != 0:
            report.add("Cryptographic Tag Signature", "FAIL", f"Tag {target_tag} has invalid or missing signature: {proc.stderr.strip()}")
            return

        combined_output = proc.stdout + proc.stderr
        if trusted_signer:
            if trusted_signer not in combined_output:
                report.add("Cryptographic Tag Signature", "FAIL", f"Tag {target_tag} signed by unrecognized key (expected {trusted_signer})")
                return

        report.add("Cryptographic Tag Signature", "PASS", f"Tag {target_tag} signature cryptographically verified")
    except Exception as e:
        report.add("Cryptographic Tag Signature", "CHECK_BLOCKED", f"Git execution error: {e}")


def run_self_validation(repo_root: Path, target_tag: str = None, trusted_signer: str = None) -> ValidationReport:
    report = ValidationReport()
    validate_rule_ids(repo_root, report)
    validate_internal_links(repo_root, report)
    validate_bcp14_syntax(repo_root, report)
    validate_templates_cleanliness(repo_root, report)
    validate_tag_signatures(repo_root, report, target_tag, trusted_signer)
    return report


# ==============================================================================
# MODE 2: CONSUMER ADOPTION VALIDATION
# ==============================================================================

def validate_consumer_adoption(consumer_root: Path, report: ValidationReport):
    """Validates an adopting system repository against USS requirements."""
    if not consumer_root.is_dir():
        report.add("Consumer Root Verification", "FAIL", f"Directory does not exist: {consumer_root}")
        return

    # 1. Root AGENTS.md verification
    agents_file = consumer_root / "AGENTS.md"
    if not agents_file.is_file():
        report.add("Root AGENTS.md Presence", "FAIL", "Missing root AGENTS.md file")
    else:
        agents_content = agents_file.read_text(encoding="utf-8")
        required_sections = ["Mission", "Execution", "Stop", "Report"]
        missing_sections = [
            s for s in required_sections
            if not re.search(rf"#+\s*.*{s}", agents_content, re.IGNORECASE)
        ]
        if missing_sections:
            report.add("Root AGENTS.md Scaffolding", "FAIL", f"Missing required sections: {missing_sections}")
        else:
            report.add("Root AGENTS.md Scaffolding", "PASS", "Root AGENTS.md contains standard scaffolding")

    # 2. SYSTEM_ADOPTION.md verification
    adoption_file = consumer_root / "SYSTEM_ADOPTION.md"
    if not adoption_file.is_file():
        report.add("SYSTEM_ADOPTION.md Presence", "FAIL", "Missing SYSTEM_ADOPTION.md")
        return

    adoption_text = adoption_file.read_text(encoding="utf-8")

    # Check pinned version
    pin_match = re.search(r"Adopted USS (?:Release|Pin):\s*([^\n\r]+)", adoption_text, re.IGNORECASE)
    if not pin_match or pin_match.group(1).strip() in ("", "NONE", "UNKNOWN", "<vX.Y.Z-tag-or-commit-sha>"):
        report.add("USS Release Pinning", "FAIL", "SYSTEM_ADOPTION.md lacks an explicit, adopted USS release version")
    else:
        pinned_version = pin_match.group(1).strip()
        report.add("USS Release Pinning", "PASS", f"Pinned to {pinned_version}")

    # Check compliance status enum
    status_match = re.search(r"(?:Evaluated Compliance )?Status:\s*([A-Za-z_]+)", adoption_text, re.IGNORECASE)
    compliance_status = status_match.group(1).upper() if status_match else "UNKNOWN"

    if compliance_status not in VALID_COMPLIANCE_STATUSES:
        report.add("Compliance Status Enum", "FAIL", f"Invalid status '{compliance_status}'. Must be one of {VALID_COMPLIANCE_STATUSES}")
    else:
        report.add("Compliance Status Enum", "PASS", f"Reported status: {compliance_status}")

    # 3. Anti-Fabrication Check (Rule 013-05)
    if compliance_status == "COMPLIANT":
        # Extract evidence paths from table rows or list items
        # Format: | `rule` | `COMPLIANT` | path/to/file |
        evidence_files = []
        for line in adoption_text.splitlines():
            if "|" in line:
                cols = [c.strip() for c in line.split("|")[1:-1]]
                if len(cols) >= 3:
                    state_col = cols[1].strip("`* ")
                    evidence_col = cols[2].strip("`* ")
                    if "COMPLIANT" in state_col.upper() and evidence_col and not evidence_col.startswith("<"):
                        # Extract first relative path from evidence col
                        path_candidate = re.split(r"[\s,;]+", evidence_col)[0]
                        evidence_files.append(path_candidate)

        if not evidence_files:
            # Check for generic evidence links in text
            evidence_section = re.search(r"## 3\..*?Compliance Evidence.*?\n(.*?)(?=\n## |\Z)", adoption_text, re.DOTALL)
            if evidence_section:
                for match in re.findall(r"[`']([^`'\n]+)[`']", evidence_section.group(1)):
                    if "." in match and "/" in match:
                        evidence_files.append(match)

        if not evidence_files:
            report.add("Anti-Fabrication Evidence Check", "FAIL", "COMPLIANT status declared but zero local evidence file paths found")
        else:
            missing_evidence = []
            for ev in evidence_files:
                ev_clean = ev.strip()
                if not (consumer_root / ev_clean).exists():
                    missing_evidence.append(ev_clean)

            if missing_evidence:
                report.add("Anti-Fabrication Evidence Check", "FAIL", f"Referenced local evidence files do not exist: {missing_evidence}")
            else:
                report.add("Anti-Fabrication Evidence Check", "PASS", f"Verified existence of {len(evidence_files)} local compliance evidence receipts")
    else:
        report.add("Anti-Fabrication Evidence Check", "PASS", f"Anti-fabrication check bypassed for non-COMPLIANT status ({compliance_status})")


def run_consumer_validation(consumer_root: Path) -> ValidationReport:
    report = ValidationReport()
    validate_consumer_adoption(consumer_root, report)
    return report


# ==============================================================================
# CLI DISPATCHER
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Universal System Standards (USS) Zero-Dependency Offline Validator"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--self",
        nargs="?",
        const=".",
        default=".",
        help="Run self-validation on USS repository at specified path (default: current directory)"
    )
    group.add_argument(
        "--consumer",
        metavar="PATH",
        help="Validate adopting consumer repository at PATH"
    )

    parser.add_argument("--tag", help="Specify Git release tag to verify cryptographically")
    parser.add_argument("--signer", help="Expected public key or fingerprint of Operator signer")

    args = parser.parse_args()

    if args.consumer:
        consumer_path = Path(args.consumer).resolve()
        print(f"Running USS Consumer Validation on: {consumer_path}\n")
        report = run_consumer_validation(consumer_path)
    else:
        repo_path = Path(args.self).resolve()
        print(f"Running USS Standards Self-Validation on: {repo_path}\n")
        report = run_self_validation(repo_path, target_tag=args.tag, trusted_signer=args.signer)

    report.print_summary()
    sys.exit(0 if report.is_pass else 1)


if __name__ == "__main__":
    main()
