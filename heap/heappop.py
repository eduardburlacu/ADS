# Remove the root of the heap and return it. Returns the minimum element from the heap.

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

def heappop(heap: list[int]) -> int:
    heap[0], heap[-1]= heap[-1], heap[0]
    result = heap.pop()
    heapify(heap, 0)
    return result

if __name__ == "__main__":
    heap = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(heappop(heap)) # 0
    print(heap) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(heappop(heap)) # 1
    print(heap) # [2, 4, 3, 8, 5, 6, 7, 9]
    print(heappop(heap)) # 2
    print(heap) # [3, 4, 6, 8, 5, 9, 7]
    print(heappop(heap)) # 3
    print(heap) # [4, 5, 6, 8, 7, 9]
    print(heappop(heap)) # 4
    print(heap) # [5, 7, 6, 8, 9]
    print(heappop(heap)) # 5
    print(heap) # [6, 7, 9, 8]
    print(heappop(heap)) # 6 
    print(heap) # [7, 8, 9]
    print(heappop(heap)) # 7
    print(heap) # [8, 9]
    print(heappop(heap)) # 8
    print(heap) # [9]
    print(heappop(heap)) # 9
    print(heap) # []
