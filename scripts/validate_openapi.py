#!/usr/bin/env python3
"""Strict structural checks for the draft xShop OpenAPI spec; requires PyYAML."""
from __future__ import annotations
import sys
from pathlib import Path
try:
    import yaml
except ImportError:
    print("Missing PyYAML; install: python3 -m pip install -r scripts/requirements-docs.txt")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "packages/contracts/openapi/xshop-v1.yaml"

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

UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
)

def walk(value):
    if isinstance(value, dict):
        yield value
        for v in value.values():
            yield from walk(v)
    elif isinstance(value, list):
        for v in value:
            yield from walk(v)

def main() -> None:
    doc = yaml.load(SPEC.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    assert isinstance(doc, dict) and str(doc.get("openapi", "")).startswith("3.1."), "Expected OpenAPI 3.1"
    assert isinstance(doc.get("paths"), dict) and doc["paths"], "Missing paths"
    assert doc.get("components", {}).get("schemas"), "Missing component schemas"

    operation_ids = set()
    operations = 0
    for path, methods in doc["paths"].items():
        assert path.startswith("/"), f"Invalid path: {path}"
        for verb, definition in methods.items():
            if verb.lower() not in {"get", "post", "put", "patch", "delete", "options", "head", "trace"}:
                continue
            operations += 1
            op_id = definition.get("operationId")
            assert op_id and op_id not in operation_ids, f"Duplicate/missing operationId: {op_id}"
            operation_ids.add(op_id)
            assert definition.get("responses"), f"Missing responses: {verb} {path}"

    for node in walk(doc):
        ref = node.get("$ref")
        if ref is None:
            continue
        assert isinstance(ref, str) and ref.startswith("#/"), f"Unexpected ref: {ref}"
        current = doc
        for segment in ref[2:].split("/"):
            segment = segment.replace("~1", "/").replace("~0", "~")
            assert isinstance(current, dict) and segment in current, f"Broken ref: {ref}"
            current = current[segment]
    # Approved xShop invariants as of 2026-10-16.
    required_paths = (
        "/auth/v1/register", "/auth/v1/verify-email", "/auth/v1/login",
        "/auth/v1/refresh", "/auth/v1/logout", "/v1/carts",
        "/v1/carts/{cartId}/quote", "/v1/checkouts",
        "/v1/orders", "/v1/orders/{orderId}",
        "/v1/merchant/fx-rate", "/v1/merchant/orders",
    )
    for required in required_paths:
        assert required in doc["paths"], f"Required route missing: {required}"

    protected = (
        ("/v1/carts", "post"),
        ("/v1/carts/{cartId}", "get"),
        ("/v1/carts/{cartId}/items", "patch"),
        ("/v1/carts/{cartId}/quote", "get"),
        ("/v1/checkouts", "post"),
        ("/v1/orders", "get"),
        ("/v1/orders/{orderId}", "get"),
        ("/v1/merchant/fx-rate", "get"),
    )
    for path, verb in protected:
        op = doc["paths"][path][verb]
        assert {"bearerAuth": []} in op.get("security", []), (
            f"Auth absent: {verb.upper()} {path}"
        )

    schemas = doc["components"]["schemas"]
    assert "DualPrice" not in schemas, "Old independent dual prices must be removed"
    assert "CartCreated" not in schemas and "CartToken" not in doc["components"].get("parameters", {})
    assert "PriceQuote" in schemas and "FxRateSnapshot" in schemas
    assert "EmailAddress" in schemas, "Email identity required (no SMS)"
    assert "email" in schemas["RegisterCustomer"]["required"]
    assert "phoneE164" not in schemas["RegisterCustomer"]["required"]
    assert "quoteId" in schemas["CheckoutRequest"]["required"]
    assert "basePriceUsd" in schemas["VariantInput"]["required"], "USD-only source price"
    assert schemas["SupportedCurrency"]["enum"] == ["CDF"], "RDC commercial public currency must be CDF"
    assert "/v1/carts/{cartId}/currency" not in doc["paths"], "Old switch-currency route"
    assert operations >= 25, "OpenAPI draft too incomplete"
    print(f"OpenAPI 3.1 draft parsed: {operations} operations, component references resolved.")

if __name__ == "__main__":
    main()
