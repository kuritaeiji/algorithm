import sys
import io
from collections import deque

INPUT = """\
1 2 + 3 4 - *
"""

sys.stdin = io.StringIO(INPUT)

porland = input()

def calc_porland(porland: str):
    stack = deque([])
    for value in porland.split():
        if value.isdigit():
            stack.append(int(value))
        else:
            value2 = stack.pop()
            value1 = stack.pop()
            result = eval(f"{value1} {value} {value2}")
            stack.append(result)

    return stack.pop()

assert calc_porland(porland) == -3