"""
Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

Ex: nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true].
For each query, the subarray sums are [12, 14, 12].
"""
def answer(nums:list[int], queries:list[list[int]], lim:int)->list[bool]:
    pr = [nums[0]]
    out =[]
    for i in range(1,len(nums)):
        pr.append(nums[i] + pr[-1])
    pr.append(0)
    for idx, (start, end) in enumerate(queries):
        out.append(pr[end]- pr[start - 1] < lim)
    return out

if __name__=="__main__":
    print(answer([1, 6, 3, 2, 7, 2],[[0, 3], [2, 5], [2, 4]], lim=13))
