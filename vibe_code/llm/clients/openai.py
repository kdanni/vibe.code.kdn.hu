"""OpenAI client implementation."""

from __future__ import annotations

import time

from .base import BaseHTTPClient
from ..interfaces import LLMClientConfig, LLMServiceHealth


class OpenAIClient(BaseHTTPClient):
    """HTTP client tailored for the OpenAI API."""

    def __init__(self, config: LLMClientConfig, *, session=None) -> None:
        super().__init__(config=config, session=session)

    def ping(self) -> LLMServiceHealth:
        """Call the configured health endpoint and return the parsed status."""

        started_at = time.perf_counter()
        response = self._request("GET", self.config.health_endpoint)
        return self._health_from_response(response, started_at)
