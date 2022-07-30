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

def all_search(array: list[int], target: int, n: int, depth: int = 0, sum: int = 0):
    if depth == n:
        return sum == target

    result1 = all_search(array, target, n, depth+1, sum)
    result2 = all_search(array, target, n, depth+1, sum+array[depth])
    if result1 or result2:
        return True
    else:
        return False

for m in M:
    if all_search(A, m, n):
        print("yes")
    else:
        print("no")