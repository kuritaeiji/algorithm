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

def eratosthenes(max):
    prime_nums = [True] * (max + 1)
    prime_nums[0], prime_nums[1] = (False, False)

    for i in range(2, int(sqrt(max)) + 1):
        if prime_nums[i]:
            for j in range(2 * i, max + 1, i):
                prime_nums[j] = False

    return prime_nums

is_prime = eratosthenes(10)
n = int(input())

count = 0
for _ in range(n):
    if is_prime[int(input())]:
        count += 1

print(count)