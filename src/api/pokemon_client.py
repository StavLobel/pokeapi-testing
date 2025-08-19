"""
Pokémon API client for PokéAPI v2.
"""

from typing import Dict, Any, Optional
from ..core.base_api_client import BaseAPIClient


class PokemonAPIClient(BaseAPIClient):
    """API client for Pokémon endpoints."""
    
    def get_pokemon_by_id(self, pokemon_id: int) -> Dict[str, Any]:
        """
        Retrieve a Pokémon by its ID.
        
        Args:
            pokemon_id: The Pokémon ID (e.g., 1 for Bulbasaur)
            
        Returns:
            Pokémon data as dictionary
            
        Raises:
            Exception: If the request fails
        """
        endpoint = f"/pokemon/{pokemon_id}"
        return self.get(endpoint)
    
    def get_pokemon_by_name(self, pokemon_name: str) -> Dict[str, Any]:
        """
        Retrieve a Pokémon by its name.
        
        Args:
            pokemon_name: The Pokémon name (e.g., 'bulbasaur')
            
        Returns:
            Pokémon data as dictionary
            
        Raises:
            Exception: If the request fails
        """
        endpoint = f"/pokemon/{pokemon_name}"
        return self.get(endpoint)
    
    def list_pokemon(self, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
        """
        List Pokémon with optional pagination.
        
        Args:
            limit: Maximum number of results to return
            offset: Number of results to skip
            
        Returns:
            List of Pokémon resources as dictionary
            
        Raises:
            Exception: If the request fails
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
            
        return self.get("/pokemon", params=params)
    
    def test_http_method(self, method: str, pokemon_id: int = 1) -> Dict[str, Any]:
        """
        Test different HTTP methods on Pokémon endpoints.
        
        Args:
            method: HTTP method to test (POST, PUT, DELETE, etc.)
            pokemon_id: Pokémon ID to test against
            
        Returns:
            Response data as dictionary
            
        Raises:
            Exception: If the request fails
        """
        endpoint = f"/pokemon/{pokemon_id}"
        
        if method.upper() == "POST":
            return self.post(endpoint, data={})
        elif method.upper() == "PUT":
            return self.put(endpoint, data={})
        elif method.upper() == "DELETE":
            return self.delete(endpoint)
        elif method.upper() == "PATCH":
            return self.patch(endpoint, data={})
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
    
    def get_pokemon_with_headers(self, pokemon_id: int) -> Dict[str, Any]:
        """
        Get Pokémon with custom headers for testing.
        
        Args:
            pokemon_id: The Pokémon ID
            
        Returns:
            Pokémon data as dictionary
            
        Raises:
            Exception: If the request fails
        """
        endpoint = f"/pokemon/{pokemon_id}"
        headers = {"Accept": "application/json"}
        return self.get(endpoint, headers=headers)
