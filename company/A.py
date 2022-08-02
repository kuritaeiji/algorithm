# import sys
# import io

# INPUT = """\
# 10 10 9 
# 2 2 4 
# 2 2 3 
# 2 2 5 
# 2 2 2 
# 2 2 6 
# 2 2 1 
# 2 2 7 
# 2 2 0 
# 2 2 8 
# """

# sys.stdin = io.StringIO(INPUT)

f_h, f_w, n = [int(v) for v in input().split()]

class Field:
    def __init__(self, h, w):
        self.w = w
        self.h = h
        self.state = [["."] * w for _ in range(h)]

    def insert(self, block):
        start_x = block.x
        end_x = block.x + block.w - 1

        h = 0
        while h < self.h:
            flag = False
            for i, state in enumerate(self.state[h]):
                if start_x <= i <= end_x and state == "#":
                    flag = True
                    break

            if flag == True:
                break

            h += 1

        end_h = h - 1
        start_h = end_h - block.h + 1

        for i in range(start_h, end_h + 1):
            for j in range(start_x, end_x + 1):
                self.state[i][j] = "#"

    def __repr__(self):
        text = ""
        for i in range(self.h):
            for j in range(self.w):
                text += self.state[i][j]
            text += "\n"
        return text

field = Field(f_h, f_w)

class Block:
    def __init__(self, h, w, x):
        self.h = h
        self.w = w
        self.x = x

blocks = []
for _ in range(n):
    info = [int(v) for v in input().split()]
    blocks.append(Block(*info))

for block in blocks:
    field.insert(block)

print(field)