"""LLM client utilities and helpers."""

from .interfaces import LLMClient, LLMClientConfig, LLMServiceHealth
from .clients import GoogleAIClient, HuggingFaceClient, OpenAIClient, RESTLLMClient

__all__ = [
    "GoogleAIClient",
    "HuggingFaceClient",
    "LLMClient",
    "LLMClientConfig",
    "LLMServiceHealth",
    "OpenAIClient",
    "RESTLLMClient",
    "create_default_client",
]


def create_default_client(config: LLMClientConfig) -> RESTLLMClient:
    """Return the default REST-based LLM client implementation."""

    return RESTLLMClient(config=config)
