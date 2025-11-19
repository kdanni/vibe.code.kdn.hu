"""Google AI Platform (Gemini) client implementation."""

from __future__ import annotations

import time
from typing import MutableMapping, Optional

from .base import USER_AGENT, BaseHTTPClient
from ..interfaces import LLMClientConfig, LLMServiceHealth


class GoogleAIClient(BaseHTTPClient):
    """HTTP client for Google's AI Platform / Gemini endpoints."""

    def __init__(self, config: LLMClientConfig, *, session=None) -> None:
        super().__init__(config=config, session=session)

    def _headers(self, extra: Optional[MutableMapping[str, str]] = None):
        headers = {
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
            **self.config.extra_headers,
        }
        if self.config.api_key:
            headers.setdefault("x-goog-api-key", self.config.api_key)
        if extra:
            headers.update(extra)
        return headers

    def ping(self) -> LLMServiceHealth:
        """Call the configured health endpoint and return the parsed status."""

        started_at = time.perf_counter()
        response = self._request("GET", self.config.health_endpoint)
        return self._health_from_response(response, started_at)
