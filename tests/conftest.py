"""Test configuration for Risk Assessment Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "risk-assessment-agent", "category": "Security AI"}
