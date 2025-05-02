
from typing import Dict, Callable
from heapq import heappush, heappop
def a_star(
        graph,
        src:int,
        heuristic:Callable,
        dest:None|int = None
)->Dict[int, float|int]|float|int:

    queue = [(heuristic(src), src)]
    dist = {src:0}
    while len(queue)>0:
        f_node, node = heappop(queue)
        if node==dest:
            return dist[node]
        if f_node > dist.get(node,float("inf")) + heuristic(node):
            continue
        for neighbor, weight in graph[node]:
            g_neighbor = dist[node] + weight
            if g_neighbor < dist.get(neighbor, float("inf")):
                dist[neighbor] = g_neighbor
                heappush(
                    queue, (g_neighbor+heuristic(neighbor), neighbor)
                )
    return dist if dest is None else float("inf")


if __name__=="__main__":
    graph = {
        0: [(1, 1), (2, 4)],
        1: [(2, 2), (3, 5)],
        2: [(3, 1)],
        3: []
    }
    heuristic = lambda x: abs(x-2)
    print(a_star(graph, 0, heuristic)) # {0:0,1:1,2:3,3:4}
    graph = {0: [(1, 10), (2, 5)], 1: [(2, 2), (3, 1)], 2: [(1, 3), (3, 9), (4, 2)], 3: [(4, 4)], 4: []}
    print(a_star(graph, 0, heuristic)) # {0:0,1:8,2:5,3:9,4:7}
    print(a_star(graph, 0, heuristic, dest=2)) # 5
