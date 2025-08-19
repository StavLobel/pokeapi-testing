"""
Pydantic models for PokéAPI v2 data validation.
"""

# Base models (shared across resource families)
from .base import (
    NamedAPIResource,
    APIResource,
    Name,
    Description,
    FlavorText,
    Effect,
    VersionGameIndex,
    MachineVersionDetail,
    VerboseEffect,
    VersionGroupFlavorText,
    GenerationGameIndex,
    Encounter,
    EncounterMethodRate,
    EncounterVersionDetail,
    PokemonEncounter,
    VersionEncounterDetail,
)

# Resource-specific models
from .pokemon import (
    PokemonAbility,
    PokemonMove,
    PokemonType,
    PokemonStat,
    PokemonSprites,
    Pokemon,
)

__all__ = [
    # Base models
    "NamedAPIResource",
    "APIResource", 
    "Name",
    "Description",
    "FlavorText",
    "Effect",
    "VersionGameIndex",
    "MachineVersionDetail",
    "VerboseEffect",
    "VersionGroupFlavorText",
    "GenerationGameIndex",
    "Encounter",
    "EncounterMethodRate",
    "EncounterVersionDetail",
    "PokemonEncounter",
    "VersionEncounterDetail",
    # Pokémon models
    "PokemonAbility",
    "PokemonMove", 
    "PokemonType",
    "PokemonStat",
    "PokemonSprites",
    "Pokemon",
]
