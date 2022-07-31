import sys
import io

INPUT = """\
10
4 1 3 2 16 9 10 14 8 7
"""

sys.stdin = io.StringIO(INPUT)

n = int(input())
heap = [int(key) for key in input().split()]
heap.insert(0, 0)

def max_heapify(heap, index, n = n):
    # largets_indexが変化しなければloop終了

    # left_index = index * 2
    # right_index = index * 2 + 1
    # largest_index = index

    # if left_index <= n and heap[left_index] > heap[largest_index]:
    #     largest_index = left_index
    # if right_index <= n and heap[right_index] > heap[largest_index]:
    #     largest_index = right_index

    # if largest_index != index:
    #     heap[largest_index], heap[index] = heap[index], heap[largest_index]
    #     max_heapify(heap, largest_index)

    original_index = index
    largest_index = index

    while True:
        left_index = original_index * 2
        right_index = original_index * 2 + 1
        if left_index <= n and heap[left_index] > heap[largest_index]:
            largest_index = left_index
        if right_index <= n and heap[right_index] > heap[largest_index]:
            largest_index = right_index

        if largest_index == original_index:
            break

        heap[original_index], heap[largest_index] = heap[largest_index], heap[original_index]
        original_index = largest_index



for i in reversed(range(1, n)):
    max_heapify(heap, i)

print(heap)
assert heap == [0, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1]