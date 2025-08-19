# 📋 Schema Organization Guide

## **📁 Schema Location**

All Pydantic schemas for PokéAPI v2 data validation are stored in the `src/models/` directory.

## **🏗️ Directory Structure**

```
src/models/
├── __init__.py          # Package exports and imports
├── base.py              # Shared base models (NamedAPIResource, etc.)
├── pokemon.py           # Pokémon-specific schemas ✅
├── abilities.py         # Abilities-specific schemas ⏳
├── moves.py             # Moves-specific schemas ⏳
├── types.py             # Types-specific schemas ⏳
├── items.py             # Items-specific schemas ⏳
├── berries.py           # Berries-specific schemas ⏳
├── machines.py          # Machines-specific schemas ⏳
├── evolution.py         # Evolution-specific schemas ⏳
├── encounters.py        # Encounters-specific schemas ⏳
├── games.py             # Games-specific schemas ⏳
├── locations.py         # Locations-specific schemas ⏳
├── regions.py           # Regions-specific schemas ⏳
├── pokedexes.py         # Pokedexes-specific schemas ⏳
├── generations.py       # Generations-specific schemas ⏳
└── versions.py          # Versions-specific schemas ⏳
```

## **🔧 Base Models (`src/models/base.py`)**

These models are shared across multiple resource families:

### **Core Reference Models:**
- **`NamedAPIResource`** - Named resource references (name + URL)
- **`APIResource`** - Unnamed resource references (URL only)

### **Localization Models:**
- **`Name`** - Localized names with language info
- **`Description`** - Localized descriptions
- **`FlavorText`** - Localized flavor text with version info
- **`Effect`** - Effect entries with optional short effects
- **`VerboseEffect`** - Detailed effect entries

### **Game Data Models:**
- **`VersionGameIndex`** - Version-specific game indices
- **`GenerationGameIndex`** - Generation-specific game indices
- **`MachineVersionDetail`** - Machine version details

### **Encounter Models:**
- **`Encounter`** - Basic encounter information
- **`EncounterMethodRate`** - Encounter method rates
- **`EncounterVersionDetail`** - Version-specific encounter details
- **`PokemonEncounter`** - Pokémon-specific encounters
- **`VersionEncounterDetail`** - Version-specific encounter details

## **🎯 Resource-Specific Models**

### **Pokémon Models (`src/models/pokemon.py`)**
- **`PokemonAbility`** - Pokémon ability data
- **`PokemonMove`** - Pokémon move data
- **`PokemonType`** - Pokémon type data
- **`PokemonStat`** - Pokémon stat data
- **`PokemonSprites`** - Pokémon sprite URLs
- **`Pokemon`** - Complete Pokémon data model

### **Future Resource Models:**
Each resource family will have its own file with specific models:

- **`src/models/abilities.py`** - Ability models
- **`src/models/moves.py`** - Move models
- **`src/models/types.py`** - Type models
- **`src/models/items.py`** - Item models
- **`src/models/berries.py`** - Berry models
- **`src/models/machines.py`** - Machine models
- **`src/models/evolution.py`** - Evolution models
- **`src/models/encounters.py`** - Encounter models
- **`src/models/games.py`** - Game models
- **`src/models/locations.py`** - Location models
- **`src/models/regions.py`** - Region models
- **`src/models/pokedexes.py`** - Pokédex models
- **`src/models/generations.py`** - Generation models
- **`src/models/versions.py`** - Version models

## **📦 Package Exports (`src/models/__init__.py`)**

The `__init__.py` file exports all models for easy importing:

```python
# Import base models
from src.models import NamedAPIResource, APIResource, Name

# Import resource-specific models
from src.models import Pokemon, PokemonAbility, PokemonType
```

## **🔍 Usage Examples**

### **Importing Models:**
```python
# Import specific models
from src.models.pokemon import Pokemon, PokemonAbility
from src.models.base import NamedAPIResource

# Import from package
from src.models import Pokemon, NamedAPIResource
```

### **Using Models for Validation:**
```python
from src.models.pokemon import Pokemon

# Validate API response
response_data = api_client.get_pokemon_by_id(1)
pokemon = Pokemon.model_validate(response_data)

# Access validated data
print(f"Pokémon: {pokemon.name} (ID: {pokemon.id})")
print(f"Types: {[t.type.name for t in pokemon.types]}")
```

### **Creating Test Data:**
```python
from src.models.base import NamedAPIResource

# Create test data
ability_ref = NamedAPIResource(
    name="overgrow",
    url="https://pokeapi.co/api/v2/ability/65/"
)
```

## **🎨 Schema Design Principles**

### **1. Reusability:**
- Base models are shared across resource families
- Common patterns (NamedAPIResource, localization) are standardized

### **2. Type Safety:**
- All models use Pydantic for validation
- Field constraints ensure data integrity
- Type hints provide IDE support

### **3. Documentation:**
- Each model has descriptive docstrings
- Field descriptions explain purpose and constraints
- Examples show proper usage

### **4. Validation:**
- Field constraints (min_length, ge, etc.) ensure data quality
- Custom validators handle complex business rules
- Error messages are clear and helpful

## **🚀 Best Practices**

### **Creating New Schemas:**
1. **Check base models first** - Use existing shared models when possible
2. **Follow naming conventions** - ResourceName + ModelType (e.g., `PokemonAbility`)
3. **Add proper validation** - Use Field constraints and custom validators
4. **Document thoroughly** - Include docstrings and field descriptions
5. **Update exports** - Add new models to `__init__.py`

### **Schema Organization:**
1. **One file per resource family** - Keep related models together
2. **Base models in base.py** - Share common patterns
3. **Clear imports** - Use explicit imports for clarity
4. **Consistent structure** - Follow established patterns

### **Testing Schemas:**
1. **Validate real API responses** - Test with actual PokéAPI data
2. **Test edge cases** - Invalid data, missing fields, etc.
3. **Test constraints** - Ensure validation rules work correctly
4. **Test serialization** - Verify model.dict() and model.json() work

## **📚 References**

- [Pydantic Documentation](https://docs.pydantic.dev/)
- [PokéAPI v2 Documentation](https://pokeapi.co/docs/v2)
- [Test Cases](docs/test-cases.md)
- [Software Test Plan](docs/software-test-plan.md)
