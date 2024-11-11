"""
Given the head of a linked list with an odd number of nodes head,
    return the value of the node in the middle.
"""
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def middle(head):
    fast = head
    slow = head
    while fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print(
        middle(head)
    )