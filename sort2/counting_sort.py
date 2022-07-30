import sys
import io

from itertools import accumulate

INPUT = """\
7
2 5 1 3 2 3 0
"""

sys.stdin = io.StringIO(INPUT)

n = int(input())
A = [int(value) for value in input().split()]

def counting_sort(array: list[int]):
    max_num = max(array)
    counting_array = [0] * (max_num + 1)

    for value in array:
        counting_array[value] += 1

    counting_array = [*accumulate(counting_array)]

    sorted_array = [0] * len(array)
    for value in array:
        counting_array[value] -= 1
        sorted_array[counting_array[value]] = value

    return sorted_array

assert counting_sort(A) == [0, 1, 2, 2, 3, 3, 5]