.PHONY: help install setup test test-api test-smoke clean lint type-check security performance deploy docker-build

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

setup: ## Setup development environment
	pip install -r requirements.txt
	playwright install
	pre-commit install

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

test-performance: ## Run performance tests
	pytest -m performance -v

test-security: ## Run security tests
	pytest tests/security/ -v

lint: ## Run code linting and formatting
	black src/ tests/
	isort src/ tests/
	flake8 src/ tests/

type-check: ## Run type checking
	mypy src/

security-scan: ## Run security scanning
	safety check
	bandit -r src/ --format json --output bandit-report.json

quality: ## Run all quality checks (lint, type-check, security)
	$(MAKE) lint
	$(MAKE) type-check
	$(MAKE) security-scan

performance-baseline: ## Generate performance baseline
	pytest --performance-baseline

performance-regression: ## Check for performance regressions
	pytest --performance-regression

docker-build: ## Build Docker image
	docker build -t pokeapi-testing:latest .

docker-run: ## Run tests in Docker container
	docker run --rm pokeapi-testing:latest

deploy-staging: ## Deploy to staging environment
	./scripts/deploy.sh staging

deploy-production: ## Deploy to production environment
	./scripts/deploy.sh production

clean: ## Clean up generated files
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -f .coverage
	rm -f bandit-report.json
	rm -f safety-report.json
	find . -type d -name __pycache__ -delete
	find . -name "*.pyc" -delete

ci: ## Run CI pipeline locally
	$(MAKE) quality
	$(MAKE) test
	$(MAKE) test-performance
	$(MAKE) test-security
