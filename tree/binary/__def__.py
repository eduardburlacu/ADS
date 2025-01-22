class Node:
    def __init__(self, data: int|float|str|None = None, left: Node|None = None, right: Node|None = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root: Node|None = None):
        self.root = root
        self.nodes = [root] if root else []

    def add(
            self,
            node:int|float,
            parent: Node|None = None,
            is_left:bool|None = None
    )->None:

        if parent is None:
            # Asked to change the root
            if self.root: # Check if the tree already has a root
                assert is_left is None, "Cannot change the root and specify the direction"
                left = self.root.left
                right = self.root.right
                node_obj = Node(node, left, right)
                self.root = node_obj
            else:
                node_obj = Node(node)
                self.root = node_obj

        elif is_left:
            left = parent.left
            node_obj = Node(node, left.left, left.right)
            parent.left = node_obj
            self.nodes.remove(left)

        else:
            right = parent.right
            node_obj = Node(node, right.left, right.right)
            parent.right = node_obj
            self.nodes.remove(right)

        self.nodes.append(node_obj)
        return

    def populate(self, values:list[int|float|None])->None:
        if len(values) == 0:
            return

        if not self.root:
            self.add(values.pop(0))
        low = len(self.nodes)
        high = len(self.nodes) + len(values)
        direction = lambda i: (i + low) % 2 == 1
        """
        Maps the position in the list to a direction
        :return: 
            True if the node is left
            False if the node is right
        """
        positions = map(
            direction, range(low, high)
        )
        """
        Maps each node with its parent relative location(left or right)
        """
        for idx, (pos ,value) in enumerate(zip(positions, values)):
            self.add(value, self.nodes[idx], pos)

        return

    def traverse(self):
        pass

    def _sum(self, curr:Node|None)->int|float:
        if curr is None:
            return 0
        return curr.data + self.sum(curr.left) + self.sum(curr.right)

    def sum(self)->int|float:
        return self._sum(self.root)

    def __repr__(self):
        return f"BinaryTree({self.root})"

if __name__=="__main__":
    root = Node(0)
    values = [root, Node(1)]
    for i in range(1, 10):
        values.append(Node(i))
    tree = BinaryTree()