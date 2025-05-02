from typing import Dict
from heapq import heappush, heappop

# Graph is represented as
# src -> (neighbor, weight)

def dijkstra(
        graph,
        src:int,
        dest:None|int = None
)->Dict[int, float|int]|float|int:
    queue = [(0, src)]
    dist = {src: 0}
    while len(queue)>0:
        node_dist, node = heappop(queue)
        if dest is not None and node == dest:
            return dist[dest]
        if node_dist > dist.get(node, float("inf")):
            continue
        for neighbor, weight in graph[node]:
            current = weight + node_dist
            if current < dist.get(neighbor, float("inf")):
                dist[neighbor] = current
                heappush(queue, (current, neighbor))
    return dist if dest is None else float("inf")

if __name__ == "__main__":
    graph = {
        0: [(1, 1), (2, 4)],
        1: [(2, 2), (3, 5)],
        2: [(3, 1)],
        3: []
    }
    print(dijkstra(graph, 0)) # {0: 0, 1: 1, 2: 3, 3: 4}
    graph = {0: [(1, 10), (2, 5)], 1: [(2, 2), (3, 1)], 2: [(1, 3), (3, 9), (4, 2)], 3: [(4, 4)], 4: []}
    print(dijkstra(graph, 0)) # {0:0,1:8,2:5,3:9,4:7}
    print(dijkstra(graph, 0, 2))