# Iterative tweet generator

OpenAI calls draft a tweet, evaluate it, and revise it using the evaluator’s feedback. Conditional routing stops on approval or after the revision limit.

[Source file](TWEET%20GENERATOR%20ITERATIVE%20WORKFLOW.ipynb) · [Setup](README.md)

## Run

Set `OPENAI_API_KEY`. Change `topic` and `max_iterations` in `initial_state`. Set `iteration` to zero for a new draft.

## What to inspect

Inspect the final tweet, evaluation, feedback, and revision history in the returned state. The model’s judgment determines approval.
