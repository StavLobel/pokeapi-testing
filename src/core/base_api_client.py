"""
Base API client for PokéAPI v2 endpoints.
"""

from typing import Any, Dict, Optional
from playwright.sync_api import APIRequestContext
import logging
import os
from ..config.settings import settings


class BaseAPIClient:
    """Base class for all API clients with common functionality."""
    
    def __init__(self, api_request_context: APIRequestContext, base_url: Optional[str] = None, logger: Optional[logging.Logger] = None):
        """
        Initialize the API client.
        
        Args:
            api_request_context: Playwright API request context
            base_url: Optional base URL override (takes precedence over settings)
            logger: Optional logger instance
        """
        self.api_request_context = api_request_context
        self.logger = logger or logging.getLogger(__name__)
        
        # Priority: 1. Explicit base_url parameter, 2. Environment variable, 3. Default settings
        if base_url:
            self.base_url = base_url
        else:
            # Check environment variables at runtime for CLI overrides
            env_base_url = os.getenv('POKEAPI_BASE_URL') or os.getenv('TEST_BASE_URL')
            self.base_url = env_base_url or settings.base_url
        
        self.logger.info(f"BaseAPIClient initialized with base_url: {self.base_url}")
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make a GET request to the specified endpoint.
        
        Args:
            endpoint: API endpoint path (e.g., '/pokemon/1')
            params: Optional query parameters
            
        Returns:
            Response data as dictionary
            
        Raises:
            Exception: If the request fails
        """
        # Build full URL using configured base URL
        full_url = f"{self.base_url.rstrip('/')}{endpoint}"
        self.logger.info(f"Making GET request to {full_url} with params: {params}")
        
        try:
            response = self.api_request_context.get(full_url, params=params)
            
            self.logger.info(f"Response status: {response.status}")
            self.logger.info(f"Response URL: {response.url}")
            
            # Check if response is successful
            if not response.ok:
                self.logger.error(f"HTTP {response.status} error for {full_url}")
                raise Exception(f"HTTP {response.status} error for {full_url}")
            
            data = response.json()
            
            self.logger.info(f"Successfully retrieved data from {full_url}")
            return data
            
        except Exception as e:
            self.logger.error(f"Failed to make GET request to {full_url}: {str(e)}")
            raise
