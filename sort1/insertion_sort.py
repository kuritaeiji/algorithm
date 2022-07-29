import sys
import io

INPUT = """\
6
5 2 4 6 1 3
"""

sys.stdin = io.StringIO(INPUT)
n = int(input())
A = list(map(int, input().split()))

def insertion_sort(array, n):
    for i in range(n):
        target = array[i]
        j = i - 1
        while j >= 0 and target < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = target

insertion_sort(A, n)
assert A == [1, 2, 3, 4, 5, 6]