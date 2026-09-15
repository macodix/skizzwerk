#!/usr/bin/env python3
"""Validate structured swk-02 inventory data and render Markdown."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

EVIDENCE_STATUSES = {
    "USER_PROVIDED", "VERIFIED", "DOCUMENTED", "INFERRED",
    "ASSUMED", "UNKNOWN", "CONFLICT", "DISPROVED",
}
SOURCE_TYPES = {
    "USER_STATEMENT", "SOURCE_CODE", "AUTOMATED_TEST", "MANUAL_TEST",
    "PRIMARY_DOCUMENTATION", "PROJECT_DOCUMENTATION", "ISSUE_OR_PR",
    "SECONDARY_SOURCE", "ANALYSIS", "NONE",
}
DOCUMENT_STATUSES = {"input", "draft", "review", "accepted", "blocked", "superseded"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
EVD_RE = re.compile(r"^evd-(\d{3,})$")


class ValidationError(Exception):
    pass


def load(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(str(exc)) from exc
    if not isinstance(data, dict):
        raise ValidationError("top level must be an object")
    return data


def text(value: Any, location: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{location}: non-empty string required")
        return ""
    return value.strip()


def text_list(value: Any, location: str, errors: list[str], allow_empty: bool = False) -> list[str]:
    if not isinstance(value, list) or (not value and not allow_empty):
        errors.append(f"{location}: {'list' if allow_empty else 'non-empty list'} required")
        return []
    result: list[str] = []
    for index, item in enumerate(value):
        result.append(text(item, f"{location}[{index}]", errors))
    return result


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schema_version") != 1:
        errors.append("schema_version: must be 1")

    meta = data.get("metadata")
    if not isinstance(meta, dict):
        errors.append("metadata: object required")
        meta = {}
    for key in ("project", "basis"):
        text(meta.get(key), f"metadata.{key}", errors)
    if meta.get("document") != "inventory":
        errors.append("metadata.document: must be 'inventory'")
    if meta.get("process_phase") != "swk-02":
        errors.append("metadata.process_phase: must be 'swk-02'")
    if meta.get("status") not in DOCUMENT_STATUSES:
        errors.append("metadata.status: invalid document status")
    for key in ("created", "last_updated"):
        value = meta.get(key)
        if not isinstance(value, str) or not DATE_RE.fullmatch(value):
            errors.append(f"metadata.{key}: YYYY-MM-DD required")

    for key in ("assignment", "scope", "investigation", "limitations", "findings", "review"):
        if key not in data:
            errors.append(f"{key}: required")

    text(data.get("assignment"), "assignment", errors)
    text_list(data.get("limitations"), "limitations", errors, allow_empty=True)

    review = data.get("review")
    if not isinstance(review, dict):
        errors.append("review: object required")
        review = {}
    for key in ("precheck_passed", "quality_gate_passed"):
        if not isinstance(review.get(key), bool):
            errors.append(f"review.{key}: boolean required")
    text_list(review.get("unmet_criteria"), "review.unmet_criteria", errors, allow_empty=True)
    if meta.get("status") in {"review", "accepted"}:
        if review.get("precheck_passed") is not True or review.get("quality_gate_passed") is not True:
            errors.append("review: passed precheck and quality gate required for review/accepted")
        if review.get("unmet_criteria"):
            errors.append("review.unmet_criteria: must be empty for review/accepted")
        checked_at = text(review.get("checked_at"), "review.checked_at", errors)
        text(review.get("checked_by"), "review.checked_by", errors)
        if checked_at and not DATE_RE.fullmatch(checked_at):
            errors.append("review.checked_at: YYYY-MM-DD required")

    approval = data.get("approval")
    if meta.get("status") == "accepted":
        if not isinstance(approval, dict):
            errors.append("approval: object required for accepted")
        else:
            accepted_at = text(approval.get("accepted_at"), "approval.accepted_at", errors)
            text(approval.get("accepted_by"), "approval.accepted_by", errors)
            text(approval.get("note"), "approval.note", errors)
            if accepted_at and not DATE_RE.fullmatch(accepted_at):
                errors.append("approval.accepted_at: YYYY-MM-DD required")
    elif approval not in (None, {}):
        errors.append("approval: allowed only for accepted")

    for section in ("scope", "investigation"):
        items = data.get(section)
        if not isinstance(items, list) or not items:
            errors.append(f"{section}: non-empty list required")
            continue
        for index, item in enumerate(items):
            location = f"{section}[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{location}: object required")
                continue
            required = ("area", "idea_reference", "relevance") if section == "scope" else (
                "area", "examined", "not_examined", "limitations"
            )
            for key in required:
                if key in ("examined", "not_examined", "limitations"):
                    text_list(item.get(key), f"{location}.{key}", errors, allow_empty=True)
                else:
                    text(item.get(key), f"{location}.{key}", errors)

    findings = data.get("findings")
    if not isinstance(findings, list) or not findings:
        errors.append("findings: non-empty list required")
        return errors

    seen: set[str] = set()
    numbers: list[int] = []
    for index, finding in enumerate(findings):
        location = f"findings[{index}]"
        if not isinstance(finding, dict):
            errors.append(f"{location}: object required")
            continue
        identifier = text(finding.get("id"), f"{location}.id", errors)
        match = EVD_RE.fullmatch(identifier)
        if not match:
            errors.append(f"{location}.id: expected evd-nnn")
        else:
            numbers.append(int(match.group(1)))
        if identifier in seen:
            errors.append(f"{location}.id: duplicate {identifier}")
        seen.add(identifier)

        text(finding.get("statement"), f"{location}.statement", errors)
        status = finding.get("evidence_status")
        if status not in EVIDENCE_STATUSES:
            errors.append(f"{location}.evidence_status: invalid status")
        text(finding.get("status_reason"), f"{location}.status_reason", errors)
        text(finding.get("conclusion"), f"{location}.conclusion", errors)

        idea = finding.get("idea_reference")
        if not isinstance(idea, dict):
            errors.append(f"{location}.idea_reference: object required")
        else:
            text(idea.get("location"), f"{location}.idea_reference.location", errors)
            text(idea.get("significance"), f"{location}.idea_reference.significance", errors)

        verification = finding.get("verification")
        if not isinstance(verification, dict):
            errors.append(f"{location}.verification: object required")
        else:
            text_list(verification.get("performed"), f"{location}.verification.performed", errors, allow_empty=True)
            text(verification.get("result"), f"{location}.verification.result", errors)
            text_list(verification.get("not_performed"), f"{location}.verification.not_performed", errors, allow_empty=True)
            text(verification.get("limitation"), f"{location}.verification.limitation", errors)

        sources = finding.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{location}.sources: non-empty list required")
            sources = []
        source_types: set[str] = set()
        for source_index, source in enumerate(sources):
            source_location = f"{location}.sources[{source_index}]"
            if not isinstance(source, dict):
                errors.append(f"{source_location}: object required")
                continue
            source_type = source.get("type")
            if source_type not in SOURCE_TYPES:
                errors.append(f"{source_location}.type: invalid source type")
            else:
                source_types.add(source_type)
            for key in ("location", "version", "checked_at", "contribution"):
                value = text(source.get(key), f"{source_location}.{key}", errors)
                if key == "checked_at" and value and not DATE_RE.fullmatch(value):
                    errors.append(f"{source_location}.checked_at: YYYY-MM-DD required")

        if status == "USER_PROVIDED" and "USER_STATEMENT" not in source_types:
            errors.append(f"{location}: USER_PROVIDED requires USER_STATEMENT")
        if status == "INFERRED" and "ANALYSIS" not in source_types:
            errors.append(f"{location}: INFERRED requires ANALYSIS")
        if status == "VERIFIED" and "PROJECT_DOCUMENTATION" in source_types:
            errors.append(
                f"{location}: VERIFIED may not mix PROJECT_DOCUMENTATION; split the finding"
            )

        conflict = finding.get("conflict")
        if status == "CONFLICT":
            if len(sources) < 2:
                errors.append(f"{location}: CONFLICT requires at least two sources")
            if not isinstance(conflict, dict):
                errors.append(f"{location}.conflict: object required for CONFLICT")
            else:
                for key in (
                    "statement_1", "source_1", "statement_2", "source_2",
                    "common_subject", "time_scope", "applicability", "incompatibility",
                ):
                    text(conflict.get(key), f"{location}.conflict.{key}", errors)
        elif conflict not in (None, {}):
            errors.append(f"{location}.conflict: allowed only for CONFLICT")

    if numbers and numbers != list(range(1, len(numbers) + 1)):
        errors.append("findings: identifiers must be ordered and contiguous from evd-001")
    return errors


def md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def bullets(values: list[str]) -> list[str]:
    return [f"- {value}" for value in values] or ["- keine"]


def render(data: dict[str, Any]) -> str:
    meta = data["metadata"]
    lines = [
        "---", "document: inventory", "process_phase: swk-02",
        f'project: "{meta["project"]}"', f'status: {meta["status"]}',
        f'created: {meta["created"]}', f'last_updated: {meta["last_updated"]}',
        f'basis: {meta["basis"]}', "---", "", "# Bestandsuntersuchung", "",
        "<!-- Automatisch erzeugt. Nicht direkt bearbeiten. -->", "",
        "## 1. Grundlage und Untersuchungsauftrag", "", data["assignment"], "",
        "## 2. Untersuchungsumfang", "",
        "| Untersuchungsbereich | Bezug zur Idee | Begründung der Relevanz |",
        "|---|---|---|",
    ]
    for item in data["scope"]:
        lines.append(f'| {md(item["area"])} | {md(item["idea_reference"])} | {md(item["relevance"])} |')
    lines.extend(["", "## 3. Durchgeführte Untersuchung", "",
                  "| Untersuchungsbereich | Untersucht | Nicht untersucht | Einschränkungen |",
                  "|---|---|---|---|"])
    for item in data["investigation"]:
        lines.append("| " + " | ".join([
            md(item["area"]), md("; ".join(item["examined"]) or "–"),
            md("; ".join(item["not_examined"]) or "–"),
            md("; ".join(item["limitations"]) or "–"),
        ]) + " |")
    lines.extend(["", "## 4. Befundübersicht", "", "| Kennung | Aussage | Nachweisstatus |",
                  "|---|---|---|"])
    for finding in data["findings"]:
        lines.append(f'| `{finding["id"]}` | {md(finding["statement"])} | `{finding["evidence_status"]}` |')
    lines.extend(["", "## 5. Einzelbefunde", ""])
    for finding in data["findings"]:
        lines.extend([
            f'### {finding["id"]}', "", "Aussage:", finding["statement"], "",
            "Nachweisstatus:", f'`{finding["evidence_status"]}`', "",
            "Begründung des Nachweisstatus:", finding["status_reason"], "", "Quellen:", "",
            "| Quellenart | Fundstelle | Version oder Commit | Prüfdatum | Beitrag zum Befund |",
            "|---|---|---|---|---|",
        ])
        for source in finding["sources"]:
            lines.append("| " + " | ".join([
                f'`{source["type"]}`', md(source["location"]), md(source["version"]),
                source["checked_at"], md(source["contribution"]),
            ]) + " |")
        verification = finding["verification"]
        lines.extend(["", "Prüfung:", "", "Durchgeführt:", *bullets(verification["performed"]), "",
                      f'Ergebnis: {verification["result"]}', "", "Nicht durchgeführt:",
                      *bullets(verification["not_performed"]), "",
                      f'Einschränkung der Aussagekraft: {verification["limitation"]}', ""])
        if finding["evidence_status"] == "CONFLICT":
            conflict = finding["conflict"]
            lines.extend(["Konflikt:", ""] + [
                f'- {label}: {conflict[key]}' for key, label in (
                    ("statement_1", "Aussage 1"), ("source_1", "Quelle 1"),
                    ("statement_2", "Aussage 2"), ("source_2", "Quelle 2"),
                    ("common_subject", "Gemeinsamer Sachverhalt"),
                    ("time_scope", "Bezugszeitpunkt oder Gültigkeitszeitraum"),
                    ("applicability", "Geltungsbereich"),
                    ("incompatibility", "Logische Unvereinbarkeit"),
                )
            ] + [""])
        lines.extend(["Bezug zur Projektidee:", "",
                      f'- Fundstelle: {finding["idea_reference"]["location"]}',
                      f'- Bedeutung: {finding["idea_reference"]["significance"]}', "",
                      "Folgerung:", finding["conclusion"], ""])
    review = data["review"]
    lines.extend(["## 6. Grenzen der Bestandsuntersuchung", "", *bullets(data["limitations"]), "",
                  "## 7. Prüfergebnis swk-02", "",
                  f'- Vorprüfung bestanden: `{str(review["precheck_passed"]).lower()}`',
                  f'- Qualitätsgrenze bestanden: `{str(review["quality_gate_passed"]).lower()}`',
                  f'- geprüft am: {review.get("checked_at") or "–"}',
                  f'- geprüft durch: {review.get("checked_by") or "–"}', "",
                  "Nicht erfüllte Kriterien:", *bullets(review["unmet_criteria"]), "",
                  f'- Begründung einer möglichen Blockade: {review.get("blockage") or "keine"}', "",
                  "## 8. Freigabestatus", "", f'- Dokumentstatus: `{meta["status"]}`'])
    approval = data.get("approval")
    if approval:
        lines.extend([f'- angenommen am: {approval["accepted_at"]}',
                      f'- angenommen durch: {approval["accepted_by"]}',
                      f'- Anmerkungen: {approval["note"]}'])
    else:
        lines.extend(["- angenommen am: –", "- angenommen durch: –", "- Anmerkungen: –"])
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "render", "check"):
        item = sub.add_parser(command)
        item.add_argument("input", type=Path)
        if command != "validate":
            item.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        data = load(args.input)
        errors = validate(data)
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        if args.command == "validate":
            print(f"valid: {args.input}")
            return 0
        output = render(data)
        if args.command == "render":
            args.output.write_text(output, encoding="utf-8")
            print(f"rendered: {args.output}")
            return 0
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != output:
            print(f"ERROR: {args.output} is not generated from {args.input}", file=sys.stderr)
            return 1
        print(f"current: {args.output}")
        return 0
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
