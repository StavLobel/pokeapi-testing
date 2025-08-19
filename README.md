# PokeAPI Testing Framework

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg?logo=python)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/playwright-1.37+-green.svg?logo=playwright)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/pytest-7.4+-yellow.svg?logo=pytest)](https://pytest.org/)
[![Pydantic](https://img.shields.io/badge/pydantic-2.0+-orange.svg)](https://pydantic.dev/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive Python-based API testing framework for PokéAPI v2 using Playwright's APIRequestContext and Pydantic for data validation.

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Playwright browsers

### Local Setup (5 minutes)

```bash
# 1) Clone the repo
git clone https://github.com/StavLobel/pokeapi-testing.git
cd pokeapi-testing

# 2) Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# 3) Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4) Install Playwright browsers
playwright install
```

### Installation (via Makefile shortcuts)
```bash
# Install dependencies
make install

# Setup development environment (includes Playwright browsers)
make setup

# Run all tests
make test
```

### Running Tests
```bash
# All tests
make test

# API tests only
make test-api

# Smoke tests only
make test-smoke

# Specific test categories
pytest -m smoke
pytest -m regression
```

## 🧪 Test Coverage

### PokéAPI v2 Endpoints
Based on the [Software Test Plan](docs/software-test-plan.md), the framework covers:

- **Pokémon**: Individual and list endpoints
- **Abilities**: Ability details and listings
- **Moves**: Move information and collections
- **Types**: Type data and relationships
- **Items**: Item details and listings
- **Berries**: Berry information
- **Machines**: Machine data
- **Evolution**: Evolution chains
- **Encounters**: Encounter data
- **Games**: Game information
- **Locations**: Location data
- **Regions**: Region information
- **Pokedexes**: Pokedex entries
- **Generations**: Generation data
- **Versions**: Version information

### Test Categories
- **Positive Tests**: Valid ID/name retrieval, pagination
- **Negative Tests**: Invalid IDs, error handling
- **Schema Tests**: Response structure validation
- **Cross-Resource Tests**: Reference integrity

## 🏗️ Architecture

Built with:
- **Playwright APIRequestContext** for HTTP requests
- **Pydantic** for data validation and modeling
- **SOLID principles** for maintainability
- **Type safety** with Python type hints
- **Structured logging** with correlation IDs

## ✨ Key Features

### 🧪 **Comprehensive API Testing**
- **REST API Testing**: Full HTTP request/response validation
- **Pydantic Validation**: Automatic response structure validation
- **Performance Testing**: Response time tracking and analysis
- **Error Handling**: Comprehensive error scenario testing

### 🚀 **Development Excellence**
- **Makefile Commands**: Streamlined development workflow
- **Quality Gates**: Automated code quality checks and validation

### 🛡️ **Code Quality**
- **Type Safety**: Full type checking for reliability
- **Code Formatting**: Automated formatting with Black
- **Clean Architecture**: SOLID principles and best practices

### 🏗️ **Architecture**
- **SOLID Principles**: Clean, maintainable, and extensible code
- **Structured Logging**: Correlation ID tracking and detailed execution logs
- **Environment Flexibility**: Support for local, CI, and staging environments
- **Pydantic Models**: Type-safe data validation and serialization

## 📚 Documentation

- [Software Test Plan](docs/software-test-plan.md) - Comprehensive testing strategy for PokéAPI v2
- [Test Cases](docs/test-cases.md) - Detailed test cases for each resource family
- [Development Guide](docs/README.md) - Setup and development guidelines

## 🔗 Links

- **📖 PokéAPI v2 Documentation**: [https://pokeapi.co/docs/v2](https://pokeapi.co/docs/v2)
- **🎭 Playwright Documentation**: [https://playwright.dev/](https://playwright.dev/)
- **🐍 Pydantic Documentation**: [https://pydantic.dev/](https://pydantic.dev/)

---

**Built with ❤️ using Playwright, Python, and Pydantic**
