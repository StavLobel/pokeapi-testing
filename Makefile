.PHONY: help install setup test test-api test-smoke clean

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

clean: ## Clean up generated files
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -delete
	find . -name "*.pyc" -delete
