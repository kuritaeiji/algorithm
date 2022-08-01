import sys
import io
from collections import deque

INPUT = """\
4
1 2 2 4
2 1 4
3 0
4 1 3
"""

sys.stdin = io.StringIO(INPUT)

n = int(input())
G = [None] * n
for _ in range(n):
    u, _, *V = [int(value) for value in input().split()]
    G[u-1] = [v - 1 for v in V]

queue = deque([])
distance = [None] * n
queue.append(0)
distance[0] = 0

while queue:
    u = queue.popleft()
    for v in G[u]:
        if distance[v] == None:
            distance[v] = distance[u] + 1
            queue.append(v)

for v in range(n):
    print(v + 1, distance[v])