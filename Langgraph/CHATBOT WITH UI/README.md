# LangGraph Streamlit chatbot

This local chatbot uses `llama3.2` through Ollama. The LangGraph backend appends human and assistant messages to a conversation, and its SQLite checkpointer stores state per thread.

## Run locally

Install the dependencies from the [LangGraph setup](../README.md), start Ollama, and run `ollama pull llama3.2`. From the chatbot directory, choose one entry point.

```sh
python -m streamlit run UI_WITH_DB.py
```

- [UI.py](UI.py) sends one request at a time with a fixed thread ID. [File README](UI.README.md)
- [UI_WITH_STREAMING.py](UI_WITH_STREAMING.py) streams assistant messages and keeps the thread list in the current Streamlit session. [File README](UI_WITH_STREAMING.README.md)
- [UI_WITH_DB.py](UI_WITH_DB.py) streams assistant messages and restores saved thread IDs from SQLite after a restart. [File README](UI_WITH_DB.README.md)
- [Backend.py](Backend.py) defines the graph, model and SQLite checkpointer used by all three variants. [File README](Backend.README.md)

The backend creates `chatbot.db` in the current working directory when it runs. The database is ignored by Git and can contain chat history. The app is intended for local use.

See the [Streamlit CLI documentation](https://docs.streamlit.io/develop/api-reference/cli/run) for launch options.
