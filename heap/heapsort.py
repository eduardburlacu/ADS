from typing import List

def heapify(heap: List[int], i: int, last=None) -> None:
    N = len(heap) if last is None else last+1
    left = 2*i+1; right = left+1
    best = i
    if left<N and heap[left]>heap[best]:
        best = left
    if right<N and heap[right]>heap[best]:
        best = right
    if best!=i:
        heap[best], heap[i] = heap[i], heap[best]
        heapify(heap, i=best, last=last)

def build_max_heap(data: List[int]) -> List[int]:
    heap = data.copy()
    half = (len(data)+1)//2
    for i in range(half, -1, -1):
        heapify(heap, i)
    return heap

def heapsort(arr:List[int]):
    last = len(arr)-1
    if last<1: # empty or 1 element
        return arr

    heap = build_max_heap(arr)
    while last>0:
        heap[0], heap[last] = heap[last], heap[0]
        last -= 1
        heapify(heap,i=0,last=last)
    return heap

if __name__=="__main__":

    arr = [4,10,3,5,1,15]
    print(f"arr: {arr}")
    print(heapsort(arr)) # [1, 3, 4, 5, 10, 15]

    arr = [4,10,3,5,1,15,2]
    print(f"arr: {arr}")
    print(heapsort(arr)) # [1, 2, 3, 4, 5, 10, 15]
