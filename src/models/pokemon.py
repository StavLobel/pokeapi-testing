"""
Pydantic models for Pokémon data validation.
"""

from typing import List, Optional, Any
from pydantic import BaseModel, Field, field_validator


class NamedAPIResource(BaseModel):
    """Model for a named API resource reference."""
    
    name: str = Field(..., description="The name of the referenced resource")
    url: str = Field(..., description="The URL of the referenced resource")


class PokemonAbility(BaseModel):
    """Model for Pokémon ability data."""
    
    ability: NamedAPIResource = Field(..., description="Ability reference")
    is_hidden: bool = Field(..., description="Whether the ability is hidden")
    slot: int = Field(..., ge=0, description="Ability slot number")


class PokemonMove(BaseModel):
    """Model for Pokémon move data."""
    
    move: NamedAPIResource = Field(..., description="Move reference")
    version_group_details: List[dict] = Field(..., description="Version group details")


class PokemonType(BaseModel):
    """Model for Pokémon type data."""
    
    slot: int = Field(..., ge=1, description="Type slot number")
    type: NamedAPIResource = Field(..., description="Type reference")


class PokemonStat(BaseModel):
    """Model for Pokémon stat data."""
    
    base_stat: int = Field(..., ge=0, description="Base stat value")
    effort: int = Field(..., ge=0, description="Effort value")
    stat: NamedAPIResource = Field(..., description="Stat reference")


class PokemonSprites(BaseModel):
    """Model for Pokémon sprites data."""
    
    front_default: Optional[str] = Field(None, description="Default front sprite URL")
    front_shiny: Optional[str] = Field(None, description="Shiny front sprite URL")
    front_female: Optional[str] = Field(None, description="Female front sprite URL")
    front_shiny_female: Optional[str] = Field(None, description="Shiny female front sprite URL")
    back_default: Optional[str] = Field(None, description="Default back sprite URL")
    back_shiny: Optional[str] = Field(None, description="Shiny back sprite URL")
    back_female: Optional[str] = Field(None, description="Female back sprite URL")
    back_shiny_female: Optional[str] = Field(None, description="Shiny female back sprite URL")


class Pokemon(BaseModel):
    """Model for Pokémon data validation."""
    
    id: int = Field(..., ge=1, description="Pokémon ID")
    name: str = Field(..., min_length=1, description="Pokémon name")
    height: int = Field(..., gt=0, description="Pokémon height in decimeters")
    weight: int = Field(..., gt=0, description="Pokémon weight in hectograms")
    base_experience: int = Field(..., ge=0, description="Base experience value")
    abilities: List[PokemonAbility] = Field(..., min_length=1, description="List of abilities")
    moves: List[PokemonMove] = Field(..., description="List of moves")
    types: List[PokemonType] = Field(..., min_length=1, max_length=2, description="List of types")
    stats: List[PokemonStat] = Field(..., min_length=6, max_length=6, description="List of stats")
    sprites: PokemonSprites = Field(..., description="Sprite URLs")
    species: NamedAPIResource = Field(..., description="Species reference")
    
    @field_validator('name')
    @classmethod
    def name_must_be_lowercase(cls, v):
        """Validate that name is lowercase."""
        if not v.islower():
            raise ValueError('Name must be lowercase')
        return v
