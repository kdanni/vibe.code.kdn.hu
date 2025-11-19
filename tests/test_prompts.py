from pathlib import Path

import pytest

PROMPT_PATH = Path("prompts/p001_health_check.md")


def read_prompt() -> str:
    try:
        return PROMPT_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:  # pragma: no cover - make failure clearer
        pytest.fail(f"Prompt file not found: {PROMPT_PATH}")


def test_prompt_exists():
    assert PROMPT_PATH.exists(), "Health-check prompt must exist"


def test_prompt_has_required_sections():
    content = read_prompt()
    for section in (
        "# p001: Environment Health Check Prompt",
        "## Vibe",
        "## Requirements",
        "## Success Criteria",
        "## Tooling and Constraints",
    ):
        assert section in content, f"Missing section heading: {section}"


def test_prompt_explains_goal_and_constraints():
    content = read_prompt()
    assert "health check" in content.lower(), "Prompt should clearly mention health check"
    assert "prompt→slop→result" in content or "prompt→slop→result".replace("→", "->") in content
    assert "Avoid network calls" in content, "Prompt should forbid network usage"
    assert "Keep total runtime under a few seconds" in content, "Prompt should enforce runtime limit"
