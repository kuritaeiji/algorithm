import sys
import io

INPUT = """\
5
5
1
3
2
4
"""

sys.stdin = io.StringIO(INPUT)

import bisect

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

dp = [nums[0]]

for i in range(1, n):
    num = nums[i]
    if num > dp[-1]:
        dp.append(num)
    else:
        index = bisect.bisect_right(dp, num)
        dp[index] = num

print(len(dp))

# n = int(input())
# nums = [0]

# for _ in range(n):
#     nums.append(int(input()))

# length = [0]

# for i in range(1, n + 1):
#     num = nums[i]
#     max_length = 0

#     for j in reversed(range(i)):
#         if nums[j] < num:
#             max_length = max(length[j], max_length)

#     length.append(max_length + 1)

# print(max(length))