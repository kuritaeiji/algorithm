import sys
import io

INPUT = """\
5
0 3 2 3 3 1 1 2
1 2 0 2 3 4
2 3 0 3 3 1 4 1
3 4 2 1 0 1 1 4 4 3
4 2 2 1 3 3
"""

sys.stdin = io.StringIO(INPUT)

MAXIMUM = 200000

n = int(input())
matrices = [[MAXIMUM] * n for _ in range(n)]
for _ in range(n):
    tmp = [int(v) for v in input().split()]
    if tmp[1] != 0:
        node = tmp[0]
        index = None
        for i, v in enumerate(tmp[2:]):
            if i % 2 == 0:
                index = v
            else:
                matrices[node][index] = v

state = [False] * n
weight = [MAXIMUM] * n
weight[0] = 0

while True:
    v = None
    min_cost = MAXIMUM
    for i in range(n):
        if state[i] == False and weight[i] < min_cost:
            v = i
            min_cost = weight[i]

    if v == None:
        break

    state[v] = True

    for i in range(n):
        if state[i] == False and matrices[v][i] != MAXIMUM:
            if weight[v] + matrices[v][i] < weight[i]:
                weight[i] = weight[v] + matrices[v][i]

for i, w in enumerate(weight):
    print(i, w)