import sys
import io

INPUT = """\
5
-1 2 3 1 -1
2 -1 -1 4 -1
3 -1 -1 -1 1 1
1 4 1 -1 3
-1 -1 1 3 -1
"""

sys.stdin = io.StringIO(INPUT)

MAXIMUM = 10000

n = int(input())
matrices = []
for _ in range(n):
    weights = [int(w) for w in input().split()]
    matrices.append([MAXIMUM if w == -1 else w for w in weights])

state = [False] * n
weight = [MAXIMUM] * n
parent = [-1] * n

weight[0] = 0

while True:
    u = None
    min_cost = MAXIMUM
    for i in range(n):
        if state[i] == False and weight[i] < min_cost:
            min_cost = weight[i]
            u = i

    if u == None:
        print(sum(weight))
        break

    state[u] = True

    for v in range(n):
        if state[v] == False and matrices[u][v] != MAXIMUM:
            if matrices[u][v] < weight[v]:
                weight[v] = matrices[u][v]
                parent[v] = u