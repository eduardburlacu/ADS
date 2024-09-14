def prefix_sum(nums:list[int])->list[int]:
    prefix = nums.copy()
    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
    return prefix

if __name__=="__main__":
    print(
        prefix_sum([1,5,7,8,9,-5,-6,3,9,8,10])
    )
    