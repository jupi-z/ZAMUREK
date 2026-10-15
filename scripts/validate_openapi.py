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
    assert operations >= 10, "OpenAPI contract too incomplete for V1 draft"
    print(f"OpenAPI 3.1 draft parsed: {operations} operations, component references resolved.")

if __name__ == "__main__":
    main()
