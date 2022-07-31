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

class Heap:
    def __init__(self):
        self.heap = [0]

    def insert(self, key):
        self.heap.append(key)

        index = len(self.heap) - 1
        parent_index = index // 2

        while parent_index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = index // 2

    def extract_max(self):
        max_key = self.heap.pop(1)
        self.heap.insert(1, self.heap.pop())
        self.max_heapify(1)
        return max_key

    def max_heapify(self, index):
        original_index = index
        largest_index = index

        while True:
            left_index = original_index * 2
            right_index = original_index * 2 + 1

            if left_index <= len(self.heap) - 1 and heap[left_index] > heap[largest_index]:
                largest_index = left_index
            if right_index <= len(self.heap) - 1 and heap[right_index] > heap[largest_index]:
                largest_index = right_index

            if largest_index == original_index:
                return

            self.heap[largest_index], self.heap[original_index] = self.heap[original_index], self.heap[largest_index]
            original_index = largest_index

heap = Heap()
while True:
    instruction = input().split()
    if instruction[0] == "end":
        break

    if instruction[0] == "insert":
        heap.insert(int(instruction[1]))
    else:
        print(heap.extract_max())