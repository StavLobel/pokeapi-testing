"""
Pydantic settings for PokeAPI testing configuration.
"""

import os
from typing import Optional
from pydantic import BaseModel, Field


class Settings(BaseModel):
    """Base settings for the application."""
    
    base_url: str = Field(
        default=os.getenv('POKEAPI_BASE_URL', 'https://pokeapi.co/api/v2'),
        description="Base URL for the PokeAPI"
    )
    timeout: int = Field(
        default=int(os.getenv('POKEAPI_TIMEOUT', '30000')),
        description="Default timeout for API requests in milliseconds"
    )
    log_level: str = Field(
        default=os.getenv('POKEAPI_LOG_LEVEL', 'INFO'),
        description="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)"
    )
    
    # Add other global settings here


class TestSettings(BaseModel):
    """Test-specific settings, overriding global settings for testing."""
    
    base_url: str = Field(
        default=os.getenv('TEST_BASE_URL', 'https://pokeapi.co/api/v2'),
        description="Base URL for the PokeAPI in test environment"
    )
    timeout: int = Field(
        default=int(os.getenv('TEST_TIMEOUT', '30')),
        description="Default timeout for API requests in seconds"
    )
    parallel_workers: int = Field(
        default=int(os.getenv('TEST_PARALLEL_WORKERS', '4')),
        description="Number of parallel test workers"
    )


# Global settings instances
settings = Settings()
test_settings = TestSettings()

# Configuration validation
def validate_config():
    """Validate configuration settings."""
    if not settings.base_url.startswith(('http://', 'https://')):
        raise ValueError(f"Invalid base_url: {settings.base_url}. Must start with http:// or https://")
    
    if settings.timeout <= 0:
        raise ValueError(f"Invalid timeout: {settings.timeout}. Must be positive")
    
    if test_settings.timeout <= 0:
        raise ValueError(f"Invalid test timeout: {test_settings.timeout}. Must be positive")
    
    if test_settings.parallel_workers <= 0:
        raise ValueError(f"Invalid parallel workers: {test_settings.parallel_workers}. Must be positive")

# Validate configuration on import
validate_config()
