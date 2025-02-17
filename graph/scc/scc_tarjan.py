"""
Reference from:
    https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

Tarjan’s Algorithm is more efficient because it finds SCCs in a single DFS pass
    using a stack and some additional bookkeeping:

DFS Traversal: During the DFS, maintain an index for each node and
the smallest index (low-link value) that can be reached from the node.

Stack: Keep track of nodes currently in the recursion stack (part of the current SCC).

Identifying SCCs: When a node’s low-link value equals its index, it means we have found an SCC.
    Pop all nodes from the stack until we reach the current node.

Steps:
Initialize index to 0.
For each unvisited node, perform DFS.
Set the node’s index and low-link value.
Push the node onto the stack.
For each adjacent node, either perform DFS if it’s not visited or
    update the low-link value if it’s in the stack.
If the node’s low-link value equals its index,
    pop nodes from the stack to form an SCC.
"""

from typing import Dict, Set, List

def tarjan_scc(graph:Dict[int, Set[int]])-> List[Set[int]]:
    V = len(graph)
    t = 0
    visit_time = [-1] * V
    low = [-1]* V
    sccs = []
    on_stack = [False]*V
    stack = []

    def dfs(v:int):
        stack.append(v)
        on_stack[v] = True
        nonlocal t
        low[v] = t; visit_time[v] = t
        t += 1

        for neighbor in graph[v]:
            if visit_time[neighbor] == -1: # forward edge
                dfs(neighbor)
                low[v] = min(low[v], low[neighbor])

            elif on_stack[neighbor]: # back edge
                low[v]= min(low[v], visit_time[neighbor])

        if low[v] == visit_time[v]:
            scc = set()
            node = -1 #some unreachable value
            while node != v:
                node = stack.pop()
                on_stack[node] = False
                scc.add(node)
            sccs.append(scc)

    for source in graph:
        if visit_time[source]==-1:
            dfs(source)
    return sccs

def kosaraju_scc(graph:Dict[int, Set[int]])-> List[Set[int]]:
    V = len(graph)
    t = 0
    visit_time = [-1] * V
    low = [-1]* V
    sccs = []
    on_stack = [False]*V
    stack = []

    def dfs(v:int):
        stack.append(v)
        on_stack[v] = True
        nonlocal t
        low[v] = t; visit_time[v] = t
        t += 1

        for neighbor in graph[v]:
            if visit_time[neighbor] == -1: # forward edge
                dfs(neighbor)
                low[v] = min(low[v], low[neighbor])

            elif on_stack[neighbor]: # back edge
                low[v]= min(low[v], visit_time[neighbor])

        if low[v] == visit_time[v]:
            scc = set()
            node = -1 #some unreachable value
            while node != v:
                node = stack.pop()
                on_stack[node] = False
                scc.add(node)
            sccs.append(scc)

    for source in graph:
        if visit_time[source]==-1:
            dfs(source)
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
    sccs = tarjan_scc(dag)
    for scc in sccs:
        print(scc)