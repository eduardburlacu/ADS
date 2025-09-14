def heapify(arr:list[int], i:int) -> None:
    left = 2*i+1
    right = left+1
    best = i
    if left<len(arr) and arr[left] < arr[best]:
        best = left
    if right<len(arr) and arr[right] < arr[best]:
        best = right
    if best!=i:
        arr[i],arr[best] = arr[best],arr[i]
        heapify(arr, best)

def heapreplace(heap: list[int], val: int) -> int:
    result = heap[0]
    heap[0] = val
    heapify(heap, 0)
    return result

if __name__ == "__main__":
    heap = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(heapreplace(heap, -1)) # 0
    print(heap) # [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(heapreplace(heap, 0)) # -1
    print(heap) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(heapreplace(heap, 1)) # 0
    print(heap) # [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(heapreplace(heap, 10))
    print(heap) # [1, 3, 2, 7, 4, 5, 6, 10, 8, 9]
    print(heapreplace(heap, 5))
    print(heap) # [2, 3, 5, 7, 4, 9, 6, 10, 8, 5]