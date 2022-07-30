import sys
import io

INPUT = """\
12
13 19 9 5 12 8 7 4 21 2 6 11
"""

sys.stdin = io.StringIO(INPUT)

n = int(input())
A = list(map(int, input().split()))

def partition(array: list[int], n: int):
    target = array[-1]
    i = -1
    for j in range(n-1):
        if array[j] <= target:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[-1] = array[-1], array[i+1]
    return i + 1

index = partition(A, n)
string = ""
for i, value in enumerate(A):
    if i == index:
        string += f"[{value}] "
    else:
        string += f"{value} "

result = string.strip()

assert result == "9 5 8 7 4 2 6 [11] 21 13 19 12"