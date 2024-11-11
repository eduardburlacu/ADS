"""
Given the head of a linked list and an integer k,
    return the kth node from the end of the linked list.

For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, return the node with value 4, as it is the 2nd node from the end.
"""

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def last_k(
        head:Node,
        k:int
)->Node:
    prev = head
    for _ in range(k):
        head = head.next
    while head.next:
        head, prev = head.next, prev.next
    return prev
