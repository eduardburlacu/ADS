from typing import Dict, List, Set, Tuple

def bellman_ford(
        graph:Dict[int, Set[Tuple[int,float]]], source:int,
        detect_negative_cycle:bool=False
)-> Tuple[List[int], List[float]]:
    V=len(graph)
    dist = [float("inf")]*V
    dist[source] = 0.
    ps = [None]*V
    for _ in range(V-1):
        for u in range(V):
            for v, w in graph[u]:
                target = dist[u] + w
                if dist[v] > target:
                    dist[v] = target
                    ps[v] = u

    if detect_negative_cycle:
        for u in range(V):
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    raise ValueError("Negative Cycle Detected")
        print("No negative cycle detected")
    return ps, dist

def backtrack_path(parents:List[int], target:int):
    "Find the trace from source -> target given the parents and the d"
    path = []
    while target is not None:
        path.append(target)
        target = parents[target]
    path.reverse()
    return path

if __name__=="__main__":
    graph = {
        0: {(1, 1), (2, 4)},
        1: {(2, 2), (3, 5)},
        2: {(3, 1),(4, -1)},
        3: set(),
        4: {(0, 1), (3, 3)}
    }
    source = 0
    print(f"Graph: {graph}")
    parents, dists = bellman_ford(graph, source, detect_negative_cycle=True)
    print(f"Parents: {parents}")
    print(f"Dists: {dists}")
    for target in range(len(graph)):
        path = backtrack_path(parents, target)
        print(
            f"Path from {source} to {target}: {path} with cost {dists[target]}"
        )
