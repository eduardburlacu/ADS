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

    return parents.reverse()

def topological_sort_kahn(graph:Dict[int, Set[int]]):
    ...
    return

if __name__=="__main__":
    dag = { 0: {1, 2}, 1: {3}, 2: {3}, 3: set(),
            4: {2}, 5:set(), 6: {5}, 7: {6, 5},
            8: {7}, 9: {8}, 10:set()
            }
    print(topological_sort(dag, "dfs")) # [0, 1, 3, 2, 4, 6, 5, 7, 8, 9, 10]
    #print(topological_sort(dag, "kahn"))
