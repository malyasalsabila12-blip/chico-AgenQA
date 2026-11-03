# Assignment: AI QA Automation Engineer

This repository contains a fully realized AI Agent specialized in Quality Assurance. It integrates the **Model Context Protocol (MCP)**, a sophisticated **System Prompt**, and **Professional Skill Sets**.

## 🚀 Core Components

### 1. The AI Agent (Persona)
The agent is defined in `AGENTS.md`. It acts as a Senior QA Lead with 10+ years of experience, enforcing strict reliability standards such as the **Smart Wait Strategy** and **Root Cause Analysis (RCA)**.

### 2. MCP Integration (The "Hands")
This agent utilizes the **Playwright MCP Server** to interact with the web. 
- **Configuration**: See `mcp/mobile-mcp.json` for mobile environment protocols.
- **Tools**: The agent uses MCP tools (`playwright-browser_*`) to navigate, click, and inspect the DOM factually.

### 3. Professional Skills (The "Brain")
Located in `skills/`, these are structured workflows that the agent can "load" to perform specialized tasks:
- **Automation**: `regression-check`, `api-testing`.
- **User Experience**: `accessibility-audit`, `performance-vitals`.
- **Design**: `visual-regression`.

### 4. Implementation Framework (The "Automation")
The `ai_qa_agent/` directory contains a professional-grade testing framework:
- **Architecture**: Page Object Model (POM).
- **Tooling**: Python, Pytest, Playwright, Allure Reporting.
- **Config**: Centralized `config.py` for environment-agnostic execution.

## 🛠️ How to Run
To initiate the autonomous QA flow:
```powershell
python ai_qa_agent/main.py
```

To run the professional test suite directly:
```powershell
pytest ai_qa_agent/test_saucedemo.py --alluredir=allure-results
```

---
*Created for the QA Automation AI Engineer Assignment.*
