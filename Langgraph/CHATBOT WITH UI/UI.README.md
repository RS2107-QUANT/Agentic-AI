# Basic Streamlit chatbot

The basic interface renders a Streamlit chat and waits for a full model reply. It uses a fixed thread ID and keeps its displayed messages in Streamlit session state.

[Source file](UI.py) · [Setup](README.md)

## Run

Start Ollama with `llama3.2`, then run `python -m streamlit run UI.py` from the chatbot directory.

## What to inspect

Enter a message and wait for the full reply. Use the database UI for a sidebar with stored conversations.
