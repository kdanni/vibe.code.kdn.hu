from unittest.mock import Mock

import pytest

from vibe_code.llm import LLMClientConfig
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
