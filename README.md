# PokeAPI Testing Framework

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg?logo=python)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/playwright-1.37+-green.svg?logo=playwright)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/pytest-7.4+-yellow.svg?logo=pytest)](https://pytest.org/)
[![Pydantic](https://img.shields.io/badge/pydantic-2.0+-orange.svg)](https://pydantic.dev/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Type Check](https://img.shields.io/badge/type%20check-mypy-blue.svg)](https://mypy.readthedocs.io/)
[![Security](https://img.shields.io/badge/security-bandit%20%7C%20safety-red.svg)](https://bandit.readthedocs.io/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue.svg)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A comprehensive Python-based API testing framework for PokéAPI v2 using Playwright's APIRequestContext and Pydantic for data validation. Built with enterprise-grade quality standards, security scanning, performance monitoring, and multi-environment deployment support.

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Playwright browsers
- Docker (optional, for containerized testing)

### Local Setup (5 minutes)

```bash
# 1) Clone the repo
git clone https://github.com/StavLobel/pokeapi-testing.git
cd pokeapi-testing

# 2) Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# 3) Install dependencies and setup
make setup
```

### Installation (via Makefile shortcuts)
```bash
# Install dependencies
make install

# Setup development environment (includes Playwright browsers and pre-commit hooks)
make setup

# Run all tests
make test

# Run quality checks (linting, type checking, security scanning)
make quality
```

### Running Tests
```bash
# All tests
make test

# API tests only
make test-api

# Smoke tests only
make test-smoke

# Performance tests
make test-performance

# Security tests
make test-security

# Specific test categories
pytest -m smoke
pytest -m regression
pytest -m performance
```

## 🧪 Test Coverage

### Current Implementation Status
- **✅ Pokémon Resource Family**: 4/10 test cases implemented
  - POK-01: Retrieve Pokémon by valid ID ✅
  - POK-02: Retrieve Pokémon by valid name ✅
  - POK-06: Schema validation ✅
  - POK-08: Error handling (404) ✅
  - POK-03, POK-04, POK-05, POK-07, POK-09, POK-10, POK-11, POK-12: Pending

### Planned PokéAPI v2 Endpoints
Based on the [Software Test Plan](docs/software-test-plan.md), the framework will cover:

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
- **Performance Tests**: Response time and throughput monitoring
- **Security Tests**: Vulnerability scanning and security validation

## 🏗️ Architecture

### Core Components
- **Playwright APIRequestContext** for HTTP requests
- **Pydantic** for data validation and modeling
- **SOLID principles** for maintainability
- **Type safety** with Python type hints
- **Structured logging** with correlation IDs

### Project Structure
```
pokeapi-testing/
├── src/
│   ├── api/           # API clients for each resource family
│   ├── config/        # Configuration management
│   ├── core/          # Base classes and framework components
│   ├── models/        # Pydantic data models
│   └── utils/         # Utilities and helpers
├── tests/
│   ├── api/           # API test suites
│   ├── security/      # Security test suites
│   └── conftest.py    # Pytest configuration
├── testdata/          # Test data and fixtures
├── docs/              # Documentation
└── .github/           # CI/CD workflows
```

## ⚙️ Configuration

### Configuration Sources
The framework supports multiple configuration sources with priority order:

1. **CLI Arguments** (highest priority) - `--api-base-url`
2. **Environment Variables** 
3. **Default Values** (lowest priority)

### Key Configuration Options

| Setting | Environment Variable | CLI Argument | Default | Description |
|---------|---------------------|--------------|---------|-------------|
| **Base URL** | `POKEAPI_BASE_URL` | `--api-base-url` | `https://pokeapi.co/api/v2` | API base URL for requests |
| **Timeout** | `POKEAPI_TIMEOUT` | - | `30000` | Request timeout in milliseconds |
| **Log Level** | `POKEAPI_LOG_LEVEL` | - | `INFO` | Logging verbosity |
| **Test Timeout** | `TEST_TIMEOUT` | - | `30` | Test timeout in seconds |
| **Parallel Workers** | `TEST_PARALLEL_WORKERS` | - | `4` | Number of parallel test workers |

### Quick Configuration Examples

```bash
# Override base URL for local development
export POKEAPI_BASE_URL="http://localhost:8000/api/v2"

# Increase timeout for slow environments
export POKEAPI_TIMEOUT="60000"

# Set debug logging
export POKEAPI_LOG_LEVEL="DEBUG"

# Run tests with custom settings
POKEAPI_BASE_URL="https://staging-api.example.com" make test
```

### CLI Arguments (Recommended for Quick Testing)

```bash
# Override base URL for local development
pytest --api-base-url=http://localhost:8000/api/v2

# Override base URL for staging
pytest --api-base-url=https://staging-api.example.com/api/v2

# Override base URL and run specific tests
pytest --api-base-url=http://localhost:8000/api/v2 tests/api/test_pokemon.py

# Combine with other pytest options
pytest --api-base-url=http://localhost:8000/api/v2 -v -k "test_pok_01"
```

### Environment-Specific Configurations

```bash
# Local development
POKEAPI_BASE_URL="http://localhost:8000/api/v2"
POKEAPI_TIMEOUT="10000"
POKEAPI_LOG_LEVEL="DEBUG"

# CI/CD environment
POKEAPI_BASE_URL="https://pokeapi.co/api/v2"
POKEAPI_TIMEOUT="30000"
POKEAPI_LOG_LEVEL="INFO"
TEST_PARALLEL_WORKERS="8"

# Staging environment
POKEAPI_BASE_URL="https://staging-pokeapi.example.com/api/v2"
POKEAPI_TIMEOUT="60000"
POKEAPI_LOG_LEVEL="WARNING"
```

For detailed configuration options, see [Configuration Guide](docs/configuration.md).

## ✨ Key Features

### 🧪 **Comprehensive API Testing**
- **REST API Testing**: Full HTTP request/response validation
- **Pydantic Validation**: Automatic response structure validation
- **Performance Testing**: Response time tracking and analysis
- **Error Handling**: Comprehensive error scenario testing
- **Parameterized Tests**: Data-driven testing with @pytest.mark.parametrize

### 🚀 **Development Excellence**
- **Makefile Commands**: Streamlined development workflow
- **Quality Gates**: Automated code quality checks and validation
- **Pre-commit Hooks**: Automated formatting and linting
- **Type Safety**: Full mypy type checking

### 🛡️ **Security & Quality**
- **Security Scanning**: Bandit and Safety for vulnerability detection
- **Code Quality**: Black, isort, flake8 for consistent code style
- **Type Safety**: Full type checking for reliability
- **Clean Architecture**: SOLID principles and best practices

### 📊 **Performance & Monitoring**
- **Performance Metrics**: Response time tracking and analysis
- **Performance Baselines**: Establish and monitor performance standards
- **Regression Detection**: Automated performance regression testing
- **Monitoring Integration**: CI/CD performance monitoring

### 🌐 **Deployment & Operations**
- **Multi-Environment Support**: Local, CI, staging, production configurations
- **Docker Containerization**: Containerized testing framework
- **Kubernetes Deployment**: Production deployment manifests
- **CI/CD Pipeline**: Automated testing and deployment

## 🔧 Development Workflow

### Quality Assurance
```bash
# Run all quality checks
make quality

# Individual quality checks
make lint          # Code formatting and linting
make type-check    # Type checking with mypy
make security-scan # Security vulnerability scanning
```

### Testing
```bash
# Run all tests
make test

# Specific test categories
make test-api       # API tests only
make test-smoke     # Smoke tests only
make test-performance # Performance tests
make test-security  # Security tests
```

### Performance Testing
```bash
# Generate performance baseline
make performance-baseline

# Check for performance regressions
make performance-regression
```

### Deployment
```bash
# Build Docker image
make docker-build

# Run tests in Docker
make docker-run

# Deploy to environments
make deploy-staging
make deploy-production
```

## 📚 Documentation

- [Software Test Plan](docs/software-test-plan.md) - Comprehensive testing strategy for PokéAPI v2
- [Test Cases](docs/test-cases.md) - Detailed test cases for each resource family
- [Schema Documentation](docs/schemas.md) - Pydantic model documentation and usage
- [Development Guide](docs/README.md) - Setup and development guidelines

## 🚀 CI/CD Pipeline

The project includes a comprehensive CI/CD pipeline with:

- **Automated Testing**: Linting, type checking, unit tests, integration tests
- **Security Scanning**: Dependency and code vulnerability scanning
- **Performance Testing**: Automated performance regression detection
- **Quality Gates**: Automated code quality enforcement
- **Multi-Environment Deployment**: Staging and production deployment automation

## 🔗 Links

- **📖 PokéAPI v2 Documentation**: [https://pokeapi.co/docs/v2](https://pokeapi.co/docs/v2)
- **🎭 Playwright Documentation**: [https://playwright.dev/](https://playwright.dev/)
- **🐍 Pydantic Documentation**: [https://pydantic.dev/](https://pydantic.dev/)
- **🔧 GitHub Issues**: [Project Issues](https://github.com/StavLobel/pokeapi-testing/issues)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following the project's coding standards
4. Run quality checks (`make quality`)
5. Run tests (`make test`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📋 TODO

### High Priority
- [ ] Complete Pokémon resource family test cases (6 remaining)
- [ ] Implement remaining 13 resource families
- [ ] Add performance metrics collection
- [ ] Implement security scanning

### Medium Priority
- [ ] Add multi-environment deployment
- [ ] Enhance Playwright expect() usage
- [ ] Create comprehensive test reporting
- [ ] Add cross-resource validation tests

### Low Priority
- [ ] Add UI testing capabilities
- [ ] Implement advanced performance testing
- [ ] Create test data management system
- [ ] Add API documentation generation

---

**Built with ❤️ using Playwright, Python, Pydantic, and enterprise-grade quality standards**
