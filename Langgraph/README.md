# LangGraph projects

A collection of Python notebooks for learning LangGraph and a local Streamlit chatbot. The examples progress from deterministic graphs to model-backed workflows, loops, checkpointing and streaming.

## Setup

Use Python 3.13. From this folder, create and activate a virtual environment, then install the pinned dependencies.

```sh
python -m venv .venv
python -m pip install -r requirements.txt
jupyter lab
```

Choose the kernel from that environment. The deterministic notebooks run without a model. To run the OpenAI notebooks, set `OPENAI_API_KEY` in the shell that starts Jupyter. You can also copy `.env.example` to `.env` for notebooks that call `load_dotenv()`. For the Ollama examples, install and start Ollama locally and run `ollama pull llama3.2`.

## Notebook projects

### Deterministic workflows

- [Non-LLM workflow](NON%20LLM%20WORKKFLOW.ipynb) computes and labels a sample BMI through two sequential nodes. Use a positive height. The optional Mermaid diagram cell can require network access. [File README](NON%20LLM%20WORKKFLOW.README.md)
- [Conditional workflow](SIMPLE%20CONDITIONAL%20WORKFLOW.ipynb) routes a quadratic equation according to its discriminant. Use a nonzero quadratic coefficient. [File README](SIMPLE%20CONDITIONAL%20WORKFLOW.README.md)
- [Parallel workflow](SIMPLE%20PARALLEL%20WORKFLOW.ipynb) computes three cricket batting metrics in parallel and joins them into a summary. Use positive runs and balls and at least one boundary. [File README](SIMPLE%20PARALLEL%20WORKFLOW.README.md)
- [Fault tolerance simulation](FAULT%20TOLERANCE%20SIMULATION.ipynb) pauses for 30 seconds in its second node so you can interrupt the cell and inspect the latest checkpoint. Keep the same kernel and thread ID to inspect in-memory state. [File README](FAULT%20TOLERANCE%20SIMULATION.README.md)

### OpenAI workflows

- [Linear LLM workflow](LINEAR%20LLM%20WORKFLOW.ipynb) sends a question to one model node and records its answer. [File README](LINEAR%20LLM%20WORKFLOW.README.md)
- [Blog maker](BLOG%20MAKER%20WORKFLOW.ipynb) generates an outline, then uses it to draft a blog post. [File README](BLOG%20MAKER%20WORKFLOW.README.md)
- [Basic chatbot](BASIC%20CHATBOT.ipynb) adds model responses to the message history using an in-memory checkpointer. Type `exit` to leave the input loop. [File README](BASIC%20CHATBOT.README.md)
- [Review routing](LLM%20CONDITIONAL%20WORKFLOW%20FOR%20REVIEW.ipynb) classifies a review, then sends positive feedback to a thank-you node or negative feedback through diagnosis and response nodes. [File README](LLM%20CONDITIONAL%20WORKFLOW%20FOR%20REVIEW.README.md)
- [Parallel essay analysis](ESSAY%20ANALYSIS%20PARALLEL%20WORKFLOW.ipynb) evaluates language, analytical depth and clarity in parallel, then summarizes the feedback and averages the three scores. [File README](ESSAY%20ANALYSIS%20PARALLEL%20WORKFLOW.README.md)
- [Iterative tweet generator](TWEET%20GENERATOR%20ITERATIVE%20WORKFLOW.ipynb) drafts, evaluates and revises a post until the evaluator approves it or the configured revision limit is reached. [File README](TWEET%20GENERATOR%20ITERATIVE%20WORKFLOW.README.md)

### Local Ollama projects

- [Joke generator](JOKE%20GENERATOR.ipynb) generates and explains a joke, then shows checkpoint history. [File README](JOKE%20GENERATOR.README.md)
- [Streamlit chatbot](CHATBOT%20WITH%20UI/README.md) demonstrates basic replies, streaming and saved conversations.

See the [LangGraph documentation](https://docs.langchain.com/oss/python/langgraph/overview) for the graph and checkpoint APIs.
