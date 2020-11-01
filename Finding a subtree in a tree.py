class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Identical(a, b):

    if a is None and b is None:
        return True
    if a is None or b is None:
        return False

    return (a.data == b.data and
            Identical(a.left, b.left) and
            Identical(a.right, b.right)
            )


def Subtree(x, y):

    if y is None:
        return True

    if x is None:
        return False

    if Identical(x, y):
        return True

    return Subtree(x.left, y) or Subtree(x.right, y)


x = Node(7)
x.right = Node(6)
x.right.right = Node(5)
x.left = Node(4)
x.left.left = Node(2)
x.left.left.right = Node(1)
x.left.right = Node(3)

y = Node(4)
y.right = Node(3)
y.left = Node(2)
y.left.right = Node(1)

if Subtree(x, y):
    print("Tree 2 is subtree of Tree 1")
else:
    print("Tree 2 is not a subtree of Tree 1")
