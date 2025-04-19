from collections import deque
from typing import Dict, Set

def bfs(graph: Dict[int,Set[int]], s:int):
    queue = deque()
    queue.appendleft(s)
    visited = {s}
    while len(queue)>0:
        node = queue.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.appendleft(neighbor)
    return visited

if __name__ == "__main__":
    graph = {0:{1,2}, 1:{3}, 2:{3}, 3:{4}, 4:set()}
    print(bfs(graph, 0)) # {0, 1, 2, 3, 4}
    print(bfs(graph, 1)) # {1, 3, 4}
    print(bfs(graph, 2)) # {2, 3, 4}
    print(bfs(graph, 3)) # {3, 4}
    print(bfs(graph, 4)) # {4}