"""
Test data for Pokémon API tests.
"""

# Test data for valid Pokémon retrieval tests
VALID_POKEMON_BY_ID = [
    (1, "bulbasaur"),
    (25, "pikachu"), 
    (150, "mewtwo"),
    (493, "arceus"),  # High ID to test range
]

VALID_POKEMON_BY_NAME = [
    ("bulbasaur", 1),
    ("pikachu", 25),
    ("mewtwo", 150),
    ("arceus", 493),
]

# Test data for invalid scenarios
INVALID_POKEMON_IDS = [
    -1,    # Negative ID
    0,     # Zero ID
    99999, # Very high ID (likely non-existent)
]

INVALID_POKEMON_NAMES = [
    "not-a-pokemon",
    "invalid-name-123",
    "nonexistent-pokemon",
]

# Expected stat names for validation
EXPECTED_STAT_NAMES = [
    "hp",
    "attack", 
    "defense",
    "special-attack",
    "special-defense",
    "speed"
]

# Test data for pagination tests
PAGINATION_TEST_CASES = [
    # (limit, offset, expected_count, description)
    (5, 0, 5, "First 5 Pokémon"),
    (10, 0, 10, "First 10 Pokémon"),
    (20, 0, 20, "First 20 Pokémon"),
    (5, 5, 5, "Next 5 Pokémon (offset 5)"),
    (10, 20, 10, "10 Pokémon starting from offset 20"),
    (1, 0, 1, "Single Pokémon"),
    (0, 0, 0, "Zero limit"),
]

# Test data for boundary pagination tests
BOUNDARY_PAGINATION_CASES = [
    # (limit, offset, description)
    (0, 0, "Zero limit"),
    (1, 0, "Minimum limit"),
    (100, 0, "Large limit"),
    (1000, 0, "Very large limit"),
    (0, 1000, "Zero limit with large offset"),
    (1, 1000, "Single item with large offset"),
]

# Test data for invalid pagination inputs
INVALID_PAGINATION_CASES = [
    # (limit, offset, description)
    (-1, 0, "Negative limit"),
    (0, -1, "Negative offset"),
    (-5, -10, "Both negative"),
    ("abc", 0, "String limit"),
    (0, "xyz", "String offset"),
    (None, 0, "None limit"),
    (0, None, "None offset"),
]

# Test data for HTTP method testing
HTTP_METHODS_TO_TEST = [
    "POST",
    "PUT", 
    "DELETE",
    "PATCH",
]

# Test data for cross-resource validation
CROSS_RESOURCE_TEST_CASES = [
    # (pokemon_id, pokemon_name, expected_abilities, expected_types, expected_moves)
    (1, "bulbasaur", ["overgrow", "chlorophyll"], ["grass", "poison"], ["razor-wind", "swords-dance", "cut"]),
    (25, "pikachu", ["static", "lightning-rod"], ["electric"], ["mega-punch", "pay-day", "thunder-punch"]),
    (6, "charizard", ["blaze", "solar-power"], ["fire", "flying"], ["mega-punch", "fire-punch", "thunder-punch"]),
]

# Test data for server error simulation (these might trigger 5xx errors)
SERVER_ERROR_TEST_CASES = [
    # (pokemon_id, description)
    (999999, "Very high ID that might cause server issues"),
    (0, "Zero ID edge case"),
    (-999999, "Very negative ID edge case"),
]

# Test data for response header validation
HEADER_TEST_CASES = [
    # (header_name, expected_value, description)
    ("content-type", "application/json", "JSON content type"),
    ("cache-control", None, "Cache control header (may vary)"),
    ("server", None, "Server header (may vary)"),
]
