# API client setup

This directory contains HTTP clients for LLM services (OpenAI, Google AI Platform/Gemini, Hugging Face Inference API, and generic REST endpoints). Each client reads the API key from the shared `LLMClientConfig.api_key` field and sends it using provider-specific headers:

- **OpenAI / REST**: `Authorization: Bearer <API_KEY>` (default behavior in `BaseHTTPClient`).
- **Google AI Platform**: `x-goog-api-key: <API_KEY>` added by `GoogleAIClient`.
- **Hugging Face Inference API**: `Authorization: Bearer <API_KEY>` (default behavior in `BaseHTTPClient`).

## Configure API keys

Set your API keys as environment variables and pass them into `LLMClientConfig` or the helper CLI in `scripts/run_prompt.py`:

```bash
export LLM_API_BASE_URL="https://api.openai.com/v1"  # or your provider base URL
export LLM_API_KEY="sk-..."                         # provider-specific key
export LLM_API_TIMEOUT="15"                         # optional, seconds
export LLM_API_HEALTH_ENDPOINT="/health"            # optional override
```

Then create a client in Python:

```python
from vibe_code.llm import LLMClientConfig, create_default_client

config = LLMClientConfig(
    base_url="https://api.openai.com/v1",
    api_key=os.environ["LLM_API_KEY"],
    health_endpoint="/v1/models"  # replace with a provider health path
)
client = create_default_client(config)
health = client.ping()
print(health)
```

Or use the CLI helper:

```bash
LLM_API_BASE_URL="https://api.openai.com/v1" \
LLM_API_KEY="sk-..." \
python scripts/run_prompt.py prompts/example.md
```

Ensure the API key you supply matches the selected provider (OpenAI secret keys, Google AI Platform keys, or Hugging Face access tokens).
