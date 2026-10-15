# Example: Secure API

Request: “Add a public search endpoint.”

Classify as medium risk: validate a bounded query schema, enforce pagination and response limits, rate-limit if exposed to abuse, use safe errors, isolate provider calls behind an interface, and test malformed, oversized, and failed-provider responses.
