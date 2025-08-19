.PHONY: help install setup test test-api test-smoke clean lint type-check

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

setup: ## Setup development environment
	pip install -r requirements.txt
	playwright install

test: ## Run all tests
	pytest

test-api: ## Run API tests only
	pytest tests/api/ -v

test-smoke: ## Run smoke tests only
	pytest -m smoke -v

test-local: ## Run tests against local API (requires local server)
	pytest --api-base-url=http://localhost:8000/api/v2 -v

test-staging: ## Run tests against staging API
	pytest --api-base-url=https://staging-api.example.com/api/v2 -v

lint: ## Run code linting and formatting
	black src/ tests/
	isort src/ tests/
	flake8 src/ tests/

type-check: ## Run type checking
	mypy src/

quality: ## Run all quality checks (lint, type-check)
	$(MAKE) lint
	$(MAKE) type-check

clean: ## Clean up generated files
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -f .coverage
	find . -type d -name __pycache__ -delete
	find . -name "*.pyc" -delete
