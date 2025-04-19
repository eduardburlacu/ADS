def longest_increasing_substring(nums:list[int]):
    if len(nums)<2:
        return len(nums)

    #Base case: [c], longest_subseq = nums
    i, j = 0, 0
    best = 1
    for j in range(1, len(nums)):
        if nums[j-1]>=nums[j]:
            i=j
        best = max(best, j-i+1)
    return best

def longest_increasing_subseq(nums:list[int]):
    "Use the equality: dp[n] = max_{k\in 1:n-1} dp[k]+ 1[x_k<x_n]"
    if len(nums)<2:
        return len(nums)
    dp = [1] + [0] * (len(nums)-1)
    for n in range(1, len(nums)):
        for k in range(n):
            delta = 1 if nums[n]>nums[k] else 0
            dp[n] = max(dp[n],dp[k]+delta)
    return dp[-1]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(longest_increasing_substring(nums)) # 5
    nums = [1, 2, 3, 4, 3]
    print(longest_increasing_substring(nums)) # 4
    nums = [1, 2, 3, 2, 1]
    print(longest_increasing_substring(nums)) # 3
    nums = [1, 2, 1]
    print(longest_increasing_substring(nums)) # 2

    nums = [3, 1, 4, 11, 5, 9, 2, 6, 25, 33, 9]
    print(longest_increasing_subseq(nums)) # 7
    nums = [1, 11, 3, 21, 5]
    print(longest_increasing_subseq(nums)) # 3
    nums = [1, 11, 3, 21, 55]
    print(longest_increasing_subseq(nums)) # 4
