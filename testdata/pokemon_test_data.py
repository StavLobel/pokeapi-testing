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
