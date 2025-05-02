"""
Reference from:
    https://www.geeksforgeeks.org/strongly-connected-components/#1-kosarajus-algorithm

Kosaraju’s Algorithm involves two main phases:

- Performing Depth-First Search (DFS) on the Original Graph:
We first do a DFS on the original graph and record the finish times of nodes
(i.e., the time at which the DFS finishes exploring a node completely).
- Performing DFS on the Transposed Graph:
We then reverse the direction of all edges in the graph to create the transposed graph.
Next, we perform a DFS on the transposed graph, considering nodes
    in decreasing order of their finish times recorded in the first phase.
Each DFS traversal in this phase will give us one SCC.

Steps:
- DFS on Original Graph:
    Record finish times.
- Transpose the Graph:
    Reverse all edges.
- DFS on Transposed Graph:
    Process nodes in order of decreasing finish times to find SCCs.
"""

from typing import Dict, Set, List


def kosaraju_scc(graph:Dict[int, Set[int]])-> List[Set[int]]:
    V = len(graph)
    visited = [False]*V
    f_times=[-1]*V

    def dfs(v:int, scc:set=None):
        print(f"DFS in {v}")
        visited[v] = True
        t = -1
        if scc is not None:
            scc.add(v)
        for neighbor in graph[v]:
            if not visited[neighbor]: # this happens when the
                dfs(neighbor, scc)         # neighbor is not visited
                t = max(t, f_times[neighbor])
        t += 1
        f_times[v] = t
        return t
    # Compute the finishing times
    for source in graph:
        print(f"Source: {source}")
        if f_times[source]==-1:
            dfs(source)
    print(f"Finishing Times: {f_times}")
    # Reverse the graph
    graph_tr = dict()
    for vtx in graph:
        visited[vtx] = False # clear the visited array for the second DFS
        for neighbor in graph[vtx]:
            if neighbor not in graph_tr:
                graph_tr[neighbor] = []
            graph_tr[neighbor].append(vtx)

    print(f"Graph: {graph}")
    print(f"Graph Transposed: {graph_tr}")

    # Sort the vertices by finishing time
    vertices = list(range(V))
    vertices.sort(key=lambda x: f_times[x], reverse=True)
    print(f"Sorted Vertices: {vertices}")

    # Perform DFS on the transposed graph
    sccs = []
    for source in vertices:
        if not visited[source]:
            scc = set()
            dfs(source, scc)
            sccs.append(scc)
    return sccs

if __name__=="__main__":
    dag = {
        0: {2},
        1: {0},
        2: {1},
        3: {5},
        4: {3},
        5: {4}
    }
    sccs = kosaraju_scc(dag)
    for scc in sccs:
        print(scc)