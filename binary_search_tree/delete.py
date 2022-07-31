import sys
import io

INPUT = """\
18
insert 8
insert 2
insert 5
insert 3
insert 7
insert 22
insert 1
find 1
find 2
find 3
find 4
find 5
find 6
find 7
find 8
print
delete 5
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
        self.root = None

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
            x_parent.left = Node(key, parent=x_parent)
        else:
            x_parent.right = Node(key, parent=x_parent)

    def find(self, key):
        x = self.root
        while x != None:
            if key == x.key:
                return x

            if key < x.key:
                x = x.left
            else:
                x = x.right

        return None

    def delete(self, key):
        if key == self.root.key:
            self.root = None

        target_node = self.find(key)
        # 子を持たない場合
        if target_node.left == None and target_node.right == None:
            if target_node.parent.left == target_node:
                target_node.parent.left = None
            else:
                target_node.parent.right = None
        # 子を1つ持つ場合
        elif target_node.left == None or target_node.right == None:
            node = target_node.left or target_node.right
            node.parent = target_node.parent
            if target_node.parent.left == target_node:
                target_node.parent.left = node
            else:
                target_node.parent.right = node
        # 子を2つ持つ場合
        else:
            node = self.get_successor(target_node)
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
            # 削除するノードのkeyを置換するノードにキーに変える
            target_node.key = node.key


    def get_successor(self, node):
        # 削除対象の右部分木の中で最も左に位置するnodeを探す
        x = node.right
        while x.left != None:
            x = x.left
        return x

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

n = int(input())
tree = BST()
for i in range(n):
    instruction = input().split()
    if instruction[0] == "insert":
        tree.insert(int(instruction[1]))
    elif instruction[0] == "find":
        if tree.find(int(instruction[1])):
            print("yes")
        else:
            print("no")
    elif instruction[0] == "delete":
        tree.delete(int(instruction[1]))
    else:
        print(tree.preorder(tree.root))
        print(tree.inorder(tree.root))