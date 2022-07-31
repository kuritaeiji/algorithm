import sys
import io

INPUT = """\
5
7 8 1 2 3
"""

sys.stdin = io.StringIO(INPUT)

n = int(input())
heap = [int(key) for key in input().split()]
heap.insert(0, 0)

for index, key in enumerate(heap):
    if index == 0:
        continue

    print(f"node {index}: key = {key} ", end="")

    if index // 2 != 0:
        print(f"parent_key = {heap[index // 2]} ", end="")
    if index * 2 <= n:
        print(f"left_key = {heap[index * 2]} ", end="")
    if index * 2 + 1 <= n:
        print(f"right_key = {heap[index * 2 + 1]} ", end="")

    print()

