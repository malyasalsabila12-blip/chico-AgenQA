# Skill: Environment Health Check (Pre-Flight)

## Purpose
Validate the stability and availability of the test environment (Frontend, API, DB) before initiating a full test suite.

## Checkpoints
1. **Frontend Reachability**: Verify main URL returns `200 OK` and renders base elements.
2. **API Connectivity**: Ping core service endpoints to ensure backend is responsive.
3. **Database Latency**: (If MCP available) Check connection and simple query response time.
4. **Third-Party Services**: Verify external dependencies (e.g., Auth providers, Payment gateways) are reachable.

## Outcome
- If checks pass: Proceed with testing.
- If checks fail: Report `BLOCKED` status immediately and provide diagnostic logs.
