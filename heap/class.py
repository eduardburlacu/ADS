from typing import Dict, List, Set, Tuple, Optional

class Heap:
    def __init__(self, heap:list|None=None):
        self.heap = heap if heap else []
        self.length = len(self.heap)
        self.heap_size = self.length

    def parent(self, i:int)->int:
        return self.heap[(i-1)//2]

    def left_child(self, i:int)->int|None:
        idx = 2*i+1
        if idx<self.heap_size:
            return self.heap[idx]

    def right_child(self, i:int)->int|None:
        idx = 2*i+2
        if idx<self.heap_size:
            return self.heap[idx]
