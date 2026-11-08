# Joke generator

A two-node Ollama workflow generates a joke and explains it. It stores checkpoints in memory under a configurable thread ID.

[Source file](JOKE%20GENERATOR.ipynb) · [Setup](README.md)

## Run

Start Ollama, pull `llama3.2`, and change the `topic` in the invocation cell.

## What to inspect

The `joke` and `explanation` entries hold model messages. Use `.content` for their text. The last cells inspect the saved state and its history.
