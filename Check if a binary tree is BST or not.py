class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def IsBST(root, L=None, R=None):
    if root is None:
        return True

    if L is not None and root.data <= L.data:
        return False

    if R is not None and root.data >= R.data:
        return False

    return IsBST(root.left, L, root) and IsBST(root.right, root, R)


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    # root.left.right.right = Node(6)

    if IsBST(root, None, None):
        print("The Binary Tree is a Binary Search Tree")
    else:
        print("The Binary Tree is NOT a Binary Search Tree")

