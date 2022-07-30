import sys
import io

INPUT = """\
10
8 5 9 2 6 3 7 1 10 4
"""

sys.stdin = io.StringIO(INPUT)
n = int(input())
A = list(map(int, input().split()))
MAXIMUM = 1000000

def merge_sort(array: list[int], n: int, left: int = 0, right: int | None = None):
    if right is None:
        right = len(array)

    if right <= left + 1:
        return

    middle = (left + right) // 2
    merge_sort(array, n, left, middle)
    merge_sort(array, n, middle, right)

    left_array = array[left:middle]
    left_array.append(MAXIMUM)
    right_array = array[middle:right]
    right_array.append(MAXIMUM)

    left_index = 0
    right_index = 0
    for i in range(left, right):
        if left_array[left_index] <= right_array[right_index]:
            array[i] = left_array[left_index]
            left_index += 1
        else:
            array[i] = right_array[right_index]
            right_index += 1

merge_sort(A, n)
assert A == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]