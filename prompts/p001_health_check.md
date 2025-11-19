# p001: Environment Health Check Prompt

## Vibe
Provide a minimal request whose only purpose is to confirm the prompt→slop→result pipeline works. Keep the tone light and observational.

## Requirements
- Ask for a trivial program or textual artifact that proves the system can process prompts.
- No external dependencies or complex logic; the output can simply echo a message.
- Include a reminder to log any setup anomalies that appear during execution.

## Success Criteria
- The resulting artifact runs (or renders) without errors using the default project setup.
- Output clearly states it is a health check or proof of concept.
- Any unexpected issues discovered during execution are documented in accompanying notes.

## Tooling and Constraints
- Prefer standard language/runtime already available in the base image (e.g., Python or shell).
- Avoid network calls and heavy compute tasks.
- Keep total runtime under a few seconds.

## Sample Flow (optional)
1. Developer generates slop from this prompt.
2. Slop instructs the agent to create a script that prints "Health check passed".
3. Resulting script is executed once and its console output is captured in `results/`.
