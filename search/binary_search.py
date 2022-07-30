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

def binary_search(array: list[int], n: int, target: int):
    left = 0
    right = n

    while right > left:
        middle = (right + left) // 2
        if target == array[middle]:
            return True
        elif target > array[middle]:
            left = middle + 1
        else:
            right = middle

    return False

count = 0
for t_value in T:
    if binary_search(S, n, t_value):
        count += 1

assert count == 3