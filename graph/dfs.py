from collections import deque
from typing import Dict, Set

def dfs(graph: Dict[int,Set[int]],source:int):
    visited = {source}
    stack = deque()
    stack.append(source)
    while len(stack)>0:
        node = stack.pop()
        for v in graph[node]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return visited

if __name__ == "__main__":
    graph = {0:{1,2}, 1:{3}, 2:{3}, 3:{4}, 4:set()}
    print(dfs(graph, 0)) # {0, 1, 2, 3, 4}
    print(dfs(graph, 1)) # {1, 3, 4}
    print(dfs(graph, 2)) # {2, 3, 4}
    print(dfs(graph, 3)) # {3, 4}
    print(dfs(graph, 4)) # {4}

    graph = {0:{1,2}, 1:{3}, 2:{3}, 3:{4}, 4:set()}
    print(dfs(graph, 0)) # {0, 1, 2, 3, 4}

