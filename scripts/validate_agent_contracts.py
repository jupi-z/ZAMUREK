#!/usr/bin/env python3
"""Static integrity checks for early ZAMUREK agent/event JSON Schema contracts.

No runtime validation or permission testing is implied.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVENT = ROOT / "packages/contracts/events/event-envelope.schema.json"
TOOL = ROOT / "packages/contracts/agent-tools/tool-definition.schema.json"

def load(path):
    value = json.loads(path.read_text(encoding="utf-8"))
    assert value["$schema"] == "https://json-schema.org/draft/2020-12/schema", path
    assert value["type"] == "object", path
    assert value["additionalProperties"] is False, path
    assert set(value["required"]) <= set(value["properties"]), f"{path}: required fields missing"
    return value

def main() -> int:
    event = load(EVENT)
    tool = load(TOOL)
    event_required = {"eventId", "eventType", "schemaVersion", "organizationId",
                      "correlationId", "occurredAt", "classification", "payloadRef"}
    tool_required = {"toolId", "version", "riskLevel", "tenantScope",
                     "requiredPermissions", "inputSchema", "outputSchema",
                     "approvalPolicy", "timeoutMs", "idempotency"}
    assert event_required <= set(event["required"]), "Event envelope must be tenant-scoped"
    assert tool_required <= set(tool["required"]), "Tool definition must declare policy"
    risk = tool["properties"]["riskLevel"]["enum"]
    approval = tool["properties"]["approvalPolicy"]["enum"]
    assert set(risk) == {"READ_PUBLIC", "READ_TENANT", "DRAFT_WRITE",
                         "SENSITIVE_WRITE", "FORBIDDEN"}
    assert "HUMAN_REQUIRED" in approval and "DISALLOWED" in approval
    assert tool["properties"]["tenantScope"]["enum"] == [
        "ACTOR_ORGANIZATION", "ACTOR_ESTABLISHMENT", "PUBLIC_ONLY"
    ]
    assert tool["properties"]["requiredPermissions"].get("uniqueItems") is True
    print("Agentic/Event JSON Schema drafts: structure and tenant policy fields OK.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, KeyError, AssertionError, ValueError, json.JSONDecodeError) as e:
        print(f"Agentic contract validation FAILED: {e}")
        sys.exit(1)
