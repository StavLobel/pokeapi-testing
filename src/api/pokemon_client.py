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
