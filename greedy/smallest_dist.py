def merge(a:list,b:list):
    i, j = 0, 0
    a.append(float("inf"))
    b.append(float("inf"))
    out=[]
    while i<len(a)-1 or j<len(b)-1:
        if a[i]<b[j]:
            out.append(a[i])
            i+=1
        else:
            out.append(b[j])
            j+=1
    return out


def merge_sort(nums:list[int])->list[int]:
    if len(nums)==0:
        return []
    elif len(nums)==1:
        return nums
    half = len(nums)//2
    a, b = nums[:half], nums[half:]
    return merge(merge_sort(a), merge_sort(b))


def find_idx(nums:list[int])->tuple[int]:
    if len(nums)<2:
        raise AttributeError("Cannot find any pair in a list of size <2")
    nums_sorted = merge_sort(nums)
    nums_sorted = [(idx,num) for idx, num in enumerate(nums_sorted)]
    # Greedy on sorted array
    idx = None
    best = float("inf")
    for k in range(1, len(nums)):
        idx_high, high = nums_sorted[k]
        idx_low, low = nums_sorted[k-1]
        if best>(high-low):
            best = high-low
            i,j = idx_low, idx_high
    if i < j:
        return i,j
    return j, i

if __name__ == "__main__":
    nums = [24, 35, 11, 29, 103, 0, 600, 17, 900, 99]
    print(merge_sort(nums))
    print(find_idx(nums))
