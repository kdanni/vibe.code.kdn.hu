# LLM Service API Design

## Available LLM Service APIs

### Preferred Free Tier

- **OpenAI API**: Offers a free tier with limited usage, suitable for development and testing.
- **Google AI Platform**: Provides a free tier with access to Gemini models.
- **Hugging Face Inference API**: Offers a free tier for a wide range of open-source models.

### Preferred Standardized Interface

- **OpenAI API**: The API is well-documented and has become a de facto standard in the industry.
- **LangChain**: Provides a standardized interface for interacting with various LLM providers.

## Best Practices

- **API Key Management**: Store API keys securely and use environment variables to access them.
- **Error Handling**: Implement robust error handling to manage API failures and retries.
- **Rate Limiting**: Be mindful of rate limits and implement backoff strategies to avoid being blocked.
- **Request Optimization**: Batch requests and use streaming to improve performance and reduce costs.

## Repository client implementation

The `vibe_code.llm` package now contains the building blocks for interacting with remote LLM services:

- `LLMClientConfig`: captures base URL, API key, timeout, and health endpoint configuration.
- `LLMServiceHealth`: standardized response returned from the `ping()` method.
- `RESTLLMClient`: default HTTP client that performs the `/health` (or custom) call.
- Helper utilities in `vibe_code.llm.helpers` keep URL handling and future shared HTTP behavior centralized.

`scripts/run_prompt.py` demonstrates how to construct the client from environment variables (`LLM_API_BASE_URL`, `LLM_API_KEY`, etc.), execute the health check, and print the resulting status before issuing additional API operations.
