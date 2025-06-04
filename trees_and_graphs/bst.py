from trees_and_graphs.node import Node


def dfs(root: Node, val: int) -> Node:
    pass


def bfs(root: Node, val: int) -> Node:
    pass

def walk(root: Node) -> None:
    if root is not None:
        print(root.value)
        walk(root.right)
        walk(root.left)
    else:
        return

def main():
    n1 = Node(5)

    n1.add_node(7)
    n1.add_node(11)
    n1.add_node(8)
    n1.add_node(3)
    walk(n1)


if __name__ == '__main__':
    main()