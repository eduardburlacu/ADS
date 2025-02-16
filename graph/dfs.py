from collections import deque
from typing import Dict, Set

def dfs(graph: Dict[int,Set[int]],source:int):
    visited = set()
    queue = deque()
    queue.append(source)
    while len(queue)>0:
        node = queue.pop()
        visited.add(node)
        for v in graph[node]:
            if v not in visited:
                queue.append(v)
    return visited

if __name__ == "__main__":
    graph = {0:{1,2}, 1:{3}, 2:{3}, 3:{4}, 4:set()}
    print(dfs(graph, 0)) # {0, 1, 2, 3, 4}
    print(dfs(graph, 1)) # {1, 3, 4}
    print(dfs(graph, 2)) # {2, 3, 4}
    print(dfs(graph, 3)) # {3, 4}
    print(dfs(graph, 4)) # {4}
