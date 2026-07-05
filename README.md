# Risk Assessment Agent

[![CI](https://github.com/kogunlowo123/risk-assessment-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/risk-assessment-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Security AI | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Enterprise risk assessment agent that identifies cyber risks, calculates risk scores using FAIR methodology, maps risks to business impact, generates risk registers, and produces board-level risk reports.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `analyze` | Primary analysis function for Risk Assessment Agent |
| `scan` | Scan target for issues relevant to Risk Assessment Agent |
| `report` | Generate report for Risk Assessment Agent |
| `remediate` | Execute remediation action |
| `monitor` | Monitor for ongoing issues |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/risk-assessment/analyze` | Run analysis |
| `POST` | `/api/v1/risk-assessment/scan` | Scan target |
| `POST` | `/api/v1/risk-assessment/report` | Generate report |
| `POST` | `/api/v1/risk-assessment/remediate` | Execute remediation |
| `GET` | `/api/v1/risk-assessment/status` | Get status |

## Features

- Risk
- Assessment
- Reporting
- Monitoring

## Integrations

- Siem Connector
- Edr Connector
- Threat Intel
- Ticketing System

## Architecture

```
risk-assessment-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── risk_assessment_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Security Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
