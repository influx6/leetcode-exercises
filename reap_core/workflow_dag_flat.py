"""Implements a basic workflow DAG that supports

1. Validation to ensure no cycle exists in the provided workflow definition
2. Executes the workflow and validates completion and working code.
3. Shows consistent behaviour.
"""

from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional

from pydantic import BaseModel


class NodeNameReuseException(Exception):
    """Exception thrown when a node attempts to use a already allocated name."""

    def __init__(
        self,
        name: str,
        transgressor: str,
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
        start: str,
        end: str,
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


def validate(
    actions: Dict[str, List[str]],
):
    """
    Validate the DAG definition has definitions that
    ensures
    """
    visited_nodes = set()
    visiting_nodes = []

    def walk_tree(
        depth: int,
        node: str,
        parent: Optional[str] = None,
    ):
        """Walk a node in depth first order"""
        print("Walking: ", node, " | from parent: ", parent)

        # if we are currently visiting this none and we meet it again,
        # then we have another cyclical dependency
        if node in visiting_nodes:
            raise CyclicalDependencyFound(depth, node, node)

        # if a node is already visited, then we can skip it
        # since we've walked it's path before
        if node in visited_nodes:
            return False

        children = actions.get(node, [])

        # mark node in visiting.
        visiting_nodes.append(node)

        # loop each child of visiting node and walk its tree to ensure
        # we don't find any cyclical dependencies.
        for child in children:
            walk_tree(depth + 1, child, node)

        visiting_nodes.pop()
        visited_nodes.add(node)

        return False

    # What we should do:
    #
    # 1. Walk the actions in breath first order, storing the
    # ones we've visited and confirm do not see another node depending on each other when their should be no cyclical dependency.
    for node in actions:
        try:
            walk_tree(0, node, None)
        except CyclicalDependencyFound as err:
            print("Found cyclical dependency from :", err)
            raise err


# Example 1: has no cyclical dependency
validate(
    {
        "validate": ["reserve_order"],
        "reserve_order": ["execute_order"],
        "execute_order": ["store_result", "notify_owner"],
        "store_result": ["update_order"],
        "update_order": [],
        "notify_owner": ["send_email"],
        "send_email": [],
    }
)

# Example 2: has no cyclical dependency but has multiple branches that end at the same node (diagmond shape)
validate(
    {
        # node starter: has two nodes
        "validate": ["reserve_order", "notify_order"],
        # Node path A: reserve-order -> execute-order -> notify_owner
        "reserve_order": ["execute_order"],
        "execute_order": ["notify_owner"],
        # Node path B: notify_order -> update_order -> notify_owner
        "notify_order": ["update_order"],
        "update_order": ["notify_owner"],
        # end result action has no other node
        "notify_owner": [],
    }
)

validate(
    {
        "validate": ["reserve_order", "notify_order"],
        "reserve_order": ["complete_payment"],  # 'complete_payment' is a leaf node
        "notify_order": ["complete_payment"],  # Both point to 'complete_payment'
    }
)

# Example 3: has cyclical dependency with a node pointing back at reserve
validate(
    {
        # node starter: has two nodes
        # Node path A: validate -> reserve-order
        #                          notify_order -> reserve_order
        "validate": ["reserve_order", "notify_order"],
        # Node path A: reserve-order -> execute-order -> notify_owner -> reserve_order
        "reserve_order": [],
        # Node path B: notify_order -> update_order -> notify_owner
        "notify_order": ["reserve_order"],
    }
)
