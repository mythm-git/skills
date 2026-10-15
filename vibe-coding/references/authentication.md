# Authentication and Authorization

Use maintained providers/frameworks instead of custom protocols. Validate identity and permissions server-side; a browser user ID or hidden button is not authority. Use least privilege, deny-by-default checks, resource ownership validation, and tenant isolation. Test unauthenticated, expired/invalid token, cross-user, cross-tenant, and non-admin access.

Prefer secure HttpOnly cookies where appropriate; use Secure/SameSite settings and CSRF defenses for cookie-authenticated state changes. Do not expose privileged credentials to clients. Use expiry, invalidation, bounded brute-force protections, and strong MFA—prefer phishing-resistant methods—for privileged administrators.
