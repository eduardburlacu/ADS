"""
Given two sorted integer arrays arr1 and arr2,
    return a new array that combines both of them and is also sorted.
"""
def merge(arr1:list, arr2:list)->list:
    i=j=0
    out = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            out.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            out.append(arr2[j])
            j += 1
        else:
            out.append(arr1[i])
            out.append(arr2[j])
            i += 1
            j += 1
    while i < len(arr1):
        out.append(arr1[i])
        i += 1
    while j < len(arr2):
        out.append(arr2[j])
        j += 1
    return out

if __name__=="__main__":
    x1 = [1,2,3,67,99,100]
    x2 = [1,4,4,10,20,30, 67, 98, 100, 100 ,100, 101, 10000]
    print(merge(x1, x2))