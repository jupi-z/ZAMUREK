# ZAMUREK — Pull Request / Implementation Evidence

## Capability scope and milestone
- Version checkpoint: `0.x.0`
- Capability IDs from [normative manifest](../spec/v1/capabilities.json):
- Organisation / establishment / regulated-policy effect:
- Current and new `docs/implementation/PROGRESS.json` verified percentage:

## Domain and contract impact
- [ ] No replacement commerce framework (Mercur/Medusa/Saleor/etc.); domain code remains proprietary
- [ ] Offers/states/booking/FX/Agent tool logic follows [docs/v1](../docs/v1/README.md)
- [ ] APIs and JSON Schema updated, request errors/authorization specified
- [ ] DB registry/tenant migration and restoration path tested or marked N/A with justification
- [ ] Event envelope/outbox idempotence, replay and versioning checked
- [ ] Old installed Android and Windows clients remain compatible or migration tests provided

## Evidence, not claims
- [ ] Build, lint, typecheck and unit tests run (exact commands + exit codes)
- [ ] Integration test on genuine PostgreSQL with tenant A/B and establishment A/B
- [ ] Cross-customer/tenant/agent IDOR and access tests included
- [ ] Price USD→CDF and fractional weight test + fx quote immutability checked
- [ ] Booking concurrency, kitchen flow, repair approval, POS/manual payment tested if affected
- [ ] AI action policy/approval and data privacy tested if affected
- [ ] Local Android/Windows builds and artifacts tested on relevant devices if affected
- [ ] Vendor licenses/direct+transitive dependencies scanned and notices/SBOM updated
- [ ] No secrets, PII, source keys, tokens, confidential client data, or real mall partner marks in public repo

## Safety and release
- [ ] Regulatory gates applied for pharmacies/medicines; no unlicensed medicine transaction path
- [ ] CDF display requirements for RDC observed where applicable
- [ ] No SPA, SSR, PWA, Swagger UI or merchant administration HTML hosted in production
- [ ] No claims of signed APK/Play approval/VPS production/CI PASS without evidence
- [ ] Rollback/disaster recovery and API compatibility reviewed

## Results
Include links to CI runs, exact commands, screenshots/logs with private data removed, issues and blockers. **NOT_RUN/SKIPPED/BLOCKED are not PASS.** The 1.0.0 release is forbidden until all mandatory capabilities and P0/P1 gates are accepted.
