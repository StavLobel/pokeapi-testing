"""
Data loading utilities for test data management.
"""

import json
import yaml
from pathlib import Path
from typing import Any, Dict, List, Union
import logging

logger = logging.getLogger(__name__)


def load_json_data(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Load test data from a JSON file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Parsed JSON data as dictionary
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    path = Path(file_path)
    logger.info(f"Loading JSON data from {path}")
    
    if not path.exists():
        raise FileNotFoundError(f"Test data file not found: {path}")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logger.info(f"Successfully loaded {len(data)} items from {path}")
        return data
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {path}: {e}")
        raise


def load_yaml_data(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Load test data from a YAML file.
    
    Args:
        file_path: Path to the YAML file
        
    Returns:
        Parsed YAML data as dictionary
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        yaml.YAMLError: If the file contains invalid YAML
    """
    path = Path(file_path)
    logger.info(f"Loading YAML data from {path}")
    
    if not path.exists():
        raise FileNotFoundError(f"Test data file not found: {path}")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info(f"Successfully loaded data from {path}")
        return data
    except yaml.YAMLError as e:
        logger.error(f"Invalid YAML in {path}: {e}")
        raise


def load_test_data(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Load test data from JSON or YAML file based on extension.
    
    Args:
        file_path: Path to the test data file
        
    Returns:
        Parsed data as dictionary
        
    Raises:
        ValueError: If file extension is not supported
        FileNotFoundError: If the file doesn't exist
    """
    path = Path(file_path)
    extension = path.suffix.lower()
    
    if extension == '.json':
        return load_json_data(path)
    elif extension in ['.yaml', '.yml']:
        return load_yaml_data(path)
    else:
        raise ValueError(f"Unsupported file extension: {extension}. Use .json, .yaml, or .yml")
