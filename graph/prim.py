"""
Implement Prim's algorithm for finding the minimum spanning tree (MST) of a graph.
"""

from typing import List, Dict, Tuple
from heapq import heappush, heappop

def prim_algorithm(
        graph: Dict[int, List[Tuple[int|float]]],
        start_node:int
)->List[Tuple[int, int]]:
    """
    Prim's algorithm to find the minimum spanning tree (MST) of a graph.
    - keep track of visited nodes and the edges that form the MST
    - act greedy by always adding the smallest edge that connects a visited node to an unvisited node

    Args:
        graph: A list of edges where each edge is represented as a tuple (u, v, weight).
        start_node: The starting node for the MST.

    Returns:
        A list of edges in the MST.
    """
    mst_edges = []
    visited = set()
    queue = [(0, start_node, None)]  # (weight, current_node, parent_node)
    while queue:
        weight, node, parent = heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        if parent is not None:
            mst_edges.append((parent, node))

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heappush(queue, (edge_weight, neighbor, node))
    return mst_edges


if __name__=="__main__":
    graph = {
        0: [(1, 2), (2, 3)],
        1: [(0, 2), (2, 1), (3, 4)],
        2: [(0, 3), (1, 1), (3, 2)],
        3: [(1, 4), (2, 5)]
    }
    print(f"Graph: {graph}")
    start_node = 1
    mst = prim_algorithm(graph, start_node)
    print(f"Minimum Spanning Tree edges: {mst}")
