import sys
import io

INPUT = """\
4 6
0 1 2
1 2 3
1 3 9
2 0 1
2 3 6
3 2 4
"""

sys.stdin = io.StringIO(INPUT)

V, E = [int(v) for v in input().split()]
MAXIMUM = 10 ** 5
G = [[MAXIMUM] * V for _ in range(V)]
for _ in range(E):
    s, t, d = [int(v) for v in input().split()]
    G[s][t] = d

dp = [[MAXIMUM] * V for _ in range(2 ** V)]
for i in range(1, V):
    dp[1 << i][i] = G[0][i]

for S in range(2 ** V):
    for v in range(V):
        for u in range(V):
            if (S >> u) & 1 == 0:
                continue

            if (S >> v) & 1 == 0:
                if dp[S][u] + G[u][v] < dp[S | 1 << v][v]:
                    dp[S | 1 << v][v] = dp[S][u] + G[u][v]

if dp[2 ** V - 1][0] < MAXIMUM:
    print(dp[2 ** V - 1][0])
else:
    print(-1)