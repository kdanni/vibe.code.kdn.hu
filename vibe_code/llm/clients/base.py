"""Base HTTP client implementation for LLM services."""

from __future__ import annotations

import json
import time
from collections.abc import Mapping, MutableMapping
from typing import Any, Optional

import requests

from ..exceptions import LLMServiceResponseError
from ..helpers import join_url
from ..interfaces import LLMClient, LLMClientConfig, LLMServiceHealth

USER_AGENT = "vibe-code-llm-client/0.1"


class BaseHTTPClient(LLMClient):
    """Reusable HTTP plumbing shared by concrete clients."""

    def __init__(self, config: LLMClientConfig, *, session: Optional[requests.Session] = None) -> None:
        super().__init__(config)
        self._session = session or requests.Session()

    def _headers(self, extra: Optional[MutableMapping[str, str]] = None) -> Mapping[str, str]:
        headers = {
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
            **self.config.extra_headers,
        }
        if self.config.api_key:
            headers["Authorization"] = f"Bearer {self.config.api_key}"
        if extra:
            headers.update(extra)
        return headers

    def _request(self, method: str, endpoint: str, **kwargs: Any) -> requests.Response:
        url = join_url(self.config.base_url, endpoint)
        headers = self._headers(kwargs.pop("headers", None))
        response = self._session.request(method, url, headers=headers, timeout=self.config.timeout, **kwargs)
        if response.status_code >= 400:
            raise LLMServiceResponseError(
                f"LLM service returned HTTP {response.status_code}",
                status_code=response.status_code,
            )
        return response

    def _health_from_response(self, response: requests.Response, started_at: float) -> LLMServiceHealth:
        latency_ms = (time.perf_counter() - started_at) * 1000
        payload: Any
        try:
            payload = response.json()
        except json.JSONDecodeError:
            payload = None
        message: Optional[str] = None
        metadata = None
        if isinstance(payload, Mapping):
            metadata = payload
            raw_message = payload.get("message")
            raw_status = payload.get("status")
            raw_detail = payload.get("detail")
            if raw_message:
                message = str(raw_message)
            elif raw_status:
                message = str(raw_status)
            elif raw_detail:
                message = str(raw_detail)
        if not message:
            message = response.text.strip() or None
        return LLMServiceHealth(
            ok=response.ok,
            status_code=response.status_code,
            latency_ms=latency_ms,
            message=message,
            metadata=metadata,
        )
