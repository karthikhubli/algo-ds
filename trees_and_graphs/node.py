from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

    def add_node(self, value: int) -> None:
        """Insert a value into the subtree rooted at this node."""
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add_node(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add_node(value)
        # Duplicate values are ignored (no-op).

def test():
    print('node test')
    n1 = Node(5)

    n1.add_node(7)
    n1.add_node(11)
    n1.add_node(3)
    print(n1)

if __name__ == '__main__':
    test()