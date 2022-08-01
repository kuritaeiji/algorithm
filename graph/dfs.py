import sys
import io
from collections import deque

INPUT = """\
6
1 2 2 3
2 2 3 4
3 1 5
4 1 6
5 1 6
6 0
"""

sys.stdin = io.StringIO(INPUT)

n = int(input())
G = [None] * n
for _ in range(n):
    u, _, *V = [int(value) for value in input().split()]
    G[u-1] = [v-1 for v in V]

visited, finished = [None] * n, [None] * n
time = 0

def visit(u):
    global time
    time += 1
    visited[u] = time
    for v in G[u]:
        if visited[v] == None:
            visit(v)
    time += 1
    finished[u] = time

visit(0)
for u in range(n):
    print(u + 1, visited[u], finished[u])