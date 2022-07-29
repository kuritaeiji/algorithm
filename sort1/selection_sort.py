import sys
import io

INPUT = """\
6
5 2 4 6 1 3
"""

sys.stdin = io.StringIO(INPUT)

N = int(input())
A = list(map(int, input().split()))

def selection_sort(array, n):
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

selection_sort(A, N)
assert A == [1, 2, 3, 4, 5, 6]