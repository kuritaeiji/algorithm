import sys
import io

INPUT = """\
15 6
1 2 7 8 12 50
"""

sys.stdin = io.StringIO(INPUT)

n, m = [int(v) for v in input().split()]
coins = [int(v) for v in input().split()]
ns = [j for j in range(n + 1)]
coins.insert(0, 0)

MAXIMUM = 10 ** 6

dp = [[0] for i in range(m + 1)]
for j in range(n):
    dp[0].append(MAXIMUM)

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if j < coins[i]:
            dp[i].append(dp[i-1][j])
        else:
            dp[i].append(min(dp[i-1][j], dp[i][j-coins[i]] + 1))

print(dp[m][n])