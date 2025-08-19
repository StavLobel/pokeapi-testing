# Configuration Guide

This document explains how to configure the PokeAPI testing framework.

## Configuration Sources

The framework reads configuration from multiple sources in the following priority order:

1. **CLI Arguments** (highest priority) - `--api-base-url`
2. **Environment Variables** 
3. **Default Values** (lowest priority)

---

## Enhanced Framework Capabilities

### **Comprehensive HTTP Method Support**
The framework now supports testing all HTTP methods for comprehensive API validation:

#### **Available HTTP Methods:**
- **GET** - Standard resource retrieval (primary method)
- **POST** - Testing method not allowed scenarios
- **PUT** - Testing method not allowed scenarios  
- **DELETE** - Testing method not allowed scenarios
- **PATCH** - Testing method not allowed scenarios

#### **Enhanced Testing Features:**
- **Headers Support**: Custom headers for testing content negotiation
- **Error Handling**: Graceful handling of 4xx/5xx responses
- **Method Testing**: Comprehensive validation of read-only API contract
- **Response Validation**: Full response structure and status code validation

#### **Usage Examples:**
```python
# Test non-GET methods (should return 405 Method Not Allowed)
client.test_http_method("POST", pokemon_id=1)
client.test_http_method("PUT", pokemon_id=1)
client.test_http_method("DELETE", pokemon_id=1)
client.test_http_method("PATCH", pokemon_id=1)

# Test with custom headers
client.get_pokemon_with_headers(1)
```

### **Dynamic Configuration Override**
The CLI argument `--api-base-url` provides runtime configuration override:

```bash
# Test against local development server
pytest --api-base-url=http://localhost:8000/api/v2

# Test against staging environment
pytest --api-base-url=https://staging-pokeapi.example.com/api/v2

# Test against production with specific test selection
pytest --api-base-url=https://pokeapi.co/api/v2 -k "test_pok_01"
```

---

## CLI Arguments

### --api-base-url

Override the base URL for API requests directly from the command line:

```bash
# Override base URL for local development
pytest --api-base-url=http://localhost:8000/api/v2

# Override base URL for staging environment
pytest --api-base-url=https://staging-api.example.com/api/v2

# Override base URL and run specific tests
pytest --api-base-url=http://localhost:8000/api/v2 tests/api/test_pokemon.py

# Override base URL with other pytest options
pytest --api-base-url=http://localhost:8000/api/v2 -v -k "test_pok_01"
```

**Note**: The CLI argument takes precedence over all other configuration sources and is applied to both `POKEAPI_BASE_URL` and `TEST_BASE_URL` environment variables.

## Environment Variables

### PokeAPI Configuration

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `POKEAPI_BASE_URL` | Base URL for the PokeAPI | `https://pokeapi.co/api/v2` | `http://localhost:8000/api/v2` |
| `POKEAPI_TIMEOUT` | Request timeout in milliseconds | `30000` | `60000` |
| `POKEAPI_LOG_LEVEL` | Logging level | `INFO` | `DEBUG` |

### Test Configuration

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `TEST_BASE_URL` | Base URL for testing | `https://pokeapi.co/api/v2` | `https://staging-pokeapi.example.com/api/v2` |
| `TEST_TIMEOUT` | Test timeout in seconds | `30` | `60` |
| `TEST_PARALLEL_WORKERS` | Number of parallel test workers | `4` | `8` |

## Configuration Files

### .env File

Create a `.env` file in the project root to override default settings:

```bash
# PokeAPI Configuration
POKEAPI_BASE_URL=https://pokeapi.co/api/v2
POKEAPI_TIMEOUT=30000
POKEAPI_LOG_LEVEL=INFO

# Test Configuration
TEST_BASE_URL=https://pokeapi.co/api/v2
TEST_TIMEOUT=30
TEST_PARALLEL_WORKERS=4
```

### pyproject.toml

Configuration can also be set in `pyproject.toml`:

```toml
[tool.pokeapi]
base_url = "https://pokeapi.co/api/v2"
timeout = 30000
log_level = "INFO"

[tool.pokeapi.test]
base_url = "https://pokeapi.co/api/v2"
timeout = 30
parallel_workers = 4
```

