import sys
import io
import copy
import operator

INPUT = """\
6 5 4 3 2 1
6 
6 
2 
1 
3 
4 
3 
"""

sys.stdin = io.StringIO(INPUT)

sys.setrecursionlimit(100000000)

class Dice:
    def __init__(self, array):
        self.array = array

    def roll_right(self, array, target, count = 0):
        count += 1
        if count == 10:
            return (count, False)

        copy_array = copy.copy(array)
        copy_array[4] = array[2]
        copy_array[2] = array[5]
        copy_array[5] = array[3]
        copy_array[3] = array[4]

        if copy_array[3] == target:
            return (count, copy_array)
        else:
            result = []
            result.append(self.roll_right(copy_array, target, count))
            result.append(self.roll_forward(copy_array, target, count))
            result.append(self.roll_rewind(copy_array, target, count))

            # 全てfalseの場合
            if all([not r[1] for r in result]):
                return (0, False)
            else:
                result = [r for r in result if r[1]]
                result = min(result, key=operator.itemgetter(0))
                return result

    def roll_left(self, array, target, count = 0):
        count += 1
        if count == 10:
            return (count, False)

        copy_array = copy.copy(array)
        copy_array[4] = array[3]
        copy_array[2] = array[4]
        copy_array[5] = array[2]
        copy_array[3] = array[5]

        if copy_array[3] == target:
            return (count, copy_array)
        else:
            result = []
            result.append(self.roll_left(copy_array, target, count))
            result.append(self.roll_forward(copy_array, target, count))
            result.append(self.roll_rewind(copy_array, target, count))

            # 全てfalseの場合
            if all([not r[1] for r in result]):
                return (0, False)
            else:    
                result = [r for r in result if r[1]]
                result = min(result, key=operator.itemgetter(0))
                return result

    def roll_forward(self, array, target, count = 0):
        count += 1
        if count == 10:
            return (count, False)

        copy_array = copy.copy(array)

        copy_array[3] = array[1]
        copy_array[0] = array[3]
        copy_array[2] = array[0]
        copy_array[1] = array[2]

        if copy_array[3] == target:
            return (count, copy_array)
        else:
            result = []
            result.append(self.roll_right(copy_array, target, count))
            result.append(self.roll_left(copy_array, target, count))
            result.append(self.roll_forward(copy_array, target, count))

            # 全てfalseの場合
            if all([not r[1] for r in result]):
                return (0, False)
            else:    
                result = [r for r in result if r[1]]
                result = min(result, key=operator.itemgetter(0))
                return result

    def roll_rewind(self, array, target, count = 0):
        count += 1
        if count == 10:
            return (count, False)

        copy_array = copy.copy(array)

        copy_array[3] = array[0]
        copy_array[1] = array[3]
        copy_array[2] = array[1]
        copy_array[0] = array[2]

        if copy_array[3] == target:
            return (count, copy_array)
        else:
            result = []
            result.append(self.roll_right(copy_array, target, count))
            result.append(self.roll_left(copy_array, target, count))
            result.append(self.roll_rewind(copy_array, target, count))

            # 全てfalseの場合
            if all([not r[1] for r in result]):
                return (10, False)
            else:    
                result = [r for r in result if r[1]]
                result = min(result, key=operator.itemgetter(0))
                return result

dice = Dice([int(v) for v in input().split()])
n = int(input())
count = 0

for _ in range(n):
    target = int(input())
    result1 = dice.roll_left(dice.array, target)
    result2 = dice.roll_right(dice.array, target)
    result3 = dice.roll_forward(dice.array, target)
    result4 = dice.roll_rewind(dice.array, target)
    result = min(result1, result2, result3, result4, key=operator.itemgetter(0))
    count += result[0]
    dice.array = result[1]

print(count)