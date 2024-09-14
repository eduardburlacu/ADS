"""
You are given a 0-indexed array nums of n integers, and an integer k.
The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements
 in nums between the indices i - k and i + k (inclusive).
If there are less than k elements before or after the index i, then the k-radius average is -1.
Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
The average of x elements is the sum of the x elements divided by x, using integer division.
"""
def getAverages( nums: list[int], k: int) -> list[int]:
    cumsum = [nums[0]]
    avgs = [-1] * len(nums)
    for i in range(1, len(nums)):
        cumsum.append(cumsum[-1] + nums[i])
    window = 2 * k + 1
    for c in range(k, max(len(nums) - k, k)):
        if c == k:
            avgs[c] = cumsum[c + k] // window
        else:
            avgs[c] = (cumsum[c + k] - cumsum[c - k - 1]) // window
    return avgs

if __name__=="__main__":
    print(
        getAverages([7,4,3,9,1,8,5,2,6],3)
    )
