from typing import List

def heapify(A: List[int], i:int):
    heapsize = len(A)
    l,r = 2*i+1, 2*i+2
    best = i
    if l<heapsize and A[l]>A[best]:
        best = l
    if r<heapsize and A[r]>A[best]:
        best = r
    if best!=i:
        A[i],A[best] = A[best],A[i]
        heapify(A, best)

def build_heap(data: List[int]) -> List[int]:
    heap = data.copy()
    n =(len(data) + 1)//2
    for i in range(n-1, -1, -1):
        heapify(heap, i)
    return heap

if __name__=="__main__":
    data = [4,10,3,5,1]
    heap = build_heap(data)
    print(heap) # [10, 5, 3, 4, 1]
