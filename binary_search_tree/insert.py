import sys
import io

INPUT = """\
8
insert 30
insert 88
insert 12
insert 1
insert 20
insert 17
insert 25
print
"""

sys.stdin = io.StringIO(INPUT)

class Node:
    def __init__(self, key, parent = None, left = None, right = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        x = self.root
        while True:
            if key < x.key:
                if x.left is None:
                    x.left = Node(key, x)
                    return
                else:
                    x = x.left
            else:
                if x.right is None:
                    x.right = Node(key, x)
                    return
                else:
                    x = x.right

    def preorder(self, node, text = ""):
        if node is None:
            return text

        text += f"{node.key} "
        text = self.preorder(node.left, text)
        text = self.preorder(node.right, text)

        return text

    def inorder(self, node, text = ""):
        if node is None:
            return text

        text = self.inorder(node.left, text)
        text += f"{node.key} "
        text = self.inorder(node.right, text)
        return text


n = int(input())
bst = BST()
for _ in range(n):
    text = input().split()

    if text[0] == "insert":
        key = int(text[1])
        bst.insert(key)
    else:
        print(bst.preorder(bst.root).strip())
        print(bst.inorder(bst.root).strip())