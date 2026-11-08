# Blog maker

Two sequential OpenAI calls generate an outline and then draft a blog post from that outline.

[Source file](BLOG%20MAKER%20WORKFLOW.ipynb) · [Setup](README.md)

## Run

Set `OPENAI_API_KEY`, edit `initial_state['title']`, and run the cells in order.

## What to inspect

Read `final_state['outline']` for the plan and `final_state['content']` for the draft.
