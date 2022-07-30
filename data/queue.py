import sys
import io
from collections import deque

INPUT = """\
5 100
p1 150
p2 80
p3 200
p4 350
p5 20
"""

sys.stdin = io.StringIO(INPUT)

N, TIME = list(map(int, input().split()))

class Process:
    def __init__(self, name: str, time: int):
        self.name = name
        self.time = time

processes = deque([])

for _ in range(N):
    name, time = input().split()
    processes.append(Process(name, int(time)))

def round_robbing(processes: deque[Process], time: int, n: int):
    sum_time = 0

    while len(processes) > 0:
        process = processes.popleft()

        if process.time <= time:
            sum_time += process.time
            process.time = 0
            print(f"{process.name} {sum_time}")
        else:
            sum_time += time
            process.time -= time
            processes.append(process)

round_robbing(processes, TIME, N)