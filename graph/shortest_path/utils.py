from typing import Dict, List, Set

def init(graph:Dict[int, Set[int]], source:int):
    assert 0<=source<len(graph)
    V = len(graph)
    parents = [None]*V
    dists = [float("inf")]*V
    dists[source] = 0
    return parents, dists

def relax(u:int, v:int, w:int, parents:List[int], dists:List[int]):
    targ = dists[u] + w
    if dists[v] > targ:
        dists[v] = targ
        parents[v] = u
