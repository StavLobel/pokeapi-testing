"""
Pytest configuration and fixtures for PokeAPI testing.
"""

import pytest
from playwright.sync_api import APIRequestContext, Playwright, sync_playwright


@pytest.fixture(scope="session")
def playwright() -> Playwright:
    """Playwright instance for the test session."""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> APIRequestContext:
    """API request context for making HTTP requests."""
    context = playwright.request.new_context(
        timeout=30000,  # 30 seconds in milliseconds
    )
    yield context
    context.dispose()
