"""HTTP helper utilities for API clients."""

from __future__ import annotations

from urllib.parse import urljoin


def sanitize_base_url(base_url: str) -> str:
    """Ensure the base URL always ends with a slash."""

    if not base_url:
        raise ValueError("Base URL must be provided")
    return base_url if base_url.endswith("/") else f"{base_url}/"


def join_url(base_url: str, path: str) -> str:
    """Join a base URL with an endpoint path safely."""

    sanitized_base = sanitize_base_url(base_url)
    return urljoin(sanitized_base, path.lstrip("/"))
