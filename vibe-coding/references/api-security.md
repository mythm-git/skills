# API and External Service Security

Use schema validation for every incoming request and validate relevant provider responses. Bound body size, pagination, query complexity, retry count, and timeout. Authenticate and authorize protected actions, rate-limit abuse-prone endpoints, and return safe error messages.

For webhooks verify the provider signature using the required raw body and use replay defense when supported. Test malformed bodies, missing fields, wrong types, oversized input, injection attempts, missing/invalid signatures, modified payloads, and failed provider responses.
