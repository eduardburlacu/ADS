"""
Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
return a boolean array that represents the answer to each query.
A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13,
 answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
"""

def check_query(nums:list[int], queries:list[list[int, int]],limit:int)->list[bool]:
    # Compute the prefix sum list
    prefix = nums.copy()
    ans = []
    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
    for start, end in queries:
        if start == 0:
            ans.append(prefix[end]<limit)
        else:
            ans.append(prefix[end] - prefix[start-1] < limit)
    return ans

if __name__=="__main__":
    print(
        check_query(
            [1,3,5,7,9,11,13,15],
            queries=[[0,2],[1,2],[5,5],[6,7]],
            limit=10
        )
    )