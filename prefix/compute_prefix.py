def prefix(nums:list)->list:
    pr = [nums[0]]
    for i in range(1,len(nums)):
        pr[i] = pr[i-1] + nums[i]
    return pr
