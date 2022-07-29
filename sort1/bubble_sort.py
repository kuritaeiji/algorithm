import sys
import io

INPUT = """\
5
5 3 2 4 1
"""

sys.stdin = io.StringIO(INPUT)
N = int(input())
A = list(map(int, input().split()))

def bubble_sort(array, n):
    for i in range(n):
        for j in reversed(range(i, n-1)):
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]

bubble_sort(A, N)
assert A == [1, 2, 3, 4, 5]