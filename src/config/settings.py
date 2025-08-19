"""
Pydantic settings for PokeAPI testing configuration.
"""

from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Base settings for the application."""
    
    # Environment
    environment: str = Field(default="local", description="Environment name (local, ci, staging)")
    debug: bool = Field(default=False, description="Debug mode")
    
    # Logging
    log_level: str = Field(default="INFO", description="Logging level")
    log_format: str = Field(default="json", description="Logging format (json, text)")
    
    class Config:
        env_prefix = "POKEAPI_"
        env_file = ".env"


class TestSettings(BaseSettings):
    """Test-specific settings."""
    
    # API Configuration
    base_url: str = Field(default="https://pokeapi.co/api/v2", description="Base URL for PokéAPI")
    timeout: int = Field(default=30, description="Request timeout in seconds")
    retry_attempts: int = Field(default=3, description="Number of retry attempts")
    
    # Test Configuration
    parallel_workers: int = Field(default=4, description="Number of parallel test workers")
    test_data_path: str = Field(default="testdata", description="Path to test data directory")
    
    # Browser Configuration (future UI tests)
    browser_headless: bool = Field(default=True, description="Run browser in headless mode")
    browser_timeout: int = Field(default=30, description="Browser timeout in seconds")
    
    class Config:
        env_prefix = "TEST_"
        env_file = ".env"


# Global settings instances
settings = Settings()
test_settings = TestSettings()
