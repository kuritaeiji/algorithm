import sys
import io

INPUT = """\
6
30 35
35 15
15 5
5 10
10 20
20 25
"""

sys.stdin = io.StringIO(INPUT)

N = int(input())

for i in range(N):
    if i == 0:
        P = [int(v) for v in input().split()]
        continue

    P.append(int(input().split()[1]))

INF = 2 ** 32 - 1
dp = [[INF] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

for l in range(1, N): # lはiから幾つ離れているかを表す。
    for i in range(N):
        j = i + l
        if j >= N:
            continue

        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + P[i] * P[k + 1] * P[j + 1])

print(dp[0][-1])