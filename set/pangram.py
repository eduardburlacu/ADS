"""
Given an integer array arr, count how many elements x there are,
    such that x + 1 is also in arr.
If there are duplicates in arr, count them separately.
"""

def count_succesors(nums:list[int]):
    freq = {}
    count = 0
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    for num in nums:
        nxt = num + 1
        if nxt in freq:
            count += min(freq[num], freq[num+1])
    return count