# Verification Status

For every applicable security control report one status:

- `IMPLEMENTED_AND_TESTED`: implementation plus relevant successful evidence.
- `IMPLEMENTED_UNVERIFIED`: implemented but no adequate test.
- `PENDING`: work remains.
- `FAILED`: a check found a defect.
- `BLOCKED`: missing access, permission, infrastructure, or information prevents progress.
- `NOT_APPLICABLE`: does not apply; state why if unclear.

Static review, a committed file, and an unexecuted test are not runtime proof. Never use “secure” as a blanket conclusion.
