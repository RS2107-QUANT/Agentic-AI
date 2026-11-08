# Conditional review responses

A structured sentiment classifier routes positive reviews to a thank-you node. Negative reviews go through a diagnosis node before a reply is drafted.

[Source file](LLM%20CONDITIONAL%20WORKFLOW%20FOR%20REVIEW.ipynb) · [Setup](README.md)

## Run

Set `OPENAI_API_KEY`, edit `initial_state['review']`, and run the notebook. Try a positive review and a review describing a bug to exercise both routes.

## What to inspect

Check `sentiment` and `response` in `final_state`. The negative branch also records issue type, tone, and urgency in `diagnosis`.
