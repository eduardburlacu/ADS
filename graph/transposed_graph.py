from typing import Dict, Set

def transpose(graph:Dict[int, Set[int]]):
    graph_t = {k:set() for k in graph}
    for node in graph:
        for neighbor in graph[node]:
            graph_t[neighbor].add( node)
    return graph_t

if __name__=="__main__":
    graph = {
        0:{1,2},
        1:{},
        2:{1,0}
    }
    graph_t = transpose(graph)
    print(graph_t)
