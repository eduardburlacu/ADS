from typing import Dict, List, Set, Tuple, Optional

class Heap:
    def __init__(self, data, *args, **kwargs):
        self.heap = []
        if data:
            self.data = data

    @property
    def heapsize(self):
        return len(self.heap)

    def parent(self, i: int) -> Optional[int]:
        if i == 0:
            return None
        return (i - 1) // 2

    def left(self, i: int) -> Optional[int]:
        l = 2 * i + 1
        if l >= len(self.heap):
            return None
        return l

    def right(self, i: int) -> Optional[int]:
        r = 2 * i + 1
        if r >= len(self.heap):
            return None
        return r

