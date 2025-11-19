# Installation Guide

This guide walks through setting up a repeatable Python development environment for the `vibe.code.kdn.hu` repository. It focuses on
isolated virtual environments, dependency management, and a Docker-based workflow for maximum portability.

## 1. Prerequisites
- **Python**: 3.10 or newer (3.11 recommended to match the Docker image)
- **pip**: bundled with Python, but you should upgrade it after creating your virtual environment
- **Git**: for cloning and contributing
- **Docker** (optional): required only if you plan to use the containerized workflow described below

## 2. Local Python environment setup

### 2.1 Clone the repository
```bash
git clone https://github.com/<your-user>/vibe.code.kdn.hu.git
cd vibe.code.kdn.hu
```

### 2.2 Create a virtual environment
```bash
python3 -m venv .venv
```

### 2.3 Activate the virtual environment
- **macOS/Linux**
  ```bash
  source .venv/bin/activate
  ```
- **Windows (PowerShell)**
  ```powershell
  .venv\\Scripts\\Activate.ps1
  ```

> Tip: Add `source .venv/bin/activate` (or the Windows equivalent) to your shell profile if you work in this repo frequently.

### 2.4 Upgrade packaging tools and install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Dependency management workflow
1. Install new libraries inside the activated virtual environment:
   ```bash
   pip install <package-name>
   ```
2. Freeze the working set back into `requirements.txt` so collaborators receive identical dependencies:
   ```bash
   pip freeze > requirements.txt
   ```
3. Run project checks/tests (for example, `pytest`) to ensure the new dependency works as expected.
4. Commit the updated `requirements.txt` alongside any source changes.

Keeping dependencies pinned via `requirements.txt` lets both local and containerized environments stay in sync.

## 4. Docker-based portable development environment
If you prefer a fully isolated environment, or want a setup that runs identically across machines, use the provided `Dockerfile`.

### 4.1 Build the development image
```bash
docker build -t vibe-code-dev .
```

### 4.2 Start an interactive development container
```bash
docker run --rm -it -v "$(pwd)":/app vibe-code-dev
```
- `-v "$(pwd)":/app` mounts your local working tree so edits are reflected inside the container.
- The container drops you into `/bin/bash`; activate the virtual environment inside the container if desired or run tools directly.

### 4.3 Running commands inside the container
Once inside the container you can run the usual developer workflows, for example:
```bash
pytest          # run the test suite
python script.py  # execute project scripts
```

Because the image installs dependencies from `requirements.txt`, every contributor using Docker shares the same toolchain without
manual setup.

## 5. Keeping environments healthy
- Periodically recreate the virtual environment (`rm -rf .venv && python -m venv .venv`) to avoid stale packages.
- If Docker layers become outdated after dependency changes, rebuild the image with `docker build --no-cache -t vibe-code-dev .`.
- Document any environment-specific quirks directly in this file so future contributors can onboard quickly.
