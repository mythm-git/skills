# Security Applicability Engine

Classify each control for the actual system, then record a status and evidence. `NOT_APPLICABLE` needs a reason where non-obvious; unknown system facts are `REQUIRES_FURTHER_INFORMATION` during planning and `BLOCKED` if they prevent verification.

| Characteristic | Required controls | Recommended controls | Usually not applicable |
| --- | --- | --- | --- |
| Local CLI/files | input bounds, safe paths, dependency/config safety, safe errors | audit logging, sandboxing | CORS, browser sessions, RLS |
| Browser web app | input validation, XSS prevention, server authorization, headers | CSP, CSRF protection, rate limits | RLS without a database |
| Public API | schemas, authz where protected, size limits, safe errors | rate limits, abuse monitoring, webhook verification | browser storage protections |
| Multi-tenant database | server authz, tenant isolation, constrained queries | RLS where supported, audit logging, restore testing | RLS only if backend has no equivalent storage feature |
| File uploads | authorization, type/content/size checks, safe paths | malware scan, private objects, signed URLs | public buckets for sensitive content |
| Production/deploy | least privilege, supported versions, HTTPS, rollback | dependency scanning, monitoring | local-only controls unrelated to deployed service |

For controls that cannot be automated, define a manual verification procedure. A committed configuration file only establishes `IMPLEMENTED_UNVERIFIED` until runtime verification succeeds.
