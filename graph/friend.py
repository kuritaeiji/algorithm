import sys
import io
from collections import deque

INPUT = """\
10 9
0 1
0 2
3 4
5 7
5 6
6 7
6 8
7 8
8 9
3
0 1
5 9
1 3
"""

sys.stdin = io.StringIO(INPUT)

n, m = [int(v) for v in input().split()]
G = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = [int(v) for v in input().split()]
    G[v1].append(v2)
    G[v2].append(v1)

def dfs(vertex, visited = None):
    if visited == None:
        visited = [False] * n

    visited[vertex] = True

    for v in G[vertex]:
        if visited[v] == False:
            visited = dfs(v, visited)

    return visited

def bfs(vertex):
    visited = [False] * n
    queue = deque([vertex])
    visited[vertex] = True

    while queue:
        v = queue.popleft()
        for v1 in G[v]:
            if visited[v1] == False:
                visited[v1] = True
                queue.append(v1)

    return visited

q = int(input())
for _ in range(q):
    v1, v2 = [int(v) for v in input().split()]
    if bfs(v1)[v2]:
        print("yes")
    else:
        print("no")