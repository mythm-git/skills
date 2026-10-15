# Database Security and Recovery

Use parameterized queries or trusted query builders; never concatenate user data into executable SQL. Validate inputs and add appropriate constraints. Check database roles and cross-user/unauthenticated access. Use RLS when the database supports it and the system needs row-level multi-tenant isolation; otherwise implement equivalent server-side isolation and test it.

For important persistent data, document backup interval, retention, access controls, integrity checks, recovery objective, restore procedure, and isolated restore test. Never perform a destructive production restore without explicit authorization.
