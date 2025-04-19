"""
Given an adjacency-list representation of a multigraph GD.V; E/, describe an
O.V CE/-time algorithm to compute the adjacency-list representation of the
“equivalent” undirected graph G0
D.V; E0/, where E0 consists of the edges in E
with all multiple edges between two vertices replaced by a single edge and with all
self-loops removed.
"""

def multigraph2graph(multigraph:list[set[int]]):
    """
    Convert a multigraph to a graph by removing self-loops and multiple edges.
    :param multigraph: A list of sets representing the multigraph.
    :return: A list of sets representing the graph.
    """
    graph = {i:set() for i in multigraph} # O(V)
    for vtx, neighbors in multigraph.items():
        for neighbor in neighbors: # O(E)
            if neighbor != vtx and neighbor not in graph[vtx]: # O(1) operation
                graph[vtx].add(neighbor)
    return graph # O(V+E) time complexity

if __name__=="__main__":
    multigraph = {0:{0,1,2,2,3}, 1:{0,1,1,2,2}, 2:{0,1,2,3}, 3:{0,3,3,3}}
    graph = multigraph2graph(multigraph)
    print(graph) # {0: {1, 2, 3}, 1: {0, 2}, 2: {0, 1, 3}, 3: {0}}