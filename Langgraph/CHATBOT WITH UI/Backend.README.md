# Chatbot backend

The shared backend invokes Ollama’s `llama3.2`, appends the response to the message state, and saves state using a SQLite checkpointer.

[Source file](Backend.py) · [Setup](README.md)

## Run

Run a Streamlit entry point from the chatbot directory. It imports this module and creates `chatbot.db` in the working directory.

## What to inspect

Use `chatbot` with a `configurable.thread_id` for a conversation. `retrieve_all_threads()` lists the thread IDs found in the database.
