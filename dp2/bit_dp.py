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

# bitdpは順列から最適なものを求めるのに使われる

V, E = [int(v) for v in input().split()]
MAXIMUM = 10 ** 4
G = [[MAXIMUM] * V for _ in range(V)]
for _ in range(E):
    s, t, d = [int(v) for v in input().split()]
    G[s][t] = d

# dpは0->Sへの最小コストを表す
dp = [[MAXIMUM] * V for _ in range(2 ** V)]
for i in range(V):
    dp[1 << i][i] = G[0][i]

for S in range(2 ** V): # Sは集合をbitで表している
    for v in range(V): # dp[S][v]のvを表す。vは末項。vは集合Sに含まれる要素。
        for u in range(V): # 集合{S-{v}}の中の項を表す。cost(u, v)を求めるために必要
            if (S >> u) & 1 == 0: # uがSに含まれていない場合はスキップ
                continue

            if (S >> v) & 1 == 0: # vが集合Sに含まれていない場合
                if dp[S][u] + G[u][v] < dp[S | (1 << v)][v]: # vの含まれていないS dp[S][u]+G[u][v]がdp[S + {v}][v]より小さい場合
                    dp[S | (1 << v)][v] = dp[S][u] + G[u][v]

if dp[2 ** V - 1][0] != MAXIMUM:
    print(dp[2 ** V - 1][0])
else:
    print(-1)

# 今回は0から始まり全ての都市を通過して0に戻る問題なのでdp[2][1] = G[0][1]になる。2は2進数で10
# 全ての都市を通過するだけで戻らない問題の場合はdp[2][1] = 0になる。