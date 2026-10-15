# Frontend Security

Keep privileged secrets server-side. Use framework-safe rendering; do not inject untrusted HTML without an explicitly justified sanitizer. Configure CSP and security headers appropriate to the app; restrict CORS to approved origins when cross-origin access is needed. CORS is never authentication or authorization.

Avoid sensitive tokens in localStorage, URLs, logs, source maps, and public configuration. Test XSS-prone rendering and session/CSRF behavior where applicable.
