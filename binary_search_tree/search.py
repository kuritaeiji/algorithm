import sys
import io

INPUT = """\
10
insert 30
insert 88
insert 12
insert 1
insert 20
find 12
insert 17
insert 25
find 16
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
    def __init__(self, root = None):
        self.root = root

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
            return

        x_parent = None
        x = self.root
        while x != None:
            x_parent = x
            if key < x.key:
                x = x.left
            else:
                x = x.right

        if key < x_parent.key:
            x_parent.left = Node(key=key, parent=x_parent)
        else:
            x_parent.right = Node(key=key, parent=x_parent)

    def find(self, key):
        x = self.root
        while x != None:
            if key == x.key:
                return x

            if key < x.key:
                x = x.left
            else:
                x = x.right

    def preorder(self, node, text = ""):
        if node == None:
            return text

        text += f"{node.key} "
        text = self.preorder(node.left, text)
        text = self.preorder(node.right, text)

        return text

    def inorder(self, node, text = ""):
        if node == None:
            return text

        text = self.inorder(node.left, text)
        text += f"{node.key} "
        text = self.inorder(node.right, text)

        return text

bst = BST()
n = int(input())
for i in range(n):
    instruction = input().split()
    if instruction[0] == "insert":
        bst.insert(int(instruction[1]))
    elif instruction[0] == "find":
        if bst.find(int(instruction[1])):
            print("yes")
        else:
            print("no")
    else:
        print(bst.preorder(bst.root))
        print(bst.inorder(bst.root))