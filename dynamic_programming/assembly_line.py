def min_time(
        a:list[list[int]], # size 2 x n
        t:list[list[int]], # size 2 x n-1
        e:list[int], # len=2
        x:list[int]  # len=2
):
    """
    Start from state 0 and finish at state s+2
    Consider a recursion on 2 * (n+2) map.

    E.g.
    I only go on station 1/2--> I traverse the first/second row of the matrix

    """
    n = len(a[0])
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = e[0] + a[0][0]
    dp[1][0] = e[1] + a[1][0]

    for i in range(1, n):
        dp[0][i] = min(
            dp[0][i-1],
            dp[1][i-1]+t[1][i-1]
        ) + a[0][i]

        dp[1][i] = min(
            dp[1][i-1],
            dp[0][i-1]+t[0][i-1]
        ) + a[1][i]

    print(dp)
    return min(dp[0][-1]+x[0], dp[1][-1]+x[1])

if __name__=="__main__":
    a = [
        [7,9,3,4,8,4],
        [8,5,6,4,5,7]
    ]
    t = [
        [2,3,1,3,4],
        [2,1,2,2,1]
    ]
    e = [2, 4]
    x = [3, 2]
    print(min_time(a, t, e, x))