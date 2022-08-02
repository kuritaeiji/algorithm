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

from heapq import heapify, heappop, heappush

# 未訪問でコストがつけられているノードのコストとノード番号を格納する
class PriorityQueue:
    def __init__(self, heap):
        self.heap = heap
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)

    def __len__(self):
        return len(self.heap)

n = int(input())
lists = [[] for _ in range(n)] # (cost, node)のtuple
for _ in range(n):
    tmp = [int(v) for v in input().split()]
    node = tmp[0]
    for i in range(2, tmp[1] * 2 + 2, 2):
        lists[node].append((tmp[i + 1], tmp[i]))

MAXIMUM = 200000
weights = [MAXIMUM] * n
weights[0] = 0
visited = [False] * n
pq = PriorityQueue([(0, 0)])

while pq:
    min_cost, u = pq.pop()
    visited[u] = True

    if weights[u] < min_cost:
        continue

    for cost, node in lists[u]:
        if visited[node] == False and weights[u] + cost < weights[node]:
            weights[node] = weights[u] + cost
            pq.push((weights[node], node))

for i, w in enumerate(weights):
    print(i, w)