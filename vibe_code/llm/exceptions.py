"""Custom exceptions raised by the LLM client helpers.""" 

from __future__ import annotations

from typing import Optional


class LLMServiceError(RuntimeError):
    """Base error raised when the remote service cannot fulfill a request."""

    def __init__(self, message: str, *, status_code: Optional[int] = None) -> None:
        super().__init__(message)
        self.status_code = status_code


class LLMServiceConfigurationError(LLMServiceError):
    """Raised when the client configuration is invalid."""


class LLMServiceResponseError(LLMServiceError):
    """Raised for unexpected HTTP responses."""
