import sys
import io

INPUT = """\
147 105
"""

sys.stdin = io.StringIO(INPUT)

def gcd(x, y):
    larger_num = max(x, y)
    smaller_num = min(x, y)

    while larger_num % smaller_num != 0:
        mod = larger_num % smaller_num
        larger_num = smaller_num
        smaller_num = mod

    return smaller_num

x, y = [int(v) for v in input().split()]
print(gcd(x, y))