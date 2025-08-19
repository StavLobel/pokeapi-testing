"""
Pytest configuration and fixtures for PokeAPI testing.
"""

import pytest
import os
from playwright.sync_api import APIRequestContext, Playwright, sync_playwright
from src.api.pokemon_client import PokemonAPIClient
from src.config.settings import test_settings


def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption(
        "--api-base-url",
        action="store",
        default=None,
        help="Override base URL for API requests (e.g., --api-base-url=http://localhost:8000/api/v2)"
    )


def pytest_configure(config):
    """Configure pytest and store CLI options."""
    # Set environment variable if CLI argument is provided
    cli_base_url = config.getoption("--api-base-url")
    if cli_base_url:
        os.environ['POKEAPI_BASE_URL'] = cli_base_url
        os.environ['TEST_BASE_URL'] = cli_base_url


@pytest.fixture(scope="session")
def playwright() -> Playwright:
    """Playwright instance for the test session."""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright, dynamic_settings: dict) -> APIRequestContext:
    """API request context for making HTTP requests."""
    # Use dynamic settings if CLI override is provided, otherwise use default
    timeout = dynamic_settings['test_settings'].timeout * 1000  # Convert seconds to milliseconds
    context = playwright.request.new_context(timeout=timeout)
    yield context
    context.dispose()


@pytest.fixture(scope="function")
def pokemon_client(api_request_context: APIRequestContext, dynamic_settings: dict) -> PokemonAPIClient:
    """Create a Pokémon API client for testing."""
    # Use dynamic settings if CLI override is provided, otherwise use default
    base_url = dynamic_settings.get('cli_base_url')
    return PokemonAPIClient(api_request_context, base_url=base_url)


@pytest.fixture(scope="session")
def cli_base_url_override(request):
    """Fixture to get CLI base URL override if provided."""
    return request.config.getoption("--api-base-url")


@pytest.fixture(scope="session")
def dynamic_settings(request):
    """Fixture that provides settings with CLI overrides applied."""
    from src.config.settings import Settings, TestSettings
    
    # Get CLI override
    cli_base_url = request.config.getoption("--api-base-url")
    
    if cli_base_url:
        # Create new settings instances with CLI override
        settings = Settings(
            base_url=cli_base_url,
            timeout=int(os.getenv('POKEAPI_TIMEOUT', '30000')),
            log_level=os.getenv('POKEAPI_LOG_LEVEL', 'INFO')
        )
        test_settings = TestSettings(
            base_url=cli_base_url,
            timeout=int(os.getenv('TEST_TIMEOUT', '30')),
            parallel_workers=int(os.getenv('TEST_PARALLEL_WORKERS', '4'))
        )
    else:
        # Use default settings
        settings = Settings()
        test_settings = TestSettings()
    
    return {
        'settings': settings,
        'test_settings': test_settings,
        'cli_base_url': cli_base_url
    }
