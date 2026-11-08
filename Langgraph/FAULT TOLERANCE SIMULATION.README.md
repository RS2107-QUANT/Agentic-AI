# Fault tolerance simulation

A three-step graph writes checkpoints to an in-memory saver. The second step sleeps for 30 seconds so there is time to interrupt execution.

[Source file](FAULT%20TOLERANCE%20SIMULATION.ipynb) · [Setup](README.md)

## Run

Run the invocation cell and interrupt it during step 2. Then run the state-inspection cell in the same kernel.

## What to inspect

Look for the completed first step and the pending work in the snapshot for `thread-1`. Restarting the kernel clears these checkpoints.
