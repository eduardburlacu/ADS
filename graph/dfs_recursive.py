from typing import Dict, List

def dfs(graph: Dict[int,List[int]])->List[int]:
    visited = []

    def dfs_visit(source:int) ->None:
        visited.append(source)
        for v in graph[source]:
            if v not in visited:
                dfs_visit(v)

    for src in graph:
        if src not in visited:
            dfs_visit(src)

    return visited

if __name__ == "__main__":
    graph = {0:[1,2], 1:[3], 2:[3], 3:[4], 4:[]}
    visited = dfs(graph)
    print(visited) # [0, 1, 3, 4, 2]