def merge(arr, p:int, q:int, r:int):
    left, right = arr[p:q+1], arr[q+1:r+1]
    left.append(float("inf"))
    right.append(float("inf"))
    i, j = 0, 0
    for k in range(p, r+1):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1

def merge_sort(nums, p:int, r:int):
    if p<r:
        half = (r+p)//2
        merge_sort(nums, p, half)
        merge_sort(nums, half+1, r)
        merge(nums, p, half, r)

if __name__=="__main__":
    nums = [3,2,1,5,6,7,1,-5]
    merge_sort(nums, 0, len(nums)-1)
    print(nums)