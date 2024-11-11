"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""
from typing import Optional

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def deleteDuplicates( head: Optional[Node]) -> Optional[Node]:
    if not head:
        return head
    curr, prev = head, head
    while curr:
        while curr.val == prev.val: #curr can be removed safely
            curr = curr.next
            prev.next = curr
            if not curr:
                return head
        curr = curr.next
        prev = prev.next
    return head
