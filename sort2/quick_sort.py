import sys
import io

INPUT = """\
10
8 5 9 2 6 3 7 1 10 4
"""

sys.stdin = io.StringIO(INPUT)

n = int(input())
A = list(map(int, input().split()))

def quick_sort(array: list[int]):
    if len(array) <= 1:
        return array

    target = array.pop()

    left = [value for value in array if value <= target]
    right = [value for value in array if value > target]

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [target] + right


# print(quick_sort(A))
assert quick_sort(A) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]