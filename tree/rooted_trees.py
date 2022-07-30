import sys
import io

INPUT = """\
13
0 3 1 4 10
1 2 2 3
2 0
3 0
4 3 5 6 7
5 0
6 0
7 2 8 9
8 0
9 0
10 2 11 12
11 0
12 0
"""

sys.stdin = io.StringIO(INPUT)

class Node:
    def __init__(self, id, parent = -1, children = None):
        if children is None:
            children = []

        self.id = id
        self.parent = parent
        self.children = children

    def depth(self):
        if self.parent == -1:
            return 0

        return nodes[self.parent].depth() + 1

    def state(self):
        if self.parent == -1:
            return "root"
        elif self.children == []:
            return "leaf"
        else:
            return "internal node"

n = int(input())
nodes = []
for i in range(n):
    nodes.append(Node(i))

for i in range(n):
    nums = [int(value) for value in input().split()]
    nodes[i].children = nums[2:]
    for j in nums[2:]:
        nodes[j].parent = i

for node in nodes:
    print(f"node: {node.id}: parent = {node.parent}: depth = {node.depth()}: {node.state()}, {node.children}")

def get_depth(id):
    depth = 0
    while nodes[id].parent == -1:
        depth += 1
        id = nodes[id].parent

    return depth