import sys
import io

INPUT = """\
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1
"""

sys.stdin = io.StringIO(INPUT)

class Node:
    def __init__(self, id, parent = -1, left = -1, right = -1):
        self.id = id
        self.parent = parent
        self.left = left
        self.right = right

    def preorder(self):
        print(self.id)
        if self.left != -1:
            trees[self.left].preorder()
        if self.right != -1:
            trees[self.right].preorder()

    def inorder(self):
        if self.left != -1:
            trees[self.left].inorder()
        print(self.id)
        if self.right != -1:
            trees[self.right].inorder()

    def postorder(self):
        if self.left != -1:
            trees[self.left].postorder()
        if self.right != -1:
            trees[self.right].postorder()
        print(self.id)


n = int(input())
trees = {i: Node(i) for i in range(n)}
for _ in range(n):
    id, left, right = [int(value) for value in input().split()]
    trees[id].left = left
    trees[id].right = right
    if left != -1:
        trees[left].parent = id
    if right != -1:
        trees[right].parent = id

trees[0].preorder()
trees[0].inorder()
trees[0].postorder()