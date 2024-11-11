"""

"""
from typing import Optional

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def hasCycle(head: Optional[Node]) -> bool:
    if head is None:
        return False
    visited = {head}
    while head.next:
        head = head.next
        if head in visited:
            return True
        else:
            visited.add(head)
    return False
