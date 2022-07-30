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

    @property
    def depth(self):
        if self.parent == -1:
            return 0

        return nodes[self.parent].depth + 1

    @property
    def height(self):
        if self.left == -1 and self.right == -1:
            return 0

        left_height = nodes[self.left].height + 1
        right_height = nodes[self.right].height + 1
        return max(left_height, right_height)

    @property
    def state(self):
        if self.parent == -1:
            return "root"
        elif self.left == -1 and self.right == -1:
            return "leaf"
        else:
            return "internal node"

    @property
    def sibling(self):
        if self.parent == -1:
            return -1

        if nodes[self.parent].left == self.id:
            return nodes[self.parent].right

        return nodes[self.parent].left

    @property
    def degree(self):
        count = 0
        if self.left != -1:
            count += 1
        if self.right != -1:
            count += 1
        return count

n = int(input())
nodes = {i: Node(id=i) for i in range(n)}
for _ in range(n):
    node_id, left, right = [int(value) for value in input().split()]
    nodes[node_id].left = left
    nodes[node_id].right = right
    if left != -1:
        nodes[left].parent = node_id
    if right != -1:
        nodes[right].parent = node_id

for id, node in nodes.items():
    print(f"node {node.id}, parent = {node.parent}, sibling = {node.sibling}, degree = {node.degree}, depth = {node.depth}, height = {node.height}, {node.state}")