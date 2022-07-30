import sys
import io

INPUT = """\
5
1 5 7 10 21
4
2 4 17 8
"""

sys.stdin = io.StringIO(INPUT)
n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

def bit_all_search(array: list[int], n: int, target: int):
    for i in range(2 ** n):
        nums = 0
        for j in range(len(array)):
            if (i >> j & 1):
                nums += array[j]
        if nums == target:
            return True

    return False

for m in M:
    if bit_all_search(A, n, m):
        print("yes")
    else:
        print("no")