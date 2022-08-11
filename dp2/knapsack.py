import sys
import io

INPUT = """\
4 5
4 2
5 2
2 1
8 3
"""

sys.stdin = io.StringIO(INPUT)

n, w = [int(v) for v in input().split()]
items = []
class Item:
    def __init__(self, v, w):
        self.v = v
        self.w = w

for _ in range(n):
    items.append(Item(*[int(v) for v in input().split()]))

dp = [[0] for i in range(n + 1)]
for _ in range(w):
    dp[0].append(0)

items.insert(0, 0)

for i in range(1, n + 1):
    item = items[i]
    for j in range(1, w + 1):
        if j < item.w:
            dp[i].append(dp[i - 1][j])
        else:
            dp[i].append(max(dp[i - 1][j - item.w] + item.v, dp[i - 1][j]))

print(dp[-1][-1])