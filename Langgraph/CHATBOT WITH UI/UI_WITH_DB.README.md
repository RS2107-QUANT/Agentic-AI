# Streamlit chatbot with saved conversations

This interface streams replies and populates the sidebar from LangGraph’s SQLite checkpoints.

[Source file](UI_WITH_DB.py) · [Setup](README.md)

## Run

Start Ollama with `llama3.2`, then run `python -m streamlit run UI_WITH_DB.py` from the chatbot directory.

## What to inspect

Create a conversation, send a message, and restart from the same directory to reopen the stored thread. Conversation data lives in the local `chatbot.db`.
