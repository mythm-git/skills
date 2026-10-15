# Architecture and Maintainability

Preserve established conventions when changing an existing system. Separate interfaces, business logic, configuration, and infrastructure. Use explicit boundaries for external services and validate at boundaries. Avoid duplicate logic, speculative abstractions, and dependencies whose benefit is smaller than their maintenance cost.

Use portable relative paths, standard manifests and locks where appropriate. Keep generated data separate from sources. Add type hints and meaningful documentation in the language's normal style; use Doxygen-compatible comments for significant C/C++ APIs.
