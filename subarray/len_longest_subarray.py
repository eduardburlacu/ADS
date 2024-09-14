"""
Given a positive integer array nums and an integer k,
find the length of the longest subarray that has a sum less than or equal to k
"""

def len_max_subarray(nums:list, k:int)->int:
    left = current = best = 0
    for right in range(len(nums)):
        current += nums[right]
        while current > k:
            current -= nums[left]
            left += 1
        best = max(best, right - left + 1)
    return best

if __name__=="__main__":
    n = [11, 1, 2, 8, 2, 4]
    target = 16
    print(
        len_max_subarray(n, target)
    )
