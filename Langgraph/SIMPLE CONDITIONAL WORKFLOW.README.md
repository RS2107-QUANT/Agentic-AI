# Conditional quadratic solver

A deterministic graph computes the discriminant and routes to one of three branches for two real roots, a repeated root, or no real roots.

[Source file](SIMPLE%20CONDITIONAL%20WORKFLOW.ipynb) · [Setup](README.md)

## Run

Change `a`, `b`, and `c` in `initial_state`. Use a nonzero `a` to keep the equation quadratic.

## What to inspect

The returned `result` contains the real-root result for the selected branch. Try coefficients `(2, -6, 4)`, `(1, 2, 1)`, and `(1, 0, 1)` to cover all three branches.
