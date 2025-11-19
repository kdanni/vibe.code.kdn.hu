"""LLM client utilities and helpers."""

from .interfaces import LLMClient, LLMClientConfig, LLMServiceHealth
from .clients.rest import RESTLLMClient

__all__ = [
    "LLMClient",
    "LLMClientConfig",
    "LLMServiceHealth",
    "RESTLLMClient",
    "create_default_client",
]


def create_default_client(config: LLMClientConfig) -> RESTLLMClient:
    """Return the default REST-based LLM client implementation."""

    return RESTLLMClient(config=config)
