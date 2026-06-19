# Workflow DAG

Workflow implements a workflow DAG which was discussed in the Reap Interview previously had, where we needed to design a workflow execution engine that allows execution of a laid out workflow:

```mermaid

validate -> reserve_order -> execute_order -> store_result -> update_order
                                           -> notify_owner -> send_email

```

Where the goal is to validate a workflow engine you build will:

1. Validate the workflow description is valid and has no cycles
2. Successfully executes workflow to completion, we don't care much for correctness, just complete code.
