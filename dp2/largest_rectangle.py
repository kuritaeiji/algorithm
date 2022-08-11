import sys
import io

INPUT = """\
4 5
0 0 1 0 0
1 0 0 0 0
0 0 0 1 0
0 0 0 1 0
"""

sys.stdin = io.StringIO(INPUT)

from collections import deque

H, W = [int(v) for v in input().split()]
F = []
for _ in range(H):
    F.append([int(v) for v in input().split()])

dp = [[0] * W for _ in range(H)]
dp[0] = F[0]

for i in range(1, H):
    for j in range(W):
        if F[i][j] == 1:
            continue

        dp[i][j] = dp[i - 1][j] + 1

max_area = 0

class Item:
    def __init__(self, index, height):
        self.height = height
        self.index = index

for i in range(H):
    stack = deque([])
    stack.append(Item(0, dp[i][0]))
    dp[i].append(0)

    for j in range(1, W + 1):
        h = dp[i][j]
        last = stack[-1]
        if h > last.height:
            stack.append(Item(j, dp[i][j]))
            continue

        if h < last.height:
            while last.height > h:
                item = stack.pop()
                width = j - item.index
                max_area = max(max_area, width * item.height)
                if not stack:
                    break
                last = stack[-1]
            stack.append(Item(j, dp[i][j]))
print(max_area)