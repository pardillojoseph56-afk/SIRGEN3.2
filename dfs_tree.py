from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(values):
    """Build a binary tree by filling each level from left to right."""
    root = Node(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        current = queue.popleft()

        current.left = Node(values[i])
        queue.append(current.left)
        i += 1

        if i < len(values):
            current.right = Node(values[i])
            queue.append(current.right)
            i += 1
    return root


def preorder(node, result):
    """Root -> Left -> Right"""
    if node:
        result.append(node.data)
        preorder(node.left, result)
        preorder(node.right, result)


def inorder(node, result):
    """Left -> Root -> Right"""
    if node:
        inorder(node.left, result)
        result.append(node.data)
        inorder(node.right, result)


def postorder(node, result):
    """Left -> Right -> Root"""
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.data)


def main():
    name = "JOSEPHPARDILLO"
    root = build_tree(list(name))

    print(f"Binary tree built from: {name}\n")

    traversals = [
        ("PreOrder", preorder),
        ("InOrder", inorder),
        ("PostOrder", postorder),
    ]

    for title, func in traversals:
        result = []
        func(root, result)
        print(f"{title} DFS: {' -> '.join(result)}")


if __name__ == "__main__":
    main()