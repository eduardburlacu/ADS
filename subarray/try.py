"""
Given an integer array nums and an integer k,
    find the sum of the subarray with the largest sum whose length is k
"""
def max_sum(arr:list, k:int)->int:
    curr = 0
    for i in range(k):
        curr += arr[i]
    best = curr
    for i in range(k,len(arr)):
        curr += (arr[i]-arr[i-k])
        best = max(best, curr)
    return best

if __name__=="__main__":
    print(max_sum([1,3,5,15,7,11,13,8],3))
