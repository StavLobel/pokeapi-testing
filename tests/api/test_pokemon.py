"""
Tests for Pokémon API endpoints.
"""

import pytest
from playwright.sync_api import APIRequestContext
from src.api.pokemon_client import PokemonAPIClient
from src.models.pokemon import Pokemon


class TestPokemon:
    """Test class for Pokémon API endpoints."""
    
    @pytest.fixture
    def pokemon_client(self, api_request_context: APIRequestContext) -> PokemonAPIClient:
        """Create a Pokémon API client for testing."""
        return PokemonAPIClient(api_request_context)
    
    def test_pok_01_retrieve_pokemon_by_valid_id(self, pokemon_client: PokemonAPIClient):
        """
        POK-01: Retrieve a Pokémon by valid ID → 200 OK with correct details.
        
        Test that retrieving a Pokémon by ID returns 200 OK with the correct
        Pokémon details including all required fields and proper schema.
        """
        # Arrange
        pokemon_id = 1  # Bulbasaur
        expected_name = "bulbasaur"
        
        # Act
        response_data = pokemon_client.get_pokemon_by_id(pokemon_id)
        
        # Assert
        # Validate response structure using Pydantic model
        pokemon = Pokemon.model_validate(response_data)
        
        # Verify basic fields
        assert pokemon.id == pokemon_id
        assert pokemon.name == expected_name
        assert pokemon.height > 0
        assert pokemon.weight > 0
        assert pokemon.base_experience > 0
        
        # Verify required arrays are present and not empty
        assert len(pokemon.abilities) > 0
        assert len(pokemon.moves) > 0
        assert len(pokemon.types) > 0
        assert len(pokemon.stats) > 0
        
        # Verify sprites object is present
        assert pokemon.sprites is not None
        
        # Verify species reference is present
        assert pokemon.species is not None
        
        # Verify ability structure
        for ability in pokemon.abilities:
            assert ability.ability is not None
            assert isinstance(ability.is_hidden, bool)
            assert isinstance(ability.slot, int)
            assert ability.slot >= 0
        
        # Verify type structure
        for pokemon_type in pokemon.types:
            assert pokemon_type.type is not None
            assert isinstance(pokemon_type.slot, int)
            assert pokemon_type.slot >= 0
        
        # Verify stats structure
        for stat in pokemon.stats:
            assert stat.stat is not None
            assert isinstance(stat.base_stat, int)
            assert isinstance(stat.effort, int)
            assert stat.base_stat >= 0
            assert stat.effort >= 0
