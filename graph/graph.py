import sys
import io

INPUT = """\
4
1 2 2 4
2 1 4
3 0
4 1 3
"""

sys.stdin = io.StringIO(INPUT)

n = int(input())
matrices = [[0] * n for _ in range(n)]

for _ in range(n):
    array = [int(v) for v in input().split()]
    id = array[0]
    for key in array[2:]:
        matrices[id-1][key-1] = 1

assert matrices == [
[0, 1, 0, 1],
[0, 0, 0, 1],
[0, 0, 0, 0],
[0, 0, 1, 0]
]