"""
Note that the shortest path algorithm for DAGs is well-defined even
 with negative weights, because there are no cycles.
The algorithm is similar to the one for Bellman-Ford, but it is
 more efficient because it does not need to iterate multiple times
 and check for negative cycles.
This is because by iterating in the topological order,
we are guaranteed that Bellman-Ford converges in a single pass,
as the information propagates in the iteration direction
for each edge from start to leaves.
"""
from typing import Dict, Set, Tuple, List


def topological_sort(dag:Dict[int, Set[Tuple[int, float]]])->List[int]:
    V = len(dag)
    parents = []
    visited = [False]*V

    def dfs(v:int):
        visited[v] = True
        for neighbor, _ in dag[v]:
            if not visited[neighbor]:
                dfs(neighbor)
        parents.append(v)

    for v in range(V):
        if not visited[v]:
            dfs(v)

    parents.reverse()
    return parents

def shortest_path(
        dag:Dict[int, Set[Tuple[int,float]]],
        source:int
)->Tuple[List[int], List[float]]:

    V = len(dag)
    dist = [float("inf")]*V; dist[source] = 0.
    ps = [None]*V
    vertices_sorted = topological_sort(dag)
    print(f"Vertices Topol. Sorted: {vertices_sorted}")

    for u in vertices_sorted:
        for v, weight in dag[u]:
            target = dist[u] + weight
            if dist[v] > target:
                dist[v] = target
                ps[v] = u
    return ps, dist



if __name__=="__main__":
    dag = {
        0: {(1, 1), (2, 4)},
        1: {(2, 2), (3, 5)},
        2: {(3, 1),(4, -1)},
        3: set(),
        4: {(0, 1), (3, 3)}
    }
    source = 0
    print(f"Graph: {dag}")
    parents, dists = shortest_path(dag, source)
    print(f"Parents: {parents}")
    print(f"Dists: {dists}")