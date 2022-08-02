import sys
import io

INPUT = """\
6
2
3
4
5
6
7
"""

sys.stdin = io.StringIO(INPUT)

from math import sqrt

def is_prime(i):
    if i == 1:
        return False

    if i == 2:
        return True

    for j in range(2, i):
        if i % j == 0:
            return False

    return True

def is_prime2(x):
    if x == 1:
        return False

    if x == 2:
        return True

    if x % 2 == 0:
        return False

    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False

    return True

n = int(input())
count = 0
for _ in range(n):
    if is_prime(int(input())):
        count += 1

print(count)