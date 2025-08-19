"""
Base Pydantic models for PokéAPI v2 data validation.
These models are shared across multiple resource families.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class NamedAPIResource(BaseModel):
    """Model for a named API resource reference."""
    
    name: str = Field(..., description="The name of the referenced resource")
    url: str = Field(..., description="The URL of the referenced resource")


class APIResource(BaseModel):
    """Model for an unnamed API resource reference."""
    
    url: str = Field(..., description="The URL of the referenced resource")


class Name(BaseModel):
    """Model for localized names."""
    
    name: str = Field(..., description="The localized name")
    language: NamedAPIResource = Field(..., description="The language this name is in")


class Description(BaseModel):
    """Model for localized descriptions."""
    
    description: str = Field(..., description="The localized description")
    language: NamedAPIResource = Field(..., description="The language this description is in")


class FlavorText(BaseModel):
    """Model for localized flavor text."""
    
    flavor_text: str = Field(..., description="The localized flavor text")
    language: NamedAPIResource = Field(..., description="The language this flavor text is in")
    version: NamedAPIResource = Field(..., description="The version this flavor text is from")


class Effect(BaseModel):
    """Model for effect entries."""
    
    effect: str = Field(..., description="The localized effect text")
    language: NamedAPIResource = Field(..., description="The language this effect is in")
    short_effect: Optional[str] = Field(None, description="The localized short effect text")


class VersionGameIndex(BaseModel):
    """Model for version game indices."""
    
    game_index: int = Field(..., description="The internal id of an API resource within game data")
    version: NamedAPIResource = Field(..., description="The version relevent to this game index")


class MachineVersionDetail(BaseModel):
    """Model for machine version details."""
    
    machine: APIResource = Field(..., description="The machine that teaches a move from an item")
    version_group: NamedAPIResource = Field(..., description="The version group of this specific machine")


class VerboseEffect(BaseModel):
    """Model for verbose effect entries."""
    
    effect: str = Field(..., description="The localized effect text")
    short_effect: str = Field(..., description="The localized short effect text")
    language: NamedAPIResource = Field(..., description="The language this effect is in")


class VersionGroupFlavorText(BaseModel):
    """Model for version group flavor text."""
    
    text: str = Field(..., description="The localized name for an API resource in a specific language")
    language: NamedAPIResource = Field(..., description="The language this name is in")
    version_group: NamedAPIResource = Field(..., description="The version group which uses this flavor text")


class GenerationGameIndex(BaseModel):
    """Model for generation game indices."""
    
    game_index: int = Field(..., description="The internal id of an API resource within game data")
    generation: NamedAPIResource = Field(..., description="The generation relevent to this game index")


class Encounter(BaseModel):
    """Model for encounters."""
    
    min_level: int = Field(..., description="The lowest level the Pokémon could be encountered at")
    max_level: int = Field(..., description="The highest level the Pokémon could be encountered at")
    condition_values: List[NamedAPIResource] = Field(..., description="A list of condition values that must be in effect for this encounter to occur")
    chance: int = Field(..., description="Percent chance that this encounter will occur")
    method: NamedAPIResource = Field(..., description="The method by which this encounter happens")


class EncounterMethodRate(BaseModel):
    """Model for encounter method rates."""
    
    encounter_method: NamedAPIResource = Field(..., description="The method in which Pokémon may be encountered in an area")
    version_details: List['EncounterVersionDetail'] = Field(..., description="The chance of the encounter to occur on a version of the game")


class EncounterVersionDetail(BaseModel):
    """Model for encounter version details."""
    
    rate: int = Field(..., description="The chance of an encounter to occur")
    version: NamedAPIResource = Field(..., description="The version of the game in which the encounter can occur")


class PokemonEncounter(BaseModel):
    """Model for Pokémon encounters."""
    
    pokemon: NamedAPIResource = Field(..., description="The Pokémon being encountered")
    version_details: List['VersionEncounterDetail'] = Field(..., description="A list of versions and encounters with Pokémon that might happen in the referenced location area")


class VersionEncounterDetail(BaseModel):
    """Model for version encounter details."""
    
    version: NamedAPIResource = Field(..., description="The game version this encounter happens in")
    max_chance: int = Field(..., description="The total chance, summed from all encounter potential, of having an encounter")
    encounter_details: List['Encounter'] = Field(..., description="A list of encounters and their specifics")
