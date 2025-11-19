"""Interfaces and shared dataclasses for LLM service clients."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Mapping, MutableMapping, Optional


@dataclass(frozen=True, slots=True)
class LLMClientConfig:
    """Configuration shared by all LLM service API clients."""

    base_url: str
    api_key: Optional[str] = None
    timeout: float = 10.0
    health_endpoint: str = "/health"
    extra_headers: MutableMapping[str, str] = field(default_factory=dict)


@dataclass(slots=True)
class LLMServiceHealth:
    """Represents the result of a ping/health-check call."""

    ok: bool
    status_code: Optional[int] = None
    latency_ms: Optional[float] = None
    message: Optional[str] = None
    metadata: Mapping[str, Any] | None = None


class LLMClient(ABC):
    """Abstract base class all LLM clients must implement."""

    def __init__(self, config: LLMClientConfig) -> None:
        self.config = config

    @abstractmethod
    def ping(self) -> LLMServiceHealth:
        """Perform a health check against the remote service."""

        raise NotImplementedError
