---
description: "Validate backend API endpoints for functionality and security."
---

# API Testing Skill

## When to Use
Use this skill when testing integrations, verifying data integrity before UI checks, or when UI is not yet available but backend services are ready.

## Steps
1. **Endpoint Discovery**: Identify the base URL and specific endpoints (GET, POST, etc.).
2. **Authentication**: Configure Bearer tokens or API keys (using `<REDACTED>` in logs).
3. **Request Construction**: Build payloads and headers.
4. **Validation**:
   - Check Status Codes (200, 201, 400, etc.).
   - Validate Schema (JSON structure).
   - Check Response Latency.
5. **Report**: Summarize pass/fail per endpoint.

## Example Output
### API Test: User Authentication
- **Endpoint**: `POST /api/v1/login`
- **Status**: PASS
- **Status Code**: 200 OK
- **Response Time**: 142ms
- **Validation**: Schema matches `UserLoginResponse` definition.