## Environment-Specific Configuration

### Local Development

```bash
# .env.local
POKEAPI_BASE_URL=http://localhost:8000/api/v2
POKEAPI_TIMEOUT=10000
POKEAPI_LOG_LEVEL=DEBUG

# Or use CLI argument (recommended for quick testing)
pytest --api-base-url=http://localhost:8000/api/v2
```

### CI/CD Environment

```bash
# .env.ci
POKEAPI_BASE_URL=https://pokeapi.co/api/v2
POKEAPI_TIMEOUT=30000
POKEAPI_LOG_LEVEL=INFO
TEST_PARALLEL_WORKERS=8
```

### Staging Environment

```bash
# .env.staging
POKEAPI_BASE_URL=https://staging-pokeapi.example.com/api/v2
POKEAPI_TIMEOUT=60000
POKEAPI_LOG_LEVEL=WARNING

# Or use CLI argument
pytest --api-base-url=https://staging-pokeapi.example.com/api/v2
```

## Code Usage

### In Settings

```python
from src.config.settings import settings, test_settings

# Access configuration
base_url = settings.base_url
timeout = settings.timeout
log_level = settings.log_level

# Test-specific settings
test_timeout = test_settings.timeout
parallel_workers = test_settings.parallel_workers
```

### In Tests with CLI Override

```python
import pytest
from src.config.settings import settings

def test_with_cli_override(dynamic_settings):
    """Test that shows how to use CLI overrides in tests."""
    # Get settings that respect CLI arguments
    cli_base_url = dynamic_settings['cli_base_url']
    actual_base_url = dynamic_settings['settings'].base_url
    
    if cli_base_url:
        print(f"Using CLI override: {cli_base_url}")
        assert actual_base_url == cli_base_url
    else:
        print(f"Using default: {actual_base_url}")
```

### In API Clients

```python
from src.config.settings import settings

class BaseAPIClient:
    def __init__(self, api_request_context):
        self.base_url = settings.base_url
        self.timeout = settings.timeout
    
    def get(self, endpoint):
        full_url = f"{self.base_url.rstrip('/')}{endpoint}"
        # ... rest of implementation
```

### In Tests

```python
from src.config.settings import test_settings

@pytest.fixture(scope="session")
def api_request_context(playwright):
    context = playwright.request.new_context(
        timeout=test_settings.timeout * 1000,  # Convert to milliseconds
    )
    yield context
    context.dispose()
```

## Configuration Validation

The framework automatically validates configuration on import:

- **Base URL**: Must start with `http://` or `https://`
- **Timeouts**: Must be positive numbers
- **Parallel Workers**: Must be positive numbers

If validation fails, the application will raise a `ValueError` with details about the issue.

## Best Practices

1. **Use CLI arguments for quick testing** - `--api-base-url` is perfect for local development
2. **Use environment variables for CI/CD** - Set them in your CI pipeline
3. **Use .env files for team development** - Share common configurations
4. **Never commit sensitive data** - Use environment variables for secrets
5. **Set defaults in code** - Provide sensible defaults for all settings
6. **Validate configuration** - Always validate configuration values
7. **Document all settings** - Keep this guide updated with new settings

## Troubleshooting

### Common Issues

1. **Configuration not loaded**: Check that `.env` file is in the project root
2. **Invalid base URL**: Ensure URL starts with `http://` or `https://`
3. **Timeout errors**: Increase timeout values for slow environments
4. **Import errors**: Verify that configuration files are properly imported
5. **CLI argument not working**: Check that you're using `--api-base-url` (not `--base-url`)

### Debug Configuration

To debug configuration loading, add logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

from src.config.settings import settings
print(f"Base URL: {settings.base_url}")
print(f"Timeout: {settings.timeout}")
```

### CLI Argument Examples

```bash
# Test with local API
pytest --api-base-url=http://localhost:8000/api/v2

# Test with staging API
pytest --api-base-url=https://staging-api.example.com/api/v2

# Test with custom timeout and base URL
POKEAPI_TIMEOUT=60000 pytest --api-base-url=http://localhost:8000/api/v2

# Run specific tests with custom base URL
pytest --api-base-url=http://localhost:8000/api/v2 -k "test_pok_01" -v
```
