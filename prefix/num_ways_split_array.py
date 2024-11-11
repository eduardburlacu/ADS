"""
Given an  array nums of length n. nums contains a valid split at index i if the following are true:
- The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
- There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.
"""

def waysToSplitArray(nums: list[int]) -> int:
    pr = [nums[0]]
    for i in range(1, len(nums)):
        pr.append(nums[i] + pr[-1])
    mean = pr[-1]/2
    count = 0
    for i in range(len(nums)-1):
        if pr[i] >= mean:
            count += 1
    return count

# Or use DP + sum(list)
def dp_waysToSplitArray(nums: list[int]) -> int:
    mean = sum(nums) / 2
    curr = counts = 0
    for i in range(len(nums) - 1):
        curr += nums[i]
        if curr >= mean:
            counts += 1
    return counts
