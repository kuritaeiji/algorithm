import sys
import io

INPUT = """\
insert 8
insert 2
extract
insert 10
extract
insert 11
extract
extract
end
"""

sys.stdin = io.StringIO(INPUT)

import heapq
heap = []

while True:
    texts = input().split()
    if texts[0] == "end":
        break

    if texts[0] == "insert":
        heapq.heappush(heap, -int(texts[1]))
    else:
        print(-heapq.heappop(heap))