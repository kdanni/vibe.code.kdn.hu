# Vibe Code Roadmap

## Near-term (0–3 months)
1. **Prompt library expansion**: Add more example vibes covering web, data, and automation scenarios to `/prompts`, each with paired slop and results.
2. **Automation helpers**: Create small Python 3.11+ scripts/notebooks to run prompts, call hosted LLM APIs, and save outputs into `/slop` and `/results`.
3. **Smoke testing harness**: Introduce minimal `pytest` or shell-based smoke tests colocated with each generated artifact to ensure it runs after generation.
4. **Result capture templates**: Standardize short README templates for `/results` so runs are easy to reproduce and verify.

## Mid-term (3–6 months)
1. **Lightweight CI**: Add GitHub Actions to execute smoke tests, archive outputs, and surface failures quickly while keeping iteration fast.
2. **Packaging path for CLIs**: Provide guidance or `setup.cfg` examples for packaging select slop artifacts with `pipx`/`setuptools` when they prove stable.
3. **Prompt quality playbook**: Document best practices for writing high-context prompts that align with the Vibe Director role.
4. **Artifact tagging**: Add metadata (YAML/JSON) describing prompt IDs, LLM version, and runtime requirements to make results searchable.

## Long-term (6–12 months)
1. **Template-driven prompt runner**: Optional CLI that ingests prompts, calls preferred LLM endpoints, and writes slop/results with consistent naming.
2. **LLM provider abstraction**: Configuration-based selection of hosted LLMs (e.g., GPT-4o, Claude 3.5) without hard-coding providers in scripts.
3. **Community contributions**: Encourage PRs adding new vibes, prompts, and results; include lightweight review checklist focusing on intent alignment.
4. **Quality signals dashboard**: Simple static report summarizing number of prompts, success rate of smoke tests, and recent results to track progress.

## Success metrics
* Number of complete prompt → slop → result triads added.
* Percentage of artifacts covered by smoke tests in CI.
* Turnaround time from prompt creation to validated result.
* Diversity of vibes (domains, runtimes) represented in the library.
