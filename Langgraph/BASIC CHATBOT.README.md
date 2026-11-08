# Basic chatbot

One OpenAI-backed node appends replies to a LangGraph message list. An in-memory checkpointer keeps conversations separate by thread ID.

[Source file](BASIC%20CHATBOT.ipynb) · [Setup](README.md)

## Run

Set `OPENAI_API_KEY` in the shell that starts Jupyter. Run the sample cell, then enter messages in the interactive cell. Type `exit` to finish.

## What to inspect

The sample uses thread `demo`. The interactive loop uses thread `1` and prints the latest assistant message. Restarting the kernel clears its in-memory history.
