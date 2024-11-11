from typing import Optional
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def middleNode(self, head: Optional[Node]) -> Optional[Node]:
    slow = head
    while head and head.next:
        head, slow = head.next.next, slow.next
    return slow

