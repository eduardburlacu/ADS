"""
Given an array of positive integers nums and an integer k,
    return the number of subarrays where the product of
    all the elements in the subarray is strictly less than k.
"""
def num_subarrays(nums:list[int], k:int)->int:
    left = out = 0
    prod = 1
    for right in range(len(nums)):
        prod *= nums[right]
        while prod >= k:
            prod /= nums[left]
            left += 1
        out += (right - left + 1)
    return out

if __name__=="__main__":
    print(
        num_subarrays([10, 5, 2, 6], 100)
    )
