# Slop

This folder stores the raw AI-generated artifacts that implement each prompt. Treat these as disposable yet runnable outputs that should align with the vibe described in `/prompts`.

## Expectations
- Name files to match their prompt ID (e.g., `p001_basic_cli_tool.py`).
- Keep dependencies minimal and documented at the top of the file.
- Avoid manual refactors unless required for execution; prefer updating the prompt instead.

## Quick checklist
- Does the artifact run end-to-end for the sample flow in the prompt?
- Are any setup steps or environment variables clearly noted?
- Is there a tiny smoke test or invocation example in comments?
