from typing import  Dict, Set, Literal


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
    ...
    return

if __name__=="__main__":
    dag = { 0:set() , 1: {0}, 2: {0}, 3: {1, 2},
            4: {2}, 5:set(), 6: {5}, 7: {6, 5},
            8: {7}, 9: {8}, 10:set()
            }
    print(topological_sort(dag, "dfs")) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]g
    #print(topological_sort(dag, "kahn"))
