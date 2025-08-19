# PokeAPI Testing Framework

[![CI/CD Pipeline](https://github.com/StavLobel/pokeapi-testing/actions/workflows/ci.yml/badge.svg)](https://github.com/StavLobel/pokeapi-testing/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg?logo=python)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/playwright-1.41+-green.svg?logo=playwright)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/pytest-8.0+-yellow.svg?logo=pytest)](https://pytest.org/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A comprehensive Python-based API testing framework using Playwright's APIRequestContext, featuring JSON Schema validation and seamless CI/CD integration.

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

# 4) Set up environment variables
cp docs/.env.example .env
```

### Installation (via Makefile shortcuts)
```bash
# Install dependencies
make install

# Setup development environment
make setup

# Run all tests
make test-all
```

### Running Tests
```bash
# All API tests
make test-api

# Specific test categories
pytest -m smoke
pytest -m regression

# CI pipeline
make ci
```

## 🧪 Test Coverage

### PokeAPI Tests
- **TC-API-001**: Verify Pokemon list endpoint returns valid data
- **TC-API-002**: Verify specific Pokemon details endpoint
- **TC-API-003**: Verify API response schemas and data types
- **TC-API-004**: Verify error handling for invalid requests

## 🏗️ Architecture

Built with:
- **Playwright APIRequestContext** for HTTP requests
- **JSON Schema validation** for response validation
- **SOLID principles** for maintainability
- **Type safety** with Python type hints
- **Structured logging** with correlation IDs

## ✨ Key Features

### 🧪 **Comprehensive API Testing**
- **REST API Testing**: Full HTTP request/response validation
- **JSON Schema Validation**: Automatic response structure validation
- **Performance Testing**: Response time tracking and analysis
- **Error Handling**: Comprehensive error scenario testing

### 🚀 **CI/CD Excellence**
- **GitHub Actions**: Automated testing on every push and PR
- **Quality Gates**: Automated code quality checks and validation

### 🛡️ **Code Quality**
- **Type Safety**: Full type checking for reliability
- **Code Formatting**: Automated formatting with Black
- **Linting**: Flake8 linting for code quality standards

### 🏗️ **Architecture**
- **SOLID Principles**: Clean, maintainable, and extensible code
- **Structured Logging**: Correlation ID tracking and detailed execution logs
- **Environment Flexibility**: Support for local, CI, and staging environments
- **JSON Schema Validation**: Automatic response validation

## 📚 Documentation

- [Development Guide](docs/development.md)
- [System Requirements Document (SRD)](docs/SRD.md)
- [System Test Plan (STP)](docs/STP.md)

## 🔗 Links

- **🚀 CI/CD Pipeline**: [GitHub Actions](https://github.com/StavLobel/pokeapi-testing/actions)
- **📁 Repository**: [GitHub](https://github.com/StavLobel/pokeapi-testing)

---

**Built with ❤️ using Playwright, Python, and modern DevOps practices**
