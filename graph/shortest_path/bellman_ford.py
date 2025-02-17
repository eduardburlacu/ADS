from typing import Dict, List, Set, Tuple

def shortest_paths(graph:Dict[int, Set[Tuple[int,float]]], source:int):
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
    parents, dists = shortest_paths(graph, source)
    print(f"Graph: {graph}")
    print(f"Parents: {parents}")
    print(f"Dists: {dists}")
    for target in range(len(graph)):
        print(
            f"Path from {source} to {target}: {backtrack_path(parents, target)} with cost {dists[target]}"
        )
