"""
Given an integer array nums and an integer k,
    find the sum of the subarray with the largest sum whose length is k.
"""

def max_sum(nums:list[int], k:int)->int:
    assert k<=len(nums)
    s = 0
    for i in range(k):
        s += nums[i]
    best = s
    for i in range(k, len(nums)):
        s += nums[i]
        s -= nums[i-k]
        best = max(best, s)
    return best

if __name__=="__main__":
    print(
        max_sum([1,3,5,15,7,11,13,8],3)
    )
