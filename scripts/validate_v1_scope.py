#!/usr/bin/env python3
"""Verify ZAMUREK V1 product scope and progress templates using Python stdlib."""
from __future__ import annotations

import json
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "spec/v1/capabilities.json"
PROGRESS = ROOT / "spec/v1/progress-template.json"
FIXTURES = ROOT / "spec/v1/fixtures.json"
MATRIX = ROOT / "docs/v1/CAPABILITY-MATRIX.md"
CHARTER = ROOT / "docs/v1/PRODUCT-CHARTER.md"
ERRORS: list[str] = []


def fail(msg: str) -> None:
    ERRORS.append(msg)


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{path.relative_to(ROOT)}: cannot parse: {exc}")
        return {}
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)}: root must be JSON object")
        return {}
    return value


def main() -> int:
    data = load_json(SPEC)
    progress = load_json(PROGRESS)
    fixtures = load_json(FIXTURES)
    matrix = MATRIX.read_text(encoding="utf-8")
    charter = CHARTER.read_text(encoding="utf-8")

    if data.get("product") != "ZAMUREK" or data.get("targetRelease") != "1.0.0":
        fail("Product must be ZAMUREK, target release 1.0.0")
    if data.get("policy") != "NO_PARTIAL_COMMERCIAL_LAUNCH":
        fail("Partial release not allowed in V1 charter")
    expected_verticals = {"retail", "weighted", "food", "service", "furniture", "repair", "pharmacy", "venue"}
    if set(data.get("declaredVerticals", [])) != expected_verticals:
        fail("Incomplete mandatory business verticals")
    mandatory = {
        "FND-01", "FND-02", "FND-05", "FND-07", "FND-13", "FND-16",
        "RTL-01", "WGT-01", "WGT-02", "FOD-01", "FOD-02", "FOD-03",
        "SVC-01", "SVC-02", "FUR-01", "REP-01", "REP-02",
        "PHA-01", "PHA-02", "VEN-01", "VEN-02",
        "AGT-01", "AGT-02", "AGT-03", "AGT-04",
        "SEC-01", "OPS-01", "LEG-01",
        "POS-01", "POS-02", "POS-03", "INT-01", "INT-02",
    }
    capabilities = data.get("capabilities", [])
    if not isinstance(capabilities, list) or len(capabilities) < 43:
        fail("Expected at least 43 explicitly accountable V1 capabilities")
        capabilities = []
    ids = [cap.get("id") for cap in capabilities if isinstance(cap, dict)]
    if len(ids) != len(set(ids)):
        fail("Duplicate capability IDs")
    if not mandatory <= set(ids):
        fail(f"Required capability IDs missing: {sorted(mandatory - set(ids))}")
    for cap in capabilities:
        if not isinstance(cap, dict):
            fail("Each capability must be object")
            continue
        ident = cap.get("id", "")
        if cap.get("requiredForV1") is not True:
            fail(f"{ident}: all manifest entries must be mandatory for complete V1")
        if cap.get("priority") not in {"P0", "P1"}:
            fail(f"{ident}: invalid priority")
        if cap.get("category") not in expected_verticals | {"foundation", "ai", "security", "operations", "legal", "pos", "integration"}:
            fail(f"{ident}: unknown category")
        if not cap.get("description") or not cap.get("acceptance"):
            fail(f"{ident}: missing acceptance criteria")
        if ident not in matrix:
            fail(f"{ident}: not found in human-readable capability matrix")
    legal_controls = charter.lower()
    if not (
        ("pharmac" in legal_controls or "regulated_good" in legal_controls)
        and ("bloqu" in legal_controls or "désactiv" in legal_controls
             or "fail-closed" in legal_controls)
    ):
        fail("Charter must explicitly describe default blocking of regulated medicines")
    if "AGENTIC" not in charter.upper() and "agentique" not in charter.lower():
        fail("AI-native/agentic architecture not recorded")

    phases = progress.get("requiredWorkstreams", [])
    if not isinstance(phases, list) or len(phases) != 9:
        fail("Progress template must have nine checkpoints 0.1.0..0.9.0")
        phases = []
    if sum(s.get("weight", 0) for s in phases if isinstance(s, dict)) != 100:
        fail("Progress weights must sum to 100")
    if [s.get("version") for s in phases] != [f"0.{i}.0" for i in range(1, 10)]:
        fail("Incorrect workstream versions")
    if progress.get("overallPercent") != 0 or progress.get("releaseStatus") != "NOT_READY":
        fail("Template must start at 0% and NOT_READY; not claim work is complete")
    for phase in phases:
        if phase.get("percent") != 0 or phase.get("verifiedItems") != 0:
            fail(f"{phase.get('version')}: no unverified progress")
    if progress.get("capabilities", {}).get("total") != len(capabilities):
        fail("Progress template does not match number of capabilities")
    for priority in ("P0", "P1"):
        if progress.get("criticalGates", {}).get(priority) != "NOT_RUN":
            fail(f"{priority} is not passed before evidence")

    # Real exact-decimal fixture checks, never Python float in currency/weight.
    organizations = fixtures.get("organizations", [])
    if len(organizations) != 7:
        fail("Synthetic fixtures must contain seven industry organizations")
    industries = {o.get("capabilities", [None])[0] for o in organizations}
    if industries != {"RETAIL", "WEIGHTED", "FOOD", "SERVICES", "FURNITURE", "REPAIRS", "PHARMACY"}:
        fail("Missing industry fixture")
    try:
        rate = Decimal(fixtures["fx"]["configuredMerchantUsdToCdf"])
        for organization in organizations:
            if organization.get("id") == "org-weighted":
                offering = organization["offers"][0]
                expected = (
                    Decimal(offering["basePriceUsdMinorPerKg"]) / Decimal(100)
                    * Decimal(offering["sampleGrams"]) / Decimal(1000) * rate
                )
                assert expected == Decimal(offering["sampleTotalCdf"]), "125 g exact price fixture mismatch"
            if organization.get("id") == "org-food":
                offering = organization["offers"][0]
                total_cents = Decimal(offering["basePriceUsdMinor"]) + sum(
                    (Decimal(modifier["priceUsdMinor"]) for modifier in offering["modifiers"]),
                    Decimal(0),
                )
                expected = total_cents / Decimal(100) * rate
                assert expected == Decimal(offering["sampleCdfWithAddon"]), "Pizza addon fixture mismatch"
            if organization.get("id") == "org-pharmacy":
                assert any(
                    p["classification"] == "PRESCRIPTION_REQUIRED"
                    and p["transactionStatus"] == "BLOCKED"
                    for p in organization["offers"]
                ), "Regulated merchandise must be blocked by default"
    except (KeyError, TypeError, InvalidOperation, AssertionError) as exc:
        fail(f"Price/pharmacy fixture validation failed: {exc}")

    integration = data.get("integration", {})
    if integration.get("sharedBackend") != "MONARQUE_CONNECT_PRIVATE":
        fail("Monarque Connect must be canonical shared backend")
    if integration.get("storageModel") != "SHARED_POSTGRESQL_ORGANIZATION_ID_ESTABLISHMENT_ID":
        fail("ZAMUREK cannot require a separate PostgreSQL DB per organization in V1")
    if integration.get("noIndependentCommercialBackend") is not True:
        fail("Do not implement independent Sales/Cash/Billing backend for ZAMUREK")
    if integration.get("customerWalkInPos") is not True:
        fail("Walk-in POS checkout without buyer e-mail required")
    if "une base métier postgresql par" in charter.lower():
        fail("Old per-merchant DB charter rule is prohibited")
    if not all(s in charter.lower() for s in ("pos", "cash", "monarque connect")):
        fail("Charter must guarantee physical POS and shared Core")
    if ERRORS:
        print("ZAMUREK V1 scope validation FAILED:")
        for issue in ERRORS:
            print(" -", issue)
        return 1
    print(f"ZAMUREK V1 scope OK: {len(capabilities)} capabilities, 8 verticals, shared Core, POS, "
          "9 weighted gates, 100% evidence required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
