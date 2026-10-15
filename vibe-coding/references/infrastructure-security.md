# Infrastructure, Secrets, and Uploads

Use supported runtimes and dependencies, least-privilege identities, HTTPS, minimal exposed services, separated environments, and safe command construction. Never disable certificate verification as a shortcut. Keep secrets in environment-specific stores; validate required configuration at startup and redact values from logs/errors.

For uploads enforce authorization, allowed types, content checks where justified, maximum size, safe generated storage names, and traversal resistance. Store sensitive files privately; use authenticated download or signed URLs. Add malware scanning when threat model warrants it.
