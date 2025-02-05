"""
Find the minimum cost of transforming string u into string v using the following operations:
    - insert a character with cost c_i
    - delete a character with cost c_d
    - substitute a character with cost c_s
Return the minimum cost.
Use dynamic programming to solve this problem in O(m*n) time, where m is the length of u and n is the length of v.
See https://en.wikipedia.org/wiki/Edit_distance
"""
def D(u:str,v:str,c_i:int,c_d:int,c_s:int)->int:
    m, n = len(u), len(v)
    print("m: ",m)
    print("n: ",n)
    dist = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        dist[i][0] = i * c_d
    for j in range(1, n+1):
        dist[0][j] = j * c_i
    for i in range(1,m+1):
        for j in range(1,n+1):
            delta = 0 if u[i-1] == v[j-1] else c_s
            dist[i][j] = min(
                dist[i-1][j-1] + delta,
                dist[i-1][j] + c_d,
                dist[i][j-1] + c_i
            )
    print("dist: ",dist)
    return dist[m][n]



if __name__=="__main__":
    u = "xihi"
    v = "hii"
    c_i = 1
    c_d = 1
    c_s = 1
    print(D(u,v,c_i,c_d,c_s))
    # Output: 2
    # Explanation: delete x and substitute x with h
    u = "kitten"
    v = "sitting"
    print(D(u,v,c_i,c_d,c_s))
    # Output: 3
    # Explanation: substitute k with s, substitute e with i, insert g