from typing import Dict, Set, List

def tarjan_scc(graph:Dict[int, Set[int]])-> List[Set[int]]:
    V = len(graph)
    t = 0
    visit_time = [-1] * V
    low = [-1]* V
    sccs = []
    on_stack = [False]*V
    stack = []

    def dfs(v:int):
        stack.append(v)
        on_stack[v] = True
        nonlocal t
        low[v] = t; visit_time[v] = t
        t += 1

        for neighbor in graph[v]:
            if visit_time[neighbor] == -1: # forward edge
                dfs(neighbor)
                low[v] = min(low[v], low[neighbor])

            elif on_stack[neighbor]: # back edge
                low[v]= min(low[v], visit_time[neighbor])

        if low[v] == visit_time[v]:
            scc = set()
            node = -1 #some unreachable value
            while node != v:
                node = stack.pop()
                on_stack[node] = False
                scc.add(node)
            sccs.append(scc)

    for source in graph:
        if visit_time[source]==-1:
            dfs(source)
    return sccs

if __name__=="__main__":
    dag = {
        0: {2},
        1: {0},
        2: {1},
        3: {5},
        4: {3},
        5: {4}
    }
    sccs = tarjan_scc(dag)
    for scc in sccs:
        print(scc)