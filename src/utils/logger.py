"""
Logging utilities with correlation ID support.
"""

import logging
import uuid
from typing import Optional
from contextvars import ContextVar

# Context variable for correlation ID
correlation_id_var: ContextVar[Optional[str]] = ContextVar('correlation_id', default=None)


class CorrelationAdapter(logging.LoggerAdapter):
    """Logger adapter that adds correlation ID to log records."""
    
    def process(self, msg, kwargs):
        """Add correlation ID to log record."""
        correlation_id = get_correlation_id()
        if correlation_id:
            return f"[{correlation_id}] {msg}", kwargs
        return msg, kwargs


def get_correlation_id() -> Optional[str]:
    """Get the current correlation ID from context."""
    return correlation_id_var.get()


def set_correlation_id(correlation_id: Optional[str] = None) -> str:
    """
    Set correlation ID in context.
    
    Args:
        correlation_id: Correlation ID to set. If None, generates a new UUID.
        
    Returns:
        The correlation ID that was set
    """
    if correlation_id is None:
        correlation_id = str(uuid.uuid4())[:8]
    
    correlation_id_var.set(correlation_id)
    return correlation_id


def setup_logger(name: str, level: str = "INFO") -> CorrelationAdapter:
    """
    Set up a logger with correlation ID support.
    
    Args:
        name: Logger name
        level: Logging level
        
    Returns:
        Logger adapter with correlation ID support
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # Create formatter
    formatter = logging.Formatter(
        fmt='%(asctime)s [%(levelname)8s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Create handler if not exists
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return CorrelationAdapter(logger, {})
