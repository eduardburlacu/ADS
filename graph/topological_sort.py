from typing import  Dict, Set, Literal
from collections import deque

def topological_sort(graph:Dict[int, Set[int]], mode:Literal["dfs", "kahn"]):
    if mode == "dfs":
        return topological_sort_dfs(graph)
    elif mode == "kahn":
        return topological_sort_kahn(graph)
    else:
        raise ValueError("Invalid mode")

def topological_sort_dfs(graph:Dict[int, Set[int]]):
    parents = []
    visited = set()

    def dfs(v:int):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        parents.append(v)

    for src in graph:
        if src not in visited:
            dfs(src)
    parents.reverse()
    return parents

def topological_sort_kahn(graph:Dict[int, Set[int]]):
    #Compute in-degree in O(E)
    in_degree = [0] * len(graph)
    queue = deque()
    top_sort = []
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    #Find and cache sources in O(V)
    for node, degree in enumerate(in_degree):
        if degree == 0:
            queue.append(node)

    counter, V = 0, len(graph)
    while(len(queue))>0:
        counter += 1
        if counter>V:
            # the graph contains a cycle, return only
            # the DAG subpart before the cycle
            return top_sort
        src = queue.popleft()
        top_sort.append(src)
        for neighbor in graph[src]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor]==0:
                queue.append(neighbor)
    return top_sort


if __name__=="__main__":
    dag = { 0:set() , 1: {0}, 2: {0}, 3: {1, 2},
            4: {2}, 5:set(), 6: {5}, 7: {6, 5},
            8: {7}, 9: {8}, 10:set()
            }
    print(topological_sort(dag, "dfs")) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]g
    print(topological_sort(dag, "kahn"))
