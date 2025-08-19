# PokeAPI Testing Framework Documentation

## Overview

This framework provides comprehensive API testing for the PokeAPI using Playwright's APIRequestContext and JSON Schema validation.

## Quick Start

1. **Install dependencies:**
   ```bash
   make install
   ```

2. **Setup environment:**
   ```bash
   make setup
   ```

3. **Run tests:**
   ```bash
   make test-api
   ```

4. **Generate reports:**
   ```bash
   make allure
   ```

## Project Structure

```
pokeapi-testing/
├── src/
│   ├── api/              # API client classes
│   ├── config/           # Configuration settings
│   └── utils/            # Utility functions
├── tests/
│   └── api/              # API test files
├── schemas/              # JSON Schema definitions
├── docs/                 # Documentation
└── testdata/             # Test data files
```

## Key Features

- **Playwright APIRequestContext** for HTTP requests
- **JSON Schema validation** for response validation
- **Allure reporting** for test results
- **Pytest framework** for test execution
- **Type safety** with Python type hints

## Test Categories

- **Smoke Tests** (`@pytest.mark.smoke`): Critical functionality tests
- **API Tests** (`@pytest.mark.api`): All API endpoint tests
- **Schema Tests** (`@pytest.mark.schema`): JSON Schema validation tests

## Available Commands

- `make help` - Show available commands
- `make install` - Install dependencies
- `make setup` - Setup development environment
- `make test` - Run all tests
- `make test-api` - Run API tests only
- `make test-smoke` - Run smoke tests only
- `make allure` - Generate Allure report
- `make clean` - Clean up generated files
