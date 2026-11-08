# Parallel cricket statistics

Three deterministic branches calculate strike rate, balls per boundary, and the share of runs scored in boundaries. A final node combines the outputs.

[Source file](SIMPLE%20PARALLEL%20WORKFLOW.ipynb) · [Setup](README.md)

## Run

Edit `runs`, `balls`, `fours`, and `sixes`. Use positive runs and balls and at least one boundary.

## What to inspect

The returned state includes `sr`, `bpb`, `boundary_percent`, and `summary`.
