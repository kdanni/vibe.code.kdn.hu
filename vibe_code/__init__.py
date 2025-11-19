"""Top-level package for vibe.code utilities."""

from .llm import LLMClientConfig, LLMServiceHealth, create_default_client

__all__ = [
    "LLMClientConfig",
    "LLMServiceHealth",
    "create_default_client",
]
