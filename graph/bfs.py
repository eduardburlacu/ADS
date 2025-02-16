from collections import deque
from typing import Dict, Set

def bfs(graph: Dict[int,Set[int]],source:int):
    visited = set()
    queue = deque()
    queue.append(source)
    while len(queue)>0:
        node = queue.popleft()
        visited.add(node)
        for v in graph[node]:
            if v not in visited:
                queue.append(v)
    return visited

if __name__ == "__main__":
    graph = {0:{1,2}, 1:{3}, 2:{3}, 3:{4}, 4:set()}
    print(bfs(graph, 0)) # {0, 1, 2, 3, 4}
    print(bfs(graph, 1)) # {1, 3, 4}
    print(bfs(graph, 2)) # {2, 3, 4}
    print(bfs(graph, 3)) # {3, 4}
    print(bfs(graph, 4)) # {4}