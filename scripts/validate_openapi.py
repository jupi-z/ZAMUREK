#!/usr/bin/env python3
"""Static OpenAPI 3.1 structural/semantic assertions for normative ZAMUREK V1 draft.

This is intentionally NOT a full OpenAPI conformance validator or a backend test.
"""
from __future__ import annotations
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Missing PyYAML; pip install -r scripts/requirements-docs.txt")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "packages/contracts/openapi/zamurek-v1.yaml"


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader, node):
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key} at line {key_node.start_mark.line + 1}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)


def walk(value):
    if isinstance(value, dict):
        yield value
        for v in value.values():
            yield from walk(v)
    elif isinstance(value, list):
        for v in value:
            yield from walk(v)


def main():
    doc = yaml.load(SPEC.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    assert isinstance(doc, dict) and str(doc.get("openapi", "")).startswith("3.1."), "OpenAPI 3.1 required"
    assert "ZAMUREK" in doc.get("info", {}).get("title", ""), "Legacy xShop title not accepted"
    paths = doc.get("paths", {})
    assert isinstance(paths, dict) and paths, "Missing paths"

    required_paths = {
        "/auth/v1/register", "/auth/v1/verify-email", "/auth/v1/login",
        "/merchant/v1/sessions", "/merchant/v1/mfa/verify",
        "/v1/offerings", "/v1/merchant/weighted-offerings",
        "/v1/merchant/food-menus", "/v1/restaurant/menus",
        "/v1/restaurant/table-availability", "/v1/table-reservations",
        "/v1/appointments/availability", "/v1/appointments",
        "/v1/merchant/quotes", "/v1/quotes/{quoteId}/accept",
        "/v1/repairs", "/v1/repairs/{repairId}/approve-estimate",
        "/v1/merchant/pos/sales", "/v1/venues", "/v1/venues/{venueId}/offerings",
        "/v1/merchant/venues/{venueId}/opt-in",
        "/v1/merchant/regulated-offerings",
        "/v1/merchant/fx-rate", "/v1/agents/runs",
        "/v1/agents/approvals/{approvalId}",
        "/v1/checkouts", "/v1/orders", "/platform/v1/subscriptions",
    }
    missing = required_paths - set(paths)
    assert not missing, f"ZAMUREK V1 endpoints missing: {sorted(missing)}"
    operation_ids: set[str] = set()
    operations = 0
    methods = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
    for name, mapping in paths.items():
        assert name.startswith("/"), f"Bad path: {name}"
        assert isinstance(mapping, dict), f"Path must map to operations: {name}"
        for method, operation in mapping.items():
            if method not in methods:
                continue
            operations += 1
            assert isinstance(operation, dict), f"Invalid {method} {name}"
            operation_id = operation.get("operationId")
            assert operation_id and operation_id not in operation_ids, (
                f"Duplicate/missing operationId: {operation_id}"
            )
            operation_ids.add(operation_id)
            assert operation.get("responses"), f"Missing responses: {method} {name}"
            if name.startswith("/platform/") or name.startswith("/v1/merchant/"):
                assert {"bearerAuth": []} in operation.get("security", []), (
                    f"Privileged endpoint missing bearerAuth: {method} {name}"
                )

    components = doc.get("components", {})
    schemas = components.get("schemas", {})
    assert isinstance(schemas, dict) and len(schemas) >= 40, "Insufficient typed schemas"
    for value in walk(doc):
        ref = value.get("$ref")
        if ref is None:
            continue
        assert isinstance(ref, str) and ref.startswith("#/"), f"External/invalid ref: {ref}"
        current = doc
        for segment in ref[2:].split("/"):
            segment = segment.replace("~1", "/").replace("~0", "~")
            assert isinstance(current, dict) and segment in current, f"Broken reference {ref}"
            current = current[segment]

    required_schemas = {
        "EmailAddress", "PriceQuote", "FxRateSnapshot", "WeightedOfferingInput",
        "FoodMenuItemInput", "AppointmentInput", "TableReservationInput",
        "RepairIntake", "RepairCase", "VenueOptIn", "PosSaleInput",
        "AgentRunInput", "AgentApprovalInput", "MerchantCredentials",
        "EstablishmentInput", "OfferingInput", "Subscription",
    }
    assert required_schemas <= set(schemas), (
        f"Missing schemas: {sorted(required_schemas - set(schemas))}"
    )
    assert schemas["SupportedCurrency"]["enum"] == ["CDF"], "RDC pilot publicly priced CDF"
    assert "DualPrice" not in schemas, "Two independently priced currencies are superseded"
    assert "basePriceUsd" in schemas["OfferingInput"]["required"]
    assert "quoteId" in schemas["CheckoutRequest"]["required"]
    assert "email" in schemas["RegisterCustomer"]["required"]
    assert "/auth/v1/verify-phone" not in paths, "SMS auth not permitted by V1"
    assert "/v1/carts/{cartId}/currency" not in paths, "Legacy free USD display switch"
    assert operations >= 65, "Multi-industry V1 API surface incomplete"

    print(
        f"ZAMUREK draft OpenAPI parsed: {operations} operations, "
        f"{len(paths)} paths, all component references resolved. "
        "Schema conformance/runtime checks still required in G1."
    )


if __name__ == "__main__":
    main()
