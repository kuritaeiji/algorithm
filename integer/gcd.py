import sys
import io

INPUT = """\
147 105
"""

sys.stdin = io.StringIO(INPUT)

def gcd1(x, y):
    n = min(x, y)
    for i in reversed(range(1, n + 1)):
        if x % i == 0 and y % i == 0:
            return i

def gcd(x, y):
    bigger_num = max(x, y)
    smaller_num = min(x, y)

    while bigger_num % smaller_num != 0:
        mod = bigger_num % smaller_num
        bigger_num = smaller_num
        smaller_num = mod

    return smaller_num

x, y = [int(v) for v in input().split()]
print(gcd(x, y))