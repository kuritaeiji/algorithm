import sys
import io

from itertools import product

INPUT = """\
3
abcbdab
bdcaba
abc
abc
abc
bc
"""

sys.stdin = io.StringIO(INPUT)

def get_lcs(x, y):
    dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

n = int(input())
for i in range(n):
    print(get_lcs(input(), input()))