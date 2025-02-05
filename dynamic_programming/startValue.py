"""
Given an array of integers nums, you start with an initial positive value startValue.
In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
Return the minimum positive value of startValue such that the step by step sum is never less than 1.
"""

def minStartValue(nums: list[int]) -> int:
    curr = 0
    out = 1
    for num in nums:
        curr += num
        out = max(out, 1 - curr)
    return out
