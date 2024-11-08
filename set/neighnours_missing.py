"""
Given an integer array nums,
find all the unique numbers x in nums that satisfy the following:
    x + 1 is not in nums, and x - 1 is not in nums.
"""
def unique(nums:list):
    out = []
    nums = set(nums)
    for num in nums:
        cond = num - 1 not in nums and num + 1 not in nums
        if cond:
            out.append(num)
    return out