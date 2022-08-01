import sys
import io
import operator

# INPUT = """\
# 0 0 
# 1 
# 3 
# 0 2 4
# 1 1 5
# 1 2 6
# """

# sys.stdin = io.StringIO(INPUT)

class Place:
    def __init__(self, x, y, price = 0):
        self.x = x
        self.y = y
        self.price = price

    def distance(self, place):
        return (self.x - place.x) ** 2 + (self.y - place.y) ** 2

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}, price: {self.price}円"

target_place = Place(*[int(v) for v in input().split()])
k = int(input())
n = int(input())

places = []
for _ in range(n):
    places.append(Place(*[int(v) for v in input().split()]))

near_places = sorted(places, key=operator.methodcaller("distance", target_place))[:k]
price = round(sum([place.price for place in near_places]) / k)

print(f"{price}\n")