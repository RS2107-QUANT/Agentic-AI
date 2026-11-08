# Parallel essay analysis

Three model nodes score language, analytical depth, and clarity. Their score lists are combined by a reducer before a final node summarizes the feedback.

[Source file](ESSAY%20ANALYSIS%20PARALLEL%20WORKFLOW.ipynb) · [Setup](README.md)

## Run

Set `OPENAI_API_KEY`, replace `essay` with the text to evaluate, and run the notebook.

## What to inspect

Inspect `final_state` for the individual feedback, the combined feedback, and `avg_score`. The scores are model judgments.
