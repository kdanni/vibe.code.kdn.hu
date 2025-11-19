from unittest.mock import Mock

import pytest

from vibe_code.llm import LLMClientConfig
from vibe_code.llm.clients import GoogleAIClient, HuggingFaceClient, OpenAIClient
from vibe_code.llm.clients.rest import RESTLLMClient
from vibe_code.llm.exceptions import LLMServiceResponseError
from vibe_code.llm.helpers import join_url


def test_join_url_sanitizes_base():
    assert join_url("https://example.com/api", "/ping") == "https://example.com/api/ping"


def build_response(status_code=200, json_payload=None, text=""):
    response = Mock()
    response.status_code = status_code
    response.ok = status_code < 400
    response.text = text
    response.json = Mock()
    if json_payload is None:
        response.json.side_effect = ValueError("no json")
    else:
        response.json.return_value = json_payload
    return response


def test_ping_returns_health_metadata():
    config = LLMClientConfig(base_url="https://example.com/api", api_key="secret", health_endpoint="/ping")
    session = Mock()
    response = build_response(json_payload={"status": "ok", "service": "llm"})
    session.request.return_value = response
    client = RESTLLMClient(config=config, session=session)

    health = client.ping()

    assert health.ok is True
    assert health.message == "ok"
    assert health.metadata == {"status": "ok", "service": "llm"}
    args, kwargs = session.request.call_args
    assert args[0] == "GET"
    assert args[1] == "https://example.com/api/ping"
    assert kwargs["headers"]["Authorization"] == "Bearer secret"


def test_ping_raises_for_error_responses():
    config = LLMClientConfig(base_url="https://example.com", health_endpoint="/health")
    session = Mock()
    session.request.return_value = build_response(status_code=500, text="boom")
    client = RESTLLMClient(config=config, session=session)

    with pytest.raises(LLMServiceResponseError):
        client.ping()


def test_huggingface_client_ping():
    config = LLMClientConfig(
        base_url="https://api-inference.huggingface.co",
        api_key="hf_...",
        health_endpoint="/health",
    )
    session = Mock()
    response = build_response(json_payload={"state": "healthy", "healthy": True})
    session.request.return_value = response
    client = HuggingFaceClient(config=config, session=session)

    health = client.ping()

    assert health.ok is True
    assert health.metadata == {"state": "healthy", "healthy": True}
    args, kwargs = session.request.call_args
    assert args[0] == "GET"
    assert args[1] == "https://api-inference.huggingface.co/health"
    assert kwargs["headers"]["Authorization"] == "Bearer hf_..."


def test_openai_client_ping():
    config = LLMClientConfig(
        base_url="https://api.openai.com/v1",
        api_key="sk-...",
        health_endpoint="/models",
    )
    session = Mock()
    response = build_response(json_payload={"data": []})
    session.request.return_value = response
    client = OpenAIClient(config=config, session=session)

    health = client.ping()

    assert health.ok is True
    assert health.metadata == {"data": []}
    args, kwargs = session.request.call_args
    assert args[0] == "GET"
    assert args[1] == "https://api.openai.com/v1/models"
    assert kwargs["headers"]["Authorization"] == "Bearer sk-..."


def test_google_ai_client_ping_uses_api_key_header():
    config = LLMClientConfig(
        base_url="https://generativelanguage.googleapis.com",
        api_key="google-key",
        health_endpoint="/v1beta/models",
    )
    session = Mock()
    response = build_response(json_payload={"models": []})
    session.request.return_value = response
    client = GoogleAIClient(config=config, session=session)

    health = client.ping()

    assert health.ok is True
    assert health.metadata == {"models": []}
    args, kwargs = session.request.call_args
    assert args[0] == "GET"
    assert args[1] == "https://generativelanguage.googleapis.com/v1beta/models"
    assert kwargs["headers"]["x-goog-api-key"] == "google-key"
