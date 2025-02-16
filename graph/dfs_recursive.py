from typing import List, Dict

def dfs_visit(graph:Dict[int,List[int]], source:int, visited:Dict[int, int], path:List[int]=None)->None:
    for v in graph[source]:
        if v not in visited:
            visited[v] = source
            dfs_visit(graph, v, visited)

def dfs(graph: Dict[int,List[int]])->Dict[int,int]:
    visited = dict() # node visited: parent
    for src in graph:
        if src not in visited:
            dfs_visit(graph, src, visited)
    return visited

if __name__ == "__main__":
    graph = {0:[1,2], 1:[3], 2:[3], 3:[4], 4:[]}
    visited = dfs(graph)
    print(visited) # {1: 0, 3: 1, 4: 3, 2: 0}