"""
Tests for Pokémon API endpoints.
"""

import pytest
from playwright.sync_api import APIRequestContext
from src.api.pokemon_client import PokemonAPIClient
from src.models.pokemon import Pokemon
from testdata.pokemon_test_data import (
    VALID_POKEMON_BY_ID,
    # STASHED: VALID_POKEMON_BY_NAME,
    # STASHED: INVALID_POKEMON_IDS,
    # STASHED: INVALID_POKEMON_NAMES,
    # STASHED: EXPECTED_STAT_NAMES
)


class TestPokemon:
    """Test class for Pokémon API endpoints."""
    
    def _validate_pokemon_structure(self, pokemon: Pokemon, expected_id: int, expected_name: str):
        """
        Helper method to validate basic Pokémon structure.
        
        Args:
            pokemon: Validated Pokémon model
            expected_id: Expected Pokémon ID
            expected_name: Expected Pokémon name
        """
        # Verify basic fields
        assert pokemon.id == expected_id
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
    
    @pytest.mark.api
    @pytest.mark.pokemon
    @pytest.mark.parametrize("pokemon_id, expected_name", VALID_POKEMON_BY_ID)
    def test_pok_01_retrieve_pokemon_by_valid_id(self, pokemon_client: PokemonAPIClient, pokemon_id: int, expected_name: str):
        """
        POK-01: Retrieve a Pokémon by valid ID → 200 OK with correct details.
        
        Test that retrieving a Pokémon by ID returns 200 OK with the correct
        Pokémon details including all required fields and proper schema.
        
        Args:
            pokemon_client: API client for Pokémon endpoints
            pokemon_id: The Pokémon ID to test
            expected_name: Expected Pokémon name
        """
        # Act
        response_data = pokemon_client.get_pokemon_by_id(pokemon_id)
        
        # Assert
        # Validate response structure using Pydantic model
        pokemon = Pokemon.model_validate(response_data)
        
        # Use helper method for comprehensive validation
        self._validate_pokemon_structure(pokemon, pokemon_id, expected_name)

    @pytest.mark.api
    @pytest.mark.pokemon
    def test_pok_cli_base_url_override(self, pokemon_client: PokemonAPIClient, dynamic_settings: dict):
        """
        Test that CLI base URL override is working correctly.
        
        This test verifies that when --api-base-url is provided via CLI,
        the API client actually uses the overridden URL instead of the default.
        
        Args:
            pokemon_client: API client for Pokémon endpoints
            dynamic_settings: Dynamic settings fixture with CLI overrides
        """
        # Get the CLI override if provided
        cli_base_url = dynamic_settings.get('cli_base_url')
        
        if cli_base_url:
            # If CLI override is provided, verify the client is using it
            expected_base_url = cli_base_url.rstrip('/')
            actual_base_url = pokemon_client.base_url.rstrip('/')
            
            assert actual_base_url == expected_base_url, (
                f"CLI override not working. Expected: {expected_base_url}, Got: {actual_base_url}"
            )
            
            # Log the override for debugging
            print(f"✅ CLI override working! Client using: {actual_base_url}")
        else:
            # If no CLI override, verify default behavior
            expected_base_url = "https://pokeapi.co/api/v2"
            actual_base_url = pokemon_client.base_url.rstrip('/')
            
            assert actual_base_url == expected_base_url, (
                f"Default base URL not working. Expected: {expected_base_url}, Got: {actual_base_url}"
            )

    # ============================================================================
    # STASHED TEST CASES - Uncomment when ready to implement
    # ============================================================================
    
    # @pytest.mark.api
    # @pytest.mark.pokemon
    # @pytest.mark.parametrize("pokemon_name, expected_id", VALID_POKEMON_BY_NAME)
    # def test_pok_02_retrieve_pokemon_by_valid_name(self, pokemon_client: PokemonAPIClient, pokemon_name: str, expected_id: int):
    #     """
    #     POK-02: Retrieve a Pokémon by valid name → 200 OK with correct details.
    #     
    #     Test that retrieving a Pokémon by name returns 200 OK with the correct
    #     Pokémon details including all required fields and proper schema.
    #     
    #     Args:
    #         pokemon_client: API client for Pokémon endpoints
    #         pokemon_name: The Pokémon name to test
    #         expected_id: Expected Pokémon ID
    #     """
    #     # Act
    #         pokemon_client.get_pokemon_by_name(pokemon_name)
    #         
    #         # Assert
    #         # Validate response structure using Pydantic model
    #         pokemon = Pokemon.model_validate(response_data)
    #         
    #         # Use helper method for comprehensive validation
    #         self._validate_pokemon_structure(pokemon, expected_id, pokemon_name)
    
    # @pytest.mark.api
    # @pytest.mark.pokemon
    # @pytest.mark.parametrize("pokemon_id, expected_name", VALID_POKEMON_BY_ID)
    # def test_pok_06_schema_validation(self, pokemon_client: PokemonAPIClient, pokemon_id: int, expected_name: str):
    #     """
    #     POK-06: Schema correctness.
    #     
    #         Test that the Pokémon response has the correct schema structure,
    #         including all required fields and proper data types.
    #         
    #         Args:
    #             pokemon_client: API client for Pokémon endpoints
    #             pokemon_id: The Pokémon ID to test
    #             expected_name: Expected Pokémon name
    #         """
    #         # Act
    #         response_data = pokemon_client.get_pokemon_by_id(pokemon_id)
    #         
    #         # Assert - Pydantic validation will raise ValidationError if schema is incorrect
    #         pokemon = Pokemon.model_validate(response_data)
    #         
    #         # Verify specific schema requirements
    #         assert len(pokemon.stats) == 6, "Pokémon must have exactly 6 stats"
    #         
    #         # Verify all expected stats are present
    #         stat_names = [stat.stat.name for stat in pokemon.stats]
    #         for expected_stat in EXPECTED_STAT_NAMES:
    #             assert expected_stat in stat_names, f"Missing expected stat: {expected_stat}"
    #         
    #         # Verify types (1 or 2 types)
    #         assert 1 <= len(pokemon.types) <= 2, "Pokémon must have 1 or 2 types"
    #         
    #         # Verify abilities (at least 1)
    #         assert len(pokemon.abilities) >= 1, "Pokémon must have at least 1 ability"
    
    # @pytest.mark.api
    # @pytest.mark.pokemon
    # @pytest.mark.parametrize("invalid_id", INVALID_POKEMON_IDS)
    # def test_pok_08_retrieve_pokemon_by_invalid_id(self, pokemon_client: PokemonAPIClient, invalid_id: int):
    #     """
    #     POK-08: Non-existent Pokémon → 404 Not Found.
    #         
    #         Test that retrieving a Pokémon with an invalid ID returns 404 Not Found.
    #         
    #         Args:
    #             pokemon_client: API client for Pokémon endpoints
    #             invalid_id: Invalid Pokémon ID to test
    #         """
    #         # Act & Assert
    #         with pytest.raises(Exception) as exc_info:
    #             pokemon_client.get_pokemon_by_id(invalid_id)
    #         
    #         # Verify it's a 404 error
    #         assert "404" in str(exc_info.value)
    
    # @pytest.mark.api
    # @pytest.mark.pokemon
    # @pytest.mark.parametrize("invalid_name", INVALID_POKEMON_NAMES)
    # def test_pok_08_retrieve_pokemon_by_invalid_name(self, pokemon_client: PokemonAPIClient, invalid_name: str):
    #         """
    #         POK-08: Non-existent Pokémon → 404 Not Found.
    #         
    #         Test that retrieving a Pokémon with an invalid name returns 404 Not Found.
    #         
    #         Args:
    #             pokemon_client: API client for Pokémon endpoints
    #             invalid_name: Invalid Pokémon name to test
    #         """
    #         # Act & Assert
    #         with pytest.raises(Exception) as exc_info:
    #             pokemon_client.get_pokemon_by_name(invalid_name)
    #         
    #         # Verify it's a 404 error
    #         assert "404" in str(exc_info.value)
