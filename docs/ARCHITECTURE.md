# Vibe Code Architecture Overview

## Purpose and guiding principles
The repository demonstrates the Vibe Coding workflow: prompts capture intent, AI generates implementation “slop,” and short results validate the vibe. The architecture optimizes for developer time, rapid iteration, and hosted LLM leverage rather than hand-tuned code.

* **Human as Vibe Director:** humans write prompts and curate results instead of writing most code.
* **LLM-first delivery:** hosted LLM APIs (e.g., GPT-4o/Claude 3.5) produce runnable artifacts quickly.
* **Production-ready slop:** if generated code compiles, runs, and matches the vibe, it is good enough.

## Repository structure and data flow
```text
prompts/  ->  slop/  ->  results/
^ source      ^ generated   ^ proof of vibe
```
1. **Prompts** (`/prompts`): the “true source code” written in Markdown to express intent, constraints, and vibe.
2. **Slop** (`/slop`): raw AI-generated artifacts (typically Python 3.11+ scripts/CLIs) created from prompts.
3. **Results** (`/results`): lightweight evidence (READMEs, screenshots, terminal captures) that the generated code runs and meets the vibe.

### Supporting files
* **README.md**: philosophy, onboarding, and directory primer.
* **LICENSE**: repository license.
* Optional CI configuration (none present yet) should run fast smoke tests on generated artifacts.

## Technology stack recommendations
* **Language/runtime:** Python 3.11+ as the default for generated utilities; keep glue code simple.
* **AI generation layer:** hosted LLM APIs for rapid code production; local inference is optional and not assumed.
* **Tooling:** minimal Python scripts/notebooks to run prompts and capture outputs; use `pipx`/`setuptools` if packaging CLIs.
* **Testing:** tiny, task-focused smoke tests colocated with generated artifacts to confirm they execute.
* **CI/CD:** lightweight GitHub Actions (or similar) that execute smoke tests and archive results.

## Contribution workflow
1. Draft or refine a prompt in `/prompts` that clearly states the vibe and success criteria.
2. Generate code with an LLM and store the output in `/slop` using the same prompt ID.
3. Run the artifact locally; capture execution proof in `/results` (logs, screenshots, or short READMEs).
4. Optionally add a brief smoke test alongside the artifact.
5. Open a PR with the new prompt, slop, and result; reviewers focus on intent alignment over code style.

## Extensibility notes
* The prompts/slop/results triad is extensible to other languages or runtimes as long as the flow stays intact.
* Keep automation scripts small and repo-local to preserve the fast OODA loop.
* Prefer configuration over code for LLM provider details to keep the repo lightweight.
