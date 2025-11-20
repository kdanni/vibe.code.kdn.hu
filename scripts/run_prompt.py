"""CLI helper to run LLM prompts with environment-aware defaults."""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Optional, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from bootstrap import add_repo_root_to_path

PROJECT_ROOT = add_repo_root_to_path()

from vibe_code.llm import LLMClient, LLMClientConfig, LLMServiceHealth, create_default_client
from vibe_code.llm.exceptions import LLMServiceError


DEFAULTS = {
    "base_url": "http://localhost:8000",
    "api_key": "dev-key",
    "timeout": "10",
    "health_endpoint": "/health",
}


def usage_hint() -> str:
    """Return a short usage hint with example values."""

    return (
        "Example: LLM_API_BASE_URL={base_url} LLM_API_KEY={api_key} "
        "python scripts/run_prompt.py prompts/example.md".format(**DEFAULTS)
    )


def build_client_from_env(
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    timeout: Optional[float] = None,
    health_endpoint: Optional[str] = None,
) -> Optional[Tuple[LLMClientConfig, LLMClient]]:
    """Create a configured client using explicit values or environment variables."""

    resolved_base_url = base_url or os.environ.get("LLM_API_BASE_URL")
    if not resolved_base_url:
        print("No LLM base URL provided. Set LLM_API_BASE_URL or use --base-url.")
        print(usage_hint())
        return None

    config = LLMClientConfig(
        base_url=resolved_base_url,
        api_key=api_key or os.environ.get("LLM_API_KEY"),
        timeout=float(timeout or os.environ.get("LLM_API_TIMEOUT", DEFAULTS["timeout"])),
        health_endpoint=health_endpoint
        or os.environ.get("LLM_API_HEALTH_ENDPOINT", DEFAULTS["health_endpoint"]),
    )
    client = create_default_client(config)
    return config, client


def ping_llm_service(
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    timeout: Optional[float] = None,
    health_endpoint: Optional[str] = None,
) -> Optional[LLMServiceHealth]:
    """Ping the configured LLM service and print the status."""

    client_bundle = build_client_from_env(base_url, api_key, timeout, health_endpoint)
    if not client_bundle:
        return None
    _config, client = client_bundle
    try:
        health = client.ping()
    except LLMServiceError as exc:  # pragma: no cover - console logging only
        print(f"LLM service health check failed: {exc}")
        return None
    except Exception as exc:  # pragma: no cover - defensive logging only
        print(f"Unexpected error during health check: {exc}")
        return None
    print(
        "LLM service status: {status} (HTTP {code}, {latency:.2f} ms)".format(
            status="ok" if health.ok else "unhealthy",
            code=health.status_code or "?",
            latency=health.latency_ms or 0.0,
        )
    )
    if health.message:
        print(f"Message: {health.message}")
    return health


def run_prompt(prompt_file: str, **client_kwargs: str) -> None:
    """Reads a prompt from a file and prepares it for the remote LLM."""

    prompt_path = Path(prompt_file)
    print(f"Running prompt from: {prompt_path}")
    if not prompt_path.exists():
        print("Prompt file not found. Please provide a valid path.")
        return

    print("Repository root detected at:", PROJECT_ROOT)
    ping_llm_service(**client_kwargs)
    print("(Placeholder) Would send prompt contents to the remote API next...")
    print("Prompt preview:\n" + prompt_path.read_text())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a prompt and get a result from an LLM.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=usage_hint(),
    )
    parser.add_argument("prompt_file", help="Path to the prompt file, e.g. prompts/example.md")
    parser.add_argument(
        "--base-url",
        dest="base_url",
        default=os.environ.get("LLM_API_BASE_URL"),
        help="LLM service base URL (overrides LLM_API_BASE_URL)",
    )
    parser.add_argument(
        "--api-key",
        dest="api_key",
        default=os.environ.get("LLM_API_KEY"),
        help="Optional API key (overrides LLM_API_KEY)",
    )
    parser.add_argument(
        "--timeout",
        dest="timeout",
        type=float,
        default=float(os.environ.get("LLM_API_TIMEOUT", DEFAULTS["timeout"])),
        help="HTTP timeout in seconds (overrides LLM_API_TIMEOUT)",
    )
    parser.add_argument(
        "--health-endpoint",
        dest="health_endpoint",
        default=os.environ.get("LLM_API_HEALTH_ENDPOINT", DEFAULTS["health_endpoint"]),
        help="Health endpoint path (overrides LLM_API_HEALTH_ENDPOINT)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_prompt(
        args.prompt_file,
        base_url=args.base_url,
        api_key=args.api_key,
        timeout=args.timeout,
        health_endpoint=args.health_endpoint,
    )


if __name__ == "__main__":
    main()
