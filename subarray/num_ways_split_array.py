"""
Given an integer array nums, find the number of ways
 to split the array into two parts so that the first section has a sum greater than or equal to
 the sum of the second section.
The second section should have at least one number.
"""
def num_incr_splits(nums:list[int])->int:
    # NOTES
    # a) cumsum[-1] = sum of all entries
    # b) for loop to determine the point
    cumsum = nums.copy()
    for i in range(1, len(nums)):
        cumsum[i] = cumsum[i-1] + nums[i]
    th = 0
    while 2 * cumsum[th] < cumsum[-1]:
        th += 1
    print(f"TH={th}")
    #Get the count [a b c d e f (g ... v w x y ) z]
    return len(nums) - 1 - th

if __name__=="__main__":
    print(num_incr_splits(
        [1,3,5,7,9,11,13,15]
    ))