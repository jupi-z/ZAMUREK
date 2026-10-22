#!/usr/bin/env python3
"""Checks normative cross-repo ownership without claiming runtime integration."""
from pathlib import Path
import json
import sys

root=Path(__file__).resolve().parents[1]
errors=[]
def check(cond,message):
    if not cond: errors.append(message)

spec=json.loads((root/"spec/v1/capabilities.json").read_text(encoding="utf-8"))
progress=json.loads((root/"spec/v1/progress-template.json").read_text(encoding="utf-8"))
charter=(root/"docs/v1/PRODUCT-CHARTER.md").read_text(encoding="utf-8")
domain=(root/"docs/v1/DOMAIN-MODEL.md").read_text(encoding="utf-8")
handoff=(root/"docs/v1/CODEX-HANDOFF.md").read_text(encoding="utf-8")
oldprompt=(root/"docs/v1/CODEX-PHASE-0.1.0-PROMPT.md").read_text(encoding="utf-8")
newprompt=(root/"docs/v1/CODEX-INTEGRATION-PROMPT.md").read_text(encoding="utf-8")
pos=(root/"docs/v1/POS-AND-FISCAL-DOCUMENTS.md").read_text(encoding="utf-8")
api=(root/"packages/contracts/openapi/zamurek-v1.yaml").read_text(encoding="utf-8")
ids={c["id"] for c in spec["capabilities"]}

check(len(spec["capabilities"])==43,"43 capabilities must be maintained")
check({"POS-01","POS-02","POS-03","INT-01","INT-02"}<=ids,"POS and integration gate IDs required")
check(spec["integration"]["sharedBackend"]=="MONARQUE_CONNECT_PRIVATE","Canonical private Core missing")
check(spec["integration"]["noIndependentCommercialBackend"] is True,"Independent commercial backend prohibited")
check(spec["integration"]["customerWalkInPos"] is True,"Walk-in POS must be supported")
check(spec["integration"]["coreApiPrefix"]=="/api/v1","Core API prefix inconsistent")
check(spec["integration"]["storageModel"]=="SHARED_POSTGRESQL_ORGANIZATION_ID_ESTABLISHMENT_ID","Shared scoped Postgres required")
check(progress["capabilities"]["total"]==43,"Progress template total must match 43 gates")
check("base métier PostgreSQL par" not in charter,"Outdated one-DB-per-org rule in charter")
check("PostgreSQL partagé" in domain,"Canonical shared Core tenancy missing in domain")
check("Monarque Connect" in charter and "caissier" in charter,"POS and shared Core charter requirement")
check("ENREGISTR" not in oldprompt or "REMPLACÉ" in oldprompt,"Obsolete prompt must be explicitly retired")
check("NE PAS EXÉCUTER" in oldprompt,"Old backend Codex prompt not disabled")
check("10A.5" in newprompt and "Monarque Connect" in newprompt,"New Codex integration dependency missing")
check("SalesOrder" in pos and "PaymentRecord" in pos and "CashMovement" in pos,"Canonical financial operation required")
check("PRE-CONVERGENCE DRAFT" in api,"Noncanonical ZAMUREK OpenAPI must carry warning")
check("DB par entreprise" not in handoff,"Old independent DB constraint remains in Codex handoff")
check("Runtime IA" in handoff,"Shared Agent Runtime requirement missing")

if errors:
    print("ZAMUREK shared Core convergence checks FAILED:")
    for error in errors: print(" -",error)
    sys.exit(1)
print("Convergence documents OK: shared Monarque Core, 43 capabilities, POS/cash/print, retired G1 prompt.")
