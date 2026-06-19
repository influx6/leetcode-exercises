"""Implements a basic workflow DAG that supports

1. Validation to ensure no cycle exists in the provided workflow definition
2. Executes the workflow and validates completion and working code.
3. Shows consistent behaviour.
"""

from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional

from pydantic import BaseModel


class WorkflowActionDefinition(BaseModel):
    name: str
    waits_for: List[str]
    next_actions: List[WorkflowActionDefinition]

    def __init__(
        self,
        name: str,
        waits_for: List[str],
        next_actions: List[WorkflowActionDefinition],
    ):
        self.name = name
        self.waits_for = waits_for
        self.next_actions = next_actions


class NodeNameReuseException(Exception):
    """Exception thrown when a node attempts to use a already allocated name."""

    def __init__(
        self,
        name: str,
        transgressor: WorkflowActionDefinition,
    ):
        self.name = name
        self.transgressor = transgressor

    def __str__(self):
        return f"""Found attempt to re-use pre-allocated:
            name: {self.name}  by
            node: {self.transgressor} 
        """


class CyclicalDependencyFound(Exception):
    """Exception thrown when a node has cyclical dependency against another."""

    def __init__(
        self,
        depth: int,
        start: WorkflowActionDefinition,
        end: WorkflowActionDefinition,
    ):
        self.depth = depth
        self.start = start
        self.end = end

    def __str__(self):
        return f"""Found cyclical dependency from:
        Nodes:
            node: {self.start} 
        against 
            node: {self.end}
        At:
            Depth: {self.depth}
        """


class ExecutionDag(BaseModel):
    actions: List[WorkflowActionDefinition]

    def __init__(self, actions: List[WorkflowActionDefinition]):
        self.actions = actions

    def validate(
        self,
    ):
        """
        Validate the DAG definition has definitions that
        ensures
        """
        name_to_nodes = {}
        visited_nodes = []
        visiting_nodes = []

        def walk_tree(
            depth: int,
            node: WorkflowActionDefinition,
            parent: Optional[WorkflowActionDefinition] = None,
        ):
            if node.name in name_to_nodes:
                raise NodeNameReuseException(node.name, node)

            # once done remove it from visiting and
            # add to visited.
            if node in visited_nodes and parent:
                raise CyclicalDependencyFound(depth, node, parent)

            pass

        # What we should do:
        #
        # 1. Walk the actions in breath first order, storing the
        # ones we've visited and confirm do not see another node depending on each other when their should be no cyclical dependency.
        for node in self.actions:
            try:
                walk_tree(0, node, None)
            except CyclicalDependencyFound as err:
                print("Found cyclical dependency from :", err)
                raise err


type DagCallable = Callable[[Any], Any]


class Workflow(BaseModel):
    action: Dict[str, DagCallable]
    dag: ExecutionDag

    def __init__(
        self,
        dag: ExecutionDag,
        actions: Dict[str, DagCallable],
    ):
        self.dag = dag
        self.actions = actions
        # validate dag representation is correct.
        self.dag.validate()

    def execute(self, input: Any) -> Dict[str, Any]:
        return {}


def default_action(value: Any) -> Dict:
    return {"success": True}


if __name__ == "__main__":
    workflow = Workflow(
        dag=ExecutionDag(
            [
                WorkflowActionDefinition(
                    name="validate",
                    waits_for=[],
                    next_actions=[
                        WorkflowActionDefinition(
                            "reserve_order",
                            [],
                            [
                                WorkflowActionDefinition(
                                    "execute_order",
                                    [],
                                    [
                                        WorkflowActionDefinition(
                                            "store_result",
                                            [],
                                            [
                                                WorkflowActionDefinition(
                                                    "update_order",
                                                    [],
                                                    [],
                                                ),
                                            ],
                                        ),
                                        WorkflowActionDefinition(
                                            "notify_owner",
                                            [],
                                            [
                                                WorkflowActionDefinition(
                                                    "send_email",
                                                    [],
                                                    [],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ]
        ),
        actions={
            "validate": default_action,
            "reserve_order": default_action,
            "execute_order": default_action,
            "store_result": default_action,
            "update_order": default_action,
            "notify_owner": default_action,
            "send_email": default_action,
        },
    )
