import sys
import io

INPUT = """\
5
1 2 3 4 5
3
3 4 1
"""

sys.stdin = io.StringIO(INPUT)

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

count = 0
for t_value in T:
    for s_value in S:
        if t_value == s_value:
            count += 1

assert count == 3