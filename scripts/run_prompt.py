import argparse
import os
from typing import Optional, Tuple

from vibe_code.llm import LLMClient, LLMClientConfig, LLMServiceHealth, create_default_client
from vibe_code.llm.exceptions import LLMServiceError


def build_client_from_env() -> Optional[Tuple[LLMClientConfig, LLMClient]]:
    """Create a configured client if the required environment variables exist."""

    base_url = os.environ.get("LLM_API_BASE_URL")
    if not base_url:
        return None
    config = LLMClientConfig(
        base_url=base_url,
        api_key=os.environ.get("LLM_API_KEY"),
        timeout=float(os.environ.get("LLM_API_TIMEOUT", "10")),
        health_endpoint=os.environ.get("LLM_API_HEALTH_ENDPOINT", "/health"),
    )
    client = create_default_client(config)
    return config, client


def ping_llm_service() -> Optional[LLMServiceHealth]:
    client_bundle = build_client_from_env()
    if not client_bundle:
        print("LLM_API_BASE_URL is not configured; skipping remote health check.")
        return None
    _config, client = client_bundle
    try:
        health = client.ping()
    except LLMServiceError as exc:  # pragma: no cover - console logging only
        print(f"LLM service health check failed: {exc}")
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


def run_prompt(prompt_file: str) -> None:
    """Reads a prompt from a file and prepares it for the remote LLM."""

    print(f"Running prompt from: {prompt_file}")
    ping_llm_service()
    # In a real script, the prompt contents would be sent to the remote API.
    # The placeholder keeps the pipeline lightweight for now.


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a prompt and get a result from an LLM.")
    parser.add_argument("prompt_file", help="The path to the prompt file.")
    args = parser.parse_args()
    run_prompt(args.prompt_file)


if __name__ == "__main__":
    main()
