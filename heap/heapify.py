def heapify(arr:list[int], i:int, heapsize:int) -> None:
    left = 2*i+1
    right = left +1
    best = i

    if left<heapsize and arr[left] > arr[best]:
        best = left
    if right<heapsize and arr[right] > arr[best]:
        best = right

    if best!=i:
        arr[i],arr[best] = arr[best],arr[i]
        heapify(arr,best,heapsize)

def insert(arr:list[int], key:int) -> None:
    arr.append(key)
    i = len(arr)-1
    parent = (i-1)//2
    while i>0 and arr[parent]<arr[i]:
        arr[parent], arr[i] = arr[i], arr[parent]
        i, parent = parent, (parent-1)//2
    return arr

def update_key(arr:list[int], i:int, key:int) -> None:
    if key<arr[i]:
        arr[i] = key
        heapify(arr,i,len(arr)) # neet downwards update aka heapify
    elif key>arr[i]:
        arr[i] = key
        parent = (i-1)//2
        while arr[parent]<arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent]
            i, parent = parent, (parent-1)//2

if __name__=="__main__":
    heap = [4,10,3,5,1]
    heapsize = len(heap)
    i = 0
    heapify(heap,i,heapsize)
    print(heap) # [10, 5, 3, 4, 1]

    i = 4
    heapify(heap,i,heapsize)
    print(heap) # [10, 5, 3, 4, 1]
    key=15
    insert(heap,key)
    print(heap) # [15, 10, 3, 5, 1, 4]

    i = 0
    key = 2
    update_key(heap,i,key)
    print(heap) # [10, 5, 3, 4, 1, 2]
