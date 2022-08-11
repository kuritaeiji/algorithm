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

h, w = [int(v) for v in input().split()]
matrices = []

for _ in range(h):
    matrices.append([int(v) for v in input().split()])

dp = [[0] for _ in range(h + 1)]
for j in range(w):
    dp[0].append(0)

max_square = 0

for i in range(h):
    for j in range(w):
        if matrices[i][j] == 1:
            dp[i + 1].append(0)
        else:
            dp[i + 1].append(min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1)
            max_square = max(dp[i + 1][j + 1], max_square)

print(max_square ** 2)