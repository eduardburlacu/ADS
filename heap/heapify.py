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

def build_max_heap(arr:list[int]) -> None:
    heapsize = len(arr)
    for i in range((heapsize-1)//2, -1, -1):
        heapify(arr, i, heapsize)

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
        while parent>=0 and arr[parent]<arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent]
            i, parent = parent, (parent-1)//2

def heapsort(arr:list[int]) -> None:
    heapsize = len(arr)
    build_max_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[0],arr[i] = arr[i],arr[0]
        heapsize -= 1
        heapify(arr, 0, heapsize)


if __name__=="__main__":

    array = [4, 10, 3, 5, 1, 2, 6, 7]
    build_max_heap(array)
    print(array) # [10, 7, 6, 5, 1, 2, 3, 4]

    array = [4, 10, 3, 5, 1, 2, 6, 7]
    heapsort(array)
    print(array) # [1, 2, 3, 4, 5, 6, 7, 10]

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

    heap.append(0)
    print(heap[len(heap)//2:]) # [4, 1, 2, 0]
