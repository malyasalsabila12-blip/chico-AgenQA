# Skill: Security & Vulnerability Audit (OWASP)

## Purpose
Perform a security-focused audit of the application to identify common vulnerabilities and ensure compliance with basic security standards.

## Workflow
1. **Input Validation**: Check fields for XSS (Cross-Site Scripting) and SQL Injection patterns.
2. **Header Analysis**: Verify Security Headers (e.g., `Content-Security-Policy`, `X-Frame-Options`).
3. **Authentication Audit**: Check for insecure password fields, lack of masking, or weak session management.
4. **Endpoint Scanning**: Identify exposed API endpoints or sensitive data in responses.

## Tools
- `playwright-browser_navigate`
- `playwright-browser_evaluate` (for script injection tests)
- `playwright-browser_network_requests` (for header/response inspection)
