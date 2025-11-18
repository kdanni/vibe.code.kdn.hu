# Prompt Library

This folder stores the "true source code" for each vibe: a high-context Markdown prompt that explains what to build and how success will be measured. Follow the prompt → slop → result flow described in [`docs/ARCHITECTURE.md`](../docs/ARCHITECTURE.md).

## How to add a prompt
1. Copy `prompt_template.md` and rename it using a unique ID (for example `p001_basic_cli_tool.md`).
2. Fill in the template sections with the requested vibe, constraints, and success criteria.
3. Commit the prompt alongside its generated slop and results when they are ready.

## Prompt template reference
Use the template below as-is to keep prompts consistent and searchable.

```markdown
# <Prompt ID>: <Short Title>

## Vibe
Describe the desired experience, tone, or outcome in a few sentences.

## Requirements
- List functional expectations.
- Include inputs/outputs, edge cases, and performance notes.

## Success Criteria
- How you will know the vibe has been achieved.
- What artifacts or screenshots to capture.

## Tooling and Constraints
- Preferred languages, frameworks, or services.
- Any forbidden approaches or dependencies.

## Sample Flow (optional)
Outline a quick example of how a user interacts with the output.
```
