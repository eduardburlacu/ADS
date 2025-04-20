def topological_sort(graph):
    visited = set()
    topsort = []

    def dfs(s:int):
        visited.add(s)
        for neighbor in graph[s]:
            if neighbor not in visited:
                dfs(neighbor)
        topsort.append(s)

    for node in graph:
        if node not in visited:
            dfs(node)
    topsort.reverse()
    return topsort

def number_paths(s:int, d:int, graph):
    top_sort = topological_sort(graph)
    start, end = 0, len(top_sort) -1
    for idx, node in enumerate(top_sort):
        if node==s:
            start=idx
        elif node==d:
            end=idx
    top_sort = top_sort[start:end+1]
    # Find the number of simple paths. Let dp[i] denote the number of simple paths from s to a node i
    # dp[i]= sum_k A_ki dp[k]
    dp = dict()
    for node in top_sort:
        dp[node] = 1 if node==s else 0

    for node in dp:
        for neighbor in graph[node]:
            if neighbor in dp:
                dp[neighbor] += dp[node]
    return dp[d]

if __name__=="__main__":
    dag = { 0:set() , 1: {0}, 2: {0}, 3: {1, 2},
            4: {2}, 5:set(), 6: {5}, 7: {6, 5},
            8: {7}, 9: {8}, 10:set()
            }
    print(topological_sort(dag)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]g

    print(number_paths(9, 5, dag))