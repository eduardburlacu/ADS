import random

def merge(arr1:list, arr2:list)->list:
    "O(L+R)"
    idx = 0
    left, L, right, R = 0, len(arr1), 0, len(arr2)
    m = min(L, R)
    out = []
    while left < L and right < R:
        if arr1[left]<arr2[right]:
            out.append(arr1[left])
            left+=1
        else:
            out.append(arr2[right])
            right+=1
    if left<L:
        out.extend(arr1[left:])
    elif right<R:
        out.extend(arr2[right:])
    return out

def merge_sort(nums:list):
    if len(nums)<2:
        return nums
    half = len(nums)//2
    left, right = nums[:half], nums[half:]

    return merge(merge_sort(left), merge_sort(right))

if __name__=="__main__":
    arr = [random.randint(0, 1_000) for _ in range(30)]
    arr.sort(reverse=True)
    print(arr)
    arr_sort = merge_sort(arr)
    print(arr_sort)