"""
Pydantic models for Pokémon data validation.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class PokemonAbility(BaseModel):
    """Model for Pokémon ability data."""
    
    ability: dict = Field(..., description="Ability reference")
    is_hidden: bool = Field(..., description="Whether the ability is hidden")
    slot: int = Field(..., description="Ability slot number")


class PokemonMove(BaseModel):
    """Model for Pokémon move data."""
    
    move: dict = Field(..., description="Move reference")
    version_group_details: List[dict] = Field(..., description="Version group details")


class PokemonType(BaseModel):
    """Model for Pokémon type data."""
    
    slot: int = Field(..., description="Type slot number")
    type: dict = Field(..., description="Type reference")


class PokemonStat(BaseModel):
    """Model for Pokémon stat data."""
    
    base_stat: int = Field(..., description="Base stat value")
    effort: int = Field(..., description="Effort value")
    stat: dict = Field(..., description="Stat reference")


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
    
    id: int = Field(..., description="Pokémon ID")
    name: str = Field(..., description="Pokémon name")
    height: int = Field(..., description="Pokémon height in decimeters")
    weight: int = Field(..., description="Pokémon weight in hectograms")
    base_experience: int = Field(..., description="Base experience value")
    abilities: List[PokemonAbility] = Field(..., description="List of abilities")
    moves: List[PokemonMove] = Field(..., description="List of moves")
    types: List[PokemonType] = Field(..., description="List of types")
    stats: List[PokemonStat] = Field(..., description="List of stats")
    sprites: PokemonSprites = Field(..., description="Sprite URLs")
    species: dict = Field(..., description="Species reference")
