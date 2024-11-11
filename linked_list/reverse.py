from typing import Optional
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def my_reverse(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return head
    elif not head.next:
        return head
    curr, prev = head.next, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    head.next = None
    return prev
"This is good but I was dodgy with the starting condition. Should have started with prev, curr = None, head"

def reverse(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return head
    elif head.next is None:
        return head
    curr, prev = head, None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print(f"{head.val}->{head.next.val}->{head.next.next.val}->{head.next.next.next.val}->{head.next.next.next.next.val}")
    head = reverse(head)
    print(f"{head.val}->{head.next.val}->{head.next.next.val}->{head.next.next.next.val}->{head.next.next.next.next.val}")
    """
    1->2->3->4->5
    5->4->3->2->1
    """