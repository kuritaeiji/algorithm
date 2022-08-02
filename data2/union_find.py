import sys
import io

INPUT = """\
5 12
0 1 4
0 2 3
1 1 2
1 3 4
1 1 4
1 3 2
0 1 3
1 2 4
1 3 0
0 0 4
1 0 2
1 3 0
"""

sys.stdin = io.StringIO(INPUT)

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n

    def root(self, node):
        if self.parent[node] < 0:
            return node

        root = self.root(self.parent[node])
        self.parent[node] = root
        return root

    def size(self, node):
        return -self.parent[self.root(node)]

    def unite(self, node1, node2):
        node1 = self.root(node1)
        node2 = self.root(node2)

        if node1 == node2:
            return False

        if self.size(node1) < self.size(node2):
            node1, node2 = node2, node1

        # くっつける時に親のサイズを更新する
        self.parent[node1] += self.parent[node2]
        self.parent[node2] = node1

        return True

    def is_in_same(self, node1, node2):
        node1 = self.root(node1)
        node2 = self.root(node2)
        return node1 == node2

n, q = [int(v) for v in input().split()]
uf = UnionFind(n)
for i in range(q):
    com, x, y = [int(v) for v in input().split()]
    if com == 0:
        uf.unite(x, y)
    else:
        if uf.is_in_same(x, y):
            print("1")
        else:
            print("0")