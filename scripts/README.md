# Script Runner Toolkit

This folder contains small utilities for running local scripts without extra project configuration.

## Key Features
- **Robust imports:** `scripts/bootstrap.py` automatically adds the repository root to `sys.path`, so `python scripts/run_prompt.py` works even if you haven't installed the package.
- **Environment-aware defaults:** The CLI accepts flags or environment variables for the LLM endpoint and credentials.
- **Quick-start examples:** Copy/paste-ready commands show how to run scripts with sensible defaults.

## Usage

1. Ensure dependencies are installed (for a virtualenv):

   ```bash
   pip install -r requirements.txt
   ```

2. Run a prompt file with explicit values:

   ```bash
   python scripts/run_prompt.py prompts/example.md \
       --base-url http://localhost:8000 \
       --api-key dev-key \
       --timeout 15 \
       --health-endpoint /health
   ```

   You can alternatively set environment variables:

   ```bash
   export LLM_API_BASE_URL=http://localhost:8000
   export LLM_API_KEY=dev-key
   export LLM_API_TIMEOUT=15
   export LLM_API_HEALTH_ENDPOINT=/health
   python scripts/run_prompt.py prompts/example.md
   ```

3. If the health check succeeds, the script will print a preview of the prompt contents and note where it would send them to the configured API.

## Tips
- Use relative prompt paths from the repository root (e.g., `prompts/example.md`).
- Pass `--help` to see defaults and a quick usage hint.
- The `add_repo_root_to_path` helper can be reused by new scripts to keep imports simple.
